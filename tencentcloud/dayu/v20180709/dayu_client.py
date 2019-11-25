# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.dayu.v20180709 import models


class DayuClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'dayu.tencentcloudapi.com'


    def CreateCCSelfDefinePolicy(self, request):
        """创建CC自定义策略

        :param request: 调用CreateCCSelfDefinePolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateCCSelfDefinePolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateCCSelfDefinePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCCSelfDefinePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCCSelfDefinePolicyResponse()
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


    def CreateDDoSPolicy(self, request):
        """添加DDoS高级策略

        :param request: 调用CreateDDoSPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSPolicyResponse()
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


    def CreateDDoSPolicyCase(self, request):
        """添加策略场景

        :param request: 调用CreateDDoSPolicyCase所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateDDoSPolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDDoSPolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDDoSPolicyCaseResponse()
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


    def CreateInstanceName(self, request):
        """资源实例重命名，支持独享包、共享包、高防IP、高防IP专业版、棋牌盾；

        :param request: 调用CreateInstanceName所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateInstanceNameRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceNameResponse()
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


    def CreateL4HealthConfig(self, request):
        """上传四层健康检查配置

        :param request: 调用CreateL4HealthConfig所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL4HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL4HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL4HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL4HealthConfigResponse()
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


    def CreateL4Rules(self, request):
        """添加L4转发规则

        :param request: 调用CreateL4Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL4RulesResponse()
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


    def CreateL7CCRule(self, request):
        """支持读取，添加，删除7层CC自定义规则

        :param request: 调用CreateL7CCRule所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7CCRuleRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7CCRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7CCRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7CCRuleResponse()
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


    def CreateL7HealthConfig(self, request):
        """上传七层健康检查配置

        :param request: 调用CreateL7HealthConfig所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7HealthConfigResponse()
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


    def CreateL7RuleCert(self, request):
        """配置7层转发规则的证书

        :param request: 调用CreateL7RuleCert所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7RuleCertRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7RuleCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7RuleCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RuleCertResponse()
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


    def CreateL7Rules(self, request):
        """添加7层(网站)转发规则

        :param request: 调用CreateL7Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RulesResponse()
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


    def CreateL7RulesUpload(self, request):
        """批量上传7层转发规则

        :param request: 调用CreateL7RulesUpload所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesUploadRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateL7RulesUploadResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7RulesUpload", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RulesUploadResponse()
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


    def CreateUnblockIp(self, request):
        """IP解封操作

        :param request: 调用CreateUnblockIp所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.CreateUnblockIpRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.CreateUnblockIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUnblockIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUnblockIpResponse()
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


    def DeleteCCSelfDefinePolicy(self, request):
        """删除CC自定义策略

        :param request: 调用DeleteCCSelfDefinePolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteCCSelfDefinePolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteCCSelfDefinePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCCSelfDefinePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCCSelfDefinePolicyResponse()
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


    def DeleteDDoSPolicy(self, request):
        """删除DDoS高级策略

        :param request: 调用DeleteDDoSPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSPolicyResponse()
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


    def DeleteDDoSPolicyCase(self, request):
        """删除策略场景

        :param request: 调用DeleteDDoSPolicyCase所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteDDoSPolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDDoSPolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDDoSPolicyCaseResponse()
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


    def DeleteL4Rules(self, request):
        """删除四层转发规则

        :param request: 调用DeleteL4Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL4RulesResponse()
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


    def DeleteL7Rules(self, request):
        """删除七层转发规则

        :param request: 调用DeleteL7Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DeleteL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DeleteL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL7RulesResponse()
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


    def DescribeActionLog(self, request):
        """获取操作日志

        :param request: 调用DescribeActionLog所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeActionLogRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeActionLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeActionLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeActionLogResponse()
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


    def DescribeBaradData(self, request):
        """为大禹子产品提供从巴拉多获取指标统计数据的接口

        :param request: 调用DescribeBaradData所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeBaradDataRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeBaradDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBaradData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBaradDataResponse()
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


    def DescribeCCEvList(self, request):
        """获取CC攻击事件列表

        :param request: 调用DescribeCCEvList所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCEvListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCEvListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCEvList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCEvListResponse()
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


    def DescribeCCIpAllowDeny(self, request):
        """获取CC的IP黑白名单

        :param request: 调用DescribeCCIpAllowDeny所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCIpAllowDenyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCIpAllowDenyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCIpAllowDeny", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCIpAllowDenyResponse()
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

        :param request: 调用DescribeCCTrend所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCTrendRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCTrendResponse`

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


    def DescribeCCUrlAllow(self, request):
        """获取CC的Url白名单

        :param request: 调用DescribeCCUrlAllow所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeCCUrlAllowRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeCCUrlAllowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCCUrlAllow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCCUrlAllowResponse()
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


    def DescribeDDoSCount(self, request):
        """获取DDoS攻击占比分析

        :param request: 调用DescribeDDoSCount所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSCountRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSCountResponse()
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


    def DescribeDDoSDefendStatus(self, request):
        """获取DDoS防护状态，支持产品：基础防护，独享包，共享包，高防IP，高防IP专业版；

        :param request: 调用DescribeDDoSDefendStatus所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSDefendStatusRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSDefendStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSDefendStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSDefendStatusResponse()
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


    def DescribeDDoSEvInfo(self, request):
        """获取DDoS攻击事件详情

        :param request: 调用DescribeDDoSEvInfo所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvInfoRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSEvInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSEvInfoResponse()
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


    def DescribeDDoSEvList(self, request):
        """获取DDoS攻击事件列表

        :param request: 调用DescribeDDoSEvList所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSEvListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSEvList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSEvListResponse()
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


    def DescribeDDoSIpLog(self, request):
        """获取DDoSIP攻击日志

        :param request: 调用DescribeDDoSIpLog所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSIpLogRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSIpLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSIpLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSIpLogResponse()
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


    def DescribeDDoSNetCount(self, request):
        """获取高防IP专业版资源的DDoS攻击占比分析

        :param request: 调用DescribeDDoSNetCount所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetCountRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetCountResponse()
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


    def DescribeDDoSNetEvInfo(self, request):
        """获取高防IP专业版资源的DDoS攻击事件详情

        :param request: 调用DescribeDDoSNetEvInfo所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvInfoRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetEvInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetEvInfoResponse()
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


    def DescribeDDoSNetEvList(self, request):
        """获取高防IP专业版资源的DDoS攻击事件列表

        :param request: 调用DescribeDDoSNetEvList所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetEvListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetEvList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetEvListResponse()
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


    def DescribeDDoSNetIpLog(self, request):
        """获取高防IP专业版资源的DDoSIP攻击日志

        :param request: 调用DescribeDDoSNetIpLog所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetIpLogRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetIpLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetIpLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetIpLogResponse()
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


    def DescribeDDoSNetTrend(self, request):
        """获取高防IP专业版资源的DDoS攻击指标数据

        :param request: 调用DescribeDDoSNetTrend所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetTrendRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSNetTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSNetTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSNetTrendResponse()
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


    def DescribeDDoSPolicy(self, request):
        """获取DDoS高级策略

        :param request: 调用DescribeDDoSPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSPolicyResponse()
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

        :param request: 调用DescribeDDoSTrend所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSTrendRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSTrendResponse`

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


    def DescribeDDoSUsedStatis(self, request):
        """统计用户的高防资源的使用天数和DDoS攻击防护次数

        :param request: 调用DescribeDDoSUsedStatis所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSUsedStatisRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeDDoSUsedStatisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDDoSUsedStatis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDDoSUsedStatisResponse()
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


    def DescribeInsurePacks(self, request):
        """获取保险包套餐列表

        :param request: 调用DescribeInsurePacks所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeInsurePacksRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeInsurePacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInsurePacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInsurePacksResponse()
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


    def DescribeIpBlockList(self, request):
        """获取IP封堵列表

        :param request: 调用DescribeIpBlockList所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeIpBlockListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeIpBlockListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpBlockList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpBlockListResponse()
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


    def DescribeL4HealthConfig(self, request):
        """导出四层健康检查配置

        :param request: 调用DescribeL4HealthConfig所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeL4HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeL4HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4HealthConfigResponse()
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


    def DescribeL4RulesErrHealth(self, request):
        """获取L4转发规则健康检查异常结果

        :param request: 调用DescribeL4RulesErrHealth所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeL4RulesErrHealthRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeL4RulesErrHealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4RulesErrHealth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4RulesErrHealthResponse()
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


    def DescribeL7HealthConfig(self, request):
        """导出七层健康检查配置

        :param request: 调用DescribeL7HealthConfig所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeL7HealthConfigRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeL7HealthConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7HealthConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7HealthConfigResponse()
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


    def DescribePackIndex(self, request):
        """获取产品总览统计，支持高防包、高防IP、高防IP专业版、棋牌盾

        :param request: 调用DescribePackIndex所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribePackIndexRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribePackIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePackIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePackIndexResponse()
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


    def DescribePcap(self, request):
        """下载攻击事件的pcap包

        :param request: 调用DescribePcap所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribePcapRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribePcapResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePcap", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePcapResponse()
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


    def DescribePolicyCase(self, request):
        """获取策略场景

        :param request: 调用DescribePolicyCase所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribePolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribePolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyCaseResponse()
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


    def DescribeResIpList(self, request):
        """获取资源的IP列表

        :param request: 调用DescribeResIpList所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeResIpListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeResIpListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResIpList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResIpListResponse()
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


    def DescribeResourceList(self, request):
        """获取资源列表

        :param request: 调用DescribeResourceList所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeResourceListRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeResourceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceListResponse()
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


    def DescribeRuleSets(self, request):
        """获取资源的规则数

        :param request: 调用DescribeRuleSets所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeRuleSetsRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeRuleSetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRuleSets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRuleSetsResponse()
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


    def DescribeSecIndex(self, request):
        """获取本月安全统计

        :param request: 调用DescribeSecIndex所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeSecIndexRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeSecIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecIndexResponse()
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


    def DescribeSourceIpSegment(self, request):
        """获取回源IP段，支持的产品：高防IP，高防IP专业版，棋牌盾；

        :param request: 调用DescribeSourceIpSegment所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeSourceIpSegmentRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeSourceIpSegmentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSourceIpSegment", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSourceIpSegmentResponse()
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


    def DescribeTransmitStatis(self, request):
        """获取业务转发统计数据，支持转发流量和转发包速率

        :param request: 调用DescribeTransmitStatis所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeTransmitStatisRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeTransmitStatisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTransmitStatis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTransmitStatisResponse()
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


    def DescribeUnBlockStatis(self, request):
        """获取黑洞解封次数

        :param request: 调用DescribeUnBlockStatis所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribeUnBlockStatisRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribeUnBlockStatisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnBlockStatis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnBlockStatisResponse()
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


    def DescribleL4Rules(self, request):
        """获取四层转发规则

        :param request: 调用DescribleL4Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribleL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribleL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribleL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribleL4RulesResponse()
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


    def DescribleL7Rules(self, request):
        """获取七层转发规则

        :param request: 调用DescribleL7Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribleL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribleL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribleL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribleL7RulesResponse()
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


    def DescribleRegionCount(self, request):
        """获取地域的资源实例数

        :param request: 调用DescribleRegionCount所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.DescribleRegionCountRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.DescribleRegionCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribleRegionCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribleRegionCountResponse()
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


    def ModifyCCHostProtection(self, request):
        """开启或关闭CC域名防护

        :param request: 调用ModifyCCHostProtection所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCHostProtectionRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCHostProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCHostProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCHostProtectionResponse()
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


    def ModifyCCIpAllowDeny(self, request):
        """添加或删除CC的IP黑白名单

        :param request: 调用ModifyCCIpAllowDeny所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCIpAllowDenyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCIpAllowDenyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCIpAllowDeny", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCIpAllowDenyResponse()
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


    def ModifyCCLevel(self, request):
        """修改CC防护等级

        :param request: 调用ModifyCCLevel所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCLevelRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCLevelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCLevel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCLevelResponse()
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


    def ModifyCCPolicySwitch(self, request):
        """修改CC自定义策略开关

        :param request: 调用ModifyCCPolicySwitch所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCPolicySwitchRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCPolicySwitchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCPolicySwitch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCPolicySwitchResponse()
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


    def ModifyCCSelfDefinePolicy(self, request):
        """修改CC自定义策略

        :param request: 调用ModifyCCSelfDefinePolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCSelfDefinePolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCSelfDefinePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCSelfDefinePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCSelfDefinePolicyResponse()
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


    def ModifyCCThreshold(self, request):
        """修改CC的防护阈值

        :param request: 调用ModifyCCThreshold所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCThresholdResponse()
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


    def ModifyCCUrlAllow(self, request):
        """添加或删除CC的URL白名单

        :param request: 调用ModifyCCUrlAllow所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyCCUrlAllowRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyCCUrlAllowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCCUrlAllow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCCUrlAllowResponse()
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


    def ModifyDDoSAIStatus(self, request):
        """读取或修改DDoS的AI防护状态

        :param request: 调用ModifyDDoSAIStatus所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSAIStatusRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSAIStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSAIStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSAIStatusResponse()
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


    def ModifyDDoSDefendStatus(self, request):
        """开启或关闭DDoS防护状态

        :param request: 调用ModifyDDoSDefendStatus所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSDefendStatusRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSDefendStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSDefendStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSDefendStatusResponse()
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


    def ModifyDDoSLevel(self, request):
        """读取或修改DDoS的防护等级

        :param request: 调用ModifyDDoSLevel所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSLevelRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSLevelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSLevel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSLevelResponse()
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


    def ModifyDDoSPolicy(self, request):
        """修改DDoS高级策略

        :param request: 调用ModifyDDoSPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyResponse()
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


    def ModifyDDoSPolicyCase(self, request):
        """修改策略场景

        :param request: 调用ModifyDDoSPolicyCase所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyCaseRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyCaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSPolicyCase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyCaseResponse()
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


    def ModifyDDoSPolicyName(self, request):
        """修改DDoS高级策略名称

        :param request: 调用ModifyDDoSPolicyName所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyNameRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSPolicyNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSPolicyName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSPolicyNameResponse()
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


    def ModifyDDoSSwitch(self, request):
        """开启或关闭DDoS防护，只支持基础防护产品；

        :param request: 调用ModifyDDoSSwitch所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSSwitchRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSSwitchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSSwitch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSSwitchResponse()
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


    def ModifyDDoSThreshold(self, request):
        """修改DDoS清洗阈值

        :param request: 调用ModifyDDoSThreshold所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSThresholdRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSThresholdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSThreshold", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSThresholdResponse()
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


    def ModifyDDoSWaterKey(self, request):
        """支持水印密钥的添加，删除，开启，关闭

        :param request: 调用ModifyDDoSWaterKey所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSWaterKeyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyDDoSWaterKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDDoSWaterKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDDoSWaterKeyResponse()
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


    def ModifyElasticLimit(self, request):
        """修改弹性防护阈值

        :param request: 调用ModifyElasticLimit所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyElasticLimitRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyElasticLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyElasticLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyElasticLimitResponse()
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


    def ModifyL4Health(self, request):
        """修改L4转发规则健康检查参数，支持的子产品：高防IP、高防IP专业版

        :param request: 调用ModifyL4Health所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL4HealthRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL4HealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4Health", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4HealthResponse()
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


    def ModifyL4KeepTime(self, request):
        """修改L4转发规则的会话保持，支持的子产品：高防IP、高防IP专业版

        :param request: 调用ModifyL4KeepTime所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL4KeepTimeRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL4KeepTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4KeepTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4KeepTimeResponse()
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


    def ModifyL4Rules(self, request):
        """修改L4转发规则

        :param request: 调用ModifyL4Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL4RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL4RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4RulesResponse()
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


    def ModifyL7Rules(self, request):
        """修改L7转发规则

        :param request: 调用ModifyL7Rules所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyL7RulesRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7RulesResponse()
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


    def ModifyResBindDDoSPolicy(self, request):
        """资源实例绑定DDoS高级策略

        :param request: 调用ModifyResBindDDoSPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.dayu.v20180709.models.ModifyResBindDDoSPolicyRequest`
        :rtype: :class:`tencentcloud.dayu.v20180709.models.ModifyResBindDDoSPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyResBindDDoSPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResBindDDoSPolicyResponse()
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