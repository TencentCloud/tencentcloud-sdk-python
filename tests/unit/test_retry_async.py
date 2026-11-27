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

from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry_async import StandardRetryer


@pytest.mark.asyncio
async def test_std_retry_recovers_after_failure():
    max_attempts = 5

    async def backoff_fn(n):
        return 0

    retryer = StandardRetryer(max_attempts=max_attempts, backoff_fn=backoff_fn)

    stats = {"attempts": 0}

    async def request_func():
        stats["attempts"] += 1
        if stats["attempts"] < 3:
            raise TencentCloudSDKException("ClientNetworkError", "")
        return "ok"

    assert await retryer.send_request(request_func) == "ok"
    assert stats["attempts"] == 3
