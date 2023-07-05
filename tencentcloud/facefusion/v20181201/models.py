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
        :type ActivityId: int
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class FaceFusionLiteRequest(AbstractModel):
    """FaceFusionLite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param _ModelId: 素材 ID，请在人脸融合控制台查看。
        :type ModelId: str
        :param _MergeInfos: 用户人脸图片、素材模板图的人脸位置信息。
        :type MergeInfos: list of MergeInfo
        :param _RspImgType: 返回图像方式（url 或 base64) ，二选一。默认url, url有效期为30天。
        :type RspImgType: str
        :param _CelebrityIdentify: 请注意，鉴政服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。
        :type CelebrityIdentify: int
        :param _Engine: 算法引擎参数:  1）选脸版 - youturecreat; 2）优享版 - youtu1vN； 3）畅享版 - ptu； 4）随机 - ALL;  默认为活动选择的算法
        :type Engine: str
        """
        self._ProjectId = None
        self._ModelId = None
        self._MergeInfos = None
        self._RspImgType = None
        self._CelebrityIdentify = None
        self._Engine = None

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
    def MergeInfos(self):
        return self._MergeInfos

    @MergeInfos.setter
    def MergeInfos(self, MergeInfos):
        self._MergeInfos = MergeInfos

    @property
    def RspImgType(self):
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType

    @property
    def CelebrityIdentify(self):
        return self._CelebrityIdentify

    @CelebrityIdentify.setter
    def CelebrityIdentify(self, CelebrityIdentify):
        self._CelebrityIdentify = CelebrityIdentify

    @property
    def Engine(self):
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ModelId = params.get("ModelId")
        if params.get("MergeInfos") is not None:
            self._MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self._MergeInfos.append(obj)
        self._RspImgType = params.get("RspImgType")
        self._CelebrityIdentify = params.get("CelebrityIdentify")
        self._Engine = params.get("Engine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceFusionLiteResponse(AbstractModel):
    """FaceFusionLite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type Image: str
        :param _ReviewResultSet: 鉴政结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Image = None
        self._ReviewResultSet = None
        self._RequestId = None

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ReviewResultSet(self):
        return self._ReviewResultSet

    @ReviewResultSet.setter
    def ReviewResultSet(self, ReviewResultSet):
        self._ReviewResultSet = ReviewResultSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Image = params.get("Image")
        if params.get("ReviewResultSet") is not None:
            self._ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self._ReviewResultSet.append(obj)
        self._RequestId = params.get("RequestId")


class FaceFusionRequest(AbstractModel):
    """FaceFusion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param _ModelId: 素材 ID，请在人脸融合控制台查看。
        :type ModelId: str
        :param _RspImgType: 返回图像方式（url 或 base64) ，二选一。url有效期为7天。
        :type RspImgType: str
        :param _Image: 图片 base64 数据。请确保人脸为正脸，无旋转。若某些手机拍摄后人脸被旋转，请使用图片的 EXIF 信息对图片进行旋转处理；请勿在 base64 数据中包含头部，如“data:image/jpeg;base64,”。
        :type Image: str
        :param _PornDetect: 历史遗留字段，无需填写。因为融合只需提取人脸特征，不需要鉴黄。
        :type PornDetect: int
        :param _CelebrityIdentify: 0表示不需要不适宜内容识别，1表示需要不适宜内容识别。默认值为0。
请注意，不适宜内容识别服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。
        :type CelebrityIdentify: int
        :param _Url: 图片Url地址
        :type Url: str
        """
        self._ProjectId = None
        self._ModelId = None
        self._RspImgType = None
        self._Image = None
        self._PornDetect = None
        self._CelebrityIdentify = None
        self._Url = None

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
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def PornDetect(self):
        return self._PornDetect

    @PornDetect.setter
    def PornDetect(self, PornDetect):
        self._PornDetect = PornDetect

    @property
    def CelebrityIdentify(self):
        return self._CelebrityIdentify

    @CelebrityIdentify.setter
    def CelebrityIdentify(self, CelebrityIdentify):
        self._CelebrityIdentify = CelebrityIdentify

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ModelId = params.get("ModelId")
        self._RspImgType = params.get("RspImgType")
        self._Image = params.get("Image")
        self._PornDetect = params.get("PornDetect")
        self._CelebrityIdentify = params.get("CelebrityIdentify")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceFusionResponse(AbstractModel):
    """FaceFusion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type Image: str
        :param _ReviewResultSet: 不适宜内容识别结果
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Image = None
        self._ReviewResultSet = None
        self._RequestId = None

    @property
    def Image(self):
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ReviewResultSet(self):
        return self._ReviewResultSet

    @ReviewResultSet.setter
    def ReviewResultSet(self, ReviewResultSet):
        self._ReviewResultSet = ReviewResultSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Image = params.get("Image")
        if params.get("ReviewResultSet") is not None:
            self._ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self._ReviewResultSet.append(obj)
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
        :param _ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param _ModelId: 素材 ID，请在人脸融合控制台查看。
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
        :param _CelebrityIdentify: 0表示不需要不适宜内容识别，1表示需要不适宜内容识别。默认值为0。
请注意，不适宜内容识别服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。
        :type CelebrityIdentify: int
        """
        self._ProjectId = None
        self._ModelId = None
        self._RspImgType = None
        self._MergeInfos = None
        self._FuseProfileDegree = None
        self._FuseFaceDegree = None
        self._CelebrityIdentify = None

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
    def CelebrityIdentify(self):
        return self._CelebrityIdentify

    @CelebrityIdentify.setter
    def CelebrityIdentify(self, CelebrityIdentify):
        self._CelebrityIdentify = CelebrityIdentify


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
        self._CelebrityIdentify = params.get("CelebrityIdentify")
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
        :param _ReviewResultSet: 不适宜内容识别结果。该数组的顺序和请求中mergeinfo的顺序一致，一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FusedImage = None
        self._ReviewResultSet = None
        self._RequestId = None

    @property
    def FusedImage(self):
        return self._FusedImage

    @FusedImage.setter
    def FusedImage(self, FusedImage):
        self._FusedImage = FusedImage

    @property
    def ReviewResultSet(self):
        return self._ReviewResultSet

    @ReviewResultSet.setter
    def ReviewResultSet(self, ReviewResultSet):
        self._ReviewResultSet = ReviewResultSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FusedImage = params.get("FusedImage")
        if params.get("ReviewResultSet") is not None:
            self._ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self._ReviewResultSet.append(obj)
        self._RequestId = params.get("RequestId")


class FuseFaceReviewDetail(AbstractModel):
    """人脸融合不适宜内容识别人脸信息

    """

    def __init__(self):
        r"""
        :param _Field: 保留字段
        :type Field: str
        :param _Label: 人员名称
        :type Label: str
        :param _Confidence: 对应识别label的置信度，分数越高意味违法违规可能性越大。 
0到70，Suggestion建议为PASS； 
70到80，Suggestion建议为REVIEW； 
80到100，Suggestion建议为BLOCK。
        :type Confidence: float
        :param _Suggestion: 识别场景的审核结论：  
PASS：正常 
REVIEW：疑似  
BLOCK：违规
        :type Suggestion: str
        """
        self._Field = None
        self._Label = None
        self._Confidence = None
        self._Suggestion = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Label = params.get("Label")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FuseFaceReviewResult(AbstractModel):
    """人脸融合不适宜内容识别返回参数item

    """

    def __init__(self):
        r"""
        :param _Category: 保留字段
        :type Category: str
        :param _Code: 状态码， 0为处理成功，其他值为处理失败
        :type Code: str
        :param _CodeDescription: 对应状态码信息描述
        :type CodeDescription: str
        :param _Confidence: 保留字段
        :type Confidence: float
        :param _Suggestion: 保留字段
        :type Suggestion: str
        :param _DetailSet: 审核详细内容
        :type DetailSet: list of FuseFaceReviewDetail
        """
        self._Category = None
        self._Code = None
        self._CodeDescription = None
        self._Confidence = None
        self._Suggestion = None
        self._DetailSet = None

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def CodeDescription(self):
        return self._CodeDescription

    @CodeDescription.setter
    def CodeDescription(self, CodeDescription):
        self._CodeDescription = CodeDescription

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def DetailSet(self):
        return self._DetailSet

    @DetailSet.setter
    def DetailSet(self, DetailSet):
        self._DetailSet = DetailSet


    def _deserialize(self, params):
        self._Category = params.get("Category")
        self._Code = params.get("Code")
        self._CodeDescription = params.get("CodeDescription")
        self._Confidence = params.get("Confidence")
        self._Suggestion = params.get("Suggestion")
        if params.get("DetailSet") is not None:
            self._DetailSet = []
            for item in params.get("DetailSet"):
                obj = FuseFaceReviewDetail()
                obj._deserialize(item)
                self._DetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaterialFaceList(AbstractModel):
    """人脸信息

    """

    def __init__(self):
        r"""
        :param _FaceId: 人脸序号
        :type FaceId: str
        :param _FaceInfo: 人脸框信息
        :type FaceInfo: :class:`tencentcloud.facefusion.v20181201.models.FaceInfo`
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
        :type InputImageFaceRect: :class:`tencentcloud.facefusion.v20181201.models.FaceRect`
        :param _TemplateFaceID: 控制台上传的素材人脸ID，不填默认取最大人脸
        :type TemplateFaceID: str
        """
        self._Image = None
        self._Url = None
        self._InputImageFaceRect = None
        self._TemplateFaceID = None

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


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        if params.get("InputImageFaceRect") is not None:
            self._InputImageFaceRect = FaceRect()
            self._InputImageFaceRect._deserialize(params.get("InputImageFaceRect"))
        self._TemplateFaceID = params.get("TemplateFaceID")
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
        :param _BlendParamPtu: 脸型参数P图
        :type BlendParamPtu: int
        :param _PositionParamPtu: 五官参数P图
        :type PositionParamPtu: int
        :param _BlendParamYoutu: 脸型参数优图
        :type BlendParamYoutu: int
        :param _PositionParamYoutu: 五官参数优图
        :type PositionParamYoutu: int
        :param _Url: 素材COS地址
        :type Url: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 修改时间
        :type UpdateTime: str
        :param _MaterialFaceList: 人脸信息
        :type MaterialFaceList: list of MaterialFaceList
        """
        self._MaterialId = None
        self._MaterialStatus = None
        self._BlendParamPtu = None
        self._PositionParamPtu = None
        self._BlendParamYoutu = None
        self._PositionParamYoutu = None
        self._Url = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MaterialFaceList = None

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
    def BlendParamPtu(self):
        return self._BlendParamPtu

    @BlendParamPtu.setter
    def BlendParamPtu(self, BlendParamPtu):
        self._BlendParamPtu = BlendParamPtu

    @property
    def PositionParamPtu(self):
        return self._PositionParamPtu

    @PositionParamPtu.setter
    def PositionParamPtu(self, PositionParamPtu):
        self._PositionParamPtu = PositionParamPtu

    @property
    def BlendParamYoutu(self):
        return self._BlendParamYoutu

    @BlendParamYoutu.setter
    def BlendParamYoutu(self, BlendParamYoutu):
        self._BlendParamYoutu = BlendParamYoutu

    @property
    def PositionParamYoutu(self):
        return self._PositionParamYoutu

    @PositionParamYoutu.setter
    def PositionParamYoutu(self, PositionParamYoutu):
        self._PositionParamYoutu = PositionParamYoutu

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

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


    def _deserialize(self, params):
        self._MaterialId = params.get("MaterialId")
        self._MaterialStatus = params.get("MaterialStatus")
        self._BlendParamPtu = params.get("BlendParamPtu")
        self._PositionParamPtu = params.get("PositionParamPtu")
        self._BlendParamYoutu = params.get("BlendParamYoutu")
        self._PositionParamYoutu = params.get("PositionParamYoutu")
        self._Url = params.get("Url")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("MaterialFaceList") is not None:
            self._MaterialFaceList = []
            for item in params.get("MaterialFaceList"):
                obj = MaterialFaceList()
                obj._deserialize(item)
                self._MaterialFaceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        