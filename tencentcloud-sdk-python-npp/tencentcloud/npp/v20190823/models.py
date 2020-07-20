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

from tencentcloud.common.abstract_model import AbstractModel


class CallBackCdr(AbstractModel):
    """话单详情

    """

    def __init__(self):
        """
        :param CallId: 呼叫通话 ID
        :type CallId: str
        :param Src: 主叫号码
        :type Src: str
        :param Dst: 被叫号码
        :type Dst: str
        :param StartSrcCallTime: 主叫呼叫开始时间
        :type StartSrcCallTime: str
        :param StartSrcRingTime: 主叫响铃开始时间
        :type StartSrcRingTime: str
        :param SrcAcceptTime: 主叫接听时间
        :type SrcAcceptTime: str
        :param StartDstCallTime: 被叫呼叫开始时间
        :type StartDstCallTime: str
        :param StartDstRingTime: 被叫响铃开始时间
        :type StartDstRingTime: str
        :param DstAcceptTime: 被叫接听时间
        :type DstAcceptTime: str
        :param EndCallTime: 用户挂机通话结束时间
        :type EndCallTime: str
        :param CallEndStatus: 通话最后状态：0：未知状态 1：正常通话 2：主叫未接 3：主叫接听，被叫未接 4：主叫未接通 5：被叫未接通
        :type CallEndStatus: str
        :param Duration: 通话计费时间
        :type Duration: str
        :param RecordUrl: 录音 URL，如果不录音或录音失败，该值为空
        :type RecordUrl: str
        :param CallType: 通话类型(1: VOIP 2:IP TO PSTN 3: PSTN TO PSTN)，如果话单中没有该字段，默认值为回拨 3 (PSTN TO PSTN)
注意：此字段可能返回 null，表示取不到有效值。
        :type CallType: str
        :param BizId: 同回拨请求中的 bizId，如果回拨请求中带 bizId 会有该字段返回
注意：此字段可能返回 null，表示取不到有效值。
        :type BizId: str
        :param OrderId: 订单 ID,最大长度不超过 64 个字节，对于一些有订单状态 App 相关应用（如达人帮接入 App 应用)，该字段只在帐单中带上，其它回调不附带该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        """
        self.CallId = None
        self.Src = None
        self.Dst = None
        self.StartSrcCallTime = None
        self.StartSrcRingTime = None
        self.SrcAcceptTime = None
        self.StartDstCallTime = None
        self.StartDstRingTime = None
        self.DstAcceptTime = None
        self.EndCallTime = None
        self.CallEndStatus = None
        self.Duration = None
        self.RecordUrl = None
        self.CallType = None
        self.BizId = None
        self.OrderId = None


    def _deserialize(self, params):
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.StartSrcCallTime = params.get("StartSrcCallTime")
        self.StartSrcRingTime = params.get("StartSrcRingTime")
        self.SrcAcceptTime = params.get("SrcAcceptTime")
        self.StartDstCallTime = params.get("StartDstCallTime")
        self.StartDstRingTime = params.get("StartDstRingTime")
        self.DstAcceptTime = params.get("DstAcceptTime")
        self.EndCallTime = params.get("EndCallTime")
        self.CallEndStatus = params.get("CallEndStatus")
        self.Duration = params.get("Duration")
        self.RecordUrl = params.get("RecordUrl")
        self.CallType = params.get("CallType")
        self.BizId = params.get("BizId")
        self.OrderId = params.get("OrderId")


class CallBackPhoneCode(AbstractModel):
    """回拨号码字段

    """

    def __init__(self):
        """
        :param Nation: 国家码，统一以 00 开头
        :type Nation: str
        :param Phone: 号码（固话区号前加 0，如075586013388）
        :type Phone: str
        """
        self.Nation = None
        self.Phone = None


    def _deserialize(self, params):
        self.Nation = params.get("Nation")
        self.Phone = params.get("Phone")


class CreateCallBackRequest(AbstractModel):
    """CreateCallBack请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        :param Src: 主叫号码(必须为 11 位手机号，号码前加 0086，如 008613631686024)
        :type Src: str
        :param Dst: 被叫号码(必须为 11 位手机或固话号码,号码前加 0086，如008613631686024，固话如：0086075586013388)
        :type Dst: str
        :param SrcDisplayNum: 主叫显示系统分配的固话号码，如不填显示随机分配号码
        :type SrcDisplayNum: str
        :param DstDisplayNum: 被叫显示系统分配的固话号码，如不填显示随机分配号码
        :type DstDisplayNum: str
        :param Record: 是否录音，0 表示不录音，1 表示录音。默认为不录音
        :type Record: str
        :param MaxAllowTime: 允许最大通话时间，不填默认为 30 分钟（单位：分钟）
        :type MaxAllowTime: str
        :param StatusFlag: 主叫发起呼叫状态：1 被叫发起呼叫状态：256 主叫响铃状态：2 被叫响铃状态：512 主叫接听状态：4 被叫接听状态：1024 主叫拒绝接听状态：8 被叫拒绝接听状态：2048 主叫正常挂机状态：16 被叫正常挂机状态：4096 主叫呼叫异常：32 被叫呼叫异常：8192
例如：当值为 0：表示所有状态不需要推送；当值为 4：表示只要推送主叫接听状态；当值为 16191：表示所有状态都需要推送(上面所有值和)
        :type StatusFlag: str
        :param StatusUrl: 状态回调通知地址，正式环境可以配置默认推送地址
        :type StatusUrl: str
        :param HangupUrl: 话单回调通知地址，正式环境可以配置默认推送地址
        :type HangupUrl: str
        :param RecordUrl: 录单 URL 回调通知地址，正式环境可以配置默认推送地址
        :type RecordUrl: str
        :param BizId: 业务应用 key，业务用该 key 可以区分内部业务或客户产品等，该 key 需保证在该 appId 下全局唯一，最大长度不超过 64 个字节，bizId 只能包含数字、字母。
        :type BizId: str
        :param LastCallId: 最后一次呼叫 callId，带上该字段以后，平台会参考该 callId 分配线路，优先不分配该 callId 通话线路（注：谨慎使用，这个会影响线路调度）
        :type LastCallId: str
        :param PreCallerHandle: 结构体，主叫呼叫预处理操作，根据不同操作确认是否呼通被叫。如需使用，本结构体需要与 keyList 结构体配合使用，此时这两个参数都为必填项
        :type PreCallerHandle: :class:`tencentcloud.npp.v20190823.models.RreCallerHandle`
        :param OrderId: 订单 ID，最大长度不超过64个字节，对于一些有订单状态 App 相关应用使用（如达人帮接入 App 应用)，该字段只在帐单中带上，其它回调不附带该字段
        :type OrderId: str
        """
        self.BizAppId = None
        self.Src = None
        self.Dst = None
        self.SrcDisplayNum = None
        self.DstDisplayNum = None
        self.Record = None
        self.MaxAllowTime = None
        self.StatusFlag = None
        self.StatusUrl = None
        self.HangupUrl = None
        self.RecordUrl = None
        self.BizId = None
        self.LastCallId = None
        self.PreCallerHandle = None
        self.OrderId = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.SrcDisplayNum = params.get("SrcDisplayNum")
        self.DstDisplayNum = params.get("DstDisplayNum")
        self.Record = params.get("Record")
        self.MaxAllowTime = params.get("MaxAllowTime")
        self.StatusFlag = params.get("StatusFlag")
        self.StatusUrl = params.get("StatusUrl")
        self.HangupUrl = params.get("HangupUrl")
        self.RecordUrl = params.get("RecordUrl")
        self.BizId = params.get("BizId")
        self.LastCallId = params.get("LastCallId")
        if params.get("PreCallerHandle") is not None:
            self.PreCallerHandle = RreCallerHandle()
            self.PreCallerHandle._deserialize(params.get("PreCallerHandle"))
        self.OrderId = params.get("OrderId")


class CreateCallBackResponse(AbstractModel):
    """CreateCallBack返回参数结构体

    """

    def __init__(self):
        """
        :param CallId: 话单id
注意：此字段可能返回 null，表示取不到有效值。
        :type CallId: str
        :param SrcDisplayNum: 主叫显示系统分配的固话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcDisplayNum: str
        :param DstDisplayNum: 被叫显示系统分配的固话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type DstDisplayNum: str
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CallId = None
        self.SrcDisplayNum = None
        self.DstDisplayNum = None
        self.ErrorCode = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CallId = params.get("CallId")
        self.SrcDisplayNum = params.get("SrcDisplayNum")
        self.DstDisplayNum = params.get("DstDisplayNum")
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DelVirtualNumRequest(AbstractModel):
    """DelVirtualNum请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        :param BindId: 双方号码 + 中间号绑定 ID，该 ID 全局唯一
        :type BindId: str
        :param BizId: 应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节。
        :type BizId: str
        """
        self.BizAppId = None
        self.BindId = None
        self.BizId = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.BindId = params.get("BindId")
        self.BizId = params.get("BizId")


class DelVirtualNumResponse(AbstractModel):
    """DelVirtualNum返回参数结构体

    """

    def __init__(self):
        """
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param Msg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param BindId: 绑定 ID，该 ID 全局唯一
注意：此字段可能返回 null，表示取不到有效值。
        :type BindId: str
        :param RefLeftNum: 中间号还剩引用计数，如果计数为 0 会解绑
注意：此字段可能返回 null，表示取不到有效值。
        :type RefLeftNum: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.BindId = None
        self.RefLeftNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.BindId = params.get("BindId")
        self.RefLeftNum = params.get("RefLeftNum")
        self.RequestId = params.get("RequestId")


class DeleteCallBackRequest(AbstractModel):
    """DeleteCallBack请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        :param CallId: 回拨请求响应中返回的 callId
        :type CallId: str
        :param CancelFlag: 0：不管通话状态直接拆线（默认) 1：主叫响铃以后状态不拆线 2：主叫接听以后状态不拆线 3：被叫响铃以后状态不拆线 4：被叫接听以后状态不拆线
        :type CancelFlag: str
        """
        self.BizAppId = None
        self.CallId = None
        self.CancelFlag = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.CancelFlag = params.get("CancelFlag")


class DeleteCallBackResponse(AbstractModel):
    """DeleteCallBack返回参数结构体

    """

    def __init__(self):
        """
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param CallId: 话单id
注意：此字段可能返回 null，表示取不到有效值。
        :type CallId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.CallId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.CallId = params.get("CallId")
        self.RequestId = params.get("RequestId")


class DescribeCallBackCdrRequest(AbstractModel):
    """DescribeCallBackCdr请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        :param CallId: 回拨请求响应中返回的 callId，按 callId 查询该话单详细信息
        :type CallId: str
        :param Src: 查询主叫用户产生的呼叫话单，如填空表示拉取这个时间段所有话单
        :type Src: str
        :param StartTimeStamp: 话单开始时间戳
        :type StartTimeStamp: str
        :param EndTimeStamp: 话单结束时间戳
        :type EndTimeStamp: str
        """
        self.BizAppId = None
        self.CallId = None
        self.Src = None
        self.StartTimeStamp = None
        self.EndTimeStamp = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")


class DescribeCallBackCdrResponse(AbstractModel):
    """DescribeCallBackCdr返回参数结构体

    """

    def __init__(self):
        """
        :param Cdr: 话单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Cdr: list of CallBackCdr
        :param Offset: 偏移
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: str
        :param ErrorCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Cdr = None
        self.Offset = None
        self.ErrorCode = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cdr") is not None:
            self.Cdr = []
            for item in params.get("Cdr"):
                obj = CallBackCdr()
                obj._deserialize(item)
                self.Cdr.append(obj)
        self.Offset = params.get("Offset")
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeCallBackStatusRequest(AbstractModel):
    """DescribeCallBackStatus请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        :param CallId: 回拨请求响应中返回的 callId
        :type CallId: str
        :param Src: 主叫号码
        :type Src: str
        :param Dst: 被叫号码
        :type Dst: str
        :param CallStatus: 通话最后状态：0：未知状态 1：主叫响铃中 2：主叫接听 3：被叫响铃中 4：正常通话中 5：通话结束
        :type CallStatus: str
        """
        self.BizAppId = None
        self.CallId = None
        self.Src = None
        self.Dst = None
        self.CallStatus = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.CallStatus = params.get("CallStatus")


class DescribeCallBackStatusResponse(AbstractModel):
    """DescribeCallBackStatus返回参数结构体

    """

    def __init__(self):
        """
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param Msg: 错误信息
        :type Msg: str
        :param AppId: 业务appid
        :type AppId: str
        :param CallId: 回拨请求响应中返回的 callId
        :type CallId: str
        :param Src: 主叫号码
        :type Src: str
        :param Dst: 被叫号码
        :type Dst: str
        :param CallStatus: 通话最后状态：0：未知状态 1：主叫响铃中 2：主叫接听 3：被叫响铃中 4：正常通话中 5：通话结束
        :type CallStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.AppId = None
        self.CallId = None
        self.Src = None
        self.Dst = None
        self.CallStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.AppId = params.get("AppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.CallStatus = params.get("CallStatus")
        self.RequestId = params.get("RequestId")


class DescribeCallerDisplayListRequest(AbstractModel):
    """DescribeCallerDisplayList请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        """
        self.BizAppId = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")


class DescribeCallerDisplayListResponse(AbstractModel):
    """DescribeCallerDisplayList返回参数结构体

    """

    def __init__(self):
        """
        :param AppId: appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param CodeList: 主叫显号号码集合，codeList[0...*] 结构体数组，如果业务是主被叫互显，该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeList: list of CallBackPhoneCode
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.CodeList = None
        self.ErrorCode = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        if params.get("CodeList") is not None:
            self.CodeList = []
            for item in params.get("CodeList"):
                obj = CallBackPhoneCode()
                obj._deserialize(item)
                self.CodeList.append(obj)
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class Get400CdrRequest(AbstractModel):
    """Get400Cdr请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        :param CallId: 通话唯一标识 callId，即直拨呼叫响应中返回的 callId
        :type CallId: str
        :param Src: 查询主叫用户产生的呼叫话单（0086开头），设置为空表示拉取该时间段的所有话单
        :type Src: str
        :param StartTimeStamp: 话单开始时间戳
        :type StartTimeStamp: str
        :param EndTimeStamp: 话单结束时间戳
        :type EndTimeStamp: str
        """
        self.BizAppId = None
        self.CallId = None
        self.Src = None
        self.StartTimeStamp = None
        self.EndTimeStamp = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")


class Get400CdrResponse(AbstractModel):
    """Get400Cdr返回参数结构体

    """

    def __init__(self):
        """
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Offset: 偏移
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: str
        :param Cdr: 话单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Cdr: list of VirturalNumCdr
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.Offset = None
        self.Cdr = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.Offset = params.get("Offset")
        if params.get("Cdr") is not None:
            self.Cdr = []
            for item in params.get("Cdr"):
                obj = VirturalNumCdr()
                obj._deserialize(item)
                self.Cdr.append(obj)
        self.RequestId = params.get("RequestId")


class GetVirtualNumRequest(AbstractModel):
    """GetVirtualNum请求参数结构体

    """

    def __init__(self):
        """
        :param BizAppId: 业务appid
        :type BizAppId: str
        :param Dst: 被叫号码(号码前加 0086，如 008613631686024)
        :type Dst: str
        :param Src: 主叫号码(号码前加 0086，如 008613631686024)，xb 模式下是不用填写，axb 模式下是必选
        :type Src: str
        :param AccreditList: {“accreditList”:[“008613631686024”,”008612345678910”]}，主要用于 N-1 场景，号码绑定非共享是独占型，指定了 dst 独占中间号绑定，accreditList 表示这个列表成员可以拨打 dst 绑 定的中间号，默认值为空，表示所有号码都可以拨打独占型中间号绑定，最大集合不允许超过 30 个，仅适用于xb模式
        :type AccreditList: list of str
        :param AssignVirtualNum: 指定中间号（格式：008617013541251），如果该中间号已被使用则返回绑定失败。如果不带该字段则由腾讯侧从号码池里自动分配
        :type AssignVirtualNum: str
        :param Record: 是否录音，0表示不录音，1表示录音。默认为不录音，注意如果需要录音回调，通话完成后需要等待一段时间，收到录音回调之后，再解绑中间号。
        :type Record: str
        :param CityId: 主被叫显号号码归属地，指定该参数说明显号归属该城市，如果没有该城市号码会随机选取一个城市或者后台配置返回107，返回码详见 《腾讯-中间号-城市id.xlsx》
        :type CityId: str
        :param BizId: 应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节。
        :type BizId: str
        :param MaxAssignTime: 号码最大绑定时间，不填默认为 24 小时，最长绑定时间是168小时，单位秒
        :type MaxAssignTime: str
        :param StatusFlag: 主叫发起呼叫状态：1
被叫发起呼叫状态：256
主叫响铃状态：2
被叫响铃状态：512
主叫接听状态：4
被叫接听状态：1024
主叫拒绝接听状态：8
被叫拒绝接听状态：2048
主叫正常挂机状态：16
被叫正常挂机状态：4096
主叫呼叫异常：32
被叫呼叫异常：8192

例如：
值为 0：表示所有状态不需要推送
值为 4：表示只要推送主叫接听状态
值为 16191：表示所有状态都需要推送（上面所有值和）
        :type StatusFlag: str
        :param StatusUrl: 请填写statusFlag并设置值，状态回调通知地址，正式环境可以配置默认推送地址
        :type StatusUrl: str
        :param HangupUrl: 话单回调通知地址，正式环境可以配置默认推送地址
        :type HangupUrl: str
        :param RecordUrl: 录单 URL 回调通知地址，正式环境可以配置默认推送地址
        :type RecordUrl: str
        """
        self.BizAppId = None
        self.Dst = None
        self.Src = None
        self.AccreditList = None
        self.AssignVirtualNum = None
        self.Record = None
        self.CityId = None
        self.BizId = None
        self.MaxAssignTime = None
        self.StatusFlag = None
        self.StatusUrl = None
        self.HangupUrl = None
        self.RecordUrl = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.Dst = params.get("Dst")
        self.Src = params.get("Src")
        self.AccreditList = params.get("AccreditList")
        self.AssignVirtualNum = params.get("AssignVirtualNum")
        self.Record = params.get("Record")
        self.CityId = params.get("CityId")
        self.BizId = params.get("BizId")
        self.MaxAssignTime = params.get("MaxAssignTime")
        self.StatusFlag = params.get("StatusFlag")
        self.StatusUrl = params.get("StatusUrl")
        self.HangupUrl = params.get("HangupUrl")
        self.RecordUrl = params.get("RecordUrl")


class GetVirtualNumResponse(AbstractModel):
    """GetVirtualNum返回参数结构体

    """

    def __init__(self):
        """
        :param ErrorCode: 错误码
        :type ErrorCode: str
        :param BindId: 绑定 ID，该 ID 全局唯一
注意：此字段可能返回 null，表示取不到有效值。
        :type BindId: str
        :param RefNum: 中间号还剩引用计数，如果计数为 0 会解绑
注意：此字段可能返回 null，表示取不到有效值。
        :type RefNum: str
        :param VirtualNum: 中间号
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualNum: str
        :param Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.BindId = None
        self.RefNum = None
        self.VirtualNum = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.BindId = params.get("BindId")
        self.RefNum = params.get("RefNum")
        self.VirtualNum = params.get("VirtualNum")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class KeyList(AbstractModel):
    """对应按键操作,如果没有结构体里定义按键操作用户按键以后都从 interruptPrompt 重新播放

    """

    def __init__(self):
        """
        :param Key: 用户按键（0-9、*、#、A-D)
        :type Key: str
        :param Operate: 1: 呼通被叫 2：interruptPrompt 重播提示 3：拆线
        :type Operate: str
        """
        self.Key = None
        self.Operate = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operate = params.get("Operate")


class RreCallerHandle(AbstractModel):
    """结构体，主叫呼叫预处理操作，根据不同操作确认是否呼通被叫。如需使用，本结构体需要与 keyList 结构体配合使用，此时这两个参数都为必填项

    """

    def __init__(self):
        """
        :param ReadPrompt: 呼叫主叫以后，给主叫用户的语音提示，播放该提示时用户所有按键无效
        :type ReadPrompt: str
        :param InterruptPrompt: 可中断提示，播放该提示时，用户可以按键
        :type InterruptPrompt: str
        :param KeyList: 对应按键操作,如果没有结构体里定义按键操作用户按键以后都从 interruptPrompt 重新播放
        :type KeyList: list of KeyList
        :param RepeatTimes: 最多重复播放次数，超过该次数拆线
        :type RepeatTimes: str
        :param KeyPressUrl: 用户按键回调通知地址，如果为空不回调
        :type KeyPressUrl: str
        :param PromptGender: 提示音男声女声：1女声，2男声。默认女声
        :type PromptGender: str
        """
        self.ReadPrompt = None
        self.InterruptPrompt = None
        self.KeyList = None
        self.RepeatTimes = None
        self.KeyPressUrl = None
        self.PromptGender = None


    def _deserialize(self, params):
        self.ReadPrompt = params.get("ReadPrompt")
        self.InterruptPrompt = params.get("InterruptPrompt")
        if params.get("KeyList") is not None:
            self.KeyList = []
            for item in params.get("KeyList"):
                obj = KeyList()
                obj._deserialize(item)
                self.KeyList.append(obj)
        self.RepeatTimes = params.get("RepeatTimes")
        self.KeyPressUrl = params.get("KeyPressUrl")
        self.PromptGender = params.get("PromptGender")


class VirturalNumCdr(AbstractModel):
    """直拨话单详情

    """

    def __init__(self):
        """
        :param CallId: 呼叫通话 ID
        :type CallId: str
        :param BindId: 双方号码 + 中间号绑定 ID，该 ID 全局唯一
        :type BindId: str
        :param Src: 主叫号码
        :type Src: str
        :param Dst: 被叫号码
        :type Dst: str
        :param DstVirtualNum: 主叫通讯录直拨虚拟保护号码
        :type DstVirtualNum: str
        :param CallCenterAcceptTime: 虚拟保护号码平台收到呼叫时间
        :type CallCenterAcceptTime: str
        :param StartDstCallTime: 被叫呼叫开始时间
        :type StartDstCallTime: str
        :param StartDstRingTime: 被叫响铃开始时间
        :type StartDstRingTime: str
        :param DstAcceptTime: 被叫接听时间
        :type DstAcceptTime: str
        :param EndCallTime: 用户挂机通话结束时间
        :type EndCallTime: str
        :param CallEndStatus: 通话最后状态：0：未知状态 1：正常通话 2：查询呼叫转移被叫号异常 3：未接通 4：未接听 5：拒接挂断 6：关机 7：空号 8：通话中 9：欠费 10：运营商线路或平台异常
        :type CallEndStatus: str
        :param SrcDuration: 主叫接通虚拟保护号码到通话结束通话时间
        :type SrcDuration: str
        :param DstDuration: 呼叫转接被叫接通到通话结束通话时间
        :type DstDuration: str
        :param RecordUrl: 录音 URL，如果不录音或录音失败，该值为空
        :type RecordUrl: str
        """
        self.CallId = None
        self.BindId = None
        self.Src = None
        self.Dst = None
        self.DstVirtualNum = None
        self.CallCenterAcceptTime = None
        self.StartDstCallTime = None
        self.StartDstRingTime = None
        self.DstAcceptTime = None
        self.EndCallTime = None
        self.CallEndStatus = None
        self.SrcDuration = None
        self.DstDuration = None
        self.RecordUrl = None


    def _deserialize(self, params):
        self.CallId = params.get("CallId")
        self.BindId = params.get("BindId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.DstVirtualNum = params.get("DstVirtualNum")
        self.CallCenterAcceptTime = params.get("CallCenterAcceptTime")
        self.StartDstCallTime = params.get("StartDstCallTime")
        self.StartDstRingTime = params.get("StartDstRingTime")
        self.DstAcceptTime = params.get("DstAcceptTime")
        self.EndCallTime = params.get("EndCallTime")
        self.CallEndStatus = params.get("CallEndStatus")
        self.SrcDuration = params.get("SrcDuration")
        self.DstDuration = params.get("DstDuration")
        self.RecordUrl = params.get("RecordUrl")