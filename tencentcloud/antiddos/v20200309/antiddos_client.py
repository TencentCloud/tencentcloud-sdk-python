# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.antiddos.v20200309 import models


class AntiddosClient(AbstractClient):
    _apiVersion = '2020-03-09'
    _endpoint = 'antiddos.tencentcloudapi.com'
    _service = 'antiddos'


    def AssociateDDoSEipAddress(self, request):
        """本接口 (AssociateDDoSEipAddress) 用于将高防弹性公网IP绑定到实例或弹性网卡的指定内网 IP 上。

        :param request: Request instance for AssociateDDoSEipAddress.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipAddressRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDDoSEipAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateDDoSEipAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateDDoSEipLoadBalancer(self, request):
        """本接口 (AssociateDDoSEipLoadBalancer) 用于将高防弹性公网IP绑定到负载均衡指定内网 IP 上。

        :param request: Request instance for AssociateDDoSEipLoadBalancer.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipLoadBalancerRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDDoSEipLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateDDoSEipLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBlackWhiteIpList(self, request):
        """添加DDoS防护的IP黑白名单

        :param request: Request instance for CreateBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBoundIP(self, request):
        """绑定IP到高防包实例，支持独享包、共享包；需要注意的是此接口绑定或解绑IP是异步接口，当处于绑定或解绑中时，则不允许再进行绑定或解绑，需要等待当前绑定或解绑完成。

        :param request: Request instance for CreateBoundIP.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateBoundIPRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateBoundIPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBoundIP", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBoundIPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCCPrecisionPolicy(self, request):
        """新增CC精准防护策略

        :param request: Request instance for CreateCCPrecisionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCCPrecisionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCCPrecisionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCCPrecisionPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCCPrecisionPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCCReqLimitPolicy(self, request):
        """新增CC频率限制策略

        :param request: Request instance for CreateCCReqLimitPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCCReqLimitPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCCReqLimitPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCCReqLimitPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCCReqLimitPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCcBlackWhiteIpList(self, request):
        """新建CC四层黑白名单

        :param request: Request instance for CreateCcBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCcBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCcBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCcBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCcBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCcGeoIPBlockConfig(self, request):
        """新建cc防护的地域封禁配置

        :param request: Request instance for CreateCcGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateCcGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateCcGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCcGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCcGeoIPBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDDoSAI(self, request):
        """设置DDoS防护的AI防护开关

        :param request: Request instance for CreateDDoSAI.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSAIRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSAIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSAI", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDDoSAIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDDoSBlackWhiteIpList(self, request):
        """添加DDoS防护的IP网段黑白名单

        :param request: Request instance for CreateDDoSBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDDoSBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDDoSConnectLimit(self, request):
        """配置DDoS连接抑制选项

        :param request: Request instance for CreateDDoSConnectLimit.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSConnectLimitRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSConnectLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSConnectLimit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDDoSConnectLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDDoSGeoIPBlockConfig(self, request):
        """添加DDoS防护的区域封禁配置

        :param request: Request instance for CreateDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDDoSGeoIPBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDDoSSpeedLimitConfig(self, request):
        """添加DDoS防护的访问限速配置

        :param request: Request instance for CreateDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDDoSSpeedLimitConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDefaultAlarmThreshold(self, request):
        """设置单IP默认告警阈值配置

        :param request: Request instance for CreateDefaultAlarmThreshold.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDefaultAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDefaultAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefaultAlarmThreshold", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDefaultAlarmThresholdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIPAlarmThresholdConfig(self, request):
        """设置单IP告警阈值配置

        :param request: Request instance for CreateIPAlarmThresholdConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateIPAlarmThresholdConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateIPAlarmThresholdConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIPAlarmThresholdConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIPAlarmThresholdConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateL7RuleCerts(self, request):
        """批量配置L7转发规则的证书供SSL测调用

        :param request: Request instance for CreateL7RuleCerts.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateL7RuleCertsRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateL7RuleCertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateL7RuleCerts", params, headers=headers)
            response = json.loads(body)
            model = models.CreateL7RuleCertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNewL7Rules(self, request):
        """添加7层转发规则

        :param request: Request instance for CreateNewL7Rules.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateNewL7RulesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateNewL7RulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNewL7Rules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNewL7RulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePacketFilterConfig(self, request):
        """添加DDoS防护的特征过滤规则

        :param request: Request instance for CreatePacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreatePacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreatePacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePacketFilterConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePortAclConfig(self, request):
        """添加DDoS防护的端口acl策略

        :param request: Request instance for CreatePortAclConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreatePortAclConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreatePortAclConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePortAclConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePortAclConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePortAclConfigList(self, request):
        """批量添加DDoS防护的端口acl策略

        :param request: Request instance for CreatePortAclConfigList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreatePortAclConfigListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreatePortAclConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePortAclConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePortAclConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProtocolBlockConfig(self, request):
        """设置DDoS防护的协议封禁配置

        :param request: Request instance for CreateProtocolBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateProtocolBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateProtocolBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProtocolBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProtocolBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSchedulingDomain(self, request):
        """创建一个域名，可用于在封堵时调度切换IP

        :param request: Request instance for CreateSchedulingDomain.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateSchedulingDomainRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateSchedulingDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSchedulingDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSchedulingDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWaterPrintConfig(self, request):
        """添加DDoS防护的水印防护配置

        :param request: Request instance for CreateWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWaterPrintConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWaterPrintKey(self, request):
        """添加DDoS防护的水印防护密钥

        :param request: Request instance for CreateWaterPrintKey.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintKeyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWaterPrintKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWaterPrintKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCCLevelPolicy(self, request):
        """删除CC分级策略

        :param request: Request instance for DeleteCCLevelPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCLevelPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCLevelPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCLevelPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCCLevelPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCCPrecisionPolicy(self, request):
        """删除CC精准防护策略

        :param request: Request instance for DeleteCCPrecisionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCPrecisionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCPrecisionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCPrecisionPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCCPrecisionPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCCRequestLimitPolicy(self, request):
        """删除CC频率限制策略

        :param request: Request instance for DeleteCCRequestLimitPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCRequestLimitPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCRequestLimitPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCRequestLimitPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCCRequestLimitPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCCThresholdPolicy(self, request):
        """删除CC清洗阈值策略

        :param request: Request instance for DeleteCCThresholdPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCThresholdPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCCThresholdPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCThresholdPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCCThresholdPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCcBlackWhiteIpList(self, request):
        """删除CC四层黑白名单

        :param request: Request instance for DeleteCcBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCcBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCcBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCcGeoIPBlockConfig(self, request):
        """删除CC防护的区域封禁配置

        :param request: Request instance for DeleteCcGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteCcGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCcGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCcGeoIPBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDDoSBlackWhiteIpList(self, request):
        """删除DDoS防护的IP网段黑白名单

        :param request: Request instance for DeleteDDoSBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDDoSBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDDoSBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDDoSGeoIPBlockConfig(self, request):
        """删除DDoS防护的区域封禁配置

        :param request: Request instance for DeleteDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDDoSGeoIPBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDDoSSpeedLimitConfig(self, request):
        """删除DDoS防护的访问限速配置

        :param request: Request instance for DeleteDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDDoSSpeedLimitConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePacketFilterConfig(self, request):
        """删除DDoS防护的特征过滤规则

        :param request: Request instance for DeletePacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeletePacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeletePacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePacketFilterConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePortAclConfig(self, request):
        """删除DDoS防护的端口acl策略

        :param request: Request instance for DeletePortAclConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeletePortAclConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeletePortAclConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePortAclConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePortAclConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWaterPrintConfig(self, request):
        """删除DDoS防护的水印防护配置

        :param request: Request instance for DeleteWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWaterPrintConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWaterPrintKey(self, request):
        """删除DDoS防护的水印防护密钥

        :param request: Request instance for DeleteWaterPrintKey.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintKeyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWaterPrintKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWaterPrintKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBasicDeviceStatus(self, request):
        """获取基础防护攻击状态

        :param request: Request instance for DescribeBasicDeviceStatus.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBasicDeviceStatusRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBasicDeviceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBasicDeviceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBasicDeviceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBgpBizTrend(self, request):
        """获取高防包流量折线图

        :param request: Request instance for DescribeBgpBizTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBgpBizTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBgpBizTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBgpBizTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBgpBizTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBizHttpStatus(self, request):
        """获取业务流量状态码统计列表

        :param request: Request instance for DescribeBizHttpStatus.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizHttpStatusRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizHttpStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBizHttpStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBizHttpStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBizTrend(self, request):
        """获取业务流量曲线

        :param request: Request instance for DescribeBizTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBizTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBizTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlackWhiteIpList(self, request):
        """获取DDoS防护的IP黑白名单

        :param request: Request instance for DescribeBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCLevelList(self, request):
        """获取边界防护CC防护等级列表

        :param request: Request instance for DescribeCCLevelList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCLevelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCLevelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCLevelPolicy(self, request):
        """获取CC分级策略

        :param request: Request instance for DescribeCCLevelPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCLevelPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCLevelPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCLevelPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCPrecisionPlyList(self, request):
        """获取CC精准防护列表

        :param request: Request instance for DescribeCCPrecisionPlyList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCPrecisionPlyListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCPrecisionPlyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCPrecisionPlyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCPrecisionPlyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCReqLimitPolicyList(self, request):
        """获取CC频率限制策略列表

        :param request: Request instance for DescribeCCReqLimitPolicyList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCReqLimitPolicyListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCReqLimitPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCReqLimitPolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCReqLimitPolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCThresholdList(self, request):
        """获取CC清洗阈值列表

        :param request: Request instance for DescribeCCThresholdList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCThresholdListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCThresholdListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCThresholdList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCThresholdListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCTrend(self, request):
        """获取CC攻击指标数据，包括总请求峰值(QPS)和攻击请求(QPS)以及总请求次数和攻击请求次数

        :param request: Request instance for DescribeCCTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcBlackWhiteIpList(self, request):
        """获取CC四层黑白名单列表

        :param request: Request instance for DescribeCcBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCcBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCcBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcGeoIPBlockConfigList(self, request):
        """获取CC防护的区域封禁配置列表

        :param request: Request instance for DescribeCcGeoIPBlockConfigList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCcGeoIPBlockConfigListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCcGeoIPBlockConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcGeoIPBlockConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcGeoIPBlockConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSBlackWhiteIpList(self, request):
        """获取DDoS防护的IP网段黑白名单

        :param request: Request instance for DescribeDDoSBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSConnectLimitList(self, request):
        """获取DDoS连接抑制配置列表

        :param request: Request instance for DescribeDDoSConnectLimitList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSConnectLimitListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSConnectLimitListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSConnectLimitList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSConnectLimitListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDDoSTrend(self, request):
        """获取DDoS攻击流量带宽和攻击包速率数据

        :param request: Request instance for DescribeDDoSTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDDoSTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDDoSTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultAlarmThreshold(self, request):
        """获取单IP默认告警阈值配置

        :param request: Request instance for DescribeDefaultAlarmThreshold.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDefaultAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDefaultAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultAlarmThreshold", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultAlarmThresholdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeL7RulesBySSLCertId(self, request):
        """查询与证书ID对于域名匹配的七层规则

        :param request: Request instance for DescribeL7RulesBySSLCertId.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeL7RulesBySSLCertIdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeL7RulesBySSLCertIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeL7RulesBySSLCertId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeL7RulesBySSLCertIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListBGPIPInstances(self, request):
        """获取高防IP资产实例列表

        :param request: Request instance for DescribeListBGPIPInstances.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPIPInstancesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPIPInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListBGPIPInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListBGPIPInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListBGPInstances(self, request):
        """获取高防包资产实例列表

        :param request: Request instance for DescribeListBGPInstances.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPInstancesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListBGPInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListBGPInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListBlackWhiteIpList(self, request):
        """获取DDoS防护的IP黑白名单列表

        :param request: Request instance for DescribeListBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListDDoSAI(self, request):
        """获取DDoS防护的AI防护开关列表

        :param request: Request instance for DescribeListDDoSAI.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSAIRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSAIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListDDoSAI", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListDDoSAIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListDDoSGeoIPBlockConfig(self, request):
        """获取DDoS防护的区域封禁配置列表

        :param request: Request instance for DescribeListDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListDDoSGeoIPBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListDDoSSpeedLimitConfig(self, request):
        """获取DDoS防护的访问限速配置列表

        :param request: Request instance for DescribeListDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListDDoSSpeedLimitConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListIPAlarmConfig(self, request):
        """获取单IP告警阈值配置列表

        :param request: Request instance for DescribeListIPAlarmConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListIPAlarmConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListIPAlarmConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListIPAlarmConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListIPAlarmConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListListener(self, request):
        """获取转发监听器列表

        :param request: Request instance for DescribeListListener.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListListenerRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListListener", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListPacketFilterConfig(self, request):
        """获取DDoS防护的特征过滤规则列表

        :param request: Request instance for DescribeListPacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListPacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListPacketFilterConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListPortAclList(self, request):
        """获取DDoS防护的端口acl策略列表

        :param request: Request instance for DescribeListPortAclList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPortAclListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPortAclListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListPortAclList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListPortAclListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListProtectThresholdConfig(self, request):
        """获取防护阈值配置列表，包括DDoS的AI、等级、CC阈值开关等

        :param request: Request instance for DescribeListProtectThresholdConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtectThresholdConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtectThresholdConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListProtectThresholdConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListProtectThresholdConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListProtocolBlockConfig(self, request):
        """获取DDoS防护的协议封禁配置列表

        :param request: Request instance for DescribeListProtocolBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtocolBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtocolBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListProtocolBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListProtocolBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListSchedulingDomain(self, request):
        """获取智能调度域名列表

        :param request: Request instance for DescribeListSchedulingDomain.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListSchedulingDomainRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListSchedulingDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListSchedulingDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListSchedulingDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListWaterPrintConfig(self, request):
        """获取DDoS防护的水印防护配置列表

        :param request: Request instance for DescribeListWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListWaterPrintConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNewL7Rules(self, request):
        """高防IP获取7层规则

        :param request: Request instance for DescribeNewL7Rules.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeNewL7RulesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeNewL7RulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNewL7Rules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNewL7RulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNewL7RulesErrHealth(self, request):
        """获取L7转发规则健康检查异常结果列表

        :param request: Request instance for DescribeNewL7RulesErrHealth.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeNewL7RulesErrHealthRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeNewL7RulesErrHealthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNewL7RulesErrHealth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNewL7RulesErrHealthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewAttackTrend(self, request):
        """拉取防护概览攻击趋势

        :param request: Request instance for DescribeOverviewAttackTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewAttackTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewAttackTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewAttackTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewAttackTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewCCTrend(self, request):
        """获取防护概览总请求峰值(QPS)和攻击请求(QPS)以及总请求次数和攻击请求次数

        :param request: Request instance for DescribeOverviewCCTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewCCTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewCCTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewCCTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewCCTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewDDoSEventList(self, request):
        """获取防护概览的ddos攻击事件

        :param request: Request instance for DescribeOverviewDDoSEventList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewDDoSEventListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewDDoSEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewDDoSEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewDDoSEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewDDoSTrend(self, request):
        """获取防护概览DDoS攻击流量带宽和攻击包速率数据

        :param request: Request instance for DescribeOverviewDDoSTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewDDoSTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewDDoSTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewDDoSTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewDDoSTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewIndex(self, request):
        """拉取防护概览指标

        :param request: Request instance for DescribeOverviewIndex.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewIndexRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeOverviewIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePendingRiskInfo(self, request):
        """查询账号维度待处理风险信息，包括是否为付费用户，查询攻击中、封堵中、过期资源数量等

        :param request: Request instance for DescribePendingRiskInfo.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribePendingRiskInfoRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribePendingRiskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePendingRiskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePendingRiskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateDDoSEipAddress(self, request):
        """本接口 (DisassociateDDoSEipAddress) 用于解绑高防弹性公网IP。

        :param request: Request instance for DisassociateDDoSEipAddress.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DisassociateDDoSEipAddressRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DisassociateDDoSEipAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateDDoSEipAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateDDoSEipAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCCLevelPolicy(self, request):
        """修改CC防护等级

        :param request: Request instance for ModifyCCLevelPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCLevelPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCLevelPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCCLevelPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCCLevelPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCCPrecisionPolicy(self, request):
        """修改CC精准防护策略

        :param request: Request instance for ModifyCCPrecisionPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCPrecisionPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCPrecisionPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCCPrecisionPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCCPrecisionPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCCReqLimitPolicy(self, request):
        """修改CC频率限制策略

        :param request: Request instance for ModifyCCReqLimitPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCReqLimitPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCReqLimitPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCCReqLimitPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCCReqLimitPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCCThresholdPolicy(self, request):
        """修改CC清洗阈值

        :param request: Request instance for ModifyCCThresholdPolicy.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCThresholdPolicyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyCCThresholdPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCCThresholdPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCCThresholdPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcBlackWhiteIpList(self, request):
        """修改CC四层黑白名单

        :param request: Request instance for ModifyCcBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyCcBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyCcBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSBlackWhiteIpList(self, request):
        """修改DDoS黑白名单列表

        :param request: Request instance for ModifyDDoSBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSBlackWhiteIpList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSBlackWhiteIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSGeoIPBlockConfig(self, request):
        """修改DDoS防护的区域封禁配置

        :param request: Request instance for ModifyDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSGeoIPBlockConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSGeoIPBlockConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSLevel(self, request):
        """读取或修改DDoS的防护等级

        :param request: Request instance for ModifyDDoSLevel.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSLevelRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSLevel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSSpeedLimitConfig(self, request):
        """修改DDoS防护的访问限速配置

        :param request: Request instance for ModifyDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSSpeedLimitConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSSpeedLimitConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDDoSThreshold(self, request):
        """修改DDoS清洗阈值

        :param request: Request instance for ModifyDDoSThreshold.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSThresholdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSThresholdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDDoSThreshold", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDDoSThresholdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainUsrName(self, request):
        """修改智能解析域名名称

        :param request: Request instance for ModifyDomainUsrName.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDomainUsrNameRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDomainUsrNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainUsrName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainUsrNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNewDomainRules(self, request):
        """修改7层转发规则

        :param request: Request instance for ModifyNewDomainRules.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyNewDomainRulesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyNewDomainRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNewDomainRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNewDomainRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPacketFilterConfig(self, request):
        """修改DDoS防护的特征过滤规则

        :param request: Request instance for ModifyPacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyPacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyPacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPacketFilterConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPacketFilterConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPortAclConfig(self, request):
        """修改DDoS防护的端口acl策略

        :param request: Request instance for ModifyPortAclConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyPortAclConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyPortAclConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPortAclConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPortAclConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchWaterPrintConfig(self, request):
        """开启或关闭DDoS防护的水印防护配置

        :param request: Request instance for SwitchWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.SwitchWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SwitchWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchWaterPrintConfig", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchWaterPrintConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))