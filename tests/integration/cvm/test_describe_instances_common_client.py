# -*- coding: utf8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.common_client import CommonClient

def test_describe_instances():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    client = CommonClient("cvm", '2017-03-12', cred, "ap-shanghai")
    rsp = client.call_json("DescribeInstances", {"Limit": 10})
    assert rsp["Response"]["TotalCount"] <= 10
