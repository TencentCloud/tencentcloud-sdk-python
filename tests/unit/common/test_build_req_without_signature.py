import copy
import json
import os
from unittest.mock import MagicMock, patch
from tencentcloud.common import credential, abstract_client
from urllib.parse import urlencode
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

_default_content_type = "application/json"
_form_urlencoded_content = "application/x-www-form-urlencoded"
_json_content = "application/json"
_multipart_content = "multipart/form-data"
_octet_stream = "application/octet-stream"


def get_client():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "sts.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "HmacSHA256"

    client = abstract_client.AbstractClient(cred, "ap-shanghai", profile=clientProfile)
    return client


class Request:
    def __init__(self, data, header, method):
        self.data = data
        self.header = header
        self.method = method


def test_build_req_without_signature_get_method():
    """测试 GET 请求"""
    client = get_client()
    req = Request({}, {}, "GET")
    action = 'DescribeServices'
    params = {'service': 'cvm'}
    options = None
    client._build_req_without_signature(action, params, req, options)
    print(req.header)
    assert req.header["Content-Type"] == _form_urlencoded_content
    assert req.data == urlencode(copy.deepcopy(client._fix_params(params)))


def test_build_req_without_signature_post_method():
    """测试 POST 请求"""
    client = get_client()
    req = Request({}, {}, "GET")
    action = 'DescribeServices'
    params = {'service': 'cvm'}
    options = None
    req.method = 'POST'
    client._build_req_without_signature(action, params, req, options)
    assert req.header["Content-Type"] == _json_content
    assert req.data == json.dumps(params)


def test_build_req_without_signature_multipart_method(mocker):
    """测试 multipart格式"""
    client = get_client()
    req = Request({}, {}, "GET")
    action = 'DescribeServices'
    params = {'service': 'cvm'}
    options = {"IsMultipart": True}
    req.method = 'POST'
    with mocker.patch('uuid.uuid4', return_value=MagicMock(hex="123456")):
        client._build_req_without_signature(action, params, req, options)
        expected_content_type = f"{_multipart_content}; boundary=123456"
        assert req.header["Content-Type"] == expected_content_type


def test_build_req_without_signature_octet_stream_method():
    """测试 octet-stream"""
    client = get_client()
    req = Request({}, {}, "POST")
    action = 'DescribeServices'
    params = {'service': 'cvm'}
    options = {"IsOctetStream": True}
    client._build_req_without_signature(action, params, req, options)
    assert req.header["Content-Type"] == _octet_stream


def test_build_req_without_signature_unsigned_payload():
    """测试无签名"""
    client = get_client()
    req = Request({}, {}, "POST")
    action = 'DescribeServices'
    params = {'service': 'cvm'}
    options = None
    client.profile.unsignedPayload = True
    client._build_req_without_signature(action, params, req, options)
    assert req.header["X-TC-Content-SHA256"] == "UNSIGNED-PAYLOAD"


def test_build_req_without_signature_region():
    """测试 region"""
    client = get_client()
    req = Request({}, {}, "POST")
    action = 'DescribeServices'
    params = {'service': 'cvm'}
    options = None
    client._build_req_without_signature(action, params, req, options)
    assert req.header['X-TC-Region'] == client.region


def test_build_req_without_signature_language():
    """测试所选语言"""
    client = get_client()
    req = Request({}, {}, "POST")
    action = 'DescribeServices'
    params = {'service': 'cvm'}
    options = None
    client.profile.language = 'zh-CN'
    client._build_req_without_signature(action, params, req, options)
    assert req.header['X-TC-Language'] == client.profile.language
