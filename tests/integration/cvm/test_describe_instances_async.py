# -*- coding: utf8 -*-
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.cvm.v20170312 import cvm_client_async, models


async def _test_describe_instances(http_method, sign_method, unsigned_payload=False):
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.reqMethod = http_method

    clientProfile = ClientProfile()
    clientProfile.signMethod = sign_method
    clientProfile.unsignedPayload = unsigned_payload
    clientProfile.httpProfile = httpProfile

    client = cvm_client_async.CvmClient(cred, "ap-guangzhou", clientProfile)
    req = models.DescribeInstancesRequest()
    fzone = models.Filter()
    fzone.Name = "zone"
    fzone.Values = ["ap-guangzhou-1", "ap-guangzhou-2"]
    fname = models.Filter()
    fname.Name = "instance-name"
    fname.Values = [u"中文", u"测试"]
    req.Filters = [fzone, fname]
    resp = await client.DescribeInstances(req)
    assert resp.TotalCount >= 0


@pytest.mark.asyncio
async def test_describe_instances_get_sha1():
    await _test_describe_instances("GET", "HmacSHA1")


@pytest.mark.asyncio
async def test_describe_instances_post_sha1():
    await _test_describe_instances("POST", "HmacSHA1")


@pytest.mark.asyncio
async def test_describe_instances_get_sha256():
    await _test_describe_instances("GET", "HmacSHA256")


@pytest.mark.asyncio
async def test_describe_instances_post_sha256():
    await _test_describe_instances("POST", "HmacSHA256")


@pytest.mark.asyncio
async def test_describe_instances_get_tc3():
    await _test_describe_instances("GET", "TC3-HMAC-SHA256")


@pytest.mark.asyncio
async def test_describe_instances_post_tc3():
    await _test_describe_instances("POST", "TC3-HMAC-SHA256")


@pytest.mark.asyncio
async def test_describe_instances_get_tc3_unsigned_payload():
    await _test_describe_instances("GET", "TC3-HMAC-SHA256", True)


@pytest.mark.asyncio
async def test_describe_instances_post_tc3_unsigned_payload():
    await _test_describe_instances("POST", "TC3-HMAC-SHA256", True)