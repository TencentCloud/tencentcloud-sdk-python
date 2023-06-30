# Copyright (c) 2018 Tencent Ltd.
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
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.http_profile import HttpProfile


class ClientProfile(object):
    unsignedPayload = False

    def __init__(self, signMethod=None, httpProfile=None, language="zh-CN",
                 disable_region_breaker=True, region_breaker_profile=None):
        """SDK profile.

        :param signMethod: The signature method, valid choice: HmacSHA1, HmacSHA256, TC3-HMAC-SHA256
        :type signMethod: str
        :param httpProfile: The http profile
        :type httpProfile: :class:`HttpProfile`
        :param language: Valid choice: en-US, zh-CN.
        :type language: str
        :param disable_region_breaker: Switch of region breaker.
        :type disable_region_breaker: bool
        :param region_breaker_profile: The region breaker profile.
        :type region_breaker_profile: :class:`RegionBreakerProfile`
        """
        self.httpProfile = HttpProfile() if httpProfile is None else httpProfile
        self.signMethod = "TC3-HMAC-SHA256" if signMethod is None else signMethod
        valid_language = ["zh-CN", "en-US"]
        if language not in valid_language:
            raise TencentCloudSDKException("ClientError", "Language invalid, choices: %s" % valid_language)
        self.language = language
        self.disable_region_breaker = disable_region_breaker
        self.region_breaker_profile = region_breaker_profile
        if not self.disable_region_breaker and self.region_breaker_profile is None:
            self.region_breaker_profile = RegionBreakerProfile()


class RegionBreakerProfile(object):

    def __init__(self, backup_endpoint="ap-guangzhou.tencentcloudapi.com",
                 max_fail_num=5,
                 max_fail_percent=0.75,
                 window_interval=60*5,
                 timeout=60,
                 max_requests=5):
        """RegionBreaker profile.

        :param backup_endpoint: Backup region of endpoint, default ap-guangzhou.tencentcloudapi.com.
        :type backup_endpoint: str
        :param max_fail_num: Max failure to trigger breaker, default 5.
        :type max_fail_num: int
        :param max_fail_percent: Max failure percent to trigger breaker, default 0.75.
        :type max_fail_percent: float
        :param window_interval: Decides when to reset counter if the state is StateClosed, default 5 minutes.
        :type window_interval: int
        :param timeout: Decides when to turn StateOpen to StateHalfOpen, default 1 minutes.
        :type timeout: int
        :param max_requests: Decides when to turn StateHalfOpen to StateClosed, default 5 successful requests.
        :type timeout: int
        """
        self.backup_endpoint = backup_endpoint
        if not self.check_endpoint():
            raise TencentCloudSDKException("ClientError", "the format of `backup_endpoint` must be tencentcloudapi.com "
                                                          "or ${region}.tencentcloudapi.com")
        self.max_fail_num = max_fail_num
        self.max_fail_percent = max_fail_percent
        if self.max_fail_percent < 0 or self.max_fail_percent > 1:
            raise TencentCloudSDKException("ClientError", "max fail percent must be set between 0 and 1")
        self.window_interval = window_interval
        self.timeout = timeout
        self.max_requests = max_requests

    def check_endpoint(self):
        endpoint_split = self.backup_endpoint.split(".")
        if len(endpoint_split) != 3 and len(endpoint_split) != 2:
            return False
        if endpoint_split[-2] != "tencentcloudapi" or endpoint_split[-1] != "com":
            return False
        if len(endpoint_split) == 3:
            region = endpoint_split[0]
            if len(region.split("-")) != 2:
                return False
        return True

