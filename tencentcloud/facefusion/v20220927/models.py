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
        :param _ActivityId: 活动Id
        :type ActivityId: str
        :param _MaterialId: 素材Id
        :type MaterialId: str
        :param _Limit: 每次拉取条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._ActivityId = None
        self._MaterialId = None
        self._Limit = None
        self._Offset = None

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def MaterialId(self):
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._MaterialId = params.get("MaterialId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaterialListResponse(AbstractModel):
    """DescribeMaterialList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MaterialInfos: 素材列表数据
        :type MaterialInfos: list of PublicMaterialInfos
        :param _Count: 素材条数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MaterialInfos = None
        self._Count = None
        self._RequestId = None

    @property
    def MaterialInfos(self):
        return self._MaterialInfos

    @MaterialInfos.setter
    def MaterialInfos(self, MaterialInfos):
        self._MaterialInfos = MaterialInfos

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MaterialInfos") is not None:
            self._MaterialInfos = []
            for item in params.get("MaterialInfos"):
                obj = PublicMaterialInfos()
                obj._deserialize(item)
                self._MaterialInfos.append(obj)
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class FaceInfo(AbstractModel):
    """人脸信息

    """

    def __init__(self):
        r"""
        :param _X: 人脸框的横坐标
        :type X: int
        :param _Y: 人脸框的纵坐标
        :type Y: int
        :param _Width: 人脸框的宽度
        :type Width: int
        :param _Height: 人脸框的高度
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
        


class FaceRect(AbstractModel):
    """人脸框信息

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
        


class FuseFaceRequest(AbstractModel):
    """FuseFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 活动 ID，请在<a href="https://console.cloud.tencent.com/facefusion" target="_blank">人脸融合控制台</a>查看。
        :type ProjectId: str
        :param _ModelId: 素材 ID，请在<a href="https://console.cloud.tencent.com/facefusion" target="_blank">人脸融合控制台</a>查看。
        :type ModelId: str
        :param _RspImgType: 返回图像方式（url 或 base64) ，二选一。url有效期为7天。
        :type RspImgType: str
        :param _MergeInfos: 用户人脸图片、素材模板图的人脸位置信息。
        :type MergeInfos: list of MergeInfo
        :param _FuseProfileDegree: 脸型融合比例，数值越高，融合后的脸型越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中脸型参数数值。（换脸版算法暂不支持此参数调整）
        :type FuseProfileDegree: int
        :param _FuseFaceDegree: 五官融合比例，数值越高，融合后的五官越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中五官参数数值。（换脸版算法暂不支持此参数调整）
        :type FuseFaceDegree: int
        :param _LogoAdd: 为融合结果图添加合成标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示结果图使用了人脸融合技术，是AI合成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在融合结果图右下角添加“本图片为AI合成图片”字样，您可根据自身需要替换为其他的Logo图片。
        :type LogoParam: :class:`tencentcloud.facefusion.v20220927.models.LogoParam`
        :param _FuseParam: 融合参数。
        :type FuseParam: :class:`tencentcloud.facefusion.v20220927.models.FuseParam`
        """
        self._ProjectId = None
        self._ModelId = None
        self._RspImgType = None
        self._MergeInfos = None
        self._FuseProfileDegree = None
        self._FuseFaceDegree = None
        self._LogoAdd = None
        self._LogoParam = None
        self._FuseParam = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def RspImgType(self):
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def MergeInfos(self):
        return self._MergeInfos

    @MergeInfos.setter
    def MergeInfos(self, MergeInfos):
        self._MergeInfos = MergeInfos

    @property
    def FuseProfileDegree(self):
        return self._FuseProfileDegree

    @FuseProfileDegree.setter
    def FuseProfileDegree(self, FuseProfileDegree):
        self._FuseProfileDegree = FuseProfileDegree

    @property
    def FuseFaceDegree(self):
        return self._FuseFaceDegree

    @FuseFaceDegree.setter
    def FuseFaceDegree(self, FuseFaceDegree):
        self._FuseFaceDegree = FuseFaceDegree

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

    @property
    def FuseParam(self):
        return self._FuseParam

    @FuseParam.setter
    def FuseParam(self, FuseParam):
        self._FuseParam = FuseParam


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ModelId = params.get("ModelId")
        self._RspImgType = params.get("RspImgType")
        if params.get("MergeInfos") is not None:
            self._MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self._MergeInfos.append(obj)
        self._FuseProfileDegree = params.get("FuseProfileDegree")
        self._FuseFaceDegree = params.get("FuseFaceDegree")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        if params.get("FuseParam") is not None:
            self._FuseParam = FuseParam()
            self._FuseParam._deserialize(params.get("FuseParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FuseFaceResponse(AbstractModel):
    """FuseFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FusedImage: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type FusedImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FusedImage = None
        self._RequestId = None

    @property
    def FusedImage(self):
        return self._FusedImage

    @FusedImage.setter
    def FusedImage(self, FusedImage):
        self._FusedImage = FusedImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FusedImage = params.get("FusedImage")
        self._RequestId = params.get("RequestId")


class FuseParam(AbstractModel):
    """融合参数

    """

    def __init__(self):
        r"""
        :param _ImageCodecParam: 图片编码参数
        :type ImageCodecParam: :class:`tencentcloud.facefusion.v20220927.models.ImageCodecParam`
        """
        self._ImageCodecParam = None

    @property
    def ImageCodecParam(self):
        return self._ImageCodecParam

    @ImageCodecParam.setter
    def ImageCodecParam(self, ImageCodecParam):
        self._ImageCodecParam = ImageCodecParam


    def _deserialize(self, params):
        if params.get("ImageCodecParam") is not None:
            self._ImageCodecParam = ImageCodecParam()
            self._ImageCodecParam._deserialize(params.get("ImageCodecParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageCodecParam(AbstractModel):
    """图片编码参数

    """

    def __init__(self):
        r"""
        :param _MetaData: 元数据
        :type MetaData: list of MetaData
        """
        self._MetaData = None

    @property
    def MetaData(self):
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self._MetaData = []
            for item in params.get("MetaData"):
                obj = MetaData()
                obj._deserialize(item)
                self._MetaData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoParam(AbstractModel):
    """logo参数

    """

    def __init__(self):
        r"""
        :param _LogoRect: 标识图片位于融合结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
        :type LogoRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        :param _LogoUrl: 标识图片Url地址
        :type LogoUrl: str
        :param _LogoImage: 标识图片base64
        :type LogoImage: str
        """
        self._LogoRect = None
        self._LogoUrl = None
        self._LogoImage = None

    @property
    def LogoRect(self):
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect

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


    def _deserialize(self, params):
        if params.get("LogoRect") is not None:
            self._LogoRect = FaceRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialFaces(AbstractModel):
    """人脸信息

    """

    def __init__(self):
        r"""
        :param _FaceId: 人脸序号
        :type FaceId: str
        :param _FaceInfo: 人脸框信息
        :type FaceInfo: :class:`tencentcloud.facefusion.v20220927.models.FaceInfo`
        """
        self._FaceId = None
        self._FaceInfo = None

    @property
    def FaceId(self):
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def FaceInfo(self):
        return self._FaceInfo

    @FaceInfo.setter
    def FaceInfo(self, FaceInfo):
        self._FaceInfo = FaceInfo


    def _deserialize(self, params):
        self._FaceId = params.get("FaceId")
        if params.get("FaceInfo") is not None:
            self._FaceInfo = FaceInfo()
            self._FaceInfo._deserialize(params.get("FaceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MergeInfo(AbstractModel):
    """人脸图片和待被融合的素材模板图的人脸位置信息。

    """

    def __init__(self):
        r"""
        :param _Image: 输入图片base64
        :type Image: str
        :param _Url: 输入图片url
        :type Url: str
        :param _InputImageFaceRect: 上传的图片人脸位置信息（人脸框）
        :type InputImageFaceRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        :param _TemplateFaceID: 素材人脸ID，不填默认取最大人脸。
        :type TemplateFaceID: str
        :param _TemplateFaceRect: 模板中人脸位置信息(人脸框)，不填默认取最大人脸。此字段仅适用于图片融合自定义模板素材场景。
        :type TemplateFaceRect: :class:`tencentcloud.facefusion.v20220927.models.FaceRect`
        """
        self._Image = None
        self._Url = None
        self._InputImageFaceRect = None
        self._TemplateFaceID = None
        self._TemplateFaceRect = None

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def InputImageFaceRect(self):
        return self._InputImageFaceRect

    @InputImageFaceRect.setter
    def InputImageFaceRect(self, InputImageFaceRect):
        self._InputImageFaceRect = InputImageFaceRect

    @property
    def TemplateFaceID(self):
        return self._TemplateFaceID

    @TemplateFaceID.setter
    def TemplateFaceID(self, TemplateFaceID):
        self._TemplateFaceID = TemplateFaceID

    @property
    def TemplateFaceRect(self):
        return self._TemplateFaceRect

    @TemplateFaceRect.setter
    def TemplateFaceRect(self, TemplateFaceRect):
        self._TemplateFaceRect = TemplateFaceRect


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        if params.get("InputImageFaceRect") is not None:
            self._InputImageFaceRect = FaceRect()
            self._InputImageFaceRect._deserialize(params.get("InputImageFaceRect"))
        self._TemplateFaceID = params.get("TemplateFaceID")
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
        


class MetaData(AbstractModel):
    """MetaData数据结构，Key/Value格式

    """

    def __init__(self):
        r"""
        :param _MetaKey: MetaData的Key
        :type MetaKey: str
        :param _MetaValue: MetaData的Value
        :type MetaValue: str
        """
        self._MetaKey = None
        self._MetaValue = None

    @property
    def MetaKey(self):
        return self._MetaKey

    @MetaKey.setter
    def MetaKey(self, MetaKey):
        self._MetaKey = MetaKey

    @property
    def MetaValue(self):
        return self._MetaValue

    @MetaValue.setter
    def MetaValue(self, MetaValue):
        self._MetaValue = MetaValue


    def _deserialize(self, params):
        self._MetaKey = params.get("MetaKey")
        self._MetaValue = params.get("MetaValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicMaterialInfos(AbstractModel):
    """素材信息

    """

    def __init__(self):
        r"""
        :param _MaterialId: 素材Id
        :type MaterialId: str
        :param _MaterialStatus: 素材状态
        :type MaterialStatus: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _MaterialFaceList: 人脸信息
        :type MaterialFaceList: list of MaterialFaces
        :param _MaterialName: 素材名
        :type MaterialName: str
        :param _AuditResult: 审核原因
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditResult: str
        """
        self._MaterialId = None
        self._MaterialStatus = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MaterialFaceList = None
        self._MaterialName = None
        self._AuditResult = None

    @property
    def MaterialId(self):
        return self._MaterialId

    @MaterialId.setter
    def MaterialId(self, MaterialId):
        self._MaterialId = MaterialId

    @property
    def MaterialStatus(self):
        return self._MaterialStatus

    @MaterialStatus.setter
    def MaterialStatus(self, MaterialStatus):
        self._MaterialStatus = MaterialStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MaterialFaceList(self):
        return self._MaterialFaceList

    @MaterialFaceList.setter
    def MaterialFaceList(self, MaterialFaceList):
        self._MaterialFaceList = MaterialFaceList

    @property
    def MaterialName(self):
        return self._MaterialName

    @MaterialName.setter
    def MaterialName(self, MaterialName):
        self._MaterialName = MaterialName

    @property
    def AuditResult(self):
        return self._AuditResult

    @AuditResult.setter
    def AuditResult(self, AuditResult):
        self._AuditResult = AuditResult


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._MaterialStatus = params.get("MaterialStatus")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("MaterialFaceList") is not None:
            self._MaterialFaceList = []
            for item in params.get("MaterialFaceList"):
                obj = MaterialFaces()
                obj._deserialize(item)
                self._MaterialFaceList.append(obj)
        self._MaterialName = params.get("MaterialName")
        self._AuditResult = params.get("AuditResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        