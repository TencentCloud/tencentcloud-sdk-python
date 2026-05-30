from mock.mock import patch

from tencentcloud.common.credential import STSAssumeRoleCredential


@patch('tencentcloud.common.credential.CommonClient')
def test_sts_assume_role_credential(mock_client):
    credential = STSAssumeRoleCredential('secret_id', 'secret_key', 'role_name', 'role_session_name')
    client = mock_client.return_value
    client.call_json.return_value = {
            "Response": {
                "Credentials": {
                    "Token": "mocked_token",
                    "TmpSecretId": "mocked_tmp_secret_id",
                    "TmpSecretKey": "mocked_tmp_secret_key"
                },
                "ExpiredTime": 1633072800
            }
        }
    credential.get_sts_tmp_role_arn()
    assert credential._token == 'mocked_token'
    assert credential._tmp_secret_id == 'mocked_tmp_secret_id'
    assert credential._tmp_secret_key == 'mocked_tmp_secret_key'
    assert credential._expired_time == 1633066320.0
