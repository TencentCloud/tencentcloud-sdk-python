# -*- coding: utf-8 -*-
import json
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou")

    req = models.ChatStdRequest()
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "你好，可以讲个笑话吗"
    req.Messages = [msg]

    resp = client.ChatStd(req)

    full_content = ""
    for event in resp:
        print(event)
        data = json.loads(event['data'])
        for choice in data['Choices']:
            full_content += choice['Delta']['Content']

    print(full_content)

except TencentCloudSDKException as err:
    print(err)
