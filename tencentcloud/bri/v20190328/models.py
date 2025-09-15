# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class BRIRequest(AbstractModel):
    r"""BRI请求

    """

    def __init__(self):
        r"""
        :param _Service: 业务名, 必须是以下六个业务名之一(bri_num,bri_dev,bri_ip_bri_apk,bri_url,bri_social)
        :type Service: str
        :param _QQ: QQ号 (业务名为bri_social时必填, 除非已填Wechat)
        :type QQ: str
        :param _QQTag: QQ号的可疑标签
        :type QQTag: str
        :param _Url: 网址 (业务名为bri_url时必填)
        :type Url: str
        :param _CertMd5: Apk证书Md5  (业务名为bri_apk时必填，除非已填FileMd5)
        :type CertMd5: str
        :param _PackageName: Apk安装包名 (业务名为bri_apk时必填，除非已填FileMd5)
        :type PackageName: str
        :param _FileMd5: Apk文件Md5 (业务名为bri_apk时必填，除非已填PackageName,CertMd5,FileSize)
        :type FileMd5: str
        :param _Scene: 业务场景 (1-注册, 2-登录, 3-发消息)
        :type Scene: str
        :param _PhoneNumber: 电话号码 (业务名为bri_num时必填)
        :type PhoneNumber: str
        :param _FileSize: Apk文件大小  (业务名为bri_apk时必填，除非已填FileMd5)
        :type FileSize: int
        :param _Ip: 点分格式的IP (业务名为bri_ip时必填)
        :type Ip: str
        :param _Imei: 安卓设备的Imei (业务名为bri_dev时必填)
        :type Imei: str
        :param _Wechat: 微信号 (业务名为bri_social时必填, 除非已填QQ)
        :type Wechat: str
        :param _WechatTag: 微信号的可疑标签
        :type WechatTag: str
        :param _SubAppid: 子客户ID
        :type SubAppid: str
        """
        self._Service = None
        self._QQ = None
        self._QQTag = None
        self._Url = None
        self._CertMd5 = None
        self._PackageName = None
        self._FileMd5 = None
        self._Scene = None
        self._PhoneNumber = None
        self._FileSize = None
        self._Ip = None
        self._Imei = None
        self._Wechat = None
        self._WechatTag = None
        self._SubAppid = None

    @property
    def Service(self):
        r"""业务名, 必须是以下六个业务名之一(bri_num,bri_dev,bri_ip_bri_apk,bri_url,bri_social)
        :rtype: str
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def QQ(self):
        r"""QQ号 (业务名为bri_social时必填, 除非已填Wechat)
        :rtype: str
        """
        return self._QQ

    @QQ.setter
    def QQ(self, QQ):
        self._QQ = QQ

    @property
    def QQTag(self):
        r"""QQ号的可疑标签
        :rtype: str
        """
        return self._QQTag

    @QQTag.setter
    def QQTag(self, QQTag):
        self._QQTag = QQTag

    @property
    def Url(self):
        r"""网址 (业务名为bri_url时必填)
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def CertMd5(self):
        r"""Apk证书Md5  (业务名为bri_apk时必填，除非已填FileMd5)
        :rtype: str
        """
        return self._CertMd5

    @CertMd5.setter
    def CertMd5(self, CertMd5):
        self._CertMd5 = CertMd5

    @property
    def PackageName(self):
        r"""Apk安装包名 (业务名为bri_apk时必填，除非已填FileMd5)
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def FileMd5(self):
        r"""Apk文件Md5 (业务名为bri_apk时必填，除非已填PackageName,CertMd5,FileSize)
        :rtype: str
        """
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def Scene(self):
        r"""业务场景 (1-注册, 2-登录, 3-发消息)
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def PhoneNumber(self):
        r"""电话号码 (业务名为bri_num时必填)
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def FileSize(self):
        r"""Apk文件大小  (业务名为bri_apk时必填，除非已填FileMd5)
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Ip(self):
        r"""点分格式的IP (业务名为bri_ip时必填)
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Imei(self):
        r"""安卓设备的Imei (业务名为bri_dev时必填)
        :rtype: str
        """
        return self._Imei

    @Imei.setter
    def Imei(self, Imei):
        self._Imei = Imei

    @property
    def Wechat(self):
        r"""微信号 (业务名为bri_social时必填, 除非已填QQ)
        :rtype: str
        """
        return self._Wechat

    @Wechat.setter
    def Wechat(self, Wechat):
        self._Wechat = Wechat

    @property
    def WechatTag(self):
        r"""微信号的可疑标签
        :rtype: str
        """
        return self._WechatTag

    @WechatTag.setter
    def WechatTag(self, WechatTag):
        self._WechatTag = WechatTag

    @property
    def SubAppid(self):
        r"""子客户ID
        :rtype: str
        """
        return self._SubAppid

    @SubAppid.setter
    def SubAppid(self, SubAppid):
        self._SubAppid = SubAppid


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._QQ = params.get("QQ")
        self._QQTag = params.get("QQTag")
        self._Url = params.get("Url")
        self._CertMd5 = params.get("CertMd5")
        self._PackageName = params.get("PackageName")
        self._FileMd5 = params.get("FileMd5")
        self._Scene = params.get("Scene")
        self._PhoneNumber = params.get("PhoneNumber")
        self._FileSize = params.get("FileSize")
        self._Ip = params.get("Ip")
        self._Imei = params.get("Imei")
        self._Wechat = params.get("Wechat")
        self._WechatTag = params.get("WechatTag")
        self._SubAppid = params.get("SubAppid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BRIResponse(AbstractModel):
    r"""响应

    """

    def __init__(self):
        r"""
        :param _Score: 风险分值，取值[0,100], 分值越高风险越高
        :type Score: float
        :param _Tags: 当Service为bri_num时,返回的风险标签有:
1) 疑似垃圾流量     说明: 结合号码的历史数据表现，判断该号码历史用互联网业务作恶行为，其产生的互联网行为对于其他业务来说属于作弊或垃圾流量。 
2) 疑似新客户       说明: 通过号码互联网行为（社交，浏览等）是否异常判断为小号或接码平台帐号。 

当Service为bri_dev时,返回的风险标签有:
1) 疑似真机假用户    说明: 根据设备的一些数据表现，我们判定为群控设备
2) 疑似假机         说明: 根据设备的一些数据表现，我们判定为模拟器或虚假设备ID
3) 疑似真用户假行为  说明: 根据设备的用户使用情况，我们判定该用户存在使用脚本、外挂、病毒等作弊行为

当Service为bri_ip时,返回的风险标签有:
1) 疑似垃圾流量     说明:结合IP的历史数据表现，判断该IP历史用互联网业务作恶行为，其产生的互联网行为对于其他业务来说属于作弊或垃圾流量。

当Service为bri_url时,返回的风险标签有:
1) 社工欺诈    说明: URL为社工欺诈
2) 信息诈骗    说明: URL为信息诈骗
3) 虚假销售    说明: URL为虚假销售
4) 恶意文件    说明: URL为恶意文件
5) 博彩网站    说明: URL为博彩网站
6) 色情网站    说明: URL为色情网站

当Service为bri_apk时,返回的风险标签有:
1) 安全   说明: APK为正规应用
2) 一般   说明: APK为未发现问题的正常应用
3) 风险   说明: APK为外挂或色情等风险应用
4) 病毒   说明: APK为包含恶意代码的恶意软件,可能破坏系统或者其他app正常使用
        :type Tags: list of str
        """
        self._Score = None
        self._Tags = None

    @property
    def Score(self):
        r"""风险分值，取值[0,100], 分值越高风险越高
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Tags(self):
        r"""当Service为bri_num时,返回的风险标签有:
1) 疑似垃圾流量     说明: 结合号码的历史数据表现，判断该号码历史用互联网业务作恶行为，其产生的互联网行为对于其他业务来说属于作弊或垃圾流量。 
2) 疑似新客户       说明: 通过号码互联网行为（社交，浏览等）是否异常判断为小号或接码平台帐号。 

当Service为bri_dev时,返回的风险标签有:
1) 疑似真机假用户    说明: 根据设备的一些数据表现，我们判定为群控设备
2) 疑似假机         说明: 根据设备的一些数据表现，我们判定为模拟器或虚假设备ID
3) 疑似真用户假行为  说明: 根据设备的用户使用情况，我们判定该用户存在使用脚本、外挂、病毒等作弊行为

当Service为bri_ip时,返回的风险标签有:
1) 疑似垃圾流量     说明:结合IP的历史数据表现，判断该IP历史用互联网业务作恶行为，其产生的互联网行为对于其他业务来说属于作弊或垃圾流量。

当Service为bri_url时,返回的风险标签有:
1) 社工欺诈    说明: URL为社工欺诈
2) 信息诈骗    说明: URL为信息诈骗
3) 虚假销售    说明: URL为虚假销售
4) 恶意文件    说明: URL为恶意文件
5) 博彩网站    说明: URL为博彩网站
6) 色情网站    说明: URL为色情网站

当Service为bri_apk时,返回的风险标签有:
1) 安全   说明: APK为正规应用
2) 一般   说明: APK为未发现问题的正常应用
3) 风险   说明: APK为外挂或色情等风险应用
4) 病毒   说明: APK为包含恶意代码的恶意软件,可能破坏系统或者其他app正常使用
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBRIRequest(AbstractModel):
    r"""DescribeBRI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestData: 业务风险情报请求体
        :type RequestData: :class:`tencentcloud.bri.v20190328.models.BRIRequest`
        :param _ResourceId: 客户用于计费的资源ID
        :type ResourceId: str
        """
        self._RequestData = None
        self._ResourceId = None

    @property
    def RequestData(self):
        r"""业务风险情报请求体
        :rtype: :class:`tencentcloud.bri.v20190328.models.BRIRequest`
        """
        return self._RequestData

    @RequestData.setter
    def RequestData(self, RequestData):
        self._RequestData = RequestData

    @property
    def ResourceId(self):
        r"""客户用于计费的资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self._RequestData = BRIRequest()
            self._RequestData._deserialize(params.get("RequestData"))
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBRIResponse(AbstractModel):
    r"""DescribeBRI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResponseData: 业务风险情报响应体
        :type ResponseData: :class:`tencentcloud.bri.v20190328.models.BRIResponse`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResponseData = None
        self._RequestId = None

    @property
    def ResponseData(self):
        r"""业务风险情报响应体
        :rtype: :class:`tencentcloud.bri.v20190328.models.BRIResponse`
        """
        return self._ResponseData

    @ResponseData.setter
    def ResponseData(self, ResponseData):
        self._ResponseData = ResponseData

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self._ResponseData = BRIResponse()
            self._ResponseData._deserialize(params.get("ResponseData"))
        self._RequestId = params.get("RequestId")