from tencentcloud.common.credential import STSAssumeRoleCredential, Credential
from tencentcloud.common.common_client import CommonClient


def test_need_refresh_has_None(mocker):
    credential = STSAssumeRoleCredential(None, None, None, None, 7200, "us-east-1")
    get_sts_tmp_role_arn = mocker.patch.object(credential, "get_sts_tmp_role_arn")
    credential._need_refresh()
    get_sts_tmp_role_arn.assert_called_once()


