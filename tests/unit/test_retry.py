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
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry import StandardRetryer


def test_std_retry_err_code():
    ecs = [
        "ClientNetworkError",
        "ServerNetworkError",
        "RequestLimitExceeded",
        "RequestLimitExceeded.UinLimitExceeded",
        "RequestLimitExceeded.GlobalRegionUinLimitExceeded",
    ]

    max_attempts = 3

    for ec in ecs:
        retryer = StandardRetryer(max_attempts=max_attempts, backoff_fn=lambda n: 0)

        stats = {"attempts": 1}

        def request_func():
            stats["attempts"] += 1
            raise TencentCloudSDKException(ec, "")

        resp = None
        err = None
        try:
            resp = retryer.send_request(request_func)
        except Exception as e:
            err = e

        assert resp is None
        assert err is not None
        assert isinstance(err, TencentCloudSDKException)
        assert err.get_code() == ec
        assert stats["attempts"] == max_attempts + 1
