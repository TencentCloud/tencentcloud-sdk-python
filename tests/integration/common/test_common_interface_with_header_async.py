# -*- coding: utf-8 -*-

import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.common_client_async import CommonClient


@pytest.mark.asyncio
async def test_common_interface():
    service = "cvm"
    version = "2017-03-12"
    region = "ap-guangzhou"

    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        httpProfile = HttpProfile()
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        headers = {
            "X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca",
        }
        client = CommonClient(service, version, cred, region, clientProfile)
        resp = await client.call_and_deserialize("DescribeZones", {}, headers=headers)
    except TencentCloudSDKException as err:
        assert False