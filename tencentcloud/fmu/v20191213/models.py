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


class BeautifyPicRequest(AbstractModel):
    """BeautifyPic请求参数结构体

    """

    def __init__(self):
        """
        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param Url: 图片的 Url 。对应图片 base64 编码后大小不可超过5M。 
Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Url: str\n        :param Whitening: 美白程度，取值范围[0,100]。0不美白，100代表最高程度。默认值30。\n        :type Whitening: int\n        :param Smoothing: 磨皮程度，取值范围[0,100]。0不磨皮，100代表最高程度。默认值10。\n        :type Smoothing: int\n        :param FaceLifting: 瘦脸程度，取值范围[0,100]。0不瘦脸，100代表最高程度。默认值70。\n        :type FaceLifting: int\n        :param EyeEnlarging: 大眼程度，取值范围[0,100]。0不大眼，100代表最高程度。默认值70。\n        :type EyeEnlarging: int\n        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。\n        :type RspImgType: str\n        """
        self.Image = None
        self.Url = None
        self.Whitening = None
        self.Smoothing = None
        self.FaceLifting = None
        self.EyeEnlarging = None
        self.RspImgType = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.Whitening = params.get("Whitening")
        self.Smoothing = params.get("Smoothing")
        self.FaceLifting = params.get("FaceLifting")
        self.EyeEnlarging = params.get("EyeEnlarging")
        self.RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BeautifyPicResponse(AbstractModel):
    """BeautifyPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64\n        :type ResultImage: str\n        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。\n        :type ResultUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")


class BeautifyVideoOutput(AbstractModel):
    """视频美颜返回结果

    """

    def __init__(self):
        """
        :param VideoUrl: 视频美颜输出的url
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoUrl: str\n        :param VideoMD5: 视频美颜输出的视频MD5，用于校验
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoMD5: str\n        :param CoverImage: 美颜输出的视频封面图base64字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type CoverImage: str\n        :param Width: 视频宽度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Width: int\n        :param Height: 视频高度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Height: int\n        :param Fps: 每秒传输帧数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Fps: float\n        :param DurationInSec: 视频播放时长，单位为秒
注意：此字段可能返回 null，表示取不到有效值。\n        :type DurationInSec: float\n        """
        self.VideoUrl = None
        self.VideoMD5 = None
        self.CoverImage = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.DurationInSec = None


    def _deserialize(self, params):
        self.VideoUrl = params.get("VideoUrl")
        self.VideoMD5 = params.get("VideoMD5")
        self.CoverImage = params.get("CoverImage")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.DurationInSec = params.get("DurationInSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BeautifyVideoRequest(AbstractModel):
    """BeautifyVideo请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 视频url地址\n        :type Url: str\n        :param BeautyParam: 美颜参数 - 美白、平滑、大眼和瘦脸。参数值范围[0, 100]。参数值为0，则不做美颜。参数默认值为0。目前默认取数组第一个元素是对所有人脸美颜。\n        :type BeautyParam: list of BeautyParam\n        :param OutputVideoType: 目前只支持mp4\n        :type OutputVideoType: str\n        """
        self.Url = None
        self.BeautyParam = None
        self.OutputVideoType = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("BeautyParam") is not None:
            self.BeautyParam = []
            for item in params.get("BeautyParam"):
                obj = BeautyParam()
                obj._deserialize(item)
                self.BeautyParam.append(obj)
        self.OutputVideoType = params.get("OutputVideoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BeautifyVideoResponse(AbstractModel):
    """BeautifyVideo返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 视频美颜任务的Job id\n        :type JobId: str\n        :param EstimatedProcessTime: 预估处理时间，粒度为秒\n        :type EstimatedProcessTime: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.JobId = None
        self.EstimatedProcessTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.EstimatedProcessTime = params.get("EstimatedProcessTime")
        self.RequestId = params.get("RequestId")


class BeautyParam(AbstractModel):
    """全局美颜参数，针对所有人脸做美颜。参数全部为0，则为不做美颜

    """

    def __init__(self):
        """
        :param WhitenLevel: 美白程度，取值范围[0,100]。0不美白，100代表最高程度。默认值30。\n        :type WhitenLevel: int\n        :param SmoothingLevel: 磨皮程度，取值范围[0,100]。0不磨皮，100代表最高程度。默认值30。\n        :type SmoothingLevel: int\n        :param EyeEnlargeLevel: 大眼程度，取值范围[0,100]。0不大眼，100代表最高程度。默认值70。\n        :type EyeEnlargeLevel: int\n        :param FaceShrinkLevel: 瘦脸程度，取值范围[0,100]。0不瘦脸，100代表最高程度。默认值70。\n        :type FaceShrinkLevel: int\n        """
        self.WhitenLevel = None
        self.SmoothingLevel = None
        self.EyeEnlargeLevel = None
        self.FaceShrinkLevel = None


    def _deserialize(self, params):
        self.WhitenLevel = params.get("WhitenLevel")
        self.SmoothingLevel = params.get("SmoothingLevel")
        self.EyeEnlargeLevel = params.get("EyeEnlargeLevel")
        self.FaceShrinkLevel = params.get("FaceShrinkLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelBeautifyVideoJobRequest(AbstractModel):
    """CancelBeautifyVideoJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 美颜视频的Job id\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelBeautifyVideoJobResponse(AbstractModel):
    """CancelBeautifyVideoJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateModelRequest(AbstractModel):
    """CreateModel请求参数结构体

    """

    def __init__(self):
        """
        :param LUTFile: 图片base64数据，用于试唇色，要求必须是LUT 格式的cube文件转换成512*512的PNG图片。查看 [LUT文件的使用说明](https://cloud.tencent.com/document/product/1172/41701)。了解 [cube文件转png图片小工具](http://yyb.gtimg.com/aiplat/static/qcloud-cube-to-png.html)。\n        :type LUTFile: str\n        :param Description: 文件描述信息，可用于备注。\n        :type Description: str\n        """
        self.LUTFile = None
        self.Description = None


    def _deserialize(self, params):
        self.LUTFile = params.get("LUTFile")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModelResponse(AbstractModel):
    """CreateModel返回参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 唇色素材ID。\n        :type ModelId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ModelId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.RequestId = params.get("RequestId")


class DeleteModelRequest(AbstractModel):
    """DeleteModel请求参数结构体

    """

    def __init__(self):
        """
        :param ModelId: 素材ID。\n        :type ModelId: str\n        """
        self.ModelId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModelResponse(AbstractModel):
    """DeleteModel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。\n        :type X: int\n        :param Y: 人脸框左上角纵坐标。\n        :type Y: int\n        :param Width: 人脸框宽度。\n        :type Width: int\n        :param Height: 人脸框高度。\n        :type Height: int\n        """
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
        


class GetModelListRequest(AbstractModel):
    """GetModelList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 起始序号，默认值为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认值为10，最大值为100。\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetModelListResponse(AbstractModel):
    """GetModelList返回参数结构体

    """

    def __init__(self):
        """
        :param ModelIdNum: 唇色素材总数量。\n        :type ModelIdNum: int\n        :param ModelInfos: 素材数据
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModelInfos: list of ModelInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ModelIdNum = None
        self.ModelInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelIdNum = params.get("ModelIdNum")
        if params.get("ModelInfos") is not None:
            self.ModelInfos = []
            for item in params.get("ModelInfos"):
                obj = ModelInfo()
                obj._deserialize(item)
                self.ModelInfos.append(obj)
        self.RequestId = params.get("RequestId")


class LipColorInfo(AbstractModel):
    """唇色信息

    """

    def __init__(self):
        """
        :param RGBA: 使用RGBA模型试唇色。\n        :type RGBA: :class:`tencentcloud.fmu.v20191213.models.RGBAInfo`\n        :param ModelId: 使用已注册的 LUT 文件试唇色。  
ModelId 和 RGBA 两个参数只需提供一个，若都提供只使用 ModelId。\n        :type ModelId: str\n        :param FaceRect: 人脸框位置。若不输入则选择 Image 或 Url 中面积最大的人脸。  
您可以通过 [人脸检测与分析](https://cloud.tencent.com/document/api/867/32800)  接口获取人脸框位置信息。\n        :type FaceRect: :class:`tencentcloud.fmu.v20191213.models.FaceRect`\n        :param ModelAlpha: 涂妆浓淡[0,100]。建议取值50。本参数仅控制ModelId对应的涂妆浓淡。\n        :type ModelAlpha: int\n        """
        self.RGBA = None
        self.ModelId = None
        self.FaceRect = None
        self.ModelAlpha = None


    def _deserialize(self, params):
        if params.get("RGBA") is not None:
            self.RGBA = RGBAInfo()
            self.RGBA._deserialize(params.get("RGBA"))
        self.ModelId = params.get("ModelId")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.ModelAlpha = params.get("ModelAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInfo(AbstractModel):
    """LUT素材信息

    """

    def __init__(self):
        """
        :param ModelId: 唇色素材ID\n        :type ModelId: str\n        :param LUTFileUrl: 唇色素材 url 。 LUT 文件 url 5分钟有效。\n        :type LUTFileUrl: str\n        :param Description: 文件描述信息。\n        :type Description: str\n        """
        self.ModelId = None
        self.LUTFileUrl = None
        self.Description = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.LUTFileUrl = params.get("LUTFileUrl")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBeautifyVideoJobRequest(AbstractModel):
    """QueryBeautifyVideoJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 视频美颜Job id\n        :type JobId: str\n        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBeautifyVideoJobResponse(AbstractModel):
    """QueryBeautifyVideoJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobStatus: 当前任务状态：排队中、处理中、处理失败或者处理完成\n        :type JobStatus: str\n        :param BeautifyVideoOutput: 视频美颜输出的结果信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type BeautifyVideoOutput: :class:`tencentcloud.fmu.v20191213.models.BeautifyVideoOutput`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.JobStatus = None
        self.BeautifyVideoOutput = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobStatus = params.get("JobStatus")
        if params.get("BeautifyVideoOutput") is not None:
            self.BeautifyVideoOutput = BeautifyVideoOutput()
            self.BeautifyVideoOutput._deserialize(params.get("BeautifyVideoOutput"))
        self.RequestId = params.get("RequestId")


class RGBAInfo(AbstractModel):
    """RGBA通道信息

    """

    def __init__(self):
        """
        :param R: R通道数值。[0,255]。\n        :type R: int\n        :param G: G通道数值。[0,255]。\n        :type G: int\n        :param B: B通道数值。[0,255]。\n        :type B: int\n        :param A: A通道数值。[0,100]。建议取值50。\n        :type A: int\n        """
        self.R = None
        self.G = None
        self.B = None
        self.A = None


    def _deserialize(self, params):
        self.R = params.get("R")
        self.G = params.get("G")
        self.B = params.get("B")
        self.A = params.get("A")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StyleImageProRequest(AbstractModel):
    """StyleImagePro请求参数结构体

    """

    def __init__(self):
        """
        :param FilterType: 滤镜类型，取值如下： 
1.白茶；2 白皙；3.初夏；4.东京；5.告白；6.暖阳；7.蔷薇；8.清澄；9.清透；10.甜薄荷；11.默认；12.心动；13.哑灰；14.樱桃布丁；15.自然；16.清逸；17.黑白；18.水果；19.爱情；20.冬日；21.相片；22.夏日；23.香氛；24.魅惑；25.悸动；26.沙滩；27.街拍；28.甜美；29.初吻；30.午后；31.活力；32.朦胧；33.悦动；34.时尚；35.气泡；36.柠檬；37.棉花糖；38.小溪；39.丽人；40.咖啡；41.嫩芽；42.热情；43.渐暖；44.早餐；45.白茶；46.白嫩；47.圣代；48.森林；49.冲浪；50.奶咖；51.清澈；52.微风；53.日落；54.水光；55.日系；56.星光；57.阳光；58.落叶；59.生机；60.甜心；61.清逸；62.春意；63.罗马；64.青涩；65.清风；66.暖心；67.海水；68.神秘；69.旧调1；70.旧调2；71.雪顶；72.日光；73.浮云；74.流彩；75.胶片；76.回味；77.奶酪；78.蝴蝶。\n        :type FilterType: int\n        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP 等图片格式，不支持 GIF 图片。\n        :type Url: str\n        :param FilterDegree: 滤镜效果，取值[0,100]，0表示无效果，100表示满滤镜效果。默认值为80。\n        :type FilterDegree: int\n        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。\n        :type RspImgType: str\n        """
        self.FilterType = None
        self.Image = None
        self.Url = None
        self.FilterDegree = None
        self.RspImgType = None


    def _deserialize(self, params):
        self.FilterType = params.get("FilterType")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FilterDegree = params.get("FilterDegree")
        self.RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StyleImageProResponse(AbstractModel):
    """StyleImagePro返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultImage: str\n        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")


class StyleImageRequest(AbstractModel):
    """StyleImage请求参数结构体

    """

    def __init__(self):
        """
        :param FilterType: 滤镜类型，取值如下： 
1.白茶；2 白皙；3.初夏；4.东京；5.告白；6.暖阳；7.蔷薇；8.清澄；9.清透；10.甜薄荷；11.默认；12.心动；13.哑灰；14.樱桃布丁；15.自然；16.清逸；17.黑白；18.水果；19.爱情；20.冬日；21.相片；22.夏日；23.香氛；24.魅惑；25.悸动；26.沙滩；27.街拍；28.甜美；29.初吻；30.午后。\n        :type FilterType: int\n        :param Image: 图片 base64 数据，base64 编码后大小不可超过5M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过5M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。  
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。  
非腾讯云存储的Url速度和稳定性可能受一定影响。  
支持PNG、JPG、JPEG、BMP 等图片格式，不支持 GIF 图片。\n        :type Url: str\n        :param FilterDegree: 滤镜效果，取值[0,100]，0表示无效果，100表示满滤镜效果。默认值为80。\n        :type FilterDegree: int\n        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。\n        :type RspImgType: str\n        """
        self.FilterType = None
        self.Image = None
        self.Url = None
        self.FilterDegree = None
        self.RspImgType = None


    def _deserialize(self, params):
        self.FilterType = params.get("FilterType")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FilterDegree = params.get("FilterDegree")
        self.RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StyleImageResponse(AbstractModel):
    """StyleImage返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultImage: str\n        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResultUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")


class TryLipstickPicRequest(AbstractModel):
    """TryLipstickPic请求参数结构体

    """

    def __init__(self):
        """
        :param LipColorInfos: 唇色信息。 
您可以输入最多3个 LipColorInfo 来实现给一张图中的最多3张人脸试唇色。\n        :type LipColorInfos: list of LipColorInfo\n        :param Image: 图片 base64 数据，base64 编码后大小不可超过6M。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Image: str\n        :param Url: 图片的 Url ，对应图片 base64 编码后大小不可超过6M。 
图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 
图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 
非腾讯云存储的Url速度和稳定性可能受一定影响。 
支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。\n        :type Url: str\n        :param RspImgType: 返回图像方式（base64 或 url ) ，二选一。url有效期为1天。\n        :type RspImgType: str\n        """
        self.LipColorInfos = None
        self.Image = None
        self.Url = None
        self.RspImgType = None


    def _deserialize(self, params):
        if params.get("LipColorInfos") is not None:
            self.LipColorInfos = []
            for item in params.get("LipColorInfos"):
                obj = LipColorInfo()
                obj._deserialize(item)
                self.LipColorInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TryLipstickPicResponse(AbstractModel):
    """TryLipstickPic返回参数结构体

    """

    def __init__(self):
        """
        :param ResultImage: RspImgType 为 base64 时，返回处理后的图片 base64 数据。默认返回base64\n        :type ResultImage: str\n        :param ResultUrl: RspImgType 为 url 时，返回处理后的图片 url 数据。\n        :type ResultUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResultImage = None
        self.ResultUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultUrl = params.get("ResultUrl")
        self.RequestId = params.get("RequestId")