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
import os
import json

from tencentcloud.common import common_client
from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException

try:
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    # 实例化要请求的common client对象，clientProfile是可选的。
    client = common_client.CommonClient("cls", '2020-10-16', cred, "ap-guangzhou")
    fpath = os.path.join(os.path.dirname(__file__), "binary.data")
    with open(fpath, "rb") as f:
        body = f.read()
    headers = {
        # 使用对应地域下真实存在的日志主题ID
        "X-CLS-TopicId": "f6c4fa6f-367a-4f14-8289-1ff6f77ed975",
        # 主题分区，https://cloud.tencent.com/document/product/614/39259
        # 取值00000000000000000000000000000000，ffffffffffffffffffffffffffffffff
        "X-CLS-HashKey": "0fffffffffffffffffffffffffffffff",
        # 压缩类型
        "X-CLS-CompressType": "",
    }
    # 接口参数作为headers json字典传入，二进制数据作为body字节传入
    # 得到的输出是json字典，请求失败将抛出异常
    print(client.call_octet_stream("UploadLog", headers, body))
except TencentCloudSDKException as err:
    print(err)
