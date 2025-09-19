# -*- coding: utf-8 -*-
import json
import os

import httpx
import pytest

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client_async, models

time_max = 60
time_min = 0.1


@pytest.mark.asyncio
async def test_request_timeout_max():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.reqTimeout = time_max
    httpProfile.endpoint = "cvm.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cvm_client_async.CvmClient(cred, "ap-guangzhou", clientProfile)

    req = models.DescribeZonesRequest()
    try:
        resp = await client.DescribeZones(req)
    except TencentCloudSDKException as err:
        assert False


@pytest.mark.asyncio
async def test_request_timeout_min():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.reqTimeout = time_min
    httpProfile.endpoint = "cvm.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cvm_client_async.CvmClient(cred, "ap-guangzhou", clientProfile)

    req = models.DescribeZonesRequest()
    try:
        resp = await client.DescribeZones(req)
        assert False, "request should fail because timeout"
    except httpx.ConnectTimeout:
        pass