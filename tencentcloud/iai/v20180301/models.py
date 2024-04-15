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


class AnalyzeDenseLandmarksRequest(AbstractModel):
    """AnalyzeDenseLandmarks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 检测模式。0 为检测所有出现的人脸， 1 为检测面积最大的人脸。 
默认为 0。 
最多返回 5 张人脸的五官定位（人脸关键点）具体信息。
        :type Mode: int
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。  
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。本接口仅支持 “3.0“ 输入。
        :type FaceModelVersion: str
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._Mode = None
        self._Image = None
        self._Url = None
        self._FaceModelVersion = None
        self._NeedRotateDetection = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

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
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeDenseLandmarksResponse(AbstractModel):
    """AnalyzeDenseLandmarks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param _ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param _DenseFaceShapeSet: 稠密人脸关键点具体信息。
        :type DenseFaceShapeSet: list of DenseFaceShape
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。本接口仅支持 “3.0“ 输入。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageWidth = None
        self._ImageHeight = None
        self._DenseFaceShapeSet = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def DenseFaceShapeSet(self):
        return self._DenseFaceShapeSet

    @DenseFaceShapeSet.setter
    def DenseFaceShapeSet(self, DenseFaceShapeSet):
        self._DenseFaceShapeSet = DenseFaceShapeSet

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        if params.get("DenseFaceShapeSet") is not None:
            self._DenseFaceShapeSet = []
            for item in params.get("DenseFaceShapeSet"):
                obj = DenseFaceShape()
                obj._deserialize(item)
                self._DenseFaceShapeSet.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class AnalyzeFaceRequest(AbstractModel):
    """AnalyzeFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 检测模式。0 为检测所有出现的人脸， 1 为检测面积最大的人脸。默认为 0。最多返回 10 张人脸的五官定位（人脸关键点）具体信息。
        :type Mode: int
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。

目前入参支持 “2.0”和“3.0“ 两个输入。

2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。

2020年11月26日后开通服务的账号仅支持输入“3.0”。

不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._Mode = None
        self._Image = None
        self._Url = None
        self._FaceModelVersion = None
        self._NeedRotateDetection = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

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
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeFaceResponse(AbstractModel):
    """AnalyzeFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param _ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param _FaceShapeSet: 五官定位（人脸关键点）具体信息。
        :type FaceShapeSet: list of FaceShape
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageWidth = None
        self._ImageHeight = None
        self._FaceShapeSet = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def FaceShapeSet(self):
        return self._FaceShapeSet

    @FaceShapeSet.setter
    def FaceShapeSet(self, FaceShapeSet):
        self._FaceShapeSet = FaceShapeSet

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        if params.get("FaceShapeSet") is not None:
            self._FaceShapeSet = []
            for item in params.get("FaceShapeSet"):
                obj = FaceShape()
                obj._deserialize(item)
                self._FaceShapeSet.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class AttributeItem(AbstractModel):
    """人脸属性信息

    """

    def __init__(self):
        r"""
        :param _Type: 属性值
        :type Type: int
        :param _Probability: Type识别概率值,[0,1],代表判断正确的概率。
        :type Probability: float
        """
        self._Type = None
        self._Probability = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Probability(self):
        return self._Probability

    @Probability.setter
    def Probability(self, Probability):
        self._Probability = Probability


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Probability = params.get("Probability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Candidate(AbstractModel):
    """识别出的最相似候选人

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        :param _FaceId: 人脸ID，仅在SearchFaces/SearchFacesReturnsByGroup接口返回时有效。人员搜索类接口采用融合特征方式检索，该字段无意义
        :type FaceId: str
        :param _Score: 候选者的匹配得分。 

1万大小人脸底库下，误识率百分之一对应分数为70分，误识率千分之一对应分数为80分，误识率万分之一对应分数为90分；
10万大小人脸底库下，误识率百分之一对应分数为80分，误识率千分之一对应分数为90分，误识率万分之一对应分数为100分；
30万大小人脸底库下，误识率百分之一对应分数为85分，误识率千分之一对应分数为95分。

一般80分左右可适用大部分场景，建议分数不要超过90分。您可以根据实际情况选择合适的分数。
        :type Score: float
        :param _PersonName: 人员名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonName: str
        :param _Gender: 人员性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Gender: int
        :param _PersonGroupInfos: 包含此人员的人员库及描述字段内容列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonGroupInfos: list of PersonGroupInfo
        """
        self._PersonId = None
        self._FaceId = None
        self._Score = None
        self._PersonName = None
        self._Gender = None
        self._PersonGroupInfos = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def FaceId(self):
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def PersonGroupInfos(self):
        return self._PersonGroupInfos

    @PersonGroupInfos.setter
    def PersonGroupInfos(self, PersonGroupInfos):
        self._PersonGroupInfos = PersonGroupInfos


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._FaceId = params.get("FaceId")
        self._Score = params.get("Score")
        self._PersonName = params.get("PersonName")
        self._Gender = params.get("Gender")
        if params.get("PersonGroupInfos") is not None:
            self._PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self._PersonGroupInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareFaceRequest(AbstractModel):
    """CompareFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageA: A 图片 base64 数据，base64 编码后大小不可超过5M。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageA: str
        :param _ImageB: B 图片 base64 数据，base64 编码后大小不可超过5M。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageB: str
        :param _UrlA: A 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
A 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type UrlA: str
        :param _UrlB: B 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
B 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type UrlB: str
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。

目前入参支持 “2.0”和“3.0“ 两个输入。

2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。

2020年11月26日后开通服务的账号仅支持输入“3.0”。

不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1: 较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多，在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._ImageA = None
        self._ImageB = None
        self._UrlA = None
        self._UrlB = None
        self._FaceModelVersion = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def ImageA(self):
        return self._ImageA

    @ImageA.setter
    def ImageA(self, ImageA):
        self._ImageA = ImageA

    @property
    def ImageB(self):
        return self._ImageB

    @ImageB.setter
    def ImageB(self, ImageB):
        self._ImageB = ImageB

    @property
    def UrlA(self):
        return self._UrlA

    @UrlA.setter
    def UrlA(self, UrlA):
        self._UrlA = UrlA

    @property
    def UrlB(self):
        return self._UrlB

    @UrlB.setter
    def UrlB(self, UrlB):
        self._UrlB = UrlB

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._ImageA = params.get("ImageA")
        self._ImageB = params.get("ImageB")
        self._UrlA = params.get("UrlA")
        self._UrlB = params.get("UrlB")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompareFaceResponse(AbstractModel):
    """CompareFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Score: 两张图片中人脸的相似度分数。
不同算法版本返回的相似度分数不同。 
若需要验证两张图片中人脸是否为同一人，3.0版本误识率千分之一对应分数为40分，误识率万分之一对应分数为50分，误识率十万分之一对应分数为60分。  一般超过50分则可认定为同一人。 
2.0版本误识率千分之一对应分数为70分，误识率万分之一对应分数为80分，误识率十万分之一对应分数为90分。 一般超过80分则可认定为同一人。 
若需要验证两张图片中的人脸是否为同一人，建议使用人脸验证接口。
        :type Score: float
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Score = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class CopyPersonRequest(AbstractModel):
    """CopyPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        :param _GroupIds: 待加入的人员库列表
        :type GroupIds: list of str
        """
        self._PersonId = None
        self._GroupIds = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyPersonResponse(AbstractModel):
    """CopyPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SucGroupNum: 成功加入的人员库数量
        :type SucGroupNum: int
        :param _SucGroupIds: 成功加入的人员库列表
        :type SucGroupIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SucGroupNum = None
        self._SucGroupIds = None
        self._RequestId = None

    @property
    def SucGroupNum(self):
        return self._SucGroupNum

    @SucGroupNum.setter
    def SucGroupNum(self, SucGroupNum):
        self._SucGroupNum = SucGroupNum

    @property
    def SucGroupIds(self):
        return self._SucGroupIds

    @SucGroupIds.setter
    def SucGroupIds(self, SucGroupIds):
        self._SucGroupIds = SucGroupIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SucGroupNum = params.get("SucGroupNum")
        self._SucGroupIds = params.get("SucGroupIds")
        self._RequestId = params.get("RequestId")


class CreateFaceRequest(AbstractModel):
    """CreateFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID。
        :type PersonId: str
        :param _Images: 图片 base64 数据，base64 编码后大小不可超过5M。
人员人脸总数量不可超过5张。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param _Urls: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
人员人脸总数量不可超过5张。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
        :type Urls: list of str
        :param _FaceMatchThreshold: 只有和该人员已有的人脸相似度超过FaceMatchThreshold值的人脸，才能增加人脸成功。 
默认值60分。取值范围[0,100] 。
        :type FaceMatchThreshold: float
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._PersonId = None
        self._Images = None
        self._Urls = None
        self._FaceMatchThreshold = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Images(self):
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Images = params.get("Images")
        self._Urls = params.get("Urls")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFaceResponse(AbstractModel):
    """CreateFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SucFaceNum: 加入成功的人脸数量
        :type SucFaceNum: int
        :param _SucFaceIds: 加入成功的人脸ID列表
        :type SucFaceIds: list of str
        :param _RetCode: 每张人脸图片添加结果，-1101 代表未检测到人脸，-1102 代表图片解码失败，-1109 代表图片尺寸过大或者过小， 
-1601代表不符合图片质量控制要求, -1604 代表人脸相似度没有超过FaceMatchThreshold。 
其他非 0 值代表算法服务异常。 
RetCode的顺序和入参中 Images 或 Urls 的顺序一致。
        :type RetCode: list of int
        :param _SucIndexes: 加入成功的人脸索引。索引顺序和入参中 Images 或 Urls 的顺序一致。 
例， Urls 中 有 3 个 url，第二个 url 失败，则 SucIndexes 值为 [0,2] 。
        :type SucIndexes: list of int non-negative
        :param _SucFaceRects: 加入成功的人脸框位置。顺序和入参中 Images 或 Urls 的顺序一致。
        :type SucFaceRects: list of FaceRect
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SucFaceNum = None
        self._SucFaceIds = None
        self._RetCode = None
        self._SucIndexes = None
        self._SucFaceRects = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def SucFaceNum(self):
        return self._SucFaceNum

    @SucFaceNum.setter
    def SucFaceNum(self, SucFaceNum):
        self._SucFaceNum = SucFaceNum

    @property
    def SucFaceIds(self):
        return self._SucFaceIds

    @SucFaceIds.setter
    def SucFaceIds(self, SucFaceIds):
        self._SucFaceIds = SucFaceIds

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode

    @property
    def SucIndexes(self):
        return self._SucIndexes

    @SucIndexes.setter
    def SucIndexes(self, SucIndexes):
        self._SucIndexes = SucIndexes

    @property
    def SucFaceRects(self):
        return self._SucFaceRects

    @SucFaceRects.setter
    def SucFaceRects(self, SucFaceRects):
        self._SucFaceRects = SucFaceRects

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SucFaceNum = params.get("SucFaceNum")
        self._SucFaceIds = params.get("SucFaceIds")
        self._RetCode = params.get("RetCode")
        self._SucIndexes = params.get("SucIndexes")
        if params.get("SucFaceRects") is not None:
            self._SucFaceRects = []
            for item in params.get("SucFaceRects"):
                obj = FaceRect()
                obj._deserialize(item)
                self._SucFaceRects.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 人员库名称，[1,60]个字符，可修改，不可重复。
        :type GroupName: str
        :param _GroupId: 人员库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :type GroupId: str
        :param _GroupExDescriptions: 人员库自定义描述字段，用于描述人员库中人员属性，该人员库下所有人员将拥有此描述字段。 
最多可以创建5个。 
每个自定义描述字段支持[1,30]个字符。 
在同一人员库中自定义描述字段不可重复。 
例： 设置某人员库“自定义描述字段”为["学号","工号","手机号"]， 
则该人员库下所有人员将拥有名为“学号”、“工号”、“手机号”的描述字段， 
可在对应人员描述字段中填写内容，登记该人员的学号、工号、手机号等信息。
        :type GroupExDescriptions: list of str
        :param _Tag: 人员库信息备注，[0，40]个字符。
        :type Tag: str
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。
目前入参支持 “2.0”和“3.0“ 两个输入。
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。
2020年11月26日后开通服务的账号仅支持输入“3.0”。
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        """
        self._GroupName = None
        self._GroupId = None
        self._GroupExDescriptions = None
        self._Tag = None
        self._FaceModelVersion = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupExDescriptions(self):
        return self._GroupExDescriptions

    @GroupExDescriptions.setter
    def GroupExDescriptions(self, GroupExDescriptions):
        self._GroupExDescriptions = GroupExDescriptions

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._GroupExDescriptions = params.get("GroupExDescriptions")
        self._Tag = params.get("Tag")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 待加入的人员库ID。
        :type GroupId: str
        :param _PersonName: 人员名称。[1，60]个字符，可修改，可重复。
        :type PersonName: str
        :param _PersonId: 人员ID，单个腾讯云账号下不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :type PersonId: str
        :param _Gender: 0代表未填写，1代表男性，2代表女性。
        :type Gender: int
        :param _PersonExDescriptionInfos: 人员描述字段内容，key-value。[0，60]个字符，可修改，可重复。
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _UniquePersonControl: 此参数用于控制判断 Image 或 Url 中图片包含的人脸，是否在人员库中已有疑似的同一人。 
如果判断为已有相同人在人员库中，则不会创建新的人员，返回疑似同一人的人员信息。 
如果判断没有，则完成创建人员。 
0: 不进行判断，无论是否有疑似同一人在库中均完成入库； 
1:较低的同一人判断要求（百一误识别率）； 
2: 一般的同一人判断要求（千一误识别率）； 
3: 较高的同一人判断要求（万一误识别率）； 
4: 很高的同一人判断要求（十万一误识别率）。 
默认 0。  
注： 要求越高，则疑似同一人的概率越小。不同要求对应的误识别率仅为参考值，您可以根据实际情况调整。
        :type UniquePersonControl: int
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._GroupId = None
        self._PersonName = None
        self._PersonId = None
        self._Gender = None
        self._PersonExDescriptionInfos = None
        self._Image = None
        self._Url = None
        self._UniquePersonControl = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def PersonExDescriptionInfos(self):
        return self._PersonExDescriptionInfos

    @PersonExDescriptionInfos.setter
    def PersonExDescriptionInfos(self, PersonExDescriptionInfos):
        self._PersonExDescriptionInfos = PersonExDescriptionInfos

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
    def UniquePersonControl(self):
        return self._UniquePersonControl

    @UniquePersonControl.setter
    def UniquePersonControl(self, UniquePersonControl):
        self._UniquePersonControl = UniquePersonControl

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PersonName = params.get("PersonName")
        self._PersonId = params.get("PersonId")
        self._Gender = params.get("Gender")
        if params.get("PersonExDescriptionInfos") is not None:
            self._PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self._PersonExDescriptionInfos.append(obj)
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._UniquePersonControl = params.get("UniquePersonControl")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceId: 人脸图片唯一标识。
        :type FaceId: str
        :param _FaceRect: 检测出的人脸框的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceRect: :class:`tencentcloud.iai.v20180301.models.FaceRect`
        :param _SimilarPersonId: 疑似同一人的PersonId。 
当 UniquePersonControl 参数不为0且人员库中有疑似的同一人，此参数才有意义。
        :type SimilarPersonId: str
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceId = None
        self._FaceRect = None
        self._SimilarPersonId = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def FaceId(self):
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def SimilarPersonId(self):
        return self._SimilarPersonId

    @SimilarPersonId.setter
    def SimilarPersonId(self, SimilarPersonId):
        self._SimilarPersonId = SimilarPersonId

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceId = params.get("FaceId")
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        self._SimilarPersonId = params.get("SimilarPersonId")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class DeleteFaceRequest(AbstractModel):
    """DeleteFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        :param _FaceIds: 待删除的人脸ID列表
        :type FaceIds: list of str
        """
        self._PersonId = None
        self._FaceIds = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def FaceIds(self):
        return self._FaceIds

    @FaceIds.setter
    def FaceIds(self, FaceIds):
        self._FaceIds = FaceIds


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._FaceIds = params.get("FaceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFaceResponse(AbstractModel):
    """DeleteFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SucDeletedNum: 删除成功的人脸数量
        :type SucDeletedNum: int
        :param _SucFaceIds: 删除成功的人脸ID列表
        :type SucFaceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SucDeletedNum = None
        self._SucFaceIds = None
        self._RequestId = None

    @property
    def SucDeletedNum(self):
        return self._SucDeletedNum

    @SucDeletedNum.setter
    def SucDeletedNum(self, SucDeletedNum):
        self._SucDeletedNum = SucDeletedNum

    @property
    def SucFaceIds(self):
        return self._SucFaceIds

    @SucFaceIds.setter
    def SucFaceIds(self, SucFaceIds):
        self._SucFaceIds = SucFaceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SucDeletedNum = params.get("SucDeletedNum")
        self._SucFaceIds = params.get("SucFaceIds")
        self._RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人员库ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePersonFromGroupRequest(AbstractModel):
    """DeletePersonFromGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        :param _GroupId: 人员库ID
        :type GroupId: str
        """
        self._PersonId = None
        self._GroupId = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonFromGroupResponse(AbstractModel):
    """DeletePersonFromGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        """
        self._PersonId = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DenseFaceShape(AbstractModel):
    """稠密关键点详细信息

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
        :param _LeftEye: 描述左侧眼睛轮廓的 XX 点。
        :type LeftEye: list of Point
        :param _RightEye: 描述右侧眼睛轮廓的 XX 点。
        :type RightEye: list of Point
        :param _LeftEyeBrow: 描述左侧眉毛轮廓的 XX 点。
        :type LeftEyeBrow: list of Point
        :param _RightEyeBrow: 描述右侧眉毛轮廓的 XX 点。
        :type RightEyeBrow: list of Point
        :param _MouthOutside: 描述外嘴巴轮廓的 XX 点， 从左侧开始逆时针返回。
        :type MouthOutside: list of Point
        :param _MouthInside: 描述内嘴巴轮廓的 XX 点，从左侧开始逆时针返回。
        :type MouthInside: list of Point
        :param _Nose: 描述鼻子轮廓的 XX 点。
        :type Nose: list of Point
        :param _LeftPupil: 左瞳孔轮廓的 XX 个点。
        :type LeftPupil: list of Point
        :param _RightPupil: 右瞳孔轮廓的 XX 个点。
        :type RightPupil: list of Point
        :param _CentralAxis: 中轴线轮廓的 XX 个点。
        :type CentralAxis: list of Point
        :param _Chin: 下巴轮廓的 XX 个点。
        :type Chin: list of Point
        :param _LeftEyeBags: 左眼袋的 XX 个点。
        :type LeftEyeBags: list of Point
        :param _RightEyeBags: 右眼袋的 XX 个点。
        :type RightEyeBags: list of Point
        :param _Forehead: 额头的 XX 个点。
        :type Forehead: list of Point
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._LeftEye = None
        self._RightEye = None
        self._LeftEyeBrow = None
        self._RightEyeBrow = None
        self._MouthOutside = None
        self._MouthInside = None
        self._Nose = None
        self._LeftPupil = None
        self._RightPupil = None
        self._CentralAxis = None
        self._Chin = None
        self._LeftEyeBags = None
        self._RightEyeBags = None
        self._Forehead = None

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

    @property
    def LeftEye(self):
        return self._LeftEye

    @LeftEye.setter
    def LeftEye(self, LeftEye):
        self._LeftEye = LeftEye

    @property
    def RightEye(self):
        return self._RightEye

    @RightEye.setter
    def RightEye(self, RightEye):
        self._RightEye = RightEye

    @property
    def LeftEyeBrow(self):
        return self._LeftEyeBrow

    @LeftEyeBrow.setter
    def LeftEyeBrow(self, LeftEyeBrow):
        self._LeftEyeBrow = LeftEyeBrow

    @property
    def RightEyeBrow(self):
        return self._RightEyeBrow

    @RightEyeBrow.setter
    def RightEyeBrow(self, RightEyeBrow):
        self._RightEyeBrow = RightEyeBrow

    @property
    def MouthOutside(self):
        return self._MouthOutside

    @MouthOutside.setter
    def MouthOutside(self, MouthOutside):
        self._MouthOutside = MouthOutside

    @property
    def MouthInside(self):
        return self._MouthInside

    @MouthInside.setter
    def MouthInside(self, MouthInside):
        self._MouthInside = MouthInside

    @property
    def Nose(self):
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def LeftPupil(self):
        return self._LeftPupil

    @LeftPupil.setter
    def LeftPupil(self, LeftPupil):
        self._LeftPupil = LeftPupil

    @property
    def RightPupil(self):
        return self._RightPupil

    @RightPupil.setter
    def RightPupil(self, RightPupil):
        self._RightPupil = RightPupil

    @property
    def CentralAxis(self):
        return self._CentralAxis

    @CentralAxis.setter
    def CentralAxis(self, CentralAxis):
        self._CentralAxis = CentralAxis

    @property
    def Chin(self):
        return self._Chin

    @Chin.setter
    def Chin(self, Chin):
        self._Chin = Chin

    @property
    def LeftEyeBags(self):
        return self._LeftEyeBags

    @LeftEyeBags.setter
    def LeftEyeBags(self, LeftEyeBags):
        self._LeftEyeBags = LeftEyeBags

    @property
    def RightEyeBags(self):
        return self._RightEyeBags

    @RightEyeBags.setter
    def RightEyeBags(self, RightEyeBags):
        self._RightEyeBags = RightEyeBags

    @property
    def Forehead(self):
        return self._Forehead

    @Forehead.setter
    def Forehead(self, Forehead):
        self._Forehead = Forehead


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        if params.get("LeftEye") is not None:
            self._LeftEye = []
            for item in params.get("LeftEye"):
                obj = Point()
                obj._deserialize(item)
                self._LeftEye.append(obj)
        if params.get("RightEye") is not None:
            self._RightEye = []
            for item in params.get("RightEye"):
                obj = Point()
                obj._deserialize(item)
                self._RightEye.append(obj)
        if params.get("LeftEyeBrow") is not None:
            self._LeftEyeBrow = []
            for item in params.get("LeftEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self._LeftEyeBrow.append(obj)
        if params.get("RightEyeBrow") is not None:
            self._RightEyeBrow = []
            for item in params.get("RightEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self._RightEyeBrow.append(obj)
        if params.get("MouthOutside") is not None:
            self._MouthOutside = []
            for item in params.get("MouthOutside"):
                obj = Point()
                obj._deserialize(item)
                self._MouthOutside.append(obj)
        if params.get("MouthInside") is not None:
            self._MouthInside = []
            for item in params.get("MouthInside"):
                obj = Point()
                obj._deserialize(item)
                self._MouthInside.append(obj)
        if params.get("Nose") is not None:
            self._Nose = []
            for item in params.get("Nose"):
                obj = Point()
                obj._deserialize(item)
                self._Nose.append(obj)
        if params.get("LeftPupil") is not None:
            self._LeftPupil = []
            for item in params.get("LeftPupil"):
                obj = Point()
                obj._deserialize(item)
                self._LeftPupil.append(obj)
        if params.get("RightPupil") is not None:
            self._RightPupil = []
            for item in params.get("RightPupil"):
                obj = Point()
                obj._deserialize(item)
                self._RightPupil.append(obj)
        if params.get("CentralAxis") is not None:
            self._CentralAxis = []
            for item in params.get("CentralAxis"):
                obj = Point()
                obj._deserialize(item)
                self._CentralAxis.append(obj)
        if params.get("Chin") is not None:
            self._Chin = []
            for item in params.get("Chin"):
                obj = Point()
                obj._deserialize(item)
                self._Chin.append(obj)
        if params.get("LeftEyeBags") is not None:
            self._LeftEyeBags = []
            for item in params.get("LeftEyeBags"):
                obj = Point()
                obj._deserialize(item)
                self._LeftEyeBags.append(obj)
        if params.get("RightEyeBags") is not None:
            self._RightEyeBags = []
            for item in params.get("RightEyeBags"):
                obj = Point()
                obj._deserialize(item)
                self._RightEyeBags.append(obj)
        if params.get("Forehead") is not None:
            self._Forehead = []
            for item in params.get("Forehead"):
                obj = Point()
                obj._deserialize(item)
                self._Forehead.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectFaceAttributesRequest(AbstractModel):
    """DetectFaceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxFaceNum: 最多处理的人脸数目。 
默认值为1（仅检测图片中面积最大的那张人脸），最大值为120。 
此参数用于控制处理待检测图片中的人脸个数，值越小，处理速度越快。
        :type MaxFaceNum: int
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。 
对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 
Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _FaceAttributesType: 是否返回年龄、性别、情绪等属性。 
合法值为（大小写不敏感）：None、Age、Beauty、Emotion、Eye、Eyebrow、 
Gender、Hair、Hat、Headpose、Mask、Mouth、Moustache、Nose、Shape、Skin、Smile。 
None为不需要返回。默认为 None。即FaceAttributesType属性为空时，各属性返回值为0。
需要将属性组成一个用逗号分隔的字符串，属性之间的顺序没有要求。 
关于各属性的详细描述，参见下文出参。 
最多返回面积最大的 5 张人脸属性信息，超过 5 张人脸（第 6 张及以后的人脸）的 AttributesInfo 不具备参考意义。
        :type FaceAttributesType: str
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。本接口仅支持“3.0”输入
        :type FaceModelVersion: str
        """
        self._MaxFaceNum = None
        self._Image = None
        self._Url = None
        self._FaceAttributesType = None
        self._NeedRotateDetection = None
        self._FaceModelVersion = None

    @property
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

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
    def FaceAttributesType(self):
        return self._FaceAttributesType

    @FaceAttributesType.setter
    def FaceAttributesType(self, FaceAttributesType):
        self._FaceAttributesType = FaceAttributesType

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceAttributesType = params.get("FaceAttributesType")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectFaceAttributesResponse(AbstractModel):
    """DetectFaceAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param _ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param _FaceDetailInfos: 人脸信息列表。
        :type FaceDetailInfos: list of FaceDetailInfo
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageWidth = None
        self._ImageHeight = None
        self._FaceDetailInfos = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def FaceDetailInfos(self):
        return self._FaceDetailInfos

    @FaceDetailInfos.setter
    def FaceDetailInfos(self, FaceDetailInfos):
        self._FaceDetailInfos = FaceDetailInfos

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        if params.get("FaceDetailInfos") is not None:
            self._FaceDetailInfos = []
            for item in params.get("FaceDetailInfos"):
                obj = FaceDetailInfo()
                obj._deserialize(item)
                self._FaceDetailInfos.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class DetectFaceRequest(AbstractModel):
    """DetectFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxFaceNum: 最多处理的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为120。 
此参数用于控制处理待检测图片中的人脸个数，值越小，处理速度越快。
        :type MaxFaceNum: int
        :param _MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。
默认为34。建议不低于34。
低于MinFaceSize值的人脸不会被检测。
        :type MinFaceSize: int
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _NeedFaceAttributes: 是否需要返回人脸属性信息（FaceAttributesInfo）。0 为不需要返回，1 为需要返回。默认为 0。 
非 1 值均视为不需要返回，此时 FaceAttributesInfo 不具备参考意义。  
最多返回面积最大的 5 张人脸属性信息，超过 5 张人脸（第 6 张及以后的人脸）的 FaceAttributesInfo 不具备参考意义。  
提取人脸属性信息较为耗时，如不需要人脸属性信息，建议关闭此项功能，加快人脸检测速度。
        :type NeedFaceAttributes: int
        :param _NeedQualityDetection: 是否开启质量检测。0 为关闭，1 为开启。默认为 0。 
非 1 值均视为不进行质量检测。
最多返回面积最大的 30 张人脸质量分信息，超过 30 张人脸（第 31 张及以后的人脸）的 FaceQualityInfo不具备参考意义。  
建议：人脸入库操作建议开启此功能。
        :type NeedQualityDetection: int
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。  
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._Image = None
        self._Url = None
        self._NeedFaceAttributes = None
        self._NeedQualityDetection = None
        self._FaceModelVersion = None
        self._NeedRotateDetection = None

    @property
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

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
    def NeedFaceAttributes(self):
        return self._NeedFaceAttributes

    @NeedFaceAttributes.setter
    def NeedFaceAttributes(self, NeedFaceAttributes):
        self._NeedFaceAttributes = NeedFaceAttributes

    @property
    def NeedQualityDetection(self):
        return self._NeedQualityDetection

    @NeedQualityDetection.setter
    def NeedQualityDetection(self, NeedQualityDetection):
        self._NeedQualityDetection = NeedQualityDetection

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._NeedFaceAttributes = params.get("NeedFaceAttributes")
        self._NeedQualityDetection = params.get("NeedQualityDetection")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectFaceResponse(AbstractModel):
    """DetectFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param _ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param _FaceInfos: 人脸信息列表。包含人脸坐标信息、属性信息（若需要）、质量分信息（若需要）。
        :type FaceInfos: list of FaceInfo
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。
目前入参支持 “2.0”和“3.0“ 两个输入。
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。
2020年11月26日后开通服务的账号仅支持输入“3.0”。
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageWidth = None
        self._ImageHeight = None
        self._FaceInfos = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def FaceInfos(self):
        return self._FaceInfos

    @FaceInfos.setter
    def FaceInfos(self, FaceInfos):
        self._FaceInfos = FaceInfos

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        if params.get("FaceInfos") is not None:
            self._FaceInfos = []
            for item in params.get("FaceInfos"):
                obj = FaceInfo()
                obj._deserialize(item)
                self._FaceInfos.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class DetectLiveFaceRequest(AbstractModel):
    """DetectLiveFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M（图片的宽高比请接近3:4，不符合宽高比的图片返回的分值不具备参考意义）。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。 
（图片的宽高比请接近 3:4，不符合宽高比的图片返回的分值不具备参考意义） 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。

目前入参支持 “2.0”和“3.0“ 两个输入。

2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。

2020年11月26日后开通服务的账号仅支持输入“3.0”。

不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        """
        self._Image = None
        self._Url = None
        self._FaceModelVersion = None

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
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetectLiveFaceResponse(AbstractModel):
    """DetectLiveFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Score: 活体打分，取值范围 [0,100]，分数一般落于[80, 100]区间内，0分也为常见值。推荐相大于 87 时可判断为活体。可根据具体场景自行调整阈值。
本字段当且仅当FaceModelVersion为2.0时才具备参考意义。
        :type Score: float
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _IsLiveness: 活体检测是否通过。
本字段只有FaceModelVersion为3.0时才具备参考意义。
        :type IsLiveness: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Score = None
        self._FaceModelVersion = None
        self._IsLiveness = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def IsLiveness(self):
        return self._IsLiveness

    @IsLiveness.setter
    def IsLiveness(self, IsLiveness):
        self._IsLiveness = IsLiveness

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._IsLiveness = params.get("IsLiveness")
        self._RequestId = params.get("RequestId")


class Eye(AbstractModel):
    """眼睛信息

    """

    def __init__(self):
        r"""
        :param _Glass: 识别是否佩戴眼镜。
AttributeItem对应的Type为 —— 0：无眼镜，1：普通眼镜，2：墨镜
        :type Glass: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _EyeOpen: 识别眼睛的睁开、闭合状态。
AttributeItem对应的Type为 —— 0：睁开，1：闭眼
        :type EyeOpen: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _EyelidType: 识别是否双眼皮。
AttributeItem对应的Type为 —— 0：无，1：有。
        :type EyelidType: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _EyeSize: 眼睛大小。
AttributeItem对应的Type为 —— 0：小眼睛，1：普通眼睛，2：大眼睛。
        :type EyeSize: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        """
        self._Glass = None
        self._EyeOpen = None
        self._EyelidType = None
        self._EyeSize = None

    @property
    def Glass(self):
        return self._Glass

    @Glass.setter
    def Glass(self, Glass):
        self._Glass = Glass

    @property
    def EyeOpen(self):
        return self._EyeOpen

    @EyeOpen.setter
    def EyeOpen(self, EyeOpen):
        self._EyeOpen = EyeOpen

    @property
    def EyelidType(self):
        return self._EyelidType

    @EyelidType.setter
    def EyelidType(self, EyelidType):
        self._EyelidType = EyelidType

    @property
    def EyeSize(self):
        return self._EyeSize

    @EyeSize.setter
    def EyeSize(self, EyeSize):
        self._EyeSize = EyeSize


    def _deserialize(self, params):
        if params.get("Glass") is not None:
            self._Glass = AttributeItem()
            self._Glass._deserialize(params.get("Glass"))
        if params.get("EyeOpen") is not None:
            self._EyeOpen = AttributeItem()
            self._EyeOpen._deserialize(params.get("EyeOpen"))
        if params.get("EyelidType") is not None:
            self._EyelidType = AttributeItem()
            self._EyelidType._deserialize(params.get("EyelidType"))
        if params.get("EyeSize") is not None:
            self._EyeSize = AttributeItem()
            self._EyeSize._deserialize(params.get("EyeSize"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Eyebrow(AbstractModel):
    """眉毛信息

    """

    def __init__(self):
        r"""
        :param _EyebrowDensity: 眉毛浓密。
AttributeItem对应的Type为 —— 0：淡眉，1：浓眉。
        :type EyebrowDensity: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _EyebrowCurve: 眉毛弯曲。
AttributeItem对应的Type为 —— 0：不弯，1：弯眉。
        :type EyebrowCurve: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _EyebrowLength: 眉毛长短。
AttributeItem对应的Type为 —— 0：短眉毛，1：长眉毛。
        :type EyebrowLength: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        """
        self._EyebrowDensity = None
        self._EyebrowCurve = None
        self._EyebrowLength = None

    @property
    def EyebrowDensity(self):
        return self._EyebrowDensity

    @EyebrowDensity.setter
    def EyebrowDensity(self, EyebrowDensity):
        self._EyebrowDensity = EyebrowDensity

    @property
    def EyebrowCurve(self):
        return self._EyebrowCurve

    @EyebrowCurve.setter
    def EyebrowCurve(self, EyebrowCurve):
        self._EyebrowCurve = EyebrowCurve

    @property
    def EyebrowLength(self):
        return self._EyebrowLength

    @EyebrowLength.setter
    def EyebrowLength(self, EyebrowLength):
        self._EyebrowLength = EyebrowLength


    def _deserialize(self, params):
        if params.get("EyebrowDensity") is not None:
            self._EyebrowDensity = AttributeItem()
            self._EyebrowDensity._deserialize(params.get("EyebrowDensity"))
        if params.get("EyebrowCurve") is not None:
            self._EyebrowCurve = AttributeItem()
            self._EyebrowCurve._deserialize(params.get("EyebrowCurve"))
        if params.get("EyebrowLength") is not None:
            self._EyebrowLength = AttributeItem()
            self._EyebrowLength._deserialize(params.get("EyebrowLength"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceAttributesInfo(AbstractModel):
    """人脸属性信息，包含性别( gender )、年龄( age )、表情( expression )、
    魅力( beauty )、眼镜( glass )、口罩（mask）、头发（hair）和姿态 (pitch，roll，yaw )。只有当 NeedFaceAttributes 设为 1 时才返回有效信息，最多返回面积最大的 5 张人脸属性信息，超过 5 张人脸（第 6 张及以后的人脸）的 FaceAttributesInfo 不具备参考意义。

    """

    def __init__(self):
        r"""
        :param _Gender: 性别[0~49]为女性，[50，100]为男性，越接近0和100表示置信度越高。NeedFaceAttributes 不为 1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Gender: int
        :param _Age: 年龄 [0~100]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Age: int
        :param _Expression: 微笑[0(normal，正常))~100(laugh，大笑)]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Expression: int
        :param _Glass: 是否有眼镜 [true,false]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Glass: bool
        :param _Pitch: 上下偏移[-30,30]，单位角度。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。 
建议：人脸入库选择[-10,10]的图片。
        :type Pitch: int
        :param _Yaw: 左右偏移[-30,30]，单位角度。 NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。 
建议：人脸入库选择[-10,10]的图片。
        :type Yaw: int
        :param _Roll: 平面旋转[-180,180]，单位角度。 NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。  
建议：人脸入库选择[-20,20]的图片。
        :type Roll: int
        :param _Beauty: 魅力[0~100]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Beauty: int
        :param _Hat: 是否有帽子 [true,false]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hat: bool
        :param _Mask: 是否有口罩 [true,false]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mask: bool
        :param _Hair: 头发信息，包含头发长度（length）、有无刘海（bang）、头发颜色（color）。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hair: :class:`tencentcloud.iai.v20180301.models.FaceHairAttributesInfo`
        :param _EyeOpen: 双眼是否睁开 [true,false]。只要有超过一只眼睛闭眼，就返回false。 NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type EyeOpen: bool
        """
        self._Gender = None
        self._Age = None
        self._Expression = None
        self._Glass = None
        self._Pitch = None
        self._Yaw = None
        self._Roll = None
        self._Beauty = None
        self._Hat = None
        self._Mask = None
        self._Hair = None
        self._EyeOpen = None

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Expression(self):
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression

    @property
    def Glass(self):
        return self._Glass

    @Glass.setter
    def Glass(self, Glass):
        self._Glass = Glass

    @property
    def Pitch(self):
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch

    @property
    def Yaw(self):
        return self._Yaw

    @Yaw.setter
    def Yaw(self, Yaw):
        self._Yaw = Yaw

    @property
    def Roll(self):
        return self._Roll

    @Roll.setter
    def Roll(self, Roll):
        self._Roll = Roll

    @property
    def Beauty(self):
        return self._Beauty

    @Beauty.setter
    def Beauty(self, Beauty):
        self._Beauty = Beauty

    @property
    def Hat(self):
        return self._Hat

    @Hat.setter
    def Hat(self, Hat):
        self._Hat = Hat

    @property
    def Mask(self):
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def Hair(self):
        return self._Hair

    @Hair.setter
    def Hair(self, Hair):
        self._Hair = Hair

    @property
    def EyeOpen(self):
        return self._EyeOpen

    @EyeOpen.setter
    def EyeOpen(self, EyeOpen):
        self._EyeOpen = EyeOpen


    def _deserialize(self, params):
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Expression = params.get("Expression")
        self._Glass = params.get("Glass")
        self._Pitch = params.get("Pitch")
        self._Yaw = params.get("Yaw")
        self._Roll = params.get("Roll")
        self._Beauty = params.get("Beauty")
        self._Hat = params.get("Hat")
        self._Mask = params.get("Mask")
        if params.get("Hair") is not None:
            self._Hair = FaceHairAttributesInfo()
            self._Hair._deserialize(params.get("Hair"))
        self._EyeOpen = params.get("EyeOpen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceDetailAttributesInfo(AbstractModel):
    """人脸属性信息，根据 FaceAttributesType 输入的类型，返回年龄（Age）、颜值（Beauty）
    情绪（Emotion）、眼睛信息（Eye）、眉毛（Eyebrow）、性别（Gender）
    头发（Hair）、帽子（Hat）、姿态（Headpose）、口罩（Mask）、嘴巴（Mouse）、胡子（Moustache）
    鼻子（Nose）、脸型（Shape）、肤色（Skin）、微笑（Smile）等人脸属性信息。
    若 FaceAttributesType 没有输入相关类型，则FaceDetaiAttributesInfo返回的细项不具备参考意义。

    """

    def __init__(self):
        r"""
        :param _Age: 年龄 [0,65]，其中65代表“65岁及以上”。 
FaceAttributesType 不含Age 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Age: int
        :param _Beauty: 美丑打分[0,100]。 
FaceAttributesType 不含 Beauty 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Beauty: int
        :param _Emotion: 情绪，可识别自然、高兴、惊讶、生气、悲伤、厌恶、害怕。 
AttributeItem对应的Type为 —— 0：自然，1：高兴，2：惊讶，3：生气，4：悲伤，5：厌恶，6：害怕
FaceAttributesType 不含Emotion 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Emotion: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Eye: 眼睛相关信息，可识别是否戴眼镜、是否闭眼、是否双眼皮和眼睛大小。 
FaceAttributesType 不含Eye 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Eye: :class:`tencentcloud.iai.v20180301.models.Eye`
        :param _Eyebrow: 眉毛相关信息，可识别眉毛浓密、弯曲、长短信息。 
FaceAttributesType 不含Eyebrow 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Eyebrow: :class:`tencentcloud.iai.v20180301.models.Eyebrow`
        :param _Gender: 性别信息。 
AttributeItem对应的Type为 —— 	0：男性，1：女性。
FaceAttributesType 不含Gender 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Gender: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Hair: 头发信息，包含头发长度、有无刘海、头发颜色。 
FaceAttributesType 不含Hair 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Hair: :class:`tencentcloud.iai.v20180301.models.Hair`
        :param _Hat: 帽子信息，可识别是否佩戴帽子、帽子款式、帽子颜色。 
FaceAttributesType 不含Hat 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Hat: :class:`tencentcloud.iai.v20180301.models.Hat`
        :param _HeadPose: 姿态信息，包含人脸的上下偏移、左右偏移、平面旋转信息。 
FaceAttributesType 不含Headpose 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type HeadPose: :class:`tencentcloud.iai.v20180301.models.HeadPose`
        :param _Mask: 口罩佩戴信息。 
AttributeItem对应的Type为 —— 0: 无口罩， 1: 有口罩不遮脸，2: 有口罩遮下巴，3: 有口罩遮嘴，4: 正确佩戴口罩。
FaceAttributesType 不含Mask 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Mask: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Mouth: 嘴巴信息，可识别是否张嘴、嘴唇厚度。 
FaceAttributesType 不含 Mouth 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Mouth: :class:`tencentcloud.iai.v20180301.models.Mouth`
        :param _Moustache: 胡子信息。
AttributeItem对应的Type为 —— 0：无胡子，1：有胡子。 
FaceAttributesType 不含 Moustache 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Moustache: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Nose: 鼻子信息。 
AttributeItem对应的Type为 —— 0：朝天鼻，1：鹰钩鼻，2：普通，3：圆鼻头
FaceAttributesType 不含 Nose 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Nose: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Shape: 脸型信息。 
AttributeItem对应的Type为 —— 0：方脸，1：三角脸，2：鹅蛋脸，3：心形脸，4：圆脸。
FaceAttributesType 不含 Shape 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Shape: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Skin: 肤色信息。 
AttributeItem对应的Type为 —— 0：黄色皮肤，1：棕色皮肤，2：黑色皮肤，3：白色皮肤。
FaceAttributesType 不含 Skin 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Skin: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Smile: 微笑程度，[0,100]。 
FaceAttributesType 不含 Smile 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Smile: int
        """
        self._Age = None
        self._Beauty = None
        self._Emotion = None
        self._Eye = None
        self._Eyebrow = None
        self._Gender = None
        self._Hair = None
        self._Hat = None
        self._HeadPose = None
        self._Mask = None
        self._Mouth = None
        self._Moustache = None
        self._Nose = None
        self._Shape = None
        self._Skin = None
        self._Smile = None

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def Beauty(self):
        return self._Beauty

    @Beauty.setter
    def Beauty(self, Beauty):
        self._Beauty = Beauty

    @property
    def Emotion(self):
        return self._Emotion

    @Emotion.setter
    def Emotion(self, Emotion):
        self._Emotion = Emotion

    @property
    def Eye(self):
        return self._Eye

    @Eye.setter
    def Eye(self, Eye):
        self._Eye = Eye

    @property
    def Eyebrow(self):
        return self._Eyebrow

    @Eyebrow.setter
    def Eyebrow(self, Eyebrow):
        self._Eyebrow = Eyebrow

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Hair(self):
        return self._Hair

    @Hair.setter
    def Hair(self, Hair):
        self._Hair = Hair

    @property
    def Hat(self):
        return self._Hat

    @Hat.setter
    def Hat(self, Hat):
        self._Hat = Hat

    @property
    def HeadPose(self):
        return self._HeadPose

    @HeadPose.setter
    def HeadPose(self, HeadPose):
        self._HeadPose = HeadPose

    @property
    def Mask(self):
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def Mouth(self):
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def Moustache(self):
        return self._Moustache

    @Moustache.setter
    def Moustache(self, Moustache):
        self._Moustache = Moustache

    @property
    def Nose(self):
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def Shape(self):
        return self._Shape

    @Shape.setter
    def Shape(self, Shape):
        self._Shape = Shape

    @property
    def Skin(self):
        return self._Skin

    @Skin.setter
    def Skin(self, Skin):
        self._Skin = Skin

    @property
    def Smile(self):
        return self._Smile

    @Smile.setter
    def Smile(self, Smile):
        self._Smile = Smile


    def _deserialize(self, params):
        self._Age = params.get("Age")
        self._Beauty = params.get("Beauty")
        if params.get("Emotion") is not None:
            self._Emotion = AttributeItem()
            self._Emotion._deserialize(params.get("Emotion"))
        if params.get("Eye") is not None:
            self._Eye = Eye()
            self._Eye._deserialize(params.get("Eye"))
        if params.get("Eyebrow") is not None:
            self._Eyebrow = Eyebrow()
            self._Eyebrow._deserialize(params.get("Eyebrow"))
        if params.get("Gender") is not None:
            self._Gender = AttributeItem()
            self._Gender._deserialize(params.get("Gender"))
        if params.get("Hair") is not None:
            self._Hair = Hair()
            self._Hair._deserialize(params.get("Hair"))
        if params.get("Hat") is not None:
            self._Hat = Hat()
            self._Hat._deserialize(params.get("Hat"))
        if params.get("HeadPose") is not None:
            self._HeadPose = HeadPose()
            self._HeadPose._deserialize(params.get("HeadPose"))
        if params.get("Mask") is not None:
            self._Mask = AttributeItem()
            self._Mask._deserialize(params.get("Mask"))
        if params.get("Mouth") is not None:
            self._Mouth = Mouth()
            self._Mouth._deserialize(params.get("Mouth"))
        if params.get("Moustache") is not None:
            self._Moustache = AttributeItem()
            self._Moustache._deserialize(params.get("Moustache"))
        if params.get("Nose") is not None:
            self._Nose = AttributeItem()
            self._Nose._deserialize(params.get("Nose"))
        if params.get("Shape") is not None:
            self._Shape = AttributeItem()
            self._Shape._deserialize(params.get("Shape"))
        if params.get("Skin") is not None:
            self._Skin = AttributeItem()
            self._Skin._deserialize(params.get("Skin"))
        self._Smile = params.get("Smile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceDetailInfo(AbstractModel):
    """人脸信息列表。

    """

    def __init__(self):
        r"""
        :param _FaceRect: 检测出的人脸框位置。
        :type FaceRect: :class:`tencentcloud.iai.v20180301.models.FaceRect`
        :param _FaceDetailAttributesInfo: 人脸属性信息，根据 FaceAttributesType 输入的类型，返回年龄（Age）、颜值（Beauty） 
情绪（Emotion）、眼睛信息（Eye）、眉毛（Eyebrow）、性别（Gender） 
头发（Hair）、帽子（Hat）、姿态（Headpose）、口罩（Mask）、嘴巴（Mouth）、胡子（Moustache） 
鼻子（Nose）、脸型（Shape）、肤色（Skin）、微笑（Smile）等人脸属性信息。  
若 FaceAttributesType 没有输入相关类型，则FaceDetaiAttributesInfo返回的细项不具备参考意义。
        :type FaceDetailAttributesInfo: :class:`tencentcloud.iai.v20180301.models.FaceDetailAttributesInfo`
        """
        self._FaceRect = None
        self._FaceDetailAttributesInfo = None

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def FaceDetailAttributesInfo(self):
        return self._FaceDetailAttributesInfo

    @FaceDetailAttributesInfo.setter
    def FaceDetailAttributesInfo(self, FaceDetailAttributesInfo):
        self._FaceDetailAttributesInfo = FaceDetailAttributesInfo


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        if params.get("FaceDetailAttributesInfo") is not None:
            self._FaceDetailAttributesInfo = FaceDetailAttributesInfo()
            self._FaceDetailAttributesInfo._deserialize(params.get("FaceDetailAttributesInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceHairAttributesInfo(AbstractModel):
    """人脸属性中的发型信息。

    """

    def __init__(self):
        r"""
        :param _Length: 0：光头，1：短发，2：中发，3：长发，4：绑发
注意：此字段可能返回 null，表示取不到有效值。
        :type Length: int
        :param _Bang: 0：有刘海，1：无刘海
注意：此字段可能返回 null，表示取不到有效值。
        :type Bang: int
        :param _Color: 0：黑色，1：金色，2：棕色，3：灰白色
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: int
        """
        self._Length = None
        self._Bang = None
        self._Color = None

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Bang(self):
        return self._Bang

    @Bang.setter
    def Bang(self, Bang):
        self._Bang = Bang

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        self._Length = params.get("Length")
        self._Bang = params.get("Bang")
        self._Color = params.get("Color")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceInfo(AbstractModel):
    """人脸信息列表。

    """

    def __init__(self):
        r"""
        :param _X: 人脸框左上角横坐标。
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
        :type X: int
        :param _Y: 人脸框左上角纵坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
        :type Y: int
        :param _Width: 人脸框宽度。
        :type Width: int
        :param _Height: 人脸框高度。
        :type Height: int
        :param _FaceAttributesInfo: 人脸属性信息，包含性别( gender )、年龄( age )、表情( expression )、 
魅力( beauty )、眼镜( glass )、口罩（mask）、头发（hair）和姿态 (pitch，roll，yaw )。只有当 NeedFaceAttributes 设为 1 时才返回有效信息。
        :type FaceAttributesInfo: :class:`tencentcloud.iai.v20180301.models.FaceAttributesInfo`
        :param _FaceQualityInfo: 人脸质量信息，包含质量分（score）、模糊分（sharpness）、光照分（brightness）、遮挡分（completeness）。只有当NeedFaceDetection设为1时才返回有效信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceQualityInfo: :class:`tencentcloud.iai.v20180301.models.FaceQualityInfo`
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._FaceAttributesInfo = None
        self._FaceQualityInfo = None

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

    @property
    def FaceAttributesInfo(self):
        return self._FaceAttributesInfo

    @FaceAttributesInfo.setter
    def FaceAttributesInfo(self, FaceAttributesInfo):
        self._FaceAttributesInfo = FaceAttributesInfo

    @property
    def FaceQualityInfo(self):
        return self._FaceQualityInfo

    @FaceQualityInfo.setter
    def FaceQualityInfo(self, FaceQualityInfo):
        self._FaceQualityInfo = FaceQualityInfo


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        if params.get("FaceAttributesInfo") is not None:
            self._FaceAttributesInfo = FaceAttributesInfo()
            self._FaceAttributesInfo._deserialize(params.get("FaceAttributesInfo"))
        if params.get("FaceQualityInfo") is not None:
            self._FaceQualityInfo = FaceQualityInfo()
            self._FaceQualityInfo._deserialize(params.get("FaceQualityInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceQualityCompleteness(AbstractModel):
    """五官遮挡分，评价眉毛（Eyebrow）、眼睛（Eye）、鼻子（Nose）、脸颊（Cheek）、嘴巴（Mouth）、下巴（Chin）的被遮挡程度。

    """

    def __init__(self):
        r"""
        :param _Eyebrow: 眉毛的遮挡分数[0,100]，分数越高遮挡越少。 
参考范围：[0,80]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Eyebrow: int
        :param _Eye: 眼睛的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,80]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Eye: int
        :param _Nose: 鼻子的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,60]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Nose: int
        :param _Cheek: 脸颊的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,70]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cheek: int
        :param _Mouth: 嘴巴的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,50]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mouth: int
        :param _Chin: 下巴的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,70]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Chin: int
        """
        self._Eyebrow = None
        self._Eye = None
        self._Nose = None
        self._Cheek = None
        self._Mouth = None
        self._Chin = None

    @property
    def Eyebrow(self):
        return self._Eyebrow

    @Eyebrow.setter
    def Eyebrow(self, Eyebrow):
        self._Eyebrow = Eyebrow

    @property
    def Eye(self):
        return self._Eye

    @Eye.setter
    def Eye(self, Eye):
        self._Eye = Eye

    @property
    def Nose(self):
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def Cheek(self):
        return self._Cheek

    @Cheek.setter
    def Cheek(self, Cheek):
        self._Cheek = Cheek

    @property
    def Mouth(self):
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def Chin(self):
        return self._Chin

    @Chin.setter
    def Chin(self, Chin):
        self._Chin = Chin


    def _deserialize(self, params):
        self._Eyebrow = params.get("Eyebrow")
        self._Eye = params.get("Eye")
        self._Nose = params.get("Nose")
        self._Cheek = params.get("Cheek")
        self._Mouth = params.get("Mouth")
        self._Chin = params.get("Chin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceQualityInfo(AbstractModel):
    """人脸质量信息，包含质量分（score）、模糊分（sharpness）、光照分（brightness）、遮挡分（completeness）。只有当NeedFaceDetection设为1时才返回有效信息。

    """

    def __init__(self):
        r"""
        :param _Score: 质量分: [0,100]，综合评价图像质量是否适合人脸识别，分数越高质量越好。 
正常情况，只需要使用Score作为质量分总体的判断标准即可。Sharpness、Brightness、Completeness等细项分仅供参考。
参考范围：[0,40]较差，[40,60] 一般，[60,80]较好，[80,100]很好。 
建议：人脸入库选取70以上的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Sharpness: 清晰分：[0,100]，评价图片清晰程度，分数越高越清晰。 
参考范围：[0,40]特别模糊，[40,60]模糊，[60,80]一般，[80,100]清晰。 
建议：人脸入库选取80以上的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sharpness: int
        :param _Brightness: 光照分：[0,100]，评价图片光照程度，分数越高越亮。 
参考范围： [0,30]偏暗，[30,70]光照正常，[70,100]偏亮。 
建议：人脸入库选取[30,70]的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Brightness: int
        :param _Completeness: 五官遮挡分，评价眉毛（Eyebrow）、眼睛（Eye）、鼻子（Nose）、脸颊（Cheek）、嘴巴（Mouth）、下巴（Chin）的被遮挡程度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Completeness: :class:`tencentcloud.iai.v20180301.models.FaceQualityCompleteness`
        """
        self._Score = None
        self._Sharpness = None
        self._Brightness = None
        self._Completeness = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Sharpness(self):
        return self._Sharpness

    @Sharpness.setter
    def Sharpness(self, Sharpness):
        self._Sharpness = Sharpness

    @property
    def Brightness(self):
        return self._Brightness

    @Brightness.setter
    def Brightness(self, Brightness):
        self._Brightness = Brightness

    @property
    def Completeness(self):
        return self._Completeness

    @Completeness.setter
    def Completeness(self, Completeness):
        self._Completeness = Completeness


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._Sharpness = params.get("Sharpness")
        self._Brightness = params.get("Brightness")
        if params.get("Completeness") is not None:
            self._Completeness = FaceQualityCompleteness()
            self._Completeness._deserialize(params.get("Completeness"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    """检测出的人脸框的位置

    """

    def __init__(self):
        r"""
        :param _X: 人脸框左上角横坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
        :type X: int
        :param _Y: 人脸框左上角纵坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
        :type Y: int
        :param _Width: 人脸宽度
        :type Width: int
        :param _Height: 人脸高度
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
        


class FaceShape(AbstractModel):
    """五官定位（人脸关键点）具体信息。
    ![image](https://iai-face-demo-default-1254418846.cos.ap-guangzhou.myqcloud.com/130pts.jpg)

    """

    def __init__(self):
        r"""
        :param _FaceProfile: 描述脸型轮廓的 21 点。
        :type FaceProfile: list of Point
        :param _LeftEye: 描述左侧眼睛轮廓的 8 点。
        :type LeftEye: list of Point
        :param _RightEye: 描述右侧眼睛轮廓的 8 点。
        :type RightEye: list of Point
        :param _LeftEyeBrow: 描述左侧眉毛轮廓的 8 点。
        :type LeftEyeBrow: list of Point
        :param _RightEyeBrow: 描述右侧眉毛轮廓的 8 点。
        :type RightEyeBrow: list of Point
        :param _Mouth: 描述嘴巴轮廓的 22 点。
        :type Mouth: list of Point
        :param _Nose: 描述鼻子轮廓的 13 点。
        :type Nose: list of Point
        :param _LeftPupil: 左瞳孔轮廓的 1 个点。
        :type LeftPupil: list of Point
        :param _RightPupil: 右瞳孔轮廓的 1 个点。
        :type RightPupil: list of Point
        """
        self._FaceProfile = None
        self._LeftEye = None
        self._RightEye = None
        self._LeftEyeBrow = None
        self._RightEyeBrow = None
        self._Mouth = None
        self._Nose = None
        self._LeftPupil = None
        self._RightPupil = None

    @property
    def FaceProfile(self):
        return self._FaceProfile

    @FaceProfile.setter
    def FaceProfile(self, FaceProfile):
        self._FaceProfile = FaceProfile

    @property
    def LeftEye(self):
        return self._LeftEye

    @LeftEye.setter
    def LeftEye(self, LeftEye):
        self._LeftEye = LeftEye

    @property
    def RightEye(self):
        return self._RightEye

    @RightEye.setter
    def RightEye(self, RightEye):
        self._RightEye = RightEye

    @property
    def LeftEyeBrow(self):
        return self._LeftEyeBrow

    @LeftEyeBrow.setter
    def LeftEyeBrow(self, LeftEyeBrow):
        self._LeftEyeBrow = LeftEyeBrow

    @property
    def RightEyeBrow(self):
        return self._RightEyeBrow

    @RightEyeBrow.setter
    def RightEyeBrow(self, RightEyeBrow):
        self._RightEyeBrow = RightEyeBrow

    @property
    def Mouth(self):
        return self._Mouth

    @Mouth.setter
    def Mouth(self, Mouth):
        self._Mouth = Mouth

    @property
    def Nose(self):
        return self._Nose

    @Nose.setter
    def Nose(self, Nose):
        self._Nose = Nose

    @property
    def LeftPupil(self):
        return self._LeftPupil

    @LeftPupil.setter
    def LeftPupil(self, LeftPupil):
        self._LeftPupil = LeftPupil

    @property
    def RightPupil(self):
        return self._RightPupil

    @RightPupil.setter
    def RightPupil(self, RightPupil):
        self._RightPupil = RightPupil


    def _deserialize(self, params):
        if params.get("FaceProfile") is not None:
            self._FaceProfile = []
            for item in params.get("FaceProfile"):
                obj = Point()
                obj._deserialize(item)
                self._FaceProfile.append(obj)
        if params.get("LeftEye") is not None:
            self._LeftEye = []
            for item in params.get("LeftEye"):
                obj = Point()
                obj._deserialize(item)
                self._LeftEye.append(obj)
        if params.get("RightEye") is not None:
            self._RightEye = []
            for item in params.get("RightEye"):
                obj = Point()
                obj._deserialize(item)
                self._RightEye.append(obj)
        if params.get("LeftEyeBrow") is not None:
            self._LeftEyeBrow = []
            for item in params.get("LeftEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self._LeftEyeBrow.append(obj)
        if params.get("RightEyeBrow") is not None:
            self._RightEyeBrow = []
            for item in params.get("RightEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self._RightEyeBrow.append(obj)
        if params.get("Mouth") is not None:
            self._Mouth = []
            for item in params.get("Mouth"):
                obj = Point()
                obj._deserialize(item)
                self._Mouth.append(obj)
        if params.get("Nose") is not None:
            self._Nose = []
            for item in params.get("Nose"):
                obj = Point()
                obj._deserialize(item)
                self._Nose.append(obj)
        if params.get("LeftPupil") is not None:
            self._LeftPupil = []
            for item in params.get("LeftPupil"):
                obj = Point()
                obj._deserialize(item)
                self._LeftPupil.append(obj)
        if params.get("RightPupil") is not None:
            self._RightPupil = []
            for item in params.get("RightPupil"):
                obj = Point()
                obj._deserialize(item)
                self._RightPupil.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupInfoRequest(AbstractModel):
    """GetGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人员库 ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupInfoResponse(AbstractModel):
    """GetGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 人员库名称
        :type GroupName: str
        :param _GroupId: 人员库ID
        :type GroupId: str
        :param _GroupExDescriptions: 人员库自定义描述字段
        :type GroupExDescriptions: list of str
        :param _Tag: 人员库信息备注
        :type Tag: str
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。
        :type CreationTimestamp: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupName = None
        self._GroupId = None
        self._GroupExDescriptions = None
        self._Tag = None
        self._FaceModelVersion = None
        self._CreationTimestamp = None
        self._RequestId = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupExDescriptions(self):
        return self._GroupExDescriptions

    @GroupExDescriptions.setter
    def GroupExDescriptions(self, GroupExDescriptions):
        self._GroupExDescriptions = GroupExDescriptions

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def CreationTimestamp(self):
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        self._CreationTimestamp = CreationTimestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._GroupExDescriptions = params.get("GroupExDescriptions")
        self._Tag = params.get("Tag")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._CreationTimestamp = params.get("CreationTimestamp")
        self._RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始序号，默认值为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为1000
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupInfos: 返回的人员库信息
        :type GroupInfos: list of GroupInfo
        :param _GroupNum: 人员库总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupInfos = None
        self._GroupNum = None
        self._RequestId = None

    @property
    def GroupInfos(self):
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos

    @property
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        self._GroupNum = params.get("GroupNum")
        self._RequestId = params.get("RequestId")


class GetPersonBaseInfoRequest(AbstractModel):
    """GetPersonBaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        """
        self._PersonId = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonBaseInfoResponse(AbstractModel):
    """GetPersonBaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _Gender: 人员性别
        :type Gender: int
        :param _FaceIds: 包含的人脸 ID 列表
        :type FaceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonName = None
        self._Gender = None
        self._FaceIds = None
        self._RequestId = None

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def FaceIds(self):
        return self._FaceIds

    @FaceIds.setter
    def FaceIds(self, FaceIds):
        self._FaceIds = FaceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PersonName = params.get("PersonName")
        self._Gender = params.get("Gender")
        self._FaceIds = params.get("FaceIds")
        self._RequestId = params.get("RequestId")


class GetPersonGroupInfoRequest(AbstractModel):
    """GetPersonGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        :param _Offset: 起始序号，默认值为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为100
        :type Limit: int
        """
        self._PersonId = None
        self._Offset = None
        self._Limit = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonGroupInfoResponse(AbstractModel):
    """GetPersonGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonGroupInfos: 包含此人员的人员库及描述字段内容列表
        :type PersonGroupInfos: list of PersonGroupInfo
        :param _GroupNum: 人员库总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNum: int
        :param _FaceModelVersion: 人脸识别服务所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonGroupInfos = None
        self._GroupNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def PersonGroupInfos(self):
        return self._PersonGroupInfos

    @PersonGroupInfos.setter
    def PersonGroupInfos(self, PersonGroupInfos):
        self._PersonGroupInfos = PersonGroupInfos

    @property
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PersonGroupInfos") is not None:
            self._PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self._PersonGroupInfos.append(obj)
        self._GroupNum = params.get("GroupNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class GetPersonListNumRequest(AbstractModel):
    """GetPersonListNum请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人员库ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonListNumResponse(AbstractModel):
    """GetPersonListNum返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonNum: 人员数量
        :type PersonNum: int
        :param _FaceNum: 人脸数量
        :type FaceNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonNum = None
        self._FaceNum = None
        self._RequestId = None

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PersonNum = params.get("PersonNum")
        self._FaceNum = params.get("FaceNum")
        self._RequestId = params.get("RequestId")


class GetPersonListRequest(AbstractModel):
    """GetPersonList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人员库ID
        :type GroupId: str
        :param _Offset: 起始序号，默认值为0
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为1000
        :type Limit: int
        """
        self._GroupId = None
        self._Offset = None
        self._Limit = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPersonListResponse(AbstractModel):
    """GetPersonList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonInfos: 返回的人员信息
        :type PersonInfos: list of PersonInfo
        :param _PersonNum: 该人员库的人员数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonNum: int
        :param _FaceNum: 该人员库的人脸数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceNum: int
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonInfos = None
        self._PersonNum = None
        self._FaceNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def PersonInfos(self):
        return self._PersonInfos

    @PersonInfos.setter
    def PersonInfos(self, PersonInfos):
        self._PersonInfos = PersonInfos

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self._PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self._PersonInfos.append(obj)
        self._PersonNum = params.get("PersonNum")
        self._FaceNum = params.get("FaceNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class GetUpgradeGroupFaceModelVersionJobListRequest(AbstractModel):
    """GetUpgradeGroupFaceModelVersionJobList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 起始序号，默认值为0。
        :type Offset: int
        :param _Limit: 返回数量，默认值为10，最大值为1000。
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUpgradeGroupFaceModelVersionJobListResponse(AbstractModel):
    """GetUpgradeGroupFaceModelVersionJobList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobInfos: 人员库升级任务信息列表。
        :type JobInfos: list of UpgradeJobInfo
        :param _JobNum: 升级任务总数量。
        :type JobNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobInfos = None
        self._JobNum = None
        self._RequestId = None

    @property
    def JobInfos(self):
        return self._JobInfos

    @JobInfos.setter
    def JobInfos(self, JobInfos):
        self._JobInfos = JobInfos

    @property
    def JobNum(self):
        return self._JobNum

    @JobNum.setter
    def JobNum(self, JobNum):
        self._JobNum = JobNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("JobInfos") is not None:
            self._JobInfos = []
            for item in params.get("JobInfos"):
                obj = UpgradeJobInfo()
                obj._deserialize(item)
                self._JobInfos.append(obj)
        self._JobNum = params.get("JobNum")
        self._RequestId = params.get("RequestId")


class GetUpgradeGroupFaceModelVersionResultRequest(AbstractModel):
    """GetUpgradeGroupFaceModelVersionResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 升级任务ID，用于查询、获取人员库升级的进度和结果。
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
        


class GetUpgradeGroupFaceModelVersionResultResponse(AbstractModel):
    """GetUpgradeGroupFaceModelVersionResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTimestamp: 人员升级任务预估结束时间。 StartTimestamp的值是自 Unix 纪元时间到人员查重任务预估结束的毫秒数。  
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。 
如果为0表示这个任务已经执行完毕。
        :type EndTimestamp: int
        :param _Progress: 升级任务完成进度。取值[0.0，100.0]。
        :type Progress: float
        :param _Status: 0表示升级中，1表示升级完毕，2表示回滚完毕。
        :type Status: int
        :param _StartTime: 升级起始时间。 
StartTime的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。 
有关更多信息，请参阅 Unix 时间。
        :type StartTime: int
        :param _FromFaceModelVersion: 当前算法模型版本。
        :type FromFaceModelVersion: str
        :param _ToFaceModelVersion: 目标算法模型版本。
        :type ToFaceModelVersion: str
        :param _GroupId: 人员库ID。
        :type GroupId: str
        :param _FailedFacesUrl: 无法升级的人脸Id信息，文件格式为json。半小时有效
        :type FailedFacesUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EndTimestamp = None
        self._Progress = None
        self._Status = None
        self._StartTime = None
        self._FromFaceModelVersion = None
        self._ToFaceModelVersion = None
        self._GroupId = None
        self._FailedFacesUrl = None
        self._RequestId = None

    @property
    def EndTimestamp(self):
        return self._EndTimestamp

    @EndTimestamp.setter
    def EndTimestamp(self, EndTimestamp):
        self._EndTimestamp = EndTimestamp

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def FromFaceModelVersion(self):
        return self._FromFaceModelVersion

    @FromFaceModelVersion.setter
    def FromFaceModelVersion(self, FromFaceModelVersion):
        self._FromFaceModelVersion = FromFaceModelVersion

    @property
    def ToFaceModelVersion(self):
        return self._ToFaceModelVersion

    @ToFaceModelVersion.setter
    def ToFaceModelVersion(self, ToFaceModelVersion):
        self._ToFaceModelVersion = ToFaceModelVersion

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def FailedFacesUrl(self):
        return self._FailedFacesUrl

    @FailedFacesUrl.setter
    def FailedFacesUrl(self, FailedFacesUrl):
        self._FailedFacesUrl = FailedFacesUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EndTimestamp = params.get("EndTimestamp")
        self._Progress = params.get("Progress")
        self._Status = params.get("Status")
        self._StartTime = params.get("StartTime")
        self._FromFaceModelVersion = params.get("FromFaceModelVersion")
        self._ToFaceModelVersion = params.get("ToFaceModelVersion")
        self._GroupId = params.get("GroupId")
        self._FailedFacesUrl = params.get("FailedFacesUrl")
        self._RequestId = params.get("RequestId")


class GroupCandidate(AbstractModel):
    """分组识别结果Item

    """

    def __init__(self):
        r"""
        :param _GroupId: 人员库ID 。
        :type GroupId: str
        :param _Candidates: 识别出的最相似候选人。
        :type Candidates: list of Candidate
        """
        self._GroupId = None
        self._Candidates = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Candidates(self):
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Candidates") is not None:
            self._Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self._Candidates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupExDescriptionInfo(AbstractModel):
    """需要修改的人员库自定义描述字段key-value

    """

    def __init__(self):
        r"""
        :param _GroupExDescriptionIndex: 人员库自定义描述字段Index，从0开始
        :type GroupExDescriptionIndex: int
        :param _GroupExDescription: 需要更新的人员库自定义描述字段内容
        :type GroupExDescription: str
        """
        self._GroupExDescriptionIndex = None
        self._GroupExDescription = None

    @property
    def GroupExDescriptionIndex(self):
        return self._GroupExDescriptionIndex

    @GroupExDescriptionIndex.setter
    def GroupExDescriptionIndex(self, GroupExDescriptionIndex):
        self._GroupExDescriptionIndex = GroupExDescriptionIndex

    @property
    def GroupExDescription(self):
        return self._GroupExDescription

    @GroupExDescription.setter
    def GroupExDescription(self, GroupExDescription):
        self._GroupExDescription = GroupExDescription


    def _deserialize(self, params):
        self._GroupExDescriptionIndex = params.get("GroupExDescriptionIndex")
        self._GroupExDescription = params.get("GroupExDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfo(AbstractModel):
    """返回的人员库信息

    """

    def __init__(self):
        r"""
        :param _GroupName: 人员库名称
        :type GroupName: str
        :param _GroupId: 人员库ID
        :type GroupId: str
        :param _GroupExDescriptions: 人员库自定义描述字段
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupExDescriptions: list of str
        :param _Tag: 人员库信息备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param _CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。有关更多信息，请参阅 Unix 时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTimestamp: int
        """
        self._GroupName = None
        self._GroupId = None
        self._GroupExDescriptions = None
        self._Tag = None
        self._FaceModelVersion = None
        self._CreationTimestamp = None

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupExDescriptions(self):
        return self._GroupExDescriptions

    @GroupExDescriptions.setter
    def GroupExDescriptions(self, GroupExDescriptions):
        self._GroupExDescriptions = GroupExDescriptions

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def CreationTimestamp(self):
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        self._CreationTimestamp = CreationTimestamp


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupId = params.get("GroupId")
        self._GroupExDescriptions = params.get("GroupExDescriptions")
        self._Tag = params.get("Tag")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._CreationTimestamp = params.get("CreationTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hair(AbstractModel):
    """头发信息

    """

    def __init__(self):
        r"""
        :param _Length: 头发长度信息。
AttributeItem对应的Type为 —— 0：光头，1：短发，2：中发，3：长发，4：绑发。
        :type Length: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Bang: 刘海信息。
AttributeItem对应的Type为 —— 0：无刘海，1：有刘海。
        :type Bang: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Color: 头发颜色信息。
AttributeItem对应的Type为 —— 0：黑色，1：金色，2：棕色，3：灰白色。
        :type Color: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        """
        self._Length = None
        self._Bang = None
        self._Color = None

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Bang(self):
        return self._Bang

    @Bang.setter
    def Bang(self, Bang):
        self._Bang = Bang

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        if params.get("Length") is not None:
            self._Length = AttributeItem()
            self._Length._deserialize(params.get("Length"))
        if params.get("Bang") is not None:
            self._Bang = AttributeItem()
            self._Bang._deserialize(params.get("Bang"))
        if params.get("Color") is not None:
            self._Color = AttributeItem()
            self._Color._deserialize(params.get("Color"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hat(AbstractModel):
    """帽子信息

    """

    def __init__(self):
        r"""
        :param _Style: 帽子佩戴状态信息。
AttributeItem对应的Type为 —— 0：不戴帽子，1：普通帽子，2：头盔，3：保安帽。
        :type Style: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        :param _Color: 帽子颜色。
AttributeItem对应的Type为 —— 0：不戴帽子，1：红色系，2：黄色系，3：蓝色系，4：黑色系，5：灰白色系，6：混色系。
        :type Color: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        """
        self._Style = None
        self._Color = None

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, Color):
        self._Color = Color


    def _deserialize(self, params):
        if params.get("Style") is not None:
            self._Style = AttributeItem()
            self._Style._deserialize(params.get("Style"))
        if params.get("Color") is not None:
            self._Color = AttributeItem()
            self._Color._deserialize(params.get("Color"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadPose(AbstractModel):
    """姿态信息

    """

    def __init__(self):
        r"""
        :param _Pitch: 上下偏移[-30,30]。
        :type Pitch: int
        :param _Yaw: 左右偏移[-30,30]。
        :type Yaw: int
        :param _Roll: 平面旋转[-180,180]。
        :type Roll: int
        """
        self._Pitch = None
        self._Yaw = None
        self._Roll = None

    @property
    def Pitch(self):
        return self._Pitch

    @Pitch.setter
    def Pitch(self, Pitch):
        self._Pitch = Pitch

    @property
    def Yaw(self):
        return self._Yaw

    @Yaw.setter
    def Yaw(self, Yaw):
        self._Yaw = Yaw

    @property
    def Roll(self):
        return self._Roll

    @Roll.setter
    def Roll(self, Roll):
        self._Roll = Roll


    def _deserialize(self, params):
        self._Pitch = params.get("Pitch")
        self._Yaw = params.get("Yaw")
        self._Roll = params.get("Roll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人员库ID
        :type GroupId: str
        :param _GroupName: 人员库名称
        :type GroupName: str
        :param _GroupExDescriptionInfos: 需要修改的人员库自定义描述字段，key-value
        :type GroupExDescriptionInfos: list of GroupExDescriptionInfo
        :param _Tag: 人员库信息备注
        :type Tag: str
        """
        self._GroupId = None
        self._GroupName = None
        self._GroupExDescriptionInfos = None
        self._Tag = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupExDescriptionInfos(self):
        return self._GroupExDescriptionInfos

    @GroupExDescriptionInfos.setter
    def GroupExDescriptionInfos(self, GroupExDescriptionInfos):
        self._GroupExDescriptionInfos = GroupExDescriptionInfos

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("GroupExDescriptionInfos") is not None:
            self._GroupExDescriptionInfos = []
            for item in params.get("GroupExDescriptionInfos"):
                obj = GroupExDescriptionInfo()
                obj._deserialize(item)
                self._GroupExDescriptionInfos.append(obj)
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPersonBaseInfoRequest(AbstractModel):
    """ModifyPersonBaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人员ID
        :type PersonId: str
        :param _PersonName: 需要修改的人员名称
        :type PersonName: str
        :param _Gender: 需要修改的人员性别
        :type Gender: int
        """
        self._PersonId = None
        self._PersonName = None
        self._Gender = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._PersonName = params.get("PersonName")
        self._Gender = params.get("Gender")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonBaseInfoResponse(AbstractModel):
    """ModifyPersonBaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPersonGroupInfoRequest(AbstractModel):
    """ModifyPersonGroupInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 人员库ID
        :type GroupId: str
        :param _PersonId: 人员ID
        :type PersonId: str
        :param _PersonExDescriptionInfos: 需要修改的人员描述字段内容，key-value
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        """
        self._GroupId = None
        self._PersonId = None
        self._PersonExDescriptionInfos = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonExDescriptionInfos(self):
        return self._PersonExDescriptionInfos

    @PersonExDescriptionInfos.setter
    def PersonExDescriptionInfos(self, PersonExDescriptionInfos):
        self._PersonExDescriptionInfos = PersonExDescriptionInfos


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PersonId = params.get("PersonId")
        if params.get("PersonExDescriptionInfos") is not None:
            self._PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self._PersonExDescriptionInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonGroupInfoResponse(AbstractModel):
    """ModifyPersonGroupInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Mouth(AbstractModel):
    """嘴巴信息。

    """

    def __init__(self):
        r"""
        :param _MouthOpen: 是否张嘴信息。
AttributeItem对应的Type为 —— 0：不张嘴，1：张嘴。
        :type MouthOpen: :class:`tencentcloud.iai.v20180301.models.AttributeItem`
        """
        self._MouthOpen = None

    @property
    def MouthOpen(self):
        return self._MouthOpen

    @MouthOpen.setter
    def MouthOpen(self, MouthOpen):
        self._MouthOpen = MouthOpen


    def _deserialize(self, params):
        if params.get("MouthOpen") is not None:
            self._MouthOpen = AttributeItem()
            self._MouthOpen._deserialize(params.get("MouthOpen"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonExDescriptionInfo(AbstractModel):
    """需要修改的人员描述字段内容，key-value

    """

    def __init__(self):
        r"""
        :param _PersonExDescriptionIndex: 人员描述字段Index，从0开始
        :type PersonExDescriptionIndex: int
        :param _PersonExDescription: 需要更新的人员描述字段内容
        :type PersonExDescription: str
        """
        self._PersonExDescriptionIndex = None
        self._PersonExDescription = None

    @property
    def PersonExDescriptionIndex(self):
        return self._PersonExDescriptionIndex

    @PersonExDescriptionIndex.setter
    def PersonExDescriptionIndex(self, PersonExDescriptionIndex):
        self._PersonExDescriptionIndex = PersonExDescriptionIndex

    @property
    def PersonExDescription(self):
        return self._PersonExDescription

    @PersonExDescription.setter
    def PersonExDescription(self, PersonExDescription):
        self._PersonExDescription = PersonExDescription


    def _deserialize(self, params):
        self._PersonExDescriptionIndex = params.get("PersonExDescriptionIndex")
        self._PersonExDescription = params.get("PersonExDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonGroupInfo(AbstractModel):
    """包含此人员的人员库及描述字段内容列表

    """

    def __init__(self):
        r"""
        :param _GroupId: 包含此人员的人员库ID
        :type GroupId: str
        :param _PersonExDescriptions: 人员描述字段内容
        :type PersonExDescriptions: list of str
        """
        self._GroupId = None
        self._PersonExDescriptions = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PersonExDescriptions(self):
        return self._PersonExDescriptions

    @PersonExDescriptions.setter
    def PersonExDescriptions(self, PersonExDescriptions):
        self._PersonExDescriptions = PersonExDescriptions


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._PersonExDescriptions = params.get("PersonExDescriptions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """返回的人员信息

    """

    def __init__(self):
        r"""
        :param _PersonName: 人员名称
        :type PersonName: str
        :param _PersonId: 人员Id
        :type PersonId: str
        :param _Gender: 人员性别
        :type Gender: int
        :param _PersonExDescriptions: 人员描述字段内容
        :type PersonExDescriptions: list of str
        :param _FaceIds: 包含的人脸照片列表
        :type FaceIds: list of str
        :param _CreationTimestamp: 人员的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。有关更多信息，请参阅 Unix 时间。
        :type CreationTimestamp: int
        """
        self._PersonName = None
        self._PersonId = None
        self._Gender = None
        self._PersonExDescriptions = None
        self._FaceIds = None
        self._CreationTimestamp = None

    @property
    def PersonName(self):
        return self._PersonName

    @PersonName.setter
    def PersonName(self, PersonName):
        self._PersonName = PersonName

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def PersonExDescriptions(self):
        return self._PersonExDescriptions

    @PersonExDescriptions.setter
    def PersonExDescriptions(self, PersonExDescriptions):
        self._PersonExDescriptions = PersonExDescriptions

    @property
    def FaceIds(self):
        return self._FaceIds

    @FaceIds.setter
    def FaceIds(self, FaceIds):
        self._FaceIds = FaceIds

    @property
    def CreationTimestamp(self):
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        self._CreationTimestamp = CreationTimestamp


    def _deserialize(self, params):
        self._PersonName = params.get("PersonName")
        self._PersonId = params.get("PersonId")
        self._Gender = params.get("Gender")
        self._PersonExDescriptions = params.get("PersonExDescriptions")
        self._FaceIds = params.get("FaceIds")
        self._CreationTimestamp = params.get("CreationTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Point(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param _X: x坐标
        :type X: int
        :param _Y: Y坐标
        :type Y: int
        """
        self._X = None
        self._Y = None

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


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Result(AbstractModel):
    """人脸的识别结果

    """

    def __init__(self):
        r"""
        :param _Candidates: 识别出的最相似候选人
        :type Candidates: list of Candidate
        :param _FaceRect: 检测出的人脸框位置
        :type FaceRect: :class:`tencentcloud.iai.v20180301.models.FaceRect`
        :param _RetCode: 检测出的人脸图片状态返回码。0 表示正常。 
-1601代表不符合图片质量控制要求，此时Candidate内容为空。
        :type RetCode: int
        """
        self._Candidates = None
        self._FaceRect = None
        self._RetCode = None

    @property
    def Candidates(self):
        return self._Candidates

    @Candidates.setter
    def Candidates(self, Candidates):
        self._Candidates = Candidates

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self._Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self._Candidates.append(obj)
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        self._RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultsReturnsByGroup(AbstractModel):
    """识别结果。

    """

    def __init__(self):
        r"""
        :param _FaceRect: 检测出的人脸框位置。
        :type FaceRect: :class:`tencentcloud.iai.v20180301.models.FaceRect`
        :param _GroupCandidates: 识别结果。
        :type GroupCandidates: list of GroupCandidate
        :param _RetCode: 检测出的人脸图片状态返回码。0 表示正常。 
-1601代表不符合图片质量控制要求，此时Candidate内容为空。
        :type RetCode: int
        """
        self._FaceRect = None
        self._GroupCandidates = None
        self._RetCode = None

    @property
    def FaceRect(self):
        return self._FaceRect

    @FaceRect.setter
    def FaceRect(self, FaceRect):
        self._FaceRect = FaceRect

    @property
    def GroupCandidates(self):
        return self._GroupCandidates

    @GroupCandidates.setter
    def GroupCandidates(self, GroupCandidates):
        self._GroupCandidates = GroupCandidates

    @property
    def RetCode(self):
        return self._RetCode

    @RetCode.setter
    def RetCode(self, RetCode):
        self._RetCode = RetCode


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self._FaceRect = FaceRect()
            self._FaceRect._deserialize(params.get("FaceRect"))
        if params.get("GroupCandidates") is not None:
            self._GroupCandidates = []
            for item in params.get("GroupCandidates"):
                obj = GroupCandidate()
                obj._deserialize(item)
                self._GroupCandidates.append(obj)
        self._RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevertGroupFaceModelVersionRequest(AbstractModel):
    """RevertGroupFaceModelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 需要回滚的升级任务ID。
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
        


class RevertGroupFaceModelVersionResponse(AbstractModel):
    """RevertGroupFaceModelVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SearchFacesRequest(AbstractModel):
    """SearchFaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 希望搜索的人员库列表，上限100个。
        :type GroupIds: list of str
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。 
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。 
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param _MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34的人脸图片无法被识别。建议设置为80。
        :type MinFaceSize: int
        :param _MaxPersonNum: 单张被识别的人脸返回的最相似人员数量。默认值为5，最大值为100。 
例，设MaxFaceNum为1，MaxPersonNum为8，则返回Top8相似的人员信息。
值越大，需要处理的时间越长。建议不要超过10。
        :type MaxPersonNum: int
        :param _NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _FaceMatchThreshold: 出参Score中，只有超过FaceMatchThreshold值的结果才会返回。默认为0。
        :type FaceMatchThreshold: float
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNum = None
        self._NeedPersonInfo = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNum(self):
        return self._MaxPersonNum

    @MaxPersonNum.setter
    def MaxPersonNum(self, MaxPersonNum):
        self._MaxPersonNum = MaxPersonNum

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNum = params.get("MaxPersonNum")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFacesResponse(AbstractModel):
    """SearchFaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 识别结果。
        :type Results: list of Result
        :param _FaceNum: 搜索的人员库中包含的人脸数。
        :type FaceNum: int
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._FaceNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self._Results.append(obj)
        self._FaceNum = params.get("FaceNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class SearchFacesReturnsByGroupRequest(AbstractModel):
    """SearchFacesReturnsByGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 希望搜索的人员库列表，上限60个。
        :type GroupIds: list of str
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param _MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。
        :type MinFaceSize: int
        :param _MaxPersonNumPerGroup: 被检测到的人脸，对应最多返回的最相似人员数目。默认值为5，最大值为10。  
例，设MaxFaceNum为3，MaxPersonNumPerGroup为5，GroupIds长度为3，则最多可能返回3*5*3=45个人员。
        :type MaxPersonNumPerGroup: int
        :param _NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _FaceMatchThreshold: 出参Score中，只有大于等于FaceMatchThreshold值的结果才会返回。
默认为0。
取值范围[0.0,100.0) 。
        :type FaceMatchThreshold: float
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNumPerGroup = None
        self._NeedPersonInfo = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNumPerGroup(self):
        return self._MaxPersonNumPerGroup

    @MaxPersonNumPerGroup.setter
    def MaxPersonNumPerGroup(self, MaxPersonNumPerGroup):
        self._MaxPersonNumPerGroup = MaxPersonNumPerGroup

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchFacesReturnsByGroupResponse(AbstractModel):
    """SearchFacesReturnsByGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FaceNum: 搜索的人员库中包含的人脸数。
        :type FaceNum: int
        :param _ResultsReturnsByGroup: 识别结果。
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FaceNum = None
        self._ResultsReturnsByGroup = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def FaceNum(self):
        return self._FaceNum

    @FaceNum.setter
    def FaceNum(self, FaceNum):
        self._FaceNum = FaceNum

    @property
    def ResultsReturnsByGroup(self):
        return self._ResultsReturnsByGroup

    @ResultsReturnsByGroup.setter
    def ResultsReturnsByGroup(self, ResultsReturnsByGroup):
        self._ResultsReturnsByGroup = ResultsReturnsByGroup

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FaceNum = params.get("FaceNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self._ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self._ResultsReturnsByGroup.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class SearchPersonsRequest(AbstractModel):
    """SearchPersons请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 希望搜索的人员库列表，上限100个。
        :type GroupIds: list of str
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param _MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。
        :type MinFaceSize: int
        :param _MaxPersonNum: 单张被识别的人脸返回的最相似人员数量。默认值为5，最大值为100。
例，设MaxFaceNum为1，MaxPersonNum为8，则返回Top8相似的人员信息。
值越大，需要处理的时间越长。建议不要超过10。
        :type MaxPersonNum: int
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _FaceMatchThreshold: 出参Score中，只有大于等于FaceMatchThreshold值的结果才会返回。默认为0。取值范围[0.0,100.0) 。
        :type FaceMatchThreshold: float
        :param _NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNum = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedPersonInfo = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNum(self):
        return self._MaxPersonNum

    @MaxPersonNum.setter
    def MaxPersonNum(self, MaxPersonNum):
        self._MaxPersonNum = MaxPersonNum

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNum = params.get("MaxPersonNum")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchPersonsResponse(AbstractModel):
    """SearchPersons返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 识别结果。
        :type Results: list of Result
        :param _PersonNum: 搜索的人员库中包含的人员数。若输入图片中所有人脸均不符合质量要求，则返回0。
        :type PersonNum: int
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._PersonNum = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self._Results.append(obj)
        self._PersonNum = params.get("PersonNum")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class SearchPersonsReturnsByGroupRequest(AbstractModel):
    """SearchPersonsReturnsByGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 希望搜索的人员库列表，上限60个。
        :type GroupIds: list of str
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param _MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。
        :type MinFaceSize: int
        :param _MaxPersonNumPerGroup: 被检测到的人脸，对应最多返回的最相似人员数目。默认值为5，最大值为10。  
例，设MaxFaceNum为3，MaxPersonNumPerGroup为5，GroupIds长度为3，则最多可能返回3*5*3=45个人员。
        :type MaxPersonNumPerGroup: int
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _FaceMatchThreshold: 出参Score中，只有超过FaceMatchThreshold值的结果才会返回。默认为0。
        :type FaceMatchThreshold: float
        :param _NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._GroupIds = None
        self._Image = None
        self._Url = None
        self._MaxFaceNum = None
        self._MinFaceSize = None
        self._MaxPersonNumPerGroup = None
        self._QualityControl = None
        self._FaceMatchThreshold = None
        self._NeedPersonInfo = None
        self._NeedRotateDetection = None

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

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
    def MaxFaceNum(self):
        return self._MaxFaceNum

    @MaxFaceNum.setter
    def MaxFaceNum(self, MaxFaceNum):
        self._MaxFaceNum = MaxFaceNum

    @property
    def MinFaceSize(self):
        return self._MinFaceSize

    @MinFaceSize.setter
    def MinFaceSize(self, MinFaceSize):
        self._MinFaceSize = MinFaceSize

    @property
    def MaxPersonNumPerGroup(self):
        return self._MaxPersonNumPerGroup

    @MaxPersonNumPerGroup.setter
    def MaxPersonNumPerGroup(self, MaxPersonNumPerGroup):
        self._MaxPersonNumPerGroup = MaxPersonNumPerGroup

    @property
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def FaceMatchThreshold(self):
        return self._FaceMatchThreshold

    @FaceMatchThreshold.setter
    def FaceMatchThreshold(self, FaceMatchThreshold):
        self._FaceMatchThreshold = FaceMatchThreshold

    @property
    def NeedPersonInfo(self):
        return self._NeedPersonInfo

    @NeedPersonInfo.setter
    def NeedPersonInfo(self, NeedPersonInfo):
        self._NeedPersonInfo = NeedPersonInfo

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._MaxFaceNum = params.get("MaxFaceNum")
        self._MinFaceSize = params.get("MinFaceSize")
        self._MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self._QualityControl = params.get("QualityControl")
        self._FaceMatchThreshold = params.get("FaceMatchThreshold")
        self._NeedPersonInfo = params.get("NeedPersonInfo")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchPersonsReturnsByGroupResponse(AbstractModel):
    """SearchPersonsReturnsByGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonNum: 搜索的人员库中包含的人员数。若输入图片中所有人脸均不符合质量要求，则返回0。
        :type PersonNum: int
        :param _ResultsReturnsByGroup: 识别结果。
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonNum = None
        self._ResultsReturnsByGroup = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def PersonNum(self):
        return self._PersonNum

    @PersonNum.setter
    def PersonNum(self, PersonNum):
        self._PersonNum = PersonNum

    @property
    def ResultsReturnsByGroup(self):
        return self._ResultsReturnsByGroup

    @ResultsReturnsByGroup.setter
    def ResultsReturnsByGroup(self, ResultsReturnsByGroup):
        self._ResultsReturnsByGroup = ResultsReturnsByGroup

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PersonNum = params.get("PersonNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self._ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self._ResultsReturnsByGroup.append(obj)
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class UpgradeGroupFaceModelVersionRequest(AbstractModel):
    """UpgradeGroupFaceModelVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 需要升级的人员库ID。
        :type GroupId: str
        :param _FaceModelVersion: 需要升级至的算法模型版本。默认为最新版本。不可逆向升级
        :type FaceModelVersion: str
        """
        self._GroupId = None
        self._FaceModelVersion = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._FaceModelVersion = params.get("FaceModelVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeGroupFaceModelVersionResponse(AbstractModel):
    """UpgradeGroupFaceModelVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 升级任务ID，用于查询、获取升级的进度和结果。
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


class UpgradeJobInfo(AbstractModel):
    """人员库升级任务信息

    """

    def __init__(self):
        r"""
        :param _JobId: 人员库升级任务ID，用于查询、获取升级的进度和结果。
        :type JobId: str
        :param _GroupId: 人员库ID。
        :type GroupId: str
        :param _FromFaceModelVersion: 当前算法模型版本。
        :type FromFaceModelVersion: str
        :param _ToFaceModelVersion: 目标算法模型版本。
        :type ToFaceModelVersion: str
        :param _StartTime: 升级起始时间。 
StartTime的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。 
有关更多信息，请参阅 Unix 时间。
        :type StartTime: int
        :param _Status: 0表示升级中，1表示升级完毕，2表示回滚完毕。
        :type Status: int
        """
        self._JobId = None
        self._GroupId = None
        self._FromFaceModelVersion = None
        self._ToFaceModelVersion = None
        self._StartTime = None
        self._Status = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def FromFaceModelVersion(self):
        return self._FromFaceModelVersion

    @FromFaceModelVersion.setter
    def FromFaceModelVersion(self, FromFaceModelVersion):
        self._FromFaceModelVersion = FromFaceModelVersion

    @property
    def ToFaceModelVersion(self):
        return self._ToFaceModelVersion

    @ToFaceModelVersion.setter
    def ToFaceModelVersion(self, ToFaceModelVersion):
        self._ToFaceModelVersion = ToFaceModelVersion

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._GroupId = params.get("GroupId")
        self._FromFaceModelVersion = params.get("FromFaceModelVersion")
        self._ToFaceModelVersion = params.get("ToFaceModelVersion")
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyFaceRequest(AbstractModel):
    """VerifyFace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 待验证的人员ID。人员ID具体信息请参考人员库管理相关接口。
        :type PersonId: str
        :param _Image: 图片 base64 数据，base64 编码后大小不可超过5M。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._PersonId = None
        self._Image = None
        self._Url = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

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
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyFaceResponse(AbstractModel):
    """VerifyFace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Score: 给定的人脸图片与 PersonId 对应人脸的相似度。若 PersonId 下有多张人脸（Face），返回相似度最大的分数。

不同算法版本返回的相似度分数不同。
若需要验证两张图片中人脸是否为同一人，3.0版本误识率千分之一对应分数为40分，误识率万分之一对应分数为50分，误识率十万分之一对应分数为60分。 一般超过50分则可认定为同一人。
2.0版本误识率千分之一对应分数为70分，误识率万分之一对应分数为80分，误识率十万分之一对应分数为90分。 一般超过80分则可认定为同一人。
        :type Score: float
        :param _IsMatch: 是否为同一人判断，固定阈值分数为60分，若想更灵活地调整阈值可取Score参数返回进行判断
        :type IsMatch: bool
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Score = None
        self._IsMatch = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def IsMatch(self):
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._IsMatch = params.get("IsMatch")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")


class VerifyPersonRequest(AbstractModel):
    """VerifyPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 待验证的人员ID。人员ID具体信息请参考人员库管理相关接口。
        :type PersonId: str
        :param _Image: 图片 base64 数据。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param _Url: 图片的 Url 。 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param _QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param _NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self._PersonId = None
        self._Image = None
        self._Url = None
        self._QualityControl = None
        self._NeedRotateDetection = None

    @property
    def PersonId(self):
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

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
    def QualityControl(self):
        return self._QualityControl

    @QualityControl.setter
    def QualityControl(self, QualityControl):
        self._QualityControl = QualityControl

    @property
    def NeedRotateDetection(self):
        return self._NeedRotateDetection

    @NeedRotateDetection.setter
    def NeedRotateDetection(self, NeedRotateDetection):
        self._NeedRotateDetection = NeedRotateDetection


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Image = params.get("Image")
        self._Url = params.get("Url")
        self._QualityControl = params.get("QualityControl")
        self._NeedRotateDetection = params.get("NeedRotateDetection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyPersonResponse(AbstractModel):
    """VerifyPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Score: 给定的人脸照片与 PersonId 对应的相似度。若 PersonId 下有多张人脸（Face），会融合多张人脸信息进行验证。
        :type Score: float
        :param _IsMatch: 是否为同一人的判断。
        :type IsMatch: bool
        :param _FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Score = None
        self._IsMatch = None
        self._FaceModelVersion = None
        self._RequestId = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def IsMatch(self):
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def FaceModelVersion(self):
        return self._FaceModelVersion

    @FaceModelVersion.setter
    def FaceModelVersion(self, FaceModelVersion):
        self._FaceModelVersion = FaceModelVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._IsMatch = params.get("IsMatch")
        self._FaceModelVersion = params.get("FaceModelVersion")
        self._RequestId = params.get("RequestId")