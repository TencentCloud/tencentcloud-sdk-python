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
from tencentcloud.ccc.v20200210 import models
from typing import Dict


class CccClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'ccc.tencentcloudapi.com'
    _service = 'ccc'

    async def AbortAgentCruiseDialingCampaign(
            self,
            request: models.AbortAgentCruiseDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.AbortAgentCruiseDialingCampaignResponse:
        """
        停止座席巡航式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "AbortAgentCruiseDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortAgentCruiseDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AbortPredictiveDialingCampaign(
            self,
            request: models.AbortPredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.AbortPredictiveDialingCampaignResponse:
        """
        停止预测式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "AbortPredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AbortPredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindNumberCallInInterface(
            self,
            request: models.BindNumberCallInInterfaceRequest,
            opts: Dict = None,
    ) -> models.BindNumberCallInInterfaceResponse:
        """
        绑定号码呼入回调接口
        """
        
        kwargs = {}
        kwargs["action"] = "BindNumberCallInInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindNumberCallInInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindNumberCallOutSkillGroup(
            self,
            request: models.BindNumberCallOutSkillGroupRequest,
            opts: Dict = None,
    ) -> models.BindNumberCallOutSkillGroupResponse:
        """
        绑定号码外呼技能组
        """
        
        kwargs = {}
        kwargs["action"] = "BindNumberCallOutSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindNumberCallOutSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindStaffSkillGroupList(
            self,
            request: models.BindStaffSkillGroupListRequest,
            opts: Dict = None,
    ) -> models.BindStaffSkillGroupListResponse:
        """
        绑定座席所属技能组
        """
        
        kwargs = {}
        kwargs["action"] = "BindStaffSkillGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindStaffSkillGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlAIConversation(
            self,
            request: models.ControlAIConversationRequest,
            opts: Dict = None,
    ) -> models.ControlAIConversationResponse:
        """
        提供服务端控制机器人的功能
        """
        
        kwargs = {}
        kwargs["action"] = "ControlAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIAgentCall(
            self,
            request: models.CreateAIAgentCallRequest,
            opts: Dict = None,
    ) -> models.CreateAIAgentCallResponse:
        """
        用于创建**一次性的智能体外呼通话**。你可以在管理端-智能体管理中，新建语音智能体，进行 [对话流程配置](https://cloud.tencent.com/document/product/679/119796) 。该接口可调用配置完成的智能体发起单次的外呼任务。若需创建批量智能体外呼任务，请参考文档 [创建自动外呼任务](https://cloud.tencent.com/document/product/679/69194)。

        该功能需购买语音智能体通话套餐，并且仅限自有电话号码使用。详情请参考 [语音智能体通话购买指引](https://cloud.tencent.com/document/product/679/125953)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIAgentCall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIAgentCallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAICall(
            self,
            request: models.CreateAICallRequest,
            opts: Dict = None,
    ) -> models.CreateAICallResponse:
        """
        用于调用AI模型发起外呼通话，仅限自有电话号码使用，目前开通高级版座席**限时**免费体验。

        发起通话前，请先确认您的AI模型是否兼容 OpenAI、Azure 或 Minimax 协议，并前往模型服务商网站获取相关鉴权信息。 具体功能说明请参考文档 [腾讯云联络中心AI通话平台](https://cloud.tencent.com/document/product/679/112100)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAICall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAICallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAdminURL(
            self,
            request: models.CreateAdminURLRequest,
            opts: Dict = None,
    ) -> models.CreateAdminURLResponse:
        """
        创建管理端访问链接
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAdminURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAdminURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentCruiseDialingCampaign(
            self,
            request: models.CreateAgentCruiseDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.CreateAgentCruiseDialingCampaignResponse:
        """
        座席巡航式外呼。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentCruiseDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentCruiseDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoCalloutTask(
            self,
            request: models.CreateAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAutoCalloutTaskResponse:
        """
        用于**创建批量自动外呼通话**，系统将根据任务配置，自动向指定的**被叫号码列表**发起外呼通话。该接口可调用配置完成的智能体发起批量的外呼任务，你可以在管理端-智能体管理中，新建语音智能体，进行 [对话流程配置](https://cloud.tencent.com/document/product/679/119796)。若需创建单次智能体外呼任务，请参考文档 [创建单次智能体通话](https://cloud.tencent.com/document/product/679/115681)。

        该功能需购买语音智能体通话套餐，并且仅限自有电话号码使用。详情请参考 [语音智能体通话购买指引](https://cloud.tencent.com/document/product/679/125953)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCCCSkillGroup(
            self,
            request: models.CreateCCCSkillGroupRequest,
            opts: Dict = None,
    ) -> models.CreateCCCSkillGroupResponse:
        """
        新建技能组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCCCSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCCCSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCallOutSession(
            self,
            request: models.CreateCallOutSessionRequest,
            opts: Dict = None,
    ) -> models.CreateCallOutSessionResponse:
        """
        创建外呼会话，当前仅支持双呼，即先使用平台号码呼出到座席手机上，座席接听后，然后再外呼用户，而且由于运营商频率限制，座席手机号必须先加白名单，避免频控导致外呼失败。所以调用此接口前，下述操作均已完成
        1. UserId 指定的座席已经[绑定手机号](https://cloud.tencent.com/document/product/679/76067#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E5.AE.8C.E5.96.84.E8.B4.A6.E5.8F.B7.E4.BF.A1.E6.81.AF)
        2. 座席绑定的手机号已经[申请并通过了外呼白名单](https://cloud.tencent.com/document/product/679/76744#.E6.93.8D.E4.BD.9C.E6.AD.A5.E9.AA.A4)
        3. 当前座席侧只能呼叫其手机，所以 IsForceMobile 字段当前必须为 true
        4. 被叫不要填当前 UserId 所绑定的手机号，否则会造成占线呼叫失败
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCallOutSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCallOutSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCarrierPrivilegeNumberApplicant(
            self,
            request: models.CreateCarrierPrivilegeNumberApplicantRequest,
            opts: Dict = None,
    ) -> models.CreateCarrierPrivilegeNumberApplicantResponse:
        """
        用于无限频率地呼叫坐席手机
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCarrierPrivilegeNumberApplicant"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCarrierPrivilegeNumberApplicantResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCompanyApply(
            self,
            request: models.CreateCompanyApplyRequest,
            opts: Dict = None,
    ) -> models.CreateCompanyApplyResponse:
        """
        创建公司资质申请（1、首次使用接口，建议先在云联络中心控制台查看各个资料模板:https://console.cloud.tencent.com/ccc/enterprise/update。2、参数中图片Url建议使用腾讯云Cos存储的临时链接）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCompanyApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCompanyApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExtension(
            self,
            request: models.CreateExtensionRequest,
            opts: Dict = None,
    ) -> models.CreateExtensionResponse:
        """
        创建话机账号
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIVRSession(
            self,
            request: models.CreateIVRSessionRequest,
            opts: Dict = None,
    ) -> models.CreateIVRSessionResponse:
        """
        创建关联 IVR 的会话，仅高级版支持，目前支持呼入和自动外呼两种 IVR 类型。收到请求后 TCCC 会先尝试呼通被叫，然后进入 IVR 流程。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIVRSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIVRSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOwnNumberApply(
            self,
            request: models.CreateOwnNumberApplyRequest,
            opts: Dict = None,
    ) -> models.CreateOwnNumberApplyResponse:
        """
        创建客户自携号码接入审核
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOwnNumberApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOwnNumberApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePredictiveDialingCampaign(
            self,
            request: models.CreatePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.CreatePredictiveDialingCampaignResponse:
        """
        创建预测式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSDKLoginToken(
            self,
            request: models.CreateSDKLoginTokenRequest,
            opts: Dict = None,
    ) -> models.CreateSDKLoginTokenResponse:
        """
        创建 SDK 登录 Token。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSDKLoginToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSDKLoginTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStaff(
            self,
            request: models.CreateStaffRequest,
            opts: Dict = None,
    ) -> models.CreateStaffResponse:
        """
        创建客服账号。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStaff"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStaffResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserSig(
            self,
            request: models.CreateUserSigRequest,
            opts: Dict = None,
    ) -> models.CreateUserSigResponse:
        """
        创建用户数据签名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserSig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserSigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCCCSkillGroup(
            self,
            request: models.DeleteCCCSkillGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteCCCSkillGroupResponse:
        """
        删除技能组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCCCSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCCCSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExtension(
            self,
            request: models.DeleteExtensionRequest,
            opts: Dict = None,
    ) -> models.DeleteExtensionResponse:
        """
        删除话机账号
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePredictiveDialingCampaign(
            self,
            request: models.DeletePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.DeletePredictiveDialingCampaignResponse:
        """
        删除预测式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStaff(
            self,
            request: models.DeleteStaffRequest,
            opts: Dict = None,
    ) -> models.DeleteStaffResponse:
        """
        删除坐席信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStaff"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStaffResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAgentInfoList(
            self,
            request: models.DescribeAIAgentInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAgentInfoListResponse:
        """
        本接口用于分页查询指定实例（SdkAppId）下已配置的智能体信息列表，包括智能体ID和名称等基本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAgentInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAgentInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIAnalysisResult(
            self,
            request: models.DescribeAIAnalysisResultRequest,
            opts: Dict = None,
    ) -> models.DescribeAIAnalysisResultResponse:
        """
        获取 AI 会话分析结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIAnalysisResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIAnalysisResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAICallExtractResult(
            self,
            request: models.DescribeAICallExtractResultRequest,
            opts: Dict = None,
    ) -> models.DescribeAICallExtractResultResponse:
        """
        本接口用于：在语音智能体通话结束后，通过 Session ID 查询指定会话的 **话后标签** 结果。相关话后标签需提前在管理端完成配置，具体说明请参见 [话后标签](https://cloud.tencent.com/document/product/679/119800) 。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAICallExtractResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAICallExtractResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAILatency(
            self,
            request: models.DescribeAILatencyRequest,
            opts: Dict = None,
    ) -> models.DescribeAILatencyResponse:
        """
        调用该接口，可以通过 Session ID 查询指定会话在特定时间段内，AI服务的处理时延明细与统计数据，时延信息包括：
        - 端到端（ETE）时延：统计从用户语音输入到 AI 返回完整响应的整体耗时。
        - 自动语音识别（ASR）时延：统计语音输入被识别为文本所需的处理耗时。
        - 大语言模型（LLM）时延：统计 AI 模型生成文本内容的推理耗时。
        - 语音合成（TTS）时延：统计文本转换为语音音频的合成耗时。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAILatency"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAILatencyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActiveCarrierPrivilegeNumber(
            self,
            request: models.DescribeActiveCarrierPrivilegeNumberRequest,
            opts: Dict = None,
    ) -> models.DescribeActiveCarrierPrivilegeNumberResponse:
        """
        查询生效运营商白名单规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActiveCarrierPrivilegeNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActiveCarrierPrivilegeNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentCruiseDialingCampaign(
            self,
            request: models.DescribeAgentCruiseDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentCruiseDialingCampaignResponse:
        """
        查询 座席巡航式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentCruiseDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentCruiseDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoCalloutTask(
            self,
            request: models.DescribeAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoCalloutTaskResponse:
        """
        查询自动外呼任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoCalloutTasks(
            self,
            request: models.DescribeAutoCalloutTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoCalloutTasksResponse:
        """
        批量查询自动外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoCalloutTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoCalloutTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCCCBuyInfoList(
            self,
            request: models.DescribeCCCBuyInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeCCCBuyInfoListResponse:
        """
        获取用户购买信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCCCBuyInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCCCBuyInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallInMetrics(
            self,
            request: models.DescribeCallInMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeCallInMetricsResponse:
        """
        获取呼入实时数据统计指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallInMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallInMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCarrierPrivilegeNumberApplicants(
            self,
            request: models.DescribeCarrierPrivilegeNumberApplicantsRequest,
            opts: Dict = None,
    ) -> models.DescribeCarrierPrivilegeNumberApplicantsResponse:
        """
        查询单状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCarrierPrivilegeNumberApplicants"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCarrierPrivilegeNumberApplicantsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChatMessages(
            self,
            request: models.DescribeChatMessagesRequest,
            opts: Dict = None,
    ) -> models.DescribeChatMessagesResponse:
        """
        获取指定服务记录文本聊天内容，需要先使用查询在线客服记录（DescribeIMCdrs） API 获取服务记录 SessionId。

        文本聊天记录只保存了 1 年内的，1 年之前会自动清理。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChatMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChatMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompanyList(
            self,
            request: models.DescribeCompanyListRequest,
            opts: Dict = None,
    ) -> models.DescribeCompanyListResponse:
        """
        查询公司资质申请列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompanyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompanyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtension(
            self,
            request: models.DescribeExtensionRequest,
            opts: Dict = None,
    ) -> models.DescribeExtensionResponse:
        """
        获取话机信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtensions(
            self,
            request: models.DescribeExtensionsRequest,
            opts: Dict = None,
    ) -> models.DescribeExtensionsResponse:
        """
        查询话机列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtensions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtensionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIMCdrList(
            self,
            request: models.DescribeIMCdrListRequest,
            opts: Dict = None,
    ) -> models.DescribeIMCdrListResponse:
        """
        获取包括全媒体和文本会话两种类型的服务记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIMCdrList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIMCdrListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIMCdrs(
            self,
            request: models.DescribeIMCdrsRequest,
            opts: Dict = None,
    ) -> models.DescribeIMCdrsResponse:
        """
        获取包括全媒体和文本会话两种类型的服务记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIMCdrs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIMCdrsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIvrAudioList(
            self,
            request: models.DescribeIvrAudioListRequest,
            opts: Dict = None,
    ) -> models.DescribeIvrAudioListResponse:
        """
        查询IVR音频文件列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIvrAudioList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIvrAudioListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNumbers(
            self,
            request: models.DescribeNumbersRequest,
            opts: Dict = None,
    ) -> models.DescribeNumbersResponse:
        """
        查询号码列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNumbers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNumbersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePSTNActiveSessionList(
            self,
            request: models.DescribePSTNActiveSessionListRequest,
            opts: Dict = None,
    ) -> models.DescribePSTNActiveSessionListResponse:
        """
        获取当前正在通话的会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePSTNActiveSessionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePSTNActiveSessionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePredictiveDialingCampaign(
            self,
            request: models.DescribePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.DescribePredictiveDialingCampaignResponse:
        """
        查询预测式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePredictiveDialingCampaigns(
            self,
            request: models.DescribePredictiveDialingCampaignsRequest,
            opts: Dict = None,
    ) -> models.DescribePredictiveDialingCampaignsResponse:
        """
        查询预测式外呼任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePredictiveDialingCampaigns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePredictiveDialingCampaignsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePredictiveDialingSessions(
            self,
            request: models.DescribePredictiveDialingSessionsRequest,
            opts: Dict = None,
    ) -> models.DescribePredictiveDialingSessionsResponse:
        """
        查询预测式外呼呼叫列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePredictiveDialingSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePredictiveDialingSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectedTelCdr(
            self,
            request: models.DescribeProtectedTelCdrRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectedTelCdrResponse:
        """
        获取主被叫受保护的电话服务记录与录音
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectedTelCdr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectedTelCdrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionDetail(
            self,
            request: models.DescribeSessionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionDetailResponse:
        """
        获取通话详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSkillGroupInfoList(
            self,
            request: models.DescribeSkillGroupInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeSkillGroupInfoListResponse:
        """
        获取技能组信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSkillGroupInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSkillGroupInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStaffInfoList(
            self,
            request: models.DescribeStaffInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeStaffInfoListResponse:
        """
        获取坐席信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStaffInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStaffInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStaffStatusHistory(
            self,
            request: models.DescribeStaffStatusHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeStaffStatusHistoryResponse:
        """
        查询座席状态历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStaffStatusHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStaffStatusHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStaffStatusMetrics(
            self,
            request: models.DescribeStaffStatusMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeStaffStatusMetricsResponse:
        """
        获取坐席实时状态统计指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStaffStatusMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStaffStatusMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelCallInfo(
            self,
            request: models.DescribeTelCallInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTelCallInfoResponse:
        """
        按实例获取电话消耗统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelCallInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelCallInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelCdr(
            self,
            request: models.DescribeTelCdrRequest,
            opts: Dict = None,
    ) -> models.DescribeTelCdrResponse:
        """
        获取电话服务记录与录音
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelCdr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelCdrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelRecordAsr(
            self,
            request: models.DescribeTelRecordAsrRequest,
            opts: Dict = None,
    ) -> models.DescribeTelRecordAsrResponse:
        """
        拉取会话录音转文本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelRecordAsr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelRecordAsrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTelSession(
            self,
            request: models.DescribeTelSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeTelSessionResponse:
        """
        获取 PSTN 会话信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTelSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTelSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableCCCPhoneNumber(
            self,
            request: models.DisableCCCPhoneNumberRequest,
            opts: Dict = None,
    ) -> models.DisableCCCPhoneNumberResponse:
        """
        停用号码
        """
        
        kwargs = {}
        kwargs["action"] = "DisableCCCPhoneNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableCCCPhoneNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForceMemberOffline(
            self,
            request: models.ForceMemberOfflineRequest,
            opts: Dict = None,
    ) -> models.ForceMemberOfflineResponse:
        """
        强制客服下线
        """
        
        kwargs = {}
        kwargs["action"] = "ForceMemberOffline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForceMemberOfflineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HangUpCall(
            self,
            request: models.HangUpCallRequest,
            opts: Dict = None,
    ) -> models.HangUpCallResponse:
        """
        挂断电话
        """
        
        kwargs = {}
        kwargs["action"] = "HangUpCall"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HangUpCallResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCompanyApply(
            self,
            request: models.ModifyCompanyApplyRequest,
            opts: Dict = None,
    ) -> models.ModifyCompanyApplyResponse:
        """
        修改公司资质申请，只能修改状态为驳回或待审核的申请单。（1、首次使用接口，建议先在云联络中心控制台查看各个资料模板:https://console.cloud.tencent.com/ccc/enterprise/update。2、参数中图片Url建议使用腾讯云Cos存储的临时链接）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCompanyApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCompanyApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExtension(
            self,
            request: models.ModifyExtensionRequest,
            opts: Dict = None,
    ) -> models.ModifyExtensionResponse:
        """
        修改话机账号(绑定技能组、绑定坐席账号)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExtension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExtensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOwnNumberApply(
            self,
            request: models.ModifyOwnNumberApplyRequest,
            opts: Dict = None,
    ) -> models.ModifyOwnNumberApplyResponse:
        """
        修改客户自携号码审批单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOwnNumberApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOwnNumberApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStaff(
            self,
            request: models.ModifyStaffRequest,
            opts: Dict = None,
    ) -> models.ModifyStaffResponse:
        """
        修改客服账号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStaff"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStaffResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStaffPassword(
            self,
            request: models.ModifyStaffPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyStaffPasswordResponse:
        """
        修改座席的密码
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStaffPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStaffPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseAutoCalloutTask(
            self,
            request: models.PauseAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.PauseAutoCalloutTaskResponse:
        """
        用于通过 TaskId **暂停一个正在执行的自动外呼任务**。调用该接口后，任务将被临时中断，不再发起新的外呼请求；已发起的通话不受影响。
        暂停后的任务可通过 [恢复暂停的自动外呼任务](https://cloud.tencent.com/document/product/679/125356) 接口继续执行。如需永久终止任务，请参考 [停止自动外呼任务](https://cloud.tencent.com/document/product/679/69192)。
        """
        
        kwargs = {}
        kwargs["action"] = "PauseAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PausePredictiveDialingCampaign(
            self,
            request: models.PausePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.PausePredictiveDialingCampaignResponse:
        """
        暂停预测式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "PausePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PausePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetExtensionPassword(
            self,
            request: models.ResetExtensionPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetExtensionPasswordResponse:
        """
        重置话机注册密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetExtensionPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetExtensionPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreMemberOnline(
            self,
            request: models.RestoreMemberOnlineRequest,
            opts: Dict = None,
    ) -> models.RestoreMemberOnlineResponse:
        """
        恢复客服上线
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreMemberOnline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreMemberOnlineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeAutoCalloutTask(
            self,
            request: models.ResumeAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.ResumeAutoCalloutTaskResponse:
        """
        用于通过 TaskId **恢复一个已被暂停的自动外呼任务**。该接口适用于在调用 [暂停自动外呼任务](https://cloud.tencent.com/document/product/679/125357) 后，需继续执行剩余外呼计划的场景。调用成功后，任务将从暂停状态恢复，重新发起未完成的外呼请求。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumePredictiveDialingCampaign(
            self,
            request: models.ResumePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.ResumePredictiveDialingCampaignResponse:
        """
        恢复预测式外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "ResumePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetStaffStatus(
            self,
            request: models.SetStaffStatusRequest,
            opts: Dict = None,
    ) -> models.SetStaffStatusResponse:
        """
        设置 staff 状态
        """
        
        kwargs = {}
        kwargs["action"] = "SetStaffStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetStaffStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAutoCalloutTask(
            self,
            request: models.StopAutoCalloutTaskRequest,
            opts: Dict = None,
    ) -> models.StopAutoCalloutTaskResponse:
        """
        停止自动外呼任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopAutoCalloutTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAutoCalloutTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransferToManual(
            self,
            request: models.TransferToManualRequest,
            opts: Dict = None,
    ) -> models.TransferToManualResponse:
        """
        特定场景下讲会话转接到人工坐席
        """
        
        kwargs = {}
        kwargs["action"] = "TransferToManual"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransferToManualResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindNumberCallOutSkillGroup(
            self,
            request: models.UnbindNumberCallOutSkillGroupRequest,
            opts: Dict = None,
    ) -> models.UnbindNumberCallOutSkillGroupResponse:
        """
        解绑号码外呼技能组
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindNumberCallOutSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindNumberCallOutSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindStaffSkillGroupList(
            self,
            request: models.UnbindStaffSkillGroupListRequest,
            opts: Dict = None,
    ) -> models.UnbindStaffSkillGroupListResponse:
        """
        解绑坐席所属技能组
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindStaffSkillGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindStaffSkillGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCCCSkillGroup(
            self,
            request: models.UpdateCCCSkillGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateCCCSkillGroupResponse:
        """
        更新技能组
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCCCSkillGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCCCSkillGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePredictiveDialingCampaign(
            self,
            request: models.UpdatePredictiveDialingCampaignRequest,
            opts: Dict = None,
    ) -> models.UpdatePredictiveDialingCampaignResponse:
        """
        任务未启动前，更新预测式外呼任务。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePredictiveDialingCampaign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePredictiveDialingCampaignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadIvrAudio(
            self,
            request: models.UploadIvrAudioRequest,
            opts: Dict = None,
    ) -> models.UploadIvrAudioResponse:
        """
        上传IVR中使用的音频文件，每日上传文件限制50个。（参数中音频文件Url建议使用腾讯云Cos存储的临时链接）
        """
        
        kwargs = {}
        kwargs["action"] = "UploadIvrAudio"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadIvrAudioResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)