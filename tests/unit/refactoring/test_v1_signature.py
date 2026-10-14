from mock.mock import patch, MagicMock

from tencentcloud.common.http.request import RequestInternal

from tencentcloud.common import abstract_client, credential


@patch("tencentcloud.common.abstract_client.Sign.sign")
@patch("tencentcloud.common.abstract_client.random.randint")
@patch("tencentcloud.common.abstract_client.time.time")
def test_build_req_with_old_signature_inter_correct(mock_time, mock_randint, mock_sign):
    mock_sign.return_value = "mocked_sign"
    mock_time.return_value = 1590000000
    mock_randint.return_value = 123456789
    cred = credential.Credential("secret_id", "secret_key")
    client = abstract_client.AbstractClient(cred, "ap-shanghai", None)
    req = RequestInternal(method="GET", header={"Content-Type": "application"}, data="")
    client.request_client = 'test_client'
    client._apiVersion = '2020-01-01'
    client.region = 'ap-guangzhou'
    client.profile = MagicMock()
    client.profile.signMethod = 'HmacSHA256'
    client.profile.language = 'zh-CN'
    client._build_req_with_old_signature("DELETE", {}, req)
    assert req.data == ("Action=DELETE&RequestClient=test_client&Nonce=123456789&Timestamp=1590000000&Version=2020-01"
                        "-01&Region=ap-guangzhou&SecretId=secret_id&SignatureMethod=HmacSHA256&Language=zh-CN"
                        "&Signature=mocked_sign")
    assert req.header["Content-Type"] == "application/x-www-form-urlencoded"
