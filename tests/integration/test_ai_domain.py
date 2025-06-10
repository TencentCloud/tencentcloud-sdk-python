# -*- coding: utf-8 -*-
import itertools
from contextlib import contextmanager

from tencentcloud.common import credential
from tencentcloud.common import common_client
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.es.v20250101 import es_client, models


# patch requests.Session.request to get underlying request we send
@contextmanager
def mock_requests():
    import requests
    real_request = requests.Session.request

    req_args = {}

    def interceptor(self, method, url, **kwargs):
        req_args["self"] = self
        req_args["method"] = method
        req_args["url"] = url
        req_args.update(kwargs)
        return real_request(self, method, url, **kwargs)

    requests.Session.request = interceptor

    yield req_args

    requests.Session.request = real_request


def parse_host(url):
    try:
        from urlparse import urlparse  # Python 2
    except ImportError:
        from urllib.parse import urlparse  # Python 3
    return urlparse(url).hostname


def test_ai_domain_by_default():
    """sse API use ai-domain by default"""
    sign_methods = ["TC3-HMAC-SHA256", "HmacSHA1", "HmacSHA256"]
    req_methods = ["GET", "POST"]
    expected_host = "es.ai.tencentcloudapi.com"

    for sign_method, req_method in itertools.product(sign_methods, req_methods):
        cred = credential.Credential("xx", "yy")
        cpf = ClientProfile()
        cpf.signMethod = sign_method
        cpf.httpProfile.reqMethod = req_method
        cli = es_client.EsClient(cred, "", cpf)

        with mock_requests() as req_args:
            req = models.ParseDocumentRequest()
            try:
                cli.ParseDocument(req)
            except TencentCloudSDKException:
                pass

            assert req_args["method"] == req_method
            assert parse_host(req_args["url"]) == expected_host


def test_ai_domain_override_by_endpoint():
    """sse API use ClientProfile.HttpProfile.Endpoint instead of ai-domain if specified"""
    sign_methods = ["TC3-HMAC-SHA256", "HmacSHA1", "HmacSHA256"]
    req_methods = ["GET", "POST"]
    expected_host = "es.tencentcloudapi.com"

    for sign_method, req_method in itertools.product(sign_methods, req_methods):
        cred = credential.Credential("xx", "yy")
        cpf = ClientProfile()
        cpf.httpProfile.endpoint = expected_host
        cpf.signMethod = sign_method
        cpf.httpProfile.reqMethod = req_method
        cli = es_client.EsClient(cred, "", cpf)

        with mock_requests() as req_args:
            req = models.ParseDocumentRequest()
            try:
                cli.ParseDocument(req)
            except TencentCloudSDKException:
                pass

            assert req_args["method"] == req_method
            assert parse_host(req_args["url"]) == expected_host


def test_ai_domain_override_by_options():
    """sse API use domain specified by options["Endpoint"]"""
    sign_methods = ["TC3-HMAC-SHA256", "HmacSHA1", "HmacSHA256"]
    req_methods = ["GET", "POST"]
    expected_host = "es.ai.tencentcloudapi.com"

    for sign_method, req_method in itertools.product(sign_methods, req_methods):
        cred = credential.Credential("xx", "yy")
        cpf = ClientProfile()
        cpf.signMethod = sign_method
        cpf.httpProfile.reqMethod = req_method
        cli = common_client.CommonClient("cvm", '2017-03-12', cred, "ap-shanghai", profile=cpf)

        with mock_requests() as req_args:
            try:
                cli.call_sse("ParseDocument", {}, options={"Host": expected_host})
            except TencentCloudSDKException:
                pass

            assert req_args["method"] == req_method
            assert parse_host(req_args["url"]) == expected_host
