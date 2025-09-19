# -*- coding: utf-8 -*-
"""
这是一个使用腾讯云通用客户端（CommonClient）异步 API 的示例。
它演示了如何使用通用客户端调用混元大模型的 ChatCompletions 接口，
以非流式（non-stream）方式进行对话，并获取完整的响应内容。
"""
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

import asyncio
import json
import os
import sys

from tencentcloud.common.common_client_async import CommonClient
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile


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
        # 这里使用默认配置，你也可以根据需要进行自定义，如设置超时时间。
        cpf = ClientProfile()
        # 流式接口可能耗时较长，因此将请求超时时间设置为 400 秒。
        cpf.httpProfile.reqTimeout = 400

        # 3. 设置自定义请求头（Headers）
        # 通用客户端支持在请求中指定自定义 HTTP Headers。
        # 这里的例子中设置了 X-TC-TraceId，可用于请求追踪。
        headers = {
            "X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca"
        }

        # 4. 实例化通用客户端（CommonClient）
        # 指定要请求的服务（"hunyuan"）、版本（"2023-09-01"）、凭证、地域和客户端配置。
        # 使用 'async with' 语法可以确保客户端在使用完毕后自动关闭连接。
        async with CommonClient("hunyuan", "2023-09-01", cred, "ap-shanghai", profile=cpf) as client:
            # 5. 构建请求参数
            # 将接口参数以 JSON 字典形式构建。
            # "Model": 指定要调用的模型。
            # "Messages": 定义对话内容，"Role" 为 "user" 表示用户输入，"Content" 为具体文本。
            # "Stream": 设置为 False 表示以非流式方式获取完整结果。
            req = {
                "Model": "hunyuan-standard",
                "Messages": [{
                    "Role": "user",
                    "Content": "你好，可以讲个笑话吗",
                }],
                "Stream": False,
            }

            # 6. 发起 API 调用并反序列化响应
            # 使用 `call_and_deserialize` 方法调用 ChatCompletions 接口。
            # 返回结果是一个 JSON 字典。
            resp = await client.call_and_deserialize("ChatCompletions", req, headers=headers)

            full_content = ""
            # 7. 处理响应结果
            if req["Stream"]:
                # 流式模式处理（仅作示例，本例中 Stream 为 False）
                async for event in resp:
                    data = json.loads(event['data'])
                    for choice in data['Choices']:
                        full_content += choice['Delta']['Content']
            else:
                # 非流式模式处理
                # 从返回的 JSON 字典中提取完整内容。
                full_content = resp["Choices"][0]["Message"]["Content"]

            # 8. 打印完整内容
            print(full_content)

    except TencentCloudSDKException as err:
        # 捕获并打印腾讯云 SDK 的异常，以便处理 API 调用中的错误。
        print(err)


# 9. 运行主函数
# 使用 asyncio.run() 来启动异步事件循环，并运行 main 函数。
asyncio.run(main())
