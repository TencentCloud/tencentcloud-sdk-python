# -*- coding: utf-8 -*-
# Copyright 2017-2021 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
这是一个使用腾讯云混元大模型 SDK 异步 API 的示例。
该脚本演示了如何以流式（stream）方式调用 ChatCompletions 接口，
实现与混元大模型的对话，并逐步获取返回的内容。
"""
import asyncio
import json
import os
import sys

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.hunyuan.v20230901 import hunyuan_client_async, models


async def main():
    """
    主函数，异步执行与混元大模型的对话。
    """
    try:
        # 1. 创建认证凭证（Credential）
        # 从环境变量中获取密钥 ID 和密钥 Key，这是访问云 API 的必需凭证。
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        # 2. 创建客户端配置（ClientProfile）
        cpf = ClientProfile()
        # 流式接口可能耗时较长，因此将请求超时时间设置为 400 秒。
        cpf.httpProfile.reqTimeout = 400

        # 3. 创建异步 HunyuanClient 客户端
        # 指定服务所在的地域为“ap-guangzhou”。
        # 使用 'async with' 语法可以确保客户端在使用完毕后自动关闭连接。
        async with hunyuan_client_async.HunyuanClient(cred, "ap-guangzhou", cpf) as client:
            # 4. 开启调试日志
            # 将 SDK 的调试日志输出到标准输出，这对于问题排查很有帮助。
            client.set_stream_logger(sys.stdout)

            # 5. 创建并设置请求对象（Request）
            req = models.ChatCompletionsRequest()
            # 指定要使用的模型，例如“hunyuan-standard”。
            req.Model = "hunyuan-standard"

            # 6. 设置对话消息
            # 创建一个 Message 对象，角色为“user”，内容为用户的提问。
            msg = models.Message()
            msg.Role = "user"
            msg.Content = "你好，可以讲个笑话吗"
            req.Messages = [msg]

            # 7. 指定为流式 API 调用
            # hunyuan ChatCompletions 同时支持流式和非流式两种模式。
            # 将 Stream 参数设置为 True，表示以流式方式获取响应。
            req.Stream = True
            # 发起异步 API 调用，并使用 'await' 等待其返回结果。
            resp = await client.ChatCompletions(req)

            full_content = ""
            # 8. 处理流式响应
            if req.Stream:
                # 迭代异步响应流，逐个处理返回的事件。
                async for event in resp:
                    # 解析每个事件的 JSON 数据。
                    data = json.loads(event['data'])
                    for choice in data['Choices']:
                        # 拼接每个片段的内容，逐步构建完整的响应。
                        full_content += choice['Delta']['Content']
            # 9. 处理非流式响应（仅作示例）
            else:
                # 当 Stream=False 时，一次性获取完整的响应内容。
                full_content = resp.Choices[0].Message.Content

            # 10. 打印完整内容
            print(full_content)

    except TencentCloudSDKException as err:
        # 捕获并打印腾讯云 SDK 的异常，以便处理 API 调用中的错误。
        print(err)


# 11. 运行主函数
# 使用 asyncio.get_event_loop().run_until_complete(main()) 来启动异步事件循环，并运行 main 函数。
asyncio.get_event_loop().run_until_complete(main())
