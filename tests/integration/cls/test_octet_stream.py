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

import pytest

from tencentcloud.common import credential
from tencentcloud.common import common_client
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


def test_octet_stream_req_default():
    profile = ClientProfile()
    try:
        _test_octet_stream_req(profile)
    except TencentCloudSDKException as e:
        assert e.code in ("OperationDenied",  # cls service is not open on console
                          "ResourceNotFound.TopicNotExist")  # topic-id is invalid


def test_octet_stream_req_get():
    http_profile = HttpProfile(reqMethod="GET")
    profile = ClientProfile(httpProfile=http_profile)
    try:
        _test_octet_stream_req(profile)
    except TencentCloudSDKException as e:
        assert e.code == "ClientError"


def test_octet_stream_req_signature_v1():
    profile = ClientProfile(signMethod="HmacSHA1")
    try:
        _test_octet_stream_req(profile)
    except TencentCloudSDKException as e:
        assert e.code == "ClientError"

    profile = ClientProfile(signMethod="HmacSHA256")
    try:
        _test_octet_stream_req(profile)
    except TencentCloudSDKException as e:
        assert e.code == "ClientError"


def _test_octet_stream_req(profile):
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    client = common_client.CommonClient(
        "cls", '2020-10-16', cred, "ap-guangzhou", profile=profile)
    fpath = os.path.join(os.path.dirname(__file__), "binary.data")
    with open(fpath, "rb") as f:
        body = f.read()
    headers = {
        "X-CLS-TopicId": "f6c4fa6f-367a-4f14-8289-1ff6f77ed975",
        "X-CLS-HashKey": "0fffffffffffffffffffffffffffffff",
        "X-CLS-CompressType": "",
    }
    rsp = client.call_octet_stream("UploadLog", headers, body)
