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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ses.v20201002 import models
from typing import Dict


class SesClient(AbstractClient):
    _apiVersion = '2020-10-02'
    _endpoint = 'ses.tencentcloudapi.com'
    _service = 'ses'

    async def BatchSendEmail(
            self,
            request: models.BatchSendEmailRequest,
            opts: Dict = None,
    ) -> models.BatchSendEmailResponse:
        """
        您可以通过此API批量发送TEXT或者HTML邮件，适用于营销类、通知类邮件。默认仅支持使用模板发送邮件。批量发送之前，需先创建收件人列表，和收件人地址，并通过收件人列表id来进行发送。批量发送任务支持定时发送和周期重复发送，定时发送需传TimedParam，周期重复发送需传CycleParam
        """
        
        kwargs = {}
        kwargs["action"] = "BatchSendEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchSendEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAddressUnsubscribeConfig(
            self,
            request: models.CreateAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.CreateAddressUnsubscribeConfigResponse:
        """
        创建地址级退订配置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomBlacklist(
            self,
            request: models.CreateCustomBlacklistRequest,
            opts: Dict = None,
    ) -> models.CreateCustomBlacklistResponse:
        """
        添加自定义黑名单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomBlacklist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomBlacklistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmailAddress(
            self,
            request: models.CreateEmailAddressRequest,
            opts: Dict = None,
    ) -> models.CreateEmailAddressResponse:
        """
        在验证了发信域名之后，您需要一个发信地址来发送邮件。例如发信域名是mail.qcloud.com，那么发信地址可以为 service@mail.qcloud.com。如果您想要收件人在收件箱列表中显示您的别名，例如"腾讯云邮件通知"。那么发信地址为： 别名 空格 尖括号 邮箱地址。请注意中间需要有空格
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmailIdentity(
            self,
            request: models.CreateEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.CreateEmailIdentityResponse:
        """
        在使用身份发送电子邮件之前，您需要有一个电子邮件域名，该域名可以是您的网站或者移动应用的域名。您首先必须进行验证，证明自己是该域名的所有者，并且授权给腾讯云SES发送许可，才可以从该域名发送电子邮件。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmailTemplate(
            self,
            request: models.CreateEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateEmailTemplateResponse:
        """
        创建模板，该模板可以是TXT或者HTML，请注意如果HTML不要包含外部文件的CSS。模板中的变量使用 {{变量名}} 表示。
        注意：模板需要审核通过才可以使用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReceiver(
            self,
            request: models.CreateReceiverRequest,
            opts: Dict = None,
    ) -> models.CreateReceiverResponse:
        """
        创建收件人列表，收件人列表是发送批量邮件的目标邮件地址列表。创建列表后，需要上传收件人邮箱地址。之后创建发送任务，关联列表，便可以实现批量发送邮件的功能
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReceiverDetail(
            self,
            request: models.CreateReceiverDetailRequest,
            opts: Dict = None,
    ) -> models.CreateReceiverDetailResponse:
        """
        在创建完收件人列表后，向这个收件人列表中批量增加收件人邮箱地址，一次最大支持2万，异步完成处理。数据量比较大的时候，上传可能需要一点时间，可以通过查询收件人列表了解上传状态和上传数量。本接口与接口CreateReceiverDetailWithData的功能特性基本一致，只是不支持上传发信时的模板参数。用户首先调用创建收件人列表接口-CreateReceiver后，然后调用本接口传入收件人地址，最后使用批量发送邮件接口-BatchSendEmail，即可完成批量发信。本接口也支持追加收件人地址，也不支持去重，需要用户自己保证收件人地址不重复。本接口一次请求的收件人地址数量限制为2W条，但收件人列表中收件人地址的总量不能超过一定的数量，目前是限制5万条。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReceiverDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReceiverDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReceiverDetailWithData(
            self,
            request: models.CreateReceiverDetailWithDataRequest,
            opts: Dict = None,
    ) -> models.CreateReceiverDetailWithDataResponse:
        """
        添加收件人地址附带模板参数，使用本接口在添加收件人地址的同时传入模板参数，使每一个收件人地址在发信的时候使用的模板变量取值不同。用户首先调用创建收件人列表接口-CreateReceiver后，然后调用本接口传入收件人地址和发信时的模板参数，最后使用批量发送邮件接口-BatchSendEmail，即可完成批量发信。需要注意的是在使用本接口后BatchSendEmail接口中的Template参数不需再传。用户也可以在控制台上邮件发送-收件人列表菜单中，通过导入文件的方式，导入收件人地址和模板变量和参数值。本接口一次请求的收件人地址数量限制为2W条，本接口同时也可以用来向已经上传完成的收件人列表追加收件人地址，但收件人列表中收件人地址的总量不能超过一定的数量，目前是限制5万条。本接口不支持去除重复的收件人地址，用户需要自己保证上传和追加地址不重复，不与之前上传的地址重复。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReceiverDetailWithData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReceiverDetailWithDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressUnsubscribeConfig(
            self,
            request: models.DeleteAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressUnsubscribeConfigResponse:
        """
        删除地址级退订配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBlackList(
            self,
            request: models.DeleteBlackListRequest,
            opts: Dict = None,
    ) -> models.DeleteBlackListResponse:
        """
        邮箱被拉黑之后，用户如果确认收件邮箱有效或者已经处于激活状态，可以从腾讯云地址库中删除该黑名单之后继续投递。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBlackList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBlackListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomBlackList(
            self,
            request: models.DeleteCustomBlackListRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomBlackListResponse:
        """
        删除自定义黑名单邮箱地址
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomBlackList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomBlackListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEmailAddress(
            self,
            request: models.DeleteEmailAddressRequest,
            opts: Dict = None,
    ) -> models.DeleteEmailAddressResponse:
        """
        删除发信人地址
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEmailIdentity(
            self,
            request: models.DeleteEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.DeleteEmailIdentityResponse:
        """
        删除发信域名，删除后，将不可再使用该域名进行发信
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEmailTemplate(
            self,
            request: models.DeleteEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteEmailTemplateResponse:
        """
        删除发信模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReceiver(
            self,
            request: models.DeleteReceiverRequest,
            opts: Dict = None,
    ) -> models.DeleteReceiverResponse:
        """
        根据收件id删除收件人列表,同时删除列表中的所有收件邮箱
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEmailIdentity(
            self,
            request: models.GetEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.GetEmailIdentityResponse:
        """
        获取某个发信域名的配置详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEmailTemplate(
            self,
            request: models.GetEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.GetEmailTemplateResponse:
        """
        根据模板ID获取模板详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSendEmailStatus(
            self,
            request: models.GetSendEmailStatusRequest,
            opts: Dict = None,
    ) -> models.GetSendEmailStatusResponse:
        """
        获取邮件发送状态。仅支持查询30天之内的数据
        """
        
        kwargs = {}
        kwargs["action"] = "GetSendEmailStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSendEmailStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetStatisticsReport(
            self,
            request: models.GetStatisticsReportRequest,
            opts: Dict = None,
    ) -> models.GetStatisticsReportResponse:
        """
        获取近期发送的统计情况，包含发送量、送达率、打开率、退信率等一系列数据。
        """
        
        kwargs = {}
        kwargs["action"] = "GetStatisticsReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetStatisticsReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAddressUnsubscribeConfig(
            self,
            request: models.ListAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.ListAddressUnsubscribeConfigResponse:
        """
        获取地址级退订配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListBlackEmailAddress(
            self,
            request: models.ListBlackEmailAddressRequest,
            opts: Dict = None,
    ) -> models.ListBlackEmailAddressResponse:
        """
        腾讯云发送的邮件一旦被收件方判断为硬退(Hard Bounce)，腾讯云会拉黑该地址，并不允许所有用户向该地址发送邮件。成为邮箱黑名单。如果业务方确认是误判，可以从黑名单中删除。
        """
        
        kwargs = {}
        kwargs["action"] = "ListBlackEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListBlackEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCustomBlacklist(
            self,
            request: models.ListCustomBlacklistRequest,
            opts: Dict = None,
    ) -> models.ListCustomBlacklistResponse:
        """
        获取自定义黑名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListCustomBlacklist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCustomBlacklistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEmailAddress(
            self,
            request: models.ListEmailAddressRequest,
            opts: Dict = None,
    ) -> models.ListEmailAddressResponse:
        """
        获取发信地址列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEmailIdentities(
            self,
            request: models.ListEmailIdentitiesRequest,
            opts: Dict = None,
    ) -> models.ListEmailIdentitiesResponse:
        """
        获取当前发信域名列表，包含已验证通过与未验证的域名
        """
        
        kwargs = {}
        kwargs["action"] = "ListEmailIdentities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEmailIdentitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEmailTemplates(
            self,
            request: models.ListEmailTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListEmailTemplatesResponse:
        """
        获取当前邮件模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListEmailTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEmailTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReceiverDetails(
            self,
            request: models.ListReceiverDetailsRequest,
            opts: Dict = None,
    ) -> models.ListReceiverDetailsResponse:
        """
        根据收件人列表id查询收件人列表中的所有收件人邮箱地址，分页查询，可以根据收件邮箱地址来过滤查询
        """
        
        kwargs = {}
        kwargs["action"] = "ListReceiverDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReceiverDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReceivers(
            self,
            request: models.ListReceiversRequest,
            opts: Dict = None,
    ) -> models.ListReceiversResponse:
        """
        根据条件查询收件人列表，支持分页，模糊查询，状态查询
        """
        
        kwargs = {}
        kwargs["action"] = "ListReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSendTasks(
            self,
            request: models.ListSendTasksRequest,
            opts: Dict = None,
    ) -> models.ListSendTasksResponse:
        """
        分页查询批量发送邮件任务，包含即时发送任务，定时发送任务，周期重复发送任务，查询发送情况，包括请求数量，已发数量，缓存数量，任务状态等信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListSendTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSendTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendEmail(
            self,
            request: models.SendEmailRequest,
            opts: Dict = None,
    ) -> models.SendEmailResponse:
        """
        您可以通过此API发送HTML或者TEXT邮件，适用于触发类邮件（验证码、交易类）。默认仅支持使用模板发送邮件。
        """
        
        kwargs = {}
        kwargs["action"] = "SendEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAddressUnsubscribeConfig(
            self,
            request: models.UpdateAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateAddressUnsubscribeConfigResponse:
        """
        用于更新地址级退订配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCustomBlackList(
            self,
            request: models.UpdateCustomBlackListRequest,
            opts: Dict = None,
    ) -> models.UpdateCustomBlackListResponse:
        """
        更新自定义黑名单
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCustomBlackList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCustomBlackListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEmailIdentity(
            self,
            request: models.UpdateEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.UpdateEmailIdentityResponse:
        """
        您已经成功配置好了您的DNS，接下来请求腾讯云验证您的DNS配置是否正确
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEmailSmtpPassWord(
            self,
            request: models.UpdateEmailSmtpPassWordRequest,
            opts: Dict = None,
    ) -> models.UpdateEmailSmtpPassWordResponse:
        """
        设置邮箱的smtp密码。若要通过smtp发送邮件，必须为邮箱设置smtp密码。初始时，邮箱没有设置smtp密码，不能使用smtp的方式发送邮件。设置smtp密码后，可以修改密码。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEmailSmtpPassWord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEmailSmtpPassWordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEmailTemplate(
            self,
            request: models.UpdateEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateEmailTemplateResponse:
        """
        更新邮件模板，更新后需再次审核
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)