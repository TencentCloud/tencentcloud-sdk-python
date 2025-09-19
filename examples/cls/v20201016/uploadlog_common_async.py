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
该脚本演示了如何向腾讯云日志服务（CLS）上传日志数据，
并处理 LZ4 压缩和自定义协议头。
"""
import asyncio
import os
import sys

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common import common_client_async
from tencentcloud.common.profile.client_profile import ClientProfile
import pb


async def main():
    """
    主函数，异步执行日志上传操作。
    """
    try:
        # 1. 设置配置参数
        compress_type = ""  # 压缩方式，目前只支持 "lz4"。空字符串表示不压缩。
        region = "ap-guangzhou"  # 服务的地域，需要根据你的实际情况填写。
        # CLS 的 Topic ID，用于指定日志上传到哪个主题。
        # 注意：这里需要使用实际的 Topic ID，而不是 Topic 名称。
        topic_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        # Hash Key 是一个可选参数，用于指定日志分发到 CLS 的哪个分区。
        hash_key = ""

        # 2. 创建认证凭证（Credential）
        # 优先从环境变量中获取密钥，以确保安全。
        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))

        # 3. 创建客户端配置（ClientProfile）
        cpf = ClientProfile()

        # 4. 实例化通用客户端（CommonClient）
        # 指定服务（"cls"）、版本（"2020-10-16"）、凭证、地域和客户端配置。
        # 使用 'async with' 语法可以确保客户端在使用完毕后自动关闭连接。
        async with common_client_async.CommonClient("cls", '2020-10-16', cred, region, cpf) as client:
            # 5. 开启调试日志
            client.set_stream_logger(sys.stdout)

            # 6. 生成请求正文
            # 使用 pb 库生成二进制格式的日志数据。
            body = pb.pb_gen(1, 1)

            # 7. 处理数据压缩
            # 如果配置了 compress_type 为 "lz4"，则对正文进行压缩。
            if compress_type == "lz4":
                from lz4.block import compress
                body = compress(body)

            # 8. 设置协议头
            # CLS 的自定义协议需要特定的请求头来处理 Topic ID、Hash Key 和压缩类型。
            headers = {
                "X-CLS-TopicId": topic_id,
                "X-CLS-HashKey": hash_key,
                "X-CLS-CompressType": compress_type,
            }

            # 9. 设置上传选项
            # 日志上传接口是一个二进制流协议，需要指定 IsOctetStream=True。
            opts = {
                "IsOctetStream": True,
            }

            # 10. 发起 API 调用
            # 调用 "UploadLog" 接口，并传入请求正文、协议头和上传选项。
            resp = await client.call_and_deserialize("UploadLog", params=body, headers=headers, opts=opts)

            # 11. 打印回包
            # 输出服务器返回的 JSON 格式字符串，用于确认日志上传结果。
            print("%s" % resp)

    except TencentCloudSDKException as err:
        # 捕获并打印腾讯云 SDK 的异常，以便处理 API 调用中的错误。
        print("%s" % err)


# 12. 运行主函数
# 使用 asyncio.run() 启动异步事件循环。
asyncio.run(main())
