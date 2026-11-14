import json
import os
import types

import pytest

from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models


def test_chat_completions():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "hunyuan.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = hunyuan_client.HunyuanClient(cred, "", clientProfile)

    req = models.ChatCompletionsRequest()
    params = {
        "Model": "hunyuan-pro",
        "Messages": [
            {
                "Role": "user",
                "Content": "你好啊，早上好"
            }
        ]
    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个ChatCompletionsResponse的实例，与请求对象对应
    resp = client.ChatCompletions(req)
    assert isinstance(resp, types.GeneratorType) is False

    req1 = models.ChatCompletionsRequest()
    params = {
        "Model": "hunyuan-pro",
        "Messages": [
            {
                "Role": "user",
                "Content": "你好啊，早上好"
            }
        ],
        "Stream": True
    }
    req1.from_json_string(json.dumps(params))

    resp = client.ChatCompletions(req1)
    assert isinstance(resp, types.GeneratorType) is True


def test_chat_completions_with_exception():
    with pytest.raises(TencentCloudSDKException):
        client = hunyuan_client.HunyuanClient(None, "", None)
        params = {}
        client.ChatCompletions(params)


def test_hunyuan_get_embedding():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.endpoint = "hunyuan.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = hunyuan_client.HunyuanClient(cred, "", clientProfile)

    req = models.GetEmbeddingRequest()
    params = {
        "Input": "你好"
    }
    req.from_json_string(json.dumps(params))

    resp = client.GetEmbedding(req)
    assert resp is not None


def test_hunyuan_get_embedding_with_exception():
    with pytest.raises(TencentCloudSDKException):
        client = hunyuan_client.HunyuanClient(None, "", None)
        params = {}
        client.GetEmbedding(params)


def test_hunyuan_get_token_count():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "hunyuan.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = hunyuan_client.HunyuanClient(cred, "", clientProfile)

    req = models.GetTokenCountRequest()
    params = {
        "Prompt": "你好"
    }
    req.from_json_string(json.dumps(params))

    resp = client.GetTokenCount(req)
    assert resp.TokenCount == 1
    assert resp.CharacterCount == 2
    assert resp.Tokens == ["你好"]


def test_hunyuan_get_token_count_with_exception():
    with pytest.raises(TencentCloudSDKException):
        client = hunyuan_client.HunyuanClient(None, "", None)
        params = {}
        client.GetTokenCount(params)


def test_submit_hunyuan_image_job():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    httpProfile = HttpProfile()
    httpProfile.endpoint = "hunyuan.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", clientProfile)

    req = models.SubmitHunyuanImageJobRequest()
    params = {
        "Prompt": "火山"
    }
    req.from_json_string(json.dumps(params))

    resp = client.SubmitHunyuanImageJob(req)
    assert resp is not None


def test_submit_hunyuan_image_job_with_exception():
    with pytest.raises(TencentCloudSDKException):
        client = hunyuan_client.HunyuanClient(None, "", None)
        params = {}
        client.SubmitHunyuanImageJob(params)
