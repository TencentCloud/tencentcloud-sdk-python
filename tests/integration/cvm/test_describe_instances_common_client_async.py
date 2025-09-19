# -*- coding: utf8 -*-
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.common_client_async import CommonClient


@pytest.mark.asyncio
async def test_describe_instances():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    client = CommonClient("cvm", '2017-03-12', cred, "ap-shanghai")
    rsp = await client.call_json("DescribeInstances", {"Limit": 10})
    assert rsp["Response"]["TotalCount"] <= 10