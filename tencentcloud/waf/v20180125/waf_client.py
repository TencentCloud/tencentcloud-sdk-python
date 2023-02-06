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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoDenyIP(self, request):
        """描述WAF自动封禁IP详情,对齐自动封堵状态

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccessPeriod(self, request):
        """本接口用于修改访问日志保存期限

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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)


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
                raise TencentCloudSDKException(e.message, e.message)