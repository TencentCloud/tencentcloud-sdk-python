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
from tencentcloud.ccc.v20200210 import models


class CccClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'ccc.tencentcloudapi.com'
    _service = 'ccc'


    def AbortAgentCruiseDialingCampaign(self, request):
        """停止座席巡航式外呼任务

        :param request: Request instance for AbortAgentCruiseDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.AbortAgentCruiseDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AbortAgentCruiseDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AbortAgentCruiseDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.AbortAgentCruiseDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AbortPredictiveDialingCampaign(self, request):
        """停止预测式外呼任务

        :param request: Request instance for AbortPredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.AbortPredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.AbortPredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AbortPredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.AbortPredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindNumberCallOutSkillGroup(self, request):
        """绑定号码外呼技能组

        :param request: Request instance for BindNumberCallOutSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.BindNumberCallOutSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.BindNumberCallOutSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindNumberCallOutSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.BindNumberCallOutSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindStaffSkillGroupList(self, request):
        """绑定座席所属技能组

        :param request: Request instance for BindStaffSkillGroupList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.BindStaffSkillGroupListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.BindStaffSkillGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindStaffSkillGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.BindStaffSkillGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAIAgentCall(self, request):
        """用于调用AI模型发起外呼通话，仅限自有电话号码使用，目前开通高级版座席**限时**免费体验。

        发起通话前，请先确认您的AI模型是否兼容 OpenAI、Azure 或 Minimax 协议，并前往模型服务商网站获取相关鉴权信息。 具体功能说明请参考文档 [腾讯云联络中心AI通话平台](https://cloud.tencent.com/document/product/679/112100)。

        :param request: Request instance for CreateAIAgentCall.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAIAgentCallRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAIAgentCallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAIAgentCall", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAIAgentCallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAICall(self, request):
        """用于调用AI模型发起外呼通话，仅限自有电话号码使用，目前开通高级版座席**限时**免费体验。

        发起通话前，请先确认您的AI模型是否兼容 OpenAI、Azure 或 Minimax 协议，并前往模型服务商网站获取相关鉴权信息。 具体功能说明请参考文档 [腾讯云联络中心AI通话平台](https://cloud.tencent.com/document/product/679/112100)。

        :param request: Request instance for CreateAICall.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAICallRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAICallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAICall", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAICallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAdminURL(self, request):
        """创建管理端访问链接

        :param request: Request instance for CreateAdminURL.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAdminURLRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAdminURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAdminURL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAdminURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAgentCruiseDialingCampaign(self, request):
        """座席巡航式外呼。

        :param request: Request instance for CreateAgentCruiseDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAgentCruiseDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAgentCruiseDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAgentCruiseDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAgentCruiseDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoCalloutTask(self, request):
        """创建自动外呼任务

        :param request: Request instance for CreateAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCCCSkillGroup(self, request):
        """新建技能组

        :param request: Request instance for CreateCCCSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCCCSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCCCSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCCCSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCCCSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCallOutSession(self, request):
        """创建外呼会话，当前仅支持双呼，即先使用平台号码呼出到座席手机上，座席接听后，然后再外呼用户，而且由于运营商频率限制，座席手机号必须先加白名单，避免频控导致外呼失败。所以调用此接口前，下述操作均已完成
        1. UserId 指定的座席已经[绑定手机号](https://cloud.tencent.com/document/product/679/76067#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E5.AE.8C.E5.96.84.E8.B4.A6.E5.8F.B7.E4.BF.A1.E6.81.AF)
        2. 座席绑定的手机号已经[申请并通过了外呼白名单](https://cloud.tencent.com/document/product/679/76744#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)
        3. 当前座席侧只能呼叫其手机，所以 IsForceMobile 字段当前必须为 true
        4. 被叫不要填当前 UserId 所绑定的手机号，否则会造成占线呼叫失败

        :param request: Request instance for CreateCallOutSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCallOutSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCallOutSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCallOutSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCallOutSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCarrierPrivilegeNumberApplicant(self, request):
        """用于无限频率地呼叫坐席手机

        :param request: Request instance for CreateCarrierPrivilegeNumberApplicant.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCarrierPrivilegeNumberApplicantRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCarrierPrivilegeNumberApplicantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCarrierPrivilegeNumberApplicant", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCarrierPrivilegeNumberApplicantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCompanyApply(self, request):
        """创建公司资质申请（1、首次使用接口，建议先在云联络中心控制台查看各个资料模板:https://console.cloud.tencent.com/ccc/enterprise/update。2、参数中图片Url建议使用腾讯云Cos存储的临时链接）

        :param request: Request instance for CreateCompanyApply.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCompanyApplyRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCompanyApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCompanyApply", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCompanyApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExtension(self, request):
        """创建话机账号

        :param request: Request instance for CreateExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExtension", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIVRSession(self, request):
        """创建关联 IVR 的会话，仅高级版支持，目前支持呼入和自动外呼两种 IVR 类型。收到请求后 TCCC 会先尝试呼通被叫，然后进入 IVR 流程。

        :param request: Request instance for CreateIVRSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateIVRSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateIVRSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIVRSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIVRSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOwnNumberApply(self, request):
        """创建客户自携号码接入审核

        :param request: Request instance for CreateOwnNumberApply.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateOwnNumberApplyRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateOwnNumberApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOwnNumberApply", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOwnNumberApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePredictiveDialingCampaign(self, request):
        """创建预测式外呼任务

        :param request: Request instance for CreatePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreatePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreatePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSDKLoginToken(self, request):
        """创建 SDK 登录 Token。

        :param request: Request instance for CreateSDKLoginToken.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSDKLoginToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSDKLoginTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStaff(self, request):
        """创建客服账号。

        :param request: Request instance for CreateStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStaff", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserSig(self, request):
        """创建用户数据签名

        :param request: Request instance for CreateUserSig.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateUserSigRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateUserSigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserSig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserSigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteExtension(self, request):
        """删除话机账号

        :param request: Request instance for DeleteExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeleteExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeleteExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExtension", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePredictiveDialingCampaign(self, request):
        """删除预测式外呼任务

        :param request: Request instance for DeletePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeletePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeletePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStaff(self, request):
        """删除坐席信息

        :param request: Request instance for DeleteStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeleteStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeleteStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStaff", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAICallExtractResult(self, request):
        """获取 AI 通话内容提取结果。

        :param request: Request instance for DescribeAICallExtractResult.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAICallExtractResultRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAICallExtractResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAICallExtractResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAICallExtractResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAILatency(self, request):
        """获取 AI 时延信息

        :param request: Request instance for DescribeAILatency.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAILatencyRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAILatencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAILatency", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAILatencyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeActiveCarrierPrivilegeNumber(self, request):
        """查询生效运营商白名单规则

        :param request: Request instance for DescribeActiveCarrierPrivilegeNumber.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeActiveCarrierPrivilegeNumberRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeActiveCarrierPrivilegeNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeActiveCarrierPrivilegeNumber", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeActiveCarrierPrivilegeNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentCruiseDialingCampaign(self, request):
        """查询 座席巡航式外呼任务

        :param request: Request instance for DescribeAgentCruiseDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAgentCruiseDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAgentCruiseDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentCruiseDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentCruiseDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoCalloutTask(self, request):
        """查询自动外呼任务详情

        :param request: Request instance for DescribeAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoCalloutTasks(self, request):
        """批量查询自动外呼任务

        :param request: Request instance for DescribeAutoCalloutTasks.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTasksRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoCalloutTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoCalloutTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCCBuyInfoList(self, request):
        """获取用户购买信息列表

        :param request: Request instance for DescribeCCCBuyInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCCCBuyInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCCCBuyInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCCBuyInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCCBuyInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallInMetrics(self, request):
        """获取呼入实时数据统计指标

        :param request: Request instance for DescribeCallInMetrics.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCallInMetricsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCallInMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallInMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallInMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCarrierPrivilegeNumberApplicants(self, request):
        """查询单状态

        :param request: Request instance for DescribeCarrierPrivilegeNumberApplicants.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCarrierPrivilegeNumberApplicantsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCarrierPrivilegeNumberApplicantsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCarrierPrivilegeNumberApplicants", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCarrierPrivilegeNumberApplicantsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChatMessages(self, request):
        """获取指定服务记录文本聊天内容，需要先使用查询在线客服记录（DescribeIMCdrs） API 获取服务记录 SessionId。

        文本聊天记录只保存了 1 年内的，1 年之前会自动清理。

        :param request: Request instance for DescribeChatMessages.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeChatMessagesRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeChatMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChatMessages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChatMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompanyList(self, request):
        """查询公司资质申请列表

        :param request: Request instance for DescribeCompanyList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCompanyListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCompanyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompanyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompanyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtension(self, request):
        """获取话机信息

        :param request: Request instance for DescribeExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtension", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtensions(self, request):
        """查询话机列表信息

        :param request: Request instance for DescribeExtensions.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtensions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtensionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIMCdrList(self, request):
        """获取包括全媒体和文本会话两种类型的服务记录。

        :param request: Request instance for DescribeIMCdrList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIMCdrList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIMCdrListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIMCdrs(self, request):
        """获取包括全媒体和文本会话两种类型的服务记录。

        :param request: Request instance for DescribeIMCdrs.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIMCdrs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIMCdrsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIvrAudioList(self, request):
        """查询IVR音频文件列表信息

        :param request: Request instance for DescribeIvrAudioList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeIvrAudioListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeIvrAudioListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIvrAudioList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIvrAudioListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNumbers(self, request):
        """查询号码列表

        :param request: Request instance for DescribeNumbers.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeNumbersRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeNumbersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNumbers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNumbersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePSTNActiveSessionList(self, request):
        """获取当前正在通话的会话列表

        :param request: Request instance for DescribePSTNActiveSessionList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePSTNActiveSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePSTNActiveSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePredictiveDialingCampaign(self, request):
        """查询预测式外呼任务

        :param request: Request instance for DescribePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePredictiveDialingCampaigns(self, request):
        """查询预测式外呼任务列表

        :param request: Request instance for DescribePredictiveDialingCampaigns.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingCampaignsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePredictiveDialingCampaigns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePredictiveDialingCampaignsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePredictiveDialingSessions(self, request):
        """查询预测式外呼呼叫列表

        :param request: Request instance for DescribePredictiveDialingSessions.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingSessionsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePredictiveDialingSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePredictiveDialingSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePredictiveDialingSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectedTelCdr(self, request):
        """获取主被叫受保护的电话服务记录与录音

        :param request: Request instance for DescribeProtectedTelCdr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeProtectedTelCdrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeProtectedTelCdrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectedTelCdr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectedTelCdrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillGroupInfoList(self, request):
        """获取技能组信息列表

        :param request: Request instance for DescribeSkillGroupInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillGroupInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillGroupInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaffInfoList(self, request):
        """获取坐席信息列表

        :param request: Request instance for DescribeStaffInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaffInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaffInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaffStatusMetrics(self, request):
        """获取坐席实时状态统计指标

        :param request: Request instance for DescribeStaffStatusMetrics.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffStatusMetricsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffStatusMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaffStatusMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaffStatusMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelCallInfo(self, request):
        """按实例获取电话消耗统计

        :param request: Request instance for DescribeTelCallInfo.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelCallInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelCallInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelCdr(self, request):
        """获取电话服务记录与录音

        :param request: Request instance for DescribeTelCdr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelCdr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelCdrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelRecordAsr(self, request):
        """拉取会话录音转文本信息

        :param request: Request instance for DescribeTelRecordAsr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelRecordAsrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelRecordAsrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelRecordAsr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelRecordAsrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelSession(self, request):
        """获取 PSTN 会话信息

        :param request: Request instance for DescribeTelSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableCCCPhoneNumber(self, request):
        """停用号码

        :param request: Request instance for DisableCCCPhoneNumber.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DisableCCCPhoneNumberRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DisableCCCPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableCCCPhoneNumber", params, headers=headers)
            response = json.loads(body)
            model = models.DisableCCCPhoneNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForceMemberOffline(self, request):
        """强制客服下线

        :param request: Request instance for ForceMemberOffline.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ForceMemberOfflineRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ForceMemberOfflineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForceMemberOffline", params, headers=headers)
            response = json.loads(body)
            model = models.ForceMemberOfflineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HangUpCall(self, request):
        """挂断电话

        :param request: Request instance for HangUpCall.
        :type request: :class:`tencentcloud.ccc.v20200210.models.HangUpCallRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.HangUpCallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HangUpCall", params, headers=headers)
            response = json.loads(body)
            model = models.HangUpCallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCompanyApply(self, request):
        """修改公司资质申请，只能修改状态为驳回或待审核的申请单。（1、首次使用接口，建议先在云联络中心控制台查看各个资料模板:https://console.cloud.tencent.com/ccc/enterprise/update。2、参数中图片Url建议使用腾讯云Cos存储的临时链接）

        :param request: Request instance for ModifyCompanyApply.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyCompanyApplyRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyCompanyApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCompanyApply", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCompanyApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExtension(self, request):
        """修改话机账号(绑定技能组、绑定坐席账号)

        :param request: Request instance for ModifyExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExtension", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOwnNumberApply(self, request):
        """修改客户自携号码审批单

        :param request: Request instance for ModifyOwnNumberApply.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyOwnNumberApplyRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyOwnNumberApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOwnNumberApply", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOwnNumberApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStaff(self, request):
        """修改客服账号

        :param request: Request instance for ModifyStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStaff", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStaffPassword(self, request):
        """修改座席的密码

        :param request: Request instance for ModifyStaffPassword.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffPasswordRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStaffPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStaffPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PausePredictiveDialingCampaign(self, request):
        """暂停预测式外呼任务

        :param request: Request instance for PausePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.PausePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.PausePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PausePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.PausePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetExtensionPassword(self, request):
        """重置话机注册密码

        :param request: Request instance for ResetExtensionPassword.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ResetExtensionPasswordRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ResetExtensionPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetExtensionPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetExtensionPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreMemberOnline(self, request):
        """恢复客服上线

        :param request: Request instance for RestoreMemberOnline.
        :type request: :class:`tencentcloud.ccc.v20200210.models.RestoreMemberOnlineRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.RestoreMemberOnlineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreMemberOnline", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreMemberOnlineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumePredictiveDialingCampaign(self, request):
        """恢复预测式外呼任务

        :param request: Request instance for ResumePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ResumePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ResumePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.ResumePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAutoCalloutTask(self, request):
        """停止自动外呼任务

        :param request: Request instance for StopAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.StopAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.StopAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransferToManual(self, request):
        """特定场景下讲会话转接到人工坐席

        :param request: Request instance for TransferToManual.
        :type request: :class:`tencentcloud.ccc.v20200210.models.TransferToManualRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.TransferToManualResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransferToManual", params, headers=headers)
            response = json.loads(body)
            model = models.TransferToManualResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindNumberCallOutSkillGroup(self, request):
        """解绑号码外呼技能组

        :param request: Request instance for UnbindNumberCallOutSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UnbindNumberCallOutSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UnbindNumberCallOutSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindNumberCallOutSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindNumberCallOutSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindStaffSkillGroupList(self, request):
        """解绑坐席所属技能组

        :param request: Request instance for UnbindStaffSkillGroupList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UnbindStaffSkillGroupListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UnbindStaffSkillGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindStaffSkillGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindStaffSkillGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCCCSkillGroup(self, request):
        """更新技能组

        :param request: Request instance for UpdateCCCSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UpdateCCCSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UpdateCCCSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCCCSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCCCSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePredictiveDialingCampaign(self, request):
        """任务未启动前，更新预测式外呼任务。

        :param request: Request instance for UpdatePredictiveDialingCampaign.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UpdatePredictiveDialingCampaignRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UpdatePredictiveDialingCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePredictiveDialingCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePredictiveDialingCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadIvrAudio(self, request):
        """上传IVR中使用的音频文件，每日上传文件限制50个。（参数中音频文件Url建议使用腾讯云Cos存储的临时链接）

        :param request: Request instance for UploadIvrAudio.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UploadIvrAudioRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UploadIvrAudioResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadIvrAudio", params, headers=headers)
            response = json.loads(body)
            model = models.UploadIvrAudioResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))