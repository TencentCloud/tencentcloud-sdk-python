# -*- coding: utf8 -*-
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.cvm.v20170312 import cvm_client_async, models


@pytest.mark.skipif(not os.environ.get("TENCENTCLOUD_ROLE_ARN"),
                    reason="TENCENTCLOUD_ROLE_ARN env var not found")
@pytest.mark.asyncio
async def test_describe_instances():
    cred = credential.STSAssumeRoleCredential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"),
        os.environ.get("TENCENTCLOUD_ROLE_ARN"),
        "test")

    client = cvm_client_async.CvmClient(cred, "ap-guangzhou")
    req = models.DescribeInstancesRequest()
    resp = await client.DescribeInstances(req)
    assert resp.TotalCount >= 0


@pytest.mark.asyncio
async def test_describe_instances_with_empty_token():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"),
        "")

    client = cvm_client_async.CvmClient(cred, "ap-guangzhou")
    req = models.DescribeInstancesRequest()
    resp = await client.DescribeInstances(req)
    assert resp.TotalCount >= 0


@pytest.mark.asyncio
async def test_describe_instances_with_null_token():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"),
        None)

    client = cvm_client_async.CvmClient(cred, "ap-guangzhou")
    req = models.DescribeInstancesRequest()
    resp = await client.DescribeInstances(req)
    assert resp.TotalCount >= 0