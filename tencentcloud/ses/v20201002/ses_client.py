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
        """您可以通过此API批量发送TEXT或者HTML邮件，适用于营销类、通知类邮件。默认仅支持使用模板发送邮件。批量发送之前，需先创建收件人列表，和收件人地址，并通过收件人列表id来进行发送。批量发送任务支持定时发送和周期重复发送，定时发送需传TimedParam，周期重复发送需传CycleParam

        :param request: Request instance for BatchSendEmail.
        :type request: :class:`tencentcloud.ses.v20201002.models.BatchSendEmailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.BatchSendEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchSendEmail", params, headers=headers)
            response = json.loads(body)
            model = models.BatchSendEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAddressUnsubscribeConfig(self, request):
        """创建地址级退订配置

        :param request: Request instance for CreateAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomBlacklist(self, request):
        """添加自定义黑名单

        :param request: Request instance for CreateCustomBlacklist.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateCustomBlacklistRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateCustomBlacklistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomBlacklist", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomBlacklistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmailAddress(self, request):
        """在验证了发信域名之后，您需要一个发信地址来发送邮件。例如发信域名是mail.qcloud.com，那么发信地址可以为 service@mail.qcloud.com。如果您想要收件人在收件箱列表中显示您的别名，例如"腾讯云邮件通知"。那么发信地址为： 别名 空格 尖括号 邮箱地址。请注意中间需要有空格

        :param request: Request instance for CreateEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmailIdentity(self, request):
        """在使用身份发送电子邮件之前，您需要有一个电子邮件域名，该域名可以是您的网站或者移动应用的域名。您首先必须进行验证，证明自己是该域名的所有者，并且授权给腾讯云SES发送许可，才可以从该域名发送电子邮件。

        :param request: Request instance for CreateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmailTemplate(self, request):
        """创建模板，该模板可以是TXT或者HTML，请注意如果HTML不要包含外部文件的CSS。模板中的变量使用 {{变量名}} 表示。
        注意：模板需要审核通过才可以使用。

        :param request: Request instance for CreateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReceiver(self, request):
        """创建收件人列表，收件人列表是发送批量邮件的目标邮件地址列表。创建列表后，需要上传收件人邮箱地址。之后创建发送任务，关联列表，便可以实现批量发送邮件的功能

        :param request: Request instance for CreateReceiver.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReceiverDetail(self, request):
        """在创建完收件人列表后，向这个收件人列表中批量增加收件人邮箱地址，一次最大支持2万，异步完成处理。数据量比较大的时候，上传可能需要一点时间，可以通过查询收件人列表了解上传状态和上传数量。本接口与接口CreateReceiverDetailWithData的功能特性基本一致，只是不支持上传发信时的模板参数。用户首先调用创建收件人列表接口-CreateReceiver后，然后调用本接口传入收件人地址，最后使用批量发送邮件接口-BatchSendEmail，即可完成批量发信。本接口也支持追加收件人地址，也不支持去重，需要用户自己保证收件人地址不重复。本接口一次请求的收件人地址数量限制为2W条，但收件人列表中收件人地址的总量不能超过一定的数量，目前是限制5万条。

        :param request: Request instance for CreateReceiverDetail.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReceiverDetail", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReceiverDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReceiverDetailWithData(self, request):
        """添加收件人地址附带模板参数，使用本接口在添加收件人地址的同时传入模板参数，使每一个收件人地址在发信的时候使用的模板变量取值不同。用户首先调用创建收件人列表接口-CreateReceiver后，然后调用本接口传入收件人地址和发信时的模板参数，最后使用批量发送邮件接口-BatchSendEmail，即可完成批量发信。需要注意的是在使用本接口后BatchSendEmail接口中的Template参数不需再传。用户也可以在控制台上邮件发送-收件人列表菜单中，通过导入文件的方式，导入收件人地址和模板变量和参数值。本接口一次请求的收件人地址数量限制为2W条，本接口同时也可以用来向已经上传完成的收件人列表追加收件人地址，但收件人列表中收件人地址的总量不能超过一定的数量，目前是限制5万条。本接口不支持去除重复的收件人地址，用户需要自己保证上传和追加地址不重复，不与之前上传的地址重复。

        :param request: Request instance for CreateReceiverDetailWithData.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailWithDataRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailWithDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReceiverDetailWithData", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReceiverDetailWithDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressUnsubscribeConfig(self, request):
        """删除地址级退订配置

        :param request: Request instance for DeleteAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBlackList(self, request):
        """邮箱被拉黑之后，用户如果确认收件邮箱有效或者已经处于激活状态，可以从腾讯云地址库中删除该黑名单之后继续投递。

        :param request: Request instance for DeleteBlackList.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlackList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBlackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomBlackList(self, request):
        """删除自定义黑名单邮箱地址

        :param request: Request instance for DeleteCustomBlackList.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteCustomBlackListRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteCustomBlackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomBlackList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomBlackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEmailAddress(self, request):
        """删除发信人地址

        :param request: Request instance for DeleteEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEmailIdentity(self, request):
        """删除发信域名，删除后，将不可再使用该域名进行发信

        :param request: Request instance for DeleteEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEmailTemplate(self, request):
        """删除发信模板

        :param request: Request instance for DeleteEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReceiver(self, request):
        """根据收件id删除收件人列表,同时删除列表中的所有收件邮箱

        :param request: Request instance for DeleteReceiver.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteReceiverRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmailIdentity(self, request):
        """获取某个发信域名的配置详情

        :param request: Request instance for GetEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.GetEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmailTemplate(self, request):
        """根据模板ID获取模板详情

        :param request: Request instance for GetEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.GetEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSendEmailStatus(self, request):
        """获取邮件发送状态。仅支持查询30天之内的数据

        :param request: Request instance for GetSendEmailStatus.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetSendEmailStatusRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetSendEmailStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSendEmailStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetSendEmailStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetStatisticsReport(self, request):
        """获取近期发送的统计情况，包含发送量、送达率、打开率、退信率等一系列数据。

        :param request: Request instance for GetStatisticsReport.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetStatisticsReport", params, headers=headers)
            response = json.loads(body)
            model = models.GetStatisticsReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAddressUnsubscribeConfig(self, request):
        """获取地址级退订配置列表

        :param request: Request instance for ListAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ListAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListBlackEmailAddress(self, request):
        """腾讯云发送的邮件一旦被收件方判断为硬退(Hard Bounce)，腾讯云会拉黑该地址，并不允许所有用户向该地址发送邮件。成为邮箱黑名单。如果业务方确认是误判，可以从黑名单中删除。

        :param request: Request instance for ListBlackEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListBlackEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ListBlackEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCustomBlacklist(self, request):
        """获取自定义黑名单列表

        :param request: Request instance for ListCustomBlacklist.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListCustomBlacklistRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListCustomBlacklistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCustomBlacklist", params, headers=headers)
            response = json.loads(body)
            model = models.ListCustomBlacklistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEmailAddress(self, request):
        """获取发信地址列表

        :param request: Request instance for ListEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ListEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEmailIdentities(self, request):
        """获取当前发信域名列表，包含已验证通过与未验证的域名

        :param request: Request instance for ListEmailIdentities.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEmailIdentities", params, headers=headers)
            response = json.loads(body)
            model = models.ListEmailIdentitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEmailTemplates(self, request):
        """获取当前邮件模板列表

        :param request: Request instance for ListEmailTemplates.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEmailTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListEmailTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReceiverDetails(self, request):
        """根据收件人列表id查询收件人列表中的所有收件人邮箱地址，分页查询，可以根据收件邮箱地址来过滤查询

        :param request: Request instance for ListReceiverDetails.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListReceiverDetailsRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListReceiverDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReceiverDetails", params, headers=headers)
            response = json.loads(body)
            model = models.ListReceiverDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReceivers(self, request):
        """根据条件查询收件人列表，支持分页，模糊查询，状态查询

        :param request: Request instance for ListReceivers.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListReceiversRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListReceiversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReceivers", params, headers=headers)
            response = json.loads(body)
            model = models.ListReceiversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSendTasks(self, request):
        """分页查询批量发送邮件任务，包含即时发送任务，定时发送任务，周期重复发送任务，查询发送情况，包括请求数量，已发数量，缓存数量，任务状态等信息

        :param request: Request instance for ListSendTasks.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListSendTasksRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListSendTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSendTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListSendTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendEmail(self, request):
        """您可以通过此API发送HTML或者TEXT邮件，适用于触发类邮件（验证码、交易类）。默认仅支持使用模板发送邮件。

        :param request: Request instance for SendEmail.
        :type request: :class:`tencentcloud.ses.v20201002.models.SendEmailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.SendEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendEmail", params, headers=headers)
            response = json.loads(body)
            model = models.SendEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAddressUnsubscribeConfig(self, request):
        """用于更新地址级退订配置

        :param request: Request instance for UpdateAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCustomBlackList(self, request):
        """更新自定义黑名单

        :param request: Request instance for UpdateCustomBlackList.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateCustomBlackListRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateCustomBlackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCustomBlackList", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCustomBlackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEmailIdentity(self, request):
        """您已经成功配置好了您的DNS，接下来请求腾讯云验证您的DNS配置是否正确

        :param request: Request instance for UpdateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEmailSmtpPassWord(self, request):
        """设置邮箱的smtp密码。若要通过smtp发送邮件，必须为邮箱设置smtp密码。初始时，邮箱没有设置smtp密码，不能使用smtp的方式发送邮件。设置smtp密码后，可以修改密码。

        :param request: Request instance for UpdateEmailSmtpPassWord.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailSmtpPassWordRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailSmtpPassWordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEmailSmtpPassWord", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEmailSmtpPassWordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEmailTemplate(self, request):
        """更新邮件模板，更新后需再次审核

        :param request: Request instance for UpdateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))