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


    def AddAcRule(self, request):
        """添加互联网边界规则

        :param request: Request instance for AddAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.AddAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.AddAcRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAcRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddAcRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.AddEnterpriseSecurityGroupRulesResponse()
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


    def CreateAcRules(self, request):
        """创建规则

        :param request: Request instance for CreateAcRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAcRulesResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateChooseVpcsResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateDatabaseWhiteListRulesResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateNatFwInstanceResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateNatFwInstanceWithDomainResponse()
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


    def CreateSecurityGroupApiRules(self, request):
        """创建安全组API规则

        :param request: Request instance for CreateSecurityGroupApiRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupApiRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupApiRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupApiRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupApiRulesResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupRulesResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteAcRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteAllAccessControlRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteNatFwInstanceResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteResourceGroupResponse()
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
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupRuleResponse()
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


    def DeleteVpcInstance(self, request):
        """删除防火墙实例

        :param request: Request instance for DeleteVpcInstance.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteVpcInstanceRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteVpcInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcInstanceResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeAcListsResponse()
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


    def DescribeAddrTemplateList(self, request):
        """获取地址模板列表

        :param request: Request instance for DescribeAddrTemplateList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAddrTemplateListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAddrTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddrTemplateList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddrTemplateListResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeAssociatedInstanceListResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeBlockByIpTimesListResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeBlockStaticListResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeCfwEipsResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeEnterpriseSecurityGroupRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeGuideScanInfoResponse()
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


    def DescribeIPStatusList(self, request):
        """ip防护状态查询

        :param request: Request instance for DescribeIPStatusList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeIPStatusListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeIPStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStatusList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIPStatusListResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeNatFwInfoCountResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeNatFwInstanceResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeNatFwInstanceWithRegionResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeNatFwInstancesInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeNatFwVpcDnsLstResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeResourceGroupResponse()
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


    def DescribeResourceGroupNew(self, request):
        """DescribeResourceGroupNew资产中心资产树信息

        :param request: Request instance for DescribeResourceGroupNew.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupNewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeResourceGroupNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceGroupNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceGroupNewResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeRuleOverviewResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupListResponse()
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


    def DescribeSourceAsset(self, request):
        """DescribeSourceAsset-查询资产组全部资产信息

        :param request: Request instance for DescribeSourceAsset.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSourceAssetRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSourceAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSourceAsset", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSourceAssetResponse()
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


    def DescribeSwitchLists(self, request):
        """防火墙开关列表

        :param request: Request instance for DescribeSwitchLists.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSwitchLists", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSwitchListsResponse()
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


    def DescribeSyncAssetStatus(self, request):
        """同步资产状态查询-互联网&VPC

        :param request: Request instance for DescribeSyncAssetStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSyncAssetStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSyncAssetStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSyncAssetStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSyncAssetStatusResponse()
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


    def DescribeTLogInfo(self, request):
        """DescribeTLogInfo告警中心概况

        :param request: Request instance for DescribeTLogInfo.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogInfoRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTLogInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTLogInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTLogInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeTLogIpListResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeTableStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeUnHandleEventTabListResponse()
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


    def DescribeVpcRuleOverview(self, request):
        """vpc规则列表概况

        :param request: Request instance for DescribeVpcRuleOverview.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcRuleOverviewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcRuleOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcRuleOverview", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcRuleOverviewResponse()
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
            if "Error" not in response["Response"]:
                model = models.ExpandCfwVerticalResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAcRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAllPublicIPSwitchStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAllRuleStatusResponse()
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


    def ModifyAllSwitchStatus(self, request):
        """一键开启和关闭

        :param request: Request instance for ModifyAllSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllSwitchStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAllSwitchStatusResponse()
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


    def ModifyAllVPCSwitchStatus(self, request):
        """VPC防火墙一键开关

        :param request: Request instance for ModifyAllVPCSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllVPCSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllVPCSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllVPCSwitchStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAllVPCSwitchStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyAssetScanResponse()
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


    def ModifyBlockIgnoreList(self, request):
        """支持对拦截列表、忽略列表如下操作：
        批量增加拦截IP、忽略IP/域名
        批量删除拦截IP、忽略IP/域名
        批量修改拦截IP、忽略IP/域名生效事件

        :param request: Request instance for ModifyBlockIgnoreList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyBlockIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockIgnoreList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBlockIgnoreListResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyBlockTopResponse()
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


    def ModifyItemSwitchStatus(self, request):
        """修改单个防火墙开关

        :param request: Request instance for ModifyItemSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyItemSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyItemSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyItemSwitchStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyItemSwitchStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyNatFwReSelectResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyNatFwSwitchResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyNatFwVpcDnsSwitchResponse()
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


    def ModifyPublicIPSwitchStatus(self, request):
        """单个修改互联网边界防火墙开关

        :param request: Request instance for ModifyPublicIPSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyPublicIPSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyPublicIPSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublicIPSwitchStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPublicIPSwitchStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyResourceGroupResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyRunSyncAssetResponse()
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


    def ModifySecurityGroupAllRuleStatus(self, request):
        """启用停用全部规则

        :param request: Request instance for ModifySecurityGroupAllRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupAllRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupAllRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupAllRuleStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupAllRuleStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupItemRuleStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupSequenceRulesResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifySequenceRulesResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyTableStatusResponse()
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
            if "Error" not in response["Response"]:
                model = models.RemoveAcRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.RemoveEnterpriseSecurityGroupRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.SetNatFwDnatRuleResponse()
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
            if "Error" not in response["Response"]:
                model = models.SetNatFwEipResponse()
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
            if "Error" not in response["Response"]:
                model = models.StopSecurityGroupRuleDispatchResponse()
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