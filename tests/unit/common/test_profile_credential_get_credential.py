import os

from tencentcloud.common.credential import ProfileCredential


def test_get_credential_file_not_exists(mocker):
    os.environ['HOME'] = "tencent"
    cred = ProfileCredential()
    assert cred.get_credential() is None
    assert cred.secret_id is None
    assert cred.secret_key is None
    assert cred.role_arn is None
