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
from tencentcloud.waf.v20180125 import models


class WafClient(AbstractClient):
    _apiVersion = '2018-01-25'
    _endpoint = 'waf.tencentcloudapi.com'
    _service = 'waf'


    def AddCustomRule(self, request):
        """增加自定义策略

        :param request: Request instance for AddCustomRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddCustomRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddCustomRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddCustomRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddCustomRuleResponse()
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


    def CreateAttackDownloadTask(self, request):
        """创建攻击日志下载任务

        :param request: Request instance for CreateAttackDownloadTask.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateAttackDownloadTaskRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateAttackDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAttackDownloadTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAttackDownloadTaskResponse()
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


    def DeleteAttackDownloadRecord(self, request):
        """删除攻击日志下载任务记录

        :param request: Request instance for DeleteAttackDownloadRecord.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAttackDownloadRecordRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAttackDownloadRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAttackDownloadRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAttackDownloadRecordResponse()
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


    def DeleteDownloadRecord(self, request):
        """删除访问日志下载记录

        :param request: Request instance for DeleteDownloadRecord.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteDownloadRecordRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteDownloadRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDownloadRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDownloadRecordResponse()
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


    def DeleteSession(self, request):
        """删除CC攻击的session设置

        :param request: Request instance for DeleteSession.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteSessionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteSessionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSession", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSessionResponse()
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


    def DescribeCustomRules(self, request):
        """获取防护配置中的自定义策略列表

        :param request: Request instance for DescribeCustomRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomRulesResponse()
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


    def DescribeFlowTrend(self, request):
        """获取waf流量访问趋势

        :param request: Request instance for DescribeFlowTrend.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeFlowTrendRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeFlowTrendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowTrend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowTrendResponse()
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


    def DescribeUserClbWafRegions(self, request):
        """在负载均衡型WAF的添加、编辑域名配置的时候，需要展示负载均衡型WAF（clb-waf)支持的地域列表，通过DescribeUserClbWafRegions既可以获得当前对客户已经开放的地域列表

        :param request: Request instance for DescribeUserClbWafRegions.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserClbWafRegionsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserClbWafRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserClbWafRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserClbWafRegionsResponse()
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


    def ModifyAccessPeriod(self, request):
        """本接口用于修改访问日志保存期限

        :param request: Request instance for ModifyAccessPeriod.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAccessPeriodRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAccessPeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessPeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessPeriodResponse()
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


    def ModifyCustomRuleStatus(self, request):
        """开启或禁用自定义策略

        :param request: Request instance for ModifyCustomRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCustomRuleStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCustomRuleStatusResponse()
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