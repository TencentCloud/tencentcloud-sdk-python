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


class Device(AbstractModel):
    """Device结果

    """

    def __init__(self):
        """
        :param Ip: 发表消息设备IP
        :type Ip: str
        :param Mac: Mac地址
        :type Mac: str
        :param TokenId: 设备指纹Token
        :type TokenId: str
        :param DeviceId: 设备指纹ID
        :type DeviceId: str
        :param IMEI: 设备序列号
        :type IMEI: str
        :param IDFA: IOS设备，Identifier For Advertising（广告标识符）
        :type IDFA: str
        :param IDFV: IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）
        :type IDFV: str
        :param IpType: IP地址类型 0 代表ipv4 1 代表ipv6
        :type IpType: int
        """
        self.Ip = None
        self.Mac = None
        self.TokenId = None
        self.DeviceId = None
        self.IMEI = None
        self.IDFA = None
        self.IDFV = None
        self.IpType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Mac = params.get("Mac")
        self.TokenId = params.get("TokenId")
        self.DeviceId = params.get("DeviceId")
        self.IMEI = params.get("IMEI")
        self.IDFA = params.get("IDFA")
        self.IDFV = params.get("IDFV")
        self.IpType = params.get("IpType")


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        """
        :param BizType: 该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略。 -- 该字段暂未开放。
        :type BizType: str
        :param DataId: 数据ID，可以由英文字母、数字、下划线、-、@#组成，不超过64个字符
        :type DataId: str
        :param FileContent: 数据Base64编码，图片检测接口为图片文件内容，大小不能超过5M
        :type FileContent: str
        :param FileUrl: 图片资源访问链接，__与FileContent参数必须二选一输入__
        :type FileUrl: str
        :param Interval: 截帧频率，GIF图/长图检测专用，默认值为0，表示只会检测GIF图/长图的第一帧
        :type Interval: int
        :param MaxFrames: GIF图/长图检测专用，代表均匀最大截帧数量，默认值为1（即只取GIF第一张，或长图不做切分处理（可能会造成处理超时））。
        :type MaxFrames: int
        :param User: 账号相关信息字段，填入后可识别违规风险账号。
        :type User: :class:`tencentcloud.ims.v20200713.models.User`
        :param Device: 设备相关信息字段，填入后可识别违规风险设备。
        :type Device: :class:`tencentcloud.ims.v20200713.models.Device`
        """
        self.BizType = None
        self.DataId = None
        self.FileContent = None
        self.FileUrl = None
        self.Interval = None
        self.MaxFrames = None
        self.User = None
        self.Device = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        self.Interval = params.get("Interval")
        self.MaxFrames = params.get("MaxFrames")
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        """
        :param HitFlag: 数据是否属于恶意类型。
0：正常，1：可疑；
        :type HitFlag: int
        :param Suggestion: 建议您拿到判断结果后的执行操作。
建议值，Block：建议屏蔽，Review：建议复审，Pass：建议通过
        :type Suggestion: str
        :param Label: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义图片。
        :type Label: str
        :param SubLabel: 子标签名称，如色情--性行为；当未命中子标签时，返回空字符串；
        :type SubLabel: str
        :param Score: 机器判断当前分类的置信度，取值范围：0.00~100.00。分数越高，表示越有可能属于当前分类。
（如：色情 99.99，则该样本属于色情的置信度非常高。）
        :type Score: int
        :param LabelResults: 识别模型的审核结果，包括涉黄、性感、涉暴、违法违规、等审核结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelResults: list of LabelResult
        :param ObjectResults: 物体检测模型的审核结果，包括涉政实体、广告台标/二维码等物体坐标信息与内容审核信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectResults: list of ObjectResult
        :param OcrResults: OCR识别后的文本审核结果，包括文本所处图片的OCR坐标信息以及图片文本的审核结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrResults: list of OcrResult
        :param LibResults: 基于图片风险库识别的结果。
风险库包括违规黑库与正常白库的结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibResults: list of LibResult
        :param DataId: 请求参数中的DataId。
        :type DataId: str
        :param BizType: 您在入参时所填入的Biztype参数。 -- 该字段暂未开放。
        :type BizType: str
        :param Extra: 扩展字段，用于特定信息返回，不同客户/Biztype下返回信息不同。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HitFlag = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.LabelResults = None
        self.ObjectResults = None
        self.OcrResults = None
        self.LibResults = None
        self.DataId = None
        self.BizType = None
        self.Extra = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HitFlag = params.get("HitFlag")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("LabelResults") is not None:
            self.LabelResults = []
            for item in params.get("LabelResults"):
                obj = LabelResult()
                obj._deserialize(item)
                self.LabelResults.append(obj)
        if params.get("ObjectResults") is not None:
            self.ObjectResults = []
            for item in params.get("ObjectResults"):
                obj = ObjectResult()
                obj._deserialize(item)
                self.ObjectResults.append(obj)
        if params.get("OcrResults") is not None:
            self.OcrResults = []
            for item in params.get("OcrResults"):
                obj = OcrResult()
                obj._deserialize(item)
                self.OcrResults.append(obj)
        if params.get("LibResults") is not None:
            self.LibResults = []
            for item in params.get("LibResults"):
                obj = LibResult()
                obj._deserialize(item)
                self.LibResults.append(obj)
        self.DataId = params.get("DataId")
        self.BizType = params.get("BizType")
        self.Extra = params.get("Extra")
        self.RequestId = params.get("RequestId")


class LabelDetailItem(AbstractModel):
    """分类模型命中子标签结果

    """

    def __init__(self):
        """
        :param Id: 序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Name: 子标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Score: 子标签分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self.Id = None
        self.Name = None
        self.Score = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Score = params.get("Score")


class LabelResult(AbstractModel):
    """分类模型命中结果

    """

    def __init__(self):
        """
        :param Scene: 场景识别结果
        :type Scene: str
        :param Suggestion: 建议值，Block：打击，Review：待复审，Pass：正常
        :type Suggestion: str
        :param Label: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义图片
        :type Label: str
        :param SubLabel: 子标签检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param Score: 该标签模型命中的分值
        :type Score: int
        :param Details: 分类模型命中子标签结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of LabelDetailItem
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = LabelDetailItem()
                obj._deserialize(item)
                self.Details.append(obj)


class LibDetail(AbstractModel):
    """自定义库/黑白库明细

    """

    def __init__(self):
        """
        :param Id: 序号
        :type Id: int
        :param LibId: 仅当Lable为Custom自定义关键词时有效，表示自定义库id
        :type LibId: str
        :param LibName: 仅当Lable为Custom自定义关键词时有效，表示自定义库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param ImageId: 图片ID
        :type ImageId: str
        :param Label: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义图片
        :type Label: str
        :param Tag: 自定义标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param Score: 命中的模型分值
        :type Score: int
        """
        self.Id = None
        self.LibId = None
        self.LibName = None
        self.ImageId = None
        self.Label = None
        self.Tag = None
        self.Score = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.ImageId = params.get("ImageId")
        self.Label = params.get("Label")
        self.Tag = params.get("Tag")
        self.Score = params.get("Score")


class LibResult(AbstractModel):
    """黑白库结果明细

    """

    def __init__(self):
        """
        :param Scene: 场景识别结果
        :type Scene: str
        :param Suggestion: 建议值，Block：打击，Review：待复审，Pass：正常
        :type Suggestion: str
        :param Label: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义图片
        :type Label: str
        :param SubLabel: 子标签检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param Score: 该标签模型命中的分值
        :type Score: int
        :param Details: 黑白库结果明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of LibDetail
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = LibDetail()
                obj._deserialize(item)
                self.Details.append(obj)


class Location(AbstractModel):
    """坐标

    """

    def __init__(self):
        """
        :param X: 左上角横坐标
        :type X: float
        :param Y: 左上角纵坐标
        :type Y: float
        :param Width: 宽度
        :type Width: float
        :param Height: 高度
        :type Height: float
        :param Rotate: 检测框的旋转角度
        :type Rotate: float
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.Rotate = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Rotate = params.get("Rotate")


class ObjectDetail(AbstractModel):
    """实体检测结果明细，当检测场景为政治实体、广告台标、二维码和人脸属性时表示模型检测目标框的标签名称、标签值、标签分数以及检测框的位置信息。

    """

    def __init__(self):
        """
        :param Id: 序号
        :type Id: int
        :param Name: 标签名称
        :type Name: str
        :param Value: 标签值，
当标签为二维码时，表示URL地址，如Name为QrCode时，Value为"http//abc.com/aaa"
当标签为人脸属性，表示属性值，如Name为Age时 Value为18
        :type Value: str
        :param Score: 分数
        :type Score: int
        :param Location: 检测框坐标
        :type Location: :class:`tencentcloud.ims.v20200713.models.Location`
        """
        self.Id = None
        self.Name = None
        self.Value = None
        self.Score = None
        self.Location = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Score = params.get("Score")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))


class ObjectResult(AbstractModel):
    """实体检测结果详情：政治实体、广告台标、二维码

    """

    def __init__(self):
        """
        :param Scene: 场景识别结果
        :type Scene: str
        :param Suggestion: 建议值，Block：打击，Review：待复审，Pass：正常
        :type Suggestion: str
        :param Label: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义图片
        :type Label: str
        :param SubLabel: 子标签检测结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param Score: 该标签模型命中的分值
        :type Score: int
        :param Names: 实体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Names: list of str
        :param Details: 实体检测结果明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of ObjectDetail
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Names = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        self.Names = params.get("Names")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ObjectDetail()
                obj._deserialize(item)
                self.Details.append(obj)


class OcrResult(AbstractModel):
    """OCR结果检测详情

    """

    def __init__(self):
        """
        :param Scene: 场景识别结果
        :type Scene: str
        :param Suggestion: 建议值，Block：打击，Review：待复审，Pass：正常
        :type Suggestion: str
        :param Label: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告
        :type Label: str
        :param SubLabel: 子标签检测结果
        :type SubLabel: str
        :param Score: 该标签模型命中的分值
        :type Score: int
        :param Details: ocr结果详情
        :type Details: list of OcrTextDetail
        """
        self.Scene = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = OcrTextDetail()
                obj._deserialize(item)
                self.Details.append(obj)


class OcrTextDetail(AbstractModel):
    """OCR文本结果详情

    """

    def __init__(self):
        """
        :param Text: OCR文本内容
        :type Text: str
        :param Label: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义关键词
        :type Label: str
        :param LibId: 仅当Lable为Custom自定义关键词时有效，表示自定义库id
        :type LibId: str
        :param LibName: 仅当Lable为Custom自定义关键词时有效，表示自定义库名称
        :type LibName: str
        :param Keywords: 该标签下命中的关键词
        :type Keywords: list of str
        :param Score: 该标签模型命中的分值
        :type Score: int
        :param Location: OCR位置
        :type Location: :class:`tencentcloud.ims.v20200713.models.Location`
        """
        self.Text = None
        self.Label = None
        self.LibId = None
        self.LibName = None
        self.Keywords = None
        self.Score = None
        self.Location = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Label = params.get("Label")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))


class User(AbstractModel):
    """User结果

    """

    def __init__(self):
        """
        :param UserId: 业务用户ID 如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。
        :type UserId: str
        :param AccountType: 业务用户ID类型 "1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"
        :type AccountType: str
        :param Nickname: 用户昵称
        :type Nickname: str
        :param Gender: 性别 默认0 未知 1 男性 2 女性
        :type Gender: int
        :param Age: 年龄 默认0 未知
        :type Age: int
        :param Level: 用户等级，默认0 未知 1 低 2 中 3 高
        :type Level: int
        :param Phone: 手机号
        :type Phone: str
        :param Desc: 用户简介，长度不超过5000字
        :type Desc: str
        :param HeadUrl: 用户头像图片链接
        :type HeadUrl: str
        """
        self.UserId = None
        self.AccountType = None
        self.Nickname = None
        self.Gender = None
        self.Age = None
        self.Level = None
        self.Phone = None
        self.Desc = None
        self.HeadUrl = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.AccountType = params.get("AccountType")
        self.Nickname = params.get("Nickname")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.Level = params.get("Level")
        self.Phone = params.get("Phone")
        self.Desc = params.get("Desc")
        self.HeadUrl = params.get("HeadUrl")