import os

from tencentcloud.common.credential import EnvironmentVariableCredential


def test_get_credential_with_valid_env_vars():
    credential = EnvironmentVariableCredential()
    os.environ['TENCENTCLOUD_SECRET_ID'] = 'valid_secret_id'
    os.environ['TENCENTCLOUD_SECRET_KEY'] = 'valid_secret_key'
    assert credential.get_credential() is not None
    assert credential.secret_id == 'valid_secret_id'
    assert credential.secret_key == 'valid_secret_key'


def test_get_credential_with_missing_env_vars():
    credential = EnvironmentVariableCredential()
    # 清除环境变量
    if 'TENCENTCLOUD_SECRET_ID' in os.environ:
        del os.environ['TENCENTCLOUD_SECRET_ID']
    if 'TENCENTCLOUD_SECRET_KEY' in os.environ:
        del os.environ['TENCENTCLOUD_SECRET_KEY']
    assert credential.get_credential() is None


def test_get_credential_with_empty_env_vars():
    credential = EnvironmentVariableCredential()
    os.environ['TENCENTCLOUD_SECRET_ID'] = ''
    os.environ['TENCENTCLOUD_SECRET_KEY'] = ''
    assert credential.get_credential() is None
