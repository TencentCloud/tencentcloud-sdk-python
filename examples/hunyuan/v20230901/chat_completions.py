# -*- coding: utf-8 -*-
import json
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    cpf = ClientProfile()
    # 预先建立连接可以降低访问延迟
    cpf.httpProfile.pre_conn_pool_size = 3
    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", cpf)

    req = models.ChatCompletionsRequest()
    req.Model = "hunyuan-standard"
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "你好，可以讲个笑话吗"
    req.Messages = [msg]

    # hunyuan ChatCompletions/ChatPro 同时支持 stream 和非 stream 的情况
    req.Stream = True
    resp = client.ChatCompletions(req)

    full_content = ""
    if req.Stream:  # stream 示例
        for event in resp:
            print(event["data"])
            data = json.loads(event['data'])
            for choice in data['Choices']:
                full_content += choice['Delta']['Content']
    else:  # 非 stream 示例
        # 通过 Stream=False 参数来指定非 stream 协议, 一次性拿到结果
        full_content = resp.Choices[0].Message.Content

    print(full_content)

except TencentCloudSDKException as err:
    print(err)
