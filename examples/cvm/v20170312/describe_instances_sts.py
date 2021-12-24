import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    cred = credential.STSAssumeRoleCredential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"), # or read it from your config file
        os.environ.get("TENCENTCLOUD_SECRET_KEY"),
        "must-a-valid-role-arn", # for e.g.: "qcs::cam::uin/100123456789:roleName/test"
        "whatever-role-session-name")

    client = cvm_client.CvmClient(cred, "ap-guangzhou")
    req = models.DescribeInstancesRequest()
    resp = client.DescribeInstances(req)
    print(resp.to_json_string(indent=2))
except TencentCloudSDKException as err:
    print(err)
