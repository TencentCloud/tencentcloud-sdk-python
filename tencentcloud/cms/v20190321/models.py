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


class AudioModerationRequest(AbstractModel):
    """AudioModeration请求参数结构体

    """

    def __init__(self):
        """
        :param CallbackUrl: 回调URL，音频识别结果将以POST请求方式发送到此地址
        :type CallbackUrl: str
        :param FileContent: 音频内容的base64
        :type FileContent: str
        :param FileMD5: 音频文件的MD5值
        :type FileMD5: str
        :param FileUrl: 音频内容Url ，其中FileUrl和FileContent二选一
        :type FileUrl: str
        """
        self.CallbackUrl = None
        self.FileContent = None
        self.FileMD5 = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.FileContent = params.get("FileContent")
        self.FileMD5 = params.get("FileMD5")
        self.FileUrl = params.get("FileUrl")


class AudioModerationResponse(AbstractModel):
    """AudioModeration返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessCode: 业务返回码 
60001：成功请求回调任务
        :type BusinessCode: int
        :param Data: 识别返回结果
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCode = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CodeDetail(AbstractModel):
    """从图片中检测到的二维码，可能为多个

    """

    def __init__(self):
        """
        :param CodePosition: 二维码在图片中的位置，由4个点的坐标表示
        :type CodePosition: list of CodePosition
        :param CodeCharset: 二维码文本的编码格式
        :type CodeCharset: str
        :param CodeText: 二维码的文本内容
        :type CodeText: str
        :param CodeType: 二维码的类型：1：ONED_BARCODE，2：QRCOD，3:WXCODE，4：PDF417，5:DATAMATRIX
        :type CodeType: int
        """
        self.CodePosition = None
        self.CodeCharset = None
        self.CodeText = None
        self.CodeType = None


    def _deserialize(self, params):
        if params.get("CodePosition") is not None:
            self.CodePosition = []
            for item in params.get("CodePosition"):
                obj = CodePosition()
                obj._deserialize(item)
                self.CodePosition.append(obj)
        self.CodeCharset = params.get("CodeCharset")
        self.CodeText = params.get("CodeText")
        self.CodeType = params.get("CodeType")


class CodeDetect(AbstractModel):
    """图片二维码详情

    """

    def __init__(self):
        """
        :param ModerationDetail: 从图片中检测到的二维码，可能为多个
        :type ModerationDetail: list of CodeDetail
        :param ModerationCode: 检测是否成功，0：成功，-1：出错
        :type ModerationCode: int
        """
        self.ModerationDetail = None
        self.ModerationCode = None


    def _deserialize(self, params):
        if params.get("ModerationDetail") is not None:
            self.ModerationDetail = []
            for item in params.get("ModerationDetail"):
                obj = CodeDetail()
                obj._deserialize(item)
                self.ModerationDetail.append(obj)
        self.ModerationCode = params.get("ModerationCode")


class CodePosition(AbstractModel):
    """二维码在图片中的位置，由4个点的坐标表示

    """

    def __init__(self):
        """
        :param FloatX: 二维码边界点X轴坐标
        :type FloatX: float
        :param FloatY: 二维码边界点Y轴坐标
        :type FloatY: float
        """
        self.FloatX = None
        self.FloatY = None


    def _deserialize(self, params):
        self.FloatX = params.get("FloatX")
        self.FloatY = params.get("FloatY")


class CreateFileSampleRequest(AbstractModel):
    """CreateFileSample请求参数结构体

    """

    def __init__(self):
        """
        :param Contents: 文件类型结构数组
        :type Contents: list of FileSample
        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
21000：综合
20105：广告引流
        :type EvilType: int
        :param FileType: 文件类型
image：图片
audio：音频
video：视频
        :type FileType: str
        :param Label: 样本类型
1：黑库
2：白库
        :type Label: int
        """
        self.Contents = None
        self.EvilType = None
        self.FileType = None
        self.Label = None


    def _deserialize(self, params):
        if params.get("Contents") is not None:
            self.Contents = []
            for item in params.get("Contents"):
                obj = FileSample()
                obj._deserialize(item)
                self.Contents.append(obj)
        self.EvilType = params.get("EvilType")
        self.FileType = params.get("FileType")
        self.Label = params.get("Label")


class CreateFileSampleResponse(AbstractModel):
    """CreateFileSample返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态
1：已完成
2：处理中
        :type Progress: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class CreateTextSampleRequest(AbstractModel):
    """CreateTextSample请求参数结构体

    """

    def __init__(self):
        """
        :param Contents: 关键词数组
        :type Contents: list of str
        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
21000：综合
20105：广告引流
        :type EvilType: int
        :param Label: 样本类型
1：黑库
2：白库
        :type Label: int
        """
        self.Contents = None
        self.EvilType = None
        self.Label = None


    def _deserialize(self, params):
        self.Contents = params.get("Contents")
        self.EvilType = params.get("EvilType")
        self.Label = params.get("Label")


class CreateTextSampleResponse(AbstractModel):
    """CreateTextSample返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态
1：已完成
2：处理中
        :type Progress: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteFileSampleRequest(AbstractModel):
    """DeleteFileSample请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 唯一标识数组
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteFileSampleResponse(AbstractModel):
    """DeleteFileSample返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态
1：已完成
2：处理中
        :type Progress: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteTextSampleRequest(AbstractModel):
    """DeleteTextSample请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 唯一标识数组，目前暂时只支持单个删除
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteTextSampleResponse(AbstractModel):
    """DeleteTextSample返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态
1：已完成
2：处理中
        :type Progress: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeFileSampleRequest(AbstractModel):
    """DescribeFileSample请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过标签值进行筛选
        :type Filters: list of Filter
        :param Limit: 数量限制，默认为20，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc
        :type OrderDirection: str
        :param OrderField: 按某个字段排序，目前仅支持CreatedAt排序
        :type OrderField: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderDirection = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderDirection = params.get("OrderDirection")
        self.OrderField = params.get("OrderField")


class DescribeFileSampleResponse(AbstractModel):
    """DescribeFileSample返回参数结构体

    """

    def __init__(self):
        """
        :param FileSampleSet: 符合要求的样本的信息
        :type FileSampleSet: list of FileSampleInfo
        :param TotalCount: 符合要求的样本的数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileSampleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSampleSet") is not None:
            self.FileSampleSet = []
            for item in params.get("FileSampleSet"):
                obj = FileSampleInfo()
                obj._deserialize(item)
                self.FileSampleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeModerationOverviewRequest(AbstractModel):
    """DescribeModerationOverview请求参数结构体

    """

    def __init__(self):
        """
        :param Date: 日期，如2019-01-01， 查询该日期的概览数据
        :type Date: str
        :param ServiceTypes: 服务类型数组，可以动态配置，Text:文本，Image:图片，Audio:音频，Video:视频, 使用"ALL"表示所有类型, 不区分大小写，如 ["Text", "Image"]查询文本和图片服务的数据，["all"]查询所有服务的数据。
        :type ServiceTypes: list of str
        :param Channels: 渠道号数组，1:直播 2:点播 3:IM 4:GME，统计指定渠道组合的汇总数据，如[1,2]表示获取直播和点播两个渠道的汇总数据，不填[]为所有渠道汇总数据
        :type Channels: list of int non-negative
        """
        self.Date = None
        self.ServiceTypes = None
        self.Channels = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.ServiceTypes = params.get("ServiceTypes")
        self.Channels = params.get("Channels")


class DescribeModerationOverviewResponse(AbstractModel):
    """DescribeModerationOverview返回参数结构体

    """

    def __init__(self):
        """
        :param Results: 概览数据集合
        :type Results: list of OverviewRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = OverviewRecord()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTextSampleRequest(AbstractModel):
    """DescribeTextSample请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过标签值进行筛选
        :type Filters: list of Filter
        :param Limit: 数量限制，默认为20，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc
        :type OrderDirection: str
        :param OrderField: 按某个字段排序，目前仅支持CreatedAt排序
        :type OrderField: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderDirection = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderDirection = params.get("OrderDirection")
        self.OrderField = params.get("OrderField")


class DescribeTextSampleResponse(AbstractModel):
    """DescribeTextSample返回参数结构体

    """

    def __init__(self):
        """
        :param TextSampleSet: 符合要求的样本的信息
        :type TextSampleSet: list of TextSample
        :param TotalCount: 符合要求的样本的数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TextSampleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextSampleSet") is not None:
            self.TextSampleSet = []
            for item in params.get("TextSampleSet"):
                obj = TextSample()
                obj._deserialize(item)
                self.TextSampleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class FileSample(AbstractModel):
    """文件类型样本

    """

    def __init__(self):
        """
        :param FileMd5: 文件md5
        :type FileMd5: str
        :param FileName: 文件名称
        :type FileName: str
        :param FileUrl: 文件url
        :type FileUrl: str
        """
        self.FileMd5 = None
        self.FileName = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.FileMd5 = params.get("FileMd5")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")


class FileSampleInfo(AbstractModel):
    """文件样本返回信息

    """

    def __init__(self):
        """
        :param Code: 处理错误码
        :type Code: int
        :param CreatedAt: 创建时间戳
        :type CreatedAt: int
        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
21000：综合
        :type EvilType: int
        :param FileMd5: 文件的md5
        :type FileMd5: str
        :param FileName: 文件名称
        :type FileName: str
        :param FileType: 文件类型
        :type FileType: str
        :param Id: 唯一标识
        :type Id: str
        :param Label: 样本类型
1：黑库
2：白库
        :type Label: int
        :param Status: 任务状态
1：已完成
2：处理中
        :type Status: int
        :param FileUrl: 文件的url
        :type FileUrl: str
        """
        self.Code = None
        self.CreatedAt = None
        self.EvilType = None
        self.FileMd5 = None
        self.FileName = None
        self.FileType = None
        self.Id = None
        self.Label = None
        self.Status = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.CreatedAt = params.get("CreatedAt")
        self.EvilType = params.get("EvilType")
        self.FileMd5 = params.get("FileMd5")
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.Id = params.get("Id")
        self.Label = params.get("Label")
        self.Status = params.get("Status")
        self.FileUrl = params.get("FileUrl")


class Filter(AbstractModel):
    """筛选数据结构

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段
        :type Name: str
        :param Value: 需要过滤字段的值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class ImageData(AbstractModel):
    """图片识别结果详情

    """

    def __init__(self):
        """
        :param EvilFlag: 是否恶意 0：正常 1：可疑
        :type EvilFlag: int
        :param EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
20103：性感
24001：暴恐
21000：综合
        :type EvilType: int
        :param CodeDetect: 图片二维码详情
        :type CodeDetect: :class:`tencentcloud.cms.v20190321.models.CodeDetect`
        :param HotDetect: 图片性感详情
        :type HotDetect: :class:`tencentcloud.cms.v20190321.models.ImageHotDetect`
        :param IllegalDetect: 图片违法详情
        :type IllegalDetect: :class:`tencentcloud.cms.v20190321.models.ImageIllegalDetect`
        :param OCRDetect: 图片OCR详情
        :type OCRDetect: :class:`tencentcloud.cms.v20190321.models.OCRDetect`
        :param PolityDetect: 图片涉政详情
        :type PolityDetect: :class:`tencentcloud.cms.v20190321.models.ImagePolityDetect`
        :param PornDetect: 图片涉黄详情
        :type PornDetect: :class:`tencentcloud.cms.v20190321.models.ImagePornDetect`
        :param Similar: 图片相似度详情
        :type Similar: :class:`tencentcloud.cms.v20190321.models.Similar`
        :param TerrorDetect: 图片暴恐详情
        :type TerrorDetect: :class:`tencentcloud.cms.v20190321.models.ImageTerrorDetect`
        """
        self.EvilFlag = None
        self.EvilType = None
        self.CodeDetect = None
        self.HotDetect = None
        self.IllegalDetect = None
        self.OCRDetect = None
        self.PolityDetect = None
        self.PornDetect = None
        self.Similar = None
        self.TerrorDetect = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        if params.get("CodeDetect") is not None:
            self.CodeDetect = CodeDetect()
            self.CodeDetect._deserialize(params.get("CodeDetect"))
        if params.get("HotDetect") is not None:
            self.HotDetect = ImageHotDetect()
            self.HotDetect._deserialize(params.get("HotDetect"))
        if params.get("IllegalDetect") is not None:
            self.IllegalDetect = ImageIllegalDetect()
            self.IllegalDetect._deserialize(params.get("IllegalDetect"))
        if params.get("OCRDetect") is not None:
            self.OCRDetect = OCRDetect()
            self.OCRDetect._deserialize(params.get("OCRDetect"))
        if params.get("PolityDetect") is not None:
            self.PolityDetect = ImagePolityDetect()
            self.PolityDetect._deserialize(params.get("PolityDetect"))
        if params.get("PornDetect") is not None:
            self.PornDetect = ImagePornDetect()
            self.PornDetect._deserialize(params.get("PornDetect"))
        if params.get("Similar") is not None:
            self.Similar = Similar()
            self.Similar._deserialize(params.get("Similar"))
        if params.get("TerrorDetect") is not None:
            self.TerrorDetect = ImageTerrorDetect()
            self.TerrorDetect._deserialize(params.get("TerrorDetect"))


class ImageHotDetect(AbstractModel):
    """图片性感详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常
20103：性感
        :type EvilType: int
        :param HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param Labels: 性感标签：性感特征中文描述
        :type Labels: list of str
        :param Score: 性感分：分值范围 0-100，分数越高性感倾向越明显
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")


class ImageIllegalDetect(AbstractModel):
    """图片违法详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常 
20006：涉毒违法
        :type EvilType: int
        :param HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param Labels: 违法标签：返回违法特征中文描述，如赌桌，枪支
        :type Labels: list of str
        :param Score: 违法分：分值范围 0-100，分数越高违法倾向越明显
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 文件内容 Base64,与FileUrl必须二填一
        :type FileContent: str
        :param FileMD5: 文件MD5值
        :type FileMD5: str
        :param FileUrl: 文件地址
        :type FileUrl: str
        """
        self.FileContent = None
        self.FileMD5 = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileMD5 = params.get("FileMD5")
        self.FileUrl = params.get("FileUrl")


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 识别结果
        :type Data: :class:`tencentcloud.cms.v20190321.models.ImageData`
        :param BusinessCode: 业务返回码
        :type BusinessCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.BusinessCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ImageData()
            self.Data._deserialize(params.get("Data"))
        self.BusinessCode = params.get("BusinessCode")
        self.RequestId = params.get("RequestId")


class ImagePolityDetect(AbstractModel):
    """图片涉政详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常 
20001：政治
        :type EvilType: int
        :param HitFlag: 处置判定  0：正常 1：可疑
        :type HitFlag: int
        :param FaceNames: 命中的人脸名称
        :type FaceNames: list of str
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param PolityItems: 命中的政治物品名称
        :type PolityItems: list of str
        :param Score: 政治（人脸）分：分值范围 0-100，分数越高可疑程度越高
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.FaceNames = None
        self.Keywords = None
        self.PolityItems = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.FaceNames = params.get("FaceNames")
        self.Keywords = params.get("Keywords")
        self.PolityItems = params.get("PolityItems")
        self.Score = params.get("Score")


class ImagePornDetect(AbstractModel):
    """图片涉黄详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常
20002：色情
        :type EvilType: int
        :param HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param Labels: 色情标签：色情特征中文描述
        :type Labels: list of str
        :param Score: 色情分：分值范围 0-100，分数越高色情倾向越明显
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")


class ImageTerrorDetect(AbstractModel):
    """图片暴恐详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常
24001：暴恐
        :type EvilType: int
        :param HitFlag: 处置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param Labels: 暴恐标签：返回暴恐特征中文描述
        :type Labels: list of str
        :param Score: 暴恐分：分值范围0--100，分数越高暴恐倾向越明显
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")


class OCRDetect(AbstractModel):
    """OCR识别结果详情

    """

    def __init__(self):
        """
        :param TextInfo: 识别到的文本信息
        :type TextInfo: str
        """
        self.TextInfo = None


    def _deserialize(self, params):
        self.TextInfo = params.get("TextInfo")


class OverviewRecord(AbstractModel):
    """概览数据

    """

    def __init__(self):
        """
        :param EvilCount: 调用恶意量
        :type EvilCount: int
        :param ServiceType: Text表示文本，Image表示图片，Audio表示音频，Video表示视频
        :type ServiceType: str
        :param TotalCount: 调用总量
        :type TotalCount: int
        :param Yoy: 恶意量同比增长率
        :type Yoy: str
        """
        self.EvilCount = None
        self.ServiceType = None
        self.TotalCount = None
        self.Yoy = None


    def _deserialize(self, params):
        self.EvilCount = params.get("EvilCount")
        self.ServiceType = params.get("ServiceType")
        self.TotalCount = params.get("TotalCount")
        self.Yoy = params.get("Yoy")


class Similar(AbstractModel):
    """相似度详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
21000：综合
        :type EvilType: int
        :param HitFlag: 处置判定 0：未匹配到 1：恶意 2：白样本
        :type HitFlag: int
        :param SeedUrl: 返回的种子url
        :type SeedUrl: str
        """
        self.EvilType = None
        self.HitFlag = None
        self.SeedUrl = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.SeedUrl = params.get("SeedUrl")


class TextData(AbstractModel):
    """文本识别结果详情

    """

    def __init__(self):
        """
        :param EvilFlag: 是否恶意 0：正常 1：可疑
        :type EvilFlag: int
        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂
20105：广告引流 
24001：暴恐
21000：综合
        :type EvilType: int
        :param Keywords: 命中的关键词
        :type Keywords: list of str
        """
        self.EvilFlag = None
        self.EvilType = None
        self.Keywords = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        self.Keywords = params.get("Keywords")


class TextModerationRequest(AbstractModel):
    """TextModeration请求参数结构体

    """

    def __init__(self):
        """
        :param Content: 文本内容Base64编码
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")


class TextModerationResponse(AbstractModel):
    """TextModeration返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 识别结果
        :type Data: :class:`tencentcloud.cms.v20190321.models.TextData`
        :param BusinessCode: 业务返回码
        :type BusinessCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.BusinessCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TextData()
            self.Data._deserialize(params.get("Data"))
        self.BusinessCode = params.get("BusinessCode")
        self.RequestId = params.get("RequestId")


class TextSample(AbstractModel):
    """文字样本信息

    """

    def __init__(self):
        """
        :param Code: 处理错误码
        :type Code: int
        :param Content: 关键词
        :type Content: str
        :param CreatedAt: 创建时间戳
        :type CreatedAt: int
        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
20105：广告引流 
24001：暴恐
20004/21000：综合
        :type EvilType: int
        :param Id: 唯一标识
        :type Id: str
        :param Label: 样本类型
1：黑库
2：白库
        :type Label: int
        :param Status: 任务状态
1：已完成
2：处理中
        :type Status: int
        """
        self.Code = None
        self.Content = None
        self.CreatedAt = None
        self.EvilType = None
        self.Id = None
        self.Label = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Content = params.get("Content")
        self.CreatedAt = params.get("CreatedAt")
        self.EvilType = params.get("EvilType")
        self.Id = params.get("Id")
        self.Label = params.get("Label")
        self.Status = params.get("Status")


class VideoModerationRequest(AbstractModel):
    """VideoModeration请求参数结构体

    """

    def __init__(self):
        """
        :param CallbackUrl: 回调URL，音频识别结果将以POST请求方式发送到此地址
        :type CallbackUrl: str
        :param FileMD5: 视频文件MD5
        :type FileMD5: str
        :param FileContent: 视频内容base64
        :type FileContent: str
        :param FileUrl: 视频内容Url,其中FileUrl与FileContent二选一
        :type FileUrl: str
        """
        self.CallbackUrl = None
        self.FileMD5 = None
        self.FileContent = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.FileMD5 = params.get("FileMD5")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")


class VideoModerationResponse(AbstractModel):
    """VideoModeration返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessCode: 业务返回码
60001：成功请求回调任务
        :type BusinessCode: int
        :param Data: 识别返回结果
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCode = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")