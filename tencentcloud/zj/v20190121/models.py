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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddCrowdPackInfoRequest(AbstractModel):
    """AddCrowdPackInfo请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param Name: 人群包名称
        :type Name: str
        :param FileName: 人群包文件名称,人群包文件必须为utf8编码，动态参数只能是汉字、数字、英文字母的组合，不能包含其他字符
        :type FileName: str
        :param Desc: 人群包描述
        :type Desc: str
        :param CosUrl: 已经上传好的人群包cos地址
        :type CosUrl: str
        :param PhoneNum: 人群包手机号数量
        :type PhoneNum: int
        """
        self.License = None
        self.Name = None
        self.FileName = None
        self.Desc = None
        self.CosUrl = None
        self.PhoneNum = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.Name = params.get("Name")
        self.FileName = params.get("FileName")
        self.Desc = params.get("Desc")
        self.CosUrl = params.get("CosUrl")
        self.PhoneNum = params.get("PhoneNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddCrowdPackInfoResponse(AbstractModel):
    """AddCrowdPackInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsAddCrowdPackInfoResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsAddCrowdPackInfoResponse()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param SignType: 签名类型。其中每种类型后面标注了其可选的 DocumentType（证明类型）：
0：公司（0，1，2，3）。
1：APP（0，1，2，3，4） 。
2：网站（0，1，2，3，5）。
3：公众号或者小程序（0，1，2，3，6）。
4：商标（7）。
5：政府/机关事业单位/其他机构（2，3）。
注：必须按照对应关系选择证明类型，否则会审核失败。
        :type SignType: int
        :param DocumentType: 证明类型：
0：三证合一。
1：企业营业执照。
2：组织机构代码证书。
3：社会信用代码证书。
4：应用后台管理截图（个人开发APP）。
5：网站备案后台截图（个人开发网站）。
6：小程序设置页面截图（个人认证小程序）。
7：商标注册书
        :type DocumentType: int
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param ProofImage: 资质图片url
        :type ProofImage: str
        :param SignName: 签名内容
        :type SignName: str
        :param Remark: 签名备注，比如申请原因，使用场景等,可以填空
        :type Remark: str
        """
        self.License = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.ProofImage = None
        self.SignName = None
        self.Remark = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.ProofImage = params.get("ProofImage")
        self.SignName = params.get("SignName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 签名id数组
        :type Data: :class:`tencentcloud.zj.v20190121.models.PaasCreateSignResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = PaasCreateSignResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddSmsTemplateDataStruct(AbstractModel):
    """短信模板创建接口返回

    """

    def __init__(self):
        """
        :param TemplateId: 短信模板ID
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddSmsTemplateRequest(AbstractModel):
    """AddSmsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param SignID: 短信签名，创建签名时返回
        :type SignID: int
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param TemplateContent: 短信内容，动态内容使用占位符{1}，{2}等表示
        :type TemplateContent: str
        :param SmsType: 短信类型：{0:普通短信，1:营销短信}
        :type SmsType: int
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param Remark: 短信模板标签
        :type Remark: str
        :param Urls: 发送短信活动时配置的落地链接地址,仅用作短信活动
        :type Urls: list of str
        :param CommonParams: 发送短信活动时用于展示人群包动态参数模板占位符序号或接口发送时变量占位符序号
        :type CommonParams: list of int
        :param UrlParams: 发送短信活动时用于展示短连接模板占位符序号,仅用作短信活动
        :type UrlParams: list of int
        """
        self.License = None
        self.SignID = None
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None
        self.Urls = None
        self.CommonParams = None
        self.UrlParams = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.SignID = params.get("SignID")
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")
        self.Urls = params.get("Urls")
        self.CommonParams = params.get("CommonParams")
        self.UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 短信模板创建接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.AddSmsTemplateDataStruct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AddSmsTemplateDataStruct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelActivityData(AbstractModel):
    """取消活动的返回值Data部分

    """

    def __init__(self):
        """
        :param Message: 成功返回时的文字描述
        :type Message: str
        """
        self.Message = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelCampaignRequest(AbstractModel):
    """CancelCampaign请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param CampaignId: 短信活动id
        :type CampaignId: int
        """
        self.License = None
        self.CampaignId = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CancelCampaignResponse(AbstractModel):
    """CancelCampaign返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 处理结果
        :type Data: :class:`tencentcloud.zj.v20190121.models.CancelActivityData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CancelActivityData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCampaignRequest(AbstractModel):
    """CreateCampaign请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param SendTime: 短信活动发送时间
        :type SendTime: int
        :param Name: 短信活动名称
        :type Name: str
        :param Strategies: 发送策略
        :type Strategies: list of PaasStrategy
        :param TemplateId: 废弃
        :type TemplateId: int
        :param CrowdID: 废弃
        :type CrowdID: int
        :param SmsType: 活动类型(0-短信,1-超短,不填默认为超短)
        :type SmsType: int
        """
        self.License = None
        self.SendTime = None
        self.Name = None
        self.Strategies = None
        self.TemplateId = None
        self.CrowdID = None
        self.SmsType = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.SendTime = params.get("SendTime")
        self.Name = params.get("Name")
        if params.get("Strategies") is not None:
            self.Strategies = []
            for item in params.get("Strategies"):
                obj = PaasStrategy()
                obj._deserialize(item)
                self.Strategies.append(obj)
        self.TemplateId = params.get("TemplateId")
        self.CrowdID = params.get("CrowdID")
        self.SmsType = params.get("SmsType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateCampaignResponse(AbstractModel):
    """CreateCampaign返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 活动信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsCreateCampaignResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsCreateCampaignResponse()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMmsInstanceItem(AbstractModel):
    """创建样例时候content元素

    """

    def __init__(self):
        """
        :param ContentType: 素材类型：1-文本 2-图片 3-视频 4-音频
        :type ContentType: int
        :param Content: 素材内容：如果素材是文本类型，直接填写文本内容，否则填写素材文件上传到cos后的url地址
        :type Content: str
        """
        self.ContentType = None
        self.Content = None


    def _deserialize(self, params):
        self.ContentType = params.get("ContentType")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMmsInstanceRequest(AbstractModel):
    """CreateMmsInstance请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param InstanceName: 样例名称
        :type InstanceName: str
        :param Title: 标题
        :type Title: str
        :param Sign: 签名
        :type Sign: str
        :param Contents: 素材内容
        :type Contents: list of CreateMmsInstanceItem
        :param Urls: 样例中链接动态变量对应的链接，和占位符顺序一致
        :type Urls: list of str
        :param PhoneType: 机型列表
        :type PhoneType: list of int non-negative
        :param CommonParams: 发送超短活动时用于展示人群包动态参数模板占位符序号或接口发送时变量占位符序号
        :type CommonParams: list of int non-negative
        :param UrlParams: 发送超短活动时用于展示短连接模板占位符序号,仅用作超短活动
        :type UrlParams: list of int non-negative
        """
        self.License = None
        self.InstanceName = None
        self.Title = None
        self.Sign = None
        self.Contents = None
        self.Urls = None
        self.PhoneType = None
        self.CommonParams = None
        self.UrlParams = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.InstanceName = params.get("InstanceName")
        self.Title = params.get("Title")
        self.Sign = params.get("Sign")
        if params.get("Contents") is not None:
            self.Contents = []
            for item in params.get("Contents"):
                obj = CreateMmsInstanceItem()
                obj._deserialize(item)
                self.Contents.append(obj)
        self.Urls = params.get("Urls")
        self.PhoneType = params.get("PhoneType")
        self.CommonParams = params.get("CommonParams")
        self.UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMmsInstanceResp(AbstractModel):
    """创建超级短信样例返回结果

    """

    def __init__(self):
        """
        :param ReturnCode: 返回码：0-成功 其它-失败
        :type ReturnCode: int
        :param ReturnMsg: 返回信息
        :type ReturnMsg: str
        :param InstanceId: 样例id
        :type InstanceId: int
        """
        self.ReturnCode = None
        self.ReturnMsg = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMmsInstanceResponse(AbstractModel):
    """CreateMmsInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 创建样例返回信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.CreateMmsInstanceResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CreateMmsInstanceResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DelCrowdPackRequest(AbstractModel):
    """DelCrowdPack请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param ID: 人群包id
        :type ID: int
        """
        self.License = None
        self.ID = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DelCrowdPackResponse(AbstractModel):
    """DelCrowdPack返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsSuccessResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsSuccessResponse()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DelMmsInstanceData(AbstractModel):
    """删除超短样例响应

    """

    def __init__(self):
        """
        :param InstanceId: 样例id
        :type InstanceId: int
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DelTemplateRequest(AbstractModel):
    """DelTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param TemplateID: 短信模板ID
        :type TemplateID: int
        """
        self.License = None
        self.TemplateID = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DelTemplateResponse(AbstractModel):
    """DelTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 接口返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsSuccessResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsSuccessResponse()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMmsInstanceRequest(AbstractModel):
    """DeleteMmsInstance请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param InstanceId: 超级短信样例id
        :type InstanceId: int
        """
        self.License = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMmsInstanceResponse(AbstractModel):
    """DeleteMmsInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 删除信息返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.DelMmsInstanceData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DelMmsInstanceData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMmsInstanceInfoRequest(AbstractModel):
    """DescribeMmsInstanceInfo请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param InstanceId: 彩信实例id
        :type InstanceId: int
        """
        self.License = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMmsInstanceInfoResponse(AbstractModel):
    """DescribeMmsInstanceInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 彩信实例信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.MmsInstanceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = MmsInstanceInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMmsInstanceListRequest(AbstractModel):
    """DescribeMmsInstanceList请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        :param AppSubId: 业务代码
        :type AppSubId: str
        :param Title: 实例标题
        :type Title: str
        """
        self.License = None
        self.Offset = None
        self.Limit = None
        self.AppSubId = None
        self.Title = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.AppSubId = params.get("AppSubId")
        self.Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMmsInstanceListResponse(AbstractModel):
    """DescribeMmsInstanceList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 彩信实例信息列表返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.MmsInstanceInfoList`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = MmsInstanceInfoList()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsCampaignStatisticsRequest(AbstractModel):
    """DescribeSmsCampaignStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param CampaignId: 活动id
        :type CampaignId: int
        :param License: 商户证书
        :type License: str
        """
        self.CampaignId = None
        self.License = None


    def _deserialize(self, params):
        self.CampaignId = params.get("CampaignId")
        self.License = params.get("License")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsCampaignStatisticsResponse(AbstractModel):
    """DescribeSmsCampaignStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 响应数据
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsCampaignStatisticsData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsCampaignStatisticsData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsSignListDataStruct(AbstractModel):
    """获取普通短信签名信息返回信息

    """

    def __init__(self):
        """
        :param SignId: 签名Id
        :type SignId: int
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param StatusCode: 申请签名状态。其中：
0：表示审核通过。
-1：表示审核未通过或审核失败。
        :type StatusCode: int
        :param ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param SignName: 签名名称。
        :type SignName: str
        :param CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        """
        self.SignId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.SignName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.SignName = params.get("SignName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param SignIdSet: 签名ID数组
        :type SignIdSet: list of int non-negative
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        """
        self.License = None
        self.SignIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.SignIdSet = params.get("SignIdSet")
        self.International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回数据
        :type Data: list of DescribeSmsSignListDataStruct
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DescribeSmsSignListDataStruct()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsTemplateListDataStruct(AbstractModel):
    """获取短信模板状态返回

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id
        :type TemplateId: int
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param StatusCode: 申请签名状态。其中：
0：表示审核通过。
-1：表示审核未通过或审核失败。
        :type StatusCode: int
        :param ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        """
        self.TemplateId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.TemplateName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.TemplateName = params.get("TemplateName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param TemplateIdSet: 短信模板id数组
        :type TemplateIdSet: list of int non-negative
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        """
        self.License = None
        self.TemplateIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.TemplateIdSet = params.get("TemplateIdSet")
        self.International = params.get("International")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回数据信息
        :type Data: list of DescribeSmsTemplateListDataStruct
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DescribeSmsTemplateListDataStruct()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetCrowdPackListRequest(AbstractModel):
    """GetCrowdPackList请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制返回数量
        :type Limit: int
        :param Name: 人群包名称，用于过滤人群包
        :type Name: str
        :param Status: 人群包状态，默认-1，用于过滤人群包
        :type Status: int
        """
        self.License = None
        self.Offset = None
        self.Limit = None
        self.Name = None
        self.Status = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetCrowdPackListResponse(AbstractModel):
    """GetCrowdPackList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 人群包信息列表
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsGetCrowdPackListResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsGetCrowdPackListResponse()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetCrowdUploadInfoRequest(AbstractModel):
    """GetCrowdUploadInfo请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param FileName: 上传文件名称
        :type FileName: str
        """
        self.License = None
        self.FileName = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetCrowdUploadInfoResponse(AbstractModel):
    """GetCrowdUploadInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsGetCrowdUploadInfoResponse`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsGetCrowdUploadInfoResponse()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetSmsAmountInfoRequest(AbstractModel):
    """GetSmsAmountInfo请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        """
        self.License = None


    def _deserialize(self, params):
        self.License = params.get("License")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetSmsAmountInfoResponse(AbstractModel):
    """GetSmsAmountInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 短信账号额度接口
        :type Data: :class:`tencentcloud.zj.v20190121.models.SmsAmountDataStruct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsAmountDataStruct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetSmsCampaignStatusRequest(AbstractModel):
    """GetSmsCampaignStatus请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param CampaignId: 活动ID
        :type CampaignId: int
        """
        self.License = None
        self.CampaignId = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetSmsCampaignStatusResponse(AbstractModel):
    """GetSmsCampaignStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 活动状态
        :type Data: :class:`tencentcloud.zj.v20190121.models.PaasSmsCampaignStatusResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = PaasSmsCampaignStatusResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        """
        :param InstanceId: 彩信实例id
        :type InstanceId: int
        :param InstanceName: 彩信实例名称
        :type InstanceName: str
        :param Status: 状态是否通知
        :type Status: int
        :param StatusInfo: 实例审核状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInfo: list of MmsInstanceStateInfo
        :param AppSubId: 业务码
        :type AppSubId: str
        :param Title: 彩信标题
        :type Title: str
        :param Sign: 签名
        :type Sign: str
        :param Contents: 彩信内容
        :type Contents: str
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param Urls: 样例配置的链接地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Urls: list of str
        :param PhoneType: 机型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneType: list of int non-negative
        :param CommonParams: 普通参数序号数组
注意：此字段可能返回 null，表示取不到有效值。
        :type CommonParams: list of int non-negative
        :param UrlParams: 链接参数序号数组
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlParams: list of int non-negative
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.StatusInfo = None
        self.AppSubId = None
        self.Title = None
        self.Sign = None
        self.Contents = None
        self.CreatedAt = None
        self.Urls = None
        self.PhoneType = None
        self.CommonParams = None
        self.UrlParams = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        if params.get("StatusInfo") is not None:
            self.StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = MmsInstanceStateInfo()
                obj._deserialize(item)
                self.StatusInfo.append(obj)
        self.AppSubId = params.get("AppSubId")
        self.Title = params.get("Title")
        self.Sign = params.get("Sign")
        self.Contents = params.get("Contents")
        self.CreatedAt = params.get("CreatedAt")
        self.Urls = params.get("Urls")
        self.PhoneType = params.get("PhoneType")
        self.CommonParams = params.get("CommonParams")
        self.UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MmsInstanceInfoList(AbstractModel):
    """彩信实例状态列表

    """

    def __init__(self):
        """
        :param Total: 总数据量
        :type Total: int
        :param List: 彩信实例状态信息列表
        :type List: list of MmsInstanceInfo
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = MmsInstanceInfo()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MmsInstanceStateInfo(AbstractModel):
    """彩信实例审核状态

    """

    def __init__(self):
        """
        :param Operator: 运营商
        :type Operator: str
        :param State: 审核状态：0未审核，1审核通过，2审核拒绝
        :type State: int
        """
        self.Operator = None
        self.State = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySmsTemplateDataStruct(AbstractModel):
    """短信模板编辑接口出参

    """

    def __init__(self):
        """
        :param TemplateId: 短信模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySmsTemplateRequest(AbstractModel):
    """ModifySmsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param TemplateId: 短信模板id
        :type TemplateId: int
        :param SignID: 短信签名，创建签名时返回
        :type SignID: int
        :param TemplateName: 模板名称
        :type TemplateName: str
        :param TemplateContent: 短信内容，动态内容使用占位符{1}，{2}等表示
        :type TemplateContent: str
        :param SmsType: 短信类型：{0:普通短信，1:营销短信}
        :type SmsType: int
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param Remark: 短信模板标签
        :type Remark: str
        :param Urls: 发送短信活动时配置的落地链接地址,仅用作短信活动
        :type Urls: list of str
        :param CommonParams: 发送短信活动时用于展示人群包动态参数模板占位符序号,仅用作短信活动
        :type CommonParams: list of int
        :param UrlParams: 发送短信活动时用于展示短连接模板占位符序号,仅用作短信活动
        :type UrlParams: list of int
        """
        self.License = None
        self.TemplateId = None
        self.SignID = None
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None
        self.Urls = None
        self.CommonParams = None
        self.UrlParams = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.TemplateId = params.get("TemplateId")
        self.SignID = params.get("SignID")
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")
        self.Urls = params.get("Urls")
        self.CommonParams = params.get("CommonParams")
        self.UrlParams = params.get("UrlParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 返回
        :type Data: :class:`tencentcloud.zj.v20190121.models.ModifySmsTemplateDataStruct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ModifySmsTemplateDataStruct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PaasCreateSignResp(AbstractModel):
    """创建签名返回结构

    """

    def __init__(self):
        """
        :param SignId: 签名id
        :type SignId: int
        """
        self.SignId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PaasSmsCampaignStatusResp(AbstractModel):
    """拉取活动状态返回

    """

    def __init__(self):
        """
        :param Status: 0-未发送 1-发送中 2-发送结束 3-发送取消
        :type Status: int
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PaasStrategy(AbstractModel):
    """短信发送人群包策略

    """

    def __init__(self):
        """
        :param CrowdID: 人群包id
        :type CrowdID: int
        :param Items: 待选素材数组
        :type Items: list of PaasStrategyItem
        """
        self.CrowdID = None
        self.Items = None


    def _deserialize(self, params):
        self.CrowdID = params.get("CrowdID")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = PaasStrategyItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PaasStrategyItem(AbstractModel):
    """短信活动策略元素

    """

    def __init__(self):
        """
        :param Id: 短信模板id或超级短信样例id
        :type Id: int
        :param ContentType: 素材类型 0-普短 1-超短
        :type ContentType: int
        """
        self.Id = None
        self.ContentType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushMmsContentRequest(AbstractModel):
    """PushMmsContent请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param InstanceId: 素材样例id
        :type InstanceId: int
        :param Tel: 手机号
        :type Tel: str
        :param Session: 附带数据字段
        :type Session: str
        :param DynamicParaKey: 动态参数key(即申请样例时设置的u_或p_开头的动态参数,要求序号有序)
        :type DynamicParaKey: list of str
        :param DynamicParaValue: 动态参数值,和DynamicParaKey对应
        :type DynamicParaValue: list of str
        """
        self.License = None
        self.InstanceId = None
        self.Tel = None
        self.Session = None
        self.DynamicParaKey = None
        self.DynamicParaValue = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.InstanceId = params.get("InstanceId")
        self.Tel = params.get("Tel")
        self.Session = params.get("Session")
        self.DynamicParaKey = params.get("DynamicParaKey")
        self.DynamicParaValue = params.get("DynamicParaValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushMmsContentResp(AbstractModel):
    """发送超级短信返回

    """

    def __init__(self):
        """
        :param ReturnCode: 返回码：0-成功 其它-失败
        :type ReturnCode: int
        :param ReturnMsg: 返回信息
        :type ReturnMsg: str
        :param MessageId: 消息回执id
        :type MessageId: int
        """
        self.ReturnCode = None
        self.ReturnMsg = None
        self.MessageId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")
        self.MessageId = params.get("MessageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushMmsContentResponse(AbstractModel):
    """PushMmsContent返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 推送短信返回信息
        :type Data: :class:`tencentcloud.zj.v20190121.models.PushMmsContentResp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = PushMmsContentResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendSmsPaasDataStruct(AbstractModel):
    """发送短信返回

    """

    def __init__(self):
        """
        :param SerialNo: 发送流水号
        :type SerialNo: str
        :param PhoneNumber: 手机号码,e.164标准，+[国家或地区码][手机号] ，示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type PhoneNumber: str
        :param Fee: 计费条数
        :type Fee: int
        :param Code: OK为成功
        :type Code: str
        :param Message: 短信请求错误码描述
        :type Message: str
        """
        self.SerialNo = None
        self.PhoneNumber = None
        self.Fee = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.SerialNo = params.get("SerialNo")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Fee = params.get("Fee")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendSmsRequest(AbstractModel):
    """SendSms请求参数结构体

    """

    def __init__(self):
        """
        :param License: 商户证书
        :type License: str
        :param Phone: 手机号码,采用 e.164 标准，格式为+[国家或地区码][手机号]，单次请求最多支持200个手机号且要求全为境内手机号,如:+8613800138000
        :type Phone: list of str
        :param TemplateId: 短信模板id(推荐使用模板id发送,使用内容发送时模板id留空)
        :type TemplateId: str
        :param Params: 模板参数，若无模板参数，则设置为空。
        :type Params: list of str
        :param Sign: 短信签名内容，使用 UTF-8 编码，必须填写已审核通过的签名。注：国内短信为必填参数。
        :type Sign: str
        :param SenderId: 国际/港澳台短信 senderid，国内短信填空
        :type SenderId: str
        :param SmsType: 短信类型：{0:普通短信，1:营销短信}，使用内容发送时必填
        :type SmsType: int
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。使用内容发送时必填
        :type International: int
        :param Content: 发送使用的模板内容,如果有占位符,此处也包括占位符,占位符的实际内容通过Params参数传递,使用模板id发送时此字段为空
        :type Content: str
        """
        self.License = None
        self.Phone = None
        self.TemplateId = None
        self.Params = None
        self.Sign = None
        self.SenderId = None
        self.SmsType = None
        self.International = None
        self.Content = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.Phone = params.get("Phone")
        self.TemplateId = params.get("TemplateId")
        self.Params = params.get("Params")
        self.Sign = params.get("Sign")
        self.SenderId = params.get("SenderId")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SendSmsResponse(AbstractModel):
    """SendSms返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 出参数据
        :type Data: list of SendSmsPaasDataStruct
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SendSmsPaasDataStruct()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsAddCrowdPackInfoResponse(AbstractModel):
    """添加短信人群包信息接口返回

    """

    def __init__(self):
        """
        :param ID: 人群包id
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsAmountDataStruct(AbstractModel):
    """短信子账号额度接口出参

    """

    def __init__(self):
        """
        :param SmsCampaignAmount: 短信活动配额
        :type SmsCampaignAmount: int
        :param SmsCampaignConsume: 短信活动消耗配额
        :type SmsCampaignConsume: int
        :param SmsSendAmount: 短信发送额度
        :type SmsSendAmount: int
        :param SmsSendConsume: 短信发送消耗额度
        :type SmsSendConsume: int
        :param MmsCampaignAmount: 超短活动额度
        :type MmsCampaignAmount: int
        :param MmsCampaignConsume: 超短活动消耗额度
        :type MmsCampaignConsume: int
        :param MmsSendAmount: 超短短信额度
        :type MmsSendAmount: int
        :param MmsSendConsume: 超短短信消耗额度
        :type MmsSendConsume: int
        """
        self.SmsCampaignAmount = None
        self.SmsCampaignConsume = None
        self.SmsSendAmount = None
        self.SmsSendConsume = None
        self.MmsCampaignAmount = None
        self.MmsCampaignConsume = None
        self.MmsSendAmount = None
        self.MmsSendConsume = None


    def _deserialize(self, params):
        self.SmsCampaignAmount = params.get("SmsCampaignAmount")
        self.SmsCampaignConsume = params.get("SmsCampaignConsume")
        self.SmsSendAmount = params.get("SmsSendAmount")
        self.SmsSendConsume = params.get("SmsSendConsume")
        self.MmsCampaignAmount = params.get("MmsCampaignAmount")
        self.MmsCampaignConsume = params.get("MmsCampaignConsume")
        self.MmsSendAmount = params.get("MmsSendAmount")
        self.MmsSendConsume = params.get("MmsSendConsume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsCampaignStatisticsCrowdData(AbstractModel):
    """短信活动统计人群包数据

    """

    def __init__(self):
        """
        :param CrowdId: 人群包id
        :type CrowdId: int
        :param CrowdName: 人群包名称
        :type CrowdName: str
        :param CrowdCount: 人群包目标触达总数
        :type CrowdCount: int
        :param TemplateList: 模板列表
        :type TemplateList: list of SmsCampaignStatisticsTemplateData
        """
        self.CrowdId = None
        self.CrowdName = None
        self.CrowdCount = None
        self.TemplateList = None


    def _deserialize(self, params):
        self.CrowdId = params.get("CrowdId")
        self.CrowdName = params.get("CrowdName")
        self.CrowdCount = params.get("CrowdCount")
        if params.get("TemplateList") is not None:
            self.TemplateList = []
            for item in params.get("TemplateList"):
                obj = SmsCampaignStatisticsTemplateData()
                obj._deserialize(item)
                self.TemplateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsCampaignStatisticsData(AbstractModel):
    """短信活动统计响应

    """

    def __init__(self):
        """
        :param CampaignId: 活动Id
        :type CampaignId: int
        :param Statistics: 统计数据
        :type Statistics: list of SmsCampaignStatisticsCrowdData
        """
        self.CampaignId = None
        self.Statistics = None


    def _deserialize(self, params):
        self.CampaignId = params.get("CampaignId")
        if params.get("Statistics") is not None:
            self.Statistics = []
            for item in params.get("Statistics"):
                obj = SmsCampaignStatisticsCrowdData()
                obj._deserialize(item)
                self.Statistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsCampaignStatisticsTemplateData(AbstractModel):
    """短信活动统计模板展示结构

    """

    def __init__(self):
        """
        :param TemplateId: 模板或样例id
        :type TemplateId: str
        :param TemplateContent: 模板内容
        :type TemplateContent: str
        :param SendCount: 触达成功数
        :type SendCount: int
        :param ClickCount: 短链点击数
        :type ClickCount: int
        """
        self.TemplateId = None
        self.TemplateContent = None
        self.SendCount = None
        self.ClickCount = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateContent = params.get("TemplateContent")
        self.SendCount = params.get("SendCount")
        self.ClickCount = params.get("ClickCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsCreateCampaignResponse(AbstractModel):
    """创建短信活动返回结构

    """

    def __init__(self):
        """
        :param CampaignId: 活动id
        :type CampaignId: int
        """
        self.CampaignId = None


    def _deserialize(self, params):
        self.CampaignId = params.get("CampaignId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsGetCrowdPackList(AbstractModel):
    """短信获取人群包列表的返回数据信息

    """

    def __init__(self):
        """
        :param CreatedAt: 创建时间
        :type CreatedAt: str
        :param ID: 人群包id
        :type ID: int
        :param Name: 人群包名称
        :type Name: str
        :param Status: 人群包状态
        :type Status: int
        :param PhoneNum: 人群包手机号数量
        :type PhoneNum: int
        :param Tag: 人群包标签信息
        :type Tag: str
        :param MD5: 人群包md5
        :type MD5: str
        :param FileName: 人群包文件名称
        :type FileName: str
        :param Desc: 人群包描述
        :type Desc: str
        """
        self.CreatedAt = None
        self.ID = None
        self.Name = None
        self.Status = None
        self.PhoneNum = None
        self.Tag = None
        self.MD5 = None
        self.FileName = None
        self.Desc = None


    def _deserialize(self, params):
        self.CreatedAt = params.get("CreatedAt")
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.PhoneNum = params.get("PhoneNum")
        self.Tag = params.get("Tag")
        self.MD5 = params.get("MD5")
        self.FileName = params.get("FileName")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsGetCrowdPackListResponse(AbstractModel):
    """短信人群包返回信息

    """

    def __init__(self):
        """
        :param Total: 人群包总数
        :type Total: int
        :param List: 人群包返回数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of SmsGetCrowdPackList
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SmsGetCrowdPackList()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsGetCrowdUploadInfoResponse(AbstractModel):
    """获取短信人群包上传信息返回

    """

    def __init__(self):
        """
        :param ExpiredTime: 过期时间
        :type ExpiredTime: int
        :param SessionToken: 会话token
        :type SessionToken: str
        :param TmpSecretId: 临时密钥id
        :type TmpSecretId: str
        :param TmpSecretKey: 临时密钥
        :type TmpSecretKey: str
        :param CosInfo: cos信息
        :type CosInfo: :class:`tencentcloud.zj.v20190121.models.UploadFansInfoCosInfo`
        """
        self.ExpiredTime = None
        self.SessionToken = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.CosInfo = None


    def _deserialize(self, params):
        self.ExpiredTime = params.get("ExpiredTime")
        self.SessionToken = params.get("SessionToken")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        if params.get("CosInfo") is not None:
            self.CosInfo = UploadFansInfoCosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SmsSuccessResponse(AbstractModel):
    """短信api成功返回信息

    """

    def __init__(self):
        """
        :param Message: 成功返回信息
        :type Message: str
        """
        self.Message = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UploadFansInfoCosInfo(AbstractModel):
    """接口返回给服务商的COS路径等信息

    """

    def __init__(self):
        """
        :param Bucket: COS bucket
        :type Bucket: str
        :param Key: COS路径
        :type Key: str
        :param Region: COS区域
        :type Region: str
        """
        self.Bucket = None
        self.Key = None
        self.Region = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Key = params.get("Key")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        