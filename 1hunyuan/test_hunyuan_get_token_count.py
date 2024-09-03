import json
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models


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
