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
这是一个使用腾讯云CVM SDK异步API的示例脚本。
它演示了如何使用异步方式查询位于上海地域指定可用区的云服务器实例列表。
"""
import asyncio
import os
import sys

from tencentcloud.common import credential, retry_async
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.cvm.v20170312 import cvm_client_async, models


async def main():
    """
    主函数，异步执行查询云服务器实例的操作。
    """
    try:
        # 1. 创建认证凭证（Credential）
        # 从环境变量中获取密钥ID和密钥Key，这是访问云API的必需凭证。
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        # 2. 创建客户端配置（ClientProfile）
        # 用于配置客户端的行为，如重试策略
        cpf = ClientProfile()
        # 启用异步重试功能，设置最大重试次数为3次
        # 如果请求失败，SDK会自动重试
        cpf.retryer = retry_async.StandardRetryer(max_attempts=3)

        # 3. 创建异步CVM客户端（CvmClient）
        # "ap-shanghai"指定了服务所在的地域
        # 使用"async with"语法可以确保客户端在使用完毕后自动关闭连接
        async with cvm_client_async.CvmClient(cred, "ap-shanghai", cpf) as client:
            # 4. 开启调试日志
            # 将SDK的调试日志输出到标准输出，这对于问题排查很有帮助
            client.set_stream_logger(sys.stdout)

            # 5. 创建并设置请求对象（Request）
            # 创建一个DescribeInstancesRequest请求，用于查询实例列表
            req = models.DescribeInstancesRequest()

            # 6. 设置过滤条件
            # 创建一个Filter对象，并设置其名称为"zone"，值为上海的两个可用区
            # 这将只查询指定可用区内的CVM实例
            resp_filter = models.Filter()
            resp_filter.Name = "zone"
            resp_filter.Values = ["ap-shanghai-1", "ap-shanghai-2"]
            req.Filters = [resp_filter]

            # 7. 发起异步API调用
            # 调用DescribeInstances方法，并使用'await'等待其返回结果。
            resp = await client.DescribeInstances(req)

            # 8. 打印结果
            # 将返回的JSON对象格式化并打印出来，方便阅读。
            print(resp.to_json_string(indent=2))

    except TencentCloudSDKException as err:
        # 捕获并打印腾讯云SDK的异常，以便处理API调用中的错误。
        print(err)


# 9. 运行主函数
# 使用 asyncio.run() 来启动异步事件循环，并运行 main 函数。
asyncio.run(main())
