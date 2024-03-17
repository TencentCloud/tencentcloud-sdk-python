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


class Device(AbstractModel):
    """Device结果

    """

    def __init__(self):
        r"""
        :param _Ip: 发表消息设备IP
        :type Ip: str
        :param _Mac: Mac地址
        :type Mac: str
        :param _TokenId: 设备指纹Token
        :type TokenId: str
        :param _DeviceId: 设备指纹ID
        :type DeviceId: str
        :param _IMEI: 设备序列号
        :type IMEI: str
        :param _IDFA: IOS设备，Identifier For Advertising（广告标识符）
        :type IDFA: str
        :param _IDFV: IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）
        :type IDFV: str
        :param _IpType: IP地址类型 0 代表ipv4 1 代表ipv6
        :type IpType: int
        """
        self._Ip = None
        self._Mac = None
        self._TokenId = None
        self._DeviceId = None
        self._IMEI = None
        self._IDFA = None
        self._IDFV = None
        self._IpType = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Mac(self):
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac

    @property
    def TokenId(self):
        return self._TokenId

    @TokenId.setter
    def TokenId(self, TokenId):
        self._TokenId = TokenId

    @property
    def DeviceId(self):
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def IMEI(self):
        return self._IMEI

    @IMEI.setter
    def IMEI(self, IMEI):
        self._IMEI = IMEI

    @property
    def IDFA(self):
        return self._IDFA

    @IDFA.setter
    def IDFA(self, IDFA):
        self._IDFA = IDFA

    @property
    def IDFV(self):
        return self._IDFV

    @IDFV.setter
    def IDFV(self, IDFV):
        self._IDFV = IDFV

    @property
    def IpType(self):
        return self._IpType

    @IpType.setter
    def IpType(self, IpType):
        self._IpType = IpType


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Mac = params.get("Mac")
        self._TokenId = params.get("TokenId")
        self._DeviceId = params.get("DeviceId")
        self._IMEI = params.get("IMEI")
        self._IDFA = params.get("IDFA")
        self._IDFV = params.get("IDFV")
        self._IpType = params.get("IpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BizType: 该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略。 -- 该字段暂未开放。
        :type BizType: str
        :param _DataId: 数据ID，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type DataId: str
        :param _FileContent: 数据Base64编码，图片检测接口为图片文件内容，大小不能超过5M
        :type FileContent: str
        :param _FileUrl: 图片资源访问链接，__与FileContent参数必须二选一输入__ 。由于网络安全策略，送审带重定向的链接，可能引起下载失败，请尽量避免，比如Http返回302状态码的链接，可能导致接口返回ResourceUnavailable.ImageDownloadError
        :type FileUrl: str
        :param _Interval: 截帧频率，GIF图/长图检测专用，默认值为0，表示只会检测GIF图/长图的第一帧
        :type Interval: int
        :param _MaxFrames: GIF图/长图检测专用，代表均匀最大截帧数量，默认值为1（即只取GIF第一张，或长图不做切分处理（可能会造成处理超时））。
        :type MaxFrames: int
        :param _User: 账号相关信息字段，填入后可识别违规风险账号。
        :type User: :class:`tencentcloud.ims.v20200713.models.User`
        :param _Device: 设备相关信息字段，填入后可识别违规风险设备。
        :type Device: :class:`tencentcloud.ims.v20200713.models.Device`
        """
        self._BizType = None
        self._DataId = None
        self._FileContent = None
        self._FileUrl = None
        self._Interval = None
        self._MaxFrames = None
        self._User = None
        self._Device = None

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MaxFrames(self):
        return self._MaxFrames

    @MaxFrames.setter
    def MaxFrames(self, MaxFrames):
        self._MaxFrames = MaxFrames

    @property
    def User(self):
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Device(self):
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device


    def _deserialize(self, params):
        self._BizType = params.get("BizType")
        self._DataId = params.get("DataId")
        self._FileContent = params.get("FileContent")
        self._FileUrl = params.get("FileUrl")
        self._Interval = params.get("Interval")
        self._MaxFrames = params.get("MaxFrames")
        if params.get("User") is not None:
            self._User = User()
            self._User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self._Device = Device()
            self._Device._deserialize(params.get("Device"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HitFlag: 数据是否属于恶意类型。
0：正常，1：可疑；
        :type HitFlag: int
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义图片。
以及令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _SubLabel: 子标签名称，如色情--性行为；当未命中子标签时，返回空字符串；
        :type SubLabel: str
        :param _Score: 机器判断当前分类的置信度，取值范围：0.00~100.00。分数越高，表示越有可能属于当前分类。
（如：色情 99.99，则该样本属于色情的置信度非常高。）
        :type Score: int
        :param _LabelResults: 智能模型的识别结果，包括涉黄、广告等令人反感、不安全或不适宜的内容类型识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelResults: list of LabelResult
        :param _ObjectResults: 物体检测模型的审核结果，包括实体、广告台标/二维码等物体坐标信息与内容审核信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectResults: list of ObjectResult
        :param _OcrResults: OCR识别后的文本识别结果，包括文本所处图片的OCR坐标信息以及图片文本的识别结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrResults: list of OcrResult
        :param _LibResults: 基于图片风险库识别的结果。
风险库包括不安全黑库与正常白库的结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibResults: list of LibResult
        :param _DataId: 请求参数中的DataId。
        :type DataId: str
        :param _BizType: 您在入参时所填入的Biztype参数。 -- 该字段暂未开放。
        :type BizType: str
        :param _Extra: 扩展字段，用于特定信息返回，不同客户/Biztype下返回信息不同。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _RecognitionResults: 该字段用于返回仅识别图片元素的模型结果；包括：场景模型命中的标签、置信度和位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognitionResults: list of RecognitionResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HitFlag = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._LabelResults = None
        self._ObjectResults = None
        self._OcrResults = None
        self._LibResults = None
        self._DataId = None
        self._BizType = None
        self._Extra = None
        self._RecognitionResults = None
        self._RequestId = None

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def LabelResults(self):
        return self._LabelResults

    @LabelResults.setter
    def LabelResults(self, LabelResults):
        self._LabelResults = LabelResults

    @property
    def ObjectResults(self):
        return self._ObjectResults

    @ObjectResults.setter
    def ObjectResults(self, ObjectResults):
        self._ObjectResults = ObjectResults

    @property
    def OcrResults(self):
        return self._OcrResults

    @OcrResults.setter
    def OcrResults(self, OcrResults):
        self._OcrResults = OcrResults

    @property
    def LibResults(self):
        return self._LibResults

    @LibResults.setter
    def LibResults(self, LibResults):
        self._LibResults = LibResults

    @property
    def DataId(self):
        return self._DataId

    @DataId.setter
    def DataId(self, DataId):
        self._DataId = DataId

    @property
    def BizType(self):
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def RecognitionResults(self):
        return self._RecognitionResults

    @RecognitionResults.setter
    def RecognitionResults(self, RecognitionResults):
        self._RecognitionResults = RecognitionResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HitFlag = params.get("HitFlag")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("LabelResults") is not None:
            self._LabelResults = []
            for item in params.get("LabelResults"):
                obj = LabelResult()
                obj._deserialize(item)
                self._LabelResults.append(obj)
        if params.get("ObjectResults") is not None:
            self._ObjectResults = []
            for item in params.get("ObjectResults"):
                obj = ObjectResult()
                obj._deserialize(item)
                self._ObjectResults.append(obj)
        if params.get("OcrResults") is not None:
            self._OcrResults = []
            for item in params.get("OcrResults"):
                obj = OcrResult()
                obj._deserialize(item)
                self._OcrResults.append(obj)
        if params.get("LibResults") is not None:
            self._LibResults = []
            for item in params.get("LibResults"):
                obj = LibResult()
                obj._deserialize(item)
                self._LibResults.append(obj)
        self._DataId = params.get("DataId")
        self._BizType = params.get("BizType")
        self._Extra = params.get("Extra")
        if params.get("RecognitionResults") is not None:
            self._RecognitionResults = []
            for item in params.get("RecognitionResults"):
                obj = RecognitionResult()
                obj._deserialize(item)
                self._RecognitionResults.append(obj)
        self._RequestId = params.get("RequestId")


class LabelDetailItem(AbstractModel):
    """分类模型命中子标签结果

    """

    def __init__(self):
        r"""
        :param _Id: 序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 子标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Score: 子标签分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self._Id = None
        self._Name = None
        self._Score = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LabelResult(AbstractModel):
    """分类模型命中结果

    """

    def __init__(self):
        r"""
        :param _Scene: 场景识别结果
        :type Scene: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义图片。
以及令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _SubLabel: 子标签检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _Score: 该标签模型命中的分值
        :type Score: int
        :param _Details: 分类模型命中子标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of LabelDetailItem
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = LabelDetailItem()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibDetail(AbstractModel):
    """自定义库/黑白库明细

    """

    def __init__(self):
        r"""
        :param _Id: 序号
        :type Id: int
        :param _LibId: 仅当Label为Custom自定义关键词时有效，表示自定义库id
        :type LibId: str
        :param _LibName: 仅当Label为Custom自定义关键词时有效，表示自定义库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param _ImageId: 图片ID
        :type ImageId: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及其他令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _Tag: 自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param _Score: 命中的模型分值
        :type Score: int
        """
        self._Id = None
        self._LibId = None
        self._LibName = None
        self._ImageId = None
        self._Label = None
        self._Tag = None
        self._Score = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._ImageId = params.get("ImageId")
        self._Label = params.get("Label")
        self._Tag = params.get("Tag")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibResult(AbstractModel):
    """黑白库结果明细

    """

    def __init__(self):
        r"""
        :param _Scene: 场景识别结果
        :type Scene: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _SubLabel: 子标签检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _Score: 该标签模型命中的分值
        :type Score: int
        :param _Details: 黑白库结果明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of LibDetail
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = LibDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Location(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param _X: 左上角横坐标
        :type X: float
        :param _Y: 左上角纵坐标
        :type Y: float
        :param _Width: 宽度
        :type Width: float
        :param _Height: 高度
        :type Height: float
        :param _Rotate: 检测框的旋转角度
        :type Rotate: float
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None
        self._Rotate = None

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
    def Rotate(self):
        return self._Rotate

    @Rotate.setter
    def Rotate(self, Rotate):
        self._Rotate = Rotate


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Rotate = params.get("Rotate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectDetail(AbstractModel):
    """实体检测结果明细，当检测场景为实体、广告台标、二维码时表示模型检测目标框的标签名称、标签值、标签分数以及检测框的位置信息。

    """

    def __init__(self):
        r"""
        :param _Id: 序号
        :type Id: int
        :param _Name: 标签名称
        :type Name: str
        :param _Value: 标签值，
当标签为二维码时，表示URL地址，如Name为QrCode时，Value为"http//abc.com/aaa"
        :type Value: str
        :param _Score: 分数
        :type Score: int
        :param _Location: 检测框坐标
        :type Location: :class:`tencentcloud.ims.v20200713.models.Location`
        :param _SubLabel: 二级标签名称
        :type SubLabel: str
        :param _GroupId: 图库或人脸库id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _ObjectId: 图或人脸id
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectId: str
        """
        self._Id = None
        self._Name = None
        self._Value = None
        self._Score = None
        self._Location = None
        self._SubLabel = None
        self._GroupId = None
        self._ObjectId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ObjectId(self):
        return self._ObjectId

    @ObjectId.setter
    def ObjectId(self, ObjectId):
        self._ObjectId = ObjectId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        self._SubLabel = params.get("SubLabel")
        self._GroupId = params.get("GroupId")
        self._ObjectId = params.get("ObjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectResult(AbstractModel):
    """实体检测结果详情：实体、广告台标、二维码

    """

    def __init__(self):
        r"""
        :param _Scene: 场景识别结果
        :type Scene: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义图片。
以及令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _SubLabel: 子标签检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param _Score: 该标签模型命中的分值
        :type Score: int
        :param _Names: 实体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Names: list of str
        :param _Details: 实体检测结果明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of ObjectDetail
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Names = None
        self._Details = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        self._Names = params.get("Names")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ObjectDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrResult(AbstractModel):
    """OCR结果检测详情

    """

    def __init__(self):
        r"""
        :param _Scene: 场景识别结果
        :type Scene: str
        :param _Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _SubLabel: 子标签检测结果
        :type SubLabel: str
        :param _Score: 该标签模型命中的分值
        :type Score: int
        :param _Details: ocr结果详情
        :type Details: list of OcrTextDetail
        :param _Text: ocr识别出的文本结果
        :type Text: str
        :param _HitFlag: 是否命中结果，0 未命中 1命中
        :type HitFlag: int
        """
        self._Scene = None
        self._Suggestion = None
        self._Label = None
        self._SubLabel = None
        self._Score = None
        self._Details = None
        self._Text = None
        self._HitFlag = None

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Suggestion(self):
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def HitFlag(self):
        return self._HitFlag

    @HitFlag.setter
    def HitFlag(self, HitFlag):
        self._HitFlag = HitFlag


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._Suggestion = params.get("Suggestion")
        self._Label = params.get("Label")
        self._SubLabel = params.get("SubLabel")
        self._Score = params.get("Score")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = OcrTextDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._Text = params.get("Text")
        self._HitFlag = params.get("HitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrTextDetail(AbstractModel):
    """OCR文本结果详情

    """

    def __init__(self):
        r"""
        :param _Text: OCR文本内容
        :type Text: str
        :param _Label: 恶意标签，Normal：正常，Porn：色情，Abuse：谩骂，Ad：广告，Custom：自定义词库。
以及令人反感、不安全或不适宜的内容类型。
        :type Label: str
        :param _LibId: 仅当Label为Custom自定义关键词时有效，表示自定义库id
        :type LibId: str
        :param _LibName: 仅当Label为Custom自定义关键词时有效，表示自定义库名称
        :type LibName: str
        :param _Keywords: 该标签下命中的关键词
        :type Keywords: list of str
        :param _Score: 该标签模型命中的分值
        :type Score: int
        :param _Location: OCR位置
        :type Location: :class:`tencentcloud.ims.v20200713.models.Location`
        :param _Rate: OCR文本识别置信度
        :type Rate: int
        :param _SubLabel: OCR文本命中的二级标签
        :type SubLabel: str
        """
        self._Text = None
        self._Label = None
        self._LibId = None
        self._LibName = None
        self._Keywords = None
        self._Score = None
        self._Location = None
        self._Rate = None
        self._SubLabel = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def LibId(self):
        return self._LibId

    @LibId.setter
    def LibId(self, LibId):
        self._LibId = LibId

    @property
    def LibName(self):
        return self._LibName

    @LibName.setter
    def LibName(self, LibName):
        self._LibName = LibName

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def SubLabel(self):
        return self._SubLabel

    @SubLabel.setter
    def SubLabel(self, SubLabel):
        self._SubLabel = SubLabel


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Label = params.get("Label")
        self._LibId = params.get("LibId")
        self._LibName = params.get("LibName")
        self._Keywords = params.get("Keywords")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        self._Rate = params.get("Rate")
        self._SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionResult(AbstractModel):
    """识别类型标签结果信息

    """

    def __init__(self):
        r"""
        :param _Label: 当前可能的取值：Scene（图片场景模型）
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Tags: Label对应模型下的识别标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of RecognitionTag
        """
        self._Label = None
        self._Tags = None

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Label = params.get("Label")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = RecognitionTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionTag(AbstractModel):
    """识别类型标签信息

    """

    def __init__(self):
        r"""
        :param _Name: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Score: 置信分：0～100，数值越大表示置信度越高
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param _Location: 标签位置信息，若模型无位置信息，则可能为零值
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: :class:`tencentcloud.ims.v20200713.models.Location`
        """
        self._Name = None
        self._Score = None
        self._Location = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        if params.get("Location") is not None:
            self._Location = Location()
            self._Location._deserialize(params.get("Location"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """User结果

    """

    def __init__(self):
        r"""
        :param _UserId: 业务用户ID 如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param _AccountType: 业务用户ID类型 "1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :type AccountType: str
        :param _Nickname: 用户昵称
        :type Nickname: str
        :param _Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param _Age: 年龄 默认0 未知
        :type Age: int
        :param _Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param _Phone: 手机号
        :type Phone: str
        :param _Desc: 用户简介，长度不超过5000字
        :type Desc: str
        :param _HeadUrl: 用户头像图片链接
        :type HeadUrl: str
        """
        self._UserId = None
        self._AccountType = None
        self._Nickname = None
        self._Gender = None
        self._Age = None
        self._Level = None
        self._Phone = None
        self._Desc = None
        self._HeadUrl = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

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
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def HeadUrl(self):
        return self._HeadUrl

    @HeadUrl.setter
    def HeadUrl(self, HeadUrl):
        self._HeadUrl = HeadUrl


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._AccountType = params.get("AccountType")
        self._Nickname = params.get("Nickname")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._Level = params.get("Level")
        self._Phone = params.get("Phone")
        self._Desc = params.get("Desc")
        self._HeadUrl = params.get("HeadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        