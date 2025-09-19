# -*- coding: utf8 -*-
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry import StandardRetryer, NoopRetryer
from tencentcloud.cvm.v20170312 import cvm_client_async, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


@pytest.mark.asyncio
async def test_noop_retryer():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.retryer = NoopRetryer()

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
async def test_standard_retryer():
    max_attempts = 3
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.retryer = StandardRetryer(max_attempts=max_attempts)

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


class StandardRetryCounter(StandardRetryer):
    def __init__(self, *args, **kwargs):
        super(StandardRetryCounter, self).__init__(*args, **kwargs)
        self.attempts = 0

    async def on_retry(self, n, sleep, resp, err):
        self.attempts += 1


@pytest.mark.asyncio
async def test_standard_retryer_attempts():
    max_attempts = 3
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.endpoint = "not-exist"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    async def backoff_fn(n):
        return 0
    retryer = StandardRetryCounter(max_attempts=max_attempts, backoff_fn=backoff_fn)
    clientProfile.retryer = retryer

    client = cvm_client_async.CvmClient(cred, "ap-guangzhou", clientProfile)
    req = models.DescribeInstancesRequest()
    fzone = models.Filter()
    fzone.Name = "zone"
    fzone.Values = ["ap-guangzhou-1", "ap-guangzhou-2"]
    fname = models.Filter()
    fname.Name = "instance-name"
    fname.Values = [u"中文", u"测试"]
    req.Filters = [fzone, fname]

    resp = None
    err = None
    try:
        resp = await client.DescribeInstances(req)
    except TencentCloudSDKException as e:
        err = e

    assert resp is None
    assert err is not None
    assert isinstance(err, TencentCloudSDKException)
    assert retryer.attempts == max_attempts