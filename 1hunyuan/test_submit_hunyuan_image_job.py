import json
import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models


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
