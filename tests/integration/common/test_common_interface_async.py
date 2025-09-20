# -*- coding: utf-8 -*-

import os

import pytest

from tencentcloud.common import credential
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

        client = CommonClient(service, version, cred, region)
        resp = await client.call_and_deserialize("DescribeZones", {})
    except TencentCloudSDKException as err:
        assert False