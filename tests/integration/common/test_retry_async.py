# -*- coding: utf8 -*-
import json
import os

import httpx
import pytest

from tencentcloud.common import credential, common_client_async
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry_async import StandardRetryer
from tencentcloud.common.profile.client_profile import ClientProfile


class StandardRetryCounter(StandardRetryer):
    def __init__(self, *args, **kwargs):
        super(StandardRetryCounter, self).__init__(*args, **kwargs)
        self.attempts = 0

    async def on_retry(self, n, sleep, resp, err):
        self.attempts += 1


@pytest.mark.asyncio
async def test_standard_retryer_call_json():
    service = "cvm"
    version = "2017-03-12"
    action = "DescribeInstances"
    region = "ap-guangzhou"
    body = {"Limit": 10}

    cred = credential.Credential(os.environ.get("TENCENTCLOUD_SECRET_ID"), os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    cpf = ClientProfile()
    cpf.retryer = StandardRetryer()

    client = common_client_async.CommonClient(service, version, cred, region, cpf)

    resp = await client.call_and_deserialize(action, body)
    assert resp["Response"]["TotalCount"] >= 0

