import os

from tencentcloud.common import abstract_client, credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


class Request:
    def __init__(self, data, header):
        self.data = data
        self.header = header


def test_build_req_with_old_signature_inter_correct(mocker):
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "sts.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.signMethod = "HmacSHA256"

    client = abstract_client.AbstractClient(cred, None, profile=clientProfile)

    req = Request({
        "data": {
            "name": "张三",
            "age": 30,
            "email": "zhangsan@example.com"
        }
    },
        {
            "header": {
                "Content-Type": "application/json"
            }})
    with mocker.patch('time.time', return_value=1634567890), mocker.patch('random.randint', return_value=123456):
        """设置mock对象，固定时间戳和随机数"""
        client._build_req_with_old_signature('action', {}, req)
        assert req.header["Content-Type"] == "application/x-www-form-urlencoded"
