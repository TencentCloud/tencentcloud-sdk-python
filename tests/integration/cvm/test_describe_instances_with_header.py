# -*- coding: utf8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.cvm.v20170312 import cvm_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


def _test_describe_instances(http_method, sign_method, unsigned_payload=False):
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.reqMethod = http_method

    clientProfile = ClientProfile()
    clientProfile.signMethod = sign_method
    clientProfile.unsignedPayload = unsigned_payload
    clientProfile.httpProfile = httpProfile

    client = cvm_client.CvmClient(cred, "ap-guangzhou", clientProfile)
    req = models.DescribeInstancesRequest()
    header = {
        "X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca",
    }

    fzone = models.Filter()
    fzone.Name = "zone"
    fzone.Values = ["ap-guangzhou-1", "ap-guangzhou-2"]
    fname = models.Filter()
    fname.Name = "instance-name"
    fname.Values = [u"中文", u"测试"]
    req.Filters = [fzone, fname]
    resp = client.DescribeInstances(req, header)
    assert resp.TotalCount >= 0


def test_describe_instances_get_sha1():
    _test_describe_instances("GET", "HmacSHA1")


def test_describe_instances_post_sha1():
    _test_describe_instances("POST", "HmacSHA1")


def test_describe_instances_get_sha256():
    _test_describe_instances("GET", "HmacSHA256")


def test_describe_instances_post_sha256():
    _test_describe_instances("POST", "HmacSHA256")


def test_describe_instances_get_tc3():
    _test_describe_instances("GET", "TC3-HMAC-SHA256")


def test_describe_instances_post_tc3():
    _test_describe_instances("POST", "TC3-HMAC-SHA256")


def test_describe_instances_get_tc3_unsigned_payload():
    _test_describe_instances("GET", "TC3-HMAC-SHA256", True)


def test_describe_instances_post_tc3_unsigned_payload():
    _test_describe_instances("POST", "TC3-HMAC-SHA256", True)
