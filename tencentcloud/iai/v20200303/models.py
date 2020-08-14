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


class AnalyzeDenseLandmarksRequest(AbstractModel):
    """AnalyzeDenseLandmarks请求参数结构体

    """

    def __init__(self):
        """
        :param Mode: 检测模式。0 为检测所有出现的人脸， 1 为检测面积最大的人脸。 
默认为 0。 
最多返回 5 张人脸的五官定位（人脸关键点）具体信息。
        :type Mode: int
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。  
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。  
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。本接口仅支持 “3.0“ 输入。
        :type FaceModelVersion: str
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.Mode = None
        self.Image = None
        self.Url = None
        self.FaceModelVersion = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class AnalyzeDenseLandmarksResponse(AbstractModel):
    """AnalyzeDenseLandmarks返回参数结构体

    """

    def __init__(self):
        """
        :param ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param DenseFaceShapeSet: 稠密人脸关键点具体信息。
        :type DenseFaceShapeSet: list of DenseFaceShape
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。本接口仅支持 “3.0“ 输入。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.DenseFaceShapeSet = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("DenseFaceShapeSet") is not None:
            self.DenseFaceShapeSet = []
            for item in params.get("DenseFaceShapeSet"):
                obj = DenseFaceShape()
                obj._deserialize(item)
                self.DenseFaceShapeSet.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class AnalyzeFaceRequest(AbstractModel):
    """AnalyzeFace请求参数结构体

    """

    def __init__(self):
        """
        :param Mode: 检测模式。0 为检测所有出现的人脸， 1 为检测面积最大的人脸。默认为 0。最多返回 10 张人脸的五官定位（人脸关键点）具体信息。
        :type Mode: int
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。  
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。  
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用最新版本。
        :type FaceModelVersion: str
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.Mode = None
        self.Image = None
        self.Url = None
        self.FaceModelVersion = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class AnalyzeFaceResponse(AbstractModel):
    """AnalyzeFace返回参数结构体

    """

    def __init__(self):
        """
        :param ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param FaceShapeSet: 五官定位（人脸关键点）具体信息。
        :type FaceShapeSet: list of FaceShape
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceShapeSet = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("FaceShapeSet") is not None:
            self.FaceShapeSet = []
            for item in params.get("FaceShapeSet"):
                obj = FaceShape()
                obj._deserialize(item)
                self.FaceShapeSet.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class AttributeItem(AbstractModel):
    """人脸属性信息

    """

    def __init__(self):
        """
        :param Type: 属性值
        :type Type: int
        :param Probability: Type识别概率值，【0,1】,代表判断正确的概率。
        :type Probability: float
        """
        self.Type = None
        self.Probability = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Probability = params.get("Probability")


class Candidate(AbstractModel):
    """识别出的最相似候选人

    """

    def __init__(self):
        """
        :param PersonId: 人员ID
        :type PersonId: str
        :param FaceId: 人脸ID
        :type FaceId: str
        :param Score: 候选者的匹配得分。 

1万大小人脸底库下，误识率百分之一对应分数为70分，误识率千分之一对应分数为80分，误识率万分之一对应分数为90分；
10万大小人脸底库下，误识率百分之一对应分数为80分，误识率千分之一对应分数为90分，误识率万分之一对应分数为100分；
30万大小人脸底库下，误识率百分之一对应分数为85分，误识率千分之一对应分数为95分。

一般80分左右可适用大部分场景，建议分数不要超过90分。您可以根据实际情况选择合适的分数。
        :type Score: float
        :param PersonName: 人员名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonName: str
        :param Gender: 人员性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Gender: int
        :param PersonGroupInfos: 包含此人员的人员库及描述字段内容列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonGroupInfos: list of PersonGroupInfo
        """
        self.PersonId = None
        self.FaceId = None
        self.Score = None
        self.PersonName = None
        self.Gender = None
        self.PersonGroupInfos = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.FaceId = params.get("FaceId")
        self.Score = params.get("Score")
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")
        if params.get("PersonGroupInfos") is not None:
            self.PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self.PersonGroupInfos.append(obj)


class CheckSimilarPersonRequest(AbstractModel):
    """CheckSimilarPerson请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIds: 待整理的人员库列表。 
人员库总人数不可超过200万，人员库个数不可超过10个。
数组元素取值为创建人员库接口中的GroupId
        :type GroupIds: list of str
        :param UniquePersonControl: 人员查重整理力度的控制。
1：力度较高的档案整理，能够消除更多的重复身份，对应稍高的非重复身份误清除率；
2：力度较低的档案整理，非重复身份的误清除率较低，对应稍低的重复身份消除率。
        :type UniquePersonControl: int
        """
        self.GroupIds = None
        self.UniquePersonControl = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.UniquePersonControl = params.get("UniquePersonControl")


class CheckSimilarPersonResponse(AbstractModel):
    """CheckSimilarPerson返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 查重任务ID，用于查询、获取查重的进度和结果。
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CompareFaceRequest(AbstractModel):
    """CompareFace请求参数结构体

    """

    def __init__(self):
        """
        :param ImageA: A 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageA: str
        :param ImageB: B 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageB: str
        :param UrlA: A 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
A 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type UrlA: str
        :param UrlB: B 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
B 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type UrlB: str
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。 
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.ImageA = None
        self.ImageB = None
        self.UrlA = None
        self.UrlB = None
        self.FaceModelVersion = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.ImageA = params.get("ImageA")
        self.ImageB = params.get("ImageB")
        self.UrlA = params.get("UrlA")
        self.UrlB = params.get("UrlB")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CompareFaceResponse(AbstractModel):
    """CompareFace返回参数结构体

    """

    def __init__(self):
        """
        :param Score: 两张图片中人脸的相似度分数。
不同算法版本返回的相似度分数不同。 
若需要验证两张图片中人脸是否为同一人，3.0版本误识率千分之一对应分数为40分，误识率万分之一对应分数为50分，误识率十万分之一对应分数为60分。  一般超过50分则可认定为同一人。 
2.0版本误识率千分之一对应分数为70分，误识率万分之一对应分数为80分，误识率十万分之一对应分数为90分。 一般超过80分则可认定为同一人。 
若需要验证两张图片中的人脸是否为同一人，建议使用人脸验证接口。
        :type Score: float
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CopyPersonRequest(AbstractModel):
    """CopyPerson请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        :param GroupIds: 待加入的人员库列表，数组元素取值为创建人员库接口中的GroupId
        :type GroupIds: list of str
        """
        self.PersonId = None
        self.GroupIds = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.GroupIds = params.get("GroupIds")


class CopyPersonResponse(AbstractModel):
    """CopyPerson返回参数结构体

    """

    def __init__(self):
        """
        :param SucGroupNum: 成功加入的人员库数量
        :type SucGroupNum: int
        :param SucGroupIds: 成功加入的人员库列表
        :type SucGroupIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SucGroupNum = None
        self.SucGroupIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucGroupNum = params.get("SucGroupNum")
        self.SucGroupIds = params.get("SucGroupIds")
        self.RequestId = params.get("RequestId")


class CreateFaceRequest(AbstractModel):
    """CreateFace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        :param Images: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
人员人脸总数量不可超过5张。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param Urls: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
人员人脸总数量不可超过5张。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
        :type Urls: list of str
        :param FaceMatchThreshold: 只有和该人员已有的人脸相似度超过FaceMatchThreshold值的人脸，才能增加人脸成功。 
默认值60分。取值范围[0,100] 。
        :type FaceMatchThreshold: float
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.PersonId = None
        self.Images = None
        self.Urls = None
        self.FaceMatchThreshold = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CreateFaceResponse(AbstractModel):
    """CreateFace返回参数结构体

    """

    def __init__(self):
        """
        :param SucFaceNum: 加入成功的人脸数量
        :type SucFaceNum: int
        :param SucFaceIds: 加入成功的人脸ID列表
        :type SucFaceIds: list of str
        :param RetCode: 每张人脸图片添加结果，-1101 代表未检测到人脸，-1102 代表图片解码失败， 
-1601代表不符合图片质量控制要求, -1604 代表人脸相似度没有超过FaceMatchThreshold。 
其他非 0 值代表算法服务异常。 
RetCode的顺序和入参中 Images 或 Urls 的顺序一致。
        :type RetCode: list of int
        :param SucIndexes: 加入成功的人脸索引。索引顺序和入参中 Images 或 Urls 的顺序一致。 
例， Urls 中 有 3 个 url，第二个 url 失败，则 SucIndexes 值为 [0,2] 。
        :type SucIndexes: list of int non-negative
        :param SucFaceRects: 加入成功的人脸框位置。顺序和入参中 Images 或 Urls 的顺序一致。
        :type SucFaceRects: list of FaceRect
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SucFaceNum = None
        self.SucFaceIds = None
        self.RetCode = None
        self.SucIndexes = None
        self.SucFaceRects = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucFaceNum = params.get("SucFaceNum")
        self.SucFaceIds = params.get("SucFaceIds")
        self.RetCode = params.get("RetCode")
        self.SucIndexes = params.get("SucIndexes")
        if params.get("SucFaceRects") is not None:
            self.SucFaceRects = []
            for item in params.get("SucFaceRects"):
                obj = FaceRect()
                obj._deserialize(item)
                self.SucFaceRects.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 人员库名称，[1,60]个字符，可修改，不可重复。
        :type GroupName: str
        :param GroupId: 人员库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :type GroupId: str
        :param GroupExDescriptions: 人员库自定义描述字段，用于描述人员库中人员属性，该人员库下所有人员将拥有此描述字段。 
最多可以创建5个。 
每个自定义描述字段支持[1,30]个字符。 
在同一人员库中自定义描述字段不可重复。 
例： 设置某人员库“自定义描述字段”为["学号","工号","手机号"]， 
则该人员库下所有人员将拥有名为“学号”、“工号”、“手机号”的描述字段， 
可在对应人员描述字段中填写内容，登记该人员的学号、工号、手机号等信息。
        :type GroupExDescriptions: list of str
        :param Tag: 人员库信息备注，[0，40]个字符。
        :type Tag: str
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 待加入的人员库ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        :param PersonName: 人员名称。[1，60]个字符，可修改，可重复。
        :type PersonName: str
        :param PersonId: 人员ID，单个腾讯云账号下不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :type PersonId: str
        :param Gender: 0代表未填写，1代表男性，2代表女性。
        :type Gender: int
        :param PersonExDescriptionInfos: 人员描述字段内容，key-value。[0，60]个字符，可修改，可重复。
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param UniquePersonControl: 此参数用于控制判断 Image 或 Url 中图片包含的人脸，是否在人员库中已有疑似的同一人。 
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
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupId = None
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptionInfos = None
        self.Image = None
        self.Url = None
        self.UniquePersonControl = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        if params.get("PersonExDescriptionInfos") is not None:
            self.PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self.PersonExDescriptionInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.UniquePersonControl = params.get("UniquePersonControl")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        """
        :param FaceId: 人脸图片唯一标识。
        :type FaceId: str
        :param FaceRect: 检测出的人脸框的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param SimilarPersonId: 疑似同一人的PersonId。 
当 UniquePersonControl 参数不为0且人员库中有疑似的同一人，此参数才有意义。
        :type SimilarPersonId: str
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceId = None
        self.FaceRect = None
        self.SimilarPersonId = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.SimilarPersonId = params.get("SimilarPersonId")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class DeleteFaceRequest(AbstractModel):
    """DeleteFace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        :param FaceIds: 待删除的人脸ID列表，数组元素取值为增加人脸接口返回的FaceId
        :type FaceIds: list of str
        """
        self.PersonId = None
        self.FaceIds = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.FaceIds = params.get("FaceIds")


class DeleteFaceResponse(AbstractModel):
    """DeleteFace返回参数结构体

    """

    def __init__(self):
        """
        :param SucDeletedNum: 删除成功的人脸数量
        :type SucDeletedNum: int
        :param SucFaceIds: 删除成功的人脸ID列表
        :type SucFaceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SucDeletedNum = None
        self.SucFaceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucDeletedNum = params.get("SucDeletedNum")
        self.SucFaceIds = params.get("SucFaceIds")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人员库ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonFromGroupRequest(AbstractModel):
    """DeletePersonFromGroup请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        :param GroupId: 人员库ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        """
        self.PersonId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.GroupId = params.get("GroupId")


class DeletePersonFromGroupResponse(AbstractModel):
    """DeletePersonFromGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DenseFaceShape(AbstractModel):
    """稠密关键点详细信息

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
        :param LeftEye: 描述左侧眼睛轮廓的 XX 点。
        :type LeftEye: list of Point
        :param RightEye: 描述右侧眼睛轮廓的 XX 点。
        :type RightEye: list of Point
        :param LeftEyeBrow: 描述左侧眉毛轮廓的 XX 点。
        :type LeftEyeBrow: list of Point
        :param RightEyeBrow: 描述右侧眉毛轮廓的 XX 点。
        :type RightEyeBrow: list of Point
        :param MouthOutside: 描述外嘴巴轮廓的 XX 点， 从左侧开始逆时针返回。
        :type MouthOutside: list of Point
        :param MouthInside: 描述内嘴巴轮廓的 XX 点，从左侧开始逆时针返回。
        :type MouthInside: list of Point
        :param Nose: 描述鼻子轮廓的 XX 点。
        :type Nose: list of Point
        :param LeftPupil: 左瞳孔轮廓的 XX 个点。
        :type LeftPupil: list of Point
        :param RightPupil: 右瞳孔轮廓的 XX 个点。
        :type RightPupil: list of Point
        :param CentralAxis: 中轴线轮廓的 XX 个点。
        :type CentralAxis: list of Point
        :param Chin: 下轮廓的 XX 个点。
        :type Chin: list of Point
        :param LeftEyeBags: 左眼袋的 XX 个点。
        :type LeftEyeBags: list of Point
        :param RightEyeBags: 右眼袋的 XX 个点。
        :type RightEyeBags: list of Point
        :param Forehead: 额头的 XX 个点。
        :type Forehead: list of Point
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.LeftEye = None
        self.RightEye = None
        self.LeftEyeBrow = None
        self.RightEyeBrow = None
        self.MouthOutside = None
        self.MouthInside = None
        self.Nose = None
        self.LeftPupil = None
        self.RightPupil = None
        self.CentralAxis = None
        self.Chin = None
        self.LeftEyeBags = None
        self.RightEyeBags = None
        self.Forehead = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("LeftEye") is not None:
            self.LeftEye = []
            for item in params.get("LeftEye"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEye.append(obj)
        if params.get("RightEye") is not None:
            self.RightEye = []
            for item in params.get("RightEye"):
                obj = Point()
                obj._deserialize(item)
                self.RightEye.append(obj)
        if params.get("LeftEyeBrow") is not None:
            self.LeftEyeBrow = []
            for item in params.get("LeftEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEyeBrow.append(obj)
        if params.get("RightEyeBrow") is not None:
            self.RightEyeBrow = []
            for item in params.get("RightEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.RightEyeBrow.append(obj)
        if params.get("MouthOutside") is not None:
            self.MouthOutside = []
            for item in params.get("MouthOutside"):
                obj = Point()
                obj._deserialize(item)
                self.MouthOutside.append(obj)
        if params.get("MouthInside") is not None:
            self.MouthInside = []
            for item in params.get("MouthInside"):
                obj = Point()
                obj._deserialize(item)
                self.MouthInside.append(obj)
        if params.get("Nose") is not None:
            self.Nose = []
            for item in params.get("Nose"):
                obj = Point()
                obj._deserialize(item)
                self.Nose.append(obj)
        if params.get("LeftPupil") is not None:
            self.LeftPupil = []
            for item in params.get("LeftPupil"):
                obj = Point()
                obj._deserialize(item)
                self.LeftPupil.append(obj)
        if params.get("RightPupil") is not None:
            self.RightPupil = []
            for item in params.get("RightPupil"):
                obj = Point()
                obj._deserialize(item)
                self.RightPupil.append(obj)
        if params.get("CentralAxis") is not None:
            self.CentralAxis = []
            for item in params.get("CentralAxis"):
                obj = Point()
                obj._deserialize(item)
                self.CentralAxis.append(obj)
        if params.get("Chin") is not None:
            self.Chin = []
            for item in params.get("Chin"):
                obj = Point()
                obj._deserialize(item)
                self.Chin.append(obj)
        if params.get("LeftEyeBags") is not None:
            self.LeftEyeBags = []
            for item in params.get("LeftEyeBags"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEyeBags.append(obj)
        if params.get("RightEyeBags") is not None:
            self.RightEyeBags = []
            for item in params.get("RightEyeBags"):
                obj = Point()
                obj._deserialize(item)
                self.RightEyeBags.append(obj)
        if params.get("Forehead") is not None:
            self.Forehead = []
            for item in params.get("Forehead"):
                obj = Point()
                obj._deserialize(item)
                self.Forehead.append(obj)


class DetectFaceAttributesRequest(AbstractModel):
    """DetectFaceAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param MaxFaceNum: 最多处理的人脸数目。 
默认值为1（仅检测图片中面积最大的那张人脸），最大值为120。 
此参数用于控制处理待检测图片中的人脸个数，值越小，处理速度越快。
        :type MaxFaceNum: int
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。 
对应图片 base64 编码后大小不可超过5M。 
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param FaceAttributesType: 是否返回年龄、性别、情绪等属性。 
合法值为（大小写不敏感）：None、Age、Beauty、Emotion、Eye、Eyebrow 
Gender、Hair、Hat、Headpose、Mask、Mouth、Moustache、Nose、Shape、Skin、Smile。 
None为不需要返回。默认为 None。 
需要将属性组成一个用逗号分隔的字符串，属性之间的顺序没有要求。 
关于各属性的详细描述，参见下文出参。 
最多返回面积最大的 5 张人脸属性信息，超过 5 张人脸（第 6 张及以后的人脸）的 AttributesInfo 不具备参考意义。
        :type FaceAttributesType: str
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。本接口仅支持“3.0”输入
        :type FaceModelVersion: str
        """
        self.MaxFaceNum = None
        self.Image = None
        self.Url = None
        self.FaceAttributesType = None
        self.NeedRotateDetection = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceAttributesType = params.get("FaceAttributesType")
        self.NeedRotateDetection = params.get("NeedRotateDetection")
        self.FaceModelVersion = params.get("FaceModelVersion")


class DetectFaceAttributesResponse(AbstractModel):
    """DetectFaceAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param FaceDetailInfos: 人脸信息列表。
        :type FaceDetailInfos: list of FaceDetailInfo
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceDetailInfos = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("FaceDetailInfos") is not None:
            self.FaceDetailInfos = []
            for item in params.get("FaceDetailInfos"):
                obj = FaceDetailInfo()
                obj._deserialize(item)
                self.FaceDetailInfos.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class DetectFaceRequest(AbstractModel):
    """DetectFace请求参数结构体

    """

    def __init__(self):
        """
        :param MaxFaceNum: 最多处理的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为120。 
此参数用于控制处理待检测图片中的人脸个数，值越小，处理速度越快。
        :type MaxFaceNum: int
        :param MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。
默认为34。建议不低于34。
低于MinFaceSize值的人脸不会被检测。
        :type MinFaceSize: int
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param NeedFaceAttributes: 是否需要返回人脸属性信息（FaceAttributesInfo）。0 为不需要返回，1 为需要返回。默认为 0。 
非 1 值均视为不需要返回，此时 FaceAttributesInfo 不具备参考意义。  
最多返回面积最大的 5 张人脸属性信息，超过 5 张人脸（第 6 张及以后的人脸）的 FaceAttributesInfo 不具备参考意义。  
提取人脸属性信息较为耗时，如不需要人脸属性信息，建议关闭此项功能，加快人脸检测速度。
        :type NeedFaceAttributes: int
        :param NeedQualityDetection: 是否开启质量检测。0 为关闭，1 为开启。默认为 0。 
非 1 值均视为不进行质量检测。
最多返回面积最大的 30 张人脸质量分信息，超过 30 张人脸（第 31 张及以后的人脸）的 FaceQualityInfo不具备参考意义。  
建议：人脸入库操作建议开启此功能。
        :type NeedQualityDetection: int
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。  
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.Image = None
        self.Url = None
        self.NeedFaceAttributes = None
        self.NeedQualityDetection = None
        self.FaceModelVersion = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.NeedFaceAttributes = params.get("NeedFaceAttributes")
        self.NeedQualityDetection = params.get("NeedQualityDetection")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class DetectFaceResponse(AbstractModel):
    """DetectFace返回参数结构体

    """

    def __init__(self):
        """
        :param ImageWidth: 请求的图片宽度。
        :type ImageWidth: int
        :param ImageHeight: 请求的图片高度。
        :type ImageHeight: int
        :param FaceInfos: 人脸信息列表。包含人脸坐标信息、属性信息（若需要）、质量分信息（若需要）。
        :type FaceInfos: list of FaceInfo
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceInfos = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("FaceInfos") is not None:
            self.FaceInfos = []
            for item in params.get("FaceInfos"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfos.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class DetectLiveFaceRequest(AbstractModel):
    """DetectLiveFace请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。（图片的宽高比请接近3:4，不符合宽高比的图片返回的分值不具备参考意义）。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。 
（图片的宽高比请接近 3:4，不符合宽高比的图片返回的分值不具备参考意义） 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。目前入参支持 “2.0”和“3.0“ 两个输入。  
2020年4月2日开始，默认为“3.0”，之前使用过本接口的账号若未填写本参数默认为“2.0”。 
不同算法模型版本对应的人脸识别算法不同，新版本的整体效果会优于旧版本，建议使用“3.0”版本。
        :type FaceModelVersion: str
        """
        self.Image = None
        self.Url = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceModelVersion = params.get("FaceModelVersion")


class DetectLiveFaceResponse(AbstractModel):
    """DetectLiveFace返回参数结构体

    """

    def __init__(self):
        """
        :param Score: 活体打分，取值范围 [0,100]，分数一般落于[80, 100]区间内，0分也为常见值。推荐相大于 87 时可判断为活体。可根据具体场景自行调整阈值。
本字段当且仅当FaceModelVersion为2.0时才具备参考意义。
        :type Score: float
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param IsLiveness: 活体检测是否通过。
本字段只有FaceModelVersion为3.0时才具备参考意义。
        :type IsLiveness: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.FaceModelVersion = None
        self.IsLiveness = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.IsLiveness = params.get("IsLiveness")
        self.RequestId = params.get("RequestId")


class EstimateCheckSimilarPersonCostTimeRequest(AbstractModel):
    """EstimateCheckSimilarPersonCostTime请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIds: 待整理的人员库列表。 
人员库总人数不可超过200万，人员库个数不可超过10个。
数组元素取值为创建人员库接口中的GroupId
        :type GroupIds: list of str
        """
        self.GroupIds = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")


class EstimateCheckSimilarPersonCostTimeResponse(AbstractModel):
    """EstimateCheckSimilarPersonCostTime返回参数结构体

    """

    def __init__(self):
        """
        :param EstimatedTimeCost: 人员查重任务预估需要耗费时间。 单位为分钟。
        :type EstimatedTimeCost: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EstimatedTimeCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EstimatedTimeCost = params.get("EstimatedTimeCost")
        self.RequestId = params.get("RequestId")


class Eye(AbstractModel):
    """眼睛信息

    """

    def __init__(self):
        """
        :param Glass: 识别是否佩戴眼镜。
AttributeItem对应的Type为 —— 0：无眼镜，1：普通眼镜，2：墨镜
        :type Glass: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param EyeOpen: 识别眼睛的睁开、闭合状态。
AttributeItem对应的Type为 —— 0：睁开，1：闭眼
        :type EyeOpen: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param EyelidType: 识别是否双眼皮。
AttributeItem对应的Type为 —— 0：无，1：有。
        :type EyelidType: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param EyeSize: 眼睛大小。
AttributeItem对应的Type为 —— 0：小眼睛，1：普通眼睛，2：大眼睛。
        :type EyeSize: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self.Glass = None
        self.EyeOpen = None
        self.EyelidType = None
        self.EyeSize = None


    def _deserialize(self, params):
        if params.get("Glass") is not None:
            self.Glass = AttributeItem()
            self.Glass._deserialize(params.get("Glass"))
        if params.get("EyeOpen") is not None:
            self.EyeOpen = AttributeItem()
            self.EyeOpen._deserialize(params.get("EyeOpen"))
        if params.get("EyelidType") is not None:
            self.EyelidType = AttributeItem()
            self.EyelidType._deserialize(params.get("EyelidType"))
        if params.get("EyeSize") is not None:
            self.EyeSize = AttributeItem()
            self.EyeSize._deserialize(params.get("EyeSize"))


class Eyebrow(AbstractModel):
    """眉毛信息

    """

    def __init__(self):
        """
        :param EyebrowDensity: 眉毛浓密。
AttributeItem对应的Type为 —— 0：淡眉，1：浓眉。
        :type EyebrowDensity: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param EyebrowCurve: 眉毛弯曲。
AttributeItem对应的Type为 —— 0：不弯，1：弯眉。
        :type EyebrowCurve: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param EyebrowLength: 眉毛长短。
AttributeItem对应的Type为 —— 0：短眉毛，1：长眉毛。
        :type EyebrowLength: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self.EyebrowDensity = None
        self.EyebrowCurve = None
        self.EyebrowLength = None


    def _deserialize(self, params):
        if params.get("EyebrowDensity") is not None:
            self.EyebrowDensity = AttributeItem()
            self.EyebrowDensity._deserialize(params.get("EyebrowDensity"))
        if params.get("EyebrowCurve") is not None:
            self.EyebrowCurve = AttributeItem()
            self.EyebrowCurve._deserialize(params.get("EyebrowCurve"))
        if params.get("EyebrowLength") is not None:
            self.EyebrowLength = AttributeItem()
            self.EyebrowLength._deserialize(params.get("EyebrowLength"))


class FaceAttributesInfo(AbstractModel):
    """人脸属性信息，包含性别( gender )、年龄( age )、表情( expression )、
    魅力( beauty )、眼镜( glass )、口罩（mask）、头发（hair）和姿态 (pitch，roll，yaw )。只有当 NeedFaceAttributes 设为 1 时才返回有效信息，最多返回面积最大的 5 张人脸属性信息，超过 5 张人脸（第 6 张及以后的人脸）的 FaceAttributesInfo 不具备参考意义。

    """

    def __init__(self):
        """
        :param Gender: 性别[0~49]为女性，[50，100]为男性，越接近0和100表示置信度越高。NeedFaceAttributes 不为 1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Gender: int
        :param Age: 年龄 [0~100]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Age: int
        :param Expression: 微笑[0(normal，正常)~50(smile，微笑)~100(laugh，大笑)]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Expression: int
        :param Glass: 是否有眼镜 [true,false]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Glass: bool
        :param Pitch: 上下偏移[-30,30]，单位角度。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。 
建议：人脸入库选择[-10,10]的图片。
        :type Pitch: int
        :param Yaw: 左右偏移[-30,30]，单位角度。 NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。 
建议：人脸入库选择[-10,10]的图片。
        :type Yaw: int
        :param Roll: 平面旋转[-180,180]，单位角度。 NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。  
建议：人脸入库选择[-20,20]的图片。
        :type Roll: int
        :param Beauty: 魅力[0~100]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Beauty: int
        :param Hat: 是否有帽子 [true,false]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hat: bool
        :param Mask: 是否有口罩 [true,false]。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mask: bool
        :param Hair: 头发信息，包含头发长度（length）、有无刘海（bang）、头发颜色（color）。NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type Hair: :class:`tencentcloud.iai.v20200303.models.FaceHairAttributesInfo`
        :param EyeOpen: 双眼是否睁开 [true,false]。只要有超过一只眼睛闭眼，就返回false。 NeedFaceAttributes 不为1 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
注意：此字段可能返回 null，表示取不到有效值。
        :type EyeOpen: bool
        """
        self.Gender = None
        self.Age = None
        self.Expression = None
        self.Glass = None
        self.Pitch = None
        self.Yaw = None
        self.Roll = None
        self.Beauty = None
        self.Hat = None
        self.Mask = None
        self.Hair = None
        self.EyeOpen = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.Expression = params.get("Expression")
        self.Glass = params.get("Glass")
        self.Pitch = params.get("Pitch")
        self.Yaw = params.get("Yaw")
        self.Roll = params.get("Roll")
        self.Beauty = params.get("Beauty")
        self.Hat = params.get("Hat")
        self.Mask = params.get("Mask")
        if params.get("Hair") is not None:
            self.Hair = FaceHairAttributesInfo()
            self.Hair._deserialize(params.get("Hair"))
        self.EyeOpen = params.get("EyeOpen")


class FaceDetailAttributesInfo(AbstractModel):
    """人脸属性信息，根据 FaceAttributesType 输入的类型，返回年龄（Age）、颜值（Beauty）
    情绪（Emotion）、眼睛信息（Eye）、眉毛（Eyebrow）、性别（Gender）
    头发（Hair）、帽子（Hat）、姿态（Headpose）、口罩（Mask）、嘴巴（Mouse）、胡子（Moustache）
    鼻子（Nose）、脸型（Shape）、肤色（Skin）、微笑（Smile）等人脸属性信息。
    若 FaceAttributesType 没有输入相关类型，则FaceDetaiAttributesInfo返回的细项不具备参考意义。

    """

    def __init__(self):
        """
        :param Age: 年龄 [0,65]，其中65代表“65岁及以上”。 
FaceAttributesType 不为含Age 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Age: int
        :param Beauty: 美丑打分[0,100]。 
FaceAttributesType 不含 Beauty 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Beauty: int
        :param Emotion: 情绪，可识别自然、高兴、惊讶、生气、悲伤、厌恶、害怕。 
AttributeItem对应的Type为 —— 0：自然，1：高兴，2：惊讶，3：生气，4：悲伤，5：厌恶，6：害怕
FaceAttributesType 不含Emotion 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Emotion: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Eye: 眼睛相关信息，可识别是否戴眼镜、是否闭眼、是否双眼皮和眼睛大小。 
FaceAttributesType 不含Eye 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Eye: :class:`tencentcloud.iai.v20200303.models.Eye`
        :param Eyebrow: 眉毛相关信息，可识别眉毛浓密、弯曲、长短信息。 
FaceAttributesType 不含Eyebrow 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Eyebrow: :class:`tencentcloud.iai.v20200303.models.Eyebrow`
        :param Gender: 性别信息。 
AttributeItem对应的Type为 —— 	0：男性，1：女性。
FaceAttributesType 不含Gender 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Gender: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Hair: 头发信息，包含头发长度、有无刘海、头发颜色。 
FaceAttributesType 不含Hair 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Hair: :class:`tencentcloud.iai.v20200303.models.Hair`
        :param Hat: 帽子信息，可识别是否佩戴帽子、帽子款式、帽子颜色。 
FaceAttributesType 不含Hat 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Hat: :class:`tencentcloud.iai.v20200303.models.Hat`
        :param HeadPose: 姿态信息，包含人脸的上下偏移、左右偏移、平面旋转信息。 
FaceAttributesType 不含Headpose 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type HeadPose: :class:`tencentcloud.iai.v20200303.models.HeadPose`
        :param Mask: 口罩佩戴信息。 
AttributeItem对应的Type为 —— 0: 无口罩， 1: 有口罩不遮脸，2: 有口罩遮下巴，3: 有口罩遮嘴，4: 正确佩戴口罩。
FaceAttributesType 不含Mask 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Mask: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Mouth: 嘴巴信息，可识别是否张嘴、嘴唇厚度。 
FaceAttributesType 不含 Mouth 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Mouth: :class:`tencentcloud.iai.v20200303.models.Mouth`
        :param Moustache: 胡子信息。
AttributeItem对应的Type为 —— 0：无胡子，1：有胡子。 
FaceAttributesType 不含 Moustache 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Moustache: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Nose: 鼻子信息。 
AttributeItem对应的Type为 —— 0：朝天鼻，1：鹰钩鼻，2：普通，3：圆鼻头
FaceAttributesType 不含 Nose 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Nose: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Shape: 脸型信息。 
AttributeItem对应的Type为 —— 0：方脸，1：三角脸，2：鹅蛋脸，3：心形脸，4：圆脸。
FaceAttributesType 不含 Shape 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Shape: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Skin: 肤色信息。 
AttributeItem对应的Type为 —— 0：黄色皮肤，1：棕色皮肤，2：黑色皮肤，3：白色皮肤。
FaceAttributesType 不含 Skin 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Skin: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Smile: 微笑程度，[0,100]。 
FaceAttributesType 不含 Smile 或检测超过 5 张人脸时，此参数仍返回，但不具备参考意义。
        :type Smile: int
        """
        self.Age = None
        self.Beauty = None
        self.Emotion = None
        self.Eye = None
        self.Eyebrow = None
        self.Gender = None
        self.Hair = None
        self.Hat = None
        self.HeadPose = None
        self.Mask = None
        self.Mouth = None
        self.Moustache = None
        self.Nose = None
        self.Shape = None
        self.Skin = None
        self.Smile = None


    def _deserialize(self, params):
        self.Age = params.get("Age")
        self.Beauty = params.get("Beauty")
        if params.get("Emotion") is not None:
            self.Emotion = AttributeItem()
            self.Emotion._deserialize(params.get("Emotion"))
        if params.get("Eye") is not None:
            self.Eye = Eye()
            self.Eye._deserialize(params.get("Eye"))
        if params.get("Eyebrow") is not None:
            self.Eyebrow = Eyebrow()
            self.Eyebrow._deserialize(params.get("Eyebrow"))
        if params.get("Gender") is not None:
            self.Gender = AttributeItem()
            self.Gender._deserialize(params.get("Gender"))
        if params.get("Hair") is not None:
            self.Hair = Hair()
            self.Hair._deserialize(params.get("Hair"))
        if params.get("Hat") is not None:
            self.Hat = Hat()
            self.Hat._deserialize(params.get("Hat"))
        if params.get("HeadPose") is not None:
            self.HeadPose = HeadPose()
            self.HeadPose._deserialize(params.get("HeadPose"))
        if params.get("Mask") is not None:
            self.Mask = AttributeItem()
            self.Mask._deserialize(params.get("Mask"))
        if params.get("Mouth") is not None:
            self.Mouth = Mouth()
            self.Mouth._deserialize(params.get("Mouth"))
        if params.get("Moustache") is not None:
            self.Moustache = AttributeItem()
            self.Moustache._deserialize(params.get("Moustache"))
        if params.get("Nose") is not None:
            self.Nose = AttributeItem()
            self.Nose._deserialize(params.get("Nose"))
        if params.get("Shape") is not None:
            self.Shape = AttributeItem()
            self.Shape._deserialize(params.get("Shape"))
        if params.get("Skin") is not None:
            self.Skin = AttributeItem()
            self.Skin._deserialize(params.get("Skin"))
        self.Smile = params.get("Smile")


class FaceDetailInfo(AbstractModel):
    """人脸信息列表。

    """

    def __init__(self):
        """
        :param FaceRect: 检测出的人脸框位置。
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param FaceDetailAttributesInfo: 人脸属性信息，根据 FaceAttributesType 输入的类型，返回年龄（Age）、颜值（Beauty） 
情绪（Emotion）、眼睛信息（Eye）、眉毛（Eyebrow）、性别（Gender） 
头发（Hair）、帽子（Hat）、姿态（Headpose）、口罩（Mask）、嘴巴（Mouse）、胡子（Moustache） 
鼻子（Nose）、脸型（Shape）、肤色（Skin）、微笑（Smile）等人脸属性信息。  
若 FaceAttributesType 没有输入相关类型，则FaceDetaiAttributesInfo返回的细项不具备参考意义。
        :type FaceDetailAttributesInfo: :class:`tencentcloud.iai.v20200303.models.FaceDetailAttributesInfo`
        """
        self.FaceRect = None
        self.FaceDetailAttributesInfo = None


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        if params.get("FaceDetailAttributesInfo") is not None:
            self.FaceDetailAttributesInfo = FaceDetailAttributesInfo()
            self.FaceDetailAttributesInfo._deserialize(params.get("FaceDetailAttributesInfo"))


class FaceHairAttributesInfo(AbstractModel):
    """人脸属性中的发型信息。

    """

    def __init__(self):
        """
        :param Length: 0：光头，1：短发，2：中发，3：长发，4：绑发
注意：此字段可能返回 null，表示取不到有效值。
        :type Length: int
        :param Bang: 0：有刘海，1：无刘海
注意：此字段可能返回 null，表示取不到有效值。
        :type Bang: int
        :param Color: 0：黑色，1：金色，2：棕色，3：灰白色
注意：此字段可能返回 null，表示取不到有效值。
        :type Color: int
        """
        self.Length = None
        self.Bang = None
        self.Color = None


    def _deserialize(self, params):
        self.Length = params.get("Length")
        self.Bang = params.get("Bang")
        self.Color = params.get("Color")


class FaceInfo(AbstractModel):
    """人脸信息列表。

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completeness满足需求的情况下，将负值坐标取0。
        :type X: int
        :param Y: 人脸框左上角纵坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completeness满足需求的情况下，将负值坐标取0。
        :type Y: int
        :param Width: 人脸框宽度。
        :type Width: int
        :param Height: 人脸框高度。
        :type Height: int
        :param FaceAttributesInfo: 人脸属性信息，包含性别( gender )、年龄( age )、表情( expression )、 
魅力( beauty )、眼镜( glass )、口罩（mask）、头发（hair）和姿态 (pitch，roll，yaw )。只有当 NeedFaceAttributes 设为 1 时才返回有效信息。
        :type FaceAttributesInfo: :class:`tencentcloud.iai.v20200303.models.FaceAttributesInfo`
        :param FaceQualityInfo: 人脸质量信息，包含质量分（score）、模糊分（sharpness）、光照分（brightness）、遮挡分（completeness）。只有当NeedFaceDetection设为1时才返回有效信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceQualityInfo: :class:`tencentcloud.iai.v20200303.models.FaceQualityInfo`
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.FaceAttributesInfo = None
        self.FaceQualityInfo = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("FaceAttributesInfo") is not None:
            self.FaceAttributesInfo = FaceAttributesInfo()
            self.FaceAttributesInfo._deserialize(params.get("FaceAttributesInfo"))
        if params.get("FaceQualityInfo") is not None:
            self.FaceQualityInfo = FaceQualityInfo()
            self.FaceQualityInfo._deserialize(params.get("FaceQualityInfo"))


class FaceQualityCompleteness(AbstractModel):
    """五官遮挡分，评价眉毛（Eyebrow）、眼睛（Eye）、鼻子（Nose）、脸颊（Cheek）、嘴巴（Mouth）、下巴（Chin）的被遮挡程度。

    """

    def __init__(self):
        """
        :param Eyebrow: 眉毛的遮挡分数[0,100]，分数越高遮挡越少。 
参考范围：[0,80]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Eyebrow: int
        :param Eye: 眼睛的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,80]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Eye: int
        :param Nose: 鼻子的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,60]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Nose: int
        :param Cheek: 脸颊的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,70]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cheek: int
        :param Mouth: 嘴巴的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,50]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mouth: int
        :param Chin: 下巴的遮挡分数[0,100],分数越高遮挡越少。 
参考范围：[0,70]表示发生遮挡。
注意：此字段可能返回 null，表示取不到有效值。
        :type Chin: int
        """
        self.Eyebrow = None
        self.Eye = None
        self.Nose = None
        self.Cheek = None
        self.Mouth = None
        self.Chin = None


    def _deserialize(self, params):
        self.Eyebrow = params.get("Eyebrow")
        self.Eye = params.get("Eye")
        self.Nose = params.get("Nose")
        self.Cheek = params.get("Cheek")
        self.Mouth = params.get("Mouth")
        self.Chin = params.get("Chin")


class FaceQualityInfo(AbstractModel):
    """人脸质量信息，包含质量分（score）、模糊分（sharpness）、光照分（brightness）、遮挡分（completeness）。只有当NeedFaceDetection设为1时才返回有效信息。

    """

    def __init__(self):
        """
        :param Score: 质量分: [0,100]，综合评价图像质量是否适合人脸识别，分数越高质量越好。 
正常情况，只需要使用Score作为质量分总体的判断标准即可。Sharpness、Brightness、Completeness等细项分仅供参考。
参考范围：[0,40]较差，[40,60] 一般，[60,80]较好，[80,100]很好。 
建议：人脸入库选取70以上的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Sharpness: 清晰分：[0,100]，评价图片清晰程度，分数越高越清晰。 
参考范围：[0,40]特别模糊，[40,60]模糊，[60,80]一般，[80,100]清晰。 
建议：人脸入库选取80以上的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sharpness: int
        :param Brightness: 光照分：[0,100]，评价图片光照程度，分数越高越亮。 
参考范围： [0,30]偏暗，[30,70]光照正常，[70,100]偏亮。 
建议：人脸入库选取[30,70]的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type Brightness: int
        :param Completeness: 五官遮挡分，评价眉毛（Eyebrow）、眼睛（Eye）、鼻子（Nose）、脸颊（Cheek）、嘴巴（Mouth）、下巴（Chin）的被遮挡程度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Completeness: :class:`tencentcloud.iai.v20200303.models.FaceQualityCompleteness`
        """
        self.Score = None
        self.Sharpness = None
        self.Brightness = None
        self.Completeness = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.Sharpness = params.get("Sharpness")
        self.Brightness = params.get("Brightness")
        if params.get("Completeness") is not None:
            self.Completeness = FaceQualityCompleteness()
            self.Completeness._deserialize(params.get("Completeness"))


class FaceRect(AbstractModel):
    """检测出的人脸框的位置

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
        :type X: int
        :param Y: 人脸框左上角纵坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
        :type Y: int
        :param Width: 人脸宽度
        :type Width: int
        :param Height: 人脸高度
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


class FaceShape(AbstractModel):
    """五官定位（人脸关键点）具体信息。

    """

    def __init__(self):
        """
        :param FaceProfile: 描述脸型轮廓的 21 点。
        :type FaceProfile: list of Point
        :param LeftEye: 描述左侧眼睛轮廓的 8 点。
        :type LeftEye: list of Point
        :param RightEye: 描述右侧眼睛轮廓的 8 点。
        :type RightEye: list of Point
        :param LeftEyeBrow: 描述左侧眉毛轮廓的 8 点。
        :type LeftEyeBrow: list of Point
        :param RightEyeBrow: 描述右侧眉毛轮廓的 8 点。
        :type RightEyeBrow: list of Point
        :param Mouth: 描述嘴巴轮廓的 22 点。
        :type Mouth: list of Point
        :param Nose: 描述鼻子轮廓的 13 点。
        :type Nose: list of Point
        :param LeftPupil: 左瞳孔轮廓的 1 个点。
        :type LeftPupil: list of Point
        :param RightPupil: 右瞳孔轮廓的 1 个点。
        :type RightPupil: list of Point
        """
        self.FaceProfile = None
        self.LeftEye = None
        self.RightEye = None
        self.LeftEyeBrow = None
        self.RightEyeBrow = None
        self.Mouth = None
        self.Nose = None
        self.LeftPupil = None
        self.RightPupil = None


    def _deserialize(self, params):
        if params.get("FaceProfile") is not None:
            self.FaceProfile = []
            for item in params.get("FaceProfile"):
                obj = Point()
                obj._deserialize(item)
                self.FaceProfile.append(obj)
        if params.get("LeftEye") is not None:
            self.LeftEye = []
            for item in params.get("LeftEye"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEye.append(obj)
        if params.get("RightEye") is not None:
            self.RightEye = []
            for item in params.get("RightEye"):
                obj = Point()
                obj._deserialize(item)
                self.RightEye.append(obj)
        if params.get("LeftEyeBrow") is not None:
            self.LeftEyeBrow = []
            for item in params.get("LeftEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEyeBrow.append(obj)
        if params.get("RightEyeBrow") is not None:
            self.RightEyeBrow = []
            for item in params.get("RightEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.RightEyeBrow.append(obj)
        if params.get("Mouth") is not None:
            self.Mouth = []
            for item in params.get("Mouth"):
                obj = Point()
                obj._deserialize(item)
                self.Mouth.append(obj)
        if params.get("Nose") is not None:
            self.Nose = []
            for item in params.get("Nose"):
                obj = Point()
                obj._deserialize(item)
                self.Nose.append(obj)
        if params.get("LeftPupil") is not None:
            self.LeftPupil = []
            for item in params.get("LeftPupil"):
                obj = Point()
                obj._deserialize(item)
                self.LeftPupil.append(obj)
        if params.get("RightPupil") is not None:
            self.RightPupil = []
            for item in params.get("RightPupil"):
                obj = Point()
                obj._deserialize(item)
                self.RightPupil.append(obj)


class GetCheckSimilarPersonJobIdListRequest(AbstractModel):
    """GetCheckSimilarPersonJobIdList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为1000。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetCheckSimilarPersonJobIdListResponse(AbstractModel):
    """GetCheckSimilarPersonJobIdList返回参数结构体

    """

    def __init__(self):
        """
        :param JobIdInfos: 人员查重任务信息列表。
        :type JobIdInfos: list of JobIdInfo
        :param JobIdNum: 查重任务总数量。
        :type JobIdNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobIdInfos = None
        self.JobIdNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobIdInfos") is not None:
            self.JobIdInfos = []
            for item in params.get("JobIdInfos"):
                obj = JobIdInfo()
                obj._deserialize(item)
                self.JobIdInfos.append(obj)
        self.JobIdNum = params.get("JobIdNum")
        self.RequestId = params.get("RequestId")


class GetGroupInfoRequest(AbstractModel):
    """GetGroupInfo请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人员库 ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetGroupInfoResponse(AbstractModel):
    """GetGroupInfo返回参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 人员库名称
        :type GroupName: str
        :param GroupId: 人员库ID
        :type GroupId: str
        :param GroupExDescriptions: 人员库自定义描述字段
        :type GroupExDescriptions: list of str
        :param Tag: 人员库信息备注
        :type Tag: str
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。
        :type CreationTimestamp: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None
        self.CreationTimestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")
        self.RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始序号，默认值为0
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为1000
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param GroupInfos: 返回的人员库信息
        :type GroupInfos: list of GroupInfo
        :param GroupNum: 人员库总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupInfos = None
        self.GroupNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self.GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
        self.RequestId = params.get("RequestId")


class GetPersonBaseInfoRequest(AbstractModel):
    """GetPersonBaseInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，创建人员接口中的PersonId
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class GetPersonBaseInfoResponse(AbstractModel):
    """GetPersonBaseInfo返回参数结构体

    """

    def __init__(self):
        """
        :param PersonName: 人员名称
        :type PersonName: str
        :param Gender: 人员性别，0代表未填写，1代表男性，2代表女性
        :type Gender: int
        :param FaceIds: 包含的人脸 ID 列表
        :type FaceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonName = None
        self.Gender = None
        self.FaceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")
        self.FaceIds = params.get("FaceIds")
        self.RequestId = params.get("RequestId")


class GetPersonGroupInfoRequest(AbstractModel):
    """GetPersonGroupInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        :param Offset: 起始序号，默认值为0
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为100
        :type Limit: int
        """
        self.PersonId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetPersonGroupInfoResponse(AbstractModel):
    """GetPersonGroupInfo返回参数结构体

    """

    def __init__(self):
        """
        :param PersonGroupInfos: 包含此人员的人员库及描述字段内容列表
        :type PersonGroupInfos: list of PersonGroupInfo
        :param GroupNum: 人员库总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNum: int
        :param FaceModelVersion: 人脸识别服务所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonGroupInfos = None
        self.GroupNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonGroupInfos") is not None:
            self.PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self.PersonGroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class GetPersonListNumRequest(AbstractModel):
    """GetPersonListNum请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人员库ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetPersonListNumResponse(AbstractModel):
    """GetPersonListNum返回参数结构体

    """

    def __init__(self):
        """
        :param PersonNum: 人员数量
        :type PersonNum: int
        :param FaceNum: 人脸数量
        :type FaceNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonNum = None
        self.FaceNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonNum = params.get("PersonNum")
        self.FaceNum = params.get("FaceNum")
        self.RequestId = params.get("RequestId")


class GetPersonListRequest(AbstractModel):
    """GetPersonList请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人员库ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        :param Offset: 起始序号，默认值为0
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为1000
        :type Limit: int
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetPersonListResponse(AbstractModel):
    """GetPersonList返回参数结构体

    """

    def __init__(self):
        """
        :param PersonInfos: 返回的人员信息
        :type PersonInfos: list of PersonInfo
        :param PersonNum: 该人员库的人员数量
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonNum: int
        :param FaceNum: 该人员库的人脸数量
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceNum: int
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonInfos = None
        self.PersonNum = None
        self.FaceNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self.PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfos.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.FaceNum = params.get("FaceNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class GetSimilarPersonResultRequest(AbstractModel):
    """GetSimilarPersonResult请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 查重任务ID，用于查询、获取查重的进度和结果。取值为人员查重接口返回的JobId
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class GetSimilarPersonResultResponse(AbstractModel):
    """GetSimilarPersonResult返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 查重任务完成进度。取值[0.0，100.0]。当且仅当值为100时，SimilarPersons才有意义。
        :type Progress: float
        :param SimilarPersonsUrl: 疑似同一人的人员信息文件临时下载链接， 有效时间为5分钟，结果文件实际保存90天。
文件内容由 SimilarPerson 的数组组成。
        :type SimilarPersonsUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.SimilarPersonsUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.SimilarPersonsUrl = params.get("SimilarPersonsUrl")
        self.RequestId = params.get("RequestId")


class GetUpgradeGroupFaceModelVersionJobListRequest(AbstractModel):
    """GetUpgradeGroupFaceModelVersionJobList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为1000。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetUpgradeGroupFaceModelVersionJobListResponse(AbstractModel):
    """GetUpgradeGroupFaceModelVersionJobList返回参数结构体

    """

    def __init__(self):
        """
        :param JobInfos: 人员库升级任务信息列表。
        :type JobInfos: list of UpgradeJobInfo
        :param JobNum: 升级任务总数量。
        :type JobNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobInfos = None
        self.JobNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobInfos") is not None:
            self.JobInfos = []
            for item in params.get("JobInfos"):
                obj = UpgradeJobInfo()
                obj._deserialize(item)
                self.JobInfos.append(obj)
        self.JobNum = params.get("JobNum")
        self.RequestId = params.get("RequestId")


class GetUpgradeGroupFaceModelVersionResultRequest(AbstractModel):
    """GetUpgradeGroupFaceModelVersionResult请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 升级任务ID，用于查询、获取人员库升级的进度和结果。
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class GetUpgradeGroupFaceModelVersionResultResponse(AbstractModel):
    """GetUpgradeGroupFaceModelVersionResult返回参数结构体

    """

    def __init__(self):
        """
        :param EndTimestamp: 人员升级任务预估结束时间。 StartTimestamp的值是自 Unix 纪元时间到人员查重任务预估结束的毫秒数。  
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。 
如果为0表示这个任务已经执行完毕。
        :type EndTimestamp: int
        :param Progress: 升级任务完成进度。取值[0.0，100.0]。
        :type Progress: float
        :param Status: 0表示升级中，1表示升级完毕，2表示回滚完毕，3表示升级失败。
        :type Status: int
        :param StartTime: 升级起始时间。 
StartTime的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。 
有关更多信息，请参阅 Unix 时间。
        :type StartTime: int
        :param FromFaceModelVersion: 当前算法模型版本。
        :type FromFaceModelVersion: str
        :param ToFaceModelVersion: 目标算法模型版本。
        :type ToFaceModelVersion: str
        :param GroupId: 人员库ID。
        :type GroupId: str
        :param FailedFacesUrl: 无法升级的人脸Id信息，文件格式
        :type FailedFacesUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EndTimestamp = None
        self.Progress = None
        self.Status = None
        self.StartTime = None
        self.FromFaceModelVersion = None
        self.ToFaceModelVersion = None
        self.GroupId = None
        self.FailedFacesUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EndTimestamp = params.get("EndTimestamp")
        self.Progress = params.get("Progress")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.FromFaceModelVersion = params.get("FromFaceModelVersion")
        self.ToFaceModelVersion = params.get("ToFaceModelVersion")
        self.GroupId = params.get("GroupId")
        self.FailedFacesUrl = params.get("FailedFacesUrl")
        self.RequestId = params.get("RequestId")


class GroupCandidate(AbstractModel):
    """分组识别结果Item

    """

    def __init__(self):
        """
        :param GroupId: 人员库ID 。
        :type GroupId: str
        :param Candidates: 识别出的最相似候选人。
        :type Candidates: list of Candidate
        """
        self.GroupId = None
        self.Candidates = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)


class GroupExDescriptionInfo(AbstractModel):
    """需要修改的人员库自定义描述字段key-value

    """

    def __init__(self):
        """
        :param GroupExDescriptionIndex: 人员库自定义描述字段Index，从0开始
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupExDescriptionIndex: int
        :param GroupExDescription: 需要更新的人员库自定义描述字段内容
        :type GroupExDescription: str
        """
        self.GroupExDescriptionIndex = None
        self.GroupExDescription = None


    def _deserialize(self, params):
        self.GroupExDescriptionIndex = params.get("GroupExDescriptionIndex")
        self.GroupExDescription = params.get("GroupExDescription")


class GroupInfo(AbstractModel):
    """返回的人员库信息

    """

    def __init__(self):
        """
        :param GroupName: 人员库名称
        :type GroupName: str
        :param GroupId: 人员库ID
        :type GroupId: str
        :param GroupExDescriptions: 人员库自定义描述字段
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupExDescriptions: list of str
        :param Tag: 人员库信息备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。有关更多信息，请参阅 Unix 时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTimestamp: int
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")


class Hair(AbstractModel):
    """头发信息

    """

    def __init__(self):
        """
        :param Length: 头发长度信息。
AttributeItem对应的Type为 —— 0：光头，1：短发，2：中发，3：长发，4：绑发。
        :type Length: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Bang: 刘海信息。
AttributeItem对应的Type为 —— 0：无刘海，1：有刘海。
        :type Bang: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Color: 头发颜色信息。
AttributeItem对应的Type为 —— 0：黑色，1：金色，2：棕色，3：灰白色。
        :type Color: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self.Length = None
        self.Bang = None
        self.Color = None


    def _deserialize(self, params):
        if params.get("Length") is not None:
            self.Length = AttributeItem()
            self.Length._deserialize(params.get("Length"))
        if params.get("Bang") is not None:
            self.Bang = AttributeItem()
            self.Bang._deserialize(params.get("Bang"))
        if params.get("Color") is not None:
            self.Color = AttributeItem()
            self.Color._deserialize(params.get("Color"))


class Hat(AbstractModel):
    """帽子信息

    """

    def __init__(self):
        """
        :param Style: 帽子佩戴状态信息。
AttributeItem对应的Type为 —— 0：不戴帽子，1：普通帽子，2：头盔，3：保安帽。
        :type Style: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        :param Color: 帽子颜色。
AttributeItem对应的Type为 —— 0：不戴帽子，1：红色系，2：黄色系，3：蓝色系，4：黑色系，5：灰白色系，6：混色系子。
        :type Color: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self.Style = None
        self.Color = None


    def _deserialize(self, params):
        if params.get("Style") is not None:
            self.Style = AttributeItem()
            self.Style._deserialize(params.get("Style"))
        if params.get("Color") is not None:
            self.Color = AttributeItem()
            self.Color._deserialize(params.get("Color"))


class HeadPose(AbstractModel):
    """姿态信息

    """

    def __init__(self):
        """
        :param Pitch: 上下偏移[-30,30]。
        :type Pitch: int
        :param Yaw: 左右偏移[-30,30]。
        :type Yaw: int
        :param Roll: 平面旋转[-180,180]。
        :type Roll: int
        """
        self.Pitch = None
        self.Yaw = None
        self.Roll = None


    def _deserialize(self, params):
        self.Pitch = params.get("Pitch")
        self.Yaw = params.get("Yaw")
        self.Roll = params.get("Roll")


class JobIdInfo(AbstractModel):
    """查重任务信息

    """

    def __init__(self):
        """
        :param JobId: 查重任务ID，用于查询、获取查重的进度和结果。
        :type JobId: str
        :param StartTime: 查重起始时间。 
StartTime的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。 
有关更多信息，请参阅 Unix 时间。
        :type StartTime: int
        :param JobStatus: 查重任务是否已完成。0: 成功 1: 未完成 2: 失败
        :type JobStatus: int
        """
        self.JobId = None
        self.StartTime = None
        self.JobStatus = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.JobStatus = params.get("JobStatus")


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人员库ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        :param GroupName: 人员库名称
        :type GroupName: str
        :param GroupExDescriptionInfos: 需要修改的人员库自定义描述字段，key-value
        :type GroupExDescriptionInfos: list of GroupExDescriptionInfo
        :param Tag: 人员库信息备注
        :type Tag: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupExDescriptionInfos = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("GroupExDescriptionInfos") is not None:
            self.GroupExDescriptionInfos = []
            for item in params.get("GroupExDescriptionInfos"):
                obj = GroupExDescriptionInfo()
                obj._deserialize(item)
                self.GroupExDescriptionInfos.append(obj)
        self.Tag = params.get("Tag")


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonBaseInfoRequest(AbstractModel):
    """ModifyPersonBaseInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        :param PersonName: 需要修改的人员名称
        :type PersonName: str
        :param Gender: 需要修改的人员性别，1代表男性，2代表女性
        :type Gender: int
        """
        self.PersonId = None
        self.PersonName = None
        self.Gender = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")


class ModifyPersonBaseInfoResponse(AbstractModel):
    """ModifyPersonBaseInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonGroupInfoRequest(AbstractModel):
    """ModifyPersonGroupInfo请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人员库ID，取值为创建人员库接口中的GroupId
        :type GroupId: str
        :param PersonId: 人员ID，取值为创建人员接口中的PersonId
        :type PersonId: str
        :param PersonExDescriptionInfos: 需要修改的人员描述字段内容，key-value
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        """
        self.GroupId = None
        self.PersonId = None
        self.PersonExDescriptionInfos = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonId = params.get("PersonId")
        if params.get("PersonExDescriptionInfos") is not None:
            self.PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self.PersonExDescriptionInfos.append(obj)


class ModifyPersonGroupInfoResponse(AbstractModel):
    """ModifyPersonGroupInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Mouth(AbstractModel):
    """嘴巴信息。

    """

    def __init__(self):
        """
        :param MouthOpen: 是否张嘴信息。
AttributeItem对应的Type为 —— 0：不张嘴，1：张嘴。
        :type MouthOpen: :class:`tencentcloud.iai.v20200303.models.AttributeItem`
        """
        self.MouthOpen = None


    def _deserialize(self, params):
        if params.get("MouthOpen") is not None:
            self.MouthOpen = AttributeItem()
            self.MouthOpen._deserialize(params.get("MouthOpen"))


class PersonExDescriptionInfo(AbstractModel):
    """需要修改的人员描述字段内容，key-value

    """

    def __init__(self):
        """
        :param PersonExDescriptionIndex: 人员描述字段Index，从0开始
注意：此字段可能返回 null，表示取不到有效值。
        :type PersonExDescriptionIndex: int
        :param PersonExDescription: 需要更新的人员描述字段内容
        :type PersonExDescription: str
        """
        self.PersonExDescriptionIndex = None
        self.PersonExDescription = None


    def _deserialize(self, params):
        self.PersonExDescriptionIndex = params.get("PersonExDescriptionIndex")
        self.PersonExDescription = params.get("PersonExDescription")


class PersonGroupInfo(AbstractModel):
    """包含此人员的人员库及描述字段内容列表

    """

    def __init__(self):
        """
        :param GroupId: 包含此人员的人员库ID
        :type GroupId: str
        :param PersonExDescriptions: 人员描述字段内容
        :type PersonExDescriptions: list of str
        """
        self.GroupId = None
        self.PersonExDescriptions = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonExDescriptions = params.get("PersonExDescriptions")


class PersonInfo(AbstractModel):
    """返回的人员信息

    """

    def __init__(self):
        """
        :param PersonName: 人员名称
        :type PersonName: str
        :param PersonId: 人员Id
        :type PersonId: str
        :param Gender: 人员性别
        :type Gender: int
        :param PersonExDescriptions: 人员描述字段内容
        :type PersonExDescriptions: list of str
        :param FaceIds: 包含的人脸照片列表
        :type FaceIds: list of str
        :param CreationTimestamp: 人员的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。有关更多信息，请参阅 Unix 时间。
        :type CreationTimestamp: int
        """
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptions = None
        self.FaceIds = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        self.PersonExDescriptions = params.get("PersonExDescriptions")
        self.FaceIds = params.get("FaceIds")
        self.CreationTimestamp = params.get("CreationTimestamp")


class Point(AbstractModel):
    """坐标

    """

    def __init__(self):
        """
        :param X: x坐标
        :type X: int
        :param Y: Y坐标
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


class Result(AbstractModel):
    """人脸的识别结果

    """

    def __init__(self):
        """
        :param Candidates: 识别出的最相似候选人
        :type Candidates: list of Candidate
        :param FaceRect: 检测出的人脸框位置
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param RetCode: 检测出的人脸图片状态返回码。0 表示正常。 
-1601代表不符合图片质量控制要求，此时Candidate内容为空。
        :type RetCode: int
        """
        self.Candidates = None
        self.FaceRect = None
        self.RetCode = None


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.RetCode = params.get("RetCode")


class ResultsReturnsByGroup(AbstractModel):
    """识别结果。

    """

    def __init__(self):
        """
        :param FaceRect: 检测出的人脸框位置。
        :type FaceRect: :class:`tencentcloud.iai.v20200303.models.FaceRect`
        :param GroupCandidates: 识别结果。
        :type GroupCandidates: list of GroupCandidate
        :param RetCode: 检测出的人脸图片状态返回码。0 表示正常。 
-1601代表不符合图片质量控制要求，此时Candidate内容为空。
        :type RetCode: int
        """
        self.FaceRect = None
        self.GroupCandidates = None
        self.RetCode = None


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        if params.get("GroupCandidates") is not None:
            self.GroupCandidates = []
            for item in params.get("GroupCandidates"):
                obj = GroupCandidate()
                obj._deserialize(item)
                self.GroupCandidates.append(obj)
        self.RetCode = params.get("RetCode")


class RevertGroupFaceModelVersionRequest(AbstractModel):
    """RevertGroupFaceModelVersion请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 需要回滚的升级任务ID。
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class RevertGroupFaceModelVersionResponse(AbstractModel):
    """RevertGroupFaceModelVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchFacesRequest(AbstractModel):
    """SearchFaces请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人员库列表，上限100个。数组元素取值为创建人员库接口中的GroupId
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。 
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。 
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34的人脸图片无法被识别。建议设置为80。
        :type MinFaceSize: int
        :param MaxPersonNum: 单张被识别的人脸返回的最相似人员数量。默认值为5，最大值为100。 
例，设MaxFaceNum为1，MaxPersonNum为8，则返回Top8相似的人员信息。
值越大，需要处理的时间越长。建议不要超过10。
        :type MaxPersonNum: int
        :param NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出参Score中，只有超过FaceMatchThreshold值的结果才会返回。默认为0。
        :type FaceMatchThreshold: float
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNum = None
        self.NeedPersonInfo = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchFacesResponse(AbstractModel):
    """SearchFaces返回参数结构体

    """

    def __init__(self):
        """
        :param Results: 识别结果。
        :type Results: list of Result
        :param FaceNum: 搜索的人员库中包含的人脸数。
        :type FaceNum: int
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.FaceNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self.Results.append(obj)
        self.FaceNum = params.get("FaceNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchFacesReturnsByGroupRequest(AbstractModel):
    """SearchFacesReturnsByGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人员库列表，上限60个。数组元素取值为创建人员库接口中的GroupId
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。
        :type MinFaceSize: int
        :param MaxPersonNumPerGroup: 被检测到的人脸，对应最多返回的最相似人员数目。默认值为5，最大值为10。  
例，设MaxFaceNum为3，MaxPersonNum为5，则最多可能返回3*5=15个人员。
        :type MaxPersonNumPerGroup: int
        :param NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出参Score中，只有大于等于FaceMatchThreshold值的结果才会返回。
默认为0。
取值范围[0.0,100.0) 。
        :type FaceMatchThreshold: float
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNumPerGroup = None
        self.NeedPersonInfo = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchFacesReturnsByGroupResponse(AbstractModel):
    """SearchFacesReturnsByGroup返回参数结构体

    """

    def __init__(self):
        """
        :param FaceNum: 搜索的人员库中包含的人脸数。
        :type FaceNum: int
        :param ResultsReturnsByGroup: 识别结果。
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceNum = None
        self.ResultsReturnsByGroup = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceNum = params.get("FaceNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self.ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self.ResultsReturnsByGroup.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchPersonsRequest(AbstractModel):
    """SearchPersons请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人员库列表，上限100个。数组元素取值为创建人员库接口中的GroupId
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。
        :type MinFaceSize: int
        :param MaxPersonNum: 单张被识别的人脸返回的最相似人员数量。默认值为5，最大值为100。
例，设MaxFaceNum为1，MaxPersonNum为8，则返回Top8相似的人员信息。
值越大，需要处理的时间越长。建议不要超过10。
        :type MaxPersonNum: int
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出参Score中，只有大于等于FaceMatchThreshold值的结果才会返回。默认为0。取值范围[0.0,100.0) 。
        :type FaceMatchThreshold: float
        :param NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNum = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedPersonInfo = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchPersonsResponse(AbstractModel):
    """SearchPersons返回参数结构体

    """

    def __init__(self):
        """
        :param Results: 识别结果。
        :type Results: list of Result
        :param PersonNum: 搜索的人员库中包含的人员数。若输入图片中所有人脸均不符合质量要求，则返回0。
        :type PersonNum: int
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.PersonNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self.Results.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchPersonsReturnsByGroupRequest(AbstractModel):
    """SearchPersonsReturnsByGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人员库列表，上限60个。数组元素取值为创建人员库接口中的GroupId
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的Url速度和稳定性可能受一定影响。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param MaxFaceNum: 最多识别的人脸数目。默认值为1（仅检测图片中面积最大的那张人脸），最大值为10。
MaxFaceNum用于，当输入的待识别图片包含多张人脸时，设定要搜索的人脸的数量。
例：输入的Image或Url中的图片包含多张人脸，设MaxFaceNum=5，则会识别图片中面积最大的5张人脸。
        :type MaxFaceNum: int
        :param MinFaceSize: 人脸长和宽的最小尺寸，单位为像素。默认为34。低于34将影响搜索精度。建议设置为80。
        :type MinFaceSize: int
        :param MaxPersonNumPerGroup: 被检测到的人脸，对应最多返回的最相似人员数目。默认值为5，最大值为10。  
例，设MaxFaceNum为3，MaxPersonNumPerGroup为5，GroupIds长度为3，则最多可能返回3*5*3=45个人员。
        :type MaxPersonNumPerGroup: int
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出参Score中，只有超过FaceMatchThreshold值的结果才会返回。默认为0。
        :type FaceMatchThreshold: float
        :param NeedPersonInfo: 是否返回人员具体信息。0 为关闭，1 为开启。默认为 0。其他非0非1值默认为0
        :type NeedPersonInfo: int
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNumPerGroup = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedPersonInfo = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchPersonsReturnsByGroupResponse(AbstractModel):
    """SearchPersonsReturnsByGroup返回参数结构体

    """

    def __init__(self):
        """
        :param PersonNum: 搜索的人员库中包含的人员数。若输入图片中所有人脸均不符合质量要求，则返回0。
        :type PersonNum: int
        :param ResultsReturnsByGroup: 识别结果。
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonNum = None
        self.ResultsReturnsByGroup = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonNum = params.get("PersonNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self.ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self.ResultsReturnsByGroup.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class UpgradeGroupFaceModelVersionRequest(AbstractModel):
    """UpgradeGroupFaceModelVersion请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 需要升级的人员库ID。
        :type GroupId: str
        :param FaceModelVersion: 需要升级至的算法模型版本。默认为最新版本。
        :type FaceModelVersion: str
        """
        self.GroupId = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.FaceModelVersion = params.get("FaceModelVersion")


class UpgradeGroupFaceModelVersionResponse(AbstractModel):
    """UpgradeGroupFaceModelVersion返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 升级任务ID，用于查询、获取升级的进度和结果。
        :type JobId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class UpgradeJobInfo(AbstractModel):
    """人员库升级任务信息

    """

    def __init__(self):
        """
        :param JobId: 人员库升级任务ID，用于查询、获取升级的进度和结果。
        :type JobId: str
        :param GroupId: 人员库ID。
        :type GroupId: str
        :param FromFaceModelVersion: 当前算法模型版本。
        :type FromFaceModelVersion: str
        :param ToFaceModelVersion: 目标算法模型版本。
        :type ToFaceModelVersion: str
        :param StartTime: 升级起始时间。 
StartTime的值是自 Unix 纪元时间到Group创建时间的毫秒数。 
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 00:00:00。 
有关更多信息，请参阅 Unix 时间。
        :type StartTime: int
        :param Status: 0表示升级中，1表示升级完毕，2表示回滚完毕，3表示升级失败。
        :type Status: int
        """
        self.JobId = None
        self.GroupId = None
        self.FromFaceModelVersion = None
        self.ToFaceModelVersion = None
        self.StartTime = None
        self.Status = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.GroupId = params.get("GroupId")
        self.FromFaceModelVersion = params.get("FromFaceModelVersion")
        self.ToFaceModelVersion = params.get("ToFaceModelVersion")
        self.StartTime = params.get("StartTime")
        self.Status = params.get("Status")


class VerifyFaceRequest(AbstractModel):
    """VerifyFace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 待验证的人员ID。人员ID具体信息请参考人员库管理相关接口。
        :type PersonId: str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.PersonId = None
        self.Image = None
        self.Url = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class VerifyFaceResponse(AbstractModel):
    """VerifyFace返回参数结构体

    """

    def __init__(self):
        """
        :param Score: 给定的人脸图片与 PersonId 对应人脸的相似度。若 PersonId 下有多张人脸（Face），返回相似度最大的分数。

不同算法版本返回的相似度分数不同。
若需要验证两张图片中人脸是否为同一人，3.0版本误识率千分之一对应分数为40分，误识率万分之一对应分数为50分，误识率十万分之一对应分数为60分。 一般超过50分则可认定为同一人。
2.0版本误识率千分之一对应分数为70分，误识率万分之一对应分数为80分，误识率十万分之一对应分数为90分。 一般超过80分则可认定为同一人。
        :type Score: float
        :param IsMatch: 是否为同一人的判断。
        :type IsMatch: bool
        :param FaceModelVersion: 人脸识别所用的算法模型版本，是该 Person 所在的人员库的算法模型版本。在创建人员库时设置，详情可参考[算法模型版本](https://cloud.tencent.com/document/product/867/40042)
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.IsMatch = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.IsMatch = params.get("IsMatch")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class VerifyPersonRequest(AbstractModel):
    """VerifyPerson请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据。
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 
jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。。
 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param PersonId: 待验证的人员ID。人员ID具体信息请参考人员库管理相关接口。
        :type PersonId: str
        :param QualityControl: 图片质量控制。 
0: 不进行控制； 
1:较低的质量要求，图像存在非常模糊，眼睛鼻子嘴巴遮挡至少其中一种或多种的情况； 
2: 一般的质量要求，图像存在偏亮，偏暗，模糊或一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，至少其中三种的情况； 
3: 较高的质量要求，图像存在偏亮，偏暗，一般模糊，眉毛遮挡，脸颊遮挡，下巴遮挡，其中一到两种的情况； 
4: 很高的质量要求，各个维度均为最好或最多在某一维度上存在轻微问题； 
默认 0。 
若图片质量不满足要求，则返回结果中会提示图片质量检测不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否开启图片旋转识别支持。0为不开启，1为开启。默认为0。本参数的作用为，当图片中的人脸被旋转且图片没有exif信息时，如果不开启图片旋转识别支持则无法正确检测、识别图片中的人脸。若您确认图片包含exif信息或者您确认输入图中人脸不会出现被旋转情况，请不要开启本参数。开启后，整体耗时将可能增加数百毫秒。
        :type NeedRotateDetection: int
        """
        self.Image = None
        self.Url = None
        self.PersonId = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.PersonId = params.get("PersonId")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class VerifyPersonResponse(AbstractModel):
    """VerifyPerson返回参数结构体

    """

    def __init__(self):
        """
        :param Score: 给定的人脸照片与 PersonId 对应的相似度。若 PersonId 下有多张人脸（Face），会融合多张人脸信息进行验证。
        :type Score: float
        :param IsMatch: 是否为同一人的判断。
        :type IsMatch: bool
        :param FaceModelVersion: 人脸识别所用的算法模型版本，是该 Person 所在的人员库的算法模型版本。在创建人员库时设置，详情可参考[算法模型版本](https://cloud.tencent.com/document/product/867/40042)
        :type FaceModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.IsMatch = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.IsMatch = params.get("IsMatch")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")