# -*- coding: utf-8 -*-

import os

from tencentcloud.cls.v20201016 import cls_client
from tencentcloud.cls.v20201016 import models
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def main():
    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        client = cls_client.ClsClient(cred, "ap-chongqing")
        req = models.SearchLogRequest()
        req.TopicId = "TopicId"
        req.From = 1626192000000 # timestamp for ms
        req.To = 1626278400000   # timestamp for ms
        req.Query = ""
        req.Limit = 100
        resp = client.SearchLog(req)
        print(resp)
    except TencentCloudSDKException as err:
        print(err)

if __name__ == "__main__":
    main()
