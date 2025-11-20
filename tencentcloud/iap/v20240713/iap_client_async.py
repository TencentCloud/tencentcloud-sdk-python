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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.iap.v20240713 import models
from typing import Dict


class IapClient(AbstractClient):
    _apiVersion = '2024-07-13'
    _endpoint = 'iap.tencentcloudapi.com'
    _service = 'iap'

    async def CreateIAPUserOIDCConfig(
            self,
            request: models.CreateIAPUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.CreateIAPUserOIDCConfigResponse:
        """
        创建用户OIDC配置。只能创建一个用户OIDC身份提供商，并且创建用户OIDC配置之后会自动关闭用户SAML SSO身份提供商。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIAPUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIAPUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIAPLoginSessionDuration(
            self,
            request: models.DescribeIAPLoginSessionDurationRequest,
            opts: Dict = None,
    ) -> models.DescribeIAPLoginSessionDurationResponse:
        """
        查询登录会话时长
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIAPLoginSessionDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIAPLoginSessionDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIAPUserOIDCConfig(
            self,
            request: models.DescribeIAPUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeIAPUserOIDCConfigResponse:
        """
        查询用户OIDC配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIAPUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIAPUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableIAPUserSSO(
            self,
            request: models.DisableIAPUserSSORequest,
            opts: Dict = None,
    ) -> models.DisableIAPUserSSOResponse:
        """
        禁用用户SSO
        """
        
        kwargs = {}
        kwargs["action"] = "DisableIAPUserSSO"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableIAPUserSSOResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIAPLoginSessionDuration(
            self,
            request: models.ModifyIAPLoginSessionDurationRequest,
            opts: Dict = None,
    ) -> models.ModifyIAPLoginSessionDurationResponse:
        """
        修改登录会话时长
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIAPLoginSessionDuration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIAPLoginSessionDurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateIAPUserOIDCConfig(
            self,
            request: models.UpdateIAPUserOIDCConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateIAPUserOIDCConfigResponse:
        """
        修改用户OIDC配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateIAPUserOIDCConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateIAPUserOIDCConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)