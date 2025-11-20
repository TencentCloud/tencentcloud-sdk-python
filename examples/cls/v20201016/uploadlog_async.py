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
from tencentcloud.cls.v20201016 import cls_client_async, models
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

        cred = credential.Credential(
            os.environ.get("TENCENTCLOUD_SECRET_ID"),
            os.environ.get("TENCENTCLOUD_SECRET_KEY"))


        cpf = ClientProfile()

        async with cls_client_async.ClsClient(cred, region, cpf) as client:
            client.set_stream_logger(sys.stdout)

            req = models.UploadLogRequest()
            req.TopicId = topic_id
            req.HashKey = hash_key
            req.CompressType = compress_type
            # 使用 pb 库生成二进制格式的日志数据。
            body = pb.pb_gen(1, 1)

            if compress_type == "lz4":
                # pip install lz4
                from lz4.block import compress
                body = compress(body)

            resp = await client.UploadLog(req, body=body)

            print("%s" % resp)

    except TencentCloudSDKException as err:
        # 捕获并打印腾讯云 SDK 的异常，以便处理 API 调用中的错误。
        print("%s" % err)


asyncio.get_event_loop().run_until_complete(main())
