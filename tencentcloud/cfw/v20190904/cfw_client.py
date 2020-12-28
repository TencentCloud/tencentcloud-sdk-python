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
from tencentcloud.cfw.v20190904 import models


class CfwClient(AbstractClient):
    _apiVersion = '2019-09-04'
    _endpoint = 'cfw.tencentcloudapi.com'
    _service = 'cfw'


    def CreateAcRules(self, request):
        """创建规则

        :param request: Request instance for CreateAcRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateAcRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAcRules", params)
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


    def CreateSecurityGroupApiRules(self, request):
        """创建安全组API规则

        :param request: Request instance for CreateSecurityGroupApiRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupApiRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.CreateSecurityGroupApiRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroupApiRules", params)
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


    def DeleteAcRule(self, request):
        """删除规则

        :param request: Request instance for DeleteAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteAcRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAcRule", params)
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
            body = self.call("DeleteAllAccessControlRule", params)
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


    def DeleteSecurityGroupAllRule(self, request):
        """删除全部规则

        :param request: Request instance for DeleteSecurityGroupAllRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DeleteSecurityGroupAllRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DeleteSecurityGroupAllRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityGroupAllRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupAllRuleResponse()
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
            body = self.call("DeleteSecurityGroupRule", params)
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


    def DescribeAcLists(self, request):
        """访问控制列表

        :param request: Request instance for DescribeAcLists.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAcListsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAcListsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAcLists", params)
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


    def DescribeAssociatedInstanceList(self, request):
        """获取安全组关联实例列表

        :param request: Request instance for DescribeAssociatedInstanceList.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeAssociatedInstanceListRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeAssociatedInstanceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssociatedInstanceList", params)
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


    def DescribeNatRuleOverview(self, request):
        """nat规则列表概况

        :param request: Request instance for DescribeNatRuleOverview.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeNatRuleOverviewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeNatRuleOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatRuleOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatRuleOverviewResponse()
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
            body = self.call("DescribeRuleOverview", params)
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
            body = self.call("DescribeSecurityGroupList", params)
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


    def DescribeSwitchLists(self, request):
        """防火墙开关列表

        :param request: Request instance for DescribeSwitchLists.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeSwitchListsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSwitchLists", params)
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
            body = self.call("DescribeSyncAssetStatus", params)
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


    def DescribeTableStatus(self, request):
        """查询规则表状态

        :param request: Request instance for DescribeTableStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeTableStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeTableStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableStatus", params)
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


    def DescribeVpcRuleOverview(self, request):
        """vpc规则列表概况

        :param request: Request instance for DescribeVpcRuleOverview.
        :type request: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcRuleOverviewRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.DescribeVpcRuleOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcRuleOverview", params)
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


    def ModifyAcRule(self, request):
        """修改规则

        :param request: Request instance for ModifyAcRule.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAcRuleRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAcRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAcRule", params)
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


    def ModifyAllRuleStatus(self, request):
        """启用停用全部规则

        :param request: Request instance for ModifyAllRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyAllRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyAllRuleStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAllRuleStatus", params)
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
            body = self.call("ModifyAllSwitchStatus", params)
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


    def ModifyItemSwitchStatus(self, request):
        """修改单个防火墙开关

        :param request: Request instance for ModifyItemSwitchStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifyItemSwitchStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifyItemSwitchStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyItemSwitchStatus", params)
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


    def ModifySecurityGroupAllRuleStatus(self, request):
        """启用停用全部规则

        :param request: Request instance for ModifySecurityGroupAllRuleStatus.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupAllRuleStatusRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySecurityGroupAllRuleStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityGroupAllRuleStatus", params)
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


    def ModifySequenceRules(self, request):
        """修改规则执行顺序

        :param request: Request instance for ModifySequenceRules.
        :type request: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceRulesRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.ModifySequenceRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySequenceRules", params)
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
            body = self.call("ModifyTableStatus", params)
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


    def RunSyncAsset(self, request):
        """同步资产-互联网&VPC

        :param request: Request instance for RunSyncAsset.
        :type request: :class:`tencentcloud.cfw.v20190904.models.RunSyncAssetRequest`
        :rtype: :class:`tencentcloud.cfw.v20190904.models.RunSyncAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunSyncAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunSyncAssetResponse()
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