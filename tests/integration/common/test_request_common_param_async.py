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
async def test_request_common_param_language():
    endpoint = "cvm.tencentcloudapi.com"
    region = "ap-guangzhou"
    language = "en-US"

    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = endpoint

        clientProfile = ClientProfile(language=language)
        clientProfile.httpProfile = httpProfile
        client = cvm_client_async.CvmClient(cred, region, clientProfile)

        req = models.DescribeZonesRequest()
        resp = await client.DescribeZones(req)
        if resp.TotalCount > 0:
            assert "Guangzhou" in resp.to_json_string(), "language=en-US not working"
    except TencentCloudSDKException as err:
        assert False, "unexpected request failure"