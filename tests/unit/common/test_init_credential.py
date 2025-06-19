from tencentcloud.common.credential import Credential
from tencentcloud.common.exception import TencentCloudSDKException


def test_init_credential():
    try:
        credential = Credential(None, None)
    except TencentCloudSDKException as e:
        assert e.message == "secret id should not be none or empty"
        assert e.code == "InvalidCredential"
    try:
        credential = Credential(" 123456", None)
    except TencentCloudSDKException as e:
        assert e.message == "secret id should not contain spaces"
        assert e.code == "InvalidCredential"

    try:
        credential = Credential("123456", None)
    except TencentCloudSDKException as e:
        assert e.message == "secret key should not be none or empty"
        assert e.code == "InvalidCredential"
    try:
        credential = Credential("123456"," 123456")
    except TencentCloudSDKException as e:
        assert e.message == "secret key should not contain spaces"
        assert e.code == "InvalidCredential"


def test_init_credential_return_value():
    credential = Credential("secret_id", "secret_key")
    assert credential.secretId == "secret_id"
    assert credential.secretKey == "secret_key"
