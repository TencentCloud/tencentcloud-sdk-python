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
from tencentcloud.dayu.v20180709 import models
from typing import Dict


class DayuClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'dayu.tencentcloudapi.com'
    _service = 'dayu'

    async def CreateBasicDDoSAlarmThreshold(
            self,
            request: models.CreateBasicDDoSAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.CreateBasicDDoSAlarmThresholdResponse:
        """
        设置基础防护的DDoS告警阈值，只支持基础防护产品
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBasicDDoSAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBasicDDoSAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBoundIP(
            self,
            request: models.CreateBoundIPRequest,
            opts: Dict = None,
    ) -> models.CreateBoundIPResponse:
        """
        绑定IP到高防包实例，支持独享包、共享包；需要注意的是此接口绑定或解绑IP是异步接口，当处于绑定或解绑中时，则不允许再进行绑定或解绑，需要等待当前绑定或解绑完成。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBoundIP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBoundIPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCFrequencyRules(
            self,
            request: models.CreateCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.CreateCCFrequencyRulesResponse:
        """
        添加CC防护的访问频率控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCSelfDefinePolicy(
            self,
            request: models.CreateCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCCSelfDefinePolicyResponse:
        """
        创建CC自定义策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSPolicy(
            self,
            request: models.CreateDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSPolicyResponse:
        """
        添加DDoS高级策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSPolicyCase(
            self,
            request: models.CreateDDoSPolicyCaseRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSPolicyCaseResponse:
        """
        添加策略场景
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSPolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSPolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceName(
            self,
            request: models.CreateInstanceNameRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceNameResponse:
        """
        资源实例重命名，支持独享包、共享包、高防IP、高防IP专业版；
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4HealthConfig(
            self,
            request: models.CreateL4HealthConfigRequest,
            opts: Dict = None,
    ) -> models.CreateL4HealthConfigResponse:
        """
        上传四层健康检查配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4Rules(
            self,
            request: models.CreateL4RulesRequest,
            opts: Dict = None,
    ) -> models.CreateL4RulesResponse:
        """
        添加L4转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7CCRule(
            self,
            request: models.CreateL7CCRuleRequest,
            opts: Dict = None,
    ) -> models.CreateL7CCRuleResponse:
        """
        此接口是7层CC的访问频控自定义规则（IP+Host维度，不支持具体的URI），此接口已弃用，请调用新接口CreateCCFrequencyRules，新接口同时支持IP+Host维度以及具体的URI；
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7CCRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7CCRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7HealthConfig(
            self,
            request: models.CreateL7HealthConfigRequest,
            opts: Dict = None,
    ) -> models.CreateL7HealthConfigResponse:
        """
        上传七层健康检查配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7RuleCert(
            self,
            request: models.CreateL7RuleCertRequest,
            opts: Dict = None,
    ) -> models.CreateL7RuleCertResponse:
        """
        配置7层转发规则的证书
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7RuleCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RuleCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7Rules(
            self,
            request: models.CreateL7RulesRequest,
            opts: Dict = None,
    ) -> models.CreateL7RulesResponse:
        """
        添加7层(网站)转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7RulesUpload(
            self,
            request: models.CreateL7RulesUploadRequest,
            opts: Dict = None,
    ) -> models.CreateL7RulesUploadResponse:
        """
        批量上传7层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7RulesUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RulesUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetReturn(
            self,
            request: models.CreateNetReturnRequest,
            opts: Dict = None,
    ) -> models.CreateNetReturnResponse:
        """
        高防IP专业版一键切回源站
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetReturn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetReturnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNewL4Rules(
            self,
            request: models.CreateNewL4RulesRequest,
            opts: Dict = None,
    ) -> models.CreateNewL4RulesResponse:
        """
        添加L4转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNewL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNewL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNewL7Rules(
            self,
            request: models.CreateNewL7RulesRequest,
            opts: Dict = None,
    ) -> models.CreateNewL7RulesResponse:
        """
        添加7层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNewL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNewL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNewL7RulesUpload(
            self,
            request: models.CreateNewL7RulesUploadRequest,
            opts: Dict = None,
    ) -> models.CreateNewL7RulesUploadResponse:
        """
        批量上传7层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNewL7RulesUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNewL7RulesUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUnblockIp(
            self,
            request: models.CreateUnblockIpRequest,
            opts: Dict = None,
    ) -> models.CreateUnblockIpResponse:
        """
        IP解封操作
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUnblockIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUnblockIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCFrequencyRules(
            self,
            request: models.DeleteCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteCCFrequencyRulesResponse:
        """
        删除CC防护的访问频率控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCSelfDefinePolicy(
            self,
            request: models.DeleteCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCSelfDefinePolicyResponse:
        """
        删除CC自定义策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSPolicy(
            self,
            request: models.DeleteDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSPolicyResponse:
        """
        删除DDoS高级策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSPolicyCase(
            self,
            request: models.DeleteDDoSPolicyCaseRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSPolicyCaseResponse:
        """
        删除策略场景
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSPolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSPolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL4Rules(
            self,
            request: models.DeleteL4RulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL4RulesResponse:
        """
        删除四层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL7Rules(
            self,
            request: models.DeleteL7RulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL7RulesResponse:
        """
        删除七层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNewL4Rules(
            self,
            request: models.DeleteNewL4RulesRequest,
            opts: Dict = None,
    ) -> models.DeleteNewL4RulesResponse:
        """
        删除L4转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNewL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNewL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNewL7Rules(
            self,
            request: models.DeleteNewL7RulesRequest,
            opts: Dict = None,
    ) -> models.DeleteNewL7RulesResponse:
        """
        删除L7转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNewL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNewL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActionLog(
            self,
            request: models.DescribeActionLogRequest,
            opts: Dict = None,
    ) -> models.DescribeActionLogResponse:
        """
        获取操作日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActionLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActionLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBGPIPL7RuleMaxCnt(
            self,
            request: models.DescribeBGPIPL7RuleMaxCntRequest,
            opts: Dict = None,
    ) -> models.DescribeBGPIPL7RuleMaxCntResponse:
        """
        获取高防IP可添加的最多7层规则数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBGPIPL7RuleMaxCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBGPIPL7RuleMaxCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaradData(
            self,
            request: models.DescribeBaradDataRequest,
            opts: Dict = None,
    ) -> models.DescribeBaradDataResponse:
        """
        为大禹子产品提供业务转发指标数据的接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaradData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaradDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicCCThreshold(
            self,
            request: models.DescribeBasicCCThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicCCThresholdResponse:
        """
        获取基础防护CC防护阈值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicCCThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicCCThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicDeviceThreshold(
            self,
            request: models.DescribeBasicDeviceThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicDeviceThresholdResponse:
        """
        获取基础防护黑洞阈值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicDeviceThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicDeviceThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBizHttpStatus(
            self,
            request: models.DescribeBizHttpStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBizHttpStatusResponse:
        """
        获取业务流量状态码统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBizHttpStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBizHttpStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBizTrend(
            self,
            request: models.DescribeBizTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeBizTrendResponse:
        """
        获取业务流量曲线
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBizTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBizTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCAlarmThreshold(
            self,
            request: models.DescribeCCAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeCCAlarmThresholdResponse:
        """
        获取高防包、高防IP、高防IP专业版、棋牌盾产品设置CC攻击的告警通知阈值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCEvList(
            self,
            request: models.DescribeCCEvListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCEvListResponse:
        """
        获取CC攻击事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCEvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCEvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCFrequencyRules(
            self,
            request: models.DescribeCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCCFrequencyRulesResponse:
        """
        获取CC防护的访问频率控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCIpAllowDeny(
            self,
            request: models.DescribeCCIpAllowDenyRequest,
            opts: Dict = None,
    ) -> models.DescribeCCIpAllowDenyResponse:
        """
        获取CC的IP黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCIpAllowDeny"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCIpAllowDenyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCSelfDefinePolicy(
            self,
            request: models.DescribeCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeCCSelfDefinePolicyResponse:
        """
        获取CC自定义策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCTrend(
            self,
            request: models.DescribeCCTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeCCTrendResponse:
        """
        获取CC攻击指标数据，包括总请求峰值(QPS)和攻击请求(QPS)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCUrlAllow(
            self,
            request: models.DescribeCCUrlAllowRequest,
            opts: Dict = None,
    ) -> models.DescribeCCUrlAllowResponse:
        """
        获取CC的Url白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCUrlAllow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCUrlAllowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAlarmThreshold(
            self,
            request: models.DescribeDDoSAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAlarmThresholdResponse:
        """
        获取高防包、高防IP、高防IP专业版、棋牌盾产品设置DDoS攻击的告警通知阈值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackIPRegionMap(
            self,
            request: models.DescribeDDoSAttackIPRegionMapRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackIPRegionMapResponse:
        """
        获取DDoS攻击源IP地域分布图，支持全球攻击分布和国内省份攻击分布；
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackIPRegionMap"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackIPRegionMapResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackSource(
            self,
            request: models.DescribeDDoSAttackSourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackSourceResponse:
        """
        获取DDoS攻击源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSCount(
            self,
            request: models.DescribeDDoSCountRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSCountResponse:
        """
        获取DDoS攻击占比分析
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSDefendStatus(
            self,
            request: models.DescribeDDoSDefendStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSDefendStatusResponse:
        """
        获取DDoS防护状态（临时关闭状态），支持产品：基础防护，独享包，共享包，高防IP，高防IP专业版；调用此接口是获取当前是否有设置临时关闭DDoS防护状态，如果有设置会返回临时关闭的时长等参数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSDefendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSDefendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSEvInfo(
            self,
            request: models.DescribeDDoSEvInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSEvInfoResponse:
        """
        获取DDoS攻击事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSEvInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSEvInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSEvList(
            self,
            request: models.DescribeDDoSEvListRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSEvListResponse:
        """
        获取DDoS攻击事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSEvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSEvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSIpLog(
            self,
            request: models.DescribeDDoSIpLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSIpLogResponse:
        """
        获取DDoSIP攻击日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSIpLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSIpLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetCount(
            self,
            request: models.DescribeDDoSNetCountRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetCountResponse:
        """
        获取高防IP专业版资源的DDoS攻击占比分析
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetEvInfo(
            self,
            request: models.DescribeDDoSNetEvInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetEvInfoResponse:
        """
        获取高防IP专业版资源的DDoS攻击事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetEvInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetEvInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetEvList(
            self,
            request: models.DescribeDDoSNetEvListRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetEvListResponse:
        """
        获取高防IP专业版资源的DDoS攻击事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetEvList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetEvListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetIpLog(
            self,
            request: models.DescribeDDoSNetIpLogRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetIpLogResponse:
        """
        获取高防IP专业版资源的DDoSIP攻击日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetIpLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetIpLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSNetTrend(
            self,
            request: models.DescribeDDoSNetTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSNetTrendResponse:
        """
        获取高防IP专业版资源的DDoS攻击指标数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSNetTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSNetTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSPolicy(
            self,
            request: models.DescribeDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSPolicyResponse:
        """
        获取DDoS高级策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSTrend(
            self,
            request: models.DescribeDDoSTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSTrendResponse:
        """
        获取DDoS攻击流量带宽和攻击包速率数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSUsedStatis(
            self,
            request: models.DescribeDDoSUsedStatisRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSUsedStatisResponse:
        """
        统计用户的高防资源的使用天数和DDoS攻击防护次数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSUsedStatis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSUsedStatisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPProductInfo(
            self,
            request: models.DescribeIPProductInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeIPProductInfoResponse:
        """
        获取独享包或共享包IP对应的云资产信息，只支持独享包和共享包的IP
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPProductInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPProductInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInsurePacks(
            self,
            request: models.DescribeInsurePacksRequest,
            opts: Dict = None,
    ) -> models.DescribeInsurePacksResponse:
        """
        获取保险包套餐列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInsurePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInsurePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpBlockList(
            self,
            request: models.DescribeIpBlockListRequest,
            opts: Dict = None,
    ) -> models.DescribeIpBlockListResponse:
        """
        获取IP封堵列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpBlockList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpBlockListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpUnBlockList(
            self,
            request: models.DescribeIpUnBlockListRequest,
            opts: Dict = None,
    ) -> models.DescribeIpUnBlockListResponse:
        """
        获取IP解封记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpUnBlockList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpUnBlockListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4HealthConfig(
            self,
            request: models.DescribeL4HealthConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeL4HealthConfigResponse:
        """
        导出四层健康检查配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4RulesErrHealth(
            self,
            request: models.DescribeL4RulesErrHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeL4RulesErrHealthResponse:
        """
        获取L4转发规则健康检查异常结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4RulesErrHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4RulesErrHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7HealthConfig(
            self,
            request: models.DescribeL7HealthConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeL7HealthConfigResponse:
        """
        导出七层健康检查配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7HealthConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7HealthConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewL4Rules(
            self,
            request: models.DescribeNewL4RulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNewL4RulesResponse:
        """
        获取L4转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewL4RulesErrHealth(
            self,
            request: models.DescribeNewL4RulesErrHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeNewL4RulesErrHealthResponse:
        """
        获取L4转发规则健康检查异常结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewL4RulesErrHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewL4RulesErrHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewL7RulesErrHealth(
            self,
            request: models.DescribeNewL7RulesErrHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeNewL7RulesErrHealthResponse:
        """
        获取L7转发规则健康检查异常结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewL7RulesErrHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewL7RulesErrHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackIndex(
            self,
            request: models.DescribePackIndexRequest,
            opts: Dict = None,
    ) -> models.DescribePackIndexResponse:
        """
        获取产品总览统计，支持高防包、高防IP、高防IP专业版；
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePcap(
            self,
            request: models.DescribePcapRequest,
            opts: Dict = None,
    ) -> models.DescribePcapResponse:
        """
        下载攻击事件的pcap包
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePcap"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePcapResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyCase(
            self,
            request: models.DescribePolicyCaseRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyCaseResponse:
        """
        获取策略场景
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResIpList(
            self,
            request: models.DescribeResIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeResIpListResponse:
        """
        获取资源的IP列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceList(
            self,
            request: models.DescribeResourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceListResponse:
        """
        获取资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleSets(
            self,
            request: models.DescribeRuleSetsRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleSetsResponse:
        """
        获取资源的规则数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulingDomainList(
            self,
            request: models.DescribeSchedulingDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulingDomainListResponse:
        """
        获取调度域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulingDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulingDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecIndex(
            self,
            request: models.DescribeSecIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeSecIndexResponse:
        """
        获取本月安全统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceIpSegment(
            self,
            request: models.DescribeSourceIpSegmentRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceIpSegmentResponse:
        """
        获取回源IP段，支持的产品：高防IP，高防IP专业版；
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceIpSegment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceIpSegmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTransmitStatis(
            self,
            request: models.DescribeTransmitStatisRequest,
            opts: Dict = None,
    ) -> models.DescribeTransmitStatisResponse:
        """
        获取业务转发统计数据，支持转发流量和转发包速率
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTransmitStatis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTransmitStatisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnBlockStatis(
            self,
            request: models.DescribeUnBlockStatisRequest,
            opts: Dict = None,
    ) -> models.DescribeUnBlockStatisResponse:
        """
        获取黑洞解封次数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnBlockStatis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnBlockStatisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribleL4Rules(
            self,
            request: models.DescribleL4RulesRequest,
            opts: Dict = None,
    ) -> models.DescribleL4RulesResponse:
        """
        获取四层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribleL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribleL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribleL7Rules(
            self,
            request: models.DescribleL7RulesRequest,
            opts: Dict = None,
    ) -> models.DescribleL7RulesResponse:
        """
        获取七层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribleL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribleL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribleNewL7Rules(
            self,
            request: models.DescribleNewL7RulesRequest,
            opts: Dict = None,
    ) -> models.DescribleNewL7RulesResponse:
        """
        获取7层规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribleNewL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribleNewL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribleRegionCount(
            self,
            request: models.DescribleRegionCountRequest,
            opts: Dict = None,
    ) -> models.DescribleRegionCountResponse:
        """
        获取地域的资源实例数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribleRegionCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribleRegionCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCAlarmThreshold(
            self,
            request: models.ModifyCCAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyCCAlarmThresholdResponse:
        """
        为高防包、高防IP、高防IP专业版、棋牌盾产品设置CC攻击的告警通知阈值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCFrequencyRules(
            self,
            request: models.ModifyCCFrequencyRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyCCFrequencyRulesResponse:
        """
        修改CC防护的访问频率控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCFrequencyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCFrequencyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCFrequencyRulesStatus(
            self,
            request: models.ModifyCCFrequencyRulesStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCCFrequencyRulesStatusResponse:
        """
        开启或关闭CC防护的访问频率控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCFrequencyRulesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCFrequencyRulesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCHostProtection(
            self,
            request: models.ModifyCCHostProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyCCHostProtectionResponse:
        """
        开启或关闭CC域名防护
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCHostProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCHostProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCIpAllowDeny(
            self,
            request: models.ModifyCCIpAllowDenyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCIpAllowDenyResponse:
        """
        添加或删除CC的IP黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCIpAllowDeny"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCIpAllowDenyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCLevel(
            self,
            request: models.ModifyCCLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyCCLevelResponse:
        """
        修改CC防护等级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCPolicySwitch(
            self,
            request: models.ModifyCCPolicySwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyCCPolicySwitchResponse:
        """
        修改CC自定义策略开关
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCPolicySwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCPolicySwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCSelfDefinePolicy(
            self,
            request: models.ModifyCCSelfDefinePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCSelfDefinePolicyResponse:
        """
        修改CC自定义策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCSelfDefinePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCSelfDefinePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCThreshold(
            self,
            request: models.ModifyCCThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyCCThresholdResponse:
        """
        修改CC的防护阈值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCUrlAllow(
            self,
            request: models.ModifyCCUrlAllowRequest,
            opts: Dict = None,
    ) -> models.ModifyCCUrlAllowResponse:
        """
        添加或删除CC的URL白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCUrlAllow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCUrlAllowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSAIStatus(
            self,
            request: models.ModifyDDoSAIStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSAIStatusResponse:
        """
        读取或修改DDoS的AI防护状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSAIStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSAIStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSAlarmThreshold(
            self,
            request: models.ModifyDDoSAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSAlarmThresholdResponse:
        """
        为高防包、高防IP、高防IP专业版、棋牌盾等产品设置DDoS攻击的告警通知阈值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSDefendStatus(
            self,
            request: models.ModifyDDoSDefendStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSDefendStatusResponse:
        """
        开启或关闭DDoS防护状态，调用此接口允许临时关闭DDoS防护一段时间，等时间到了会自动开启DDoS防护；
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSDefendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSDefendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSLevel(
            self,
            request: models.ModifyDDoSLevelRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSLevelResponse:
        """
        读取或修改DDoS的防护等级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSLevel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSLevelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicy(
            self,
            request: models.ModifyDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyResponse:
        """
        修改DDoS高级策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicyCase(
            self,
            request: models.ModifyDDoSPolicyCaseRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyCaseResponse:
        """
        修改策略场景
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicyCase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyCaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSPolicyName(
            self,
            request: models.ModifyDDoSPolicyNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSPolicyNameResponse:
        """
        修改DDoS高级策略名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSPolicyName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSPolicyNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSSwitch(
            self,
            request: models.ModifyDDoSSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSSwitchResponse:
        """
        开启或关闭DDoS防护，只支持基础防护产品；
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSThreshold(
            self,
            request: models.ModifyDDoSThresholdRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSThresholdResponse:
        """
        修改DDoS清洗阈值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSWaterKey(
            self,
            request: models.ModifyDDoSWaterKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSWaterKeyResponse:
        """
        支持水印密钥的添加，删除，开启，关闭
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSWaterKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSWaterKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyElasticLimit(
            self,
            request: models.ModifyElasticLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyElasticLimitResponse:
        """
        修改弹性防护阈值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyElasticLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyElasticLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Health(
            self,
            request: models.ModifyL4HealthRequest,
            opts: Dict = None,
    ) -> models.ModifyL4HealthResponse:
        """
        修改L4转发规则健康检查参数，支持的子产品：高防IP、高防IP专业版
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4Health"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4HealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4KeepTime(
            self,
            request: models.ModifyL4KeepTimeRequest,
            opts: Dict = None,
    ) -> models.ModifyL4KeepTimeResponse:
        """
        修改L4转发规则的会话保持，支持的子产品：高防IP、高防IP专业版
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4KeepTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4KeepTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Rules(
            self,
            request: models.ModifyL4RulesRequest,
            opts: Dict = None,
    ) -> models.ModifyL4RulesResponse:
        """
        修改L4转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7Rules(
            self,
            request: models.ModifyL7RulesRequest,
            opts: Dict = None,
    ) -> models.ModifyL7RulesResponse:
        """
        修改L7转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetReturnSwitch(
            self,
            request: models.ModifyNetReturnSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyNetReturnSwitchResponse:
        """
        在客户收攻击或者被封堵时，切回到源站，并设置回切的时长
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetReturnSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetReturnSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNewDomainRules(
            self,
            request: models.ModifyNewDomainRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyNewDomainRulesResponse:
        """
        修改7层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNewDomainRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNewDomainRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNewL4Rule(
            self,
            request: models.ModifyNewL4RuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNewL4RuleResponse:
        """
        修改4层转发规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNewL4Rule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNewL4RuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResBindDDoSPolicy(
            self,
            request: models.ModifyResBindDDoSPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyResBindDDoSPolicyResponse:
        """
        资源实例绑定DDoS高级策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResBindDDoSPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResBindDDoSPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceRenewFlag(
            self,
            request: models.ModifyResourceRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceRenewFlagResponse:
        """
        修改资源自动续费标记
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)