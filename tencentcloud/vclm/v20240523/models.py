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


class AsrTimestamps(AbstractModel):
    """文本片段及其时间戳

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
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def StartMs(self):
        return self._StartMs

    @StartMs.setter
    def StartMs(self, StartMs):
        self._StartMs = StartMs

    @property
    def EndMs(self):
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
        


class ConfirmVideoTranslateJobRequest(AbstractModel):
    """ConfirmVideoTranslateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频翻译任务 ID
        :type JobId: str
        :param _TranslateResults: 待确认文本
        :type TranslateResults: list of TranslateResult
        """
        self._JobId = None
        self._TranslateResults = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TranslateResults(self):
        return self._TranslateResults

    @TranslateResults.setter
    def TranslateResults(self, TranslateResults):
        self._TranslateResults = TranslateResults


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        if params.get("TranslateResults") is not None:
            self._TranslateResults = []
            for item in params.get("TranslateResults"):
                obj = TranslateResult()
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
    """ConfirmVideoTranslateJob返回参数结构体

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
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
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


class DescribeImageAnimateJobRequest(AbstractModel):
    """DescribeImageAnimateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
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
        


class DescribeImageAnimateJobResponse(AbstractModel):
    """DescribeImageAnimateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 错误码。
        :type ErrorCode: str
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _MaskVideoUrl: 掩码视频链接
        :type MaskVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._MaskVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def MaskVideoUrl(self):
        return self._MaskVideoUrl

    @MaskVideoUrl.setter
    def MaskVideoUrl(self, MaskVideoUrl):
        self._MaskVideoUrl = MaskVideoUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._MaskVideoUrl = params.get("MaskVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribePortraitSingJobRequest(AbstractModel):
    """DescribePortraitSingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
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
        


class DescribePortraitSingJobResponse(AbstractModel):
    """DescribePortraitSingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _StatusCode: 任务状态码
—RUN：处理中
—FAIL：处理失败
—STOP：处理终止
—DONE：处理完成
        :type StatusCode: str
        :param _StatusMsg: 任务状态信息
        :type StatusMsg: str
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _ErrorMessage: 错误信息
        :type ErrorMessage: str
        :param _ResultVideoUrl: 生成视频的URL地址
有效期24小时
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._StatusCode = None
        self._StatusMsg = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def ErrorCode(self):
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StatusCode = params.get("StatusCode")
        self._StatusMsg = params.get("StatusMsg")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeVideoStylizationJobRequest(AbstractModel):
    """DescribeVideoStylizationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
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
        


class DescribeVideoStylizationJobResponse(AbstractModel):
    """DescribeVideoStylizationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        :param _StatusCode: 任务状态码：
JobInit:  "初始化中"
JobModerationFailed: "审核失败",
JobRunning: "处理中",
JobFailed: "处理失败",
JobSuccess: "处理完成"。
        :type StatusCode: str
        :param _StatusMsg: 任务状态描述。
        :type StatusMsg: str
        :param _ResultVideoUrl: 处理结果视频Url。URL有效期为24小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._StatusCode = None
        self._StatusMsg = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def ResultVideoUrl(self):
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StatusCode = params.get("StatusCode")
        self._StatusMsg = params.get("StatusMsg")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeVideoTranslateJobRequest(AbstractModel):
    """DescribeVideoTranslateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频转译任务 ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
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
    """DescribeVideoTranslateJob返回参数结构体

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
        :param _JobAudioModerationId: 音频审核任务 ID	
        :type JobAudioModerationId: str
        :param _JobVideoId: 口型驱动任务 ID	
        :type JobVideoId: str
        :param _OriginalVideoUrl: 视频素材原始 URL	
        :type OriginalVideoUrl: str
        :param _AsrTimestamps: 文本片段及其时间戳	
        :type AsrTimestamps: list of AsrTimestamps
        :param _JobSubmitReqId: 提交视频翻译任务时的 requestId	
        :type JobSubmitReqId: str
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
        self._JobAudioModerationId = None
        self._JobVideoId = None
        self._OriginalVideoUrl = None
        self._AsrTimestamps = None
        self._JobSubmitReqId = None
        self._RequestId = None

    @property
    def JobStatus(self):
        return self._JobStatus

    @JobStatus.setter
    def JobStatus(self, JobStatus):
        self._JobStatus = JobStatus

    @property
    def JobErrorCode(self):
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultVideoUrl(self):
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def TranslateResults(self):
        return self._TranslateResults

    @TranslateResults.setter
    def TranslateResults(self, TranslateResults):
        self._TranslateResults = TranslateResults

    @property
    def JobConfirm(self):
        return self._JobConfirm

    @JobConfirm.setter
    def JobConfirm(self, JobConfirm):
        self._JobConfirm = JobConfirm

    @property
    def JobAudioTaskId(self):
        return self._JobAudioTaskId

    @JobAudioTaskId.setter
    def JobAudioTaskId(self, JobAudioTaskId):
        self._JobAudioTaskId = JobAudioTaskId

    @property
    def JobVideoModerationId(self):
        return self._JobVideoModerationId

    @JobVideoModerationId.setter
    def JobVideoModerationId(self, JobVideoModerationId):
        self._JobVideoModerationId = JobVideoModerationId

    @property
    def JobAudioModerationId(self):
        return self._JobAudioModerationId

    @JobAudioModerationId.setter
    def JobAudioModerationId(self, JobAudioModerationId):
        self._JobAudioModerationId = JobAudioModerationId

    @property
    def JobVideoId(self):
        return self._JobVideoId

    @JobVideoId.setter
    def JobVideoId(self, JobVideoId):
        self._JobVideoId = JobVideoId

    @property
    def OriginalVideoUrl(self):
        return self._OriginalVideoUrl

    @OriginalVideoUrl.setter
    def OriginalVideoUrl(self, OriginalVideoUrl):
        self._OriginalVideoUrl = OriginalVideoUrl

    @property
    def AsrTimestamps(self):
        return self._AsrTimestamps

    @AsrTimestamps.setter
    def AsrTimestamps(self, AsrTimestamps):
        self._AsrTimestamps = AsrTimestamps

    @property
    def JobSubmitReqId(self):
        return self._JobSubmitReqId

    @JobSubmitReqId.setter
    def JobSubmitReqId(self, JobSubmitReqId):
        self._JobSubmitReqId = JobSubmitReqId

    @property
    def RequestId(self):
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
        self._JobAudioModerationId = params.get("JobAudioModerationId")
        self._JobVideoId = params.get("JobVideoId")
        self._OriginalVideoUrl = params.get("OriginalVideoUrl")
        if params.get("AsrTimestamps") is not None:
            self._AsrTimestamps = []
            for item in params.get("AsrTimestamps"):
                obj = AsrTimestamps()
                obj._deserialize(item)
                self._AsrTimestamps.append(obj)
        self._JobSubmitReqId = params.get("JobSubmitReqId")
        self._RequestId = params.get("RequestId")


class LogoParam(AbstractModel):
    """logo参数

    """

    def __init__(self):
        r"""
        :param _LogoUrl: 水印 Url
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoUrl: str
        :param _LogoImage: 水印 Base64，Url 和 Base64 二选一传入，如果都提供以 Url 为准
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoImage: str
        :param _LogoRect: 水印图片位于生成结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type LogoRect: :class:`tencentcloud.vclm.v20240523.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect


    def _deserialize(self, params):
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        if params.get("LogoRect") is not None:
            self._LogoRect = LogoRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoRect(AbstractModel):
    """输入框

    """

    def __init__(self):
        r"""
        :param _X: 左上角X坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: int
        :param _Y: 左上角Y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: int
        :param _Width: 方框宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _Height: 方框高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageAnimateJobRequest(AbstractModel):
    """SubmitImageAnimateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片格式：支持PNG、JPG、JPEG格式；
图片分辨率：长边分辨率不超过2056；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageUrl: str
        :param _ImageBase64: 图片base64数据。图片格式：支持PNG、JPG、JPEG格式；图片分辨率：长边分辨率不超过2056；图片大小：不超过10M；图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageBase64: str
        :param _TemplateId: 动作模板ID。取值说明：ke3 科目三；tuziwu 兔子舞；huajiangwu 划桨舞。

        :type TemplateId: str
        :param _EnableAudio: 结果视频是否保留模板音频。默认为true
        :type EnableAudio: bool
        :param _EnableBodyJoins: 是否检测输入图人体12个身体部位（头部、颈部、右肩、右肘、右腕、左肩、左肘、左腕、右髋、左髋,、左膝、右膝）。默认不检测。
        :type EnableBodyJoins: bool
        :param _EnableSegment: 最终视频是否保留原图的背景（该模式对于tuziwu、huajiangwu不生效）

        :type EnableSegment: bool
        :param _LogoAdd: 为生成视频添加标识的开关，默认为0。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._TemplateId = None
        self._EnableAudio = None
        self._EnableBodyJoins = None
        self._EnableSegment = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def EnableAudio(self):
        return self._EnableAudio

    @EnableAudio.setter
    def EnableAudio(self, EnableAudio):
        self._EnableAudio = EnableAudio

    @property
    def EnableBodyJoins(self):
        return self._EnableBodyJoins

    @EnableBodyJoins.setter
    def EnableBodyJoins(self, EnableBodyJoins):
        self._EnableBodyJoins = EnableBodyJoins

    @property
    def EnableSegment(self):
        return self._EnableSegment

    @EnableSegment.setter
    def EnableSegment(self, EnableSegment):
        self._EnableSegment = EnableSegment

    @property
    def LogoAdd(self):
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._TemplateId = params.get("TemplateId")
        self._EnableAudio = params.get("EnableAudio")
        self._EnableBodyJoins = params.get("EnableBodyJoins")
        self._EnableSegment = params.get("EnableSegment")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageAnimateJobResponse(AbstractModel):
    """SubmitImageAnimateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitPortraitSingJobRequest(AbstractModel):
    """SubmitPortraitSingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AudioUrl: 传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav、m4a
        :type AudioUrl: str
        :param _ImageUrl: 传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:2到2:1范围内
- 图片内容：避免上传无人脸/宠物脸或脸部过小、不完整、不清晰、偏转角度过大的图片。
        :type ImageUrl: str
        :param _ImageBase64: 传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageBase64为准。
        :type ImageBase64: str
        :param _Mode: 唱演模式，默认使用人像模式。
Person：人像模式，仅支持上传人像图片，人像生成效果更好，如果图中未检测到有效人脸将被拦截，生成时会将视频短边分辨率放缩至512。
Pet：宠物模式，支持宠物等非人像图片，固定生成512:512分辨率视频。
        :type Mode: str
        """
        self._AudioUrl = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._Mode = None

    @property
    def AudioUrl(self):
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._AudioUrl = params.get("AudioUrl")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitPortraitSingJobResponse(AbstractModel):
    """SubmitPortraitSingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoStylizationJobRequest(AbstractModel):
    """SubmitVideoStylizationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StyleId: 风格ID，取值说明：2d_anime 2D动漫；3d_cartoon 3D卡通；3d_china 3D国潮；pixel_art	像素风。
        :type StyleId: str
        :param _VideoUrl: 输入视频URL。视频要求：
- 视频格式：mp4、mov；
- 视频时长：1～60秒；
- 视频分辨率：540P~2056P，即长宽像素数均在540px～2056px范围内；
- 视频大小：不超过200M；
- 视频FPS：15～60fps。
        :type VideoUrl: str
        :param _StyleStrength: 风格化强度 可选参数["low","medium","high"] 
"low":风格化强度弱,"medium":"风格化强度中等","high":"风格化强度强" 
默认为medium
        :type StyleStrength: str
        """
        self._StyleId = None
        self._VideoUrl = None
        self._StyleStrength = None

    @property
    def StyleId(self):
        return self._StyleId

    @StyleId.setter
    def StyleId(self, StyleId):
        self._StyleId = StyleId

    @property
    def VideoUrl(self):
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def StyleStrength(self):
        return self._StyleStrength

    @StyleStrength.setter
    def StyleStrength(self, StyleStrength):
        self._StyleStrength = StyleStrength


    def _deserialize(self, params):
        self._StyleId = params.get("StyleId")
        self._VideoUrl = params.get("VideoUrl")
        self._StyleStrength = params.get("StyleStrength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoStylizationJobResponse(AbstractModel):
    """SubmitVideoStylizationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoTranslateJobRequest(AbstractModel):
    """SubmitVideoTranslateJob请求参数结构体

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
        :type DstLang: str
        :param _AudioUrl: 当音频 URL 不为空时，默认以音频驱动视频任务口型。
格式要求：支持 mp3、m4a、acc、wav 格式。
时长要求：【10~300】秒
大小要求：不超过 100M。
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
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def SrcLang(self):
        return self._SrcLang

    @SrcLang.setter
    def SrcLang(self, SrcLang):
        self._SrcLang = SrcLang

    @property
    def DstLang(self):
        return self._DstLang

    @DstLang.setter
    def DstLang(self, DstLang):
        self._DstLang = DstLang

    @property
    def AudioUrl(self):
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def RemoveVocal(self):
        return self._RemoveVocal

    @RemoveVocal.setter
    def RemoveVocal(self, RemoveVocal):
        self._RemoveVocal = RemoveVocal

    @property
    def Confirm(self):
        return self._Confirm

    @Confirm.setter
    def Confirm(self, Confirm):
        self._Confirm = Confirm

    @property
    def LipSync(self):
        return self._LipSync

    @LipSync.setter
    def LipSync(self, LipSync):
        self._LipSync = LipSync

    @property
    def VoiceType(self):
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
    """SubmitVideoTranslateJob返回参数结构体

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
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class TranslateResult(AbstractModel):
    """音频翻译结果

    """

    def __init__(self):
        r"""
        :param _SourceText: 翻译源文字
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
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
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
        