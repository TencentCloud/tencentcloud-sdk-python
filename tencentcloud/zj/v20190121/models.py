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


class AddCrowdPackInfoRequest(AbstractModel):
    """AddCrowdPackInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _Name: 人群包名称
        :type Name: str
        :param _FileName: 人群包文件名称,人群包文件必须为utf8编码，动态参数只能是汉字、数字、英文字母的组合，不能包含其他字符
        :type FileName: str
        :param _Desc: 人群包描述
        :type Desc: str
        :param _CosUrl: 已经上传好的人群包cos地址
        :type CosUrl: str
        :param _PhoneNum: 人群包手机号数量
        :type PhoneNum: int
        """
        self._License = None
        self._Name = None
        self._FileName = None
        self._Desc = None
        self._CosUrl = None
        self._PhoneNum = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum


    def _deserialize(self, params):
        self._License = params.get("License")
        self._Name = params.get("Name")
        self._FileName = params.get("FileName")
        self._Desc = params.get("Desc")
        self._CosUrl = params.get("CosUrl")
        self._PhoneNum = params.get("PhoneNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCrowdPackInfoResponse(AbstractModel):
    """AddCrowdPackInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsAddCrowdPackInfoResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsAddCrowdPackInfoResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _SignType: 签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司（0，1，2，3）。
1：APP（0，1，2，3，4） 。
2：网站（0，1，2，3，5）。
3：公众号或者小程序（0，1，2，3，6）。
4：商标（7）。
5：政府/机关事业单位/其他机构（2，3）。
注：必须按照对应关系选择证明类型，否则会审核失败。
        :type SignType: int
        :param _DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
5：网站备案后台截图（个人开发网站）。
6：小程序设置页面截图（个人认证小程序）。
7：商标注册书
        :type DocumentType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _ProofImage: 资质图片url
        :type ProofImage: str
        :param _SignName: 签名内容
        :type SignName: str
        :param _Remark: 签名备注，比如申请原因，使用场景等,可以填空
        :type Remark: str
        """
        self._License = None
        self._SignType = None
        self._DocumentType = None
        self._International = None
        self._ProofImage = None
        self._SignName = None
        self._Remark = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def SignType(self):
        return self._SignType

    @SignType.setter
    def SignType(self, SignType):
        self._SignType = SignType

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def ProofImage(self):
        return self._ProofImage

    @ProofImage.setter
    def ProofImage(self, ProofImage):
        self._ProofImage = ProofImage

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._License = params.get("License")
        self._SignType = params.get("SignType")
        self._DocumentType = params.get("DocumentType")
        self._International = params.get("International")
        self._ProofImage = params.get("ProofImage")
        self._SignName = params.get("SignName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 签名id数组
        :type Data: :class:`tencentcloud.zj.v20190121.models.PaasCreateSignResp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = PaasCreateSignResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddSmsTemplateDataStruct(AbstractModel):
    """短信模板创建接口返回

    """

    def __init__(self):
        r"""
        :param _TemplateId: 短信模板ID
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsTemplateRequest(AbstractModel):
    """AddSmsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _SignID: 短信签名，创建签名时返回
        :type SignID: int
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _TemplateContent: 短信内容，动态内容使用占位符{1}，{2}等表示
        :type TemplateContent: str
        :param _SmsType: 短信类型：{0:普通短信，1:营销短信}
        :type SmsType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _Remark: 短信模板标签
        :type Remark: str
        :param _Urls: 发送短信活动时配置的落地链接地址,仅用作短信活动
        :type Urls: list of str
        :param _CommonParams: 发送短信活动时用于展示人群包动态参数模板占位符序号或接口发送时变量占位符序号
        :type CommonParams: list of int
        :param _UrlParams: 发送短信活动时用于展示短连接模板占位符序号,仅用作短信活动
        :type UrlParams: list of int
        """
        self._License = None
        self._SignID = None
        self._TemplateName = None
        self._TemplateContent = None
        self._SmsType = None
        self._International = None
        self._Remark = None
        self._Urls = None
        self._CommonParams = None
        self._UrlParams = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def SignID(self):
        return self._SignID

    @SignID.setter
    def SignID(self, SignID):
        self._SignID = SignID

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def CommonParams(self):
        return self._CommonParams

    @CommonParams.setter
    def CommonParams(self, CommonParams):
        self._CommonParams = CommonParams

    @property
    def UrlParams(self):
        return self._UrlParams

    @UrlParams.setter
    def UrlParams(self, UrlParams):
        self._UrlParams = UrlParams


    def _deserialize(self, params):
        self._License = params.get("License")
        self._SignID = params.get("SignID")
        self._TemplateName = params.get("TemplateName")
        self._TemplateContent = params.get("TemplateContent")
        self._SmsType = params.get("SmsType")
        self._International = params.get("International")
        self._Remark = params.get("Remark")
        self._Urls = params.get("Urls")
        self._CommonParams = params.get("CommonParams")
        self._UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 短信模板创建接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.AddSmsTemplateDataStruct`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = AddSmsTemplateDataStruct()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CancelActivityData(AbstractModel):
    """取消活动的返回值Data部分

    """

    def __init__(self):
        r"""
        :param _Message: 成功返回时的文字描述
        :type Message: str
        """
        self._Message = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCampaignRequest(AbstractModel):
    """CancelCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _CampaignId: 短信活动id
        :type CampaignId: int
        """
        self._License = None
        self._CampaignId = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def CampaignId(self):
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._License = params.get("License")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCampaignResponse(AbstractModel):
    """CancelCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 处理结果
        :type Data: :class:`tencentcloud.zj.v20190121.models.CancelActivityData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CancelActivityData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateCampaignRequest(AbstractModel):
    """CreateCampaign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _SendTime: 短信活动发送时间
        :type SendTime: int
        :param _Name: 短信活动名称
        :type Name: str
        :param _Strategies: 发送策略
        :type Strategies: list of PaasStrategy
        :param _TemplateId: 废弃
        :type TemplateId: int
        :param _CrowdID: 废弃
        :type CrowdID: int
        :param _SmsType: 活动类型(0-短信,1-超短,不填默认为超短)
        :type SmsType: int
        """
        self._License = None
        self._SendTime = None
        self._Name = None
        self._Strategies = None
        self._TemplateId = None
        self._CrowdID = None
        self._SmsType = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def SendTime(self):
        return self._SendTime

    @SendTime.setter
    def SendTime(self, SendTime):
        self._SendTime = SendTime

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Strategies(self):
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def CrowdID(self):
        return self._CrowdID

    @CrowdID.setter
    def CrowdID(self, CrowdID):
        self._CrowdID = CrowdID

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType


    def _deserialize(self, params):
        self._License = params.get("License")
        self._SendTime = params.get("SendTime")
        self._Name = params.get("Name")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = PaasStrategy()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._TemplateId = params.get("TemplateId")
        self._CrowdID = params.get("CrowdID")
        self._SmsType = params.get("SmsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCampaignResponse(AbstractModel):
    """CreateCampaign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 活动信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsCreateCampaignResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsCreateCampaignResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateMmsInstanceItem(AbstractModel):
    """创建样例时候content元素

    """

    def __init__(self):
        r"""
        :param _ContentType: 素材类型：1-文本 2-图片 3-视频 4-音频
        :type ContentType: int
        :param _Content: 素材内容：如果素材是文本类型，直接填写文本内容，否则填写素材文件上传到cos后的url地址
        :type Content: str
        """
        self._ContentType = None
        self._Content = None

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ContentType = params.get("ContentType")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMmsInstanceRequest(AbstractModel):
    """CreateMmsInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _InstanceName: 样例名称
        :type InstanceName: str
        :param _Title: 标题
        :type Title: str
        :param _Sign: 签名
        :type Sign: str
        :param _Contents: 素材内容
        :type Contents: list of CreateMmsInstanceItem
        :param _Urls: 样例中链接动态变量对应的链接，和占位符顺序一致
        :type Urls: list of str
        :param _PhoneType: 机型列表
        :type PhoneType: list of int non-negative
        :param _CommonParams: 发送超短活动时用于展示人群包动态参数模板占位符序号或接口发送时变量占位符序号
        :type CommonParams: list of int non-negative
        :param _UrlParams: 发送超短活动时用于展示短连接模板占位符序号,仅用作超短活动
        :type UrlParams: list of int non-negative
        """
        self._License = None
        self._InstanceName = None
        self._Title = None
        self._Sign = None
        self._Contents = None
        self._Urls = None
        self._PhoneType = None
        self._CommonParams = None
        self._UrlParams = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def Contents(self):
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def PhoneType(self):
        return self._PhoneType

    @PhoneType.setter
    def PhoneType(self, PhoneType):
        self._PhoneType = PhoneType

    @property
    def CommonParams(self):
        return self._CommonParams

    @CommonParams.setter
    def CommonParams(self, CommonParams):
        self._CommonParams = CommonParams

    @property
    def UrlParams(self):
        return self._UrlParams

    @UrlParams.setter
    def UrlParams(self, UrlParams):
        self._UrlParams = UrlParams


    def _deserialize(self, params):
        self._License = params.get("License")
        self._InstanceName = params.get("InstanceName")
        self._Title = params.get("Title")
        self._Sign = params.get("Sign")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = CreateMmsInstanceItem()
                obj._deserialize(item)
                self._Contents.append(obj)
        self._Urls = params.get("Urls")
        self._PhoneType = params.get("PhoneType")
        self._CommonParams = params.get("CommonParams")
        self._UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMmsInstanceResp(AbstractModel):
    """创建超级短信样例返回结果

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回码：0-成功 其它-失败
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息
        :type ReturnMsg: str
        :param _InstanceId: 样例id
        :type InstanceId: int
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._InstanceId = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMmsInstanceResponse(AbstractModel):
    """CreateMmsInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建样例返回信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.CreateMmsInstanceResp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateMmsInstanceResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DelCrowdPackRequest(AbstractModel):
    """DelCrowdPack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _ID: 人群包id
        :type ID: int
        """
        self._License = None
        self._ID = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._License = params.get("License")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DelCrowdPackResponse(AbstractModel):
    """DelCrowdPack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsSuccessResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsSuccessResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DelMmsInstanceData(AbstractModel):
    """删除超短样例响应

    """

    def __init__(self):
        r"""
        :param _InstanceId: 样例id
        :type InstanceId: int
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DelTemplateRequest(AbstractModel):
    """DelTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _TemplateID: 短信模板ID
        :type TemplateID: int
        """
        self._License = None
        self._TemplateID = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def TemplateID(self):
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID


    def _deserialize(self, params):
        self._License = params.get("License")
        self._TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DelTemplateResponse(AbstractModel):
    """DelTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsSuccessResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsSuccessResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteMmsInstanceRequest(AbstractModel):
    """DeleteMmsInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _InstanceId: 超级短信样例id
        :type InstanceId: int
        """
        self._License = None
        self._InstanceId = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._License = params.get("License")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMmsInstanceResponse(AbstractModel):
    """DeleteMmsInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 删除信息返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.DelMmsInstanceData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DelMmsInstanceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMmsInstanceInfoRequest(AbstractModel):
    """DescribeMmsInstanceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _InstanceId: 彩信实例id
        :type InstanceId: int
        """
        self._License = None
        self._InstanceId = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._License = params.get("License")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMmsInstanceInfoResponse(AbstractModel):
    """DescribeMmsInstanceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 彩信实例信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.MmsInstanceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = MmsInstanceInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeMmsInstanceListRequest(AbstractModel):
    """DescribeMmsInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        :param _AppSubId: 业务代码
        :type AppSubId: str
        :param _Title: 实例标题
        :type Title: str
        """
        self._License = None
        self._Offset = None
        self._Limit = None
        self._AppSubId = None
        self._Title = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AppSubId(self):
        return self._AppSubId

    @AppSubId.setter
    def AppSubId(self, AppSubId):
        self._AppSubId = AppSubId

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._License = params.get("License")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AppSubId = params.get("AppSubId")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMmsInstanceListResponse(AbstractModel):
    """DescribeMmsInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 彩信实例信息列表返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.MmsInstanceInfoList`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = MmsInstanceInfoList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSmsCampaignStatisticsRequest(AbstractModel):
    """DescribeSmsCampaignStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CampaignId: 活动id
        :type CampaignId: int
        :param _License: 商户证书
        :type License: str
        """
        self._CampaignId = None
        self._License = None

    @property
    def CampaignId(self):
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        self._License = params.get("License")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsCampaignStatisticsResponse(AbstractModel):
    """DescribeSmsCampaignStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 响应数据
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsCampaignStatisticsData`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsCampaignStatisticsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeSmsSignListDataStruct(AbstractModel):
    """获取普通短信签名信息返回信息

    """

    def __init__(self):
        r"""
        :param _SignId: 签名Id
        :type SignId: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _StatusCode: 申请签名状态。其中：
0：表示审核通过。
-1：表示审核未通过或审核失败。
        :type StatusCode: int
        :param _ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param _SignName: 签名名称。
        :type SignName: str
        :param _CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        """
        self._SignId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._SignName = None
        self._CreateTime = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def SignName(self):
        return self._SignName

    @SignName.setter
    def SignName(self, SignName):
        self._SignName = SignName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._SignName = params.get("SignName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _SignIdSet: 签名ID数组
        :type SignIdSet: list of int non-negative
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        """
        self._License = None
        self._SignIdSet = None
        self._International = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def SignIdSet(self):
        return self._SignIdSet

    @SignIdSet.setter
    def SignIdSet(self, SignIdSet):
        self._SignIdSet = SignIdSet

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International


    def _deserialize(self, params):
        self._License = params.get("License")
        self._SignIdSet = params.get("SignIdSet")
        self._International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据
        :type Data: list of DescribeSmsSignListDataStruct
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeSmsSignListDataStruct()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSmsTemplateListDataStruct(AbstractModel):
    """获取短信模板状态返回

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板Id
        :type TemplateId: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _StatusCode: 申请签名状态。其中：
0：表示审核通过。
-1：表示审核未通过或审核失败。
        :type StatusCode: int
        :param _ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param _TemplateName: 模板名称。
        :type TemplateName: str
        :param _CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        """
        self._TemplateId = None
        self._International = None
        self._StatusCode = None
        self._ReviewReply = None
        self._TemplateName = None
        self._CreateTime = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ReviewReply(self):
        return self._ReviewReply

    @ReviewReply.setter
    def ReviewReply(self, ReviewReply):
        self._ReviewReply = ReviewReply

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._International = params.get("International")
        self._StatusCode = params.get("StatusCode")
        self._ReviewReply = params.get("ReviewReply")
        self._TemplateName = params.get("TemplateName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _TemplateIdSet: 短信模板id数组
        :type TemplateIdSet: list of int non-negative
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        """
        self._License = None
        self._TemplateIdSet = None
        self._International = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def TemplateIdSet(self):
        return self._TemplateIdSet

    @TemplateIdSet.setter
    def TemplateIdSet(self, TemplateIdSet):
        self._TemplateIdSet = TemplateIdSet

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International


    def _deserialize(self, params):
        self._License = params.get("License")
        self._TemplateIdSet = params.get("TemplateIdSet")
        self._International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回数据信息
        :type Data: list of DescribeSmsTemplateListDataStruct
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeSmsTemplateListDataStruct()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class GetCrowdPackListRequest(AbstractModel):
    """GetCrowdPackList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限制返回数量
        :type Limit: int
        :param _Name: 人群包名称，用于过滤人群包
        :type Name: str
        :param _Status: 人群包状态，默认-1，用于过滤人群包
        :type Status: int
        """
        self._License = None
        self._Offset = None
        self._Limit = None
        self._Name = None
        self._Status = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._License = params.get("License")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCrowdPackListResponse(AbstractModel):
    """GetCrowdPackList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 人群包信息列表
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsGetCrowdPackListResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsGetCrowdPackListResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetCrowdUploadInfoRequest(AbstractModel):
    """GetCrowdUploadInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _FileName: 上传文件名称
        :type FileName: str
        """
        self._License = None
        self._FileName = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._License = params.get("License")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCrowdUploadInfoResponse(AbstractModel):
    """GetCrowdUploadInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsGetCrowdUploadInfoResponse`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsGetCrowdUploadInfoResponse()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetSmsAmountInfoRequest(AbstractModel):
    """GetSmsAmountInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        """
        self._License = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License


    def _deserialize(self, params):
        self._License = params.get("License")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSmsAmountInfoResponse(AbstractModel):
    """GetSmsAmountInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 短信账号额度接口
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsAmountDataStruct`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = SmsAmountDataStruct()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetSmsCampaignStatusRequest(AbstractModel):
    """GetSmsCampaignStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _CampaignId: 活动ID
        :type CampaignId: int
        """
        self._License = None
        self._CampaignId = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def CampaignId(self):
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._License = params.get("License")
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSmsCampaignStatusResponse(AbstractModel):
    """GetSmsCampaignStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 活动状态
        :type Data: :class:`tencentcloud.zj.v20190121.models.PaasSmsCampaignStatusResp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = PaasSmsCampaignStatusResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class MmsInstanceInfo(AbstractModel):
    """彩信实例信息
    InstanceId   int
    	InstanceName string
    	Status       int
    	StatusInfo   string
    	AppSubId     string
    	Title        string
    	Sign         string
    	Contents     string
    	CreatedAt    string

    """

    def __init__(self):
        r"""
        :param _InstanceId: 彩信实例id
        :type InstanceId: int
        :param _InstanceName: 彩信实例名称
        :type InstanceName: str
        :param _Status: 状态是否通知
        :type Status: int
        :param _StatusInfo: 实例审核状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInfo: list of MmsInstanceStateInfo
        :param _AppSubId: 业务码
        :type AppSubId: str
        :param _Title: 彩信标题
        :type Title: str
        :param _Sign: 签名
        :type Sign: str
        :param _Contents: 彩信内容
        :type Contents: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _Urls: 样例配置的链接地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Urls: list of str
        :param _PhoneType: 机型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneType: list of int non-negative
        :param _CommonParams: 普通参数序号数组
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonParams: list of int non-negative
        :param _UrlParams: 链接参数序号数组
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlParams: list of int non-negative
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Status = None
        self._StatusInfo = None
        self._AppSubId = None
        self._Title = None
        self._Sign = None
        self._Contents = None
        self._CreatedAt = None
        self._Urls = None
        self._PhoneType = None
        self._CommonParams = None
        self._UrlParams = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusInfo(self):
        return self._StatusInfo

    @StatusInfo.setter
    def StatusInfo(self, StatusInfo):
        self._StatusInfo = StatusInfo

    @property
    def AppSubId(self):
        return self._AppSubId

    @AppSubId.setter
    def AppSubId(self, AppSubId):
        self._AppSubId = AppSubId

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def Contents(self):
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def PhoneType(self):
        return self._PhoneType

    @PhoneType.setter
    def PhoneType(self, PhoneType):
        self._PhoneType = PhoneType

    @property
    def CommonParams(self):
        return self._CommonParams

    @CommonParams.setter
    def CommonParams(self, CommonParams):
        self._CommonParams = CommonParams

    @property
    def UrlParams(self):
        return self._UrlParams

    @UrlParams.setter
    def UrlParams(self, UrlParams):
        self._UrlParams = UrlParams


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Status = params.get("Status")
        if params.get("StatusInfo") is not None:
            self._StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = MmsInstanceStateInfo()
                obj._deserialize(item)
                self._StatusInfo.append(obj)
        self._AppSubId = params.get("AppSubId")
        self._Title = params.get("Title")
        self._Sign = params.get("Sign")
        self._Contents = params.get("Contents")
        self._CreatedAt = params.get("CreatedAt")
        self._Urls = params.get("Urls")
        self._PhoneType = params.get("PhoneType")
        self._CommonParams = params.get("CommonParams")
        self._UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MmsInstanceInfoList(AbstractModel):
    """彩信实例状态列表

    """

    def __init__(self):
        r"""
        :param _Total: 总数据量
        :type Total: int
        :param _List: 彩信实例状态信息列表
        :type List: list of MmsInstanceInfo
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = MmsInstanceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MmsInstanceStateInfo(AbstractModel):
    """彩信实例审核状态

    """

    def __init__(self):
        r"""
        :param _Operator: 运营商
        :type Operator: str
        :param _State: 审核状态：0未审核，1审核通过，2审核拒绝
        :type State: int
        """
        self._Operator = None
        self._State = None

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._Operator = params.get("Operator")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsTemplateDataStruct(AbstractModel):
    """短信模板编辑接口出参

    """

    def __init__(self):
        r"""
        :param _TemplateId: 短信模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: int
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsTemplateRequest(AbstractModel):
    """ModifySmsTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _TemplateId: 短信模板id
        :type TemplateId: int
        :param _SignID: 短信签名，创建签名时返回
        :type SignID: int
        :param _TemplateName: 模板名称
        :type TemplateName: str
        :param _TemplateContent: 短信内容，动态内容使用占位符{1}，{2}等表示
        :type TemplateContent: str
        :param _SmsType: 短信类型：{0:普通短信，1:营销短信}
        :type SmsType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param _Remark: 短信模板标签
        :type Remark: str
        :param _Urls: 发送短信活动时配置的落地链接地址,仅用作短信活动
        :type Urls: list of str
        :param _CommonParams: 发送短信活动时用于展示人群包动态参数模板占位符序号,仅用作短信活动
        :type CommonParams: list of int
        :param _UrlParams: 发送短信活动时用于展示短连接模板占位符序号,仅用作短信活动
        :type UrlParams: list of int
        """
        self._License = None
        self._TemplateId = None
        self._SignID = None
        self._TemplateName = None
        self._TemplateContent = None
        self._SmsType = None
        self._International = None
        self._Remark = None
        self._Urls = None
        self._CommonParams = None
        self._UrlParams = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def SignID(self):
        return self._SignID

    @SignID.setter
    def SignID(self, SignID):
        self._SignID = SignID

    @property
    def TemplateName(self):
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def CommonParams(self):
        return self._CommonParams

    @CommonParams.setter
    def CommonParams(self, CommonParams):
        self._CommonParams = CommonParams

    @property
    def UrlParams(self):
        return self._UrlParams

    @UrlParams.setter
    def UrlParams(self, UrlParams):
        self._UrlParams = UrlParams


    def _deserialize(self, params):
        self._License = params.get("License")
        self._TemplateId = params.get("TemplateId")
        self._SignID = params.get("SignID")
        self._TemplateName = params.get("TemplateName")
        self._TemplateContent = params.get("TemplateContent")
        self._SmsType = params.get("SmsType")
        self._International = params.get("International")
        self._Remark = params.get("Remark")
        self._Urls = params.get("Urls")
        self._CommonParams = params.get("CommonParams")
        self._UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.ModifySmsTemplateDataStruct`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = ModifySmsTemplateDataStruct()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class PaasCreateSignResp(AbstractModel):
    """创建签名返回结构

    """

    def __init__(self):
        r"""
        :param _SignId: 签名id
        :type SignId: int
        """
        self._SignId = None

    @property
    def SignId(self):
        return self._SignId

    @SignId.setter
    def SignId(self, SignId):
        self._SignId = SignId


    def _deserialize(self, params):
        self._SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaasSmsCampaignStatusResp(AbstractModel):
    """拉取活动状态返回

    """

    def __init__(self):
        r"""
        :param _Status: 0-未发送 1-发送中 2-发送结束 3-发送取消
        :type Status: int
        """
        self._Status = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaasStrategy(AbstractModel):
    """短信发送人群包策略

    """

    def __init__(self):
        r"""
        :param _CrowdID: 人群包id
        :type CrowdID: int
        :param _Items: 待选素材数组
        :type Items: list of PaasStrategyItem
        """
        self._CrowdID = None
        self._Items = None

    @property
    def CrowdID(self):
        return self._CrowdID

    @CrowdID.setter
    def CrowdID(self, CrowdID):
        self._CrowdID = CrowdID

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._CrowdID = params.get("CrowdID")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = PaasStrategyItem()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaasStrategyItem(AbstractModel):
    """短信活动策略元素

    """

    def __init__(self):
        r"""
        :param _Id: 短信模板id或超级短信样例id
        :type Id: int
        :param _ContentType: 素材类型 0-普短 1-超短
        :type ContentType: int
        """
        self._Id = None
        self._ContentType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushMmsContentRequest(AbstractModel):
    """PushMmsContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _InstanceId: 素材样例id
        :type InstanceId: int
        :param _Tel: 手机号
        :type Tel: str
        :param _Session: 附带数据字段
        :type Session: str
        :param _DynamicParaKey: 动态参数key(即申请样例时设置的u_或p_开头的动态参数,要求序号有序)
        :type DynamicParaKey: list of str
        :param _DynamicParaValue: 动态参数值,和DynamicParaKey对应
        :type DynamicParaValue: list of str
        """
        self._License = None
        self._InstanceId = None
        self._Tel = None
        self._Session = None
        self._DynamicParaKey = None
        self._DynamicParaValue = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Tel(self):
        return self._Tel

    @Tel.setter
    def Tel(self, Tel):
        self._Tel = Tel

    @property
    def Session(self):
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

    @property
    def DynamicParaKey(self):
        return self._DynamicParaKey

    @DynamicParaKey.setter
    def DynamicParaKey(self, DynamicParaKey):
        self._DynamicParaKey = DynamicParaKey

    @property
    def DynamicParaValue(self):
        return self._DynamicParaValue

    @DynamicParaValue.setter
    def DynamicParaValue(self, DynamicParaValue):
        self._DynamicParaValue = DynamicParaValue


    def _deserialize(self, params):
        self._License = params.get("License")
        self._InstanceId = params.get("InstanceId")
        self._Tel = params.get("Tel")
        self._Session = params.get("Session")
        self._DynamicParaKey = params.get("DynamicParaKey")
        self._DynamicParaValue = params.get("DynamicParaValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushMmsContentResp(AbstractModel):
    """发送超级短信返回

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 返回码：0-成功 其它-失败
        :type ReturnCode: int
        :param _ReturnMsg: 返回信息
        :type ReturnMsg: str
        :param _MessageId: 消息回执id
        :type MessageId: int
        """
        self._ReturnCode = None
        self._ReturnMsg = None
        self._MessageId = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def ReturnMsg(self):
        return self._ReturnMsg

    @ReturnMsg.setter
    def ReturnMsg(self, ReturnMsg):
        self._ReturnMsg = ReturnMsg

    @property
    def MessageId(self):
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._ReturnMsg = params.get("ReturnMsg")
        self._MessageId = params.get("MessageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushMmsContentResponse(AbstractModel):
    """PushMmsContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 推送短信返回信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.PushMmsContentResp`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = PushMmsContentResp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SendSmsPaasDataStruct(AbstractModel):
    """发送短信返回

    """

    def __init__(self):
        r"""
        :param _SerialNo: 发送流水号
        :type SerialNo: str
        :param _PhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param _Fee: 计费条数
        :type Fee: int
        :param _Code: OK为成功
        :type Code: str
        :param _Message: 短信请求错误码描述
        :type Message: str
        """
        self._SerialNo = None
        self._PhoneNumber = None
        self._Fee = None
        self._Code = None
        self._Message = None

    @property
    def SerialNo(self):
        return self._SerialNo

    @SerialNo.setter
    def SerialNo(self, SerialNo):
        self._SerialNo = SerialNo

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def Fee(self):
        return self._Fee

    @Fee.setter
    def Fee(self, Fee):
        self._Fee = Fee

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._SerialNo = params.get("SerialNo")
        self._PhoneNumber = params.get("PhoneNumber")
        self._Fee = params.get("Fee")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsRequest(AbstractModel):
    """SendSms请求参数结构体

    """

    def __init__(self):
        r"""
        :param _License: 商户证书
        :type License: str
        :param _Phone: 手机号码,采用 e.164 标准，格式为+[国家或地区码][手机号]，单次请求最多支持200个手机号且要求全为境内手机号,如:+8613800138000
        :type Phone: list of str
        :param _TemplateId: 短信模板id(推荐使用模板id发送,使用内容发送时模板id留空)
        :type TemplateId: str
        :param _Params: 模板参数，若无模板参数，则设置为空。
        :type Params: list of str
        :param _Sign: 短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名。注：国内短信为必填参数。
        :type Sign: str
        :param _SenderId: 国际/港澳台短信 senderid，国内短信填空
        :type SenderId: str
        :param _SmsType: 短信类型：{0:普通短信，1:营销短信}，使用内容发送时必填
        :type SmsType: int
        :param _International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。使用内容发送时必填
        :type International: int
        :param _Content: 发送使用的模板内容,如果有占位符,此处也包括占位符,占位符的实际内容通过Params参数传递,使用模板id发送时此字段为空
        :type Content: str
        """
        self._License = None
        self._Phone = None
        self._TemplateId = None
        self._Params = None
        self._Sign = None
        self._SenderId = None
        self._SmsType = None
        self._International = None
        self._Content = None

    @property
    def License(self):
        return self._License

    @License.setter
    def License(self, License):
        self._License = License

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def SenderId(self):
        return self._SenderId

    @SenderId.setter
    def SenderId(self, SenderId):
        self._SenderId = SenderId

    @property
    def SmsType(self):
        return self._SmsType

    @SmsType.setter
    def SmsType(self, SmsType):
        self._SmsType = SmsType

    @property
    def International(self):
        return self._International

    @International.setter
    def International(self, International):
        self._International = International

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._License = params.get("License")
        self._Phone = params.get("Phone")
        self._TemplateId = params.get("TemplateId")
        self._Params = params.get("Params")
        self._Sign = params.get("Sign")
        self._SenderId = params.get("SenderId")
        self._SmsType = params.get("SmsType")
        self._International = params.get("International")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsResponse(AbstractModel):
    """SendSms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 出参数据
        :type Data: list of SendSmsPaasDataStruct
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SendSmsPaasDataStruct()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class SmsAddCrowdPackInfoResponse(AbstractModel):
    """添加短信人群包信息接口返回

    """

    def __init__(self):
        r"""
        :param _ID: 人群包id
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsAmountDataStruct(AbstractModel):
    """短信子账号额度接口出参

    """

    def __init__(self):
        r"""
        :param _SmsCampaignAmount: 短信活动配额
        :type SmsCampaignAmount: int
        :param _SmsCampaignConsume: 短信活动消耗配额
        :type SmsCampaignConsume: int
        :param _SmsSendAmount: 短信发送额度
        :type SmsSendAmount: int
        :param _SmsSendConsume: 短信发送消耗额度
        :type SmsSendConsume: int
        :param _MmsCampaignAmount: 超短活动额度
        :type MmsCampaignAmount: int
        :param _MmsCampaignConsume: 超短活动消耗额度
        :type MmsCampaignConsume: int
        :param _MmsSendAmount: 超短短信额度
        :type MmsSendAmount: int
        :param _MmsSendConsume: 超短短信消耗额度
        :type MmsSendConsume: int
        """
        self._SmsCampaignAmount = None
        self._SmsCampaignConsume = None
        self._SmsSendAmount = None
        self._SmsSendConsume = None
        self._MmsCampaignAmount = None
        self._MmsCampaignConsume = None
        self._MmsSendAmount = None
        self._MmsSendConsume = None

    @property
    def SmsCampaignAmount(self):
        return self._SmsCampaignAmount

    @SmsCampaignAmount.setter
    def SmsCampaignAmount(self, SmsCampaignAmount):
        self._SmsCampaignAmount = SmsCampaignAmount

    @property
    def SmsCampaignConsume(self):
        return self._SmsCampaignConsume

    @SmsCampaignConsume.setter
    def SmsCampaignConsume(self, SmsCampaignConsume):
        self._SmsCampaignConsume = SmsCampaignConsume

    @property
    def SmsSendAmount(self):
        return self._SmsSendAmount

    @SmsSendAmount.setter
    def SmsSendAmount(self, SmsSendAmount):
        self._SmsSendAmount = SmsSendAmount

    @property
    def SmsSendConsume(self):
        return self._SmsSendConsume

    @SmsSendConsume.setter
    def SmsSendConsume(self, SmsSendConsume):
        self._SmsSendConsume = SmsSendConsume

    @property
    def MmsCampaignAmount(self):
        return self._MmsCampaignAmount

    @MmsCampaignAmount.setter
    def MmsCampaignAmount(self, MmsCampaignAmount):
        self._MmsCampaignAmount = MmsCampaignAmount

    @property
    def MmsCampaignConsume(self):
        return self._MmsCampaignConsume

    @MmsCampaignConsume.setter
    def MmsCampaignConsume(self, MmsCampaignConsume):
        self._MmsCampaignConsume = MmsCampaignConsume

    @property
    def MmsSendAmount(self):
        return self._MmsSendAmount

    @MmsSendAmount.setter
    def MmsSendAmount(self, MmsSendAmount):
        self._MmsSendAmount = MmsSendAmount

    @property
    def MmsSendConsume(self):
        return self._MmsSendConsume

    @MmsSendConsume.setter
    def MmsSendConsume(self, MmsSendConsume):
        self._MmsSendConsume = MmsSendConsume


    def _deserialize(self, params):
        self._SmsCampaignAmount = params.get("SmsCampaignAmount")
        self._SmsCampaignConsume = params.get("SmsCampaignConsume")
        self._SmsSendAmount = params.get("SmsSendAmount")
        self._SmsSendConsume = params.get("SmsSendConsume")
        self._MmsCampaignAmount = params.get("MmsCampaignAmount")
        self._MmsCampaignConsume = params.get("MmsCampaignConsume")
        self._MmsSendAmount = params.get("MmsSendAmount")
        self._MmsSendConsume = params.get("MmsSendConsume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsCampaignStatisticsCrowdData(AbstractModel):
    """短信活动统计人群包数据

    """

    def __init__(self):
        r"""
        :param _CrowdId: 人群包id
        :type CrowdId: int
        :param _CrowdName: 人群包名称
        :type CrowdName: str
        :param _CrowdCount: 人群包目标触达总数
        :type CrowdCount: int
        :param _TemplateList: 模板列表
        :type TemplateList: list of SmsCampaignStatisticsTemplateData
        """
        self._CrowdId = None
        self._CrowdName = None
        self._CrowdCount = None
        self._TemplateList = None

    @property
    def CrowdId(self):
        return self._CrowdId

    @CrowdId.setter
    def CrowdId(self, CrowdId):
        self._CrowdId = CrowdId

    @property
    def CrowdName(self):
        return self._CrowdName

    @CrowdName.setter
    def CrowdName(self, CrowdName):
        self._CrowdName = CrowdName

    @property
    def CrowdCount(self):
        return self._CrowdCount

    @CrowdCount.setter
    def CrowdCount(self, CrowdCount):
        self._CrowdCount = CrowdCount

    @property
    def TemplateList(self):
        return self._TemplateList

    @TemplateList.setter
    def TemplateList(self, TemplateList):
        self._TemplateList = TemplateList


    def _deserialize(self, params):
        self._CrowdId = params.get("CrowdId")
        self._CrowdName = params.get("CrowdName")
        self._CrowdCount = params.get("CrowdCount")
        if params.get("TemplateList") is not None:
            self._TemplateList = []
            for item in params.get("TemplateList"):
                obj = SmsCampaignStatisticsTemplateData()
                obj._deserialize(item)
                self._TemplateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsCampaignStatisticsData(AbstractModel):
    """短信活动统计响应

    """

    def __init__(self):
        r"""
        :param _CampaignId: 活动Id
        :type CampaignId: int
        :param _Statistics: 统计数据
        :type Statistics: list of SmsCampaignStatisticsCrowdData
        """
        self._CampaignId = None
        self._Statistics = None

    @property
    def CampaignId(self):
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId

    @property
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        if params.get("Statistics") is not None:
            self._Statistics = []
            for item in params.get("Statistics"):
                obj = SmsCampaignStatisticsCrowdData()
                obj._deserialize(item)
                self._Statistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsCampaignStatisticsTemplateData(AbstractModel):
    """短信活动统计模板展示结构

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板或样例id
        :type TemplateId: str
        :param _TemplateContent: 模板内容
        :type TemplateContent: str
        :param _SendCount: 触达成功数
        :type SendCount: int
        :param _ClickCount: 短链点击数
        :type ClickCount: int
        """
        self._TemplateId = None
        self._TemplateContent = None
        self._SendCount = None
        self._ClickCount = None

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateContent(self):
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def SendCount(self):
        return self._SendCount

    @SendCount.setter
    def SendCount(self, SendCount):
        self._SendCount = SendCount

    @property
    def ClickCount(self):
        return self._ClickCount

    @ClickCount.setter
    def ClickCount(self, ClickCount):
        self._ClickCount = ClickCount


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateContent = params.get("TemplateContent")
        self._SendCount = params.get("SendCount")
        self._ClickCount = params.get("ClickCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsCreateCampaignResponse(AbstractModel):
    """创建短信活动返回结构

    """

    def __init__(self):
        r"""
        :param _CampaignId: 活动id
        :type CampaignId: int
        """
        self._CampaignId = None

    @property
    def CampaignId(self):
        return self._CampaignId

    @CampaignId.setter
    def CampaignId(self, CampaignId):
        self._CampaignId = CampaignId


    def _deserialize(self, params):
        self._CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsGetCrowdPackList(AbstractModel):
    """短信获取人群包列表的返回数据信息

    """

    def __init__(self):
        r"""
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _ID: 人群包id
        :type ID: int
        :param _Name: 人群包名称
        :type Name: str
        :param _Status: 人群包状态
        :type Status: int
        :param _PhoneNum: 人群包手机号数量
        :type PhoneNum: int
        :param _Tag: 人群包标签信息
        :type Tag: str
        :param _MD5: 人群包md5
        :type MD5: str
        :param _FileName: 人群包文件名称
        :type FileName: str
        :param _Desc: 人群包描述
        :type Desc: str
        """
        self._CreatedAt = None
        self._ID = None
        self._Name = None
        self._Status = None
        self._PhoneNum = None
        self._Tag = None
        self._MD5 = None
        self._FileName = None
        self._Desc = None

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PhoneNum(self):
        return self._PhoneNum

    @PhoneNum.setter
    def PhoneNum(self, PhoneNum):
        self._PhoneNum = PhoneNum

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def MD5(self):
        return self._MD5

    @MD5.setter
    def MD5(self, MD5):
        self._MD5 = MD5

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._CreatedAt = params.get("CreatedAt")
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._PhoneNum = params.get("PhoneNum")
        self._Tag = params.get("Tag")
        self._MD5 = params.get("MD5")
        self._FileName = params.get("FileName")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsGetCrowdPackListResponse(AbstractModel):
    """短信人群包返回信息

    """

    def __init__(self):
        r"""
        :param _Total: 人群包总数
        :type Total: int
        :param _List: 人群包返回数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of SmsGetCrowdPackList
        """
        self._Total = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SmsGetCrowdPackList()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsGetCrowdUploadInfoResponse(AbstractModel):
    """获取短信人群包上传信息返回

    """

    def __init__(self):
        r"""
        :param _ExpiredTime: 过期时间
        :type ExpiredTime: int
        :param _SessionToken: 会话token
        :type SessionToken: str
        :param _TmpSecretId: 临时密钥id
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时密钥
        :type TmpSecretKey: str
        :param _CosInfo: cos信息
        :type CosInfo: :class:`tencentcloud.zj.v20190121.models.UploadFansInfoCosInfo`
        """
        self._ExpiredTime = None
        self._SessionToken = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._CosInfo = None

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SessionToken(self):
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def CosInfo(self):
        return self._CosInfo

    @CosInfo.setter
    def CosInfo(self, CosInfo):
        self._CosInfo = CosInfo


    def _deserialize(self, params):
        self._ExpiredTime = params.get("ExpiredTime")
        self._SessionToken = params.get("SessionToken")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        if params.get("CosInfo") is not None:
            self._CosInfo = UploadFansInfoCosInfo()
            self._CosInfo._deserialize(params.get("CosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmsSuccessResponse(AbstractModel):
    """短信api成功返回信息

    """

    def __init__(self):
        r"""
        :param _Message: 成功返回信息
        :type Message: str
        """
        self._Message = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFansInfoCosInfo(AbstractModel):
    """接口返回给服务商的COS路径等信息

    """

    def __init__(self):
        r"""
        :param _Bucket: COS bucket
        :type Bucket: str
        :param _Key: COS路径
        :type Key: str
        :param _Region: COS区域
        :type Region: str
        """
        self._Bucket = None
        self._Key = None
        self._Region = None

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Key = params.get("Key")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        