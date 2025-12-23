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
from tencentcloud.antiddos.v20200309 import models
from typing import Dict


class AntiddosClient(AbstractClient):
    _apiVersion = '2020-03-09'
    _endpoint = 'antiddos.tencentcloudapi.com'
    _service = 'antiddos'

    async def AssociateDDoSEipAddress(
            self,
            request: models.AssociateDDoSEipAddressRequest,
            opts: Dict = None,
    ) -> models.AssociateDDoSEipAddressResponse:
        """
        本接口 (AssociateDDoSEipAddress) 用于将高防弹性公网IP绑定到实例或弹性网卡的指定内网 IP 上。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDDoSEipAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDDoSEipAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateDDoSEipLoadBalancer(
            self,
            request: models.AssociateDDoSEipLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.AssociateDDoSEipLoadBalancerResponse:
        """
        本接口 (AssociateDDoSEipLoadBalancer) 用于将高防弹性公网IP绑定到负载均衡指定内网 IP 上。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDDoSEipLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDDoSEipLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBgpInstance(
            self,
            request: models.CreateBgpInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateBgpInstanceResponse:
        """
        通过API 购买高防包接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBgpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBgpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBlackWhiteIpList(
            self,
            request: models.CreateBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.CreateBlackWhiteIpListResponse:
        """
        添加DDoS防护的IP黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBoundIP(
            self,
            request: models.CreateBoundIPRequest,
            opts: Dict = None,
    ) -> models.CreateBoundIPResponse:
        """
        绑定IP到高防包实例，支持独享包、共享包（新版）；需要注意的是此接口绑定或解绑IP是异步接口，当处于绑定或解绑中时，则不允许再进行绑定或解绑，需要等待当前绑定或解绑完成。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBoundIP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBoundIPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCPrecisionPolicy(
            self,
            request: models.CreateCCPrecisionPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCCPrecisionPolicyResponse:
        """
        新增CC精准防护策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCPrecisionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCPrecisionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCReqLimitPolicy(
            self,
            request: models.CreateCCReqLimitPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCCReqLimitPolicyResponse:
        """
        新增CC频率限制策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCReqLimitPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCReqLimitPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCcBlackWhiteIpList(
            self,
            request: models.CreateCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.CreateCcBlackWhiteIpListResponse:
        """
        新建CC四层黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCcGeoIPBlockConfig(
            self,
            request: models.CreateCcGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.CreateCcGeoIPBlockConfigResponse:
        """
        新建CC防护的地域封禁配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCcGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCcGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSAI(
            self,
            request: models.CreateDDoSAIRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSAIResponse:
        """
        设置DDoS防护的AI防护开关
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSAI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSAIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSBlackWhiteIpList(
            self,
            request: models.CreateDDoSBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSBlackWhiteIpListResponse:
        """
        添加DDoS防护的IP网段黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSConnectLimit(
            self,
            request: models.CreateDDoSConnectLimitRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSConnectLimitResponse:
        """
        配置DDoS连接抑制选项
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSConnectLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSConnectLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSGeoIPBlockConfig(
            self,
            request: models.CreateDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSGeoIPBlockConfigResponse:
        """
        添加DDoS防护的区域封禁配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDDoSSpeedLimitConfig(
            self,
            request: models.CreateDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.CreateDDoSSpeedLimitConfigResponse:
        """
        添加DDoS防护的访问限速配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDDoSSpeedLimitConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDefaultAlarmThreshold(
            self,
            request: models.CreateDefaultAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.CreateDefaultAlarmThresholdResponse:
        """
        设置单IP默认告警阈值配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDefaultAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDefaultAlarmThresholdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIPAlarmThresholdConfig(
            self,
            request: models.CreateIPAlarmThresholdConfigRequest,
            opts: Dict = None,
    ) -> models.CreateIPAlarmThresholdConfigResponse:
        """
        设置单IP告警阈值配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIPAlarmThresholdConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIPAlarmThresholdConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7RuleCerts(
            self,
            request: models.CreateL7RuleCertsRequest,
            opts: Dict = None,
    ) -> models.CreateL7RuleCertsResponse:
        """
        批量配置L7转发规则的证书供SSL测调用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7RuleCerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RuleCertsResponse
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
        
    async def CreatePacketFilterConfig(
            self,
            request: models.CreatePacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.CreatePacketFilterConfigResponse:
        """
        添加DDoS防护的特征过滤规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePortAclConfig(
            self,
            request: models.CreatePortAclConfigRequest,
            opts: Dict = None,
    ) -> models.CreatePortAclConfigResponse:
        """
        添加DDoS防护的端口acl策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePortAclConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePortAclConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePortAclConfigList(
            self,
            request: models.CreatePortAclConfigListRequest,
            opts: Dict = None,
    ) -> models.CreatePortAclConfigListResponse:
        """
        批量添加DDoS防护的端口acl策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePortAclConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePortAclConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProtocolBlockConfig(
            self,
            request: models.CreateProtocolBlockConfigRequest,
            opts: Dict = None,
    ) -> models.CreateProtocolBlockConfigResponse:
        """
        设置DDoS防护的协议封禁配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProtocolBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProtocolBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSchedulingDomain(
            self,
            request: models.CreateSchedulingDomainRequest,
            opts: Dict = None,
    ) -> models.CreateSchedulingDomainResponse:
        """
        创建一个域名，可用于在封堵时调度切换IP
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSchedulingDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSchedulingDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWaterPrintConfig(
            self,
            request: models.CreateWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.CreateWaterPrintConfigResponse:
        """
        添加DDoS防护的水印防护配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWaterPrintKey(
            self,
            request: models.CreateWaterPrintKeyRequest,
            opts: Dict = None,
    ) -> models.CreateWaterPrintKeyResponse:
        """
        添加DDoS防护的水印防护密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWaterPrintKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWaterPrintKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCLevelPolicy(
            self,
            request: models.DeleteCCLevelPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCLevelPolicyResponse:
        """
        删除CC分级策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCLevelPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCLevelPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCPrecisionPolicy(
            self,
            request: models.DeleteCCPrecisionPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCPrecisionPolicyResponse:
        """
        删除CC精准防护策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCPrecisionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCPrecisionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCRequestLimitPolicy(
            self,
            request: models.DeleteCCRequestLimitPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCRequestLimitPolicyResponse:
        """
        删除CC频率限制策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCRequestLimitPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCRequestLimitPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCThresholdPolicy(
            self,
            request: models.DeleteCCThresholdPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteCCThresholdPolicyResponse:
        """
        删除CC清洗阈值策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCThresholdPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCThresholdPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCcBlackWhiteIpList(
            self,
            request: models.DeleteCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DeleteCcBlackWhiteIpListResponse:
        """
        删除CC四层黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCcGeoIPBlockConfig(
            self,
            request: models.DeleteCcGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteCcGeoIPBlockConfigResponse:
        """
        删除CC防护的区域封禁配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCcGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCcGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSBlackWhiteIpList(
            self,
            request: models.DeleteDDoSBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSBlackWhiteIpListResponse:
        """
        删除DDoS防护的IP网段黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSGeoIPBlockConfig(
            self,
            request: models.DeleteDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSGeoIPBlockConfigResponse:
        """
        删除DDoS防护的区域封禁配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDDoSSpeedLimitConfig(
            self,
            request: models.DeleteDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteDDoSSpeedLimitConfigResponse:
        """
        删除DDoS防护的访问限速配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDDoSSpeedLimitConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePacketFilterConfig(
            self,
            request: models.DeletePacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.DeletePacketFilterConfigResponse:
        """
        删除DDoS防护的特征过滤规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePortAclConfig(
            self,
            request: models.DeletePortAclConfigRequest,
            opts: Dict = None,
    ) -> models.DeletePortAclConfigResponse:
        """
        删除DDoS防护的端口acl策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePortAclConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePortAclConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWaterPrintConfig(
            self,
            request: models.DeleteWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteWaterPrintConfigResponse:
        """
        删除DDoS防护的水印防护配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWaterPrintKey(
            self,
            request: models.DeleteWaterPrintKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteWaterPrintKeyResponse:
        """
        删除DDoS防护的水印防护密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWaterPrintKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWaterPrintKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBGPIPL7Rules(
            self,
            request: models.DescribeBGPIPL7RulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBGPIPL7RulesResponse:
        """
        高防IP获取7层规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBGPIPL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBGPIPL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicDeviceStatus(
            self,
            request: models.DescribeBasicDeviceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicDeviceStatusResponse:
        """
        获取基础防护攻击状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicDeviceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicDeviceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBgpBizTrend(
            self,
            request: models.DescribeBgpBizTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeBgpBizTrendResponse:
        """
        获取高防包流量折线图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBgpBizTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBgpBizTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBgpInstances(
            self,
            request: models.DescribeBgpInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeBgpInstancesResponse:
        """
        购买后，查询购买的高防包实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBgpInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBgpInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBizHttpStatus(
            self,
            request: models.DescribeBizHttpStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBizHttpStatusResponse:
        """
        获取业务流量状态码统计列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBizHttpStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBizHttpStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBizMonitorTrend(
            self,
            request: models.DescribeBizMonitorTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeBizMonitorTrendResponse:
        """
        获取高防IP业务监控流量曲线
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBizMonitorTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBizMonitorTrendResponse
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
        
    async def DescribeCCLevelList(
            self,
            request: models.DescribeCCLevelListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCLevelListResponse:
        """
        获取边界防护CC防护等级列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCLevelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCLevelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCLevelPolicy(
            self,
            request: models.DescribeCCLevelPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeCCLevelPolicyResponse:
        """
        获取CC分级策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCLevelPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCLevelPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCPrecisionPlyList(
            self,
            request: models.DescribeCCPrecisionPlyListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCPrecisionPlyListResponse:
        """
        获取CC精准防护列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCPrecisionPlyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCPrecisionPlyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCReqLimitPolicyList(
            self,
            request: models.DescribeCCReqLimitPolicyListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCReqLimitPolicyListResponse:
        """
        获取CC频率限制策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCReqLimitPolicyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCReqLimitPolicyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCThresholdList(
            self,
            request: models.DescribeCCThresholdListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCThresholdListResponse:
        """
        获取CC清洗阈值列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCThresholdList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCThresholdListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCTrend(
            self,
            request: models.DescribeCCTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeCCTrendResponse:
        """
        获取CC攻击指标数据，包括总请求峰值(QPS)和攻击请求(QPS)以及总请求次数和攻击请求次数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcBlackWhiteIpList(
            self,
            request: models.DescribeCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeCcBlackWhiteIpListResponse:
        """
        获取CC四层黑白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcGeoIPBlockConfigList(
            self,
            request: models.DescribeCcGeoIPBlockConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribeCcGeoIPBlockConfigListResponse:
        """
        获取CC防护的区域封禁配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcGeoIPBlockConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcGeoIPBlockConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSBlackWhiteIpList(
            self,
            request: models.DescribeDDoSBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSBlackWhiteIpListResponse:
        """
        获取DDoS防护的IP网段黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSConnectLimitList(
            self,
            request: models.DescribeDDoSConnectLimitListRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSConnectLimitListResponse:
        """
        获取DDoS连接抑制配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSConnectLimitList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSConnectLimitListResponse
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
        
    async def DescribeDefaultAlarmThreshold(
            self,
            request: models.DescribeDefaultAlarmThresholdRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultAlarmThresholdResponse:
        """
        获取单IP默认告警阈值配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultAlarmThreshold"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultAlarmThresholdResponse
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
        
    async def DescribeL7RulesBySSLCertId(
            self,
            request: models.DescribeL7RulesBySSLCertIdRequest,
            opts: Dict = None,
    ) -> models.DescribeL7RulesBySSLCertIdResponse:
        """
        查询与证书ID对于域名匹配的七层规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7RulesBySSLCertId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7RulesBySSLCertIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListBGPIPInstances(
            self,
            request: models.DescribeListBGPIPInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeListBGPIPInstancesResponse:
        """
        获取高防IP资产实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListBGPIPInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListBGPIPInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListBGPInstances(
            self,
            request: models.DescribeListBGPInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeListBGPInstancesResponse:
        """
        获取高防包资产实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListBGPInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListBGPInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListBlackWhiteIpList(
            self,
            request: models.DescribeListBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.DescribeListBlackWhiteIpListResponse:
        """
        获取DDoS防护的IP黑白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListDDoSAI(
            self,
            request: models.DescribeListDDoSAIRequest,
            opts: Dict = None,
    ) -> models.DescribeListDDoSAIResponse:
        """
        获取DDoS防护的AI防护开关列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListDDoSAI"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListDDoSAIResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListDDoSGeoIPBlockConfig(
            self,
            request: models.DescribeListDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListDDoSGeoIPBlockConfigResponse:
        """
        获取DDoS防护的区域封禁配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListDDoSGeoIPBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListDDoSSpeedLimitConfig(
            self,
            request: models.DescribeListDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListDDoSSpeedLimitConfigResponse:
        """
        获取DDoS防护的访问限速配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListDDoSSpeedLimitConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListIPAlarmConfig(
            self,
            request: models.DescribeListIPAlarmConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListIPAlarmConfigResponse:
        """
        获取单IP告警阈值配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListIPAlarmConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListIPAlarmConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListListener(
            self,
            request: models.DescribeListListenerRequest,
            opts: Dict = None,
    ) -> models.DescribeListListenerResponse:
        """
        获取转发监听器列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListPacketFilterConfig(
            self,
            request: models.DescribeListPacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListPacketFilterConfigResponse:
        """
        获取DDoS防护的特征过滤规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListPacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListPacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListPortAclList(
            self,
            request: models.DescribeListPortAclListRequest,
            opts: Dict = None,
    ) -> models.DescribeListPortAclListResponse:
        """
        获取DDoS防护的端口acl策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListPortAclList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListPortAclListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListProtectThresholdConfigNew(
            self,
            request: models.DescribeListProtectThresholdConfigNewRequest,
            opts: Dict = None,
    ) -> models.DescribeListProtectThresholdConfigNewResponse:
        """
        获取防护阈值配置列表，包括DDoS的AI、等级、CC阈值开关等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListProtectThresholdConfigNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListProtectThresholdConfigNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListProtocolBlockConfig(
            self,
            request: models.DescribeListProtocolBlockConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListProtocolBlockConfigResponse:
        """
        获取DDoS防护的协议封禁配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListProtocolBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListProtocolBlockConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListSchedulingDomain(
            self,
            request: models.DescribeListSchedulingDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeListSchedulingDomainResponse:
        """
        获取智能调度域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListSchedulingDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListSchedulingDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListWaterPrintConfig(
            self,
            request: models.DescribeListWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeListWaterPrintConfigResponse:
        """
        获取DDoS防护的水印防护配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewL7Rules(
            self,
            request: models.DescribeNewL7RulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNewL7RulesResponse:
        """
        高防IP获取7层规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNewL7RulesErrHealth(
            self,
            request: models.DescribeNewL7RulesErrHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeNewL7RulesErrHealthResponse:
        """
        获取L7转发规则健康检查异常结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNewL7RulesErrHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewL7RulesErrHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewAttackTrend(
            self,
            request: models.DescribeOverviewAttackTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewAttackTrendResponse:
        """
        拉取防护概览攻击趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewAttackTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewAttackTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewCCTrend(
            self,
            request: models.DescribeOverviewCCTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewCCTrendResponse:
        """
        获取防护概览总请求峰值(QPS)和攻击请求(QPS)以及总请求次数和攻击请求次数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewCCTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewCCTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewDDoSEventList(
            self,
            request: models.DescribeOverviewDDoSEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewDDoSEventListResponse:
        """
        获取防护概览的ddos攻击事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewDDoSEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewDDoSEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewDDoSTrend(
            self,
            request: models.DescribeOverviewDDoSTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewDDoSTrendResponse:
        """
        获取防护概览DDoS攻击流量带宽和攻击包速率数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewDDoSTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewDDoSTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewIndex(
            self,
            request: models.DescribeOverviewIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewIndexResponse:
        """
        拉取防护概览指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePendingRiskInfo(
            self,
            request: models.DescribePendingRiskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePendingRiskInfoResponse:
        """
        查询账号维度待处理风险信息，包括是否为付费用户，查询攻击中、封堵中、过期资源数量等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePendingRiskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePendingRiskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateDDoSEipAddress(
            self,
            request: models.DisassociateDDoSEipAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateDDoSEipAddressResponse:
        """
        本接口 (DisassociateDDoSEipAddress) 用于解绑高防弹性公网IP。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateDDoSEipAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateDDoSEipAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCLevelPolicy(
            self,
            request: models.ModifyCCLevelPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCLevelPolicyResponse:
        """
        修改CC防护等级
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCLevelPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCLevelPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCPrecisionPolicy(
            self,
            request: models.ModifyCCPrecisionPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCPrecisionPolicyResponse:
        """
        修改CC精准防护策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCPrecisionPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCPrecisionPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCReqLimitPolicy(
            self,
            request: models.ModifyCCReqLimitPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCReqLimitPolicyResponse:
        """
        修改CC频率限制策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCReqLimitPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCReqLimitPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCCThresholdPolicy(
            self,
            request: models.ModifyCCThresholdPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCCThresholdPolicyResponse:
        """
        修改CC清洗阈值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCCThresholdPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCCThresholdPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcBlackWhiteIpList(
            self,
            request: models.ModifyCcBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.ModifyCcBlackWhiteIpListResponse:
        """
        修改CC四层黑白名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSBlackWhiteIpList(
            self,
            request: models.ModifyDDoSBlackWhiteIpListRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSBlackWhiteIpListResponse:
        """
        修改DDoS黑白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSBlackWhiteIpList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSBlackWhiteIpListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSGeoIPBlockConfig(
            self,
            request: models.ModifyDDoSGeoIPBlockConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSGeoIPBlockConfigResponse:
        """
        修改DDoS防护的区域封禁配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSGeoIPBlockConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSGeoIPBlockConfigResponse
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
        
    async def ModifyDDoSSpeedLimitConfig(
            self,
            request: models.ModifyDDoSSpeedLimitConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSSpeedLimitConfigResponse:
        """
        修改DDoS防护的访问限速配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSSpeedLimitConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSSpeedLimitConfigResponse
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
        
    async def ModifyDomainUsrName(
            self,
            request: models.ModifyDomainUsrNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainUsrNameResponse:
        """
        修改智能解析域名名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainUsrName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainUsrNameResponse
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
        
    async def ModifyPacketFilterConfig(
            self,
            request: models.ModifyPacketFilterConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPacketFilterConfigResponse:
        """
        修改DDoS防护的特征过滤规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPacketFilterConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPacketFilterConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPortAclConfig(
            self,
            request: models.ModifyPortAclConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPortAclConfigResponse:
        """
        修改DDoS防护的端口acl策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPortAclConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPortAclConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchWaterPrintConfig(
            self,
            request: models.SwitchWaterPrintConfigRequest,
            opts: Dict = None,
    ) -> models.SwitchWaterPrintConfigResponse:
        """
        开启或关闭DDoS防护的水印防护配置，此功能为付费增值服务，有需求请联系售后
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchWaterPrintConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchWaterPrintConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)