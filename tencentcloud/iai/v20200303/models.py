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


class AnalyzeFaceRequest(AbstractModel):
    """AnalyzeFace请求参数结构体

    """

    def __init__(self):
        """
        :param Mode: 检测模式。0 为检测所有出现的人脸， 1 为检测面积最大的人脸。默认为 0。最多返回 10 张人脸的五官定位（人脸关键点）具体信息。
        :type Mode: int
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageA: str
        :param ImageB: B 图片 base64 数据，base64 编码后大小不可超过5M。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type ImageB: str
        :param UrlA: A 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
A 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type UrlA: str
        :param UrlB: B 图片的 Url ，对应图片 base64 编码后大小不可超过5M。
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
        :param PersonId: 人员ID
        :type PersonId: str
        :param GroupIds: 待加入的人员库列表
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
        :param PersonId: 人员ID。
        :type PersonId: str
        :param Images: 图片 base64 数据，base64 编码后大小不可超过5M。
人员人脸总数量不可超过5张。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param Urls: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
        :param GroupId: 待加入的人员库ID。
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
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
        :param PersonId: 人员ID
        :type PersonId: str
        :param FaceIds: 待删除的人脸ID列表
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
        :param GroupId: 人员库ID。
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
        :param PersonId: 人员ID
        :type PersonId: str
        :param GroupId: 人员库ID
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
        :param PersonId: 人员ID
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
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M（图片的宽高比请接近3:4，不符合宽高比的图片返回的分值不具备参考意义）。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
        :type X: int
        :param Y: 人脸框左上角纵坐标。 
人脸框包含人脸五官位置并在此基础上进行一定的扩展，若人脸框超出图片范围，会导致坐标负值。 
若需截取完整人脸，可以在完整分completess满足需求的情况下，将负值坐标取0。
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
        :param GroupId: 人员库 ID。
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
        :param PersonId: 人员ID
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
        :param Gender: 人员性别
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
        :param PersonId: 人员ID
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
        :param GroupId: 人员库ID
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
        :param GroupId: 人员库ID
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
        :param JobId: 查重任务ID，用于查询、获取查重的进度和结果。
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
        :param GroupId: 人员库ID
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
        :param PersonId: 人员ID
        :type PersonId: str
        :param PersonName: 需要修改的人员名称
        :type PersonName: str
        :param Gender: 需要修改的人员性别
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
        :param GroupId: 人员库ID
        :type GroupId: str
        :param PersonId: 人员ID
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


class SearchFacesRequest(AbstractModel):
    """SearchFaces请求参数结构体

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人员库列表，上限100个。
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
        :param GroupIds: 希望搜索的人员库列表，上限60个。
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
        :param GroupIds: 希望搜索的人员库列表，上限100个。
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
        :param GroupIds: 希望搜索的人员库列表，上限60个。
        :type GroupIds: list of str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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


class VerifyFaceRequest(AbstractModel):
    """VerifyFace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 待验证的人员ID。人员ID具体信息请参考人员库管理相关接口。
        :type PersonId: str
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。
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
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
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
若图片中包含多张人脸，只选取其中人脸面积最大的人脸。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。 图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
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
        :param FaceModelVersion: 人脸识别所用的算法模型版本。
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