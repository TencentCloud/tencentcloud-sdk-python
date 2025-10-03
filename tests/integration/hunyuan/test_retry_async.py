# -*- coding: utf8 -*-
import json
import os

import httpx
import pytest

from tencentcloud.common import credential
from tencentcloud.common.retry_async import StandardRetryer, NoopRetryer
from tencentcloud.hunyuan.v20230901 import hunyuan_client_async, models
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

    client = hunyuan_client_async.HunyuanClient(cred, "ap-guangzhou", clientProfile)
    req = models.ChatCompletionsRequest()
    req.Model = "hunyuan-lite"
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "hi, tell me a joke !"
    req.Messages = [msg]
    req.Stream = True
    resp = await client.ChatCompletions(req)

    full_content = ""
    async for event in resp:
        data = json.loads(event['data'])
        for choice in data['Choices']:
            full_content += choice['Delta']['Content']
    assert len(full_content) > 0


@pytest.mark.asyncio
async def test_standard_retryer():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.retryer = StandardRetryer()

    client = hunyuan_client_async.HunyuanClient(cred, "ap-guangzhou", clientProfile)
    req = models.ChatCompletionsRequest()
    req.Model = "hunyuan-lite"
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "hi, tell me a joke about AI !"
    req.Messages = [msg]
    req.Stream = True
    resp = await client.ChatCompletions(req)

    full_content = ""
    async for event in resp:
        data = json.loads(event['data'])
        for choice in data['Choices']:
            full_content += choice['Delta']['Content']
    assert len(full_content) > 0


class StandardRetryCounter(StandardRetryer):
    def __init__(self, *args, **kwargs):
        super(StandardRetryCounter, self).__init__(*args, **kwargs)
        self.attempts = 0

    async def on_retry(self, n, sleep, resp, err):
        self.attempts += 1


@pytest.mark.asyncio
async def test_standard_retryer_err():
    max_attempts = 3
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.httpProfile.endpoint = "non-exist"
    async def backoff_fn(n):
        return 0
    retryer = StandardRetryCounter(max_attempts=max_attempts, backoff_fn=backoff_fn)
    clientProfile.retryer = retryer

    client = hunyuan_client_async.HunyuanClient(cred, "ap-guangzhou", clientProfile)
    req = models.ChatCompletionsRequest()
    req.Model = "hunyuan-lite"
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "hi, tell me a joke about AI !"
    req.Messages = [msg]
    req.Stream = True

    resp = None
    err = None
    try:
        resp = await client.ChatCompletions(req)
    except httpx.TransportError as e:
        err = e

    assert resp is None
    assert err is not None
    assert retryer.attempts == max_attempts