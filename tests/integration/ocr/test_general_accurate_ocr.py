import base64
import os
import sys

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

from tencentcloud.ocr.v20181119 import ocr_client
from tencentcloud.ocr.v20181119 import models


def test_iai_create_person():
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    client = ocr_client.OcrClient(cred, "ap-guangzhou")
    req = models.GeneralAccurateOCRRequest()
    dirname = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(dirname, "ocr.png"), "rb") as f:
        if sys.version_info[0] == 2:
            # py2 base64 returns str
            content = base64.b64encode(f.read())
        else:
            # py3 base64 returns byte but sdk requires string, so decode it
            content = base64.b64encode(f.read()).decode('utf-8')
    req.ImageBase64 = content
    try:
        resp = client.GeneralAccurateOCR(req)
    except TencentCloudSDKException as e:
        # expected behavior because ocr requires high solution pictures
        assert e.code == 'FailedOperation.UnOpenError'
