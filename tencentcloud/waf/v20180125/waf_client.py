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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.waf.v20180125 import models


class WafClient(AbstractClient):
    _apiVersion = '2018-01-25'
    _endpoint = 'waf.tencentcloudapi.com'
    _service = 'waf'


    def AddAntiFakeUrl(self, request):
        r"""添加防篡改url

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
        r"""添加信息防泄漏规则

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


    def AddAreaBanAreas(self, request):
        r"""添加地域封禁中的地域信息

        :param request: Request instance for AddAreaBanAreas.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddAreaBanAreasRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddAreaBanAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAreaBanAreas", params, headers=headers)
            response = json.loads(body)
            model = models.AddAreaBanAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddAttackWhiteRule(self, request):
        r"""供用户控制台调用，增加Tiga规则引擎白名单。

        :param request: Request instance for AddAttackWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.AddAttackWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.AddAttackWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAttackWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddAttackWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddCustomRule(self, request):
        r"""增加访问控制（自定义策略）

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
        r"""增加精准白名单规则

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
        r"""增加域名规则白名单

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
        r"""添加SaaS型WAF防护域名

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


    def BatchOperateUserSignatureRules(self, request):
        r"""批量操作tiga子规则

        :param request: Request instance for BatchOperateUserSignatureRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.BatchOperateUserSignatureRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.BatchOperateUserSignatureRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchOperateUserSignatureRules", params, headers=headers)
            response = json.loads(body)
            model = models.BatchOperateUserSignatureRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccessExport(self, request):
        r"""本接口用于创建访问日志导出

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


    def CreateAreaBanRule(self, request):
        r"""添加（编辑）地域封禁中的地域信息

        :param request: Request instance for CreateAreaBanRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateAreaBanRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateAreaBanRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAreaBanRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAreaBanRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBatchIpAccessControl(self, request):
        r"""批量IP黑白名单新增接口

        :param request: Request instance for CreateBatchIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateBatchIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateBatchIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBatchIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBatchIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeals(self, request):
        r"""计费资源购买、续费下单接口

        :param request: Request instance for CreateDeals.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateDealsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateDealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeals", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExport(self, request):
        r"""本接口仅创建下载任务，任务返回的下载地址，请用户调用DescribeExports查看任务列表。其中有下载地址CosPath参数。参考文档https://cloud.tencent.com/document/product/614/56449

        :param request: Request instance for CreateExport.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateExportRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHost(self, request):
        r"""clb-waf中添加防护域名

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


    def CreateIpAccessControl(self, request):
        r"""Waf IP黑白名单新增接口

        :param request: Request instance for CreateIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOwaspWhiteRule(self, request):
        r"""添加规则引擎白名单

        :param request: Request instance for CreateOwaspWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreateOwaspWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreateOwaspWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOwaspWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOwaspWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePostCKafkaFlow(self, request):
        r"""创建CKafka投递流任务

        :param request: Request instance for CreatePostCKafkaFlow.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreatePostCKafkaFlowRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreatePostCKafkaFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePostCKafkaFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePostCKafkaFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePostCLSFlow(self, request):
        r"""创建CLS投递流任务

        :param request: Request instance for CreatePostCLSFlow.
        :type request: :class:`tencentcloud.waf.v20180125.models.CreatePostCLSFlowRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.CreatePostCLSFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePostCLSFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePostCLSFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccessExport(self, request):
        r"""本接口用于删除访问日志导出

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
        r"""删除防篡改url

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
        r"""信息防泄漏删除规则

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
        r"""删除攻击日志下载任务记录

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


    def DeleteAttackWhiteRule(self, request):
        r"""供用户控制台调用，删除Tiga规则引擎白名单。

        :param request: Request instance for DeleteAttackWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteAttackWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteAttackWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAttackWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAttackWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBatchIpAccessControl(self, request):
        r"""批量黑白名单删除接口

        :param request: Request instance for DeleteBatchIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteBatchIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteBatchIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBatchIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBatchIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBotSceneUCBRule(self, request):
        r"""场景化后删除Bot的UCB自定义规则

        :param request: Request instance for DeleteBotSceneUCBRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteBotSceneUCBRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteBotSceneUCBRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBotSceneUCBRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBotSceneUCBRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCCRule(self, request):
        r"""Waf  CC V2 Delete接口

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
        r"""删除自定义规则

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
        r"""删除精准白名单规则

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
        r"""删除域名规则白名单

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


    def DeleteExport(self, request):
        r"""本接口用于删除日志下载任务

        :param request: Request instance for DeleteExport.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteExportRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHost(self, request):
        r"""删除负载均衡型域名，支持批量操作。

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
        r"""Waf IP黑白名单Delete接口（建议使用DeleteIpAccessControlV2来替换当前接口）

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


    def DeleteIpAccessControlV2(self, request):
        r"""Waf IP黑白名单最新版本删除接口

        :param request: Request instance for DeleteIpAccessControlV2.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteIpAccessControlV2Request`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteIpAccessControlV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIpAccessControlV2", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIpAccessControlV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOwaspRuleStatus(self, request):
        r"""解除门神规则的状态锁

        :param request: Request instance for DeleteOwaspRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteOwaspRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteOwaspRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOwaspRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOwaspRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOwaspWhiteRule(self, request):
        r"""删除用户规则引擎白名单

        :param request: Request instance for DeleteOwaspWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DeleteOwaspWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DeleteOwaspWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOwaspWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOwaspWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSession(self, request):
        r"""删除CC攻击的session设置

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
        r"""SaaS型WAF删除防护域名

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
        r"""本接口用于获取访问日志导出列表

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
        r"""本接口用于访问日志的快速分析

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
        r"""本接口用于访问日志柱状趋势图

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
        r"""本接口用于获取访问日志索引配置信息

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
        r"""获取防篡改url

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


    def DescribeAntiInfoLeakageRules(self, request):
        r"""取得信息防泄漏规则列表

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


    def DescribeApiDetail(self, request):
        r"""获取Api请求详情信息

        :param request: Request instance for DescribeApiDetail.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeApiDetailRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeApiDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiListVersionTwo(self, request):
        r"""api资产列表

        :param request: Request instance for DescribeApiListVersionTwo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeApiListVersionTwoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeApiListVersionTwoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiListVersionTwo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiListVersionTwoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAreaBanAreas(self, request):
        r"""获取地域封禁配置包括地域封禁开关，设置封禁的地区信息

        :param request: Request instance for DescribeAreaBanAreas.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAreaBanAreasRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAreaBanAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAreaBanAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAreaBanAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAreaBanRule(self, request):
        r"""获取地域封禁规则配置

        :param request: Request instance for DescribeAreaBanRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAreaBanRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAreaBanRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAreaBanRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAreaBanRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAreaBanSupportAreas(self, request):
        r"""获取WAF地域封禁支持的地域列表

        :param request: Request instance for DescribeAreaBanSupportAreas.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAreaBanSupportAreasRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAreaBanSupportAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAreaBanSupportAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAreaBanSupportAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackOverview(self, request):
        r"""攻击总览

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


    def DescribeAttackType(self, request):
        r"""查询指定域名TOP N攻击类型

        :param request: Request instance for DescribeAttackType.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAttackTypeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAttackTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackWhiteRule(self, request):
        r"""获取用户规则白名单列表

        :param request: Request instance for DescribeAttackWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeAttackWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeAttackWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoDenyIP(self, request):
        r"""描述WAF自动封禁IP详情,对齐自动封堵状态

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
        r"""Waf 批量防护IP黑白名单查询

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


    def DescribeBotSceneList(self, request):
        r"""获取BOT场景列表与概览

        :param request: Request instance for DescribeBotSceneList.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeBotSceneListRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeBotSceneListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotSceneList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBotSceneListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBotSceneOverview(self, request):
        r"""获取Bot场景全局概览

        :param request: Request instance for DescribeBotSceneOverview.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeBotSceneOverviewRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeBotSceneOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotSceneOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBotSceneOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBotSceneUCBRule(self, request):
        r"""场景化后Bot获取UCB自定义规则策略

        :param request: Request instance for DescribeBotSceneUCBRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeBotSceneUCBRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeBotSceneUCBRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotSceneUCBRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBotSceneUCBRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCAutoStatus(self, request):
        r"""获取SAAS型接入的紧急CC防护状态

        :param request: Request instance for DescribeCCAutoStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCCAutoStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCCAutoStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCAutoStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCAutoStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCRule(self, request):
        r"""Waf  CC V2 Query接口

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
        r"""根据多条件查询CC规则

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


    def DescribeCertificateVerifyResult(self, request):
        r"""获取证书的检查结果

        :param request: Request instance for DescribeCertificateVerifyResult.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeCertificateVerifyResultRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeCertificateVerifyResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateVerifyResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateVerifyResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCiphersDetail(self, request):
        r"""Saas型WAF接入查询加密套件信息

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
        r"""获取防护配置中的访问控制策略列表

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
        r"""获取防护配置中的精准白名单策略列表

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
        r"""获取域名概况

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
        r"""获取一个clbwaf域名详情

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
        r"""查询单个saaswaf域名详情

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


    def DescribeDomainRules(self, request):
        r"""拉取域名的防护规则列表

        :param request: Request instance for DescribeDomainRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeDomainRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeDomainRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainVerifyResult(self, request):
        r"""获取添加域名操作的结果

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
        r"""获取域名的规则白名单

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
        r"""查询用户所有域名的详细信息

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


    def DescribeExports(self, request):
        r"""本接口用于获取日志下载任务列表

        :param request: Request instance for DescribeExports.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeExportsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFindDomainList(self, request):
        r"""获取发现域名列表接口

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
        r"""获取waf流量访问趋势

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


    def DescribeHistogram(self, request):
        r"""查询多种条件的聚类分析

        :param request: Request instance for DescribeHistogram.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeHistogramRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHost(self, request):
        r"""clb-waf获取防护域名详情

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
        r"""添加域名的首先验证是否购买了套餐，是否没有达到购买套餐的限制，域名是否已经添加

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
        r"""clb-waf中获取防护域名列表

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
        r"""查询用户所有实例的详细信息

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
        r"""Waf ip黑白名单查询

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
        r"""Waf  IP封堵状态查询

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


    def DescribeLogHistogram(self, request):
        r"""本接口用于构建日志数量直方图

        :param request: Request instance for DescribeLogHistogram.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeLogHistogramRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeLogHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModuleStatus(self, request):
        r"""查询各个waf基础安全模块的开关状态，看每个模块是否开启

        :param request: Request instance for DescribeModuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeModuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeModuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeObjects(self, request):
        r"""查看防护对象列表

        :param request: Request instance for DescribeObjects.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeObjectsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeObjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOwaspRuleTypes(self, request):
        r"""查询规则引擎的规则类型列表

        :param request: Request instance for DescribeOwaspRuleTypes.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeOwaspRuleTypesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeOwaspRuleTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOwaspRuleTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOwaspRuleTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOwaspRules(self, request):
        r"""查询规则引擎的规则列表

        :param request: Request instance for DescribeOwaspRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeOwaspRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeOwaspRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOwaspRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOwaspRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOwaspWhiteRules(self, request):
        r"""获取规则引擎白名单列表

        :param request: Request instance for DescribeOwaspWhiteRules.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeOwaspWhiteRulesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeOwaspWhiteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOwaspWhiteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOwaspWhiteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePeakPoints(self, request):
        r"""查询业务和攻击概要趋势

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
        r"""获取业务和攻击概览峰值

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
        r"""获取防护状态以及生效的实例id

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
        r"""获取Saas型WAF防护端口列表

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


    def DescribePostCKafkaFlows(self, request):
        r"""获取CKafka投递流任务列表

        :param request: Request instance for DescribePostCKafkaFlows.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePostCKafkaFlowsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePostCKafkaFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostCKafkaFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostCKafkaFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePostCLSFlows(self, request):
        r"""获取CLS投递流任务列表

        :param request: Request instance for DescribePostCLSFlows.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribePostCLSFlowsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribePostCLSFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostCLSFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostCLSFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectionModes(self, request):
        r"""查询Tiga引擎大类规则及其防护模式

        :param request: Request instance for DescribeProtectionModes.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeProtectionModesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeProtectionModesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectionModes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectionModesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleLimit(self, request):
        r"""获取各个模块具体的规格限制

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


    def DescribeScanIp(self, request):
        r"""查询扫描ip

        :param request: Request instance for DescribeScanIp.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeScanIpRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeScanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSession(self, request):
        r"""Waf 会话定义查询接口

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


    def DescribeSpartaProtectionInfo(self, request):
        r"""waf斯巴达-获取防护域名信息

        :param request: Request instance for DescribeSpartaProtectionInfo.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeSpartaProtectionInfoRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeSpartaProtectionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpartaProtectionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpartaProtectionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTlsVersion(self, request):
        r"""查询SaaS型WAF支持的TLS版本

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


    def DescribeTopAttackDomain(self, request):
        r"""查询Top5的攻击域名

        :param request: Request instance for DescribeTopAttackDomain.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeTopAttackDomainRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeTopAttackDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopAttackDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopAttackDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopics(self, request):
        r"""本接口用于获取日志主题列表，支持分页

        :param request: Request instance for DescribeTopics.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeTopicsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserCdcClbWafRegions(self, request):
        r"""在CDC场景下，负载均衡型WAF的添加、编辑域名配置的时候，需要展示CDC负载均衡型WAF（cdc-clb-waf)支持的地域列表，通过DescribeUserCdcClbWafRegions既可以获得当前对客户已经开放的地域列表

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
        r"""在负载均衡型WAF的添加、编辑域名配置的时候，需要展示负载均衡型WAF（clb-waf)支持的地域列表，通过DescribeUserClbWafRegions既可以获得当前对客户已经开放的地域列表

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
        r"""查询saas和clb的域名信息

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


    def DescribeUserLevel(self, request):
        r"""获取用户防护规则等级

        :param request: Request instance for DescribeUserLevel.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserLevelRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserLevel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserSignatureClass(self, request):
        r"""查询Tiga引擎规则类型及状态

        :param request: Request instance for DescribeUserSignatureClass.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserSignatureClassRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserSignatureClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserSignatureClass", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserSignatureClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserSignatureRule(self, request):
        r"""获取用户特征规则列表

        :param request: Request instance for DescribeUserSignatureRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserSignatureRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserSignatureRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserSignatureRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserSignatureRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserSignatureRuleV2(self, request):
        r"""获取用户特征规则列表

        :param request: Request instance for DescribeUserSignatureRuleV2.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeUserSignatureRuleV2Request`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeUserSignatureRuleV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserSignatureRuleV2", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserSignatureRuleV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVipInfo(self, request):
        r"""根据过滤条件查询VIP信息

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
        r"""返回ip惩罚规则详细信息

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
        r"""废弃接口

        描述WAF自动封禁模块详情

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


    def DescribeWafThreatenIntelligence(self, request):
        r"""描述WAF威胁情报封禁模块配置详情

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


    def DescribeWebshellStatus(self, request):
        r"""获取域名的webshell状态

        :param request: Request instance for DescribeWebshellStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.DescribeWebshellStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DescribeWebshellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebshellStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebshellStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyPostCKafkaFlow(self, request):
        r"""销毁CKafka投递流任务

        :param request: Request instance for DestroyPostCKafkaFlow.
        :type request: :class:`tencentcloud.waf.v20180125.models.DestroyPostCKafkaFlowRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DestroyPostCKafkaFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPostCKafkaFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPostCKafkaFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyPostCLSFlow(self, request):
        r"""销毁CLS投递流任务

        :param request: Request instance for DestroyPostCLSFlow.
        :type request: :class:`tencentcloud.waf.v20180125.models.DestroyPostCLSFlowRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.DestroyPostCLSFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPostCLSFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPostCLSFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreshAntiFakeUrl(self, request):
        r"""刷新防篡改url

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
        r"""计费资源购买、续费下单接口

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
        r"""查询下载攻击日志任务记录列表

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
        r"""生成攻击日志的产生时间柱状图

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
        r"""按照条件查询展示攻击总次数

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
        r"""获取套餐实例的弹性qps上限

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


    def ImportIpAccessControl(self, request):
        r"""导入IP黑白名单

        :param request: Request instance for ImportIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.ImportIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ImportIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.ImportIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAntiFakeUrl(self, request):
        r"""编辑防篡改url

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
        r"""切换防篡改开关

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
        r"""信息防泄漏切换规则开关

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
        r"""编辑信息防泄漏规则

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
        r"""api分析页面开关

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


    def ModifyApiSecEventChange(self, request):
        r"""api安全状态变更接口

        :param request: Request instance for ModifyApiSecEventChange.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyApiSecEventChangeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyApiSecEventChangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiSecEventChange", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiSecEventChangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAreaBanAreas(self, request):
        r"""修改地域封禁中的地域信息

        :param request: Request instance for ModifyAreaBanAreas.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAreaBanAreasRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAreaBanAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAreaBanAreas", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAreaBanAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAreaBanRule(self, request):
        r"""添加（编辑）地域封禁中的地域信息

        :param request: Request instance for ModifyAreaBanRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAreaBanRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAreaBanRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAreaBanRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAreaBanRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAreaBanStatus(self, request):
        r"""修改防护域名的地域封禁状态

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


    def ModifyAttackWhiteRule(self, request):
        r"""供用户控制台调用，修改Tiga规则引擎白名单。

        :param request: Request instance for ModifyAttackWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyAttackWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyAttackWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAttackWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAttackWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBatchIpAccessControl(self, request):
        r"""批量IP黑白名单新增接口

        :param request: Request instance for ModifyBatchIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyBatchIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyBatchIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBatchIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBatchIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBotSceneStatus(self, request):
        r"""bot子场景开关

        :param request: Request instance for ModifyBotSceneStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyBotSceneStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyBotSceneStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBotSceneStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBotSceneStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBotSceneUCBRule(self, request):
        r"""【接口复用】场景化后更新Bot的UCB自定义规则，两个调用位置：1.BOT全局白名单 2.BOT场景配置

        :param request: Request instance for ModifyBotSceneUCBRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyBotSceneUCBRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyBotSceneUCBRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBotSceneUCBRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBotSceneUCBRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBotStatus(self, request):
        r"""Bot_V2 bot总开关更新

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
        r"""编辑自定义规则

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
        r"""开启或禁用访问控制（自定义策略）

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
        r"""编辑精准白名单

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
        r"""开启或禁用精准白名单

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
        r"""切换ipv6开关

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


    def ModifyDomainPostAction(self, request):
        r"""修改域名投递状态

        :param request: Request instance for ModifyDomainPostAction.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyDomainPostActionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyDomainPostActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainPostAction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainPostActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainWhiteRule(self, request):
        r"""修改域名规则白名单

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
        r"""修改域名列表的访问日志开关

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


    def ModifyGenerateDeals(self, request):
        r"""提供给clb等使用的waf实例下单接口，目前只支持clb旗舰版实例的下单，该接口会进行入参校验，然后调用是否为收购用户，然后调用计费接口下单。目前只支持预付费下单

        :param request: Request instance for ModifyGenerateDeals.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyGenerateDealsRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyGenerateDealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGenerateDeals", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGenerateDealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHost(self, request):
        r"""编辑负载均衡型WAF防护域名配置

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
        r"""设置负载均衡型WAF防护域名的流量模式，切换镜像模式和清洗模式

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
        r"""clb-waf设置防护域名防护状态

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
        r"""clb-waf 设置防护域名WAF开关
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


    def ModifyInstanceAttackLogPost(self, request):
        r"""修改实例攻击日志投递开关，企业版及以上版本可以开通，否则返回错误

        :param request: Request instance for ModifyInstanceAttackLogPost.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceAttackLogPostRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyInstanceAttackLogPostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceAttackLogPost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceAttackLogPostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceElasticMode(self, request):
        r"""修改实例的QPS弹性计费开关

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
        r"""修改实例的名称

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
        r"""设置套餐实例的弹性qps上限

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
        r"""修改实例的自动续费开关

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


    def ModifyIpAccessControl(self, request):
        r"""Waf IP黑白名单编辑接口

        :param request: Request instance for ModifyIpAccessControl.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyIpAccessControlRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyIpAccessControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIpAccessControl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIpAccessControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleStatus(self, request):
        r"""设置某个domain下基础安全模块的开关

        :param request: Request instance for ModifyModuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyModuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyModuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyObject(self, request):
        r"""修改防护对象

        :param request: Request instance for ModifyObject.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyObjectRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyObject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOwaspRuleStatus(self, request):
        r"""更新规则的开关

        :param request: Request instance for ModifyOwaspRuleStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOwaspRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOwaspRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOwaspRuleTypeAction(self, request):
        r"""更新规则类型的防护模式

        :param request: Request instance for ModifyOwaspRuleTypeAction.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleTypeActionRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleTypeActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOwaspRuleTypeAction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOwaspRuleTypeActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOwaspRuleTypeLevel(self, request):
        r"""更新规则类型的防护等级

        :param request: Request instance for ModifyOwaspRuleTypeLevel.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleTypeLevelRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleTypeLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOwaspRuleTypeLevel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOwaspRuleTypeLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOwaspRuleTypeStatus(self, request):
        r"""更新规则类型的开关

        :param request: Request instance for ModifyOwaspRuleTypeStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleTypeStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspRuleTypeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOwaspRuleTypeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOwaspRuleTypeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOwaspWhiteRule(self, request):
        r"""编辑规则引擎白名单

        :param request: Request instance for ModifyOwaspWhiteRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspWhiteRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyOwaspWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOwaspWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOwaspWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtectionLevel(self, request):
        r"""更改防护等级

        :param request: Request instance for ModifyProtectionLevel.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyProtectionLevelRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyProtectionLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectionLevel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectionLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtectionStatus(self, request):
        r"""开启、关闭WAF开关

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
        r"""编辑SaaS型WAF域名配置

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
        r"""设置waf防护状态

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


    def ModifyUserLevel(self, request):
        r"""修改用户防护规则等级

        :param request: Request instance for ModifyUserLevel.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyUserLevelRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyUserLevelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserLevel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserLevelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserSignatureClass(self, request):
        r"""切换Tiga引擎规则类型的生效开关

        :param request: Request instance for ModifyUserSignatureClass.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureClassRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserSignatureClass", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserSignatureClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserSignatureRule(self, request):
        r"""修改用户防护规则，开启关闭具体的某条规则

        :param request: Request instance for ModifyUserSignatureRule.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureRuleRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserSignatureRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserSignatureRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserSignatureRuleV2(self, request):
        r"""修改用户防护规则，开启关闭具体的某条规则

        :param request: Request instance for ModifyUserSignatureRuleV2.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureRuleV2Request`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyUserSignatureRuleV2Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserSignatureRuleV2", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserSignatureRuleV2Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWafAutoDenyRules(self, request):
        r"""修改ip惩罚规则

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


    def ModifyWafThreatenIntelligence(self, request):
        r"""配置WAF威胁情报封禁模块详情

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


    def ModifyWebshellStatus(self, request):
        r"""设置域名的webshell状态。

        :param request: Request instance for ModifyWebshellStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.ModifyWebshellStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.ModifyWebshellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebshellStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebshellStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PostAttackDownloadTask(self, request):
        r"""创建搜索下载攻击日志任务，使用CLS新版本的搜索下载getlog接口

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
        r"""刷新接入检查的结果，后台会生成接入检查任务

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
        r"""本接口用于搜索WAF访问日志

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
        r"""新版本CLS接口存在参数变化，query改成了query_string支持lucence语法接口搜索查询。

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


    def SearchLog(self, request):
        r"""本接口用于检索分析日志，使用该接口时请注意如下事项：
        1. 该接口除受默认接口请求频率限制外，针对单个日志主题，查询并发数不能超过15。
        2. 检索语法建议使用CQL语法规则，请使用SyntaxRule参数，将值设置为1。
        3. API返回数据包最大49MB，建议启用 gzip 压缩（HTTP Request Header Accept-Encoding:gzip）。

        :param request: Request instance for SearchLog.
        :type request: :class:`tencentcloud.waf.v20180125.models.SearchLogRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.SearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDomainRules(self, request):
        r"""切换域名的规则开关

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


    def SwitchElasticMode(self, request):
        r"""切换弹性的开关

        :param request: Request instance for SwitchElasticMode.
        :type request: :class:`tencentcloud.waf.v20180125.models.SwitchElasticModeRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.SwitchElasticModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchElasticMode", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchElasticModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProtectionModes(self, request):
        r"""更新Tiga引擎下大类规则的防护模式

        :param request: Request instance for UpdateProtectionModes.
        :type request: :class:`tencentcloud.waf.v20180125.models.UpdateProtectionModesRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.UpdateProtectionModesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProtectionModes", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProtectionModesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpsertCCAutoStatus(self, request):
        r"""编辑SAAS型接入的紧急CC防护状态

        :param request: Request instance for UpsertCCAutoStatus.
        :type request: :class:`tencentcloud.waf.v20180125.models.UpsertCCAutoStatusRequest`
        :rtype: :class:`tencentcloud.waf.v20180125.models.UpsertCCAutoStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpsertCCAutoStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpsertCCAutoStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpsertCCRule(self, request):
        r"""Waf  CC V2 Upsert接口

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
        r"""Waf IP黑白名单Upsert接口（建议使用CreateIpAccessControl、ModifyIpAccessControl来替换当前接口）

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
        r"""Waf  会话定义 Upsert接口

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