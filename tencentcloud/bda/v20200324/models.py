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


class BodyDetectResult(AbstractModel):
    """图中检测出来的人体框。

    """

    def __init__(self):
        """
        :param Confidence: 检测出的人体置信度。 
误识率百分之十对应的阈值是0.14；误识率百分之五对应的阈值是0.32；误识率百分之二对应的阈值是0.62；误识率百分之一对应的阈值是0.81。 
通常情况建议使用阈值0.32，可适用大多数情况。
        :type Confidence: float
        :param BodyRect: 图中检测出来的人体框
        :type BodyRect: :class:`tencentcloud.bda.v20200324.models.BodyRect`
        """
        self.Confidence = None
        self.BodyRect = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        if params.get("BodyRect") is not None:
            self.BodyRect = BodyRect()
            self.BodyRect._deserialize(params.get("BodyRect"))


class BodyRect(AbstractModel):
    """人体框

    """

    def __init__(self):
        """
        :param X: 人体框左上角横坐标。
        :type X: int
        :param Y: 人体框左上角纵坐标。
        :type Y: int
        :param Width: 人体宽度。
        :type Width: int
        :param Height: 人体高度。
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


class Candidate(AbstractModel):
    """识别出的最相似候选人。

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
        :type PersonId: str
        :param TraceId: 人体轨迹ID。
        :type TraceId: str
        :param Score: 候选者的匹配得分。 
十万人体库下，误识率百分之五对应的分数为70分；误识率百分之二对应的分数为80分；误识率百分之一对应的分数为90分。
 
二十万人体库下，误识率百分之五对应的分数为80分；误识率百分之二对应的分数为90分；误识率百分之一对应的分数为95分。
 
通常情况建议使用分数80分（保召回）。若希望获得较高精度，建议使用分数90分（保准确）。
        :type Score: float
        """
        self.PersonId = None
        self.TraceId = None
        self.Score = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")
        self.Score = params.get("Score")


class CreateGroupRequest(AbstractModel):
    """CreateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 人体库名称，[1,60]个字符，可修改，不可重复。
        :type GroupName: str
        :param GroupId: 人体库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。
        :type GroupId: str
        :param Tag: 人体库信息备注，[0，40]个字符。
        :type Tag: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。 
目前入参仅支持 “1.0”1个输入。 默认为"1.0"。  
不同算法模型版本对应的人体识别算法不同，新版本的整体效果会优于旧版本，后续我们将推出更新版本。
        :type BodyModelVersion: str
        """
        self.GroupName = None
        self.GroupId = None
        self.Tag = None
        self.BodyModelVersion = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.Tag = params.get("Tag")
        self.BodyModelVersion = params.get("BodyModelVersion")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param PersonId: 人员ID，单个腾讯云账号下不可修改，不可重复。 
支持英文、数字、-%@#&_，，长度限制64B。
        :type PersonId: str
        :param Trace: 人体轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        self.GroupId = None
        self.PersonName = None
        self.PersonId = None
        self.Trace = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回参数结构体

    """

    def __init__(self):
        """
        :param TraceId: 人员轨迹唯一标识。
        :type TraceId: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。
RetCode 的顺序和入参中Images 或 Urls 的顺序一致。
        :type InputRetCodeDetails: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.BodyModelVersion = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.RequestId = params.get("RequestId")


class CreateTraceRequest(AbstractModel):
    """CreateTrace请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
        :type PersonId: str
        :param Trace: 人体轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        """
        self.PersonId = None
        self.Trace = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))


class CreateTraceResponse(AbstractModel):
    """CreateTrace返回参数结构体

    """

    def __init__(self):
        """
        :param TraceId: 人员轨迹唯一标识。
        :type TraceId: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。
        :type InputRetCodeDetails: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.BodyModelVersion = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人体库ID。
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


class DeletePersonRequest(AbstractModel):
    """DeletePerson请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
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


class DetectBodyRequest(AbstractModel):
    """DetectBody请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 人体图片 Base64 数据。
图片 base64 编码后大小不可超过5M。
图片分辨率不得超过 2048*2048。
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 人体图片 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片 base64 编码后大小不可超过5M。 
图片分辨率不得超过 2048*2048。
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        :param MaxBodyNum: 最多检测的人体数目，默认值为1（仅检测图片中面积最大的那个人体）； 最大值10 ，检测图片中面积最大的10个人体。
        :type MaxBodyNum: int
        """
        self.Image = None
        self.Url = None
        self.MaxBodyNum = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxBodyNum = params.get("MaxBodyNum")


class DetectBodyResponse(AbstractModel):
    """DetectBody返回参数结构体

    """

    def __init__(self):
        """
        :param BodyDetectResults: 图中检测出来的人体框。
        :type BodyDetectResults: list of BodyDetectResult
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BodyDetectResults = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BodyDetectResults") is not None:
            self.BodyDetectResults = []
            for item in params.get("BodyDetectResults"):
                obj = BodyDetectResult()
                obj._deserialize(item)
                self.BodyDetectResults.append(obj)
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList请求参数结构体

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


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回参数结构体

    """

    def __init__(self):
        """
        :param GroupInfos: 返回的人体库信息。
        :type GroupInfos: list of GroupInfo
        :param GroupNum: 人体库总数量。
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


class GetPersonListRequest(AbstractModel):
    """GetPersonList请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人体库ID。
        :type GroupId: str
        :param Offset: 起始序号，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为10，最大值为1000。
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
        :param PersonInfos: 返回的人员信息。
        :type PersonInfos: list of PersonInfo
        :param PersonNum: 该人体库的人员数量。
        :type PersonNum: int
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonInfos = None
        self.PersonNum = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self.PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfos.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """返回的人员库信息。

    """

    def __init__(self):
        """
        :param GroupName: 人体库名称。
        :type GroupName: str
        :param GroupId: 人体库ID。
        :type GroupId: str
        :param Tag: 人体库信息备注。
        :type Tag: str
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param CreationTimestamp: Group的创建时间和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 纪元时间到Group创建时间的毫秒数。  
Unix 纪元时间是 1970 年 1 月 1 日星期四，协调世界时 (UTC) 。
        :type CreationTimestamp: int
        """
        self.GroupName = None
        self.GroupId = None
        self.Tag = None
        self.BodyModelVersion = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.Tag = params.get("Tag")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 人体库ID。
        :type GroupId: str
        :param GroupName: 人体库名称。
        :type GroupName: str
        :param Tag: 人体库信息备注。
        :type Tag: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
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


class ModifyPersonInfoRequest(AbstractModel):
    """ModifyPersonInfo请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 人员ID。
        :type PersonId: str
        :param PersonName: 人员名称。
        :type PersonName: str
        """
        self.PersonId = None
        self.PersonName = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")


class ModifyPersonInfoResponse(AbstractModel):
    """ModifyPersonInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PersonInfo(AbstractModel):
    """人员信息。

    """

    def __init__(self):
        """
        :param PersonName: 人员名称。
        :type PersonName: str
        :param PersonId: 人员ID。
        :type PersonId: str
        :param TraceInfos: 包含的人体轨迹图片信息列表。
        :type TraceInfos: list of TraceInfo
        """
        self.PersonName = None
        self.PersonId = None
        self.TraceInfos = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        if params.get("TraceInfos") is not None:
            self.TraceInfos = []
            for item in params.get("TraceInfos"):
                obj = TraceInfo()
                obj._deserialize(item)
                self.TraceInfos.append(obj)


class SearchTraceRequest(AbstractModel):
    """SearchTrace请求参数结构体

    """

    def __init__(self):
        """
        :param GroupId: 希望搜索的人体库ID。
        :type GroupId: str
        :param Trace: 人体轨迹信息。
        :type Trace: :class:`tencentcloud.bda.v20200324.models.Trace`
        :param MaxPersonNum: 单张被识别的人体轨迹返回的最相似人员数量。
默认值为5，最大值为100。
 例，设MaxPersonNum为8，则返回Top8相似的人员信息。 值越大，需要处理的时间越长。建议不要超过10。
        :type MaxPersonNum: int
        :param TraceMatchThreshold: 出参Score中，只有超过TraceMatchThreshold值的结果才会返回。
默认为0。范围[0, 100.0]。
        :type TraceMatchThreshold: float
        """
        self.GroupId = None
        self.Trace = None
        self.MaxPersonNum = None
        self.TraceMatchThreshold = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.TraceMatchThreshold = params.get("TraceMatchThreshold")


class SearchTraceResponse(AbstractModel):
    """SearchTrace返回参数结构体

    """

    def __init__(self):
        """
        :param Candidates: 识别出的最相似候选人。
        :type Candidates: list of Candidate
        :param InputRetCode: 输入的人体轨迹图片中的合法性校验结果。
只有为0时结果才有意义。
-1001: 输入图片不合法。-1002: 输入图片不能构成轨迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 输入的人体轨迹图片中的合法性校验结果详情。 
-1101:图片无效，-1102:url不合法。-1103:图片过大。-1104:图片下载失败。-1105:图片解码失败。-1109:图片分辨率过高。-2023:轨迹中有非同人图片。-2024: 轨迹提取失败。-2025: 人体检测失败。
        :type InputRetCodeDetails: list of int
        :param BodyModelVersion: 人体识别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Candidates = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class SegmentPortraitPicRequest(AbstractModel):
    """SegmentPortraitPic请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。
图片分辨率须小于2000*2000。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Image: str
        :param Url: 图片的 Url 。
Url、Image必须提供一个，如果都提供，只使用 Url。
图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Url: str
        """
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class SegmentPortraitPicResponse(AbstractModel):
    """SegmentPortraitPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: 处理后的图片 base64 数据，透明背景图
        :type ResultImage: str
        :param ResultMask: 一个通过 Base64 编码的文件，解码后文件由 Float 型浮点数组成。这些浮点数代表原图从左上角开始的每一行的每一个像素点，每一个浮点数的值是原图相应像素点位于人体轮廓内的置信度（0-1）转化的灰度值（0-255）
        :type ResultMask: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.ResultMask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultMask = params.get("ResultMask")
        self.RequestId = params.get("RequestId")


class Trace(AbstractModel):
    """人体轨迹信息

    """

    def __init__(self):
        """
        :param Images: 人体轨迹图片 Base64 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Images: list of str
        :param Urls: 人体轨迹图片 Url 数组。 
数组长度最小为1最大为5。 
单个图片 base64 编码后大小不可超过2M。 
Urls、Images必须提供一个，如果都提供，只使用 Urls。 
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。
        :type Urls: list of str
        :param BodyRects: 若输入的Images 和 Urls 是已经裁剪后的人体小图，则可以忽略本参数。 
若否，或图片中包含多个人体，则需要通过本参数来指定图片中的人体框。 
顺序对应 Images 或 Urls 中的顺序。  
当不输入本参数时，我们将认为输入图片已是经过裁剪后的人体小图，不会进行人体检测而直接进行特征提取处理。
        :type BodyRects: list of BodyRect
        """
        self.Images = None
        self.Urls = None
        self.BodyRects = None


    def _deserialize(self, params):
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")
        if params.get("BodyRects") is not None:
            self.BodyRects = []
            for item in params.get("BodyRects"):
                obj = BodyRect()
                obj._deserialize(item)
                self.BodyRects.append(obj)


class TraceInfo(AbstractModel):
    """人体轨迹信息。

    """

    def __init__(self):
        """
        :param TraceId: 人体轨迹ID。
        :type TraceId: str
        :param BodyIds: 包含的人体轨迹图片Id列表。
        :type BodyIds: list of str
        """
        self.TraceId = None
        self.BodyIds = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyIds = params.get("BodyIds")