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


    def AddAntiFakeUrl(self, request):
        """添加防篡改url

        :param request: Request instance for AddAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.AddAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAntiInfoLeakRules(self, request):
        """添加信息防泄漏规则

        :param request: Request instance for AddAntiInfoLeakRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddAntiInfoLeakRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddAntiInfoLeakRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAntiInfoLeakRules", params, headers=headers)
            response = json.loads(body)
            model = models.AddAntiInfoLeakRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCustomRule(self, request):
        """增加访问控制（自定义策略）

        :param request: Request instance for AddCustomRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddCustomRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCustomWhiteRule(self, request):
        """增加精准白名单规则

        :param request: Request instance for AddCustomWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddCustomWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddCustomWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCustomWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddCustomWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddDomainWhiteRule(self, request):
        """增加域名规则白名单

        :param request: Request instance for AddDomainWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddDomainWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddDomainWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDomainWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddDomainWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddSpartaProtection(self, request):
        """添加Spart防护域名

        :param request: Request instance for AddSpartaProtection.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddSpartaProtectionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddSpartaProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSpartaProtection", params, headers=headers)
            response = json.loads(body)
            model = models.AddSpartaProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessExport(self, request):
        """本接口用于创建访问日志导出

        :param request: Request instance for CreateAccessExport.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateAccessExportRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateAccessExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccessExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccessExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHost(self, request):
        """clb-waf中添加防护的域名

        :param request: Request instance for CreateHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccessExport(self, request):
        """本接口用于删除访问日志导出

        :param request: Request instance for DeleteAccessExport.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAccessExportRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAccessExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccessExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccessExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAntiFakeUrl(self, request):
        """删除防篡改url

        :param request: Request instance for DeleteAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAntiInfoLeakRule(self, request):
        """信息防泄漏删除规则

        :param request: Request instance for DeleteAntiInfoLeakRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAntiInfoLeakRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAntiInfoLeakRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAntiInfoLeakRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAntiInfoLeakRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAttackDownloadRecord(self, request):
        """删除攻击日志下载任务记录

        :param request: Request instance for DeleteAttackDownloadRecord.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAttackDownloadRecordRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAttackDownloadRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAttackDownloadRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAttackDownloadRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCCRule(self, request):
        """Waf  CC V2 Delete接口

        :param request: Request instance for DeleteCCRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteCCRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteCCRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCCRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCCRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomRule(self, request):
        """删除自定义规则

        :param request: Request instance for DeleteCustomRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteCustomRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomWhiteRule(self, request):
        """删除精准白名单规则

        :param request: Request instance for DeleteCustomWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteCustomWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteCustomWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainWhiteRules(self, request):
        """删除域名规则白名单

        :param request: Request instance for DeleteDomainWhiteRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteDomainWhiteRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteDomainWhiteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainWhiteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainWhiteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDownloadRecord(self, request):
        """删除访问日志下载记录

        :param request: Request instance for DeleteDownloadRecord.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteDownloadRecordRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteDownloadRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDownloadRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDownloadRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHost(self, request):
        """删除CLB-WAF防护域名
        支持批量操作

        :param request: Request instance for DeleteHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIpAccessControl(self, request):
        """Waf IP黑白名单Delete接口

        :param request: Request instance for DeleteIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSession(self, request):
        """删除CC攻击的session设置

        :param request: Request instance for DeleteSession.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteSessionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSession", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSpartaProtection(self, request):
        """SAASWAF删除防护域名

        :param request: Request instance for DeleteSpartaProtection.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteSpartaProtectionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteSpartaProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSpartaProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSpartaProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessExports(self, request):
        """本接口用于获取访问日志导出列表

        :param request: Request instance for DescribeAccessExports.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAccessExportsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAccessExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessFastAnalysis(self, request):
        """本接口用于访问日志的快速分析

        :param request: Request instance for DescribeAccessFastAnalysis.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAccessFastAnalysisRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAccessFastAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessFastAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessFastAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessHistogram(self, request):
        """本接口用于访问日志柱状趋势图

        :param request: Request instance for DescribeAccessHistogram.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAccessHistogramRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAccessHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessIndex(self, request):
        """本接口用于获取访问日志索引配置信息

        :param request: Request instance for DescribeAccessIndex.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAccessIndexRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAccessIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiFakeRules(self, request):
        """获取防篡改url

        :param request: Request instance for DescribeAntiFakeRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiFakeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiFakeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiFakeUrl(self, request):
        """获取防篡改url

        :param request: Request instance for DescribeAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiInfoLeakRules(self, request):
        """老接口已经不再使用。

        获取信息防泄漏规则列表

        :param request: Request instance for DescribeAntiInfoLeakRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiInfoLeakRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiInfoLeakRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAntiInfoLeakageRules(self, request):
        """取得信息防泄漏规则列表

        :param request: Request instance for DescribeAntiInfoLeakageRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakageRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAntiInfoLeakageRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAntiInfoLeakageRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAntiInfoLeakageRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackOverview(self, request):
        """攻击总览

        :param request: Request instance for DescribeAttackOverview.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAttackOverviewRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAttackOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoDenyIP(self, request):
        """接口已废弃

        描述WAF自动封禁IP详情,对齐自动封堵状态

        :param request: Request instance for DescribeAutoDenyIP.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAutoDenyIPRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAutoDenyIPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoDenyIP", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoDenyIPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchIpAccessControl(self, request):
        """Waf 多域名ip黑白名单查询

        :param request: Request instance for DescribeBatchIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeBatchIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeBatchIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCRule(self, request):
        """Waf  CC V2 Query接口

        :param request: Request instance for DescribeCCRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCRuleList(self, request):
        """根据多条件查询CC规则

        :param request: Request instance for DescribeCCRuleList.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleListRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCCRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCiphersDetail(self, request):
        """查询加密套件信息

        :param request: Request instance for DescribeCiphersDetail.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCiphersDetailRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCiphersDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCiphersDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCiphersDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomRuleList(self, request):
        """获取防护配置中的访问控制策略列表

        :param request: Request instance for DescribeCustomRuleList.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRuleListRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCustomRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomWhiteRule(self, request):
        """获取防护配置中的精准白名单策略列表

        :param request: Request instance for DescribeCustomWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCustomWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCustomWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainCountInfo(self, request):
        """获取域名概况

        :param request: Request instance for DescribeDomainCountInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainCountInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainCountInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainCountInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainCountInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainDetailsClb(self, request):
        """获取一个clb域名详情

        :param request: Request instance for DescribeDomainDetailsClb.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsClbRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsClbResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainDetailsClb", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainDetailsClbResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainDetailsSaas(self, request):
        """查询单个saas域名详情

        :param request: Request instance for DescribeDomainDetailsSaas.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsSaasRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainDetailsSaasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainDetailsSaas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainDetailsSaasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainVerifyResult(self, request):
        """获取添加域名操作的结果

        :param request: Request instance for DescribeDomainVerifyResult.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainVerifyResultRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainVerifyResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainVerifyResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainVerifyResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainWhiteRules(self, request):
        """获取域名的规则白名单

        :param request: Request instance for DescribeDomainWhiteRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainWhiteRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainWhiteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainWhiteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainWhiteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomains(self, request):
        """查询用户所有域名的详细信息

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFindDomainList(self, request):
        """获取发现域名列表接口

        :param request: Request instance for DescribeFindDomainList.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeFindDomainListRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeFindDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFindDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFindDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowTrend(self, request):
        """获取waf流量访问趋势

        :param request: Request instance for DescribeFlowTrend.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeFlowTrendRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeFlowTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHost(self, request):
        """clb-waf获取防护域名详情

        :param request: Request instance for DescribeHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostLimit(self, request):
        """添加域名的首先验证是否购买了套餐，是否没有达到购买套餐的限制，域名是否已经添加

        :param request: Request instance for DescribeHostLimit.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHostLimitRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHostLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHosts(self, request):
        """clb-waf中获取防护域名列表

        :param request: Request instance for DescribeHosts.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHostsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """查询用户所有实例的详细信息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpAccessControl(self, request):
        """Waf ip黑白名单查询

        :param request: Request instance for DescribeIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpHitItems(self, request):
        """Waf  IP封堵状态查询

        :param request: Request instance for DescribeIpHitItems.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeIpHitItemsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeIpHitItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpHitItems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpHitItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePeakPoints(self, request):
        """查询业务和攻击概要趋势

        :param request: Request instance for DescribePeakPoints.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePeakPointsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePeakPointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePeakPoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePeakPointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePeakValue(self, request):
        """获取业务和攻击概览峰值

        :param request: Request instance for DescribePeakValue.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePeakValueRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePeakValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePeakValue", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePeakValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePolicyStatus(self, request):
        """获取防护状态以及生效的实例id

        :param request: Request instance for DescribePolicyStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePolicyStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePorts(self, request):
        """获取非标端口列表

        :param request: Request instance for DescribePorts.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePortsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePortsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePorts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePortsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleLimit(self, request):
        """获取各个模块具体的规格限制

        :param request: Request instance for DescribeRuleLimit.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeRuleLimitRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeRuleLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSession(self, request):
        """Waf 会话定义查询接口

        :param request: Request instance for DescribeSession.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeSessionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTlsVersion(self, request):
        """查询用户TLS版本

        :param request: Request instance for DescribeTlsVersion.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeTlsVersionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeTlsVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTlsVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTlsVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCdcClbWafRegions(self, request):
        """在CDC场景下，负载均衡型WAF的添加、编辑域名配置的时候，需要展示CDC负载均衡型WAF（cdc-clb-waf)支持的地域列表，通过DescribeUserCdcClbWafRegions既可以获得当前对客户已经开放的地域列表

        :param request: Request instance for DescribeUserCdcClbWafRegions.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserCdcClbWafRegionsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserCdcClbWafRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCdcClbWafRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserCdcClbWafRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserClbWafRegions(self, request):
        """在负载均衡型WAF的添加、编辑域名配置的时候，需要展示负载均衡型WAF（clb-waf)支持的地域列表，通过DescribeUserClbWafRegions既可以获得当前对客户已经开放的地域列表

        :param request: Request instance for DescribeUserClbWafRegions.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserClbWafRegionsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserClbWafRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserClbWafRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserClbWafRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDomainInfo(self, request):
        """查询saas和clb的域名信息

        :param request: Request instance for DescribeUserDomainInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserDomainInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserDomainInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDomainInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDomainInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVipInfo(self, request):
        """根据过滤条件查询VIP信息

        :param request: Request instance for DescribeVipInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeVipInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeVipInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVipInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVipInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafAutoDenyRules(self, request):
        """返回ip惩罚规则详细信息

        :param request: Request instance for DescribeWafAutoDenyRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeWafAutoDenyRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeWafAutoDenyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafAutoDenyRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafAutoDenyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafAutoDenyStatus(self, request):
        """描述WAF自动封禁模块详情

        :param request: Request instance for DescribeWafAutoDenyStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeWafAutoDenyStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeWafAutoDenyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafAutoDenyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafAutoDenyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafInfo(self, request):
        """获取负载均衡绑定的WAF信息，可以根据租户负载均衡实例ID、负载均衡监听器ID、负载均衡的域名信息来查询对应绑定的 Waf的状态信息。
        查询的范围：负载均衡实例ID、负载均衡实例ID+监听器ID、负载均衡实例ID+监听器ID+域名。
        可能的错误码：ResourceNotFound（没有找到对应的资源）、UnsupportedRegion（目前clb-waf只支持北京、广州、上海、成都、重庆、香港地域）。

        :param request: Request instance for DescribeWafInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeWafInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeWafInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafThreatenIntelligence(self, request):
        """描述WAF威胁情报封禁模块配置详情

        :param request: Request instance for DescribeWafThreatenIntelligence.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeWafThreatenIntelligenceRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeWafThreatenIntelligenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafThreatenIntelligence", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafThreatenIntelligenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreshAntiFakeUrl(self, request):
        """刷新防篡改url

        :param request: Request instance for FreshAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.FreshAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.FreshAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreshAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.FreshAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateDealsAndPayNew(self, request):
        """计费资源购买、续费下单接口

        :param request: Request instance for GenerateDealsAndPayNew.
        :type request: :class:`tencentcloud.waf.v20180125.models.GenerateDealsAndPayNewRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.GenerateDealsAndPayNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateDealsAndPayNew", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateDealsAndPayNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAttackDownloadRecords(self, request):
        """查询下载攻击日志任务记录列表

        :param request: Request instance for GetAttackDownloadRecords.
        :type request: :class:`tencentcloud.waf.v20180125.models.GetAttackDownloadRecordsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.GetAttackDownloadRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAttackDownloadRecords", params, headers=headers)
            response = json.loads(body)
            model = models.GetAttackDownloadRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAttackHistogram(self, request):
        """生成攻击日志的产生时间柱状图

        :param request: Request instance for GetAttackHistogram.
        :type request: :class:`tencentcloud.waf.v20180125.models.GetAttackHistogramRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.GetAttackHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAttackHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.GetAttackHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAttackTotalCount(self, request):
        """按照条件查询展示攻击总次数

        :param request: Request instance for GetAttackTotalCount.
        :type request: :class:`tencentcloud.waf.v20180125.models.GetAttackTotalCountRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.GetAttackTotalCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAttackTotalCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAttackTotalCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetInstanceQpsLimit(self, request):
        """获取套餐实例的弹性qps上限

        :param request: Request instance for GetInstanceQpsLimit.
        :type request: :class:`tencentcloud.waf.v20180125.models.GetInstanceQpsLimitRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.GetInstanceQpsLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInstanceQpsLimit", params, headers=headers)
            response = json.loads(body)
            model = models.GetInstanceQpsLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccessPeriod(self, request):
        """本接口用于修改访问日志保存期限及大字段是否存储

        :param request: Request instance for ModifyAccessPeriod.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAccessPeriodRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAccessPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccessPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiFakeUrl(self, request):
        """编辑防篡改url

        :param request: Request instance for ModifyAntiFakeUrl.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiFakeUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiFakeUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiFakeUrlStatus(self, request):
        """切换防篡改开关

        :param request: Request instance for ModifyAntiFakeUrlStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiFakeUrlStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiFakeUrlStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiFakeUrlStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiInfoLeakRuleStatus(self, request):
        """信息防泄漏切换规则开关

        :param request: Request instance for ModifyAntiInfoLeakRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiInfoLeakRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiInfoLeakRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiInfoLeakRules(self, request):
        """编辑信息防泄漏规则

        :param request: Request instance for ModifyAntiInfoLeakRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAntiInfoLeakRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAntiInfoLeakRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAntiInfoLeakRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApiAnalyzeStatus(self, request):
        """api分析页面开关

        :param request: Request instance for ModifyApiAnalyzeStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyApiAnalyzeStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyApiAnalyzeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiAnalyzeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiAnalyzeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAreaBanStatus(self, request):
        """修改防护域名的地域封禁状态

        :param request: Request instance for ModifyAreaBanStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAreaBanStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAreaBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAreaBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAreaBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBotStatus(self, request):
        """Bot_V2 bot总开关更新

        :param request: Request instance for ModifyBotStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyBotStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyBotStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBotStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBotStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomRule(self, request):
        """编辑自定义规则

        :param request: Request instance for ModifyCustomRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomRuleStatus(self, request):
        """开启或禁用访问控制（自定义策略）

        :param request: Request instance for ModifyCustomRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomWhiteRule(self, request):
        """编辑精准白名单

        :param request: Request instance for ModifyCustomWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomWhiteRuleStatus(self, request):
        """开启或禁用精准白名单

        :param request: Request instance for ModifyCustomWhiteRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyCustomWhiteRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyCustomWhiteRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomWhiteRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomWhiteRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainIpv6Status(self, request):
        """修改ipv6开关

        :param request: Request instance for ModifyDomainIpv6Status.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyDomainIpv6StatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyDomainIpv6StatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainIpv6Status", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainIpv6StatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainWhiteRule(self, request):
        """更改某一条规则

        :param request: Request instance for ModifyDomainWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyDomainWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyDomainWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainsCLSStatus(self, request):
        """修改域名列表的访问日志开关

        :param request: Request instance for ModifyDomainsCLSStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyDomainsCLSStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyDomainsCLSStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainsCLSStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainsCLSStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHost(self, request):
        """clb-waf编辑防护域名配置

        :param request: Request instance for ModifyHost.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostFlowMode(self, request):
        """clb-waf 设置防护域名的流量模式

        :param request: Request instance for ModifyHostFlowMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostFlowModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostFlowModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostFlowMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostFlowModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostMode(self, request):
        """clb-waf设置防护域名防护状态

        :param request: Request instance for ModifyHostMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostStatus(self, request):
        """clb-waf 设置防护域名WAF开关
        支持批量操作。

        :param request: Request instance for ModifyHostStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyHostStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyHostStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceElasticMode(self, request):
        """修改实例的QPS弹性计费开关

        :param request: Request instance for ModifyInstanceElasticMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceElasticModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceElasticModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceElasticMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceElasticModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceName(self, request):
        """修改实例的名称

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceQpsLimit(self, request):
        """设置套餐实例的弹性qps上限

        :param request: Request instance for ModifyInstanceQpsLimit.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceQpsLimitRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceQpsLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceQpsLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceQpsLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceRenewFlag(self, request):
        """修改实例的自动续费开关

        :param request: Request instance for ModifyInstanceRenewFlag.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceRenewFlagRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtectionStatus(self, request):
        """waf斯巴达-waf开关

        :param request: Request instance for ModifyProtectionStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyProtectionStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyProtectionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySpartaProtection(self, request):
        """修改域名配置

        :param request: Request instance for ModifySpartaProtection.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySpartaProtection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySpartaProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySpartaProtectionMode(self, request):
        """设置waf防护状态

        :param request: Request instance for ModifySpartaProtectionMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifySpartaProtectionModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySpartaProtectionMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySpartaProtectionModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWafAutoDenyRules(self, request):
        """修改ip惩罚规则

        :param request: Request instance for ModifyWafAutoDenyRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyWafAutoDenyRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyWafAutoDenyRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWafAutoDenyRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWafAutoDenyRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWafAutoDenyStatus(self, request):
        """配置WAF自动封禁模块状态

        :param request: Request instance for ModifyWafAutoDenyStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyWafAutoDenyStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyWafAutoDenyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWafAutoDenyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWafAutoDenyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWafThreatenIntelligence(self, request):
        """配置WAF威胁情报封禁模块详情

        :param request: Request instance for ModifyWafThreatenIntelligence.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyWafThreatenIntelligenceRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyWafThreatenIntelligenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWafThreatenIntelligence", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWafThreatenIntelligenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PostAttackDownloadTask(self, request):
        """创建搜索下载攻击日志任务，使用CLS新版本的搜索下载getlog接口

        :param request: Request instance for PostAttackDownloadTask.
        :type request: :class:`tencentcloud.waf.v20180125.models.PostAttackDownloadTaskRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.PostAttackDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PostAttackDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.PostAttackDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshAccessCheckResult(self, request):
        """刷新接入检查的结果，后台会生成接入检查任务

        :param request: Request instance for RefreshAccessCheckResult.
        :type request: :class:`tencentcloud.waf.v20180125.models.RefreshAccessCheckResultRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.RefreshAccessCheckResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshAccessCheckResult", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshAccessCheckResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchAccessLog(self, request):
        """本接口用于搜索WAF访问日志

        :param request: Request instance for SearchAccessLog.
        :type request: :class:`tencentcloud.waf.v20180125.models.SearchAccessLogRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.SearchAccessLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchAccessLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchAccessLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchAttackLog(self, request):
        """新版本CLS接口存在参数变化，query改成了query_string支持lucence语法接口搜索查询。

        :param request: Request instance for SearchAttackLog.
        :type request: :class:`tencentcloud.waf.v20180125.models.SearchAttackLogRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.SearchAttackLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchAttackLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchAttackLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDomainRules(self, request):
        """切换域名的规则开关

        :param request: Request instance for SwitchDomainRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.SwitchDomainRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.SwitchDomainRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDomainRules", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDomainRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpsertCCRule(self, request):
        """Waf  CC V2 Upsert接口

        :param request: Request instance for UpsertCCRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.UpsertCCRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.UpsertCCRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpsertCCRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpsertCCRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpsertIpAccessControl(self, request):
        """Waf IP黑白名单Upsert接口

        :param request: Request instance for UpsertIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.UpsertIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.UpsertIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpsertIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.UpsertIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpsertSession(self, request):
        """Waf  会话定义 Upsert接口

        :param request: Request instance for UpsertSession.
        :type request: :class:`tencentcloud.waf.v20180125.models.UpsertSessionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.UpsertSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpsertSession", params, headers=headers)
            response = json.loads(body)
            model = models.UpsertSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))