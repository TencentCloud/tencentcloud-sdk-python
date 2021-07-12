# -*- coding: utf8 -*-
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.cvm.v20170312 import cvm_client, models


@pytest.mark.skipif(not os.environ.get("TENCENTCLOUD_ROLE_ARN"),
                    reason="TENCENTCLOUD_ROLE_ARN env var not found")
def test_describe_instances():
    cred = credential.STSAssumeRoleCredential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"),
        os.environ.get("TENCENTCLOUD_ROLE_ARN"),
        "test")

    client = cvm_client.CvmClient(cred, "ap-guangzhou")
    req = models.DescribeInstancesRequest()
    resp = client.DescribeInstances(req)
    assert resp.TotalCount >= 0
