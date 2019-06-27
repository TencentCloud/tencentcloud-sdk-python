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
        :param Result: 认证结果码。
  '0': '认证通过'
  '-1': '认证未通过'
  '-2': '姓名校验不通过'
  '-3': '银行卡号码有误'
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
  '-16': '服务繁忙'
        :type Result: str
        :param Description: 认证结果信息。
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
        :param IdCard: 身份证号码
        :type IdCard: str
        :param CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。（不填默认0）
0 身份证
1 军官证
2 护照
3 港澳证
4 台胞证
5 警官证
6 士兵证
7 其它证件
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
        :param Result: 认证结果码。
  '0': '认证通过'
  '-1': '认证未通过'
  '-2': '姓名校验不通过'
  '-3': '身份证号码有误'
  '-4': '银行卡号码有误'
  '-5': '手机号码不合法'
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
  '-18': '服务繁忙'
        :type Result: str
        :param Description: 认证结果信息。
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
        :param IdCard: 身份证号
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param BankCard: 银行卡
        :type BankCard: str
        :param CertType: 证件类型，请确认该证件为开户时使用的证件类型，未用于开户的证件信息不支持验证。（不填默认0）
0 身份证
1 军官证
2 护照
3 港澳证
4 台胞证
5 警官证
6 士兵证
7 其它证件
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
        :param Result: 认证结果码。
'0': '认证通过'
'-1': '认证未通过'
'-2': '姓名校验不通过'
'-3': '身份证号码有误'
'-4': '银行卡号码有误'
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
'-17': '服务繁忙'
        :type Result: str
        :param Description: 认证结果信息。
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


class DetectAuthRequest(AbstractModel):
    """DetectAuth请求参数结构体

    """

    def __init__(self):
        """
        :param RuleId: 用于细分客户使用场景，申请开通服务后，可以在腾讯云慧眼人脸核身控制台（https://console.cloud.tencent.com/faceid） 自助接入里面创建，审核通过后即可调用。如有疑问，请加慧眼小助手微信（faceid001）进行咨询。
        :type RuleId: str
        :param TerminalType: 本接口不需要传递此参数。
        :type TerminalType: str
        :param IdCard: 身份标识（与公安权威库比对时必须是身份证号）。
规则：a-zA-Z0-9组合。最长长度32位。
        :type IdCard: str
        :param Name: 姓名。最长长度32位。中文请使用UTF-8编码。
        :type Name: str
        :param RedirectUrl: 认证结束后重定向的回调链接地址。最长长度1024位。
        :type RedirectUrl: str
        :param Extra: 透传字段，在获取验证结果时返回。
        :type Extra: str
        :param ImageBase64: 用于人脸比对的照片，图片的BASE64值；
BASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
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


class GetActionSequenceRequest(AbstractModel):
    """GetActionSequence请求参数结构体

    """


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
    "Location": null, // 地理位置信息
    "Extra": "",          // DetectAuth结果传进来的Extra信息
    "Detail": {           // 活体一比一信息详情
      "LivenessData": []
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
        :param Result: 认证结果码。
0: 姓名和身份证号一致
-1: 姓名和身份证号不一致
-2: 身份证号错误
-3: 姓名错误
-4: 认证出错
        :type Result: str
        :param Description: 认证结果信息。
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
        :param ImageBase64: 用于人脸比对的照片，图片的BASE64值；
BASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
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
        :param Description: 业务错误描述
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
        :param ImageBase64: 用于人脸比对的照片，图片的BASE64值；
BASE64编码后的图片数据大小不超过3M，仅支持jpg、png格式。
        :type ImageBase64: str
        :param VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过5M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：空。
        :type ValidateData: str
        :param Optional: 本接口不需要传递此参数。
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
        :type BestFrameBase64: str
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）。
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务错误描述
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
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
BASE64编码后的大小不超过5M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：空。
        :type ValidateData: str
        :param Optional: 本接口不需要传递此参数。
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
        :type BestFrameBase64: str
        :param Sim: 相似度，取值范围 [0.00, 100.00]。推荐相似度大于等于70时可判断为同一人，可根据具体场景自行调整阈值（阈值70的误通过率为千分之一，阈值80的误通过率是万分之一）
        :type Sim: float
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务错误描述
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class LivenessRequest(AbstractModel):
    """Liveness请求参数结构体

    """

    def __init__(self):
        """
        :param VideoBase64: 用于活体检测的视频，视频的BASE64值；
BASE64编码后的大小不超过5M，支持mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活体检测类型，取值：LIP/ACTION/SILENT。
LIP为数字模式，ACTION为动作模式，SILENT为静默模式，三种模式选择一种传入。
        :type LivenessType: str
        :param ValidateData: 数字模式传参：数字验证码(1234)，需先调用接口获取数字验证码；
动作模式传参：传动作顺序(2,1 or 1,2)，需先调用接口获取动作顺序；
静默模式传参：不需要传递此参数。
        :type ValidateData: str
        :param Optional: 本接口不需要传递此参数。
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
        :type BestFrameBase64: str
        :param Result: 业务错误码，成功情况返回Success, 错误情况请参考下方错误码 列表中FailedOperation部分
        :type Result: str
        :param Description: 业务错误描述
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")