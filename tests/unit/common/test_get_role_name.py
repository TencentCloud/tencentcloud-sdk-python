from tencentcloud.common.credential import CVMRoleCredential
from tencentcloud.common.exception import TencentCloudSDKException


def test_get_role_name():
    credential = CVMRoleCredential("cvm")
    assert credential.get_role_name() == "cvm"


def test_need_refresh(mocker):
    credential = CVMRoleCredential()
    with mocker.patch("time.time", return_value=0):
        assert credential._need_refresh() is True

    with mocker.patch("time.time", return_value=-400):
        assert credential._need_refresh() is False

