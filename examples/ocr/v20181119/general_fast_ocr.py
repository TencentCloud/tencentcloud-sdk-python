import os

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
try:
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)

    req = models.GeneralFastOCRRequest()
    req.ImageUrl = "https://mc.qcloudimg.com/static/img/6d4f1676deba26377d4303a462ca5074/image.png"
    resp = client.GeneralFastOCR(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
