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


class AgeInfo(AbstractModel):
    """人脸变年龄信息

    """

    def __init__(self):
        """
        :param Age: 变化到的人脸年龄 [10,80]。
        :type Age: int
        :param FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.ft.v20200304.models.FaceRect`
        """
        self.Age = None
        self.FaceRect = None


    def _deserialize(self, params):
        self.Age = params.get("Age")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))


class ChangeAgePicRequest(AbstractModel):
    """ChangeAgePic请求参数结构体

    """

    def __init__(self):
        """
        :param AgeInfos: 人脸变老变年轻信息。 
您可以输入最多3个 AgeInfo 来实现给一张图中的最多3张人脸变老变年轻。
        :type AgeInfos: list of AgeInfo
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self.AgeInfos = None
        self.Image = None
        self.Url = None
        self.RspImgType = None


    def _deserialize(self, params):
        if params.get("AgeInfos") is not None:
            self.AgeInfos = []
            for item in params.get("AgeInfos"):
                obj = AgeInfo()
                obj._deserialize(item)
                self.AgeInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.RspImgType = params.get("RspImgType")


class ChangeAgePicResponse(AbstractModel):
    """ChangeAgePic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :type ResultImage: str
        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
        :type ResultUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人脸框位置

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。
        :type X: int
        :param Y: 人脸框左上角纵坐标。
        :type Y: int
        :param Width: 人脸框宽度。
        :type Width: int
        :param Height: 人脸框高度。
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class GenderInfo(AbstractModel):
    """人脸转换性别信息

    """

    def __init__(self):
        """
        :param Gender: 选择转换方向，0：男变女，1：女变男。
        :type Gender: int
        :param FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。
        :type FaceRect: :class:`tencentcloud.ft.v20200304.models.FaceRect`
        """
        self.Gender = None
        self.FaceRect = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))


class SwapGenderPicRequest(AbstractModel):
    """SwapGenderPic请求参数结构体

    """

    def __init__(self):
        """
        :param GenderInfos: 人脸转化性别信息。 
您可以输入最多3个 GenderInfo 来实现给一张图中的最多3张人脸转换性别。
        :type GenderInfos: list of GenderInfo
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。
        :type RspImgType: str
        """
        self.GenderInfos = None
        self.Image = None
        self.Url = None
        self.RspImgType = None


    def _deserialize(self, params):
        if params.get("GenderInfos") is not None:
            self.GenderInfos = []
            for item in params.get("GenderInfos"):
                obj = GenderInfo()
                obj._deserialize(item)
                self.GenderInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.RspImgType = params.get("RspImgType")


class SwapGenderPicResponse(AbstractModel):
    """SwapGenderPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
        :type ResultImage: str
        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
        :type ResultUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")