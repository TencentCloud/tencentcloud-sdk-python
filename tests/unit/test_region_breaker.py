# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
import pytest

from tencentcloud.common import credential
from tencentcloud.common.common_client import CommonClient
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.retry import StandardRetryer


@pytest.mark.parametrize("disable_region_breaker", [True, False])
def test_network_error_is_raised_and_retried(disable_region_breaker):
    max_attempts = 3
    retryer = StandardRetryer(max_attempts=max_attempts, backoff_fn=lambda n: 0)
    cp = ClientProfile(disable_region_breaker=disable_region_breaker, retryer=retryer)
    cred = credential.Credential("mock-id", "mock-key")
    client = CommonClient("cvm", "2017-03-12", cred, "ap-guangzhou", profile=cp)

    stats = {"attempts": 0}

    def send_request(req):
        stats["attempts"] += 1
        raise TencentCloudSDKException("ClientNetworkError", "connection refused")

    client.request.send_request = send_request

    with pytest.raises(TencentCloudSDKException) as e:
        client.call_json("DescribeRegions", {})
    assert e.value.get_code() == "ClientNetworkError"
    assert stats["attempts"] == max_attempts
    if not disable_region_breaker:
        assert client.circuit_breaker.counter.failures == max_attempts
