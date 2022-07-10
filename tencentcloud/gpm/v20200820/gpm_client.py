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
from tencentcloud.gpm.v20200820 import models


class GpmClient(AbstractClient):
    _apiVersion = '2020-08-20'
    _endpoint = 'gpm.tencentcloudapi.com'
    _service = 'gpm'


    def CancelMatching(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        取消匹配。

        :param request: Request instance for CancelMatching.
        :type request: :class:`tencentcloud.gpm.v20200820.models.CancelMatchingRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.CancelMatchingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelMatching", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelMatchingResponse()
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


    def CreateMatch(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        创建匹配

        :param request: Request instance for CreateMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.CreateMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.CreateMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMatchResponse()
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


    def CreateRule(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        创建规则

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
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


    def DeleteMatch(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        删除匹配

        :param request: Request instance for DeleteMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DeleteMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DeleteMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMatchResponse()
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


    def DeleteRule(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        删除规则

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
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


    def DescribeData(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        统计数据

        :param request: Request instance for DescribeData.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeDataRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDataResponse()
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


    def DescribeMatch(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        查询匹配详情

        :param request: Request instance for DescribeMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMatchResponse()
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


    def DescribeMatchCodes(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        分页查询匹配Code

        :param request: Request instance for DescribeMatchCodes.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchCodesRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatchCodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMatchCodesResponse()
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


    def DescribeMatches(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        分页查询匹配列表

        :param request: Request instance for DescribeMatches.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchesRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatches", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMatchesResponse()
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


    def DescribeMatchingProgress(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        查询匹配进度。

        :param request: Request instance for DescribeMatchingProgress.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchingProgressRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchingProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatchingProgress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMatchingProgressResponse()
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


    def DescribeRule(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        查询规则详情

        :param request: Request instance for DescribeRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRuleResponse()
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


    def DescribeRules(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        分页查询规则集列表

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesResponse()
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


    def DescribeToken(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        查询匹配Token，Token用于push消息验证。

        :param request: Request instance for DescribeToken.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeTokenRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTokenResponse()
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


    def ModifyMatch(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        修改匹配

        :param request: Request instance for ModifyMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.ModifyMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ModifyMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMatchResponse()
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


    def ModifyRule(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        修改规则（描述、标签）

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRuleResponse()
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


    def ModifyToken(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        修改匹配Token。

        :param request: Request instance for ModifyToken.
        :type request: :class:`tencentcloud.gpm.v20200820.models.ModifyTokenRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ModifyTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTokenResponse()
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


    def StartMatching(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        支持传入一个玩家或多个玩家发起匹配，在同一个请求内的玩家将被分到同一个对局。

        :param request: Request instance for StartMatching.
        :type request: :class:`tencentcloud.gpm.v20200820.models.StartMatchingRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.StartMatchingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMatching", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMatchingResponse()
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


    def StartMatchingBackfill(self, request):
        """此接口无法使用，游戏玩家匹配GPM已于6.1正式下架，感谢您的支持

        通过调用StartMatchingBackfill，用户可以传入一个回填的匹配请求，GPM为回填请求搜索符合条件的ticket并形成一个新的match。

        :param request: Request instance for StartMatchingBackfill.
        :type request: :class:`tencentcloud.gpm.v20200820.models.StartMatchingBackfillRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.StartMatchingBackfillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMatchingBackfill", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMatchingBackfillResponse()
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