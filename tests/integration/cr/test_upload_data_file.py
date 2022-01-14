import os

import pytest

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

from tencentcloud.cr.v20180321 import cr_client, models


def test_cr_upload_data_file_multipart():
    pytest.skip("ActionOffline")
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    client = cr_client.CrClient(cred, "ap-shenzhen-fsi")
    req = models.UploadDataFileRequest()
    req.Module = "Data"
    req.Operation = "Upload"
    req.FileName = "data.xlsx"
    curdir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(curdir, "data.xlsx"), "rb+") as f:
        req.File = f.read()
    try:
        resp = client.UploadDataFile(req)
    except TencentCloudSDKException as e:
        assert e.code == "FailedOperation.UploadDataError"
