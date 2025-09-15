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


class AsrTimestamps(AbstractModel):
    r"""文本片段及其时间戳

    """

    def __init__(self):
        r"""
        :param _Text: 文本片段
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _StartMs: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartMs: int
        :param _EndMs: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndMs: int
        """
        self._Text = None
        self._StartMs = None
        self._EndMs = None

    @property
    def Text(self):
        r"""文本片段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def StartMs(self):
        r"""开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._StartMs

    @StartMs.setter
    def StartMs(self, StartMs):
        self._StartMs = StartMs

    @property
    def EndMs(self):
        r"""结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EndMs

    @EndMs.setter
    def EndMs(self, EndMs):
        self._EndMs = EndMs


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._StartMs = params.get("StartMs")
        self._EndMs = params.get("EndMs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTranslateResult(AbstractModel):
    r"""音频翻译结果

    """

    def __init__(self):
        r"""
        :param _SourceText: 原文本
        :type SourceText: str
        :param _TargetText: 目标文本
        :type TargetText: str
        """
        self._SourceText = None
        self._TargetText = None

    @property
    def SourceText(self):
        r"""原文本
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""目标文本
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmVideoTranslateJobRequest(AbstractModel):
    r"""ConfirmVideoTranslateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频翻译任务 ID
        :type JobId: str
        :param _TranslateResults: 待确认文本
        :type TranslateResults: list of AudioTranslateResult
        """
        self._JobId = None
        self._TranslateResults = None

    @property
    def JobId(self):
        r"""视频翻译任务 ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TranslateResults(self):
        r"""待确认文本
        :rtype: list of AudioTranslateResult
        """
        return self._TranslateResults

    @TranslateResults.setter
    def TranslateResults(self, TranslateResults):
        self._TranslateResults = TranslateResults


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("TranslateResults") is not None:
            self._TranslateResults = []
            for item in params.get("TranslateResults"):
                obj = AudioTranslateResult()
                obj._deserialize(item)
                self._TranslateResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmVideoTranslateJobResponse(AbstractModel):
    r"""ConfirmVideoTranslateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频翻译任务 ID
        :type JobId: str
        :param _TaskId: 音频转换任务 ID
        :type TaskId: str
        :param _SessionId: 音频翻译结果确认 session
        :type SessionId: str
        :param _Status: 视频转译任务状态
        :type Status: int
        :param _Message: 视频转译任务信息
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._TaskId = None
        self._SessionId = None
        self._Status = None
        self._Message = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""视频翻译任务 ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskId(self):
        r"""音频转换任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        r"""音频翻译结果确认 session
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Status(self):
        r"""视频转译任务状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        r"""视频转译任务信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._JobId = params.get("JobId")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeVideoTranslateJobRequest(AbstractModel):
    r"""DescribeVideoTranslateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: JobId。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""JobId。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoTranslateJobResponse(AbstractModel):
    r"""DescribeVideoTranslateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatus: 任务状态。 1：音频翻译中。 2：音频翻译失败。 3：音频翻译成功。 4：音频结果待确认。 5：音频结果已确认完毕。6：视频翻译中。 7：视频翻译失败。 8：视频翻译成功。
        :type JobStatus: int
        :param _JobErrorCode: 任务错误码。
        :type JobErrorCode: str
        :param _JobErrorMsg: 任务错误信息。
        :type JobErrorMsg: str
        :param _ResultVideoUrl: 视频翻译结果。
        :type ResultVideoUrl: str
        :param _TranslateResults: 音频翻译结果。
        :type TranslateResults: list of TranslateResult
        :param _JobConfirm: 是否需要确认翻译结果。0：不需要，1：需要
        :type JobConfirm: int
        :param _JobAudioTaskId: 音频任务 ID
        :type JobAudioTaskId: str
        :param _JobVideoModerationId: 视频审核任务ID
        :type JobVideoModerationId: str
        :param _JobVideoId: 视频生成任务 ID
        :type JobVideoId: str
        :param _OriginalVideoUrl: 视频素材原始 URL
        :type OriginalVideoUrl: str
        :param _AsrTimestamps: 文本片段及其时间戳
        :type AsrTimestamps: list of AsrTimestamps
        :param _JobSubmitReqId: 提交视频翻译任务时的 requestId
        :type JobSubmitReqId: str
        :param _JobAudioModerationId: 音频审核任务 ID
        :type JobAudioModerationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatus = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultVideoUrl = None
        self._TranslateResults = None
        self._JobConfirm = None
        self._JobAudioTaskId = None
        self._JobVideoModerationId = None
        self._JobVideoId = None
        self._OriginalVideoUrl = None
        self._AsrTimestamps = None
        self._JobSubmitReqId = None
        self._JobAudioModerationId = None
        self._RequestId = None

    @property
    def JobStatus(self):
        r"""任务状态。 1：音频翻译中。 2：音频翻译失败。 3：音频翻译成功。 4：音频结果待确认。 5：音频结果已确认完毕。6：视频翻译中。 7：视频翻译失败。 8：视频翻译成功。
        :rtype: int
        """
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def JobErrorCode(self):
        r"""任务错误码。
        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        r"""任务错误信息。
        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultVideoUrl(self):
        r"""视频翻译结果。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def TranslateResults(self):
        r"""音频翻译结果。
        :rtype: list of TranslateResult
        """
        return self._TranslateResults

    @TranslateResults.setter
    def TranslateResults(self, TranslateResults):
        self._TranslateResults = TranslateResults

    @property
    def JobConfirm(self):
        r"""是否需要确认翻译结果。0：不需要，1：需要
        :rtype: int
        """
        return self._JobConfirm

    @JobConfirm.setter
    def JobConfirm(self, JobConfirm):
        self._JobConfirm = JobConfirm

    @property
    def JobAudioTaskId(self):
        r"""音频任务 ID
        :rtype: str
        """
        return self._JobAudioTaskId

    @JobAudioTaskId.setter
    def JobAudioTaskId(self, JobAudioTaskId):
        self._JobAudioTaskId = JobAudioTaskId

    @property
    def JobVideoModerationId(self):
        r"""视频审核任务ID
        :rtype: str
        """
        return self._JobVideoModerationId

    @JobVideoModerationId.setter
    def JobVideoModerationId(self, JobVideoModerationId):
        self._JobVideoModerationId = JobVideoModerationId

    @property
    def JobVideoId(self):
        r"""视频生成任务 ID
        :rtype: str
        """
        return self._JobVideoId

    @JobVideoId.setter
    def JobVideoId(self, JobVideoId):
        self._JobVideoId = JobVideoId

    @property
    def OriginalVideoUrl(self):
        r"""视频素材原始 URL
        :rtype: str
        """
        return self._OriginalVideoUrl

    @OriginalVideoUrl.setter
    def OriginalVideoUrl(self, OriginalVideoUrl):
        self._OriginalVideoUrl = OriginalVideoUrl

    @property
    def AsrTimestamps(self):
        r"""文本片段及其时间戳
        :rtype: list of AsrTimestamps
        """
        return self._AsrTimestamps

    @AsrTimestamps.setter
    def AsrTimestamps(self, AsrTimestamps):
        self._AsrTimestamps = AsrTimestamps

    @property
    def JobSubmitReqId(self):
        r"""提交视频翻译任务时的 requestId
        :rtype: str
        """
        return self._JobSubmitReqId

    @JobSubmitReqId.setter
    def JobSubmitReqId(self, JobSubmitReqId):
        self._JobSubmitReqId = JobSubmitReqId

    @property
    def JobAudioModerationId(self):
        r"""音频审核任务 ID
        :rtype: str
        """
        return self._JobAudioModerationId

    @JobAudioModerationId.setter
    def JobAudioModerationId(self, JobAudioModerationId):
        self._JobAudioModerationId = JobAudioModerationId

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
        self._JobStatus = params.get("JobStatus")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        if params.get("TranslateResults") is not None:
            self._TranslateResults = []
            for item in params.get("TranslateResults"):
                obj = TranslateResult()
                obj._deserialize(item)
                self._TranslateResults.append(obj)
        self._JobConfirm = params.get("JobConfirm")
        self._JobAudioTaskId = params.get("JobAudioTaskId")
        self._JobVideoModerationId = params.get("JobVideoModerationId")
        self._JobVideoId = params.get("JobVideoId")
        self._OriginalVideoUrl = params.get("OriginalVideoUrl")
        if params.get("AsrTimestamps") is not None:
            self._AsrTimestamps = []
            for item in params.get("AsrTimestamps"):
                obj = AsrTimestamps()
                obj._deserialize(item)
                self._AsrTimestamps.append(obj)
        self._JobSubmitReqId = params.get("JobSubmitReqId")
        self._JobAudioModerationId = params.get("JobAudioModerationId")
        self._RequestId = params.get("RequestId")


class SubmitVideoTranslateJobRequest(AbstractModel):
    r"""SubmitVideoTranslateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 视频地址URL。
格式要求：支持 mp4、mov 。
时长要求：【10-300】秒。
fps 要求：【15-60】fps
分辨率要求：单边像素要求在 【540~1920】 之间。
        :type VideoUrl: str
        :param _SrcLang: 源语言：zh(中文), en(英文)
        :type SrcLang: str
        :param _DstLang: 目标语种：
zh(简体中文)、en(英语)、ar(阿拉伯语)、de(德语)、es(西班牙语)、fr(法语)、id(印尼语)、it(意大利语)、ja(日语)、ko(韩语)、ms(马来语)、pt(葡萄牙语)、ru(俄语)、th(泰语)、tr(土耳其语)、vi(越南语)
示例值：ar(阿拉伯语)
        :type DstLang: str
        :param _AudioUrl: 当音频 URL 不为空时，默认以音频驱动视频任务口型。
格式要求：支持 mp3、m4a、acc、wav 格式。
时长要求：【10~300】秒
大小要求：不超过 100M。
示例值：http://xxx/audio.mp3
        :type AudioUrl: str
        :param _RemoveVocal: 是否需要去除VideoUrl或AudioUrl中背景音，取值范围：0-不需要，1-需要，默认0 。
        :type RemoveVocal: int
        :param _Confirm: 是否需要确认翻译结果0：不需要，1：需要
        :type Confirm: int
        :param _LipSync: 是否开启口型驱动，0：不开启，1：开启。默认开启。
        :type LipSync: int
        :param _VoiceType: 音色种别：一种音色种别对应一种不同区域的音色
1）目标语种为小语种(非zh,en)时，该项为必填
2）目标语种为zh,en时，该项为非必填，若填入，则对应填入的音色

具体音色包含请见“支持音色种别列表”
        :type VoiceType: str
        """
        self._VideoUrl = None
        self._SrcLang = None
        self._DstLang = None
        self._AudioUrl = None
        self._RemoveVocal = None
        self._Confirm = None
        self._LipSync = None
        self._VoiceType = None

    @property
    def VideoUrl(self):
        r"""视频地址URL。
格式要求：支持 mp4、mov 。
时长要求：【10-300】秒。
fps 要求：【15-60】fps
分辨率要求：单边像素要求在 【540~1920】 之间。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def SrcLang(self):
        r"""源语言：zh(中文), en(英文)
        :rtype: str
        """
        return self._SrcLang

    @SrcLang.setter
    def SrcLang(self, SrcLang):
        self._SrcLang = SrcLang

    @property
    def DstLang(self):
        r"""目标语种：
zh(简体中文)、en(英语)、ar(阿拉伯语)、de(德语)、es(西班牙语)、fr(法语)、id(印尼语)、it(意大利语)、ja(日语)、ko(韩语)、ms(马来语)、pt(葡萄牙语)、ru(俄语)、th(泰语)、tr(土耳其语)、vi(越南语)
示例值：ar(阿拉伯语)
        :rtype: str
        """
        return self._DstLang

    @DstLang.setter
    def DstLang(self, DstLang):
        self._DstLang = DstLang

    @property
    def AudioUrl(self):
        r"""当音频 URL 不为空时，默认以音频驱动视频任务口型。
格式要求：支持 mp3、m4a、acc、wav 格式。
时长要求：【10~300】秒
大小要求：不超过 100M。
示例值：http://xxx/audio.mp3
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def RemoveVocal(self):
        r"""是否需要去除VideoUrl或AudioUrl中背景音，取值范围：0-不需要，1-需要，默认0 。
        :rtype: int
        """
        return self._RemoveVocal

    @RemoveVocal.setter
    def RemoveVocal(self, RemoveVocal):
        self._RemoveVocal = RemoveVocal

    @property
    def Confirm(self):
        r"""是否需要确认翻译结果0：不需要，1：需要
        :rtype: int
        """
        return self._Confirm

    @Confirm.setter
    def Confirm(self, Confirm):
        self._Confirm = Confirm

    @property
    def LipSync(self):
        r"""是否开启口型驱动，0：不开启，1：开启。默认开启。
        :rtype: int
        """
        return self._LipSync

    @LipSync.setter
    def LipSync(self, LipSync):
        self._LipSync = LipSync

    @property
    def VoiceType(self):
        r"""音色种别：一种音色种别对应一种不同区域的音色
1）目标语种为小语种(非zh,en)时，该项为必填
2）目标语种为zh,en时，该项为非必填，若填入，则对应填入的音色

具体音色包含请见“支持音色种别列表”
        :rtype: str
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._SrcLang = params.get("SrcLang")
        self._DstLang = params.get("DstLang")
        self._AudioUrl = params.get("AudioUrl")
        self._RemoveVocal = params.get("RemoveVocal")
        self._Confirm = params.get("Confirm")
        self._LipSync = params.get("LipSync")
        self._VoiceType = params.get("VoiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoTranslateJobResponse(AbstractModel):
    r"""SubmitVideoTranslateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频转译任务的Job id
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""视频转译任务的Job id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

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
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class TranslateResult(AbstractModel):
    r"""音频翻译结果。

    """

    def __init__(self):
        r"""
        :param _SourceText: 翻译源文字。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceText: str
        :param _TargetText: 翻译后文字。
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetText: str
        """
        self._SourceText = None
        self._TargetText = None

    @property
    def SourceText(self):
        r"""翻译源文字。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""翻译后文字。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        