# -*- coding: utf8 -*-
import json
import os

from tencentcloud.common import credential, common_client
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry import StandardRetryer
from tencentcloud.common.profile.client_profile import ClientProfile


class StandardRetryCounter(StandardRetryer):
    def __init__(self, *args, **kwargs):
        super(StandardRetryCounter, self).__init__(*args, **kwargs)
        self.attempts = 0

    def on_retry(self, n, sleep, resp, err):
        self.attempts += 1


def test_standard_retryer_call_json():
    service = "cvm"
    version = "2017-03-12"
    action = "DescribeInstances"
    region = "ap-guangzhou"
    body = {"Limit": 10}

    cred = credential.Credential(os.environ.get("TENCENTCLOUD_SECRET_ID"), os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    cpf = ClientProfile()
    cpf.retryer = StandardRetryer()

    client = common_client.CommonClient(service, version, cred, region, cpf)

    resp = client.call_json(action, body)
    assert resp["Response"]["TotalCount"] >= 0


def test_standard_retryer_call_json_err():
    service = "cvm"
    version = "2017-03-12"
    action = "DescribeInstances"
    region = "ap-guangzhou"
    body = {"Limit": 10}
    max_attempts = 3

    cred = credential.Credential(os.environ.get("TENCENTCLOUD_SECRET_ID"), os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    cpf = ClientProfile()
    retryer = StandardRetryCounter(max_attempts=max_attempts, backoff_fn=lambda _: 0)
    cpf.retryer = retryer
    cpf.httpProfile.endpoint = "non-exist"

    client = common_client.CommonClient(service, version, cred, region, cpf)

    resp = None
    err = None
    try:
        resp = client.call_json(action, body)
    except TencentCloudSDKException as e:
        err = e

    assert resp is None
    assert err is not None
    assert isinstance(err, TencentCloudSDKException)
    assert retryer.attempts == max_attempts


def test_standard_retryer_call_sse():
    service = "hunyuan"
    version = "2023-09-01"
    action = "ChatCompletions"
    region = "ap-guangzhou"
    body = {"Model": "hunyuan-lite", "Messages": [{"Role": "user", "Content": "hi"}], "Stream": True}

    cred = credential.Credential(os.environ.get("TENCENTCLOUD_SECRET_ID"), os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    cpf = ClientProfile()
    cpf.retryer = StandardRetryer()

    client = common_client.CommonClient(service, version, cred, region, cpf)

    resp = client.call_sse(action, body)
    full_content = ""
    for event in resp:
        data = json.loads(event['data'])
        for choice in data['Choices']:
            full_content += choice['Delta']['Content']
    assert len(full_content) > 0


def test_standard_retryer_call_sse_err():
    service = "hunyuan"
    version = "2023-09-01"
    action = "ChatCompletions"
    region = "ap-guangzhou"
    body = {"Model": "hunyuan-lite", "Messages": [{"Role": "user", "Content": "hi"}], "Stream": True}
    max_attempts = 3

    cred = credential.Credential(os.environ.get("TENCENTCLOUD_SECRET_ID"), os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    cpf = ClientProfile()
    retryer = StandardRetryCounter(max_attempts=max_attempts, backoff_fn=lambda _: 0)
    cpf.retryer = retryer
    cpf.httpProfile.endpoint = "non-exist"

    client = common_client.CommonClient(service, version, cred, region, cpf)

    resp = None
    err = None
    try:
        resp = client.call_sse(action, body)
    except TencentCloudSDKException as e:
        err = e

    assert resp is None
    assert err is not None
    assert isinstance(err, TencentCloudSDKException)
    assert retryer.attempts == max_attempts
