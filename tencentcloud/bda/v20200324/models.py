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


class CreateSegmentationTaskRequest(AbstractModel):
    r"""CreateSegmentationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 需要分割的视频URL，可外网访问。
        :type VideoUrl: str
        :param _BackgroundImageUrl: 背景图片URL。 
可以将视频背景替换为输入的图片。 
如果不输入背景图片，则输出人像区域mask。
        :type BackgroundImageUrl: str
        :param _Config: 预留字段，后期用于展示更多识别信息。
        :type Config: str
        """
        self._VideoUrl = None
        self._BackgroundImageUrl = None
        self._Config = None

    @property
    def VideoUrl(self):
        r"""需要分割的视频URL，可外网访问。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def BackgroundImageUrl(self):
        r"""背景图片URL。 
可以将视频背景替换为输入的图片。 
如果不输入背景图片，则输出人像区域mask。
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def Config(self):
        r"""预留字段，后期用于展示更多识别信息。
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        self._Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSegmentationTaskResponse(AbstractModel):
    r"""CreateSegmentationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 任务标识ID,可以用与追溯任务状态，查看任务结果
        :type TaskID: str
        :param _EstimatedProcessingTime: 预估处理时间，单位为秒
        :type EstimatedProcessingTime: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskID = None
        self._EstimatedProcessingTime = None
        self._RequestId = None

    @property
    def TaskID(self):
        r"""任务标识ID,可以用与追溯任务状态，查看任务结果
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def EstimatedProcessingTime(self):
        r"""预估处理时间，单位为秒
        :rtype: float
        """
        return self._EstimatedProcessingTime

    @EstimatedProcessingTime.setter
    def EstimatedProcessingTime(self, EstimatedProcessingTime):
        self._EstimatedProcessingTime = EstimatedProcessingTime

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
        self._TaskID = params.get("TaskID")
        self._EstimatedProcessingTime = params.get("EstimatedProcessingTime")
        self._RequestId = params.get("RequestId")


class DescribeSegmentationTaskRequest(AbstractModel):
    r"""DescribeSegmentationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 在提交分割任务成功时返回的任务标识ID。
        :type TaskID: str
        """
        self._TaskID = None

    @property
    def TaskID(self):
        r"""在提交分割任务成功时返回的任务标识ID。
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSegmentationTaskResponse(AbstractModel):
    r"""DescribeSegmentationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 当前任务状态：
QUEUING 排队中
PROCESSING 处理中
FINISHED 处理完成
        :type TaskStatus: str
        :param _ResultVideoUrl: 分割后视频URL, 存储于腾讯云COS
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultVideoUrl: str
        :param _ResultVideoMD5: 分割后视频MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultVideoMD5: str
        :param _VideoBasicInformation: 视频基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoBasicInformation: :class:`tencentcloud.bda.v20200324.models.VideoBasicInformation`
        :param _ErrorMsg: 分割任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._ResultVideoUrl = None
        self._ResultVideoMD5 = None
        self._VideoBasicInformation = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        r"""当前任务状态：
QUEUING 排队中
PROCESSING 处理中
FINISHED 处理完成
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ResultVideoUrl(self):
        r"""分割后视频URL, 存储于腾讯云COS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ResultVideoMD5(self):
        r"""分割后视频MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultVideoMD5

    @ResultVideoMD5.setter
    def ResultVideoMD5(self, ResultVideoMD5):
        self._ResultVideoMD5 = ResultVideoMD5

    @property
    def VideoBasicInformation(self):
        r"""视频基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.bda.v20200324.models.VideoBasicInformation`
        """
        return self._VideoBasicInformation

    @VideoBasicInformation.setter
    def VideoBasicInformation(self, VideoBasicInformation):
        self._VideoBasicInformation = VideoBasicInformation

    @property
    def ErrorMsg(self):
        r"""分割任务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

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
        self._TaskStatus = params.get("TaskStatus")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ResultVideoMD5 = params.get("ResultVideoMD5")
        if params.get("VideoBasicInformation") is not None:
            self._VideoBasicInformation = VideoBasicInformation()
            self._VideoBasicInformation._deserialize(params.get("VideoBasicInformation"))
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class ImageRect(AbstractModel):
    r"""图像坐标信息。

    """

    def __init__(self):
        r"""
        :param _X: 左上角横坐标。
        :type X: int
        :param _Y: 左上角纵坐标。
        :type Y: int
        :param _Width: 人体宽度。
        :type Width: int
        :param _Height: 人体高度。
        :type Height: int
        :param _Label: 分割选项名称。
        :type Label: str
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._Label = None

    @property
    def X(self):
        r"""左上角横坐标。
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""左上角纵坐标。
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""人体宽度。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""人体高度。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Label(self):
        r"""分割选项名称。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentCustomizedPortraitPicRequest(AbstractModel):
    r"""SegmentCustomizedPortraitPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SegmentationOptions: 此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。
        :type SegmentationOptions: :class:`tencentcloud.bda.v20200324.models.SegmentationOptions`
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        """
        self._SegmentationOptions = None
        self._Image = None
        self._Url = None

    @property
    def SegmentationOptions(self):
        r"""此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。
        :rtype: :class:`tencentcloud.bda.v20200324.models.SegmentationOptions`
        """
        return self._SegmentationOptions

    @SegmentationOptions.setter
    def SegmentationOptions(self, SegmentationOptions):
        self._SegmentationOptions = SegmentationOptions

    @property
    def Image(self):
        r"""图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        r"""图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        if params.get("SegmentationOptions") is not None:
            self._SegmentationOptions = SegmentationOptions()
            self._SegmentationOptions._deserialize(params.get("SegmentationOptions"))
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentCustomizedPortraitPicResponse(AbstractModel):
    r"""SegmentCustomizedPortraitPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PortraitImage: 根据指定标签分割输出的透明背景人像图片的 base64 数据。
        :type PortraitImage: str
        :param _MaskImage: 指定标签处理后的Mask。一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）
        :type MaskImage: str
        :param _ImageRects: 坐标信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageRects: list of ImageRect
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PortraitImage = None
        self._MaskImage = None
        self._ImageRects = None
        self._RequestId = None

    @property
    def PortraitImage(self):
        r"""根据指定标签分割输出的透明背景人像图片的 base64 数据。
        :rtype: str
        """
        return self._PortraitImage

    @PortraitImage.setter
    def PortraitImage(self, PortraitImage):
        self._PortraitImage = PortraitImage

    @property
    def MaskImage(self):
        r"""指定标签处理后的Mask。一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）
        :rtype: str
        """
        return self._MaskImage

    @MaskImage.setter
    def MaskImage(self, MaskImage):
        self._MaskImage = MaskImage

    @property
    def ImageRects(self):
        r"""坐标信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageRect
        """
        return self._ImageRects

    @ImageRects.setter
    def ImageRects(self, ImageRects):
        self._ImageRects = ImageRects

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
        self._PortraitImage = params.get("PortraitImage")
        self._MaskImage = params.get("MaskImage")
        if params.get("ImageRects") is not None:
            self._ImageRects = []
            for item in params.get("ImageRects"):
                obj = ImageRect()
                obj._deserialize(item)
                self._ImageRects.append(obj)
        self._RequestId = params.get("RequestId")


class SegmentPortraitPicRequest(AbstractModel):
    r"""SegmentPortraitPic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _RspImgType: 返回图像方式（base64 或 Url ) ，二选一。url有效期为30分钟。
        :type RspImgType: str
        :param _Scene: 适用场景类型。

取值：GEN/GS。GEN为通用场景模式；GS为绿幕场景模式，针对绿幕场景下的人像分割效果更好。
两种模式选择一种传入，默认为GEN。
        :type Scene: str
        """
        self._Image = None
        self._Url = None
        self._RspImgType = None
        self._Scene = None

    @property
    def Image(self):
        r"""图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        r"""图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RspImgType(self):
        r"""返回图像方式（base64 或 Url ) ，二选一。url有效期为30分钟。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def Scene(self):
        r"""适用场景类型。

取值：GEN/GS。GEN为通用场景模式；GS为绿幕场景模式，针对绿幕场景下的人像分割效果更好。
两种模式选择一种传入，默认为GEN。
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._RspImgType = params.get("RspImgType")
        self._Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentPortraitPicResponse(AbstractModel):
    r"""SegmentPortraitPic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 处理后的图片 base64 数据，透明背景图。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultImage: str
        :param _ResultMask: 一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMask: str
        :param _HasForeground: 图片是否存在前景。
注意：此字段可能返回 null，表示取不到有效值。
        :type HasForeground: bool
        :param _ResultImageUrl: 支持将处理过的图片 base64 数据，透明背景图以Url的形式返回值，Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultImageUrl: str
        :param _ResultMaskUrl: 一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。支持以Url形式的返回值；Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultMaskUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._ResultMask = None
        self._HasForeground = None
        self._ResultImageUrl = None
        self._ResultMaskUrl = None
        self._RequestId = None

    @property
    def ResultImage(self):
        r"""处理后的图片 base64 数据，透明背景图。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultMask(self):
        r"""一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultMask

    @ResultMask.setter
    def ResultMask(self, ResultMask):
        self._ResultMask = ResultMask

    @property
    def HasForeground(self):
        r"""图片是否存在前景。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HasForeground

    @HasForeground.setter
    def HasForeground(self, HasForeground):
        self._HasForeground = HasForeground

    @property
    def ResultImageUrl(self):
        r"""支持将处理过的图片 base64 数据，透明背景图以Url的形式返回值，Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultImageUrl

    @ResultImageUrl.setter
    def ResultImageUrl(self, ResultImageUrl):
        self._ResultImageUrl = ResultImageUrl

    @property
    def ResultMaskUrl(self):
        r"""一个通过 base64 编码的文件，解码后文件由 Float 型浮点数组成。支持以Url形式的返回值；Url有效期为30分钟。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultMaskUrl

    @ResultMaskUrl.setter
    def ResultMaskUrl(self, ResultMaskUrl):
        self._ResultMaskUrl = ResultMaskUrl

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
        self._ResultImage = params.get("ResultImage")
        self._ResultMask = params.get("ResultMask")
        self._HasForeground = params.get("HasForeground")
        self._ResultImageUrl = params.get("ResultImageUrl")
        self._ResultMaskUrl = params.get("ResultMaskUrl")
        self._RequestId = params.get("RequestId")


class SegmentationOptions(AbstractModel):
    r"""此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。

    """

    def __init__(self):
        r"""
        :param _Background: 分割选项-背景
        :type Background: bool
        :param _Hair: 分割选项-头发
        :type Hair: bool
        :param _LeftEyebrow: 分割选项-左眉
        :type LeftEyebrow: bool
        :param _RightEyebrow: 分割选项-右眉
        :type RightEyebrow: bool
        :param _LeftEye: 分割选项-左眼
        :type LeftEye: bool
        :param _RightEye: 分割选项-右眼
        :type RightEye: bool
        :param _Nose: 分割选项-鼻子
        :type Nose: bool
        :param _UpperLip: 分割选项-上唇
        :type UpperLip: bool
        :param _LowerLip: 分割选项-下唇
        :type LowerLip: bool
        :param _Tooth: 分割选项-牙齿
        :type Tooth: bool
        :param _Mouth: 分割选项-口腔（不包含牙齿）
        :type Mouth: bool
        :param _LeftEar: 分割选项-左耳
        :type LeftEar: bool
        :param _RightEar: 分割选项-右耳
        :type RightEar: bool
        :param _Face: 分割选项-面部(不包含眼、耳、口、鼻等五官及头发。)
        :type Face: bool
        :param _Head: 复合分割选项-头部(包含所有的头部元素，相关装饰除外)
        :type Head: bool
        :param _Body: 分割选项-身体（包含脖子）
        :type Body: bool
        :param _Hat: 分割选项-帽子
        :type Hat: bool
        :param _Headdress: 分割选项-头饰
        :type Headdress: bool
        :param _Earrings: 分割选项-耳环
        :type Earrings: bool
        :param _Necklace: 分割选项-项链
        :type Necklace: bool
        :param _Belongings: 分割选项-随身物品（ 例如伞、包、手机等。 ）
        :type Belongings: bool
        """
        self._Background = None
        self._Hair = None
        self._LeftEyebrow = None
        self._RightEyebrow = None
        self._LeftEye = None
        self._RightEye = None
        self._Nose = None
        self._UpperLip = None
        self._LowerLip = None
        self._Tooth = None
        self._Mouth = None
        self._LeftEar = None
        self._RightEar = None
        self._Face = None
        self._Head = None
        self._Body = None
        self._Hat = None
        self._Headdress = None
        self._Earrings = None
        self._Necklace = None
        self._Belongings = None

    @property
    def Background(self):
        r"""分割选项-背景
        :rtype: bool
        """
        return self._Background

    @Background.setter
    def Background(self, Background):
        self._Background = Background

    @property
    def Hair(self):
        r"""分割选项-头发
        :rtype: bool
        """
        return self._Hair

    @Hair.setter
    def Hair(self, Hair):
        self._Hair = Hair

    @property
    def LeftEyebrow(self):
        r"""分割选项-左眉
        :rtype: bool
        """
        return self._LeftEyebrow

    @LeftEyebrow.setter
    def LeftEyebrow(self, LeftEyebrow):
        self._LeftEyebrow = LeftEyebrow

    @property
    def RightEyebrow(self):
        r"""分割选项-右眉
        :rtype: bool
        """
        return self._RightEyebrow

    @RightEyebrow.setter
    def RightEyebrow(self, RightEyebrow):
        self._RightEyebrow = RightEyebrow

    @property
    def LeftEye(self):
        r"""分割选项-左眼
        :rtype: bool
        """
        return self._LeftEye

    @LeftEye.setter
    def LeftEye(self, LeftEye):
        self._LeftEye = LeftEye

    @property
    def RightEye(self):
        r"""分割选项-右眼
        :rtype: bool
        """
        return self._RightEye

    @RightEye.setter
    def RightEye(self, RightEye):
        self._RightEye = RightEye

    @property
    def Nose(self):
        r"""分割选项-鼻子
        :rtype: bool
        """
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def UpperLip(self):
        r"""分割选项-上唇
        :rtype: bool
        """
        return self._UpperLip

    @UpperLip.setter
    def UpperLip(self, UpperLip):
        self._UpperLip = UpperLip

    @property
    def LowerLip(self):
        r"""分割选项-下唇
        :rtype: bool
        """
        return self._LowerLip

    @LowerLip.setter
    def LowerLip(self, LowerLip):
        self._LowerLip = LowerLip

    @property
    def Tooth(self):
        r"""分割选项-牙齿
        :rtype: bool
        """
        return self._Tooth

    @Tooth.setter
    def Tooth(self, Tooth):
        self._Tooth = Tooth

    @property
    def Mouth(self):
        r"""分割选项-口腔（不包含牙齿）
        :rtype: bool
        """
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def LeftEar(self):
        r"""分割选项-左耳
        :rtype: bool
        """
        return self._LeftEar

    @LeftEar.setter
    def LeftEar(self, LeftEar):
        self._LeftEar = LeftEar

    @property
    def RightEar(self):
        r"""分割选项-右耳
        :rtype: bool
        """
        return self._RightEar

    @RightEar.setter
    def RightEar(self, RightEar):
        self._RightEar = RightEar

    @property
    def Face(self):
        r"""分割选项-面部(不包含眼、耳、口、鼻等五官及头发。)
        :rtype: bool
        """
        return self._Face

    @Face.setter
    def Face(self, Face):
        self._Face = Face

    @property
    def Head(self):
        r"""复合分割选项-头部(包含所有的头部元素，相关装饰除外)
        :rtype: bool
        """
        return self._Head

    @Head.setter
    def Head(self, Head):
        self._Head = Head

    @property
    def Body(self):
        r"""分割选项-身体（包含脖子）
        :rtype: bool
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Hat(self):
        r"""分割选项-帽子
        :rtype: bool
        """
        return self._Hat

    @Hat.setter
    def Hat(self, Hat):
        self._Hat = Hat

    @property
    def Headdress(self):
        r"""分割选项-头饰
        :rtype: bool
        """
        return self._Headdress

    @Headdress.setter
    def Headdress(self, Headdress):
        self._Headdress = Headdress

    @property
    def Earrings(self):
        r"""分割选项-耳环
        :rtype: bool
        """
        return self._Earrings

    @Earrings.setter
    def Earrings(self, Earrings):
        self._Earrings = Earrings

    @property
    def Necklace(self):
        r"""分割选项-项链
        :rtype: bool
        """
        return self._Necklace

    @Necklace.setter
    def Necklace(self, Necklace):
        self._Necklace = Necklace

    @property
    def Belongings(self):
        r"""分割选项-随身物品（ 例如伞、包、手机等。 ）
        :rtype: bool
        """
        return self._Belongings

    @Belongings.setter
    def Belongings(self, Belongings):
        self._Belongings = Belongings


    def _deserialize(self, params):
        self._Background = params.get("Background")
        self._Hair = params.get("Hair")
        self._LeftEyebrow = params.get("LeftEyebrow")
        self._RightEyebrow = params.get("RightEyebrow")
        self._LeftEye = params.get("LeftEye")
        self._RightEye = params.get("RightEye")
        self._Nose = params.get("Nose")
        self._UpperLip = params.get("UpperLip")
        self._LowerLip = params.get("LowerLip")
        self._Tooth = params.get("Tooth")
        self._Mouth = params.get("Mouth")
        self._LeftEar = params.get("LeftEar")
        self._RightEar = params.get("RightEar")
        self._Face = params.get("Face")
        self._Head = params.get("Head")
        self._Body = params.get("Body")
        self._Hat = params.get("Hat")
        self._Headdress = params.get("Headdress")
        self._Earrings = params.get("Earrings")
        self._Necklace = params.get("Necklace")
        self._Belongings = params.get("Belongings")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateSegmentationTaskRequest(AbstractModel):
    r"""TerminateSegmentationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskID: 在提交分割任务成功时返回的任务标识ID。
        :type TaskID: str
        """
        self._TaskID = None

    @property
    def TaskID(self):
        r"""在提交分割任务成功时返回的任务标识ID。
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateSegmentationTaskResponse(AbstractModel):
    r"""TerminateSegmentationTask返回参数结构体

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


class VideoBasicInformation(AbstractModel):
    r"""视频基础信息

    """

    def __init__(self):
        r"""
        :param _FrameWidth: 视频宽度
        :type FrameWidth: int
        :param _FrameHeight: 视频高度
        :type FrameHeight: int
        :param _FramesPerSecond: 视频帧速率(FPS)
        :type FramesPerSecond: int
        :param _Duration: 视频时长
        :type Duration: float
        :param _TotalFrames: 视频帧数
        :type TotalFrames: int
        """
        self._FrameWidth = None
        self._FrameHeight = None
        self._FramesPerSecond = None
        self._Duration = None
        self._TotalFrames = None

    @property
    def FrameWidth(self):
        r"""视频宽度
        :rtype: int
        """
        return self._FrameWidth

    @FrameWidth.setter
    def FrameWidth(self, FrameWidth):
        self._FrameWidth = FrameWidth

    @property
    def FrameHeight(self):
        r"""视频高度
        :rtype: int
        """
        return self._FrameHeight

    @FrameHeight.setter
    def FrameHeight(self, FrameHeight):
        self._FrameHeight = FrameHeight

    @property
    def FramesPerSecond(self):
        r"""视频帧速率(FPS)
        :rtype: int
        """
        return self._FramesPerSecond

    @FramesPerSecond.setter
    def FramesPerSecond(self, FramesPerSecond):
        self._FramesPerSecond = FramesPerSecond

    @property
    def Duration(self):
        r"""视频时长
        :rtype: float
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def TotalFrames(self):
        r"""视频帧数
        :rtype: int
        """
        return self._TotalFrames

    @TotalFrames.setter
    def TotalFrames(self, TotalFrames):
        self._TotalFrames = TotalFrames


    def _deserialize(self, params):
        self._FrameWidth = params.get("FrameWidth")
        self._FrameHeight = params.get("FrameHeight")
        self._FramesPerSecond = params.get("FramesPerSecond")
        self._Duration = params.get("Duration")
        self._TotalFrames = params.get("TotalFrames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        