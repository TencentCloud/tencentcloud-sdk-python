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
from tencentcloud.ses.v20201002 import models


class SesClient(AbstractClient):
    _apiVersion = '2020-10-02'
    _endpoint = 'ses.tencentcloudapi.com'
    _service = 'ses'


    def BatchSendEmail(self, request):
        """您可以通过此API批量发送TEXT或者HTML邮件，适用于营销类、通知类邮件。默认仅支持使用模板发送邮件，如需发送自定义内容，请单独联系商务开通此功能。批量发送之前，需先创建收件人列表，和收件人地址，并通过收件人列表id来进行发送。批量发送任务支持定时发送和周期重复发送，定时发送需传TimedParam，周期重复发送需传CycleParam

        :param request: Request instance for BatchSendEmail.
        :type request: :class:`tencentcloud.ses.v20201002.models.BatchSendEmailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.BatchSendEmailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchSendEmail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchSendEmailResponse()
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


    def CreateEmailAddress(self, request):
        """在验证了发信域名之后，您需要一个发信地址来发送邮件。例如发信域名是mail.qcloud.com，那么发信地址可以为 service@mail.qcloud.com。如果您想要收件人在收件箱列表中显示您的别名，例如"腾讯云邮件通知"。那么发信地址为： 别名 空格 尖括号 邮箱地址。请注意中间需要有空格

        :param request: Request instance for CreateEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEmailAddressResponse()
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


    def CreateEmailIdentity(self, request):
        """在使用身份发送电子邮件之前，您需要有一个电子邮件域名，该域名可以是您的网站或者移动应用的域名。您首先必须进行验证，证明自己是该域名的所有者，并且授权给腾讯云SES发送许可，才可以从该域名发送电子邮件。

        :param request: Request instance for CreateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEmailIdentityResponse()
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


    def CreateEmailTemplate(self, request):
        """创建模板，该模板可以是TXT或者HTML，请注意如果HTML不要包含外部文件的CSS。模板中的变量使用 {{变量名}} 表示。
        注意：模版需要审核通过才可以使用。

        :param request: Request instance for CreateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEmailTemplateResponse()
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


    def CreateReceiver(self, request):
        """创建收件人列表，收件人列表是发送批量邮件的目标邮件地址列表。创建列表后，需要上传收件人邮箱地址。之后创建发送任务，关联列表，便可以实现批量发送邮件的功能

        :param request: Request instance for CreateReceiver.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReceiver", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReceiverResponse()
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


    def CreateReceiverDetail(self, request):
        """在创建完收件人列表后，向这个收件人列表中批量增加收件人邮箱地址，一次最大支持10W，异步完成处理。收件人列表只可以上传一次，不可追加上传。数据量比较大的时候，上传可能需要一点时间，可以通过查询收件人列表了解上传状态和上传数量

        :param request: Request instance for CreateReceiverDetail.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReceiverDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReceiverDetailResponse()
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


    def DeleteBlackList(self, request):
        """邮箱被拉黑之后，用户如果确认收件邮箱有效或者已经处于激活状态，可以从腾讯云地址库中删除该黑名单之后继续投递。

        :param request: Request instance for DeleteBlackList.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBlackList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBlackListResponse()
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


    def DeleteEmailAddress(self, request):
        """删除发信人地址

        :param request: Request instance for DeleteEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEmailAddressResponse()
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


    def DeleteEmailIdentity(self, request):
        """删除发信域名，删除后，将不可再使用该域名进行发信

        :param request: Request instance for DeleteEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEmailIdentityResponse()
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


    def DeleteEmailTemplate(self, request):
        """删除发信模板

        :param request: Request instance for DeleteEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEmailTemplateResponse()
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


    def GetEmailIdentity(self, request):
        """获取某个发信域名的配置详情

        :param request: Request instance for GetEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetEmailIdentityResponse()
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


    def GetEmailTemplate(self, request):
        """根据模板ID获取模板详情

        :param request: Request instance for GetEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetEmailTemplateResponse()
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


    def GetSendEmailStatus(self, request):
        """获取邮件发送状态。仅支持查询30天之内的数据

        :param request: Request instance for GetSendEmailStatus.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetSendEmailStatusRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetSendEmailStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSendEmailStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSendEmailStatusResponse()
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


    def GetStatisticsReport(self, request):
        """获取近期发送的统计情况，包含发送量、送达率、打开率、退信率等一系列数据。

        :param request: Request instance for GetStatisticsReport.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetStatisticsReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetStatisticsReportResponse()
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


    def ListBlackEmailAddress(self, request):
        """腾讯云发送的邮件一旦被收件方判断为硬退(Hard Bounce)，腾讯云会拉黑该地址，并不允许所有用户向该地址发送邮件。成为邮箱黑名单。如果业务方确认是误判，可以从黑名单中删除。

        :param request: Request instance for ListBlackEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListBlackEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListBlackEmailAddressResponse()
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


    def ListEmailAddress(self, request):
        """获取发信地址列表

        :param request: Request instance for ListEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEmailAddressResponse()
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


    def ListEmailIdentities(self, request):
        """获取当前发信域名列表，包含已验证通过与未验证的域名

        :param request: Request instance for ListEmailIdentities.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEmailIdentities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEmailIdentitiesResponse()
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


    def ListEmailTemplates(self, request):
        """获取当前邮件模板列表

        :param request: Request instance for ListEmailTemplates.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEmailTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEmailTemplatesResponse()
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


    def ListReceivers(self, request):
        """根据条件查询收件人列表，支持分页，模糊查询，状态查询

        :param request: Request instance for ListReceivers.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListReceiversRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListReceiversResponse()
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


    def ListSendTasks(self, request):
        """分页查询批量发送邮件任务，包含即时发送任务，定时发送任务，周期重复发送任务，查询发送情况，包括请求数量，已发数量，缓存数量，任务状态等信息

        :param request: Request instance for ListSendTasks.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListSendTasksRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListSendTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSendTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSendTasksResponse()
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


    def SendEmail(self, request):
        """您可以通过此API发送TEXT或者HTML邮件，适用于触发类邮件（验证码、交易类）。默认仅支持使用模板发送邮件，如需发送自定义内容，请单独联系商务开通此功能。

        :param request: Request instance for SendEmail.
        :type request: :class:`tencentcloud.ses.v20201002.models.SendEmailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.SendEmailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendEmail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendEmailResponse()
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


    def UpdateEmailIdentity(self, request):
        """您已经成功配置好了您的DNS，接下来请求腾讯云验证您的DNS配置是否正确

        :param request: Request instance for UpdateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEmailIdentityResponse()
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


    def UpdateEmailTemplate(self, request):
        """更新邮件模板，更新后需再次审核

        :param request: Request instance for UpdateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEmailTemplateResponse()
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