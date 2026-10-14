from tencentcloud.common.credential import CVMRoleCredential


def test_cvm_role_credential_init_id(mocker):
    credential = CVMRoleCredential("cvm")
    update_credential = mocker.patch.object(credential, "update_credential")
    _secret_id = credential.secret_id
    update_credential.assert_called_once()
    assert _secret_id == credential.secretId


def test_cvm_role_credential_init_key(mocker):
    credential = CVMRoleCredential("cvm")
    update_credential = mocker.patch.object(credential, "update_credential")
    _secret_key = credential.secret_key
    update_credential.assert_called_once()
    assert _secret_key == credential.secretId
    assert credential.secretKey is None


def test_cvm_role_credential_init_token(mocker):
    credential = CVMRoleCredential("cvm")
    update_credential = mocker.patch.object(credential, "update_credential")
    credential.token
    update_credential.assert_called_once()
    assert credential.token is None
