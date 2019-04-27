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
        :param CallbackUrl: 回调url
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
24001：暴恐
21000：综合
        :type EvilType: int
        :param IllegalDetect: 图片违法详情
        :type IllegalDetect: :class:`tencentcloud.cms.v20190321.models.ImageIllegalDetect`
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
        self.IllegalDetect = None
        self.PolityDetect = None
        self.PornDetect = None
        self.Similar = None
        self.TerrorDetect = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        if params.get("IllegalDetect") is not None:
            self.IllegalDetect = ImageIllegalDetect()
            self.IllegalDetect._deserialize(params.get("IllegalDetect"))
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


class ImageIllegalDetect(AbstractModel):
    """图片违法详情

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
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
21000：综合
        :type EvilType: int
        :param HitFlag: 处置判定  0：正常 1：可疑
        :type HitFlag: int
        :param FaceNames: 命中的人脸名称
        :type FaceNames: list of str
        :param Keywords: 关键词明细
        :type Keywords: list of str
        :param Score: 政治（人脸）分：分值范围 0-100，分数越高可疑程度越高
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.FaceNames = None
        self.Keywords = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.FaceNames = params.get("FaceNames")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")


class ImagePornDetect(AbstractModel):
    """图片涉黄详情

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
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
21000：综合
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


class VideoModerationRequest(AbstractModel):
    """VideoModeration请求参数结构体

    """

    def __init__(self):
        """
        :param CallbackUrl: 回调Url
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