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
这是一个使用腾讯云通用客户端（CommonClient）异步 API 的示例。
它演示了如何使用通用客户端调用任意服务和版本下的 API，
例如查询 CVM 云服务器实例列表，并自定义请求头。
"""
import asyncio
import os

from tencentcloud.common.common_client_async import CommonClient
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile


async def main():
    """
    主函数，异步执行通用客户端的 API 调用。
    """
    try:
        # 1. 创建认证凭证（Credential）
        # 从环境变量中获取密钥 ID 和密钥 Key，这是访问云 API 的必需凭证。
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        # 2. 创建客户端配置（ClientProfile）
        # 这里使用默认配置，也可以根据需要进行自定义。
        cpf = ClientProfile()

        # 3. 设置自定义请求头（Headers）
        # 通用客户端支持在请求中指定自定义 HTTP Headers。
        # 这里的例子中设置了 X-TC-TraceId，可用于请求追踪。
        headers = {
            "X-TC-TraceId": "ffe0c072-8a5d-4e17-8887-a8a60252abca"
        }

        # 4. 实例化通用客户端（CommonClient）
        # 指定要请求的服务（"cvm"）、版本（"2017-03-12"）、凭证、地域和客户端配置。
        # 使用 'async with' 语法可以确保客户端在使用完毕后自动关闭连接。
        async with CommonClient("cvm", "2017-03-12", cred, "ap-shanghai", profile=cpf) as client:
            # 5. 调用 API 并反序列化响应
            # 使用 `call_and_deserialize` 方法，将接口参数以 JSON 字典形式传入。
            # 返回的结果也是一个 JSON 字典。
            # 请求失败时会抛出异常。
            # headers 参数是可选的。
            req = {"Limit": 10}

            resp = await client.call_and_deserialize("DescribeInstances", req, headers=headers)

            print(resp)

    except TencentCloudSDKException as err:
        # 捕获并打印腾讯云 SDK 的异常，以便处理 API 调用中的错误。
        print(err)


# 6. 运行主函数
# 使用 asyncio.get_event_loop().run_until_complete(main()) 来启动异步事件循环，并运行 main 函数。
asyncio.get_event_loop().run_until_complete(main())
