# -*- coding: utf-8 -*-
import asyncio
import json
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client_async, models


async def main():
    try:
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        cpf = ClientProfile()
        cpf.httpProfile.reqTimeout = 400  # 流式接口可能耗时较长
        client = hunyuan_client_async.HunyuanClient(cred, "ap-guangzhou", cpf)

        req = models.ChatCompletionsRequest()
        req.Model = "hunyuan-standard"
        msg = models.Message()
        msg.Role = "user"
        msg.Content = "你好，可以讲个笑话吗"
        req.Messages = [msg]

        # hunyuan ChatCompletions 同时支持 stream 和非 stream 的情况
        req.Stream = True
        resp = await client.ChatCompletions(req)

        full_content = ""
        if req.Stream:  # stream 示例
            async for event in resp:
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


asyncio.run(main())
