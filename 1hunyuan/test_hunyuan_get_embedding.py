import json
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models


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
