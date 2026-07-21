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
from tencentcloud.ga2.v20250115 import models
from typing import Dict


class Ga2Client(AbstractClient):
    _apiVersion = '2025-01-15'
    _endpoint = 'ga2.tencentcloudapi.com'
    _service = 'ga2'

    async def CreateAccelerateAreas(
            self,
            request: models.CreateAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.CreateAccelerateAreasResponse:
        """
        创建加速地域
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEndpointGroup(
            self,
            request: models.CreateEndpointGroupRequest,
            opts: Dict = None,
    ) -> models.CreateEndpointGroupResponse:
        """
        创建终端节点组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEndpointGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEndpointGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateForwardingPolicy(
            self,
            request: models.CreateForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateForwardingPolicyResponse:
        """
        创建七层转发策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateForwardingRule(
            self,
            request: models.CreateForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.CreateForwardingRuleResponse:
        """
        创建七层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAccelerator(
            self,
            request: models.CreateGlobalAcceleratorRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorResponse:
        """
        创建全球加速实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAccelerator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAcceleratorAccessLog(
            self,
            request: models.CreateGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorAccessLogResponse:
        """
        创建GA访问日志
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAcceleratorAclPolicy(
            self,
            request: models.CreateGlobalAcceleratorAclPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorAclPolicyResponse:
        """
        创建访问控制策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAcceleratorAclPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorAclPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAcceleratorAclRule(
            self,
            request: models.CreateGlobalAcceleratorAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorAclRuleResponse:
        """
        创建ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAcceleratorAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListener(
            self,
            request: models.CreateListenerRequest,
            opts: Dict = None,
    ) -> models.CreateListenerResponse:
        """
        创建监听器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListenerAdditionalCert(
            self,
            request: models.CreateListenerAdditionalCertRequest,
            opts: Dict = None,
    ) -> models.CreateListenerAdditionalCertResponse:
        """
        添加扩展证书
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListenerAdditionalCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerAdditionalCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccelerateAreas(
            self,
            request: models.DeleteAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.DeleteAccelerateAreasResponse:
        """
        删除加速地域
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEndpointGroups(
            self,
            request: models.DeleteEndpointGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteEndpointGroupsResponse:
        """
        删除终端节点组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEndpointGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEndpointGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteForwardingPolicy(
            self,
            request: models.DeleteForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteForwardingPolicyResponse:
        """
        删除七层转发策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteForwardingRule(
            self,
            request: models.DeleteForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteForwardingRuleResponse:
        """
        删除七层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAccelerator(
            self,
            request: models.DeleteGlobalAcceleratorRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorResponse:
        """
        删除全球加速实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAccelerator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAcceleratorAccessLog(
            self,
            request: models.DeleteGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorAccessLogResponse:
        """
        删除GA日志任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAcceleratorAclPolicy(
            self,
            request: models.DeleteGlobalAcceleratorAclPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorAclPolicyResponse:
        """
        删除访问控制策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAcceleratorAclPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorAclPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAcceleratorAclRule(
            self,
            request: models.DeleteGlobalAcceleratorAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorAclRuleResponse:
        """
        删除ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAcceleratorAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListener(
            self,
            request: models.DeleteListenerRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerResponse:
        """
        删除监听器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListenerAdditionalCert(
            self,
            request: models.DeleteListenerAdditionalCertRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerAdditionalCertResponse:
        """
        删除扩展证书
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListenerAdditionalCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerAdditionalCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccelerateAreas(
            self,
            request: models.DescribeAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeAccelerateAreasResponse:
        """
        查询加速地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccelerateRegions(
            self,
            request: models.DescribeAccelerateRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccelerateRegionsResponse:
        """
        查询可选加速区域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccelerateRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccelerateRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessLogParam(
            self,
            request: models.DescribeAccessLogParamRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessLogParamResponse:
        """
        查看访问日志上报参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessLogParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessLogParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBorderSettlement(
            self,
            request: models.DescribeCrossBorderSettlementRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderSettlementResponse:
        """
        查询跨境账单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderSettlement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderSettlementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEndpointGroups(
            self,
            request: models.DescribeEndpointGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeEndpointGroupsResponse:
        """
        查询终端节点组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndpointGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndpointGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardingPolicy(
            self,
            request: models.DescribeForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardingPolicyResponse:
        """
        查看七层转发策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardingRule(
            self,
            request: models.DescribeForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardingRuleResponse:
        """
        查看七层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAcceleratorAccessLog(
            self,
            request: models.DescribeGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorAccessLogResponse:
        """
        查询日志任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAcceleratorAclPolicies(
            self,
            request: models.DescribeGlobalAcceleratorAclPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorAclPoliciesResponse:
        """
        查看访问控制策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAcceleratorAclPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorAclPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAcceleratorAclRules(
            self,
            request: models.DescribeGlobalAcceleratorAclRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorAclRulesResponse:
        """
        查看ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAcceleratorAclRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorAclRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAccelerators(
            self,
            request: models.DescribeGlobalAcceleratorsRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorsResponse:
        """
        修改全球加速实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAccelerators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListeners(
            self,
            request: models.DescribeListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenersResponse:
        """
        查询监听器
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        查询异步任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccelerateAreas(
            self,
            request: models.ModifyAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.ModifyAccelerateAreasResponse:
        """
        修改加速地域
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessLogStatus(
            self,
            request: models.ModifyAccessLogStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessLogStatusResponse:
        """
        修改日志任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessLogStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessLogStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEndpointGroup(
            self,
            request: models.ModifyEndpointGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyEndpointGroupResponse:
        """
        修改终端节点组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEndpointGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEndpointGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyForwardingPolicy(
            self,
            request: models.ModifyForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyForwardingPolicyResponse:
        """
        修改七层转发策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyForwardingRule(
            self,
            request: models.ModifyForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyForwardingRuleResponse:
        """
        修改七层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAccelerator(
            self,
            request: models.ModifyGlobalAcceleratorRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorResponse:
        """
        修改全球加速实例
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAccelerator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAcceleratorAccessLog(
            self,
            request: models.ModifyGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorAccessLogResponse:
        """
        修改GA访问日志
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAcceleratorAclPolicy(
            self,
            request: models.ModifyGlobalAcceleratorAclPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorAclPolicyResponse:
        """
        修改访问控制策略状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAcceleratorAclPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorAclPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAcceleratorAclRule(
            self,
            request: models.ModifyGlobalAcceleratorAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorAclRuleResponse:
        """
        修改ACL规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAcceleratorAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyListener(
            self,
            request: models.ModifyListenerRequest,
            opts: Dict = None,
    ) -> models.ModifyListenerResponse:
        """
        修改监听器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceListenerAdditionalCert(
            self,
            request: models.ReplaceListenerAdditionalCertRequest,
            opts: Dict = None,
    ) -> models.ReplaceListenerAdditionalCertResponse:
        """
        替换扩展证书
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceListenerAdditionalCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceListenerAdditionalCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)