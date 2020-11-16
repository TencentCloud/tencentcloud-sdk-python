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


class BankCard2EVerificationRequest(AbstractModel):
    """BankCard2EVerification请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 姓名
        :type Name: str
        :param BankCard: 银行卡
        :type BankCard: str
        """
        self.Name = None
        self.BankCard = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")


class BankCard2EVerificationResponse(AbstractModel):
    """BankCard2EVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码
计费结果码：
  '0': '认证通过'
  '-1': '认证未通过'
 '-4': '持卡人信息有误'
  '-5': '未开通无卡支付'
  '-6': '此卡被没收'
  '-7': '无效卡号'
  '-8': '此卡无对应发卡行'
  '-9': '该卡未初始化或睡眠卡'
  '-10': '作弊卡、吞卡'
  '-11': '此卡已挂失'
  '-12': '该卡已过期'
  '-13': '受限制的卡'
  '-14': '密码错误次数超限'
  '-15': '发卡行不支持此交易'
不计费结果码：
  '-2': '姓名校验不通过'
  '-3': '银行卡号码有误'
  '-16': '验证中心服务繁忙'
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class BankCard4EVerificationRequest(AbstractModel):
    """BankCard4EVerification请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 姓名
        :type Name: str
        :param BankCard: 银行卡
        :type BankCard: str
        :param Phone: 手机号码
        :type Phone: str
        :param IdCard: 开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。
        :type IdCard: str
        :param CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。
目前默认为0：身份证，其他证件类型暂不支持。
        :type CertType: int
        """
        self.Name = None
        self.BankCard = None
        self.Phone = None
        self.IdCard = None
        self.CertType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")
        self.Phone = params.get("Phone")
        self.IdCard = params.get("IdCard")
        self.CertType = params.get("CertType")


class BankCard4EVerificationResponse(AbstractModel):
    """BankCard4EVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码
收费结果码：
'0': '认证通过'
'-1': '认证未通过'
'-6': '持卡人信息有误'
'-7': '未开通无卡支付'
'-8': '此卡被没收'
'-9': '无效卡号'
'-10': '此卡无对应发卡行'
'-11': '该卡未初始化或睡眠卡'
'-12': '作弊卡、吞卡'
'-13': '此卡已挂失'
'-14': '该卡已过期'
'-15': '受限制的卡'
'-16': '密码错误次数超限'
'-17': '发卡行不支持此交易'
不收费结果码：
'-2': '姓名校验不通过'
'-3': '身份证号码有误'
'-4': '银行卡号码有误'
'-5': '手机号码不合法'
'-18': '验证中心服务繁忙'
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class BankCardVerificationRequest(AbstractModel):
    """BankCardVerification请求参数结构体

    """

    def __init__(self):
        """
        :param IdCard: 开户证件号，与CertType参数的证件类型一致，如：身份证，则传入身份证号。
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param BankCard: 银行卡
        :type BankCard: str
        :param CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。
目前默认：0 身份证，其他证件类型需求可以联系小助手faceid001确认。
        :type CertType: int
        """
        self.IdCard = None
        self.Name = None
        self.BankCard = None
        self.CertType = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")
        self.CertType = params.get("CertType")


class BankCardVerificationResponse(AbstractModel):
    """BankCardVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码
收费结果码：
'0': '认证通过'
'-1': '认证未通过'
'-5': '持卡人信息有误'
'-6': '未开通无卡支付'
'-7': '此卡被没收'
'-8': '无效卡号'
'-9': '此卡无对应发卡行'
'-10': '该卡未初始化或睡眠卡'
'-11': '作弊卡、吞卡'
'-12': '此卡已挂失'
'-13': '该卡已过期'
'-14': '受限制的卡'
'-15': '密码错误次数超限'
'-16': '发卡行不支持此交易'
不收费结果码：
'-2': '姓名校验不通过'
'-3': '身份证号码有误'
'-4': '银行卡号码有误'
'-17': '验证中心服务繁忙'
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class CheckBankCardInformationRequest(AbstractModel):
    """CheckBankCardInformation请求参数结构体

    """

    def __init__(self):
        """
        :param BankCard: 银行卡号。
        :type BankCard: str
        """
        self.BankCard = None


    def _deserialize(self, params):
        self.BankCard = params.get("BankCard")


class CheckBankCardInformationResponse(AbstractModel):
    """CheckBankCardInformation返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 查询成功
-1: 未查到信息
不收费结果码
-2：验证中心服务繁忙
-3：银行卡不存在
        :type Result: str
        :param Description: 业务结果描述
        :type Description: str
        :param AccountBank: 开户行
        :type AccountBank: str
        :param AccountType: 卡性质：1. 借记卡；2. 贷记卡
        :type AccountType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.AccountBank = None
        self.AccountType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.AccountBank = params.get("AccountBank")
        self.AccountType = params.get("AccountType")
        self.RequestId = params.get("RequestId")


class CheckIdCardInformationRequest(AbstractModel):
    """CheckIdCardInformation请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 身份证人像面的 Base64 值
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 7M。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
ImageBase64、ImageUrl二者必须提供其中之一。若都提供了，则按照ImageUrl>ImageBase64的优先级使用参数。
        :type ImageBase64: str
        :param ImageUrl: 身份证人像面的 Url 地址
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        :param Config: 以下可选字段均为bool 类型，默认false：
CopyWarn，复印件告警
BorderCheckWarn，边框和框内遮挡告警
ReshootWarn，翻拍告警
DetectPsWarn，PS检测告警
TempIdWarn，临时身份证告警
Quality，图片质量告警（评价图片模糊程度）

SDK 设置方式参考：
Config = Json.stringify({"CopyWarn":true,"ReshootWarn":true})
API 3.0 Explorer 设置方式参考：
Config = {"CopyWarn":true,"ReshootWarn":true}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")


class CheckIdCardInformationResponse(AbstractModel):
    """CheckIdCardInformation返回参数结构体

    """

    def __init__(self):
        """
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param Name: 姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param Nation: 民族
        :type Nation: str
        :param Birth: 出生日期
        :type Birth: str
        :param Address: 地址
        :type Address: str
        :param IdNum: 身份证号
        :type IdNum: str
        :param Portrait: 身份证头像照片的base64编码，如果抠图失败会拿整张身份证做比对并返回空。
        :type Portrait: str
        :param Warnings: 告警信息，当在Config中配置了告警信息会停止人像比对，Result返回错误（FailedOperation.OcrWarningOccurred）并有此告警信息，Code 告警码列表和释义：

-9101 身份证边框不完整告警，
-9102 身份证复印件告警，
-9103 身份证翻拍告警，
-9105 身份证框内遮挡告警，
-9104 临时身份证告警，
-9106 身份证 PS 告警。
-8001 图片模糊告警
多个会 |  隔开如 "-9101|-9106|-9104"
        :type Warnings: str
        :param Quality: 图片质量分数，当请求Config中配置图片模糊告警该参数才有意义，取值范围（0～100），目前默认阈值是50分，低于50分会触发模糊告警。
        :type Quality: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Sim = None
        self.Result = None
        self.Description = None
        self.Name = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.IdNum = None
        self.Portrait = None
        self.Warnings = None
        self.Quality = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdNum = params.get("IdNum")
        self.Portrait = params.get("Portrait")
        self.Warnings = params.get("Warnings")
        self.Quality = params.get("Quality")
        self.RequestId = params.get("RequestId")


class DetectAuthRequest(AbstractModel):
    """DetectAuth请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请加慧眼小助手微信（faceid001）进行咨询。
        :type RuleId: str
        :param TerminalType: 本接口不需要传递此参数。
        :type TerminalType: str
        :param IdCard: 身份标识（未使用OCR服务时，必须传入）。
规则：a-zA-Z0-9组合。最长长度32位。
        :type IdCard: str
        :param Name: 姓名。（未使用OCR服务时，必须传入）最长长度32位。中文请使用UTF-8编码。
        :type Name: str
        :param RedirectUrl: 认证结束后重定向的回调链接地址。最长长度1024位。
        :type RedirectUrl: str
        :param Extra: 透传字段，在获取验证结果时返回。
        :type Extra: str
        :param ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        """
        self.RuleId = None
        self.TerminalType = None
        self.IdCard = None
        self.Name = None
        self.RedirectUrl = None
        self.Extra = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.TerminalType = params.get("TerminalType")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.RedirectUrl = params.get("RedirectUrl")
        self.Extra = params.get("Extra")
        self.ImageBase64 = params.get("ImageBase64")


class DetectAuthResponse(AbstractModel):
    """DetectAuth返回参数结构体

    """

    def __init__(self):
        """
        :param Url: 用于发起核身流程的URL，仅微信H5场景使用。
        :type Url: str
        :param BizToken: 一次核身流程的标识，有效时间为7,200秒；
完成核身后，可用该标识获取验证结果信息。
        :type BizToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.BizToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.BizToken = params.get("BizToken")
        self.RequestId = params.get("RequestId")


class DetectDetail(AbstractModel):
    """活体一比一详情

    """

    def __init__(self):
        """
        :param ReqTime: 请求时间戳。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReqTime: str
        :param Seq: 本次活体一比一请求的唯一标记。
注意：此字段可能返回 null，表示取不到有效值。
        :type Seq: str
        :param Idcard: 参与本次活体一比一的身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type Idcard: str
        :param Name: 参与本次活体一比一的姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Sim: 本次活体一比一的相似度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sim: str
        :param IsNeedCharge: 本次活体一比一是否收费
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNeedCharge: bool
        :param Errcode: 本次活体一比一最终结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Errcode: int
        :param Errmsg: 本次活体一比一最终结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Errmsg: str
        :param Livestatus: 本次活体结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Livestatus: int
        :param Livemsg: 本次活体结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Livemsg: str
        :param Comparestatus: 本次一比一结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param Comparemsg: 本次一比一结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        """
        self.ReqTime = None
        self.Seq = None
        self.Idcard = None
        self.Name = None
        self.Sim = None
        self.IsNeedCharge = None
        self.Errcode = None
        self.Errmsg = None
        self.Livestatus = None
        self.Livemsg = None
        self.Comparestatus = None
        self.Comparemsg = None


    def _deserialize(self, params):
        self.ReqTime = params.get("ReqTime")
        self.Seq = params.get("Seq")
        self.Idcard = params.get("Idcard")
        self.Name = params.get("Name")
        self.Sim = params.get("Sim")
        self.IsNeedCharge = params.get("IsNeedCharge")
        self.Errcode = params.get("Errcode")
        self.Errmsg = params.get("Errmsg")
        self.Livestatus = params.get("Livestatus")
        self.Livemsg = params.get("Livemsg")
        self.Comparestatus = params.get("Comparestatus")
        self.Comparemsg = params.get("Comparemsg")


class DetectInfoBestFrame(AbstractModel):
    """核身最佳帧信息

    """

    def __init__(self):
        """
        :param BestFrame: 活体比对最佳帧。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: str
        :param BestFrames: 自截帧。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrames: list of str
        """
        self.BestFrame = None
        self.BestFrames = None


    def _deserialize(self, params):
        self.BestFrame = params.get("BestFrame")
        self.BestFrames = params.get("BestFrames")


class DetectInfoIdCardData(AbstractModel):
    """核身身份证图片信息

    """

    def __init__(self):
        """
        :param OcrFront: OCR正面照片的base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrFront: str
        :param OcrBack: OCR反面照片的base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrBack: str
        :param ProcessedFrontImage: 旋转裁边后的正面照片base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedFrontImage: str
        :param ProcessedBackImage: 旋转裁边后的背面照片base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessedBackImage: str
        :param Avatar: 身份证正面人像图base64编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        """
        self.OcrFront = None
        self.OcrBack = None
        self.ProcessedFrontImage = None
        self.ProcessedBackImage = None
        self.Avatar = None


    def _deserialize(self, params):
        self.OcrFront = params.get("OcrFront")
        self.OcrBack = params.get("OcrBack")
        self.ProcessedFrontImage = params.get("ProcessedFrontImage")
        self.ProcessedBackImage = params.get("ProcessedBackImage")
        self.Avatar = params.get("Avatar")


class DetectInfoText(AbstractModel):
    """核身文本信息

    """

    def __init__(self):
        """
        :param ErrCode: 本次流程最终验证结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param ErrMsg: 本次流程最终验证结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param IdCard: 本次验证使用的身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param Name: 本次验证使用的姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param OcrNation: Ocr识别结果。民族。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrNation: str
        :param OcrAddress: Ocr识别结果。家庭住址。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrAddress: str
        :param OcrBirth: Ocr识别结果。生日。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrBirth: str
        :param OcrAuthority: Ocr识别结果。签发机关。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrAuthority: str
        :param OcrValidDate: Ocr识别结果。有效日期。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrValidDate: str
        :param OcrName: Ocr识别结果。姓名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrName: str
        :param OcrIdCard: Ocr识别结果。身份证号。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrIdCard: str
        :param OcrGender: Ocr识别结果。性别。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcrGender: str
        :param LiveStatus: 本次流程最终活体结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveStatus: int
        :param LiveMsg: 本次流程最终活体结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveMsg: str
        :param Comparestatus: 本次流程最终一比一结果。0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param Comparemsg: 本次流程最终一比一结果描述。（仅描述用，文案更新时不会通知。）
注意：此字段可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        :param Sim: 本次流程活体一比一的分数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Sim: str
        :param Location: 地理位置经纬度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: str
        :param Extra: Auth接口带入额外信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param LivenessDetail: 本次流程进行的活体一比一流水。
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessDetail: list of DetectDetail
        :param Mobile: 手机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
        self.ErrCode = None
        self.ErrMsg = None
        self.IdCard = None
        self.Name = None
        self.OcrNation = None
        self.OcrAddress = None
        self.OcrBirth = None
        self.OcrAuthority = None
        self.OcrValidDate = None
        self.OcrName = None
        self.OcrIdCard = None
        self.OcrGender = None
        self.LiveStatus = None
        self.LiveMsg = None
        self.Comparestatus = None
        self.Comparemsg = None
        self.Sim = None
        self.Location = None
        self.Extra = None
        self.LivenessDetail = None
        self.Mobile = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.OcrNation = params.get("OcrNation")
        self.OcrAddress = params.get("OcrAddress")
        self.OcrBirth = params.get("OcrBirth")
        self.OcrAuthority = params.get("OcrAuthority")
        self.OcrValidDate = params.get("OcrValidDate")
        self.OcrName = params.get("OcrName")
        self.OcrIdCard = params.get("OcrIdCard")
        self.OcrGender = params.get("OcrGender")
        self.LiveStatus = params.get("LiveStatus")
        self.LiveMsg = params.get("LiveMsg")
        self.Comparestatus = params.get("Comparestatus")
        self.Comparemsg = params.get("Comparemsg")
        self.Sim = params.get("Sim")
        self.Location = params.get("Location")
        self.Extra = params.get("Extra")
        if params.get("LivenessDetail") is not None:
            self.LivenessDetail = []
            for item in params.get("LivenessDetail"):
                obj = DetectDetail()
                obj._deserialize(item)
                self.LivenessDetail.append(obj)
        self.Mobile = params.get("Mobile")


class DetectInfoVideoData(AbstractModel):
    """核身视频信息

    """

    def __init__(self):
        """
        :param LivenessVideo: 活体视频的base64编码
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessVideo: str
        """
        self.LivenessVideo = None


    def _deserialize(self, params):
        self.LivenessVideo = params.get("LivenessVideo")


class GetActionSequenceRequest(AbstractModel):
    """GetActionSequence请求参数结构体

    """

    def __init__(self):
        """
        :param ActionType: 默认不需要使用
        :type ActionType: str
        """
        self.ActionType = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")


class GetActionSequenceResponse(AbstractModel):
    """GetActionSequence返回参数结构体

    """

    def __init__(self):
        """
        :param ActionSequence: 动作顺序(2,1 or 1,2) 。1代表张嘴，2代表闭眼。
        :type ActionSequence: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ActionSequence = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActionSequence = params.get("ActionSequence")
        self.RequestId = params.get("RequestId")


class GetDetectInfoEnhancedRequest(AbstractModel):
    """GetDetectInfoEnhanced请求参数结构体

    """

    def __init__(self):
        """
        :param BizToken: 人脸核身流程的标识，调用DetectAuth接口时生成。
        :type BizToken: str
        :param RuleId: 用于细分客户使用场景，由腾讯侧在线下对接时分配。
        :type RuleId: str
        :param InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证信息；3：视频最佳截图信息；4：视频信息）。
如 134表示拉取文本类、视频最佳截图信息、视频信息。
默认值：0
        :type InfoType: str
        :param BestFramesCount: 从活体视频中截取一定张数的最佳帧。默认为0，最大为10，超出10的最多只给10张。（InfoType需要包含3）
        :type BestFramesCount: int
        :param IsCutIdCardImage: 是否对身份证照片进行裁边。默认为false。（InfoType需要包含2）
        :type IsCutIdCardImage: bool
        :param IsNeedIdCardAvatar: 是否需要从身份证中抠出头像。默认为false。（InfoType需要包含2）
        :type IsNeedIdCardAvatar: bool
        """
        self.BizToken = None
        self.RuleId = None
        self.InfoType = None
        self.BestFramesCount = None
        self.IsCutIdCardImage = None
        self.IsNeedIdCardAvatar = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        self.RuleId = params.get("RuleId")
        self.InfoType = params.get("InfoType")
        self.BestFramesCount = params.get("BestFramesCount")
        self.IsCutIdCardImage = params.get("IsCutIdCardImage")
        self.IsNeedIdCardAvatar = params.get("IsNeedIdCardAvatar")


class GetDetectInfoEnhancedResponse(AbstractModel):
    """GetDetectInfoEnhanced返回参数结构体

    """

    def __init__(self):
        """
        :param Text: 文本类信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: :class:`tencentcloud.faceid.v20180301.models.DetectInfoText`
        :param IdCardData: 身份证照片信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoIdCardData`
        :param BestFrame: 最佳帧信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrame: :class:`tencentcloud.faceid.v20180301.models.DetectInfoBestFrame`
        :param VideoData: 视频信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoData: :class:`tencentcloud.faceid.v20180301.models.DetectInfoVideoData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Text = None
        self.IdCardData = None
        self.BestFrame = None
        self.VideoData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self.Text = DetectInfoText()
            self.Text._deserialize(params.get("Text"))
        if params.get("IdCardData") is not None:
            self.IdCardData = DetectInfoIdCardData()
            self.IdCardData._deserialize(params.get("IdCardData"))
        if params.get("BestFrame") is not None:
            self.BestFrame = DetectInfoBestFrame()
            self.BestFrame._deserialize(params.get("BestFrame"))
        if params.get("VideoData") is not None:
            self.VideoData = DetectInfoVideoData()
            self.VideoData._deserialize(params.get("VideoData"))
        self.RequestId = params.get("RequestId")


class GetDetectInfoRequest(AbstractModel):
    """GetDetectInfo请求参数结构体

    """

    def __init__(self):
        """
        :param BizToken: 人脸核身流程的标识，调用DetectAuth接口时生成。
        :type BizToken: str
        :param RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请加慧眼小助手微信（faceid001）进行咨询。
        :type RuleId: str
        :param InfoType: 指定拉取的结果信息，取值（0：全部；1：文本类；2：身份证正反面；3：视频最佳截图照片；4：视频）。
如 134表示拉取文本类、视频最佳截图照片、视频。
默认值：0
        :type InfoType: str
        """
        self.BizToken = None
        self.RuleId = None
        self.InfoType = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        self.RuleId = params.get("RuleId")
        self.InfoType = params.get("InfoType")


class GetDetectInfoResponse(AbstractModel):
    """GetDetectInfo返回参数结构体

    """

    def __init__(self):
        """
        :param DetectInfo: JSON字符串。
{
  // 文本类信息
  "Text": {
    "ErrCode": null,      // 本次核身最终结果。0为成功
    "ErrMsg": null,       // 本次核身最终结果信息描述。
    "IdCard": "",         // 本次核身最终获得的身份证号。
    "Name": "",           // 本次核身最终获得的姓名。
    "OcrNation": null,    // ocr阶段获取的民族
    "OcrAddress": null,   // ocr阶段获取的地址
    "OcrBirth": null,     // ocr阶段获取的出生信息
    "OcrAuthority": null, // ocr阶段获取的证件签发机关
    "OcrValidDate": null, // ocr阶段获取的证件有效期
    "OcrName": null,      // ocr阶段获取的姓名
    "OcrIdCard": null,    // ocr阶段获取的身份证号
    "OcrGender": null,    // ocr阶段获取的性别
    "LiveStatus": null,   // 活体检测阶段的错误码。0为成功
    "LiveMsg": null,      // 活体检测阶段的错误信息
    "Comparestatus": null,// 一比一阶段的错误码。0为成功
    "Comparemsg": null,   // 一比一阶段的错误信息
    "Sim": null, // 比对相似度
    "Location": null, // 地理位置信息
    "Extra": "",          // DetectAuth结果传进来的Extra信息
    "Detail": {           // 活体一比一信息详情
      "LivenessData": [
            {
              ErrCode: null, // 活体比对验证错误码
              ErrMsg: null, // 活体比对验证错误描述
              ReqTime: null, // 活体验证时间戳
              IdCard: null, // 验证身份证号
              Name: null // 验证姓名
            }
      ]
    }
  },
  // 身份证正反面照片Base64
  "IdCardData": {
    "OcrFront": null,
    "OcrBack": null
  },
  // 视频最佳帧截图Base64
  "BestFrame": {
    "BestFrame": null
  },
  // 活体视频Base64
  "VideoData": {
    "LivenessVideo": null
  }
}
        :type DetectInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DetectInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DetectInfo = params.get("DetectInfo")
        self.RequestId = params.get("RequestId")


class GetFaceIdResultRequest(AbstractModel):
    """GetFaceIdResult请求参数结构体

    """

    def __init__(self):
        """
        :param FaceIdToken: SDK人脸核身流程的标识，调用GetFaceIdToken接口时生成。
        :type FaceIdToken: str
        :param IsNeedVideo: 是否需要拉取视频，默认false不需要
        :type IsNeedVideo: bool
        :param IsNeedBestFrame: 是否需要拉取截帧，默认false不需要
        :type IsNeedBestFrame: bool
        """
        self.FaceIdToken = None
        self.IsNeedVideo = None
        self.IsNeedBestFrame = None


    def _deserialize(self, params):
        self.FaceIdToken = params.get("FaceIdToken")
        self.IsNeedVideo = params.get("IsNeedVideo")
        self.IsNeedBestFrame = params.get("IsNeedBestFrame")


class GetFaceIdResultResponse(AbstractModel):
    """GetFaceIdResult返回参数结构体

    """

    def __init__(self):
        """
        :param IdCard: 身份证
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Result: 业务核验结果，参考https://cloud.tencent.com/document/product/1007/47912
        :type Result: str
        :param Description: 业务核验描述
        :type Description: str
        :param Similarity: 相似度，0-100，数值越大相似度越高
        :type Similarity: float
        :param VideoBase64: 用户核验的视频
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoBase64: str
        :param BestFrameBase64: 用户核验视频的截帧
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Extra: 获取token时透传的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdCard = None
        self.Name = None
        self.Result = None
        self.Description = None
        self.Similarity = None
        self.VideoBase64 = None
        self.BestFrameBase64 = None
        self.Extra = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Similarity = params.get("Similarity")
        self.VideoBase64 = params.get("VideoBase64")
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Extra = params.get("Extra")
        self.RequestId = params.get("RequestId")


class GetFaceIdTokenRequest(AbstractModel):
    """GetFaceIdToken请求参数结构体

    """

    def __init__(self):
        """
        :param CompareLib: 本地上传照片(LOCAL)、商业库(BUSINESS)
        :type CompareLib: str
        :param IdCard: CompareLib为商业库时必传。
        :type IdCard: str
        :param Name: CompareLib为商业库库时必传。
        :type Name: str
        :param ImageBase64: CompareLib为上传照片比对时必传，Base64后图片最大8MB。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param Meta: SDK中生成的Meta字符串
        :type Meta: str
        :param Extra: 透传参数 1000长度字符串
        :type Extra: str
        """
        self.CompareLib = None
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.Meta = None
        self.Extra = None


    def _deserialize(self, params):
        self.CompareLib = params.get("CompareLib")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.Meta = params.get("Meta")
        self.Extra = params.get("Extra")


class GetFaceIdTokenResponse(AbstractModel):
    """GetFaceIdToken返回参数结构体

    """

    def __init__(self):
        """
        :param FaceIdToken: 有效期 10分钟。只能完成1次核身。
        :type FaceIdToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FaceIdToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceIdToken = params.get("FaceIdToken")
        self.RequestId = params.get("RequestId")


class GetLiveCodeRequest(AbstractModel):
    """GetLiveCode请求参数结构体

    """


class GetLiveCodeResponse(AbstractModel):
    """GetLiveCode返回参数结构体

    """

    def __init__(self):
        """
        :param LiveCode: 数字验证码，如：1234
        :type LiveCode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LiveCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LiveCode = params.get("LiveCode")
        self.RequestId = params.get("RequestId")


class IdCardOCRVerificationRequest(AbstractModel):
    """IdCardOCRVerification请求参数结构体

    """

    def __init__(self):
        """
        :param IdCard: 身份证号
姓名和身份证号、ImageBase64、ImageUrl三者必须提供其中之一。若都提供了，则按照姓名和身份证号>ImageBase64>ImageUrl的优先级使用参数。
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param ImageBase64: 身份证人像面的 Base64 值
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经Base64编码后不超过 3M。请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param ImageUrl: 身份证人像面的 Url 地址
支持的图片格式：PNG、JPG、JPEG，暂不支持 GIF 格式。
支持的图片大小：所下载图片经 Base64 编码后不超过 3M。图片下载时间不超过 3 秒。
图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。
非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type ImageUrl: str
        """
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class IdCardOCRVerificationResponse(AbstractModel):
    """IdCardOCRVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 姓名和身份证号一致
-1: 姓名和身份证号不一致
不收费结果码：
-2: 非法身份证号（长度、校验位等不正确）
-3: 非法姓名（长度、格式等不正确）
-4: 证件库服务异常
-5: 证件库中无此身份证记录
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param Name: 用于验证的姓名
        :type Name: str
        :param IdCard: 用于验证的身份证号
        :type IdCard: str
        :param Sex: OCR得到的性别
注意：此字段可能返回 null，表示取不到有效值。
        :type Sex: str
        :param Nation: OCR得到的民族
注意：此字段可能返回 null，表示取不到有效值。
        :type Nation: str
        :param Birth: OCR得到的生日
注意：此字段可能返回 null，表示取不到有效值。
        :type Birth: str
        :param Address: OCR得到的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.Name = None
        self.IdCard = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.IdCard = params.get("IdCard")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.RequestId = params.get("RequestId")


class IdCardVerificationRequest(AbstractModel):
    """IdCardVerification请求参数结构体

    """

    def __init__(self):
        """
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        """
        self.IdCard = None
        self.Name = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")


class IdCardVerificationResponse(AbstractModel):
    """IdCardVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 姓名和身份证号一致
-1: 姓名和身份证号不一致
不收费结果码：
-2: 非法身份证号（长度、校验位等不正确）
-3: 非法姓名（长度、格式等不正确）
-4: 证件库服务异常
-5: 证件库中无此身份证记录
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class ImageRecognitionRequest(AbstractModel):
    """ImageRecognition请求参数结构体

    """

    def __init__(self):
        """
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名。中文请使用UTF-8编码。
        :type Name: str
        :param ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param Optional: 本接口不需要传递此参数。
        :type Optional: str
        """
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.Optional = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.Optional = params.get("Optional")


class ImageRecognitionResponse(AbstractModel):
    """ImageRecognition返回参数结构体

    """

    def __init__(self):
        """
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Sim = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class LivenessCompareRequest(AbstractModel):
    """LivenessCompare请求参数结构体

    """

    def __init__(self):
        """
        :param ImageBase64: 用于人脸比对的照片，图片的Base64值；
Base64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type ImageBase64: str
        :param VideoBase64: 用于活体检测的视频，视频的Base64值；
Base64编码后的大小不超过8M，支持mp4、avi、flv格式。
请使用标准的Base64编码方式(带=补位)，编码规范参考RFC4648。
        :type VideoBase64: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：空。
        :type ValidateData: str
        :param Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围1-10
}
        :type Optional: str
        """
        self.ImageBase64 = None
        self.VideoBase64 = None
        self.LivenessType = None
        self.ValidateData = None
        self.Optional = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.VideoBase64 = params.get("VideoBase64")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")


class LivenessCompareResponse(AbstractModel):
    """LivenessCompare返回参数结构体

    """

    def __init__(self):
        """
        :param BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）。
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param BestFrameList: 最佳截图列表，仅在配置了返回多张最佳截图时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")


class LivenessRecognitionRequest(AbstractModel):
    """LivenessRecognition请求参数结构体

    """

    def __init__(self):
        """
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名。中文请使用UTF-8编码。
        :type Name: str
        :param VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过8M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：空。
        :type ValidateData: str
        :param Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围1-10
}
        :type Optional: str
        """
        self.IdCard = None
        self.Name = None
        self.VideoBase64 = None
        self.LivenessType = None
        self.ValidateData = None
        self.Optional = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.VideoBase64 = params.get("VideoBase64")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")


class LivenessRecognitionResponse(AbstractModel):
    """LivenessRecognition返回参数结构体

    """

    def __init__(self):
        """
        :param BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param BestFrameList: 最佳截图列表，仅在配置了返回多张最佳截图时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")


class LivenessRequest(AbstractModel):
    """Liveness请求参数结构体

    """

    def __init__(self):
        """
        :param VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过8M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：不需要传递此参数。
        :type ValidateData: str
        :param Optional: 额外配置，传入JSON字符串。
{
"BestFrameNum": 2  //需要返回多张最佳截图，取值范围1-10
}
        :type Optional: str
        """
        self.VideoBase64 = None
        self.LivenessType = None
        self.ValidateData = None
        self.Optional = None


    def _deserialize(self, params):
        self.VideoBase64 = params.get("VideoBase64")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")


class LivenessResponse(AbstractModel):
    """Liveness返回参数结构体

    """

    def __init__(self):
        """
        :param BestFrameBase64: 验证通过后的视频最佳截图照片，照片为BASE64编码后的值，jpg格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameBase64: str
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param BestFrameList: 最佳最佳截图列表，仅在配置了返回多张最佳截图时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type BestFrameList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Result = None
        self.Description = None
        self.BestFrameList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.BestFrameList = params.get("BestFrameList")
        self.RequestId = params.get("RequestId")


class MinorsVerificationRequest(AbstractModel):
    """MinorsVerification请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 参与校验的参数类型。
0：使用手机号进行校验；
1：使用姓名与身份证号进行校验。
        :type Type: str
        :param Mobile: 手机号，11位数字，
特别提示：
手机号验证只限制在腾讯健康守护可信模型覆盖的数据范围内，与手机号本身在运营商是否实名无关联，不在范围会提示“手机号未实名”，建议客户与传入姓名和身份证号信息组合使用。
        :type Mobile: str
        :param IdCard: 身份证号码。
        :type IdCard: str
        :param Name: 姓名。
        :type Name: str
        """
        self.Type = None
        self.Mobile = None
        self.IdCard = None
        self.Name = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Mobile = params.get("Mobile")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")


class MinorsVerificationResponse(AbstractModel):
    """MinorsVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 结果码，收费情况如下。
收费结果码：
0: 成年
-1: 未成年
-3: 姓名和身份证号不一致

不收费结果码：
-2: 未查询到手机号信息
-4: 非法身份证号（长度、校验位等不正确）
-5: 非法姓名（长度、格式等不正确）
-6: 权威数据源服务异常
-7: 未查询到身份信息
-8: 权威数据源升级中，请稍后再试
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param AgeRange: 该字段的值为年龄区间。格式为[a,b)，
[0,8)表示年龄小于8周岁区间，不包括8岁；
[8,16)表示年龄8-16周岁区间，不包括16岁；
[16,18)表示年龄16-18周岁区间，不包括18岁；
[18,+)表示年龄大于18周岁。
        :type AgeRange: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.AgeRange = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.AgeRange = params.get("AgeRange")
        self.RequestId = params.get("RequestId")


class MobileNetworkTimeVerificationRequest(AbstractModel):
    """MobileNetworkTimeVerification请求参数结构体

    """

    def __init__(self):
        """
        :param Mobile: 手机号码
        :type Mobile: str
        """
        self.Mobile = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")


class MobileNetworkTimeVerificationResponse(AbstractModel):
    """MobileNetworkTimeVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0: 成功
-2: 手机号不存在
-3: 手机号存在，但无法查询到在网时长
不收费结果码：
-1: 手机号格式不正确
-4: 验证中心服务繁忙
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param Range: 在网时长区间。
格式为(a,b]，表示在网时长在a个月以上，b个月以下。若b为+时表示没有上限。
        :type Range: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.Range = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Range = params.get("Range")
        self.RequestId = params.get("RequestId")


class MobileStatusRequest(AbstractModel):
    """MobileStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Mobile: 手机号码
        :type Mobile: str
        """
        self.Mobile = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")


class MobileStatusResponse(AbstractModel):
    """MobileStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码，收费情况如下。
收费结果码：
0：成功
不收费结果码：
-1：未查询到结果
-2：手机号格式不正确
-3：验证中心服务繁忙
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param StatusCode: 状态码：
0：正常
1：停机
2：销号
3：空号
4：不在网
99：未知状态
        :type StatusCode: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.StatusCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.StatusCode = params.get("StatusCode")
        self.RequestId = params.get("RequestId")


class PhoneVerificationRequest(AbstractModel):
    """PhoneVerification请求参数结构体

    """

    def __init__(self):
        """
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Phone: 手机号
        :type Phone: str
        :param CiphertextBlob: 有加密需求的用户，接入传入kms的CiphertextBlob
        :type CiphertextBlob: str
        :param EncryptList: 在使用加密服务时，填入要被加密的字段。本接口中可填入加密后的IdCard，Name，Phone中的一个或多个
        :type EncryptList: list of str
        :param Iv: 有加密需求的用户，传入CBC加密的初试向量
        :type Iv: str
        """
        self.IdCard = None
        self.Name = None
        self.Phone = None
        self.CiphertextBlob = None
        self.EncryptList = None
        self.Iv = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.EncryptList = params.get("EncryptList")
        self.Iv = params.get("Iv")


class PhoneVerificationResponse(AbstractModel):
    """PhoneVerification返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 认证结果码:
收费结果码
0: 认证通过
-4: 信息不一致（手机号已实名，但姓名和身份证号与实名信息不一致）
-5: 手机号未实名
不收费结果码
-6: 手机号码不合法
-7: 身份证号码有误
-8: 姓名校验不通过
-9: 没有记录
-10: 认证未通过
-11: 验证中心服务繁忙
        :type Result: str
        :param Description: 业务结果描述。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")