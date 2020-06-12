import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

from tencentcloud.iai.v20180301 import iai_client, models

def test_iai_create_person():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    client = iai_client.IaiClient(cred, "ap-guangzhou")
    req = models.CreatePersonRequest()
    req.GroupId = "1"
    req.PersonName = "foo"
    req.PersonId = "3"
    req.Gender = 1
    try:
        resp = client.CreatePerson(req)
    except TencentCloudSDKException as e:
        assert e.code == 'InvalidParameterValue.ImageEmpty'
