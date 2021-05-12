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
from tencentcloud.ic.v20190307 import models


class IcClient(AbstractClient):
    _apiVersion = '2019-03-07'
    _endpoint = 'ic.tencentcloudapi.com'
    _service = 'ic'


    def DescribeApp(self, request):
        """根据应用id查询物联卡应用详情

        :param request: Request instance for DescribeApp.
        :type request: :class:`tencentcloud.ic.v20190307.models.DescribeAppRequest`
        :rtype: :class:`tencentcloud.ic.v20190307.models.DescribeAppResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAppResponse()
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


    def DescribeCard(self, request):
        """查询卡片详细信息

        :param request: Request instance for DescribeCard.
        :type request: :class:`tencentcloud.ic.v20190307.models.DescribeCardRequest`
        :rtype: :class:`tencentcloud.ic.v20190307.models.DescribeCardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCard", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCardResponse()
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


    def DescribeCards(self, request):
        """查询卡片列表信息

        :param request: Request instance for DescribeCards.
        :type request: :class:`tencentcloud.ic.v20190307.models.DescribeCardsRequest`
        :rtype: :class:`tencentcloud.ic.v20190307.models.DescribeCardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCardsResponse()
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


    def ModifyUserCardRemark(self, request):
        """编辑卡片备注

        :param request: Request instance for ModifyUserCardRemark.
        :type request: :class:`tencentcloud.ic.v20190307.models.ModifyUserCardRemarkRequest`
        :rtype: :class:`tencentcloud.ic.v20190307.models.ModifyUserCardRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUserCardRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUserCardRemarkResponse()
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


    def RenewCards(self, request):
        """批量为卡片续费，此接口建议调用至少间隔10s,如果出现返回deal lock failed相关的错误，请过10s再重试。
        续费的必要条件：
        1、单次续费的卡片不可以超过 100张。
        2、接口只支持在控制台购买的卡片进行续费
        3、销户和未激活的卡片不支持续费。
        4、每张物联网卡，续费总周期不能超过24个月

        :param request: Request instance for RenewCards.
        :type request: :class:`tencentcloud.ic.v20190307.models.RenewCardsRequest`
        :rtype: :class:`tencentcloud.ic.v20190307.models.RenewCardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewCards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewCardsResponse()
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


    def SendMultiSms(self, request):
        """群发短信

        :param request: Request instance for SendMultiSms.
        :type request: :class:`tencentcloud.ic.v20190307.models.SendMultiSmsRequest`
        :rtype: :class:`tencentcloud.ic.v20190307.models.SendMultiSmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendMultiSms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendMultiSmsResponse()
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


    def SendSms(self, request):
        """发送短信息接口

        :param request: Request instance for SendSms.
        :type request: :class:`tencentcloud.ic.v20190307.models.SendSmsRequest`
        :rtype: :class:`tencentcloud.ic.v20190307.models.SendSmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendSms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendSmsResponse()
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