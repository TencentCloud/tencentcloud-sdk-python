# -*- coding: utf8 -*-
import json
import os

from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry import StandardRetryer, NoopRetryer
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models
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

    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", clientProfile)
    req = models.ChatCompletionsRequest()
    req.Model = "hunyuan-lite"
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "hi, tell me a joke !"
    req.Messages = [msg]
    req.Stream = True
    resp = client.ChatCompletions(req)

    full_content = ""
    for event in resp:
        data = json.loads(event['data'])
        for choice in data['Choices']:
            full_content += choice['Delta']['Content']
    assert len(full_content) > 0


def test_standard_retryer():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.retryer = StandardRetryer()

    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", clientProfile)
    req = models.ChatCompletionsRequest()
    req.Model = "hunyuan-lite"
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "hi, tell me a joke about AI !"
    req.Messages = [msg]
    req.Stream = True
    resp = client.ChatCompletions(req)

    full_content = ""
    for event in resp:
        data = json.loads(event['data'])
        for choice in data['Choices']:
            full_content += choice['Delta']['Content']
    assert len(full_content) > 0


class StandardRetryCounter(StandardRetryer):
    def __init__(self, *args, **kwargs):
        super(StandardRetryCounter, self).__init__(*args, **kwargs)
        self.attempts = 0

    def on_retry(self, n, sleep, resp, err):
        self.attempts += 1


def test_standard_retryer_err():
    max_attempts = 3
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    clientProfile.httpProfile.endpoint = "non-exist"
    retryer = StandardRetryCounter(max_attempts=max_attempts, backoff_fn=lambda _: 0)
    clientProfile.retryer = retryer

    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", clientProfile)
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
        resp = client.ChatCompletions(req)
    except TencentCloudSDKException as e:
        err = e

    assert resp is None
    assert err is not None
    assert isinstance(err, TencentCloudSDKException)
    assert retryer.attempts == max_attempts
