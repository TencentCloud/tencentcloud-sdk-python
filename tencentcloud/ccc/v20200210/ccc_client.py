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
from tencentcloud.ccc.v20200210 import models


class CccClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'ccc.tencentcloudapi.com'
    _service = 'ccc'


    def CreateSDKLoginToken(self, request):
        """创建 SDK 登录 Token。

        :param request: Request instance for CreateSDKLoginToken.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSDKLoginToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSDKLoginTokenResponse()
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


    def CreateStaff(self, request):
        """创建客服账号。

        :param request: Request instance for CreateStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateStaffResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStaff", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStaffResponse()
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


    def DescribeChatMessages(self, request):
        """包括具体聊天内容

        :param request: Request instance for DescribeChatMessages.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeChatMessagesRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeChatMessagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeChatMessages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeChatMessagesResponse()
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


    def DescribeIMCdrs(self, request):
        """包括全媒体和文本两种类型

        :param request: Request instance for DescribeIMCdrs.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIMCdrs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIMCdrsResponse()
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


    def DescribePSTNActiveSessionList(self, request):
        """获取 PSTN 活动会话列表。

        :param request: Request instance for DescribePSTNActiveSessionList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePSTNActiveSessionList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePSTNActiveSessionListResponse()
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


    def DescribeSeatUserList(self, request):
        """获取坐席用户列表（废弃）

        :param request: Request instance for DescribeSeatUserList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeSeatUserListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeSeatUserListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSeatUserList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSeatUserListResponse()
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


    def DescribeSkillGroupInfoList(self, request):
        """获取技能组信息列表

        :param request: Request instance for DescribeSkillGroupInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSkillGroupInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSkillGroupInfoListResponse()
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


    def DescribeStaffInfoList(self, request):
        """获取坐席信息列表

        :param request: Request instance for DescribeStaffInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStaffInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStaffInfoListResponse()
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


    def DescribeTelCallInfo(self, request):
        """按实例获取电话消耗统计

        :param request: Request instance for DescribeTelCallInfo.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTelCallInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTelCallInfoResponse()
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


    def DescribeTelCdr(self, request):
        """获取电话服务记录与录音

        :param request: Request instance for DescribeTelCdr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTelCdr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTelCdrResponse()
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


    def DescribeTelSession(self, request):
        """获取 PSTN 会话信息

        :param request: Request instance for DescribeTelSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTelSession", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTelSessionResponse()
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