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
