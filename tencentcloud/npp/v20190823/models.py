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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CallBackCdr(AbstractModel):
    """话单详情

    """

    def __init__(self):
        r"""
        :param _CallId: 呼叫通话 ID
        :type CallId: str
        :param _Src: 主叫号码
        :type Src: str
        :param _Dst: 被叫号码
        :type Dst: str
        :param _StartSrcCallTime: 主叫呼叫开始时间
        :type StartSrcCallTime: str
        :param _StartSrcRingTime: 主叫响铃开始时间
        :type StartSrcRingTime: str
        :param _SrcAcceptTime: 主叫接听时间
        :type SrcAcceptTime: str
        :param _StartDstCallTime: 被叫呼叫开始时间
        :type StartDstCallTime: str
        :param _StartDstRingTime: 被叫响铃开始时间
        :type StartDstRingTime: str
        :param _DstAcceptTime: 被叫接听时间
        :type DstAcceptTime: str
        :param _EndCallTime: 用户挂机通话结束时间
        :type EndCallTime: str
        :param _CallEndStatus: 通话最后状态：0：未知状态 1：正常通话 2：主叫未接 3：主叫接听，被叫未接 4：主叫未接通 5：被叫未接通
        :type CallEndStatus: str
        :param _Duration: 通话计费时间
        :type Duration: str
        :param _RecordUrl: 录音 URL，如果不录音或录音失败，该值为空
        :type RecordUrl: str
        :param _CallType: 通话类型(1: VOIP 2:IP TO PSTN 3: PSTN TO PSTN)，如果话单中没有该字段，默认值为回拨 3 (PSTN TO PSTN)
注意：此字段可能返回 null，表示取不到有效值。
        :type CallType: str
        :param _BizId: 同回拨请求中的 bizId，如果回拨请求中带 bizId 会有该字段返回
注意：此字段可能返回 null，表示取不到有效值。
        :type BizId: str
        :param _OrderId: 订单 ID,最大长度不超过 64 个字节，对于一些有订单状态 App 相关应用（如达人帮接入 App 应用)，该字段只在帐单中带上，其它回调不附带该字段
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        """
        self._CallId = None
        self._Src = None
        self._Dst = None
        self._StartSrcCallTime = None
        self._StartSrcRingTime = None
        self._SrcAcceptTime = None
        self._StartDstCallTime = None
        self._StartDstRingTime = None
        self._DstAcceptTime = None
        self._EndCallTime = None
        self._CallEndStatus = None
        self._Duration = None
        self._RecordUrl = None
        self._CallType = None
        self._BizId = None
        self._OrderId = None

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Dst(self):
        return self._Dst

    @Dst.setter
    def Dst(self, Dst):
        self._Dst = Dst

    @property
    def StartSrcCallTime(self):
        return self._StartSrcCallTime

    @StartSrcCallTime.setter
    def StartSrcCallTime(self, StartSrcCallTime):
        self._StartSrcCallTime = StartSrcCallTime

    @property
    def StartSrcRingTime(self):
        return self._StartSrcRingTime

    @StartSrcRingTime.setter
    def StartSrcRingTime(self, StartSrcRingTime):
        self._StartSrcRingTime = StartSrcRingTime

    @property
    def SrcAcceptTime(self):
        return self._SrcAcceptTime

    @SrcAcceptTime.setter
    def SrcAcceptTime(self, SrcAcceptTime):
        self._SrcAcceptTime = SrcAcceptTime

    @property
    def StartDstCallTime(self):
        return self._StartDstCallTime

    @StartDstCallTime.setter
    def StartDstCallTime(self, StartDstCallTime):
        self._StartDstCallTime = StartDstCallTime

    @property
    def StartDstRingTime(self):
        return self._StartDstRingTime

    @StartDstRingTime.setter
    def StartDstRingTime(self, StartDstRingTime):
        self._StartDstRingTime = StartDstRingTime

    @property
    def DstAcceptTime(self):
        return self._DstAcceptTime

    @DstAcceptTime.setter
    def DstAcceptTime(self, DstAcceptTime):
        self._DstAcceptTime = DstAcceptTime

    @property
    def EndCallTime(self):
        return self._EndCallTime

    @EndCallTime.setter
    def EndCallTime(self, EndCallTime):
        self._EndCallTime = EndCallTime

    @property
    def CallEndStatus(self):
        return self._CallEndStatus

    @CallEndStatus.setter
    def CallEndStatus(self, CallEndStatus):
        self._CallEndStatus = CallEndStatus

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def CallType(self):
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._CallId = params.get("CallId")
        self._Src = params.get("Src")
        self._Dst = params.get("Dst")
        self._StartSrcCallTime = params.get("StartSrcCallTime")
        self._StartSrcRingTime = params.get("StartSrcRingTime")
        self._SrcAcceptTime = params.get("SrcAcceptTime")
        self._StartDstCallTime = params.get("StartDstCallTime")
        self._StartDstRingTime = params.get("StartDstRingTime")
        self._DstAcceptTime = params.get("DstAcceptTime")
        self._EndCallTime = params.get("EndCallTime")
        self._CallEndStatus = params.get("CallEndStatus")
        self._Duration = params.get("Duration")
        self._RecordUrl = params.get("RecordUrl")
        self._CallType = params.get("CallType")
        self._BizId = params.get("BizId")
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallBackPhoneCode(AbstractModel):
    """回拨号码字段

    """

    def __init__(self):
        r"""
        :param _Nation: 国家码，统一以 00 开头
        :type Nation: str
        :param _Phone: 号码（固话区号前加 0，如075586013388）
        :type Phone: str
        """
        self._Nation = None
        self._Phone = None

    @property
    def Nation(self):
        return self._Nation

    @Nation.setter
    def Nation(self, Nation):
        self._Nation = Nation

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone


    def _deserialize(self, params):
        self._Nation = params.get("Nation")
        self._Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCallBackRequest(AbstractModel):
    """CreateCallBack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        :param _Src: 主叫号码(必须为 11 位手机号，号码前加 0086，如 008613631686024)
        :type Src: str
        :param _Dst: 被叫号码(必须为 11 位手机或固话号码,号码前加 0086，如008613631686024，固话如：0086075586013388)
        :type Dst: str
        :param _SrcDisplayNum: 主叫显示系统分配的固话号码，如不填显示随机分配号码
        :type SrcDisplayNum: str
        :param _DstDisplayNum: 被叫显示系统分配的固话号码，如不填显示随机分配号码
        :type DstDisplayNum: str
        :param _Record: 是否录音，0 表示不录音，1 表示录音。默认为不录音
        :type Record: str
        :param _MaxAllowTime: 允许最大通话时间，不填默认为 30 分钟（单位：分钟）
        :type MaxAllowTime: str
        :param _StatusFlag: 主叫发起呼叫状态：1 被叫发起呼叫状态：256 主叫响铃状态：2 被叫响铃状态：512 主叫接听状态：4 被叫接听状态：1024 主叫拒绝接听状态：8 被叫拒绝接听状态：2048 主叫正常挂机状态：16 被叫正常挂机状态：4096 主叫呼叫异常：32 被叫呼叫异常：8192
例如：当值为 0：表示所有状态不需要推送；当值为 4：表示只要推送主叫接听状态；当值为 16191：表示所有状态都需要推送(上面所有值和)
        :type StatusFlag: str
        :param _StatusUrl: 状态回调通知地址，正式环境可以配置默认推送地址
        :type StatusUrl: str
        :param _HangupUrl: 话单回调通知地址，正式环境可以配置默认推送地址
        :type HangupUrl: str
        :param _RecordUrl: 录单 URL 回调通知地址，正式环境可以配置默认推送地址
        :type RecordUrl: str
        :param _BizId: 业务应用 key，业务用该 key 可以区分内部业务或客户产品等，该 key 需保证在该 appId 下全局唯一，最大长度不超过 64 个字节，bizId 只能包含数字、字母。
        :type BizId: str
        :param _LastCallId: 最后一次呼叫 callId，带上该字段以后，平台会参考该 callId 分配线路，优先不分配该 callId 通话线路（注：谨慎使用，这个会影响线路调度）
        :type LastCallId: str
        :param _PreCallerHandle: 结构体，主叫呼叫预处理操作，根据不同操作确认是否呼通被叫。如需使用，本结构体需要与 keyList 结构体配合使用，此时这两个参数都为必填项
        :type PreCallerHandle: :class:`tencentcloud.npp.v20190823.models.RreCallerHandle`
        :param _OrderId: 订单 ID，最大长度不超过64个字节，对于一些有订单状态 App 相关应用使用（如达人帮接入 App 应用)，该字段只在帐单中带上，其它回调不附带该字段
        :type OrderId: str
        """
        self._BizAppId = None
        self._Src = None
        self._Dst = None
        self._SrcDisplayNum = None
        self._DstDisplayNum = None
        self._Record = None
        self._MaxAllowTime = None
        self._StatusFlag = None
        self._StatusUrl = None
        self._HangupUrl = None
        self._RecordUrl = None
        self._BizId = None
        self._LastCallId = None
        self._PreCallerHandle = None
        self._OrderId = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Dst(self):
        return self._Dst

    @Dst.setter
    def Dst(self, Dst):
        self._Dst = Dst

    @property
    def SrcDisplayNum(self):
        return self._SrcDisplayNum

    @SrcDisplayNum.setter
    def SrcDisplayNum(self, SrcDisplayNum):
        self._SrcDisplayNum = SrcDisplayNum

    @property
    def DstDisplayNum(self):
        return self._DstDisplayNum

    @DstDisplayNum.setter
    def DstDisplayNum(self, DstDisplayNum):
        self._DstDisplayNum = DstDisplayNum

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def MaxAllowTime(self):
        return self._MaxAllowTime

    @MaxAllowTime.setter
    def MaxAllowTime(self, MaxAllowTime):
        self._MaxAllowTime = MaxAllowTime

    @property
    def StatusFlag(self):
        return self._StatusFlag

    @StatusFlag.setter
    def StatusFlag(self, StatusFlag):
        self._StatusFlag = StatusFlag

    @property
    def StatusUrl(self):
        return self._StatusUrl

    @StatusUrl.setter
    def StatusUrl(self, StatusUrl):
        self._StatusUrl = StatusUrl

    @property
    def HangupUrl(self):
        return self._HangupUrl

    @HangupUrl.setter
    def HangupUrl(self, HangupUrl):
        self._HangupUrl = HangupUrl

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def LastCallId(self):
        return self._LastCallId

    @LastCallId.setter
    def LastCallId(self, LastCallId):
        self._LastCallId = LastCallId

    @property
    def PreCallerHandle(self):
        return self._PreCallerHandle

    @PreCallerHandle.setter
    def PreCallerHandle(self, PreCallerHandle):
        self._PreCallerHandle = PreCallerHandle

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        self._Src = params.get("Src")
        self._Dst = params.get("Dst")
        self._SrcDisplayNum = params.get("SrcDisplayNum")
        self._DstDisplayNum = params.get("DstDisplayNum")
        self._Record = params.get("Record")
        self._MaxAllowTime = params.get("MaxAllowTime")
        self._StatusFlag = params.get("StatusFlag")
        self._StatusUrl = params.get("StatusUrl")
        self._HangupUrl = params.get("HangupUrl")
        self._RecordUrl = params.get("RecordUrl")
        self._BizId = params.get("BizId")
        self._LastCallId = params.get("LastCallId")
        if params.get("PreCallerHandle") is not None:
            self._PreCallerHandle = RreCallerHandle()
            self._PreCallerHandle._deserialize(params.get("PreCallerHandle"))
        self._OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCallBackResponse(AbstractModel):
    """CreateCallBack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CallId: 话单id
注意：此字段可能返回 null，表示取不到有效值。
        :type CallId: str
        :param _SrcDisplayNum: 主叫显示系统分配的固话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcDisplayNum: str
        :param _DstDisplayNum: 被叫显示系统分配的固话号码
注意：此字段可能返回 null，表示取不到有效值。
        :type DstDisplayNum: str
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CallId = None
        self._SrcDisplayNum = None
        self._DstDisplayNum = None
        self._ErrorCode = None
        self._Msg = None
        self._RequestId = None

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def SrcDisplayNum(self):
        return self._SrcDisplayNum

    @SrcDisplayNum.setter
    def SrcDisplayNum(self, SrcDisplayNum):
        self._SrcDisplayNum = SrcDisplayNum

    @property
    def DstDisplayNum(self):
        return self._DstDisplayNum

    @DstDisplayNum.setter
    def DstDisplayNum(self, DstDisplayNum):
        self._DstDisplayNum = DstDisplayNum

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CallId = params.get("CallId")
        self._SrcDisplayNum = params.get("SrcDisplayNum")
        self._DstDisplayNum = params.get("DstDisplayNum")
        self._ErrorCode = params.get("ErrorCode")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DelVirtualNumRequest(AbstractModel):
    """DelVirtualNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        :param _BindId: 双方号码 + 中间号绑定 ID，该 ID 全局唯一
        :type BindId: str
        :param _BizId: 应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节。
        :type BizId: str
        """
        self._BizAppId = None
        self._BindId = None
        self._BizId = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId

    @property
    def BindId(self):
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        self._BindId = params.get("BindId")
        self._BizId = params.get("BizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DelVirtualNumResponse(AbstractModel):
    """DelVirtualNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _Msg: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _BindId: 绑定 ID，该 ID 全局唯一
注意：此字段可能返回 null，表示取不到有效值。
        :type BindId: str
        :param _RefLeftNum: 中间号还剩引用计数，如果计数为 0 会解绑
注意：此字段可能返回 null，表示取不到有效值。
        :type RefLeftNum: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._Msg = None
        self._BindId = None
        self._RefLeftNum = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def BindId(self):
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def RefLeftNum(self):
        return self._RefLeftNum

    @RefLeftNum.setter
    def RefLeftNum(self, RefLeftNum):
        self._RefLeftNum = RefLeftNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._Msg = params.get("Msg")
        self._BindId = params.get("BindId")
        self._RefLeftNum = params.get("RefLeftNum")
        self._RequestId = params.get("RequestId")


class DeleteCallBackRequest(AbstractModel):
    """DeleteCallBack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        :param _CallId: 回拨请求响应中返回的 callId
        :type CallId: str
        :param _CancelFlag: 0：不管通话状态直接拆线（默认) 1：主叫响铃以后状态不拆线 2：主叫接听以后状态不拆线 3：被叫响铃以后状态不拆线 4：被叫接听以后状态不拆线
        :type CancelFlag: str
        """
        self._BizAppId = None
        self._CallId = None
        self._CancelFlag = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def CancelFlag(self):
        return self._CancelFlag

    @CancelFlag.setter
    def CancelFlag(self, CancelFlag):
        self._CancelFlag = CancelFlag


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        self._CallId = params.get("CallId")
        self._CancelFlag = params.get("CancelFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCallBackResponse(AbstractModel):
    """DeleteCallBack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _CallId: 话单id
注意：此字段可能返回 null，表示取不到有效值。
        :type CallId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._Msg = None
        self._CallId = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._Msg = params.get("Msg")
        self._CallId = params.get("CallId")
        self._RequestId = params.get("RequestId")


class DescribeCallBackCdrRequest(AbstractModel):
    """DescribeCallBackCdr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        :param _CallId: 回拨请求响应中返回的 callId，按 callId 查询该话单详细信息
        :type CallId: str
        :param _Src: 查询主叫用户产生的呼叫话单，如填空表示拉取这个时间段所有话单
        :type Src: str
        :param _StartTimeStamp: 话单开始时间戳
        :type StartTimeStamp: str
        :param _EndTimeStamp: 话单结束时间戳
        :type EndTimeStamp: str
        """
        self._BizAppId = None
        self._CallId = None
        self._Src = None
        self._StartTimeStamp = None
        self._EndTimeStamp = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def StartTimeStamp(self):
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        self._CallId = params.get("CallId")
        self._Src = params.get("Src")
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallBackCdrResponse(AbstractModel):
    """DescribeCallBackCdr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Cdr: 话单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Cdr: list of CallBackCdr
        :param _Offset: 偏移
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: str
        :param _ErrorCode: 错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param _Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Cdr = None
        self._Offset = None
        self._ErrorCode = None
        self._Msg = None
        self._RequestId = None

    @property
    def Cdr(self):
        return self._Cdr

    @Cdr.setter
    def Cdr(self, Cdr):
        self._Cdr = Cdr

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Cdr") is not None:
            self._Cdr = []
            for item in params.get("Cdr"):
                obj = CallBackCdr()
                obj._deserialize(item)
                self._Cdr.append(obj)
        self._Offset = params.get("Offset")
        self._ErrorCode = params.get("ErrorCode")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeCallBackStatusRequest(AbstractModel):
    """DescribeCallBackStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        :param _CallId: 回拨请求响应中返回的 callId
        :type CallId: str
        :param _Src: 主叫号码
        :type Src: str
        :param _Dst: 被叫号码
        :type Dst: str
        :param _CallStatus: 通话最后状态：0：未知状态 1：主叫响铃中 2：主叫接听 3：被叫响铃中 4：正常通话中 5：通话结束
        :type CallStatus: str
        """
        self._BizAppId = None
        self._CallId = None
        self._Src = None
        self._Dst = None
        self._CallStatus = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Dst(self):
        return self._Dst

    @Dst.setter
    def Dst(self, Dst):
        self._Dst = Dst

    @property
    def CallStatus(self):
        return self._CallStatus

    @CallStatus.setter
    def CallStatus(self, CallStatus):
        self._CallStatus = CallStatus


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        self._CallId = params.get("CallId")
        self._Src = params.get("Src")
        self._Dst = params.get("Dst")
        self._CallStatus = params.get("CallStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallBackStatusResponse(AbstractModel):
    """DescribeCallBackStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _Msg: 错误信息
        :type Msg: str
        :param _AppId: 业务appid
        :type AppId: str
        :param _CallId: 回拨请求响应中返回的 callId
        :type CallId: str
        :param _Src: 主叫号码
        :type Src: str
        :param _Dst: 被叫号码
        :type Dst: str
        :param _CallStatus: 通话最后状态：0：未知状态 1：主叫响铃中 2：主叫接听 3：被叫响铃中 4：正常通话中 5：通话结束
        :type CallStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._Msg = None
        self._AppId = None
        self._CallId = None
        self._Src = None
        self._Dst = None
        self._CallStatus = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Dst(self):
        return self._Dst

    @Dst.setter
    def Dst(self, Dst):
        self._Dst = Dst

    @property
    def CallStatus(self):
        return self._CallStatus

    @CallStatus.setter
    def CallStatus(self, CallStatus):
        self._CallStatus = CallStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._Msg = params.get("Msg")
        self._AppId = params.get("AppId")
        self._CallId = params.get("CallId")
        self._Src = params.get("Src")
        self._Dst = params.get("Dst")
        self._CallStatus = params.get("CallStatus")
        self._RequestId = params.get("RequestId")


class DescribeCallerDisplayListRequest(AbstractModel):
    """DescribeCallerDisplayList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        """
        self._BizAppId = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallerDisplayListResponse(AbstractModel):
    """DescribeCallerDisplayList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _CodeList: 主叫显号号码集合，codeList[0...*] 结构体数组，如果业务是主被叫互显，该字段为空
注意：此字段可能返回 null，表示取不到有效值。
        :type CodeList: list of CallBackPhoneCode
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._CodeList = None
        self._ErrorCode = None
        self._Msg = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CodeList(self):
        return self._CodeList

    @CodeList.setter
    def CodeList(self, CodeList):
        self._CodeList = CodeList

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("CodeList") is not None:
            self._CodeList = []
            for item in params.get("CodeList"):
                obj = CallBackPhoneCode()
                obj._deserialize(item)
                self._CodeList.append(obj)
        self._ErrorCode = params.get("ErrorCode")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class Get400CdrRequest(AbstractModel):
    """Get400Cdr请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        :param _CallId: 通话唯一标识 callId，即直拨呼叫响应中返回的 callId
        :type CallId: str
        :param _Src: 查询主叫用户产生的呼叫话单（0086开头），设置为空表示拉取该时间段的所有话单
        :type Src: str
        :param _StartTimeStamp: 话单开始时间戳
        :type StartTimeStamp: str
        :param _EndTimeStamp: 话单结束时间戳
        :type EndTimeStamp: str
        """
        self._BizAppId = None
        self._CallId = None
        self._Src = None
        self._StartTimeStamp = None
        self._EndTimeStamp = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def StartTimeStamp(self):
        return self._StartTimeStamp

    @StartTimeStamp.setter
    def StartTimeStamp(self, StartTimeStamp):
        self._StartTimeStamp = StartTimeStamp

    @property
    def EndTimeStamp(self):
        return self._EndTimeStamp

    @EndTimeStamp.setter
    def EndTimeStamp(self, EndTimeStamp):
        self._EndTimeStamp = EndTimeStamp


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        self._CallId = params.get("CallId")
        self._Src = params.get("Src")
        self._StartTimeStamp = params.get("StartTimeStamp")
        self._EndTimeStamp = params.get("EndTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Get400CdrResponse(AbstractModel):
    """Get400Cdr返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Offset: 偏移
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: str
        :param _Cdr: 话单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Cdr: list of VirturalNumCdr
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._Msg = None
        self._Offset = None
        self._Cdr = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Cdr(self):
        return self._Cdr

    @Cdr.setter
    def Cdr(self, Cdr):
        self._Cdr = Cdr

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._Msg = params.get("Msg")
        self._Offset = params.get("Offset")
        if params.get("Cdr") is not None:
            self._Cdr = []
            for item in params.get("Cdr"):
                obj = VirturalNumCdr()
                obj._deserialize(item)
                self._Cdr.append(obj)
        self._RequestId = params.get("RequestId")


class GetVirtualNumRequest(AbstractModel):
    """GetVirtualNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizAppId: 业务appid
        :type BizAppId: str
        :param _Dst: 被叫号码(号码前加 0086，如 008613631686024)
        :type Dst: str
        :param _Src: 主叫号码(号码前加 0086，如 008613631686024)，xb 模式下是不用填写，axb 模式下是必选
        :type Src: str
        :param _AccreditList: {“accreditList”:[“008613631686024”,”008612345678910”]}，主要用于 N-1 场景，号码绑定非共享是独占型，指定了 dst 独占中间号绑定，accreditList 表示这个列表成员可以拨打 dst 绑 定的中间号，默认值为空，表示所有号码都可以拨打独占型中间号绑定，最大集合不允许超过 30 个，仅适用于xb模式
        :type AccreditList: list of str
        :param _AssignVirtualNum: 指定中间号（格式：008617013541251），如果该中间号已被使用则返回绑定失败。如果不带该字段则由腾讯侧从号码池里自动分配
        :type AssignVirtualNum: str
        :param _Record: 是否录音，0表示不录音，1表示录音。默认为不录音，注意如果需要录音回调，通话完成后需要等待一段时间，收到录音回调之后，再解绑中间号。
        :type Record: str
        :param _CityId: 主被叫显号号码归属地，指定该参数说明显号归属该城市，如果没有该城市号码会随机选取一个城市或者后台配置返回107，返回码详见 《腾讯-中间号-城市id.xlsx》
        :type CityId: str
        :param _BizId: 应用二级业务 ID，bizId 需保证在该 appId 下全局唯一，最大长度不超过 16 个字节。
        :type BizId: str
        :param _MaxAssignTime: 号码最大绑定时间，不填默认为 24 小时，最长绑定时间是168小时，单位秒
        :type MaxAssignTime: str
        :param _StatusFlag: 主叫发起呼叫状态：1
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
        :param _StatusUrl: 请填写statusFlag并设置值，状态回调通知地址，正式环境可以配置默认推送地址
        :type StatusUrl: str
        :param _HangupUrl: 话单回调通知地址，正式环境可以配置默认推送地址
        :type HangupUrl: str
        :param _RecordUrl: 录单 URL 回调通知地址，正式环境可以配置默认推送地址
        :type RecordUrl: str
        """
        self._BizAppId = None
        self._Dst = None
        self._Src = None
        self._AccreditList = None
        self._AssignVirtualNum = None
        self._Record = None
        self._CityId = None
        self._BizId = None
        self._MaxAssignTime = None
        self._StatusFlag = None
        self._StatusUrl = None
        self._HangupUrl = None
        self._RecordUrl = None

    @property
    def BizAppId(self):
        return self._BizAppId

    @BizAppId.setter
    def BizAppId(self, BizAppId):
        self._BizAppId = BizAppId

    @property
    def Dst(self):
        return self._Dst

    @Dst.setter
    def Dst(self, Dst):
        self._Dst = Dst

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def AccreditList(self):
        return self._AccreditList

    @AccreditList.setter
    def AccreditList(self, AccreditList):
        self._AccreditList = AccreditList

    @property
    def AssignVirtualNum(self):
        return self._AssignVirtualNum

    @AssignVirtualNum.setter
    def AssignVirtualNum(self, AssignVirtualNum):
        self._AssignVirtualNum = AssignVirtualNum

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def CityId(self):
        return self._CityId

    @CityId.setter
    def CityId(self, CityId):
        self._CityId = CityId

    @property
    def BizId(self):
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def MaxAssignTime(self):
        return self._MaxAssignTime

    @MaxAssignTime.setter
    def MaxAssignTime(self, MaxAssignTime):
        self._MaxAssignTime = MaxAssignTime

    @property
    def StatusFlag(self):
        return self._StatusFlag

    @StatusFlag.setter
    def StatusFlag(self, StatusFlag):
        self._StatusFlag = StatusFlag

    @property
    def StatusUrl(self):
        return self._StatusUrl

    @StatusUrl.setter
    def StatusUrl(self, StatusUrl):
        self._StatusUrl = StatusUrl

    @property
    def HangupUrl(self):
        return self._HangupUrl

    @HangupUrl.setter
    def HangupUrl(self, HangupUrl):
        self._HangupUrl = HangupUrl

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl


    def _deserialize(self, params):
        self._BizAppId = params.get("BizAppId")
        self._Dst = params.get("Dst")
        self._Src = params.get("Src")
        self._AccreditList = params.get("AccreditList")
        self._AssignVirtualNum = params.get("AssignVirtualNum")
        self._Record = params.get("Record")
        self._CityId = params.get("CityId")
        self._BizId = params.get("BizId")
        self._MaxAssignTime = params.get("MaxAssignTime")
        self._StatusFlag = params.get("StatusFlag")
        self._StatusUrl = params.get("StatusUrl")
        self._HangupUrl = params.get("HangupUrl")
        self._RecordUrl = params.get("RecordUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetVirtualNumResponse(AbstractModel):
    """GetVirtualNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _BindId: 绑定 ID，该 ID 全局唯一
注意：此字段可能返回 null，表示取不到有效值。
        :type BindId: str
        :param _RefNum: 中间号还剩引用计数，如果计数为 0 会解绑
注意：此字段可能返回 null，表示取不到有效值。
        :type RefNum: str
        :param _VirtualNum: 中间号
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualNum: str
        :param _Msg: 错误原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorCode = None
        self._BindId = None
        self._RefNum = None
        self._VirtualNum = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def BindId(self):
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def RefNum(self):
        return self._RefNum

    @RefNum.setter
    def RefNum(self, RefNum):
        self._RefNum = RefNum

    @property
    def VirtualNum(self):
        return self._VirtualNum

    @VirtualNum.setter
    def VirtualNum(self, VirtualNum):
        self._VirtualNum = VirtualNum

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorCode = params.get("ErrorCode")
        self._BindId = params.get("BindId")
        self._RefNum = params.get("RefNum")
        self._VirtualNum = params.get("VirtualNum")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class KeyList(AbstractModel):
    """对应按键操作,如果没有结构体里定义按键操作用户按键以后都从 interruptPrompt 重新播放

    """

    def __init__(self):
        r"""
        :param _Key: 用户按键（0-9、*、#、A-D)
        :type Key: str
        :param _Operate: 1: 呼通被叫 2：interruptPrompt 重播提示 3：拆线
        :type Operate: str
        """
        self._Key = None
        self._Operate = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RreCallerHandle(AbstractModel):
    """结构体，主叫呼叫预处理操作，根据不同操作确认是否呼通被叫。如需使用，本结构体需要与 keyList 结构体配合使用，此时这两个参数都为必填项

    """

    def __init__(self):
        r"""
        :param _ReadPrompt: 呼叫主叫以后，给主叫用户的语音提示，播放该提示时用户所有按键无效
        :type ReadPrompt: str
        :param _InterruptPrompt: 可中断提示，播放该提示时，用户可以按键
        :type InterruptPrompt: str
        :param _KeyList: 对应按键操作,如果没有结构体里定义按键操作用户按键以后都从 interruptPrompt 重新播放
        :type KeyList: list of KeyList
        :param _RepeatTimes: 最多重复播放次数，超过该次数拆线
        :type RepeatTimes: str
        :param _KeyPressUrl: 用户按键回调通知地址，如果为空不回调
        :type KeyPressUrl: str
        :param _PromptGender: 提示音男声女声：1女声，2男声。默认女声
        :type PromptGender: str
        """
        self._ReadPrompt = None
        self._InterruptPrompt = None
        self._KeyList = None
        self._RepeatTimes = None
        self._KeyPressUrl = None
        self._PromptGender = None

    @property
    def ReadPrompt(self):
        return self._ReadPrompt

    @ReadPrompt.setter
    def ReadPrompt(self, ReadPrompt):
        self._ReadPrompt = ReadPrompt

    @property
    def InterruptPrompt(self):
        return self._InterruptPrompt

    @InterruptPrompt.setter
    def InterruptPrompt(self, InterruptPrompt):
        self._InterruptPrompt = InterruptPrompt

    @property
    def KeyList(self):
        return self._KeyList

    @KeyList.setter
    def KeyList(self, KeyList):
        self._KeyList = KeyList

    @property
    def RepeatTimes(self):
        return self._RepeatTimes

    @RepeatTimes.setter
    def RepeatTimes(self, RepeatTimes):
        self._RepeatTimes = RepeatTimes

    @property
    def KeyPressUrl(self):
        return self._KeyPressUrl

    @KeyPressUrl.setter
    def KeyPressUrl(self, KeyPressUrl):
        self._KeyPressUrl = KeyPressUrl

    @property
    def PromptGender(self):
        return self._PromptGender

    @PromptGender.setter
    def PromptGender(self, PromptGender):
        self._PromptGender = PromptGender


    def _deserialize(self, params):
        self._ReadPrompt = params.get("ReadPrompt")
        self._InterruptPrompt = params.get("InterruptPrompt")
        if params.get("KeyList") is not None:
            self._KeyList = []
            for item in params.get("KeyList"):
                obj = KeyList()
                obj._deserialize(item)
                self._KeyList.append(obj)
        self._RepeatTimes = params.get("RepeatTimes")
        self._KeyPressUrl = params.get("KeyPressUrl")
        self._PromptGender = params.get("PromptGender")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirturalNumCdr(AbstractModel):
    """直拨话单详情

    """

    def __init__(self):
        r"""
        :param _CallId: 呼叫通话 ID
        :type CallId: str
        :param _BindId: 双方号码 + 中间号绑定 ID，该 ID 全局唯一
        :type BindId: str
        :param _Src: 主叫号码
        :type Src: str
        :param _Dst: 被叫号码
        :type Dst: str
        :param _DstVirtualNum: 主叫通讯录直拨虚拟保护号码
        :type DstVirtualNum: str
        :param _CallCenterAcceptTime: 虚拟保护号码平台收到呼叫时间
        :type CallCenterAcceptTime: str
        :param _StartDstCallTime: 被叫呼叫开始时间
        :type StartDstCallTime: str
        :param _StartDstRingTime: 被叫响铃开始时间
        :type StartDstRingTime: str
        :param _DstAcceptTime: 被叫接听时间
        :type DstAcceptTime: str
        :param _EndCallTime: 用户挂机通话结束时间
        :type EndCallTime: str
        :param _CallEndStatus: 通话最后状态：0：未知状态 1：正常通话 2：查询呼叫转移被叫号异常 3：未接通 4：未接听 5：拒接挂断 6：关机 7：空号 8：通话中 9：欠费 10：运营商线路或平台异常
        :type CallEndStatus: str
        :param _SrcDuration: 主叫接通虚拟保护号码到通话结束通话时间
        :type SrcDuration: str
        :param _DstDuration: 呼叫转接被叫接通到通话结束通话时间
        :type DstDuration: str
        :param _RecordUrl: 录音 URL，如果不录音或录音失败，该值为空
        :type RecordUrl: str
        """
        self._CallId = None
        self._BindId = None
        self._Src = None
        self._Dst = None
        self._DstVirtualNum = None
        self._CallCenterAcceptTime = None
        self._StartDstCallTime = None
        self._StartDstRingTime = None
        self._DstAcceptTime = None
        self._EndCallTime = None
        self._CallEndStatus = None
        self._SrcDuration = None
        self._DstDuration = None
        self._RecordUrl = None

    @property
    def CallId(self):
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def BindId(self):
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def Src(self):
        return self._Src

    @Src.setter
    def Src(self, Src):
        self._Src = Src

    @property
    def Dst(self):
        return self._Dst

    @Dst.setter
    def Dst(self, Dst):
        self._Dst = Dst

    @property
    def DstVirtualNum(self):
        return self._DstVirtualNum

    @DstVirtualNum.setter
    def DstVirtualNum(self, DstVirtualNum):
        self._DstVirtualNum = DstVirtualNum

    @property
    def CallCenterAcceptTime(self):
        return self._CallCenterAcceptTime

    @CallCenterAcceptTime.setter
    def CallCenterAcceptTime(self, CallCenterAcceptTime):
        self._CallCenterAcceptTime = CallCenterAcceptTime

    @property
    def StartDstCallTime(self):
        return self._StartDstCallTime

    @StartDstCallTime.setter
    def StartDstCallTime(self, StartDstCallTime):
        self._StartDstCallTime = StartDstCallTime

    @property
    def StartDstRingTime(self):
        return self._StartDstRingTime

    @StartDstRingTime.setter
    def StartDstRingTime(self, StartDstRingTime):
        self._StartDstRingTime = StartDstRingTime

    @property
    def DstAcceptTime(self):
        return self._DstAcceptTime

    @DstAcceptTime.setter
    def DstAcceptTime(self, DstAcceptTime):
        self._DstAcceptTime = DstAcceptTime

    @property
    def EndCallTime(self):
        return self._EndCallTime

    @EndCallTime.setter
    def EndCallTime(self, EndCallTime):
        self._EndCallTime = EndCallTime

    @property
    def CallEndStatus(self):
        return self._CallEndStatus

    @CallEndStatus.setter
    def CallEndStatus(self, CallEndStatus):
        self._CallEndStatus = CallEndStatus

    @property
    def SrcDuration(self):
        return self._SrcDuration

    @SrcDuration.setter
    def SrcDuration(self, SrcDuration):
        self._SrcDuration = SrcDuration

    @property
    def DstDuration(self):
        return self._DstDuration

    @DstDuration.setter
    def DstDuration(self, DstDuration):
        self._DstDuration = DstDuration

    @property
    def RecordUrl(self):
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl


    def _deserialize(self, params):
        self._CallId = params.get("CallId")
        self._BindId = params.get("BindId")
        self._Src = params.get("Src")
        self._Dst = params.get("Dst")
        self._DstVirtualNum = params.get("DstVirtualNum")
        self._CallCenterAcceptTime = params.get("CallCenterAcceptTime")
        self._StartDstCallTime = params.get("StartDstCallTime")
        self._StartDstRingTime = params.get("StartDstRingTime")
        self._DstAcceptTime = params.get("DstAcceptTime")
        self._EndCallTime = params.get("EndCallTime")
        self._CallEndStatus = params.get("CallEndStatus")
        self._SrcDuration = params.get("SrcDuration")
        self._DstDuration = params.get("DstDuration")
        self._RecordUrl = params.get("RecordUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        