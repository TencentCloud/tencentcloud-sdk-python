from unittest import mock

from tencentcloud.common.credential import OIDCRoleArnCredential


def test_oidc_role_arn_credential_secretId(mocker):
    cred = OIDCRoleArnCredential('', '', '', '', '', 7200)
    _keep_fresh = mocker.patch.object(cred, '_keep_fresh')
    cred.secretId
    _keep_fresh.assert_called_once()
    assert cred._tmp_secret_id is None


def test_oidc_role_arn_credential_secretKey(mocker):
    cred = OIDCRoleArnCredential('', '', '', '', '', 7200)
    _keep_fresh = mocker.patch.object(cred, '_keep_fresh')
    cred.secretKey
    _keep_fresh.assert_called_once()
    assert cred._tmp_secret_key is None


def test_oidc_role_arn_credential_secret_id(mocker):
    cred = OIDCRoleArnCredential('', '', '', '', '', 7200)
    _keep_fresh = mocker.patch.object(cred, '_keep_fresh')
    cred.secret_id
    _keep_fresh.assert_called_once()
    assert cred._tmp_secret_id is None


def test_oidc_role_arn_credential_secret_key(mocker):
    cred = OIDCRoleArnCredential('', '', '', '', '', 7200)
    _keep_fresh = mocker.patch.object(cred, '_keep_fresh')
    cred.secret_key
    _keep_fresh.assert_called_once()
    assert cred._tmp_secret_key is None


def test_oidc_role_arn_credential_secret_token(mocker):
    cred = OIDCRoleArnCredential('', '', '', '', '', 7200)
    _keep_fresh = mocker.patch.object(cred, '_keep_fresh')
    cred.token
    _keep_fresh.assert_called_once()
    assert cred._token is None


def test_oidc_role_arn_credential_keep_fresh(mocker):
    cred = OIDCRoleArnCredential('', '', '', '', '', 7200)
    refresh = mocker.patch.object(cred, 'refresh')
    cred._keep_fresh()
    refresh.assert_called_once()


def test_oidc_role_arn_credential_refresh(mocker):
    cred = OIDCRoleArnCredential('ap-shanghai', '', '', '', '', 7200)
    _init_from_tke = mocker.patch.object(cred, '_init_from_tke')
    cred._is_tke = True
    rsp = {
        "Response": {
            "Credentials": {
                "Token": "your_token",
                "TmpSecretId": "your_tmp_secret_id",
                "TmpSecretKey": "your_tmp_secret_key"
            },
            "ExpiredTime": 1000  # 例如：设置为某个时间点的时间戳
        }
    }
    with mock.patch('tencentcloud.common.common_client.CommonClient.call_json', return_value=rsp):
        cred.refresh()
        _init_from_tke.assert_called_once()
        assert cred._token == 'your_token'
        assert cred._tmp_secret_id == 'your_tmp_secret_id'
        assert cred._tmp_secret_key == 'your_tmp_secret_key'
        assert cred._expired_time == 280
