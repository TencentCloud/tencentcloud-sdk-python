# -*- coding: utf-8 -*-
#
# Copyright 1999-2017 Tencent Ltd.
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

from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


class CommonClient(AbstractClient):
    """General client for all products.

     With CommonClient, you only need to install the tencentcloud-sdk-python-common package to access APIs of all products.
     See GitHub examples for usage details: https://github.com/TencentCloud/tencentcloud-sdk-python/tree/master/examples/common_client

    :param service: Product name
    :type service: str
    :param version: Version of API
    :type version: str
    :param credential: Request credential
    :type credential: tencentcloud.common.credential.Credential or tencentcloud.common.credential.STSAssumeRoleCredential or None
    :param region: Request region
    :type region: str
    :param profile: Request SDK profile
    :type profile: tencentcloud.common.profile.client_profile.ClientProfile
    """

    def __init__(self, service, version, credential, region, profile=None):
        if region is None or version is None or service is None:
            raise TencentCloudSDKException("CommonClient Parameter Error, "
                                           "credential region version service all required.")
        self._apiVersion = version
        self._service = service
        super(CommonClient, self).__init__(credential, region, profile)
