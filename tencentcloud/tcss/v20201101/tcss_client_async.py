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
from tencentcloud.tcss.v20201101 import models
from typing import Dict


class TcssClient(AbstractClient):
    _apiVersion = '2020-11-01'
    _endpoint = 'tcss.tencentcloudapi.com'
    _service = 'tcss'

    async def AddAndPublishNetworkFirewallPolicyDetail(
            self,
            request: models.AddAndPublishNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.AddAndPublishNetworkFirewallPolicyDetailResponse:
        """
        容器网络创建网络策略添加并发布任务
        """
        
        kwargs = {}
        kwargs["action"] = "AddAndPublishNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAndPublishNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAndPublishNetworkFirewallPolicyYamlDetail(
            self,
            request: models.AddAndPublishNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse:
        """
        容器网络创建Yaml网络策略并发布任务
        """
        
        kwargs = {}
        kwargs["action"] = "AddAndPublishNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAssetImageRegistryRegistryDetail(
            self,
            request: models.AddAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.AddAssetImageRegistryRegistryDetailResponse:
        """
        新增单个镜像仓库详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "AddAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddComplianceAssetPolicySetToWhitelist(
            self,
            request: models.AddComplianceAssetPolicySetToWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddComplianceAssetPolicySetToWhitelistResponse:
        """
        新增安全合规忽略(资产+检测项列表)列表，不显示指定的检查项包含的资产内容
        参考的AddCompliancePolicyItemToWhitelist，除输入字段外，其它应该是一致的，如果有不同可能是定义的不对
        """
        
        kwargs = {}
        kwargs["action"] = "AddComplianceAssetPolicySetToWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddComplianceAssetPolicySetToWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCompliancePolicyAssetSetToWhitelist(
            self,
            request: models.AddCompliancePolicyAssetSetToWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddCompliancePolicyAssetSetToWhitelistResponse:
        """
        新增安全合规忽略(检测项+资产)列表，不显示指定的检查项包含的资产内容
        参考的AddCompliancePolicyItemToWhitelist，除输入字段外，其它应该是一致的，如果有不同可能是定义的不对
        """
        
        kwargs = {}
        kwargs["action"] = "AddCompliancePolicyAssetSetToWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCompliancePolicyAssetSetToWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCompliancePolicyItemToWhitelist(
            self,
            request: models.AddCompliancePolicyItemToWhitelistRequest,
            opts: Dict = None,
    ) -> models.AddCompliancePolicyItemToWhitelistResponse:
        """
        将指定的检测项添加到白名单中，不显示未通过结果。
        """
        
        kwargs = {}
        kwargs["action"] = "AddCompliancePolicyItemToWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCompliancePolicyItemToWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditAbnormalProcessRule(
            self,
            request: models.AddEditAbnormalProcessRuleRequest,
            opts: Dict = None,
    ) -> models.AddEditAbnormalProcessRuleResponse:
        """
        添加编辑运行时异常进程策略
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditAbnormalProcessRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditAbnormalProcessRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditAccessControlRule(
            self,
            request: models.AddEditAccessControlRuleRequest,
            opts: Dict = None,
    ) -> models.AddEditAccessControlRuleResponse:
        """
        添加编辑运行时访问控制策略
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditAccessControlRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditAccessControlRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditImageAutoAuthorizedRule(
            self,
            request: models.AddEditImageAutoAuthorizedRuleRequest,
            opts: Dict = None,
    ) -> models.AddEditImageAutoAuthorizedRuleResponse:
        """
        新增或编辑本地镜像自动授权规则
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditImageAutoAuthorizedRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditImageAutoAuthorizedRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditReverseShellWhiteList(
            self,
            request: models.AddEditReverseShellWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddEditReverseShellWhiteListResponse:
        """
        添加编辑运行时反弹shell白名单
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditReverseShellWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditReverseShellWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditRiskSyscallWhiteList(
            self,
            request: models.AddEditRiskSyscallWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddEditRiskSyscallWhiteListResponse:
        """
        添加编辑运行时高危系统调用白名单
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditRiskSyscallWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditRiskSyscallWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEditWarningRules(
            self,
            request: models.AddEditWarningRulesRequest,
            opts: Dict = None,
    ) -> models.AddEditWarningRulesResponse:
        """
        添加编辑告警策略
        """
        
        kwargs = {}
        kwargs["action"] = "AddEditWarningRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEditWarningRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddEscapeWhiteList(
            self,
            request: models.AddEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.AddEscapeWhiteListResponse:
        """
        新增逃逸白名单
        """
        
        kwargs = {}
        kwargs["action"] = "AddEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddIgnoreVul(
            self,
            request: models.AddIgnoreVulRequest,
            opts: Dict = None,
    ) -> models.AddIgnoreVulResponse:
        """
        新增漏洞扫描忽略漏洞
        """
        
        kwargs = {}
        kwargs["action"] = "AddIgnoreVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddIgnoreVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNetworkFirewallPolicyDetail(
            self,
            request: models.AddNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.AddNetworkFirewallPolicyDetailResponse:
        """
        容器网络创建网络策略添加任务
        """
        
        kwargs = {}
        kwargs["action"] = "AddNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNetworkFirewallPolicyYamlDetail(
            self,
            request: models.AddNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.AddNetworkFirewallPolicyYamlDetailResponse:
        """
        容器网络创建Yaml网络策略添加任务
        """
        
        kwargs = {}
        kwargs["action"] = "AddNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckNetworkFirewallPolicyYaml(
            self,
            request: models.CheckNetworkFirewallPolicyYamlRequest,
            opts: Dict = None,
    ) -> models.CheckNetworkFirewallPolicyYamlResponse:
        """
        容器网络创建检查Yaml网络策略任务
        """
        
        kwargs = {}
        kwargs["action"] = "CheckNetworkFirewallPolicyYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckNetworkFirewallPolicyYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckRepeatAssetImageRegistry(
            self,
            request: models.CheckRepeatAssetImageRegistryRequest,
            opts: Dict = None,
    ) -> models.CheckRepeatAssetImageRegistryResponse:
        """
        检查单个镜像仓库名是否重复
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRepeatAssetImageRegistry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRepeatAssetImageRegistryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmNetworkFirewallPolicy(
            self,
            request: models.ConfirmNetworkFirewallPolicyRequest,
            opts: Dict = None,
    ) -> models.ConfirmNetworkFirewallPolicyResponse:
        """
        容器网络创建网络策略确认任务
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmNetworkFirewallPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmNetworkFirewallPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAbnormalProcessRulesExportJob(
            self,
            request: models.CreateAbnormalProcessRulesExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAbnormalProcessRulesExportJobResponse:
        """
        创建异常进程规则导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAbnormalProcessRulesExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAbnormalProcessRulesExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessControlsRuleExportJob(
            self,
            request: models.CreateAccessControlsRuleExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAccessControlsRuleExportJobResponse:
        """
        创建文件篡改规则导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessControlsRuleExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessControlsRuleExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageRegistryScanTask(
            self,
            request: models.CreateAssetImageRegistryScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageRegistryScanTaskResponse:
        """
        镜像仓库创建镜像扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageRegistryScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageRegistryScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageRegistryScanTaskOneKey(
            self,
            request: models.CreateAssetImageRegistryScanTaskOneKeyRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageRegistryScanTaskOneKeyResponse:
        """
        镜像仓库创建镜像一键扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageRegistryScanTaskOneKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageRegistryScanTaskOneKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageScanSetting(
            self,
            request: models.CreateAssetImageScanSettingRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageScanSettingResponse:
        """
        添加容器安全镜像扫描设置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageScanTask(
            self,
            request: models.CreateAssetImageScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageScanTaskResponse:
        """
        容器安全创建镜像扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssetImageVirusExportJob(
            self,
            request: models.CreateAssetImageVirusExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateAssetImageVirusExportJobResponse:
        """
        创建本地镜像木马列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssetImageVirusExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssetImageVirusExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCheckComponent(
            self,
            request: models.CreateCheckComponentRequest,
            opts: Dict = None,
    ) -> models.CreateCheckComponentResponse:
        """
        安装检查组件，创建防护容器
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCheckComponent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCheckComponentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterAccess(
            self,
            request: models.CreateClusterAccessRequest,
            opts: Dict = None,
    ) -> models.CreateClusterAccessResponse:
        """
        创建集群接入
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterCheckTask(
            self,
            request: models.CreateClusterCheckTaskRequest,
            opts: Dict = None,
    ) -> models.CreateClusterCheckTaskResponse:
        """
        创建集群检查任务，用户检查用户的集群相关风险项
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterCheckTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterCheckTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComplianceTask(
            self,
            request: models.CreateComplianceTaskRequest,
            opts: Dict = None,
    ) -> models.CreateComplianceTaskResponse:
        """
        创建合规检查任务，在资产级别触发重新检测时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComplianceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComplianceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComponentExportJob(
            self,
            request: models.CreateComponentExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateComponentExportJobResponse:
        """
        查询本地镜像组件列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComponentExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComponentExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDefenceVulExportJob(
            self,
            request: models.CreateDefenceVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateDefenceVulExportJobResponse:
        """
        创建支持防御的漏洞导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDefenceVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDefenceVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmergencyVulExportJob(
            self,
            request: models.CreateEmergencyVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEmergencyVulExportJobResponse:
        """
        创建应急漏洞导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmergencyVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmergencyVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEscapeEventsExportJob(
            self,
            request: models.CreateEscapeEventsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEscapeEventsExportJobResponse:
        """
        创建逃逸事件导出异步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEscapeEventsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEscapeEventsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEscapeWhiteListExportJob(
            self,
            request: models.CreateEscapeWhiteListExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateEscapeWhiteListExportJobResponse:
        """
        创建逃逸白名单导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEscapeWhiteListExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEscapeWhiteListExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExportComplianceStatusListJob(
            self,
            request: models.CreateExportComplianceStatusListJobRequest,
            opts: Dict = None,
    ) -> models.CreateExportComplianceStatusListJobResponse:
        """
        创建一个导出安全合规信息的任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExportComplianceStatusListJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportComplianceStatusListJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostExportJob(
            self,
            request: models.CreateHostExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateHostExportJobResponse:
        """
        创建主机列表导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageExportJob(
            self,
            request: models.CreateImageExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateImageExportJobResponse:
        """
        创建镜像导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateK8sApiAbnormalEventExportJob(
            self,
            request: models.CreateK8sApiAbnormalEventExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateK8sApiAbnormalEventExportJobResponse:
        """
        创建k8s api异常事件导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateK8sApiAbnormalEventExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateK8sApiAbnormalEventExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateK8sApiAbnormalRuleExportJob(
            self,
            request: models.CreateK8sApiAbnormalRuleExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateK8sApiAbnormalRuleExportJobResponse:
        """
        创建k8sApi异常规则导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateK8sApiAbnormalRuleExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateK8sApiAbnormalRuleExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateK8sApiAbnormalRuleInfo(
            self,
            request: models.CreateK8sApiAbnormalRuleInfoRequest,
            opts: Dict = None,
    ) -> models.CreateK8sApiAbnormalRuleInfoResponse:
        """
        创建k8sapi异常事件规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateK8sApiAbnormalRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateK8sApiAbnormalRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallClusterRefresh(
            self,
            request: models.CreateNetworkFirewallClusterRefreshRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallClusterRefreshResponse:
        """
        容器网络集群下发刷新任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallClusterRefresh"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallClusterRefreshResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallPolicyDiscover(
            self,
            request: models.CreateNetworkFirewallPolicyDiscoverRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallPolicyDiscoverResponse:
        """
        容器网络集群网络策略创建自动发现任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallPolicyDiscover"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallPolicyDiscoverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallPublish(
            self,
            request: models.CreateNetworkFirewallPublishRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallPublishResponse:
        """
        容器网络创建网络策略发布任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallPublish"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallPublishResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkFirewallUndoPublish(
            self,
            request: models.CreateNetworkFirewallUndoPublishRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkFirewallUndoPublishResponse:
        """
        容器网络创建网络策略撤销任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkFirewallUndoPublish"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkFirewallUndoPublishResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrModifyPostPayCores(
            self,
            request: models.CreateOrModifyPostPayCoresRequest,
            opts: Dict = None,
    ) -> models.CreateOrModifyPostPayCoresResponse:
        """
        CreateOrModifyPostPayCores  创建或者编辑弹性计费上限
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrModifyPostPayCores"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrModifyPostPayCoresResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProcessEventsExportJob(
            self,
            request: models.CreateProcessEventsExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateProcessEventsExportJobResponse:
        """
        创建异常进程事件导出异步任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProcessEventsExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProcessEventsExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRefreshTask(
            self,
            request: models.CreateRefreshTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRefreshTaskResponse:
        """
        下发刷新任务，会刷新资产信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRefreshTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRefreshTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRiskDnsEventExportJob(
            self,
            request: models.CreateRiskDnsEventExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateRiskDnsEventExportJobResponse:
        """
        创建恶意请求事件导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRiskDnsEventExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRiskDnsEventExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSearchTemplate(
            self,
            request: models.CreateSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateSearchTemplateResponse:
        """
        添加检索模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSystemVulExportJob(
            self,
            request: models.CreateSystemVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateSystemVulExportJobResponse:
        """
        创建系统漏洞导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSystemVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSystemVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVirusScanAgain(
            self,
            request: models.CreateVirusScanAgainRequest,
            opts: Dict = None,
    ) -> models.CreateVirusScanAgainResponse:
        """
        运行时文件查杀重新检测
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVirusScanAgain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVirusScanAgainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVirusScanTask(
            self,
            request: models.CreateVirusScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVirusScanTaskResponse:
        """
        运行时文件查杀一键扫描
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVirusScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVirusScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulContainerExportJob(
            self,
            request: models.CreateVulContainerExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulContainerExportJobResponse:
        """
        创建受漏洞影响的容器导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulContainerExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulContainerExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulDefenceEventExportJob(
            self,
            request: models.CreateVulDefenceEventExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulDefenceEventExportJobResponse:
        """
        创建漏洞防御导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulDefenceEventExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulDefenceEventExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulDefenceHostExportJob(
            self,
            request: models.CreateVulDefenceHostExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulDefenceHostExportJobResponse:
        """
        创建漏洞防御主机导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulDefenceHostExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulDefenceHostExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulExportJob(
            self,
            request: models.CreateVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulExportJobResponse:
        """
        查询本地镜像漏洞列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulImageExportJob(
            self,
            request: models.CreateVulImageExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateVulImageExportJobResponse:
        """
        创建受漏洞影响的镜像导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulImageExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulImageExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVulScanTask(
            self,
            request: models.CreateVulScanTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVulScanTaskResponse:
        """
        创建漏洞扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVulScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVulScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebVulExportJob(
            self,
            request: models.CreateWebVulExportJobRequest,
            opts: Dict = None,
    ) -> models.CreateWebVulExportJobResponse:
        """
        创建web漏洞导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebVulExportJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebVulExportJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAbnormalProcessRules(
            self,
            request: models.DeleteAbnormalProcessRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAbnormalProcessRulesResponse:
        """
        删除运行异常进程策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAbnormalProcessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAbnormalProcessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccessControlRules(
            self,
            request: models.DeleteAccessControlRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAccessControlRulesResponse:
        """
        删除运行访问控制策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccessControlRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccessControlRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteComplianceAssetPolicySetFromWhitelist(
            self,
            request: models.DeleteComplianceAssetPolicySetFromWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteComplianceAssetPolicySetFromWhitelistResponse:
        """
        移除安全合规忽略(资产+检测项)列表，不显示指定的检查项包含的资产内容
        参考的AddCompliancePolicyAssetSetToWhitelist，除输入字段外，其它应该是一致的，如果有不同可能是定义的不对
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteComplianceAssetPolicySetFromWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteComplianceAssetPolicySetFromWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompliancePolicyAssetSetFromWhitelist(
            self,
            request: models.DeleteCompliancePolicyAssetSetFromWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteCompliancePolicyAssetSetFromWhitelistResponse:
        """
        新增安全合规忽略(检测项+资产)列表，不显示指定的检查项包含的资产内容
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompliancePolicyAssetSetFromWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompliancePolicyAssetSetFromWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompliancePolicyItemFromWhitelist(
            self,
            request: models.DeleteCompliancePolicyItemFromWhitelistRequest,
            opts: Dict = None,
    ) -> models.DeleteCompliancePolicyItemFromWhitelistResponse:
        """
        产品重构优化，这几个接口已经没有调用了

        从白名单中删除将指定的检测项。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompliancePolicyItemFromWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompliancePolicyItemFromWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEscapeWhiteList(
            self,
            request: models.DeleteEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteEscapeWhiteListResponse:
        """
        删除逃逸白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIgnoreVul(
            self,
            request: models.DeleteIgnoreVulRequest,
            opts: Dict = None,
    ) -> models.DeleteIgnoreVulResponse:
        """
        取消漏洞扫描忽略漏洞
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIgnoreVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIgnoreVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteK8sApiAbnormalRule(
            self,
            request: models.DeleteK8sApiAbnormalRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteK8sApiAbnormalRuleResponse:
        """
        删除k8sapi异常事件规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteK8sApiAbnormalRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteK8sApiAbnormalRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachine(
            self,
            request: models.DeleteMachineRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineResponse:
        """
        卸载Agent客户端
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkFirewallPolicyDetail(
            self,
            request: models.DeleteNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkFirewallPolicyDetailResponse:
        """
        容器网络创建网络策略删除任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRaspRules(
            self,
            request: models.DeleteRaspRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRaspRulesResponse:
        """
        删除漏洞防御白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellEvents(
            self,
            request: models.DeleteReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellEventsResponse:
        """
        删除运行时反弹shell事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReverseShellWhiteLists(
            self,
            request: models.DeleteReverseShellWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DeleteReverseShellWhiteListsResponse:
        """
        删除运行时反弹shell白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReverseShellWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReverseShellWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskSyscallEvents(
            self,
            request: models.DeleteRiskSyscallEventsRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskSyscallEventsResponse:
        """
        删除运行时高危系统调用事件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskSyscallEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskSyscallEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRiskSyscallWhiteLists(
            self,
            request: models.DeleteRiskSyscallWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DeleteRiskSyscallWhiteListsResponse:
        """
        删除运行时高危系统调用白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRiskSyscallWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRiskSyscallWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSearchTemplate(
            self,
            request: models.DeleteSearchTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSearchTemplateResponse:
        """
        删除检索模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSearchTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSearchTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeABTestConfig(
            self,
            request: models.DescribeABTestConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeABTestConfigResponse:
        """
        获取用户当前灰度配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeABTestConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeABTestConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessDetail(
            self,
            request: models.DescribeAbnormalProcessDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessDetailResponse:
        """
        查询运行时异常进程事件详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessEventTendency(
            self,
            request: models.DescribeAbnormalProcessEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessEventTendencyResponse:
        """
        查询待处理异常进程事件趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessEvents(
            self,
            request: models.DescribeAbnormalProcessEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessEventsResponse:
        """
        查询运行时异常进程事件列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessLevelSummary(
            self,
            request: models.DescribeAbnormalProcessLevelSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessLevelSummaryResponse:
        """
        统计异常进程各威胁等级待处理事件数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessLevelSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessLevelSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessRuleDetail(
            self,
            request: models.DescribeAbnormalProcessRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessRuleDetailResponse:
        """
        查询运行时异常策略详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAbnormalProcessRules(
            self,
            request: models.DescribeAbnormalProcessRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAbnormalProcessRulesResponse:
        """
        查询运行时异常进程策略列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAbnormalProcessRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAbnormalProcessRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlDetail(
            self,
            request: models.DescribeAccessControlDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlDetailResponse:
        """
        查询运行时访问控制事件的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlEvents(
            self,
            request: models.DescribeAccessControlEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlEventsResponse:
        """
        查询运行时访问控制事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlEventsExport(
            self,
            request: models.DescribeAccessControlEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlEventsExportResponse:
        """
        查询运行时访问控制事件列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlRuleDetail(
            self,
            request: models.DescribeAccessControlRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlRuleDetailResponse:
        """
        查询运行时访问控制策略详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessControlRules(
            self,
            request: models.DescribeAccessControlRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessControlRulesResponse:
        """
        查询运行访问控制策略列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessControlRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessControlRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAffectedClusterCount(
            self,
            request: models.DescribeAffectedClusterCountRequest,
            opts: Dict = None,
    ) -> models.DescribeAffectedClusterCountResponse:
        """
        获取受影响的集群数量，返回数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAffectedClusterCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAffectedClusterCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAffectedNodeList(
            self,
            request: models.DescribeAffectedNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeAffectedNodeListResponse:
        """
        查询节点类型的影响范围，返回节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAffectedNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAffectedNodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAffectedWorkloadList(
            self,
            request: models.DescribeAffectedWorkloadListRequest,
            opts: Dict = None,
    ) -> models.DescribeAffectedWorkloadListResponse:
        """
        查询workload类型的影响范围，返回workload列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAffectedWorkloadList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAffectedWorkloadListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentDaemonSetCmd(
            self,
            request: models.DescribeAgentDaemonSetCmdRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentDaemonSetCmdResponse:
        """
        查询平行容器安装命令
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentDaemonSetCmd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentDaemonSetCmdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstallCommand(
            self,
            request: models.DescribeAgentInstallCommandRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstallCommandResponse:
        """
        查询agent安装命令
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstallCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstallCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetAppServiceList(
            self,
            request: models.DescribeAssetAppServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetAppServiceListResponse:
        """
        容器安全查询app服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetAppServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetAppServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetClusterList(
            self,
            request: models.DescribeAssetClusterListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetClusterListResponse:
        """
        查询集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetClusterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetClusterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetComponentList(
            self,
            request: models.DescribeAssetComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetComponentListResponse:
        """
        容器安全搜索查询容器组件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetContainerDetail(
            self,
            request: models.DescribeAssetContainerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetContainerDetailResponse:
        """
        查询容器详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetContainerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetContainerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetContainerList(
            self,
            request: models.DescribeAssetContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetContainerListResponse:
        """
        搜索查询容器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetDBServiceList(
            self,
            request: models.DescribeAssetDBServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetDBServiceListResponse:
        """
        容器安全查询db服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetDBServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetDBServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetHostDetail(
            self,
            request: models.DescribeAssetHostDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetHostDetailResponse:
        """
        查询主机详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetHostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetHostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetHostList(
            self,
            request: models.DescribeAssetHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetHostListResponse:
        """
        容器安全搜索查询主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageBindRuleInfo(
            self,
            request: models.DescribeAssetImageBindRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageBindRuleInfoResponse:
        """
        镜像绑定规则列表信息，包含运行时访问控制和异常进程公用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageBindRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageBindRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageDetail(
            self,
            request: models.DescribeAssetImageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageDetailResponse:
        """
        查询镜像详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageHostList(
            self,
            request: models.DescribeAssetImageHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageHostListResponse:
        """
        容器安全查询镜像关联主机
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageList(
            self,
            request: models.DescribeAssetImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageListResponse:
        """
        容器安全搜索查询镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryAssetStatus(
            self,
            request: models.DescribeAssetImageRegistryAssetStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryAssetStatusResponse:
        """
        查看镜像仓库资产更新进度状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryAssetStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryAssetStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryDetail(
            self,
            request: models.DescribeAssetImageRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryDetailResponse:
        """
        镜像仓库镜像仓库列表详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryList(
            self,
            request: models.DescribeAssetImageRegistryListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryListResponse:
        """
        镜像仓库镜像仓库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryListExport(
            self,
            request: models.DescribeAssetImageRegistryListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryListExportResponse:
        """
        镜像仓库镜像列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRegistryDetail(
            self,
            request: models.DescribeAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRegistryDetailResponse:
        """
        查看单个镜像仓库详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRegistryList(
            self,
            request: models.DescribeAssetImageRegistryRegistryListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRegistryListResponse:
        """
        镜像仓库仓库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRegistryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRegistryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRiskInfoList(
            self,
            request: models.DescribeAssetImageRegistryRiskInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRiskInfoListResponse:
        """
        镜像仓库查询镜像高危行为列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRiskInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRiskInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryRiskListExport(
            self,
            request: models.DescribeAssetImageRegistryRiskListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryRiskListExportResponse:
        """
        镜像仓库敏感信息列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryRiskListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryRiskListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryScanStatusOneKey(
            self,
            request: models.DescribeAssetImageRegistryScanStatusOneKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryScanStatusOneKeyResponse:
        """
        镜像仓库查询一键镜像扫描状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryScanStatusOneKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryScanStatusOneKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistrySummary(
            self,
            request: models.DescribeAssetImageRegistrySummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistrySummaryResponse:
        """
        镜像仓库查询镜像统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistrySummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistrySummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVirusList(
            self,
            request: models.DescribeAssetImageRegistryVirusListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVirusListResponse:
        """
        镜像仓库查询木马病毒列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVirusListExport(
            self,
            request: models.DescribeAssetImageRegistryVirusListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVirusListExportResponse:
        """
        镜像仓库木马信息列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVirusListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVirusListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVulList(
            self,
            request: models.DescribeAssetImageRegistryVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVulListResponse:
        """
        镜像仓库查询镜像漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRegistryVulListExport(
            self,
            request: models.DescribeAssetImageRegistryVulListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRegistryVulListExportResponse:
        """
        镜像仓库漏洞列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRegistryVulListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRegistryVulListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRiskList(
            self,
            request: models.DescribeAssetImageRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRiskListResponse:
        """
        容器安全查询镜像风险列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageRiskListExport(
            self,
            request: models.DescribeAssetImageRiskListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageRiskListExportResponse:
        """
        容器安全搜索查询镜像风险列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageRiskListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageRiskListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageScanSetting(
            self,
            request: models.DescribeAssetImageScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageScanSettingResponse:
        """
        获取镜像扫描设置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageScanStatus(
            self,
            request: models.DescribeAssetImageScanStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageScanStatusResponse:
        """
        容器安全查询镜像扫描状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageScanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageScanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageScanTask(
            self,
            request: models.DescribeAssetImageScanTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageScanTaskResponse:
        """
        查询正在一键扫描的镜像扫描taskid
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageSimpleList(
            self,
            request: models.DescribeAssetImageSimpleListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageSimpleListResponse:
        """
        容器安全搜索查询镜像简略信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageSimpleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageSimpleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVirusList(
            self,
            request: models.DescribeAssetImageVirusListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVirusListResponse:
        """
        容器安全查询镜像病毒列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVirusListExport(
            self,
            request: models.DescribeAssetImageVirusListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVirusListExportResponse:
        """
        容器安全搜索查询镜像木马列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVirusListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVirusListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVulList(
            self,
            request: models.DescribeAssetImageVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVulListResponse:
        """
        容器安全查询镜像漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetImageVulListExport(
            self,
            request: models.DescribeAssetImageVulListExportRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetImageVulListExportResponse:
        """
        容器安全搜索查询镜像漏洞列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetImageVulListExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetImageVulListExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetPortList(
            self,
            request: models.DescribeAssetPortListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetPortListResponse:
        """
        容器安全搜索查询端口占用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetPortList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetPortListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetProcessList(
            self,
            request: models.DescribeAssetProcessListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetProcessListResponse:
        """
        容器安全搜索查询进程列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetProcessList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetProcessListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSummary(
            self,
            request: models.DescribeAssetSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSummaryResponse:
        """
        查询账户容器、镜像等统计信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSuperNodeList(
            self,
            request: models.DescribeAssetSuperNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSuperNodeListResponse:
        """
        查询超级节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSuperNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSuperNodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetSyncLastTime(
            self,
            request: models.DescribeAssetSyncLastTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetSyncLastTimeResponse:
        """
        查询资产同步最近时间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetSyncLastTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetSyncLastTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssetWebServiceList(
            self,
            request: models.DescribeAssetWebServiceListRequest,
            opts: Dict = None,
    ) -> models.DescribeAssetWebServiceListResponse:
        """
        容器安全查询web服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssetWebServiceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssetWebServiceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoAuthorizedRuleHost(
            self,
            request: models.DescribeAutoAuthorizedRuleHostRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoAuthorizedRuleHostResponse:
        """
        查询自动授权规则授权范围主机信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoAuthorizedRuleHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoAuthorizedRuleHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckItemList(
            self,
            request: models.DescribeCheckItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckItemListResponse:
        """
        查询所有检查项接口，返回总数和检查项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        查询单个集群的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodes(
            self,
            request: models.DescribeClusterNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodesResponse:
        """
        查询集群节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSummary(
            self,
            request: models.DescribeClusterSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSummaryResponse:
        """
        查询用户集群资产总览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceAssetDetailInfo(
            self,
            request: models.DescribeComplianceAssetDetailInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceAssetDetailInfoResponse:
        """
        查询某个资产的详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceAssetDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceAssetDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceAssetList(
            self,
            request: models.DescribeComplianceAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceAssetListResponse:
        """
        查询某类资产的列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceAssetPolicyItemList(
            self,
            request: models.DescribeComplianceAssetPolicyItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceAssetPolicyItemListResponse:
        """
        查询某资产下的检测项列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceAssetPolicyItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceAssetPolicyItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePeriodTaskList(
            self,
            request: models.DescribeCompliancePeriodTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePeriodTaskListResponse:
        """
        查询合规检测的定时任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePeriodTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePeriodTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePolicyItemAffectedAssetList(
            self,
            request: models.DescribeCompliancePolicyItemAffectedAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePolicyItemAffectedAssetListResponse:
        """
        按照 检测项 → 资产 的两级层次展开的第二层级：资产层级。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePolicyItemAffectedAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePolicyItemAffectedAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePolicyItemAffectedSummary(
            self,
            request: models.DescribeCompliancePolicyItemAffectedSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePolicyItemAffectedSummaryResponse:
        """
        按照 检测项 → 资产 的两级层次展开的第一层级：检测项层级。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePolicyItemAffectedSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePolicyItemAffectedSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceScanFailedAssetList(
            self,
            request: models.DescribeComplianceScanFailedAssetListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceScanFailedAssetListResponse:
        """
        按照 资产 → 检测项 二层结构展示的信息。这里查询第一层 资产的通过率汇总信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceScanFailedAssetList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceScanFailedAssetListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceTaskAssetSummary(
            self,
            request: models.DescribeComplianceTaskAssetSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceTaskAssetSummaryResponse:
        """
        查询上次任务的资产通过率汇总信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceTaskAssetSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceTaskAssetSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceTaskPolicyItemSummaryList(
            self,
            request: models.DescribeComplianceTaskPolicyItemSummaryListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceTaskPolicyItemSummaryListResponse:
        """
        查询最近一次任务发现的检测项的汇总信息列表，按照 检测项 → 资产 的两级层次展开。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceTaskPolicyItemSummaryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceTaskPolicyItemSummaryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComplianceWhitelistItemList(
            self,
            request: models.DescribeComplianceWhitelistItemListRequest,
            opts: Dict = None,
    ) -> models.DescribeComplianceWhitelistItemListResponse:
        """
        查询白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComplianceWhitelistItemList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComplianceWhitelistItemListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerAssetSummary(
            self,
            request: models.DescribeContainerAssetSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerAssetSummaryResponse:
        """
        查询容器资产概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerAssetSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerAssetSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContainerSecEventSummary(
            self,
            request: models.DescribeContainerSecEventSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeContainerSecEventSummaryResponse:
        """
        查询容器安全未处理事件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContainerSecEventSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContainerSecEventSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeESAggregations(
            self,
            request: models.DescribeESAggregationsRequest,
            opts: Dict = None,
    ) -> models.DescribeESAggregationsResponse:
        """
        获取ES字段聚合结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeESAggregations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeESAggregationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeESHits(
            self,
            request: models.DescribeESHitsRequest,
            opts: Dict = None,
    ) -> models.DescribeESHitsResponse:
        """
        获取ES查询文档列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeESHits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeESHitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmergencyVulList(
            self,
            request: models.DescribeEmergencyVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeEmergencyVulListResponse:
        """
        查询应急漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmergencyVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmergencyVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventDetail(
            self,
            request: models.DescribeEscapeEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventDetailResponse:
        """
        DescribeEscapeEventDetail  查询容器逃逸事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventInfo(
            self,
            request: models.DescribeEscapeEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventInfoResponse:
        """
        DescribeEscapeEventInfo 查询容器逃逸事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventTendency(
            self,
            request: models.DescribeEscapeEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventTendencyResponse:
        """
        查询待处理逃逸事件趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeEventTypeSummary(
            self,
            request: models.DescribeEscapeEventTypeSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeEventTypeSummaryResponse:
        """
        统计容器逃逸各事件类型和待处理事件数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeEventTypeSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeEventTypeSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeRuleInfo(
            self,
            request: models.DescribeEscapeRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeRuleInfoResponse:
        """
        DescribeEscapeRuleInfo 查询容器逃逸扫描规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeSafeState(
            self,
            request: models.DescribeEscapeSafeStateRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeSafeStateResponse:
        """
        DescribeEscapeSafeState 查询容器逃逸安全状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeSafeState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeSafeStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEscapeWhiteList(
            self,
            request: models.DescribeEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeEscapeWhiteListResponse:
        """
        查询逃逸白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventEscapeImageList(
            self,
            request: models.DescribeEventEscapeImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeEventEscapeImageListResponse:
        """
        DescribeRiskContainerImageList查询风险容器镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventEscapeImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventEscapeImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobDownloadURL(
            self,
            request: models.DescribeExportJobDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobDownloadURLResponse:
        """
        查询导出任务下载URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobManageList(
            self,
            request: models.DescribeExportJobManageListRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobManageListResponse:
        """
        查询导出任务管理列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobManageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobManageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExportJobResult(
            self,
            request: models.DescribeExportJobResultRequest,
            opts: Dict = None,
    ) -> models.DescribeExportJobResultResponse:
        """
        查询导出接口进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExportJobResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportJobResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAuthorizedInfo(
            self,
            request: models.DescribeImageAuthorizedInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAuthorizedInfoResponse:
        """
        DescribeImageAuthorizedInfo  查询镜像授权信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAuthorizedInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAuthorizedInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAutoAuthorizedLogList(
            self,
            request: models.DescribeImageAutoAuthorizedLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAutoAuthorizedLogListResponse:
        """
        查询镜像自动授权结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAutoAuthorizedLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAutoAuthorizedLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAutoAuthorizedRule(
            self,
            request: models.DescribeImageAutoAuthorizedRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAutoAuthorizedRuleResponse:
        """
        查询本地镜像自动授权规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAutoAuthorizedRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAutoAuthorizedRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageAutoAuthorizedTaskList(
            self,
            request: models.DescribeImageAutoAuthorizedTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageAutoAuthorizedTaskListResponse:
        """
        查询镜像自动授权任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageAutoAuthorizedTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageAutoAuthorizedTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageComponentList(
            self,
            request: models.DescribeImageComponentListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageComponentListResponse:
        """
        查询本地镜像组件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageComponentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageComponentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryNamespaceList(
            self,
            request: models.DescribeImageRegistryNamespaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryNamespaceListResponse:
        """
        查询用户镜像仓库下的命令空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryNamespaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryNamespaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRegistryTimingScanTask(
            self,
            request: models.DescribeImageRegistryTimingScanTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRegistryTimingScanTaskResponse:
        """
        镜像仓库查看定时任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRegistryTimingScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRegistryTimingScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRiskSummary(
            self,
            request: models.DescribeImageRiskSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRiskSummaryResponse:
        """
        查询本地镜像风险概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRiskSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRiskSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageRiskTendency(
            self,
            request: models.DescribeImageRiskTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeImageRiskTendencyResponse:
        """
        查询容器安全本地镜像风险趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageRiskTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageRiskTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImageSimpleList(
            self,
            request: models.DescribeImageSimpleListRequest,
            opts: Dict = None,
    ) -> models.DescribeImageSimpleListResponse:
        """
        DescribeImageSimpleList 查询全部镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImageSimpleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageSimpleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexList(
            self,
            request: models.DescribeIndexListRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexListResponse:
        """
        获取索引列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInspectionReport(
            self,
            request: models.DescribeInspectionReportRequest,
            opts: Dict = None,
    ) -> models.DescribeInspectionReportResponse:
        """
        查询检查报告
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInspectionReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInspectionReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalEventInfo(
            self,
            request: models.DescribeK8sApiAbnormalEventInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalEventInfoResponse:
        """
        查询k8s api 异常事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalEventInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalEventInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalEventList(
            self,
            request: models.DescribeK8sApiAbnormalEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalEventListResponse:
        """
        查询k8s api异常事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalRuleInfo(
            self,
            request: models.DescribeK8sApiAbnormalRuleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalRuleInfoResponse:
        """
        查询k8sapi异常请求规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalRuleList(
            self,
            request: models.DescribeK8sApiAbnormalRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalRuleListResponse:
        """
        查询k8sapi异常请求规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalRuleScopeList(
            self,
            request: models.DescribeK8sApiAbnormalRuleScopeListRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalRuleScopeListResponse:
        """
        查询k8sapi 异常规则中范围列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalRuleScopeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalRuleScopeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalSummary(
            self,
            request: models.DescribeK8sApiAbnormalSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalSummaryResponse:
        """
        查询k8sapi异常事件统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeK8sApiAbnormalTendency(
            self,
            request: models.DescribeK8sApiAbnormalTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeK8sApiAbnormalTendencyResponse:
        """
        查询k8sapi异常事件趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeK8sApiAbnormalTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeK8sApiAbnormalTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogStorageStatistic(
            self,
            request: models.DescribeLogStorageStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeLogStorageStatisticResponse:
        """
        获取日志检索容量使用统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogStorageStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogStorageStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallAuditRecord(
            self,
            request: models.DescribeNetworkFirewallAuditRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallAuditRecordResponse:
        """
        查询集群策略审计列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallAuditRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallAuditRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallClusterList(
            self,
            request: models.DescribeNetworkFirewallClusterListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallClusterListResponse:
        """
        查询集群策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallClusterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallClusterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallClusterRefreshStatus(
            self,
            request: models.DescribeNetworkFirewallClusterRefreshStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallClusterRefreshStatusResponse:
        """
        容器网络查询资产任务进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallClusterRefreshStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallClusterRefreshStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallNamespaceLabelList(
            self,
            request: models.DescribeNetworkFirewallNamespaceLabelListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallNamespaceLabelListResponse:
        """
        查询集群网络空间标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallNamespaceLabelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallNamespaceLabelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallNamespaceList(
            self,
            request: models.DescribeNetworkFirewallNamespaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallNamespaceListResponse:
        """
        查询集群网络空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallNamespaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallNamespaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPodLabelsList(
            self,
            request: models.DescribeNetworkFirewallPodLabelsListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPodLabelsListResponse:
        """
        查询集群网络pod标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPodLabelsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPodLabelsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyDetail(
            self,
            request: models.DescribeNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyDetailResponse:
        """
        容器网络集群查看策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyDiscover(
            self,
            request: models.DescribeNetworkFirewallPolicyDiscoverRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyDiscoverResponse:
        """
        容器网络查询网络策略自动发现任务进度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyDiscover"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyDiscoverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyList(
            self,
            request: models.DescribeNetworkFirewallPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyListResponse:
        """
        查询集群网络策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyStatus(
            self,
            request: models.DescribeNetworkFirewallPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyStatusResponse:
        """
        容器网络查询网络策略策略执行状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkFirewallPolicyYamlDetail(
            self,
            request: models.DescribeNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkFirewallPolicyYamlDetailResponse:
        """
        容器网络集群查看Yaml网络策略详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewestVul(
            self,
            request: models.DescribeNewestVulRequest,
            opts: Dict = None,
    ) -> models.DescribeNewestVulResponse:
        """
        查询最新披露漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewestVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewestVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostPayDetail(
            self,
            request: models.DescribePostPayDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePostPayDetailResponse:
        """
        DescribePostPayDetail  查询后付费详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostPayDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostPayDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProVersionInfo(
            self,
            request: models.DescribeProVersionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProVersionInfoResponse:
        """
        DescribeProVersionInfo  查询专业版需购买信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProVersionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProVersionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePromotionActivity(
            self,
            request: models.DescribePromotionActivityRequest,
            opts: Dict = None,
    ) -> models.DescribePromotionActivityResponse:
        """
        查询促销活动
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePromotionActivity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePromotionActivityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicKey(
            self,
            request: models.DescribePublicKeyRequest,
            opts: Dict = None,
    ) -> models.DescribePublicKeyResponse:
        """
        获取公钥
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurchaseStateInfo(
            self,
            request: models.DescribePurchaseStateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePurchaseStateInfoResponse:
        """
        DescribePurchaseStateInfo 查询容器安全服务已购买信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurchaseStateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurchaseStateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRaspRuleVuls(
            self,
            request: models.DescribeRaspRuleVulsRequest,
            opts: Dict = None,
    ) -> models.DescribeRaspRuleVulsResponse:
        """
        获取漏洞防御白名单漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRaspRuleVuls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRaspRuleVulsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRaspRules(
            self,
            request: models.DescribeRaspRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRaspRulesResponse:
        """
        查询支持防御的漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRefreshTask(
            self,
            request: models.DescribeRefreshTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRefreshTaskResponse:
        """
        查询刷新任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRefreshTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRefreshTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellDetail(
            self,
            request: models.DescribeReverseShellDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellDetailResponse:
        """
        查询运行时反弹shell事件详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEvents(
            self,
            request: models.DescribeReverseShellEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventsResponse:
        """
        查询运行时反弹shell事件列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellEventsExport(
            self,
            request: models.DescribeReverseShellEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellEventsExportResponse:
        """
        查询运行时反弹shell事件列表信息导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellWhiteListDetail(
            self,
            request: models.DescribeReverseShellWhiteListDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellWhiteListDetailResponse:
        """
        查询运行时反弹shell白名单详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellWhiteListDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellWhiteListDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReverseShellWhiteLists(
            self,
            request: models.DescribeReverseShellWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DescribeReverseShellWhiteListsResponse:
        """
        查询运行时运行时反弹shell白名单列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReverseShellWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReverseShellWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsEventDetail(
            self,
            request: models.DescribeRiskDnsEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsEventDetailResponse:
        """
        查询恶意请求事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskDnsList(
            self,
            request: models.DescribeRiskDnsListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskDnsListResponse:
        """
        查询恶意请求事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskDnsList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskDnsListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskList(
            self,
            request: models.DescribeRiskListRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskListResponse:
        """
        查询最近一次任务发现的风险项的信息列表，支持根据特殊字段进行过滤
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallDetail(
            self,
            request: models.DescribeRiskSyscallDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallDetailResponse:
        """
        查询高危系统调用事件详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallEvents(
            self,
            request: models.DescribeRiskSyscallEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallEventsResponse:
        """
        查询运行时运行时高危系统调用列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallEventsExport(
            self,
            request: models.DescribeRiskSyscallEventsExportRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallEventsExportResponse:
        """
        运行时高危系统调用列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallEventsExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallEventsExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallNames(
            self,
            request: models.DescribeRiskSyscallNamesRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallNamesResponse:
        """
        查询运行时高危系统调用系统名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallWhiteListDetail(
            self,
            request: models.DescribeRiskSyscallWhiteListDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallWhiteListDetailResponse:
        """
        查询运行时高危系统调用白名单详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallWhiteListDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallWhiteListDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRiskSyscallWhiteLists(
            self,
            request: models.DescribeRiskSyscallWhiteListsRequest,
            opts: Dict = None,
    ) -> models.DescribeRiskSyscallWhiteListsResponse:
        """
        查询运行时高危系统调用白名单列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRiskSyscallWhiteLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRiskSyscallWhiteListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScanIgnoreVulList(
            self,
            request: models.DescribeScanIgnoreVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeScanIgnoreVulListResponse:
        """
        查询扫描忽略的漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScanIgnoreVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScanIgnoreVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchExportList(
            self,
            request: models.DescribeSearchExportListRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchExportListResponse:
        """
        导出ES查询文档列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchExportList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchExportListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchLogs(
            self,
            request: models.DescribeSearchLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchLogsResponse:
        """
        获取历史搜索记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchTemplates(
            self,
            request: models.DescribeSearchTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchTemplatesResponse:
        """
        获取快速检索列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecEventsTendency(
            self,
            request: models.DescribeSecEventsTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeSecEventsTendencyResponse:
        """
        查询容器运行时安全事件趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecEventsTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecEventsTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogAlertMsg(
            self,
            request: models.DescribeSecLogAlertMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogAlertMsgResponse:
        """
        查询安全日志告警信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogAlertMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogAlertMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogCleanSettingInfo(
            self,
            request: models.DescribeSecLogCleanSettingInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogCleanSettingInfoResponse:
        """
        查询安全日志清理设置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogCleanSettingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogCleanSettingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryClsOptions(
            self,
            request: models.DescribeSecLogDeliveryClsOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryClsOptionsResponse:
        """
        查询安全日志投递cls可选项
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryClsOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryClsOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryClsSetting(
            self,
            request: models.DescribeSecLogDeliveryClsSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryClsSettingResponse:
        """
        查询安全日志投递Cls配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryClsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryClsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryKafkaOptions(
            self,
            request: models.DescribeSecLogDeliveryKafkaOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryKafkaOptionsResponse:
        """
        查询安全日志投递kafka可选项
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryKafkaOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryKafkaOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogDeliveryKafkaSetting(
            self,
            request: models.DescribeSecLogDeliveryKafkaSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogDeliveryKafkaSettingResponse:
        """
        查询安全日志投递kafka配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogDeliveryKafkaSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogDeliveryKafkaSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogJoinObjectList(
            self,
            request: models.DescribeSecLogJoinObjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogJoinObjectListResponse:
        """
        查询安全日志接入对象列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogJoinObjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogJoinObjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogJoinTypeList(
            self,
            request: models.DescribeSecLogJoinTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogJoinTypeListResponse:
        """
        查询安全日志接入列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogJoinTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogJoinTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogKafkaUIN(
            self,
            request: models.DescribeSecLogKafkaUINRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogKafkaUINResponse:
        """
        查询安全日志KafkaUIN
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogKafkaUIN"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogKafkaUINResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecLogVasInfo(
            self,
            request: models.DescribeSecLogVasInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecLogVasInfoResponse:
        """
        查询安全日志商品信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecLogVasInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecLogVasInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSuperNodePodList(
            self,
            request: models.DescribeSuperNodePodListRequest,
            opts: Dict = None,
    ) -> models.DescribeSuperNodePodListResponse:
        """
        查询超级节点pod列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSuperNodePodList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSuperNodePodListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportDefenceVul(
            self,
            request: models.DescribeSupportDefenceVulRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportDefenceVulResponse:
        """
        查询支持防御的漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportDefenceVul"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportDefenceVulResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemVulList(
            self,
            request: models.DescribeSystemVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemVulListResponse:
        """
        查询系统漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResultSummary(
            self,
            request: models.DescribeTaskResultSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultSummaryResponse:
        """
        查询检查结果总览，返回受影响的节点数量，返回7天的数据，总共7个
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResultSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTcssSummary(
            self,
            request: models.DescribeTcssSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeTcssSummaryResponse:
        """
        查询容器安全概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTcssSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTcssSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnauthorizedCoresTendency(
            self,
            request: models.DescribeUnauthorizedCoresTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeUnauthorizedCoresTendencyResponse:
        """
        查询当天未授权核数趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnauthorizedCoresTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnauthorizedCoresTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnfinishRefreshTask(
            self,
            request: models.DescribeUnfinishRefreshTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeUnfinishRefreshTaskResponse:
        """
        查询未完成的刷新资产任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnfinishRefreshTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnfinishRefreshTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCluster(
            self,
            request: models.DescribeUserClusterRequest,
            opts: Dict = None,
    ) -> models.DescribeUserClusterResponse:
        """
        安全概览和集群安全页进入调用该接口，查询用户集群相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserPodList(
            self,
            request: models.DescribeUserPodListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserPodListResponse:
        """
        获取用户的pod列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserPodList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserPodListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeValueAddedSrvInfo(
            self,
            request: models.DescribeValueAddedSrvInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeValueAddedSrvInfoResponse:
        """
        DescribeValueAddedSrvInfo查询增值服务需购买信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeValueAddedSrvInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeValueAddedSrvInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSampleDetail(
            self,
            request: models.DescribeVirusAutoIsolateSampleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSampleDetailResponse:
        """
        查询木马自动隔离样本详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSampleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSampleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSampleDownloadURL(
            self,
            request: models.DescribeVirusAutoIsolateSampleDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSampleDownloadURLResponse:
        """
        查询木马自动隔离样本下载链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSampleDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSampleDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSampleList(
            self,
            request: models.DescribeVirusAutoIsolateSampleListRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSampleListResponse:
        """
        查询木马自动隔离样本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSampleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSampleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusAutoIsolateSetting(
            self,
            request: models.DescribeVirusAutoIsolateSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusAutoIsolateSettingResponse:
        """
        查询木马自动隔离设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusAutoIsolateSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusAutoIsolateSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusDetail(
            self,
            request: models.DescribeVirusDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusDetailResponse:
        """
        运行时查询木马文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusEventTendency(
            self,
            request: models.DescribeVirusEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusEventTendencyResponse:
        """
        查询木马事件趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusList(
            self,
            request: models.DescribeVirusListRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusListResponse:
        """
        查询运行时文件查杀事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusManualScanEstimateTimeout(
            self,
            request: models.DescribeVirusManualScanEstimateTimeoutRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusManualScanEstimateTimeoutResponse:
        """
        查询木马一键检测预估超时时间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusManualScanEstimateTimeout"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusManualScanEstimateTimeoutResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusMonitorSetting(
            self,
            request: models.DescribeVirusMonitorSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusMonitorSettingResponse:
        """
        运行时查询文件查杀实时监控设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusMonitorSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusMonitorSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusSampleDownloadUrl(
            self,
            request: models.DescribeVirusSampleDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusSampleDownloadUrlResponse:
        """
        查询木马样本下载url
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusSampleDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusSampleDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusScanSetting(
            self,
            request: models.DescribeVirusScanSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusScanSettingResponse:
        """
        运行时查询文件查杀设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusScanTaskStatus(
            self,
            request: models.DescribeVirusScanTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusScanTaskStatusResponse:
        """
        运行时查询文件查杀任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusScanTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusScanTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusScanTimeoutSetting(
            self,
            request: models.DescribeVirusScanTimeoutSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusScanTimeoutSettingResponse:
        """
        运行时文件扫描超时设置查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusScanTimeoutSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusScanTimeoutSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusSummary(
            self,
            request: models.DescribeVirusSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusSummaryResponse:
        """
        运行时查询木马概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVirusTaskList(
            self,
            request: models.DescribeVirusTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeVirusTaskListResponse:
        """
        运行时查询文件查杀任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVirusTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVirusTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulContainerList(
            self,
            request: models.DescribeVulContainerListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulContainerListResponse:
        """
        查询受漏洞的容器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulContainerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulContainerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEvent(
            self,
            request: models.DescribeVulDefenceEventRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventResponse:
        """
        查询漏洞防御事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEventDetail(
            self,
            request: models.DescribeVulDefenceEventDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventDetailResponse:
        """
        查询漏洞防御事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEventDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceEventTendency(
            self,
            request: models.DescribeVulDefenceEventTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceEventTendencyResponse:
        """
        查询漏洞防御攻击事件趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceEventTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceEventTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceHost(
            self,
            request: models.DescribeVulDefenceHostRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceHostResponse:
        """
        查询漏洞防御的主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefencePlugin(
            self,
            request: models.DescribeVulDefencePluginRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefencePluginResponse:
        """
        查询漏洞防御插件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefencePlugin"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefencePluginResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDefenceSetting(
            self,
            request: models.DescribeVulDefenceSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDefenceSettingResponse:
        """
        查询漏洞防御设置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulDetail(
            self,
            request: models.DescribeVulDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeVulDetailResponse:
        """
        查询漏洞详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulIgnoreLocalImageList(
            self,
            request: models.DescribeVulIgnoreLocalImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulIgnoreLocalImageListResponse:
        """
        查询漏洞扫描忽略的本地镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulIgnoreLocalImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulIgnoreLocalImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulIgnoreRegistryImageList(
            self,
            request: models.DescribeVulIgnoreRegistryImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulIgnoreRegistryImageListResponse:
        """
        查询漏洞扫描忽略的仓库镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulIgnoreRegistryImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulIgnoreRegistryImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulImageList(
            self,
            request: models.DescribeVulImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulImageListResponse:
        """
        查询漏洞影响的镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulImageSummary(
            self,
            request: models.DescribeVulImageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulImageSummaryResponse:
        """
        查询漏洞镜像统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulImageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulImageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLevelImageSummary(
            self,
            request: models.DescribeVulLevelImageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLevelImageSummaryResponse:
        """
        查询应急漏洞各威胁等级统计镜像数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLevelImageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLevelImageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulLevelSummary(
            self,
            request: models.DescribeVulLevelSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulLevelSummaryResponse:
        """
        查询漏洞各威胁等级统计数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulLevelSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulLevelSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulRegistryImageList(
            self,
            request: models.DescribeVulRegistryImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulRegistryImageListResponse:
        """
        查询漏洞影响的仓库镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulRegistryImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulRegistryImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanAuthorizedImageSummary(
            self,
            request: models.DescribeVulScanAuthorizedImageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanAuthorizedImageSummaryResponse:
        """
        统计漏洞扫描页已授权和未扫描镜像数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanAuthorizedImageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanAuthorizedImageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanInfo(
            self,
            request: models.DescribeVulScanInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanInfoResponse:
        """
        查询漏洞扫描任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulScanLocalImageList(
            self,
            request: models.DescribeVulScanLocalImageListRequest,
            opts: Dict = None,
    ) -> models.DescribeVulScanLocalImageListResponse:
        """
        查询漏洞扫描任务的本地镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulScanLocalImageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulScanLocalImageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulSummary(
            self,
            request: models.DescribeVulSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeVulSummaryResponse:
        """
        查询漏洞风险统计概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTendency(
            self,
            request: models.DescribeVulTendencyRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTendencyResponse:
        """
        查询本地镜像、仓库镜像中严重&高危的漏洞趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTendency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTendencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVulTopRanking(
            self,
            request: models.DescribeVulTopRankingRequest,
            opts: Dict = None,
    ) -> models.DescribeVulTopRankingResponse:
        """
        查询漏洞Top排名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVulTopRanking"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVulTopRankingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWarningRules(
            self,
            request: models.DescribeWarningRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeWarningRulesResponse:
        """
        获取告警策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWarningRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWarningRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebVulList(
            self,
            request: models.DescribeWebVulListRequest,
            opts: Dict = None,
    ) -> models.DescribeWebVulListResponse:
        """
        查询web应用漏洞列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebVulList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebVulListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportVirusList(
            self,
            request: models.ExportVirusListRequest,
            opts: Dict = None,
    ) -> models.ExportVirusListResponse:
        """
        运行时文件查杀事件列表导出
        """
        
        kwargs = {}
        kwargs["action"] = "ExportVirusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportVirusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InitializeUserComplianceEnvironment(
            self,
            request: models.InitializeUserComplianceEnvironmentRequest,
            opts: Dict = None,
    ) -> models.InitializeUserComplianceEnvironmentResponse:
        """
        为客户初始化合规基线的使用环境，创建必要的数据和选项。
        """
        
        kwargs = {}
        kwargs["action"] = "InitializeUserComplianceEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InitializeUserComplianceEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAbnormalProcessRuleStatus(
            self,
            request: models.ModifyAbnormalProcessRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAbnormalProcessRuleStatusResponse:
        """
        修改运行时异常进程策略的开启关闭状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAbnormalProcessRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAbnormalProcessRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAbnormalProcessStatus(
            self,
            request: models.ModifyAbnormalProcessStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAbnormalProcessStatusResponse:
        """
        修改异常进程事件的状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAbnormalProcessStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAbnormalProcessStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessControlRuleStatus(
            self,
            request: models.ModifyAccessControlRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessControlRuleStatusResponse:
        """
        修改运行时访问控制策略的状态，启用或者禁用
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessControlRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessControlRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessControlStatus(
            self,
            request: models.ModifyAccessControlStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessControlStatusResponse:
        """
        修改运行时访问控制事件状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessControlStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessControlStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAsset(
            self,
            request: models.ModifyAssetRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetResponse:
        """
        容器安全主机资产刷新
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetImageRegistryScanStop(
            self,
            request: models.ModifyAssetImageRegistryScanStopRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetImageRegistryScanStopResponse:
        """
        镜像仓库停止镜像扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetImageRegistryScanStop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetImageRegistryScanStopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetImageRegistryScanStopOneKey(
            self,
            request: models.ModifyAssetImageRegistryScanStopOneKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetImageRegistryScanStopOneKeyResponse:
        """
        镜像仓库停止镜像一键扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetImageRegistryScanStopOneKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetImageRegistryScanStopOneKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssetImageScanStop(
            self,
            request: models.ModifyAssetImageScanStopRequest,
            opts: Dict = None,
    ) -> models.ModifyAssetImageScanStopResponse:
        """
        容器安全停止镜像扫描
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssetImageScanStop"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssetImageScanStopResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCompliancePeriodTask(
            self,
            request: models.ModifyCompliancePeriodTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyCompliancePeriodTaskResponse:
        """
        修改定时任务的设置，包括检测周期、开启/禁用合规基准。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCompliancePeriodTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCompliancePeriodTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContainerNetStatus(
            self,
            request: models.ModifyContainerNetStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyContainerNetStatusResponse:
        """
        隔离容器网络状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContainerNetStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContainerNetStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefendStatus(
            self,
            request: models.ModifyDefendStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDefendStatusResponse:
        """
        修改防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEscapeEventStatus(
            self,
            request: models.ModifyEscapeEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyEscapeEventStatusResponse:
        """
        ModifyEscapeEventStatus  修改容器逃逸扫描事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEscapeEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEscapeEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEscapeRule(
            self,
            request: models.ModifyEscapeRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyEscapeRuleResponse:
        """
        ModifyEscapeRule  修改容器逃逸扫描规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEscapeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEscapeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEscapeWhiteList(
            self,
            request: models.ModifyEscapeWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyEscapeWhiteListResponse:
        """
        修改逃逸白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEscapeWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEscapeWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageAuthorized(
            self,
            request: models.ModifyImageAuthorizedRequest,
            opts: Dict = None,
    ) -> models.ModifyImageAuthorizedResponse:
        """
        批量授权镜像扫描V2.0
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageAuthorized"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageAuthorizedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyK8sApiAbnormalEventStatus(
            self,
            request: models.ModifyK8sApiAbnormalEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyK8sApiAbnormalEventStatusResponse:
        """
        修改k8sapi异常事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyK8sApiAbnormalEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyK8sApiAbnormalEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyK8sApiAbnormalRuleInfo(
            self,
            request: models.ModifyK8sApiAbnormalRuleInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyK8sApiAbnormalRuleInfoResponse:
        """
        修改k8sapi异常规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyK8sApiAbnormalRuleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyK8sApiAbnormalRuleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyK8sApiAbnormalRuleStatus(
            self,
            request: models.ModifyK8sApiAbnormalRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyK8sApiAbnormalRuleStatusResponse:
        """
        修改k8sapi异常事件规则状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyK8sApiAbnormalRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyK8sApiAbnormalRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRaspRules(
            self,
            request: models.ModifyRaspRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyRaspRulesResponse:
        """
        编辑或者创建java内存马白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRaspRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRaspRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReverseShellStatus(
            self,
            request: models.ModifyReverseShellStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyReverseShellStatusResponse:
        """
        修改反弹shell事件的状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReverseShellStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReverseShellStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskDnsEventStatus(
            self,
            request: models.ModifyRiskDnsEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskDnsEventStatusResponse:
        """
        编辑恶意请求事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskDnsEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskDnsEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRiskSyscallStatus(
            self,
            request: models.ModifyRiskSyscallStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRiskSyscallStatusResponse:
        """
        修改高危系统调用事件的状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRiskSyscallStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRiskSyscallStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogCleanSettingInfo(
            self,
            request: models.ModifySecLogCleanSettingInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogCleanSettingInfoResponse:
        """
        修改安全日志清理设置信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogCleanSettingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogCleanSettingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogDeliveryClsSetting(
            self,
            request: models.ModifySecLogDeliveryClsSettingRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogDeliveryClsSettingResponse:
        """
        更新安全日志-日志投递cls配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogDeliveryClsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogDeliveryClsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogDeliveryKafkaSetting(
            self,
            request: models.ModifySecLogDeliveryKafkaSettingRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogDeliveryKafkaSettingResponse:
        """
        更新安全日志投递kafka设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogDeliveryKafkaSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogDeliveryKafkaSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogJoinObjects(
            self,
            request: models.ModifySecLogJoinObjectsRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogJoinObjectsResponse:
        """
        修改安全日志接入对象
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogJoinObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogJoinObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogJoinState(
            self,
            request: models.ModifySecLogJoinStateRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogJoinStateResponse:
        """
        修改安全日志接入状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogJoinState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogJoinStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecLogKafkaUIN(
            self,
            request: models.ModifySecLogKafkaUINRequest,
            opts: Dict = None,
    ) -> models.ModifySecLogKafkaUINResponse:
        """
        修改安全日志kafkaUIN
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecLogKafkaUIN"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecLogKafkaUINResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusAutoIsolateExampleSwitch(
            self,
            request: models.ModifyVirusAutoIsolateExampleSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusAutoIsolateExampleSwitchResponse:
        """
        修改木马自动隔离样本开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusAutoIsolateExampleSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusAutoIsolateExampleSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusAutoIsolateSetting(
            self,
            request: models.ModifyVirusAutoIsolateSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusAutoIsolateSettingResponse:
        """
        修改木马自动隔离设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusAutoIsolateSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusAutoIsolateSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusFileStatus(
            self,
            request: models.ModifyVirusFileStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusFileStatusResponse:
        """
        运行时更新木马文件事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusFileStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusFileStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusMonitorSetting(
            self,
            request: models.ModifyVirusMonitorSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusMonitorSettingResponse:
        """
        运行时更新文件查杀实时监控设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusMonitorSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusMonitorSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusScanSetting(
            self,
            request: models.ModifyVirusScanSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusScanSettingResponse:
        """
        运行时更新文件查杀设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusScanSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusScanSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVirusScanTimeoutSetting(
            self,
            request: models.ModifyVirusScanTimeoutSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVirusScanTimeoutSettingResponse:
        """
        运行时文件扫描超时设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVirusScanTimeoutSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVirusScanTimeoutSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulDefenceEventStatus(
            self,
            request: models.ModifyVulDefenceEventStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyVulDefenceEventStatusResponse:
        """
        修改漏洞防御事件状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulDefenceEventStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulDefenceEventStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVulDefenceSetting(
            self,
            request: models.ModifyVulDefenceSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyVulDefenceSettingResponse:
        """
        编辑漏洞防御设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVulDefenceSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVulDefenceSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenTcssTrial(
            self,
            request: models.OpenTcssTrialRequest,
            opts: Dict = None,
    ) -> models.OpenTcssTrialResponse:
        """
        开通容器安全服务试用
        """
        
        kwargs = {}
        kwargs["action"] = "OpenTcssTrial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenTcssTrialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveAssetImageRegistryRegistryDetail(
            self,
            request: models.RemoveAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.RemoveAssetImageRegistryRegistryDetailResponse:
        """
        删除单个镜像仓库详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewImageAuthorizeState(
            self,
            request: models.RenewImageAuthorizeStateRequest,
            opts: Dict = None,
    ) -> models.RenewImageAuthorizeStateResponse:
        """
        RenewImageAuthorizeState   授权镜像扫描
        """
        
        kwargs = {}
        kwargs["action"] = "RenewImageAuthorizeState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewImageAuthorizeStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetSecLogTopicConfig(
            self,
            request: models.ResetSecLogTopicConfigRequest,
            opts: Dict = None,
    ) -> models.ResetSecLogTopicConfigResponse:
        """
        重置安全日志主题设置
        """
        
        kwargs = {}
        kwargs["action"] = "ResetSecLogTopicConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetSecLogTopicConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanComplianceAssets(
            self,
            request: models.ScanComplianceAssetsRequest,
            opts: Dict = None,
    ) -> models.ScanComplianceAssetsResponse:
        """
        重新检测选定的资产
        """
        
        kwargs = {}
        kwargs["action"] = "ScanComplianceAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanComplianceAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanComplianceAssetsByPolicyItem(
            self,
            request: models.ScanComplianceAssetsByPolicyItemRequest,
            opts: Dict = None,
    ) -> models.ScanComplianceAssetsByPolicyItemResponse:
        """
        用指定的检测项重新检测选定的资产，返回创建的合规检查任务的ID。
        """
        
        kwargs = {}
        kwargs["action"] = "ScanComplianceAssetsByPolicyItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanComplianceAssetsByPolicyItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanCompliancePolicyItems(
            self,
            request: models.ScanCompliancePolicyItemsRequest,
            opts: Dict = None,
    ) -> models.ScanCompliancePolicyItemsResponse:
        """
        重新检测选的检测项下的所有资产，返回创建的合规检查任务的ID。
        """
        
        kwargs = {}
        kwargs["action"] = "ScanCompliancePolicyItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanCompliancePolicyItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScanComplianceScanFailedAssets(
            self,
            request: models.ScanComplianceScanFailedAssetsRequest,
            opts: Dict = None,
    ) -> models.ScanComplianceScanFailedAssetsResponse:
        """
        重新检测选定的检测失败的资产下的所有失败的检测项，返回创建的合规检查任务的ID。
        """
        
        kwargs = {}
        kwargs["action"] = "ScanComplianceScanFailedAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScanComplianceScanFailedAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCheckMode(
            self,
            request: models.SetCheckModeRequest,
            opts: Dict = None,
    ) -> models.SetCheckModeResponse:
        """
        设置检测模式和自动检查
        """
        
        kwargs = {}
        kwargs["action"] = "SetCheckMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCheckModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopVirusScanTask(
            self,
            request: models.StopVirusScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopVirusScanTaskResponse:
        """
        运行时停止木马查杀任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopVirusScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopVirusScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopVulScanTask(
            self,
            request: models.StopVulScanTaskRequest,
            opts: Dict = None,
    ) -> models.StopVulScanTaskResponse:
        """
        停止漏洞扫描任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopVulScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopVulScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchImageAutoAuthorizedRule(
            self,
            request: models.SwitchImageAutoAuthorizedRuleRequest,
            opts: Dict = None,
    ) -> models.SwitchImageAutoAuthorizedRuleResponse:
        """
        编辑本地镜像自动授权开关
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchImageAutoAuthorizedRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchImageAutoAuthorizedRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncAssetImageRegistryAsset(
            self,
            request: models.SyncAssetImageRegistryAssetRequest,
            opts: Dict = None,
    ) -> models.SyncAssetImageRegistryAssetResponse:
        """
        镜像仓库资产刷新
        """
        
        kwargs = {}
        kwargs["action"] = "SyncAssetImageRegistryAsset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncAssetImageRegistryAssetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallClusterContainerSecurity(
            self,
            request: models.UninstallClusterContainerSecurityRequest,
            opts: Dict = None,
    ) -> models.UninstallClusterContainerSecurityResponse:
        """
        卸载集群容器安全
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallClusterContainerSecurity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallClusterContainerSecurityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAndPublishNetworkFirewallPolicyDetail(
            self,
            request: models.UpdateAndPublishNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateAndPublishNetworkFirewallPolicyDetailResponse:
        """
        容器网络创建网络策略更新并发布任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAndPublishNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAndPublishNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAndPublishNetworkFirewallPolicyYamlDetail(
            self,
            request: models.UpdateAndPublishNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse:
        """
        容器网络更新Yaml网络策略并发布任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAndPublishNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAssetImageRegistryRegistryDetail(
            self,
            request: models.UpdateAssetImageRegistryRegistryDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateAssetImageRegistryRegistryDetailResponse:
        """
        更新单个镜像仓库详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAssetImageRegistryRegistryDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAssetImageRegistryRegistryDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateImageRegistryTimingScanTask(
            self,
            request: models.UpdateImageRegistryTimingScanTaskRequest,
            opts: Dict = None,
    ) -> models.UpdateImageRegistryTimingScanTaskResponse:
        """
        镜像仓库更新定时任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateImageRegistryTimingScanTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateImageRegistryTimingScanTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNetworkFirewallPolicyDetail(
            self,
            request: models.UpdateNetworkFirewallPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateNetworkFirewallPolicyDetailResponse:
        """
        容器网络创建网络策略更新任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNetworkFirewallPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNetworkFirewallPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNetworkFirewallPolicyYamlDetail(
            self,
            request: models.UpdateNetworkFirewallPolicyYamlDetailRequest,
            opts: Dict = None,
    ) -> models.UpdateNetworkFirewallPolicyYamlDetailResponse:
        """
        容器网络更新Yaml网络策略任务
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNetworkFirewallPolicyYamlDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNetworkFirewallPolicyYamlDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)