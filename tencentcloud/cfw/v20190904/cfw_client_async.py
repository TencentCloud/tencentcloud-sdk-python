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
from tencentcloud.cfw.v20190904 import models
from typing import Dict


class CfwClient(AbstractClient):
    _apiVersion = '2019-09-04'
    _endpoint = 'cfw.tencentcloudapi.com'
    _service = 'cfw'

    async def AddAclRule(
            self,
            request: models.AddAclRuleRequest,
            opts: Dict = None,
    ) -> models.AddAclRuleResponse:
        """
        添加互联网边界访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEnterpriseSecurityGroupRules(
            self,
            request: models.AddEnterpriseSecurityGroupRulesRequest,
            opts: Dict = None,
    ) -> models.AddEnterpriseSecurityGroupRulesResponse:
        """
        创建新企业安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddEnterpriseSecurityGroupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEnterpriseSecurityGroupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNatAcRule(
            self,
            request: models.AddNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.AddNatAcRuleResponse:
        """
        添加nat访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddVpcAcRule(
            self,
            request: models.AddVpcAcRuleRequest,
            opts: Dict = None,
    ) -> models.AddVpcAcRuleResponse:
        """
        添加VPC内网间规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddVpcAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddVpcAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAcRules(
            self,
            request: models.CreateAcRulesRequest,
            opts: Dict = None,
    ) -> models.CreateAcRulesResponse:
        """
        创建访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAcRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAcRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAddressTemplate(
            self,
            request: models.CreateAddressTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAddressTemplateResponse:
        """
        创建地址模板规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlertCenterIsolate(
            self,
            request: models.CreateAlertCenterIsolateRequest,
            opts: Dict = None,
    ) -> models.CreateAlertCenterIsolateResponse:
        """
        用户告警中心-封隔离处置按钮
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlertCenterIsolate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlertCenterIsolateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlertCenterOmit(
            self,
            request: models.CreateAlertCenterOmitRequest,
            opts: Dict = None,
    ) -> models.CreateAlertCenterOmitResponse:
        """
        用户告警中心-忽略处置按钮
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlertCenterOmit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlertCenterOmitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlertCenterRule(
            self,
            request: models.CreateAlertCenterRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAlertCenterRuleResponse:
        """
        用户告警中心-封禁、放通处置按钮
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlertCenterRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlertCenterRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBlockIgnoreRuleList(
            self,
            request: models.CreateBlockIgnoreRuleListRequest,
            opts: Dict = None,
    ) -> models.CreateBlockIgnoreRuleListResponse:
        """
        批量添加入侵防御封禁列表、放通列表规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBlockIgnoreRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBlockIgnoreRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBlockIgnoreRuleNew(
            self,
            request: models.CreateBlockIgnoreRuleNewRequest,
            opts: Dict = None,
    ) -> models.CreateBlockIgnoreRuleNewResponse:
        """
        批量添加入侵防御封禁列表、放通列表规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBlockIgnoreRuleNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBlockIgnoreRuleNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateChooseVpcs(
            self,
            request: models.CreateChooseVpcsRequest,
            opts: Dict = None,
    ) -> models.CreateChooseVpcsResponse:
        """
        创建、选择vpc
        """
        
        kwargs = {}
        kwargs["action"] = "CreateChooseVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateChooseVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatabaseWhiteListRules(
            self,
            request: models.CreateDatabaseWhiteListRulesRequest,
            opts: Dict = None,
    ) -> models.CreateDatabaseWhiteListRulesResponse:
        """
        创建暴露数据库白名单规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatabaseWhiteListRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatabaseWhiteListRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatFwInstance(
            self,
            request: models.CreateNatFwInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateNatFwInstanceResponse:
        """
        创建NAT防火墙实例（Region参数必填）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatFwInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatFwInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatFwInstanceWithDomain(
            self,
            request: models.CreateNatFwInstanceWithDomainRequest,
            opts: Dict = None,
    ) -> models.CreateNatFwInstanceWithDomainResponse:
        """
        创建防火墙实例和接入域名（Region参数必填）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatFwInstanceWithDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatFwInstanceWithDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupRules(
            self,
            request: models.CreateSecurityGroupRulesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupRulesResponse:
        """
        创建企业安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcFwGroup(
            self,
            request: models.CreateVpcFwGroupRequest,
            opts: Dict = None,
    ) -> models.CreateVpcFwGroupResponse:
        """
        创建VPC间防火墙(防火墙组)
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcFwGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcFwGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAcRule(
            self,
            request: models.DeleteAcRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAcRuleResponse:
        """
        删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressTemplate(
            self,
            request: models.DeleteAddressTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressTemplateResponse:
        """
        删除地址模板规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllAccessControlRule(
            self,
            request: models.DeleteAllAccessControlRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAllAccessControlRuleResponse:
        """
        业务废弃

        全部删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllAccessControlRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllAccessControlRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBlockIgnoreRuleList(
            self,
            request: models.DeleteBlockIgnoreRuleListRequest,
            opts: Dict = None,
    ) -> models.DeleteBlockIgnoreRuleListResponse:
        """
        批量删除入侵防御封禁列表、放通列表规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBlockIgnoreRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBlockIgnoreRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBlockIgnoreRuleNew(
            self,
            request: models.DeleteBlockIgnoreRuleNewRequest,
            opts: Dict = None,
    ) -> models.DeleteBlockIgnoreRuleNewResponse:
        """
        批量删除入侵防御封禁列表、放通列表规则（新）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBlockIgnoreRuleNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBlockIgnoreRuleNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatFwInstance(
            self,
            request: models.DeleteNatFwInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteNatFwInstanceResponse:
        """
        销毁防火墙实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatFwInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatFwInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRemoteAccessDomain(
            self,
            request: models.DeleteRemoteAccessDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteRemoteAccessDomainResponse:
        """
        删除远程运维域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRemoteAccessDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRemoteAccessDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceGroup(
            self,
            request: models.DeleteResourceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceGroupResponse:
        """
        DeleteResourceGroup-资产中心资产组删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroupRule(
            self,
            request: models.DeleteSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupRuleResponse:
        """
        删除规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcFwGroup(
            self,
            request: models.DeleteVpcFwGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcFwGroupResponse:
        """
        删除防火墙(组)，或者删除其中实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcFwGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcFwGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAcLists(
            self,
            request: models.DescribeAcListsRequest,
            opts: Dict = None,
    ) -> models.DescribeAcListsResponse:
        """
        访问控制列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAcLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAcListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAclRule(
            self,
            request: models.DescribeAclRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeAclRuleResponse:
        """
        查询互联网边界访问控制列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressTemplateList(
            self,
            request: models.DescribeAddressTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressTemplateListResponse:
        """
        查询地址模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSync(
            self,
            request: models.DescribeAssetSyncRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSyncResponse:
        """
        资产同步状态查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssociatedInstanceList(
            self,
            request: models.DescribeAssociatedInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssociatedInstanceListResponse:
        """
        获取安全组关联实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssociatedInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssociatedInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockByIpTimesList(
            self,
            request: models.DescribeBlockByIpTimesListRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockByIpTimesListResponse:
        """
        DescribeBlockByIpTimesList 告警中心阻断IP折线图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockByIpTimesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockByIpTimesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockIgnoreList(
            self,
            request: models.DescribeBlockIgnoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockIgnoreListResponse:
        """
        查询入侵防御放通封禁列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockIgnoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockIgnoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockStaticList(
            self,
            request: models.DescribeBlockStaticListRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockStaticListResponse:
        """
        DescribeBlockStaticList 告警中心柱形图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockStaticList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockStaticListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfwEips(
            self,
            request: models.DescribeCfwEipsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfwEipsResponse:
        """
        查询防火墙弹性公网IP
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfwEips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfwEipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfwInsStatus(
            self,
            request: models.DescribeCfwInsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCfwInsStatusResponse:
        """
        cfw实例运行状态查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfwInsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfwInsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefenseSwitch(
            self,
            request: models.DescribeDefenseSwitchRequest,
            opts: Dict = None,
    ) -> models.DescribeDefenseSwitchResponse:
        """
        获取入侵防御按钮列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefenseSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefenseSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnterpriseSGRuleProgress(
            self,
            request: models.DescribeEnterpriseSGRuleProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeEnterpriseSGRuleProgressResponse:
        """
        查询新版安全组下发进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnterpriseSGRuleProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnterpriseSGRuleProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnterpriseSecurityGroupRule(
            self,
            request: models.DescribeEnterpriseSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeEnterpriseSecurityGroupRuleResponse:
        """
        查询新企业安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnterpriseSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnterpriseSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnterpriseSecurityGroupRuleList(
            self,
            request: models.DescribeEnterpriseSecurityGroupRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeEnterpriseSecurityGroupRuleListResponse:
        """
        查询新企业安全组规则  从node接口迁移   原接口DescribeSecurityGroupNewList
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnterpriseSecurityGroupRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnterpriseSecurityGroupRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFwEdgeIps(
            self,
            request: models.DescribeFwEdgeIpsRequest,
            opts: Dict = None,
    ) -> models.DescribeFwEdgeIpsResponse:
        """
        串行防火墙IP开关列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFwEdgeIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFwEdgeIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFwGroupInstanceInfo(
            self,
            request: models.DescribeFwGroupInstanceInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeFwGroupInstanceInfoResponse:
        """
        获取租户所有VPC防火墙(组)及VPC防火墙实例卡片信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFwGroupInstanceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFwGroupInstanceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFwSyncStatus(
            self,
            request: models.DescribeFwSyncStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeFwSyncStatusResponse:
        """
        获取防火墙同步状态，一般在执行同步操作后查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFwSyncStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFwSyncStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGuideScanInfo(
            self,
            request: models.DescribeGuideScanInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeGuideScanInfoResponse:
        """
        DescribeGuideScanInfo新手引导扫描接口信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGuideScanInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGuideScanInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPStatusList(
            self,
            request: models.DescribeIPStatusListRequest,
            opts: Dict = None,
    ) -> models.DescribeIPStatusListResponse:
        """
        IP防护状态查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPStatusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPStatusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageStatistic(
            self,
            request: models.DescribeLogStorageStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageStatisticResponse:
        """
        租户日志存储统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogs(
            self,
            request: models.DescribeLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogsResponse:
        """
        日志审计日志查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatAcRule(
            self,
            request: models.DescribeNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeNatAcRuleResponse:
        """
        查询NAT访问控制列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwDnatRule(
            self,
            request: models.DescribeNatFwDnatRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwDnatRuleResponse:
        """
        查询Nat防火墙Dnat规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwDnatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwDnatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInfoCount(
            self,
            request: models.DescribeNatFwInfoCountRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInfoCountResponse:
        """
        获取当前用户接入nat防火墙的所有子网数及natfw实例个数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInfoCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInfoCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInstance(
            self,
            request: models.DescribeNatFwInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInstanceResponse:
        """
        DescribeNatFwInstance 获取租户所有NAT实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInstanceWithRegion(
            self,
            request: models.DescribeNatFwInstanceWithRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInstanceWithRegionResponse:
        """
        GetNatFwInstanceWithRegion 获取租户新增运维的NAT实例，带上地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInstanceWithRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInstanceWithRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwInstancesInfo(
            self,
            request: models.DescribeNatFwInstancesInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwInstancesInfoResponse:
        """
        GetNatInstance 获取租户所有NAT实例及实例卡片信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwInstancesInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwInstancesInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwSwitch(
            self,
            request: models.DescribeNatFwSwitchRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwSwitchResponse:
        """
        查询NAT边界防火墙开关列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatFwVpcDnsLst(
            self,
            request: models.DescribeNatFwVpcDnsLstRequest,
            opts: Dict = None,
    ) -> models.DescribeNatFwVpcDnsLstResponse:
        """
        展示当前natfw 实例对应的vpc dns开关
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatFwVpcDnsLst"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatFwVpcDnsLstResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceGroup(
            self,
            request: models.DescribeResourceGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceGroupResponse:
        """
        DescribeResourceGroup资产中心资产树信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceGroupNew(
            self,
            request: models.DescribeResourceGroupNewRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceGroupNewResponse:
        """
        资产中心资产组数数据信息查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceGroupNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceGroupNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleOverview(
            self,
            request: models.DescribeRuleOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleOverviewResponse:
        """
        查询规则列表概况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupList(
            self,
            request: models.DescribeSecurityGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupListResponse:
        """
        查询安全组规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceAsset(
            self,
            request: models.DescribeSourceAssetRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceAssetResponse:
        """
        DescribeSourceAsset-查询全部资产信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSwitchLists(
            self,
            request: models.DescribeSwitchListsRequest,
            opts: Dict = None,
    ) -> models.DescribeSwitchListsResponse:
        """
        防火墙开关列表，请换用DescribeFwEdgeIps
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSwitchLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSwitchListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTLogInfo(
            self,
            request: models.DescribeTLogInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTLogInfoResponse:
        """
        DescribeTLogInfo告警中心概况查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTLogInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTLogInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTLogIpList(
            self,
            request: models.DescribeTLogIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeTLogIpListResponse:
        """
        DescribeTLogIpList告警中心IP柱形图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTLogIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTLogIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableStatus(
            self,
            request: models.DescribeTableStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTableStatusResponse:
        """
        查询规则表状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnHandleEventTabList(
            self,
            request: models.DescribeUnHandleEventTabListRequest,
            opts: Dict = None,
    ) -> models.DescribeUnHandleEventTabListResponse:
        """
        DescribeUnHandleEventTabList 告警中心伪攻击链事件未处置接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnHandleEventTabList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnHandleEventTabListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcAcRule(
            self,
            request: models.DescribeVpcAcRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcAcRuleResponse:
        """
        查询内网间访问控制列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcFwGroupSwitch(
            self,
            request: models.DescribeVpcFwGroupSwitchRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcFwGroupSwitchResponse:
        """
        VPC防火墙(组)开关列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcFwGroupSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcFwGroupSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExpandCfwVertical(
            self,
            request: models.ExpandCfwVerticalRequest,
            opts: Dict = None,
    ) -> models.ExpandCfwVerticalResponse:
        """
        防火墙垂直扩容
        """
        
        kwargs = {}
        kwargs["action"] = "ExpandCfwVertical"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExpandCfwVerticalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAcRule(
            self,
            request: models.ModifyAcRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAcRuleResponse:
        """
        修改规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAclRule(
            self,
            request: models.ModifyAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAclRuleResponse:
        """
        修改互联网边界访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressTemplate(
            self,
            request: models.ModifyAddressTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressTemplateResponse:
        """
        修改地址模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllPublicIPSwitchStatus(
            self,
            request: models.ModifyAllPublicIPSwitchStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAllPublicIPSwitchStatusResponse:
        """
        互联网边界防火墙一键开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllPublicIPSwitchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllPublicIPSwitchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllRuleStatus(
            self,
            request: models.ModifyAllRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAllRuleStatusResponse:
        """
        启用停用全部规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetScan(
            self,
            request: models.ModifyAssetScanRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetScanResponse:
        """
        资产扫描
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetScan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetScanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetSync(
            self,
            request: models.ModifyAssetSyncRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetSyncResponse:
        """
        资产同步
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlockIgnoreList(
            self,
            request: models.ModifyBlockIgnoreListRequest,
            opts: Dict = None,
    ) -> models.ModifyBlockIgnoreListResponse:
        """
        支持对封禁列表、放通列表如下操作：
        批量增加封禁IP、放通IP/域名
        批量删除封禁IP、放通IP/域名
        批量修改封禁IP、放通IP/域名生效事件
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlockIgnoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlockIgnoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlockIgnoreRule(
            self,
            request: models.ModifyBlockIgnoreRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyBlockIgnoreRuleResponse:
        """
        编辑单条入侵防御封禁列表、放通列表规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlockIgnoreRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlockIgnoreRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlockIgnoreRuleNew(
            self,
            request: models.ModifyBlockIgnoreRuleNewRequest,
            opts: Dict = None,
    ) -> models.ModifyBlockIgnoreRuleNewResponse:
        """
        编辑单条入侵防御封禁列表、放通列表规则（新）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlockIgnoreRuleNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlockIgnoreRuleNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlockTop(
            self,
            request: models.ModifyBlockTopRequest,
            opts: Dict = None,
    ) -> models.ModifyBlockTopResponse:
        """
        ModifyBlockTop取消置顶接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlockTop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlockTopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEWRuleStatus(
            self,
            request: models.ModifyEWRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEWRuleStatusResponse:
        """
        启用停用VPC间规则或Nat边界规则
        VPC间规则需指定EdgeId。Nat边界规则需指定地域Region与Direction。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEWRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEWRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdgeIpSwitch(
            self,
            request: models.ModifyEdgeIpSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyEdgeIpSwitchResponse:
        """
        修改边界防火墙开关(旁路、串行)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdgeIpSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdgeIpSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnterpriseSecurityDispatchStatus(
            self,
            request: models.ModifyEnterpriseSecurityDispatchStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEnterpriseSecurityDispatchStatusResponse:
        """
        修改企业安全组下发状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnterpriseSecurityDispatchStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnterpriseSecurityDispatchStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnterpriseSecurityGroupRule(
            self,
            request: models.ModifyEnterpriseSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyEnterpriseSecurityGroupRuleResponse:
        """
        编辑新企业安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnterpriseSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnterpriseSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFwGroupSwitch(
            self,
            request: models.ModifyFwGroupSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyFwGroupSwitchResponse:
        """
        修改防火墙(组)开关(支持单点模式、多点模式、全互通模式)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFwGroupSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFwGroupSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatAcRule(
            self,
            request: models.ModifyNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNatAcRuleResponse:
        """
        修改NAT访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatFwReSelect(
            self,
            request: models.ModifyNatFwReSelectRequest,
            opts: Dict = None,
    ) -> models.ModifyNatFwReSelectResponse:
        """
        防火墙实例重新选择vpc或nat
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatFwReSelect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatFwReSelectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatFwSwitch(
            self,
            request: models.ModifyNatFwSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyNatFwSwitchResponse:
        """
        修改NAT防火墙开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatFwSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatFwSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatFwVpcDnsSwitch(
            self,
            request: models.ModifyNatFwVpcDnsSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyNatFwVpcDnsSwitchResponse:
        """
        nat 防火墙VPC DNS 开关切换
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatFwVpcDnsSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatFwVpcDnsSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatInstance(
            self,
            request: models.ModifyNatInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyNatInstanceResponse:
        """
        编辑NAT防火墙
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatSequenceRules(
            self,
            request: models.ModifyNatSequenceRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyNatSequenceRulesResponse:
        """
        NAT防火墙规则快速排序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatSequenceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatSequenceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceGroup(
            self,
            request: models.ModifyResourceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceGroupResponse:
        """
        ModifyResourceGroup-资产中心资产组信息修改
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRunSyncAsset(
            self,
            request: models.ModifyRunSyncAssetRequest,
            opts: Dict = None,
    ) -> models.ModifyRunSyncAssetResponse:
        """
        同步资产-互联网&VPC（新）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRunSyncAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRunSyncAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupItemRuleStatus(
            self,
            request: models.ModifySecurityGroupItemRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupItemRuleStatusResponse:
        """
        启用停用单条企业安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupItemRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupItemRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupRule(
            self,
            request: models.ModifySecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupRuleResponse:
        """
        编辑单条安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupSequenceRules(
            self,
            request: models.ModifySecurityGroupSequenceRulesRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupSequenceRulesResponse:
        """
        企业安全组规则快速排序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupSequenceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupSequenceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySequenceAclRules(
            self,
            request: models.ModifySequenceAclRulesRequest,
            opts: Dict = None,
    ) -> models.ModifySequenceAclRulesResponse:
        """
        互联网边界规则快速排序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySequenceAclRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySequenceAclRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySequenceRules(
            self,
            request: models.ModifySequenceRulesRequest,
            opts: Dict = None,
    ) -> models.ModifySequenceRulesResponse:
        """
        修改规则执行顺序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySequenceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySequenceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStorageSetting(
            self,
            request: models.ModifyStorageSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyStorageSettingResponse:
        """
        日志存储设置，可以修改存储时间和清空日志
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStorageSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStorageSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableStatus(
            self,
            request: models.ModifyTableStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyTableStatusResponse:
        """
        修改规则表状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAcRule(
            self,
            request: models.ModifyVpcAcRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAcRuleResponse:
        """
        修改内网间访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcFwGroup(
            self,
            request: models.ModifyVpcFwGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcFwGroupResponse:
        """
        编辑VPC间防火墙(防火墙组)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcFwGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcFwGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcFwSequenceRules(
            self,
            request: models.ModifyVpcFwSequenceRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcFwSequenceRulesResponse:
        """
        vpc间规则快速排序
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcFwSequenceRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcFwSequenceRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveAcRule(
            self,
            request: models.RemoveAcRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveAcRuleResponse:
        """
        删除互联网边界规则
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveAclRule(
            self,
            request: models.RemoveAclRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveAclRuleResponse:
        """
        删除互联网边界访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveEnterpriseSecurityGroupRule(
            self,
            request: models.RemoveEnterpriseSecurityGroupRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveEnterpriseSecurityGroupRuleResponse:
        """
        删除新企业安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveEnterpriseSecurityGroupRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveEnterpriseSecurityGroupRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveNatAcRule(
            self,
            request: models.RemoveNatAcRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveNatAcRuleResponse:
        """
        删除NAT访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveNatAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveNatAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveVpcAcRule(
            self,
            request: models.RemoveVpcAcRuleRequest,
            opts: Dict = None,
    ) -> models.RemoveVpcAcRuleResponse:
        """
        删除VPC间规则
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveVpcAcRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveVpcAcRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        本接口用于检索分析日志，使用该接口时请注意如下事项：
        1. 该接口除受默认接口请求频率限制外，针对单个日志主题，查询并发数不能超过15。
        2. 检索语法建议使用日志服务专用检索语法CQL，请使用SyntaxRule参数，将值设置为1，控制台默认也使用该语法规则。
        3. API返回数据包最大49MB，建议启用 gzip 压缩（HTTP Request Header Accept-Encoding:gzip）。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNatFwDnatRule(
            self,
            request: models.SetNatFwDnatRuleRequest,
            opts: Dict = None,
    ) -> models.SetNatFwDnatRuleResponse:
        """
        配置防火墙Dnat规则
        """
        
        kwargs = {}
        kwargs["action"] = "SetNatFwDnatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNatFwDnatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNatFwEip(
            self,
            request: models.SetNatFwEipRequest,
            opts: Dict = None,
    ) -> models.SetNatFwEipResponse:
        """
        设置防火墙实例弹性公网ip，目前仅支持新增模式的防火墙实例
        """
        
        kwargs = {}
        kwargs["action"] = "SetNatFwEip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNatFwEipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSecurityGroupRuleDispatch(
            self,
            request: models.StopSecurityGroupRuleDispatchRequest,
            opts: Dict = None,
    ) -> models.StopSecurityGroupRuleDispatchResponse:
        """
        中止安全组规则下发
        """
        
        kwargs = {}
        kwargs["action"] = "StopSecurityGroupRuleDispatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSecurityGroupRuleDispatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncFwOperate(
            self,
            request: models.SyncFwOperateRequest,
            opts: Dict = None,
    ) -> models.SyncFwOperateResponse:
        """
        同步防火墙操作，包括同步防火墙路由（若vpc，专线网关等增加了Cidr，需要手动同步一下路由使之在防火墙上生效）等。
        """
        
        kwargs = {}
        kwargs["action"] = "SyncFwOperate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncFwOperateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)