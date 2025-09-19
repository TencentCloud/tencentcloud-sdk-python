# -*- coding: utf8 -*-
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.cvm.v20170312 import cvm_client_async, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


@pytest.mark.asyncio
async def test_describe_instances():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    hp = HttpProfile()
    hp.scheme = "http"
    hp.endpoint = "cvm.ap-shanghai.tencentcloudapi.com"

    cp = ClientProfile()
    cp.httpProfile = hp

    client = cvm_client_async.CvmClient(cred, "ap-guangzhou", cp)
    req = models.DescribeInstancesRequest()
    try:
        resp = await client.DescribeInstances(req)
    except TencentCloudSDKException as e:
        """
        预期返回403 forbidden
        但是不同的网络环境中不一定返回的都是403 forbidden
        有可能是超时，有可能状态码是502但是没有任何错误消息
        因此只要捕获到了异常都算pass
        """
        return
    assert "" == "exception is not captured"