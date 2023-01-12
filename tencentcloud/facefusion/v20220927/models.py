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


class DescribeMaterialListRequest(AbstractModel):
    """DescribeMaterialList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ActivityId: 活动Id
        :type ActivityId: str
        :param MaterialId: 素材Id
        :type MaterialId: str
        :param Limit: 每次拉取条数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.ActivityId = None
        self.MaterialId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.MaterialId = params.get("MaterialId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaterialListResponse(AbstractModel):
    """DescribeMaterialList返回参数结构体

    """

    def __init__(self):
        r"""
        :param MaterialInfos: 素材列表数据
        :type MaterialInfos: list of PublicMaterialInfos
        :param Count: 素材条数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialInfos = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MaterialInfos") is not None:
            self.MaterialInfos = []
            for item in params.get("MaterialInfos"):
                obj = PublicMaterialInfos()
                obj._deserialize(item)
                self.MaterialInfos.append(obj)
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class FaceInfo(AbstractModel):
    """人脸信息

    """

    def __init__(self):
        r"""
        :param X: 人脸框的横坐标
        :type X: int
        :param Y: 人脸框的纵坐标
        :type Y: int
        :param Width: 人脸框的宽度
        :type Width: int
        :param Height: 人脸框的高度
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FuseFaceRequest(AbstractModel):
    """FuseFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 活动 ID，请在<a href="https://console.cloud.tencent.com/facefusion" target="_blank">人脸融合控制台</a>查看。
        :type ProjectId: str
        :param ModelId: 素材 ID，请在<a href="https://console.cloud.tencent.com/facefusion" target="_blank">人脸融合控制台</a>查看。
        :type ModelId: str
        :param RspImgType: 返回图像方式（url 或 base64) ，二选一。url有效期为7天。
        :type RspImgType: str
        :param MergeInfos: 用户人脸图片、素材模板图的人脸位置信息。
        :type MergeInfos: list of MergeInfo
        :param FuseProfileDegree: 脸型融合比例，数值越高，融合后的脸型越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中脸型参数数值。（换脸版算法暂不支持此参数调整）
        :type FuseProfileDegree: int
        :param FuseFaceDegree: 五官融合比例，数值越高，融合后的五官越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中五官参数数值。（换脸版算法暂不支持此参数调整）
        :type FuseFaceDegree: int
        :param LogoAdd: 为融合结果图添加合成标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了人脸融合技术，是AI合成的图片。
        :type LogoAdd: int
        :param LogoParam: 标识内容设置。
默认在融合结果图右下角添加“本图片为AI合成图片”字样，您可根据自身需要替换为其他的Logo图片。
        :type LogoParam: :class:`tencentcloud.facefusion.v20220927.models.LogoParam`
        """
        self.ProjectId = None
        self.ModelId = None
        self.RspImgType = None
        self.MergeInfos = None
        self.FuseProfileDegree = None
        self.FuseFaceDegree = None
        self.LogoAdd = None
        self.LogoParam = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        self.RspImgType = params.get("RspImgType")
        if params.get("MergeInfos") is not None:
            self.MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self.MergeInfos.append(obj)
        self.FuseProfileDegree = params.get("FuseProfileDegree")
        self.FuseFaceDegree = params.get("FuseFaceDegree")
        self.LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self.LogoParam = LogoParam()
            self.LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FuseFaceResponse(AbstractModel):
    """FuseFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param FusedImage: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type FusedImage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FusedImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FusedImage = params.get("FusedImage")
        self.RequestId = params.get("RequestId")


class LogoParam(AbstractModel):
    """logo参数

    """

    def __init__(self):
        r"""
        :param LogoRect: 标识图片位于融合结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
        :type LogoRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        :param LogoUrl: 标识图片Url地址
        :type LogoUrl: str
        :param LogoImage: 标识图片base64
        :type LogoImage: str
        """
        self.LogoRect = None
        self.LogoUrl = None
        self.LogoImage = None


    def _deserialize(self, params):
        if params.get("LogoRect") is not None:
            self.LogoRect = FaceRect()
            self.LogoRect._deserialize(params.get("LogoRect"))
        self.LogoUrl = params.get("LogoUrl")
        self.LogoImage = params.get("LogoImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialFaces(AbstractModel):
    """人脸信息

    """

    def __init__(self):
        r"""
        :param FaceId: 人脸序号
        :type FaceId: str
        :param FaceInfo: 人脸框信息
        :type FaceInfo: :class:`tencentcloud.facefusion.v20220927.models.FaceInfo`
        """
        self.FaceId = None
        self.FaceInfo = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        if params.get("FaceInfo") is not None:
            self.FaceInfo = FaceInfo()
            self.FaceInfo._deserialize(params.get("FaceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeInfo(AbstractModel):
    """人脸图片和待被融合的素材模板图的人脸位置信息。

    """

    def __init__(self):
        r"""
        :param Image: 输入图片base64
        :type Image: str
        :param Url: 输入图片url
        :type Url: str
        :param InputImageFaceRect: 上传的图片人脸位置信息（人脸框）
        :type InputImageFaceRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        :param TemplateFaceID: 控制台上传的素材人脸ID，不填默认取最大人脸
        :type TemplateFaceID: str
        """
        self.Image = None
        self.Url = None
        self.InputImageFaceRect = None
        self.TemplateFaceID = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        if params.get("InputImageFaceRect") is not None:
            self.InputImageFaceRect = FaceRect()
            self.InputImageFaceRect._deserialize(params.get("InputImageFaceRect"))
        self.TemplateFaceID = params.get("TemplateFaceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicMaterialInfos(AbstractModel):
    """素材信息

    """

    def __init__(self):
        r"""
        :param MaterialId: 素材Id
        :type MaterialId: str
        :param MaterialStatus: 素材状态
        :type MaterialStatus: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        :param MaterialFaceList: 人脸信息
        :type MaterialFaceList: list of MaterialFaces
        :param MaterialName: 素材名
        :type MaterialName: str
        """
        self.MaterialId = None
        self.MaterialStatus = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MaterialFaceList = None
        self.MaterialName = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.MaterialStatus = params.get("MaterialStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("MaterialFaceList") is not None:
            self.MaterialFaceList = []
            for item in params.get("MaterialFaceList"):
                obj = MaterialFaces()
                obj._deserialize(item)
                self.MaterialFaceList.append(obj)
        self.MaterialName = params.get("MaterialName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        