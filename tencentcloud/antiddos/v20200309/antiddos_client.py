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
            body = self.call("AssociateDDoSEipAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateDDoSEipAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateDDoSEipLoadBalancer(self, request):
        """本接口 (AssociateDDoSEipLoadBalancer) 用于将高防弹性公网IP绑定到负载均衡指定内网 IP 上。

        :param request: Request instance for AssociateDDoSEipLoadBalancer.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipLoadBalancerRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AssociateDDoSEipLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateDDoSEipLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateDDoSEipLoadBalancerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBlackWhiteIpList(self, request):
        """添加DDoS防护的IP黑白名单

        :param request: Request instance for CreateBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBlackWhiteIpList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBoundIP(self, request):
        """绑定IP到高防包实例，支持独享包、共享包；需要注意的是此接口绑定或解绑IP是异步接口，当处于绑定或解绑中时，则不允许再进行绑定或解绑，需要等待当前绑定或解绑完成。

        :param request: Request instance for CreateBoundIP.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateBoundIPRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateBoundIPResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBoundIP", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBoundIPResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDDoSAI(self, request):
        """设置DDoS防护的AI防护开关

        :param request: Request instance for CreateDDoSAI.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSAIRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSAIResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDDoSAI", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSAIResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDDoSGeoIPBlockConfig(self, request):
        """添加DDoS防护的区域封禁配置

        :param request: Request instance for CreateDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDDoSGeoIPBlockConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDDoSSpeedLimitConfig(self, request):
        """添加DDoS防护的访问限速配置

        :param request: Request instance for CreateDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDDoSSpeedLimitConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDefaultAlarmThreshold(self, request):
        """设置单IP默认告警阈值配置

        :param request: Request instance for CreateDefaultAlarmThreshold.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateDefaultAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateDefaultAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDefaultAlarmThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultAlarmThresholdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIPAlarmThresholdConfig(self, request):
        """设置单IP告警阈值配置

        :param request: Request instance for CreateIPAlarmThresholdConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateIPAlarmThresholdConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateIPAlarmThresholdConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateIPAlarmThresholdConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIPAlarmThresholdConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateL7RuleCerts(self, request):
        """批量配置L7转发规则的证书供SSL测调用

        :param request: Request instance for CreateL7RuleCerts.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateL7RuleCertsRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateL7RuleCertsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7RuleCerts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RuleCertsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePacketFilterConfig(self, request):
        """添加DDoS防护的特征过滤规则

        :param request: Request instance for CreatePacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreatePacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreatePacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePacketFilterConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProtocolBlockConfig(self, request):
        """设置DDoS防护的协议封禁配置

        :param request: Request instance for CreateProtocolBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateProtocolBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateProtocolBlockConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProtocolBlockConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProtocolBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSchedulingDomain(self, request):
        """创建一个域名，可用于在封堵时调度切换IP

        :param request: Request instance for CreateSchedulingDomain.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateSchedulingDomainRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateSchedulingDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSchedulingDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSchedulingDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWaterPrintConfig(self, request):
        """添加DDoS防护的水印防护配置

        :param request: Request instance for CreateWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWaterPrintConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWaterPrintKey(self, request):
        """添加DDoS防护的水印防护密钥

        :param request: Request instance for CreateWaterPrintKey.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintKeyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CreateWaterPrintKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWaterPrintKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWaterPrintKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteBlackWhiteIpList(self, request):
        """删除DDoS防护的IP黑白名单

        :param request: Request instance for DeleteBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBlackWhiteIpList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDDoSGeoIPBlockConfig(self, request):
        """删除DDoS防护的区域封禁配置

        :param request: Request instance for DeleteDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDDoSGeoIPBlockConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDDoSSpeedLimitConfig(self, request):
        """删除DDoS防护的访问限速配置

        :param request: Request instance for DeleteDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDDoSSpeedLimitConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePacketFilterConfig(self, request):
        """删除DDoS防护的特征过滤规则

        :param request: Request instance for DeletePacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeletePacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeletePacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePacketFilterConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWaterPrintConfig(self, request):
        """删除DDoS防护的水印防护配置

        :param request: Request instance for DeleteWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWaterPrintConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWaterPrintKey(self, request):
        """删除DDoS防护的水印防护密钥

        :param request: Request instance for DeleteWaterPrintKey.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintKeyRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DeleteWaterPrintKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWaterPrintKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWaterPrintKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBasicDeviceStatus(self, request):
        """获取基础防护攻击状态

        :param request: Request instance for DescribeBasicDeviceStatus.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBasicDeviceStatusRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBasicDeviceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBasicDeviceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicDeviceStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBizTrend(self, request):
        """获取业务流量曲线

        :param request: Request instance for DescribeBizTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBizTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBizTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBizTrendResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBlackWhiteIpList(self, request):
        """获取DDoS防护的IP黑白名单

        :param request: Request instance for DescribeBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBlackWhiteIpList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCCTrend(self, request):
        """获取CC攻击指标数据，包括总请求峰值(QPS)和攻击请求(QPS)

        :param request: Request instance for DescribeCCTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeCCTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCTrendResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDDoSTrend(self, request):
        """获取DDoS攻击流量带宽和攻击包速率数据

        :param request: Request instance for DescribeDDoSTrend.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSTrendRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDDoSTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSTrendResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDefaultAlarmThreshold(self, request):
        """获取单IP默认告警阈值配置

        :param request: Request instance for DescribeDefaultAlarmThreshold.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeDefaultAlarmThresholdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeDefaultAlarmThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDefaultAlarmThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDefaultAlarmThresholdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeL7RulesBySSLCertId(self, request):
        """查询与证书ID对于域名匹配的七层规则

        :param request: Request instance for DescribeL7RulesBySSLCertId.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeL7RulesBySSLCertIdRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeL7RulesBySSLCertIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7RulesBySSLCertId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7RulesBySSLCertIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListBGPIPInstances(self, request):
        """获取高防IP资产实例列表

        :param request: Request instance for DescribeListBGPIPInstances.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPIPInstancesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPIPInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListBGPIPInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListBGPIPInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListBGPInstances(self, request):
        """获取高防包资产实例列表

        :param request: Request instance for DescribeListBGPInstances.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPInstancesRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBGPInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListBGPInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListBGPInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListBlackWhiteIpList(self, request):
        """获取DDoS防护的IP黑白名单列表

        :param request: Request instance for DescribeListBlackWhiteIpList.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBlackWhiteIpListRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListBlackWhiteIpListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListBlackWhiteIpList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListBlackWhiteIpListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListDDoSAI(self, request):
        """获取DDoS防护的AI防护开关列表

        :param request: Request instance for DescribeListDDoSAI.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSAIRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSAIResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListDDoSAI", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListDDoSAIResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListDDoSGeoIPBlockConfig(self, request):
        """获取DDoS防护的区域封禁配置列表

        :param request: Request instance for DescribeListDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListDDoSGeoIPBlockConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListDDoSSpeedLimitConfig(self, request):
        """获取DDoS防护的访问限速配置列表

        :param request: Request instance for DescribeListDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListDDoSSpeedLimitConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListIPAlarmConfig(self, request):
        """获取单IP告警阈值配置列表

        :param request: Request instance for DescribeListIPAlarmConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListIPAlarmConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListIPAlarmConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListIPAlarmConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListIPAlarmConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListListener(self, request):
        """获取转发监听器列表

        :param request: Request instance for DescribeListListener.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListListenerRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListListenerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListPacketFilterConfig(self, request):
        """获取DDoS防护的特征过滤规则列表

        :param request: Request instance for DescribeListPacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListPacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListPacketFilterConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListPacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListProtectThresholdConfig(self, request):
        """获取防护阈值配置列表，包括DDoS的AI、等级、CC阈值开关等

        :param request: Request instance for DescribeListProtectThresholdConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtectThresholdConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtectThresholdConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListProtectThresholdConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListProtectThresholdConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListProtocolBlockConfig(self, request):
        """获取DDoS防护的协议封禁配置列表

        :param request: Request instance for DescribeListProtocolBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtocolBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListProtocolBlockConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListProtocolBlockConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListProtocolBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListSchedulingDomain(self, request):
        """获取智能调度域名列表

        :param request: Request instance for DescribeListSchedulingDomain.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListSchedulingDomainRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListSchedulingDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListSchedulingDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListSchedulingDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListWaterPrintConfig(self, request):
        """获取DDoS防护的水印防护配置列表

        :param request: Request instance for DescribeListWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DescribeListWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DescribeListWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListWaterPrintConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateDDoSEipAddress(self, request):
        """本接口 (DisassociateDDoSEipAddress) 用于解绑高防弹性公网IP。

        :param request: Request instance for DisassociateDDoSEipAddress.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.DisassociateDDoSEipAddressRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DisassociateDDoSEipAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateDDoSEipAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateDDoSEipAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDDoSGeoIPBlockConfig(self, request):
        """修改DDoS防护的区域封禁配置

        :param request: Request instance for ModifyDDoSGeoIPBlockConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSGeoIPBlockConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSGeoIPBlockConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSGeoIPBlockConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSGeoIPBlockConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDDoSSpeedLimitConfig(self, request):
        """修改DDoS防护的访问限速配置

        :param request: Request instance for ModifyDDoSSpeedLimitConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSSpeedLimitConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDDoSSpeedLimitConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSSpeedLimitConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSSpeedLimitConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDomainUsrName(self, request):
        """修改智能解析域名名称

        :param request: Request instance for ModifyDomainUsrName.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyDomainUsrNameRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyDomainUsrNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomainUsrName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainUsrNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyL7RulesEdge(self, request):
        """修改边界防护L7转发规则

        :param request: Request instance for ModifyL7RulesEdge.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyL7RulesEdgeRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyL7RulesEdgeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7RulesEdge", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7RulesEdgeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPacketFilterConfig(self, request):
        """修改DDoS防护的特征过滤规则

        :param request: Request instance for ModifyPacketFilterConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.ModifyPacketFilterConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ModifyPacketFilterConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPacketFilterConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPacketFilterConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchWaterPrintConfig(self, request):
        """开启或关闭DDoS防护的水印防护配置

        :param request: Request instance for SwitchWaterPrintConfig.
        :type request: :class:`tencentcloud.antiddos.v20200309.models.SwitchWaterPrintConfigRequest`
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SwitchWaterPrintConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchWaterPrintConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchWaterPrintConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)