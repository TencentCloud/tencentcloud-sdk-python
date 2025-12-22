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


class CheckAnimateImageJobRequest(AbstractModel):
    r"""CheckAnimateImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 动作模板ID。
        :type TemplateId: str
        :param _ImageUrl: 图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageUrl: str
        :param _ImageBase64: 图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageBase64: str
        :param _EnableBodyJoins: 是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :type EnableBodyJoins: bool
        :param _EnableFace: 是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :type EnableFace: bool
        """
        self._TemplateId = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._EnableBodyJoins = None
        self._EnableFace = None

    @property
    def TemplateId(self):
        r"""动作模板ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ImageUrl(self):
        r"""图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def EnableBodyJoins(self):
        r"""是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :rtype: bool
        """
        return self._EnableBodyJoins

    @EnableBodyJoins.setter
    def EnableBodyJoins(self, EnableBodyJoins):
        self._EnableBodyJoins = EnableBodyJoins

    @property
    def EnableFace(self):
        r"""是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :rtype: bool
        """
        return self._EnableFace

    @EnableFace.setter
    def EnableFace(self, EnableFace):
        self._EnableFace = EnableFace


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._EnableBodyJoins = params.get("EnableBodyJoins")
        self._EnableFace = params.get("EnableFace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAnimateImageJobResponse(AbstractModel):
    r"""CheckAnimateImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckPass: 输入图是否通过校验。
        :type CheckPass: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckPass = None
        self._RequestId = None

    @property
    def CheckPass(self):
        r"""输入图是否通过校验。
        :rtype: bool
        """
        return self._CheckPass

    @CheckPass.setter
    def CheckPass(self, CheckPass):
        self._CheckPass = CheckPass

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
        self._CheckPass = params.get("CheckPass")
        self._RequestId = params.get("RequestId")


class DescribeHumanActorJobRequest(AbstractModel):
    r"""DescribeHumanActorJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
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
        


class DescribeHumanActorJobResponse(AbstractModel):
    r"""DescribeHumanActorJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ResultVideoUrl = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class DescribeHunyuanToVideoJobRequest(AbstractModel):
    r"""DescribeHunyuanToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
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
        


class DescribeHunyuanToVideoJobResponse(AbstractModel):
    r"""DescribeHunyuanToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeImageAnimateJobRequest(AbstractModel):
    r"""DescribeImageAnimateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
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
        


class DescribeImageAnimateJobResponse(AbstractModel):
    r"""DescribeImageAnimateJob返回参数结构体

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
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""错误码。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""错误信息。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def MaskVideoUrl(self):
        r"""掩码视频链接
        :rtype: str
        """
        return self._MaskVideoUrl

    @MaskVideoUrl.setter
    def MaskVideoUrl(self, MaskVideoUrl):
        self._MaskVideoUrl = MaskVideoUrl

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._MaskVideoUrl = params.get("MaskVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeImageToVideoGeneralJobRequest(AbstractModel):
    r"""DescribeImageToVideoGeneralJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
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
        


class DescribeImageToVideoGeneralJobResponse(AbstractModel):
    r"""DescribeImageToVideoGeneralJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribePortraitSingJobRequest(AbstractModel):
    r"""DescribePortraitSingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
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
        


class DescribePortraitSingJobResponse(AbstractModel):
    r"""DescribePortraitSingJob返回参数结构体

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
        :param _ErrorCode: 任务执行错误码。当任务状态不为FAIL时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为FAIL时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 生成视频的URL地址。有效期24小时。
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
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StatusCode(self):
        r"""任务状态码
—RUN：处理中
—FAIL：处理失败
—STOP：处理终止
—DONE：处理完成
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMsg(self):
        r"""任务状态信息
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为FAIL时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为FAIL时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""生成视频的URL地址。有效期24小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

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
        self._StatusCode = params.get("StatusCode")
        self._StatusMsg = params.get("StatusMsg")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeTemplateToVideoJobRequest(AbstractModel):
    r"""DescribeTemplateToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
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
        


class DescribeTemplateToVideoJobResponse(AbstractModel):
    r"""DescribeTemplateToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeVideoEditJobRequest(AbstractModel):
    r"""DescribeVideoEditJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
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
        


class DescribeVideoEditJobResponse(AbstractModel):
    r"""DescribeVideoEditJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ResultVideoUrl = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class DescribeVideoFaceFusionJobRequest(AbstractModel):
    r"""DescribeVideoFaceFusionJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
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
        


class DescribeVideoFaceFusionJobResponse(AbstractModel):
    r"""DescribeVideoFaceFusionJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

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
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeVideoStylizationJobRequest(AbstractModel):
    r"""DescribeVideoStylizationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
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
        


class DescribeVideoStylizationJobResponse(AbstractModel):
    r"""DescribeVideoStylizationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        :param _StatusCode: 任务状态码。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
        :type StatusCode: str
        :param _StatusMsg: 任务状态描述。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
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
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StatusCode(self):
        r"""任务状态码。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMsg(self):
        r"""任务状态描述。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def ResultVideoUrl(self):
        r"""处理结果视频Url。URL有效期为24小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

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
        self._StatusCode = params.get("StatusCode")
        self._StatusMsg = params.get("StatusMsg")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeVideoVoiceJobRequest(AbstractModel):
    r"""DescribeVideoVoiceJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
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
        


class DescribeVideoVoiceJobResponse(AbstractModel):
    r"""DescribeVideoVoiceJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ResultVideoUrl = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class ExtraParam(AbstractModel):
    r"""扩展字段。

    """

    def __init__(self):
        r"""
        :param _UserDesignatedUrl: 预签名的上传url，支持把视频直接传到客户指定的地址。
        :type UserDesignatedUrl: str
        """
        self._UserDesignatedUrl = None

    @property
    def UserDesignatedUrl(self):
        r"""预签名的上传url，支持把视频直接传到客户指定的地址。
        :rtype: str
        """
        return self._UserDesignatedUrl

    @UserDesignatedUrl.setter
    def UserDesignatedUrl(self, UserDesignatedUrl):
        self._UserDesignatedUrl = UserDesignatedUrl


    def _deserialize(self, params):
        self._UserDesignatedUrl = params.get("UserDesignatedUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceMergeInfo(AbstractModel):
    r"""人脸图片和待被融合的素材模板图的人脸位置信息。

    """

    def __init__(self):
        r"""
        :param _MergeFaceImage: 融合图片
        :type MergeFaceImage: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _MergeFaceRect: 上传的图片人脸位置信息（人脸框）
Width、Height >= 30。
        :type MergeFaceRect: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        :param _TemplateFaceID: 素材人脸ID，不填默认取上传图片中最大人脸。
        :type TemplateFaceID: str
        """
        self._MergeFaceImage = None
        self._MergeFaceRect = None
        self._TemplateFaceID = None

    @property
    def MergeFaceImage(self):
        r"""融合图片
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._MergeFaceImage

    @MergeFaceImage.setter
    def MergeFaceImage(self, MergeFaceImage):
        self._MergeFaceImage = MergeFaceImage

    @property
    def MergeFaceRect(self):
        r"""上传的图片人脸位置信息（人脸框）
Width、Height >= 30。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        """
        return self._MergeFaceRect

    @MergeFaceRect.setter
    def MergeFaceRect(self, MergeFaceRect):
        self._MergeFaceRect = MergeFaceRect

    @property
    def TemplateFaceID(self):
        r"""素材人脸ID，不填默认取上传图片中最大人脸。
        :rtype: str
        """
        return self._TemplateFaceID

    @TemplateFaceID.setter
    def TemplateFaceID(self, TemplateFaceID):
        self._TemplateFaceID = TemplateFaceID


    def _deserialize(self, params):
        if params.get("MergeFaceImage") is not None:
            self._MergeFaceImage = Image()
            self._MergeFaceImage._deserialize(params.get("MergeFaceImage"))
        if params.get("MergeFaceRect") is not None:
            self._MergeFaceRect = FaceRect()
            self._MergeFaceRect._deserialize(params.get("MergeFaceRect"))
        self._TemplateFaceID = params.get("TemplateFaceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    r"""人脸框信息。

    """

    def __init__(self):
        r"""
        :param _X: 人脸框左上角横坐标。
        :type X: int
        :param _Y: 人脸框左上角纵坐标。
        :type Y: int
        :param _Width: 人脸框宽度。
        :type Width: int
        :param _Height: 人脸框高度。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""人脸框左上角横坐标。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""人脸框左上角纵坐标。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""人脸框宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""人脸框高度。
        :rtype: int
        """
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
        


class FaceTemplateInfo(AbstractModel):
    r"""模板信息

    """

    def __init__(self):
        r"""
        :param _TemplateFaceID: 角色ID。需要与MergeInfos中的TemplateFaceID依次对应。需要填数字，建议填"0"、"1"，依次累加。
        :type TemplateFaceID: str
        :param _TemplateFaceImage: 视频模板中要替换的人脸图片
        :type TemplateFaceImage: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _TemplateFaceRect: 视频模板中要替换的人脸图片的人脸框。不填默认取要替换的人脸图片中最大人脸。
        :type TemplateFaceRect: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        """
        self._TemplateFaceID = None
        self._TemplateFaceImage = None
        self._TemplateFaceRect = None

    @property
    def TemplateFaceID(self):
        r"""角色ID。需要与MergeInfos中的TemplateFaceID依次对应。需要填数字，建议填"0"、"1"，依次累加。
        :rtype: str
        """
        return self._TemplateFaceID

    @TemplateFaceID.setter
    def TemplateFaceID(self, TemplateFaceID):
        self._TemplateFaceID = TemplateFaceID

    @property
    def TemplateFaceImage(self):
        r"""视频模板中要替换的人脸图片
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._TemplateFaceImage

    @TemplateFaceImage.setter
    def TemplateFaceImage(self, TemplateFaceImage):
        self._TemplateFaceImage = TemplateFaceImage

    @property
    def TemplateFaceRect(self):
        r"""视频模板中要替换的人脸图片的人脸框。不填默认取要替换的人脸图片中最大人脸。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        """
        return self._TemplateFaceRect

    @TemplateFaceRect.setter
    def TemplateFaceRect(self, TemplateFaceRect):
        self._TemplateFaceRect = TemplateFaceRect


    def _deserialize(self, params):
        self._TemplateFaceID = params.get("TemplateFaceID")
        if params.get("TemplateFaceImage") is not None:
            self._TemplateFaceImage = Image()
            self._TemplateFaceImage._deserialize(params.get("TemplateFaceImage"))
        if params.get("TemplateFaceRect") is not None:
            self._TemplateFaceRect = FaceRect()
            self._TemplateFaceRect._deserialize(params.get("TemplateFaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    r"""图片

    """

    def __init__(self):
        r"""
        :param _Base64: 图片Base64
        :type Base64: str
        :param _Url: 图片Url
        :type Url: str
        """
        self._Base64 = None
        self._Url = None

    @property
    def Base64(self):
        r"""图片Base64
        :rtype: str
        """
        return self._Base64

    @Base64.setter
    def Base64(self, Base64):
        self._Base64 = Base64

    @property
    def Url(self):
        r"""图片Url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Base64 = params.get("Base64")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoParam(AbstractModel):
    r"""logo参数

    """

    def __init__(self):
        r"""
        :param _LogoUrl: 水印 Url
        :type LogoUrl: str
        :param _LogoImage: 水印 Base64，Url 和 Base64 二选一传入，如果都提供以 Url 为准
        :type LogoImage: str
        :param _LogoRect: 水印图片位于生成结果图中的坐标及宽高，将按照坐标对标识图片进行位置和大小的拉伸匹配。
        :type LogoRect: :class:`tencentcloud.vclm.v20240523.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        r"""水印 Url
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        r"""水印 Base64，Url 和 Base64 二选一传入，如果都提供以 Url 为准
        :rtype: str
        """
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        r"""水印图片位于生成结果图中的坐标及宽高，将按照坐标对标识图片进行位置和大小的拉伸匹配。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoRect`
        """
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
    r"""水印图输入框

    """

    def __init__(self):
        r"""
        :param _X: 水印图框X坐标值。当值大于0时，坐标轴原点位于原图左侧，方向指右；当值小于0时，坐标轴原点位于原图右侧，方向指左。
        :type X: int
        :param _Y: 水印图框Y坐标值。当值大于0时，坐标轴原点位于原图上侧，方向指下；当值小于0时，坐标轴原点位于原图下侧，方向指上。
        :type Y: int
        :param _Width: 水印图框宽度。
        :type Width: int
        :param _Height: 水印图框高度。
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""水印图框X坐标值。当值大于0时，坐标轴原点位于原图左侧，方向指右；当值小于0时，坐标轴原点位于原图右侧，方向指左。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""水印图框Y坐标值。当值大于0时，坐标轴原点位于原图上侧，方向指下；当值小于0时，坐标轴原点位于原图下侧，方向指上。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""水印图框宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""水印图框高度。
        :rtype: int
        """
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
        


class SubmitHumanActorJobRequest(AbstractModel):
    r"""SubmitHumanActorJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本提示词，不能超过5000字符。
提示词支持全局和局部控制：

- 全局控制：正常输入提示词即可
- 局部控制：可用双井号进行特定时间的提示词约束，例如： "画面中的人物正在对着镜头讲话，偶尔做些手势匹配说话的内容。镜头保持固定。#3#画面中的人物正在对着镜头讲话，同时做出单手做向左方引导的手势。镜头保持固定。"（意思是第三秒的时候让人物做出左方引导手势）
 -- 局部控制时间建议整数，最大可读小数点后两位。
        :type Prompt: str
        :param _AudioUrl: 传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav
- 音频大小：10M以内
        :type AudioUrl: str
        :param _ImageUrl: 传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:4到4:1范围内
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :type ImageUrl: str
        :param _ImageBase64: 传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageUrl为准。
        :type ImageBase64: str
        :param _Resolution: 生成视频分辨率
枚举值：720p，1080p
默认1080p
        :type Resolution: str
        :param _FrameRate: 生成视频帧数，单位fps。
枚举值：25，50
默认50帧
        :type FrameRate: int
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Prompt = None
        self._AudioUrl = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._Resolution = None
        self._FrameRate = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        r"""文本提示词，不能超过5000字符。
提示词支持全局和局部控制：

- 全局控制：正常输入提示词即可
- 局部控制：可用双井号进行特定时间的提示词约束，例如： "画面中的人物正在对着镜头讲话，偶尔做些手势匹配说话的内容。镜头保持固定。#3#画面中的人物正在对着镜头讲话，同时做出单手做向左方引导的手势。镜头保持固定。"（意思是第三秒的时候让人物做出左方引导手势）
 -- 局部控制时间建议整数，最大可读小数点后两位。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def AudioUrl(self):
        r"""传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav
- 音频大小：10M以内
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def ImageUrl(self):
        r"""传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:4到4:1范围内
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageUrl为准。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Resolution(self):
        r"""生成视频分辨率
枚举值：720p，1080p
默认1080p
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def FrameRate(self):
        r"""生成视频帧数，单位fps。
枚举值：25，50
默认50帧
        :rtype: int
        """
        return self._FrameRate

    @FrameRate.setter
    def FrameRate(self, FrameRate):
        self._FrameRate = FrameRate

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._AudioUrl = params.get("AudioUrl")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._Resolution = params.get("Resolution")
        self._FrameRate = params.get("FrameRate")
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
        


class SubmitHumanActorJobResponse(AbstractModel):
    r"""SubmitHumanActorJob返回参数结构体

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
        r"""任务ID。
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


class SubmitHunyuanToVideoJobRequest(AbstractModel):
    r"""SubmitHunyuanToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。 示例值：一只猫在草原上奔跑，写实风格
        :type Prompt: str
        :param _Image: 输入图片
上传图url大小不超过 10M，base64不超过8M。
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :type Image: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _Resolution: 目前仅支持720p视频分辨率，默认720p。
        :type Resolution: str
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。
 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。
        :type LogoAdd: int
        :param _LogoParam: 默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Prompt = None
        self._Image = None
        self._Resolution = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        r"""视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。 示例值：一只猫在草原上奔跑，写实风格
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Image(self):
        r"""输入图片
上传图url大小不超过 10M，base64不超过8M。
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Resolution(self):
        r"""目前仅支持720p视频分辨率，默认720p。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。
 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        self._Resolution = params.get("Resolution")
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
        


class SubmitHunyuanToVideoJobResponse(AbstractModel):
    r"""SubmitHunyuanToVideoJob返回参数结构体

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
        r"""任务ID
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


class SubmitImageAnimateJobRequest(AbstractModel):
    r"""SubmitImageAnimateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageUrl: str
        :param _ImageBase64: 图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageBase64: str
        :param _TemplateId: 动作模板ID。取值说明：ke3 科目三；tuziwu 兔子舞；huajiangwu 划桨舞。

        :type TemplateId: str
        :param _EnableAudio: 结果视频是否保留模板音频。默认为true
        :type EnableAudio: bool
        :param _EnableBodyJoins: 是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :type EnableBodyJoins: bool
        :param _EnableSegment: 是否对结果视频背景进行分割，默认值为false。
true：分割结果视频，结果视频（ResultVideoUrl）将为去除背景的绿幕视频，并返回掩码视频（MaskVideoUrl）；
false：不分割结果视频，结果视频（ResultVideoUrl）为带背景的视频，掩码视频（MaskVideoUrl）为空字符串。
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
        :param _EnableFace: 是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :type EnableFace: bool
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._TemplateId = None
        self._EnableAudio = None
        self._EnableBodyJoins = None
        self._EnableSegment = None
        self._LogoAdd = None
        self._LogoParam = None
        self._EnableFace = None

    @property
    def ImageUrl(self):
        r"""图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def TemplateId(self):
        r"""动作模板ID。取值说明：ke3 科目三；tuziwu 兔子舞；huajiangwu 划桨舞。

        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def EnableAudio(self):
        r"""结果视频是否保留模板音频。默认为true
        :rtype: bool
        """
        return self._EnableAudio

    @EnableAudio.setter
    def EnableAudio(self, EnableAudio):
        self._EnableAudio = EnableAudio

    @property
    def EnableBodyJoins(self):
        r"""是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :rtype: bool
        """
        return self._EnableBodyJoins

    @EnableBodyJoins.setter
    def EnableBodyJoins(self, EnableBodyJoins):
        self._EnableBodyJoins = EnableBodyJoins

    @property
    def EnableSegment(self):
        r"""是否对结果视频背景进行分割，默认值为false。
true：分割结果视频，结果视频（ResultVideoUrl）将为去除背景的绿幕视频，并返回掩码视频（MaskVideoUrl）；
false：不分割结果视频，结果视频（ResultVideoUrl）为带背景的视频，掩码视频（MaskVideoUrl）为空字符串。
        :rtype: bool
        """
        return self._EnableSegment

    @EnableSegment.setter
    def EnableSegment(self, EnableSegment):
        self._EnableSegment = EnableSegment

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为0。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。
默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def EnableFace(self):
        r"""是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :rtype: bool
        """
        return self._EnableFace

    @EnableFace.setter
    def EnableFace(self, EnableFace):
        self._EnableFace = EnableFace


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
        self._EnableFace = params.get("EnableFace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageAnimateJobResponse(AbstractModel):
    r"""SubmitImageAnimateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 图片跳舞任务ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""图片跳舞任务ID。
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


class SubmitImageToVideoGeneralJobRequest(AbstractModel):
    r"""SubmitImageToVideoGeneralJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 输入图片
Base64 和 Url 必须提供一个，如果都提供以ImageUrl为准。
上传图url大小不超过 8M
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :type Image: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _Prompt: 视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。
        :type Prompt: str
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。  1：添加标识；  0：不添加标识；  其他数值：默认按1处理。
        :type LogoAdd: int
        :param _LogoParam: 默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Image = None
        self._Prompt = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Image(self):
        r"""输入图片
Base64 和 Url 必须提供一个，如果都提供以ImageUrl为准。
上传图url大小不超过 8M
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Prompt(self):
        r"""视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。  1：添加标识；  0：不添加标识；  其他数值：默认按1处理。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        self._Prompt = params.get("Prompt")
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
        


class SubmitImageToVideoGeneralJobResponse(AbstractModel):
    r"""SubmitImageToVideoGeneralJob返回参数结构体

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
        r"""任务ID
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


class SubmitPortraitSingJobRequest(AbstractModel):
    r"""SubmitPortraitSingJob请求参数结构体

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
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :type ImageUrl: str
        :param _ImageBase64: 传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageBase64为准。
        :type ImageBase64: str
        :param _Mode: 唱演模式，默认使用人像模式。
Person：人像模式，仅支持上传人像图片，人像生成效果更好，如果图中未检测到有效人脸将被拦截，生成时会将视频短边分辨率放缩至512。
Pet：宠物模式，支持宠物等非人像图片，固定生成512:512分辨率视频。
        :type Mode: str
        :param _Resolution: 生成视频尺寸。可选取值："512:512"。

人像模式下，如果不传该参数，默认生成视频的短边分辨率为512，长边分辨率不固定、由模型根据生成效果自动适配得到。如需固定生成分辨率可传入512:512。

宠物模式下，如果不传该参数，默认将脸部唱演视频回贴原图，生成视频分辨率与原图一致。如不需要脸部回贴，仅保留脸部唱演视频，可传入512:512。
        :type Resolution: str
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 
1：添加标识；
 0：不添加标识；
其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._AudioUrl = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._Mode = None
        self._Resolution = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def AudioUrl(self):
        r"""传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav、m4a
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def ImageUrl(self):
        r"""传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:2到2:1范围内
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageBase64为准。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Mode(self):
        r"""唱演模式，默认使用人像模式。
Person：人像模式，仅支持上传人像图片，人像生成效果更好，如果图中未检测到有效人脸将被拦截，生成时会将视频短边分辨率放缩至512。
Pet：宠物模式，支持宠物等非人像图片，固定生成512:512分辨率视频。
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Resolution(self):
        r"""生成视频尺寸。可选取值："512:512"。

人像模式下，如果不传该参数，默认生成视频的短边分辨率为512，长边分辨率不固定、由模型根据生成效果自动适配得到。如需固定生成分辨率可传入512:512。

宠物模式下，如果不传该参数，默认将脸部唱演视频回贴原图，生成视频分辨率与原图一致。如不需要脸部回贴，仅保留脸部唱演视频，可传入512:512。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 
1：添加标识；
 0：不添加标识；
其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._AudioUrl = params.get("AudioUrl")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._Mode = params.get("Mode")
        self._Resolution = params.get("Resolution")
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
        


class SubmitPortraitSingJobResponse(AbstractModel):
    r"""SubmitPortraitSingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。任务有效期为48小时。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID。任务有效期为48小时。
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


class SubmitTemplateToVideoJobRequest(AbstractModel):
    r"""SubmitTemplateToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: 特效模板名称。请在 [视频特效模板列表](https://cloud.tencent.com/document/product/1616/119194)  中选择想要生成的特效对应的 template 名称。
        :type Template: str
        :param _Images: 参考图像，不同特效输入图片的数量详见： [视频特效模板-图片要求说明](https://cloud.tencent.com/document/product/1616/119194)
- 支持传入图片Base64编码或图片URL（确保可访问）
- 图片格式：支持png、jpg、jpeg、webp、bmp、tiff
- 图片文件：大小不能超过10MB（base64后），图片分辨率不小于300*300px，不大于4096*4096，图片宽高比应在1:4 ~ 4:1之间
        :type Images: list of Image
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。传0 需前往  [控制台](https://console.cloud.tencent.com/vtc/setting) 申请开启显式标识自主完成后方可生效。
1：添加标识；
0：不添加标识；
其他数值：默认按1处理。
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往  [控制台](https://console.cloud.tencent.com/vtc/setting) 申请开启显式标识自主完成。

        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        :param _Resolution: 视频输出分辨率，默认值：360p 。不同特效支持的清晰度及消耗积分数详见：[视频特效模板-单次调用消耗积分数列](https://cloud.tencent.com/document/product/1616/119194 )
        :type Resolution: str
        :param _BGM: 是否为生成的视频添加背景音乐。默认：false，  传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。
        :type BGM: bool
        :param _ExtraParam: 扩展字段。
        :type ExtraParam: :class:`tencentcloud.vclm.v20240523.models.ExtraParam`
        """
        self._Template = None
        self._Images = None
        self._LogoAdd = None
        self._LogoParam = None
        self._Resolution = None
        self._BGM = None
        self._ExtraParam = None

    @property
    def Template(self):
        r"""特效模板名称。请在 [视频特效模板列表](https://cloud.tencent.com/document/product/1616/119194)  中选择想要生成的特效对应的 template 名称。
        :rtype: str
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Images(self):
        r"""参考图像，不同特效输入图片的数量详见： [视频特效模板-图片要求说明](https://cloud.tencent.com/document/product/1616/119194)
- 支持传入图片Base64编码或图片URL（确保可访问）
- 图片格式：支持png、jpg、jpeg、webp、bmp、tiff
- 图片文件：大小不能超过10MB（base64后），图片分辨率不小于300*300px，不大于4096*4096，图片宽高比应在1:4 ~ 4:1之间
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。传0 需前往  [控制台](https://console.cloud.tencent.com/vtc/setting) 申请开启显式标识自主完成后方可生效。
1：添加标识；
0：不添加标识；
其他数值：默认按1处理。
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。
默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往  [控制台](https://console.cloud.tencent.com/vtc/setting) 申请开启显式标识自主完成。

        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Resolution(self):
        r"""视频输出分辨率，默认值：360p 。不同特效支持的清晰度及消耗积分数详见：[视频特效模板-单次调用消耗积分数列](https://cloud.tencent.com/document/product/1616/119194 )
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def BGM(self):
        r"""是否为生成的视频添加背景音乐。默认：false，  传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。
        :rtype: bool
        """
        return self._BGM

    @BGM.setter
    def BGM(self, BGM):
        self._BGM = BGM

    @property
    def ExtraParam(self):
        r"""扩展字段。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.ExtraParam`
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam


    def _deserialize(self, params):
        self._Template = params.get("Template")
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._Resolution = params.get("Resolution")
        self._BGM = params.get("BGM")
        if params.get("ExtraParam") is not None:
            self._ExtraParam = ExtraParam()
            self._ExtraParam._deserialize(params.get("ExtraParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTemplateToVideoJobResponse(AbstractModel):
    r"""SubmitTemplateToVideoJob返回参数结构体

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
        r"""任务ID。
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


class SubmitVideoEditJobRequest(AbstractModel):
    r"""SubmitVideoEditJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 输入视频

- 视频格式：MP4
- 视频时长：5s以内
- 视频分辨率：无限制（待验证是否可以无损输出）
        :type VideoUrl: str
        :param _Prompt: 视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。
支持风格迁移、替换、元素增加、删除控制
        :type Prompt: str
        :param _Image: 图片base64或者图片url

- Base64 和 Url 必须提供一个，如果都提供以Url为准。
- 上传图url大小不超过 8M
- 支持jpg，png，jpeg，webp，bmp，tiff 格式
- 单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :type Image: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._VideoUrl = None
        self._Prompt = None
        self._Image = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def VideoUrl(self):
        r"""输入视频

- 视频格式：MP4
- 视频时长：5s以内
- 视频分辨率：无限制（待验证是否可以无损输出）
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def Prompt(self):
        r"""视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。
支持风格迁移、替换、元素增加、删除控制
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Image(self):
        r"""图片base64或者图片url

- Base64 和 Url 必须提供一个，如果都提供以Url为准。
- 上传图url大小不超过 8M
- 支持jpg，png，jpeg，webp，bmp，tiff 格式
- 单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._Prompt = params.get("Prompt")
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
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
        


class SubmitVideoEditJobResponse(AbstractModel):
    r"""SubmitVideoEditJob返回参数结构体

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
        r"""任务ID。
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


class SubmitVideoFaceFusionJobRequest(AbstractModel):
    r"""SubmitVideoFaceFusionJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 视频素材下载地址。用户自定义模版视频下载地址，使用前需要先调用视频审核接口进行内容审核。视频限制：分辨率≤4k，fps≤25，视频大小≤1G，时长≤20 秒，支持格式mp4。

输入视频建议：
姿态：人脸相对镜头水平方向角度转动不超过 90°,垂直方向角度转动不超过 20°。遮挡：脸部遮挡面积不超过 50%，不要完全遮挡五官，不要有半透明遮挡（强光，玻璃，透明眼镜等）、以及细碎离散的脸部遮挡（如飘落的花瓣）。妆容及光照：避免浓妆、复杂妆容，避免复杂光照、闪烁，这些属性无法完全恢复，并对稳定性有影响。针对特殊表情和微表情，针对局部肌肉控制下的微表情，以及过于夸张的特殊表情等不保证表情效果完全恢复。
        :type VideoUrl: str
        :param _TemplateInfos: 视频素材模板的人脸位置信息。
目前最多支持融合视频素材中的 6 张人脸  
输入图片要求：  
1、用户图限制大小不超过 10MB  
2、图片最大分辨率不超过 4k，建议最小为 128，  人脸框最小为 68
3、支持格式 jpg，png  
4、如果用户图中未指定人脸且有多张人脸，  默认融合最大人脸  
输入图片建议：  包含上述视频中出现的人物的单人照，并且正面、清晰、无遮挡
        :type TemplateInfos: list of FaceTemplateInfo
        :param _MergeInfos: 用户人脸图片位置信息。
输入图片要求：
1、用户图限制大小不超过 10MB
2、图片最大分辨率不超过 4k，建议最小为 128，人脸框最小为 68
3、支持格式 jpg，png
4、如果未指定人脸且用户图中有多张人脸，
默认融合最大人脸
输入图建议：
正脸无遮挡
        :type MergeInfos: list of FaceMergeInfo
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 
1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 视频水印Logo参数标识内容设置。   
默认在融合结果图右下角添加“AI生成”类似字样，您可根据自身需要替换为其他的Logo图片。   
输入建议：输入水印图片宽高需小于视频宽高
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._VideoUrl = None
        self._TemplateInfos = None
        self._MergeInfos = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def VideoUrl(self):
        r"""视频素材下载地址。用户自定义模版视频下载地址，使用前需要先调用视频审核接口进行内容审核。视频限制：分辨率≤4k，fps≤25，视频大小≤1G，时长≤20 秒，支持格式mp4。

输入视频建议：
姿态：人脸相对镜头水平方向角度转动不超过 90°,垂直方向角度转动不超过 20°。遮挡：脸部遮挡面积不超过 50%，不要完全遮挡五官，不要有半透明遮挡（强光，玻璃，透明眼镜等）、以及细碎离散的脸部遮挡（如飘落的花瓣）。妆容及光照：避免浓妆、复杂妆容，避免复杂光照、闪烁，这些属性无法完全恢复，并对稳定性有影响。针对特殊表情和微表情，针对局部肌肉控制下的微表情，以及过于夸张的特殊表情等不保证表情效果完全恢复。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def TemplateInfos(self):
        r"""视频素材模板的人脸位置信息。
目前最多支持融合视频素材中的 6 张人脸  
输入图片要求：  
1、用户图限制大小不超过 10MB  
2、图片最大分辨率不超过 4k，建议最小为 128，  人脸框最小为 68
3、支持格式 jpg，png  
4、如果用户图中未指定人脸且有多张人脸，  默认融合最大人脸  
输入图片建议：  包含上述视频中出现的人物的单人照，并且正面、清晰、无遮挡
        :rtype: list of FaceTemplateInfo
        """
        return self._TemplateInfos

    @TemplateInfos.setter
    def TemplateInfos(self, TemplateInfos):
        self._TemplateInfos = TemplateInfos

    @property
    def MergeInfos(self):
        r"""用户人脸图片位置信息。
输入图片要求：
1、用户图限制大小不超过 10MB
2、图片最大分辨率不超过 4k，建议最小为 128，人脸框最小为 68
3、支持格式 jpg，png
4、如果未指定人脸且用户图中有多张人脸，
默认融合最大人脸
输入图建议：
正脸无遮挡
        :rtype: list of FaceMergeInfo
        """
        return self._MergeInfos

    @MergeInfos.setter
    def MergeInfos(self, MergeInfos):
        self._MergeInfos = MergeInfos

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 
1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""视频水印Logo参数标识内容设置。   
默认在融合结果图右下角添加“AI生成”类似字样，您可根据自身需要替换为其他的Logo图片。   
输入建议：输入水印图片宽高需小于视频宽高
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        if params.get("TemplateInfos") is not None:
            self._TemplateInfos = []
            for item in params.get("TemplateInfos"):
                obj = FaceTemplateInfo()
                obj._deserialize(item)
                self._TemplateInfos.append(obj)
        if params.get("MergeInfos") is not None:
            self._MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = FaceMergeInfo()
                obj._deserialize(item)
                self._MergeInfos.append(obj)
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
        


class SubmitVideoFaceFusionJobResponse(AbstractModel):
    r"""SubmitVideoFaceFusionJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频人脸融合任务的job id（job有效期24小时）
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""视频人脸融合任务的job id（job有效期24小时）
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


class SubmitVideoStylizationJobRequest(AbstractModel):
    r"""SubmitVideoStylizationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StyleId: 风格ID。取值说明：
2d_anime：2D动漫；
3d_cartoon：3D卡通；
3d_china：3D国潮；
pixel_art：像素风。
        :type StyleId: str
        :param _VideoUrl: 输入视频URL。视频要求：
- 视频格式：mp4、mov；
- 视频时长：1～60秒；
- 视频分辨率：540P~2056P，即长宽像素数均在540px～2056px范围内；
- 视频大小：不超过200M；
- 视频FPS：15～60fps。
        :type VideoUrl: str
        :param _StyleStrength: 风格化强度。取值说明：
low：风格化强度弱；
medium：风格化强度中等；
high：风格化强度强。
默认值为medium。
        :type StyleStrength: str
        """
        self._StyleId = None
        self._VideoUrl = None
        self._StyleStrength = None

    @property
    def StyleId(self):
        r"""风格ID。取值说明：
2d_anime：2D动漫；
3d_cartoon：3D卡通；
3d_china：3D国潮；
pixel_art：像素风。
        :rtype: str
        """
        return self._StyleId

    @StyleId.setter
    def StyleId(self, StyleId):
        self._StyleId = StyleId

    @property
    def VideoUrl(self):
        r"""输入视频URL。视频要求：
- 视频格式：mp4、mov；
- 视频时长：1～60秒；
- 视频分辨率：540P~2056P，即长宽像素数均在540px～2056px范围内；
- 视频大小：不超过200M；
- 视频FPS：15～60fps。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def StyleStrength(self):
        r"""风格化强度。取值说明：
low：风格化强度弱；
medium：风格化强度中等；
high：风格化强度强。
默认值为medium。
        :rtype: str
        """
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
    r"""SubmitVideoStylizationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。任务有效期为48小时。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID。任务有效期为48小时。
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


class SubmitVideoVoiceJobRequest(AbstractModel):
    r"""SubmitVideoVoiceJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 输入视频的Url  上传视频时长限制：1-15s 视频格式：MP4，MOV 视频大小：不超过1 GB URL地址中不能包含中文字符。
        :type VideoUrl: str
        :param _Prompt: 描述音效内容的正向提示词。输入上限50个字符。
        :type Prompt: str
        :param _NegativePrompt: 音效内容的原始负向提示词。输入上限50个字符。
        :type NegativePrompt: str
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._VideoUrl = None
        self._Prompt = None
        self._NegativePrompt = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def VideoUrl(self):
        r"""输入视频的Url  上传视频时长限制：1-15s 视频格式：MP4，MOV 视频大小：不超过1 GB URL地址中不能包含中文字符。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def Prompt(self):
        r"""描述音效内容的正向提示词。输入上限50个字符。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        r"""音效内容的原始负向提示词。输入上限50个字符。
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
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
        


class SubmitVideoVoiceJobResponse(AbstractModel):
    r"""SubmitVideoVoiceJob返回参数结构体

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
        r"""任务ID。
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