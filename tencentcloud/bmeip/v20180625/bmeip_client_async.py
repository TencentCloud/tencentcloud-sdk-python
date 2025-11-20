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
from tencentcloud.bmeip.v20180625 import models
from typing import Dict


class BmeipClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmeip.tencentcloudapi.com'
    _service = 'bmeip'

    async def BindEipAcls(
            self,
            request: models.BindEipAclsRequest,
            opts: Dict = None,
    ) -> models.BindEipAclsResponse:
        """
        此接口用于为某个 EIP 关联 ACL。
        """
        
        kwargs = {}
        kwargs["action"] = "BindEipAcls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindEipAclsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindHosted(
            self,
            request: models.BindHostedRequest,
            opts: Dict = None,
    ) -> models.BindHostedResponse:
        """
        BindHosted接口用于绑定黑石弹性公网IP到黑石托管机器上
        """
        
        kwargs = {}
        kwargs["action"] = "BindHosted"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindHostedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindRs(
            self,
            request: models.BindRsRequest,
            opts: Dict = None,
    ) -> models.BindRsResponse:
        """
        绑定黑石EIP
        """
        
        kwargs = {}
        kwargs["action"] = "BindRs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindRsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindVpcIp(
            self,
            request: models.BindVpcIpRequest,
            opts: Dict = None,
    ) -> models.BindVpcIpResponse:
        """
        黑石EIP绑定VPC IP
        """
        
        kwargs = {}
        kwargs["action"] = "BindVpcIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindVpcIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEip(
            self,
            request: models.CreateEipRequest,
            opts: Dict = None,
    ) -> models.CreateEipResponse:
        """
        创建黑石弹性公网IP
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEipAcl(
            self,
            request: models.CreateEipAclRequest,
            opts: Dict = None,
    ) -> models.CreateEipAclResponse:
        """
        创建黑石弹性公网 EIP ACL
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEipAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEipAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEip(
            self,
            request: models.DeleteEipRequest,
            opts: Dict = None,
    ) -> models.DeleteEipResponse:
        """
        释放黑石弹性公网IP
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEipAcl(
            self,
            request: models.DeleteEipAclRequest,
            opts: Dict = None,
    ) -> models.DeleteEipAclResponse:
        """
        删除弹性公网IP ACL
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEipAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEipAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEipAcls(
            self,
            request: models.DescribeEipAclsRequest,
            opts: Dict = None,
    ) -> models.DescribeEipAclsResponse:
        """
        查询弹性公网IP ACL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEipAcls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEipAclsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEipQuota(
            self,
            request: models.DescribeEipQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeEipQuotaResponse:
        """
        查询黑石EIP 限额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEipQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEipQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEipTask(
            self,
            request: models.DescribeEipTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeEipTaskResponse:
        """
        黑石EIP查询任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEipTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEipTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEips(
            self,
            request: models.DescribeEipsRequest,
            opts: Dict = None,
    ) -> models.DescribeEipsResponse:
        """
        黑石EIP查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEipAcl(
            self,
            request: models.ModifyEipAclRequest,
            opts: Dict = None,
    ) -> models.ModifyEipAclResponse:
        """
        修改弹性公网IP ACL
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEipAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEipAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEipCharge(
            self,
            request: models.ModifyEipChargeRequest,
            opts: Dict = None,
    ) -> models.ModifyEipChargeResponse:
        """
        黑石EIP修改计费方式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEipCharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEipChargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEipName(
            self,
            request: models.ModifyEipNameRequest,
            opts: Dict = None,
    ) -> models.ModifyEipNameResponse:
        """
        更新黑石EIP名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEipName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEipNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindEipAcls(
            self,
            request: models.UnbindEipAclsRequest,
            opts: Dict = None,
    ) -> models.UnbindEipAclsResponse:
        """
        解绑弹性公网IP ACL
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindEipAcls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindEipAclsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindHosted(
            self,
            request: models.UnbindHostedRequest,
            opts: Dict = None,
    ) -> models.UnbindHostedResponse:
        """
        UnbindHosted接口用于解绑托管机器上的EIP
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindHosted"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindHostedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindRs(
            self,
            request: models.UnbindRsRequest,
            opts: Dict = None,
    ) -> models.UnbindRsResponse:
        """
        解绑黑石EIP
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindRs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindRsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindRsList(
            self,
            request: models.UnbindRsListRequest,
            opts: Dict = None,
    ) -> models.UnbindRsListResponse:
        """
        批量解绑物理机弹性公网IP接口
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindRsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindRsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindVpcIp(
            self,
            request: models.UnbindVpcIpRequest,
            opts: Dict = None,
    ) -> models.UnbindVpcIpResponse:
        """
        黑石EIP解绑VPCIP
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindVpcIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindVpcIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)