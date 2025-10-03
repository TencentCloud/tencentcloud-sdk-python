# -*- coding: utf-8 -*-
#
# Copyright 2017-2021 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import copy
import hashlib
import json
import logging
import logging.handlers
import random
import sys
import time
import uuid
import warnings
from datetime import datetime
from typing import Dict, Type, Union, List, Callable, Awaitable, Optional

import httpx

import tencentcloud
from tencentcloud.common.abstract_client import logger, urlparse, urlencode
from tencentcloud.common.abstract_model import AbstractModel
from tencentcloud.common.circuit_breaker import CircuitBreaker
from tencentcloud.common.credential import Credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.http.request_async import ApiRequest, ApiResponse, ResponsePrettyFormatter, \
    RequestPrettyFormatter
from tencentcloud.common.profile.client_profile import ClientProfile, RegionBreakerProfile
from tencentcloud.common.retry_async import NoopRetryer
from tencentcloud.common.sign import Sign

warnings.filterwarnings("ignore", module="tencentcloud", category=UserWarning)

_json_content = 'application/json'
_multipart_content = 'multipart/form-data'
_form_urlencoded_content = 'application/x-www-form-urlencoded'
_octet_stream = "application/octet-stream"

LOGGER_NAME = "tencentcloud_sdk_common"

InterceptorType = Callable[["RequestChain"], Awaitable]
ParamsType = Union[Dict, str, bytes]


class RequestChain(object):
    def __init__(self):
        self.request: Optional[ApiRequest] = None

        self._inters: List[InterceptorType] = []
        self._idx = 0

    async def proceed(self):
        interceptor = self._inters[self._idx]
        snapshot = self._new_snapshot()
        snapshot._idx += 1
        return await interceptor(snapshot)

    def add_interceptor(self, inter: InterceptorType, idx=sys.maxsize):
        self._inters.insert(idx, inter)
        return self

    def _new_snapshot(self) -> 'RequestChain':
        new_chain = RequestChain()
        new_chain.request = self.request
        new_chain._inters = self._inters
        new_chain._idx = self._idx
        return new_chain


class AbstractClient(object):
    _requestPath = '/'
    _params = {}
    _apiVersion = ''
    _endpoint = ''
    _service = ''
    _sdkVersion = 'SDK_PYTHON_%s' % tencentcloud.__version__
    _default_content_type = _form_urlencoded_content
    FMT = '%(asctime)s %(process)d %(filename)s L%(lineno)s %(levelname)s %(message)s'

    def __init__(self, credential: Credential, region: str, profile: ClientProfile = None):
        self.credential = credential
        self.region = region
        self.profile = profile or ClientProfile()
        self.circuit_breaker = None

        kwargs: Dict = {"timeout": self.profile.httpProfile.reqTimeout}

        if not self.profile.httpProfile.keepAlive:
            kwargs["limits"] = httpx.Limits(max_keepalive_connections=0)

        if self.profile.httpProfile.proxy:
            kwargs["proxies"] = self.profile.httpProfile.proxy

        if self.profile.httpProfile.certification is False:
            kwargs["verify"] = False
        elif isinstance(self.profile.httpProfile.certification, str) and self.profile.httpProfile.certification != "":
            kwargs["cert"] = self.profile.httpProfile.certification

        self.http_client = httpx.AsyncClient(**kwargs)

        if not self.profile.disable_region_breaker:
            if self.profile.region_breaker_profile is None:
                self.profile.region_breaker_profile = RegionBreakerProfile()
            self.circuit_breaker = CircuitBreaker(self.profile.region_breaker_profile)
        if self.profile.request_client:
            self.request_client = self._sdkVersion + "; " + self.profile.request_client
        else:
            self.request_client = self._sdkVersion

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self.http_client.aclose()

    async def call_and_deserialize(
            self,
            action: str,
            params: ParamsType,
            resp_cls: Type = dict,
            headers: Dict[str, str] = None,
            opts: Dict = None,
    ):
        opts = opts or {}
        headers = headers or {}
        chain = self._create_default_chain(action, params, resp_cls, headers, opts)
        return await chain.proceed()

    def _create_default_chain(
            self,
            action: str,
            params: ParamsType,
            resp_cls: Type,
            headers: Dict[str, str],
            opts: Dict,
    ):
        chain = RequestChain()
        chain.add_interceptor(self._inter_retry)
        chain.add_interceptor(self._inter_deserialize_resp(resp_cls))
        if self.circuit_breaker:
            chain.add_interceptor(self._inter_breaker(opts))
        chain.add_interceptor(self._inter_build_request(action, params, headers, opts))
        chain.add_interceptor(self._inter_send_request)
        return chain

    async def _inter_retry(self, chain: RequestChain):
        retryer = self.profile.retryer or NoopRetryer()
        return await retryer.send_request(chain.proceed)

    def _inter_build_request(
            self,
            action: str,
            params: ParamsType,
            headers: Dict[str, str],
            opts: Dict,
    ):
        async def inter(chain: RequestChain):
            nonlocal action, params, opts, headers

            if headers is None:
                headers = {}

            if not isinstance(headers, dict):
                raise TencentCloudSDKException("ClientError", "headers must be a dict.")

            if "x-tc-traceid" not in (k.lower() for k in headers.keys()):
                headers["X-TC-TraceId"] = str(uuid.uuid4())

            req = self._build_req(action, params, headers, opts)

            if self.profile.httpProfile.apigw_endpoint:
                req.host = self.profile.httpProfile.apigw_endpoint
                req.headers["Host"] = req.host

            # 低版本的 httpx 不会使用 Client.timeout, 需要 per request setup
            req.extensions["timeout"] = self.http_client.timeout.as_dict()
            chain.request = req

            logger.debug("SendRequest:\n%s", RequestPrettyFormatter(req))

            return await chain.proceed()

        return inter

    def _inter_breaker(self, opts: Dict):
        async def inter(chain: RequestChain):
            generation, need_break = self.circuit_breaker.before_requests()

            endpoint = self._get_endpoint(opts=opts)
            if need_break:
                endpoint = self._service + "." + self.profile.region_breaker_profile.backup_endpoint

            url = self.profile.httpProfile.scheme + endpoint + self._requestPath
            chain.request.url = url

            resp = None
            try:
                resp = await chain.proceed()
                self.circuit_breaker.after_requests(generation, True)
                return resp
            except httpx.TransportError:
                self.circuit_breaker.after_requests(generation, False)
                raise
            except TencentCloudSDKException as e:
                success = resp and "RequestId" in (await resp.aread()) and e.code != "InternalError"
                self.circuit_breaker.after_requests(generation, success)
                raise

        return inter

    @staticmethod
    def _inter_deserialize_resp(resp_cls: Type):
        async def inter(chain: RequestChain):
            resp = await chain.proceed()

            await check_err(resp)

            content_type = resp.headers["Content-Type"]
            if content_type == "text/event-stream":
                return deserialize_sse(resp)

            return await deserialize_json(resp)

        async def check_err(resp: ApiResponse):
            if resp.status_code != 200:
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug("GetResponse: %s", await ResponsePrettyFormatter(resp, format_body=True).astr())
                raise TencentCloudSDKException("ServerNetworkError", await resp.aread())

            ct = resp.headers.get('Content-Type')
            if ct not in ('text/plain', _json_content):
                return

            content = await resp.aread()
            data = json.loads(content)
            if "Error" in data["Response"]:
                code = data["Response"]["Error"]["Code"]
                message = data["Response"]["Error"]["Message"]
                reqid = data["Response"]["RequestId"]
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug("GetResponse: %s", await ResponsePrettyFormatter(resp, format_body=True).astr())
                raise TencentCloudSDKException(code, message, reqid)
            if "DeprecatedWarning" in data["Response"]:
                import warnings
                warnings.filterwarnings("default")
                warnings.warn("This action is deprecated, detail: %s" % data["Response"]["DeprecatedWarning"],
                              DeprecationWarning)

        async def deserialize_json(resp: ApiResponse):
            try:
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug("GetResponse: %s", await ResponsePrettyFormatter(resp, format_body=True).astr())

                content = await resp.aread()
                if resp_cls == dict:
                    return json.loads(content)

                if issubclass(resp_cls, AbstractModel):
                    resp_model = resp_cls()
                    resp_model._deserialize(json.loads(content)["Response"])
                    return resp_model

                raise TencentCloudSDKException("ClientParamsError", "invalid resp_cls %s" % resp_cls)
            finally:
                await resp.aclose()

        async def deserialize_sse(resp: ApiResponse):
            logger.debug("GetResponse:\n%s", ResponsePrettyFormatter(resp, format_body=False))
            e = {}

            try:
                async for line in resp.aiter_lines():
                    line = line.strip()
                    if not line:
                        yield e
                        e = {}
                        continue

                    logger.debug("GetResponse.Readline: %s", line)

                    # comment
                    if line[0] == ':':
                        continue

                    colon_idx = line.find(':')
                    key = line[:colon_idx]
                    val = line[colon_idx + 1:]
                    # If value starts with a U+0020 SPACE character, remove it from value.
                    if val and val[0] == " ":
                        val = val[1:]
                    if key == 'data':
                        # The spec allows for multiple data fields per event, concatenated them with "\n".
                        if 'data' not in e:
                            e['data'] = val
                        else:
                            e['data'] += '\n' + val
                    elif key in ('event', 'id'):
                        e[key] = val
                    elif key == 'retry':
                        e[key] = int(val)
            finally:
                await resp.aclose()

        return inter

    async def _inter_send_request(self, chain: RequestChain):
        return await self.http_client.send(chain.request, stream=True)

    def _get_service_domain(self):
        root_domain = self.profile.httpProfile.rootDomain
        return self._service + "." + root_domain

    def _get_endpoint(self, opts=None):
        endpoint = self.profile.httpProfile.endpoint
        if not endpoint and opts:
            endpoint = urlparse(opts.get("Endpoint", "")).hostname
        if endpoint is None:
            endpoint = self._get_service_domain()
        return endpoint

    def _build_req(self, action: str, params: ParamsType, headers: Dict[str, str], opts: Dict) -> ApiRequest:
        if opts.get('SkipSign'):
            return self._build_req_without_signature(action, params, headers, opts)
        elif self.profile.signMethod == "TC3-HMAC-SHA256" or opts.get("IsMultipart") is True:
            return self._build_req_with_tc3_signature(action, params, headers, opts)
        elif self.profile.signMethod in ("HmacSHA1", "HmacSHA256"):
            return self._build_req_with_old_signature(action, params, headers, opts)
        else:
            raise TencentCloudSDKException("ClientError", "Invalid signature method.")

    def _build_req_without_signature(
            self, action: str, params: ParamsType, headers: Dict[str, str], opts: Dict) -> ApiRequest:
        method = self.profile.httpProfile.reqMethod
        endpoint = self._get_endpoint(opts=opts)
        url = "%s://%s%s" % (self.profile.httpProfile.scheme, endpoint, self._requestPath)
        query = {}
        body = ""

        content_type = self._default_content_type
        if method == 'GET':
            content_type = _form_urlencoded_content
        elif method == 'POST':
            content_type = _json_content
        if opts.get("IsMultipart"):
            content_type = _multipart_content
        if opts.get("IsOctetStream"):
            content_type = _octet_stream
        headers["Content-Type"] = content_type

        if method == "GET" and content_type == _multipart_content:
            raise TencentCloudSDKException("ClientError", "Invalid request method GET for multipart.")

        endpoint = self._get_endpoint(opts=opts)
        timestamp = int(time.time())
        headers["Host"] = endpoint
        headers["X-TC-Action"] = action[0].upper() + action[1:]
        headers["X-TC-RequestClient"] = self.request_client
        headers["X-TC-Timestamp"] = str(timestamp)
        headers["X-TC-Version"] = self._apiVersion
        if self.profile.unsignedPayload is True:
            headers["X-TC-Content-SHA256"] = "UNSIGNED-PAYLOAD"
        if self.region:
            headers['X-TC-Region'] = self.region
        if self.profile.language:
            headers['X-TC-Language'] = self.profile.language

        if method == 'GET':
            params = copy.deepcopy(self._fix_params(params))
            url += "?" + urlencode(params)
        elif content_type == _json_content:
            body = json.dumps(params)
        elif content_type == _multipart_content:
            boundary = uuid.uuid4().hex
            headers["Content-Type"] = content_type + "; boundary=" + boundary
            body = self._get_multipart_body(params, boundary, opts)

        headers["Authorization"] = "SKIP"
        return ApiRequest(method, url, params=query, content=body, headers=headers)

    def _build_req_with_tc3_signature(
            self, action: str, params: ParamsType, headers: Dict[str, str], opts: Dict) -> ApiRequest:
        method = self.profile.httpProfile.reqMethod
        endpoint = self._get_endpoint(opts=opts)
        host = headers.get("Host", endpoint)
        url = "%s://%s%s" % (self.profile.httpProfile.scheme, endpoint, self._requestPath)
        query = ""
        body = ""

        content_type = self._default_content_type
        if method == 'GET':
            content_type = _form_urlencoded_content
        elif method == 'POST':
            content_type = _json_content
        if opts.get("IsMultipart"):
            content_type = _multipart_content
        elif opts.get("IsOctetStream"):
            if method != "POST":
                raise TencentCloudSDKException("ClientError", "Invalid request method.")
            content_type = _octet_stream
        headers["Content-Type"] = content_type

        if method == "GET" and content_type == _multipart_content:
            raise TencentCloudSDKException("ClientError", "Invalid request method GET for multipart.")

        timestamp = int(time.time())
        cred_secret_id, cred_secret_key, cred_token = self.credential.get_credential_info()
        headers["Host"] = host
        headers["X-TC-Action"] = action[0].upper() + action[1:]
        headers["X-TC-RequestClient"] = self.request_client
        headers["X-TC-Timestamp"] = str(timestamp)
        headers["X-TC-Version"] = self._apiVersion
        if self.profile.unsignedPayload is True:
            headers["X-TC-Content-SHA256"] = "UNSIGNED-PAYLOAD"
        if self.region:
            headers['X-TC-Region'] = self.region
        if cred_token:
            headers['X-TC-Token'] = cred_token
        if self.profile.language:
            headers['X-TC-Language'] = self.profile.language

        if method == 'GET':
            query = urlencode(copy.deepcopy(self._fix_params(params)))
        elif content_type == _json_content:
            body = json.dumps(params)
        elif content_type == _multipart_content:
            boundary = uuid.uuid4().hex
            headers["Content-Type"] = content_type + "; boundary=" + boundary
            body = self._get_multipart_body(params, boundary, opts)
        elif content_type == _octet_stream:
            body = params

        if isinstance(body, str):
            body = body.encode("utf-8")

        service = self._service
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        signature = self._get_tc3_signature(
            method, self._requestPath, query, body, headers, date, service, cred_secret_key, opts)

        auth = "TC3-HMAC-SHA256 Credential=%s/%s/%s/tc3_request, SignedHeaders=content-type;host, Signature=%s" % (
            cred_secret_id, date, service, signature)
        headers["Authorization"] = auth
        # httpx 0.22.0 版本会过滤掉空 value 的 params 如 "a=&b=2"
        # 不能使用 params 参数, 需要用 url 绕过, 后续版本已经修复, 但是 py36 最高只能安装 0.22.0
        url += "?" + query
        return ApiRequest(method, url, content=body, headers=headers)

    def _build_req_with_old_signature(
            self, action: str, params: ParamsType, headers: Dict[str, str], opts: Dict) -> ApiRequest:

        if opts.get("IsOctetStream"):
            raise TencentCloudSDKException("ClientError", "Invalid signature method.")

        method = self.profile.httpProfile.reqMethod
        endpoint = self._get_endpoint(opts=opts)
        url = "%s://%s%s" % (self.profile.httpProfile.scheme, endpoint, self._requestPath)
        query = {}
        body = ""

        params = copy.deepcopy(self._fix_params(params))
        params['Action'] = action[0].upper() + action[1:]
        params['RequestClient'] = self.request_client
        params['Nonce'] = random.randint(1, sys.maxsize)
        params['Timestamp'] = int(time.time())
        params['Version'] = self._apiVersion

        cred_secret_id, cred_secret_key, cred_token = self.credential.get_credential_info()

        if self.region:
            params['Region'] = self.region

        if cred_token:
            params['Token'] = cred_token

        if cred_secret_id:
            params['SecretId'] = cred_secret_id

        if self.profile.signMethod:
            params['SignatureMethod'] = self.profile.signMethod

        if self.profile.language:
            params['Language'] = self.profile.language

        signInParam = self._format_sign_string(params, opts)
        params['Signature'] = Sign.sign(str(cred_secret_key),
                                        str(signInParam),
                                        str(self.profile.signMethod))
        if method == "GET":
            query = params
        else:
            body = urlencode(params)

        headers["Content-Type"] = "application/x-www-form-urlencoded"
        return ApiRequest(method, url, params=query, content=body, headers=headers)

    def _format_sign_string(self, params, opts=None):
        formatParam = {}
        for k in params:
            formatParam[k.replace('_', '.')] = params[k]
        strParam = '&'.join('%s=%s' % (k, formatParam[k]) for k in sorted(formatParam))
        msg = '%s%s%s?%s' % (
            self.profile.httpProfile.reqMethod, self._get_endpoint(opts=opts), self._requestPath, strParam)
        return msg

    def _fix_params(self, params):
        if not isinstance(params, (dict,)):
            return params
        return self._format_params(None, params)

    def _format_params(self, prefix, params):
        d = {}
        if params is None:
            return d

        if not isinstance(params, (tuple, list, dict)):
            d[prefix] = params
            return d

        if isinstance(params, (list, tuple)):
            for idx, item in enumerate(params):
                if prefix:
                    key = "{0}.{1}".format(prefix, idx)
                else:
                    key = "{0}".format(idx)
                d.update(self._format_params(key, item))
            return d

        if isinstance(params, dict):
            for k, v in params.items():
                if prefix:
                    key = '{0}.{1}'.format(prefix, k)
                else:
                    key = '{0}'.format(k)
                d.update(self._format_params(key, v))
            return d

        raise TencentCloudSDKException("ClientParamsError", "some params type error")

    def _get_multipart_body(self, params, boundary, options=None):
        if options is None:
            options = {}
        # boundary and params key will never contain unicode characters
        boundary = boundary.encode()
        binparas = options.get("BinaryParams", [])
        body = b''
        for k, v in params.items():
            kbytes = k.encode()
            body += b'--%s\r\n' % boundary
            body += b'Content-Disposition: form-data; name="%s"' % kbytes
            if k in binparas:
                body += b'; filename="%s"\r\n' % kbytes
            else:
                body += b"\r\n"
                if isinstance(v, list) or isinstance(v, dict):
                    v = json.dumps(v)
                    body += b'Content-Type: application/json\r\n'
            if sys.version_info[0] == 3 and isinstance(v, type("")):
                v = v.encode()
            body += b'\r\n%s\r\n' % v
        if body != b'':
            body += b'--%s--\r\n' % boundary
        return body

    @staticmethod
    def _get_tc3_signature(method: str, path: str, query: str, body: bytes, headers: Dict, date: str, service: str,
                           secret_key: str, opts: Dict):
        canonical_uri = path
        canonical_querystring = query
        payload = body

        if headers.get("X-TC-Content-SHA256") == "UNSIGNED-PAYLOAD":
            payload = b"UNSIGNED-PAYLOAD"

        payload_hash = hashlib.sha256(payload).hexdigest()

        canonical_headers = 'content-type:%s\nhost:%s\n' % (
            headers["Content-Type"], headers["Host"])
        signed_headers = 'content-type;host'
        canonical_request = '%s\n%s\n%s\n%s\n%s\n%s' % (method,
                                                        canonical_uri,
                                                        canonical_querystring,
                                                        canonical_headers,
                                                        signed_headers,
                                                        payload_hash)

        algorithm = 'TC3-HMAC-SHA256'
        credential_scope = date + '/' + service + '/tc3_request'
        if sys.version_info[0] == 3:
            canonical_request = canonical_request.encode("utf8")
        digest = hashlib.sha256(canonical_request).hexdigest()
        string2sign = '%s\n%s\n%s\n%s' % (algorithm,
                                          headers["X-TC-Timestamp"],
                                          credential_scope,
                                          digest)
        return Sign.sign_tc3(secret_key, date, service, string2sign)

    def set_stream_logger(self, stream=None, level=logging.DEBUG, log_format=None):
        """Add a stream handler

        :param stream: e.g. ``sys.stdout`` ``sys.stdin`` ``sys.stderr``
        :type stream: IO[str]
        :param level: Logging level, e.g. ``logging.INFO``
        :type level: int
        :param log_format: Log message format
        :type log_format: str
        """
        log = logging.getLogger(LOGGER_NAME)
        log.setLevel(level)
        sh = logging.StreamHandler(stream)
        sh.setLevel(level)
        if log_format is None:
            log_format = self.FMT
        formatter = logging.Formatter(log_format)
        sh.setFormatter(formatter)
        log.addHandler(sh)

    def set_file_logger(self, file_path, level=logging.DEBUG, log_format=None):
        """Add a file handler

        :param file_path: path of log file
        :type file_path: str
        :param level: Logging level, e.g. ``logging.INFO``
        :type level: int
        :param log_format: Log message format
        :type log_format: str
        """
        log = logging.getLogger(LOGGER_NAME)
        log.setLevel(level)
        mb = 1024 * 1024
        fh = logging.handlers.RotatingFileHandler(file_path, maxBytes=512 * mb, backupCount=10)
        fh.setLevel(level)
        if log_format is None:
            log_format = self.FMT
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        log.addHandler(fh)

    def set_default_logger(self):
        """Set default log handler"""
        pass
