from tencentcloud.common.credential import STSAssumeRoleCredential


def test_sts_assume_role_credential_init(mocker):
    credential = STSAssumeRoleCredential(None, None, None, None, 7200, "us-east-1")
    assert credential._endpoint == "us-east-1"


def test_sts_assume_role_credential_secretId(mocker):
    credential = STSAssumeRoleCredential(None, None, None, None, 7200, "us-east-1")
    _need_refresh = mocker.patch.object(credential, "_need_refresh")
    credential.secretId
    _need_refresh.assert_called_once()


def test_sts_assume_role_credential_secretKey(mocker):
    credential = STSAssumeRoleCredential(None, None, None, None, 7200, "us-east-1")
    _need_refresh = mocker.patch.object(credential, "_need_refresh")
    credential.secretKey
    _need_refresh.assert_called_once()


def test_sts_assume_role_credential_secret_id(mocker):
    credential = STSAssumeRoleCredential(None, None, None, None, 7200, "us-east-1")
    _need_refresh = mocker.patch.object(credential, "_need_refresh")
    credential.secret_id
    _need_refresh.assert_called_once()


def test_sts_assume_role_credential_secret_key(mocker):
    credential = STSAssumeRoleCredential(None, None, None, None, 7200, "us-east-1")
    _need_refresh = mocker.patch.object(credential, "_need_refresh")
    credential.secret_key
    _need_refresh.assert_called_once()


def test_sts_assume_role_credential_token(mocker):
    credential = STSAssumeRoleCredential(None, None, None, None, 7200, "us-east-1")
    _need_refresh = mocker.patch.object(credential, "_need_refresh")
    credential.token
    _need_refresh.assert_called_once()
