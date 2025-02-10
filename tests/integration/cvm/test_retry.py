# -*- coding: utf8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry import StandardRetryer, NoopRetryer
from tencentcloud.cvm.v20170312 import cvm_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


def test_noop_retryer():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.retryer = NoopRetryer()

    client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)
    req = models.DescribeInstancesRequest()
    fzone = models.Filter()
    fzone.Name = "zone"
    fzone.Values = ["ap-guangzhou-1", "ap-guangzhou-2"]
    fname = models.Filter()
    fname.Name = "instance-name"
    fname.Values = [u"中文", u"测试"]
    req.Filters = [fzone, fname]
    resp = client.DescribeInstances(req)
    assert resp.TotalCount >= 0


def test_standard_retryer():
    max_attempts = 3
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.retryer = StandardRetryer(max_attempts=max_attempts)

    client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)
    req = models.DescribeInstancesRequest()
    fzone = models.Filter()
    fzone.Name = "zone"
    fzone.Values = ["ap-guangzhou-1", "ap-guangzhou-2"]
    fname = models.Filter()
    fname.Name = "instance-name"
    fname.Values = [u"中文", u"测试"]
    req.Filters = [fzone, fname]
    resp = client.DescribeInstances(req)
    assert resp.TotalCount >= 0


class StandardRetryCounter(StandardRetryer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attempts = 0

    def on_retry(self, n, sleep, resp, err):
        self.attempts += 1


def test_standard_retryer_attempts():
    max_attempts = 3
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.endpoint = "not-exists-endpoint"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    retryer = StandardRetryCounter(max_attempts=max_attempts)
    clientProfile.retryer = retryer

    client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)
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
        resp = client.DescribeInstances(req)
    except TencentCloudSDKException as e:
        err = e

    assert resp is None
    assert err is not None
    assert isinstance(err, TencentCloudSDKException)
    assert retryer.attempts == max_attempts
