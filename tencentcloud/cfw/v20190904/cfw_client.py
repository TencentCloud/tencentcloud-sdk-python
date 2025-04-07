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
from tencentcloud.cfw.v20190904 import models


class CfwClient(AbstractClient):
    _apiVersion = '2019-09-04'
    _endpoint = 'cfw.tencentcloudapi.com'
    _service = 'cfw'


    def AddAclRule(self, request):
        """添加互联网边界访问控制规则

        :param request: Request instance for AddAclRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddAclRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddEnterpriseSecurityGroupRules(self, request):
        """创建新企业安全组规则

        :param request: Request instance for AddEnterpriseSecurityGroupRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddEnterpriseSecurityGroupRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddEnterpriseSecurityGroupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEnterpriseSecurityGroupRules", params, headers=headers)
            response = json.loads(body)
            model = models.AddEnterpriseSecurityGroupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNatAcRule(self, request):
        """添加nat访问控制规则

        :param request: Request instance for AddNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddVpcAcRule(self, request):
        """添加VPC内网间规则

        :param request: Request instance for AddVpcAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddVpcAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddVpcAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddVpcAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.AddVpcAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAcRules(self, request):
        """创建访问控制规则

        :param request: Request instance for CreateAcRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAcRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAddressTemplate(self, request):
        """创建地址模板规则

        :param request: Request instance for CreateAddressTemplate.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAddressTemplateRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlertCenterIsolate(self, request):
        """用户告警中心-封隔离处置按钮

        :param request: Request instance for CreateAlertCenterIsolate.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAlertCenterIsolateRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAlertCenterIsolateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlertCenterIsolate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlertCenterIsolateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlertCenterOmit(self, request):
        """用户告警中心-忽略处置按钮

        :param request: Request instance for CreateAlertCenterOmit.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAlertCenterOmitRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAlertCenterOmitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlertCenterOmit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlertCenterOmitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlertCenterRule(self, request):
        """用户告警中心-封禁、放通处置按钮

        :param request: Request instance for CreateAlertCenterRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAlertCenterRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAlertCenterRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlertCenterRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlertCenterRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBlockIgnoreRuleList(self, request):
        """批量添加入侵防御封禁列表、放通列表规则

        :param request: Request instance for CreateBlockIgnoreRuleList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateBlockIgnoreRuleListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateBlockIgnoreRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBlockIgnoreRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBlockIgnoreRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBlockIgnoreRuleNew(self, request):
        """批量添加入侵防御封禁列表、放通列表规则

        :param request: Request instance for CreateBlockIgnoreRuleNew.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateBlockIgnoreRuleNewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateBlockIgnoreRuleNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBlockIgnoreRuleNew", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBlockIgnoreRuleNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateChooseVpcs(self, request):
        """创建、选择vpc

        :param request: Request instance for CreateChooseVpcs.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateChooseVpcsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateChooseVpcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChooseVpcs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChooseVpcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatabaseWhiteListRules(self, request):
        """创建暴露数据库白名单规则

        :param request: Request instance for CreateDatabaseWhiteListRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateDatabaseWhiteListRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateDatabaseWhiteListRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatabaseWhiteListRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatabaseWhiteListRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIdsWhiteRule(self, request):
        """CreateIdsWhiteRule

        创建入侵防御规则白名单接口

        :param request: Request instance for CreateIdsWhiteRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateIdsWhiteRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateIdsWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIdsWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIdsWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatFwInstance(self, request):
        """创建NAT防火墙实例（Region参数必填）

        :param request: Request instance for CreateNatFwInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatFwInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatFwInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatFwInstanceWithDomain(self, request):
        """创建防火墙实例和接入域名（Region参数必填）

        :param request: Request instance for CreateNatFwInstanceWithDomain.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceWithDomainRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateNatFwInstanceWithDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatFwInstanceWithDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatFwInstanceWithDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupRules(self, request):
        """创建企业安全组规则

        :param request: Request instance for CreateSecurityGroupRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcFwGroup(self, request):
        """创建VPC间防火墙(防火墙组)

        :param request: Request instance for CreateVpcFwGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateVpcFwGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateVpcFwGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcFwGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcFwGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAcRule(self, request):
        """删除规则

        :param request: Request instance for DeleteAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressTemplate(self, request):
        """删除地址模板规则

        :param request: Request instance for DeleteAddressTemplate.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteAddressTemplateRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllAccessControlRule(self, request):
        """全部删除规则

        :param request: Request instance for DeleteAllAccessControlRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteAllAccessControlRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteAllAccessControlRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllAccessControlRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllAccessControlRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBlockIgnoreRuleList(self, request):
        """批量删除入侵防御封禁列表、放通列表规则

        :param request: Request instance for DeleteBlockIgnoreRuleList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteBlockIgnoreRuleListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteBlockIgnoreRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlockIgnoreRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBlockIgnoreRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBlockIgnoreRuleNew(self, request):
        """批量删除入侵防御封禁列表、放通列表规则（新）

        :param request: Request instance for DeleteBlockIgnoreRuleNew.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteBlockIgnoreRuleNewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteBlockIgnoreRuleNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlockIgnoreRuleNew", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBlockIgnoreRuleNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIdsWhiteRule(self, request):
        """历史方案，业务已迁移，接口不再适用

        删除入侵防御规则白名单接口

        :param request: Request instance for DeleteIdsWhiteRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteIdsWhiteRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteIdsWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIdsWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIdsWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatFwInstance(self, request):
        """销毁防火墙实例

        :param request: Request instance for DeleteNatFwInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteNatFwInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteNatFwInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatFwInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatFwInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRemoteAccessDomain(self, request):
        """删除远程运维域名

        :param request: Request instance for DeleteRemoteAccessDomain.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteRemoteAccessDomainRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteRemoteAccessDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRemoteAccessDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRemoteAccessDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceGroup(self, request):
        """DeleteResourceGroup-资产中心资产组删除

        :param request: Request instance for DeleteResourceGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteResourceGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroupRule(self, request):
        """删除规则

        :param request: Request instance for DeleteSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcFwGroup(self, request):
        """删除防火墙(组)，或者删除其中实例

        :param request: Request instance for DeleteVpcFwGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteVpcFwGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteVpcFwGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcFwGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcFwGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAcLists(self, request):
        """访问控制列表

        :param request: Request instance for DescribeAcLists.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAcListsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAcListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAcLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAcListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAclRule(self, request):
        """查询互联网边界访问控制列表

        :param request: Request instance for DescribeAclRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAclRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressTemplateList(self, request):
        """查询地址模板列表

        :param request: Request instance for DescribeAddressTemplateList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAddressTemplateListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAddressTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSync(self, request):
        """资产同步状态查询

        :param request: Request instance for DescribeAssetSync.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAssetSyncRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAssetSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSync", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssociatedInstanceList(self, request):
        """获取安全组关联实例列表

        :param request: Request instance for DescribeAssociatedInstanceList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAssociatedInstanceListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAssociatedInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssociatedInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssociatedInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockByIpTimesList(self, request):
        """DescribeBlockByIpTimesList 告警中心阻断IP折线图

        :param request: Request instance for DescribeBlockByIpTimesList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockByIpTimesListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockByIpTimesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockByIpTimesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockByIpTimesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockIgnoreList(self, request):
        """查询入侵防御放通封禁列表

        :param request: Request instance for DescribeBlockIgnoreList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockIgnoreListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockStaticList(self, request):
        """DescribeBlockStaticList 告警中心柱形图

        :param request: Request instance for DescribeBlockStaticList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockStaticListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeBlockStaticListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockStaticList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockStaticListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfwEips(self, request):
        """查询防火墙弹性公网IP

        :param request: Request instance for DescribeCfwEips.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeCfwEipsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeCfwEipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfwEips", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfwEipsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfwInsStatus(self, request):
        """cfw实例运行状态查询

        :param request: Request instance for DescribeCfwInsStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeCfwInsStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeCfwInsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfwInsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfwInsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefenseSwitch(self, request):
        """获取入侵防御按钮列表

        :param request: Request instance for DescribeDefenseSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeDefenseSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeDefenseSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefenseSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefenseSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnterpriseSGRuleProgress(self, request):
        """查询新版安全组下发进度

        :param request: Request instance for DescribeEnterpriseSGRuleProgress.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSGRuleProgressRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSGRuleProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnterpriseSGRuleProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnterpriseSGRuleProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnterpriseSecurityGroupRule(self, request):
        """查询新企业安全组规则

        :param request: Request instance for DescribeEnterpriseSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnterpriseSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnterpriseSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnterpriseSecurityGroupRuleList(self, request):
        """查询新企业安全组规则  从node接口迁移   原接口DescribeSecurityGroupNewList

        :param request: Request instance for DescribeEnterpriseSecurityGroupRuleList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSecurityGroupRuleListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeEnterpriseSecurityGroupRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnterpriseSecurityGroupRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnterpriseSecurityGroupRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFwEdgeIps(self, request):
        """串行防火墙IP开关列表

        :param request: Request instance for DescribeFwEdgeIps.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeFwEdgeIpsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeFwEdgeIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFwEdgeIps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFwEdgeIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFwGroupInstanceInfo(self, request):
        """获取租户所有VPC防火墙(组)及VPC防火墙实例卡片信息

        :param request: Request instance for DescribeFwGroupInstanceInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeFwGroupInstanceInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeFwGroupInstanceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFwGroupInstanceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFwGroupInstanceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFwSyncStatus(self, request):
        """获取防火墙同步状态，一般在执行同步操作后查询

        :param request: Request instance for DescribeFwSyncStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeFwSyncStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeFwSyncStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFwSyncStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFwSyncStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGuideScanInfo(self, request):
        """DescribeGuideScanInfo新手引导扫描接口信息

        :param request: Request instance for DescribeGuideScanInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeGuideScanInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeGuideScanInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGuideScanInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGuideScanInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPStatusList(self, request):
        """IP防护状态查询

        :param request: Request instance for DescribeIPStatusList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeIPStatusListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeIPStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStatusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStatusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdsWhiteRule(self, request):
        """历史方案，业务已迁移，接口不再适用

        查询入侵防御规则白名单接口

        :param request: Request instance for DescribeIdsWhiteRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeIdsWhiteRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeIdsWhiteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdsWhiteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdsWhiteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogs(self, request):
        """日志审计日志查询

        :param request: Request instance for DescribeLogs.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeLogsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatAcRule(self, request):
        """查询NAT访问控制列表

        :param request: Request instance for DescribeNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwDnatRule(self, request):
        """查询Nat防火墙Dnat规则

        :param request: Request instance for DescribeNatFwDnatRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwDnatRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwDnatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwDnatRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwDnatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInfoCount(self, request):
        """获取当前用户接入nat防火墙的所有子网数及natfw实例个数

        :param request: Request instance for DescribeNatFwInfoCount.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInfoCountRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInfoCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInfoCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInfoCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInstance(self, request):
        """DescribeNatFwInstance 获取租户所有NAT实例

        :param request: Request instance for DescribeNatFwInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInstanceWithRegion(self, request):
        """GetNatFwInstanceWithRegion 获取租户新增运维的NAT实例，带上地域

        :param request: Request instance for DescribeNatFwInstanceWithRegion.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceWithRegionRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstanceWithRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInstanceWithRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInstanceWithRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwInstancesInfo(self, request):
        """GetNatInstance 获取租户所有NAT实例及实例卡片信息

        :param request: Request instance for DescribeNatFwInstancesInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstancesInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwInstancesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwInstancesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwInstancesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatFwVpcDnsLst(self, request):
        """展示当前natfw 实例对应的vpc dns开关

        :param request: Request instance for DescribeNatFwVpcDnsLst.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwVpcDnsLstRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatFwVpcDnsLstResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatFwVpcDnsLst", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatFwVpcDnsLstResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceGroup(self, request):
        """DescribeResourceGroup资产中心资产树信息

        :param request: Request instance for DescribeResourceGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceGroupNew(self, request):
        """资产中心资产组数数据信息查询

        :param request: Request instance for DescribeResourceGroupNew.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupNewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceGroupNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceGroupNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleOverview(self, request):
        """查询规则列表概况

        :param request: Request instance for DescribeRuleOverview.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeRuleOverviewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeRuleOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupList(self, request):
        """查询安全组规则列表

        :param request: Request instance for DescribeSecurityGroupList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSecurityGroupListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSecurityGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSourceAsset(self, request):
        """DescribeSourceAsset-查询全部资产信息

        :param request: Request instance for DescribeSourceAsset.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSourceAssetRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSourceAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSourceAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSwitchLists(self, request):
        """防火墙开关列表，已废弃，请使用DescribeFwEdgeIps

        :param request: Request instance for DescribeSwitchLists.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSwitchLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSwitchListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTLogInfo(self, request):
        """DescribeTLogInfo告警中心概况查询

        :param request: Request instance for DescribeTLogInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTLogInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTLogInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTLogIpList(self, request):
        """DescribeTLogIpList告警中心IP柱形图

        :param request: Request instance for DescribeTLogIpList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogIpListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogIpListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTLogIpList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTLogIpListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableStatus(self, request):
        """查询规则表状态

        :param request: Request instance for DescribeTableStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTableStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTableStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnHandleEventTabList(self, request):
        """DescribeUnHandleEventTabList 告警中心伪攻击链事件未处置接口

        :param request: Request instance for DescribeUnHandleEventTabList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeUnHandleEventTabListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeUnHandleEventTabListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnHandleEventTabList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnHandleEventTabListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcAcRule(self, request):
        """查询内网间访问控制列表

        :param request: Request instance for DescribeVpcAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcFwGroupSwitch(self, request):
        """VPC防火墙(组)开关列表

        :param request: Request instance for DescribeVpcFwGroupSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcFwGroupSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcFwGroupSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcFwGroupSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcFwGroupSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExpandCfwVertical(self, request):
        """防火墙垂直扩容

        :param request: Request instance for ExpandCfwVertical.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ExpandCfwVerticalRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ExpandCfwVerticalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExpandCfwVertical", params, headers=headers)
            response = json.loads(body)
            model = models.ExpandCfwVerticalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAcRule(self, request):
        """修改规则

        :param request: Request instance for ModifyAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAclRule(self, request):
        """修改互联网边界访问控制规则

        :param request: Request instance for ModifyAclRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAclRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressTemplate(self, request):
        """修改地址模板

        :param request: Request instance for ModifyAddressTemplate.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAddressTemplateRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllPublicIPSwitchStatus(self, request):
        """互联网边界防火墙一键开关

        :param request: Request instance for ModifyAllPublicIPSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllPublicIPSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllPublicIPSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllPublicIPSwitchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllPublicIPSwitchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllRuleStatus(self, request):
        """启用停用全部规则

        :param request: Request instance for ModifyAllRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetScan(self, request):
        """资产扫描

        :param request: Request instance for ModifyAssetScan.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAssetScanRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAssetScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetScan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssetSync(self, request):
        """资产同步

        :param request: Request instance for ModifyAssetSync.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAssetSyncRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAssetSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetSync", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssetSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockIgnoreList(self, request):
        """支持对封禁列表、放通列表如下操作：
        批量增加封禁IP、放通IP/域名
        批量删除封禁IP、放通IP/域名
        批量修改封禁IP、放通IP/域名生效事件

        :param request: Request instance for ModifyBlockIgnoreList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockIgnoreRule(self, request):
        """编辑单条入侵防御封禁列表、放通列表规则

        :param request: Request instance for ModifyBlockIgnoreRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockIgnoreRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockIgnoreRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockIgnoreRuleNew(self, request):
        """编辑单条入侵防御封禁列表、放通列表规则（新）

        :param request: Request instance for ModifyBlockIgnoreRuleNew.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreRuleNewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreRuleNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockIgnoreRuleNew", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockIgnoreRuleNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockTop(self, request):
        """ModifyBlockTop取消置顶接口

        :param request: Request instance for ModifyBlockTop.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockTopRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockTop", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEWRuleStatus(self, request):
        """启用停用VPC间规则或Nat边界规则
        VPC间规则需指定EdgeId。Nat边界规则需指定地域Region与Direction。

        :param request: Request instance for ModifyEWRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyEWRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyEWRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEWRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEWRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEdgeIpSwitch(self, request):
        """修改边界防火墙开关(旁路、串行)

        :param request: Request instance for ModifyEdgeIpSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyEdgeIpSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyEdgeIpSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEdgeIpSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEdgeIpSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnterpriseSecurityDispatchStatus(self, request):
        """修改企业安全组下发状态

        :param request: Request instance for ModifyEnterpriseSecurityDispatchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityDispatchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityDispatchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnterpriseSecurityDispatchStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnterpriseSecurityDispatchStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnterpriseSecurityGroupRule(self, request):
        """编辑新企业安全组规则

        :param request: Request instance for ModifyEnterpriseSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyEnterpriseSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnterpriseSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnterpriseSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFwGroupSwitch(self, request):
        """修改防火墙(组)开关(支持单点模式、多点模式、全互通模式)

        :param request: Request instance for ModifyFwGroupSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyFwGroupSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyFwGroupSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFwGroupSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFwGroupSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatAcRule(self, request):
        """修改NAT访问控制规则

        :param request: Request instance for ModifyNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatFwReSelect(self, request):
        """防火墙实例重新选择vpc或nat

        :param request: Request instance for ModifyNatFwReSelect.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwReSelectRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwReSelectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatFwReSelect", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatFwReSelectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatFwSwitch(self, request):
        """修改NAT防火墙开关

        :param request: Request instance for ModifyNatFwSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatFwSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatFwSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatFwVpcDnsSwitch(self, request):
        """nat 防火墙VPC DNS 开关切换

        :param request: Request instance for ModifyNatFwVpcDnsSwitch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwVpcDnsSwitchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatFwVpcDnsSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatFwVpcDnsSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatFwVpcDnsSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatInstance(self, request):
        """编辑NAT防火墙

        :param request: Request instance for ModifyNatInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatSequenceRules(self, request):
        """NAT防火墙规则快速排序

        :param request: Request instance for ModifyNatSequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyNatSequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyNatSequenceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatSequenceRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatSequenceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceGroup(self, request):
        """ModifyResourceGroup-资产中心资产组信息修改

        :param request: Request instance for ModifyResourceGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyResourceGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRunSyncAsset(self, request):
        """同步资产-互联网&VPC（新）

        :param request: Request instance for ModifyRunSyncAsset.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyRunSyncAssetRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyRunSyncAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRunSyncAsset", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRunSyncAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupItemRuleStatus(self, request):
        """启用停用单条企业安全组规则

        :param request: Request instance for ModifySecurityGroupItemRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupItemRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupItemRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupItemRuleStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupItemRuleStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupRule(self, request):
        """编辑单条安全组规则

        :param request: Request instance for ModifySecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupSequenceRules(self, request):
        """企业安全组规则快速排序

        :param request: Request instance for ModifySecurityGroupSequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupSequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupSequenceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupSequenceRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupSequenceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySequenceAclRules(self, request):
        """互联网边界规则快速排序

        :param request: Request instance for ModifySequenceAclRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceAclRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceAclRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySequenceAclRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySequenceAclRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySequenceRules(self, request):
        """修改规则执行顺序

        :param request: Request instance for ModifySequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySequenceRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySequenceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStorageSetting(self, request):
        """日志存储设置，可以修改存储时间和清空日志

        :param request: Request instance for ModifyStorageSetting.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyStorageSettingRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyStorageSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStorageSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStorageSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableStatus(self, request):
        """修改规则表状态

        :param request: Request instance for ModifyTableStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyTableStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyTableStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcAcRule(self, request):
        """修改内网间访问控制规则

        :param request: Request instance for ModifyVpcAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyVpcAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyVpcAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcFwGroup(self, request):
        """编辑VPC间防火墙(防火墙组)

        :param request: Request instance for ModifyVpcFwGroup.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyVpcFwGroupRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyVpcFwGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcFwGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcFwGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcFwSequenceRules(self, request):
        """vpc间规则快速排序

        :param request: Request instance for ModifyVpcFwSequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyVpcFwSequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyVpcFwSequenceRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcFwSequenceRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcFwSequenceRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveAcRule(self, request):
        """删除互联网边界规则

        :param request: Request instance for RemoveAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveAclRule(self, request):
        """删除互联网边界访问控制规则

        :param request: Request instance for RemoveAclRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveAclRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveEnterpriseSecurityGroupRule(self, request):
        """删除新企业安全组规则

        :param request: Request instance for RemoveEnterpriseSecurityGroupRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveEnterpriseSecurityGroupRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveEnterpriseSecurityGroupRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveEnterpriseSecurityGroupRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveEnterpriseSecurityGroupRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveNatAcRule(self, request):
        """删除NAT访问控制规则

        :param request: Request instance for RemoveNatAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveNatAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveNatAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveNatAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveNatAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveVpcAcRule(self, request):
        """删除VPC间规则

        :param request: Request instance for RemoveVpcAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RemoveVpcAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RemoveVpcAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveVpcAcRule", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveVpcAcRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNatFwDnatRule(self, request):
        """配置防火墙Dnat规则

        :param request: Request instance for SetNatFwDnatRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.SetNatFwDnatRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SetNatFwDnatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNatFwDnatRule", params, headers=headers)
            response = json.loads(body)
            model = models.SetNatFwDnatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNatFwEip(self, request):
        """设置防火墙实例弹性公网ip，目前仅支持新增模式的防火墙实例

        :param request: Request instance for SetNatFwEip.
        :type request: :class:`tencentcloud.cfw.v20190904.models.SetNatFwEipRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SetNatFwEipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNatFwEip", params, headers=headers)
            response = json.loads(body)
            model = models.SetNatFwEipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSecurityGroupRuleDispatch(self, request):
        """中止安全组规则下发

        :param request: Request instance for StopSecurityGroupRuleDispatch.
        :type request: :class:`tencentcloud.cfw.v20190904.models.StopSecurityGroupRuleDispatchRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.StopSecurityGroupRuleDispatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSecurityGroupRuleDispatch", params, headers=headers)
            response = json.loads(body)
            model = models.StopSecurityGroupRuleDispatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncFwOperate(self, request):
        """同步防火墙操作，包括同步防火墙路由（若vpc，专线网关等增加了Cidr，需要手动同步一下路由使之在防火墙上生效）等。

        :param request: Request instance for SyncFwOperate.
        :type request: :class:`tencentcloud.cfw.v20190904.models.SyncFwOperateRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.SyncFwOperateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncFwOperate", params, headers=headers)
            response = json.loads(body)
            model = models.SyncFwOperateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))