from mock.mock import MagicMock, patch
from tencentcloud.common.http.request import RequestInternal

from tencentcloud.common import abstract_client, credential
from tencentcloud.common.exception import TencentCloudSDKException


@patch('tencentcloud.common.abstract_client.AbstractClient._get_tc3_signature')
@patch('tencentcloud.common.abstract_client.time.time')
def test_build_req_with_tc3_signature(mock_time, mock_get_tc3_signature):
    mock_time.return_value = 1732608295
    mock_get_tc3_signature.return_value = 'mocked_signature'
    cred = credential.Credential("secret_id", "secret_key")
    client = abstract_client.AbstractClient(cred, "ap-shanghai", None)
    # 测试异常情况
    header = {
        "Content-Type": "application/json",
        "host": "127.0.0.1",
        "X-TC-Action": "DescribeInstances",
        "X-TC-RequestClient": "tencentcloud-python",
        "X-TC-Version": "2018-04-09",
        "X-TC-Timestamp": "1527899580",
        "Auth": None
    }
    req = RequestInternal(method="GET", header=header)
    options = {"IsMultipart": True}
    try:
        client._build_req_with_tc3_signature("DescribeInstances", {}, req, options)
    except TencentCloudSDKException as e:
        assert e.message == "Invalid request method GET for multipart."
        assert e.code == "ClientError"

    # 测试正常情况
    req = RequestInternal(method="GET", header={"Content-Type": "application"})
    client._build_req_with_tc3_signature("DescribeInstances", {}, req, None)
    assert req.header['Content-Type'] == "application/x-www-form-urlencoded"
    assert req.header['Host'] == ".tencentcloudapi.com"
    assert req.header['X-TC-RequestClient'] == "SDK_PYTHON_3.0.1242"
    assert req.header['X-TC-Version'] == ""
    assert req.header['X-TC-Timestamp'] == "1732608295"
    assert req.header['Authorization'] == ("TC3-HMAC-SHA256 Credential=secret_id/2024-11-26//tc3_request, "
                                           "SignedHeaders=content-type;host, Signature=mocked_signature")


@patch('tencentcloud.common.abstract_client.Sign.sign_tc3')
def test_get_tc3_signature(mock_sign_tc3):
    mock_sign_tc3.return_value = "mocked_signature"
    cred = credential.Credential("secret_id", "secret_key")
    client = abstract_client.AbstractClient(cred, "ap-shanghai", None)
    header = {
        "X-TC-Content-SHA256": "UNSIGNED-PAYLOAD",
        "Content-Type": "application/json",
        "Host": "cvm.tencentcloudapi.com",
        "X-TC-Timestamp": "1732608295"
    }
    req = RequestInternal(method="GET", header=header, uri="/")
    sign = client._get_tc3_signature({}, req, "2024-11-26", "cvm")
    assert sign == "mocked_signature"
