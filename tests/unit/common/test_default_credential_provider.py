from tencentcloud.common.credential import DefaultCredentialProvider, EnvironmentVariableCredential
from tencentcloud.common.exception import TencentCloudSDKException


def test_get_credential(mocker):
    credential = DefaultCredentialProvider()
    mock_get_credentials = mocker.patch.object(credential, 'get_credentials')
    credential.get_credential()
    mock_get_credentials.assert_called_once_with()


def test_get_credentials_with_cred():
    credential = DefaultCredentialProvider()
    credential.cred = 'test'
    assert credential.get_credentials() == 'test'


def test_get_credentials_without_cred_env(mocker):
    credential = DefaultCredentialProvider()
    credential.cred = None
    with mocker.patch('tencentcloud.common.credential.EnvironmentVariableCredential.get_credential',
                      return_value="env_cred"):
        cred = credential.get_credentials()
        assert cred == "env_cred"


def test_get_credential_without_cred_pro(mocker):
    credential = DefaultCredentialProvider()
    credential.cred = None
    with mocker.patch('tencentcloud.common.credential.EnvironmentVariableCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.ProfileCredential.get_credential', return_value="env_cred"):
        cred = credential.get_credentials()
        assert cred == "env_cred"


def test_get_credential_without_cred_cvm(mocker):
    credential = DefaultCredentialProvider()
    credential.cred = None
    with mocker.patch('tencentcloud.common.credential.EnvironmentVariableCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.ProfileCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.CVMRoleCredential.get_credential', return_value="env_cred"):
        cred = credential.get_credentials()
        assert cred == "env_cred"


def test_get_credential_without_cred_default(mocker):
    credential = DefaultCredentialProvider()
    credential.cred = None
    with mocker.patch('tencentcloud.common.credential.EnvironmentVariableCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.ProfileCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.CVMRoleCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.DefaultTkeOIDCRoleArnProvider.get_credential', return_value="env_cred"):
        cred = credential.get_credentials()
        assert cred == "env_cred"


def test_get_credential_without_cred_exception(mocker):
    credential = DefaultCredentialProvider()
    credential.cred = None
    with mocker.patch('tencentcloud.common.credential.EnvironmentVariableCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.ProfileCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.CVMRoleCredential.get_credential', return_value=None), \
            mocker.patch('tencentcloud.common.credential.DefaultTkeOIDCRoleArnProvider.get_credential', return_value=None):
        try:
            cred = credential.get_credentials()
            assert cred == "env_cred"
        except TencentCloudSDKException as e:
            assert e.message == "no valid credentail."
            assert e.code == "ClientSideError"
