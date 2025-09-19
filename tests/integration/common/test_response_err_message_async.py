# -*- coding: utf-8 -*-
import json
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client_async, models


@pytest.mark.asyncio
async def test_response_error_message():
    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cvm_client_async.CvmClient(cred, "ap-guangzhou", clientProfile)

        req = models.DescribeInstancesOperationLimitRequest()
        params = {
            "InstanceIds": [""],
            "Operation": "INSTANCE_DEGRADE",
        }
        req.from_json_string(json.dumps(params))
        resp = await client.DescribeInstancesOperationLimit(req)
        assert False, "It must fail because param InstanceIds is empty"
    except TencentCloudSDKException as err:
        assert "InvalidParameterValue.InstanceIdMalformed" in err.code, "unexpected error code"