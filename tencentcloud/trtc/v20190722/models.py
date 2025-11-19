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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AbnormalEvent(AbstractModel):
    r"""造成异常体验可能的异常事件类型

    """

    def __init__(self):
        r"""
        :param _AbnormalEventId: 异常事件ID，具体值查看附录：异常体验ID映射表：https://cloud.tencent.com/document/product/647/44916
        :type AbnormalEventId: int
        :param _PeerId: 远端用户ID,""：表示异常事件不是由远端用户产生
        :type PeerId: str
        """
        self._AbnormalEventId = None
        self._PeerId = None

    @property
    def AbnormalEventId(self):
        r"""异常事件ID，具体值查看附录：异常体验ID映射表：https://cloud.tencent.com/document/product/647/44916
        :rtype: int
        """
        return self._AbnormalEventId

    @AbnormalEventId.setter
    def AbnormalEventId(self, AbnormalEventId):
        self._AbnormalEventId = AbnormalEventId

    @property
    def PeerId(self):
        r"""远端用户ID,""：表示异常事件不是由远端用户产生
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId


    def _deserialize(self, params):
        self._AbnormalEventId = params.get("AbnormalEventId")
        self._PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalExperience(AbstractModel):
    r"""用户的异常体验及可能的原因

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _ExperienceId: 异常体验ID
        :type ExperienceId: int
        :param _RoomId: 字符串房间号
        :type RoomId: str
        :param _AbnormalEventList: 异常事件数组
        :type AbnormalEventList: list of AbnormalEvent
        :param _EventTime: 异常事件的上报时间
        :type EventTime: int
        """
        self._UserId = None
        self._ExperienceId = None
        self._RoomId = None
        self._AbnormalEventList = None
        self._EventTime = None

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ExperienceId(self):
        r"""异常体验ID
        :rtype: int
        """
        return self._ExperienceId

    @ExperienceId.setter
    def ExperienceId(self, ExperienceId):
        self._ExperienceId = ExperienceId

    @property
    def RoomId(self):
        r"""字符串房间号
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def AbnormalEventList(self):
        r"""异常事件数组
        :rtype: list of AbnormalEvent
        """
        return self._AbnormalEventList

    @AbnormalEventList.setter
    def AbnormalEventList(self, AbnormalEventList):
        self._AbnormalEventList = AbnormalEventList

    @property
    def EventTime(self):
        r"""异常事件的上报时间
        :rtype: int
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._ExperienceId = params.get("ExperienceId")
        self._RoomId = params.get("RoomId")
        if params.get("AbnormalEventList") is not None:
            self._AbnormalEventList = []
            for item in params.get("AbnormalEventList"):
                obj = AbnormalEvent()
                obj._deserialize(item)
                self._AbnormalEventList.append(obj)
        self._EventTime = params.get("EventTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentConfig(AbstractModel):
    r"""机器人参数

    """

    def __init__(self):
        r"""
        :param _UserId: 机器人的UserId，用于进房发起任务。【注意】这个UserId不能与当前房间内的主播观众[UserId](https://cloud.tencent.com/document/product/647/46351#userid)重复。如果一个房间发起多个任务时，机器人的UserId也不能相互重复，否则会中断前一个任务。需要保证机器人UserId在房间内唯一。
        :type UserId: str
        :param _UserSig: 机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :type UserSig: str
        :param _TargetUserId: 机器人拉流的UserId, 填写后，机器人会拉取该UserId的流进行实时处理
        :type TargetUserId: str
        :param _MaxIdleTime: 房间内超过MaxIdleTime 没有推流，后台自动关闭任务，默认值是60s。
        :type MaxIdleTime: int
        :param _WelcomeMessage: 机器人的欢迎语
        :type WelcomeMessage: str
        :param _InterruptMode: 智能打断模式，默认为0，0表示服务端自动打断，1表示服务端不打断，由端上发送打断信令进行打断
        :type InterruptMode: int
        :param _InterruptSpeechDuration: InterruptMode为0时使用，单位为毫秒，默认为500ms。表示服务端检测到持续InterruptSpeechDuration毫秒的人声则进行打断。
        :type InterruptSpeechDuration: int
        :param _TurnDetectionMode: 控制新一轮对话的触发方式，默认为0。
- 0表示当服务端语音识别检测出的完整一句话后，自动触发一轮新的对话。
- 1表示客户端在收到字幕消息后，自行决定是否手动发送聊天信令触发一轮新的对话。
        :type TurnDetectionMode: int
        :param _FilterOneWord: 是否过滤掉用户只说了一个字的句子，true表示过滤，false表示不过滤，默认值为true
        :type FilterOneWord: bool
        :param _WelcomeMessagePriority: 欢迎消息优先级，0默认，1高优，高优不能被打断。
        :type WelcomeMessagePriority: int
        :param _FilterBracketsContent: 用于过滤LLM返回内容，不播放括号中的内容。
1：中文括号（）
2：英文括号()
3：中文方括号【】
4：英文方括号[]
5：英文花括号{}
默认值为空，表示不进行过滤。
        :type FilterBracketsContent: int
        :param _AmbientSound: 环境音设置
        :type AmbientSound: :class:`tencentcloud.trtc.v20190722.models.AmbientSound`
        :param _VoicePrint: 声纹配置
        :type VoicePrint: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        :param _TurnDetection: 语义断句检测
        :type TurnDetection: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        :param _SubtitleMode: 机器人字幕显示模式。
- 0表示尽快显示，不会和音频播放进行同步。此时字幕全量下发，后面的字幕会包含前面的字幕。
- 1表示句子级别的实时显示，会和音频播放进行同步，只有当前句子对应的音频播放完后，下一条字幕才会下发。此时字幕增量下发，端上需要把前后的字幕进行拼接才是完整字幕。
        :type SubtitleMode: int
        :param _InterruptWordList: 打断词列表，在AI说话期间，只有说出列表中的打断词才会打断AI说话。
注意：打断词不会触发AI回复。
        :type InterruptWordList: list of str
        """
        self._UserId = None
        self._UserSig = None
        self._TargetUserId = None
        self._MaxIdleTime = None
        self._WelcomeMessage = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None
        self._TurnDetectionMode = None
        self._FilterOneWord = None
        self._WelcomeMessagePriority = None
        self._FilterBracketsContent = None
        self._AmbientSound = None
        self._VoicePrint = None
        self._TurnDetection = None
        self._SubtitleMode = None
        self._InterruptWordList = None

    @property
    def UserId(self):
        r"""机器人的UserId，用于进房发起任务。【注意】这个UserId不能与当前房间内的主播观众[UserId](https://cloud.tencent.com/document/product/647/46351#userid)重复。如果一个房间发起多个任务时，机器人的UserId也不能相互重复，否则会中断前一个任务。需要保证机器人UserId在房间内唯一。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def TargetUserId(self):
        r"""机器人拉流的UserId, 填写后，机器人会拉取该UserId的流进行实时处理
        :rtype: str
        """
        return self._TargetUserId

    @TargetUserId.setter
    def TargetUserId(self, TargetUserId):
        self._TargetUserId = TargetUserId

    @property
    def MaxIdleTime(self):
        r"""房间内超过MaxIdleTime 没有推流，后台自动关闭任务，默认值是60s。
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def WelcomeMessage(self):
        r"""机器人的欢迎语
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def InterruptMode(self):
        r"""智能打断模式，默认为0，0表示服务端自动打断，1表示服务端不打断，由端上发送打断信令进行打断
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        r"""InterruptMode为0时使用，单位为毫秒，默认为500ms。表示服务端检测到持续InterruptSpeechDuration毫秒的人声则进行打断。
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration

    @property
    def TurnDetectionMode(self):
        r"""控制新一轮对话的触发方式，默认为0。
- 0表示当服务端语音识别检测出的完整一句话后，自动触发一轮新的对话。
- 1表示客户端在收到字幕消息后，自行决定是否手动发送聊天信令触发一轮新的对话。
        :rtype: int
        """
        return self._TurnDetectionMode

    @TurnDetectionMode.setter
    def TurnDetectionMode(self, TurnDetectionMode):
        self._TurnDetectionMode = TurnDetectionMode

    @property
    def FilterOneWord(self):
        r"""是否过滤掉用户只说了一个字的句子，true表示过滤，false表示不过滤，默认值为true
        :rtype: bool
        """
        return self._FilterOneWord

    @FilterOneWord.setter
    def FilterOneWord(self, FilterOneWord):
        self._FilterOneWord = FilterOneWord

    @property
    def WelcomeMessagePriority(self):
        r"""欢迎消息优先级，0默认，1高优，高优不能被打断。
        :rtype: int
        """
        return self._WelcomeMessagePriority

    @WelcomeMessagePriority.setter
    def WelcomeMessagePriority(self, WelcomeMessagePriority):
        self._WelcomeMessagePriority = WelcomeMessagePriority

    @property
    def FilterBracketsContent(self):
        r"""用于过滤LLM返回内容，不播放括号中的内容。
1：中文括号（）
2：英文括号()
3：中文方括号【】
4：英文方括号[]
5：英文花括号{}
默认值为空，表示不进行过滤。
        :rtype: int
        """
        return self._FilterBracketsContent

    @FilterBracketsContent.setter
    def FilterBracketsContent(self, FilterBracketsContent):
        self._FilterBracketsContent = FilterBracketsContent

    @property
    def AmbientSound(self):
        r"""环境音设置
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AmbientSound`
        """
        return self._AmbientSound

    @AmbientSound.setter
    def AmbientSound(self, AmbientSound):
        self._AmbientSound = AmbientSound

    @property
    def VoicePrint(self):
        r"""声纹配置
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        """
        return self._VoicePrint

    @VoicePrint.setter
    def VoicePrint(self, VoicePrint):
        self._VoicePrint = VoicePrint

    @property
    def TurnDetection(self):
        r"""语义断句检测
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        """
        return self._TurnDetection

    @TurnDetection.setter
    def TurnDetection(self, TurnDetection):
        self._TurnDetection = TurnDetection

    @property
    def SubtitleMode(self):
        r"""机器人字幕显示模式。
- 0表示尽快显示，不会和音频播放进行同步。此时字幕全量下发，后面的字幕会包含前面的字幕。
- 1表示句子级别的实时显示，会和音频播放进行同步，只有当前句子对应的音频播放完后，下一条字幕才会下发。此时字幕增量下发，端上需要把前后的字幕进行拼接才是完整字幕。
        :rtype: int
        """
        return self._SubtitleMode

    @SubtitleMode.setter
    def SubtitleMode(self, SubtitleMode):
        self._SubtitleMode = SubtitleMode

    @property
    def InterruptWordList(self):
        r"""打断词列表，在AI说话期间，只有说出列表中的打断词才会打断AI说话。
注意：打断词不会触发AI回复。
        :rtype: list of str
        """
        return self._InterruptWordList

    @InterruptWordList.setter
    def InterruptWordList(self, InterruptWordList):
        self._InterruptWordList = InterruptWordList


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._TargetUserId = params.get("TargetUserId")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        self._TurnDetectionMode = params.get("TurnDetectionMode")
        self._FilterOneWord = params.get("FilterOneWord")
        self._WelcomeMessagePriority = params.get("WelcomeMessagePriority")
        self._FilterBracketsContent = params.get("FilterBracketsContent")
        if params.get("AmbientSound") is not None:
            self._AmbientSound = AmbientSound()
            self._AmbientSound._deserialize(params.get("AmbientSound"))
        if params.get("VoicePrint") is not None:
            self._VoicePrint = VoicePrint()
            self._VoicePrint._deserialize(params.get("VoicePrint"))
        if params.get("TurnDetection") is not None:
            self._TurnDetection = TurnDetection()
            self._TurnDetection._deserialize(params.get("TurnDetection"))
        self._SubtitleMode = params.get("SubtitleMode")
        self._InterruptWordList = params.get("InterruptWordList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentParams(AbstractModel):
    r"""转推服务加入TRTC房间的机器人参数。

    """

    def __init__(self):
        r"""
        :param _UserId: 转推服务在TRTC房间使用的[UserId](https://cloud.tencent.com/document/product/647/46351#userid)，注意这个userId不能与其他TRTC或者转推服务等已经使用的UserId重复，建议可以把房间ID作为userId的标识的一部分。
        :type UserId: str
        :param _UserSig: 转推服务加入TRTC房间的用户签名，当前 UserId 对应的验证签名，相当于登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :type UserSig: str
        :param _MaxIdleTime: 所有参与混流转推的主播持续离开TRTC房间或切换成观众超过MaxIdleTime的时长，自动停止转推，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
        :type MaxIdleTime: int
        """
        self._UserId = None
        self._UserSig = None
        self._MaxIdleTime = None

    @property
    def UserId(self):
        r"""转推服务在TRTC房间使用的[UserId](https://cloud.tencent.com/document/product/647/46351#userid)，注意这个userId不能与其他TRTC或者转推服务等已经使用的UserId重复，建议可以把房间ID作为userId的标识的一部分。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""转推服务加入TRTC房间的用户签名，当前 UserId 对应的验证签名，相当于登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def MaxIdleTime(self):
        r"""所有参与混流转推的主播持续离开TRTC房间或切换成观众超过MaxIdleTime的时长，自动停止转推，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._MaxIdleTime = params.get("MaxIdleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AmbientSound(AbstractModel):
    r"""背景音设置，将在通话中添加环境音效，使体验更加逼真。目前支持以下选项：
    coffee_shops: 咖啡店氛围，背景中有人聊天。
    busy_office: 客服中心
    street_traffic: 户外街道
    evening_mountain: 户外山林

    """

    def __init__(self):
        r"""
        :param _Scene: 环境场景选择
        :type Scene: str
        :param _Volume: 控制环境音的音量。取值的范围是 [0,2]。值越低，环境音越小；值越高，环境音越响亮。如果未设置，则使用默认值 1。
        :type Volume: float
        """
        self._Scene = None
        self._Volume = None

    @property
    def Scene(self):
        r"""环境场景选择
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Volume(self):
        r"""控制环境音的音量。取值的范围是 [0,2]。值越低，环境音越小；值越高，环境音越响亮。如果未设置，则使用默认值 1。
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEncode(AbstractModel):
    r"""音频编码参数。

    """

    def __init__(self):
        r"""
        :param _SampleRate: 输出流音频采样率。取值为[48000, 44100, 32000, 24000, 16000, 8000]，单位是Hz。
        :type SampleRate: int
        :param _Channel: 输出流音频声道数，取值范围[1,2]，1表示混流输出音频为单声道，2表示混流输出音频为双声道。
        :type Channel: int
        :param _BitRate: 输出流音频码率。取值范围[8,500]，单位为kbps。
        :type BitRate: int
        :param _Codec: 输出流音频编码类型，取值范围[0, 1, 2]，0为LC-AAC，1为HE-AAC，2为HE-AACv2。默认值为0。当音频编码设置为HE-AACv2时，只支持输出流音频声道数为双声道。HE-AAC和HE-AACv2支持的输出流音频采样率范围为[48000, 44100, 32000, 24000, 16000]。
        :type Codec: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None
        self._Codec = None

    @property
    def SampleRate(self):
        r"""输出流音频采样率。取值为[48000, 44100, 32000, 24000, 16000, 8000]，单位是Hz。
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        r"""输出流音频声道数，取值范围[1,2]，1表示混流输出音频为单声道，2表示混流输出音频为双声道。
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        r"""输出流音频码率。取值范围[8,500]，单位为kbps。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Codec(self):
        r"""输出流音频编码类型，取值范围[0, 1, 2]，0为LC-AAC，1为HE-AAC，2为HE-AACv2。默认值为0。当音频编码设置为HE-AACv2时，只支持输出流音频声道数为双声道。HE-AAC和HE-AACv2支持的输出流音频采样率范围为[48000, 44100, 32000, 24000, 16000]。
        :rtype: int
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        self._Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEncodeParams(AbstractModel):
    r"""音频转码参数

    """

    def __init__(self):
        r"""
        :param _SampleRate: 音频采样率，取值为[48000, 44100]，单位是Hz。
        :type SampleRate: int
        :param _Channel: 音频声道数，取值范围[1,2]，1表示音频为单声道，2表示音频为双声道。
        :type Channel: int
        :param _BitRate: 音频码率，取值范围[8,500]，单位为kbps。
        :type BitRate: int
        :param _Volume: 音量，取值范围[0,300]。默认100，表示原始音量；0表示静音。
        :type Volume: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None
        self._Volume = None

    @property
    def SampleRate(self):
        r"""音频采样率，取值为[48000, 44100]，单位是Hz。
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        r"""音频声道数，取值范围[1,2]，1表示音频为单声道，2表示音频为双声道。
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        r"""音频码率，取值范围[8,500]，单位为kbps。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Volume(self):
        r"""音量，取值范围[0,300]。默认100，表示原始音量；0表示静音。
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioFormat(AbstractModel):
    r"""TTS音频输出的格式

    """

    def __init__(self):
        r"""
        :param _Format: 生成的音频格式，默认pcm，目前支持的格式列表：流式：[pcm]，非流式 [pcm，wav]
        :type Format: str
        :param _SampleRate: 采样率，默认24000， 可选16000, 24000 
        :type SampleRate: int
        """
        self._Format = None
        self._SampleRate = None

    @property
    def Format(self):
        r"""生成的音频格式，默认pcm，目前支持的格式列表：流式：[pcm]，非流式 [pcm，wav]
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def SampleRate(self):
        r"""采样率，默认24000， 可选16000, 24000 
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate


    def _deserialize(self, params):
        self._Format = params.get("Format")
        self._SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioParams(AbstractModel):
    r"""录制音频转码参数。

    """

    def __init__(self):
        r"""
        :param _SampleRate: 音频采样率枚举值:(注意1 代表48000HZ, 2 代表44100HZ, 3 代表16000HZ)
1：48000Hz（默认）;
2：44100Hz
3：16000Hz。
        :type SampleRate: int
        :param _Channel: 声道数枚举值:
1：单声道;
2：双声道（默认）。
        :type Channel: int
        :param _BitRate: 音频码率: 取值范围[32000, 128000] ，单位bps，默认64000bps。
        :type BitRate: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None

    @property
    def SampleRate(self):
        r"""音频采样率枚举值:(注意1 代表48000HZ, 2 代表44100HZ, 3 代表16000HZ)
1：48000Hz（默认）;
2：44100Hz
3：16000Hz。
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        r"""声道数枚举值:
1：单声道;
2：双声道（默认）。
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        r"""音频码率: 取值范围[32000, 128000] ，单位bps，默认64000bps。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditStorageParams(AbstractModel):
    r"""审核存储参数

    """

    def __init__(self):
        r"""
        :param _CloudAuditStorage: 腾讯云对象存储COS以及第三方云存储的账号信息
        :type CloudAuditStorage: :class:`tencentcloud.trtc.v20190722.models.CloudAuditStorage`
        """
        self._CloudAuditStorage = None

    @property
    def CloudAuditStorage(self):
        r"""腾讯云对象存储COS以及第三方云存储的账号信息
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudAuditStorage`
        """
        return self._CloudAuditStorage

    @CloudAuditStorage.setter
    def CloudAuditStorage(self, CloudAuditStorage):
        self._CloudAuditStorage = CloudAuditStorage


    def _deserialize(self, params):
        if params.get("CloudAuditStorage") is not None:
            self._CloudAuditStorage = CloudAuditStorage()
            self._CloudAuditStorage._deserialize(params.get("CloudAuditStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudAuditStorage(AbstractModel):
    r"""腾讯云对象存储COS以及第三方云存储的账号信息

    """

    def __init__(self):
        r"""
        :param _Vendor: 腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS
【注意】目前第三方云存储仅支持AWS，更多第三方云存储陆续支持中
示例值：0
        :type Vendor: int
        :param _Region: 腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-southeast-3	
        :type Region: str
        :param _Bucket: 云存储桶名称。
        :type Bucket: str
        :param _AccessKey: 云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
示例值：test-accesskey
        :type AccessKey: str
        :param _SecretKey: 云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
示例值：test-secretkey
        :type SecretKey: str
        :param _FileNamePrefix: 云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，录制文件xxx.m3u8在 ["prefix1", "prefix2"]作用下，会变成prefix1/prefix2/TaskId/xxx.m3u8。
示例值：["prefix1", "prefix2"]
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        r"""腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS
【注意】目前第三方云存储仅支持AWS，更多第三方云存储陆续支持中
示例值：0
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-southeast-3	
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""云存储桶名称。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
示例值：test-accesskey
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
示例值：test-secretkey
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，录制文件xxx.m3u8在 ["prefix1", "prefix2"]作用下，会变成prefix1/prefix2/TaskId/xxx.m3u8。
示例值：["prefix1", "prefix2"]
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudModerationStorage(AbstractModel):
    r"""腾讯云对象存储COS以及第三方云存储的账号信息

    """

    def __init__(self):
        r"""
        :param _Vendor: 腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS S3
2: 阿里云 OSS
示例值：0
        :type Vendor: int
        :param _Region: 腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-southeast-3	
        :type Region: str
        :param _Bucket: 云存储桶名称。
        :type Bucket: str
        :param _AccessKey: 云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
示例值：test-accesskey
        :type AccessKey: str
        :param _SecretKey: 云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
示例值：test-secretkey
        :type SecretKey: str
        :param _FileNamePrefix: 云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，切片文件xxx.mp3在 ["prefix1", "prefix2"]作用下，音频切片文件会变成prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC时间}.ogg，视频截帧会变成prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC时间}.png 
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        r"""腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS S3
2: 阿里云 OSS
示例值：0
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-southeast-3	
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""云存储桶名称。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
示例值：test-accesskey
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
示例值：test-secretkey
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，切片文件xxx.mp3在 ["prefix1", "prefix2"]作用下，音频切片文件会变成prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC时间}.ogg，视频截帧会变成prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC时间}.png 
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSliceStorage(AbstractModel):
    r"""腾讯云对象存储COS以及第三方云存储的账号信息

    """

    def __init__(self):
        r"""
        :param _Vendor: 腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS S3
2: 阿里云 OSS
示例值：0
        :type Vendor: int
        :param _Region: 腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-southeast-3	
        :type Region: str
        :param _Bucket: 云存储桶名称。
        :type Bucket: str
        :param _AccessKey: 云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
示例值：test-accesskey
        :type AccessKey: str
        :param _SecretKey: 云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
示例值：test-secretkey
        :type SecretKey: str
        :param _FileNamePrefix: 云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，切片文件xxx.mp3在 ["prefix1", "prefix2"]作用下，音频切片文件会变成prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC时间}.ogg，视频截帧会变成prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC时间}.png 
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        r"""腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS S3
2: 阿里云 OSS
示例值：0
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-southeast-3	
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""云存储桶名称。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
示例值：test-accesskey
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
示例值：test-secretkey
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，切片文件xxx.mp3在 ["prefix1", "prefix2"]作用下，音频切片文件会变成prefix1/prefix2/{taskId}/{userId}/audios/{sdkappid}_{roomId}_{userid}_{UTC时间}.ogg，视频截帧会变成prefix1/prefix2/{taskId}/{userId}/images/{sdkappid}_{roomId}_{userid}_{UTC时间}.png 
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorage(AbstractModel):
    r"""腾讯云对象存储COS以及第三方云存储的账号信息

    """

    def __init__(self):
        r"""
        :param _Vendor: 腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS
【注意】目前第三方云存储仅支持AWS，更多第三方云存储陆续支持中
        :type Vendor: int
        :param _Region: 腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
        :type Region: str
        :param _Bucket: 云存储桶名称。
        :type Bucket: str
        :param _AccessKey: 云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
        :type AccessKey: str
        :param _SecretKey: 云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
        :type SecretKey: str
        :param _FileNamePrefix: 云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，录制文件xxx.m3u8在 ["prefix1", "prefix2"]作用下，会变成prefix1/prefix2/TaskId/xxx.m3u8。
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        r"""腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS
【注意】目前第三方云存储仅支持AWS，更多第三方云存储陆续支持中
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""云存储桶名称。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，录制文件xxx.m3u8在 ["prefix1", "prefix2"]作用下，会变成prefix1/prefix2/TaskId/xxx.m3u8。
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudVod(AbstractModel):
    r"""点播相关参数。

    """

    def __init__(self):
        r"""
        :param _TencentVod: 腾讯云点播相关参数。
        :type TencentVod: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        self._TencentVod = None

    @property
    def TencentVod(self):
        r"""腾讯云点播相关参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        return self._TencentVod

    @TencentVod.setter
    def TencentVod(self, TencentVod):
        self._TencentVod = TencentVod


    def _deserialize(self, params):
        if params.get("TencentVod") is not None:
            self._TencentVod = TencentVod()
            self._TencentVod._deserialize(params.get("TencentVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlAIConversationRequest(AbstractModel):
    r"""ControlAIConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一标识
        :type TaskId: str
        :param _Command: 控制命令，目前支持命令如下：- ServerPushText，服务端发送文本给AI机器人，AI机器人会播报该文本. - InvokeLLM，服务端发送文本给大模型，触发对话
        :type Command: str
        :param _ServerPushText: 服务端发送播报文本命令，当Command为ServerPushText时必填
        :type ServerPushText: :class:`tencentcloud.trtc.v20190722.models.ServerPushText`
        :param _InvokeLLM: 服务端发送命令主动请求大模型,当Command为InvokeLLM时会把content请求到大模型,头部增加X-Invoke-LLM="1"
        :type InvokeLLM: :class:`tencentcloud.trtc.v20190722.models.InvokeLLM`
        """
        self._TaskId = None
        self._Command = None
        self._ServerPushText = None
        self._InvokeLLM = None

    @property
    def TaskId(self):
        r"""任务唯一标识
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Command(self):
        r"""控制命令，目前支持命令如下：- ServerPushText，服务端发送文本给AI机器人，AI机器人会播报该文本. - InvokeLLM，服务端发送文本给大模型，触发对话
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ServerPushText(self):
        r"""服务端发送播报文本命令，当Command为ServerPushText时必填
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ServerPushText`
        """
        return self._ServerPushText

    @ServerPushText.setter
    def ServerPushText(self, ServerPushText):
        self._ServerPushText = ServerPushText

    @property
    def InvokeLLM(self):
        r"""服务端发送命令主动请求大模型,当Command为InvokeLLM时会把content请求到大模型,头部增加X-Invoke-LLM="1"
        :rtype: :class:`tencentcloud.trtc.v20190722.models.InvokeLLM`
        """
        return self._InvokeLLM

    @InvokeLLM.setter
    def InvokeLLM(self, InvokeLLM):
        self._InvokeLLM = InvokeLLM


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Command = params.get("Command")
        if params.get("ServerPushText") is not None:
            self._ServerPushText = ServerPushText()
            self._ServerPushText._deserialize(params.get("ServerPushText"))
        if params.get("InvokeLLM") is not None:
            self._InvokeLLM = InvokeLLM()
            self._InvokeLLM._deserialize(params.get("InvokeLLM"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlAIConversationResponse(AbstractModel):
    r"""ControlAIConversation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBasicModerationRequest(AbstractModel):
    r"""CreateBasicModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，为TRTC房间所对应的RoomId。
        :type RoomId: str
        :param _UserId: 目标审核用户id
        :type UserId: str
        :param _RoomIdType: TRTC房间号的类型。【*注意】必须和TRTC的房间所对应的RoomId类型相同:0: 字符串类型的RoomId1: 32位整型的RoomId（默认）
        :type RoomIdType: int
        :param _AuditStorageParams: 音频文件上传到云存储的参数
        :type AuditStorageParams: :class:`tencentcloud.trtc.v20190722.models.AuditStorageParams`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._RoomIdType = None
        self._AuditStorageParams = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，为TRTC房间所对应的RoomId。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""目标审核用户id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型。【*注意】必须和TRTC的房间所对应的RoomId类型相同:0: 字符串类型的RoomId1: 32位整型的RoomId（默认）
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def AuditStorageParams(self):
        r"""音频文件上传到云存储的参数
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AuditStorageParams`
        """
        return self._AuditStorageParams

    @AuditStorageParams.setter
    def AuditStorageParams(self, AuditStorageParams):
        self._AuditStorageParams = AuditStorageParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("AuditStorageParams") is not None:
            self._AuditStorageParams = AuditStorageParams()
            self._AuditStorageParams._deserialize(params.get("AuditStorageParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBasicModerationResponse(AbstractModel):
    r"""CreateBasicModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 审核服务分配的任务ID。任务ID是对一次审核任务生命周期过程的唯一标识，结束任务时会失去意义。任务ID需要业务保存下来，作为下次针对这个任务操作的参数
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""审核服务分配的任务ID。任务ID是对一次审核任务生命周期过程的唯一标识，结束任务时会失去意义。任务ID需要业务保存下来，作为下次针对这个任务操作的参数
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudModerationRequest(AbstractModel):
    r"""CreateCloudModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，为TRTC房间所对应的RoomId。
        :type RoomId: str
        :param _UserId: 机器人的UserId，用于进房发起审核任务。【*注意】这个UserId不能与当前房间内的主播观众UserId重复。如果一个房间发起多个切片任务时，机器人的userid也不能相互重复，否则会中断前一个切片任务。建议可以把房间ID作为UserId的标识的一部分，即机器人UserId在房间内唯一。
        :type UserId: str
        :param _UserSig: 机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算UserSig的方案。
        :type UserSig: str
        :param _ModerationParams: 云端审核控制参数。
        :type ModerationParams: :class:`tencentcloud.trtc.v20190722.models.ModerationParams`
        :param _ModerationStorageParams: 云端审核文件上传到云存储的参数
        :type ModerationStorageParams: :class:`tencentcloud.trtc.v20190722.models.ModerationStorageParams`
        :param _RoomIdType: TRTC房间号的类型。 【*注意】必须和录制的房间所对应的RoomId类型相同: 0: 字符串类型的RoomId 1: 32位整型的RoomId（默认） 示例值：1
        :type RoomIdType: int
        :param _ResourceExpiredHour: 任务ID可以调用的时效性，从成功开启任务并获得TaskID后开始计算，超时后无法调用查询、更新和停止等接口，但是切片任务不会停止。 参数的单位是小时，默认24小时（1天），最大可设置72小时（3天），最小设置6小时。举例说明：如果不设置该参数，那么开始切片成功后，查询、更新和停止切片的调用时效为24个小时。
        :type ResourceExpiredHour: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._UserSig = None
        self._ModerationParams = None
        self._ModerationStorageParams = None
        self._RoomIdType = None
        self._ResourceExpiredHour = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，为TRTC房间所对应的RoomId。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""机器人的UserId，用于进房发起审核任务。【*注意】这个UserId不能与当前房间内的主播观众UserId重复。如果一个房间发起多个切片任务时，机器人的userid也不能相互重复，否则会中断前一个切片任务。建议可以把房间ID作为UserId的标识的一部分，即机器人UserId在房间内唯一。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算UserSig的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def ModerationParams(self):
        r"""云端审核控制参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModerationParams`
        """
        return self._ModerationParams

    @ModerationParams.setter
    def ModerationParams(self, ModerationParams):
        self._ModerationParams = ModerationParams

    @property
    def ModerationStorageParams(self):
        r"""云端审核文件上传到云存储的参数
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModerationStorageParams`
        """
        return self._ModerationStorageParams

    @ModerationStorageParams.setter
    def ModerationStorageParams(self, ModerationStorageParams):
        self._ModerationStorageParams = ModerationStorageParams

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型。 【*注意】必须和录制的房间所对应的RoomId类型相同: 0: 字符串类型的RoomId 1: 32位整型的RoomId（默认） 示例值：1
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def ResourceExpiredHour(self):
        r"""任务ID可以调用的时效性，从成功开启任务并获得TaskID后开始计算，超时后无法调用查询、更新和停止等接口，但是切片任务不会停止。 参数的单位是小时，默认24小时（1天），最大可设置72小时（3天），最小设置6小时。举例说明：如果不设置该参数，那么开始切片成功后，查询、更新和停止切片的调用时效为24个小时。
        :rtype: int
        """
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("ModerationParams") is not None:
            self._ModerationParams = ModerationParams()
            self._ModerationParams._deserialize(params.get("ModerationParams"))
        if params.get("ModerationStorageParams") is not None:
            self._ModerationStorageParams = ModerationStorageParams()
            self._ModerationStorageParams._deserialize(params.get("ModerationStorageParams"))
        self._RoomIdType = params.get("RoomIdType")
        self._ResourceExpiredHour = params.get("ResourceExpiredHour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudModerationResponse(AbstractModel):
    r"""CreateCloudModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 云端审核服务分配的任务ID。任务ID是对一次切片任务生命周期过程的唯一标识，结束任务时会失去意义。任务ID需要业务保存下来，作为下次针对这个任务操作的参数
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""云端审核服务分配的任务ID。任务ID是对一次切片任务生命周期过程的唯一标识，结束任务时会失去意义。任务ID需要业务保存下来，作为下次针对这个任务操作的参数
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudRecordingRequest(AbstractModel):
    r"""CreateCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和录制的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，录制的TRTC房间所对应的RoomId。
注：房间号类型默认为整型，若房间号类型为字符串，请通过RoomIdType指定。

        :type RoomId: str
        :param _UserId: 录制机器人的UserId，用于进房发起录制任务。
【*注意】这个UserId不能与当前房间内的主播观众[UserId](https://cloud.tencent.com/document/product/647/46351#userid)重复。如果一个房间发起多个录制任务时，机器人的userid也不能相互重复，否则会中断前一个录制任务。建议可以把房间ID作为UserId的标识的一部分，即录制机器人UserId在房间内唯一。
        :type UserId: str
        :param _UserSig: 录制机器人UserId对应的校验签名，即UserId和UserSig相当于录制机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :type UserSig: str
        :param _RecordParams: 云端录制控制参数。
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        :param _StorageParams: 云端录制文件上传到云存储的参数（不支持同时设置云点播VOD和对象存储COS）
        :type StorageParams: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        :param _RoomIdType: TRTC房间号的类型。
【*注意】必须和录制的房间所对应的RoomId类型相同:
0: 字符串类型的RoomId
1: 32位整型的RoomId（默认）
        :type RoomIdType: int
        :param _MixTranscodeParams: 合流的转码参数，录制模式为合流的时候可以设置。
        :type MixTranscodeParams: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        :param _MixLayoutParams: 合流的布局参数，录制模式为合流的时候可以设置。
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param _ResourceExpiredHour: 接口可以调用的时效性，从成功开启录制并获得任务ID后开始计算，超时后无法调用查询、更新和停止等接口，但是录制任务不会停止。 参数的单位是小时，默认72小时（3天），最大可设置720小时（30天），最小设置6小时。举例说明：如果不设置该参数，那么开始录制成功后，查询、更新和停止录制的调用时效为72个小时。
        :type ResourceExpiredHour: int
        :param _PrivateMapKey: TRTC房间权限加密串，只有在TRTC控制台启用了高级权限控制的时候需要携带，在TRTC控制台如果开启高级权限控制后，TRTC 的后台服务系统会校验一个叫做 [PrivateMapKey] 的“权限票据”，权限票据中包含了一个加密后的 RoomId 和一个加密后的“权限位列表”。由于 PrivateMapKey 中包含 RoomId，所以只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。
        :type PrivateMapKey: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._UserSig = None
        self._RecordParams = None
        self._StorageParams = None
        self._RoomIdType = None
        self._MixTranscodeParams = None
        self._MixLayoutParams = None
        self._ResourceExpiredHour = None
        self._PrivateMapKey = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和录制的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，录制的TRTC房间所对应的RoomId。
注：房间号类型默认为整型，若房间号类型为字符串，请通过RoomIdType指定。

        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""录制机器人的UserId，用于进房发起录制任务。
【*注意】这个UserId不能与当前房间内的主播观众[UserId](https://cloud.tencent.com/document/product/647/46351#userid)重复。如果一个房间发起多个录制任务时，机器人的userid也不能相互重复，否则会中断前一个录制任务。建议可以把房间ID作为UserId的标识的一部分，即录制机器人UserId在房间内唯一。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""录制机器人UserId对应的校验签名，即UserId和UserSig相当于录制机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def RecordParams(self):
        r"""云端录制控制参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        """
        return self._RecordParams

    @RecordParams.setter
    def RecordParams(self, RecordParams):
        self._RecordParams = RecordParams

    @property
    def StorageParams(self):
        r"""云端录制文件上传到云存储的参数（不支持同时设置云点播VOD和对象存储COS）
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        """
        return self._StorageParams

    @StorageParams.setter
    def StorageParams(self, StorageParams):
        self._StorageParams = StorageParams

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型。
【*注意】必须和录制的房间所对应的RoomId类型相同:
0: 字符串类型的RoomId
1: 32位整型的RoomId（默认）
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def MixTranscodeParams(self):
        r"""合流的转码参数，录制模式为合流的时候可以设置。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        """
        return self._MixTranscodeParams

    @MixTranscodeParams.setter
    def MixTranscodeParams(self, MixTranscodeParams):
        self._MixTranscodeParams = MixTranscodeParams

    @property
    def MixLayoutParams(self):
        r"""合流的布局参数，录制模式为合流的时候可以设置。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        """
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def ResourceExpiredHour(self):
        r"""接口可以调用的时效性，从成功开启录制并获得任务ID后开始计算，超时后无法调用查询、更新和停止等接口，但是录制任务不会停止。 参数的单位是小时，默认72小时（3天），最大可设置720小时（30天），最小设置6小时。举例说明：如果不设置该参数，那么开始录制成功后，查询、更新和停止录制的调用时效为72个小时。
        :rtype: int
        """
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour

    @property
    def PrivateMapKey(self):
        r"""TRTC房间权限加密串，只有在TRTC控制台启用了高级权限控制的时候需要携带，在TRTC控制台如果开启高级权限控制后，TRTC 的后台服务系统会校验一个叫做 [PrivateMapKey] 的“权限票据”，权限票据中包含了一个加密后的 RoomId 和一个加密后的“权限位列表”。由于 PrivateMapKey 中包含 RoomId，所以只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("RecordParams") is not None:
            self._RecordParams = RecordParams()
            self._RecordParams._deserialize(params.get("RecordParams"))
        if params.get("StorageParams") is not None:
            self._StorageParams = StorageParams()
            self._StorageParams._deserialize(params.get("StorageParams"))
        self._RoomIdType = params.get("RoomIdType")
        if params.get("MixTranscodeParams") is not None:
            self._MixTranscodeParams = MixTranscodeParams()
            self._MixTranscodeParams._deserialize(params.get("MixTranscodeParams"))
        if params.get("MixLayoutParams") is not None:
            self._MixLayoutParams = MixLayoutParams()
            self._MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        self._ResourceExpiredHour = params.get("ResourceExpiredHour")
        self._PrivateMapKey = params.get("PrivateMapKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingResponse(AbstractModel):
    r"""CreateCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。任务 ID需要业务保存下来，作为下次针对这个录制任务操作的参数。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。任务 ID需要业务保存下来，作为下次针对这个录制任务操作的参数。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateCloudSliceTaskRequest(AbstractModel):
    r"""CreateCloudSliceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，为TRTC房间所对应的RoomId。
        :type RoomId: str
        :param _UserId: 机器人的UserId，用于进房发起切片任务。【*注意】这个UserId不能与当前房间内的主播观众UserId重复。如果一个房间发起多个切片任务时，机器人的userid也不能相互重复，否则会中断前一个切片任务。建议可以把房间ID作为UserId的标识的一部分，即机器人UserId在房间内唯一。
        :type UserId: str
        :param _UserSig: 机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算UserSig的方案。
        :type UserSig: str
        :param _SliceParams: 云端切片控制参数。
        :type SliceParams: :class:`tencentcloud.trtc.v20190722.models.SliceParams`
        :param _SliceStorageParams: 云端切片文件上传到云存储的参数
        :type SliceStorageParams: :class:`tencentcloud.trtc.v20190722.models.SliceStorageParams`
        :param _RoomIdType: TRTC房间号的类型。 【*注意】必须和录制的房间所对应的RoomId类型相同: 0: 字符串类型的RoomId 1: 32位整型的RoomId（默认） 示例值：1
        :type RoomIdType: int
        :param _ResourceExpiredHour: 接口可以调用的时效性，从成功开启录制并获得任务ID后开始计算，超时后无法调用查询、更新和停止等接口，但是录制任务不会停止。 参数的单位是小时，默认72小时（3天），最大可设置720小时（30天），最小设置6小时。举例说明：如果不设置该参数，那么开始录制成功后，查询、更新和停止录制的调用时效为72个小时。 示例值：24
        :type ResourceExpiredHour: int
        :param _PrivateMapKey: TRTC房间权限加密串，只有在TRTC控制台启用了高级权限控制的时候需要携带，在TRTC控制台如果开启高级权限控制后，TRTC 的后台服务系统会校验一个叫做 [PrivateMapKey] 的“权限票据”，权限票据中包含了一个加密后的 RoomId 和一个加密后的“权限位列表”。由于 PrivateMapKey 中包含 RoomId，所以只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。 示例值：eJw1jcEKgkAURX9FZlvY****fL9rfNX4_
        :type PrivateMapKey: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._UserSig = None
        self._SliceParams = None
        self._SliceStorageParams = None
        self._RoomIdType = None
        self._ResourceExpiredHour = None
        self._PrivateMapKey = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，为TRTC房间所对应的RoomId。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        r"""机器人的UserId，用于进房发起切片任务。【*注意】这个UserId不能与当前房间内的主播观众UserId重复。如果一个房间发起多个切片任务时，机器人的userid也不能相互重复，否则会中断前一个切片任务。建议可以把房间ID作为UserId的标识的一部分，即机器人UserId在房间内唯一。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算UserSig的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def SliceParams(self):
        r"""云端切片控制参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SliceParams`
        """
        return self._SliceParams

    @SliceParams.setter
    def SliceParams(self, SliceParams):
        self._SliceParams = SliceParams

    @property
    def SliceStorageParams(self):
        r"""云端切片文件上传到云存储的参数
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SliceStorageParams`
        """
        return self._SliceStorageParams

    @SliceStorageParams.setter
    def SliceStorageParams(self, SliceStorageParams):
        self._SliceStorageParams = SliceStorageParams

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型。 【*注意】必须和录制的房间所对应的RoomId类型相同: 0: 字符串类型的RoomId 1: 32位整型的RoomId（默认） 示例值：1
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def ResourceExpiredHour(self):
        r"""接口可以调用的时效性，从成功开启录制并获得任务ID后开始计算，超时后无法调用查询、更新和停止等接口，但是录制任务不会停止。 参数的单位是小时，默认72小时（3天），最大可设置720小时（30天），最小设置6小时。举例说明：如果不设置该参数，那么开始录制成功后，查询、更新和停止录制的调用时效为72个小时。 示例值：24
        :rtype: int
        """
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour

    @property
    def PrivateMapKey(self):
        r"""TRTC房间权限加密串，只有在TRTC控制台启用了高级权限控制的时候需要携带，在TRTC控制台如果开启高级权限控制后，TRTC 的后台服务系统会校验一个叫做 [PrivateMapKey] 的“权限票据”，权限票据中包含了一个加密后的 RoomId 和一个加密后的“权限位列表”。由于 PrivateMapKey 中包含 RoomId，所以只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。 示例值：eJw1jcEKgkAURX9FZlvY****fL9rfNX4_
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("SliceParams") is not None:
            self._SliceParams = SliceParams()
            self._SliceParams._deserialize(params.get("SliceParams"))
        if params.get("SliceStorageParams") is not None:
            self._SliceStorageParams = SliceStorageParams()
            self._SliceStorageParams._deserialize(params.get("SliceStorageParams"))
        self._RoomIdType = params.get("RoomIdType")
        self._ResourceExpiredHour = params.get("ResourceExpiredHour")
        self._PrivateMapKey = params.get("PrivateMapKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudSliceTaskResponse(AbstractModel):
    r"""CreateCloudSliceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 云端切片服务分配的任务ID。任务ID是对一次切片任务生命周期过程的唯一标识，结束任务时会失去意义。任务ID需要业务保存下来，作为下次针对这个任务操作的参数
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""云端切片服务分配的任务ID。任务ID是对一次切片任务生命周期过程的唯一标识，结束任务时会失去意义。任务ID需要业务保存下来，作为下次针对这个任务操作的参数
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreatePictureRequest(AbstractModel):
    r"""CreatePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用id
        :type SdkAppId: int
        :param _Content: 图片内容经base64编码后的string格式,最大长度为2M
        :type Content: str
        :param _Suffix: 图片后缀名
        :type Suffix: str
        :param _Height: 图片长度
        :type Height: int
        :param _Width: 图片宽度
        :type Width: int
        :param _XPosition: 显示位置x轴方向
        :type XPosition: int
        :param _YPosition: 显示位置y轴方向
        :type YPosition: int
        """
        self._SdkAppId = None
        self._Content = None
        self._Suffix = None
        self._Height = None
        self._Width = None
        self._XPosition = None
        self._YPosition = None

    @property
    def SdkAppId(self):
        r"""应用id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Content(self):
        r"""图片内容经base64编码后的string格式,最大长度为2M
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Suffix(self):
        r"""图片后缀名
        :rtype: str
        """
        return self._Suffix

    @Suffix.setter
    def Suffix(self, Suffix):
        self._Suffix = Suffix

    @property
    def Height(self):
        r"""图片长度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        r"""图片宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def XPosition(self):
        r"""显示位置x轴方向
        :rtype: int
        """
        return self._XPosition

    @XPosition.setter
    def XPosition(self, XPosition):
        self._XPosition = XPosition

    @property
    def YPosition(self):
        r"""显示位置y轴方向
        :rtype: int
        """
        return self._YPosition

    @YPosition.setter
    def YPosition(self, YPosition):
        self._YPosition = YPosition


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._Content = params.get("Content")
        self._Suffix = params.get("Suffix")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._XPosition = params.get("XPosition")
        self._YPosition = params.get("YPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePictureResponse(AbstractModel):
    r"""CreatePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PictureId: 图片id
        :type PictureId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PictureId = None
        self._RequestId = None

    @property
    def PictureId(self):
        r"""图片id
        :rtype: int
        """
        return self._PictureId

    @PictureId.setter
    def PictureId(self, PictureId):
        self._PictureId = PictureId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PictureId = params.get("PictureId")
        self._RequestId = params.get("RequestId")


class DeleteBasicModerationRequest(AbstractModel):
    r"""DeleteBasicModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和TRTC的房间所使用的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 审核任务的唯一Id，在启动审核任务成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和TRTC的房间所使用的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""审核任务的唯一Id，在启动审核任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBasicModerationResponse(AbstractModel):
    r"""DeleteBasicModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 审核任务的唯一Id。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""审核任务的唯一Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudModerationRequest(AbstractModel):
    r"""DeleteCloudModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 审核任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""审核任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudModerationResponse(AbstractModel):
    r"""DeleteCloudModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 审核任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""审核任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudRecordingRequest(AbstractModel):
    r"""DeleteCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 录制任务的唯一Id，在启动录制成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""录制任务的唯一Id，在启动录制成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRecordingResponse(AbstractModel):
    r"""DeleteCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudSliceTaskRequest(AbstractModel):
    r"""DeleteCloudSliceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 切片任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""切片任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudSliceTaskResponse(AbstractModel):
    r"""DeleteCloudSliceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 切片任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""切片任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeletePictureRequest(AbstractModel):
    r"""DeletePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PictureId: 图片id
        :type PictureId: int
        :param _SdkAppId: 应用id
        :type SdkAppId: int
        """
        self._PictureId = None
        self._SdkAppId = None

    @property
    def PictureId(self):
        r"""图片id
        :rtype: int
        """
        return self._PictureId

    @PictureId.setter
    def PictureId(self, PictureId):
        self._PictureId = PictureId

    @property
    def SdkAppId(self):
        r"""应用id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._PictureId = params.get("PictureId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePictureResponse(AbstractModel):
    r"""DeletePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteVoicePrintRequest(AbstractModel):
    r"""DeleteVoicePrint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 声纹信息ID
        :type VoicePrintId: str
        """
        self._VoicePrintId = None

    @property
    def VoicePrintId(self):
        r"""声纹信息ID
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVoicePrintResponse(AbstractModel):
    r"""DeleteVoicePrint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAIConversationRequest(AbstractModel):
    r"""DescribeAIConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和开启转录任务的房间使用的SdkAppId相同。
        :type SdkAppId: int
        :param _TaskId: 唯一标识一次任务。
        :type TaskId: str
        :param _SessionId: 开启任务时填写的SessionId，如果没写则不返回。
        :type SessionId: str
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和开启转录任务的房间使用的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""唯一标识一次任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        r"""开启任务时填写的SessionId，如果没写则不返回。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIConversationResponse(AbstractModel):
    r"""DescribeAIConversation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _Status: 任务状态。有4个值：1、Idle表示任务未开始2、Preparing表示任务准备中3、InProgress表示任务正在运行4、Stopped表示任务已停止，正在清理资源中
        :type Status: str
        :param _TaskId: 任务的唯一标识，在启动任务时生成
        :type TaskId: str
        :param _SessionId: 开启对话任务时填写的SessionId，如果没写则不返回。
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._Status = None
        self._TaskId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""任务开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        r"""任务状态。有4个值：1、Idle表示任务未开始2、Preparing表示任务准备中3、InProgress表示任务正在运行4、Stopped表示任务已停止，正在清理资源中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""任务的唯一标识，在启动任务时生成
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        r"""开启对话任务时填写的SessionId，如果没写则不返回。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeAITranscriptionRequest(AbstractModel):
    r"""DescribeAITranscription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 查询任务状态，不使用时传入空字符串。
有两种查询方式：
1、只填写TaskId，这种方式使用TaskId来查询任务
2、TaskId为空字符串，填写SdkAppId和SessionId，这种方式不需要使用TaskId查询任务
        :type TaskId: str
        :param _SdkAppId: TRTC的SdkAppId，和SessionId配合使用。
        :type SdkAppId: int
        :param _SessionId: 开启转录任务时传入的SessionId，和SdkAppId配合使用。
        :type SessionId: str
        """
        self._TaskId = None
        self._SdkAppId = None
        self._SessionId = None

    @property
    def TaskId(self):
        r"""查询任务状态，不使用时传入空字符串。
有两种查询方式：
1、只填写TaskId，这种方式使用TaskId来查询任务
2、TaskId为空字符串，填写SdkAppId和SessionId，这种方式不需要使用TaskId查询任务
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId，和SessionId配合使用。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        r"""开启转录任务时传入的SessionId，和SdkAppId配合使用。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAITranscriptionResponse(AbstractModel):
    r"""DescribeAITranscription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 任务开始时间。
        :type StartTime: str
        :param _Status: 转录任务状态。
有4个值：
1、Idle表示任务未开始
2、Preparing表示任务准备中
3、InProgress表示任务正在运行
4、Stopped表示任务已停止，正在清理资源中
        :type Status: str
        :param _TaskId: 唯一标识一次任务。
        :type TaskId: str
        :param _SessionId: 开启转录任务时填写的SessionId，如果没写则不返回。
        :type SessionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StartTime = None
        self._Status = None
        self._TaskId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def StartTime(self):
        r"""任务开始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        r"""转录任务状态。
有4个值：
1、Idle表示任务未开始
2、Preparing表示任务准备中
3、InProgress表示任务正在运行
4、Stopped表示任务已停止，正在清理资源中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""唯一标识一次任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        r"""开启转录任务时填写的SessionId，如果没写则不返回。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeCallDetailInfoRequest(AbstractModel):
    r"""DescribeCallDetailInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommId: 通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :type CommId: str
        :param _StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777），
注意：支持查询14天内的数据。
        :type StartTime: int
        :param _EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：查询起止时间需小于1小时，超过则返回null，即与StartTime间隔时间不超过1小时。
        :type EndTime: int
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）。
        :type SdkAppId: int
        :param _UserIds: 需查询的用户数组，默认不填返回6个用户。
        :type UserIds: list of str
        :param _DataType: 需查询的指标，不填则只返回用户列表，填all则返回所有指标。
appCpu：APP CPU使用率；
sysCpu：系统 CPU使用率；
aBit：上/下行音频码率；单位：bps
aBlock：音频卡顿时长；单位：ms
bigvBit：上/下行视频码率；单位：bps
bigvCapFps：视频采集帧率；
bigvEncFps：视频发送帧率；
bigvDecFps：渲染帧率；
bigvBlock：视频卡顿时长；单位：ms
aLoss：上/下行音频丢包率；
bigvLoss：上/下行视频丢包率；
bigvWidth：上/下行分辨率宽；
bigvHeight：上/下行分辨率高；
aCapEnergy：音频采集能量；
aPlayEnergy：音频播放能量；
rtt：SDK到云端的往返延时；单位: ms
bigvRecFps: 云端送达帧率；
        :type DataType: list of str
        :param _PageNumber: 当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回6条数据。
        :type PageNumber: int
        :param _PageSize: 每页个数，默认为6，
范围：[1，100]
注意：DataType不为null，UserIds长度不能超过6，PageSize最大值不超过6；
DataType 为null，UserIds长度不超过100，PageSize最大不超过100。
        :type PageSize: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._UserIds = None
        self._DataType = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def CommId(self):
        r"""通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        r"""查询开始时间，本地unix时间戳，单位为秒（如：1590065777），
注意：支持查询14天内的数据。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：查询起止时间需小于1小时，超过则返回null，即与StartTime间隔时间不超过1小时。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        r"""需查询的用户数组，默认不填返回6个用户。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def DataType(self):
        r"""需查询的指标，不填则只返回用户列表，填all则返回所有指标。
appCpu：APP CPU使用率；
sysCpu：系统 CPU使用率；
aBit：上/下行音频码率；单位：bps
aBlock：音频卡顿时长；单位：ms
bigvBit：上/下行视频码率；单位：bps
bigvCapFps：视频采集帧率；
bigvEncFps：视频发送帧率；
bigvDecFps：渲染帧率；
bigvBlock：视频卡顿时长；单位：ms
aLoss：上/下行音频丢包率；
bigvLoss：上/下行视频丢包率；
bigvWidth：上/下行分辨率宽；
bigvHeight：上/下行分辨率高；
aCapEnergy：音频采集能量；
aPlayEnergy：音频播放能量；
rtt：SDK到云端的往返延时；单位: ms
bigvRecFps: 云端送达帧率；
        :rtype: list of str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PageNumber(self):
        r"""当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回6条数据。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页个数，默认为6，
范围：[1，100]
注意：DataType不为null，UserIds长度不能超过6，PageSize最大值不超过6；
DataType 为null，UserIds长度不超过100，PageSize最大不超过100。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._UserIds = params.get("UserIds")
        self._DataType = params.get("DataType")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallDetailInfoResponse(AbstractModel):
    r"""DescribeCallDetailInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回的用户总条数
        :type Total: int
        :param _UserList: 用户信息列表
        :type UserList: list of UserInformation
        :param _Data: 质量数据
        :type Data: list of QualityData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._UserList = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回的用户总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        r"""用户信息列表
        :rtype: list of UserInformation
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def Data(self):
        r"""质量数据
        :rtype: list of QualityData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudModerationRequest(AbstractModel):
    r"""DescribeCloudModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 云端审核任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""云端审核任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudModerationResponse(AbstractModel):
    r"""DescribeCloudModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 切片任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _Status: 云端切片任务的状态信息。Idle:表示当前任务空闲中,InProgress:表示当前任务正在进行中,Exited:表示当前任务正在退出的过程中。
        :type Status: str
        :param _SubscribeStreamUserIds: 订阅黑白名单
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._SubscribeStreamUserIds = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""切片任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""云端切片任务的状态信息。Idle:表示当前任务空闲中,InProgress:表示当前任务正在进行中,Exited:表示当前任务正在退出的过程中。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubscribeStreamUserIds(self):
        r"""订阅黑白名单
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeModerationUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self._RequestId = params.get("RequestId")


class DescribeCloudRecordingRequest(AbstractModel):
    r"""DescribeCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 录制任务的唯一Id，在启动录制成功后会返回。
        :type TaskId: str
        :param _RecorderKey: 转推录制任务发起时所填，标识一次录制
        :type RecorderKey: str
        """
        self._SdkAppId = None
        self._TaskId = None
        self._RecorderKey = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""录制任务的唯一Id，在启动录制成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecorderKey(self):
        r"""转推录制任务发起时所填，标识一次录制
        :rtype: str
        """
        return self._RecorderKey

    @RecorderKey.setter
    def RecorderKey(self, RecorderKey):
        self._RecorderKey = RecorderKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._RecorderKey = params.get("RecorderKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRecordingResponse(AbstractModel):
    r"""DescribeCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 录制任务的唯一Id。
        :type TaskId: str
        :param _Status: 云端录制任务的状态信息。
Idle：表示当前录制任务空闲中
InProgress：表示当前录制任务正在进行中。
Exited：表示当前录制任务正在退出的过程中。
        :type Status: str
        :param _StorageFileList: 录制文件信息。
        :type StorageFileList: list of StorageFile
        :param _RecorderKey: 转推录制任务发起时所填，标识一次录制
        :type RecorderKey: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._StorageFileList = None
        self._RecorderKey = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""录制任务的唯一Id。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""云端录制任务的状态信息。
Idle：表示当前录制任务空闲中
InProgress：表示当前录制任务正在进行中。
Exited：表示当前录制任务正在退出的过程中。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StorageFileList(self):
        r"""录制文件信息。
        :rtype: list of StorageFile
        """
        return self._StorageFileList

    @StorageFileList.setter
    def StorageFileList(self, StorageFileList):
        self._StorageFileList = StorageFileList

    @property
    def RecorderKey(self):
        r"""转推录制任务发起时所填，标识一次录制
        :rtype: str
        """
        return self._RecorderKey

    @RecorderKey.setter
    def RecorderKey(self, RecorderKey):
        self._RecorderKey = RecorderKey

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        if params.get("StorageFileList") is not None:
            self._StorageFileList = []
            for item in params.get("StorageFileList"):
                obj = StorageFile()
                obj._deserialize(item)
                self._StorageFileList.append(obj)
        self._RecorderKey = params.get("RecorderKey")
        self._RequestId = params.get("RequestId")


class DescribeCloudSliceTaskRequest(AbstractModel):
    r"""DescribeCloudSliceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 切片任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""切片任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudSliceTaskResponse(AbstractModel):
    r"""DescribeCloudSliceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 切片任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _Status: 云端切片任务的状态信息。Idle:表示当前任务空闲中,InProgress:表示当前任务正在进行中,Exited:表示当前任务正在退出的过程中。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""切片任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""云端切片任务的状态信息。Idle:表示当前任务空闲中,InProgress:表示当前任务正在进行中,Exited:表示当前任务正在退出的过程中。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeMixTranscodingUsageRequest(AbstractModel):
    r"""DescribeMixTranscodingUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param _SdkAppId: TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMixTranscodingUsageResponse(AbstractModel):
    r"""DescribeMixTranscodingUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsageKey: 用量类型，与UsageValue中各个位置的值对应。
        :type UsageKey: list of str
        :param _UsageList: 各个时间点用量明细。
        :type UsageList: list of TrtcUsage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""用量类型，与UsageValue中各个位置的值对应。
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""各个时间点用量明细。
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePictureRequest(AbstractModel):
    r"""DescribePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 应用ID
        :type SdkAppId: int
        :param _PictureId: 图片ID，不填时返回该应用下所有图片
        :type PictureId: int
        :param _PageSize: 每页数量，不填时默认为10
        :type PageSize: int
        :param _PageNo: 页码，不填时默认为1
        :type PageNo: int
        """
        self._SdkAppId = None
        self._PictureId = None
        self._PageSize = None
        self._PageNo = None

    @property
    def SdkAppId(self):
        r"""应用ID
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PictureId(self):
        r"""图片ID，不填时返回该应用下所有图片
        :rtype: int
        """
        return self._PictureId

    @PictureId.setter
    def PictureId(self, PictureId):
        self._PictureId = PictureId

    @property
    def PageSize(self):
        r"""每页数量，不填时默认为10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        r"""页码，不填时默认为1
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._PictureId = params.get("PictureId")
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePictureResponse(AbstractModel):
    r"""DescribePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回的图片记录数
        :type Total: int
        :param _PictureInfo: 图片信息列表
        :type PictureInfo: list of PictureInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._PictureInfo = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回的图片记录数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def PictureInfo(self):
        r"""图片信息列表
        :rtype: list of PictureInfo
        """
        return self._PictureInfo

    @PictureInfo.setter
    def PictureInfo(self, PictureInfo):
        self._PictureInfo = PictureInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("PictureInfo") is not None:
            self._PictureInfo = []
            for item in params.get("PictureInfo"):
                obj = PictureInfo()
                obj._deserialize(item)
                self._PictureInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordStatisticRequest(AbstractModel):
    r"""DescribeRecordStatistic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始日期，格式为YYYY-MM-DD。
        :type StartTime: str
        :param _EndTime: 查询结束日期，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param _SdkAppId: 应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""查询开始日期，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束日期，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordStatisticResponse(AbstractModel):
    r"""DescribeRecordStatistic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppIdUsages: 应用的用量信息数组。
        :type SdkAppIdUsages: list of SdkAppIdRecordUsage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SdkAppIdUsages = None
        self._RequestId = None

    @property
    def SdkAppIdUsages(self):
        r"""应用的用量信息数组。
        :rtype: list of SdkAppIdRecordUsage
        """
        return self._SdkAppIdUsages

    @SdkAppIdUsages.setter
    def SdkAppIdUsages(self, SdkAppIdUsages):
        self._SdkAppIdUsages = SdkAppIdUsages

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SdkAppIdUsages") is not None:
            self._SdkAppIdUsages = []
            for item in params.get("SdkAppIdUsages"):
                obj = SdkAppIdRecordUsage()
                obj._deserialize(item)
                self._SdkAppIdUsages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordingUsageRequest(AbstractModel):
    r"""DescribeRecordingUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param _MixType: 查询单流录制或合流录制，值为"single"或"multi"。
        :type MixType: str
        :param _SdkAppId: TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._MixType = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MixType(self):
        r"""查询单流录制或合流录制，值为"single"或"multi"。
        :rtype: str
        """
        return self._MixType

    @MixType.setter
    def MixType(self, MixType):
        self._MixType = MixType

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MixType = params.get("MixType")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingUsageResponse(AbstractModel):
    r"""DescribeRecordingUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsageKey: 用量类型，与UsageValue中各个位置的值对应。
        :type UsageKey: list of str
        :param _UsageList: 各个时间点用量明细。
        :type UsageList: list of TrtcUsage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""用量类型，与UsageValue中各个位置的值对应。
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""各个时间点用量明细。
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRelayUsageRequest(AbstractModel):
    r"""DescribeRelayUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param _SdkAppId: TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelayUsageResponse(AbstractModel):
    r"""DescribeRelayUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsageKey: 用量类型，与UsageValue中各个位置的值对应。
        :type UsageKey: list of str
        :param _UsageList: 各个时间点用量明细。
        :type UsageList: list of TrtcUsage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""用量类型，与UsageValue中各个位置的值对应。
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""各个时间点用量明细。
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoomInfoRequest(AbstractModel):
    r"""DescribeRoomInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param _StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）注意：最大支持查询14天内的数据
        :type StartTime: int
        :param _EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：与StartTime间隔时间不超过24小时。
        :type EndTime: int
        :param _RoomId: 房间号（如：223)
        :type RoomId: str
        :param _PageNumber: 当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回10条数据。
        :type PageNumber: int
        :param _PageSize: 每页个数，默认为10，
范围：[1，100]
        :type PageSize: int
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""查询开始时间，本地unix时间戳，单位为秒（如：1590065777）注意：最大支持查询14天内的数据
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：与StartTime间隔时间不超过24小时。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""房间号（如：223)
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def PageNumber(self):
        r"""当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回10条数据。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页个数，默认为10，
范围：[1，100]
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomInfoResponse(AbstractModel):
    r"""DescribeRoomInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回当页数据总数
        :type Total: int
        :param _RoomList: 房间信息列表
        :type RoomList: list of RoomState
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RoomList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回当页数据总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RoomList(self):
        r"""房间信息列表
        :rtype: list of RoomState
        """
        return self._RoomList

    @RoomList.setter
    def RoomList(self, RoomList):
        self._RoomList = RoomList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("RoomList") is not None:
            self._RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self._RoomList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScaleInfoRequest(AbstractModel):
    r"""DescribeScaleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param _StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据。
        :type StartTime: int
        :param _EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877），建议与StartTime间隔时间超过24小时。
注意：按天统计，结束时间大于前一天，否则查询数据为空（如：需查询20号数据，结束时间需晚于20号0点）。
        :type EndTime: int
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，本地unix时间戳，单位为秒（如：1590065877），建议与StartTime间隔时间超过24小时。
注意：按天统计，结束时间大于前一天，否则查询数据为空（如：需查询20号数据，结束时间需晚于20号0点）。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScaleInfoResponse(AbstractModel):
    r"""DescribeScaleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回的数据条数
        :type Total: int
        :param _ScaleList: 返回的数据
        :type ScaleList: list of ScaleInfomation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ScaleList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回的数据条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ScaleList(self):
        r"""返回的数据
        :rtype: list of ScaleInfomation
        """
        return self._ScaleList

    @ScaleList.setter
    def ScaleList(self, ScaleList):
        self._ScaleList = ScaleList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ScaleList") is not None:
            self._ScaleList = []
            for item in params.get("ScaleList"):
                obj = ScaleInfomation()
                obj._deserialize(item)
                self._ScaleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamIngestRequest(AbstractModel):
    r"""DescribeStreamIngest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和任务的房间所对应的SDKAppId相同
        :type SdkAppId: int
        :param _TaskId: 任务的唯一Id，在启动任务成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和任务的房间所对应的SDKAppId相同
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""任务的唯一Id，在启动任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamIngestResponse(AbstractModel):
    r"""DescribeStreamIngest返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务的状态信息。
InProgress：表示当前任务正在进行中。
NotExist：表示当前任务不存在。
示例值：InProgress
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务的状态信息。
InProgress：表示当前任务正在进行中。
NotExist：表示当前任务不存在。
示例值：InProgress
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketQualityDataRequest(AbstractModel):
    r"""DescribeTRTCMarketQualityData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: str
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
        :type EndTime: str
        :param _Period: 返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :type Period: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCMarketQualityDataResponse(AbstractModel):
    r"""DescribeTRTCMarketQualityData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketQualityMetricDataRequest(AbstractModel):
    r"""DescribeTRTCMarketQualityMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: str
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
        :type EndTime: str
        :param _Period: 返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :type Period: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCMarketQualityMetricDataResponse(AbstractModel):
    r"""DescribeTRTCMarketQualityMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketScaleDataRequest(AbstractModel):
    r"""DescribeTRTCMarketScaleData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId
        :type SdkAppId: str
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
        :type EndTime: str
        :param _Period: 返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :type Period: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCMarketScaleDataResponse(AbstractModel):
    r"""DescribeTRTCMarketScaleData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketScaleMetricDataRequest(AbstractModel):
    r"""DescribeTRTCMarketScaleMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId
        :type SdkAppId: str
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
        :type EndTime: str
        :param _Period: 返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :type Period: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。（查询时间范围根据监控仪表盘功能版本而定，【基础版】可查近30天，【进阶版】可查近60天）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""返回数据的粒度，支持设为以下值：
d：按天。此时返回查询时间范围内 UTC 时间为零点的数据。
h：按小时。此时返回查询时间范围内 UTC 时间为整小时的数据。
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCMarketScaleMetricDataResponse(AbstractModel):
    r"""DescribeTRTCMarketScaleMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeQualityDataRequest(AbstractModel):
    r"""DescribeTRTCRealTimeQualityData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: str
        :param _StartTime: 开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间戳，单位：秒
        :type EndTime: int
        :param _RoomId: 房间ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，unix时间戳，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeQualityDataResponse(AbstractModel):
    r"""DescribeTRTCRealTimeQualityData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeQualityMetricDataRequest(AbstractModel):
    r"""DescribeTRTCRealTimeQualityMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: str
        :param _StartTime: 开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间戳，单位：秒
        :type EndTime: int
        :param _RoomId: 房间ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，unix时间戳，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeQualityMetricDataResponse(AbstractModel):
    r"""DescribeTRTCRealTimeQualityMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeScaleDataRequest(AbstractModel):
    r"""DescribeTRTCRealTimeScaleData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: str
        :param _StartTime: 开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间戳，单位：秒
        :type EndTime: int
        :param _RoomId: 房间ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，unix时间戳，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeScaleDataResponse(AbstractModel):
    r"""DescribeTRTCRealTimeScaleData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeScaleMetricDataRequest(AbstractModel):
    r"""DescribeTRTCRealTimeScaleMetricData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: str
        :param _StartTime: 开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间戳，单位：秒
        :type EndTime: int
        :param _RoomId: 房间ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""开始时间，unix时间戳，单位：秒（查询时间范围根据监控仪表盘功能版本而定，基础版可查近3小时，进阶版可查近12小时）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，unix时间戳，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""房间ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeScaleMetricDataResponse(AbstractModel):
    r"""DescribeTRTCRealTimeScaleMetricData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""TRTC监控数据出参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = TRTCDataResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTrtcMcuTranscodeTimeRequest(AbstractModel):
    r"""DescribeTrtcMcuTranscodeTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param _SdkAppId: 应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""应用ID，可不传。传应用ID时返回的是该应用的用量，不传时返回多个应用的合计值。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcMcuTranscodeTimeResponse(AbstractModel):
    r"""DescribeTrtcMcuTranscodeTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Usages: 应用的用量信息数组。
        :type Usages: list of OneSdkAppIdTranscodeTimeUsagesInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Usages = None
        self._RequestId = None

    @property
    def Usages(self):
        r"""应用的用量信息数组。
        :rtype: list of OneSdkAppIdTranscodeTimeUsagesInfo
        """
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Usages") is not None:
            self._Usages = []
            for item in params.get("Usages"):
                obj = OneSdkAppIdTranscodeTimeUsagesInfo()
                obj._deserialize(item)
                self._Usages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrtcRoomUsageRequest(AbstractModel):
    r"""DescribeTrtcRoomUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppid: TRTC的SdkAppId，和房间所对应的SdkAppId相同。
        :type SdkAppid: int
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD HH:MM，精确到分钟级。
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD HH:MM，单次查询不超过24h。
        :type EndTime: str
        """
        self._SdkAppid = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppid(self):
        r"""TRTC的SdkAppId，和房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppid

    @SdkAppid.setter
    def SdkAppid(self, SdkAppid):
        self._SdkAppid = SdkAppid

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD HH:MM，精确到分钟级。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD HH:MM，单次查询不超过24h。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppid = params.get("SdkAppid")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcRoomUsageResponse(AbstractModel):
    r"""DescribeTrtcRoomUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 房间维度用量数据，csv文件格式，单位：秒。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""房间维度用量数据，csv文件格式，单位：秒。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeTrtcUsageRequest(AbstractModel):
    r"""DescribeTrtcUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询开始时间，格式为YYYY-MM-DD。
        :type StartTime: str
        :param _EndTime: 查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :type EndTime: str
        :param _SdkAppId: TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        r"""查询开始时间，格式为YYYY-MM-DD。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，格式为YYYY-MM-DD。
单次查询统计区间最多不能超过31天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId，和房间所对应的SdkAppId相同。如果没有这个参数，返回用户下全部实时音视频应用的汇总。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcUsageResponse(AbstractModel):
    r"""DescribeTrtcUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UsageKey: 用量类型，与UsageValue中各个位置的值对应。
        :type UsageKey: list of str
        :param _UsageList: 各个时间点用量明细，单位:分钟
        :type UsageList: list of TrtcUsage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        r"""用量类型，与UsageValue中各个位置的值对应。
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        r"""各个时间点用量明细，单位:分钟
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUnusualEventRequest(AbstractModel):
    r"""DescribeUnusualEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param _StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :type StartTime: int
        :param _EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）注意：与StartTime间隔时间不超过1小时。
        :type EndTime: int
        :param _RoomId: 房间号，查询房间内任意20条以内异常体验事件
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        r"""查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，本地unix时间戳，单位为秒（如：1590065877）注意：与StartTime间隔时间不超过1小时。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        r"""房间号，查询房间内任意20条以内异常体验事件
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnusualEventResponse(AbstractModel):
    r"""DescribeUnusualEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回的数据总条数
范围：[0，20]
        :type Total: int
        :param _AbnormalExperienceList: 异常体验列表
        :type AbnormalExperienceList: list of AbnormalExperience
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AbnormalExperienceList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回的数据总条数
范围：[0，20]
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AbnormalExperienceList(self):
        r"""异常体验列表
        :rtype: list of AbnormalExperience
        """
        return self._AbnormalExperienceList

    @AbnormalExperienceList.setter
    def AbnormalExperienceList(self, AbnormalExperienceList):
        self._AbnormalExperienceList = AbnormalExperienceList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("AbnormalExperienceList") is not None:
            self._AbnormalExperienceList = []
            for item in params.get("AbnormalExperienceList"):
                obj = AbnormalExperience()
                obj._deserialize(item)
                self._AbnormalExperienceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserEventRequest(AbstractModel):
    r"""DescribeUserEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommId: 通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :type CommId: str
        :param _StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :type StartTime: int
        :param _EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：查询时间大于房间结束时间，以房间结束时间为准。
        :type EndTime: int
        :param _UserId: 用户UserId
        :type UserId: str
        :param _RoomId: 房间号（如：223）
        :type RoomId: str
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._UserId = None
        self._RoomId = None
        self._SdkAppId = None

    @property
    def CommId(self):
        r"""通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        r"""查询开始时间，本地unix时间戳，单位为秒（如：1590065777）
注意：支持查询14天内的数据
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：查询时间大于房间结束时间，以房间结束时间为准。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserId(self):
        r"""用户UserId
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        r"""房间号（如：223）
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserEventResponse(AbstractModel):
    r"""DescribeUserEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回的事件列表，若没有数据，会返回空数组。
        :type Data: list of EventList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回的事件列表，若没有数据，会返回空数组。
        :rtype: list of EventList
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EventList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    r"""DescribeUserInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommId: 通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :type CommId: str
        :param _StartTime: 查询开始时间，本地unix时间戳，单位为秒（如：1590065777）注意：最大支持查询14天内的数据
        :type StartTime: int
        :param _EndTime: 查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：与StartTime间隔时间不超过4小时。
        :type EndTime: int
        :param _SdkAppId: 用户SdkAppId（如：1400xxxxxx）
        :type SdkAppId: int
        :param _UserIds: 需查询的用户数组，不填默认返回6个用户
范围：[1，100]。
        :type UserIds: list of str
        :param _PageNumber: 当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回6条数据。
        :type PageNumber: int
        :param _PageSize: 每页个数，默认为6，
范围：[1，100]。
        :type PageSize: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._UserIds = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def CommId(self):
        r"""通话 ID（唯一标识一次通话）： SdkAppId_RoomId（房间号）_ CreateTime（房间创建时间，unix时间戳，单位为s）例：1400xxxxxx_218695_1590065777。通过 DescribeRoomInfo（查询历史房间列表）接口获取（[查询历史房间列表](https://cloud.tencent.com/document/product/647/44050)）。
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        r"""查询开始时间，本地unix时间戳，单位为秒（如：1590065777）注意：最大支持查询14天内的数据
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""查询结束时间，本地unix时间戳，单位为秒（如：1590065877）
注意：与StartTime间隔时间不超过4小时。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        r"""用户SdkAppId（如：1400xxxxxx）
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        r"""需查询的用户数组，不填默认返回6个用户
范围：[1，100]。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def PageNumber(self):
        r"""当前页数，默认为0，
注意：PageNumber和PageSize 其中一个不填均默认返回6条数据。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页个数，默认为6，
范围：[1，100]。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._UserIds = params.get("UserIds")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    r"""DescribeUserInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 返回的用户总条数
        :type Total: int
        :param _UserList: 用户信息列表
        :type UserList: list of UserInformation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._UserList = None
        self._RequestId = None

    @property
    def Total(self):
        r"""返回的用户总条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        r"""用户信息列表
        :rtype: list of UserInformation
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVoicePrintRequest(AbstractModel):
    r"""DescribeVoicePrint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DescribeMode: 查询方式，0表示查询特定VoicePrintId，1表示分页查询
        :type DescribeMode: int
        :param _VoicePrintIdList: 声纹ID
        :type VoicePrintIdList: list of str
        :param _PageIndex: 当前页码,从1开始,DescribeMode为1时填写
        :type PageIndex: int
        :param _PageSize: 每页条数 最少20,DescribeMode为1时填写
        :type PageSize: int
        """
        self._DescribeMode = None
        self._VoicePrintIdList = None
        self._PageIndex = None
        self._PageSize = None

    @property
    def DescribeMode(self):
        r"""查询方式，0表示查询特定VoicePrintId，1表示分页查询
        :rtype: int
        """
        return self._DescribeMode

    @DescribeMode.setter
    def DescribeMode(self, DescribeMode):
        self._DescribeMode = DescribeMode

    @property
    def VoicePrintIdList(self):
        r"""声纹ID
        :rtype: list of str
        """
        return self._VoicePrintIdList

    @VoicePrintIdList.setter
    def VoicePrintIdList(self, VoicePrintIdList):
        self._VoicePrintIdList = VoicePrintIdList

    @property
    def PageIndex(self):
        r"""当前页码,从1开始,DescribeMode为1时填写
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def PageSize(self):
        r"""每页条数 最少20,DescribeMode为1时填写
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._DescribeMode = params.get("DescribeMode")
        self._VoicePrintIdList = params.get("VoicePrintIdList")
        self._PageIndex = params.get("PageIndex")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVoicePrintResponse(AbstractModel):
    r"""DescribeVoicePrint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总的条数
        :type TotalCount: int
        :param _Data: 声纹信息
        :type Data: list of VoicePrintInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总的条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        r"""声纹信息
        :rtype: list of VoicePrintInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VoicePrintInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWebRecordRequest(AbstractModel):
    r"""DescribeWebRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 开始页面录制时返回的任务id
        :type TaskId: str
        :param _SdkAppId: 发起页面录制时传递的SdkAppId
        :type SdkAppId: int
        :param _RecordId: 发起录制时传递的RecordId, 传入此值时需要传递SdkAppId
        :type RecordId: str
        """
        self._TaskId = None
        self._SdkAppId = None
        self._RecordId = None

    @property
    def TaskId(self):
        r"""开始页面录制时返回的任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SdkAppId(self):
        r"""发起页面录制时传递的SdkAppId
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RecordId(self):
        r"""发起录制时传递的RecordId, 传入此值时需要传递SdkAppId
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SdkAppId = params.get("SdkAppId")
        self._RecordId = params.get("RecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWebRecordResponse(AbstractModel):
    r"""DescribeWebRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 1: 正在录制中
        :type Status: int
        :param _TaskId: 在使用RecordId查询时返回
        :type TaskId: str
        :param _RecordId: 在使用TaskId查询时返回
        :type RecordId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._TaskId = None
        self._RecordId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""1: 正在录制中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""在使用RecordId查询时返回
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordId(self):
        r"""在使用TaskId查询时返回
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class DismissRoomByStrRoomIdRequest(AbstractModel):
    r"""DismissRoomByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _RoomId: 字符串类型房间号。
本接口仅支持解散字符串类型房间号，如需解散数字类型房间号，请使用：DismissRoom
        :type RoomId: str
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""字符串类型房间号。
本接口仅支持解散字符串类型房间号，如需解散数字类型房间号，请使用：DismissRoom
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomByStrRoomIdResponse(AbstractModel):
    r"""DismissRoomByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    r"""DismissRoom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _RoomId: 数字房间号。本接口仅支持解散数字类型房间号，如需解散字符串类型房间号，请使用DismissRoomByStrRoomId。
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""数字房间号。本接口仅支持解散数字类型房间号，如需解散字符串类型房间号，请使用DismissRoomByStrRoomId。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    r"""DismissRoom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EmulateMobileParams(AbstractModel):
    r"""渲染移动模式参数，不渲染移动模式时，请勿设置此参数。

    """

    def __init__(self):
        r"""
        :param _MobileDeviceType: 移动设备类型，
0: 手机
1: 平板
        :type MobileDeviceType: int
        :param _ScreenOrientation: 屏幕方向，
0: 竖屏，
1: 横屏
        :type ScreenOrientation: int
        """
        self._MobileDeviceType = None
        self._ScreenOrientation = None

    @property
    def MobileDeviceType(self):
        r"""移动设备类型，
0: 手机
1: 平板
        :rtype: int
        """
        return self._MobileDeviceType

    @MobileDeviceType.setter
    def MobileDeviceType(self, MobileDeviceType):
        self._MobileDeviceType = MobileDeviceType

    @property
    def ScreenOrientation(self):
        r"""屏幕方向，
0: 竖屏，
1: 横屏
        :rtype: int
        """
        return self._ScreenOrientation

    @ScreenOrientation.setter
    def ScreenOrientation(self, ScreenOrientation):
        self._ScreenOrientation = ScreenOrientation


    def _deserialize(self, params):
        self._MobileDeviceType = params.get("MobileDeviceType")
        self._ScreenOrientation = params.get("ScreenOrientation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncodeParams(AbstractModel):
    r"""MCU混流输出流编码参数

    """

    def __init__(self):
        r"""
        :param _AudioSampleRate: 混流-输出流音频采样率。取值为[48000, 44100, 32000, 24000, 16000, 8000]，单位是Hz。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :type AudioSampleRate: int
        :param _AudioBitrate: 混流-输出流音频码率。取值范围[8,500]，单位为kbps。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :type AudioBitrate: int
        :param _AudioChannels: 混流-输出流音频声道数，取值范围[1,2]，1表示混流输出音频为单声道，2表示混流输出音频为双声道。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :type AudioChannels: int
        :param _VideoWidth: 混流-输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :type VideoWidth: int
        :param _VideoHeight: 混流-输出流高，音视频输出时必填。取值范围[0,1080]，单位为像素值。
        :type VideoHeight: int
        :param _VideoBitrate: 混流-输出流码率，音视频输出时必填。取值范围[1,10000]，单位为kbps。
        :type VideoBitrate: int
        :param _VideoFramerate: 混流-输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :type VideoFramerate: int
        :param _VideoGop: 混流-输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :type VideoGop: int
        :param _BackgroundColor: 混流-输出流背景色，取值是十进制整数。常用的颜色有：
红色：0xff0000，对应的十进制整数是16724736。
黄色：0xffff00。对应的十进制整数是16776960。
绿色：0x33cc00。对应的十进制整数是3394560。
蓝色：0x0066ff。对应的十进制整数是26367。
黑色：0x000000。对应的十进制整数是0。
白色：0xFFFFFF。对应的十进制整数是16777215。
灰色：0x999999。对应的十进制整数是10066329。
        :type BackgroundColor: int
        :param _BackgroundImageId: 混流-输出流背景图片，取值为实时音视频控制台上传的图片ID。
        :type BackgroundImageId: int
        :param _AudioCodec: 混流-输出流音频编码类型，取值范围[0,1, 2]，0为LC-AAC，1为HE-AAC，2为HE-AACv2。默认值为0。当音频编码设置为HE-AACv2时，只支持输出流音频声道数为双声道。HE-AAC和HE-AACv2支持的输出流音频采样率范围为[48000, 44100, 32000, 24000, 16000]。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :type AudioCodec: int
        :param _BackgroundImageUrl: 混流-输出流背景图片URL地址，支持png、jpg、jpeg、bmp格式，暂不支持透明通道。URL链接长度限制为512字节。BackgroundImageUrl和BackgroundImageId参数都填时，以BackgroundImageUrl为准。图片大小限制不超过2MB。
        :type BackgroundImageUrl: str
        """
        self._AudioSampleRate = None
        self._AudioBitrate = None
        self._AudioChannels = None
        self._VideoWidth = None
        self._VideoHeight = None
        self._VideoBitrate = None
        self._VideoFramerate = None
        self._VideoGop = None
        self._BackgroundColor = None
        self._BackgroundImageId = None
        self._AudioCodec = None
        self._BackgroundImageUrl = None

    @property
    def AudioSampleRate(self):
        r"""混流-输出流音频采样率。取值为[48000, 44100, 32000, 24000, 16000, 8000]，单位是Hz。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :rtype: int
        """
        return self._AudioSampleRate

    @AudioSampleRate.setter
    def AudioSampleRate(self, AudioSampleRate):
        self._AudioSampleRate = AudioSampleRate

    @property
    def AudioBitrate(self):
        r"""混流-输出流音频码率。取值范围[8,500]，单位为kbps。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :rtype: int
        """
        return self._AudioBitrate

    @AudioBitrate.setter
    def AudioBitrate(self, AudioBitrate):
        self._AudioBitrate = AudioBitrate

    @property
    def AudioChannels(self):
        r"""混流-输出流音频声道数，取值范围[1,2]，1表示混流输出音频为单声道，2表示混流输出音频为双声道。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :rtype: int
        """
        return self._AudioChannels

    @AudioChannels.setter
    def AudioChannels(self, AudioChannels):
        self._AudioChannels = AudioChannels

    @property
    def VideoWidth(self):
        r"""混流-输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :rtype: int
        """
        return self._VideoWidth

    @VideoWidth.setter
    def VideoWidth(self, VideoWidth):
        self._VideoWidth = VideoWidth

    @property
    def VideoHeight(self):
        r"""混流-输出流高，音视频输出时必填。取值范围[0,1080]，单位为像素值。
        :rtype: int
        """
        return self._VideoHeight

    @VideoHeight.setter
    def VideoHeight(self, VideoHeight):
        self._VideoHeight = VideoHeight

    @property
    def VideoBitrate(self):
        r"""混流-输出流码率，音视频输出时必填。取值范围[1,10000]，单位为kbps。
        :rtype: int
        """
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def VideoFramerate(self):
        r"""混流-输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :rtype: int
        """
        return self._VideoFramerate

    @VideoFramerate.setter
    def VideoFramerate(self, VideoFramerate):
        self._VideoFramerate = VideoFramerate

    @property
    def VideoGop(self):
        r"""混流-输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :rtype: int
        """
        return self._VideoGop

    @VideoGop.setter
    def VideoGop(self, VideoGop):
        self._VideoGop = VideoGop

    @property
    def BackgroundColor(self):
        r"""混流-输出流背景色，取值是十进制整数。常用的颜色有：
红色：0xff0000，对应的十进制整数是16724736。
黄色：0xffff00。对应的十进制整数是16776960。
绿色：0x33cc00。对应的十进制整数是3394560。
蓝色：0x0066ff。对应的十进制整数是26367。
黑色：0x000000。对应的十进制整数是0。
白色：0xFFFFFF。对应的十进制整数是16777215。
灰色：0x999999。对应的十进制整数是10066329。
        :rtype: int
        """
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor

    @property
    def BackgroundImageId(self):
        r"""混流-输出流背景图片，取值为实时音视频控制台上传的图片ID。
        :rtype: int
        """
        return self._BackgroundImageId

    @BackgroundImageId.setter
    def BackgroundImageId(self, BackgroundImageId):
        self._BackgroundImageId = BackgroundImageId

    @property
    def AudioCodec(self):
        r"""混流-输出流音频编码类型，取值范围[0,1, 2]，0为LC-AAC，1为HE-AAC，2为HE-AACv2。默认值为0。当音频编码设置为HE-AACv2时，只支持输出流音频声道数为双声道。HE-AAC和HE-AACv2支持的输出流音频采样率范围为[48000, 44100, 32000, 24000, 16000]。混流任务发起过程中，为了保持CDN链接的稳定，不要修改音频参数（codec、采样率、码率、声道数）。
        :rtype: int
        """
        return self._AudioCodec

    @AudioCodec.setter
    def AudioCodec(self, AudioCodec):
        self._AudioCodec = AudioCodec

    @property
    def BackgroundImageUrl(self):
        r"""混流-输出流背景图片URL地址，支持png、jpg、jpeg、bmp格式，暂不支持透明通道。URL链接长度限制为512字节。BackgroundImageUrl和BackgroundImageId参数都填时，以BackgroundImageUrl为准。图片大小限制不超过2MB。
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl


    def _deserialize(self, params):
        self._AudioSampleRate = params.get("AudioSampleRate")
        self._AudioBitrate = params.get("AudioBitrate")
        self._AudioChannels = params.get("AudioChannels")
        self._VideoWidth = params.get("VideoWidth")
        self._VideoHeight = params.get("VideoHeight")
        self._VideoBitrate = params.get("VideoBitrate")
        self._VideoFramerate = params.get("VideoFramerate")
        self._VideoGop = params.get("VideoGop")
        self._BackgroundColor = params.get("BackgroundColor")
        self._BackgroundImageId = params.get("BackgroundImageId")
        self._AudioCodec = params.get("AudioCodec")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventList(AbstractModel):
    r"""sdk或webrtc的事件列表。

    """

    def __init__(self):
        r"""
        :param _Content: 数据内容
        :type Content: list of EventMessage
        :param _PeerId: 发送端的userId
        :type PeerId: str
        """
        self._Content = None
        self._PeerId = None

    @property
    def Content(self):
        r"""数据内容
        :rtype: list of EventMessage
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def PeerId(self):
        r"""发送端的userId
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = EventMessage()
                obj._deserialize(item)
                self._Content.append(obj)
        self._PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventMessage(AbstractModel):
    r"""事件信息，包括，事件时间戳，事件ID,

    """

    def __init__(self):
        r"""
        :param _Type: 视频流类型：
0：与视频无关的事件；
2：视频为大画面；
3：视频为小画面；
7：视频为旁路画面；
        :type Type: int
        :param _Time: 事件上报的时间戳，unix时间（1589891188801ms)
        :type Time: int
        :param _EventId: 事件Id：分为sdk的事件和webrtc的事件，详情见：附录/事件 ID 映射表：https://cloud.tencent.com/document/product/647/44916
        :type EventId: int
        :param _ParamOne: 事件的第一个参数，如视频分辨率宽
        :type ParamOne: int
        :param _ParamTwo: 事件的第二个参数，如视频分辨率高
        :type ParamTwo: int
        """
        self._Type = None
        self._Time = None
        self._EventId = None
        self._ParamOne = None
        self._ParamTwo = None

    @property
    def Type(self):
        r"""视频流类型：
0：与视频无关的事件；
2：视频为大画面；
3：视频为小画面；
7：视频为旁路画面；
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        r"""事件上报的时间戳，unix时间（1589891188801ms)
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def EventId(self):
        r"""事件Id：分为sdk的事件和webrtc的事件，详情见：附录/事件 ID 映射表：https://cloud.tencent.com/document/product/647/44916
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def ParamOne(self):
        r"""事件的第一个参数，如视频分辨率宽
        :rtype: int
        """
        return self._ParamOne

    @ParamOne.setter
    def ParamOne(self, ParamOne):
        self._ParamOne = ParamOne

    @property
    def ParamTwo(self):
        r"""事件的第二个参数，如视频分辨率高
        :rtype: int
        """
        return self._ParamTwo

    @ParamTwo.setter
    def ParamTwo(self, ParamTwo):
        self._ParamTwo = ParamTwo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        self._EventId = params.get("EventId")
        self._ParamOne = params.get("ParamOne")
        self._ParamTwo = params.get("ParamTwo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeLLM(AbstractModel):
    r"""调用服务端主动发起请求到LLM

    """

    def __init__(self):
        r"""
        :param _Content: 请求LLM的内容
        :type Content: str
        :param _Interrupt: 是否允许该文本打断机器人说话
        :type Interrupt: bool
        """
        self._Content = None
        self._Interrupt = None

    @property
    def Content(self):
        r"""请求LLM的内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Interrupt(self):
        r"""是否允许该文本打断机器人说话
        :rtype: bool
        """
        return self._Interrupt

    @Interrupt.setter
    def Interrupt(self, Interrupt):
        self._Interrupt = Interrupt


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Interrupt = params.get("Interrupt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayoutParams(AbstractModel):
    r"""MCU混流布局参数

    """

    def __init__(self):
        r"""
        :param _Template: 混流布局模板ID，0为悬浮模板(默认);1为九宫格模板;2为屏幕分享模板;3为画中画模板;4为自定义模板。
        :type Template: int
        :param _MainVideoUserId: 屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的用户ID。
        :type MainVideoUserId: str
        :param _MainVideoStreamType: 屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的流类型，0为摄像头，1为屏幕分享。左侧大画面为web用户时此值填0。
        :type MainVideoStreamType: int
        :param _SmallVideoLayoutParams: 画中画模板中有效，代表小画面的布局参数。
        :type SmallVideoLayoutParams: :class:`tencentcloud.trtc.v20190722.models.SmallVideoLayoutParams`
        :param _MainVideoRightAlign: 屏幕分享模板有效。设置为1时代表大画面居右，小画面居左布局。默认为0。
        :type MainVideoRightAlign: int
        :param _MixVideoUids: 指定混视频的用户ID列表。设置此参数后，输出流混合此参数中包含用户的音视频，以及其他用户的纯音频。悬浮模板、九宫格、屏幕分享模板有效，最多可设置16个用户。
        :type MixVideoUids: list of str
        :param _PresetLayoutConfig: 自定义模板中有效，指定用户视频在混合画面中的位置。
        :type PresetLayoutConfig: list of PresetLayoutConfig
        :param _PlaceHolderMode: 自定义模板中有效，设置为1时代表启用占位图功能，0时代表不启用占位图功能，默认为0。启用占位图功能时，在预设位置的用户没有上行视频时可显示对应的占位图。
        :type PlaceHolderMode: int
        :param _PureAudioHoldPlaceMode: 悬浮模板、九宫格、屏幕分享模板生效，用于控制纯音频上行是否占用画面布局位置。设置为0是代表后台默认处理方式，悬浮小画面占布局位置，九宫格画面占布局位置、屏幕分享小画面不占布局位置；设置为1时代表纯音频上行占布局位置；设置为2时代表纯音频上行不占布局位置。默认为0。
        :type PureAudioHoldPlaceMode: int
        :param _WaterMarkParams: 水印参数。
        :type WaterMarkParams: :class:`tencentcloud.trtc.v20190722.models.WaterMarkParams`
        :param _RenderMode: 屏幕分享模板、悬浮模板、九宫格模板、画中画模版有效，画面在输出时的显示模式：0为裁剪，1为缩放，2为缩放并显示黑底，不填采用后台的默认渲染方式（屏幕分享大画面为缩放，其他为裁剪）。若此参数不生效，请提交工单寻求帮助。
        :type RenderMode: int
        """
        self._Template = None
        self._MainVideoUserId = None
        self._MainVideoStreamType = None
        self._SmallVideoLayoutParams = None
        self._MainVideoRightAlign = None
        self._MixVideoUids = None
        self._PresetLayoutConfig = None
        self._PlaceHolderMode = None
        self._PureAudioHoldPlaceMode = None
        self._WaterMarkParams = None
        self._RenderMode = None

    @property
    def Template(self):
        r"""混流布局模板ID，0为悬浮模板(默认);1为九宫格模板;2为屏幕分享模板;3为画中画模板;4为自定义模板。
        :rtype: int
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def MainVideoUserId(self):
        r"""屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的用户ID。
        :rtype: str
        """
        return self._MainVideoUserId

    @MainVideoUserId.setter
    def MainVideoUserId(self, MainVideoUserId):
        self._MainVideoUserId = MainVideoUserId

    @property
    def MainVideoStreamType(self):
        r"""屏幕分享模板、悬浮模板、画中画模板中有效，代表大画面对应的流类型，0为摄像头，1为屏幕分享。左侧大画面为web用户时此值填0。
        :rtype: int
        """
        return self._MainVideoStreamType

    @MainVideoStreamType.setter
    def MainVideoStreamType(self, MainVideoStreamType):
        self._MainVideoStreamType = MainVideoStreamType

    @property
    def SmallVideoLayoutParams(self):
        r"""画中画模板中有效，代表小画面的布局参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SmallVideoLayoutParams`
        """
        return self._SmallVideoLayoutParams

    @SmallVideoLayoutParams.setter
    def SmallVideoLayoutParams(self, SmallVideoLayoutParams):
        self._SmallVideoLayoutParams = SmallVideoLayoutParams

    @property
    def MainVideoRightAlign(self):
        r"""屏幕分享模板有效。设置为1时代表大画面居右，小画面居左布局。默认为0。
        :rtype: int
        """
        return self._MainVideoRightAlign

    @MainVideoRightAlign.setter
    def MainVideoRightAlign(self, MainVideoRightAlign):
        self._MainVideoRightAlign = MainVideoRightAlign

    @property
    def MixVideoUids(self):
        r"""指定混视频的用户ID列表。设置此参数后，输出流混合此参数中包含用户的音视频，以及其他用户的纯音频。悬浮模板、九宫格、屏幕分享模板有效，最多可设置16个用户。
        :rtype: list of str
        """
        return self._MixVideoUids

    @MixVideoUids.setter
    def MixVideoUids(self, MixVideoUids):
        self._MixVideoUids = MixVideoUids

    @property
    def PresetLayoutConfig(self):
        r"""自定义模板中有效，指定用户视频在混合画面中的位置。
        :rtype: list of PresetLayoutConfig
        """
        return self._PresetLayoutConfig

    @PresetLayoutConfig.setter
    def PresetLayoutConfig(self, PresetLayoutConfig):
        self._PresetLayoutConfig = PresetLayoutConfig

    @property
    def PlaceHolderMode(self):
        r"""自定义模板中有效，设置为1时代表启用占位图功能，0时代表不启用占位图功能，默认为0。启用占位图功能时，在预设位置的用户没有上行视频时可显示对应的占位图。
        :rtype: int
        """
        return self._PlaceHolderMode

    @PlaceHolderMode.setter
    def PlaceHolderMode(self, PlaceHolderMode):
        self._PlaceHolderMode = PlaceHolderMode

    @property
    def PureAudioHoldPlaceMode(self):
        r"""悬浮模板、九宫格、屏幕分享模板生效，用于控制纯音频上行是否占用画面布局位置。设置为0是代表后台默认处理方式，悬浮小画面占布局位置，九宫格画面占布局位置、屏幕分享小画面不占布局位置；设置为1时代表纯音频上行占布局位置；设置为2时代表纯音频上行不占布局位置。默认为0。
        :rtype: int
        """
        return self._PureAudioHoldPlaceMode

    @PureAudioHoldPlaceMode.setter
    def PureAudioHoldPlaceMode(self, PureAudioHoldPlaceMode):
        self._PureAudioHoldPlaceMode = PureAudioHoldPlaceMode

    @property
    def WaterMarkParams(self):
        r"""水印参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkParams`
        """
        return self._WaterMarkParams

    @WaterMarkParams.setter
    def WaterMarkParams(self, WaterMarkParams):
        self._WaterMarkParams = WaterMarkParams

    @property
    def RenderMode(self):
        r"""屏幕分享模板、悬浮模板、九宫格模板、画中画模版有效，画面在输出时的显示模式：0为裁剪，1为缩放，2为缩放并显示黑底，不填采用后台的默认渲染方式（屏幕分享大画面为缩放，其他为裁剪）。若此参数不生效，请提交工单寻求帮助。
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode


    def _deserialize(self, params):
        self._Template = params.get("Template")
        self._MainVideoUserId = params.get("MainVideoUserId")
        self._MainVideoStreamType = params.get("MainVideoStreamType")
        if params.get("SmallVideoLayoutParams") is not None:
            self._SmallVideoLayoutParams = SmallVideoLayoutParams()
            self._SmallVideoLayoutParams._deserialize(params.get("SmallVideoLayoutParams"))
        self._MainVideoRightAlign = params.get("MainVideoRightAlign")
        self._MixVideoUids = params.get("MixVideoUids")
        if params.get("PresetLayoutConfig") is not None:
            self._PresetLayoutConfig = []
            for item in params.get("PresetLayoutConfig"):
                obj = PresetLayoutConfig()
                obj._deserialize(item)
                self._PresetLayoutConfig.append(obj)
        self._PlaceHolderMode = params.get("PlaceHolderMode")
        self._PureAudioHoldPlaceMode = params.get("PureAudioHoldPlaceMode")
        if params.get("WaterMarkParams") is not None:
            self._WaterMarkParams = WaterMarkParams()
            self._WaterMarkParams._deserialize(params.get("WaterMarkParams"))
        self._RenderMode = params.get("RenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxVideoUser(AbstractModel):
    r"""指定动态布局中悬浮布局和屏幕分享布局的大画面信息，只在悬浮布局和屏幕分享布局有效。

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: 用户媒体流参数。
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self._UserMediaStream = None

    @property
    def UserMediaStream(self):
        r"""用户媒体流参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuAudioParams(AbstractModel):
    r"""混流转推的音频相关参数。

    """

    def __init__(self):
        r"""
        :param _AudioEncode: 音频编码参数。
        :type AudioEncode: :class:`tencentcloud.trtc.v20190722.models.AudioEncode`
        :param _SubscribeAudioList: 音频用户白名单，start时，为空或不填表示混所有主播音频，填具体值表示混指定主播音频；update时，不填表示不更新，为空表示更新为混所有主播音频，填具体值表示更新为混指定主播音频。
使用黑白名单时，黑白名单必须同时填写。都不填写时表示不更新。同一个用户同时在黑白名单时，以黑名单为主。
注：如果是跨房pk时，跨房混流需要指定音频白名单，否则pk主播的的音频上行会被拉到两次，产生重音。
        :type SubscribeAudioList: list of McuUserInfoParams
        :param _UnSubscribeAudioList: 音频用户黑名单，为空或不填表示无黑名单，填具体值表示不混指定主播音频。update时，不填表示不更新，为空表示更新为清空黑名单，填具体值表示更新为不混指定主播音频。
使用黑白名单时，黑白名单必须同时填写。都不填写时表示不更新。同一个用户同时在黑白名单时，以黑名单为主。
        :type UnSubscribeAudioList: list of McuUserInfoParams
        """
        self._AudioEncode = None
        self._SubscribeAudioList = None
        self._UnSubscribeAudioList = None

    @property
    def AudioEncode(self):
        r"""音频编码参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioEncode`
        """
        return self._AudioEncode

    @AudioEncode.setter
    def AudioEncode(self, AudioEncode):
        self._AudioEncode = AudioEncode

    @property
    def SubscribeAudioList(self):
        r"""音频用户白名单，start时，为空或不填表示混所有主播音频，填具体值表示混指定主播音频；update时，不填表示不更新，为空表示更新为混所有主播音频，填具体值表示更新为混指定主播音频。
使用黑白名单时，黑白名单必须同时填写。都不填写时表示不更新。同一个用户同时在黑白名单时，以黑名单为主。
注：如果是跨房pk时，跨房混流需要指定音频白名单，否则pk主播的的音频上行会被拉到两次，产生重音。
        :rtype: list of McuUserInfoParams
        """
        return self._SubscribeAudioList

    @SubscribeAudioList.setter
    def SubscribeAudioList(self, SubscribeAudioList):
        self._SubscribeAudioList = SubscribeAudioList

    @property
    def UnSubscribeAudioList(self):
        r"""音频用户黑名单，为空或不填表示无黑名单，填具体值表示不混指定主播音频。update时，不填表示不更新，为空表示更新为清空黑名单，填具体值表示更新为不混指定主播音频。
使用黑白名单时，黑白名单必须同时填写。都不填写时表示不更新。同一个用户同时在黑白名单时，以黑名单为主。
        :rtype: list of McuUserInfoParams
        """
        return self._UnSubscribeAudioList

    @UnSubscribeAudioList.setter
    def UnSubscribeAudioList(self, UnSubscribeAudioList):
        self._UnSubscribeAudioList = UnSubscribeAudioList


    def _deserialize(self, params):
        if params.get("AudioEncode") is not None:
            self._AudioEncode = AudioEncode()
            self._AudioEncode._deserialize(params.get("AudioEncode"))
        if params.get("SubscribeAudioList") is not None:
            self._SubscribeAudioList = []
            for item in params.get("SubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self._SubscribeAudioList.append(obj)
        if params.get("UnSubscribeAudioList") is not None:
            self._UnSubscribeAudioList = []
            for item in params.get("UnSubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self._UnSubscribeAudioList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuBackgroundCustomRender(AbstractModel):
    r"""混流自定义渲染参数

    """

    def __init__(self):
        r"""
        :param _Width: 自定义渲染画面的宽度，单位为像素值，需大于0，且不能超过子布局的宽。
        :type Width: int
        :param _Height: 自定义渲染画面的高度，单位为像素值，需大于0，且不能超过子布局的高。
        :type Height: int
        :param _Radius: 自定义渲染画面的圆角半径，单位为像素值，不能超过渲染画面Width和Height最小值的一半，不指定默认为0，表示直角。
        :type Radius: int
        """
        self._Width = None
        self._Height = None
        self._Radius = None

    @property
    def Width(self):
        r"""自定义渲染画面的宽度，单位为像素值，需大于0，且不能超过子布局的宽。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""自定义渲染画面的高度，单位为像素值，需大于0，且不能超过子布局的高。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Radius(self):
        r"""自定义渲染画面的圆角半径，单位为像素值，不能超过渲染画面Width和Height最小值的一半，不指定默认为0，表示直角。
        :rtype: int
        """
        return self._Radius

    @Radius.setter
    def Radius(self, Radius):
        self._Radius = Radius


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Radius = params.get("Radius")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuCloudVod(AbstractModel):
    r"""Mcu转推录制，点播相关参数。

    """

    def __init__(self):
        r"""
        :param _McuTencentVod: 腾讯云点播相关参数。	
        :type McuTencentVod: :class:`tencentcloud.trtc.v20190722.models.McuTencentVod`
        """
        self._McuTencentVod = None

    @property
    def McuTencentVod(self):
        r"""腾讯云点播相关参数。	
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuTencentVod`
        """
        return self._McuTencentVod

    @McuTencentVod.setter
    def McuTencentVod(self, McuTencentVod):
        self._McuTencentVod = McuTencentVod


    def _deserialize(self, params):
        if params.get("McuTencentVod") is not None:
            self._McuTencentVod = McuTencentVod()
            self._McuTencentVod._deserialize(params.get("McuTencentVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuCustomCrop(AbstractModel):
    r"""混流自定义裁剪参数

    """

    def __init__(self):
        r"""
        :param _LocationX: 自定义裁剪起始位置的X偏移，单位为像素值，大于等于0。
        :type LocationX: int
        :param _LocationY: 自定义裁剪起始位置的Y偏移，单位为像素值，大于等于0。
        :type LocationY: int
        :param _Width: 自定义裁剪画面的宽度，单位为像素值，大于0，且LocationX+Width不超过10000
        :type Width: int
        :param _Height: 自定义裁剪画面的高度，单位为像素值，大于0，且LocationY+Height不超过10000
        :type Height: int
        """
        self._LocationX = None
        self._LocationY = None
        self._Width = None
        self._Height = None

    @property
    def LocationX(self):
        r"""自定义裁剪起始位置的X偏移，单位为像素值，大于等于0。
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""自定义裁剪起始位置的Y偏移，单位为像素值，大于等于0。
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def Width(self):
        r"""自定义裁剪画面的宽度，单位为像素值，大于0，且LocationX+Width不超过10000
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""自定义裁剪画面的高度，单位为像素值，大于0，且LocationY+Height不超过10000
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuFeedBackRoomParams(AbstractModel):
    r"""回推房间参数。

    """

    def __init__(self):
        r"""
        :param _RoomId: 回推房间的RoomId。
        :type RoomId: str
        :param _RoomIdType: 房间类型，必须和回推房间所对应的RoomId类型相同，0为整形房间号，1为字符串房间号。
        :type RoomIdType: int
        :param _UserId: 回推房间使用的UserId(https://cloud.tencent.com/document/product/647/46351#userid)，注意这个userId不能与其他TRTC或者转推服务等已经使用的UserId重复，建议可以把房间ID作为userId的标识的一部分。
        :type UserId: str
        :param _UserSig: 回推房间UserId对应的用户签名，相当于登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :type UserSig: str
        """
        self._RoomId = None
        self._RoomIdType = None
        self._UserId = None
        self._UserSig = None

    @property
    def RoomId(self):
        r"""回推房间的RoomId。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""房间类型，必须和回推房间所对应的RoomId类型相同，0为整形房间号，1为字符串房间号。
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        r"""回推房间使用的UserId(https://cloud.tencent.com/document/product/647/46351#userid)，注意这个userId不能与其他TRTC或者转推服务等已经使用的UserId重复，建议可以把房间ID作为userId的标识的一部分。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""回推房间UserId对应的用户签名，相当于登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayout(AbstractModel):
    r"""混流布局参数。

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: 用户媒体流参数。不填时腾讯云后台按照上行主播的进房顺序自动填充。
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        :param _ImageWidth: 子画面在输出时的宽度，单位为像素值，不填默认为0。
        :type ImageWidth: int
        :param _ImageHeight: 子画面在输出时的高度，单位为像素值，不填默认为0。
        :type ImageHeight: int
        :param _LocationX: 子画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :type LocationX: int
        :param _LocationY: 子画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :type LocationY: int
        :param _ZOrder: 子画面在输出时的层级，不填默认为0。
        :type ZOrder: int
        :param _RenderMode: 子画面在输出时的显示模式：0为裁剪，1为缩放并显示背景，2为缩放并显示黑底。不填默认为0。
        :type RenderMode: int
        :param _BackGroundColor: 【此参数配置无效，暂不支持】子画面的背景颜色，常用的颜色有：
红色：0xcc0033。
黄色：0xcc9900。
绿色：0xcccc33。
蓝色：0x99CCFF。
黑色：0x000000。
白色：0xFFFFFF。
灰色：0x999999。
        :type BackGroundColor: str
        :param _BackgroundImageUrl: 子画面的占位图片url，填写该参数，当用户关闭摄像头或未进入TRTC房间时，会在布局位置填充为指定图片。若指定图片与布局位置尺寸比例不一致，则会对图片进行拉伸处理，优先级高于BackGroundColor。支持png、jpg、jpeg、bmp、gif、webm格式。图片大小限制不超过5MB。
注：
1，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，占位图片将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，占位图片将不会生效。
        :type BackgroundImageUrl: str
        :param _CustomCrop: 客户自定义裁剪，针对原始输入流裁剪
        :type CustomCrop: :class:`tencentcloud.trtc.v20190722.models.McuCustomCrop`
        :param _BackgroundRenderMode: 子背景图在输出时的显示模式：0为裁剪，1为缩放并显示背景，2为缩放并显示黑底，3为变比例伸缩，4为自定义渲染。不填默认为3。
        :type BackgroundRenderMode: int
        :param _TransparentUrl: 子画面的透明模版url，指向一张包含透明通道的模板图片。填写该参数，后台混流时会提取该模板图片的透明通道，将其缩放作为目标画面的透明通道，再和其他画面进行混合。您可以通过透明模版实现目标画面的半透明效果和任意形状裁剪（如圆角、星形、心形等）。 支持png格式。图片大小限制不超过5MB。
注：
1，模板图片宽高比应接近目标画面宽高比，以避免缩放适配目标画面时出现模板效果变形；2，透明模版只有RenderMode为0（裁剪）时才生效；3，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，透明模版将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，透明模版将不会生效。
        :type TransparentUrl: str
        :param _BackgroundCustomRender: 子背景图的自定义渲染参数，当BackgroundRenderMode为4时必须配置。
        :type BackgroundCustomRender: :class:`tencentcloud.trtc.v20190722.models.McuBackgroundCustomRender`
        :param _BackGroundColorMode: 子背景色生效模式，默认值为0表示均不生效。
bit0:占位图缩放是否生效。
bit1:上行流缩放是否生效。
您可以将相应bit位置1启动生效，例如：
0(00)表示子背景色不生效。
1(01)表示子背景色只在占位图缩放时生效。
2(10)表示子背景色只在上行流缩放时生效。
3(11)表示子背景色在占位图缩放和上行流缩放时均生效。

        :type BackGroundColorMode: int
        """
        self._UserMediaStream = None
        self._ImageWidth = None
        self._ImageHeight = None
        self._LocationX = None
        self._LocationY = None
        self._ZOrder = None
        self._RenderMode = None
        self._BackGroundColor = None
        self._BackgroundImageUrl = None
        self._CustomCrop = None
        self._BackgroundRenderMode = None
        self._TransparentUrl = None
        self._BackgroundCustomRender = None
        self._BackGroundColorMode = None

    @property
    def UserMediaStream(self):
        r"""用户媒体流参数。不填时腾讯云后台按照上行主播的进房顺序自动填充。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream

    @property
    def ImageWidth(self):
        r"""子画面在输出时的宽度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        r"""子画面在输出时的高度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def LocationX(self):
        r"""子画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""子画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        r"""子画面在输出时的层级，不填默认为0。
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def RenderMode(self):
        r"""子画面在输出时的显示模式：0为裁剪，1为缩放并显示背景，2为缩放并显示黑底。不填默认为0。
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def BackGroundColor(self):
        r"""【此参数配置无效，暂不支持】子画面的背景颜色，常用的颜色有：
红色：0xcc0033。
黄色：0xcc9900。
绿色：0xcccc33。
蓝色：0x99CCFF。
黑色：0x000000。
白色：0xFFFFFF。
灰色：0x999999。
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        r"""子画面的占位图片url，填写该参数，当用户关闭摄像头或未进入TRTC房间时，会在布局位置填充为指定图片。若指定图片与布局位置尺寸比例不一致，则会对图片进行拉伸处理，优先级高于BackGroundColor。支持png、jpg、jpeg、bmp、gif、webm格式。图片大小限制不超过5MB。
注：
1，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，占位图片将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，占位图片将不会生效。
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def CustomCrop(self):
        r"""客户自定义裁剪，针对原始输入流裁剪
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuCustomCrop`
        """
        return self._CustomCrop

    @CustomCrop.setter
    def CustomCrop(self, CustomCrop):
        self._CustomCrop = CustomCrop

    @property
    def BackgroundRenderMode(self):
        r"""子背景图在输出时的显示模式：0为裁剪，1为缩放并显示背景，2为缩放并显示黑底，3为变比例伸缩，4为自定义渲染。不填默认为3。
        :rtype: int
        """
        return self._BackgroundRenderMode

    @BackgroundRenderMode.setter
    def BackgroundRenderMode(self, BackgroundRenderMode):
        self._BackgroundRenderMode = BackgroundRenderMode

    @property
    def TransparentUrl(self):
        r"""子画面的透明模版url，指向一张包含透明通道的模板图片。填写该参数，后台混流时会提取该模板图片的透明通道，将其缩放作为目标画面的透明通道，再和其他画面进行混合。您可以通过透明模版实现目标画面的半透明效果和任意形状裁剪（如圆角、星形、心形等）。 支持png格式。图片大小限制不超过5MB。
注：
1，模板图片宽高比应接近目标画面宽高比，以避免缩放适配目标画面时出现模板效果变形；2，透明模版只有RenderMode为0（裁剪）时才生效；3，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，透明模版将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，透明模版将不会生效。
        :rtype: str
        """
        return self._TransparentUrl

    @TransparentUrl.setter
    def TransparentUrl(self, TransparentUrl):
        self._TransparentUrl = TransparentUrl

    @property
    def BackgroundCustomRender(self):
        r"""子背景图的自定义渲染参数，当BackgroundRenderMode为4时必须配置。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuBackgroundCustomRender`
        """
        return self._BackgroundCustomRender

    @BackgroundCustomRender.setter
    def BackgroundCustomRender(self, BackgroundCustomRender):
        self._BackgroundCustomRender = BackgroundCustomRender

    @property
    def BackGroundColorMode(self):
        r"""子背景色生效模式，默认值为0表示均不生效。
bit0:占位图缩放是否生效。
bit1:上行流缩放是否生效。
您可以将相应bit位置1启动生效，例如：
0(00)表示子背景色不生效。
1(01)表示子背景色只在占位图缩放时生效。
2(10)表示子背景色只在上行流缩放时生效。
3(11)表示子背景色在占位图缩放和上行流缩放时均生效。

        :rtype: int
        """
        return self._BackGroundColorMode

    @BackGroundColorMode.setter
    def BackGroundColorMode(self, BackGroundColorMode):
        self._BackGroundColorMode = BackGroundColorMode


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._ZOrder = params.get("ZOrder")
        self._RenderMode = params.get("RenderMode")
        self._BackGroundColor = params.get("BackGroundColor")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("CustomCrop") is not None:
            self._CustomCrop = McuCustomCrop()
            self._CustomCrop._deserialize(params.get("CustomCrop"))
        self._BackgroundRenderMode = params.get("BackgroundRenderMode")
        self._TransparentUrl = params.get("TransparentUrl")
        if params.get("BackgroundCustomRender") is not None:
            self._BackgroundCustomRender = McuBackgroundCustomRender()
            self._BackgroundCustomRender._deserialize(params.get("BackgroundCustomRender"))
        self._BackGroundColorMode = params.get("BackGroundColorMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutParams(AbstractModel):
    r"""混流布局参数。

    """

    def __init__(self):
        r"""
        :param _MixLayoutMode: 布局模式：动态布局（1：悬浮布局（默认），2：屏幕分享布局，3：九宫格布局），静态布局（4：自定义布局）。最多支持混入16路音视频流，如果用户只上行音频，也会被算作一路；自定义布局中，如果子画面只设置占位图，也被算作一路。
        :type MixLayoutMode: int
        :param _PureAudioHoldPlaceMode: 纯音频上行是否占布局位置，只在动态布局中有效。0表示纯音频不占布局位置，1表示纯音频占布局位置，不填默认为0。
        :type PureAudioHoldPlaceMode: int
        :param _MixLayoutList: 自定义模板中有效，指定用户视频在混合画面中的位置，最多支持设置16个输入流。
        :type MixLayoutList: list of McuLayout
        :param _MaxVideoUser: 指定动态布局中悬浮布局和屏幕分享布局的大画面信息，只在悬浮布局和屏幕分享布局有效。
        :type MaxVideoUser: :class:`tencentcloud.trtc.v20190722.models.MaxVideoUser`
        :param _RenderMode: 屏幕分享模板、悬浮模板、九宫格模版有效，画面在输出时的显示模式：0为裁剪，1为缩放，2为缩放并显示黑底
        :type RenderMode: int
        """
        self._MixLayoutMode = None
        self._PureAudioHoldPlaceMode = None
        self._MixLayoutList = None
        self._MaxVideoUser = None
        self._RenderMode = None

    @property
    def MixLayoutMode(self):
        r"""布局模式：动态布局（1：悬浮布局（默认），2：屏幕分享布局，3：九宫格布局），静态布局（4：自定义布局）。最多支持混入16路音视频流，如果用户只上行音频，也会被算作一路；自定义布局中，如果子画面只设置占位图，也被算作一路。
        :rtype: int
        """
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def PureAudioHoldPlaceMode(self):
        r"""纯音频上行是否占布局位置，只在动态布局中有效。0表示纯音频不占布局位置，1表示纯音频占布局位置，不填默认为0。
        :rtype: int
        """
        return self._PureAudioHoldPlaceMode

    @PureAudioHoldPlaceMode.setter
    def PureAudioHoldPlaceMode(self, PureAudioHoldPlaceMode):
        self._PureAudioHoldPlaceMode = PureAudioHoldPlaceMode

    @property
    def MixLayoutList(self):
        r"""自定义模板中有效，指定用户视频在混合画面中的位置，最多支持设置16个输入流。
        :rtype: list of McuLayout
        """
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def MaxVideoUser(self):
        r"""指定动态布局中悬浮布局和屏幕分享布局的大画面信息，只在悬浮布局和屏幕分享布局有效。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MaxVideoUser`
        """
        return self._MaxVideoUser

    @MaxVideoUser.setter
    def MaxVideoUser(self, MaxVideoUser):
        self._MaxVideoUser = MaxVideoUser

    @property
    def RenderMode(self):
        r"""屏幕分享模板、悬浮模板、九宫格模版有效，画面在输出时的显示模式：0为裁剪，1为缩放，2为缩放并显示黑底
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode


    def _deserialize(self, params):
        self._MixLayoutMode = params.get("MixLayoutMode")
        self._PureAudioHoldPlaceMode = params.get("PureAudioHoldPlaceMode")
        if params.get("MixLayoutList") is not None:
            self._MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = McuLayout()
                obj._deserialize(item)
                self._MixLayoutList.append(obj)
        if params.get("MaxVideoUser") is not None:
            self._MaxVideoUser = MaxVideoUser()
            self._MaxVideoUser._deserialize(params.get("MaxVideoUser"))
        self._RenderMode = params.get("RenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutVolume(AbstractModel):
    r"""音量布局SEI参数，可以自定义AppData和PayloadType类型。
    该参数内容可以为空，表示携带默认的音量布局SEI。

    """

    def __init__(self):
        r"""
        :param _AppData: AppData的内容，会被写入自定义SEI中的app_data字段，长度需小于4096。
        :type AppData: str
        :param _PayloadType: SEI消息的payload_type，默认值100，取值范围100-254（244除外，244为我们内部自定义的时间戳SEI）
        :type PayloadType: int
        :param _Interval: SEI发送间隔，单位毫秒，默认值为1000。
        :type Interval: int
        :param _FollowIdr: 取值范围[0,1]，填1：发送关键帧时会确保带SEI；填0：发送关键帧时不确保带SEI。默认值为0。
        :type FollowIdr: int
        """
        self._AppData = None
        self._PayloadType = None
        self._Interval = None
        self._FollowIdr = None

    @property
    def AppData(self):
        r"""AppData的内容，会被写入自定义SEI中的app_data字段，长度需小于4096。
        :rtype: str
        """
        return self._AppData

    @AppData.setter
    def AppData(self, AppData):
        self._AppData = AppData

    @property
    def PayloadType(self):
        r"""SEI消息的payload_type，默认值100，取值范围100-254（244除外，244为我们内部自定义的时间戳SEI）
        :rtype: int
        """
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def Interval(self):
        r"""SEI发送间隔，单位毫秒，默认值为1000。
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
        r"""取值范围[0,1]，填1：发送关键帧时会确保带SEI；填0：发送关键帧时不确保带SEI。默认值为0。
        :rtype: int
        """
        return self._FollowIdr

    @FollowIdr.setter
    def FollowIdr(self, FollowIdr):
        self._FollowIdr = FollowIdr


    def _deserialize(self, params):
        self._AppData = params.get("AppData")
        self._PayloadType = params.get("PayloadType")
        self._Interval = params.get("Interval")
        self._FollowIdr = params.get("FollowIdr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPassThrough(AbstractModel):
    r"""自定义透传SEI

    """

    def __init__(self):
        r"""
        :param _PayloadContent: 透传SEI的payload内容。
        :type PayloadContent: str
        :param _PayloadType: SEI消息的PayloadType，取值范围5、100-254（244除外，244为我们内部自定义的时间戳SEI）。
注：部分播放器可能不支持PayloadType为5带PayloadUuid的标准类型，建议优先使用其他PayloadType。
        :type PayloadType: int
        :param _PayloadUuid: PayloadType为5，PayloadUuid必须填写。PayloadType不是5时，不需要填写，填写会被后台忽略。该值必须是32长度的十六进制。
        :type PayloadUuid: str
        :param _Interval: SEI发送间隔，单位毫秒，默认值为1000。
        :type Interval: int
        :param _FollowIdr: 取值范围[0,1]，填1：发送关键帧时会确保带SEI；填0：发送关键帧时不确保带SEI。默认值为0。
        :type FollowIdr: int
        """
        self._PayloadContent = None
        self._PayloadType = None
        self._PayloadUuid = None
        self._Interval = None
        self._FollowIdr = None

    @property
    def PayloadContent(self):
        r"""透传SEI的payload内容。
        :rtype: str
        """
        return self._PayloadContent

    @PayloadContent.setter
    def PayloadContent(self, PayloadContent):
        self._PayloadContent = PayloadContent

    @property
    def PayloadType(self):
        r"""SEI消息的PayloadType，取值范围5、100-254（244除外，244为我们内部自定义的时间戳SEI）。
注：部分播放器可能不支持PayloadType为5带PayloadUuid的标准类型，建议优先使用其他PayloadType。
        :rtype: int
        """
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def PayloadUuid(self):
        r"""PayloadType为5，PayloadUuid必须填写。PayloadType不是5时，不需要填写，填写会被后台忽略。该值必须是32长度的十六进制。
        :rtype: str
        """
        return self._PayloadUuid

    @PayloadUuid.setter
    def PayloadUuid(self, PayloadUuid):
        self._PayloadUuid = PayloadUuid

    @property
    def Interval(self):
        r"""SEI发送间隔，单位毫秒，默认值为1000。
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
        r"""取值范围[0,1]，填1：发送关键帧时会确保带SEI；填0：发送关键帧时不确保带SEI。默认值为0。
        :rtype: int
        """
        return self._FollowIdr

    @FollowIdr.setter
    def FollowIdr(self, FollowIdr):
        self._FollowIdr = FollowIdr


    def _deserialize(self, params):
        self._PayloadContent = params.get("PayloadContent")
        self._PayloadType = params.get("PayloadType")
        self._PayloadUuid = params.get("PayloadUuid")
        self._Interval = params.get("Interval")
        self._FollowIdr = params.get("FollowIdr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPublishCdnParam(AbstractModel):
    r"""转推参数。

    """

    def __init__(self):
        r"""
        :param _PublishCdnUrl: CDN转推URL，只支持rtmp链接。
注：若更新转推时，URL有任何变化，都会断流重推。
        :type PublishCdnUrl: str
        :param _IsTencentCdn: 是否是腾讯云CDN，0为转推非腾讯云CDN，1为转推腾讯CDN，不携带该参数默认为1。注意：1，为避免误产生转推费用，该参数建议明确填写，转推非腾讯云CDN时会产生转推费用，详情参见接口文档说明；2，国内站默认只支持转推腾讯云CDN，如您有转推第三方CDN需求，请联系腾讯云技术支持。
        :type IsTencentCdn: int
        """
        self._PublishCdnUrl = None
        self._IsTencentCdn = None

    @property
    def PublishCdnUrl(self):
        r"""CDN转推URL，只支持rtmp链接。
注：若更新转推时，URL有任何变化，都会断流重推。
        :rtype: str
        """
        return self._PublishCdnUrl

    @PublishCdnUrl.setter
    def PublishCdnUrl(self, PublishCdnUrl):
        self._PublishCdnUrl = PublishCdnUrl

    @property
    def IsTencentCdn(self):
        r"""是否是腾讯云CDN，0为转推非腾讯云CDN，1为转推腾讯CDN，不携带该参数默认为1。注意：1，为避免误产生转推费用，该参数建议明确填写，转推非腾讯云CDN时会产生转推费用，详情参见接口文档说明；2，国内站默认只支持转推腾讯云CDN，如您有转推第三方CDN需求，请联系腾讯云技术支持。
        :rtype: int
        """
        return self._IsTencentCdn

    @IsTencentCdn.setter
    def IsTencentCdn(self, IsTencentCdn):
        self._IsTencentCdn = IsTencentCdn


    def _deserialize(self, params):
        self._PublishCdnUrl = params.get("PublishCdnUrl")
        self._IsTencentCdn = params.get("IsTencentCdn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuRecordParams(AbstractModel):
    r"""转推录制参数

    """

    def __init__(self):
        r"""
        :param _UniRecord: 转推录制模式， 
0/不填: 暂不支持，行为未定义；
1: 不开启录制；
2: 开启录制（使用控制台自动录制模板参数，参考：[跳转文档](https://cloud.tencent.com/document/product/647/111748#.E5.BD.95.E5.88.B6.E6.8E.A7.E5.88.B6.E6.96.B9.E6.A1.88)）；
3: 开启录制（使用API指定参数）。
        :type UniRecord: int
        :param _RecordKey: 录制任务 key，标识一个录制任务；您可以通过该参数，将多个转推任务录制成一个文件。不指定该参数时，只录制当前转推任务。
【限制长度为128字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线(_)和连词符(-)】
        :type RecordKey: str
        :param _RecordWaitTime: 【仅当UniRecord=3时此参数有效】
续录等待时间，对应录制模板“续录等待时长”，单位：秒。该值需大于等于 5，且小于等于 86400(24小时)，默认值为 30。启用续录时，录制任务空闲超过RecordWaitTime的时长，自动结束。
        :type RecordWaitTime: int
        :param _RecordFormat: 【仅当UniRecord=3时此参数有效】
录制输出文件格式列表，对应录制模板“文件格式”，支持“hls”、"mp4"、"aac"三种格式，默认值为"mp4"。其中"mp4"和"aac"格式，不能同时指定。
只录制 mp4格式，示例值：["mp4"]。同时录制mp4 和 HLS 格式，示例值：["mp4","hls"]。
        :type RecordFormat: list of str
        :param _MaxMediaFileDuration: 【仅当UniRecord=3时此参数有效】
单个文件录制时长，对应录制模板“单个录制文件时长”，单位：分钟。该值需大于等于 1，且小于等于 1440(24小时)，默认值为 1440。只对"mp4"或"aac"格式生效。实际单文件录制时长还受单文件大小不超过 2G 限制，超过2G则强制拆分。
        :type MaxMediaFileDuration: int
        :param _StreamType: 【仅当UniRecord=3时此参数有效】
录制的音视频类型，对应录制模板“录制格式”，0:音视频，1：纯音频，2：纯视频。最终录制文件内容是录制指定类型和转推内容的交集。
        :type StreamType: int
        :param _UserDefineRecordPrefix: 录制文件名前缀，不超过64字符。只有存储为vod时生效。
【限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线(_)和连词符(-)】
        :type UserDefineRecordPrefix: str
        :param _McuStorageParams: 【仅当UniRecord=3时此参数有效】
录制文件存储参数，对应控制台“存储位置”及相关参数。目前支持云点播VOD和对象存储COS两种存储方式，只能填写一种。
        :type McuStorageParams: :class:`tencentcloud.trtc.v20190722.models.McuStorageParams`
        """
        self._UniRecord = None
        self._RecordKey = None
        self._RecordWaitTime = None
        self._RecordFormat = None
        self._MaxMediaFileDuration = None
        self._StreamType = None
        self._UserDefineRecordPrefix = None
        self._McuStorageParams = None

    @property
    def UniRecord(self):
        r"""转推录制模式， 
0/不填: 暂不支持，行为未定义；
1: 不开启录制；
2: 开启录制（使用控制台自动录制模板参数，参考：[跳转文档](https://cloud.tencent.com/document/product/647/111748#.E5.BD.95.E5.88.B6.E6.8E.A7.E5.88.B6.E6.96.B9.E6.A1.88)）；
3: 开启录制（使用API指定参数）。
        :rtype: int
        """
        return self._UniRecord

    @UniRecord.setter
    def UniRecord(self, UniRecord):
        self._UniRecord = UniRecord

    @property
    def RecordKey(self):
        r"""录制任务 key，标识一个录制任务；您可以通过该参数，将多个转推任务录制成一个文件。不指定该参数时，只录制当前转推任务。
【限制长度为128字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线(_)和连词符(-)】
        :rtype: str
        """
        return self._RecordKey

    @RecordKey.setter
    def RecordKey(self, RecordKey):
        self._RecordKey = RecordKey

    @property
    def RecordWaitTime(self):
        r"""【仅当UniRecord=3时此参数有效】
续录等待时间，对应录制模板“续录等待时长”，单位：秒。该值需大于等于 5，且小于等于 86400(24小时)，默认值为 30。启用续录时，录制任务空闲超过RecordWaitTime的时长，自动结束。
        :rtype: int
        """
        return self._RecordWaitTime

    @RecordWaitTime.setter
    def RecordWaitTime(self, RecordWaitTime):
        self._RecordWaitTime = RecordWaitTime

    @property
    def RecordFormat(self):
        r"""【仅当UniRecord=3时此参数有效】
录制输出文件格式列表，对应录制模板“文件格式”，支持“hls”、"mp4"、"aac"三种格式，默认值为"mp4"。其中"mp4"和"aac"格式，不能同时指定。
只录制 mp4格式，示例值：["mp4"]。同时录制mp4 和 HLS 格式，示例值：["mp4","hls"]。
        :rtype: list of str
        """
        return self._RecordFormat

    @RecordFormat.setter
    def RecordFormat(self, RecordFormat):
        self._RecordFormat = RecordFormat

    @property
    def MaxMediaFileDuration(self):
        r"""【仅当UniRecord=3时此参数有效】
单个文件录制时长，对应录制模板“单个录制文件时长”，单位：分钟。该值需大于等于 1，且小于等于 1440(24小时)，默认值为 1440。只对"mp4"或"aac"格式生效。实际单文件录制时长还受单文件大小不超过 2G 限制，超过2G则强制拆分。
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration

    @property
    def StreamType(self):
        r"""【仅当UniRecord=3时此参数有效】
录制的音视频类型，对应录制模板“录制格式”，0:音视频，1：纯音频，2：纯视频。最终录制文件内容是录制指定类型和转推内容的交集。
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def UserDefineRecordPrefix(self):
        r"""录制文件名前缀，不超过64字符。只有存储为vod时生效。
【限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线(_)和连词符(-)】
        :rtype: str
        """
        return self._UserDefineRecordPrefix

    @UserDefineRecordPrefix.setter
    def UserDefineRecordPrefix(self, UserDefineRecordPrefix):
        self._UserDefineRecordPrefix = UserDefineRecordPrefix

    @property
    def McuStorageParams(self):
        r"""【仅当UniRecord=3时此参数有效】
录制文件存储参数，对应控制台“存储位置”及相关参数。目前支持云点播VOD和对象存储COS两种存储方式，只能填写一种。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuStorageParams`
        """
        return self._McuStorageParams

    @McuStorageParams.setter
    def McuStorageParams(self, McuStorageParams):
        self._McuStorageParams = McuStorageParams


    def _deserialize(self, params):
        self._UniRecord = params.get("UniRecord")
        self._RecordKey = params.get("RecordKey")
        self._RecordWaitTime = params.get("RecordWaitTime")
        self._RecordFormat = params.get("RecordFormat")
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        self._StreamType = params.get("StreamType")
        self._UserDefineRecordPrefix = params.get("UserDefineRecordPrefix")
        if params.get("McuStorageParams") is not None:
            self._McuStorageParams = McuStorageParams()
            self._McuStorageParams._deserialize(params.get("McuStorageParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuSeiParams(AbstractModel):
    r"""混流SEI参数

    """

    def __init__(self):
        r"""
        :param _LayoutVolume: 音量布局SEI
        :type LayoutVolume: :class:`tencentcloud.trtc.v20190722.models.McuLayoutVolume`
        :param _PassThrough: 透传SEI
        :type PassThrough: :class:`tencentcloud.trtc.v20190722.models.McuPassThrough`
        """
        self._LayoutVolume = None
        self._PassThrough = None

    @property
    def LayoutVolume(self):
        r"""音量布局SEI
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuLayoutVolume`
        """
        return self._LayoutVolume

    @LayoutVolume.setter
    def LayoutVolume(self, LayoutVolume):
        self._LayoutVolume = LayoutVolume

    @property
    def PassThrough(self):
        r"""透传SEI
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuPassThrough`
        """
        return self._PassThrough

    @PassThrough.setter
    def PassThrough(self, PassThrough):
        self._PassThrough = PassThrough


    def _deserialize(self, params):
        if params.get("LayoutVolume") is not None:
            self._LayoutVolume = McuLayoutVolume()
            self._LayoutVolume._deserialize(params.get("LayoutVolume"))
        if params.get("PassThrough") is not None:
            self._PassThrough = McuPassThrough()
            self._PassThrough._deserialize(params.get("PassThrough"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuStorageParams(AbstractModel):
    r"""Mcu转推录制，第三方存储参数。

    """

    def __init__(self):
        r"""
        :param _CloudStorage: 第三方云存储的账号信息（特别说明：若您选择存储至对象存储COS将会收取录制文件投递至COS的费用，详见云端录制收费说明，存储至VOD将不收取此项费用。）。
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param _McuCloudVod: 腾讯云云点播的账号信息。
        :type McuCloudVod: :class:`tencentcloud.trtc.v20190722.models.McuCloudVod`
        """
        self._CloudStorage = None
        self._McuCloudVod = None

    @property
    def CloudStorage(self):
        r"""第三方云存储的账号信息（特别说明：若您选择存储至对象存储COS将会收取录制文件投递至COS的费用，详见云端录制收费说明，存储至VOD将不收取此项费用。）。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        """
        return self._CloudStorage

    @CloudStorage.setter
    def CloudStorage(self, CloudStorage):
        self._CloudStorage = CloudStorage

    @property
    def McuCloudVod(self):
        r"""腾讯云云点播的账号信息。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuCloudVod`
        """
        return self._McuCloudVod

    @McuCloudVod.setter
    def McuCloudVod(self, McuCloudVod):
        self._McuCloudVod = McuCloudVod


    def _deserialize(self, params):
        if params.get("CloudStorage") is not None:
            self._CloudStorage = CloudStorage()
            self._CloudStorage._deserialize(params.get("CloudStorage"))
        if params.get("McuCloudVod") is not None:
            self._McuCloudVod = McuCloudVod()
            self._McuCloudVod._deserialize(params.get("McuCloudVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuTencentVod(AbstractModel):
    r"""Mcu转推录制，腾讯云点播相关参数。

    """

    def __init__(self):
        r"""
        :param _Procedure: 媒体后续任务处理操作，即完成媒体上传后，可自动发起任务流操作。参数值为任务流模板名，云点播支持 创建任务流模板 并为模板命名。
        :type Procedure: str
        :param _ExpireTime: 媒体文件过期时间，为当前时间的绝对过期时间；保存一天，就填"86400"，永久保存就填"0"，默认永久保存。
        :type ExpireTime: int
        :param _StorageRegion: 指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :type StorageRegion: str
        :param _ClassId: 分类ID，用于对媒体进行分类管理，可通过 创建分类 接口，创建分类，获得分类 ID。
默认值：0，表示其他分类。
        :type ClassId: int
        :param _SubAppId: 点播 子应用 ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param _SessionContext: 任务流上下文，任务完成回调时透传。
        :type SessionContext: str
        :param _SourceContext: 上传上下文，上传完成回调时透传。
        :type SourceContext: str
        """
        self._Procedure = None
        self._ExpireTime = None
        self._StorageRegion = None
        self._ClassId = None
        self._SubAppId = None
        self._SessionContext = None
        self._SourceContext = None

    @property
    def Procedure(self):
        r"""媒体后续任务处理操作，即完成媒体上传后，可自动发起任务流操作。参数值为任务流模板名，云点播支持 创建任务流模板 并为模板命名。
        :rtype: str
        """
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def ExpireTime(self):
        r"""媒体文件过期时间，为当前时间的绝对过期时间；保存一天，就填"86400"，永久保存就填"0"，默认永久保存。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def StorageRegion(self):
        r"""指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def ClassId(self):
        r"""分类ID，用于对媒体进行分类管理，可通过 创建分类 接口，创建分类，获得分类 ID。
默认值：0，表示其他分类。
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def SubAppId(self):
        r"""点播 子应用 ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def SessionContext(self):
        r"""任务流上下文，任务完成回调时透传。
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SourceContext(self):
        r"""上传上下文，上传完成回调时透传。
        :rtype: str
        """
        return self._SourceContext

    @SourceContext.setter
    def SourceContext(self, SourceContext):
        self._SourceContext = SourceContext


    def _deserialize(self, params):
        self._Procedure = params.get("Procedure")
        self._ExpireTime = params.get("ExpireTime")
        self._StorageRegion = params.get("StorageRegion")
        self._ClassId = params.get("ClassId")
        self._SubAppId = params.get("SubAppId")
        self._SessionContext = params.get("SessionContext")
        self._SourceContext = params.get("SourceContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuUserInfoParams(AbstractModel):
    r"""混流用户参数

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户参数。
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        :param _SoundLevel: 混音的音量调整：取值范围是0到100，100为原始上行音量，不填默认为100，值越小则音量越低。
注：该参数只在音量白名单下配置生效，其他场景配置无效。
        :type SoundLevel: int
        """
        self._UserInfo = None
        self._SoundLevel = None

    @property
    def UserInfo(self):
        r"""用户参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def SoundLevel(self):
        r"""混音的音量调整：取值范围是0到100，100为原始上行音量，不填默认为100，值越小则音量越低。
注：该参数只在音量白名单下配置生效，其他场景配置无效。
        :rtype: int
        """
        return self._SoundLevel

    @SoundLevel.setter
    def SoundLevel(self, SoundLevel):
        self._SoundLevel = SoundLevel


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = MixUserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._SoundLevel = params.get("SoundLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuVideoParams(AbstractModel):
    r"""混流转推的视频相关参数。

    """

    def __init__(self):
        r"""
        :param _VideoEncode: 输出流视频编码参数。
        :type VideoEncode: :class:`tencentcloud.trtc.v20190722.models.VideoEncode`
        :param _LayoutParams: 混流布局参数。
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.McuLayoutParams`
        :param _BackGroundColor: 整个画布背景颜色，常用的颜色有：
红色：0xcc0033。
黄色：0xcc9900。
绿色：0xcccc33。
蓝色：0x99CCFF。
黑色：0x000000。
白色：0xFFFFFF。
灰色：0x999999。
        :type BackGroundColor: str
        :param _BackgroundImageUrl: 整个画布的背景图片url，优先级高于BackGroundColor。支持png、jpg、jpeg格式。图片大小限制不超过5MB。
注：
1，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，背景图片将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，背景图片将不会生效。
        :type BackgroundImageUrl: str
        :param _WaterMarkList: 混流布局的水印参数。
        :type WaterMarkList: list of McuWaterMarkParams
        :param _BackgroundRenderMode: 背景图在输出时的显示模式：0为裁剪，1为缩放并显示黑底，2为变比例伸缩。后台默认为变比例伸缩。
        :type BackgroundRenderMode: int
        """
        self._VideoEncode = None
        self._LayoutParams = None
        self._BackGroundColor = None
        self._BackgroundImageUrl = None
        self._WaterMarkList = None
        self._BackgroundRenderMode = None

    @property
    def VideoEncode(self):
        r"""输出流视频编码参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoEncode`
        """
        return self._VideoEncode

    @VideoEncode.setter
    def VideoEncode(self, VideoEncode):
        self._VideoEncode = VideoEncode

    @property
    def LayoutParams(self):
        r"""混流布局参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuLayoutParams`
        """
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def BackGroundColor(self):
        r"""整个画布背景颜色，常用的颜色有：
红色：0xcc0033。
黄色：0xcc9900。
绿色：0xcccc33。
蓝色：0x99CCFF。
黑色：0x000000。
白色：0xFFFFFF。
灰色：0x999999。
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        r"""整个画布的背景图片url，优先级高于BackGroundColor。支持png、jpg、jpeg格式。图片大小限制不超过5MB。
注：
1，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，背景图片将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，背景图片将不会生效。
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def WaterMarkList(self):
        r"""混流布局的水印参数。
        :rtype: list of McuWaterMarkParams
        """
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def BackgroundRenderMode(self):
        r"""背景图在输出时的显示模式：0为裁剪，1为缩放并显示黑底，2为变比例伸缩。后台默认为变比例伸缩。
        :rtype: int
        """
        return self._BackgroundRenderMode

    @BackgroundRenderMode.setter
    def BackgroundRenderMode(self, BackgroundRenderMode):
        self._BackgroundRenderMode = BackgroundRenderMode


    def _deserialize(self, params):
        if params.get("VideoEncode") is not None:
            self._VideoEncode = VideoEncode()
            self._VideoEncode._deserialize(params.get("VideoEncode"))
        if params.get("LayoutParams") is not None:
            self._LayoutParams = McuLayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        self._BackGroundColor = params.get("BackGroundColor")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("WaterMarkList") is not None:
            self._WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = McuWaterMarkParams()
                obj._deserialize(item)
                self._WaterMarkList.append(obj)
        self._BackgroundRenderMode = params.get("BackgroundRenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkImage(AbstractModel):
    r"""图片水印参数。

    """

    def __init__(self):
        r"""
        :param _WaterMarkUrl: 水印图片URL地址，支持png、jpg、jpeg格式。图片大小限制不超过5MB。
注：
1，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，水印图片将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，水印图片将不会生效。
        :type WaterMarkUrl: str
        :param _WaterMarkWidth: 水印在输出时的宽。单位为像素值。
        :type WaterMarkWidth: int
        :param _WaterMarkHeight: 水印在输出时的高。单位为像素值。
        :type WaterMarkHeight: int
        :param _LocationX: 水印在输出时的X偏移。单位为像素值。
        :type LocationX: int
        :param _LocationY: 水印在输出时的Y偏移。单位为像素值。
        :type LocationY: int
        :param _ZOrder: 水印在输出时的层级，不填默认为0。
        :type ZOrder: int
        :param _DynamicPosType: 动态水印类型，默认为0。0:关闭；1:随机位置，每秒变动一次；2:边界扫描反弹，每帧变动一次。
        :type DynamicPosType: int
        """
        self._WaterMarkUrl = None
        self._WaterMarkWidth = None
        self._WaterMarkHeight = None
        self._LocationX = None
        self._LocationY = None
        self._ZOrder = None
        self._DynamicPosType = None

    @property
    def WaterMarkUrl(self):
        r"""水印图片URL地址，支持png、jpg、jpeg格式。图片大小限制不超过5MB。
注：
1，您需要确保图片链接的可访问性，后台单次下载超时时间为10秒，最多重试3次，若最终图片下载失败，水印图片将不会生效。
2，url可支持字符集：【'0-9','a-z','A-Z','-', '.', '_', '~', ':', '/', '?', '#', '[', ']','@', '!', '&', '(', ')', '*', '+', ',', '%', '=', ';', '|'】，您需要确保url字符在可支持字符集内，若存在可支持字符集外的字符，水印图片将不会生效。
        :rtype: str
        """
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def WaterMarkWidth(self):
        r"""水印在输出时的宽。单位为像素值。
        :rtype: int
        """
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        r"""水印在输出时的高。单位为像素值。
        :rtype: int
        """
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        r"""水印在输出时的X偏移。单位为像素值。
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""水印在输出时的Y偏移。单位为像素值。
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        r"""水印在输出时的层级，不填默认为0。
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def DynamicPosType(self):
        r"""动态水印类型，默认为0。0:关闭；1:随机位置，每秒变动一次；2:边界扫描反弹，每帧变动一次。
        :rtype: int
        """
        return self._DynamicPosType

    @DynamicPosType.setter
    def DynamicPosType(self, DynamicPosType):
        self._DynamicPosType = DynamicPosType


    def _deserialize(self, params):
        self._WaterMarkUrl = params.get("WaterMarkUrl")
        self._WaterMarkWidth = params.get("WaterMarkWidth")
        self._WaterMarkHeight = params.get("WaterMarkHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._ZOrder = params.get("ZOrder")
        self._DynamicPosType = params.get("DynamicPosType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkParams(AbstractModel):
    r"""水印参数。

    """

    def __init__(self):
        r"""
        :param _WaterMarkType: 水印类型，0为图片（默认），1为文字。
        :type WaterMarkType: int
        :param _WaterMarkImage: 图片水印参数。WaterMarkType为0指定。
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkImage`
        :param _WaterMarkText: 文字水印参数。WaterMarkType为1指定。
        :type WaterMarkText: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkText`
        """
        self._WaterMarkType = None
        self._WaterMarkImage = None
        self._WaterMarkText = None

    @property
    def WaterMarkType(self):
        r"""水印类型，0为图片（默认），1为文字。
        :rtype: int
        """
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        r"""图片水印参数。WaterMarkType为0指定。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkImage`
        """
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkText(self):
        r"""文字水印参数。WaterMarkType为1指定。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkText`
        """
        return self._WaterMarkText

    @WaterMarkText.setter
    def WaterMarkText(self, WaterMarkText):
        self._WaterMarkText = WaterMarkText


    def _deserialize(self, params):
        self._WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self._WaterMarkImage = McuWaterMarkImage()
            self._WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        if params.get("WaterMarkText") is not None:
            self._WaterMarkText = McuWaterMarkText()
            self._WaterMarkText._deserialize(params.get("WaterMarkText"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkText(AbstractModel):
    r"""文字水印参数。

    """

    def __init__(self):
        r"""
        :param _Text: 文字水印内容。
        :type Text: str
        :param _WaterMarkWidth: 水印在输出时的宽。单位为像素值。
        :type WaterMarkWidth: int
        :param _WaterMarkHeight: 水印在输出时的高。单位为像素值。
        :type WaterMarkHeight: int
        :param _LocationX: 水印在输出时的X偏移。单位为像素值。
        :type LocationX: int
        :param _LocationY: 水印在输出时的Y偏移。单位为像素值。
        :type LocationY: int
        :param _FontSize: 字体大小
        :type FontSize: int
        :param _FontColor: 字体颜色，默认为白色。常用的颜色有： 红色：0xcc0033。 黄色：0xcc9900。 绿色：0xcccc33。 蓝色：0x99CCFF。 黑色：0x000000。 白色：0xFFFFFF。 灰色：0x999999。	
        :type FontColor: str
        :param _BackGroundColor: 字体背景色，不配置默认为透明。常用的颜色有： 红色：0xcc0033。 黄色：0xcc9900。 绿色：0xcccc33。 蓝色：0x99CCFF。 黑色：0x000000。 白色：0xFFFFFF。 灰色：0x999999。	
        :type BackGroundColor: str
        :param _DynamicPosType: 动态水印类型，默认为0。0:关闭；1:随机位置，每秒变动一次；2:边界扫描反弹，每帧变动一次。
        :type DynamicPosType: int
        :param _ZOrder: 水印在输出时的层级，不填默认为0。
        :type ZOrder: int
        :param _Font: 水印字体，不填默认为Tencent。支持设置以下值： Tencent （默认） SourceHanSans
        :type Font: str
        """
        self._Text = None
        self._WaterMarkWidth = None
        self._WaterMarkHeight = None
        self._LocationX = None
        self._LocationY = None
        self._FontSize = None
        self._FontColor = None
        self._BackGroundColor = None
        self._DynamicPosType = None
        self._ZOrder = None
        self._Font = None

    @property
    def Text(self):
        r"""文字水印内容。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def WaterMarkWidth(self):
        r"""水印在输出时的宽。单位为像素值。
        :rtype: int
        """
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        r"""水印在输出时的高。单位为像素值。
        :rtype: int
        """
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        r"""水印在输出时的X偏移。单位为像素值。
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""水印在输出时的Y偏移。单位为像素值。
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def FontSize(self):
        r"""字体大小
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        r"""字体颜色，默认为白色。常用的颜色有： 红色：0xcc0033。 黄色：0xcc9900。 绿色：0xcccc33。 蓝色：0x99CCFF。 黑色：0x000000。 白色：0xFFFFFF。 灰色：0x999999。	
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
        r"""字体背景色，不配置默认为透明。常用的颜色有： 红色：0xcc0033。 黄色：0xcc9900。 绿色：0xcccc33。 蓝色：0x99CCFF。 黑色：0x000000。 白色：0xFFFFFF。 灰色：0x999999。	
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def DynamicPosType(self):
        r"""动态水印类型，默认为0。0:关闭；1:随机位置，每秒变动一次；2:边界扫描反弹，每帧变动一次。
        :rtype: int
        """
        return self._DynamicPosType

    @DynamicPosType.setter
    def DynamicPosType(self, DynamicPosType):
        self._DynamicPosType = DynamicPosType

    @property
    def ZOrder(self):
        r"""水印在输出时的层级，不填默认为0。
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def Font(self):
        r"""水印字体，不填默认为Tencent。支持设置以下值： Tencent （默认） SourceHanSans
        :rtype: str
        """
        return self._Font

    @Font.setter
    def Font(self, Font):
        self._Font = Font


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._WaterMarkWidth = params.get("WaterMarkWidth")
        self._WaterMarkHeight = params.get("WaterMarkHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        self._BackGroundColor = params.get("BackGroundColor")
        self._DynamicPosType = params.get("DynamicPosType")
        self._ZOrder = params.get("ZOrder")
        self._Font = params.get("Font")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayout(AbstractModel):
    r"""用户自定义混流布局参数列表。

    """

    def __init__(self):
        r"""
        :param _Top: 画布上该画面左上角的 y 轴坐标，取值范围 [0, 1920]，不能超过画布的高。
        :type Top: int
        :param _Left: 画布上该画面左上角的 x 轴坐标，取值范围 [0, 1920]，不能超过画布的宽。
        :type Left: int
        :param _Width: 画布上该画面宽度的相对值，取值范围 [0, 1920]，与Left相加不应超过画布的宽。
        :type Width: int
        :param _Height: 画布上该画面高度的相对值，取值范围 [0, 1920]，与Top相加不应超过画布的高。
        :type Height: int
        :param _UserId: 字符串内容为待显示在该画面的主播对应的UserId，如果不指定，会按照主播加入房间的顺序匹配。
        :type UserId: str
        :param _Alpha: 画布的透明度值，取值范围[0, 255]。0表示不透明，255表示全透明。默认值为0。
        :type Alpha: int
        :param _RenderMode: 0 ：拉伸模式，这个模式下整个视频内容会全部显示，并填满子画面，在源视频和目的视频宽高比不一致的时候，画面不会缺少内容，但是画面可能产生形变；

1 ：剪裁模式（默认），这个模式下会严格按照目的视频的宽高比对源视频剪裁之后再拉伸，并填满子画面画布，在源视频和目的视频宽高比不一致的时候，画面保持不变形，但是会被剪裁；

2 ：填黑模式，这个模式下会严格保持源视频的宽高比进行等比缩放，在源视频和目的视频宽高比不一致的时候，画面的上下侧边缘或者左右侧边缘会露出子画面画布的背景；

3 ：智能拉伸模式，这个模式类似剪裁模式，区别是在源视频和目的视频宽高比不一致的时候，限制了最大剪裁比例为画面的宽度或者高度的20%；
        :type RenderMode: int
        :param _MediaId: 对应订阅流的主辅路标识：
0：主流（默认）；
1：辅流；
        :type MediaId: int
        :param _ImageLayer: 该画布的图层顺序, 这个值越小表示图层越靠后。默认值为0。
        :type ImageLayer: int
        :param _SubBackgroundImage: 图片的url地址， 只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :type SubBackgroundImage: str
        """
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None
        self._UserId = None
        self._Alpha = None
        self._RenderMode = None
        self._MediaId = None
        self._ImageLayer = None
        self._SubBackgroundImage = None

    @property
    def Top(self):
        r"""画布上该画面左上角的 y 轴坐标，取值范围 [0, 1920]，不能超过画布的高。
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        r"""画布上该画面左上角的 x 轴坐标，取值范围 [0, 1920]，不能超过画布的宽。
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        r"""画布上该画面宽度的相对值，取值范围 [0, 1920]，与Left相加不应超过画布的宽。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""画布上该画面高度的相对值，取值范围 [0, 1920]，与Top相加不应超过画布的高。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def UserId(self):
        r"""字符串内容为待显示在该画面的主播对应的UserId，如果不指定，会按照主播加入房间的顺序匹配。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Alpha(self):
        r"""画布的透明度值，取值范围[0, 255]。0表示不透明，255表示全透明。默认值为0。
        :rtype: int
        """
        return self._Alpha

    @Alpha.setter
    def Alpha(self, Alpha):
        self._Alpha = Alpha

    @property
    def RenderMode(self):
        r"""0 ：拉伸模式，这个模式下整个视频内容会全部显示，并填满子画面，在源视频和目的视频宽高比不一致的时候，画面不会缺少内容，但是画面可能产生形变；

1 ：剪裁模式（默认），这个模式下会严格按照目的视频的宽高比对源视频剪裁之后再拉伸，并填满子画面画布，在源视频和目的视频宽高比不一致的时候，画面保持不变形，但是会被剪裁；

2 ：填黑模式，这个模式下会严格保持源视频的宽高比进行等比缩放，在源视频和目的视频宽高比不一致的时候，画面的上下侧边缘或者左右侧边缘会露出子画面画布的背景；

3 ：智能拉伸模式，这个模式类似剪裁模式，区别是在源视频和目的视频宽高比不一致的时候，限制了最大剪裁比例为画面的宽度或者高度的20%；
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MediaId(self):
        r"""对应订阅流的主辅路标识：
0：主流（默认）；
1：辅流；
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def ImageLayer(self):
        r"""该画布的图层顺序, 这个值越小表示图层越靠后。默认值为0。
        :rtype: int
        """
        return self._ImageLayer

    @ImageLayer.setter
    def ImageLayer(self, ImageLayer):
        self._ImageLayer = ImageLayer

    @property
    def SubBackgroundImage(self):
        r"""图片的url地址， 只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :rtype: str
        """
        return self._SubBackgroundImage

    @SubBackgroundImage.setter
    def SubBackgroundImage(self, SubBackgroundImage):
        self._SubBackgroundImage = SubBackgroundImage


    def _deserialize(self, params):
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._UserId = params.get("UserId")
        self._Alpha = params.get("Alpha")
        self._RenderMode = params.get("RenderMode")
        self._MediaId = params.get("MediaId")
        self._ImageLayer = params.get("ImageLayer")
        self._SubBackgroundImage = params.get("SubBackgroundImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayoutParams(AbstractModel):
    r"""录制的混流布局参数。

    """

    def __init__(self):
        r"""
        :param _MixLayoutMode: 布局模式:
1：悬浮布局；
2：屏幕分享布局；
3：九宫格布局；
4：自定义布局；

悬浮布局：默认第一个进入房间的主播（也可以指定一个主播）的视频画面会铺满整个屏幕。其他主播的视频画面从左下角开始依次按照进房顺序水平排列，显示为小画面，小画面悬浮于大画面之上。当画面数量小于等于17个时，每行4个（4 x 4排列）。当画面数量大于17个时，重新布局小画面为每行5个（5 x 5）排列。最多支持25个画面，如果用户只发送音频，仍然会占用画面位置。

屏幕分享布局：指定一个主播在屏幕左侧的大画面位置（如果不指定，那么大画面位置为背景色），其他主播自上而下依次垂直排列于右侧。当画面数量少于17个的时候，右侧每列最多8人，最多占据两列。当画面数量多于17个的时候，超过17个画面的主播从左下角开始依次水平排列。最多支持25个画面，如果主播只发送音频，仍然会占用画面位置。

九宫格布局：根据主播的数量自动调整每个画面的大小，每个主播的画面大小一致，最多支持25个画面。

自定义布局：根据需要在MixLayoutList内定制每个主播画面的布局。
        :type MixLayoutMode: int
        :param _MixLayoutList: 如果MixLayoutMode 选择为4自定义布局模式的话，设置此参数为每个主播所对应的布局画面的详细信息，最大不超过25个。
        :type MixLayoutList: list of MixLayout
        :param _BackGroundColor: 录制背景颜色，RGB的颜色表的16进制表示，每个颜色通过8bit长度标识，默认为黑色。比如橙色对应的RGB为 R:255 G:165 B:0, 那么对应的字符串描述为#FFA500，格式规范：‘#‘开头，后面跟固定RGB的颜色值
        :type BackGroundColor: str
        :param _MaxResolutionUserId: 在布局模式为1：悬浮布局和 2：屏幕分享布局时，设定为显示大视频画面的UserId。不填的话：悬浮布局默认是第一个进房间的主播，屏幕分享布局默认是背景色
        :type MaxResolutionUserId: str
        :param _MediaId: 主辅路标识，
0：主流（默认）；
1：辅流（屏幕分享）；
这个位置的MediaId代表的是对应MaxResolutionUserId的主辅路，MixLayoutList内代表的是自定义用户的主辅路。
        :type MediaId: int
        :param _BackgroundImageUrl: 图片的url地址，只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :type BackgroundImageUrl: str
        :param _PlaceHolderMode: 设置为1时代表启用占位图功能，0时代表不启用占位图功能，默认为0。启用占位图功能时，在预设位置的用户没有上行音视频时可显示对应的占位图。
        :type PlaceHolderMode: int
        :param _BackgroundImageRenderMode: 背景画面宽高比不一致的时候处理方案，与MixLayoutList定义的RenderMode一致。
        :type BackgroundImageRenderMode: int
        :param _DefaultSubBackgroundImage: 子画面占位图url地址，只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :type DefaultSubBackgroundImage: str
        :param _WaterMarkList: 水印布局参数， 最多支持25个。
        :type WaterMarkList: list of WaterMark
        :param _RenderMode: 模板布局下，背景画面宽高比不一致的时候处理方案。自定义布局不生效，与MixLayoutList定义的RenderMode一致。
        :type RenderMode: int
        :param _MaxResolutionUserAlign: 屏幕分享模板有效。设置为1时代表大画面居右，小画面居左布局。默认为0。
        :type MaxResolutionUserAlign: int
        """
        self._MixLayoutMode = None
        self._MixLayoutList = None
        self._BackGroundColor = None
        self._MaxResolutionUserId = None
        self._MediaId = None
        self._BackgroundImageUrl = None
        self._PlaceHolderMode = None
        self._BackgroundImageRenderMode = None
        self._DefaultSubBackgroundImage = None
        self._WaterMarkList = None
        self._RenderMode = None
        self._MaxResolutionUserAlign = None

    @property
    def MixLayoutMode(self):
        r"""布局模式:
1：悬浮布局；
2：屏幕分享布局；
3：九宫格布局；
4：自定义布局；

悬浮布局：默认第一个进入房间的主播（也可以指定一个主播）的视频画面会铺满整个屏幕。其他主播的视频画面从左下角开始依次按照进房顺序水平排列，显示为小画面，小画面悬浮于大画面之上。当画面数量小于等于17个时，每行4个（4 x 4排列）。当画面数量大于17个时，重新布局小画面为每行5个（5 x 5）排列。最多支持25个画面，如果用户只发送音频，仍然会占用画面位置。

屏幕分享布局：指定一个主播在屏幕左侧的大画面位置（如果不指定，那么大画面位置为背景色），其他主播自上而下依次垂直排列于右侧。当画面数量少于17个的时候，右侧每列最多8人，最多占据两列。当画面数量多于17个的时候，超过17个画面的主播从左下角开始依次水平排列。最多支持25个画面，如果主播只发送音频，仍然会占用画面位置。

九宫格布局：根据主播的数量自动调整每个画面的大小，每个主播的画面大小一致，最多支持25个画面。

自定义布局：根据需要在MixLayoutList内定制每个主播画面的布局。
        :rtype: int
        """
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def MixLayoutList(self):
        r"""如果MixLayoutMode 选择为4自定义布局模式的话，设置此参数为每个主播所对应的布局画面的详细信息，最大不超过25个。
        :rtype: list of MixLayout
        """
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def BackGroundColor(self):
        r"""录制背景颜色，RGB的颜色表的16进制表示，每个颜色通过8bit长度标识，默认为黑色。比如橙色对应的RGB为 R:255 G:165 B:0, 那么对应的字符串描述为#FFA500，格式规范：‘#‘开头，后面跟固定RGB的颜色值
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def MaxResolutionUserId(self):
        r"""在布局模式为1：悬浮布局和 2：屏幕分享布局时，设定为显示大视频画面的UserId。不填的话：悬浮布局默认是第一个进房间的主播，屏幕分享布局默认是背景色
        :rtype: str
        """
        return self._MaxResolutionUserId

    @MaxResolutionUserId.setter
    def MaxResolutionUserId(self, MaxResolutionUserId):
        self._MaxResolutionUserId = MaxResolutionUserId

    @property
    def MediaId(self):
        r"""主辅路标识，
0：主流（默认）；
1：辅流（屏幕分享）；
这个位置的MediaId代表的是对应MaxResolutionUserId的主辅路，MixLayoutList内代表的是自定义用户的主辅路。
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def BackgroundImageUrl(self):
        r"""图片的url地址，只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def PlaceHolderMode(self):
        r"""设置为1时代表启用占位图功能，0时代表不启用占位图功能，默认为0。启用占位图功能时，在预设位置的用户没有上行音视频时可显示对应的占位图。
        :rtype: int
        """
        return self._PlaceHolderMode

    @PlaceHolderMode.setter
    def PlaceHolderMode(self, PlaceHolderMode):
        self._PlaceHolderMode = PlaceHolderMode

    @property
    def BackgroundImageRenderMode(self):
        r"""背景画面宽高比不一致的时候处理方案，与MixLayoutList定义的RenderMode一致。
        :rtype: int
        """
        return self._BackgroundImageRenderMode

    @BackgroundImageRenderMode.setter
    def BackgroundImageRenderMode(self, BackgroundImageRenderMode):
        self._BackgroundImageRenderMode = BackgroundImageRenderMode

    @property
    def DefaultSubBackgroundImage(self):
        r"""子画面占位图url地址，只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :rtype: str
        """
        return self._DefaultSubBackgroundImage

    @DefaultSubBackgroundImage.setter
    def DefaultSubBackgroundImage(self, DefaultSubBackgroundImage):
        self._DefaultSubBackgroundImage = DefaultSubBackgroundImage

    @property
    def WaterMarkList(self):
        r"""水印布局参数， 最多支持25个。
        :rtype: list of WaterMark
        """
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def RenderMode(self):
        r"""模板布局下，背景画面宽高比不一致的时候处理方案。自定义布局不生效，与MixLayoutList定义的RenderMode一致。
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MaxResolutionUserAlign(self):
        r"""屏幕分享模板有效。设置为1时代表大画面居右，小画面居左布局。默认为0。
        :rtype: int
        """
        return self._MaxResolutionUserAlign

    @MaxResolutionUserAlign.setter
    def MaxResolutionUserAlign(self, MaxResolutionUserAlign):
        self._MaxResolutionUserAlign = MaxResolutionUserAlign


    def _deserialize(self, params):
        self._MixLayoutMode = params.get("MixLayoutMode")
        if params.get("MixLayoutList") is not None:
            self._MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = MixLayout()
                obj._deserialize(item)
                self._MixLayoutList.append(obj)
        self._BackGroundColor = params.get("BackGroundColor")
        self._MaxResolutionUserId = params.get("MaxResolutionUserId")
        self._MediaId = params.get("MediaId")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        self._PlaceHolderMode = params.get("PlaceHolderMode")
        self._BackgroundImageRenderMode = params.get("BackgroundImageRenderMode")
        self._DefaultSubBackgroundImage = params.get("DefaultSubBackgroundImage")
        if params.get("WaterMarkList") is not None:
            self._WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = WaterMark()
                obj._deserialize(item)
                self._WaterMarkList.append(obj)
        self._RenderMode = params.get("RenderMode")
        self._MaxResolutionUserAlign = params.get("MaxResolutionUserAlign")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixTranscodeParams(AbstractModel):
    r"""录制的音视频转码参数。

    """

    def __init__(self):
        r"""
        :param _VideoParams: 录制视频转码参数，注意如果设置了这个参数，那么里面的字段都是必填的，没有默认值，如果不填这个参数，那么取值为默认值。
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        :param _AudioParams: 录制音频转码参数，注意如果设置了这个参数，那么里面的字段都是必填的，没有默认值，如果不填这个参数，那么取值为默认值。
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        self._VideoParams = None
        self._AudioParams = None

    @property
    def VideoParams(self):
        r"""录制视频转码参数，注意如果设置了这个参数，那么里面的字段都是必填的，没有默认值，如果不填这个参数，那么取值为默认值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def AudioParams(self):
        r"""录制音频转码参数，注意如果设置了这个参数，那么里面的字段都是必填的，没有默认值，如果不填这个参数，那么取值为默认值。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams


    def _deserialize(self, params):
        if params.get("VideoParams") is not None:
            self._VideoParams = VideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("AudioParams") is not None:
            self._AudioParams = AudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixUserInfo(AbstractModel):
    r"""TRTC用户参数。

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID。
        :type UserId: str
        :param _RoomId: 动态布局时房间信息必须和主房间信息保持一致，自定义布局时房间信息必须和MixLayoutList中对应用户的房间信息保持一致，不填时默认与主房间信息一致。
        :type RoomId: str
        :param _RoomIdType: 房间号类型，0为整型房间号，1为字符串房间号。
        :type RoomIdType: int
        """
        self._UserId = None
        self._RoomId = None
        self._RoomIdType = None

    @property
    def UserId(self):
        r"""用户ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        r"""动态布局时房间信息必须和主房间信息保持一致，自定义布局时房间信息必须和MixLayoutList中对应用户的房间信息保持一致，不填时默认与主房间信息一致。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""房间号类型，0为整型房间号，1为字符串房间号。
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModerationParams(AbstractModel):
    r"""云端审核的控制参数。

    """

    def __init__(self):
        r"""
        :param _ModerationType: 审核任务类型， 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核4:音频流式审核 5:音频流式+视频截帧审核  默认值1 （流式审核需要供应商支持才生效）
        :type ModerationType: int
        :param _MaxIdleTime: 房间内持续没有用户（主播）上行推流的状态超过MaxIdleTime的时长，自动停止切片，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于1800秒(0.5小时)。示例值：30 
        :type MaxIdleTime: int
        :param _SliceAudio: 音频切片时长，默认15s 示例值：15
        :type SliceAudio: int
        :param _SliceVideo: 视频截帧间隔时长，默认5s
        :type SliceVideo: int
        :param _ModerationSupplier: 供应商枚举，
tianyu : 天御内容安全 （支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
ace  : ACE内容安全 （支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
shumei : 数美审核（支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
yidun : 网易易盾审核 （支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
        :type ModerationSupplier: str
        :param _ModerationSupplierParam: 第三方审核商送审需要配置信息
        :type ModerationSupplierParam: :class:`tencentcloud.trtc.v20190722.models.ModerationSupplierParam`
        :param _SaveModerationFile: 是否保存文件  0不保存文件 1保存所有文件 2仅保存命中文件
        :type SaveModerationFile: int
        :param _CallbackAllResults: 是否回调所有审核结果:0 默认回调所有结果 1 仅回调命中结果 
        :type CallbackAllResults: int
        :param _SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        """
        self._ModerationType = None
        self._MaxIdleTime = None
        self._SliceAudio = None
        self._SliceVideo = None
        self._ModerationSupplier = None
        self._ModerationSupplierParam = None
        self._SaveModerationFile = None
        self._CallbackAllResults = None
        self._SubscribeStreamUserIds = None

    @property
    def ModerationType(self):
        r"""审核任务类型， 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核4:音频流式审核 5:音频流式+视频截帧审核  默认值1 （流式审核需要供应商支持才生效）
        :rtype: int
        """
        return self._ModerationType

    @ModerationType.setter
    def ModerationType(self, ModerationType):
        self._ModerationType = ModerationType

    @property
    def MaxIdleTime(self):
        r"""房间内持续没有用户（主播）上行推流的状态超过MaxIdleTime的时长，自动停止切片，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于1800秒(0.5小时)。示例值：30 
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def SliceAudio(self):
        r"""音频切片时长，默认15s 示例值：15
        :rtype: int
        """
        return self._SliceAudio

    @SliceAudio.setter
    def SliceAudio(self, SliceAudio):
        self._SliceAudio = SliceAudio

    @property
    def SliceVideo(self):
        r"""视频截帧间隔时长，默认5s
        :rtype: int
        """
        return self._SliceVideo

    @SliceVideo.setter
    def SliceVideo(self, SliceVideo):
        self._SliceVideo = SliceVideo

    @property
    def ModerationSupplier(self):
        r"""供应商枚举，
tianyu : 天御内容安全 （支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
ace  : ACE内容安全 （支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
shumei : 数美审核（支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
yidun : 网易易盾审核 （支持 1:音频切片审核，2:视频截帧审核，3:音视切片审核+视频截帧审核）
        :rtype: str
        """
        return self._ModerationSupplier

    @ModerationSupplier.setter
    def ModerationSupplier(self, ModerationSupplier):
        self._ModerationSupplier = ModerationSupplier

    @property
    def ModerationSupplierParam(self):
        r"""第三方审核商送审需要配置信息
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModerationSupplierParam`
        """
        return self._ModerationSupplierParam

    @ModerationSupplierParam.setter
    def ModerationSupplierParam(self, ModerationSupplierParam):
        self._ModerationSupplierParam = ModerationSupplierParam

    @property
    def SaveModerationFile(self):
        r"""是否保存文件  0不保存文件 1保存所有文件 2仅保存命中文件
        :rtype: int
        """
        return self._SaveModerationFile

    @SaveModerationFile.setter
    def SaveModerationFile(self, SaveModerationFile):
        self._SaveModerationFile = SaveModerationFile

    @property
    def CallbackAllResults(self):
        r"""是否回调所有审核结果:0 默认回调所有结果 1 仅回调命中结果 
        :rtype: int
        """
        return self._CallbackAllResults

    @CallbackAllResults.setter
    def CallbackAllResults(self, CallbackAllResults):
        self._CallbackAllResults = CallbackAllResults

    @property
    def SubscribeStreamUserIds(self):
        r"""指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeModerationUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._ModerationType = params.get("ModerationType")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._SliceAudio = params.get("SliceAudio")
        self._SliceVideo = params.get("SliceVideo")
        self._ModerationSupplier = params.get("ModerationSupplier")
        if params.get("ModerationSupplierParam") is not None:
            self._ModerationSupplierParam = ModerationSupplierParam()
            self._ModerationSupplierParam._deserialize(params.get("ModerationSupplierParam"))
        self._SaveModerationFile = params.get("SaveModerationFile")
        self._CallbackAllResults = params.get("CallbackAllResults")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeModerationUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModerationStorageParams(AbstractModel):
    r"""审核存储参数

    """

    def __init__(self):
        r"""
        :param _CloudModerationStorage: 腾讯云对象存储COS以及第三方云存储的账号信息
        :type CloudModerationStorage: :class:`tencentcloud.trtc.v20190722.models.CloudModerationStorage`
        """
        self._CloudModerationStorage = None

    @property
    def CloudModerationStorage(self):
        r"""腾讯云对象存储COS以及第三方云存储的账号信息
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudModerationStorage`
        """
        return self._CloudModerationStorage

    @CloudModerationStorage.setter
    def CloudModerationStorage(self, CloudModerationStorage):
        self._CloudModerationStorage = CloudModerationStorage


    def _deserialize(self, params):
        if params.get("CloudModerationStorage") is not None:
            self._CloudModerationStorage = CloudModerationStorage()
            self._CloudModerationStorage._deserialize(params.get("CloudModerationStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModerationSupplierParam(AbstractModel):
    r"""送审到第三方审核供应商需要参数

    """

    def __init__(self):
        r"""
        :param _AppID: 供应审核商账号id，数美天御不为空，易盾为空
        :type AppID: str
        :param _SecretId: 供应审核商秘钥id
        :type SecretId: str
        :param _SecretKey: 供应审核商秘钥key
        :type SecretKey: str
        :param _AudioBizType: 音频场景，策略id或者businessId
        :type AudioBizType: str
        :param _ImageBizType: 图片场景，策略id或者businessId
        :type ImageBizType: str
        """
        self._AppID = None
        self._SecretId = None
        self._SecretKey = None
        self._AudioBizType = None
        self._ImageBizType = None

    @property
    def AppID(self):
        r"""供应审核商账号id，数美天御不为空，易盾为空
        :rtype: str
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def SecretId(self):
        r"""供应审核商秘钥id
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        r"""供应审核商秘钥key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def AudioBizType(self):
        r"""音频场景，策略id或者businessId
        :rtype: str
        """
        return self._AudioBizType

    @AudioBizType.setter
    def AudioBizType(self, AudioBizType):
        self._AudioBizType = AudioBizType

    @property
    def ImageBizType(self):
        r"""图片场景，策略id或者businessId
        :rtype: str
        """
        return self._ImageBizType

    @ImageBizType.setter
    def ImageBizType(self, ImageBizType):
        self._ImageBizType = ImageBizType


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._AudioBizType = params.get("AudioBizType")
        self._ImageBizType = params.get("ImageBizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudModerationRequest(AbstractModel):
    r"""ModifyCloudModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 审核任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SubscribeStreamUserIds = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""审核任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SubscribeStreamUserIds(self):
        r"""指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudModerationResponse(AbstractModel):
    r"""ModifyCloudModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 审核任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""审核任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyCloudRecordingRequest(AbstractModel):
    r"""ModifyCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 录制任务的唯一Id，在启动录制成功后会返回。
        :type TaskId: str
        :param _MixLayoutParams: 需要更新的混流的布局参数。
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param _SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self._SdkAppId = None
        self._TaskId = None
        self._MixLayoutParams = None
        self._SubscribeStreamUserIds = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和录制的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""录制任务的唯一Id，在启动录制成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MixLayoutParams(self):
        r"""需要更新的混流的布局参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        """
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def SubscribeStreamUserIds(self):
        r"""指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        if params.get("MixLayoutParams") is not None:
            self._MixLayoutParams = MixLayoutParams()
            self._MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingResponse(AbstractModel):
    r"""ModifyCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyCloudSliceTaskRequest(AbstractModel):
    r"""ModifyCloudSliceTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 切片任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SubscribeStreamUserIds = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和TRTC的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""切片任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SubscribeStreamUserIds(self):
        r"""指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudSliceTaskResponse(AbstractModel):
    r"""ModifyCloudSliceTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 切片任务的唯一Id，在启动切片任务成功后会返回。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""切片任务的唯一Id，在启动切片任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyPictureRequest(AbstractModel):
    r"""ModifyPicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PictureId: 图片id
        :type PictureId: int
        :param _SdkAppId: 应用id
        :type SdkAppId: int
        :param _Height: 图片长度
        :type Height: int
        :param _Width: 图片宽度
        :type Width: int
        :param _XPosition: 显示位置x轴方向
        :type XPosition: int
        :param _YPosition: 显示位置y轴方向
        :type YPosition: int
        """
        self._PictureId = None
        self._SdkAppId = None
        self._Height = None
        self._Width = None
        self._XPosition = None
        self._YPosition = None

    @property
    def PictureId(self):
        r"""图片id
        :rtype: int
        """
        return self._PictureId

    @PictureId.setter
    def PictureId(self, PictureId):
        self._PictureId = PictureId

    @property
    def SdkAppId(self):
        r"""应用id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Height(self):
        r"""图片长度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        r"""图片宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def XPosition(self):
        r"""显示位置x轴方向
        :rtype: int
        """
        return self._XPosition

    @XPosition.setter
    def XPosition(self, XPosition):
        self._XPosition = XPosition

    @property
    def YPosition(self):
        r"""显示位置y轴方向
        :rtype: int
        """
        return self._YPosition

    @YPosition.setter
    def YPosition(self, YPosition):
        self._YPosition = YPosition


    def _deserialize(self, params):
        self._PictureId = params.get("PictureId")
        self._SdkAppId = params.get("SdkAppId")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._XPosition = params.get("XPosition")
        self._YPosition = params.get("YPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPictureResponse(AbstractModel):
    r"""ModifyPicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OneSdkAppIdTranscodeTimeUsagesInfo(AbstractModel):
    r"""旁路转码时长的查询结果

    """

    def __init__(self):
        r"""
        :param _SdkAppIdTranscodeTimeUsages: 旁路转码时长查询结果数组
        :type SdkAppIdTranscodeTimeUsages: list of SdkAppIdTrtcMcuTranscodeTimeUsage
        :param _TotalNum: 查询记录数量
        :type TotalNum: int
        :param _SdkAppId: 所查询的应用ID，可能值为:1-应用的应用ID，2-total，显示为total则表示查询的是所有应用的用量合计值。
        :type SdkAppId: str
        """
        self._SdkAppIdTranscodeTimeUsages = None
        self._TotalNum = None
        self._SdkAppId = None

    @property
    def SdkAppIdTranscodeTimeUsages(self):
        r"""旁路转码时长查询结果数组
        :rtype: list of SdkAppIdTrtcMcuTranscodeTimeUsage
        """
        return self._SdkAppIdTranscodeTimeUsages

    @SdkAppIdTranscodeTimeUsages.setter
    def SdkAppIdTranscodeTimeUsages(self, SdkAppIdTranscodeTimeUsages):
        self._SdkAppIdTranscodeTimeUsages = SdkAppIdTranscodeTimeUsages

    @property
    def TotalNum(self):
        r"""查询记录数量
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def SdkAppId(self):
        r"""所查询的应用ID，可能值为:1-应用的应用ID，2-total，显示为total则表示查询的是所有应用的用量合计值。
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        if params.get("SdkAppIdTranscodeTimeUsages") is not None:
            self._SdkAppIdTranscodeTimeUsages = []
            for item in params.get("SdkAppIdTranscodeTimeUsages"):
                obj = SdkAppIdTrtcMcuTranscodeTimeUsage()
                obj._deserialize(item)
                self._SdkAppIdTranscodeTimeUsages.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputParams(AbstractModel):
    r"""MCU混流的输出参数

    """

    def __init__(self):
        r"""
        :param _StreamId: 直播流 ID，由用户自定义设置，该流 ID 不能与用户旁路的流 ID 相同，限制64字节。
        :type StreamId: str
        :param _PureAudioStream: 取值范围[0,1]， 填0：直播流为音视频(默认); 填1：直播流为纯音频
        :type PureAudioStream: int
        :param _RecordId: 自定义录制文件名称前缀。请先在实时音视频控制台开通录制功能，https://cloud.tencent.com/document/product/647/50768。
【注意】该方式仅对旧版云端录制功能的应用生效，新版云端录制功能的应用请用接口CreateCloudRecording发起录制。新、旧云端录制类型判断方式请见：https://cloud.tencent.com/document/product/647/50768#record
        :type RecordId: str
        :param _RecordAudioOnly: 取值范围[0,1]，填0无实际含义; 填1：指定录制文件格式为mp3。此参数不建议使用，建议在实时音视频控制台配置纯音频录制模板。
        :type RecordAudioOnly: int
        """
        self._StreamId = None
        self._PureAudioStream = None
        self._RecordId = None
        self._RecordAudioOnly = None

    @property
    def StreamId(self):
        r"""直播流 ID，由用户自定义设置，该流 ID 不能与用户旁路的流 ID 相同，限制64字节。
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def PureAudioStream(self):
        r"""取值范围[0,1]， 填0：直播流为音视频(默认); 填1：直播流为纯音频
        :rtype: int
        """
        return self._PureAudioStream

    @PureAudioStream.setter
    def PureAudioStream(self, PureAudioStream):
        self._PureAudioStream = PureAudioStream

    @property
    def RecordId(self):
        r"""自定义录制文件名称前缀。请先在实时音视频控制台开通录制功能，https://cloud.tencent.com/document/product/647/50768。
【注意】该方式仅对旧版云端录制功能的应用生效，新版云端录制功能的应用请用接口CreateCloudRecording发起录制。新、旧云端录制类型判断方式请见：https://cloud.tencent.com/document/product/647/50768#record
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordAudioOnly(self):
        r"""取值范围[0,1]，填0无实际含义; 填1：指定录制文件格式为mp3。此参数不建议使用，建议在实时音视频控制台配置纯音频录制模板。
        :rtype: int
        """
        return self._RecordAudioOnly

    @RecordAudioOnly.setter
    def RecordAudioOnly(self, RecordAudioOnly):
        self._RecordAudioOnly = RecordAudioOnly


    def _deserialize(self, params):
        self._StreamId = params.get("StreamId")
        self._PureAudioStream = params.get("PureAudioStream")
        self._RecordId = params.get("RecordId")
        self._RecordAudioOnly = params.get("RecordAudioOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PictureInfo(AbstractModel):
    r"""图片列表信息

    """

    def __init__(self):
        r"""
        :param _Height: 图片长度
        :type Height: int
        :param _Width: 图片宽度
        :type Width: int
        :param _XPosition: 显示位置x轴方向
        :type XPosition: int
        :param _YPosition: 显示位置y轴方向
        :type YPosition: int
        :param _SdkAppId: 应用id
        :type SdkAppId: int
        :param _PictureId: 图片id
        :type PictureId: int
        """
        self._Height = None
        self._Width = None
        self._XPosition = None
        self._YPosition = None
        self._SdkAppId = None
        self._PictureId = None

    @property
    def Height(self):
        r"""图片长度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        r"""图片宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def XPosition(self):
        r"""显示位置x轴方向
        :rtype: int
        """
        return self._XPosition

    @XPosition.setter
    def XPosition(self, XPosition):
        self._XPosition = XPosition

    @property
    def YPosition(self):
        r"""显示位置y轴方向
        :rtype: int
        """
        return self._YPosition

    @YPosition.setter
    def YPosition(self, YPosition):
        self._YPosition = YPosition

    @property
    def SdkAppId(self):
        r"""应用id
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def PictureId(self):
        r"""图片id
        :rtype: int
        """
        return self._PictureId

    @PictureId.setter
    def PictureId(self, PictureId):
        self._PictureId = PictureId


    def _deserialize(self, params):
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._XPosition = params.get("XPosition")
        self._YPosition = params.get("YPosition")
        self._SdkAppId = params.get("SdkAppId")
        self._PictureId = params.get("PictureId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PresetLayoutConfig(AbstractModel):
    r"""自定义模板中有效，指定用户视频在混合画面中的位置。

    """

    def __init__(self):
        r"""
        :param _UserId: 指定显示在该画面上的用户ID。如果不指定用户ID，会按照用户加入房间的顺序自动匹配PresetLayoutConfig中的画面设置。
        :type UserId: str
        :param _StreamType: 当该画面指定用户时，代表用户的流类型。0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :type StreamType: int
        :param _ImageWidth: 该画面在输出时的宽度，单位为像素值，不填默认为0。
        :type ImageWidth: int
        :param _ImageHeight: 该画面在输出时的高度，单位为像素值，不填默认为0。
        :type ImageHeight: int
        :param _LocationX: 该画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :type LocationX: int
        :param _LocationY: 该画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :type LocationY: int
        :param _ZOrder: 该画面在输出时的层级，不填默认为0。
        :type ZOrder: int
        :param _RenderMode: 该画面在输出时的显示模式：0为裁剪，1为缩放，2为缩放并显示黑底。不填默认为0。
        :type RenderMode: int
        :param _MixInputType: 该当前位置用户混入的流类型：0为混入音视频，1为只混入视频，2为只混入音频。默认为0，建议配合指定用户ID使用。
        :type MixInputType: int
        :param _PlaceImageId: 占位图ID。启用占位图功能时，在当前位置的用户没有上行视频时显示占位图。占位图大小不能超过2M，在实时音视频控制台上传并生成，https://cloud.tencent.com/document/product/647/50769
        :type PlaceImageId: int
        """
        self._UserId = None
        self._StreamType = None
        self._ImageWidth = None
        self._ImageHeight = None
        self._LocationX = None
        self._LocationY = None
        self._ZOrder = None
        self._RenderMode = None
        self._MixInputType = None
        self._PlaceImageId = None

    @property
    def UserId(self):
        r"""指定显示在该画面上的用户ID。如果不指定用户ID，会按照用户加入房间的顺序自动匹配PresetLayoutConfig中的画面设置。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def StreamType(self):
        r"""当该画面指定用户时，代表用户的流类型。0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def ImageWidth(self):
        r"""该画面在输出时的宽度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        r"""该画面在输出时的高度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def LocationX(self):
        r"""该画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""该画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        r"""该画面在输出时的层级，不填默认为0。
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def RenderMode(self):
        r"""该画面在输出时的显示模式：0为裁剪，1为缩放，2为缩放并显示黑底。不填默认为0。
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MixInputType(self):
        r"""该当前位置用户混入的流类型：0为混入音视频，1为只混入视频，2为只混入音频。默认为0，建议配合指定用户ID使用。
        :rtype: int
        """
        return self._MixInputType

    @MixInputType.setter
    def MixInputType(self, MixInputType):
        self._MixInputType = MixInputType

    @property
    def PlaceImageId(self):
        r"""占位图ID。启用占位图功能时，在当前位置的用户没有上行视频时显示占位图。占位图大小不能超过2M，在实时音视频控制台上传并生成，https://cloud.tencent.com/document/product/647/50769
        :rtype: int
        """
        return self._PlaceImageId

    @PlaceImageId.setter
    def PlaceImageId(self, PlaceImageId):
        self._PlaceImageId = PlaceImageId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._StreamType = params.get("StreamType")
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._ZOrder = params.get("ZOrder")
        self._RenderMode = params.get("RenderMode")
        self._MixInputType = params.get("MixInputType")
        self._PlaceImageId = params.get("PlaceImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCdnParams(AbstractModel):
    r"""第三方CDN转推参数

    """

    def __init__(self):
        r"""
        :param _BizId: 腾讯云直播BizId。
        :type BizId: int
        :param _PublishCdnUrls: 第三方CDN转推的目的地址，同时只支持转推一个第三方CDN地址。
        :type PublishCdnUrls: list of str
        """
        self._BizId = None
        self._PublishCdnUrls = None

    @property
    def BizId(self):
        r"""腾讯云直播BizId。
        :rtype: int
        """
        return self._BizId

    @BizId.setter
    def BizId(self, BizId):
        self._BizId = BizId

    @property
    def PublishCdnUrls(self):
        r"""第三方CDN转推的目的地址，同时只支持转推一个第三方CDN地址。
        :rtype: list of str
        """
        return self._PublishCdnUrls

    @PublishCdnUrls.setter
    def PublishCdnUrls(self, PublishCdnUrls):
        self._PublishCdnUrls = PublishCdnUrls


    def _deserialize(self, params):
        self._BizId = params.get("BizId")
        self._PublishCdnUrls = params.get("PublishCdnUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QualityData(AbstractModel):
    r"""Es返回的质量数据

    """

    def __init__(self):
        r"""
        :param _Content: 数据内容
        :type Content: list of TimeValue
        :param _UserId: 用户ID
        :type UserId: str
        :param _PeerId: 对端Id,为空时表示上行数据
        :type PeerId: str
        :param _DataType: 数据类型
        :type DataType: str
        """
        self._Content = None
        self._UserId = None
        self._PeerId = None
        self._DataType = None

    @property
    def Content(self):
        r"""数据内容
        :rtype: list of TimeValue
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PeerId(self):
        r"""对端Id,为空时表示上行数据
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def DataType(self):
        r"""数据类型
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self._Content.append(obj)
        self._UserId = params.get("UserId")
        self._PeerId = params.get("PeerId")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeConfig(AbstractModel):
    r"""语音识别使用的配置

    """

    def __init__(self):
        r"""
        :param _Language: 
语音转文字支持识别的语言，默认是"zh" 中文

可通过购买「AI智能识别时长包」解锁或领取包月套餐体验版解锁不同语言. 详细说明参考：[AI智能识别计费说明](https://cloud.tencent.com/document/product/647/111976)

语音转文本不同套餐版本支持的语言如下：

**基础版**：
- "zh": 中文（简体）
- "zh-TW": 中文（繁体）
- "en": 英语
- "16k_zh_edu"：中文教育
- "16k_zh_medical"：中文医疗
- "16k_zh_court"：中文法庭

**标准版：**
- "8k_zh_large": 普方大模型引擎. 当前模型同时支持中文等语言的识别，模型参数量极大，语言模型性能增强，针对电话音频中各类场景、各类中文方言的识别准确率极大提升.
- "16k_zh_large": 普方英大模型引擎. 当前模型同时支持中文、英文、多种中文方言等语言的识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.
- "16k_multi_lang": 多语种大模型引擎. 当前模型同时支持英语、日语、韩语、阿拉伯语、菲律宾语、法语、印地语、印尼语、马来语、葡萄牙语、西班牙语、泰语、土耳其语、越南语、德语的识别，可实现15个语种的自动识别(句子/段落级别).
- "16k_zh_en": 中英大模型引擎. 当前模型同时支持中文、英语识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.

**高级版：**
- "zh-dialect": 中国方言
- "zh-yue": 中国粤语
- "vi": 越南语
- "ja": 日语
- "ko": 韩语
- "id": 印度尼西亚语
- "th": 泰语
- "pt": 葡萄牙语
- "tr": 土耳其语
- "ar": 阿拉伯语
- "es": 西班牙语
- "hi": 印地语
- "fr": 法语
- "ms": 马来语
- "fil": 菲律宾语
- "de": 德语
- "it": 意大利语
- "ru": 俄语
- "sv": 瑞典语
- "da": 丹麦语
- "no": 挪威语

**注意：**
如果缺少满足您需求的语言，请联系我们技术人员。
        :type Language: str
        :param _AlternativeLanguage: **发起模糊识别为高级版能力,默认按照高级版收费,仅支持填写基础版和高级版语言.**
注意：不支持填写"zh-dialect"
        :type AlternativeLanguage: list of str
        :param _Model: 目前已不支持
        :type Model: str
        :param _TranslationLanguage: 填写则翻译，目前支持的语言：
中文: zh
英语: en
越南语: vi
日语: ja
韩语: ko
印度尼西亚语: id
泰语: th
葡萄牙语: pt
土耳其语: tr
阿拉伯语: ar
西班牙语: es
印地语: hi
法语: fr
马来语: ms
菲律宾语: fil
德语: de
意大利语: it
俄语: ru
瑞典语: sv
挪威语: no
丹麦语: da
        :type TranslationLanguage: str
        :param _HotWordList: 热词表：该参数用于提升识别准确率。 单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重[1-11]或者100，如：“腾讯云|5” 或 “ASR|11”； 热词表限制：多个热词用英文逗号分割，最多支持300个热词，如：“腾讯云|10,语音识别|5,ASR|11”；
        :type HotWordList: str
        :param _VadSilenceTime: 语音识别vad的时间，范围为240-2000，默认为1000，单位为ms。更小的值会让语音识别分句更快。
        :type VadSilenceTime: int
        :param _VadLevel: vad的远场人声抑制能力（不会对asr识别效果造成影响），范围为[0, 3]，默认为0。推荐设置为2，有较好的远场人声抑制能力。
        :type VadLevel: int
        """
        self._Language = None
        self._AlternativeLanguage = None
        self._Model = None
        self._TranslationLanguage = None
        self._HotWordList = None
        self._VadSilenceTime = None
        self._VadLevel = None

    @property
    def Language(self):
        r"""
语音转文字支持识别的语言，默认是"zh" 中文

可通过购买「AI智能识别时长包」解锁或领取包月套餐体验版解锁不同语言. 详细说明参考：[AI智能识别计费说明](https://cloud.tencent.com/document/product/647/111976)

语音转文本不同套餐版本支持的语言如下：

**基础版**：
- "zh": 中文（简体）
- "zh-TW": 中文（繁体）
- "en": 英语
- "16k_zh_edu"：中文教育
- "16k_zh_medical"：中文医疗
- "16k_zh_court"：中文法庭

**标准版：**
- "8k_zh_large": 普方大模型引擎. 当前模型同时支持中文等语言的识别，模型参数量极大，语言模型性能增强，针对电话音频中各类场景、各类中文方言的识别准确率极大提升.
- "16k_zh_large": 普方英大模型引擎. 当前模型同时支持中文、英文、多种中文方言等语言的识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.
- "16k_multi_lang": 多语种大模型引擎. 当前模型同时支持英语、日语、韩语、阿拉伯语、菲律宾语、法语、印地语、印尼语、马来语、葡萄牙语、西班牙语、泰语、土耳其语、越南语、德语的识别，可实现15个语种的自动识别(句子/段落级别).
- "16k_zh_en": 中英大模型引擎. 当前模型同时支持中文、英语识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.

**高级版：**
- "zh-dialect": 中国方言
- "zh-yue": 中国粤语
- "vi": 越南语
- "ja": 日语
- "ko": 韩语
- "id": 印度尼西亚语
- "th": 泰语
- "pt": 葡萄牙语
- "tr": 土耳其语
- "ar": 阿拉伯语
- "es": 西班牙语
- "hi": 印地语
- "fr": 法语
- "ms": 马来语
- "fil": 菲律宾语
- "de": 德语
- "it": 意大利语
- "ru": 俄语
- "sv": 瑞典语
- "da": 丹麦语
- "no": 挪威语

**注意：**
如果缺少满足您需求的语言，请联系我们技术人员。
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def AlternativeLanguage(self):
        r"""**发起模糊识别为高级版能力,默认按照高级版收费,仅支持填写基础版和高级版语言.**
注意：不支持填写"zh-dialect"
        :rtype: list of str
        """
        return self._AlternativeLanguage

    @AlternativeLanguage.setter
    def AlternativeLanguage(self, AlternativeLanguage):
        self._AlternativeLanguage = AlternativeLanguage

    @property
    def Model(self):
        warnings.warn("parameter `Model` is deprecated", DeprecationWarning) 

        r"""目前已不支持
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        warnings.warn("parameter `Model` is deprecated", DeprecationWarning) 

        self._Model = Model

    @property
    def TranslationLanguage(self):
        warnings.warn("parameter `TranslationLanguage` is deprecated", DeprecationWarning) 

        r"""填写则翻译，目前支持的语言：
中文: zh
英语: en
越南语: vi
日语: ja
韩语: ko
印度尼西亚语: id
泰语: th
葡萄牙语: pt
土耳其语: tr
阿拉伯语: ar
西班牙语: es
印地语: hi
法语: fr
马来语: ms
菲律宾语: fil
德语: de
意大利语: it
俄语: ru
瑞典语: sv
挪威语: no
丹麦语: da
        :rtype: str
        """
        return self._TranslationLanguage

    @TranslationLanguage.setter
    def TranslationLanguage(self, TranslationLanguage):
        warnings.warn("parameter `TranslationLanguage` is deprecated", DeprecationWarning) 

        self._TranslationLanguage = TranslationLanguage

    @property
    def HotWordList(self):
        r"""热词表：该参数用于提升识别准确率。 单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重[1-11]或者100，如：“腾讯云|5” 或 “ASR|11”； 热词表限制：多个热词用英文逗号分割，最多支持300个热词，如：“腾讯云|10,语音识别|5,ASR|11”；
        :rtype: str
        """
        return self._HotWordList

    @HotWordList.setter
    def HotWordList(self, HotWordList):
        self._HotWordList = HotWordList

    @property
    def VadSilenceTime(self):
        r"""语音识别vad的时间，范围为240-2000，默认为1000，单位为ms。更小的值会让语音识别分句更快。
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime

    @property
    def VadLevel(self):
        r"""vad的远场人声抑制能力（不会对asr识别效果造成影响），范围为[0, 3]，默认为0。推荐设置为2，有较好的远场人声抑制能力。
        :rtype: int
        """
        return self._VadLevel

    @VadLevel.setter
    def VadLevel(self, VadLevel):
        self._VadLevel = VadLevel


    def _deserialize(self, params):
        self._Language = params.get("Language")
        self._AlternativeLanguage = params.get("AlternativeLanguage")
        self._Model = params.get("Model")
        self._TranslationLanguage = params.get("TranslationLanguage")
        self._HotWordList = params.get("HotWordList")
        self._VadSilenceTime = params.get("VadSilenceTime")
        self._VadLevel = params.get("VadLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordParams(AbstractModel):
    r"""云端录制控制参数。

    """

    def __init__(self):
        r"""
        :param _RecordMode: 录制模式：
1：单流录制，分别录制房间的订阅UserId的音频和视频，将录制文件上传至云存储；
2：合流录制，将房间内订阅UserId的音视频混录成一个音视频文件，将录制文件上传至云存储；
        :type RecordMode: int
        :param _MaxIdleTime: 房间内持续没有主播的状态超过MaxIdleTime的时长，自动停止录制，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
        :type MaxIdleTime: int
        :param _StreamType: 录制的媒体流类型：
0：录制音频+视频流（默认）;
1：仅录制音频流；
2：仅录制视频流，
        :type StreamType: int
        :param _SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        :param _OutputFormat: 输出文件的格式（存储至COS等第三方存储时有效）。0：(默认)输出文件为hls格式。1：输出文件格式为hls+mp4。2：输出文件格式为hls+aac 。3：输出文件格式为mp4。4：输出文件格式为aac。

存储到云点播VOD时此参数无效，存储到VOD时请通过TencentVod（https://cloud.tencent.com/document/api/647/44055#TencentVod）内的MediaType设置。
        :type OutputFormat: int
        :param _AvMerge: 单流录制模式下，用户的音视频是否合并，0：单流音视频不合并（默认）。1：单流音视频合并成一个ts。合流录制此参数无需设置，默认音视频合并。
        :type AvMerge: int
        :param _MaxMediaFileDuration: 如果是aac或者mp4文件格式，超过长度限制后，系统会自动拆分视频文件。单位：分钟。默认为1440min（24h），取值范围为1-1440。【单文件限制最大为2G，满足文件大小 >2G 或录制时长度 > 24h任意一个条件，文件都会自动切分】
Hls 格式录制此参数不生效。
        :type MaxMediaFileDuration: int
        :param _MediaId: 指定录制主辅流，0：主流+辅流（默认）；1:主流；2:辅流。
        :type MediaId: int
        :param _FillType: 上行视频停止时，录制的补帧类型，0：补最后一帧 1：补黑帧
        :type FillType: int
        """
        self._RecordMode = None
        self._MaxIdleTime = None
        self._StreamType = None
        self._SubscribeStreamUserIds = None
        self._OutputFormat = None
        self._AvMerge = None
        self._MaxMediaFileDuration = None
        self._MediaId = None
        self._FillType = None

    @property
    def RecordMode(self):
        r"""录制模式：
1：单流录制，分别录制房间的订阅UserId的音频和视频，将录制文件上传至云存储；
2：合流录制，将房间内订阅UserId的音视频混录成一个音视频文件，将录制文件上传至云存储；
        :rtype: int
        """
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def MaxIdleTime(self):
        r"""房间内持续没有主播的状态超过MaxIdleTime的时长，自动停止录制，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def StreamType(self):
        r"""录制的媒体流类型：
0：录制音频+视频流（默认）;
1：仅录制音频流；
2：仅录制视频流，
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def SubscribeStreamUserIds(self):
        r"""指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

    @property
    def OutputFormat(self):
        r"""输出文件的格式（存储至COS等第三方存储时有效）。0：(默认)输出文件为hls格式。1：输出文件格式为hls+mp4。2：输出文件格式为hls+aac 。3：输出文件格式为mp4。4：输出文件格式为aac。

存储到云点播VOD时此参数无效，存储到VOD时请通过TencentVod（https://cloud.tencent.com/document/api/647/44055#TencentVod）内的MediaType设置。
        :rtype: int
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def AvMerge(self):
        r"""单流录制模式下，用户的音视频是否合并，0：单流音视频不合并（默认）。1：单流音视频合并成一个ts。合流录制此参数无需设置，默认音视频合并。
        :rtype: int
        """
        return self._AvMerge

    @AvMerge.setter
    def AvMerge(self, AvMerge):
        self._AvMerge = AvMerge

    @property
    def MaxMediaFileDuration(self):
        r"""如果是aac或者mp4文件格式，超过长度限制后，系统会自动拆分视频文件。单位：分钟。默认为1440min（24h），取值范围为1-1440。【单文件限制最大为2G，满足文件大小 >2G 或录制时长度 > 24h任意一个条件，文件都会自动切分】
Hls 格式录制此参数不生效。
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration

    @property
    def MediaId(self):
        r"""指定录制主辅流，0：主流+辅流（默认）；1:主流；2:辅流。
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def FillType(self):
        r"""上行视频停止时，录制的补帧类型，0：补最后一帧 1：补黑帧
        :rtype: int
        """
        return self._FillType

    @FillType.setter
    def FillType(self, FillType):
        self._FillType = FillType


    def _deserialize(self, params):
        self._RecordMode = params.get("RecordMode")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._StreamType = params.get("StreamType")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self._OutputFormat = params.get("OutputFormat")
        self._AvMerge = params.get("AvMerge")
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        self._MediaId = params.get("MediaId")
        self._FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordUsage(AbstractModel):
    r"""录制的使用信息。

    """

    def __init__(self):
        r"""
        :param _TimeKey: 本组数据对应的时间点，格式如:2020-09-07或2020-09-07 00:05:05。
        :type TimeKey: str
        :param _Class1VideoTime: 视频时长-标清SD，单位：秒。
        :type Class1VideoTime: int
        :param _Class2VideoTime: 视频时长-高清HD，单位：秒。
        :type Class2VideoTime: int
        :param _Class3VideoTime: 视频时长-超清HD，单位：秒。
        :type Class3VideoTime: int
        :param _AudioTime: 语音时长，单位：秒。
        :type AudioTime: int
        """
        self._TimeKey = None
        self._Class1VideoTime = None
        self._Class2VideoTime = None
        self._Class3VideoTime = None
        self._AudioTime = None

    @property
    def TimeKey(self):
        r"""本组数据对应的时间点，格式如:2020-09-07或2020-09-07 00:05:05。
        :rtype: str
        """
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def Class1VideoTime(self):
        r"""视频时长-标清SD，单位：秒。
        :rtype: int
        """
        return self._Class1VideoTime

    @Class1VideoTime.setter
    def Class1VideoTime(self, Class1VideoTime):
        self._Class1VideoTime = Class1VideoTime

    @property
    def Class2VideoTime(self):
        r"""视频时长-高清HD，单位：秒。
        :rtype: int
        """
        return self._Class2VideoTime

    @Class2VideoTime.setter
    def Class2VideoTime(self, Class2VideoTime):
        self._Class2VideoTime = Class2VideoTime

    @property
    def Class3VideoTime(self):
        r"""视频时长-超清HD，单位：秒。
        :rtype: int
        """
        return self._Class3VideoTime

    @Class3VideoTime.setter
    def Class3VideoTime(self, Class3VideoTime):
        self._Class3VideoTime = Class3VideoTime

    @property
    def AudioTime(self):
        r"""语音时长，单位：秒。
        :rtype: int
        """
        return self._AudioTime

    @AudioTime.setter
    def AudioTime(self, AudioTime):
        self._AudioTime = AudioTime


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._Class1VideoTime = params.get("Class1VideoTime")
        self._Class2VideoTime = params.get("Class2VideoTime")
        self._Class3VideoTime = params.get("Class3VideoTime")
        self._AudioTime = params.get("AudioTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterVoicePrintRequest(AbstractModel):
    r"""RegisterVoicePrint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Audio: 整个wav音频文件的base64字符串,其中wav文件限定为16k采样率, 16bit位深, 单声道, 8到18秒音频时长,有效音频不小于6秒(不能有太多静音段),编码数据大小不超过2M
        :type Audio: str
        :param _ReqTimestamp: 毫秒时间戳
        :type ReqTimestamp: int
        :param _AudioFormat: 音频格式,目前只支持0,代表wav
        :type AudioFormat: int
        :param _AudioName: 音频名称,长度不要超过32
        :type AudioName: str
        :param _AudioMetaInfo: 和声纹绑定的MetaInfo，长度最大不超过512
        :type AudioMetaInfo: str
        """
        self._Audio = None
        self._ReqTimestamp = None
        self._AudioFormat = None
        self._AudioName = None
        self._AudioMetaInfo = None

    @property
    def Audio(self):
        r"""整个wav音频文件的base64字符串,其中wav文件限定为16k采样率, 16bit位深, 单声道, 8到18秒音频时长,有效音频不小于6秒(不能有太多静音段),编码数据大小不超过2M
        :rtype: str
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def ReqTimestamp(self):
        r"""毫秒时间戳
        :rtype: int
        """
        return self._ReqTimestamp

    @ReqTimestamp.setter
    def ReqTimestamp(self, ReqTimestamp):
        self._ReqTimestamp = ReqTimestamp

    @property
    def AudioFormat(self):
        r"""音频格式,目前只支持0,代表wav
        :rtype: int
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def AudioName(self):
        r"""音频名称,长度不要超过32
        :rtype: str
        """
        return self._AudioName

    @AudioName.setter
    def AudioName(self, AudioName):
        self._AudioName = AudioName

    @property
    def AudioMetaInfo(self):
        r"""和声纹绑定的MetaInfo，长度最大不超过512
        :rtype: str
        """
        return self._AudioMetaInfo

    @AudioMetaInfo.setter
    def AudioMetaInfo(self, AudioMetaInfo):
        self._AudioMetaInfo = AudioMetaInfo


    def _deserialize(self, params):
        self._Audio = params.get("Audio")
        self._ReqTimestamp = params.get("ReqTimestamp")
        self._AudioFormat = params.get("AudioFormat")
        self._AudioName = params.get("AudioName")
        self._AudioMetaInfo = params.get("AudioMetaInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterVoicePrintResponse(AbstractModel):
    r"""RegisterVoicePrint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 声纹信息ID
        :type VoicePrintId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VoicePrintId = None
        self._RequestId = None

    @property
    def VoicePrintId(self):
        r"""声纹信息ID
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        self._RequestId = params.get("RequestId")


class RemoveUserByStrRoomIdRequest(AbstractModel):
    r"""RemoveUserByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _RoomId: 房间号。
        :type RoomId: str
        :param _UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserIds = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间号。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
        r"""要移出的用户列表，最多10个。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdResponse(AbstractModel):
    r"""RemoveUserByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RemoveUserRequest(AbstractModel):
    r"""RemoveUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _RoomId: 房间号。
        :type RoomId: int
        :param _UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserIds = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间号。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
        r"""要移出的用户列表，最多10个。
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserResponse(AbstractModel):
    r"""RemoveUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RoomState(AbstractModel):
    r"""房间信息列表

    """

    def __init__(self):
        r"""
        :param _CommId: 通话ID（唯一标识一次通话）
        :type CommId: str
        :param _RoomString: 房间号
        :type RoomString: str
        :param _CreateTime: 房间创建时间
        :type CreateTime: int
        :param _DestroyTime: 房间销毁时间
        :type DestroyTime: int
        :param _IsFinished: 房间是否已经结束
        :type IsFinished: bool
        :param _UserId: 房间创建者Id
        :type UserId: str
        """
        self._CommId = None
        self._RoomString = None
        self._CreateTime = None
        self._DestroyTime = None
        self._IsFinished = None
        self._UserId = None

    @property
    def CommId(self):
        r"""通话ID（唯一标识一次通话）
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def RoomString(self):
        r"""房间号
        :rtype: str
        """
        return self._RoomString

    @RoomString.setter
    def RoomString(self, RoomString):
        self._RoomString = RoomString

    @property
    def CreateTime(self):
        r"""房间创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DestroyTime(self):
        r"""房间销毁时间
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def IsFinished(self):
        r"""房间是否已经结束
        :rtype: bool
        """
        return self._IsFinished

    @IsFinished.setter
    def IsFinished(self, IsFinished):
        self._IsFinished = IsFinished

    @property
    def UserId(self):
        r"""房间创建者Id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._RoomString = params.get("RoomString")
        self._CreateTime = params.get("CreateTime")
        self._DestroyTime = params.get("DestroyTime")
        self._IsFinished = params.get("IsFinished")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowValues(AbstractModel):
    r"""SeriesInfo类型的二维数组

    """

    def __init__(self):
        r"""
        :param _RowValue: 数据值
注意：此字段可能返回 null，表示取不到有效值。
        :type RowValue: list of int
        """
        self._RowValue = None

    @property
    def RowValue(self):
        r"""数据值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._RowValue

    @RowValue.setter
    def RowValue(self, RowValue):
        self._RowValue = RowValue


    def _deserialize(self, params):
        self._RowValue = params.get("RowValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class STTConfig(AbstractModel):
    r"""语音转文字参数

    """

    def __init__(self):
        r"""
        :param _Language: 
语音转文字支持识别的语言，默认是"zh" 中文

可通过购买「AI智能识别时长包」解锁或领取包月套餐体验版解锁不同语言. 详细说明参考：[AI智能识别计费说明](https://cloud.tencent.com/document/product/647/111976)

语音转文本不同套餐版本支持的语言如下：

**基础版**：
- "zh": 中文（简体）
- "zh-TW": 中文（繁体）
- "en": 英语
- "16k_zh_edu"：中文教育
- "16k_zh_medical"：中文医疗
- "16k_zh_court"：中文法庭

**标准版：**
- "8k_zh_large": 普方大模型引擎. 当前模型同时支持中文等语言的识别，模型参数量极大，语言模型性能增强，针对电话音频中各类场景、各类中文方言的识别准确率极大提升.
- "16k_zh_large": 普方英大模型引擎. 当前模型同时支持中文、英文、多种中文方言等语言的识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.
- "16k_multi_lang": 多语种大模型引擎. 当前模型同时支持英语、日语、韩语、阿拉伯语、菲律宾语、法语、印地语、印尼语、马来语、葡萄牙语、西班牙语、泰语、土耳其语、越南语、德语的识别，可实现15个语种的自动识别(句子/段落级别).
- "16k_zh_en": 中英大模型引擎. 当前模型同时支持中文、英语识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.

**高级版：**
- "zh-dialect": 中国方言
- "zh-yue": 中国粤语
- "vi": 越南语
- "ja": 日语
- "ko": 韩语
- "id": 印度尼西亚语
- "th": 泰语
- "pt": 葡萄牙语
- "tr": 土耳其语
- "ar": 阿拉伯语
- "es": 西班牙语
- "hi": 印地语
- "fr": 法语
- "ms": 马来语
- "fil": 菲律宾语
- "de": 德语
- "it": 意大利语
- "ru": 俄语
- "sv": 瑞典语
- "da": 丹麦语
- "no": 挪威语

**注意：**
如果缺少满足您需求的语言，请联系我们技术人员。
        :type Language: str
        :param _AlternativeLanguage: **发起模糊识别为高级版能力,默认按照高级版收费**
注意：不支持填写"zh-dialect", "16k_zh_edu", "16k_zh_medical", "16k_zh_court", "8k_zh_large", "16k_zh_large","16k_multi_lang", "16k_zh_en"

        :type AlternativeLanguage: list of str
        :param _CustomParam: 自定义参数，联系后台使用

        :type CustomParam: str
        :param _VadSilenceTime: 语音识别vad的时间，范围为240-2000，默认为1000，单位为ms。更小的值会让语音识别分句更快。
        :type VadSilenceTime: int
        :param _HotWordList: 热词表：该参数用于提升识别准确率。 单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重[1-11]或者100，如：“腾讯云|5” 或 “ASR|11”； 热词表限制：多个热词用英文逗号分割，最多支持128个热词，如：“腾讯云|10,语音识别|5,ASR|11”；
        :type HotWordList: str
        :param _VadLevel: vad的远场人声抑制能力（不会对asr识别效果造成影响），范围为[0, 5]，默认为0，表示不开启远场人声抑制能力。推荐设置为2，有较好的远场人声抑制能力。嘈杂的办公室环境下可以设置为3，更为嘈杂的环境下可以使用4和5。注意较高的VadLevel可能会将单字当作噪声给过滤。
        :type VadLevel: int
        """
        self._Language = None
        self._AlternativeLanguage = None
        self._CustomParam = None
        self._VadSilenceTime = None
        self._HotWordList = None
        self._VadLevel = None

    @property
    def Language(self):
        r"""
语音转文字支持识别的语言，默认是"zh" 中文

可通过购买「AI智能识别时长包」解锁或领取包月套餐体验版解锁不同语言. 详细说明参考：[AI智能识别计费说明](https://cloud.tencent.com/document/product/647/111976)

语音转文本不同套餐版本支持的语言如下：

**基础版**：
- "zh": 中文（简体）
- "zh-TW": 中文（繁体）
- "en": 英语
- "16k_zh_edu"：中文教育
- "16k_zh_medical"：中文医疗
- "16k_zh_court"：中文法庭

**标准版：**
- "8k_zh_large": 普方大模型引擎. 当前模型同时支持中文等语言的识别，模型参数量极大，语言模型性能增强，针对电话音频中各类场景、各类中文方言的识别准确率极大提升.
- "16k_zh_large": 普方英大模型引擎. 当前模型同时支持中文、英文、多种中文方言等语言的识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.
- "16k_multi_lang": 多语种大模型引擎. 当前模型同时支持英语、日语、韩语、阿拉伯语、菲律宾语、法语、印地语、印尼语、马来语、葡萄牙语、西班牙语、泰语、土耳其语、越南语、德语的识别，可实现15个语种的自动识别(句子/段落级别).
- "16k_zh_en": 中英大模型引擎. 当前模型同时支持中文、英语识别，模型参数量极大，语言模型性能增强，针对噪声大、回音大、人声小、人声远等低质量音频的识别准确率极大提升.

**高级版：**
- "zh-dialect": 中国方言
- "zh-yue": 中国粤语
- "vi": 越南语
- "ja": 日语
- "ko": 韩语
- "id": 印度尼西亚语
- "th": 泰语
- "pt": 葡萄牙语
- "tr": 土耳其语
- "ar": 阿拉伯语
- "es": 西班牙语
- "hi": 印地语
- "fr": 法语
- "ms": 马来语
- "fil": 菲律宾语
- "de": 德语
- "it": 意大利语
- "ru": 俄语
- "sv": 瑞典语
- "da": 丹麦语
- "no": 挪威语

**注意：**
如果缺少满足您需求的语言，请联系我们技术人员。
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def AlternativeLanguage(self):
        r"""**发起模糊识别为高级版能力,默认按照高级版收费**
注意：不支持填写"zh-dialect", "16k_zh_edu", "16k_zh_medical", "16k_zh_court", "8k_zh_large", "16k_zh_large","16k_multi_lang", "16k_zh_en"

        :rtype: list of str
        """
        return self._AlternativeLanguage

    @AlternativeLanguage.setter
    def AlternativeLanguage(self, AlternativeLanguage):
        self._AlternativeLanguage = AlternativeLanguage

    @property
    def CustomParam(self):
        r"""自定义参数，联系后台使用

        :rtype: str
        """
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def VadSilenceTime(self):
        r"""语音识别vad的时间，范围为240-2000，默认为1000，单位为ms。更小的值会让语音识别分句更快。
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime

    @property
    def HotWordList(self):
        r"""热词表：该参数用于提升识别准确率。 单个热词限制："热词|权重"，单个热词不超过30个字符（最多10个汉字），权重[1-11]或者100，如：“腾讯云|5” 或 “ASR|11”； 热词表限制：多个热词用英文逗号分割，最多支持128个热词，如：“腾讯云|10,语音识别|5,ASR|11”；
        :rtype: str
        """
        return self._HotWordList

    @HotWordList.setter
    def HotWordList(self, HotWordList):
        self._HotWordList = HotWordList

    @property
    def VadLevel(self):
        r"""vad的远场人声抑制能力（不会对asr识别效果造成影响），范围为[0, 5]，默认为0，表示不开启远场人声抑制能力。推荐设置为2，有较好的远场人声抑制能力。嘈杂的办公室环境下可以设置为3，更为嘈杂的环境下可以使用4和5。注意较高的VadLevel可能会将单字当作噪声给过滤。
        :rtype: int
        """
        return self._VadLevel

    @VadLevel.setter
    def VadLevel(self, VadLevel):
        self._VadLevel = VadLevel


    def _deserialize(self, params):
        self._Language = params.get("Language")
        self._AlternativeLanguage = params.get("AlternativeLanguage")
        self._CustomParam = params.get("CustomParam")
        self._VadSilenceTime = params.get("VadSilenceTime")
        self._HotWordList = params.get("HotWordList")
        self._VadLevel = params.get("VadLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInfomation(AbstractModel):
    r"""历史规模信息

    """

    def __init__(self):
        r"""
        :param _Time: 每天开始的时间
        :type Time: int
        :param _UserNumber: 房间人数，用户重复进入同一个房间为1次
        :type UserNumber: int
        :param _UserCount: 房间人次，用户每次进入房间为一次
        :type UserCount: int
        :param _RoomNumbers: sdkappid下一天内的房间数
        :type RoomNumbers: int
        """
        self._Time = None
        self._UserNumber = None
        self._UserCount = None
        self._RoomNumbers = None

    @property
    def Time(self):
        r"""每天开始的时间
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def UserNumber(self):
        r"""房间人数，用户重复进入同一个房间为1次
        :rtype: int
        """
        return self._UserNumber

    @UserNumber.setter
    def UserNumber(self, UserNumber):
        self._UserNumber = UserNumber

    @property
    def UserCount(self):
        r"""房间人次，用户每次进入房间为一次
        :rtype: int
        """
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount

    @property
    def RoomNumbers(self):
        r"""sdkappid下一天内的房间数
        :rtype: int
        """
        return self._RoomNumbers

    @RoomNumbers.setter
    def RoomNumbers(self, RoomNumbers):
        self._RoomNumbers = RoomNumbers


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._UserNumber = params.get("UserNumber")
        self._UserCount = params.get("UserCount")
        self._RoomNumbers = params.get("RoomNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdRecordUsage(AbstractModel):
    r"""SdkAppId级别录制时长数据。

    """

    def __init__(self):
        r"""
        :param _SdkAppId: SdkAppId的值。
        :type SdkAppId: str
        :param _Usages: 统计的时间点数据。
        :type Usages: list of RecordUsage
        """
        self._SdkAppId = None
        self._Usages = None

    @property
    def SdkAppId(self):
        r"""SdkAppId的值。
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def Usages(self):
        r"""统计的时间点数据。
        :rtype: list of RecordUsage
        """
        return self._Usages

    @Usages.setter
    def Usages(self, Usages):
        self._Usages = Usages


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        if params.get("Usages") is not None:
            self._Usages = []
            for item in params.get("Usages"):
                obj = RecordUsage()
                obj._deserialize(item)
                self._Usages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SdkAppIdTrtcMcuTranscodeTimeUsage(AbstractModel):
    r"""查询旁路转码计费时长。
    查询时间小于等于1天时，返回每5分钟粒度的数据；查询时间大于1天时，返回按天汇总的数据。

    """

    def __init__(self):
        r"""
        :param _TimeKey: 本组数据对应的时间点，格式如：2020-09-07或2020-09-07 00:05:05。
        :type TimeKey: str
        :param _AudioTime: 语音时长，单位：秒。
        :type AudioTime: int
        :param _VideoTimeSd: 视频时长-标清SD，单位：秒。
        :type VideoTimeSd: int
        :param _VideoTimeHd: 视频时长-高清HD，单位：秒。
        :type VideoTimeHd: int
        :param _VideoTimeFhd: 视频时长-全高清FHD，单位：秒。
        :type VideoTimeFhd: int
        :param _Flux: 带宽，单位：Mbps。
        :type Flux: float
        """
        self._TimeKey = None
        self._AudioTime = None
        self._VideoTimeSd = None
        self._VideoTimeHd = None
        self._VideoTimeFhd = None
        self._Flux = None

    @property
    def TimeKey(self):
        r"""本组数据对应的时间点，格式如：2020-09-07或2020-09-07 00:05:05。
        :rtype: str
        """
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def AudioTime(self):
        r"""语音时长，单位：秒。
        :rtype: int
        """
        return self._AudioTime

    @AudioTime.setter
    def AudioTime(self, AudioTime):
        self._AudioTime = AudioTime

    @property
    def VideoTimeSd(self):
        r"""视频时长-标清SD，单位：秒。
        :rtype: int
        """
        return self._VideoTimeSd

    @VideoTimeSd.setter
    def VideoTimeSd(self, VideoTimeSd):
        self._VideoTimeSd = VideoTimeSd

    @property
    def VideoTimeHd(self):
        r"""视频时长-高清HD，单位：秒。
        :rtype: int
        """
        return self._VideoTimeHd

    @VideoTimeHd.setter
    def VideoTimeHd(self, VideoTimeHd):
        self._VideoTimeHd = VideoTimeHd

    @property
    def VideoTimeFhd(self):
        r"""视频时长-全高清FHD，单位：秒。
        :rtype: int
        """
        return self._VideoTimeFhd

    @VideoTimeFhd.setter
    def VideoTimeFhd(self, VideoTimeFhd):
        self._VideoTimeFhd = VideoTimeFhd

    @property
    def Flux(self):
        r"""带宽，单位：Mbps。
        :rtype: float
        """
        return self._Flux

    @Flux.setter
    def Flux(self, Flux):
        self._Flux = Flux


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._AudioTime = params.get("AudioTime")
        self._VideoTimeSd = params.get("VideoTimeSd")
        self._VideoTimeHd = params.get("VideoTimeHd")
        self._VideoTimeFhd = params.get("VideoTimeFhd")
        self._Flux = params.get("Flux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeriesInfo(AbstractModel):
    r"""SeriesInfo类型

    """

    def __init__(self):
        r"""
        :param _Columns: 数据列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of str
        :param _Values: 数据值
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of int
        """
        self._Columns = None
        self._Values = None

    @property
    def Columns(self):
        r"""数据列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Values(self):
        r"""数据值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Columns = params.get("Columns")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeriesInfos(AbstractModel):
    r"""SeriesInfos类型

    """

    def __init__(self):
        r"""
        :param _Columns: 数据列
注意：此字段可能返回 null，表示取不到有效值。
        :type Columns: list of str
        :param _Values: 数据值
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of RowValues
        """
        self._Columns = None
        self._Values = None

    @property
    def Columns(self):
        r"""数据列
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Values(self):
        r"""数据值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RowValues
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Columns = params.get("Columns")
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = RowValues()
                obj._deserialize(item)
                self._Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerPushText(AbstractModel):
    r"""服务端控制AI对话机器人播报指定文本

    """

    def __init__(self):
        r"""
        :param _Text: 服务端推送播报文本
        :type Text: str
        :param _Interrupt: 是否允许该文本打断机器人说话
        :type Interrupt: bool
        :param _StopAfterPlay: 播报完文本后，是否自动关闭对话任务
        :type StopAfterPlay: bool
        :param _Audio: 服务端推送播报音频
    格式说明：音频必须为单声道，采样率必须跟对应TTS的采样率保持一致，编码为Base64字符串。
    输入规则：当提供Audio字段时，将不接受Text字段的输入。系统将直接播放Audio字段中的音频内容。
        :type Audio: str
        :param _DropMode: 默认为0，仅在Interrupt为false时有效
- 0表示当前有交互发生时，会丢弃Interrupt为false的消息
- 1表示当前有交互发生时，不会丢弃Interrupt为false的消息，而是缓存下来，等待当前交互结束后，再去处理

注意：DropMode为1时，允许缓存多个消息，如果后续出现了打断，缓存的消息会被清空
        :type DropMode: int
        :param _Priority: ServerPushText消息的优先级，0表示可被打断，1表示不会被打断。**目前仅支持传入0，如果需要传入1，请提工单联系我们添加权限。**
注意：在接收到Priority=1的消息后，后续其他任何消息都会被忽略（包括Priority=1的消息），直到Priority=1的消息处理结束。该字段可与Interrupt、DropMode字段配合使用。
例子：
- Priority=1、Interrupt=true，会打断现有交互，立刻播报，播报过程中不会被打断
- Priority=1、Interrupt=false、DropMode=1，会等待当前交互结束，再进行播报，播报过程中不会被打断

        :type Priority: int
        :param _AddHistory: 是否将文本加入到llm历史上下文中
        :type AddHistory: bool
        """
        self._Text = None
        self._Interrupt = None
        self._StopAfterPlay = None
        self._Audio = None
        self._DropMode = None
        self._Priority = None
        self._AddHistory = None

    @property
    def Text(self):
        r"""服务端推送播报文本
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Interrupt(self):
        r"""是否允许该文本打断机器人说话
        :rtype: bool
        """
        return self._Interrupt

    @Interrupt.setter
    def Interrupt(self, Interrupt):
        self._Interrupt = Interrupt

    @property
    def StopAfterPlay(self):
        r"""播报完文本后，是否自动关闭对话任务
        :rtype: bool
        """
        return self._StopAfterPlay

    @StopAfterPlay.setter
    def StopAfterPlay(self, StopAfterPlay):
        self._StopAfterPlay = StopAfterPlay

    @property
    def Audio(self):
        r"""服务端推送播报音频
    格式说明：音频必须为单声道，采样率必须跟对应TTS的采样率保持一致，编码为Base64字符串。
    输入规则：当提供Audio字段时，将不接受Text字段的输入。系统将直接播放Audio字段中的音频内容。
        :rtype: str
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def DropMode(self):
        r"""默认为0，仅在Interrupt为false时有效
- 0表示当前有交互发生时，会丢弃Interrupt为false的消息
- 1表示当前有交互发生时，不会丢弃Interrupt为false的消息，而是缓存下来，等待当前交互结束后，再去处理

注意：DropMode为1时，允许缓存多个消息，如果后续出现了打断，缓存的消息会被清空
        :rtype: int
        """
        return self._DropMode

    @DropMode.setter
    def DropMode(self, DropMode):
        self._DropMode = DropMode

    @property
    def Priority(self):
        r"""ServerPushText消息的优先级，0表示可被打断，1表示不会被打断。**目前仅支持传入0，如果需要传入1，请提工单联系我们添加权限。**
注意：在接收到Priority=1的消息后，后续其他任何消息都会被忽略（包括Priority=1的消息），直到Priority=1的消息处理结束。该字段可与Interrupt、DropMode字段配合使用。
例子：
- Priority=1、Interrupt=true，会打断现有交互，立刻播报，播报过程中不会被打断
- Priority=1、Interrupt=false、DropMode=1，会等待当前交互结束，再进行播报，播报过程中不会被打断

        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def AddHistory(self):
        r"""是否将文本加入到llm历史上下文中
        :rtype: bool
        """
        return self._AddHistory

    @AddHistory.setter
    def AddHistory(self, AddHistory):
        self._AddHistory = AddHistory


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Interrupt = params.get("Interrupt")
        self._StopAfterPlay = params.get("StopAfterPlay")
        self._Audio = params.get("Audio")
        self._DropMode = params.get("DropMode")
        self._Priority = params.get("Priority")
        self._AddHistory = params.get("AddHistory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleSubscribeParams(AbstractModel):
    r"""单流旁路转推的用户上行信息。

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: 用户媒体流参数。
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self._UserMediaStream = None

    @property
    def UserMediaStream(self):
        r"""用户媒体流参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SliceParams(AbstractModel):
    r"""云端切片的控制参数。

    """

    def __init__(self):
        r"""
        :param _SliceType: 切片任务类型:
1:音频切片；
2:视频截帧；
3:音视切片+视频截帧
示例值：1 
        :type SliceType: int
        :param _MaxIdleTime: 房间内持续没有主播的状态超过MaxIdleTime的时长，自动停止录制，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
示例值：30
        :type MaxIdleTime: int
        :param _SliceAudio: 音频切片时长，默认15s 示例值：15
取值范围15-60s
        :type SliceAudio: int
        :param _SliceVideo: 视频截帧间隔时长，默认5s， 示例值：5 取值范围5-60s
        :type SliceVideo: int
        :param _SubscribeStreamUserIds: 指定订阅流白名单或者黑名单。
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        :param _SliceCallbackUrl: 已废弃，从控制台配置回调url
        :type SliceCallbackUrl: str
        """
        self._SliceType = None
        self._MaxIdleTime = None
        self._SliceAudio = None
        self._SliceVideo = None
        self._SubscribeStreamUserIds = None
        self._SliceCallbackUrl = None

    @property
    def SliceType(self):
        r"""切片任务类型:
1:音频切片；
2:视频截帧；
3:音视切片+视频截帧
示例值：1 
        :rtype: int
        """
        return self._SliceType

    @SliceType.setter
    def SliceType(self, SliceType):
        self._SliceType = SliceType

    @property
    def MaxIdleTime(self):
        r"""房间内持续没有主播的状态超过MaxIdleTime的时长，自动停止录制，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
示例值：30
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def SliceAudio(self):
        r"""音频切片时长，默认15s 示例值：15
取值范围15-60s
        :rtype: int
        """
        return self._SliceAudio

    @SliceAudio.setter
    def SliceAudio(self, SliceAudio):
        self._SliceAudio = SliceAudio

    @property
    def SliceVideo(self):
        r"""视频截帧间隔时长，默认5s， 示例值：5 取值范围5-60s
        :rtype: int
        """
        return self._SliceVideo

    @SliceVideo.setter
    def SliceVideo(self, SliceVideo):
        self._SliceVideo = SliceVideo

    @property
    def SubscribeStreamUserIds(self):
        r"""指定订阅流白名单或者黑名单。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

    @property
    def SliceCallbackUrl(self):
        r"""已废弃，从控制台配置回调url
        :rtype: str
        """
        return self._SliceCallbackUrl

    @SliceCallbackUrl.setter
    def SliceCallbackUrl(self, SliceCallbackUrl):
        self._SliceCallbackUrl = SliceCallbackUrl


    def _deserialize(self, params):
        self._SliceType = params.get("SliceType")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._SliceAudio = params.get("SliceAudio")
        self._SliceVideo = params.get("SliceVideo")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self._SliceCallbackUrl = params.get("SliceCallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SliceStorageParams(AbstractModel):
    r"""切片存储参数

    """

    def __init__(self):
        r"""
        :param _CloudSliceStorage: 腾讯云对象存储COS以及第三方云存储的账号信息
        :type CloudSliceStorage: :class:`tencentcloud.trtc.v20190722.models.CloudSliceStorage`
        """
        self._CloudSliceStorage = None

    @property
    def CloudSliceStorage(self):
        r"""腾讯云对象存储COS以及第三方云存储的账号信息
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudSliceStorage`
        """
        return self._CloudSliceStorage

    @CloudSliceStorage.setter
    def CloudSliceStorage(self, CloudSliceStorage):
        self._CloudSliceStorage = CloudSliceStorage


    def _deserialize(self, params):
        if params.get("CloudSliceStorage") is not None:
            self._CloudSliceStorage = CloudSliceStorage()
            self._CloudSliceStorage._deserialize(params.get("CloudSliceStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmallVideoLayoutParams(AbstractModel):
    r"""画中画模板中有效，代表小画面的布局参数

    """

    def __init__(self):
        r"""
        :param _UserId: 代表小画面对应的用户ID。
        :type UserId: str
        :param _StreamType: 代表小画面对应的流类型，0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :type StreamType: int
        :param _ImageWidth: 小画面在输出时的宽度，单位为像素值，不填默认为0。
        :type ImageWidth: int
        :param _ImageHeight: 小画面在输出时的高度，单位为像素值，不填默认为0。
        :type ImageHeight: int
        :param _LocationX: 小画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :type LocationX: int
        :param _LocationY: 小画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :type LocationY: int
        """
        self._UserId = None
        self._StreamType = None
        self._ImageWidth = None
        self._ImageHeight = None
        self._LocationX = None
        self._LocationY = None

    @property
    def UserId(self):
        r"""代表小画面对应的用户ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def StreamType(self):
        r"""代表小画面对应的流类型，0为摄像头，1为屏幕分享。小画面为web用户时此值填0。
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def ImageWidth(self):
        r"""小画面在输出时的宽度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        r"""小画面在输出时的高度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def LocationX(self):
        r"""小画面在输出时的X偏移，单位为像素值，LocationX与ImageWidth之和不能超过混流输出的总宽度，不填默认为0。
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""小画面在输出时的Y偏移，单位为像素值，LocationY与ImageHeight之和不能超过混流输出的总高度，不填默认为0。
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._StreamType = params.get("StreamType")
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAIConversationRequest(AbstractModel):
    r"""StartAIConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和开启转录任务的房间使用的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，表示开启对话任务的房间号。
        :type RoomId: str
        :param _AgentConfig: 机器人参数
        :type AgentConfig: :class:`tencentcloud.trtc.v20190722.models.AgentConfig`
        :param _SessionId: 调用方传入的唯一Id，可用于客户侧防止重复发起任务以及可以通过该字段查询任务状态。
        :type SessionId: str
        :param _RoomIdType: TRTC房间号的类型，0代表数字房间号，1代表字符串房间号。不填默认是数字房间号。
        :type RoomIdType: int
        :param _STTConfig: 语音识别配置。
        :type STTConfig: :class:`tencentcloud.trtc.v20190722.models.STTConfig`
        :param _LLMConfig: LLM配置。需符合openai规范，为JSON字符串，示例如下：
<pre> { <br> &emsp;  "LLMType": "大模型类型",  // String 必填，如："openai" <br> &emsp;  "Model": "您的模型名称", // String 必填，指定使用的模型<br>    "APIKey": "您的LLM API密钥", // String 必填 <br> &emsp;  "APIUrl": "https://api.xxx.com/chat/completions", // String 必填，LLM API访问的URL<br> &emsp;  "History": 10, // Integer 选填，设置 LLM 的上下文轮次，默认值为0，最大值50<br> &emsp;  "HistoryMode": 1, // Integer 选填，1表示LLM上下文中的内容会和播放音频做同步，没有播放的音频对应的文本不会出现在上下文中。0表示不会做同步，默认值为0<br> &emsp;  "Streaming": true // Boolean 非必填，指定是否使用流式传输<br> &emsp;} </pre>

        :type LLMConfig: str
        :param _TTSConfig: TTS配置，为JSON字符串，腾讯云TTS示例如下： <pre>{ <br> &emsp; "AppId": 您的应用ID, // Integer 必填<br> &emsp; "TTSType": "TTS类型", // String TTS类型, 固定为"tencent"<br> &emsp; "SecretId": "您的密钥ID", // String 必填<br> &emsp; "SecretKey":  "您的密钥Key", // String 必填<br> &emsp; "VoiceType": 101001, // Integer  必填，音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见<a href="https://cloud.tencent.com/document/product/1073/34112">语音合成计费概述</a>。完整的音色 ID 列表请参见<a href="https://cloud.tencent.com/document/product/1073/92668#55924b56-1a73-4663-a7a1-a8dd82d6e823">语音合成音色列表</a>。<br> &emsp; "Speed": 1.25, // Integer 非必填，语速，范围：[-2，6]，分别对应不同语速： -2: 代表0.6倍 -1: 代表0.8倍 0: 代表1.0倍（默认） 1: 代表1.2倍 2: 代表1.5倍  6: 代表2.5倍  如果需要更细化的语速，可以保留小数点后 2 位，例如0.5/1.25/2.81等。 参数值与实际语速转换，可参考 <a href="https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz">语速转换</a><br> &emsp; "Volume": 5, // Integer 非必填，音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。<br> &emsp; "EmotionCategory":  "angry", // String 非必填 控制合成音频的情感，仅支持多情感音色使用。取值: neutral(中性)、sad(悲伤)、happy(高兴)、angry(生气)、fear(恐惧)、news(新闻)、story(故事)、radio(广播)、poetry(诗歌)、call(客服)、sajiao(撒娇)、disgusted(厌恶)、amaze(震惊)、peaceful(平静)、exciting(兴奋)、aojiao(傲娇)、jieshuo(解说)。<br> &emsp; "EmotionIntensity":  150 // Integer 非必填 控制合成音频情感程度，取值范围为 [50,200]，默认为 100；只有 EmotionCategory 不为空时生效。<br> &emsp; }</pre>
        :type TTSConfig: str
        :param _AvatarConfig: 数字人配置，为JSON字符串。**数字人配置需要提工单加白后才能使用**
        :type AvatarConfig: str
        :param _ExperimentalParams: 实验性参数,联系后台使用
        :type ExperimentalParams: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._AgentConfig = None
        self._SessionId = None
        self._RoomIdType = None
        self._STTConfig = None
        self._LLMConfig = None
        self._TTSConfig = None
        self._AvatarConfig = None
        self._ExperimentalParams = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和开启转录任务的房间使用的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，表示开启对话任务的房间号。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def AgentConfig(self):
        r"""机器人参数
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AgentConfig`
        """
        return self._AgentConfig

    @AgentConfig.setter
    def AgentConfig(self, AgentConfig):
        self._AgentConfig = AgentConfig

    @property
    def SessionId(self):
        r"""调用方传入的唯一Id，可用于客户侧防止重复发起任务以及可以通过该字段查询任务状态。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型，0代表数字房间号，1代表字符串房间号。不填默认是数字房间号。
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def STTConfig(self):
        r"""语音识别配置。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.STTConfig`
        """
        return self._STTConfig

    @STTConfig.setter
    def STTConfig(self, STTConfig):
        self._STTConfig = STTConfig

    @property
    def LLMConfig(self):
        r"""LLM配置。需符合openai规范，为JSON字符串，示例如下：
<pre> { <br> &emsp;  "LLMType": "大模型类型",  // String 必填，如："openai" <br> &emsp;  "Model": "您的模型名称", // String 必填，指定使用的模型<br>    "APIKey": "您的LLM API密钥", // String 必填 <br> &emsp;  "APIUrl": "https://api.xxx.com/chat/completions", // String 必填，LLM API访问的URL<br> &emsp;  "History": 10, // Integer 选填，设置 LLM 的上下文轮次，默认值为0，最大值50<br> &emsp;  "HistoryMode": 1, // Integer 选填，1表示LLM上下文中的内容会和播放音频做同步，没有播放的音频对应的文本不会出现在上下文中。0表示不会做同步，默认值为0<br> &emsp;  "Streaming": true // Boolean 非必填，指定是否使用流式传输<br> &emsp;} </pre>

        :rtype: str
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        r"""TTS配置，为JSON字符串，腾讯云TTS示例如下： <pre>{ <br> &emsp; "AppId": 您的应用ID, // Integer 必填<br> &emsp; "TTSType": "TTS类型", // String TTS类型, 固定为"tencent"<br> &emsp; "SecretId": "您的密钥ID", // String 必填<br> &emsp; "SecretKey":  "您的密钥Key", // String 必填<br> &emsp; "VoiceType": 101001, // Integer  必填，音色 ID，包括标准音色与精品音色，精品音色拟真度更高，价格不同于标准音色，请参见<a href="https://cloud.tencent.com/document/product/1073/34112">语音合成计费概述</a>。完整的音色 ID 列表请参见<a href="https://cloud.tencent.com/document/product/1073/92668#55924b56-1a73-4663-a7a1-a8dd82d6e823">语音合成音色列表</a>。<br> &emsp; "Speed": 1.25, // Integer 非必填，语速，范围：[-2，6]，分别对应不同语速： -2: 代表0.6倍 -1: 代表0.8倍 0: 代表1.0倍（默认） 1: 代表1.2倍 2: 代表1.5倍  6: 代表2.5倍  如果需要更细化的语速，可以保留小数点后 2 位，例如0.5/1.25/2.81等。 参数值与实际语速转换，可参考 <a href="https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz">语速转换</a><br> &emsp; "Volume": 5, // Integer 非必填，音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。<br> &emsp; "EmotionCategory":  "angry", // String 非必填 控制合成音频的情感，仅支持多情感音色使用。取值: neutral(中性)、sad(悲伤)、happy(高兴)、angry(生气)、fear(恐惧)、news(新闻)、story(故事)、radio(广播)、poetry(诗歌)、call(客服)、sajiao(撒娇)、disgusted(厌恶)、amaze(震惊)、peaceful(平静)、exciting(兴奋)、aojiao(傲娇)、jieshuo(解说)。<br> &emsp; "EmotionIntensity":  150 // Integer 非必填 控制合成音频情感程度，取值范围为 [50,200]，默认为 100；只有 EmotionCategory 不为空时生效。<br> &emsp; }</pre>
        :rtype: str
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig

    @property
    def AvatarConfig(self):
        r"""数字人配置，为JSON字符串。**数字人配置需要提工单加白后才能使用**
        :rtype: str
        """
        return self._AvatarConfig

    @AvatarConfig.setter
    def AvatarConfig(self, AvatarConfig):
        self._AvatarConfig = AvatarConfig

    @property
    def ExperimentalParams(self):
        r"""实验性参数,联系后台使用
        :rtype: str
        """
        return self._ExperimentalParams

    @ExperimentalParams.setter
    def ExperimentalParams(self, ExperimentalParams):
        self._ExperimentalParams = ExperimentalParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        if params.get("AgentConfig") is not None:
            self._AgentConfig = AgentConfig()
            self._AgentConfig._deserialize(params.get("AgentConfig"))
        self._SessionId = params.get("SessionId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("STTConfig") is not None:
            self._STTConfig = STTConfig()
            self._STTConfig._deserialize(params.get("STTConfig"))
        self._LLMConfig = params.get("LLMConfig")
        self._TTSConfig = params.get("TTSConfig")
        self._AvatarConfig = params.get("AvatarConfig")
        self._ExperimentalParams = params.get("ExperimentalParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAIConversationResponse(AbstractModel):
    r"""StartAIConversation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 用于唯一标识对话任务。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""用于唯一标识对话任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartAITranscriptionRequest(AbstractModel):
    r"""StartAITranscription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和开启转录任务的房间使用的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，表示开启转录任务的房间号。
        :type RoomId: str
        :param _TranscriptionParams: 转录机器人的参数。
        :type TranscriptionParams: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParams`
        :param _SessionId: 调用方传入的唯一Id，服务端用来任务去重，重复的任务会发起失败。服务端固定使用SdkAppId+RoomId+RoomIdType+RobotUserId来去重，如果传入了SessionId，也会使用SessionId去重。
注意：
TranscriptionMode为0时，需要保证一个房间内只发起一个任务，如果发起多个任务，则机器人之间会相互订阅，除非主动停止任务，否则只有10小时后任务才会超时退出，这种情况下建议填写SessionId，保证后续重复发起的任务失败。
        :type SessionId: str
        :param _RoomIdType: TRTC房间号的类型，0代表数字房间号，1代表字符串房间号。不填默认是数字房间号。
        :type RoomIdType: int
        :param _RecognizeConfig: 语音识别配置。
        :type RecognizeConfig: :class:`tencentcloud.trtc.v20190722.models.RecognizeConfig`
        :param _TranslationConfig: 翻译相关配置
        :type TranslationConfig: :class:`tencentcloud.trtc.v20190722.models.TranslationConfig`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._TranscriptionParams = None
        self._SessionId = None
        self._RoomIdType = None
        self._RecognizeConfig = None
        self._TranslationConfig = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和开启转录任务的房间使用的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，表示开启转录任务的房间号。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TranscriptionParams(self):
        r"""转录机器人的参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParams`
        """
        return self._TranscriptionParams

    @TranscriptionParams.setter
    def TranscriptionParams(self, TranscriptionParams):
        self._TranscriptionParams = TranscriptionParams

    @property
    def SessionId(self):
        r"""调用方传入的唯一Id，服务端用来任务去重，重复的任务会发起失败。服务端固定使用SdkAppId+RoomId+RoomIdType+RobotUserId来去重，如果传入了SessionId，也会使用SessionId去重。
注意：
TranscriptionMode为0时，需要保证一个房间内只发起一个任务，如果发起多个任务，则机器人之间会相互订阅，除非主动停止任务，否则只有10小时后任务才会超时退出，这种情况下建议填写SessionId，保证后续重复发起的任务失败。
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型，0代表数字房间号，1代表字符串房间号。不填默认是数字房间号。
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def RecognizeConfig(self):
        r"""语音识别配置。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RecognizeConfig`
        """
        return self._RecognizeConfig

    @RecognizeConfig.setter
    def RecognizeConfig(self, RecognizeConfig):
        self._RecognizeConfig = RecognizeConfig

    @property
    def TranslationConfig(self):
        r"""翻译相关配置
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranslationConfig`
        """
        return self._TranslationConfig

    @TranslationConfig.setter
    def TranslationConfig(self, TranslationConfig):
        self._TranslationConfig = TranslationConfig


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        if params.get("TranscriptionParams") is not None:
            self._TranscriptionParams = TranscriptionParams()
            self._TranscriptionParams._deserialize(params.get("TranscriptionParams"))
        self._SessionId = params.get("SessionId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("RecognizeConfig") is not None:
            self._RecognizeConfig = RecognizeConfig()
            self._RecognizeConfig._deserialize(params.get("RecognizeConfig"))
        if params.get("TranslationConfig") is not None:
            self._TranslationConfig = TranslationConfig()
            self._TranslationConfig._deserialize(params.get("TranslationConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAITranscriptionResponse(AbstractModel):
    r"""StartAITranscription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 用于唯一标识转录任务。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""用于唯一标识转录任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    r"""StartMCUMixTranscodeByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _StrRoomId: 字符串房间号。
        :type StrRoomId: str
        :param _OutputParams: 混流输出控制参数。
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param _EncodeParams: 混流输出编码参数。
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param _LayoutParams: 混流输出布局参数。
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        :param _PublishCdnParams: 第三方CDN转推参数。如需转推至腾讯云云直播，此参数无需填写，会默认转推
        :type PublishCdnParams: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        self._SdkAppId = None
        self._StrRoomId = None
        self._OutputParams = None
        self._EncodeParams = None
        self._LayoutParams = None
        self._PublishCdnParams = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StrRoomId(self):
        r"""字符串房间号。
        :rtype: str
        """
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId

    @property
    def OutputParams(self):
        r"""混流输出控制参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        """
        return self._OutputParams

    @OutputParams.setter
    def OutputParams(self, OutputParams):
        self._OutputParams = OutputParams

    @property
    def EncodeParams(self):
        r"""混流输出编码参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        """
        return self._EncodeParams

    @EncodeParams.setter
    def EncodeParams(self, EncodeParams):
        self._EncodeParams = EncodeParams

    @property
    def LayoutParams(self):
        r"""混流输出布局参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        """
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def PublishCdnParams(self):
        r"""第三方CDN转推参数。如需转推至腾讯云云直播，此参数无需填写，会默认转推
        :rtype: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StrRoomId = params.get("StrRoomId")
        if params.get("OutputParams") is not None:
            self._OutputParams = OutputParams()
            self._OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self._EncodeParams = EncodeParams()
            self._EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self._LayoutParams = LayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = PublishCdnParams()
            self._PublishCdnParams._deserialize(params.get("PublishCdnParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    r"""StartMCUMixTranscodeByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartMCUMixTranscodeRequest(AbstractModel):
    r"""StartMCUMixTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _RoomId: 房间号。
        :type RoomId: int
        :param _OutputParams: 混流输出控制参数。
        :type OutputParams: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        :param _EncodeParams: 混流输出编码参数。
        :type EncodeParams: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        :param _LayoutParams: 混流输出布局参数。
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        :param _PublishCdnParams: 第三方CDN转推参数。如需转推至腾讯云云直播，此参数无需填写，会默认转推
        :type PublishCdnParams: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._OutputParams = None
        self._EncodeParams = None
        self._LayoutParams = None
        self._PublishCdnParams = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间号。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def OutputParams(self):
        r"""混流输出控制参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.OutputParams`
        """
        return self._OutputParams

    @OutputParams.setter
    def OutputParams(self, OutputParams):
        self._OutputParams = OutputParams

    @property
    def EncodeParams(self):
        r"""混流输出编码参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.EncodeParams`
        """
        return self._EncodeParams

    @EncodeParams.setter
    def EncodeParams(self, EncodeParams):
        self._EncodeParams = EncodeParams

    @property
    def LayoutParams(self):
        r"""混流输出布局参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.LayoutParams`
        """
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def PublishCdnParams(self):
        r"""第三方CDN转推参数。如需转推至腾讯云云直播，此参数无需填写，会默认转推
        :rtype: :class:`tencentcloud.trtc.v20190722.models.PublishCdnParams`
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        if params.get("OutputParams") is not None:
            self._OutputParams = OutputParams()
            self._OutputParams._deserialize(params.get("OutputParams"))
        if params.get("EncodeParams") is not None:
            self._EncodeParams = EncodeParams()
            self._EncodeParams._deserialize(params.get("EncodeParams"))
        if params.get("LayoutParams") is not None:
            self._LayoutParams = LayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = PublishCdnParams()
            self._PublishCdnParams._deserialize(params.get("PublishCdnParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMCUMixTranscodeResponse(AbstractModel):
    r"""StartMCUMixTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartPublishCdnStreamRequest(AbstractModel):
    r"""StartPublishCdnStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和转推的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: 主房间信息RoomId，转推的TRTC房间所对应的RoomId。
        :type RoomId: str
        :param _RoomIdType: 主房间信息RoomType，必须和转推的房间所对应的RoomId类型相同，0为整型房间号，1为字符串房间号。
        :type RoomIdType: int
        :param _AgentParams: 转推服务加入TRTC房间的机器人参数。
        :type AgentParams: :class:`tencentcloud.trtc.v20190722.models.AgentParams`
        :param _WithTranscoding: 是否转码，0表示无需转码，1表示需要转码。是否收取转码费是由WithTranscoding参数决定的，WithTranscoding为0，表示旁路转推，不会收取转码费用，WithTranscoding为1，表示混流转推，会收取转码费用。
注：混流是必须转码，这个参数需设置为1。
        :type WithTranscoding: int
        :param _AudioParams: 转推流的音频编码参数。由于音频是必转码的（不会收取转码费用），所以启动任务的时候，必须填写。
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param _VideoParams: 转推流的视频编码参数，不填表示纯音频转推。
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param _SingleSubscribeParams: 需要单流旁路转推的用户上行参数，单流旁路转推时，WithTranscoding需要设置为0。
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param _PublishCdnParams: 转推的CDN参数，一个任务最多支持10个推流URL。和回推房间参数必须要有一个。
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _SeiParams: 混流SEI参数
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param _FeedBackRoomParams: 回推房间信息，一个任务最多支持回推10个房间，和转推CDN参数必须要有一个。注：回推房间需使用10.4及以上SDK版本，如您有需求，请联系腾讯云技术支持。
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        :param _RecordParams: 转推录制参数，[参考文档](https://cloud.tencent.com/document/product/647/111748)。
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.McuRecordParams`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._AgentParams = None
        self._WithTranscoding = None
        self._AudioParams = None
        self._VideoParams = None
        self._SingleSubscribeParams = None
        self._PublishCdnParams = None
        self._SeiParams = None
        self._FeedBackRoomParams = None
        self._RecordParams = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和转推的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""主房间信息RoomId，转推的TRTC房间所对应的RoomId。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""主房间信息RoomType，必须和转推的房间所对应的RoomId类型相同，0为整型房间号，1为字符串房间号。
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def AgentParams(self):
        r"""转推服务加入TRTC房间的机器人参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AgentParams`
        """
        return self._AgentParams

    @AgentParams.setter
    def AgentParams(self, AgentParams):
        self._AgentParams = AgentParams

    @property
    def WithTranscoding(self):
        r"""是否转码，0表示无需转码，1表示需要转码。是否收取转码费是由WithTranscoding参数决定的，WithTranscoding为0，表示旁路转推，不会收取转码费用，WithTranscoding为1，表示混流转推，会收取转码费用。
注：混流是必须转码，这个参数需设置为1。
        :rtype: int
        """
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        r"""转推流的音频编码参数。由于音频是必转码的（不会收取转码费用），所以启动任务的时候，必须填写。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        r"""转推流的视频编码参数，不填表示纯音频转推。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        r"""需要单流旁路转推的用户上行参数，单流旁路转推时，WithTranscoding需要设置为0。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        """
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        r"""转推的CDN参数，一个任务最多支持10个推流URL。和回推房间参数必须要有一个。
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        r"""混流SEI参数
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        """
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
        r"""回推房间信息，一个任务最多支持回推10个房间，和转推CDN参数必须要有一个。注：回推房间需使用10.4及以上SDK版本，如您有需求，请联系腾讯云技术支持。
        :rtype: list of McuFeedBackRoomParams
        """
        return self._FeedBackRoomParams

    @FeedBackRoomParams.setter
    def FeedBackRoomParams(self, FeedBackRoomParams):
        self._FeedBackRoomParams = FeedBackRoomParams

    @property
    def RecordParams(self):
        r"""转推录制参数，[参考文档](https://cloud.tencent.com/document/product/647/111748)。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuRecordParams`
        """
        return self._RecordParams

    @RecordParams.setter
    def RecordParams(self, RecordParams):
        self._RecordParams = RecordParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("AgentParams") is not None:
            self._AgentParams = AgentParams()
            self._AgentParams._deserialize(params.get("AgentParams"))
        self._WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self._AudioParams = McuAudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self._VideoParams = McuVideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self._SingleSubscribeParams = SingleSubscribeParams()
            self._SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self._SeiParams = McuSeiParams()
            self._SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self._FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self._FeedBackRoomParams.append(obj)
        if params.get("RecordParams") is not None:
            self._RecordParams = McuRecordParams()
            self._RecordParams._deserialize(params.get("RecordParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishCdnStreamResponse(AbstractModel):
    r"""StartPublishCdnStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 用于唯一标识转推任务，由腾讯云服务端生成，后续更新和停止请求都需要携带TaskID参数。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""用于唯一标识转推任务，由腾讯云服务端生成，后续更新和停止请求都需要携带TaskID参数。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartStreamIngestRequest(AbstractModel):
    r"""StartStreamIngest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _RoomId: TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，录制的TRTC房间所对应的RoomId。
        :type RoomId: str
        :param _RoomIdType: TRTC房间号的类型。
【*注意】必须和录制的房间所对应的RoomId类型相同:
0: 字符串类型的RoomId
1: 32位整型的RoomId（默认）
        :type RoomIdType: int
        :param _UserId: 输入在线媒体流机器人的UserId，用于进房发起拉流转推任务。
        :type UserId: str
        :param _UserSig: 输入在线媒体流机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :type UserSig: str
        :param _StreamUrl: 源流URL【必填】。如果是视频流，分辨率请保持不变。
        :type StreamUrl: str
        :param _PrivateMapKey: TRTC房间权限加密串，只有在TRTC控制台启用了高级权限控制的时候需要携带，在TRTC控制台如果开启高级权限控制后，TRTC 的后台服务系统会校验一个叫做 [PrivateMapKey] 的“权限票据”，权限票据中包含了一个加密后的 RoomId 和一个加密后的“权限位列表”。由于 PrivateMapKey 中包含 RoomId，所以只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。
        :type PrivateMapKey: str
        :param _VideoEncodeParams: 【本字段已废弃】视频编码参数。可选，如果不填，保持原始流的参数。
        :type VideoEncodeParams: :class:`tencentcloud.trtc.v20190722.models.VideoEncodeParams`
        :param _AudioEncodeParams: 【本字段已废弃】音频编码参数。可选，如果不填，保持原始流的参数。
        :type AudioEncodeParams: :class:`tencentcloud.trtc.v20190722.models.AudioEncodeParams`
        :param _SourceUrl: 【本字段已废弃，请使用 StreamUrl 字段】源流URL，支持一个地址。
        :type SourceUrl: list of str
        :param _SeekSecond: 指定视频从某个秒时间戳播放
        :type SeekSecond: int
        :param _AutoPush: 开启自动旁路推流，请确认控制台已经开启该功能。
        :type AutoPush: bool
        :param _RepeatNum: 循环播放次数, 取值范围[-1, 1000],  默认1次。
 - 0 无效值
 - -1 循环播放, 需要主动调用停止接口或设置MaxDuration

        :type RepeatNum: int
        :param _MaxDuration: 循环播放最大时长,仅支持RepeatNum设置-1时生效，取值范围[1, 10080]，单位分钟。
        :type MaxDuration: int
        :param _Volume: 音量，取值范围[0, 100]，默认100，表示原音量。
        :type Volume: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._UserId = None
        self._UserSig = None
        self._StreamUrl = None
        self._PrivateMapKey = None
        self._VideoEncodeParams = None
        self._AudioEncodeParams = None
        self._SourceUrl = None
        self._SeekSecond = None
        self._AutoPush = None
        self._RepeatNum = None
        self._MaxDuration = None
        self._Volume = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和TRTC的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""TRTC的[RoomId](https://cloud.tencent.com/document/product/647/46351#roomid)，录制的TRTC房间所对应的RoomId。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型。
【*注意】必须和录制的房间所对应的RoomId类型相同:
0: 字符串类型的RoomId
1: 32位整型的RoomId（默认）
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        r"""输入在线媒体流机器人的UserId，用于进房发起拉流转推任务。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""输入在线媒体流机器人UserId对应的校验签名，即UserId和UserSig相当于机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def StreamUrl(self):
        r"""源流URL【必填】。如果是视频流，分辨率请保持不变。
        :rtype: str
        """
        return self._StreamUrl

    @StreamUrl.setter
    def StreamUrl(self, StreamUrl):
        self._StreamUrl = StreamUrl

    @property
    def PrivateMapKey(self):
        r"""TRTC房间权限加密串，只有在TRTC控制台启用了高级权限控制的时候需要携带，在TRTC控制台如果开启高级权限控制后，TRTC 的后台服务系统会校验一个叫做 [PrivateMapKey] 的“权限票据”，权限票据中包含了一个加密后的 RoomId 和一个加密后的“权限位列表”。由于 PrivateMapKey 中包含 RoomId，所以只提供了 UserSig 没有提供 PrivateMapKey 时，并不能进入指定的房间。
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey

    @property
    def VideoEncodeParams(self):
        warnings.warn("parameter `VideoEncodeParams` is deprecated", DeprecationWarning) 

        r"""【本字段已废弃】视频编码参数。可选，如果不填，保持原始流的参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoEncodeParams`
        """
        return self._VideoEncodeParams

    @VideoEncodeParams.setter
    def VideoEncodeParams(self, VideoEncodeParams):
        warnings.warn("parameter `VideoEncodeParams` is deprecated", DeprecationWarning) 

        self._VideoEncodeParams = VideoEncodeParams

    @property
    def AudioEncodeParams(self):
        warnings.warn("parameter `AudioEncodeParams` is deprecated", DeprecationWarning) 

        r"""【本字段已废弃】音频编码参数。可选，如果不填，保持原始流的参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioEncodeParams`
        """
        return self._AudioEncodeParams

    @AudioEncodeParams.setter
    def AudioEncodeParams(self, AudioEncodeParams):
        warnings.warn("parameter `AudioEncodeParams` is deprecated", DeprecationWarning) 

        self._AudioEncodeParams = AudioEncodeParams

    @property
    def SourceUrl(self):
        warnings.warn("parameter `SourceUrl` is deprecated", DeprecationWarning) 

        r"""【本字段已废弃，请使用 StreamUrl 字段】源流URL，支持一个地址。
        :rtype: list of str
        """
        return self._SourceUrl

    @SourceUrl.setter
    def SourceUrl(self, SourceUrl):
        warnings.warn("parameter `SourceUrl` is deprecated", DeprecationWarning) 

        self._SourceUrl = SourceUrl

    @property
    def SeekSecond(self):
        r"""指定视频从某个秒时间戳播放
        :rtype: int
        """
        return self._SeekSecond

    @SeekSecond.setter
    def SeekSecond(self, SeekSecond):
        self._SeekSecond = SeekSecond

    @property
    def AutoPush(self):
        r"""开启自动旁路推流，请确认控制台已经开启该功能。
        :rtype: bool
        """
        return self._AutoPush

    @AutoPush.setter
    def AutoPush(self, AutoPush):
        self._AutoPush = AutoPush

    @property
    def RepeatNum(self):
        r"""循环播放次数, 取值范围[-1, 1000],  默认1次。
 - 0 无效值
 - -1 循环播放, 需要主动调用停止接口或设置MaxDuration

        :rtype: int
        """
        return self._RepeatNum

    @RepeatNum.setter
    def RepeatNum(self, RepeatNum):
        self._RepeatNum = RepeatNum

    @property
    def MaxDuration(self):
        r"""循环播放最大时长,仅支持RepeatNum设置-1时生效，取值范围[1, 10080]，单位分钟。
        :rtype: int
        """
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def Volume(self):
        r"""音量，取值范围[0, 100]，默认100，表示原音量。
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._StreamUrl = params.get("StreamUrl")
        self._PrivateMapKey = params.get("PrivateMapKey")
        if params.get("VideoEncodeParams") is not None:
            self._VideoEncodeParams = VideoEncodeParams()
            self._VideoEncodeParams._deserialize(params.get("VideoEncodeParams"))
        if params.get("AudioEncodeParams") is not None:
            self._AudioEncodeParams = AudioEncodeParams()
            self._AudioEncodeParams._deserialize(params.get("AudioEncodeParams"))
        self._SourceUrl = params.get("SourceUrl")
        self._SeekSecond = params.get("SeekSecond")
        self._AutoPush = params.get("AutoPush")
        self._RepeatNum = params.get("RepeatNum")
        self._MaxDuration = params.get("MaxDuration")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamIngestResponse(AbstractModel):
    r"""StartStreamIngest返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 输入在线媒体流的任务 ID。任务 ID 是对一次输入在线媒体流生命周期过程的唯一标识，结束任务时会失去意义。任务 ID 需要业务保存下来，作为下次针对这个任务操作的参数。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""输入在线媒体流的任务 ID。任务 ID 是对一次输入在线媒体流生命周期过程的唯一标识，结束任务时会失去意义。任务 ID 需要业务保存下来，作为下次针对这个任务操作的参数。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartWebRecordRequest(AbstractModel):
    r"""StartWebRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordUrl: 【必填】需要录制的网页URL
        :type RecordUrl: str
        :param _StorageParams: 【必填】云存储相关的参数，目前支持腾讯云对象存储以及腾讯云云点播VOD，不支持第三方云存储；输出文件的存储格式仅支持hls或mp4
        :type StorageParams: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        :param _SdkAppId: 【必填】TRTC的SdkAppId
        :type SdkAppId: int
        :param _MaxDurationLimit: 录制最大时长限制， 单位 s, 合法取值范围[1800, 86400], 默认 86400s(24 小时)
        :type MaxDurationLimit: int
        :param _WebRecordVideoParams: 页面录制视频参数
        :type WebRecordVideoParams: :class:`tencentcloud.trtc.v20190722.models.WebRecordVideoParams`
        :param _RecordId: 当对重复任务敏感时，请关注此值： 为了避免任务在短时间内重复发起，导致任务重复
传入录制RecordId来标识此次任务， 小于32字节，若携带RecordId发起两次以上的开始录制请求，任务只会启动一个，第二个报错FailedOperation.TaskExist。注意StartWebRecord调用失败时而非FailedOperation.TaskExist错误，请更换RecordId重新发起。
        :type RecordId: str
        :param _PublishCdnParams: 若您想要推流到CDN，可以使用PublishCdnParams.N参数设置，支持最多同时推流到10个CDN地址。若转推地址是腾讯云CDN时，请将IsTencentCdn明确设置为1
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _ReadyTimeout: 录制页面资源加载的超时时间，单位：秒。默认值为 0 秒，该值需大于等于 0秒，且小于等于 60秒。录制页面未启用页面加载超时检测时，请勿设置此参数。
        :type ReadyTimeout: int
        :param _EmulateMobileParams: 渲染移动模式参数；不准备渲染移动模式页面时，请勿设置此参数。
        :type EmulateMobileParams: :class:`tencentcloud.trtc.v20190722.models.EmulateMobileParams`
        """
        self._RecordUrl = None
        self._StorageParams = None
        self._SdkAppId = None
        self._MaxDurationLimit = None
        self._WebRecordVideoParams = None
        self._RecordId = None
        self._PublishCdnParams = None
        self._ReadyTimeout = None
        self._EmulateMobileParams = None

    @property
    def RecordUrl(self):
        r"""【必填】需要录制的网页URL
        :rtype: str
        """
        return self._RecordUrl

    @RecordUrl.setter
    def RecordUrl(self, RecordUrl):
        self._RecordUrl = RecordUrl

    @property
    def StorageParams(self):
        r"""【必填】云存储相关的参数，目前支持腾讯云对象存储以及腾讯云云点播VOD，不支持第三方云存储；输出文件的存储格式仅支持hls或mp4
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        """
        return self._StorageParams

    @StorageParams.setter
    def StorageParams(self, StorageParams):
        self._StorageParams = StorageParams

    @property
    def SdkAppId(self):
        r"""【必填】TRTC的SdkAppId
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def MaxDurationLimit(self):
        r"""录制最大时长限制， 单位 s, 合法取值范围[1800, 86400], 默认 86400s(24 小时)
        :rtype: int
        """
        return self._MaxDurationLimit

    @MaxDurationLimit.setter
    def MaxDurationLimit(self, MaxDurationLimit):
        self._MaxDurationLimit = MaxDurationLimit

    @property
    def WebRecordVideoParams(self):
        r"""页面录制视频参数
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WebRecordVideoParams`
        """
        return self._WebRecordVideoParams

    @WebRecordVideoParams.setter
    def WebRecordVideoParams(self, WebRecordVideoParams):
        self._WebRecordVideoParams = WebRecordVideoParams

    @property
    def RecordId(self):
        r"""当对重复任务敏感时，请关注此值： 为了避免任务在短时间内重复发起，导致任务重复
传入录制RecordId来标识此次任务， 小于32字节，若携带RecordId发起两次以上的开始录制请求，任务只会启动一个，第二个报错FailedOperation.TaskExist。注意StartWebRecord调用失败时而非FailedOperation.TaskExist错误，请更换RecordId重新发起。
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def PublishCdnParams(self):
        r"""若您想要推流到CDN，可以使用PublishCdnParams.N参数设置，支持最多同时推流到10个CDN地址。若转推地址是腾讯云CDN时，请将IsTencentCdn明确设置为1
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def ReadyTimeout(self):
        r"""录制页面资源加载的超时时间，单位：秒。默认值为 0 秒，该值需大于等于 0秒，且小于等于 60秒。录制页面未启用页面加载超时检测时，请勿设置此参数。
        :rtype: int
        """
        return self._ReadyTimeout

    @ReadyTimeout.setter
    def ReadyTimeout(self, ReadyTimeout):
        self._ReadyTimeout = ReadyTimeout

    @property
    def EmulateMobileParams(self):
        r"""渲染移动模式参数；不准备渲染移动模式页面时，请勿设置此参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.EmulateMobileParams`
        """
        return self._EmulateMobileParams

    @EmulateMobileParams.setter
    def EmulateMobileParams(self, EmulateMobileParams):
        self._EmulateMobileParams = EmulateMobileParams


    def _deserialize(self, params):
        self._RecordUrl = params.get("RecordUrl")
        if params.get("StorageParams") is not None:
            self._StorageParams = StorageParams()
            self._StorageParams._deserialize(params.get("StorageParams"))
        self._SdkAppId = params.get("SdkAppId")
        self._MaxDurationLimit = params.get("MaxDurationLimit")
        if params.get("WebRecordVideoParams") is not None:
            self._WebRecordVideoParams = WebRecordVideoParams()
            self._WebRecordVideoParams._deserialize(params.get("WebRecordVideoParams"))
        self._RecordId = params.get("RecordId")
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        self._ReadyTimeout = params.get("ReadyTimeout")
        if params.get("EmulateMobileParams") is not None:
            self._EmulateMobileParams = EmulateMobileParams()
            self._EmulateMobileParams._deserialize(params.get("EmulateMobileParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartWebRecordResponse(AbstractModel):
    r"""StartWebRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 录制任务的唯一Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""录制任务的唯一Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopAIConversationRequest(AbstractModel):
    r"""StopAIConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 唯一标识任务。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""唯一标识任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAIConversationResponse(AbstractModel):
    r"""StopAIConversation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopAITranscriptionRequest(AbstractModel):
    r"""StopAITranscription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 唯一标识转录任务。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""唯一标识转录任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAITranscriptionResponse(AbstractModel):
    r"""StopAITranscription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopMCUMixTranscodeByStrRoomIdRequest(AbstractModel):
    r"""StopMCUMixTranscodeByStrRoomId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _StrRoomId: 字符串房间号。
        :type StrRoomId: str
        """
        self._SdkAppId = None
        self._StrRoomId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StrRoomId(self):
        r"""字符串房间号。
        :rtype: str
        """
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StrRoomId = params.get("StrRoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMCUMixTranscodeByStrRoomIdResponse(AbstractModel):
    r"""StopMCUMixTranscodeByStrRoomId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopMCUMixTranscodeRequest(AbstractModel):
    r"""StopMCUMixTranscode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param _RoomId: 房间号。
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        r"""房间号。
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMCUMixTranscodeResponse(AbstractModel):
    r"""StopMCUMixTranscode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopPublishCdnStreamRequest(AbstractModel):
    r"""StopPublishCdnStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和转推的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _TaskId: 唯一标识转推任务。
        :type TaskId: str
        :param _RecordKey: 录制任务 key，标识一个录制任务，对应转推任务发起时指定 RecordKey；
如果填写该参数，表示调用者希望立即结束该录制任务。当RecordKey 指定的录制任务正在录制当前转推任务时，录制任务立即结束，否则录制任务不受影响。
如果没有填写该参数，但是转推任务发起时填写了 RecordKey，则表示在续录等待时间结束后才结束录制任务，续录等待期间可以使用相同的 RecordKey 发起新的转推任务，和当前转推任务录制到同一文件。
        :type RecordKey: str
        """
        self._SdkAppId = None
        self._TaskId = None
        self._RecordKey = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和转推的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""唯一标识转推任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RecordKey(self):
        r"""录制任务 key，标识一个录制任务，对应转推任务发起时指定 RecordKey；
如果填写该参数，表示调用者希望立即结束该录制任务。当RecordKey 指定的录制任务正在录制当前转推任务时，录制任务立即结束，否则录制任务不受影响。
如果没有填写该参数，但是转推任务发起时填写了 RecordKey，则表示在续录等待时间结束后才结束录制任务，续录等待期间可以使用相同的 RecordKey 发起新的转推任务，和当前转推任务录制到同一文件。
        :rtype: str
        """
        return self._RecordKey

    @RecordKey.setter
    def RecordKey(self, RecordKey):
        self._RecordKey = RecordKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._RecordKey = params.get("RecordKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishCdnStreamResponse(AbstractModel):
    r"""StopPublishCdnStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 转推任务唯一的String Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""转推任务唯一的String Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopStreamIngestRequest(AbstractModel):
    r"""StopStreamIngest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和任务的房间所对应的SDKAppId相同。
        :type SdkAppId: int
        :param _TaskId: 任务的唯一Id，在启动任务成功后会返回。
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和任务的房间所对应的SDKAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""任务的唯一Id，在启动任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamIngestResponse(AbstractModel):
    r"""StopStreamIngest返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopWebRecordRequest(AbstractModel):
    r"""StopWebRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 需要停止的任务Id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""需要停止的任务Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWebRecordResponse(AbstractModel):
    r"""StopWebRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StorageFile(AbstractModel):
    r"""云端录制查询接口，录制文件的信息

    """

    def __init__(self):
        r"""
        :param _UserId: 录制文件对应的UserId，如果是混流的话的这里返回的是空串。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _FileName: 录制索引文件名。
        :type FileName: str
        :param _TrackType: 录制文件流信息。
video：视频录制文件
audio：音频录制文件
audio_video：音视频录制文件
注意：此字段可能返回 null，表示取不到有效值。
        :type TrackType: str
        :param _BeginTimeStamp: 录制文件开始Unix时间戳。
        :type BeginTimeStamp: int
        """
        self._UserId = None
        self._FileName = None
        self._TrackType = None
        self._BeginTimeStamp = None

    @property
    def UserId(self):
        r"""录制文件对应的UserId，如果是混流的话的这里返回的是空串。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def FileName(self):
        r"""录制索引文件名。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def TrackType(self):
        r"""录制文件流信息。
video：视频录制文件
audio：音频录制文件
audio_video：音视频录制文件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TrackType

    @TrackType.setter
    def TrackType(self, TrackType):
        self._TrackType = TrackType

    @property
    def BeginTimeStamp(self):
        r"""录制文件开始Unix时间戳。
        :rtype: int
        """
        return self._BeginTimeStamp

    @BeginTimeStamp.setter
    def BeginTimeStamp(self, BeginTimeStamp):
        self._BeginTimeStamp = BeginTimeStamp


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._FileName = params.get("FileName")
        self._TrackType = params.get("TrackType")
        self._BeginTimeStamp = params.get("BeginTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageParams(AbstractModel):
    r"""录制存储参数

    """

    def __init__(self):
        r"""
        :param _CloudStorage: 腾讯云对象存储COS以及第三方云存储的账号信息
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param _CloudVod: 腾讯云云点播Vod的存储信息
        :type CloudVod: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        self._CloudStorage = None
        self._CloudVod = None

    @property
    def CloudStorage(self):
        r"""腾讯云对象存储COS以及第三方云存储的账号信息
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        """
        return self._CloudStorage

    @CloudStorage.setter
    def CloudStorage(self, CloudStorage):
        self._CloudStorage = CloudStorage

    @property
    def CloudVod(self):
        r"""腾讯云云点播Vod的存储信息
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        return self._CloudVod

    @CloudVod.setter
    def CloudVod(self, CloudVod):
        self._CloudVod = CloudVod


    def _deserialize(self, params):
        if params.get("CloudStorage") is not None:
            self._CloudStorage = CloudStorage()
            self._CloudStorage._deserialize(params.get("CloudStorage"))
        if params.get("CloudVod") is not None:
            self._CloudVod = CloudVod()
            self._CloudVod._deserialize(params.get("CloudVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeModerationUserIds(AbstractModel):
    r"""指定订阅流白名单或者黑名单，音频的白名单和音频黑名单不能同时设置，视频亦然。同时实际并发订阅的媒体流路数最大支持25路流，混流场景下视频的多画面最大支持24画面。支持通过设置".*$"通配符，来前缀匹配黑白名单的UserId，注意房间里不能有和通配符规则相同的用户，否则将视为订阅具体用户，前缀规则会失效。

    """

    def __init__(self):
        r"""
        :param _SubscribeAudioUserIds: 订阅音频流白名单，指定订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表订阅UserId 1，2，3的音频流；["1.*$"], 代表订阅UserId前缀为1的音频流。默认不填订阅房间内所有的音频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscribeAudioUserIds: list of str
        :param _UnSubscribeAudioUserIds: 订阅音频流黑名单，指定不订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表不订阅UserId 1，2，3的音频流；["1.*$"], 代表不订阅UserId前缀为1的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnSubscribeAudioUserIds: list of str
        :param _SubscribeVideoUserIds: 订阅视频流白名单，指定订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表订阅UserId  1，2，3的视频流；["1.*$"], 代表订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscribeVideoUserIds: list of str
        :param _UnSubscribeVideoUserIds: 订阅视频流黑名单，指定不订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表不订阅UserId  1，2，3的视频流；["1.*$"], 代表不订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnSubscribeVideoUserIds: list of str
        """
        self._SubscribeAudioUserIds = None
        self._UnSubscribeAudioUserIds = None
        self._SubscribeVideoUserIds = None
        self._UnSubscribeVideoUserIds = None

    @property
    def SubscribeAudioUserIds(self):
        r"""订阅音频流白名单，指定订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表订阅UserId 1，2，3的音频流；["1.*$"], 代表订阅UserId前缀为1的音频流。默认不填订阅房间内所有的音频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SubscribeAudioUserIds

    @SubscribeAudioUserIds.setter
    def SubscribeAudioUserIds(self, SubscribeAudioUserIds):
        self._SubscribeAudioUserIds = SubscribeAudioUserIds

    @property
    def UnSubscribeAudioUserIds(self):
        r"""订阅音频流黑名单，指定不订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表不订阅UserId 1，2，3的音频流；["1.*$"], 代表不订阅UserId前缀为1的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._UnSubscribeAudioUserIds

    @UnSubscribeAudioUserIds.setter
    def UnSubscribeAudioUserIds(self, UnSubscribeAudioUserIds):
        self._UnSubscribeAudioUserIds = UnSubscribeAudioUserIds

    @property
    def SubscribeVideoUserIds(self):
        r"""订阅视频流白名单，指定订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表订阅UserId  1，2，3的视频流；["1.*$"], 代表订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SubscribeVideoUserIds

    @SubscribeVideoUserIds.setter
    def SubscribeVideoUserIds(self, SubscribeVideoUserIds):
        self._SubscribeVideoUserIds = SubscribeVideoUserIds

    @property
    def UnSubscribeVideoUserIds(self):
        r"""订阅视频流黑名单，指定不订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表不订阅UserId  1，2，3的视频流；["1.*$"], 代表不订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._UnSubscribeVideoUserIds

    @UnSubscribeVideoUserIds.setter
    def UnSubscribeVideoUserIds(self, UnSubscribeVideoUserIds):
        self._UnSubscribeVideoUserIds = UnSubscribeVideoUserIds


    def _deserialize(self, params):
        self._SubscribeAudioUserIds = params.get("SubscribeAudioUserIds")
        self._UnSubscribeAudioUserIds = params.get("UnSubscribeAudioUserIds")
        self._SubscribeVideoUserIds = params.get("SubscribeVideoUserIds")
        self._UnSubscribeVideoUserIds = params.get("UnSubscribeVideoUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeStreamUserIds(AbstractModel):
    r"""指定订阅流白名单或者黑名单，音频的白名单和音频黑名单不能同时设置，视频亦然。同时实际并发订阅的媒体流路数最大支持25路流，混流场景下视频的多画面最大支持24画面。支持通过设置".*$"通配符，来前缀匹配黑白名单的UserId，注意房间里不能有和通配符规则相同的用户，否则将视为订阅具体用户，前缀规则会失效。

    """

    def __init__(self):
        r"""
        :param _SubscribeAudioUserIds: 订阅音频流白名单，指定订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表订阅UserId 1，2，3的音频流；["1.*$"], 代表订阅UserId前缀为1的音频流。默认不填订阅房间内所有的音频流，订阅列表用户数不超过32。
        :type SubscribeAudioUserIds: list of str
        :param _UnSubscribeAudioUserIds: 订阅音频流黑名单，指定不订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表不订阅UserId 1，2，3的音频流；["1.*$"], 代表不订阅UserId前缀为1的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过32。
        :type UnSubscribeAudioUserIds: list of str
        :param _SubscribeVideoUserIds: 订阅视频流白名单，指定订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表订阅UserId  1，2，3的视频流；["1.*$"], 代表订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
        :type SubscribeVideoUserIds: list of str
        :param _UnSubscribeVideoUserIds: 订阅视频流黑名单，指定不订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表不订阅UserId  1，2，3的视频流；["1.*$"], 代表不订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
        :type UnSubscribeVideoUserIds: list of str
        """
        self._SubscribeAudioUserIds = None
        self._UnSubscribeAudioUserIds = None
        self._SubscribeVideoUserIds = None
        self._UnSubscribeVideoUserIds = None

    @property
    def SubscribeAudioUserIds(self):
        r"""订阅音频流白名单，指定订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表订阅UserId 1，2，3的音频流；["1.*$"], 代表订阅UserId前缀为1的音频流。默认不填订阅房间内所有的音频流，订阅列表用户数不超过32。
        :rtype: list of str
        """
        return self._SubscribeAudioUserIds

    @SubscribeAudioUserIds.setter
    def SubscribeAudioUserIds(self, SubscribeAudioUserIds):
        self._SubscribeAudioUserIds = SubscribeAudioUserIds

    @property
    def UnSubscribeAudioUserIds(self):
        r"""订阅音频流黑名单，指定不订阅哪几个UserId的音频流，例如["1", "2", "3"], 代表不订阅UserId 1，2，3的音频流；["1.*$"], 代表不订阅UserId前缀为1的音频流。默认不填订阅房间内所有音频流，订阅列表用户数不超过32。
        :rtype: list of str
        """
        return self._UnSubscribeAudioUserIds

    @UnSubscribeAudioUserIds.setter
    def UnSubscribeAudioUserIds(self, UnSubscribeAudioUserIds):
        self._UnSubscribeAudioUserIds = UnSubscribeAudioUserIds

    @property
    def SubscribeVideoUserIds(self):
        r"""订阅视频流白名单，指定订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表订阅UserId  1，2，3的视频流；["1.*$"], 代表订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
        :rtype: list of str
        """
        return self._SubscribeVideoUserIds

    @SubscribeVideoUserIds.setter
    def SubscribeVideoUserIds(self, SubscribeVideoUserIds):
        self._SubscribeVideoUserIds = SubscribeVideoUserIds

    @property
    def UnSubscribeVideoUserIds(self):
        r"""订阅视频流黑名单，指定不订阅哪几个UserId的视频流，例如["1", "2", "3"], 代表不订阅UserId  1，2，3的视频流；["1.*$"], 代表不订阅UserId前缀为1的视频流。默认不填订阅房间内所有视频流，订阅列表用户数不超过32。
        :rtype: list of str
        """
        return self._UnSubscribeVideoUserIds

    @UnSubscribeVideoUserIds.setter
    def UnSubscribeVideoUserIds(self, UnSubscribeVideoUserIds):
        self._UnSubscribeVideoUserIds = UnSubscribeVideoUserIds


    def _deserialize(self, params):
        self._SubscribeAudioUserIds = params.get("SubscribeAudioUserIds")
        self._UnSubscribeAudioUserIds = params.get("UnSubscribeAudioUserIds")
        self._SubscribeVideoUserIds = params.get("SubscribeVideoUserIds")
        self._UnSubscribeVideoUserIds = params.get("UnSubscribeVideoUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TRTCDataResp(AbstractModel):
    r"""TRTC数据大盘/实时监控 API接口数据出参

    """

    def __init__(self):
        r"""
        :param _StatementID: StatementID值，监控仪表盘下固定为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatementID: int
        :param _Series: 查询结果数据，以Columns-Values形式返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type Series: list of SeriesInfo
        :param _Total: Total值，监控仪表盘功能下固定为1。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._StatementID = None
        self._Series = None
        self._Total = None

    @property
    def StatementID(self):
        r"""StatementID值，监控仪表盘下固定为0。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StatementID

    @StatementID.setter
    def StatementID(self, StatementID):
        self._StatementID = StatementID

    @property
    def Series(self):
        r"""查询结果数据，以Columns-Values形式返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SeriesInfo
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Total(self):
        r"""Total值，监控仪表盘功能下固定为1。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._StatementID = params.get("StatementID")
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = SeriesInfo()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TRTCDataResult(AbstractModel):
    r"""TRTC数据大盘/实时监控 API接口数据出参

    """

    def __init__(self):
        r"""
        :param _StatementID: StatementID值，监控仪表盘下固定为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatementID: int
        :param _Series: 查询结果数据，以Columns-Values形式返回。	
注意：此字段可能返回 null，表示取不到有效值。
        :type Series: list of SeriesInfos
        :param _Total: Total值，监控仪表盘功能下固定为1。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._StatementID = None
        self._Series = None
        self._Total = None

    @property
    def StatementID(self):
        r"""StatementID值，监控仪表盘下固定为0。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StatementID

    @StatementID.setter
    def StatementID(self, StatementID):
        self._StatementID = StatementID

    @property
    def Series(self):
        r"""查询结果数据，以Columns-Values形式返回。	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SeriesInfos
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Total(self):
        r"""Total值，监控仪表盘功能下固定为1。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._StatementID = params.get("StatementID")
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = SeriesInfos()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TTSConfig(AbstractModel):
    r"""TTS相关配置

    """

    def __init__(self):
        r"""
        :param _VoiceId: 音色ID
        :type VoiceId: str
        :param _Model: TTS 的模型，默认是：flow_01_turbo, 可选: [ flow_01_turbo, flow_01_ex]
        :type Model: str
        :param _Speed: 语速，范围 0.5-2.0，默认 1.0
        :type Speed: float
        :param _Volume: (0, 10] 默认值1.0
        :type Volume: float
        """
        self._VoiceId = None
        self._Model = None
        self._Speed = None
        self._Volume = None

    @property
    def VoiceId(self):
        r"""音色ID
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def Model(self):
        r"""TTS 的模型，默认是：flow_01_turbo, 可选: [ flow_01_turbo, flow_01_ex]
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Speed(self):
        r"""语速，范围 0.5-2.0，默认 1.0
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def Volume(self):
        r"""(0, 10] 默认值1.0
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._VoiceId = params.get("VoiceId")
        self._Model = params.get("Model")
        self._Speed = params.get("Speed")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TencentVod(AbstractModel):
    r"""腾讯云点播相关参数。

    """

    def __init__(self):
        r"""
        :param _Procedure: 媒体后续任务处理操作，即完成媒体上传后，可自动发起任务流操作。参数值为任务流模板名，云点播支持 创建任务流模板 并为模板命名。
        :type Procedure: str
        :param _ExpireTime: 媒体文件过期时间，为当前时间的绝对过期时间；保存一天，就填"86400"，永久保存就填"0"，默认永久保存。
        :type ExpireTime: int
        :param _StorageRegion: 指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :type StorageRegion: str
        :param _ClassId: 分类ID，用于对媒体进行分类管理，可通过 创建分类 接口，创建分类，获得分类 ID。
默认值：0，表示其他分类。
        :type ClassId: int
        :param _SubAppId: 点播 子应用 ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :type SubAppId: int
        :param _SessionContext: 任务流上下文，任务完成回调时透传。
        :type SessionContext: str
        :param _SourceContext: 上传上下文，上传完成回调时透传。
        :type SourceContext: str
        :param _MediaType: 上传到vod平台的录制文件格式类型，0：mp4(默认), 1: hls, 2:aac(StreamType=1纯音频录制时有效),
3: hls+mp4, 4: hls+aac(StreamType=1纯音频录制时有效)。
        :type MediaType: int
        :param _UserDefineRecordId: 仅支持API录制上传vod，该参数表示用户可以自定义录制文件名前缀，【限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符】。前缀与自动生成的录制文件名之间用`__UserDefine_u_` 分开。
        :type UserDefineRecordId: str
        """
        self._Procedure = None
        self._ExpireTime = None
        self._StorageRegion = None
        self._ClassId = None
        self._SubAppId = None
        self._SessionContext = None
        self._SourceContext = None
        self._MediaType = None
        self._UserDefineRecordId = None

    @property
    def Procedure(self):
        r"""媒体后续任务处理操作，即完成媒体上传后，可自动发起任务流操作。参数值为任务流模板名，云点播支持 创建任务流模板 并为模板命名。
        :rtype: str
        """
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def ExpireTime(self):
        r"""媒体文件过期时间，为当前时间的绝对过期时间；保存一天，就填"86400"，永久保存就填"0"，默认永久保存。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def StorageRegion(self):
        r"""指定上传园区，仅适用于对上传地域有特殊需求的用户。
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def ClassId(self):
        r"""分类ID，用于对媒体进行分类管理，可通过 创建分类 接口，创建分类，获得分类 ID。
默认值：0，表示其他分类。
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def SubAppId(self):
        r"""点播 子应用 ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def SessionContext(self):
        r"""任务流上下文，任务完成回调时透传。
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SourceContext(self):
        r"""上传上下文，上传完成回调时透传。
        :rtype: str
        """
        return self._SourceContext

    @SourceContext.setter
    def SourceContext(self, SourceContext):
        self._SourceContext = SourceContext

    @property
    def MediaType(self):
        r"""上传到vod平台的录制文件格式类型，0：mp4(默认), 1: hls, 2:aac(StreamType=1纯音频录制时有效),
3: hls+mp4, 4: hls+aac(StreamType=1纯音频录制时有效)。
        :rtype: int
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def UserDefineRecordId(self):
        r"""仅支持API录制上传vod，该参数表示用户可以自定义录制文件名前缀，【限制长度为64字节，只允许包含大小写英文字母（a-zA-Z）、数字（0-9）及下划线和连词符】。前缀与自动生成的录制文件名之间用`__UserDefine_u_` 分开。
        :rtype: str
        """
        return self._UserDefineRecordId

    @UserDefineRecordId.setter
    def UserDefineRecordId(self, UserDefineRecordId):
        self._UserDefineRecordId = UserDefineRecordId


    def _deserialize(self, params):
        self._Procedure = params.get("Procedure")
        self._ExpireTime = params.get("ExpireTime")
        self._StorageRegion = params.get("StorageRegion")
        self._ClassId = params.get("ClassId")
        self._SubAppId = params.get("SubAppId")
        self._SessionContext = params.get("SessionContext")
        self._SourceContext = params.get("SourceContext")
        self._MediaType = params.get("MediaType")
        self._UserDefineRecordId = params.get("UserDefineRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Terminology(AbstractModel):
    r"""翻译术语

    """

    def __init__(self):
        r"""
        :param _Source: 源术语
        :type Source: str
        :param _Target: 目标术语翻译结果
        :type Target: str
        """
        self._Source = None
        self._Target = None

    @property
    def Source(self):
        r"""源术语
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标术语翻译结果
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToSpeechRequest(AbstractModel):
    r"""TextToSpeech请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 需要转语音的文字内容，长度范围：[1, 255]
        :type Text: str
        :param _Voice: 文本转语音的声音配置
        :type Voice: :class:`tencentcloud.trtc.v20190722.models.Voice`
        :param _SdkAppId: TRTC的SdkAppId
        :type SdkAppId: int
        :param _AudioFormat: 文本转语音的输出音频的格式
        :type AudioFormat: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        :param _APIKey: TTS的API密钥
        :type APIKey: str
        :param _Model: TTS的模型：flow_01_turbo，flow_01_ex
        :type Model: str
        :param _Language: 语言参数，默认为空， 参考： (ISO 639-1) 
        :type Language: str
        """
        self._Text = None
        self._Voice = None
        self._SdkAppId = None
        self._AudioFormat = None
        self._APIKey = None
        self._Model = None
        self._Language = None

    @property
    def Text(self):
        r"""需要转语音的文字内容，长度范围：[1, 255]
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Voice(self):
        r"""文本转语音的声音配置
        :rtype: :class:`tencentcloud.trtc.v20190722.models.Voice`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudioFormat(self):
        r"""文本转语音的输出音频的格式
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def APIKey(self):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        r"""TTS的API密钥
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        warnings.warn("parameter `APIKey` is deprecated", DeprecationWarning) 

        self._APIKey = APIKey

    @property
    def Model(self):
        r"""TTS的模型：flow_01_turbo，flow_01_ex
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Language(self):
        r"""语言参数，默认为空， 参考： (ISO 639-1) 
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._Text = params.get("Text")
        if params.get("Voice") is not None:
            self._Voice = Voice()
            self._Voice._deserialize(params.get("Voice"))
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AudioFormat") is not None:
            self._AudioFormat = AudioFormat()
            self._AudioFormat._deserialize(params.get("AudioFormat"))
        self._APIKey = params.get("APIKey")
        self._Model = params.get("Model")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToSpeechResponse(AbstractModel):
    r"""TextToSpeech返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Audio: Base64编码的音频数据
        :type Audio: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Audio = None
        self._RequestId = None

    @property
    def Audio(self):
        r"""Base64编码的音频数据
        :rtype: str
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Audio = params.get("Audio")
        self._RequestId = params.get("RequestId")


class TextToSpeechSSERequest(AbstractModel):
    r"""TextToSpeechSSE请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 需要转语音的文字内容，长度范围：[1, 255]
        :type Text: str
        :param _Voice: 文本转语音的声音配置
        :type Voice: :class:`tencentcloud.trtc.v20190722.models.Voice`
        :param _SdkAppId: TRTC的SdkAppId
        :type SdkAppId: int
        :param _AudioFormat: 文本转语音的输出音频的格式
        :type AudioFormat: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        :param _APIKey: TTS的API密钥
        :type APIKey: str
        :param _Model: TTS的模型：flow_01_turbo，flow_01_ex
        :type Model: str
        :param _Language: 语言参数，默认为空， 参考： (ISO 639-1) 
        :type Language: str
        """
        self._Text = None
        self._Voice = None
        self._SdkAppId = None
        self._AudioFormat = None
        self._APIKey = None
        self._Model = None
        self._Language = None

    @property
    def Text(self):
        r"""需要转语音的文字内容，长度范围：[1, 255]
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Voice(self):
        r"""文本转语音的声音配置
        :rtype: :class:`tencentcloud.trtc.v20190722.models.Voice`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def AudioFormat(self):
        r"""文本转语音的输出音频的格式
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioFormat`
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def APIKey(self):
        r"""TTS的API密钥
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        self._APIKey = APIKey

    @property
    def Model(self):
        r"""TTS的模型：flow_01_turbo，flow_01_ex
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Language(self):
        r"""语言参数，默认为空， 参考： (ISO 639-1) 
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._Text = params.get("Text")
        if params.get("Voice") is not None:
            self._Voice = Voice()
            self._Voice._deserialize(params.get("Voice"))
        self._SdkAppId = params.get("SdkAppId")
        if params.get("AudioFormat") is not None:
            self._AudioFormat = AudioFormat()
            self._AudioFormat._deserialize(params.get("AudioFormat"))
        self._APIKey = params.get("APIKey")
        self._Model = params.get("Model")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToSpeechSSEResponse(AbstractModel):
    r"""TextToSpeechSSE返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TimeValue(AbstractModel):
    r"""返回的质量数据，时间:值

    """

    def __init__(self):
        r"""
        :param _Time: 时间，unix时间戳（1590065877s)
        :type Time: int
        :param _Value: 当前时间返回参数取值，如（bigvCapFps在1590065877取值为0，则Value：0 ）
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        r"""时间，unix时间戳（1590065877s)
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        r"""当前时间返回参数取值，如（bigvCapFps在1590065877取值为0，则Value：0 ）
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscriptionParams(AbstractModel):
    r"""AI转录参数

    """

    def __init__(self):
        r"""
        :param _UserId: 转录机器人的UserId，用于进房发起转录任务。【注意】这个UserId不能与当前房间内的主播观众[UserId](https://cloud.tencent.com/document/product/647/46351#userid)重复。如果一个房间发起多个转录任务时，机器人的userid也不能相互重复，否则会中断前一个任务。需要保证转录机器人UserId在房间内唯一。
        :type UserId: str
        :param _UserSig: 转录机器人UserId对应的校验签名，即UserId和UserSig相当于转录机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :type UserSig: str
        :param _IMAdminUserId: IM[管理员账户](
https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)，如果填写，后台下发消息会使用IM通道，而不是TRTC自定义消息。
        :type IMAdminUserId: str
        :param _IMAdminUserSig: IM管理员账户生成的签名，用于向特定群组发送消息。如果填写，后台下发消息会使用IM通道，而不是TRTC自定义消息。必须和IM管理员的UserId一起填写。
        :type IMAdminUserSig: str
        :param _MaxIdleTime: 房间内推流用户全部退出后超过MaxIdleTime秒，后台自动关闭转录任务，默认值是60s。
        :type MaxIdleTime: int
        :param _TranscriptionMode: 1表示机器人只订阅单个人的流，0表示机器人订阅整个房间的流，如果不填默认订阅整个房间的流。
        :type TranscriptionMode: int
        :param _TargetUserId: TranscriptionMode为1时必填，机器人只会拉该userid的流，忽略房间里其他用户。
        :type TargetUserId: str
        :param _TargetUserIdList: 机器人订阅的用户列表
仅 TranscriptionMode 为 1或者 TranscriptionMode 为无限上麦模式支持传入多个用户列表
        :type TargetUserIdList: list of str
        :param _VoicePrint: 声纹配置
        :type VoicePrint: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        :param _TurnDetection: 语义断句检测
        :type TurnDetection: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        """
        self._UserId = None
        self._UserSig = None
        self._IMAdminUserId = None
        self._IMAdminUserSig = None
        self._MaxIdleTime = None
        self._TranscriptionMode = None
        self._TargetUserId = None
        self._TargetUserIdList = None
        self._VoicePrint = None
        self._TurnDetection = None

    @property
    def UserId(self):
        r"""转录机器人的UserId，用于进房发起转录任务。【注意】这个UserId不能与当前房间内的主播观众[UserId](https://cloud.tencent.com/document/product/647/46351#userid)重复。如果一个房间发起多个转录任务时，机器人的userid也不能相互重复，否则会中断前一个任务。需要保证转录机器人UserId在房间内唯一。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        r"""转录机器人UserId对应的校验签名，即UserId和UserSig相当于转录机器人进房的登录密码，具体计算方法请参考TRTC计算[UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig)的方案。
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def IMAdminUserId(self):
        warnings.warn("parameter `IMAdminUserId` is deprecated", DeprecationWarning) 

        r"""IM[管理员账户](
https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)，如果填写，后台下发消息会使用IM通道，而不是TRTC自定义消息。
        :rtype: str
        """
        return self._IMAdminUserId

    @IMAdminUserId.setter
    def IMAdminUserId(self, IMAdminUserId):
        warnings.warn("parameter `IMAdminUserId` is deprecated", DeprecationWarning) 

        self._IMAdminUserId = IMAdminUserId

    @property
    def IMAdminUserSig(self):
        warnings.warn("parameter `IMAdminUserSig` is deprecated", DeprecationWarning) 

        r"""IM管理员账户生成的签名，用于向特定群组发送消息。如果填写，后台下发消息会使用IM通道，而不是TRTC自定义消息。必须和IM管理员的UserId一起填写。
        :rtype: str
        """
        return self._IMAdminUserSig

    @IMAdminUserSig.setter
    def IMAdminUserSig(self, IMAdminUserSig):
        warnings.warn("parameter `IMAdminUserSig` is deprecated", DeprecationWarning) 

        self._IMAdminUserSig = IMAdminUserSig

    @property
    def MaxIdleTime(self):
        r"""房间内推流用户全部退出后超过MaxIdleTime秒，后台自动关闭转录任务，默认值是60s。
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def TranscriptionMode(self):
        r"""1表示机器人只订阅单个人的流，0表示机器人订阅整个房间的流，如果不填默认订阅整个房间的流。
        :rtype: int
        """
        return self._TranscriptionMode

    @TranscriptionMode.setter
    def TranscriptionMode(self, TranscriptionMode):
        self._TranscriptionMode = TranscriptionMode

    @property
    def TargetUserId(self):
        r"""TranscriptionMode为1时必填，机器人只会拉该userid的流，忽略房间里其他用户。
        :rtype: str
        """
        return self._TargetUserId

    @TargetUserId.setter
    def TargetUserId(self, TargetUserId):
        self._TargetUserId = TargetUserId

    @property
    def TargetUserIdList(self):
        r"""机器人订阅的用户列表
仅 TranscriptionMode 为 1或者 TranscriptionMode 为无限上麦模式支持传入多个用户列表
        :rtype: list of str
        """
        return self._TargetUserIdList

    @TargetUserIdList.setter
    def TargetUserIdList(self, TargetUserIdList):
        self._TargetUserIdList = TargetUserIdList

    @property
    def VoicePrint(self):
        r"""声纹配置
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VoicePrint`
        """
        return self._VoicePrint

    @VoicePrint.setter
    def VoicePrint(self, VoicePrint):
        self._VoicePrint = VoicePrint

    @property
    def TurnDetection(self):
        r"""语义断句检测
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TurnDetection`
        """
        return self._TurnDetection

    @TurnDetection.setter
    def TurnDetection(self, TurnDetection):
        self._TurnDetection = TurnDetection


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._IMAdminUserId = params.get("IMAdminUserId")
        self._IMAdminUserSig = params.get("IMAdminUserSig")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._TranscriptionMode = params.get("TranscriptionMode")
        self._TargetUserId = params.get("TargetUserId")
        self._TargetUserIdList = params.get("TargetUserIdList")
        if params.get("VoicePrint") is not None:
            self._VoicePrint = VoicePrint()
            self._VoicePrint._deserialize(params.get("VoicePrint"))
        if params.get("TurnDetection") is not None:
            self._TurnDetection = TurnDetection()
            self._TurnDetection._deserialize(params.get("TurnDetection"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationConfig(AbstractModel):
    r"""翻译相关配置

    """

    def __init__(self):
        r"""
        :param _TargetLanguages: 翻译的目标语言，目标语种列表（ISO 639-1）

        :type TargetLanguages: list of str
        :param _Mode:  1： 仅文字翻译，  2： 语音同传

        :type Mode: int
        :param _TTSConfig: 语音同传配置，开启同传时，需要传递
        :type TTSConfig: :class:`tencentcloud.trtc.v20190722.models.TTSConfig`
        :param _Terminology: 翻译术语集合
        :type Terminology: list of Terminology
        """
        self._TargetLanguages = None
        self._Mode = None
        self._TTSConfig = None
        self._Terminology = None

    @property
    def TargetLanguages(self):
        r"""翻译的目标语言，目标语种列表（ISO 639-1）

        :rtype: list of str
        """
        return self._TargetLanguages

    @TargetLanguages.setter
    def TargetLanguages(self, TargetLanguages):
        self._TargetLanguages = TargetLanguages

    @property
    def Mode(self):
        r""" 1： 仅文字翻译，  2： 语音同传

        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def TTSConfig(self):
        r"""语音同传配置，开启同传时，需要传递
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TTSConfig`
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig

    @property
    def Terminology(self):
        r"""翻译术语集合
        :rtype: list of Terminology
        """
        return self._Terminology

    @Terminology.setter
    def Terminology(self, Terminology):
        self._Terminology = Terminology


    def _deserialize(self, params):
        self._TargetLanguages = params.get("TargetLanguages")
        self._Mode = params.get("Mode")
        if params.get("TTSConfig") is not None:
            self._TTSConfig = TTSConfig()
            self._TTSConfig._deserialize(params.get("TTSConfig"))
        if params.get("Terminology") is not None:
            self._Terminology = []
            for item in params.get("Terminology"):
                obj = Terminology()
                obj._deserialize(item)
                self._Terminology.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrtcUsage(AbstractModel):
    r"""实时音视频用量在某一时间段的统计信息。

    """

    def __init__(self):
        r"""
        :param _TimeKey: 时间点，格式为YYYY-MM-DD HH:mm:ss。多天查询时，HH:mm:ss为00:00:00。
        :type TimeKey: str
        :param _TimeStampKey: 时间点时间戳
        :type TimeStampKey: int
        :param _UsageValue: 用量数组。每个数值含义与UsageKey对应。单位:分钟。
        :type UsageValue: list of float
        """
        self._TimeKey = None
        self._TimeStampKey = None
        self._UsageValue = None

    @property
    def TimeKey(self):
        r"""时间点，格式为YYYY-MM-DD HH:mm:ss。多天查询时，HH:mm:ss为00:00:00。
        :rtype: str
        """
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeStampKey(self):
        r"""时间点时间戳
        :rtype: int
        """
        return self._TimeStampKey

    @TimeStampKey.setter
    def TimeStampKey(self, TimeStampKey):
        self._TimeStampKey = TimeStampKey

    @property
    def UsageValue(self):
        r"""用量数组。每个数值含义与UsageKey对应。单位:分钟。
        :rtype: list of float
        """
        return self._UsageValue

    @UsageValue.setter
    def UsageValue(self, UsageValue):
        self._UsageValue = UsageValue


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._TimeStampKey = params.get("TimeStampKey")
        self._UsageValue = params.get("UsageValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TurnDetection(AbstractModel):
    r"""断句配置

    """

    def __init__(self):
        r"""
        :param _SemanticEagerness: TurnDetectionMode为3时生效，语义断句的灵敏程度


功能简介：根据用户所说的话来判断其已完成发言来分割音频


可选: "low" | "medium" | "high" | "auto"


auto 是默认值，与 medium 相同。
low 将让用户有足够的时间说话。
high 将尽快对音频进行分块。


如果您希望模型在对话模式下更频繁地响应，可以将 SemanticEagerness 设置为 high
如果您希望在用户停顿时，AI能够等待片刻，可以将 SemanticEagerness 设置为 low
无论什么模式，最终都会分割送个大模型进行回复

        :type SemanticEagerness: str
        """
        self._SemanticEagerness = None

    @property
    def SemanticEagerness(self):
        r"""TurnDetectionMode为3时生效，语义断句的灵敏程度


功能简介：根据用户所说的话来判断其已完成发言来分割音频


可选: "low" | "medium" | "high" | "auto"


auto 是默认值，与 medium 相同。
low 将让用户有足够的时间说话。
high 将尽快对音频进行分块。


如果您希望模型在对话模式下更频繁地响应，可以将 SemanticEagerness 设置为 high
如果您希望在用户停顿时，AI能够等待片刻，可以将 SemanticEagerness 设置为 low
无论什么模式，最终都会分割送个大模型进行回复

        :rtype: str
        """
        return self._SemanticEagerness

    @SemanticEagerness.setter
    def SemanticEagerness(self, SemanticEagerness):
        self._SemanticEagerness = SemanticEagerness


    def _deserialize(self, params):
        self._SemanticEagerness = params.get("SemanticEagerness")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIConversationRequest(AbstractModel):
    r"""UpdateAIConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 唯一标识一个任务
        :type TaskId: str
        :param _WelcomeMessage: 不填写则不进行更新，机器人的欢迎语
        :type WelcomeMessage: str
        :param _InterruptMode: 不填写则不进行更新。智能打断模式，0表示服务端自动打断，1表示服务端不打断，由端上发送打断信令进行打断
        :type InterruptMode: int
        :param _InterruptSpeechDuration: 不填写则不进行更新。InterruptMode为0时使用，单位为毫秒，默认为500ms。表示服务端检测到持续InterruptSpeechDuration毫秒的人声则进行打断
        :type InterruptSpeechDuration: int
        :param _LLMConfig: 不填写则不进行更新，LLM配置，详情见StartAIConversation接口
        :type LLMConfig: str
        :param _TTSConfig: 不填写则不进行更新，TTS配置，详情见StartAIConversation接口
        :type TTSConfig: str
        """
        self._TaskId = None
        self._WelcomeMessage = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None
        self._LLMConfig = None
        self._TTSConfig = None

    @property
    def TaskId(self):
        r"""唯一标识一个任务
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def WelcomeMessage(self):
        r"""不填写则不进行更新，机器人的欢迎语
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def InterruptMode(self):
        r"""不填写则不进行更新。智能打断模式，0表示服务端自动打断，1表示服务端不打断，由端上发送打断信令进行打断
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        r"""不填写则不进行更新。InterruptMode为0时使用，单位为毫秒，默认为500ms。表示服务端检测到持续InterruptSpeechDuration毫秒的人声则进行打断
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration

    @property
    def LLMConfig(self):
        r"""不填写则不进行更新，LLM配置，详情见StartAIConversation接口
        :rtype: str
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        r"""不填写则不进行更新，TTS配置，详情见StartAIConversation接口
        :rtype: str
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        self._LLMConfig = params.get("LLMConfig")
        self._TTSConfig = params.get("TTSConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIConversationResponse(AbstractModel):
    r"""UpdateAIConversation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdatePublishCdnStreamRequest(AbstractModel):
    r"""UpdatePublishCdnStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和转推的房间所对应的SdkAppId相同。
        :type SdkAppId: int
        :param _TaskId: 唯一标识转推任务。
        :type TaskId: str
        :param _SequenceNumber: 客户保证同一个任务，每次更新请求中的SequenceNumber递增，防止请求乱序。
        :type SequenceNumber: int
        :param _WithTranscoding: 是否转码，0表示无需转码，1表示需要转码。
注：混流是必须转码，这个参数需设置为1。
        :type WithTranscoding: int
        :param _AudioParams: 更新相关参数，只支持更新参与混音的主播列表参数，不支持更新Codec、采样率、码率和声道数。不填表示不更新此参数。
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param _VideoParams: 更新视频相关参数，转码时支持更新除编码类型之外的编码参数，视频布局参数，背景图片和背景颜色参数，水印参数。不填表示不更新此参数。
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param _SingleSubscribeParams: 更新单流转推的用户上行参数，仅在非转码时有效。不填表示不更新此参数。
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param _PublishCdnParams: 更新转推的CDN参数。不填表示不更新此参数。
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _SeiParams: 混流SEI参数
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param _FeedBackRoomParams: 回推房间信息
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SequenceNumber = None
        self._WithTranscoding = None
        self._AudioParams = None
        self._VideoParams = None
        self._SingleSubscribeParams = None
        self._PublishCdnParams = None
        self._SeiParams = None
        self._FeedBackRoomParams = None

    @property
    def SdkAppId(self):
        r"""TRTC的[SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid)，和转推的房间所对应的SdkAppId相同。
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""唯一标识转推任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SequenceNumber(self):
        r"""客户保证同一个任务，每次更新请求中的SequenceNumber递增，防止请求乱序。
        :rtype: int
        """
        return self._SequenceNumber

    @SequenceNumber.setter
    def SequenceNumber(self, SequenceNumber):
        self._SequenceNumber = SequenceNumber

    @property
    def WithTranscoding(self):
        r"""是否转码，0表示无需转码，1表示需要转码。
注：混流是必须转码，这个参数需设置为1。
        :rtype: int
        """
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        r"""更新相关参数，只支持更新参与混音的主播列表参数，不支持更新Codec、采样率、码率和声道数。不填表示不更新此参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        r"""更新视频相关参数，转码时支持更新除编码类型之外的编码参数，视频布局参数，背景图片和背景颜色参数，水印参数。不填表示不更新此参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        r"""更新单流转推的用户上行参数，仅在非转码时有效。不填表示不更新此参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        """
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        r"""更新转推的CDN参数。不填表示不更新此参数。
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        r"""混流SEI参数
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        """
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
        r"""回推房间信息
        :rtype: list of McuFeedBackRoomParams
        """
        return self._FeedBackRoomParams

    @FeedBackRoomParams.setter
    def FeedBackRoomParams(self, FeedBackRoomParams):
        self._FeedBackRoomParams = FeedBackRoomParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._SequenceNumber = params.get("SequenceNumber")
        self._WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self._AudioParams = McuAudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self._VideoParams = McuVideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self._SingleSubscribeParams = SingleSubscribeParams()
            self._SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self._SeiParams = McuSeiParams()
            self._SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self._FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self._FeedBackRoomParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePublishCdnStreamResponse(AbstractModel):
    r"""UpdatePublishCdnStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 转推任务唯一的String Id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""转推任务唯一的String Id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UpdateStreamIngestRequest(AbstractModel):
    r"""UpdateStreamIngest请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SDKAppId，和任务的房间所对应的SDKAppId相同
        :type SdkAppId: int
        :param _TaskId: 任务的唯一Id，在启动任务成功后会返回。
        :type TaskId: str
        :param _StreamUrl: 源流URL。
        :type StreamUrl: str
        :param _Volume: 音量，取值范围[0, 100]，默认100，表示原音量。
        :type Volume: int
        :param _IsPause: 是否暂停，默认false表示不暂停。暂停期间任务仍在进行中仍会计费，暂停超过12小时会自动销毁任务, 建议主动调用停止任务接口。
        :type IsPause: bool
        """
        self._SdkAppId = None
        self._TaskId = None
        self._StreamUrl = None
        self._Volume = None
        self._IsPause = None

    @property
    def SdkAppId(self):
        r"""TRTC的SDKAppId，和任务的房间所对应的SDKAppId相同
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        r"""任务的唯一Id，在启动任务成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StreamUrl(self):
        r"""源流URL。
        :rtype: str
        """
        return self._StreamUrl

    @StreamUrl.setter
    def StreamUrl(self, StreamUrl):
        self._StreamUrl = StreamUrl

    @property
    def Volume(self):
        r"""音量，取值范围[0, 100]，默认100，表示原音量。
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def IsPause(self):
        r"""是否暂停，默认false表示不暂停。暂停期间任务仍在进行中仍会计费，暂停超过12小时会自动销毁任务, 建议主动调用停止任务接口。
        :rtype: bool
        """
        return self._IsPause

    @IsPause.setter
    def IsPause(self, IsPause):
        self._IsPause = IsPause


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._StreamUrl = params.get("StreamUrl")
        self._Volume = params.get("Volume")
        self._IsPause = params.get("IsPause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStreamIngestResponse(AbstractModel):
    r"""UpdateStreamIngest返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务的状态信息。InProgress：表示当前任务正在进行中。NotExist：表示当前任务不存在。示例值：InProgress
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务的状态信息。InProgress：表示当前任务正在进行中。NotExist：表示当前任务不存在。示例值：InProgress
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class UpdateVoicePrintRequest(AbstractModel):
    r"""UpdateVoicePrint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 声纹信息ID
        :type VoicePrintId: str
        :param _ReqTimestamp: 毫秒时间戳
        :type ReqTimestamp: int
        :param _AudioFormat: 音频格式,目前只支持0,代表wav
        :type AudioFormat: int
        :param _Audio: 整个wav音频文件的base64字符串,其中wav文件限定为16k采样率, 16bit位深, 单声道, 8到18秒音频时长,有效音频不小于6秒(不能有太多静音段),编码数据大小不超过2M
        :type Audio: str
        :param _AudioMetaInfo: 和声纹绑定的MetaInfo，长度最大不超过512
        :type AudioMetaInfo: str
        """
        self._VoicePrintId = None
        self._ReqTimestamp = None
        self._AudioFormat = None
        self._Audio = None
        self._AudioMetaInfo = None

    @property
    def VoicePrintId(self):
        r"""声纹信息ID
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def ReqTimestamp(self):
        r"""毫秒时间戳
        :rtype: int
        """
        return self._ReqTimestamp

    @ReqTimestamp.setter
    def ReqTimestamp(self, ReqTimestamp):
        self._ReqTimestamp = ReqTimestamp

    @property
    def AudioFormat(self):
        r"""音频格式,目前只支持0,代表wav
        :rtype: int
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def Audio(self):
        r"""整个wav音频文件的base64字符串,其中wav文件限定为16k采样率, 16bit位深, 单声道, 8到18秒音频时长,有效音频不小于6秒(不能有太多静音段),编码数据大小不超过2M
        :rtype: str
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def AudioMetaInfo(self):
        r"""和声纹绑定的MetaInfo，长度最大不超过512
        :rtype: str
        """
        return self._AudioMetaInfo

    @AudioMetaInfo.setter
    def AudioMetaInfo(self, AudioMetaInfo):
        self._AudioMetaInfo = AudioMetaInfo


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        self._ReqTimestamp = params.get("ReqTimestamp")
        self._AudioFormat = params.get("AudioFormat")
        self._Audio = params.get("Audio")
        self._AudioMetaInfo = params.get("AudioMetaInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateVoicePrintResponse(AbstractModel):
    r"""UpdateVoicePrint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UserInformation(AbstractModel):
    r"""用户信息，包括用户进房时间，退房时间等

    """

    def __init__(self):
        r"""
        :param _RoomStr: 房间号
        :type RoomStr: str
        :param _UserId: 用户Id
        :type UserId: str
        :param _JoinTs: 用户进房时间
        :type JoinTs: int
        :param _LeaveTs: 用户退房时间，用户没有退房则返回当前时间
        :type LeaveTs: int
        :param _DeviceType: 终端类型
        :type DeviceType: str
        :param _SdkVersion: Sdk版本号
        :type SdkVersion: str
        :param _ClientIp: 客户端IP地址
        :type ClientIp: str
        :param _Finished: 判断用户是否已经离开房间
        :type Finished: bool
        """
        self._RoomStr = None
        self._UserId = None
        self._JoinTs = None
        self._LeaveTs = None
        self._DeviceType = None
        self._SdkVersion = None
        self._ClientIp = None
        self._Finished = None

    @property
    def RoomStr(self):
        r"""房间号
        :rtype: str
        """
        return self._RoomStr

    @RoomStr.setter
    def RoomStr(self, RoomStr):
        self._RoomStr = RoomStr

    @property
    def UserId(self):
        r"""用户Id
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def JoinTs(self):
        r"""用户进房时间
        :rtype: int
        """
        return self._JoinTs

    @JoinTs.setter
    def JoinTs(self, JoinTs):
        self._JoinTs = JoinTs

    @property
    def LeaveTs(self):
        r"""用户退房时间，用户没有退房则返回当前时间
        :rtype: int
        """
        return self._LeaveTs

    @LeaveTs.setter
    def LeaveTs(self, LeaveTs):
        self._LeaveTs = LeaveTs

    @property
    def DeviceType(self):
        r"""终端类型
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def SdkVersion(self):
        r"""Sdk版本号
        :rtype: str
        """
        return self._SdkVersion

    @SdkVersion.setter
    def SdkVersion(self, SdkVersion):
        self._SdkVersion = SdkVersion

    @property
    def ClientIp(self):
        r"""客户端IP地址
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Finished(self):
        r"""判断用户是否已经离开房间
        :rtype: bool
        """
        return self._Finished

    @Finished.setter
    def Finished(self, Finished):
        self._Finished = Finished


    def _deserialize(self, params):
        self._RoomStr = params.get("RoomStr")
        self._UserId = params.get("UserId")
        self._JoinTs = params.get("JoinTs")
        self._LeaveTs = params.get("LeaveTs")
        self._DeviceType = params.get("DeviceType")
        self._SdkVersion = params.get("SdkVersion")
        self._ClientIp = params.get("ClientIp")
        self._Finished = params.get("Finished")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserMediaStream(AbstractModel):
    r"""用户媒体流参数。

    """

    def __init__(self):
        r"""
        :param _UserInfo: TRTC用户参数。
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        :param _StreamType: 主辅路流类型，0为摄像头，1为屏幕分享，不填默认为0。
        :type StreamType: int
        """
        self._UserInfo = None
        self._StreamType = None

    @property
    def UserInfo(self):
        r"""TRTC用户参数。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def StreamType(self):
        r"""主辅路流类型，0为摄像头，1为屏幕分享，不填默认为0。
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = MixUserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._StreamType = params.get("StreamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncode(AbstractModel):
    r"""视频编码参数。

    """

    def __init__(self):
        r"""
        :param _Width: 输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :type Width: int
        :param _Height: 输出流高，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :type Height: int
        :param _Fps: 输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :type Fps: int
        :param _BitRate: 输出流码率，音视频输出时必填。取值范围[1,10000]，单位为kbps。
        :type BitRate: int
        :param _Gop: 输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        r"""输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""输出流高，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        r"""输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        r"""输出流码率，音视频输出时必填。取值范围[1,10000]，单位为kbps。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        r"""输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodeParams(AbstractModel):
    r"""视频转码参数

    """

    def __init__(self):
        r"""
        :param _Width: 宽。取值范围[0,1920]，单位为像素值。
        :type Width: int
        :param _Height: 高。取值范围[0,1080]，单位为像素值。
        :type Height: int
        :param _Fps: 帧率。取值范围[1,60]，表示帧率可选范围为1到60fps。
        :type Fps: int
        :param _BitRate: 码率。取值范围[1,10000]，单位为kbps。
        :type BitRate: int
        :param _Gop: gop。取值范围[1,2]，单位为秒。
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        r"""宽。取值范围[0,1920]，单位为像素值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""高。取值范围[0,1080]，单位为像素值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        r"""帧率。取值范围[1,60]，表示帧率可选范围为1到60fps。
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        r"""码率。取值范围[1,10000]，单位为kbps。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        r"""gop。取值范围[1,2]，单位为秒。
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoParams(AbstractModel):
    r"""录制视频转码参数。

    """

    def __init__(self):
        r"""
        :param _Width: 视频的宽度值，单位为像素，默认值360。不能超过1920，与height的乘积不能超过1920*1080。
        :type Width: int
        :param _Height: 视频的高度值，单位为像素，默认值640。不能超过1920，与width的乘积不能超过1920*1080。
        :type Height: int
        :param _Fps: 视频的帧率，范围[1, 60]，默认15。
        :type Fps: int
        :param _BitRate: 视频的码率,单位是bps，范围[64000, 8192000]，默认550000bps。
        :type BitRate: int
        :param _Gop: 视频关键帧时间间隔，单位秒，默认值10秒。
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        r"""视频的宽度值，单位为像素，默认值360。不能超过1920，与height的乘积不能超过1920*1080。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""视频的高度值，单位为像素，默认值640。不能超过1920，与width的乘积不能超过1920*1080。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        r"""视频的帧率，范围[1, 60]，默认15。
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        r"""视频的码率,单位是bps，范围[64000, 8192000]，默认550000bps。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        r"""视频关键帧时间间隔，单位秒，默认值10秒。
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Voice(AbstractModel):
    r"""TTS的声音参数

    """

    def __init__(self):
        r"""
        :param _VoiceId: TTS的声音的ID
        :type VoiceId: str
        :param _Speed: 语速，范围 0.5-2.0，默认 1.0
        :type Speed: float
        :param _Volume: (0, 10]   默认值1.0 
        :type Volume: float
        :param _Pitch: 取值[-12,12],默认0
        :type Pitch: int
        """
        self._VoiceId = None
        self._Speed = None
        self._Volume = None
        self._Pitch = None

    @property
    def VoiceId(self):
        r"""TTS的声音的ID
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def Speed(self):
        r"""语速，范围 0.5-2.0，默认 1.0
        :rtype: float
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed

    @property
    def Volume(self):
        r"""(0, 10]   默认值1.0 
        :rtype: float
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def Pitch(self):
        r"""取值[-12,12],默认0
        :rtype: int
        """
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch


    def _deserialize(self, params):
        self._VoiceId = params.get("VoiceId")
        self._Speed = params.get("Speed")
        self._Volume = params.get("Volume")
        self._Pitch = params.get("Pitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceCloneRequest(AbstractModel):
    r"""VoiceClone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC的SdkAppId
        :type SdkAppId: int
        :param _VoiceName: 声音克隆的名称, 只允许使用数字、字母、下划线，不能超过36位
        :type VoiceName: str
        :param _PromptAudio: 声音克隆的参考音频，必须为16k单声道的wav的base64字符串， 长度在5秒～12秒之间
        :type PromptAudio: str
        :param _APIKey: TTS的API密钥
        :type APIKey: str
        :param _PromptText: 声音克隆的参考文本，为参考音频对应的文字。
        :type PromptText: str
        :param _Model: TTS的模型：flow_01_turbo，flow_01_ex
        :type Model: str
        :param _Language: 语言参数，默认为空， 参考： (ISO 639-1) 
        :type Language: str
        """
        self._SdkAppId = None
        self._VoiceName = None
        self._PromptAudio = None
        self._APIKey = None
        self._PromptText = None
        self._Model = None
        self._Language = None

    @property
    def SdkAppId(self):
        r"""TRTC的SdkAppId
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def VoiceName(self):
        r"""声音克隆的名称, 只允许使用数字、字母、下划线，不能超过36位
        :rtype: str
        """
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName

    @property
    def PromptAudio(self):
        r"""声音克隆的参考音频，必须为16k单声道的wav的base64字符串， 长度在5秒～12秒之间
        :rtype: str
        """
        return self._PromptAudio

    @PromptAudio.setter
    def PromptAudio(self, PromptAudio):
        self._PromptAudio = PromptAudio

    @property
    def APIKey(self):
        r"""TTS的API密钥
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        self._APIKey = APIKey

    @property
    def PromptText(self):
        r"""声音克隆的参考文本，为参考音频对应的文字。
        :rtype: str
        """
        return self._PromptText

    @PromptText.setter
    def PromptText(self, PromptText):
        self._PromptText = PromptText

    @property
    def Model(self):
        r"""TTS的模型：flow_01_turbo，flow_01_ex
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Language(self):
        r"""语言参数，默认为空， 参考： (ISO 639-1) 
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._VoiceName = params.get("VoiceName")
        self._PromptAudio = params.get("PromptAudio")
        self._APIKey = params.get("APIKey")
        self._PromptText = params.get("PromptText")
        self._Model = params.get("Model")
        self._Language = params.get("Language")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceCloneResponse(AbstractModel):
    r"""VoiceClone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VoiceId: 克隆出的音色ID，可以用此id进行语音合成
        :type VoiceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VoiceId = None
        self._RequestId = None

    @property
    def VoiceId(self):
        r"""克隆出的音色ID，可以用此id进行语音合成
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._VoiceId = params.get("VoiceId")
        self._RequestId = params.get("RequestId")


class VoicePrint(AbstractModel):
    r"""声纹配置参数

    """

    def __init__(self):
        r"""
        :param _Mode: 默认为0，表示不启用声纹。1表示启用声纹，此时需要填写voiceprint id。
        :type Mode: int
        :param _IdList: VoicePrint Mode为1时需要填写，目前仅支持填写一个声纹id
        :type IdList: list of str
        """
        self._Mode = None
        self._IdList = None

    @property
    def Mode(self):
        r"""默认为0，表示不启用声纹。1表示启用声纹，此时需要填写voiceprint id。
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def IdList(self):
        r"""VoicePrint Mode为1时需要填写，目前仅支持填写一个声纹id
        :rtype: list of str
        """
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._IdList = params.get("IdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoicePrintInfo(AbstractModel):
    r"""声纹查询数据

    """

    def __init__(self):
        r"""
        :param _VoicePrintId: 声纹ID
        :type VoicePrintId: str
        :param _AppId: 应用id
        :type AppId: int
        :param _VoicePrintMetaInfo: 和声纹绑定的MetaInfo
        :type VoicePrintMetaInfo: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _AudioFormat: 音频格式,当前只有0(代表wav)
        :type AudioFormat: int
        :param _AudioName: 音频名称
        :type AudioName: str
        :param _ReqTimestamp: 请求毫秒时间戳
        :type ReqTimestamp: int
        """
        self._VoicePrintId = None
        self._AppId = None
        self._VoicePrintMetaInfo = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AudioFormat = None
        self._AudioName = None
        self._ReqTimestamp = None

    @property
    def VoicePrintId(self):
        r"""声纹ID
        :rtype: str
        """
        return self._VoicePrintId

    @VoicePrintId.setter
    def VoicePrintId(self, VoicePrintId):
        self._VoicePrintId = VoicePrintId

    @property
    def AppId(self):
        r"""应用id
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def VoicePrintMetaInfo(self):
        r"""和声纹绑定的MetaInfo
        :rtype: str
        """
        return self._VoicePrintMetaInfo

    @VoicePrintMetaInfo.setter
    def VoicePrintMetaInfo(self, VoicePrintMetaInfo):
        self._VoicePrintMetaInfo = VoicePrintMetaInfo

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AudioFormat(self):
        r"""音频格式,当前只有0(代表wav)
        :rtype: int
        """
        return self._AudioFormat

    @AudioFormat.setter
    def AudioFormat(self, AudioFormat):
        self._AudioFormat = AudioFormat

    @property
    def AudioName(self):
        r"""音频名称
        :rtype: str
        """
        return self._AudioName

    @AudioName.setter
    def AudioName(self, AudioName):
        self._AudioName = AudioName

    @property
    def ReqTimestamp(self):
        r"""请求毫秒时间戳
        :rtype: int
        """
        return self._ReqTimestamp

    @ReqTimestamp.setter
    def ReqTimestamp(self, ReqTimestamp):
        self._ReqTimestamp = ReqTimestamp


    def _deserialize(self, params):
        self._VoicePrintId = params.get("VoicePrintId")
        self._AppId = params.get("AppId")
        self._VoicePrintMetaInfo = params.get("VoicePrintMetaInfo")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AudioFormat = params.get("AudioFormat")
        self._AudioName = params.get("AudioName")
        self._ReqTimestamp = params.get("ReqTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMark(AbstractModel):
    r"""水印布局参数

    """

    def __init__(self):
        r"""
        :param _WaterMarkType: 水印类型，0为图片（默认），1为文字，2为时间戳。
        :type WaterMarkType: int
        :param _WaterMarkImage: 水印为图片时的参数列表，水印为图片时校验必填。
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        :param _WaterMarkChar: 水印为文字时的参数列表，水印为文字时校验必填。
        :type WaterMarkChar: :class:`tencentcloud.trtc.v20190722.models.WaterMarkChar`
        :param _WaterMarkTimestamp: 水印为时间戳时的参数列表，水印为时间戳时校验必填。
        :type WaterMarkTimestamp: :class:`tencentcloud.trtc.v20190722.models.WaterMarkTimestamp`
        """
        self._WaterMarkType = None
        self._WaterMarkImage = None
        self._WaterMarkChar = None
        self._WaterMarkTimestamp = None

    @property
    def WaterMarkType(self):
        r"""水印类型，0为图片（默认），1为文字，2为时间戳。
        :rtype: int
        """
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        r"""水印为图片时的参数列表，水印为图片时校验必填。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        """
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkChar(self):
        r"""水印为文字时的参数列表，水印为文字时校验必填。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkChar`
        """
        return self._WaterMarkChar

    @WaterMarkChar.setter
    def WaterMarkChar(self, WaterMarkChar):
        self._WaterMarkChar = WaterMarkChar

    @property
    def WaterMarkTimestamp(self):
        r"""水印为时间戳时的参数列表，水印为时间戳时校验必填。
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkTimestamp`
        """
        return self._WaterMarkTimestamp

    @WaterMarkTimestamp.setter
    def WaterMarkTimestamp(self, WaterMarkTimestamp):
        self._WaterMarkTimestamp = WaterMarkTimestamp


    def _deserialize(self, params):
        self._WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self._WaterMarkImage = WaterMarkImage()
            self._WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        if params.get("WaterMarkChar") is not None:
            self._WaterMarkChar = WaterMarkChar()
            self._WaterMarkChar._deserialize(params.get("WaterMarkChar"))
        if params.get("WaterMarkTimestamp") is not None:
            self._WaterMarkTimestamp = WaterMarkTimestamp()
            self._WaterMarkTimestamp._deserialize(params.get("WaterMarkTimestamp"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkChar(AbstractModel):
    r"""自定义文字水印数据结构

    """

    def __init__(self):
        r"""
        :param _Top: 文字水印的起始坐标Y值，从左上角开始
        :type Top: int
        :param _Left: 文字水印的起始坐标X值，从左上角开始
        :type Left: int
        :param _Width: 文字水印的宽度，单位像素值
        :type Width: int
        :param _Height: 文字水印的高度，单位像素值
        :type Height: int
        :param _Chars: 水印文字的内容
        :type Chars: str
        :param _FontSize: 水印文字的大小，单位像素，默认14
        :type FontSize: int
        :param _FontColor: 水印文字的颜色，默认白色
        :type FontColor: str
        :param _BackGroundColor: 水印文字的背景色，为空代表背景透明，默认为空
        :type BackGroundColor: str
        :param _Font: 文字水印的字体，支持设置以下值：
1. Tencent （默认）
2. SourceHanSans
        :type Font: str
        """
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None
        self._Chars = None
        self._FontSize = None
        self._FontColor = None
        self._BackGroundColor = None
        self._Font = None

    @property
    def Top(self):
        r"""文字水印的起始坐标Y值，从左上角开始
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        r"""文字水印的起始坐标X值，从左上角开始
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        r"""文字水印的宽度，单位像素值
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""文字水印的高度，单位像素值
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Chars(self):
        r"""水印文字的内容
        :rtype: str
        """
        return self._Chars

    @Chars.setter
    def Chars(self, Chars):
        self._Chars = Chars

    @property
    def FontSize(self):
        r"""水印文字的大小，单位像素，默认14
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        r"""水印文字的颜色，默认白色
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
        r"""水印文字的背景色，为空代表背景透明，默认为空
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def Font(self):
        r"""文字水印的字体，支持设置以下值：
1. Tencent （默认）
2. SourceHanSans
        :rtype: str
        """
        return self._Font

    @Font.setter
    def Font(self, Font):
        self._Font = Font


    def _deserialize(self, params):
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Chars = params.get("Chars")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        self._BackGroundColor = params.get("BackGroundColor")
        self._Font = params.get("Font")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkImage(AbstractModel):
    r"""水印类型为图片的参数列表

    """

    def __init__(self):
        r"""
        :param _WaterMarkUrl: 下载的url地址， 只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :type WaterMarkUrl: str
        :param _Top: 画布上该画面左上角的 y 轴坐标，取值范围 [0, 2560]，不能超过画布的高。
        :type Top: int
        :param _Left: 画布上该画面左上角的 x 轴坐标，取值范围 [0, 2560]，不能超过画布的宽。
        :type Left: int
        :param _Width: 画布上该画面宽度的相对值，取值范围 [0, 2560]，与Left相加不应超过画布的宽。
        :type Width: int
        :param _Height: 画布上该画面高度的相对值，取值范围 [0, 2560]，与Top相加不应超过画布的高。
        :type Height: int
        """
        self._WaterMarkUrl = None
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None

    @property
    def WaterMarkUrl(self):
        r"""下载的url地址， 只支持jpg, png, jpeg，大小限制不超过5M。注意，url必须携带格式后缀，url内只支持特定的字符串, 范围是a-z A-Z 0-9 '-', '.', '_', '~', ':', '/', '?', '#', '[', ']' '@', '!', '&', '(', ')', '*', '+', ',', '%', '='
        :rtype: str
        """
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def Top(self):
        r"""画布上该画面左上角的 y 轴坐标，取值范围 [0, 2560]，不能超过画布的高。
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        r"""画布上该画面左上角的 x 轴坐标，取值范围 [0, 2560]，不能超过画布的宽。
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        r"""画布上该画面宽度的相对值，取值范围 [0, 2560]，与Left相加不应超过画布的宽。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""画布上该画面高度的相对值，取值范围 [0, 2560]，与Top相加不应超过画布的高。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._WaterMarkUrl = params.get("WaterMarkUrl")
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkParams(AbstractModel):
    r"""MCU混流水印参数

    """

    def __init__(self):
        r"""
        :param _WaterMarkId: 混流-水印图片ID。取值为实时音视频控制台上传的图片ID。
        :type WaterMarkId: int
        :param _WaterMarkWidth: 混流-水印宽。单位为像素值。水印宽+X偏移不能超过整个画布宽。
        :type WaterMarkWidth: int
        :param _WaterMarkHeight: 混流-水印高。单位为像素值。水印高+Y偏移不能超过整个画布高。
        :type WaterMarkHeight: int
        :param _LocationX: 水印在输出时的X偏移。单位为像素值。水印宽+X偏移不能超过整个画布宽。
        :type LocationX: int
        :param _LocationY: 水印在输出时的Y偏移。单位为像素值。水印高+Y偏移不能超过整个画布高。
        :type LocationY: int
        :param _WaterMarkUrl: 混流-水印图片URL地址，支持png、jpg、jpeg、bmp格式，暂不支持透明通道。URL链接长度限制为512字节。WaterMarkUrl和WaterMarkId参数都填时，以WaterMarkUrl为准。图片大小限制不超过2MB。
        :type WaterMarkUrl: str
        """
        self._WaterMarkId = None
        self._WaterMarkWidth = None
        self._WaterMarkHeight = None
        self._LocationX = None
        self._LocationY = None
        self._WaterMarkUrl = None

    @property
    def WaterMarkId(self):
        r"""混流-水印图片ID。取值为实时音视频控制台上传的图片ID。
        :rtype: int
        """
        return self._WaterMarkId

    @WaterMarkId.setter
    def WaterMarkId(self, WaterMarkId):
        self._WaterMarkId = WaterMarkId

    @property
    def WaterMarkWidth(self):
        r"""混流-水印宽。单位为像素值。水印宽+X偏移不能超过整个画布宽。
        :rtype: int
        """
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        r"""混流-水印高。单位为像素值。水印高+Y偏移不能超过整个画布高。
        :rtype: int
        """
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        r"""水印在输出时的X偏移。单位为像素值。水印宽+X偏移不能超过整个画布宽。
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        r"""水印在输出时的Y偏移。单位为像素值。水印高+Y偏移不能超过整个画布高。
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def WaterMarkUrl(self):
        r"""混流-水印图片URL地址，支持png、jpg、jpeg、bmp格式，暂不支持透明通道。URL链接长度限制为512字节。WaterMarkUrl和WaterMarkId参数都填时，以WaterMarkUrl为准。图片大小限制不超过2MB。
        :rtype: str
        """
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl


    def _deserialize(self, params):
        self._WaterMarkId = params.get("WaterMarkId")
        self._WaterMarkWidth = params.get("WaterMarkWidth")
        self._WaterMarkHeight = params.get("WaterMarkHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._WaterMarkUrl = params.get("WaterMarkUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkTimestamp(AbstractModel):
    r"""时间戳水印数据结构

    """

    def __init__(self):
        r"""
        :param _Pos: 时间戳的位置，取值范围0-6，分别代表上左，上右，下左，下右，上居中，下居中，居中
        :type Pos: int
        :param _TimeZone: 显示时间戳的时区，默认东八区
        :type TimeZone: int
        :param _Font: 文字水印的字体，支持设置以下值：
1. Tencent （默认）
2. SourceHanSans
        :type Font: str
        """
        self._Pos = None
        self._TimeZone = None
        self._Font = None

    @property
    def Pos(self):
        r"""时间戳的位置，取值范围0-6，分别代表上左，上右，下左，下右，上居中，下居中，居中
        :rtype: int
        """
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos

    @property
    def TimeZone(self):
        r"""显示时间戳的时区，默认东八区
        :rtype: int
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone

    @property
    def Font(self):
        r"""文字水印的字体，支持设置以下值：
1. Tencent （默认）
2. SourceHanSans
        :rtype: str
        """
        return self._Font

    @Font.setter
    def Font(self, Font):
        self._Font = Font


    def _deserialize(self, params):
        self._Pos = params.get("Pos")
        self._TimeZone = params.get("TimeZone")
        self._Font = params.get("Font")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebRecordVideoParams(AbstractModel):
    r"""页面录制控制参数

    """

    def __init__(self):
        r"""
        :param _Width: 录制画面宽度，默认为1280，取值范围[0, 1920]
        :type Width: int
        :param _Height: 录制画面高度，默认为720，取值范围[0, 1080]
        :type Height: int
        :param _Format: 指定输出格式，可选hls,mp4。存储到云点播VOD时此参数无效，存储到VOD时请通过TencentVod（https://cloud.tencent.com/document/api/647/44055#TencentVod）内的MediaType设置。

        :type Format: str
        :param _MaxMediaFileDuration: 如果是aac或者mp4文件格式，超过长度限制后，系统会自动拆分视频文件。单位：分钟。默认为1440min（24h），取值范围为1-1440。【单文件限制最大为2G，满足文件大小 >2G 或录制时长度 > 24h任意一个条件，文件都会自动切分】
Hls 格式录制此参数不生效。
示例值：1440
        :type MaxMediaFileDuration: int
        """
        self._Width = None
        self._Height = None
        self._Format = None
        self._MaxMediaFileDuration = None

    @property
    def Width(self):
        r"""录制画面宽度，默认为1280，取值范围[0, 1920]
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""录制画面高度，默认为720，取值范围[0, 1080]
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Format(self):
        r"""指定输出格式，可选hls,mp4。存储到云点播VOD时此参数无效，存储到VOD时请通过TencentVod（https://cloud.tencent.com/document/api/647/44055#TencentVod）内的MediaType设置。

        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def MaxMediaFileDuration(self):
        r"""如果是aac或者mp4文件格式，超过长度限制后，系统会自动拆分视频文件。单位：分钟。默认为1440min（24h），取值范围为1-1440。【单文件限制最大为2G，满足文件大小 >2G 或录制时长度 > 24h任意一个条件，文件都会自动切分】
Hls 格式录制此参数不生效。
示例值：1440
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Format = params.get("Format")
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        