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


class ApiGatewayInstanceDetail(AbstractModel):
    """apiGateway实例详情

    """

    def __init__(self):
        r"""
        :param _ServiceId: 实例ID
        :type ServiceId: str
        :param _ServiceName: 实例名称
        :type ServiceName: str
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _Protocol: 使用协议
        :type Protocol: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._Domain = None
        self._CertId = None
        self._Protocol = None

    @property
    def ServiceId(self):
        """实例ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        """实例名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Protocol(self):
        """使用协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiGatewayInstanceList(AbstractModel):
    """apigateway实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _InstanceList: apigateway实例详情	
        :type InstanceList: list of ApiGatewayInstanceDetail
        :param _TotalCount: 该地域下apigateway实例总数	
        :type TotalCount: int
        :param _Error: 是否查询异常
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """apigateway实例详情	
        :rtype: list of ApiGatewayInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """该地域下apigateway实例总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """是否查询异常
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ApiGatewayInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DvAuthMethod: 证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单为：64.78.193.238，216.168.247.9，216.168.249.9，54.189.196.217
        :type DvAuthMethod: str
        :param _DomainName: 证书绑定的域名。
        :type DomainName: str
        :param _ProjectId: 证书关联的项目 ID。 默认为0（默认项目）
        :type ProjectId: int
        :param _PackageType: 证书类型， 可不传，目前仅支持类型83。83 = TrustAsia C1 DV Free。
        :type PackageType: str
        :param _ContactEmail: 证书订单关联邮箱。默认为腾讯云账号邮箱， 不存在则关联固定邮箱
        :type ContactEmail: str
        :param _ContactPhone: 证书关联手机号码，  不存在则关联固定手机号码
        :type ContactPhone: str
        :param _ValidityPeriod: 证书有效期，默认3（月），目前仅支持3个月。
        :type ValidityPeriod: str
        :param _CsrEncryptAlgo: 加密算法，取值为ECC、RSA， 默认为RSA
        :type CsrEncryptAlgo: str
        :param _CsrKeyParameter: 密钥对参数，RSA仅支持2048。ECC仅支持prime256v1。加密算法选择ECC时，此参数必填
        :type CsrKeyParameter: str
        :param _CsrKeyPassword: 私钥密码， 目前仅使用在生成jks、pfx格式证书时密码； 其他格式私钥证书未加密
        :type CsrKeyPassword: str
        :param _Alias: 证书别名
        :type Alias: str
        :param _OldCertificateId: 旧证书 ID，用于证书续费（证书有效期在30天内，且未过期），会建立续费关系， 可用于托管； 不传则表示新申请证书
        :type OldCertificateId: str
        :param _PackageId: 权益包ID，用于免费证书扩容包使用， 免费证书扩容包已下线
        :type PackageId: str
        :param _DeleteDnsAutoRecord: 签发后是否删除自动域名验证记录， 默认为否；仅域名为DNS_AUTO验证类型支持传参
        :type DeleteDnsAutoRecord: bool
        :param _DnsNames: 证书绑定的其他域名，待开放。目前不支持此参数
        :type DnsNames: list of str
        """
        self._DvAuthMethod = None
        self._DomainName = None
        self._ProjectId = None
        self._PackageType = None
        self._ContactEmail = None
        self._ContactPhone = None
        self._ValidityPeriod = None
        self._CsrEncryptAlgo = None
        self._CsrKeyParameter = None
        self._CsrKeyPassword = None
        self._Alias = None
        self._OldCertificateId = None
        self._PackageId = None
        self._DeleteDnsAutoRecord = None
        self._DnsNames = None

    @property
    def DvAuthMethod(self):
        """证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单为：64.78.193.238，216.168.247.9，216.168.249.9，54.189.196.217
        :rtype: str
        """
        return self._DvAuthMethod

    @DvAuthMethod.setter
    def DvAuthMethod(self, DvAuthMethod):
        self._DvAuthMethod = DvAuthMethod

    @property
    def DomainName(self):
        """证书绑定的域名。
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def ProjectId(self):
        """证书关联的项目 ID。 默认为0（默认项目）
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PackageType(self):
        """证书类型， 可不传，目前仅支持类型83。83 = TrustAsia C1 DV Free。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ContactEmail(self):
        """证书订单关联邮箱。默认为腾讯云账号邮箱， 不存在则关联固定邮箱
        :rtype: str
        """
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPhone(self):
        """证书关联手机号码，  不存在则关联固定手机号码
        :rtype: str
        """
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def ValidityPeriod(self):
        """证书有效期，默认3（月），目前仅支持3个月。
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def CsrEncryptAlgo(self):
        """加密算法，取值为ECC、RSA， 默认为RSA
        :rtype: str
        """
        return self._CsrEncryptAlgo

    @CsrEncryptAlgo.setter
    def CsrEncryptAlgo(self, CsrEncryptAlgo):
        self._CsrEncryptAlgo = CsrEncryptAlgo

    @property
    def CsrKeyParameter(self):
        """密钥对参数，RSA仅支持2048。ECC仅支持prime256v1。加密算法选择ECC时，此参数必填
        :rtype: str
        """
        return self._CsrKeyParameter

    @CsrKeyParameter.setter
    def CsrKeyParameter(self, CsrKeyParameter):
        self._CsrKeyParameter = CsrKeyParameter

    @property
    def CsrKeyPassword(self):
        """私钥密码， 目前仅使用在生成jks、pfx格式证书时密码； 其他格式私钥证书未加密
        :rtype: str
        """
        return self._CsrKeyPassword

    @CsrKeyPassword.setter
    def CsrKeyPassword(self, CsrKeyPassword):
        self._CsrKeyPassword = CsrKeyPassword

    @property
    def Alias(self):
        """证书别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OldCertificateId(self):
        """旧证书 ID，用于证书续费（证书有效期在30天内，且未过期），会建立续费关系， 可用于托管； 不传则表示新申请证书
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def PackageId(self):
        """权益包ID，用于免费证书扩容包使用， 免费证书扩容包已下线
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def DeleteDnsAutoRecord(self):
        """签发后是否删除自动域名验证记录， 默认为否；仅域名为DNS_AUTO验证类型支持传参
        :rtype: bool
        """
        return self._DeleteDnsAutoRecord

    @DeleteDnsAutoRecord.setter
    def DeleteDnsAutoRecord(self, DeleteDnsAutoRecord):
        self._DeleteDnsAutoRecord = DeleteDnsAutoRecord

    @property
    def DnsNames(self):
        """证书绑定的其他域名，待开放。目前不支持此参数
        :rtype: list of str
        """
        return self._DnsNames

    @DnsNames.setter
    def DnsNames(self, DnsNames):
        self._DnsNames = DnsNames


    def _deserialize(self, params):
        self._DvAuthMethod = params.get("DvAuthMethod")
        self._DomainName = params.get("DomainName")
        self._ProjectId = params.get("ProjectId")
        self._PackageType = params.get("PackageType")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactPhone = params.get("ContactPhone")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self._CsrKeyParameter = params.get("CsrKeyParameter")
        self._CsrKeyPassword = params.get("CsrKeyPassword")
        self._Alias = params.get("Alias")
        self._OldCertificateId = params.get("OldCertificateId")
        self._PackageId = params.get("PackageId")
        self._DeleteDnsAutoRecord = params.get("DeleteDnsAutoRecord")
        self._DnsNames = params.get("DnsNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateResponse(AbstractModel):
    """ApplyCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 新申请成功的证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """新申请成功的证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class BatchDeleteFail(AbstractModel):
    """批量删除失败的项

    """

    def __init__(self):
        r"""
        :param _CertId: 失败的证书ID
        :type CertId: str
        :param _Msg: 失败的原因
        :type Msg: str
        """
        self._CertId = None
        self._Msg = None

    @property
    def CertId(self):
        """失败的证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Msg(self):
        """失败的原因
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._Msg = params.get("Msg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindResourceRegionResult(AbstractModel):
    """绑定资源地域结果

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _TotalCount: 关联资源总数
        :type TotalCount: int
        :param _Error: 是否查询异常
        :type Error: str
        """
        self._Region = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TotalCount(self):
        """关联资源总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """是否查询异常
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindResourceResult(AbstractModel):
    """绑定资源结果

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）
        :type ResourceType: str
        :param _BindResourceRegionResult: 绑定资源地域结果
        :type BindResourceRegionResult: list of BindResourceRegionResult
        """
        self._ResourceType = None
        self._BindResourceRegionResult = None

    @property
    def ResourceType(self):
        """资源类型：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def BindResourceRegionResult(self):
        """绑定资源地域结果
        :rtype: list of BindResourceRegionResult
        """
        return self._BindResourceRegionResult

    @BindResourceRegionResult.setter
    def BindResourceRegionResult(self, BindResourceRegionResult):
        self._BindResourceRegionResult = BindResourceRegionResult


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("BindResourceRegionResult") is not None:
            self._BindResourceRegionResult = []
            for item in params.get("BindResourceRegionResult"):
                obj = BindResourceRegionResult()
                obj._deserialize(item)
                self._BindResourceRegionResult.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class COSInstanceList(AbstractModel):
    """cos实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _InstanceList: 实例详情
        :type InstanceList: list of CosInstanceDetail
        :param _TotalCount: 地域下总数
        :type TotalCount: int
        :param _Error: 错误信息
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """实例详情
        :rtype: list of CosInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """地域下总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """错误信息
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuditCertificateRequest(AbstractModel):
    """CancelAuditCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAuditCertificateResponse(AbstractModel):
    """CancelAuditCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """操作是否成功
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCertificateOrderResponse(AbstractModel):
    """CancelCertificateOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 取消订单成功的证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """取消订单成功的证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CdnInstanceDetail(AbstractModel):
    """CDN实例详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 已部署证书ID
        :type CertId: str
        :param _Status: 域名状态 rejected：域名审核未通过，域名备案过期/被注销导致，processing：部署中，online：已启动，offline：已关闭
        :type Status: str
        :param _HttpsBillingSwitch: 域名计费状态，on表示开启，off表示关闭。
        :type HttpsBillingSwitch: str
        """
        self._Domain = None
        self._CertId = None
        self._Status = None
        self._HttpsBillingSwitch = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """已部署证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """域名状态 rejected：域名审核未通过，域名备案过期/被注销导致，processing：部署中，online：已启动，offline：已关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def HttpsBillingSwitch(self):
        """域名计费状态，on表示开启，off表示关闭。
        :rtype: str
        """
        return self._HttpsBillingSwitch

    @HttpsBillingSwitch.setter
    def HttpsBillingSwitch(self, HttpsBillingSwitch):
        self._HttpsBillingSwitch = HttpsBillingSwitch


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        self._HttpsBillingSwitch = params.get("HttpsBillingSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnInstanceList(AbstractModel):
    """cdn实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该地域下CDN域名总数	
        :type TotalCount: int
        :param _InstanceList: cdn域名详情	
        :type InstanceList: list of CdnInstanceDetail
        :param _Error: 是否查询异常
        :type Error: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._Error = None

    @property
    def TotalCount(self):
        """该地域下CDN域名总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """cdn域名详情	
        :rtype: list of CdnInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def Error(self):
        """是否查询异常
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CdnInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertBasicInfo(AbstractModel):
    """证书基本信息

    """

    def __init__(self):
        r"""
        :param _Issuer: 颁发者
        :type Issuer: str
        :param _Subject: 颁发给
        :type Subject: str
        :param _Fingerprint: 证书指纹
        :type Fingerprint: str
        :param _ValidFrom: 证书有效期开始时间
        :type ValidFrom: str
        :param _ValidTo: 证书有效期结束时间
        :type ValidTo: str
        """
        self._Issuer = None
        self._Subject = None
        self._Fingerprint = None
        self._ValidFrom = None
        self._ValidTo = None

    @property
    def Issuer(self):
        """颁发者
        :rtype: str
        """
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Subject(self):
        """颁发给
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def Fingerprint(self):
        """证书指纹
        :rtype: str
        """
        return self._Fingerprint

    @Fingerprint.setter
    def Fingerprint(self, Fingerprint):
        self._Fingerprint = Fingerprint

    @property
    def ValidFrom(self):
        """证书有效期开始时间
        :rtype: str
        """
        return self._ValidFrom

    @ValidFrom.setter
    def ValidFrom(self, ValidFrom):
        self._ValidFrom = ValidFrom

    @property
    def ValidTo(self):
        """证书有效期结束时间
        :rtype: str
        """
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo


    def _deserialize(self, params):
        self._Issuer = params.get("Issuer")
        self._Subject = params.get("Subject")
        self._Fingerprint = params.get("Fingerprint")
        self._ValidFrom = params.get("ValidFrom")
        self._ValidTo = params.get("ValidTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertTaskId(AbstractModel):
    """证书异步任务ID

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID
        :type CertId: str
        :param _TaskId: 异步任务ID
        :type TaskId: str
        """
        self._CertId = None
        self._TaskId = None

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def TaskId(self):
        """异步任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificate(AbstractModel):
    """CLB证书详情

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID
        :type CertId: str
        :param _DnsNames: 证书绑定的域名
        :type DnsNames: list of str
        :param _CertCaId: 根证书ID
        :type CertCaId: str
        :param _SSLMode: 证书认证模式：UNIDIRECTIONAL单向认证，MUTUAL双向认证
        :type SSLMode: str
        """
        self._CertId = None
        self._DnsNames = None
        self._CertCaId = None
        self._SSLMode = None

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DnsNames(self):
        """证书绑定的域名
        :rtype: list of str
        """
        return self._DnsNames

    @DnsNames.setter
    def DnsNames(self, DnsNames):
        self._DnsNames = DnsNames

    @property
    def CertCaId(self):
        """根证书ID
        :rtype: str
        """
        return self._CertCaId

    @CertCaId.setter
    def CertCaId(self, CertCaId):
        self._CertCaId = CertCaId

    @property
    def SSLMode(self):
        """证书认证模式：UNIDIRECTIONAL单向认证，MUTUAL双向认证
        :rtype: str
        """
        return self._SSLMode

    @SSLMode.setter
    def SSLMode(self, SSLMode):
        self._SSLMode = SSLMode


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._DnsNames = params.get("DnsNames")
        self._CertCaId = params.get("CertCaId")
        self._SSLMode = params.get("SSLMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateExtra(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 数组下，key为CertificateExtra 的内容。

    """

    def __init__(self):
        r"""
        :param _DomainNumber: 证书可配置域名数量。
        :type DomainNumber: str
        :param _OriginCertificateId: 续费原证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCertificateId: str
        :param _ReplacedBy: 重颁发证书原始 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedBy: str
        :param _ReplacedFor: 重颁发证书ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedFor: str
        :param _RenewOrder: 续费证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewOrder: str
        :param _SMCert: 是否是国密证书
        :type SMCert: int
        :param _CompanyType: 公司类型，取值：1（个人）；2（公司）
        :type CompanyType: int
        """
        self._DomainNumber = None
        self._OriginCertificateId = None
        self._ReplacedBy = None
        self._ReplacedFor = None
        self._RenewOrder = None
        self._SMCert = None
        self._CompanyType = None

    @property
    def DomainNumber(self):
        """证书可配置域名数量。
        :rtype: str
        """
        return self._DomainNumber

    @DomainNumber.setter
    def DomainNumber(self, DomainNumber):
        self._DomainNumber = DomainNumber

    @property
    def OriginCertificateId(self):
        """续费原证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginCertificateId

    @OriginCertificateId.setter
    def OriginCertificateId(self, OriginCertificateId):
        self._OriginCertificateId = OriginCertificateId

    @property
    def ReplacedBy(self):
        """重颁发证书原始 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReplacedBy

    @ReplacedBy.setter
    def ReplacedBy(self, ReplacedBy):
        self._ReplacedBy = ReplacedBy

    @property
    def ReplacedFor(self):
        """重颁发证书ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReplacedFor

    @ReplacedFor.setter
    def ReplacedFor(self, ReplacedFor):
        self._ReplacedFor = ReplacedFor

    @property
    def RenewOrder(self):
        """续费证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RenewOrder

    @RenewOrder.setter
    def RenewOrder(self, RenewOrder):
        self._RenewOrder = RenewOrder

    @property
    def SMCert(self):
        """是否是国密证书
        :rtype: int
        """
        return self._SMCert

    @SMCert.setter
    def SMCert(self, SMCert):
        self._SMCert = SMCert

    @property
    def CompanyType(self):
        """公司类型，取值：1（个人）；2（公司）
        :rtype: int
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType


    def _deserialize(self, params):
        self._DomainNumber = params.get("DomainNumber")
        self._OriginCertificateId = params.get("OriginCertificateId")
        self._ReplacedBy = params.get("ReplacedBy")
        self._ReplacedFor = params.get("ReplacedFor")
        self._RenewOrder = params.get("RenewOrder")
        self._SMCert = params.get("SMCert")
        self._CompanyType = params.get("CompanyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfoSubmitRequest(AbstractModel):
    """CertificateInfoSubmit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: 待提交资料的付费证书 ID。	
        :type CertId: str
        :param _GenCsrType: 此字段必传。 CSR 生成方式， 取值为：
- online：腾讯云提交的填写的参数信息生成CSR和私钥，并由腾讯云加密存储
- parse：自行生成CSR和私钥，并通过上传CSR申请证书
        :type GenCsrType: str
        :param _CertCommonName: 证书绑定的通用名称， 若是上传的CSR，则该域名需与CSR解析的通用名称一致
        :type CertCommonName: str
        :param _CompanyType: 组织信息类型， 取值范围：
1（个人）：仅DV类型证书可设置为1， 个人类型证书组织信息字段可不传：Org开头，Admin开头，Tech开头
2（公司）：所有类型证书都可设置为2， 按需传组织信息字段
        :type CompanyType: int
        :param _CompanyId: 公司ID，在 [腾讯云控制台](https://console.cloud.tencent.com/ssl/info) 可进行查看，若无满足的公司信息， 则本参数传0 ； 若存在满足当前订单的公司信息， 可以根据 [DescribeCompanies](https://cloud.tencent.com/document/product/400/90375) 查看公司ID； 若传了公司ID，则Org开头的参数可不传


        :type CompanyId: str
        :param _OrgIdType: 公司证件类型，取值范围：
TYDMZ（统一社会信用代码 ）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
OTHERS（其他）
        :type OrgIdType: str
        :param _OrgIdNumber: 公司证件号码，取值范围：
TYDMZ（统一社会信用代码 ）：11532xxxxxxxx24820

        :type OrgIdNumber: str
        :param _AdminIdType: 管理人证件类型，取值范围：
SFZ（身份证）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
HZ（护照）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
        :type AdminIdType: str
        :param _AdminIdNumber: 管理人证件号码，仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段， 取值范围：
SFZ（身份证）：110000xxxxxxxx1242
HZ（护照）:EFxxxxxxx
        :type AdminIdNumber: str
        :param _TechIdType: 联系人证件类型，取值范围：
SFZ（身份证）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
HZ（护照）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
        :type TechIdType: str
        :param _TechIdNumber: 联系人证件号码，仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段，取值范围：
SFZ（身份证）：110000xxxxxxxx1242
HZ（护照）:EFxxxxxxx
        :type TechIdNumber: str
        :param _Csr: 上传的 CSR 内容。
若GenCsrType为parse， 则此字段必传。
        :type Csr: str
        :param _DnsNames: 证书绑定的其他域名， 单域名、泛域名证书无需提供。 多域名、多泛域名必填
        :type DnsNames: list of str
        :param _KeyPass: 私钥密码， 目前仅使用在生成jks、pfx格式证书时密码； 其他格式私钥证书未加密	
        :type KeyPass: str
        :param _OrgOrganization: 公司名称。若没有传CompanyId或者ManagerId， 则此字段必传
        :type OrgOrganization: str
        :param _OrgDivision: 部门名称。若没有传CompanyId或者ManagerId， 则此字段必传
        :type OrgDivision: str
        :param _OrgAddress: 公司详细地址。若没有传CompanyId或者ManagerId， 则此字段必传
        :type OrgAddress: str
        :param _OrgCountry: 国家名称，如中国：CN 。若没有传CompanyId或者ManagerId， 则此字段必传
        :type OrgCountry: str
        :param _OrgCity: 公司所在城市。若没有传CompanyId或者ManagerId， 则此字段必传
        :type OrgCity: str
        :param _OrgRegion: 公司所在省份。若没有传CompanyId或者ManagerId， 则此字段必传
        :type OrgRegion: str
        :param _OrgPhoneArea: 公司所属区号。若没有传CompanyId或者ManagerId， 则此字段必传
如：021。  手机号码传 86
        :type OrgPhoneArea: str
        :param _OrgPhoneNumber: 公司所属号码。若没有传CompanyId或者ManagerId， 则此字段必传
        :type OrgPhoneNumber: str
        :param _VerifyType: 证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单为：64.78.193.238，216.168.247.9，216.168.249.9，54.189.196.217
        :type VerifyType: str
        :param _AdminFirstName: 管理人名。若没有传ManagerId， 则此字段必传
        :type AdminFirstName: str
        :param _AdminLastName: 管理人姓。若没有传ManagerId， 则此字段必传
        :type AdminLastName: str
        :param _AdminPhone: 管理人手机号码。若没有传ManagerId， 则此字段必传
        :type AdminPhone: str
        :param _AdminEmail: 管理人邮箱地址。若没有传ManagerId， 则此字段必传
        :type AdminEmail: str
        :param _AdminTitle: 管理人职位。若没有传ManagerId， 则此字段必传
        :type AdminTitle: str
        :param _TechFirstName: 联系人名。若没有传ManagerId， 则此字段必传
        :type TechFirstName: str
        :param _TechLastName: 联系人姓。若没有传ManagerId， 则此字段必传
        :type TechLastName: str
        :param _ContactEmail: 联系人邮箱地址。CompanyType为1时， 此字段必传
        :type ContactEmail: str
        :param _AutoRenewFlag: 是否开启自动续费： 0， 不开启；  1， 开启； 默认为0
        :type AutoRenewFlag: int
        :param _CsrKeyParameter: 密钥对参数，RSA支持2048，4096。ECC仅支持prime256v1。加密算法选择ECC时，此参数必填
国密证书类型本字段不用传
        :type CsrKeyParameter: str
        :param _CsrEncryptAlgo: 加密算法，取值为ECC、RSA， 默认为RSA
国密证书类型本字段不用传
        :type CsrEncryptAlgo: str
        :param _ManagerId: 管理人ID，在 [腾讯云控制台](https://console.cloud.tencent.com/ssl/info) 可进行查看，若无满足的管理人信息， 则本参数传0 ； 若存在满足当前订单的管理人信息， 可以根据 [DescribeManagers](https://cloud.tencent.com/document/product/400/52672) 查看管理人ID； 若传了管理人ID，则Org开头、Admin开头、Tech开头的参数可不传； 管理人ID会包含公司信息

        :type ManagerId: str
        :param _TechPhone: 联系人电话。若没有传ManagerId， 则此字段必传
        :type TechPhone: str
        :param _TechEmail: 联系人邮箱
        :type TechEmail: str
        :param _TechTitle: 联系人职位。若没有传ManagerId， 则此字段必传
        :type TechTitle: str
        :param _Type: 证书类型
        :type Type: int
        :param _CaType: 只针对Dnspod系列证书有效，ca机构类型可为sectigo和digicert
        :type CaType: str
        """
        self._CertId = None
        self._GenCsrType = None
        self._CertCommonName = None
        self._CompanyType = None
        self._CompanyId = None
        self._OrgIdType = None
        self._OrgIdNumber = None
        self._AdminIdType = None
        self._AdminIdNumber = None
        self._TechIdType = None
        self._TechIdNumber = None
        self._Csr = None
        self._DnsNames = None
        self._KeyPass = None
        self._OrgOrganization = None
        self._OrgDivision = None
        self._OrgAddress = None
        self._OrgCountry = None
        self._OrgCity = None
        self._OrgRegion = None
        self._OrgPhoneArea = None
        self._OrgPhoneNumber = None
        self._VerifyType = None
        self._AdminFirstName = None
        self._AdminLastName = None
        self._AdminPhone = None
        self._AdminEmail = None
        self._AdminTitle = None
        self._TechFirstName = None
        self._TechLastName = None
        self._ContactEmail = None
        self._AutoRenewFlag = None
        self._CsrKeyParameter = None
        self._CsrEncryptAlgo = None
        self._ManagerId = None
        self._TechPhone = None
        self._TechEmail = None
        self._TechTitle = None
        self._Type = None
        self._CaType = None

    @property
    def CertId(self):
        """待提交资料的付费证书 ID。	
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def GenCsrType(self):
        """此字段必传。 CSR 生成方式， 取值为：
- online：腾讯云提交的填写的参数信息生成CSR和私钥，并由腾讯云加密存储
- parse：自行生成CSR和私钥，并通过上传CSR申请证书
        :rtype: str
        """
        return self._GenCsrType

    @GenCsrType.setter
    def GenCsrType(self, GenCsrType):
        self._GenCsrType = GenCsrType

    @property
    def CertCommonName(self):
        """证书绑定的通用名称， 若是上传的CSR，则该域名需与CSR解析的通用名称一致
        :rtype: str
        """
        return self._CertCommonName

    @CertCommonName.setter
    def CertCommonName(self, CertCommonName):
        self._CertCommonName = CertCommonName

    @property
    def CompanyType(self):
        """组织信息类型， 取值范围：
1（个人）：仅DV类型证书可设置为1， 个人类型证书组织信息字段可不传：Org开头，Admin开头，Tech开头
2（公司）：所有类型证书都可设置为2， 按需传组织信息字段
        :rtype: int
        """
        return self._CompanyType

    @CompanyType.setter
    def CompanyType(self, CompanyType):
        self._CompanyType = CompanyType

    @property
    def CompanyId(self):
        """公司ID，在 [腾讯云控制台](https://console.cloud.tencent.com/ssl/info) 可进行查看，若无满足的公司信息， 则本参数传0 ； 若存在满足当前订单的公司信息， 可以根据 [DescribeCompanies](https://cloud.tencent.com/document/product/400/90375) 查看公司ID； 若传了公司ID，则Org开头的参数可不传


        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def OrgIdType(self):
        """公司证件类型，取值范围：
TYDMZ（统一社会信用代码 ）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
OTHERS（其他）
        :rtype: str
        """
        return self._OrgIdType

    @OrgIdType.setter
    def OrgIdType(self, OrgIdType):
        self._OrgIdType = OrgIdType

    @property
    def OrgIdNumber(self):
        """公司证件号码，取值范围：
TYDMZ（统一社会信用代码 ）：11532xxxxxxxx24820

        :rtype: str
        """
        return self._OrgIdNumber

    @OrgIdNumber.setter
    def OrgIdNumber(self, OrgIdNumber):
        self._OrgIdNumber = OrgIdNumber

    @property
    def AdminIdType(self):
        """管理人证件类型，取值范围：
SFZ（身份证）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
HZ（护照）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
        :rtype: str
        """
        return self._AdminIdType

    @AdminIdType.setter
    def AdminIdType(self, AdminIdType):
        self._AdminIdType = AdminIdType

    @property
    def AdminIdNumber(self):
        """管理人证件号码，仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段， 取值范围：
SFZ（身份证）：110000xxxxxxxx1242
HZ（护照）:EFxxxxxxx
        :rtype: str
        """
        return self._AdminIdNumber

    @AdminIdNumber.setter
    def AdminIdNumber(self, AdminIdNumber):
        self._AdminIdNumber = AdminIdNumber

    @property
    def TechIdType(self):
        """联系人证件类型，取值范围：
SFZ（身份证）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
HZ（护照）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
        :rtype: str
        """
        return self._TechIdType

    @TechIdType.setter
    def TechIdType(self, TechIdType):
        self._TechIdType = TechIdType

    @property
    def TechIdNumber(self):
        """联系人证件号码，仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段，取值范围：
SFZ（身份证）：110000xxxxxxxx1242
HZ（护照）:EFxxxxxxx
        :rtype: str
        """
        return self._TechIdNumber

    @TechIdNumber.setter
    def TechIdNumber(self, TechIdNumber):
        self._TechIdNumber = TechIdNumber

    @property
    def Csr(self):
        """上传的 CSR 内容。
若GenCsrType为parse， 则此字段必传。
        :rtype: str
        """
        return self._Csr

    @Csr.setter
    def Csr(self, Csr):
        self._Csr = Csr

    @property
    def DnsNames(self):
        """证书绑定的其他域名， 单域名、泛域名证书无需提供。 多域名、多泛域名必填
        :rtype: list of str
        """
        return self._DnsNames

    @DnsNames.setter
    def DnsNames(self, DnsNames):
        self._DnsNames = DnsNames

    @property
    def KeyPass(self):
        """私钥密码， 目前仅使用在生成jks、pfx格式证书时密码； 其他格式私钥证书未加密	
        :rtype: str
        """
        return self._KeyPass

    @KeyPass.setter
    def KeyPass(self, KeyPass):
        self._KeyPass = KeyPass

    @property
    def OrgOrganization(self):
        """公司名称。若没有传CompanyId或者ManagerId， 则此字段必传
        :rtype: str
        """
        return self._OrgOrganization

    @OrgOrganization.setter
    def OrgOrganization(self, OrgOrganization):
        self._OrgOrganization = OrgOrganization

    @property
    def OrgDivision(self):
        """部门名称。若没有传CompanyId或者ManagerId， 则此字段必传
        :rtype: str
        """
        return self._OrgDivision

    @OrgDivision.setter
    def OrgDivision(self, OrgDivision):
        self._OrgDivision = OrgDivision

    @property
    def OrgAddress(self):
        """公司详细地址。若没有传CompanyId或者ManagerId， 则此字段必传
        :rtype: str
        """
        return self._OrgAddress

    @OrgAddress.setter
    def OrgAddress(self, OrgAddress):
        self._OrgAddress = OrgAddress

    @property
    def OrgCountry(self):
        """国家名称，如中国：CN 。若没有传CompanyId或者ManagerId， 则此字段必传
        :rtype: str
        """
        return self._OrgCountry

    @OrgCountry.setter
    def OrgCountry(self, OrgCountry):
        self._OrgCountry = OrgCountry

    @property
    def OrgCity(self):
        """公司所在城市。若没有传CompanyId或者ManagerId， 则此字段必传
        :rtype: str
        """
        return self._OrgCity

    @OrgCity.setter
    def OrgCity(self, OrgCity):
        self._OrgCity = OrgCity

    @property
    def OrgRegion(self):
        """公司所在省份。若没有传CompanyId或者ManagerId， 则此字段必传
        :rtype: str
        """
        return self._OrgRegion

    @OrgRegion.setter
    def OrgRegion(self, OrgRegion):
        self._OrgRegion = OrgRegion

    @property
    def OrgPhoneArea(self):
        """公司所属区号。若没有传CompanyId或者ManagerId， 则此字段必传
如：021。  手机号码传 86
        :rtype: str
        """
        return self._OrgPhoneArea

    @OrgPhoneArea.setter
    def OrgPhoneArea(self, OrgPhoneArea):
        self._OrgPhoneArea = OrgPhoneArea

    @property
    def OrgPhoneNumber(self):
        """公司所属号码。若没有传CompanyId或者ManagerId， 则此字段必传
        :rtype: str
        """
        return self._OrgPhoneNumber

    @OrgPhoneNumber.setter
    def OrgPhoneNumber(self, OrgPhoneNumber):
        self._OrgPhoneNumber = OrgPhoneNumber

    @property
    def VerifyType(self):
        """证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单为：64.78.193.238，216.168.247.9，216.168.249.9，54.189.196.217
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def AdminFirstName(self):
        """管理人名。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        """管理人姓。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhone(self):
        """管理人手机号码。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._AdminPhone

    @AdminPhone.setter
    def AdminPhone(self, AdminPhone):
        self._AdminPhone = AdminPhone

    @property
    def AdminEmail(self):
        """管理人邮箱地址。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminTitle(self):
        """管理人职位。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._AdminTitle

    @AdminTitle.setter
    def AdminTitle(self, AdminTitle):
        self._AdminTitle = AdminTitle

    @property
    def TechFirstName(self):
        """联系人名。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._TechFirstName

    @TechFirstName.setter
    def TechFirstName(self, TechFirstName):
        self._TechFirstName = TechFirstName

    @property
    def TechLastName(self):
        """联系人姓。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._TechLastName

    @TechLastName.setter
    def TechLastName(self, TechLastName):
        self._TechLastName = TechLastName

    @property
    def ContactEmail(self):
        """联系人邮箱地址。CompanyType为1时， 此字段必传
        :rtype: str
        """
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def AutoRenewFlag(self):
        """是否开启自动续费： 0， 不开启；  1， 开启； 默认为0
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CsrKeyParameter(self):
        """密钥对参数，RSA支持2048，4096。ECC仅支持prime256v1。加密算法选择ECC时，此参数必填
国密证书类型本字段不用传
        :rtype: str
        """
        return self._CsrKeyParameter

    @CsrKeyParameter.setter
    def CsrKeyParameter(self, CsrKeyParameter):
        self._CsrKeyParameter = CsrKeyParameter

    @property
    def CsrEncryptAlgo(self):
        """加密算法，取值为ECC、RSA， 默认为RSA
国密证书类型本字段不用传
        :rtype: str
        """
        return self._CsrEncryptAlgo

    @CsrEncryptAlgo.setter
    def CsrEncryptAlgo(self, CsrEncryptAlgo):
        self._CsrEncryptAlgo = CsrEncryptAlgo

    @property
    def ManagerId(self):
        """管理人ID，在 [腾讯云控制台](https://console.cloud.tencent.com/ssl/info) 可进行查看，若无满足的管理人信息， 则本参数传0 ； 若存在满足当前订单的管理人信息， 可以根据 [DescribeManagers](https://cloud.tencent.com/document/product/400/52672) 查看管理人ID； 若传了管理人ID，则Org开头、Admin开头、Tech开头的参数可不传； 管理人ID会包含公司信息

        :rtype: str
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def TechPhone(self):
        """联系人电话。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._TechPhone

    @TechPhone.setter
    def TechPhone(self, TechPhone):
        self._TechPhone = TechPhone

    @property
    def TechEmail(self):
        """联系人邮箱
        :rtype: str
        """
        return self._TechEmail

    @TechEmail.setter
    def TechEmail(self, TechEmail):
        self._TechEmail = TechEmail

    @property
    def TechTitle(self):
        """联系人职位。若没有传ManagerId， 则此字段必传
        :rtype: str
        """
        return self._TechTitle

    @TechTitle.setter
    def TechTitle(self, TechTitle):
        self._TechTitle = TechTitle

    @property
    def Type(self):
        """证书类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CaType(self):
        """只针对Dnspod系列证书有效，ca机构类型可为sectigo和digicert
        :rtype: str
        """
        return self._CaType

    @CaType.setter
    def CaType(self, CaType):
        self._CaType = CaType


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._GenCsrType = params.get("GenCsrType")
        self._CertCommonName = params.get("CertCommonName")
        self._CompanyType = params.get("CompanyType")
        self._CompanyId = params.get("CompanyId")
        self._OrgIdType = params.get("OrgIdType")
        self._OrgIdNumber = params.get("OrgIdNumber")
        self._AdminIdType = params.get("AdminIdType")
        self._AdminIdNumber = params.get("AdminIdNumber")
        self._TechIdType = params.get("TechIdType")
        self._TechIdNumber = params.get("TechIdNumber")
        self._Csr = params.get("Csr")
        self._DnsNames = params.get("DnsNames")
        self._KeyPass = params.get("KeyPass")
        self._OrgOrganization = params.get("OrgOrganization")
        self._OrgDivision = params.get("OrgDivision")
        self._OrgAddress = params.get("OrgAddress")
        self._OrgCountry = params.get("OrgCountry")
        self._OrgCity = params.get("OrgCity")
        self._OrgRegion = params.get("OrgRegion")
        self._OrgPhoneArea = params.get("OrgPhoneArea")
        self._OrgPhoneNumber = params.get("OrgPhoneNumber")
        self._VerifyType = params.get("VerifyType")
        self._AdminFirstName = params.get("AdminFirstName")
        self._AdminLastName = params.get("AdminLastName")
        self._AdminPhone = params.get("AdminPhone")
        self._AdminEmail = params.get("AdminEmail")
        self._AdminTitle = params.get("AdminTitle")
        self._TechFirstName = params.get("TechFirstName")
        self._TechLastName = params.get("TechLastName")
        self._ContactEmail = params.get("ContactEmail")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CsrKeyParameter = params.get("CsrKeyParameter")
        self._CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self._ManagerId = params.get("ManagerId")
        self._TechPhone = params.get("TechPhone")
        self._TechEmail = params.get("TechEmail")
        self._TechTitle = params.get("TechTitle")
        self._Type = params.get("Type")
        self._CaType = params.get("CaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfoSubmitResponse(AbstractModel):
    """CertificateInfoSubmit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CertificateOrderSubmitRequest(AbstractModel):
    """CertificateOrderSubmit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: 待提交资料的付费证书 ID。	
        :type CertId: str
        :param _DeleteDnsAutoRecord: 是否删除自动DNS验证值：0，不删除； 1，删除； 默认不删除
        :type DeleteDnsAutoRecord: int
        :param _VerifyType: 证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单见控制台页面
        :type VerifyType: str
        """
        self._CertId = None
        self._DeleteDnsAutoRecord = None
        self._VerifyType = None

    @property
    def CertId(self):
        """待提交资料的付费证书 ID。	
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DeleteDnsAutoRecord(self):
        """是否删除自动DNS验证值：0，不删除； 1，删除； 默认不删除
        :rtype: int
        """
        return self._DeleteDnsAutoRecord

    @DeleteDnsAutoRecord.setter
    def DeleteDnsAutoRecord(self, DeleteDnsAutoRecord):
        self._DeleteDnsAutoRecord = DeleteDnsAutoRecord

    @property
    def VerifyType(self):
        """证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单见控制台页面
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._DeleteDnsAutoRecord = params.get("DeleteDnsAutoRecord")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateOrderSubmitResponse(AbstractModel):
    """CertificateOrderSubmit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: CA机构侧订单号。
        :type OrderId: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :type Status: int
        :param _IsAudited: 是否预审核
        :type IsAudited: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._Status = None
        self._IsAudited = None
        self._RequestId = None

    @property
    def OrderId(self):
        """CA机构侧订单号。
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Status(self):
        """证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsAudited(self):
        """是否预审核
        :rtype: bool
        """
        return self._IsAudited

    @IsAudited.setter
    def IsAudited(self, IsAudited):
        self._IsAudited = IsAudited

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Status = params.get("Status")
        self._IsAudited = params.get("IsAudited")
        self._RequestId = params.get("RequestId")


class Certificates(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 的内容。

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 用户 UIN。
        :type OwnerUin: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: str
        :param _From: 证书来源：
trustasia：亚洲诚信，
upload：用户上传。
wosign：沃通
sheca：上海CA
        :type From: str
        :param _PackageType: 证书套餐类型：
null：用户上传证书（没有套餐类型），
2：TrustAsia TLS RSA CA， 
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
83：TrustAsia C1 DV Free
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书
100：CFCA 企业型通配符(OV)SSL证书
101：CFCA 增强型(EV)SSL证书
        :type PackageType: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
        :type CertificateType: str
        :param _ProductZhName: 证书产品名称
        :type ProductZhName: str
        :param _Domain: 主域名。
        :type Domain: str
        :param _Alias: 备注名称。
        :type Alias: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 自动添加DNS记录，5 = 企业证书，待提交资料，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 证书已退款。 15 = 证书迁移中
        :type Status: int
        :param _CertificateExtra: 证书扩展信息。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _VulnerabilityStatus: 漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
        :type VulnerabilityStatus: str
        :param _StatusMsg: 状态信息。
        :type StatusMsg: str
        :param _VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，DNS_PROXY = DNS代理验证。FILE_PROXY = 文件代理验证
        :type VerifyType: str
        :param _CertBeginTime: 证书生效时间。
        :type CertBeginTime: str
        :param _CertEndTime: 证书过期时间。
        :type CertEndTime: str
        :param _ValidityPeriod: 证书有效期，单位（月）。
        :type ValidityPeriod: str
        :param _InsertTime: 创建时间。
        :type InsertTime: str
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _SubjectAltName: 证书包含的多个域名（包含主域名）。
        :type SubjectAltName: list of str
        :param _PackageTypeName: 证书类型名称。
        :type PackageTypeName: str
        :param _StatusName: 状态名称。
        :type StatusName: str
        :param _IsVip: 是否为 VIP 客户。
        :type IsVip: bool
        :param _IsDv: 是否为 DV 版证书。
        :type IsDv: bool
        :param _IsWildcard: 是否为泛域名证书。
        :type IsWildcard: bool
        :param _IsVulnerability: 是否启用了漏洞扫描功能。
        :type IsVulnerability: bool
        :param _RenewAble: 是否可续费。
        :type RenewAble: bool
        :param _ProjectInfo: 项目信息。
        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        :param _BoundResource: 关联的云资源，暂不可用
        :type BoundResource: list of str
        :param _Deployable: 是否可部署。
        :type Deployable: bool
        :param _Tags: 标签列表
        :type Tags: list of Tags
        :param _IsIgnore: 是否已忽略到期通知
        :type IsIgnore: bool
        :param _IsSM: 是否国密证书
        :type IsSM: bool
        :param _EncryptAlgorithm: 证书算法
        :type EncryptAlgorithm: str
        :param _CAEncryptAlgorithms: 上传CA证书的加密算法
        :type CAEncryptAlgorithms: list of str
        :param _CAEndTimes: 上传CA证书的过期时间
        :type CAEndTimes: list of str
        :param _CACommonNames: 上传CA证书的通用名称
        :type CACommonNames: list of str
        :param _PreAuditInfo: 证书预审核信息
        :type PreAuditInfo: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        :param _AutoRenewFlag: 是否自动续费
        :type AutoRenewFlag: int
        :param _HostingStatus: 托管状态，0，托管中，5，资源替换中， 10， 托管完成， -1未托管 
        :type HostingStatus: int
        :param _HostingCompleteTime: 托管完成时间
        :type HostingCompleteTime: str
        :param _HostingRenewCertId: 托管新证书ID
        :type HostingRenewCertId: str
        :param _HasRenewOrder: 存在的续费证书ID
        :type HasRenewOrder: str
        :param _ReplaceOriCertIsDelete: 重颁发证书原证书是否删除
        :type ReplaceOriCertIsDelete: bool
        :param _IsExpiring: 是否即将过期， 证书即将到期的30天内为即将过期
        :type IsExpiring: bool
        :param _DVAuthDeadline: DV证书添加验证截止时间
        :type DVAuthDeadline: str
        :param _ValidationPassedTime: 域名验证通过时间
        :type ValidationPassedTime: str
        :param _CertSANs: 证书关联的多域名
        :type CertSANs: list of str
        :param _AwaitingValidationMsg: 域名验证驳回信息
        :type AwaitingValidationMsg: str
        :param _AllowDownload: 是否允许下载
        :type AllowDownload: bool
        :param _IsDNSPODResolve: 证书域名是否全部在DNSPOD托管解析
        :type IsDNSPODResolve: bool
        :param _IsPackage: 是否是权益点购买的证书
        :type IsPackage: bool
        :param _KeyPasswordCustomFlag: 是否存在私钥密码
        :type KeyPasswordCustomFlag: bool
        :param _SupportDownloadType: 支持下载的WEB服务器类型： nginx、apache、iis、tomcat、jks、root、other
        :type SupportDownloadType: :class:`tencentcloud.ssl.v20191205.models.SupportDownloadType`
        :param _CertRevokedTime: 证书吊销完成时间
        :type CertRevokedTime: str
        :param _HostingResourceTypes: 托管资源类型列表
        :type HostingResourceTypes: list of str
        :param _HostingConfig: 托管配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HostingConfig: :class:`tencentcloud.ssl.v20191205.models.HostingConfig`
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._PackageType = None
        self._CertificateType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._CertificateExtra = None
        self._VulnerabilityStatus = None
        self._StatusMsg = None
        self._VerifyType = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._CertificateId = None
        self._SubjectAltName = None
        self._PackageTypeName = None
        self._StatusName = None
        self._IsVip = None
        self._IsDv = None
        self._IsWildcard = None
        self._IsVulnerability = None
        self._RenewAble = None
        self._ProjectInfo = None
        self._BoundResource = None
        self._Deployable = None
        self._Tags = None
        self._IsIgnore = None
        self._IsSM = None
        self._EncryptAlgorithm = None
        self._CAEncryptAlgorithms = None
        self._CAEndTimes = None
        self._CACommonNames = None
        self._PreAuditInfo = None
        self._AutoRenewFlag = None
        self._HostingStatus = None
        self._HostingCompleteTime = None
        self._HostingRenewCertId = None
        self._HasRenewOrder = None
        self._ReplaceOriCertIsDelete = None
        self._IsExpiring = None
        self._DVAuthDeadline = None
        self._ValidationPassedTime = None
        self._CertSANs = None
        self._AwaitingValidationMsg = None
        self._AllowDownload = None
        self._IsDNSPODResolve = None
        self._IsPackage = None
        self._KeyPasswordCustomFlag = None
        self._SupportDownloadType = None
        self._CertRevokedTime = None
        self._HostingResourceTypes = None
        self._HostingConfig = None

    @property
    def OwnerUin(self):
        """用户 UIN。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """项目 ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        """证书来源：
trustasia：亚洲诚信，
upload：用户上传。
wosign：沃通
sheca：上海CA
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def PackageType(self):
        """证书套餐类型：
null：用户上传证书（没有套餐类型），
2：TrustAsia TLS RSA CA， 
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
83：TrustAsia C1 DV Free
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书
100：CFCA 企业型通配符(OV)SSL证书
101：CFCA 增强型(EV)SSL证书
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def CertificateType(self):
        """证书类型：CA = 客户端证书，SVR = 服务器证书。
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProductZhName(self):
        """证书产品名称
        :rtype: str
        """
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        """主域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        """备注名称。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        """证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 自动添加DNS记录，5 = 企业证书，待提交资料，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 证书已退款。 15 = 证书迁移中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertificateExtra(self):
        """证书扩展信息。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        """
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def VulnerabilityStatus(self):
        """漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
        :rtype: str
        """
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def StatusMsg(self):
        """状态信息。
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        """验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，DNS_PROXY = DNS代理验证。FILE_PROXY = 文件代理验证
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def CertBeginTime(self):
        """证书生效时间。
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        """证书过期时间。
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        """证书有效期，单位（月）。
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        """创建时间。
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def SubjectAltName(self):
        """证书包含的多个域名（包含主域名）。
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def PackageTypeName(self):
        """证书类型名称。
        :rtype: str
        """
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        """状态名称。
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def IsVip(self):
        """是否为 VIP 客户。
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsDv(self):
        """是否为 DV 版证书。
        :rtype: bool
        """
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsWildcard(self):
        """是否为泛域名证书。
        :rtype: bool
        """
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsVulnerability(self):
        """是否启用了漏洞扫描功能。
        :rtype: bool
        """
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        """是否可续费。
        :rtype: bool
        """
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def ProjectInfo(self):
        """项目信息。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        """
        return self._ProjectInfo

    @ProjectInfo.setter
    def ProjectInfo(self, ProjectInfo):
        self._ProjectInfo = ProjectInfo

    @property
    def BoundResource(self):
        """关联的云资源，暂不可用
        :rtype: list of str
        """
        return self._BoundResource

    @BoundResource.setter
    def BoundResource(self, BoundResource):
        self._BoundResource = BoundResource

    @property
    def Deployable(self):
        """是否可部署。
        :rtype: bool
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsIgnore(self):
        """是否已忽略到期通知
        :rtype: bool
        """
        return self._IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, IsIgnore):
        self._IsIgnore = IsIgnore

    @property
    def IsSM(self):
        """是否国密证书
        :rtype: bool
        """
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def EncryptAlgorithm(self):
        """证书算法
        :rtype: str
        """
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def CAEncryptAlgorithms(self):
        """上传CA证书的加密算法
        :rtype: list of str
        """
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CAEndTimes(self):
        """上传CA证书的过期时间
        :rtype: list of str
        """
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def CACommonNames(self):
        """上传CA证书的通用名称
        :rtype: list of str
        """
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def PreAuditInfo(self):
        """证书预审核信息
        :rtype: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        """
        return self._PreAuditInfo

    @PreAuditInfo.setter
    def PreAuditInfo(self, PreAuditInfo):
        self._PreAuditInfo = PreAuditInfo

    @property
    def AutoRenewFlag(self):
        """是否自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def HostingStatus(self):
        """托管状态，0，托管中，5，资源替换中， 10， 托管完成， -1未托管 
        :rtype: int
        """
        return self._HostingStatus

    @HostingStatus.setter
    def HostingStatus(self, HostingStatus):
        self._HostingStatus = HostingStatus

    @property
    def HostingCompleteTime(self):
        """托管完成时间
        :rtype: str
        """
        return self._HostingCompleteTime

    @HostingCompleteTime.setter
    def HostingCompleteTime(self, HostingCompleteTime):
        self._HostingCompleteTime = HostingCompleteTime

    @property
    def HostingRenewCertId(self):
        """托管新证书ID
        :rtype: str
        """
        return self._HostingRenewCertId

    @HostingRenewCertId.setter
    def HostingRenewCertId(self, HostingRenewCertId):
        self._HostingRenewCertId = HostingRenewCertId

    @property
    def HasRenewOrder(self):
        """存在的续费证书ID
        :rtype: str
        """
        return self._HasRenewOrder

    @HasRenewOrder.setter
    def HasRenewOrder(self, HasRenewOrder):
        self._HasRenewOrder = HasRenewOrder

    @property
    def ReplaceOriCertIsDelete(self):
        """重颁发证书原证书是否删除
        :rtype: bool
        """
        return self._ReplaceOriCertIsDelete

    @ReplaceOriCertIsDelete.setter
    def ReplaceOriCertIsDelete(self, ReplaceOriCertIsDelete):
        self._ReplaceOriCertIsDelete = ReplaceOriCertIsDelete

    @property
    def IsExpiring(self):
        """是否即将过期， 证书即将到期的30天内为即将过期
        :rtype: bool
        """
        return self._IsExpiring

    @IsExpiring.setter
    def IsExpiring(self, IsExpiring):
        self._IsExpiring = IsExpiring

    @property
    def DVAuthDeadline(self):
        """DV证书添加验证截止时间
        :rtype: str
        """
        return self._DVAuthDeadline

    @DVAuthDeadline.setter
    def DVAuthDeadline(self, DVAuthDeadline):
        self._DVAuthDeadline = DVAuthDeadline

    @property
    def ValidationPassedTime(self):
        """域名验证通过时间
        :rtype: str
        """
        return self._ValidationPassedTime

    @ValidationPassedTime.setter
    def ValidationPassedTime(self, ValidationPassedTime):
        self._ValidationPassedTime = ValidationPassedTime

    @property
    def CertSANs(self):
        """证书关联的多域名
        :rtype: list of str
        """
        return self._CertSANs

    @CertSANs.setter
    def CertSANs(self, CertSANs):
        self._CertSANs = CertSANs

    @property
    def AwaitingValidationMsg(self):
        """域名验证驳回信息
        :rtype: str
        """
        return self._AwaitingValidationMsg

    @AwaitingValidationMsg.setter
    def AwaitingValidationMsg(self, AwaitingValidationMsg):
        self._AwaitingValidationMsg = AwaitingValidationMsg

    @property
    def AllowDownload(self):
        """是否允许下载
        :rtype: bool
        """
        return self._AllowDownload

    @AllowDownload.setter
    def AllowDownload(self, AllowDownload):
        self._AllowDownload = AllowDownload

    @property
    def IsDNSPODResolve(self):
        """证书域名是否全部在DNSPOD托管解析
        :rtype: bool
        """
        return self._IsDNSPODResolve

    @IsDNSPODResolve.setter
    def IsDNSPODResolve(self, IsDNSPODResolve):
        self._IsDNSPODResolve = IsDNSPODResolve

    @property
    def IsPackage(self):
        """是否是权益点购买的证书
        :rtype: bool
        """
        return self._IsPackage

    @IsPackage.setter
    def IsPackage(self, IsPackage):
        self._IsPackage = IsPackage

    @property
    def KeyPasswordCustomFlag(self):
        """是否存在私钥密码
        :rtype: bool
        """
        return self._KeyPasswordCustomFlag

    @KeyPasswordCustomFlag.setter
    def KeyPasswordCustomFlag(self, KeyPasswordCustomFlag):
        self._KeyPasswordCustomFlag = KeyPasswordCustomFlag

    @property
    def SupportDownloadType(self):
        """支持下载的WEB服务器类型： nginx、apache、iis、tomcat、jks、root、other
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SupportDownloadType`
        """
        return self._SupportDownloadType

    @SupportDownloadType.setter
    def SupportDownloadType(self, SupportDownloadType):
        self._SupportDownloadType = SupportDownloadType

    @property
    def CertRevokedTime(self):
        """证书吊销完成时间
        :rtype: str
        """
        return self._CertRevokedTime

    @CertRevokedTime.setter
    def CertRevokedTime(self, CertRevokedTime):
        self._CertRevokedTime = CertRevokedTime

    @property
    def HostingResourceTypes(self):
        """托管资源类型列表
        :rtype: list of str
        """
        return self._HostingResourceTypes

    @HostingResourceTypes.setter
    def HostingResourceTypes(self, HostingResourceTypes):
        self._HostingResourceTypes = HostingResourceTypes

    @property
    def HostingConfig(self):
        """托管配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.HostingConfig`
        """
        return self._HostingConfig

    @HostingConfig.setter
    def HostingConfig(self, HostingConfig):
        self._HostingConfig = HostingConfig


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._PackageType = params.get("PackageType")
        self._CertificateType = params.get("CertificateType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._CertificateId = params.get("CertificateId")
        self._SubjectAltName = params.get("SubjectAltName")
        self._PackageTypeName = params.get("PackageTypeName")
        self._StatusName = params.get("StatusName")
        self._IsVip = params.get("IsVip")
        self._IsDv = params.get("IsDv")
        self._IsWildcard = params.get("IsWildcard")
        self._IsVulnerability = params.get("IsVulnerability")
        self._RenewAble = params.get("RenewAble")
        if params.get("ProjectInfo") is not None:
            self._ProjectInfo = ProjectInfo()
            self._ProjectInfo._deserialize(params.get("ProjectInfo"))
        self._BoundResource = params.get("BoundResource")
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsIgnore = params.get("IsIgnore")
        self._IsSM = params.get("IsSM")
        self._EncryptAlgorithm = params.get("EncryptAlgorithm")
        self._CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self._CAEndTimes = params.get("CAEndTimes")
        self._CACommonNames = params.get("CACommonNames")
        if params.get("PreAuditInfo") is not None:
            self._PreAuditInfo = PreAuditInfo()
            self._PreAuditInfo._deserialize(params.get("PreAuditInfo"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._HostingStatus = params.get("HostingStatus")
        self._HostingCompleteTime = params.get("HostingCompleteTime")
        self._HostingRenewCertId = params.get("HostingRenewCertId")
        self._HasRenewOrder = params.get("HasRenewOrder")
        self._ReplaceOriCertIsDelete = params.get("ReplaceOriCertIsDelete")
        self._IsExpiring = params.get("IsExpiring")
        self._DVAuthDeadline = params.get("DVAuthDeadline")
        self._ValidationPassedTime = params.get("ValidationPassedTime")
        self._CertSANs = params.get("CertSANs")
        self._AwaitingValidationMsg = params.get("AwaitingValidationMsg")
        self._AllowDownload = params.get("AllowDownload")
        self._IsDNSPODResolve = params.get("IsDNSPODResolve")
        self._IsPackage = params.get("IsPackage")
        self._KeyPasswordCustomFlag = params.get("KeyPasswordCustomFlag")
        if params.get("SupportDownloadType") is not None:
            self._SupportDownloadType = SupportDownloadType()
            self._SupportDownloadType._deserialize(params.get("SupportDownloadType"))
        self._CertRevokedTime = params.get("CertRevokedTime")
        self._HostingResourceTypes = params.get("HostingResourceTypes")
        if params.get("HostingConfig") is not None:
            self._HostingConfig = HostingConfig()
            self._HostingConfig._deserialize(params.get("HostingConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateChainRequest(AbstractModel):
    """CheckCertificateChain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateChain: 待检查的证书链
        :type CertificateChain: str
        """
        self._CertificateChain = None

    @property
    def CertificateChain(self):
        """待检查的证书链
        :rtype: str
        """
        return self._CertificateChain

    @CertificateChain.setter
    def CertificateChain(self, CertificateChain):
        self._CertificateChain = CertificateChain


    def _deserialize(self, params):
        self._CertificateChain = params.get("CertificateChain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateChainResponse(AbstractModel):
    """CheckCertificateChain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsValid: true为通过检查，false为未通过检查。
        :type IsValid: bool
        :param _IsTrustedCA: true为可信CA，false为不可信CA。
        :type IsTrustedCA: bool
        :param _Chains: 包含证书链中每一段证书的通用名称。
        :type Chains: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsValid = None
        self._IsTrustedCA = None
        self._Chains = None
        self._RequestId = None

    @property
    def IsValid(self):
        """true为通过检查，false为未通过检查。
        :rtype: bool
        """
        return self._IsValid

    @IsValid.setter
    def IsValid(self, IsValid):
        self._IsValid = IsValid

    @property
    def IsTrustedCA(self):
        """true为可信CA，false为不可信CA。
        :rtype: bool
        """
        return self._IsTrustedCA

    @IsTrustedCA.setter
    def IsTrustedCA(self, IsTrustedCA):
        self._IsTrustedCA = IsTrustedCA

    @property
    def Chains(self):
        """包含证书链中每一段证书的通用名称。
        :rtype: list of str
        """
        return self._Chains

    @Chains.setter
    def Chains(self, Chains):
        self._Chains = Chains

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsValid = params.get("IsValid")
        self._IsTrustedCA = params.get("IsTrustedCA")
        self._Chains = params.get("Chains")
        self._RequestId = params.get("RequestId")


class CheckCertificateDomainVerificationRequest(AbstractModel):
    """CheckCertificateDomainVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。 
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书ID。 
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateDomainVerificationResponse(AbstractModel):
    """CheckCertificateDomainVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VerificationResults: 证书域名验证结果列表， 证书若绑定了多个域名， 则返回数组有多份
注意：此字段可能返回 null，表示取不到有效值。
        :type VerificationResults: list of DomainValidationResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VerificationResults = None
        self._RequestId = None

    @property
    def VerificationResults(self):
        """证书域名验证结果列表， 证书若绑定了多个域名， 则返回数组有多份
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DomainValidationResult
        """
        return self._VerificationResults

    @VerificationResults.setter
    def VerificationResults(self, VerificationResults):
        self._VerificationResults = VerificationResults

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("VerificationResults") is not None:
            self._VerificationResults = []
            for item in params.get("VerificationResults"):
                obj = DomainValidationResult()
                obj._deserialize(item)
                self._VerificationResults.append(obj)
        self._RequestId = params.get("RequestId")


class CheckCertificateExistRequest(AbstractModel):
    """CheckCertificateExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificatePublicKey: 证书公钥内容， 包含证书链
        :type CertificatePublicKey: str
        """
        self._CertificatePublicKey = None

    @property
    def CertificatePublicKey(self):
        """证书公钥内容， 包含证书链
        :rtype: str
        """
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey


    def _deserialize(self, params):
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateExistResponse(AbstractModel):
    """CheckCertificateExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RepeatCertId: 重复的证书ID
        :type RepeatCertId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RepeatCertId = None
        self._RequestId = None

    @property
    def RepeatCertId(self):
        """重复的证书ID
        :rtype: str
        """
        return self._RepeatCertId

    @RepeatCertId.setter
    def RepeatCertId(self, RepeatCertId):
        self._RepeatCertId = RepeatCertId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RepeatCertId = params.get("RepeatCertId")
        self._RequestId = params.get("RequestId")


class ClbInstanceDetail(AbstractModel):
    """clb实例详情

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB实例ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB实例名称
        :type LoadBalancerName: str
        :param _Listeners: CLB监听器列表
        :type Listeners: list of ClbListener
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        """CLB实例ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """CLB实例名称
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        """CLB监听器列表
        :rtype: list of ClbListener
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ClbListener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbInstanceList(AbstractModel):
    """clb实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _InstanceList: clb实例详情
        :type InstanceList: list of ClbInstanceDetail
        :param _TotalCount: 该地域下Clb实例总数
        :type TotalCount: int
        :param _Error: 是否查询异常
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """clb实例详情
        :rtype: list of ClbInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """该地域下Clb实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """是否查询异常
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ClbInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListener(AbstractModel):
    """CLB实例监听器

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _SniSwitch: 是否开启SNI，1为开启，0为关闭
        :type SniSwitch: int
        :param _Protocol: 监听器协议类型， HTTPS|TCP_SSL
        :type Protocol: str
        :param _Certificate: 监听器绑定的证书数据
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _Rules: 监听器规则列表
        :type Rules: list of ClbListenerRule
        :param _NoMatchDomains: 不匹配域名列表
        :type NoMatchDomains: list of str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._SniSwitch = None
        self._Protocol = None
        self._Certificate = None
        self._Rules = None
        self._NoMatchDomains = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SniSwitch(self):
        """是否开启SNI，1为开启，0为关闭
        :rtype: int
        """
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Protocol(self):
        """监听器协议类型， HTTPS|TCP_SSL
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Certificate(self):
        """监听器绑定的证书数据
        :rtype: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Rules(self):
        """监听器规则列表
        :rtype: list of ClbListenerRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def NoMatchDomains(self):
        """不匹配域名列表
        :rtype: list of str
        """
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SniSwitch = params.get("SniSwitch")
        self._Protocol = params.get("Protocol")
        if params.get("Certificate") is not None:
            self._Certificate = Certificate()
            self._Certificate._deserialize(params.get("Certificate"))
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ClbListenerRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerRule(AbstractModel):
    """CLB监听器规则

    """

    def __init__(self):
        r"""
        :param _LocationId: 规则ID
        :type LocationId: str
        :param _Domain: 规则绑定的域名
        :type Domain: str
        :param _IsMatch: 规则是否匹配待绑定证书的域名
        :type IsMatch: bool
        :param _Certificate: 规则已绑定的证书数据
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _NoMatchDomains: 不匹配域名列表
        :type NoMatchDomains: list of str
        :param _Url: 规则绑定的路径
        :type Url: str
        """
        self._LocationId = None
        self._Domain = None
        self._IsMatch = None
        self._Certificate = None
        self._NoMatchDomains = None
        self._Url = None

    @property
    def LocationId(self):
        """规则ID
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        """规则绑定的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def IsMatch(self):
        """规则是否匹配待绑定证书的域名
        :rtype: bool
        """
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def Certificate(self):
        """规则已绑定的证书数据
        :rtype: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def NoMatchDomains(self):
        """不匹配域名列表
        :rtype: list of str
        """
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains

    @property
    def Url(self):
        """规则绑定的路径
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._IsMatch = params.get("IsMatch")
        if params.get("Certificate") is not None:
            self._Certificate = Certificate()
            self._Certificate._deserialize(params.get("Certificate"))
        self._NoMatchDomains = params.get("NoMatchDomains")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待提交资料的付费证书 ID。	
        :type CertificateId: str
        :param _VerifyType: 证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单为：64.78.193.238，216.168.247.9，216.168.249.9，54.189.196.217
        :type VerifyType: str
        """
        self._CertificateId = None
        self._VerifyType = None

    @property
    def CertificateId(self):
        """待提交资料的付费证书 ID。	
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def VerifyType(self):
        """证书域名验证方式：
DNS_AUTO： 自动添加域名DNS验证， 需用户域名解析托管在『[云解析DNS](https://console.cloud.tencent.com/cns)』，且与申请证书归属同一个腾讯云账号
DNS：手动添加域名DNS验证，需用户手动去域名解析服务商添加验证值
FILE：手动添加域名文件验证。 需要用户手动在域名站点根目录添加指定路径文件进行文件验证， http&https任一通过即可；且域名站点需海外CA机构能访问， 具体访问白名单为：64.78.193.238，216.168.247.9，216.168.249.9，54.189.196.217
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationResponse(AbstractModel):
    """CommitCertificateInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: CA机构侧订单号。
        :type OrderId: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._Status = None
        self._RequestId = None

    @property
    def OrderId(self):
        """CA机构侧订单号。
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Status(self):
        """证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CompanyInfo(AbstractModel):
    """公司信息

    """

    def __init__(self):
        r"""
        :param _CompanyName: 公司名称
        :type CompanyName: str
        :param _CompanyId: 公司ID
        :type CompanyId: int
        :param _CompanyCountry: 公司所在国家
        :type CompanyCountry: str
        :param _CompanyProvince: 公司所在省份
        :type CompanyProvince: str
        :param _CompanyCity: 公司所在城市
        :type CompanyCity: str
        :param _CompanyAddress: 公司所在详细地址
        :type CompanyAddress: str
        :param _CompanyPhone: 公司电话
        :type CompanyPhone: str
        :param _IdType: 公司证件类型，取值范围：
TYDMZ（统一社会信用代码 ）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
OTHERS（其他）
        :type IdType: str
        :param _IdNumber: 公司证件号码，取值范围：
TYDMZ（统一社会信用代码 ）：11532xxxxxxxx24820
        :type IdNumber: str
        :param _Tags: 标签
        :type Tags: list of Tags
        """
        self._CompanyName = None
        self._CompanyId = None
        self._CompanyCountry = None
        self._CompanyProvince = None
        self._CompanyCity = None
        self._CompanyAddress = None
        self._CompanyPhone = None
        self._IdType = None
        self._IdNumber = None
        self._Tags = None

    @property
    def CompanyName(self):
        """公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def CompanyId(self):
        """公司ID
        :rtype: int
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def CompanyCountry(self):
        """公司所在国家
        :rtype: str
        """
        return self._CompanyCountry

    @CompanyCountry.setter
    def CompanyCountry(self, CompanyCountry):
        self._CompanyCountry = CompanyCountry

    @property
    def CompanyProvince(self):
        """公司所在省份
        :rtype: str
        """
        return self._CompanyProvince

    @CompanyProvince.setter
    def CompanyProvince(self, CompanyProvince):
        self._CompanyProvince = CompanyProvince

    @property
    def CompanyCity(self):
        """公司所在城市
        :rtype: str
        """
        return self._CompanyCity

    @CompanyCity.setter
    def CompanyCity(self, CompanyCity):
        self._CompanyCity = CompanyCity

    @property
    def CompanyAddress(self):
        """公司所在详细地址
        :rtype: str
        """
        return self._CompanyAddress

    @CompanyAddress.setter
    def CompanyAddress(self, CompanyAddress):
        self._CompanyAddress = CompanyAddress

    @property
    def CompanyPhone(self):
        """公司电话
        :rtype: str
        """
        return self._CompanyPhone

    @CompanyPhone.setter
    def CompanyPhone(self, CompanyPhone):
        self._CompanyPhone = CompanyPhone

    @property
    def IdType(self):
        """公司证件类型，取值范围：
TYDMZ（统一社会信用代码 ）：仅CFCA类型证书需要使用本字段， 其他类型证书不需要使用本字段
OTHERS（其他）
        :rtype: str
        """
        return self._IdType

    @IdType.setter
    def IdType(self, IdType):
        self._IdType = IdType

    @property
    def IdNumber(self):
        """公司证件号码，取值范围：
TYDMZ（统一社会信用代码 ）：11532xxxxxxxx24820
        :rtype: str
        """
        return self._IdNumber

    @IdNumber.setter
    def IdNumber(self, IdNumber):
        self._IdNumber = IdNumber

    @property
    def Tags(self):
        """标签
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._CompanyName = params.get("CompanyName")
        self._CompanyId = params.get("CompanyId")
        self._CompanyCountry = params.get("CompanyCountry")
        self._CompanyProvince = params.get("CompanyProvince")
        self._CompanyCity = params.get("CompanyCity")
        self._CompanyAddress = params.get("CompanyAddress")
        self._CompanyPhone = params.get("CompanyPhone")
        self._IdType = params.get("IdType")
        self._IdNumber = params.get("IdNumber")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteCertificateRequest(AbstractModel):
    """CompleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteCertificateResponse(AbstractModel):
    """CompleteCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CosInstanceDetail(AbstractModel):
    """COS实例详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 已绑定的证书ID
        :type CertId: str
        :param _Status: ENABLED: 域名上线状态
DISABLED:域名下线状态
        :type Status: str
        :param _Bucket: 存储桶名称
        :type Bucket: str
        :param _Region: 存储桶地域
        :type Region: str
        """
        self._Domain = None
        self._CertId = None
        self._Status = None
        self._Bucket = None
        self._Region = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """已绑定的证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """ENABLED: 域名上线状态
DISABLED:域名下线状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bucket(self):
        """存储桶名称
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        """存储桶地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateBindResourceSyncTaskRequest(AbstractModel):
    """CreateCertificateBindResourceSyncTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID列表，总数不能超过100
        :type CertificateIds: list of str
        :param _IsCache: 是否使用缓存， 1使用缓存，0不使用缓存； 默认为1使用缓存； 若当前证书ID存在半小时已完成的任务， 则使用缓存的情况下， 会读取半小时内离当前时间最近的查询结果
        :type IsCache: int
        """
        self._CertificateIds = None
        self._IsCache = None

    @property
    def CertificateIds(self):
        """证书ID列表，总数不能超过100
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def IsCache(self):
        """是否使用缓存， 1使用缓存，0不使用缓存； 默认为1使用缓存； 若当前证书ID存在半小时已完成的任务， 则使用缓存的情况下， 会读取半小时内离当前时间最近的查询结果
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._IsCache = params.get("IsCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateBindResourceSyncTaskResponse(AbstractModel):
    """CreateCertificateBindResourceSyncTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertTaskIds: 证书关联云资源异步任务ID列表
        :type CertTaskIds: list of CertTaskId
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertTaskIds = None
        self._RequestId = None

    @property
    def CertTaskIds(self):
        """证书关联云资源异步任务ID列表
        :rtype: list of CertTaskId
        """
        return self._CertTaskIds

    @CertTaskIds.setter
    def CertTaskIds(self, CertTaskIds):
        self._CertTaskIds = CertTaskIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertTaskIds") is not None:
            self._CertTaskIds = []
            for item in params.get("CertTaskIds"):
                obj = CertTaskId()
                obj._deserialize(item)
                self._CertTaskIds.append(obj)
        self._RequestId = params.get("RequestId")


class CreateCertificateByPackageRequest(AbstractModel):
    """CreateCertificateByPackage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductPid: 证书产品PID，以下是对每个PID及其对应的证书文字说明：
1. 1022451 - CFCA-增强型(EV)SSL证书
2. 1022449 - CFCA-企业型(OV) SSL证书(通配符)
3. 1022447 - CFCA-企业型(OV)SSL证书
4. 1014028 - DNSPod亚信国密-企业型(OV)通配符证书
5. 1014030 - DNSPod亚信国密-企业型(OV)多域名证书
6. 1014026 - DNSPod亚信国密-企业型(OV)证书
7. 1014022 - DNSPod亚信国密-域名型(DV)通配符证书
8. 1014024 - DNSPod亚信国密-域名型(DV)多域名证书
9. 1014020 - DNSPod亚信国密-域名型(DV)证书
10. 1013949 - DNSPod SSL 域名型SSL证书(C1)
11. 1013953 - DNSPod SSL域名型多域名SSL证书(C1)
12. 1013951 - DNSPod-SSL域名型DV（泛域名）
13. 1013955 - DNSPod 企业型SSL证书(C1)
14. 1013959 - DNSPod 企业型多域名SSL证书(C1)
15. 1013957 - DNSPod 企业型通配符SSL证书(C1)
16. 1013961 - DNSPod 增强型 SSL 证书(C1)
17. 1013963 - DNSPod 增强型多域名SSL证书(C1)
18. 1005919 - TrustAsia-域名型DV（通配符多域名）
19. 1013882 - SecureSite-增强型专业版EVPro（多域名）
20. 1018559 - SecureSite-增强型专业版EVPro（单域名）
21. 1013910 - GlobalSign-增强型EV（多域名）
22. 1013904 - GlobalSign-增强型EV（单域名）
23. 1013898 - TrustAsia-增强型EV（多域名）
24. 1013888 - TrustAsia-增强型EV（单域名）
25. 1013886 - GeoTrust-增强型EV（多域名）
26. 1018529 - GeoTrust-增强型EV（单域名）
27. 1013880 - SecureSite-增强型EV（多域名）
28. 1018557 - SecureSite-增强型EV（单域名）
29. 1018586 - TrustAsia-域名型DV（泛域名）
30. 1018584 - TrustAsia-域名型DV（多域名）
31. 1013878 - SecureSite-企业型专业版OV Pro（多域名）
32. 1018582 - SecureSite-企业型专业版OV Pro（单域名）
33. 1013908 - GlobalSign-企业型OV（通配符多域名）
34. 1013902 - GlobalSign-企业型OV（泛域名）
35. 1013906 - GlobalSign-企业型OV（多域名）
36. 1013900 - GlobalSign-企业型OV（单域名）
37. 1013896 - TrustAsia-企业型OV（通配符多域名）
38. 1013892 - TrustAsia-企业型OV（泛域名）
39. 1013894 - TrustAsia-企业型OV（多域名）
40. 1013890 - TrustAsia-企业型OV（单域名）
41. 1004360 - GeoTrust-企业型OV（泛域名）
42. 1013884 - GeoTrust-企业型OV（单域名）
43. 1013874 - SecureSite-企业型OV（泛域名）
44. 1013876 - SecureSite-企业型OV（多域名）
45. 1018580 - SecureSite-企业型OV（单域名）
46. 1004460 - DNSPod-国密增强型证书（多域名）
47. 1004458 - DNSPod-国密增强型证书
48. 1004370 - DNSPod-国密企业型证书（通配符）
49. 1004368 - DNSPod-国密企业型证书（多域名）
50. 1004366 - DNSPod-国密企业型证书
51. 1004362 - DNSPod-国密域名型证书（通配符）
52. 1004364 - DNSPod-国密域名型证书（多域名）
53. 1004358 - DNSPod-国密域名型证书
54. 1004456 - WoTrus-增强型证书（多域名）
55. 1004454 - WoTrus-增强型证书
56. 1004168 - WoTrus-企业型证书（通配符）
57. 1004166 - WoTrus-企业型证书（多域名）
58. 1004164 - WoTrus-企业型证书
59. 1004159 - WoTrus-域名型证书（通配符）
60. 1004161 - WoTrus-域名型证书（多域名）
61. 1004157 - WoTrus-域名型证书
        :type ProductPid: int
        :param _PackageIds: 要消耗的权益包ID。
        :type PackageIds: list of str
        :param _DomainCount: 证书域名数量。
        :type DomainCount: str
        :param _Period: 多年期证书年限。
        :type Period: int
        :param _OldCertificateId: 要续费的原证书ID（续费时填写）。
        :type OldCertificateId: str
        :param _RenewGenCsrMethod: 续费时CSR生成方式（original、upload、online）。
        :type RenewGenCsrMethod: str
        :param _RenewCsr: 续费时选择上传CSR时填写CSR。
        :type RenewCsr: str
        :param _RenewAlgorithmType: 续费证书CSR的算法类型：RSA,ECC,SM2
        :type RenewAlgorithmType: str
        :param _RenewAlgorithmParam: 续费证书CSR的算法参数:2048,4096,prime256v1
        :type RenewAlgorithmParam: str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _Tags: 标签。
        :type Tags: list of Tags
        :param _RenewKeyPass: 续费证书的私钥密码。
        :type RenewKeyPass: str
        :param _DomainNames: 批量购买证书时预填写的域名。
        :type DomainNames: str
        :param _CertificateCount: 批量购买证书数量。
        :type CertificateCount: int
        :param _ManagerId: 预填写的管理人ID。
        :type ManagerId: int
        :param _CompanyId: 预填写的公司ID。
        :type CompanyId: int
        :param _VerifyType: 验证方式
        :type VerifyType: str
        :param _PriceKey: 询价参数，以下是对每个询价参数及其对应的证书文字说明：
1. sv_ssl_cost_cfca_ca_ev - CFCA-增强型(EV)SSL证书
2. sv_ssl_cost_cfca_ca_ovwildcard - CFCA-企业型(OV) SSL证书(通配符)
3. sv_ssl_cost_cfca_ca_ov - CFCA-企业型(OV)SSL证书
4. sv_ssl_cost_dnspod_ca_sm2_ovwildcard - DNSPod亚信国密-企业型(OV)通配符证书
5. sv_ssl_cost_dnspod_ca_sm2_ovmultidomain - DNSPod亚信国密-企业型(OV)多域名证书
6. sv_ssl_cost_dnspod_ca_sm2_ov - DNSPod亚信国密-企业型(OV)证书
7. sv_ssl_cost_dnspod_ca_sm2_dvwildcard - DNSPod亚信国密-域名型(DV)通配符证书
8. sv_ssl_cost_dnspod_ca_sm2_dvmultidomain - DNSPod亚信国密-域名型(DV)多域名证书
9. sv_ssl_cost_dnspod_ca_sm2_dv - DNSPod亚信国密-域名型(DV)证书
10. sv_ssl_cost_dnspod_ca_dv - DNSPod SSL 域名型SSL证书(C1)
11. sv_ssl_cost_dnspod_ca_dvmultidomain - DNSPod SSL域名型多域名SSL证书(C1)
12. sv_ssl_cost_dnspod_ca_dvwildcard - DNSPod-SSL域名型DV（泛域名）
13. sv_ssl_cost_dnspod_ca_ov - DNSPod 企业型SSL证书(C1)
14. sv_ssl_cost_dnspod_ca_ovmultidomain - DNSPod 企业型多域名SSL证书(C1)
15. sv_ssl_cost_dnspod_ca_ovwildcard - DNSPod 企业型通配符SSL证书(C1)
16. sv_ssl_cost_dnspod_ca_ev - DNSPod 增强型 SSL 证书(C1)
17. sv_ssl_cost_dnspod_ca_evmultidomain - DNSPod 增强型多域名SSL证书(C1)
18. sv_ssl_cost_trustasia_dvwildcardmulti - TrustAsia-域名型DV（通配符多域名）
19. sv_ssl_cost_securesiteevpromul_sh - SecureSite-增强型专业版EVPro（多域名）
20. sv_ssl_cost_symantec_evpro - SecureSite-增强型专业版EVPro（单域名）
21. sv_ssl_cost_globalsign_ev_mul_sh - GlobalSign-增强型EV（多域名）
22. sv_ssl_cost_globalsign_ev - GlobalSign-增强型EV（单域名）
23. sv_ssl_cost_trustasia_evmultidomain - TrustAsia-增强型EV（多域名）
24. sv_ssl_cost_trustasia_ev - TrustAsia-增强型EV（单域名）
25. sv_ssl_cost_geotrust_evmultidomain - GeoTrust-增强型EV（多域名）
26. sv_ssl_cost_geotrust_ev - GeoTrust-增强型EV（单域名）
27. sv_ssl_cost_symantec_evmultidomain - SecureSite-增强型EV（多域名）
28. sv_ssl_cost_symantec_ev - SecureSite-增强型EV（单域名）
29. sv_ssl_cost_trustasia_dvwildcard - TrustAsia-域名型DV（泛域名）
30. sv_ssl_cost_trustasia_dvmultidomain - TrustAsia-域名型DV（多域名）
31. sv_ssl_cost_symantec_ovpromultidomain - SecureSite-企业型专业版OV Pro（多域名）
32. sv_ssl_cost_symantec_ovpro - SecureSite-企业型专业版OV Pro（单域名）
33. sv_ssl_cost_globalsign_ovwildcardmulti - GlobalSign-企业型OV（通配符多域名）
34. sv_ssl_cost_globalsign_ovwildcard - GlobalSign-企业型OV（泛域名）
35. sv_ssl_cost_globalsign_ovmultidomain - GlobalSign-企业型OV（多域名）
36. sv_ssl_cost_globalsign_ov - GlobalSign-企业型OV（单域名）
37. sv_ssl_cost_trustasia_ovwildcardmulti - TrustAsia-企业型OV（通配符多域名）
38. sv_ssl_cost_trustasia_ovwildcard - TrustAsia-企业型OV（泛域名）
39. sv_ssl_cost_trustasia_ovmultidomain - TrustAsia-企业型OV（多域名）
40. sv_ssl_cost_trustasia_ov - TrustAsia-企业型OV（单域名）
41. sv_ssl_cost_geotrust_ovwildcard - GeoTrust-企业型OV（泛域名）
42. sv_ssl_cost_geotrust_ov - GeoTrust-企业型OV（单域名）
43. sv_ssl_cost_symantec_ovwildcard - SecureSite-企业型OV（泛域名）
44. sv_ssl_cost_symantec_ovmultidomain - SecureSite-企业型OV（多域名）
45. sv_ssl_cost_symantec_ov - SecureSite-企业型OV（单域名）
46. sv_ssl_cost_dnspod_evmultidomain - DNSPod-国密增强型证书（多域名）
47. sv_ssl_cost_dnspod_ev - DNSPod-国密增强型证书
48. sv_ssl_cost_dnspod_ovwildcard - DNSPod-国密企业型证书（通配符）
49. sv_ssl_cost_dnspod_ovmultidomain - DNSPod-国密企业型证书（多域名）
50. sv_ssl_cost_dnspod_ov - DNSPod-国密企业型证书
51. sv_ssl_cost_dnspod_dvwildcard - DNSPod-国密域名型证书（通配符）
52. sv_ssl_cost_dnspod_dvmultidomain - DNSPod-国密域名型证书（多域名）
53. sv_ssl_cost_dnspod_dv - DNSPod-国密域名型证书
54. sv_ssl_cost_wotrus_evmultidomain - WoTrus-增强型证书（多域名）
55. sv_ssl_cost_wotrus_ev - WoTrus-增强型证书
56. sv_ssl_cost_wotrus_ovwildcard - WoTrus-企业型证书（通配符）
57. sv_ssl_cost_wotrus_ovmultidomain - WoTrus-企业型证书（多域名）
58. sv_ssl_cost_wotrus_ov - WoTrus-企业型证书
59. sv_ssl_cost_wotrus_dvwildcard - WoTrus-域名型证书（通配符）
60. sv_ssl_cost_wotrus_dvmultidomain - WoTrus-域名型证书（多域名）
61. sv_ssl_cost_wotrus_dv - WoTrus-域名型证书
        :type PriceKey: str
        """
        self._ProductPid = None
        self._PackageIds = None
        self._DomainCount = None
        self._Period = None
        self._OldCertificateId = None
        self._RenewGenCsrMethod = None
        self._RenewCsr = None
        self._RenewAlgorithmType = None
        self._RenewAlgorithmParam = None
        self._ProjectId = None
        self._Tags = None
        self._RenewKeyPass = None
        self._DomainNames = None
        self._CertificateCount = None
        self._ManagerId = None
        self._CompanyId = None
        self._VerifyType = None
        self._PriceKey = None

    @property
    def ProductPid(self):
        """证书产品PID，以下是对每个PID及其对应的证书文字说明：
1. 1022451 - CFCA-增强型(EV)SSL证书
2. 1022449 - CFCA-企业型(OV) SSL证书(通配符)
3. 1022447 - CFCA-企业型(OV)SSL证书
4. 1014028 - DNSPod亚信国密-企业型(OV)通配符证书
5. 1014030 - DNSPod亚信国密-企业型(OV)多域名证书
6. 1014026 - DNSPod亚信国密-企业型(OV)证书
7. 1014022 - DNSPod亚信国密-域名型(DV)通配符证书
8. 1014024 - DNSPod亚信国密-域名型(DV)多域名证书
9. 1014020 - DNSPod亚信国密-域名型(DV)证书
10. 1013949 - DNSPod SSL 域名型SSL证书(C1)
11. 1013953 - DNSPod SSL域名型多域名SSL证书(C1)
12. 1013951 - DNSPod-SSL域名型DV（泛域名）
13. 1013955 - DNSPod 企业型SSL证书(C1)
14. 1013959 - DNSPod 企业型多域名SSL证书(C1)
15. 1013957 - DNSPod 企业型通配符SSL证书(C1)
16. 1013961 - DNSPod 增强型 SSL 证书(C1)
17. 1013963 - DNSPod 增强型多域名SSL证书(C1)
18. 1005919 - TrustAsia-域名型DV（通配符多域名）
19. 1013882 - SecureSite-增强型专业版EVPro（多域名）
20. 1018559 - SecureSite-增强型专业版EVPro（单域名）
21. 1013910 - GlobalSign-增强型EV（多域名）
22. 1013904 - GlobalSign-增强型EV（单域名）
23. 1013898 - TrustAsia-增强型EV（多域名）
24. 1013888 - TrustAsia-增强型EV（单域名）
25. 1013886 - GeoTrust-增强型EV（多域名）
26. 1018529 - GeoTrust-增强型EV（单域名）
27. 1013880 - SecureSite-增强型EV（多域名）
28. 1018557 - SecureSite-增强型EV（单域名）
29. 1018586 - TrustAsia-域名型DV（泛域名）
30. 1018584 - TrustAsia-域名型DV（多域名）
31. 1013878 - SecureSite-企业型专业版OV Pro（多域名）
32. 1018582 - SecureSite-企业型专业版OV Pro（单域名）
33. 1013908 - GlobalSign-企业型OV（通配符多域名）
34. 1013902 - GlobalSign-企业型OV（泛域名）
35. 1013906 - GlobalSign-企业型OV（多域名）
36. 1013900 - GlobalSign-企业型OV（单域名）
37. 1013896 - TrustAsia-企业型OV（通配符多域名）
38. 1013892 - TrustAsia-企业型OV（泛域名）
39. 1013894 - TrustAsia-企业型OV（多域名）
40. 1013890 - TrustAsia-企业型OV（单域名）
41. 1004360 - GeoTrust-企业型OV（泛域名）
42. 1013884 - GeoTrust-企业型OV（单域名）
43. 1013874 - SecureSite-企业型OV（泛域名）
44. 1013876 - SecureSite-企业型OV（多域名）
45. 1018580 - SecureSite-企业型OV（单域名）
46. 1004460 - DNSPod-国密增强型证书（多域名）
47. 1004458 - DNSPod-国密增强型证书
48. 1004370 - DNSPod-国密企业型证书（通配符）
49. 1004368 - DNSPod-国密企业型证书（多域名）
50. 1004366 - DNSPod-国密企业型证书
51. 1004362 - DNSPod-国密域名型证书（通配符）
52. 1004364 - DNSPod-国密域名型证书（多域名）
53. 1004358 - DNSPod-国密域名型证书
54. 1004456 - WoTrus-增强型证书（多域名）
55. 1004454 - WoTrus-增强型证书
56. 1004168 - WoTrus-企业型证书（通配符）
57. 1004166 - WoTrus-企业型证书（多域名）
58. 1004164 - WoTrus-企业型证书
59. 1004159 - WoTrus-域名型证书（通配符）
60. 1004161 - WoTrus-域名型证书（多域名）
61. 1004157 - WoTrus-域名型证书
        :rtype: int
        """
        return self._ProductPid

    @ProductPid.setter
    def ProductPid(self, ProductPid):
        self._ProductPid = ProductPid

    @property
    def PackageIds(self):
        """要消耗的权益包ID。
        :rtype: list of str
        """
        return self._PackageIds

    @PackageIds.setter
    def PackageIds(self, PackageIds):
        self._PackageIds = PackageIds

    @property
    def DomainCount(self):
        """证书域名数量。
        :rtype: str
        """
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def Period(self):
        """多年期证书年限。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def OldCertificateId(self):
        """要续费的原证书ID（续费时填写）。
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def RenewGenCsrMethod(self):
        """续费时CSR生成方式（original、upload、online）。
        :rtype: str
        """
        return self._RenewGenCsrMethod

    @RenewGenCsrMethod.setter
    def RenewGenCsrMethod(self, RenewGenCsrMethod):
        self._RenewGenCsrMethod = RenewGenCsrMethod

    @property
    def RenewCsr(self):
        """续费时选择上传CSR时填写CSR。
        :rtype: str
        """
        return self._RenewCsr

    @RenewCsr.setter
    def RenewCsr(self, RenewCsr):
        self._RenewCsr = RenewCsr

    @property
    def RenewAlgorithmType(self):
        """续费证书CSR的算法类型：RSA,ECC,SM2
        :rtype: str
        """
        return self._RenewAlgorithmType

    @RenewAlgorithmType.setter
    def RenewAlgorithmType(self, RenewAlgorithmType):
        self._RenewAlgorithmType = RenewAlgorithmType

    @property
    def RenewAlgorithmParam(self):
        """续费证书CSR的算法参数:2048,4096,prime256v1
        :rtype: str
        """
        return self._RenewAlgorithmParam

    @RenewAlgorithmParam.setter
    def RenewAlgorithmParam(self, RenewAlgorithmParam):
        self._RenewAlgorithmParam = RenewAlgorithmParam

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Tags(self):
        """标签。
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RenewKeyPass(self):
        """续费证书的私钥密码。
        :rtype: str
        """
        return self._RenewKeyPass

    @RenewKeyPass.setter
    def RenewKeyPass(self, RenewKeyPass):
        self._RenewKeyPass = RenewKeyPass

    @property
    def DomainNames(self):
        """批量购买证书时预填写的域名。
        :rtype: str
        """
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames

    @property
    def CertificateCount(self):
        """批量购买证书数量。
        :rtype: int
        """
        return self._CertificateCount

    @CertificateCount.setter
    def CertificateCount(self, CertificateCount):
        self._CertificateCount = CertificateCount

    @property
    def ManagerId(self):
        """预填写的管理人ID。
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def CompanyId(self):
        """预填写的公司ID。
        :rtype: int
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def VerifyType(self):
        """验证方式
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def PriceKey(self):
        """询价参数，以下是对每个询价参数及其对应的证书文字说明：
1. sv_ssl_cost_cfca_ca_ev - CFCA-增强型(EV)SSL证书
2. sv_ssl_cost_cfca_ca_ovwildcard - CFCA-企业型(OV) SSL证书(通配符)
3. sv_ssl_cost_cfca_ca_ov - CFCA-企业型(OV)SSL证书
4. sv_ssl_cost_dnspod_ca_sm2_ovwildcard - DNSPod亚信国密-企业型(OV)通配符证书
5. sv_ssl_cost_dnspod_ca_sm2_ovmultidomain - DNSPod亚信国密-企业型(OV)多域名证书
6. sv_ssl_cost_dnspod_ca_sm2_ov - DNSPod亚信国密-企业型(OV)证书
7. sv_ssl_cost_dnspod_ca_sm2_dvwildcard - DNSPod亚信国密-域名型(DV)通配符证书
8. sv_ssl_cost_dnspod_ca_sm2_dvmultidomain - DNSPod亚信国密-域名型(DV)多域名证书
9. sv_ssl_cost_dnspod_ca_sm2_dv - DNSPod亚信国密-域名型(DV)证书
10. sv_ssl_cost_dnspod_ca_dv - DNSPod SSL 域名型SSL证书(C1)
11. sv_ssl_cost_dnspod_ca_dvmultidomain - DNSPod SSL域名型多域名SSL证书(C1)
12. sv_ssl_cost_dnspod_ca_dvwildcard - DNSPod-SSL域名型DV（泛域名）
13. sv_ssl_cost_dnspod_ca_ov - DNSPod 企业型SSL证书(C1)
14. sv_ssl_cost_dnspod_ca_ovmultidomain - DNSPod 企业型多域名SSL证书(C1)
15. sv_ssl_cost_dnspod_ca_ovwildcard - DNSPod 企业型通配符SSL证书(C1)
16. sv_ssl_cost_dnspod_ca_ev - DNSPod 增强型 SSL 证书(C1)
17. sv_ssl_cost_dnspod_ca_evmultidomain - DNSPod 增强型多域名SSL证书(C1)
18. sv_ssl_cost_trustasia_dvwildcardmulti - TrustAsia-域名型DV（通配符多域名）
19. sv_ssl_cost_securesiteevpromul_sh - SecureSite-增强型专业版EVPro（多域名）
20. sv_ssl_cost_symantec_evpro - SecureSite-增强型专业版EVPro（单域名）
21. sv_ssl_cost_globalsign_ev_mul_sh - GlobalSign-增强型EV（多域名）
22. sv_ssl_cost_globalsign_ev - GlobalSign-增强型EV（单域名）
23. sv_ssl_cost_trustasia_evmultidomain - TrustAsia-增强型EV（多域名）
24. sv_ssl_cost_trustasia_ev - TrustAsia-增强型EV（单域名）
25. sv_ssl_cost_geotrust_evmultidomain - GeoTrust-增强型EV（多域名）
26. sv_ssl_cost_geotrust_ev - GeoTrust-增强型EV（单域名）
27. sv_ssl_cost_symantec_evmultidomain - SecureSite-增强型EV（多域名）
28. sv_ssl_cost_symantec_ev - SecureSite-增强型EV（单域名）
29. sv_ssl_cost_trustasia_dvwildcard - TrustAsia-域名型DV（泛域名）
30. sv_ssl_cost_trustasia_dvmultidomain - TrustAsia-域名型DV（多域名）
31. sv_ssl_cost_symantec_ovpromultidomain - SecureSite-企业型专业版OV Pro（多域名）
32. sv_ssl_cost_symantec_ovpro - SecureSite-企业型专业版OV Pro（单域名）
33. sv_ssl_cost_globalsign_ovwildcardmulti - GlobalSign-企业型OV（通配符多域名）
34. sv_ssl_cost_globalsign_ovwildcard - GlobalSign-企业型OV（泛域名）
35. sv_ssl_cost_globalsign_ovmultidomain - GlobalSign-企业型OV（多域名）
36. sv_ssl_cost_globalsign_ov - GlobalSign-企业型OV（单域名）
37. sv_ssl_cost_trustasia_ovwildcardmulti - TrustAsia-企业型OV（通配符多域名）
38. sv_ssl_cost_trustasia_ovwildcard - TrustAsia-企业型OV（泛域名）
39. sv_ssl_cost_trustasia_ovmultidomain - TrustAsia-企业型OV（多域名）
40. sv_ssl_cost_trustasia_ov - TrustAsia-企业型OV（单域名）
41. sv_ssl_cost_geotrust_ovwildcard - GeoTrust-企业型OV（泛域名）
42. sv_ssl_cost_geotrust_ov - GeoTrust-企业型OV（单域名）
43. sv_ssl_cost_symantec_ovwildcard - SecureSite-企业型OV（泛域名）
44. sv_ssl_cost_symantec_ovmultidomain - SecureSite-企业型OV（多域名）
45. sv_ssl_cost_symantec_ov - SecureSite-企业型OV（单域名）
46. sv_ssl_cost_dnspod_evmultidomain - DNSPod-国密增强型证书（多域名）
47. sv_ssl_cost_dnspod_ev - DNSPod-国密增强型证书
48. sv_ssl_cost_dnspod_ovwildcard - DNSPod-国密企业型证书（通配符）
49. sv_ssl_cost_dnspod_ovmultidomain - DNSPod-国密企业型证书（多域名）
50. sv_ssl_cost_dnspod_ov - DNSPod-国密企业型证书
51. sv_ssl_cost_dnspod_dvwildcard - DNSPod-国密域名型证书（通配符）
52. sv_ssl_cost_dnspod_dvmultidomain - DNSPod-国密域名型证书（多域名）
53. sv_ssl_cost_dnspod_dv - DNSPod-国密域名型证书
54. sv_ssl_cost_wotrus_evmultidomain - WoTrus-增强型证书（多域名）
55. sv_ssl_cost_wotrus_ev - WoTrus-增强型证书
56. sv_ssl_cost_wotrus_ovwildcard - WoTrus-企业型证书（通配符）
57. sv_ssl_cost_wotrus_ovmultidomain - WoTrus-企业型证书（多域名）
58. sv_ssl_cost_wotrus_ov - WoTrus-企业型证书
59. sv_ssl_cost_wotrus_dvwildcard - WoTrus-域名型证书（通配符）
60. sv_ssl_cost_wotrus_dvmultidomain - WoTrus-域名型证书（多域名）
61. sv_ssl_cost_wotrus_dv - WoTrus-域名型证书
        :rtype: str
        """
        return self._PriceKey

    @PriceKey.setter
    def PriceKey(self, PriceKey):
        self._PriceKey = PriceKey


    def _deserialize(self, params):
        self._ProductPid = params.get("ProductPid")
        self._PackageIds = params.get("PackageIds")
        self._DomainCount = params.get("DomainCount")
        self._Period = params.get("Period")
        self._OldCertificateId = params.get("OldCertificateId")
        self._RenewGenCsrMethod = params.get("RenewGenCsrMethod")
        self._RenewCsr = params.get("RenewCsr")
        self._RenewAlgorithmType = params.get("RenewAlgorithmType")
        self._RenewAlgorithmParam = params.get("RenewAlgorithmParam")
        self._ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RenewKeyPass = params.get("RenewKeyPass")
        self._DomainNames = params.get("DomainNames")
        self._CertificateCount = params.get("CertificateCount")
        self._ManagerId = params.get("ManagerId")
        self._CompanyId = params.get("CompanyId")
        self._VerifyType = params.get("VerifyType")
        self._PriceKey = params.get("PriceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateByPackageResponse(AbstractModel):
    """CreateCertificateByPackage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        :param _CertificateIds: 批量购买证书时返回多个证书ID。
        :type CertificateIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._CertificateIds = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateIds(self):
        """批量购买证书时返回多个证书ID。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateIds = params.get("CertificateIds")
        self._RequestId = params.get("RequestId")


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 证书套餐类型：
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书，不支持多年期
100：CFCA 企业型通配符(OV)SSL证书，不支持多年期
101：CFCA 增强型(EV)SSL证书，不支持多年期
102:  Rapid-域名型(DV)SSL证书
103: Rapid-域名型(DV)SSL证书(通配符)
104: TrustAsia-域名型(单域名)
105: SSL单域名证书(一年期)
        :type ProductId: int
        :param _DomainNum: 证书包含的域名数量。 多域名或者多泛域名证书类型必须大于1
        :type DomainNum: int
        :param _TimeSpan: 证书年限。 支持多年期的证书才可以大于1年
        :type TimeSpan: int
        :param _AutoVoucher: 是否自动使用代金券：1是，0否；默认为1
        :type AutoVoucher: int
        :param _Tags: 标签， 生成证书打标签
        :type Tags: list of Tags
        """
        self._ProductId = None
        self._DomainNum = None
        self._TimeSpan = None
        self._AutoVoucher = None
        self._Tags = None

    @property
    def ProductId(self):
        """证书套餐类型：
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书，不支持多年期
100：CFCA 企业型通配符(OV)SSL证书，不支持多年期
101：CFCA 增强型(EV)SSL证书，不支持多年期
102:  Rapid-域名型(DV)SSL证书
103: Rapid-域名型(DV)SSL证书(通配符)
104: TrustAsia-域名型(单域名)
105: SSL单域名证书(一年期)
        :rtype: int
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DomainNum(self):
        """证书包含的域名数量。 多域名或者多泛域名证书类型必须大于1
        :rtype: int
        """
        return self._DomainNum

    @DomainNum.setter
    def DomainNum(self, DomainNum):
        self._DomainNum = DomainNum

    @property
    def TimeSpan(self):
        """证书年限。 支持多年期的证书才可以大于1年
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def AutoVoucher(self):
        """是否自动使用代金券：1是，0否；默认为1
        :rtype: int
        """
        return self._AutoVoucher

    @AutoVoucher.setter
    def AutoVoucher(self, AutoVoucher):
        self._AutoVoucher = AutoVoucher

    @property
    def Tags(self):
        """标签， 生成证书打标签
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DomainNum = params.get("DomainNum")
        self._TimeSpan = params.get("TimeSpan")
        self._AutoVoucher = params.get("AutoVoucher")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID列表
        :type CertificateIds: list of str
        :param _DealIds: 订单号列表
        :type DealIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateIds = None
        self._DealIds = None
        self._RequestId = None

    @property
    def CertificateIds(self):
        """证书ID列表
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def DealIds(self):
        """订单号列表
        :rtype: list of str
        """
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._DealIds = params.get("DealIds")
        self._RequestId = params.get("RequestId")


class DdosInstanceDetail(AbstractModel):
    """ddos复杂类型

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Protocol: 协议类型
        :type Protocol: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _VirtualPort: 转发端口
        :type VirtualPort: str
        """
        self._Domain = None
        self._InstanceId = None
        self._Protocol = None
        self._CertId = None
        self._VirtualPort = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Protocol(self):
        """协议类型
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def VirtualPort(self):
        """转发端口
        :rtype: str
        """
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._InstanceId = params.get("InstanceId")
        self._Protocol = params.get("Protocol")
        self._CertId = params.get("CertId")
        self._VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DdosInstanceList(AbstractModel):
    """ddos实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该地域下ddos域名总数	
        :type TotalCount: int
        :param _InstanceList: ddos实例详情	
        :type InstanceList: list of DdosInstanceDetail
        :param _Error: 是否查询异常
        :type Error: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._Error = None

    @property
    def TotalCount(self):
        """该地域下ddos域名总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """ddos实例详情	
        :rtype: list of DdosInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def Error(self):
        """是否查询异常
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = DdosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _IsCheckResource: 删除时是否检查证书关联了云资源。默认不检查。如选择检查(需要授权服务角色SSL_QCSLinkedRoleInReplaceLoadCertificate)删除将变成异步,接口会返回异步任务ID。需使用DescribeDeleteCertificatesTaskResult接口查询删除是否成功。
        :type IsCheckResource: bool
        """
        self._CertificateId = None
        self._IsCheckResource = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCheckResource(self):
        """删除时是否检查证书关联了云资源。默认不检查。如选择检查(需要授权服务角色SSL_QCSLinkedRoleInReplaceLoadCertificate)删除将变成异步,接口会返回异步任务ID。需使用DescribeDeleteCertificatesTaskResult接口查询删除是否成功。
        :rtype: bool
        """
        return self._IsCheckResource

    @IsCheckResource.setter
    def IsCheckResource(self, IsCheckResource):
        self._IsCheckResource = IsCheckResource


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCheckResource = params.get("IsCheckResource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteResult: 删除结果（true：删除成功，false：删除失败）
        :type DeleteResult: bool
        :param _TaskId: 异步删除的任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteResult = None
        self._TaskId = None
        self._RequestId = None

    @property
    def DeleteResult(self):
        """删除结果（true：删除成功，false：删除失败）
        :rtype: bool
        """
        return self._DeleteResult

    @DeleteResult.setter
    def DeleteResult(self, DeleteResult):
        self._DeleteResult = DeleteResult

    @property
    def TaskId(self):
        """异步删除的任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeleteResult = params.get("DeleteResult")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCertificatesRequest(AbstractModel):
    """DeleteCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 要删除的证书ID。单次最多100个
        :type CertificateIds: list of str
        :param _IsSync: 删除时是否检查证书关联了云资源。默认不检查。如需要检查关联云资源 (需授权服务角色SSL_QCSLinkedRoleInReplaceLoadCertificate)，完成授权后且该参数传true，删除将变成异步任务，接口会返回异步任务ID。需搭配 DescribeDeleteCertificatesTaskResult接口使用，查询删除任务是否成功。
        :type IsSync: bool
        """
        self._CertificateIds = None
        self._IsSync = None

    @property
    def CertificateIds(self):
        """要删除的证书ID。单次最多100个
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def IsSync(self):
        """删除时是否检查证书关联了云资源。默认不检查。如需要检查关联云资源 (需授权服务角色SSL_QCSLinkedRoleInReplaceLoadCertificate)，完成授权后且该参数传true，删除将变成异步任务，接口会返回异步任务ID。需搭配 DescribeDeleteCertificatesTaskResult接口使用，查询删除任务是否成功。
        :rtype: bool
        """
        return self._IsSync

    @IsSync.setter
    def IsSync(self, IsSync):
        self._IsSync = IsSync


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._IsSync = params.get("IsSync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificatesResponse(AbstractModel):
    """DeleteCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功的ID
        :type Success: list of str
        :param _Fail: 失败的ID和原因
        :type Fail: list of BatchDeleteFail
        :param _CertTaskIds: 证书ID和异步任务的ID
        :type CertTaskIds: list of CertTaskId
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._Fail = None
        self._CertTaskIds = None
        self._RequestId = None

    @property
    def Success(self):
        """成功的ID
        :rtype: list of str
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def Fail(self):
        """失败的ID和原因
        :rtype: list of BatchDeleteFail
        """
        return self._Fail

    @Fail.setter
    def Fail(self, Fail):
        self._Fail = Fail

    @property
    def CertTaskIds(self):
        """证书ID和异步任务的ID
        :rtype: list of CertTaskId
        """
        return self._CertTaskIds

    @CertTaskIds.setter
    def CertTaskIds(self, CertTaskIds):
        self._CertTaskIds = CertTaskIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Success = params.get("Success")
        if params.get("Fail") is not None:
            self._Fail = []
            for item in params.get("Fail"):
                obj = BatchDeleteFail()
                obj._deserialize(item)
                self._Fail.append(obj)
        if params.get("CertTaskIds") is not None:
            self._CertTaskIds = []
            for item in params.get("CertTaskIds"):
                obj = CertTaskId()
                obj._deserialize(item)
                self._CertTaskIds.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteManagerRequest(AbstractModel):
    """DeleteManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        """
        self._ManagerId = None

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteManagerResponse(AbstractModel):
    """DeleteManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ManagerId = None
        self._RequestId = None

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._RequestId = params.get("RequestId")


class DeleteTaskResult(AbstractModel):
    """批量删除证书异步任务结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _Status: 异步查询结果： 0表示任务进行中、 1表示任务成功、 2表示任务失败、3表示未授权服务角色导致任务失败、4表示有未解绑的云资源导致任务失败、5表示查询关联云资源超时导致任务失败
        :type Status: int
        :param _Error: 错误信息
        :type Error: str
        :param _CacheTime: 当前结果缓存时间
        :type CacheTime: str
        :param _Domains: 包含的域名
        :type Domains: list of str
        """
        self._TaskId = None
        self._CertId = None
        self._Status = None
        self._Error = None
        self._CacheTime = None
        self._Domains = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """异步查询结果： 0表示任务进行中、 1表示任务成功、 2表示任务失败、3表示未授权服务角色导致任务失败、4表示有未解绑的云资源导致任务失败、5表示查询关联云资源超时导致任务失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Error(self):
        """错误信息
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def CacheTime(self):
        """当前结果缓存时间
        :rtype: str
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def Domains(self):
        """包含的域名
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        self._Error = params.get("Error")
        self._CacheTime = params.get("CacheTime")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateInstanceRequest(AbstractModel):
    """DeployCertificateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _InstanceIdList: 证书部署的实例列表，不同云资源类型如下
- clb：若监听器开启了SNI，则需要指定到域名LoadBalancerId|ListenerId|Domain，例：["lb-bid2fs4g|lbl-a8af11gs|tencent.com"]，若监听器未开启SNI或者为四层监听器，则指定到监听器，例：["lb-bid2fs4g|lbl-1c6rp5eo"]
- cdn：Domain|计费开关，例：["cdn2.tencent.com|off", "cdn.tencent.com|on"]
- ddos：InsId|Domain|VirtualPort，例：["bgpip-000001ms|tencent.com|443"]
- live：Domain，例：["live1.tencent.com", "live2.tencent.com"]
- vod：Domain， 例：["vod1.tencent.com", "vod2.tencent.com"]
- waf：Domain， 例：["waf1.tencent.com", "waf2.tencent.com"]
- apigateway：ServiceId|Domain， 例：["service-8sk7cqmd|apigw1.tencent.com", "service-8sk7cqmd|apigw2.ninghhuang.online"]
- teo：Domain， 例：["edgeone1.tencent.com", "edgeone2.tencent.com"]
- tke：ClusterId|NameSpace|SecretName， 例：["cls-42sa0ae0|default|test-tencent"]
- cos：Region|Bucket|Domain， 例：["ap-hongkong|ssl-server-1251810746|tencent.com"]
- lighthouse：Region|InstanceId|Domain， 例：["ap-shanghai|lhins-nh7lql34|tencent.com"]
- tse：GatewayId|CertificateId， 例：["gateway-s1da9151|fa61bc05-cc54-4eea-c932-24de52577372"]
- tcb：Type|Region|EnvId|Domain， 例：["AccessService|ap-shanghai|ceshi-4s5h0ymg11c839c7|tencent.com"]

        :type InstanceIdList: list of str
        :param _ResourceType: 证书部署云资源支持的云资源类型， 不传则默认部署clb：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- lighthouse
- tse
- tcb
<dx-alert infotype="explain" title="">当云资源类型传入clb、waf、apigateway、cos、lighthouse、tke、tse、tcb 时，公共参数Region必传。</dx-alert>
        :type ResourceType: str
        :param _Status: 部署云资源状态：
云直播：
-1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :type Status: int
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，默认缓存半小时
        :type IsCache: int
        """
        self._CertificateId = None
        self._InstanceIdList = None
        self._ResourceType = None
        self._Status = None
        self._IsCache = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def InstanceIdList(self):
        """证书部署的实例列表，不同云资源类型如下
- clb：若监听器开启了SNI，则需要指定到域名LoadBalancerId|ListenerId|Domain，例：["lb-bid2fs4g|lbl-a8af11gs|tencent.com"]，若监听器未开启SNI或者为四层监听器，则指定到监听器，例：["lb-bid2fs4g|lbl-1c6rp5eo"]
- cdn：Domain|计费开关，例：["cdn2.tencent.com|off", "cdn.tencent.com|on"]
- ddos：InsId|Domain|VirtualPort，例：["bgpip-000001ms|tencent.com|443"]
- live：Domain，例：["live1.tencent.com", "live2.tencent.com"]
- vod：Domain， 例：["vod1.tencent.com", "vod2.tencent.com"]
- waf：Domain， 例：["waf1.tencent.com", "waf2.tencent.com"]
- apigateway：ServiceId|Domain， 例：["service-8sk7cqmd|apigw1.tencent.com", "service-8sk7cqmd|apigw2.ninghhuang.online"]
- teo：Domain， 例：["edgeone1.tencent.com", "edgeone2.tencent.com"]
- tke：ClusterId|NameSpace|SecretName， 例：["cls-42sa0ae0|default|test-tencent"]
- cos：Region|Bucket|Domain， 例：["ap-hongkong|ssl-server-1251810746|tencent.com"]
- lighthouse：Region|InstanceId|Domain， 例：["ap-shanghai|lhins-nh7lql34|tencent.com"]
- tse：GatewayId|CertificateId， 例：["gateway-s1da9151|fa61bc05-cc54-4eea-c932-24de52577372"]
- tcb：Type|Region|EnvId|Domain， 例：["AccessService|ap-shanghai|ceshi-4s5h0ymg11c839c7|tencent.com"]

        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def ResourceType(self):
        """证书部署云资源支持的云资源类型， 不传则默认部署clb：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- lighthouse
- tse
- tcb
<dx-alert infotype="explain" title="">当云资源类型传入clb、waf、apigateway、cos、lighthouse、tke、tse、tcb 时，公共参数Region必传。</dx-alert>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        """部署云资源状态：
云直播：
-1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，默认缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._InstanceIdList = params.get("InstanceIdList")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._IsCache = params.get("IsCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateInstanceResponse(AbstractModel):
    """DeployCertificateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 云资源部署任务ID
        :type DeployRecordId: int
        :param _DeployStatus: 部署任务创建状态；1表示创建成功； 0表示当前存在部署中的任务，未创建新的部署任务；返回值DeployRecordId为部署中的任务ID
        :type DeployStatus: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._DeployStatus = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        """云资源部署任务ID
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployStatus(self):
        """部署任务创建状态；1表示创建成功； 0表示当前存在部署中的任务，未创建新的部署任务；返回值DeployRecordId为部署中的任务ID
        :rtype: int
        """
        return self._DeployStatus

    @DeployStatus.setter
    def DeployStatus(self, DeployStatus):
        self._DeployStatus = DeployStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployStatus = params.get("DeployStatus")
        self._RequestId = params.get("RequestId")


class DeployCertificateRecordRetryRequest(AbstractModel):
    """DeployCertificateRecordRetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待重试部署记录ID，通过DeployCertificateInstance获得
        :type DeployRecordId: int
        :param _DeployRecordDetailId: 待重试部署记录详情ID，通过DescribeHostDeployRecordDetail获得
        :type DeployRecordDetailId: int
        """
        self._DeployRecordId = None
        self._DeployRecordDetailId = None

    @property
    def DeployRecordId(self):
        """待重试部署记录ID，通过DeployCertificateInstance获得
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployRecordDetailId(self):
        """待重试部署记录详情ID，通过DescribeHostDeployRecordDetail获得
        :rtype: int
        """
        return self._DeployRecordDetailId

    @DeployRecordDetailId.setter
    def DeployRecordDetailId(self, DeployRecordDetailId):
        self._DeployRecordDetailId = DeployRecordDetailId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployRecordDetailId = params.get("DeployRecordDetailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateRecordRetryResponse(AbstractModel):
    """DeployCertificateRecordRetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeployCertificateRecordRollbackRequest(AbstractModel):
    """DeployCertificateRecordRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待重试部署记录ID, 就是通过DeployCertificateInstance返回的DeployRecordId
        :type DeployRecordId: int
        """
        self._DeployRecordId = None

    @property
    def DeployRecordId(self):
        """待重试部署记录ID, 就是通过DeployCertificateInstance返回的DeployRecordId
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateRecordRollbackResponse(AbstractModel):
    """DeployCertificateRecordRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 回滚部署记录ID
        :type DeployRecordId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        """回滚部署记录ID
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._RequestId = params.get("RequestId")


class DeployRecordDetail(AbstractModel):
    """部署记录详情

    """

    def __init__(self):
        r"""
        :param _Id: 部署记录详情ID
        :type Id: int
        :param _CertId: 部署证书ID
        :type CertId: str
        :param _OldCertId: 原绑定证书ID
        :type OldCertId: str
        :param _InstanceId: 部署实例ID
        :type InstanceId: str
        :param _InstanceName: 部署实例名称
        :type InstanceName: str
        :param _ListenerId: 部署监听器ID
        :type ListenerId: str
        :param _Domains: 部署域名列表
        :type Domains: list of str
        :param _Protocol: 部署监听器协议
        :type Protocol: str
        :param _Status: 部署状态
        :type Status: int
        :param _ErrorMsg: 部署错误信息
        :type ErrorMsg: str
        :param _CreateTime: 部署记录详情创建时间
        :type CreateTime: str
        :param _UpdateTime: 部署记录详情最后一次更新时间
        :type UpdateTime: str
        :param _ListenerName: 部署监听器名称
        :type ListenerName: str
        :param _SniSwitch: 是否开启SNI
        :type SniSwitch: int
        :param _Bucket: COS存储桶名称
        :type Bucket: str
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _SecretName: secret名称
        :type SecretName: str
        :param _Port: 端口
        :type Port: int
        :param _EnvId: TCB环境ID
        :type EnvId: str
        :param _TCBType: 部署的TCB类型
        :type TCBType: str
        :param _Region: 部署的TCB地域
        :type Region: str
        :param _Url: 部署CLB监听器的Url
        :type Url: list of str
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._InstanceId = None
        self._InstanceName = None
        self._ListenerId = None
        self._Domains = None
        self._Protocol = None
        self._Status = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ListenerName = None
        self._SniSwitch = None
        self._Bucket = None
        self._Namespace = None
        self._SecretName = None
        self._Port = None
        self._EnvId = None
        self._TCBType = None
        self._Region = None
        self._Url = None

    @property
    def Id(self):
        """部署记录详情ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        """部署证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        """原绑定证书ID
        :rtype: str
        """
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def InstanceId(self):
        """部署实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """部署实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ListenerId(self):
        """部署监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domains(self):
        """部署域名列表
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Protocol(self):
        """部署监听器协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Status(self):
        """部署状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        """部署错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        """部署记录详情创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """部署记录详情最后一次更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ListenerName(self):
        """部署监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SniSwitch(self):
        """是否开启SNI
        :rtype: int
        """
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Bucket(self):
        """COS存储桶名称
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Namespace(self):
        """命名空间名称
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def SecretName(self):
        """secret名称
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Port(self):
        """端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def EnvId(self):
        """TCB环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TCBType(self):
        """部署的TCB类型
        :rtype: str
        """
        return self._TCBType

    @TCBType.setter
    def TCBType(self, TCBType):
        self._TCBType = TCBType

    @property
    def Region(self):
        """部署的TCB地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Url(self):
        """部署CLB监听器的Url
        :rtype: list of str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ListenerId = params.get("ListenerId")
        self._Domains = params.get("Domains")
        self._Protocol = params.get("Protocol")
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ListenerName = params.get("ListenerName")
        self._SniSwitch = params.get("SniSwitch")
        self._Bucket = params.get("Bucket")
        self._Namespace = params.get("Namespace")
        self._SecretName = params.get("SecretName")
        self._Port = params.get("Port")
        self._EnvId = params.get("EnvId")
        self._TCBType = params.get("TCBType")
        self._Region = params.get("Region")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployRecordInfo(AbstractModel):
    """部署记录信息

    """

    def __init__(self):
        r"""
        :param _Id: 部署记录ID
        :type Id: int
        :param _CertId: 部署证书ID
        :type CertId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _Region: 部署地域
        :type Region: str
        :param _Status: 部署状态:0 未开始， 1 成功， 2 失败
        :type Status: int
        :param _CreateTime: 部署时间
        :type CreateTime: str
        :param _UpdateTime: 最近一次更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._CertId = None
        self._ResourceType = None
        self._Region = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        """部署记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        """部署证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def ResourceType(self):
        """部署资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Region(self):
        """部署地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        """部署状态:0 未开始， 1 成功， 2 失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """部署时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最近一次更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._ResourceType = params.get("ResourceType")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployedResources(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _Count: 数量
        :type Count: int
        :param _Type: 资源标识:clb,cdn,live,waf,antiddos
        :type Type: str
        :param _ResourceIds: 不建议使用。字段返回和Resources相同。本字段后续只返回null
        :type ResourceIds: list of str
        :param _Resources: 关联资源ID或关联域名。
        :type Resources: list of str
        """
        self._CertificateId = None
        self._Count = None
        self._Type = None
        self._ResourceIds = None
        self._Resources = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Count(self):
        """数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Type(self):
        """资源标识:clb,cdn,live,waf,antiddos
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResourceIds(self):
        """不建议使用。字段返回和Resources相同。本字段后续只返回null
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Resources(self):
        """关联资源ID或关联域名。
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Count = params.get("Count")
        self._Type = params.get("Type")
        self._ResourceIds = params.get("ResourceIds")
        self._Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateBindResourceTaskDetailRequest(AbstractModel):
    """DescribeCertificateBindResourceTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，根据CreateCertificateBindResourceSyncTask得到的任务ID查询绑定云资源结果
        :type TaskId: str
        :param _Limit: 每页展示数量， 默认10，最大值100; 分页总数为云资源地域下实例总数， 即第一页会拉群每个云资源的地域下面Limit数量实例
        :type Limit: str
        :param _Offset: 当前偏移量，默认为0
        :type Offset: str
        :param _ResourceTypes: 查询资源类型的结果详情， 不传则查询所有，取值支持：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- tse
- tcb
        :type ResourceTypes: list of str
        :param _Regions: 查询地域列表的数据，clb、tke、waf、apigateway、tcb、cos、tse支持地域查询， 其他资源类型不支持
        :type Regions: list of str
        """
        self._TaskId = None
        self._Limit = None
        self._Offset = None
        self._ResourceTypes = None
        self._Regions = None

    @property
    def TaskId(self):
        """任务ID，根据CreateCertificateBindResourceSyncTask得到的任务ID查询绑定云资源结果
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Limit(self):
        """每页展示数量， 默认10，最大值100; 分页总数为云资源地域下实例总数， 即第一页会拉群每个云资源的地域下面Limit数量实例
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """当前偏移量，默认为0
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ResourceTypes(self):
        """查询资源类型的结果详情， 不传则查询所有，取值支持：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- tse
- tcb
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        """查询地域列表的数据，clb、tke、waf、apigateway、tcb、cos、tse支持地域查询， 其他资源类型不支持
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ResourceTypes = params.get("ResourceTypes")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateBindResourceTaskDetailResponse(AbstractModel):
    """DescribeCertificateBindResourceTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CLB: 关联clb资源详情	
        :type CLB: list of ClbInstanceList
        :param _CDN: 关联cdn资源详情	
        :type CDN: list of CdnInstanceList
        :param _WAF: 关联waf资源详情	
        :type WAF: list of WafInstanceList
        :param _DDOS: 关联ddos资源详情	
        :type DDOS: list of DdosInstanceList
        :param _LIVE: 关联live资源详情	
        :type LIVE: list of LiveInstanceList
        :param _VOD: 关联vod资源详情	
        :type VOD: list of VODInstanceList
        :param _TKE: 关联tke资源详情	
        :type TKE: list of TkeInstanceList
        :param _APIGATEWAY: 关联apigateway资源详情	
        :type APIGATEWAY: list of ApiGatewayInstanceList
        :param _TCB: 关联tcb资源详情	
        :type TCB: list of TCBInstanceList
        :param _TEO: 关联teo资源详情	
        :type TEO: list of TeoInstanceList
        :param _Status: 关联云资源异步查询结果： 0表示查询中， 1表示查询成功。 2表示查询异常； 若状态为1，则查看BindResourceResult结果；若状态为2，则查看Error原因
        :type Status: int
        :param _CacheTime: 当前结果缓存时间
        :type CacheTime: str
        :param _TSE: 关联tse资源详情	
        :type TSE: list of TSEInstanceList
        :param _COS: 关联的COS资源详情
        :type COS: list of COSInstanceList
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CLB = None
        self._CDN = None
        self._WAF = None
        self._DDOS = None
        self._LIVE = None
        self._VOD = None
        self._TKE = None
        self._APIGATEWAY = None
        self._TCB = None
        self._TEO = None
        self._Status = None
        self._CacheTime = None
        self._TSE = None
        self._COS = None
        self._RequestId = None

    @property
    def CLB(self):
        """关联clb资源详情	
        :rtype: list of ClbInstanceList
        """
        return self._CLB

    @CLB.setter
    def CLB(self, CLB):
        self._CLB = CLB

    @property
    def CDN(self):
        """关联cdn资源详情	
        :rtype: list of CdnInstanceList
        """
        return self._CDN

    @CDN.setter
    def CDN(self, CDN):
        self._CDN = CDN

    @property
    def WAF(self):
        """关联waf资源详情	
        :rtype: list of WafInstanceList
        """
        return self._WAF

    @WAF.setter
    def WAF(self, WAF):
        self._WAF = WAF

    @property
    def DDOS(self):
        """关联ddos资源详情	
        :rtype: list of DdosInstanceList
        """
        return self._DDOS

    @DDOS.setter
    def DDOS(self, DDOS):
        self._DDOS = DDOS

    @property
    def LIVE(self):
        """关联live资源详情	
        :rtype: list of LiveInstanceList
        """
        return self._LIVE

    @LIVE.setter
    def LIVE(self, LIVE):
        self._LIVE = LIVE

    @property
    def VOD(self):
        """关联vod资源详情	
        :rtype: list of VODInstanceList
        """
        return self._VOD

    @VOD.setter
    def VOD(self, VOD):
        self._VOD = VOD

    @property
    def TKE(self):
        """关联tke资源详情	
        :rtype: list of TkeInstanceList
        """
        return self._TKE

    @TKE.setter
    def TKE(self, TKE):
        self._TKE = TKE

    @property
    def APIGATEWAY(self):
        """关联apigateway资源详情	
        :rtype: list of ApiGatewayInstanceList
        """
        return self._APIGATEWAY

    @APIGATEWAY.setter
    def APIGATEWAY(self, APIGATEWAY):
        self._APIGATEWAY = APIGATEWAY

    @property
    def TCB(self):
        """关联tcb资源详情	
        :rtype: list of TCBInstanceList
        """
        return self._TCB

    @TCB.setter
    def TCB(self, TCB):
        self._TCB = TCB

    @property
    def TEO(self):
        """关联teo资源详情	
        :rtype: list of TeoInstanceList
        """
        return self._TEO

    @TEO.setter
    def TEO(self, TEO):
        self._TEO = TEO

    @property
    def Status(self):
        """关联云资源异步查询结果： 0表示查询中， 1表示查询成功。 2表示查询异常； 若状态为1，则查看BindResourceResult结果；若状态为2，则查看Error原因
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CacheTime(self):
        """当前结果缓存时间
        :rtype: str
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def TSE(self):
        """关联tse资源详情	
        :rtype: list of TSEInstanceList
        """
        return self._TSE

    @TSE.setter
    def TSE(self, TSE):
        self._TSE = TSE

    @property
    def COS(self):
        """关联的COS资源详情
        :rtype: list of COSInstanceList
        """
        return self._COS

    @COS.setter
    def COS(self, COS):
        self._COS = COS

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CLB") is not None:
            self._CLB = []
            for item in params.get("CLB"):
                obj = ClbInstanceList()
                obj._deserialize(item)
                self._CLB.append(obj)
        if params.get("CDN") is not None:
            self._CDN = []
            for item in params.get("CDN"):
                obj = CdnInstanceList()
                obj._deserialize(item)
                self._CDN.append(obj)
        if params.get("WAF") is not None:
            self._WAF = []
            for item in params.get("WAF"):
                obj = WafInstanceList()
                obj._deserialize(item)
                self._WAF.append(obj)
        if params.get("DDOS") is not None:
            self._DDOS = []
            for item in params.get("DDOS"):
                obj = DdosInstanceList()
                obj._deserialize(item)
                self._DDOS.append(obj)
        if params.get("LIVE") is not None:
            self._LIVE = []
            for item in params.get("LIVE"):
                obj = LiveInstanceList()
                obj._deserialize(item)
                self._LIVE.append(obj)
        if params.get("VOD") is not None:
            self._VOD = []
            for item in params.get("VOD"):
                obj = VODInstanceList()
                obj._deserialize(item)
                self._VOD.append(obj)
        if params.get("TKE") is not None:
            self._TKE = []
            for item in params.get("TKE"):
                obj = TkeInstanceList()
                obj._deserialize(item)
                self._TKE.append(obj)
        if params.get("APIGATEWAY") is not None:
            self._APIGATEWAY = []
            for item in params.get("APIGATEWAY"):
                obj = ApiGatewayInstanceList()
                obj._deserialize(item)
                self._APIGATEWAY.append(obj)
        if params.get("TCB") is not None:
            self._TCB = []
            for item in params.get("TCB"):
                obj = TCBInstanceList()
                obj._deserialize(item)
                self._TCB.append(obj)
        if params.get("TEO") is not None:
            self._TEO = []
            for item in params.get("TEO"):
                obj = TeoInstanceList()
                obj._deserialize(item)
                self._TEO.append(obj)
        self._Status = params.get("Status")
        self._CacheTime = params.get("CacheTime")
        if params.get("TSE") is not None:
            self._TSE = []
            for item in params.get("TSE"):
                obj = TSEInstanceList()
                obj._deserialize(item)
                self._TSE.append(obj)
        if params.get("COS") is not None:
            self._COS = []
            for item in params.get("COS"):
                obj = COSInstanceList()
                obj._deserialize(item)
                self._COS.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateBindResourceTaskResultRequest(AbstractModel):
    """DescribeCertificateBindResourceTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: 任务ID，根据CreateCertificateBindResourceSyncTask得到的任务ID查询绑定云资源结果， 最大支持100个
        :type TaskIds: list of str
        """
        self._TaskIds = None

    @property
    def TaskIds(self):
        """任务ID，根据CreateCertificateBindResourceSyncTask得到的任务ID查询绑定云资源结果， 最大支持100个
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateBindResourceTaskResultResponse(AbstractModel):
    """DescribeCertificateBindResourceTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncTaskBindResourceResult: 异步任务绑定关联云资源结果列表
        :type SyncTaskBindResourceResult: list of SyncTaskBindResourceResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SyncTaskBindResourceResult = None
        self._RequestId = None

    @property
    def SyncTaskBindResourceResult(self):
        """异步任务绑定关联云资源结果列表
        :rtype: list of SyncTaskBindResourceResult
        """
        return self._SyncTaskBindResourceResult

    @SyncTaskBindResourceResult.setter
    def SyncTaskBindResourceResult(self, SyncTaskBindResourceResult):
        self._SyncTaskBindResourceResult = SyncTaskBindResourceResult

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SyncTaskBindResourceResult") is not None:
            self._SyncTaskBindResourceResult = []
            for item in params.get("SyncTaskBindResourceResult"):
                obj = SyncTaskBindResourceResult()
                obj._deserialize(item)
                self._SyncTaskBindResourceResult.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 证书所属用户主账号 UIN。
        :type OwnerUin: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: str
        :param _From: 证书来源：
trustasia：亚洲诚信，
upload：用户上传。
wosign：沃通
sheca：上海CA
        :type From: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
        :type CertificateType: str
        :param _PackageType: 证书套餐类型：
null：用户上传证书（没有套餐类型），
2：TrustAsia TLS RSA CA， 
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
83：TrustAsia C1 DV Free
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书
100：CFCA 企业型通配符(OV)SSL证书
101：CFCA 增强型(EV)SSL证书
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _ProductZhName: 证书产品名称
        :type ProductZhName: str
        :param _Domain: 证书绑定通用名称域名。
        :type Domain: str
        :param _Alias: 备注名称。
        :type Alias: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 自动添加DNS记录，5 = 企业证书，待提交资料，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 证书已退款。 15 = 证书迁移中
        :type Status: int
        :param _StatusMsg: 状态信息。 取值范围：
//通用状态信息
1、PRE-REVIEWING：预审核中
2、LEGAL-REVIEWING：法务审核中
3、CA-REVIEWING：CA审核中
4、PENDING-DCV：域名验证中
5、WAIT-ISSUE：等待签发（域名验证已通过）
//证书审核失败状态信息
1、订单审核失败
2、CA审核失败，域名未通过安全审查
3、域名验证超时，订单自动关闭，请您重新进行证书申请
4、证书资料未通过证书CA机构审核，审核人员会致电您证书预留的联系方式，请您留意来电。后续可通过“修改资料”重新提交资料
待持续完善
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param _VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param _VulnerabilityStatus: 漏洞扫描状态。
        :type VulnerabilityStatus: str
        :param _CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param _CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param _ValidityPeriod: 证书有效期：单位（月）。
        :type ValidityPeriod: str
        :param _InsertTime: 证书申请时间。
        :type InsertTime: str
        :param _OrderId: CA订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _CertificateExtra: 证书扩展信息。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _CertificatePrivateKey: 私钥证书， 国密证书则为签名证书中的私钥证书
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePrivateKey: str
        :param _CertificatePublicKey: 公钥证书， 国密则为签名证书中的公钥证书
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePublicKey: str
        :param _DvAuthDetail: 证书域名验证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param _VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _TypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeName: str
        :param _StatusName: 状态描述。
        :type StatusName: str
        :param _SubjectAltName: 证书包含的多个域名（不包含主域名，主域名使用Domain字段）
        :type SubjectAltName: list of str
        :param _IsVip: 是否为付费证书。
        :type IsVip: bool
        :param _IsWildcard: 是否为泛域名证书。
        :type IsWildcard: bool
        :param _IsDv: 是否为 DV 版证书。
        :type IsDv: bool
        :param _IsVulnerability: 是否启用了漏洞扫描功能。
        :type IsVulnerability: bool
        :param _SubmittedData: 付费证书提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param _RenewAble: 是否可续费。
        :type RenewAble: bool
        :param _Deployable: 是否可部署。
        :type Deployable: bool
        :param _Tags: 关联标签列表。
        :type Tags: list of Tags
        :param _RootCert: 根证书。
        :type RootCert: :class:`tencentcloud.ssl.v20191205.models.RootCertificates`
        :param _EncryptCert: 国密加密证书公钥， 仅国密证书有值
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptCert: str
        :param _EncryptPrivateKey: 国密加密私钥证书， 仅国密证书有值
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptPrivateKey: str
        :param _CertFingerprint: 签名证书 SHA1指纹
注意：此字段可能返回 null，表示取不到有效值。
        :type CertFingerprint: str
        :param _EncryptCertFingerprint: 加密证书 SHA1指纹 （国密证书特有）
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptCertFingerprint: str
        :param _EncryptAlgorithm: 证书加密算法（国密证书特有）
        :type EncryptAlgorithm: str
        :param _DvRevokeAuthDetail: DV证书吊销验证值
注意：此字段可能返回 null，表示取不到有效值。
        :type DvRevokeAuthDetail: list of DvAuths
        :param _CertChainInfo: 证书链信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CertChainInfo: list of CertBasicInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._CertificateType = None
        self._PackageType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._StatusMsg = None
        self._VerifyType = None
        self._VulnerabilityStatus = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._OrderId = None
        self._CertificateExtra = None
        self._CertificatePrivateKey = None
        self._CertificatePublicKey = None
        self._DvAuthDetail = None
        self._VulnerabilityReport = None
        self._CertificateId = None
        self._TypeName = None
        self._StatusName = None
        self._SubjectAltName = None
        self._IsVip = None
        self._IsWildcard = None
        self._IsDv = None
        self._IsVulnerability = None
        self._SubmittedData = None
        self._RenewAble = None
        self._Deployable = None
        self._Tags = None
        self._RootCert = None
        self._EncryptCert = None
        self._EncryptPrivateKey = None
        self._CertFingerprint = None
        self._EncryptCertFingerprint = None
        self._EncryptAlgorithm = None
        self._DvRevokeAuthDetail = None
        self._CertChainInfo = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        """证书所属用户主账号 UIN。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """项目 ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        """证书来源：
trustasia：亚洲诚信，
upload：用户上传。
wosign：沃通
sheca：上海CA
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        """证书类型：CA = 客户端证书，SVR = 服务器证书。
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        """证书套餐类型：
null：用户上传证书（没有套餐类型），
2：TrustAsia TLS RSA CA， 
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
83：TrustAsia C1 DV Free
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书
100：CFCA 企业型通配符(OV)SSL证书
101：CFCA 增强型(EV)SSL证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        """证书产品名称
        :rtype: str
        """
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        """证书绑定通用名称域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        """备注名称。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        """证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 自动添加DNS记录，5 = 企业证书，待提交资料，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 证书已退款。 15 = 证书迁移中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        """状态信息。 取值范围：
//通用状态信息
1、PRE-REVIEWING：预审核中
2、LEGAL-REVIEWING：法务审核中
3、CA-REVIEWING：CA审核中
4、PENDING-DCV：域名验证中
5、WAIT-ISSUE：等待签发（域名验证已通过）
//证书审核失败状态信息
1、订单审核失败
2、CA审核失败，域名未通过安全审查
3、域名验证超时，订单自动关闭，请您重新进行证书申请
4、证书资料未通过证书CA机构审核，审核人员会致电您证书预留的联系方式，请您留意来电。后续可通过“修改资料”重新提交资料
待持续完善
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        """验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        """漏洞扫描状态。
        :rtype: str
        """
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        """证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        """证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        """证书有效期：单位（月）。
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        """证书申请时间。
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        """CA订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        """证书扩展信息。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        """
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def CertificatePrivateKey(self):
        """私钥证书， 国密证书则为签名证书中的私钥证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificatePublicKey(self):
        """公钥证书， 国密则为签名证书中的公钥证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def DvAuthDetail(self):
        """证书域名验证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        """
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        """漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def TypeName(self):
        """证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def StatusName(self):
        """状态描述。
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        """证书包含的多个域名（不包含主域名，主域名使用Domain字段）
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        """是否为付费证书。
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        """是否为泛域名证书。
        :rtype: bool
        """
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        """是否为 DV 版证书。
        :rtype: bool
        """
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        """是否启用了漏洞扫描功能。
        :rtype: bool
        """
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def SubmittedData(self):
        """付费证书提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        """
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def RenewAble(self):
        """是否可续费。
        :rtype: bool
        """
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def Deployable(self):
        """是否可部署。
        :rtype: bool
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        """关联标签列表。
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RootCert(self):
        """根证书。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.RootCertificates`
        """
        return self._RootCert

    @RootCert.setter
    def RootCert(self, RootCert):
        self._RootCert = RootCert

    @property
    def EncryptCert(self):
        """国密加密证书公钥， 仅国密证书有值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EncryptCert

    @EncryptCert.setter
    def EncryptCert(self, EncryptCert):
        self._EncryptCert = EncryptCert

    @property
    def EncryptPrivateKey(self):
        """国密加密私钥证书， 仅国密证书有值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EncryptPrivateKey

    @EncryptPrivateKey.setter
    def EncryptPrivateKey(self, EncryptPrivateKey):
        self._EncryptPrivateKey = EncryptPrivateKey

    @property
    def CertFingerprint(self):
        """签名证书 SHA1指纹
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertFingerprint

    @CertFingerprint.setter
    def CertFingerprint(self, CertFingerprint):
        self._CertFingerprint = CertFingerprint

    @property
    def EncryptCertFingerprint(self):
        """加密证书 SHA1指纹 （国密证书特有）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EncryptCertFingerprint

    @EncryptCertFingerprint.setter
    def EncryptCertFingerprint(self, EncryptCertFingerprint):
        self._EncryptCertFingerprint = EncryptCertFingerprint

    @property
    def EncryptAlgorithm(self):
        """证书加密算法（国密证书特有）
        :rtype: str
        """
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def DvRevokeAuthDetail(self):
        """DV证书吊销验证值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DvAuths
        """
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

    @property
    def CertChainInfo(self):
        """证书链信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CertBasicInfo
        """
        return self._CertChainInfo

    @CertChainInfo.setter
    def CertChainInfo(self, CertChainInfo):
        self._CertChainInfo = CertChainInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._CertificateType = params.get("CertificateType")
        self._PackageType = params.get("PackageType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        if params.get("DvAuthDetail") is not None:
            self._DvAuthDetail = DvAuthDetail()
            self._DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self._VulnerabilityReport = params.get("VulnerabilityReport")
        self._CertificateId = params.get("CertificateId")
        self._TypeName = params.get("TypeName")
        self._StatusName = params.get("StatusName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._IsVip = params.get("IsVip")
        self._IsWildcard = params.get("IsWildcard")
        self._IsDv = params.get("IsDv")
        self._IsVulnerability = params.get("IsVulnerability")
        if params.get("SubmittedData") is not None:
            self._SubmittedData = SubmittedData()
            self._SubmittedData._deserialize(params.get("SubmittedData"))
        self._RenewAble = params.get("RenewAble")
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("RootCert") is not None:
            self._RootCert = RootCertificates()
            self._RootCert._deserialize(params.get("RootCert"))
        self._EncryptCert = params.get("EncryptCert")
        self._EncryptPrivateKey = params.get("EncryptPrivateKey")
        self._CertFingerprint = params.get("CertFingerprint")
        self._EncryptCertFingerprint = params.get("EncryptCertFingerprint")
        self._EncryptAlgorithm = params.get("EncryptAlgorithm")
        if params.get("DvRevokeAuthDetail") is not None:
            self._DvRevokeAuthDetail = []
            for item in params.get("DvRevokeAuthDetail"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvRevokeAuthDetail.append(obj)
        if params.get("CertChainInfo") is not None:
            self._CertChainInfo = []
            for item in params.get("CertChainInfo"):
                obj = CertBasicInfo()
                obj._deserialize(item)
                self._CertChainInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 请求日志数量，默认为20, 最大值为1000，如超过1000按照1000处理。
        :type Limit: int
        :param _StartTime: 开始时间，默认15天前。
        :type StartTime: str
        :param _EndTime: 结束时间，默认现在时间。
        :type EndTime: str
        """
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """请求日志数量，默认为20, 最大值为1000，如超过1000按照1000处理。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartTime(self):
        """开始时间，默认15天前。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，默认现在时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateOperateLogsResponse(AbstractModel):
    """DescribeCertificateOperateLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllTotal: 当前查询条件日志总数。
        :type AllTotal: int
        :param _TotalCount: 本次请求返回的日志数量。
        :type TotalCount: int
        :param _OperateLogs: 证书操作日志列表。
        :type OperateLogs: list of OperationLog
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllTotal = None
        self._TotalCount = None
        self._OperateLogs = None
        self._RequestId = None

    @property
    def AllTotal(self):
        """当前查询条件日志总数。
        :rtype: int
        """
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def TotalCount(self):
        """本次请求返回的日志数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OperateLogs(self):
        """证书操作日志列表。
        :rtype: list of OperationLog
        """
        return self._OperateLogs

    @OperateLogs.setter
    def OperateLogs(self, OperateLogs):
        self._OperateLogs = OperateLogs

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllTotal = params.get("AllTotal")
        self._TotalCount = params.get("TotalCount")
        if params.get("OperateLogs") is not None:
            self._OperateLogs = []
            for item in params.get("OperateLogs"):
                obj = OperationLog()
                obj._deserialize(item)
                self._OperateLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateRequest(AbstractModel):
    """DescribeCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateResponse(AbstractModel):
    """DescribeCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _From: 证书来源：
trustasia：亚洲诚信，
upload：用户上传。
wosign：沃通
sheca：上海CA
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param _PackageType: 证书套餐类型：
null：用户上传证书（没有套餐类型），
2：TrustAsia TLS RSA CA， 
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
83：TrustAsia C1 DV Free
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书
100：CFCA 企业型通配符(OV)SSL证书
101：CFCA 增强型(EV)SSL证书
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _ProductZhName: 证书产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param _Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 自动添加DNS记录，5 = 企业证书，待提交资料，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 证书已退款。 15 = 证书迁移中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusMsg: 状态信息。 取值范围：
//通用状态信息
1、PRE-REVIEWING：预审核中
2、LEGAL-REVIEWING：法务审核中
3、CA-REVIEWING：CA审核中
4、PENDING-DCV：域名验证中
5、WAIT-ISSUE：等待签发（域名验证已通过）
//证书审核失败状态信息
1、订单审核失败
2、CA审核失败，域名未通过安全审查
3、域名验证超时，订单自动关闭，请您重新进行证书申请
4、证书资料未通过证书CA机构审核，审核人员会致电您证书预留的联系方式，请您留意来电。后续可通过“修改资料”重新提交资料
待持续完善
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param _VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，DNS_PROXY = DNS代理验证。FILE_PROXY = 文件代理验证
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param _VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param _CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param _CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param _ValidityPeriod: 证书有效期：单位(月)。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param _InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param _VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param _CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param _PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param _StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param _SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param _IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param _IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param _IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param _IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param _RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param _SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param _Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param _Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        :param _CAEncryptAlgorithms: CA证书的所有加密方式。仅证书类型CertificateType为CA有效
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEncryptAlgorithms: list of str
        :param _CACommonNames: CA证书的所有通用名称。仅证书类型CertificateType为CA有效
注意：此字段可能返回 null，表示取不到有效值。
        :type CACommonNames: list of str
        :param _CAEndTimes: CA证书所有的到期时间。仅证书类型CertificateType为CA有效
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEndTimes: list of str
        :param _DvRevokeAuthDetail: DV证书吊销验证值
注意：此字段可能返回 null，表示取不到有效值。
        :type DvRevokeAuthDetail: list of DvAuths
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._CertificateType = None
        self._PackageType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._StatusMsg = None
        self._VerifyType = None
        self._VulnerabilityStatus = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._OrderId = None
        self._CertificateExtra = None
        self._DvAuthDetail = None
        self._VulnerabilityReport = None
        self._CertificateId = None
        self._PackageTypeName = None
        self._StatusName = None
        self._SubjectAltName = None
        self._IsVip = None
        self._IsWildcard = None
        self._IsDv = None
        self._IsVulnerability = None
        self._RenewAble = None
        self._SubmittedData = None
        self._Deployable = None
        self._Tags = None
        self._CAEncryptAlgorithms = None
        self._CACommonNames = None
        self._CAEndTimes = None
        self._DvRevokeAuthDetail = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        """用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        """证书来源：
trustasia：亚洲诚信，
upload：用户上传。
wosign：沃通
sheca：上海CA
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        """证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        """证书套餐类型：
null：用户上传证书（没有套餐类型），
2：TrustAsia TLS RSA CA， 
3：SecureSite 增强型企业版（EV Pro）， 
4：SecureSite 增强型（EV）， 
5：SecureSite 企业型专业版（OV Pro），
6：SecureSite 企业型（OV）， 
7：SecureSite 企业型（OV）通配符， 
8：Geotrust 增强型（EV）， 
9：Geotrust 企业型（OV）， 
10：Geotrust 企业型（OV）通配符， 
11：TrustAsia 域名型多域名 SSL 证书， 
12：TrustAsia 域名型（DV）通配符， 
13：TrustAsia 企业型通配符（OV）SSL 证书（D3）， 
14：TrustAsia 企业型（OV）SSL 证书（D3）， 
15：TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 
16：TrustAsia 增强型 （EV）SSL 证书（D3）， 
17：TrustAsia 增强型多域名（EV）SSL 证书（D3）， 
18：GlobalSign 企业型（OV）SSL 证书， 
19：GlobalSign 企业型通配符 （OV）SSL 证书， 
20：GlobalSign 增强型 （EV）SSL 证书， 
21：TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 
22：GlobalSign 企业型多域名（OV）SSL 证书， 
23：GlobalSign 企业型通配符多域名（OV）SSL 证书，
24：GlobalSign 增强型多域名（EV）SSL 证书，
25：Wotrus 域名型证书，
26：Wotrus 域名型多域名证书，
27：Wotrus 域名型通配符证书，
28：Wotrus 企业型证书，
29：Wotrus 企业型多域名证书，
30：Wotrus 企业型通配符证书，
31：Wotrus 增强型证书，
32：Wotrus 增强型多域名证书，
33：WoTrus-国密域名型证书，
34：WoTrus-国密域名型证书（多域名），
35：WoTrus-国密域名型证书（通配符），
37：WoTrus-国密企业型证书，
38：WoTrus-国密企业型证书（多域名），
39：WoTrus-国密企业型证书（通配符），
40：WoTrus-国密增强型证书，
41：WoTrus-国密增强型证书（多域名），
42：TrustAsia-域名型证书（通配符多域名），
43：DNSPod-企业型(OV)SSL证书
44：DNSPod-企业型(OV)通配符SSL证书
45：DNSPod-企业型(OV)多域名SSL证书
46：DNSPod-增强型(EV)SSL证书
47：DNSPod-增强型(EV)多域名SSL证书
48：DNSPod-域名型(DV)SSL证书
49：DNSPod-域名型(DV)通配符SSL证书
50：DNSPod-域名型(DV)多域名SSL证书
51：DNSPod（国密）-企业型(OV)SSL证书
52：DNSPod（国密）-企业型(OV)通配符SSL证书
53：DNSPod（国密）-企业型(OV)多域名SSL证书
54：DNSPod（国密）-域名型(DV)SSL证书
55：DNSPod（国密）-域名型(DV)通配符SSL证书
56：DNSPod（国密）-域名型(DV)多域名SSL证书
57：SecureSite 企业型专业版多域名(OV Pro)
58：SecureSite 企业型多域名(OV)
59：SecureSite 增强型专业版多域名(EV Pro)
60：SecureSite 增强型多域名(EV)
61：Geotrust 增强型多域名(EV)
75：SecureSite 企业型(OV)
76：SecureSite 企业型(OV)通配符
77：SecureSite 增强型(EV)
78：Geotrust 企业型(OV)
79：Geotrust 企业型(OV)通配符
80：Geotrust 增强型(EV)
81：GlobalSign 企业型（OV）SSL证书
82：GlobalSign 企业型通配符 （OV）SSL证书
83：TrustAsia C1 DV Free
85：GlobalSign 增强型 （EV）SSL证书
88：GlobalSign 企业型通配符多域名 （OV）SSL证书
89：GlobalSign 企业型多域名 （OV）SSL证书
90：GlobalSign 增强型多域名（EV） SSL证书
91：Geotrust 增强型多域名(EV)
92：SecureSite 企业型专业版多域名(OV Pro)
93：SecureSite 企业型多域名(OV)
94：SecureSite 增强型专业版多域名(EV Pro)
95：SecureSite 增强型多域名(EV)
96：SecureSite 增强型专业版(EV Pro)
97：SecureSite 企业型专业版(OV Pro)
98：CFCA 企业型(OV)SSL证书
99：CFCA 企业型多域名(OV)SSL证书
100：CFCA 企业型通配符(OV)SSL证书
101：CFCA 增强型(EV)SSL证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        """证书产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        """域名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        """备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        """证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 自动添加DNS记录，5 = 企业证书，待提交资料，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 证书已退款。 15 = 证书迁移中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        """状态信息。 取值范围：
//通用状态信息
1、PRE-REVIEWING：预审核中
2、LEGAL-REVIEWING：法务审核中
3、CA-REVIEWING：CA审核中
4、PENDING-DCV：域名验证中
5、WAIT-ISSUE：等待签发（域名验证已通过）
//证书审核失败状态信息
1、订单审核失败
2、CA审核失败，域名未通过安全审查
3、域名验证超时，订单自动关闭，请您重新进行证书申请
4、证书资料未通过证书CA机构审核，审核人员会致电您证书预留的联系方式，请您留意来电。后续可通过“修改资料”重新提交资料
待持续完善
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        """验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，DNS_PROXY = DNS代理验证。FILE_PROXY = 文件代理验证
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        """漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        """证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        """证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        """证书有效期：单位(月)。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        """申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        """订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        """证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        """
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def DvAuthDetail(self):
        """DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        """
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        """漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        """证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def PackageTypeName(self):
        """证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        """状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        """证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        """是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        """是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        """是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        """是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        """是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def SubmittedData(self):
        """提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        """
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def Deployable(self):
        """是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        """标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CAEncryptAlgorithms(self):
        """CA证书的所有加密方式。仅证书类型CertificateType为CA有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CACommonNames(self):
        """CA证书的所有通用名称。仅证书类型CertificateType为CA有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def CAEndTimes(self):
        """CA证书所有的到期时间。仅证书类型CertificateType为CA有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def DvRevokeAuthDetail(self):
        """DV证书吊销验证值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DvAuths
        """
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._CertificateType = params.get("CertificateType")
        self._PackageType = params.get("PackageType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        if params.get("DvAuthDetail") is not None:
            self._DvAuthDetail = DvAuthDetail()
            self._DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self._VulnerabilityReport = params.get("VulnerabilityReport")
        self._CertificateId = params.get("CertificateId")
        self._PackageTypeName = params.get("PackageTypeName")
        self._StatusName = params.get("StatusName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._IsVip = params.get("IsVip")
        self._IsWildcard = params.get("IsWildcard")
        self._IsDv = params.get("IsDv")
        self._IsVulnerability = params.get("IsVulnerability")
        self._RenewAble = params.get("RenewAble")
        if params.get("SubmittedData") is not None:
            self._SubmittedData = SubmittedData()
            self._SubmittedData._deserialize(params.get("SubmittedData"))
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self._CACommonNames = params.get("CACommonNames")
        self._CAEndTimes = params.get("CAEndTimes")
        if params.get("DvRevokeAuthDetail") is not None:
            self._DvRevokeAuthDetail = []
            for item in params.get("DvRevokeAuthDetail"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvRevokeAuthDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始。 默认为0
        :type Offset: int
        :param _Limit: 每页数量，默认10。最大值1000，如超过1000按1000处理
        :type Limit: int
        :param _SearchKey: 搜索关键词，模糊匹配证书 ID、备注名称、证书域名
        :type SearchKey: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
        :type CertificateType: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _ExpirationSort: 默认按照证书申请时间降序； 若传排序则按到期时间排序：DESC = 证书到期时间降序， ASC = 证书到期时间升序。
        :type ExpirationSort: str
        :param _CertificateStatus: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 已退款。 15 = 证书迁移中
        :type CertificateStatus: list of int non-negative
        :param _Deployable: 是否可部署，可选值：1 = 可部署，0 =  不可部署。
        :type Deployable: int
        :param _Upload: 是否筛选上传托管的 1筛选，0不筛选
        :type Upload: int
        :param _Renew: 是否筛选可续期证书 1筛选 0不筛选
        :type Renew: int
        :param _FilterSource: 筛选来源， upload：上传证书， buy：腾讯云证书， 不传默认全部
        :type FilterSource: str
        :param _IsSM: 是否筛选国密证书。1:筛选  0:不筛选
        :type IsSM: int
        :param _FilterExpiring: 筛选证书是否即将过期，传1是筛选，0不筛选
        :type FilterExpiring: int
        :param _Hostable: 是否可托管，可选值：1 = 可托管，0 =  不可托管。
        :type Hostable: int
        :param _Tags: 筛选指定标签的证书
        :type Tags: list of Tags
        :param _IsPendingIssue: 是否筛选等待签发的证书，传1是筛选，0和null不筛选
        :type IsPendingIssue: int
        :param _CertIds: 筛选指定证书ID的证书，只支持有权限的证书ID
        :type CertIds: list of str
        """
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._CertificateType = None
        self._ProjectId = None
        self._ExpirationSort = None
        self._CertificateStatus = None
        self._Deployable = None
        self._Upload = None
        self._Renew = None
        self._FilterSource = None
        self._IsSM = None
        self._FilterExpiring = None
        self._Hostable = None
        self._Tags = None
        self._IsPendingIssue = None
        self._CertIds = None

    @property
    def Offset(self):
        """分页偏移量，从0开始。 默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。最大值1000，如超过1000按1000处理
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        """搜索关键词，模糊匹配证书 ID、备注名称、证书域名
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def CertificateType(self):
        """证书类型：CA = 客户端证书，SVR = 服务器证书。
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProjectId(self):
        """项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ExpirationSort(self):
        """默认按照证书申请时间降序； 若传排序则按到期时间排序：DESC = 证书到期时间降序， ASC = 证书到期时间升序。
        :rtype: str
        """
        return self._ExpirationSort

    @ExpirationSort.setter
    def ExpirationSort(self, ExpirationSort):
        self._ExpirationSort = ExpirationSort

    @property
    def CertificateStatus(self):
        """证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。14 = 已退款。 15 = 证书迁移中
        :rtype: list of int non-negative
        """
        return self._CertificateStatus

    @CertificateStatus.setter
    def CertificateStatus(self, CertificateStatus):
        self._CertificateStatus = CertificateStatus

    @property
    def Deployable(self):
        """是否可部署，可选值：1 = 可部署，0 =  不可部署。
        :rtype: int
        """
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Upload(self):
        """是否筛选上传托管的 1筛选，0不筛选
        :rtype: int
        """
        return self._Upload

    @Upload.setter
    def Upload(self, Upload):
        self._Upload = Upload

    @property
    def Renew(self):
        """是否筛选可续期证书 1筛选 0不筛选
        :rtype: int
        """
        return self._Renew

    @Renew.setter
    def Renew(self, Renew):
        self._Renew = Renew

    @property
    def FilterSource(self):
        """筛选来源， upload：上传证书， buy：腾讯云证书， 不传默认全部
        :rtype: str
        """
        return self._FilterSource

    @FilterSource.setter
    def FilterSource(self, FilterSource):
        self._FilterSource = FilterSource

    @property
    def IsSM(self):
        """是否筛选国密证书。1:筛选  0:不筛选
        :rtype: int
        """
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def FilterExpiring(self):
        """筛选证书是否即将过期，传1是筛选，0不筛选
        :rtype: int
        """
        return self._FilterExpiring

    @FilterExpiring.setter
    def FilterExpiring(self, FilterExpiring):
        self._FilterExpiring = FilterExpiring

    @property
    def Hostable(self):
        """是否可托管，可选值：1 = 可托管，0 =  不可托管。
        :rtype: int
        """
        return self._Hostable

    @Hostable.setter
    def Hostable(self, Hostable):
        self._Hostable = Hostable

    @property
    def Tags(self):
        """筛选指定标签的证书
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsPendingIssue(self):
        """是否筛选等待签发的证书，传1是筛选，0和null不筛选
        :rtype: int
        """
        return self._IsPendingIssue

    @IsPendingIssue.setter
    def IsPendingIssue(self, IsPendingIssue):
        self._IsPendingIssue = IsPendingIssue

    @property
    def CertIds(self):
        """筛选指定证书ID的证书，只支持有权限的证书ID
        :rtype: list of str
        """
        return self._CertIds

    @CertIds.setter
    def CertIds(self, CertIds):
        self._CertIds = CertIds


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._CertificateType = params.get("CertificateType")
        self._ProjectId = params.get("ProjectId")
        self._ExpirationSort = params.get("ExpirationSort")
        self._CertificateStatus = params.get("CertificateStatus")
        self._Deployable = params.get("Deployable")
        self._Upload = params.get("Upload")
        self._Renew = params.get("Renew")
        self._FilterSource = params.get("FilterSource")
        self._IsSM = params.get("IsSM")
        self._FilterExpiring = params.get("FilterExpiring")
        self._Hostable = params.get("Hostable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsPendingIssue = params.get("IsPendingIssue")
        self._CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量。
        :type TotalCount: int
        :param _Certificates: 列表。
        :type Certificates: list of Certificates
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Certificates = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Certificates(self):
        """列表。
        :rtype: list of Certificates
        """
        return self._Certificates

    @Certificates.setter
    def Certificates(self, Certificates):
        self._Certificates = Certificates

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Certificates") is not None:
            self._Certificates = []
            for item in params.get("Certificates"):
                obj = Certificates()
                obj._deserialize(item)
                self._Certificates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCompaniesRequest(AbstractModel):
    """DescribeCompanies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，默认值为0.
        :type Offset: int
        :param _Limit: 分页每页限制数，默认值为0，最大值1000.
        :type Limit: int
        :param _CompanyId: 公司ID
        :type CompanyId: int
        """
        self._Offset = None
        self._Limit = None
        self._CompanyId = None

    @property
    def Offset(self):
        """分页偏移量，默认值为0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页每页限制数，默认值为0，最大值1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CompanyId(self):
        """公司ID
        :rtype: int
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CompanyId = params.get("CompanyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompaniesResponse(AbstractModel):
    """DescribeCompanies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Companies: 公司列表
        :type Companies: list of CompanyInfo
        :param _TotalCount: 公司总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Companies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Companies(self):
        """公司列表
        :rtype: list of CompanyInfo
        """
        return self._Companies

    @Companies.setter
    def Companies(self, Companies):
        self._Companies = Companies

    @property
    def TotalCount(self):
        """公司总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Companies") is not None:
            self._Companies = []
            for item in params.get("Companies"):
                obj = CompanyInfo()
                obj._deserialize(item)
                self._Companies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDeleteCertificatesTaskResultRequest(AbstractModel):
    """DescribeDeleteCertificatesTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskIds: DeleteCertificates接口返回的任务ID， 最大支持100个
        :type TaskIds: list of str
        """
        self._TaskIds = None

    @property
    def TaskIds(self):
        """DeleteCertificates接口返回的任务ID， 最大支持100个
        :rtype: list of str
        """
        return self._TaskIds

    @TaskIds.setter
    def TaskIds(self, TaskIds):
        self._TaskIds = TaskIds


    def _deserialize(self, params):
        self._TaskIds = params.get("TaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeleteCertificatesTaskResultResponse(AbstractModel):
    """DescribeDeleteCertificatesTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteTaskResult: 批量删除证书异步任务结果
        :type DeleteTaskResult: list of DeleteTaskResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteTaskResult = None
        self._RequestId = None

    @property
    def DeleteTaskResult(self):
        """批量删除证书异步任务结果
        :rtype: list of DeleteTaskResult
        """
        return self._DeleteTaskResult

    @DeleteTaskResult.setter
    def DeleteTaskResult(self, DeleteTaskResult):
        self._DeleteTaskResult = DeleteTaskResult

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeleteTaskResult") is not None:
            self._DeleteTaskResult = []
            for item in params.get("DeleteTaskResult"):
                obj = DeleteTaskResult()
                obj._deserialize(item)
                self._DeleteTaskResult.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeployedResourcesRequest(AbstractModel):
    """DescribeDeployedResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID
        :type CertificateIds: list of str
        :param _ResourceType: 资源类型:clb,cdn,live,waf,antiddos,teo
        :type ResourceType: str
        """
        self._CertificateIds = None
        self._ResourceType = None

    @property
    def CertificateIds(self):
        """证书ID
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ResourceType(self):
        """资源类型:clb,cdn,live,waf,antiddos,teo
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployedResourcesResponse(AbstractModel):
    """DescribeDeployedResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployedResources: 资源详情
        :type DeployedResources: list of DeployedResources
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployedResources = None
        self._RequestId = None

    @property
    def DeployedResources(self):
        """资源详情
        :rtype: list of DeployedResources
        """
        return self._DeployedResources

    @DeployedResources.setter
    def DeployedResources(self, DeployedResources):
        self._DeployedResources = DeployedResources

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeployedResources") is not None:
            self._DeployedResources = []
            for item in params.get("DeployedResources"):
                obj = DeployedResources()
                obj._deserialize(item)
                self._DeployedResources.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDownloadCertificateUrlRequest(AbstractModel):
    """DescribeDownloadCertificateUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _ServiceType: 必填选项，下载的服务类型: nginx tomcat apache iis jks other root
        :type ServiceType: str
        """
        self._CertificateId = None
        self._ServiceType = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ServiceType(self):
        """必填选项，下载的服务类型: nginx tomcat apache iis jks other root
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDownloadCertificateUrlResponse(AbstractModel):
    """DescribeDownloadCertificateUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadCertificateUrl: 下载链接
        :type DownloadCertificateUrl: str
        :param _DownloadFilename: 下载文件的名称
        :type DownloadFilename: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadCertificateUrl = None
        self._DownloadFilename = None
        self._RequestId = None

    @property
    def DownloadCertificateUrl(self):
        """下载链接
        :rtype: str
        """
        return self._DownloadCertificateUrl

    @DownloadCertificateUrl.setter
    def DownloadCertificateUrl(self, DownloadCertificateUrl):
        self._DownloadCertificateUrl = DownloadCertificateUrl

    @property
    def DownloadFilename(self):
        """下载文件的名称
        :rtype: str
        """
        return self._DownloadFilename

    @DownloadFilename.setter
    def DownloadFilename(self, DownloadFilename):
        self._DownloadFilename = DownloadFilename

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DownloadCertificateUrl = params.get("DownloadCertificateUrl")
        self._DownloadFilename = params.get("DownloadFilename")
        self._RequestId = params.get("RequestId")


class DescribeHostApiGatewayInstanceListRequest(AbstractModel):
    """DescribeHostApiGatewayInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型apigateway
        :type ResourceType: str
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        :param _Limit: 每页数量，默认10，最大值为200。	
        :type Limit: int
        :param _Offset: 分页偏移量，默认值为0。
        :type Offset: str
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None
        self._OldCertificateId = None
        self._Limit = None
        self._Offset = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """部署资源类型apigateway
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType

    @property
    def OldCertificateId(self):
        """已部署的证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Limit(self):
        """每页数量，默认10，最大值为200。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，默认值为0。
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._OldCertificateId = params.get("OldCertificateId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostApiGatewayInstanceListResponse(AbstractModel):
    """DescribeHostApiGatewayInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: apiGateway实例列表,如取不到值返回空数组
        :type InstanceList: list of ApiGatewayInstanceDetail
        :param _TotalCount: 总数，如取不到值返回0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """apiGateway实例列表,如取不到值返回空数组
        :rtype: list of ApiGatewayInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """总数，如取不到值返回0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ApiGatewayInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostCdnInstanceListRequest(AbstractModel):
    """DescribeHostCdnInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型cdn
        :type ResourceType: str
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        :param _Offset: 分页偏移量，默认值为0。	
        :type Offset: int
        :param _Limit: 每页数量，默认10，最大值为200。	
        :type Limit: int
        :param _AsyncCache: 是否异步,0表示否，1表示是，默认为0
        :type AsyncCache: int
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None
        self._OldCertificateId = None
        self._Offset = None
        self._Limit = None
        self._AsyncCache = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """部署资源类型cdn
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType

    @property
    def OldCertificateId(self):
        """原证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Offset(self):
        """分页偏移量，默认值为0。	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10，最大值为200。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AsyncCache(self):
        """是否异步,0表示否，1表示是，默认为0
        :rtype: int
        """
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._OldCertificateId = params.get("OldCertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AsyncCache = params.get("AsyncCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostCdnInstanceListResponse(AbstractModel):
    """DescribeHostCdnInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: CDN实例列表，如取不到值返回空数组
        :type InstanceList: list of CdnInstanceDetail
        :param _TotalCount: CDN域名总数，如取不到值返回0
        :type TotalCount: int
        :param _AsyncTotalNum: 异步刷新总数，如取不到值返回0
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数，如取不到值返回0
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """CDN实例列表，如取不到值返回空数组
        :rtype: list of CdnInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """CDN域名总数，如取不到值返回0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AsyncTotalNum(self):
        """异步刷新总数，如取不到值返回0
        :rtype: int
        """
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        """异步刷新当前执行数，如取不到值返回0
        :rtype: int
        """
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        """当前缓存读取时间
        :rtype: str
        """
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CdnInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostClbInstanceListRequest(AbstractModel):
    """DescribeHostClbInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _AsyncCache: 是否异步缓存,0表示否,1表示是
        :type AsyncCache: int
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self._Offset = None
        self._Limit = None
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._AsyncCache = None
        self._OldCertificateId = None

    @property
    def Offset(self):
        """分页偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AsyncCache(self):
        """是否异步缓存,0表示否,1表示是
        :rtype: int
        """
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache

    @property
    def OldCertificateId(self):
        """原证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AsyncCache = params.get("AsyncCache")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostClbInstanceListResponse(AbstractModel):
    """DescribeHostClbInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数，取不到值返回0
        :type TotalCount: int
        :param _InstanceList: CLB实例监听器列表，取不到值返回空数组
        :type InstanceList: list of ClbInstanceDetail
        :param _AsyncTotalNum: 异步刷新总数，取不到值返回0
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数，取不到值返回0
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间，去不到值返回空
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数，取不到值返回0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """CLB实例监听器列表，取不到值返回空数组
        :rtype: list of ClbInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def AsyncTotalNum(self):
        """异步刷新总数，取不到值返回0
        :rtype: int
        """
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        """异步刷新当前执行数，取不到值返回0
        :rtype: int
        """
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        """当前缓存读取时间，去不到值返回空
        :rtype: str
        """
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ClbInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostCosInstanceListRequest(AbstractModel):
    """DescribeHostCosInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型 cos
        :type ResourceType: str
        :param _OldCertificateId: 原证书ID	
        :type OldCertificateId: str
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。	
        :type Limit: int
        :param _AsyncCache: 是否异步，0表示否，1表示是
        :type AsyncCache: int
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None
        self._OldCertificateId = None
        self._Offset = None
        self._Limit = None
        self._AsyncCache = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        """部署资源类型 cos
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def OldCertificateId(self):
        """原证书ID	
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Offset(self):
        """分页偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AsyncCache(self):
        """是否异步，0表示否，1表示是
        :rtype: int
        """
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._OldCertificateId = params.get("OldCertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AsyncCache = params.get("AsyncCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostCosInstanceListResponse(AbstractModel):
    """DescribeHostCosInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: COS实例列表
        :type InstanceList: list of CosInstanceDetail
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _AsyncTotalNum: 异步刷新总数
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """COS实例列表
        :rtype: list of CosInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AsyncTotalNum(self):
        """异步刷新总数
        :rtype: int
        """
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        """异步刷新当前执行数
        :rtype: int
        """
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        """当前缓存读取时间
        :rtype: str
        """
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostDdosInstanceListRequest(AbstractModel):
    """DescribeHostDdosInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型ddos
        :type ResourceType: str
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        :param _Offset: 分页偏移量，从0开始。	
        :type Offset: int
        :param _Limit: 每页数量，默认10。	
        :type Limit: int
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None
        self._OldCertificateId = None
        self._Offset = None
        self._Limit = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        """部署资源类型ddos
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def OldCertificateId(self):
        """已部署的证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Offset(self):
        """分页偏移量，从0开始。	
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._OldCertificateId = params.get("OldCertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDdosInstanceListResponse(AbstractModel):
    """DescribeHostDdosInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: DDOS实例列表,取不到值返回空数组
        :type InstanceList: list of DdosInstanceDetail
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """DDOS实例列表,取不到值返回空数组
        :rtype: list of DdosInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = DdosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostDeployRecordDetailRequest(AbstractModel):
    """DescribeHostDeployRecordDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 部署记录ID，通过调用DeployCertificateInstance接口返回的记录ID， 或者通过DeployCertificateRecordRollback回滚接口返回的记录ID
        :type DeployRecordId: str
        :param _Offset: 分页偏移量，从0开始。默认为0
        :type Offset: int
        :param _Limit: 每页数量，默认10。最大值为200
        :type Limit: int
        """
        self._DeployRecordId = None
        self._Offset = None
        self._Limit = None

    @property
    def DeployRecordId(self):
        """部署记录ID，通过调用DeployCertificateInstance接口返回的记录ID， 或者通过DeployCertificateRecordRollback回滚接口返回的记录ID
        :rtype: str
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def Offset(self):
        """分页偏移量，从0开始。默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。最大值为200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDeployRecordDetailResponse(AbstractModel):
    """DescribeHostDeployRecordDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 部署记录总数
        :type TotalCount: int
        :param _DeployRecordDetailList: 证书部署记录列表
        :type DeployRecordDetailList: list of DeployRecordDetail
        :param _SuccessTotalCount: 成功总数
        :type SuccessTotalCount: int
        :param _FailedTotalCount: 失败总数
        :type FailedTotalCount: int
        :param _RunningTotalCount: 部署中总数
        :type RunningTotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordDetailList = None
        self._SuccessTotalCount = None
        self._FailedTotalCount = None
        self._RunningTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """部署记录总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordDetailList(self):
        """证书部署记录列表
        :rtype: list of DeployRecordDetail
        """
        return self._DeployRecordDetailList

    @DeployRecordDetailList.setter
    def DeployRecordDetailList(self, DeployRecordDetailList):
        self._DeployRecordDetailList = DeployRecordDetailList

    @property
    def SuccessTotalCount(self):
        """成功总数
        :rtype: int
        """
        return self._SuccessTotalCount

    @SuccessTotalCount.setter
    def SuccessTotalCount(self, SuccessTotalCount):
        self._SuccessTotalCount = SuccessTotalCount

    @property
    def FailedTotalCount(self):
        """失败总数
        :rtype: int
        """
        return self._FailedTotalCount

    @FailedTotalCount.setter
    def FailedTotalCount(self, FailedTotalCount):
        self._FailedTotalCount = FailedTotalCount

    @property
    def RunningTotalCount(self):
        """部署中总数
        :rtype: int
        """
        return self._RunningTotalCount

    @RunningTotalCount.setter
    def RunningTotalCount(self, RunningTotalCount):
        self._RunningTotalCount = RunningTotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeployRecordDetailList") is not None:
            self._DeployRecordDetailList = []
            for item in params.get("DeployRecordDetailList"):
                obj = DeployRecordDetail()
                obj._deserialize(item)
                self._DeployRecordDetailList.append(obj)
        self._SuccessTotalCount = params.get("SuccessTotalCount")
        self._FailedTotalCount = params.get("FailedTotalCount")
        self._RunningTotalCount = params.get("RunningTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostDeployRecordRequest(AbstractModel):
    """DescribeHostDeployRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _ResourceType: 支持的资源类型如下,clb,cdn,ddos,waf,apigateway,teo,tke,cos,lighthouse,vod,tcb,tse,live
        :type ResourceType: str
        """
        self._CertificateId = None
        self._Offset = None
        self._Limit = None
        self._ResourceType = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Offset(self):
        """分页偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourceType(self):
        """支持的资源类型如下,clb,cdn,ddos,waf,apigateway,teo,tke,cos,lighthouse,vod,tcb,tse,live
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDeployRecordResponse(AbstractModel):
    """DescribeHostDeployRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _DeployRecordList: 证书部署记录列表
        :type DeployRecordList: list of DeployRecordInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordList(self):
        """证书部署记录列表
        :rtype: list of DeployRecordInfo
        """
        return self._DeployRecordList

    @DeployRecordList.setter
    def DeployRecordList(self, DeployRecordList):
        self._DeployRecordList = DeployRecordList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeployRecordList") is not None:
            self._DeployRecordList = []
            for item in params.get("DeployRecordList"):
                obj = DeployRecordInfo()
                obj._deserialize(item)
                self._DeployRecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostLighthouseInstanceListRequest(AbstractModel):
    """DescribeHostLighthouseInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型 lighthouse
        :type ResourceType: str
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """部署资源类型 lighthouse
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostLighthouseInstanceListResponse(AbstractModel):
    """DescribeHostLighthouseInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: Lighthouse实例列表,如取不到返回空数组
        :type InstanceList: list of LighthouseInstanceDetail
        :param _TotalCount: 总数，如取不到返回0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """Lighthouse实例列表,如取不到返回空数组
        :rtype: list of LighthouseInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """总数，如取不到返回0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LighthouseInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostLiveInstanceListRequest(AbstractModel):
    """DescribeHostLiveInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """部署资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType

    @property
    def OldCertificateId(self):
        """已部署的证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostLiveInstanceListResponse(AbstractModel):
    """DescribeHostLiveInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: live实例列表,如取不到值返回空数组
        :type InstanceList: list of LiveInstanceDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """live实例列表,如取不到值返回空数组
        :rtype: list of LiveInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostTeoInstanceListRequest(AbstractModel):
    """DescribeHostTeoInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        :param _Offset: 分页偏移量，默认值为0.
        :type Offset: int
        :param _Limit: 每页数量，默认10，最大值为200。	
        :type Limit: int
        :param _AsyncCache: 是否异步，1表示是，0表示否，默认为0
        :type AsyncCache: int
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None
        self._Offset = None
        self._Limit = None
        self._AsyncCache = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """部署资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        """已部署的证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def Offset(self):
        """分页偏移量，默认值为0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10，最大值为200。	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AsyncCache(self):
        """是否异步，1表示是，0表示否，默认为0
        :rtype: int
        """
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AsyncCache = params.get("AsyncCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostTeoInstanceListResponse(AbstractModel):
    """DescribeHostTeoInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: teo实例列表，如取不到值返回空数组
        :type InstanceList: list of TeoInstanceDetail
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """teo实例列表，如取不到值返回空数组
        :rtype: list of TeoInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TeoInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostTkeInstanceListRequest(AbstractModel):
    """DescribeHostTkeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _AsyncCache: 是否异步缓存，0表示否，1表示是，默认为0
        :type AsyncCache: int
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self._Offset = None
        self._Limit = None
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._AsyncCache = None
        self._OldCertificateId = None

    @property
    def Offset(self):
        """分页偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AsyncCache(self):
        """是否异步缓存，0表示否，1表示是，默认为0
        :rtype: int
        """
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache

    @property
    def OldCertificateId(self):
        """原证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AsyncCache = params.get("AsyncCache")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostTkeInstanceListResponse(AbstractModel):
    """DescribeHostTkeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数，取不到值返回0
        :type TotalCount: int
        :param _InstanceList: tke实例列表，取不到值返回空数组
        :type InstanceList: list of TkeInstanceDetail
        :param _AsyncTotalNum: 异步刷新总数，取不到值返回0
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数，取不到值返回0
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间	
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数，取不到值返回0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """tke实例列表，取不到值返回空数组
        :rtype: list of TkeInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def AsyncTotalNum(self):
        """异步刷新总数，取不到值返回0
        :rtype: int
        """
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        """异步刷新当前执行数，取不到值返回0
        :rtype: int
        """
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        """当前缓存读取时间	
        :rtype: str
        """
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TkeInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostUpdateRecordDetailRequest(AbstractModel):
    """DescribeHostUpdateRecordDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 部署记录ID，通过调用UpdateCertificateInstance接口返回的记录ID， 或者通过UpdateCertificateRecordRollback回滚接口返回的记录ID
        :type DeployRecordId: str
        :param _Limit: 每页数量，默认10。最大值为200
        :type Limit: str
        :param _Offset: 分页偏移量，从0开始。默认为0
        :type Offset: str
        """
        self._DeployRecordId = None
        self._Limit = None
        self._Offset = None

    @property
    def DeployRecordId(self):
        """部署记录ID，通过调用UpdateCertificateInstance接口返回的记录ID， 或者通过UpdateCertificateRecordRollback回滚接口返回的记录ID
        :rtype: str
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def Limit(self):
        """每页数量，默认10。最大值为200
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，从0开始。默认为0
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordDetailResponse(AbstractModel):
    """DescribeHostUpdateRecordDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数,如果取不到返回0
        :type TotalCount: int
        :param _RecordDetailList: 证书部署记录列表，如果取不到值返回空数组
        :type RecordDetailList: list of UpdateRecordDetails
        :param _SuccessTotalCount: 成功总数,如果取不到返回0
        :type SuccessTotalCount: int
        :param _FailedTotalCount: 失败总数,如果取不到返回0
        :type FailedTotalCount: int
        :param _RunningTotalCount: 部署中总数,如果取不到返回0
        :type RunningTotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordDetailList = None
        self._SuccessTotalCount = None
        self._FailedTotalCount = None
        self._RunningTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数,如果取不到返回0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordDetailList(self):
        """证书部署记录列表，如果取不到值返回空数组
        :rtype: list of UpdateRecordDetails
        """
        return self._RecordDetailList

    @RecordDetailList.setter
    def RecordDetailList(self, RecordDetailList):
        self._RecordDetailList = RecordDetailList

    @property
    def SuccessTotalCount(self):
        """成功总数,如果取不到返回0
        :rtype: int
        """
        return self._SuccessTotalCount

    @SuccessTotalCount.setter
    def SuccessTotalCount(self, SuccessTotalCount):
        self._SuccessTotalCount = SuccessTotalCount

    @property
    def FailedTotalCount(self):
        """失败总数,如果取不到返回0
        :rtype: int
        """
        return self._FailedTotalCount

    @FailedTotalCount.setter
    def FailedTotalCount(self, FailedTotalCount):
        self._FailedTotalCount = FailedTotalCount

    @property
    def RunningTotalCount(self):
        """部署中总数,如果取不到返回0
        :rtype: int
        """
        return self._RunningTotalCount

    @RunningTotalCount.setter
    def RunningTotalCount(self, RunningTotalCount):
        self._RunningTotalCount = RunningTotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordDetailList") is not None:
            self._RecordDetailList = []
            for item in params.get("RecordDetailList"):
                obj = UpdateRecordDetails()
                obj._deserialize(item)
                self._RecordDetailList.append(obj)
        self._SuccessTotalCount = params.get("SuccessTotalCount")
        self._FailedTotalCount = params.get("FailedTotalCount")
        self._RunningTotalCount = params.get("RunningTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostUpdateRecordRequest(AbstractModel):
    """DescribeHostUpdateRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _CertificateId: 新证书ID
        :type CertificateId: str
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self._Offset = None
        self._Limit = None
        self._CertificateId = None
        self._OldCertificateId = None

    @property
    def Offset(self):
        """分页偏移量，从0开始。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，默认10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CertificateId(self):
        """新证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def OldCertificateId(self):
        """原证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CertificateId = params.get("CertificateId")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordResponse(AbstractModel):
    """DescribeHostUpdateRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _DeployRecordList: 证书部署记录列表
        :type DeployRecordList: list of UpdateRecordInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordList(self):
        """证书部署记录列表
        :rtype: list of UpdateRecordInfo
        """
        return self._DeployRecordList

    @DeployRecordList.setter
    def DeployRecordList(self, DeployRecordList):
        self._DeployRecordList = DeployRecordList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeployRecordList") is not None:
            self._DeployRecordList = []
            for item in params.get("DeployRecordList"):
                obj = UpdateRecordInfo()
                obj._deserialize(item)
                self._DeployRecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostVodInstanceListRequest(AbstractModel):
    """DescribeHostVodInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID,必填选项
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型 vod
        :type ResourceType: str
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        """待部署的证书ID,必填选项
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """部署资源类型 vod
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType

    @property
    def OldCertificateId(self):
        """已部署的证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostVodInstanceListResponse(AbstractModel):
    """DescribeHostVodInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: Vod实例列表，如果取不到值返回空数组
        :type InstanceList: list of VodInstanceDetail
        :param _TotalCount: 总数,如果取不到值返回0
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """Vod实例列表，如果取不到值返回空数组
        :rtype: list of VodInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """总数,如果取不到值返回0
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = VodInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostWafInstanceListRequest(AbstractModel):
    """DescribeHostWafInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _ResourceType: 部署资源类型，如waf
        :type ResourceType: str
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._IsCache = None
        self._Filters = None
        self._ResourceType = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        """待部署的证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsCache(self):
        """是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :rtype: int
        """
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        """过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ResourceType(self):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        """部署资源类型，如waf
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        warnings.warn("parameter `ResourceType` is deprecated", DeprecationWarning) 

        self._ResourceType = ResourceType

    @property
    def OldCertificateId(self):
        """已部署的证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostWafInstanceListResponse(AbstractModel):
    """DescribeHostWafInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: WAF实例列表，如果没有取到值返回空数组
        :type InstanceList: list of WafInstanceDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._RequestId = None

    @property
    def InstanceList(self):
        """WAF实例列表，如果没有取到值返回空数组
        :rtype: list of WafInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = WafInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeManagerDetailRequest(AbstractModel):
    """DescribeManagerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID,可以从describeManagers接口获得
        :type ManagerId: int
        :param _Limit: 分页每页数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        """
        self._ManagerId = None
        self._Limit = None
        self._Offset = None

    @property
    def ManagerId(self):
        """管理人ID,可以从describeManagers接口获得
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def Limit(self):
        warnings.warn("parameter `Limit` is deprecated", DeprecationWarning) 

        """分页每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        warnings.warn("parameter `Limit` is deprecated", DeprecationWarning) 

        self._Limit = Limit

    @property
    def Offset(self):
        warnings.warn("parameter `Offset` is deprecated", DeprecationWarning) 

        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        warnings.warn("parameter `Offset` is deprecated", DeprecationWarning) 

        self._Offset = Offset


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeManagerDetailResponse(AbstractModel):
    """DescribeManagerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :type Status: str
        :param _ManagerFirstName: 管理人姓名
        :type ManagerFirstName: str
        :param _ManagerMail: 管理人邮箱
        :type ManagerMail: str
        :param _ContactFirstName: 联系人姓名
        :type ContactFirstName: str
        :param _ManagerLastName: 管理人姓名
        :type ManagerLastName: str
        :param _ContactPosition: 联系人职位
        :type ContactPosition: str
        :param _ManagerPosition: 管理人职位
        :type ManagerPosition: str
        :param _VerifyTime: 核验通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ExpireTime: 核验过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ContactLastName: 联系人姓名
        :type ContactLastName: str
        :param _ManagerPhone: 管理人电话
        :type ManagerPhone: str
        :param _ContactPhone: 联系人电话
        :type ContactPhone: str
        :param _ContactMail: 联系人邮箱
        :type ContactMail: str
        :param _ManagerDepartment: 管理人所属部门
        :type ManagerDepartment: str
        :param _CompanyInfo: 管理人所属公司信息
        :type CompanyInfo: :class:`tencentcloud.ssl.v20191205.models.CompanyInfo`
        :param _CompanyId: 管理人公司ID
        :type CompanyId: int
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _StatusInfo: 审核状态详细信息
        :type StatusInfo: list of ManagerStatusInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ManagerFirstName = None
        self._ManagerMail = None
        self._ContactFirstName = None
        self._ManagerLastName = None
        self._ContactPosition = None
        self._ManagerPosition = None
        self._VerifyTime = None
        self._CreateTime = None
        self._ExpireTime = None
        self._ContactLastName = None
        self._ManagerPhone = None
        self._ContactPhone = None
        self._ContactMail = None
        self._ManagerDepartment = None
        self._CompanyInfo = None
        self._CompanyId = None
        self._ManagerId = None
        self._StatusInfo = None
        self._RequestId = None

    @property
    def Status(self):
        warnings.warn("parameter `Status` is deprecated", DeprecationWarning) 

        """状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        warnings.warn("parameter `Status` is deprecated", DeprecationWarning) 

        self._Status = Status

    @property
    def ManagerFirstName(self):
        """管理人姓名
        :rtype: str
        """
        return self._ManagerFirstName

    @ManagerFirstName.setter
    def ManagerFirstName(self, ManagerFirstName):
        self._ManagerFirstName = ManagerFirstName

    @property
    def ManagerMail(self):
        """管理人邮箱
        :rtype: str
        """
        return self._ManagerMail

    @ManagerMail.setter
    def ManagerMail(self, ManagerMail):
        self._ManagerMail = ManagerMail

    @property
    def ContactFirstName(self):
        """联系人姓名
        :rtype: str
        """
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ManagerLastName(self):
        """管理人姓名
        :rtype: str
        """
        return self._ManagerLastName

    @ManagerLastName.setter
    def ManagerLastName(self, ManagerLastName):
        self._ManagerLastName = ManagerLastName

    @property
    def ContactPosition(self):
        """联系人职位
        :rtype: str
        """
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def ManagerPosition(self):
        """管理人职位
        :rtype: str
        """
        return self._ManagerPosition

    @ManagerPosition.setter
    def ManagerPosition(self, ManagerPosition):
        self._ManagerPosition = ManagerPosition

    @property
    def VerifyTime(self):
        """核验通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyTime

    @VerifyTime.setter
    def VerifyTime(self, VerifyTime):
        self._VerifyTime = VerifyTime

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """核验过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ContactLastName(self):
        """联系人姓名
        :rtype: str
        """
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ManagerPhone(self):
        """管理人电话
        :rtype: str
        """
        return self._ManagerPhone

    @ManagerPhone.setter
    def ManagerPhone(self, ManagerPhone):
        self._ManagerPhone = ManagerPhone

    @property
    def ContactPhone(self):
        """联系人电话
        :rtype: str
        """
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def ContactMail(self):
        """联系人邮箱
        :rtype: str
        """
        return self._ContactMail

    @ContactMail.setter
    def ContactMail(self, ContactMail):
        self._ContactMail = ContactMail

    @property
    def ManagerDepartment(self):
        """管理人所属部门
        :rtype: str
        """
        return self._ManagerDepartment

    @ManagerDepartment.setter
    def ManagerDepartment(self, ManagerDepartment):
        self._ManagerDepartment = ManagerDepartment

    @property
    def CompanyInfo(self):
        """管理人所属公司信息
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CompanyInfo`
        """
        return self._CompanyInfo

    @CompanyInfo.setter
    def CompanyInfo(self, CompanyInfo):
        self._CompanyInfo = CompanyInfo

    @property
    def CompanyId(self):
        """管理人公司ID
        :rtype: int
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def StatusInfo(self):
        """审核状态详细信息
        :rtype: list of ManagerStatusInfo
        """
        return self._StatusInfo

    @StatusInfo.setter
    def StatusInfo(self, StatusInfo):
        self._StatusInfo = StatusInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ManagerFirstName = params.get("ManagerFirstName")
        self._ManagerMail = params.get("ManagerMail")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ManagerLastName = params.get("ManagerLastName")
        self._ContactPosition = params.get("ContactPosition")
        self._ManagerPosition = params.get("ManagerPosition")
        self._VerifyTime = params.get("VerifyTime")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ContactLastName = params.get("ContactLastName")
        self._ManagerPhone = params.get("ManagerPhone")
        self._ContactPhone = params.get("ContactPhone")
        self._ContactMail = params.get("ContactMail")
        self._ManagerDepartment = params.get("ManagerDepartment")
        if params.get("CompanyInfo") is not None:
            self._CompanyInfo = CompanyInfo()
            self._CompanyInfo._deserialize(params.get("CompanyInfo"))
        self._CompanyId = params.get("CompanyId")
        self._ManagerId = params.get("ManagerId")
        if params.get("StatusInfo") is not None:
            self._StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = ManagerStatusInfo()
                obj._deserialize(item)
                self._StatusInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeManagersRequest(AbstractModel):
    """DescribeManagers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID,可以从DescribeCompanies接口获取
        :type CompanyId: int
        :param _Offset: 分页偏移量，如果不传默认值为0
        :type Offset: int
        :param _Limit: 分页每页数量，如果不传默认值为10，最大值为1000
        :type Limit: int
        :param _ManagerName: 管理人姓名（将废弃），请使用SearchKey
        :type ManagerName: str
        :param _ManagerMail: 模糊查询管理人邮箱（将废弃），请使用SearchKey
        :type ManagerMail: str
        :param _Status: 根据管理人状态进行筛选，取值有
'none' 未提交审核
'audit', 亚信审核中
'CAaudit' CA审核中
'ok' 已审核
'invalid'  审核失败
'expiring'  即将过期
'expired' 已过期
        :type Status: str
        :param _SearchKey: 根据这样的格式:管理人姓|管理人名|邮箱|部门 ,进行精准匹配
        :type SearchKey: str
        """
        self._CompanyId = None
        self._Offset = None
        self._Limit = None
        self._ManagerName = None
        self._ManagerMail = None
        self._Status = None
        self._SearchKey = None

    @property
    def CompanyId(self):
        """公司ID,可以从DescribeCompanies接口获取
        :rtype: int
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def Offset(self):
        """分页偏移量，如果不传默认值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页每页数量，如果不传默认值为10，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ManagerName(self):
        """管理人姓名（将废弃），请使用SearchKey
        :rtype: str
        """
        return self._ManagerName

    @ManagerName.setter
    def ManagerName(self, ManagerName):
        self._ManagerName = ManagerName

    @property
    def ManagerMail(self):
        """模糊查询管理人邮箱（将废弃），请使用SearchKey
        :rtype: str
        """
        return self._ManagerMail

    @ManagerMail.setter
    def ManagerMail(self, ManagerMail):
        self._ManagerMail = ManagerMail

    @property
    def Status(self):
        """根据管理人状态进行筛选，取值有
'none' 未提交审核
'audit', 亚信审核中
'CAaudit' CA审核中
'ok' 已审核
'invalid'  审核失败
'expiring'  即将过期
'expired' 已过期
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SearchKey(self):
        """根据这样的格式:管理人姓|管理人名|邮箱|部门 ,进行精准匹配
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ManagerName = params.get("ManagerName")
        self._ManagerMail = params.get("ManagerMail")
        self._Status = params.get("Status")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeManagersResponse(AbstractModel):
    """DescribeManagers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Managers: 公司管理人列表
        :type Managers: list of ManagerInfo
        :param _TotalCount: 公司管理人总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Managers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Managers(self):
        """公司管理人列表
        :rtype: list of ManagerInfo
        """
        return self._Managers

    @Managers.setter
    def Managers(self, Managers):
        self._Managers = Managers

    @property
    def TotalCount(self):
        """公司管理人总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Managers") is not None:
            self._Managers = []
            for item in params.get("Managers"):
                obj = ManagerInfo()
                obj._deserialize(item)
                self._Managers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePackagesRequest(AbstractModel):
    """DescribePackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 限制数目，默认20。
        :type Limit: int
        :param _Status: 按状态筛选。状态值包括usable(可用)，used(已用)，expired(已过期)，refund(已退款)

        :type Status: str
        :param _ExpireTime: 按过期时间升序或降序排列，可选值为asc(升序)和desc(降序)
        :type ExpireTime: str
        :param _PackageId: 按权益包ID搜索。
        :type PackageId: str
        :param _Type: 按权益包类型搜索。类型包括：ssl_100(证书批量权益100点)，ssl_500(证书批量权益500点），ssl_2000(证书批量权益2000点）
        :type Type: str
        :param _Pid: 子产品编号
        :type Pid: int
        """
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._ExpireTime = None
        self._PackageId = None
        self._Type = None
        self._Pid = None

    @property
    def Offset(self):
        """偏移量，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数目，默认20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """按状态筛选。状态值包括usable(可用)，used(已用)，expired(已过期)，refund(已退款)

        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        """按过期时间升序或降序排列，可选值为asc(升序)和desc(降序)
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PackageId(self):
        """按权益包ID搜索。
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Type(self):
        """按权益包类型搜索。类型包括：ssl_100(证书批量权益100点)，ssl_500(证书批量权益500点），ssl_2000(证书批量权益2000点）
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pid(self):
        """子产品编号
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._PackageId = params.get("PackageId")
        self._Type = params.get("Type")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackagesResponse(AbstractModel):
    """DescribePackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Packages: 权益包列表。
        :type Packages: list of PackageInfo
        :param _TotalCount: 总条数。
        :type TotalCount: int
        :param _TotalBalance: 权益点总余额。
        :type TotalBalance: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Packages = None
        self._TotalCount = None
        self._TotalBalance = None
        self._RequestId = None

    @property
    def Packages(self):
        """权益包列表。
        :rtype: list of PackageInfo
        """
        return self._Packages

    @Packages.setter
    def Packages(self, Packages):
        self._Packages = Packages

    @property
    def TotalCount(self):
        """总条数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalBalance(self):
        """权益点总余额。
        :rtype: int
        """
        return self._TotalBalance

    @TotalBalance.setter
    def TotalBalance(self, TotalBalance):
        self._TotalBalance = TotalBalance

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Packages") is not None:
            self._Packages = []
            for item in params.get("Packages"):
                obj = PackageInfo()
                obj._deserialize(item)
                self._Packages.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TotalBalance = params.get("TotalBalance")
        self._RequestId = params.get("RequestId")


class DomainValidationResult(AbstractModel):
    """证书域名验证结果

    """

    def __init__(self):
        r"""
        :param _Domain: 证书绑定的域名。
        :type Domain: str
        :param _VerifyType: 域名验证类型。 取值为：DNS、FILE、DNS_AUTO、DNS_PROXY、FILE_PROXY
        :type VerifyType: str
        :param _LocalCheck: 腾讯云检测结果，取值：1（验证通过）； -1（被限频或者 txt record not found）；-2（txt record not match）；-3（ns record not found）；-4（file not found）；-5（file not match）；-6（cname record not found）；-7（cname record not match）；-8（ns record not found）-9（file not found）；-10（file not match）

        :type LocalCheck: int
        :param _CaCheck: CA检查结果。取值： -1（未检测通过）；2（检测通过）
        :type CaCheck: int
        :param _LocalCheckFailReason: 检查失败原因。状态LocalCheck的具体描述
        :type LocalCheckFailReason: str
        :param _CheckValue: 检查到的值。
        :type CheckValue: list of str
        :param _Frequently: 是否被限频拦截， 取值：false（未被限频）；true（被限频）
        :type Frequently: bool
        :param _Issued: 证书是否已经签发。取值： false（未签发）；true（已签发）
        :type Issued: bool
        """
        self._Domain = None
        self._VerifyType = None
        self._LocalCheck = None
        self._CaCheck = None
        self._LocalCheckFailReason = None
        self._CheckValue = None
        self._Frequently = None
        self._Issued = None

    @property
    def Domain(self):
        """证书绑定的域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def VerifyType(self):
        """域名验证类型。 取值为：DNS、FILE、DNS_AUTO、DNS_PROXY、FILE_PROXY
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def LocalCheck(self):
        """腾讯云检测结果，取值：1（验证通过）； -1（被限频或者 txt record not found）；-2（txt record not match）；-3（ns record not found）；-4（file not found）；-5（file not match）；-6（cname record not found）；-7（cname record not match）；-8（ns record not found）-9（file not found）；-10（file not match）

        :rtype: int
        """
        return self._LocalCheck

    @LocalCheck.setter
    def LocalCheck(self, LocalCheck):
        self._LocalCheck = LocalCheck

    @property
    def CaCheck(self):
        """CA检查结果。取值： -1（未检测通过）；2（检测通过）
        :rtype: int
        """
        return self._CaCheck

    @CaCheck.setter
    def CaCheck(self, CaCheck):
        self._CaCheck = CaCheck

    @property
    def LocalCheckFailReason(self):
        """检查失败原因。状态LocalCheck的具体描述
        :rtype: str
        """
        return self._LocalCheckFailReason

    @LocalCheckFailReason.setter
    def LocalCheckFailReason(self, LocalCheckFailReason):
        self._LocalCheckFailReason = LocalCheckFailReason

    @property
    def CheckValue(self):
        """检查到的值。
        :rtype: list of str
        """
        return self._CheckValue

    @CheckValue.setter
    def CheckValue(self, CheckValue):
        self._CheckValue = CheckValue

    @property
    def Frequently(self):
        """是否被限频拦截， 取值：false（未被限频）；true（被限频）
        :rtype: bool
        """
        return self._Frequently

    @Frequently.setter
    def Frequently(self, Frequently):
        self._Frequently = Frequently

    @property
    def Issued(self):
        """证书是否已经签发。取值： false（未签发）；true（已签发）
        :rtype: bool
        """
        return self._Issued

    @Issued.setter
    def Issued(self, Issued):
        self._Issued = Issued


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._VerifyType = params.get("VerifyType")
        self._LocalCheck = params.get("LocalCheck")
        self._CaCheck = params.get("CaCheck")
        self._LocalCheckFailReason = params.get("LocalCheckFailReason")
        self._CheckValue = params.get("CheckValue")
        self._Frequently = params.get("Frequently")
        self._Issued = params.get("Issued")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCertificateResponse(AbstractModel):
    """DownloadCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: ZIP base64 编码内容，base64 解码后可保存为 ZIP 文件。
        :type Content: str
        :param _ContentType: MIME 类型：application/zip = ZIP 压缩文件。
        :type ContentType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._ContentType = None
        self._RequestId = None

    @property
    def Content(self):
        """ZIP base64 编码内容，base64 解码后可保存为 ZIP 文件。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentType(self):
        """MIME 类型：application/zip = ZIP 压缩文件。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._ContentType = params.get("ContentType")
        self._RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 DvAuthDetail 的内容。

    """

    def __init__(self):
        r"""
        :param _DvAuthKey: 证书域名验证记录Key
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param _DvAuthValue: 证书域名验证记录值
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param _DvAuthDomain: 证书域名验证域名值
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param _DvAuthPath: 证书域名验证文件路径， 仅FILE、FILE_PROXY使用
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param _DvAuthKeySubDomain: 证书域名验证子域名
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKeySubDomain: str
        :param _DvAuths: 证书域名验证信息， 存在多个域名验证使用本字段
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuths: list of DvAuths
        """
        self._DvAuthKey = None
        self._DvAuthValue = None
        self._DvAuthDomain = None
        self._DvAuthPath = None
        self._DvAuthKeySubDomain = None
        self._DvAuths = None

    @property
    def DvAuthKey(self):
        """证书域名验证记录Key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        """证书域名验证记录值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        """证书域名验证域名值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        """证书域名验证文件路径， 仅FILE、FILE_PROXY使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthKeySubDomain(self):
        """证书域名验证子域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DvAuthKeySubDomain

    @DvAuthKeySubDomain.setter
    def DvAuthKeySubDomain(self, DvAuthKeySubDomain):
        self._DvAuthKeySubDomain = DvAuthKeySubDomain

    @property
    def DvAuths(self):
        """证书域名验证信息， 存在多个域名验证使用本字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DvAuths
        """
        return self._DvAuths

    @DvAuths.setter
    def DvAuths(self, DvAuths):
        self._DvAuths = DvAuths


    def _deserialize(self, params):
        self._DvAuthKey = params.get("DvAuthKey")
        self._DvAuthValue = params.get("DvAuthValue")
        self._DvAuthDomain = params.get("DvAuthDomain")
        self._DvAuthPath = params.get("DvAuthPath")
        self._DvAuthKeySubDomain = params.get("DvAuthKeySubDomain")
        if params.get("DvAuths") is not None:
            self._DvAuths = []
            for item in params.get("DvAuths"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvAuths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DvAuths(AbstractModel):
    """返回参数键为 DvAuths 的内容。

    """

    def __init__(self):
        r"""
        :param _DvAuthKey: 证书域名验证记录Key
        :type DvAuthKey: str
        :param _DvAuthValue: 证书域名验证记录值
        :type DvAuthValue: str
        :param _DvAuthDomain: 证书域名验证域名值
        :type DvAuthDomain: str
        :param _DvAuthPath: 证书域名验证文件路径， 仅FILE、FILE_PROXY使用
        :type DvAuthPath: str
        :param _DvAuthSubDomain: 证书域名验证子域名
        :type DvAuthSubDomain: str
        :param _DvAuthVerifyType: 证书域名验证类型，取值：
TXT：DNS域名验证添加TXT记录
FILE：域名文件验证
CNAME：DNS域名验证添加CNAME记录
        :type DvAuthVerifyType: str
        """
        self._DvAuthKey = None
        self._DvAuthValue = None
        self._DvAuthDomain = None
        self._DvAuthPath = None
        self._DvAuthSubDomain = None
        self._DvAuthVerifyType = None

    @property
    def DvAuthKey(self):
        """证书域名验证记录Key
        :rtype: str
        """
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        """证书域名验证记录值
        :rtype: str
        """
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        """证书域名验证域名值
        :rtype: str
        """
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        """证书域名验证文件路径， 仅FILE、FILE_PROXY使用
        :rtype: str
        """
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthSubDomain(self):
        """证书域名验证子域名
        :rtype: str
        """
        return self._DvAuthSubDomain

    @DvAuthSubDomain.setter
    def DvAuthSubDomain(self, DvAuthSubDomain):
        self._DvAuthSubDomain = DvAuthSubDomain

    @property
    def DvAuthVerifyType(self):
        """证书域名验证类型，取值：
TXT：DNS域名验证添加TXT记录
FILE：域名文件验证
CNAME：DNS域名验证添加CNAME记录
        :rtype: str
        """
        return self._DvAuthVerifyType

    @DvAuthVerifyType.setter
    def DvAuthVerifyType(self, DvAuthVerifyType):
        self._DvAuthVerifyType = DvAuthVerifyType


    def _deserialize(self, params):
        self._DvAuthKey = params.get("DvAuthKey")
        self._DvAuthValue = params.get("DvAuthValue")
        self._DvAuthDomain = params.get("DvAuthDomain")
        self._DvAuthPath = params.get("DvAuthPath")
        self._DvAuthSubDomain = params.get("DvAuthSubDomain")
        self._DvAuthVerifyType = params.get("DvAuthVerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Error(AbstractModel):
    """错误异常

    """

    def __init__(self):
        r"""
        :param _Code: 异常错误码
        :type Code: str
        :param _Message: 异常错误信息
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        """异常错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """异常错误信息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤参数列表

    """

    def __init__(self):
        r"""
        :param _FilterKey: 过滤参数key
        :type FilterKey: str
        :param _FilterValue: 过滤参数值
        :type FilterValue: str
        """
        self._FilterKey = None
        self._FilterValue = None

    @property
    def FilterKey(self):
        """过滤参数key
        :rtype: str
        """
        return self._FilterKey

    @FilterKey.setter
    def FilterKey(self, FilterKey):
        self._FilterKey = FilterKey

    @property
    def FilterValue(self):
        """过滤参数值
        :rtype: str
        """
        return self._FilterValue

    @FilterValue.setter
    def FilterValue(self, FilterValue):
        self._FilterValue = FilterValue


    def _deserialize(self, params):
        self._FilterKey = params.get("FilterKey")
        self._FilterValue = params.get("FilterValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayCertificate(AbstractModel):
    """云原生网关证书信息

    """

    def __init__(self):
        r"""
        :param _Id: 网关证书ID
        :type Id: str
        :param _Name: 网关证书名称
        :type Name: str
        :param _BindDomains: 绑定域名
        :type BindDomains: list of str
        :param _CertSource: 证书来源
        :type CertSource: str
        :param _CertId: 当前绑定的SSL证书ID
        :type CertId: str
        """
        self._Id = None
        self._Name = None
        self._BindDomains = None
        self._CertSource = None
        self._CertId = None

    @property
    def Id(self):
        """网关证书ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """网关证书名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BindDomains(self):
        """绑定域名
        :rtype: list of str
        """
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def CertSource(self):
        """证书来源
        :rtype: str
        """
        return self._CertSource

    @CertSource.setter
    def CertSource(self, CertSource):
        self._CertSource = CertSource

    @property
    def CertId(self):
        """当前绑定的SSL证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._BindDomains = params.get("BindDomains")
        self._CertSource = params.get("CertSource")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostingConfig(AbstractModel):
    """托管配置

    """

    def __init__(self):
        r"""
        :param _ReplaceTime: 托管资源替换时间， 默认为证书过期前30天存在续费证书则替换
        :type ReplaceTime: int
        :param _MessageTypes: 托管发送消息类型：0，托管开始前消息提醒（没有续费证书也会收到该提示消息）； 1， 托管开始消息提醒（存在续费证书才会收到消息提醒）； 2， 托管资源替换失败消息提醒； 3 托管资源替换成功消息提醒
        :type MessageTypes: list of int
        :param _ReplaceStartTime: 资源替换开始时间
        :type ReplaceStartTime: str
        :param _ReplaceEndTime: 资源替换结束时间
        :type ReplaceEndTime: str
        """
        self._ReplaceTime = None
        self._MessageTypes = None
        self._ReplaceStartTime = None
        self._ReplaceEndTime = None

    @property
    def ReplaceTime(self):
        """托管资源替换时间， 默认为证书过期前30天存在续费证书则替换
        :rtype: int
        """
        return self._ReplaceTime

    @ReplaceTime.setter
    def ReplaceTime(self, ReplaceTime):
        self._ReplaceTime = ReplaceTime

    @property
    def MessageTypes(self):
        """托管发送消息类型：0，托管开始前消息提醒（没有续费证书也会收到该提示消息）； 1， 托管开始消息提醒（存在续费证书才会收到消息提醒）； 2， 托管资源替换失败消息提醒； 3 托管资源替换成功消息提醒
        :rtype: list of int
        """
        return self._MessageTypes

    @MessageTypes.setter
    def MessageTypes(self, MessageTypes):
        self._MessageTypes = MessageTypes

    @property
    def ReplaceStartTime(self):
        """资源替换开始时间
        :rtype: str
        """
        return self._ReplaceStartTime

    @ReplaceStartTime.setter
    def ReplaceStartTime(self, ReplaceStartTime):
        self._ReplaceStartTime = ReplaceStartTime

    @property
    def ReplaceEndTime(self):
        """资源替换结束时间
        :rtype: str
        """
        return self._ReplaceEndTime

    @ReplaceEndTime.setter
    def ReplaceEndTime(self, ReplaceEndTime):
        self._ReplaceEndTime = ReplaceEndTime


    def _deserialize(self, params):
        self._ReplaceTime = params.get("ReplaceTime")
        self._MessageTypes = params.get("MessageTypes")
        self._ReplaceStartTime = params.get("ReplaceStartTime")
        self._ReplaceEndTime = params.get("ReplaceEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LighthouseInstanceDetail(AbstractModel):
    """Lighthouse实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _IP: IP地址
        :type IP: list of str
        :param _Domain: 可选择域名
        :type Domain: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._IP = None
        self._Domain = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def IP(self):
        """IP地址
        :rtype: list of str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Domain(self):
        """可选择域名
        :rtype: list of str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._IP = params.get("IP")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveInstanceDetail(AbstractModel):
    """live实例详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 已绑定的证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _Status: -1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :type Status: int
        """
        self._Domain = None
        self._CertId = None
        self._Status = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """已绑定的证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        """-1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveInstanceList(AbstractModel):
    """live实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该地域下live实例总数	
        :type TotalCount: int
        :param _InstanceList: live实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of LiveInstanceDetail
        :param _Error: 是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._Error = None

    @property
    def TotalCount(self):
        """该地域下live实例总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        """live实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LiveInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def Error(self):
        """是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerInfo(AbstractModel):
    """管理人信息

    """

    def __init__(self):
        r"""
        :param _Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :type Status: str
        :param _ManagerFirstName: 管理人姓名
        :type ManagerFirstName: str
        :param _ManagerLastName: 管理人姓名
        :type ManagerLastName: str
        :param _ManagerPosition: 管理人职位
        :type ManagerPosition: str
        :param _ManagerPhone: 管理人电话
        :type ManagerPhone: str
        :param _ManagerMail: 管理人邮箱
        :type ManagerMail: str
        :param _ManagerDepartment: 管理人所属部门
        :type ManagerDepartment: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _DomainCount: 管理人域名数量
        :type DomainCount: int
        :param _CertCount: 管理人证书数量
        :type CertCount: int
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _ExpireTime: 审核有效到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _SubmitAuditTime: 最近一次提交审核时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitAuditTime: str
        :param _VerifyTime: 审核通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTime: str
        :param _StatusInfo: 具体审核状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInfo: list of ManagerStatusInfo
        :param _Tags: 标签
        :type Tags: list of Tags
        """
        self._Status = None
        self._ManagerFirstName = None
        self._ManagerLastName = None
        self._ManagerPosition = None
        self._ManagerPhone = None
        self._ManagerMail = None
        self._ManagerDepartment = None
        self._CreateTime = None
        self._DomainCount = None
        self._CertCount = None
        self._ManagerId = None
        self._ExpireTime = None
        self._SubmitAuditTime = None
        self._VerifyTime = None
        self._StatusInfo = None
        self._Tags = None

    @property
    def Status(self):
        """状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ManagerFirstName(self):
        """管理人姓名
        :rtype: str
        """
        return self._ManagerFirstName

    @ManagerFirstName.setter
    def ManagerFirstName(self, ManagerFirstName):
        self._ManagerFirstName = ManagerFirstName

    @property
    def ManagerLastName(self):
        """管理人姓名
        :rtype: str
        """
        return self._ManagerLastName

    @ManagerLastName.setter
    def ManagerLastName(self, ManagerLastName):
        self._ManagerLastName = ManagerLastName

    @property
    def ManagerPosition(self):
        """管理人职位
        :rtype: str
        """
        return self._ManagerPosition

    @ManagerPosition.setter
    def ManagerPosition(self, ManagerPosition):
        self._ManagerPosition = ManagerPosition

    @property
    def ManagerPhone(self):
        """管理人电话
        :rtype: str
        """
        return self._ManagerPhone

    @ManagerPhone.setter
    def ManagerPhone(self, ManagerPhone):
        self._ManagerPhone = ManagerPhone

    @property
    def ManagerMail(self):
        """管理人邮箱
        :rtype: str
        """
        return self._ManagerMail

    @ManagerMail.setter
    def ManagerMail(self, ManagerMail):
        self._ManagerMail = ManagerMail

    @property
    def ManagerDepartment(self):
        """管理人所属部门
        :rtype: str
        """
        return self._ManagerDepartment

    @ManagerDepartment.setter
    def ManagerDepartment(self, ManagerDepartment):
        self._ManagerDepartment = ManagerDepartment

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DomainCount(self):
        """管理人域名数量
        :rtype: int
        """
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def CertCount(self):
        """管理人证书数量
        :rtype: int
        """
        return self._CertCount

    @CertCount.setter
    def CertCount(self, CertCount):
        self._CertCount = CertCount

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def ExpireTime(self):
        """审核有效到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SubmitAuditTime(self):
        """最近一次提交审核时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubmitAuditTime

    @SubmitAuditTime.setter
    def SubmitAuditTime(self, SubmitAuditTime):
        self._SubmitAuditTime = SubmitAuditTime

    @property
    def VerifyTime(self):
        """审核通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyTime

    @VerifyTime.setter
    def VerifyTime(self, VerifyTime):
        self._VerifyTime = VerifyTime

    @property
    def StatusInfo(self):
        """具体审核状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ManagerStatusInfo
        """
        return self._StatusInfo

    @StatusInfo.setter
    def StatusInfo(self, StatusInfo):
        self._StatusInfo = StatusInfo

    @property
    def Tags(self):
        """标签
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ManagerFirstName = params.get("ManagerFirstName")
        self._ManagerLastName = params.get("ManagerLastName")
        self._ManagerPosition = params.get("ManagerPosition")
        self._ManagerPhone = params.get("ManagerPhone")
        self._ManagerMail = params.get("ManagerMail")
        self._ManagerDepartment = params.get("ManagerDepartment")
        self._CreateTime = params.get("CreateTime")
        self._DomainCount = params.get("DomainCount")
        self._CertCount = params.get("CertCount")
        self._ManagerId = params.get("ManagerId")
        self._ExpireTime = params.get("ExpireTime")
        self._SubmitAuditTime = params.get("SubmitAuditTime")
        self._VerifyTime = params.get("VerifyTime")
        if params.get("StatusInfo") is not None:
            self._StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = ManagerStatusInfo()
                obj._deserialize(item)
                self._StatusInfo.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerStatusInfo(AbstractModel):
    """管理人的四种审核状态

    """

    def __init__(self):
        r"""
        :param _Type: 审核类型，枚举值：ov,ev
        :type Type: str
        :param _Status: 审核状态，枚举值：pending,completed,invalid,submitted,expiring,expired
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        """
        self._Type = None
        self._Status = None
        self._CreateTime = None
        self._ExpireTime = None

    @property
    def Type(self):
        """审核类型，枚举值：ov,ev
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """审核状态，枚举值：pending,completed,invalid,submitted,expiring,expired
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        """过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasRequest(AbstractModel):
    """ModifyCertificateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _Alias: 备注名称。
        :type Alias: str
        """
        self._CertificateId = None
        self._Alias = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Alias(self):
        """备注名称。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasResponse(AbstractModel):
    """ModifyCertificateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 修改成功的证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """修改成功的证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIdList: 需要修改所属项目的证书 ID 集合，最多100个证书。
        :type CertificateIdList: list of str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        """
        self._CertificateIdList = None
        self._ProjectId = None

    @property
    def CertificateIdList(self):
        """需要修改所属项目的证书 ID 集合，最多100个证书。
        :rtype: list of str
        """
        return self._CertificateIdList

    @CertificateIdList.setter
    def CertificateIdList(self, CertificateIdList):
        self._CertificateIdList = CertificateIdList

    @property
    def ProjectId(self):
        """项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._CertificateIdList = params.get("CertificateIdList")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateProjectResponse(AbstractModel):
    """ModifyCertificateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessCertificates: 修改所属项目成功的证书集合。
        :type SuccessCertificates: list of str
        :param _FailCertificates: 修改所属项目失败的证书集合。
        :type FailCertificates: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessCertificates = None
        self._FailCertificates = None
        self._RequestId = None

    @property
    def SuccessCertificates(self):
        """修改所属项目成功的证书集合。
        :rtype: list of str
        """
        return self._SuccessCertificates

    @SuccessCertificates.setter
    def SuccessCertificates(self, SuccessCertificates):
        self._SuccessCertificates = SuccessCertificates

    @property
    def FailCertificates(self):
        """修改所属项目失败的证书集合。
        :rtype: list of str
        """
        return self._FailCertificates

    @FailCertificates.setter
    def FailCertificates(self, FailCertificates):
        self._FailCertificates = FailCertificates

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessCertificates = params.get("SuccessCertificates")
        self._FailCertificates = params.get("FailCertificates")
        self._RequestId = params.get("RequestId")


class ModifyCertificateResubmitRequest(AbstractModel):
    """ModifyCertificateResubmit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateResubmitResponse(AbstractModel):
    """ModifyCertificateResubmit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ModifyCertificatesExpiringNotificationSwitchRequest(AbstractModel):
    """ModifyCertificatesExpiringNotificationSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID列表。最多50个
        :type CertificateIds: list of str
        :param _SwitchStatus: 0:不忽略通知。1:忽略通知
        :type SwitchStatus: int
        """
        self._CertificateIds = None
        self._SwitchStatus = None

    @property
    def CertificateIds(self):
        """证书ID列表。最多50个
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def SwitchStatus(self):
        """0:不忽略通知。1:忽略通知
        :rtype: int
        """
        return self._SwitchStatus

    @SwitchStatus.setter
    def SwitchStatus(self, SwitchStatus):
        self._SwitchStatus = SwitchStatus


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._SwitchStatus = params.get("SwitchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificatesExpiringNotificationSwitchResponse(AbstractModel):
    """ModifyCertificatesExpiringNotificationSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID列表
        :type CertificateIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateIds = None
        self._RequestId = None

    @property
    def CertificateIds(self):
        """证书ID列表
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """证书操作日志。

    """

    def __init__(self):
        r"""
        :param _Action: 操作证书动作。
        :type Action: str
        :param _CreatedOn: 操作时间。
        :type CreatedOn: str
        :param _Uin: 主账号
        :type Uin: str
        :param _SubAccountUin: 子账号
        :type SubAccountUin: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _Type: 每个操作类型都对应一个具体的操作描述。以下是对每个操作类型及其描述的文字说明：
1. apply - 表示申请一个免费的证书。
2. delete - 表示删除操作。
3. download - 表示下载操作。
4. upload - 表示上传操作。
5. revoke - 表示吊销证书。
6. cancelRevoke - 表示取消吊销操作。
7. updateAlias - 表示更新备注信息。
8. changeProject - 表示将证书分配到某个项目。
9. uploadConfirmLetter - 表示上传确认函。
10. cancel - 表示取消订单操作。
11. replace - 表示重颁发证书。
12. downloadConfirmLetter - 表示下载证书吊销确认函。
13. editRevokeLetter - 表示上传证书吊销确认函。
14. renewVIP - 表示续费付费证书。
15. applyVIP - 表示申请付费证书。
16. submitInfo - 表示提交资料。
17. downloadConfirmLetter - 表示下载确认函模版。
18. uploadFromYunAPI - 表示通过云 API 上传。
19. transferIn - 表示证书转入操作。
20. transferOut - 表示证书转出操作。
21. refund - 表示申请退款。
22. multiYearsRenew - 表示多年期自动续期。
23. modifyDownloadLimit - 表示修改下载限制开关。
24. issued - 表示证书签发。
25. domainValidationPassed - 表示域名验证完成。
26. Resubmit - 表示证书重新申请。
        :type Type: str
        """
        self._Action = None
        self._CreatedOn = None
        self._Uin = None
        self._SubAccountUin = None
        self._CertId = None
        self._Type = None

    @property
    def Action(self):
        """操作证书动作。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CreatedOn(self):
        """操作时间。
        :rtype: str
        """
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def Uin(self):
        """主账号
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        """子账号
        :rtype: str
        """
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Type(self):
        """每个操作类型都对应一个具体的操作描述。以下是对每个操作类型及其描述的文字说明：
1. apply - 表示申请一个免费的证书。
2. delete - 表示删除操作。
3. download - 表示下载操作。
4. upload - 表示上传操作。
5. revoke - 表示吊销证书。
6. cancelRevoke - 表示取消吊销操作。
7. updateAlias - 表示更新备注信息。
8. changeProject - 表示将证书分配到某个项目。
9. uploadConfirmLetter - 表示上传确认函。
10. cancel - 表示取消订单操作。
11. replace - 表示重颁发证书。
12. downloadConfirmLetter - 表示下载证书吊销确认函。
13. editRevokeLetter - 表示上传证书吊销确认函。
14. renewVIP - 表示续费付费证书。
15. applyVIP - 表示申请付费证书。
16. submitInfo - 表示提交资料。
17. downloadConfirmLetter - 表示下载确认函模版。
18. uploadFromYunAPI - 表示通过云 API 上传。
19. transferIn - 表示证书转入操作。
20. transferOut - 表示证书转出操作。
21. refund - 表示申请退款。
22. multiYearsRenew - 表示多年期自动续期。
23. modifyDownloadLimit - 表示修改下载限制开关。
24. issued - 表示证书签发。
25. domainValidationPassed - 表示域名验证完成。
26. Resubmit - 表示证书重新申请。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CreatedOn = params.get("CreatedOn")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._CertId = params.get("CertId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageInfo(AbstractModel):
    """权益包基本信息

    """

    def __init__(self):
        r"""
        :param _PackageId: 权益包ID。
        :type PackageId: str
        :param _Total: 权益包内权益点总量。
        :type Total: int
        :param _Balance: 权益包内权益点余量。
        :type Balance: int
        :param _Type: 权益包名称。
        :type Type: str
        :param _SourceUin: 权益点是转入时，来源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceUin: int
        :param _Status: 权益点状态。
        :type Status: str
        :param _ExpireTime: 过期时间。
        :type ExpireTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _CreateTime: 生成时间。
        :type CreateTime: str
        :param _SourceType: 来源类型。
        :type SourceType: str
        :param _TransferOutInfos: 转移信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferOutInfos: list of PackageTransferOutInfo
        """
        self._PackageId = None
        self._Total = None
        self._Balance = None
        self._Type = None
        self._SourceUin = None
        self._Status = None
        self._ExpireTime = None
        self._UpdateTime = None
        self._CreateTime = None
        self._SourceType = None
        self._TransferOutInfos = None

    @property
    def PackageId(self):
        """权益包ID。
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Total(self):
        """权益包内权益点总量。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Balance(self):
        """权益包内权益点余量。
        :rtype: int
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def Type(self):
        """权益包名称。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SourceUin(self):
        """权益点是转入时，来源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SourceUin

    @SourceUin.setter
    def SourceUin(self, SourceUin):
        self._SourceUin = SourceUin

    @property
    def Status(self):
        """权益点状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        """过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UpdateTime(self):
        """更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        """生成时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SourceType(self):
        """来源类型。
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TransferOutInfos(self):
        """转移信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PackageTransferOutInfo
        """
        return self._TransferOutInfos

    @TransferOutInfos.setter
    def TransferOutInfos(self, TransferOutInfos):
        self._TransferOutInfos = TransferOutInfos


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._Total = params.get("Total")
        self._Balance = params.get("Balance")
        self._Type = params.get("Type")
        self._SourceUin = params.get("SourceUin")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._SourceType = params.get("SourceType")
        if params.get("TransferOutInfos") is not None:
            self._TransferOutInfos = []
            for item in params.get("TransferOutInfos"):
                obj = PackageTransferOutInfo()
                obj._deserialize(item)
                self._TransferOutInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageTransferOutInfo(AbstractModel):
    """权益包转出详情

    """

    def __init__(self):
        r"""
        :param _PackageId: 权益包ID。
        :type PackageId: str
        :param _TransferCode: 转移码。
        :type TransferCode: str
        :param _TransferCount: 本次转移点数。
        :type TransferCount: int
        :param _ReceivePackageId: 转入的PackageID。
        :type ReceivePackageId: str
        :param _ExpireTime: 本次转移过期时间。
        :type ExpireTime: str
        :param _CreateTime: 本次转移生成时间。
        :type CreateTime: str
        :param _UpdateTime: 本次转移更新时间。
        :type UpdateTime: str
        :param _TransferStatus: 转移状态。
        :type TransferStatus: str
        :param _ReceiverUin: 接收者uin。
        :type ReceiverUin: int
        :param _ReceiveTime: 接收时间。
        :type ReceiveTime: str
        """
        self._PackageId = None
        self._TransferCode = None
        self._TransferCount = None
        self._ReceivePackageId = None
        self._ExpireTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TransferStatus = None
        self._ReceiverUin = None
        self._ReceiveTime = None

    @property
    def PackageId(self):
        """权益包ID。
        :rtype: str
        """
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def TransferCode(self):
        """转移码。
        :rtype: str
        """
        return self._TransferCode

    @TransferCode.setter
    def TransferCode(self, TransferCode):
        self._TransferCode = TransferCode

    @property
    def TransferCount(self):
        """本次转移点数。
        :rtype: int
        """
        return self._TransferCount

    @TransferCount.setter
    def TransferCount(self, TransferCount):
        self._TransferCount = TransferCount

    @property
    def ReceivePackageId(self):
        """转入的PackageID。
        :rtype: str
        """
        return self._ReceivePackageId

    @ReceivePackageId.setter
    def ReceivePackageId(self, ReceivePackageId):
        self._ReceivePackageId = ReceivePackageId

    @property
    def ExpireTime(self):
        """本次转移过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreateTime(self):
        """本次转移生成时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """本次转移更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TransferStatus(self):
        """转移状态。
        :rtype: str
        """
        return self._TransferStatus

    @TransferStatus.setter
    def TransferStatus(self, TransferStatus):
        self._TransferStatus = TransferStatus

    @property
    def ReceiverUin(self):
        """接收者uin。
        :rtype: int
        """
        return self._ReceiverUin

    @ReceiverUin.setter
    def ReceiverUin(self, ReceiverUin):
        self._ReceiverUin = ReceiverUin

    @property
    def ReceiveTime(self):
        """接收时间。
        :rtype: str
        """
        return self._ReceiveTime

    @ReceiveTime.setter
    def ReceiveTime(self, ReceiveTime):
        self._ReceiveTime = ReceiveTime


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._TransferCode = params.get("TransferCode")
        self._TransferCount = params.get("TransferCount")
        self._ReceivePackageId = params.get("ReceivePackageId")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TransferStatus = params.get("TransferStatus")
        self._ReceiverUin = params.get("ReceiverUin")
        self._ReceiveTime = params.get("ReceiveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreAuditInfo(AbstractModel):
    """预审核信息列表

    """

    def __init__(self):
        r"""
        :param _TotalPeriod: 证书总年限
        :type TotalPeriod: int
        :param _NowPeriod: 证书当前年限
        :type NowPeriod: int
        :param _ManagerId: 证书预审核管理人ID
        :type ManagerId: str
        """
        self._TotalPeriod = None
        self._NowPeriod = None
        self._ManagerId = None

    @property
    def TotalPeriod(self):
        """证书总年限
        :rtype: int
        """
        return self._TotalPeriod

    @TotalPeriod.setter
    def TotalPeriod(self, TotalPeriod):
        self._TotalPeriod = TotalPeriod

    @property
    def NowPeriod(self):
        """证书当前年限
        :rtype: int
        """
        return self._NowPeriod

    @NowPeriod.setter
    def NowPeriod(self, NowPeriod):
        self._NowPeriod = NowPeriod

    @property
    def ManagerId(self):
        """证书预审核管理人ID
        :rtype: str
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._TotalPeriod = params.get("TotalPeriod")
        self._NowPeriod = params.get("NowPeriod")
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 下，key为 ProjectInfo 的内容。

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称。
        :type ProjectName: str
        :param _ProjectCreatorUin: 项目创建用户 UIN。
        :type ProjectCreatorUin: int
        :param _ProjectCreateTime: 项目创建时间。
        :type ProjectCreateTime: str
        :param _ProjectResume: 项目信息简述。
        :type ProjectResume: str
        :param _OwnerUin: 用户 UIN。
        :type OwnerUin: int
        :param _ProjectId: 项目 ID。
        :type ProjectId: str
        """
        self._ProjectName = None
        self._ProjectCreatorUin = None
        self._ProjectCreateTime = None
        self._ProjectResume = None
        self._OwnerUin = None
        self._ProjectId = None

    @property
    def ProjectName(self):
        """项目名称。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectCreatorUin(self):
        """项目创建用户 UIN。
        :rtype: int
        """
        return self._ProjectCreatorUin

    @ProjectCreatorUin.setter
    def ProjectCreatorUin(self, ProjectCreatorUin):
        self._ProjectCreatorUin = ProjectCreatorUin

    @property
    def ProjectCreateTime(self):
        """项目创建时间。
        :rtype: str
        """
        return self._ProjectCreateTime

    @ProjectCreateTime.setter
    def ProjectCreateTime(self, ProjectCreateTime):
        self._ProjectCreateTime = ProjectCreateTime

    @property
    def ProjectResume(self):
        """项目信息简述。
        :rtype: str
        """
        return self._ProjectResume

    @ProjectResume.setter
    def ProjectResume(self, ProjectResume):
        self._ProjectResume = ProjectResume

    @property
    def OwnerUin(self):
        """用户 UIN。
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """项目 ID。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectCreatorUin = params.get("ProjectCreatorUin")
        self._ProjectCreateTime = params.get("ProjectCreateTime")
        self._ProjectResume = params.get("ProjectResume")
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateRequest(AbstractModel):
    """ReplaceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _ValidType: 验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :type ValidType: str
        :param _CsrType: 类型，默认 Original。可选项：Original = 原证书 CSR，Upload = 手动上传，Online = 在线生成。
        :type CsrType: str
        :param _CsrContent: CSR 内容，手动上传的时候需要。
        :type CsrContent: str
        :param _CsrkeyPassword: KEY 密码。
        :type CsrkeyPassword: str
        :param _Reason: 重颁发原因。
        :type Reason: str
        :param _CertCSREncryptAlgo: CSR加密方式，可选：RSA、ECC、SM2
（CsrType为Online才可选）， 默认为RSA
        :type CertCSREncryptAlgo: str
        :param _CertCSRKeyParameter: CSR加密参数，CsrEncryptAlgo为RSA时， 可选2048、4096等默认为2048；CsrEncryptAlgo为ECC时，可选prime256v1，secp384r1等，默认为prime256v1; 
        :type CertCSRKeyParameter: str
        """
        self._CertificateId = None
        self._ValidType = None
        self._CsrType = None
        self._CsrContent = None
        self._CsrkeyPassword = None
        self._Reason = None
        self._CertCSREncryptAlgo = None
        self._CertCSRKeyParameter = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ValidType(self):
        """验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :rtype: str
        """
        return self._ValidType

    @ValidType.setter
    def ValidType(self, ValidType):
        self._ValidType = ValidType

    @property
    def CsrType(self):
        """类型，默认 Original。可选项：Original = 原证书 CSR，Upload = 手动上传，Online = 在线生成。
        :rtype: str
        """
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        """CSR 内容，手动上传的时候需要。
        :rtype: str
        """
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CsrkeyPassword(self):
        """KEY 密码。
        :rtype: str
        """
        return self._CsrkeyPassword

    @CsrkeyPassword.setter
    def CsrkeyPassword(self, CsrkeyPassword):
        self._CsrkeyPassword = CsrkeyPassword

    @property
    def Reason(self):
        """重颁发原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def CertCSREncryptAlgo(self):
        """CSR加密方式，可选：RSA、ECC、SM2
（CsrType为Online才可选）， 默认为RSA
        :rtype: str
        """
        return self._CertCSREncryptAlgo

    @CertCSREncryptAlgo.setter
    def CertCSREncryptAlgo(self, CertCSREncryptAlgo):
        self._CertCSREncryptAlgo = CertCSREncryptAlgo

    @property
    def CertCSRKeyParameter(self):
        """CSR加密参数，CsrEncryptAlgo为RSA时， 可选2048、4096等默认为2048；CsrEncryptAlgo为ECC时，可选prime256v1，secp384r1等，默认为prime256v1; 
        :rtype: str
        """
        return self._CertCSRKeyParameter

    @CertCSRKeyParameter.setter
    def CertCSRKeyParameter(self, CertCSRKeyParameter):
        self._CertCSRKeyParameter = CertCSRKeyParameter


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ValidType = params.get("ValidType")
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CsrkeyPassword = params.get("CsrkeyPassword")
        self._Reason = params.get("Reason")
        self._CertCSREncryptAlgo = params.get("CertCSREncryptAlgo")
        self._CertCSRKeyParameter = params.get("CertCSRKeyParameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateResponse(AbstractModel):
    """ReplaceCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ResourceTypeRegions(AbstractModel):
    """云资源地域列表

    """

    def __init__(self):
        r"""
        :param _ResourceType: 云资源类型，支持clb、waf、apigateway、cos、tke、tse、tcb
        :type ResourceType: str
        :param _Regions: 地域列表
        :type Regions: list of str
        """
        self._ResourceType = None
        self._Regions = None

    @property
    def ResourceType(self):
        """云资源类型，支持clb、waf、apigateway、cos、tke、tse、tcb
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Regions(self):
        """地域列表
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeCertificateRequest(AbstractModel):
    """RevokeCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _Reason: 吊销证书原因。
        :type Reason: str
        """
        self._CertificateId = None
        self._Reason = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Reason(self):
        """吊销证书原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeCertificateResponse(AbstractModel):
    """RevokeCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RevokeDomainValidateAuths: 吊销证书域名验证信息。
        :type RevokeDomainValidateAuths: list of RevokeDomainValidateAuths
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RevokeDomainValidateAuths = None
        self._RequestId = None

    @property
    def RevokeDomainValidateAuths(self):
        """吊销证书域名验证信息。
        :rtype: list of RevokeDomainValidateAuths
        """
        return self._RevokeDomainValidateAuths

    @RevokeDomainValidateAuths.setter
    def RevokeDomainValidateAuths(self, RevokeDomainValidateAuths):
        self._RevokeDomainValidateAuths = RevokeDomainValidateAuths

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RevokeDomainValidateAuths") is not None:
            self._RevokeDomainValidateAuths = []
            for item in params.get("RevokeDomainValidateAuths"):
                obj = RevokeDomainValidateAuths()
                obj._deserialize(item)
                self._RevokeDomainValidateAuths.append(obj)
        self._RequestId = params.get("RequestId")


class RevokeDomainValidateAuths(AbstractModel):
    """吊销证书域名验证信息。

    """

    def __init__(self):
        r"""
        :param _DomainValidateAuthPath: DV 认证值路径。
        :type DomainValidateAuthPath: str
        :param _DomainValidateAuthKey: DV 认证 KEY。
        :type DomainValidateAuthKey: str
        :param _DomainValidateAuthValue: DV 认证值。
        :type DomainValidateAuthValue: str
        :param _DomainValidateAuthDomain: DV 认证域名。
        :type DomainValidateAuthDomain: str
        """
        self._DomainValidateAuthPath = None
        self._DomainValidateAuthKey = None
        self._DomainValidateAuthValue = None
        self._DomainValidateAuthDomain = None

    @property
    def DomainValidateAuthPath(self):
        """DV 认证值路径。
        :rtype: str
        """
        return self._DomainValidateAuthPath

    @DomainValidateAuthPath.setter
    def DomainValidateAuthPath(self, DomainValidateAuthPath):
        self._DomainValidateAuthPath = DomainValidateAuthPath

    @property
    def DomainValidateAuthKey(self):
        """DV 认证 KEY。
        :rtype: str
        """
        return self._DomainValidateAuthKey

    @DomainValidateAuthKey.setter
    def DomainValidateAuthKey(self, DomainValidateAuthKey):
        self._DomainValidateAuthKey = DomainValidateAuthKey

    @property
    def DomainValidateAuthValue(self):
        """DV 认证值。
        :rtype: str
        """
        return self._DomainValidateAuthValue

    @DomainValidateAuthValue.setter
    def DomainValidateAuthValue(self, DomainValidateAuthValue):
        self._DomainValidateAuthValue = DomainValidateAuthValue

    @property
    def DomainValidateAuthDomain(self):
        """DV 认证域名。
        :rtype: str
        """
        return self._DomainValidateAuthDomain

    @DomainValidateAuthDomain.setter
    def DomainValidateAuthDomain(self, DomainValidateAuthDomain):
        self._DomainValidateAuthDomain = DomainValidateAuthDomain


    def _deserialize(self, params):
        self._DomainValidateAuthPath = params.get("DomainValidateAuthPath")
        self._DomainValidateAuthKey = params.get("DomainValidateAuthKey")
        self._DomainValidateAuthValue = params.get("DomainValidateAuthValue")
        self._DomainValidateAuthDomain = params.get("DomainValidateAuthDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RootCertificates(AbstractModel):
    """根证书

    """

    def __init__(self):
        r"""
        :param _Sign: 国密签名证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Sign: str
        :param _Encrypt: 国密加密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: str
        :param _Standard: 标准证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        """
        self._Sign = None
        self._Encrypt = None
        self._Standard = None

    @property
    def Sign(self):
        """国密签名证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def Encrypt(self):
        """国密加密证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def Standard(self):
        """标准证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard


    def _deserialize(self, params):
        self._Sign = params.get("Sign")
        self._Encrypt = params.get("Encrypt")
        self._Standard = params.get("Standard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAuditManagerRequest(AbstractModel):
    """SubmitAuditManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        """
        self._ManagerId = None

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAuditManagerResponse(AbstractModel):
    """SubmitAuditManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ManagerId = None
        self._RequestId = None

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._RequestId = params.get("RequestId")


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待提交资料的付费证书 ID。
        :type CertificateId: str
        :param _CsrType: 此字段必传。 CSR 生成方式， 取值为：
online：腾讯云提交的填写的参数信息生成CSR和私钥， 并由腾讯云加密存储
parse：自行生成CSR和私钥， 并通过上传CSR申请证书
        :type CsrType: str
        :param _CsrContent: 上传的 CSR 内容。
若CstType为parse， 则此字段必传。
        :type CsrContent: str
        :param _CertificateDomain: 证书绑定的通用名称， 若是上传的CSR，则该域名需与CSR解析的通用名称一致
        :type CertificateDomain: str
        :param _DomainList: 证书绑定的其他域名， 单域名、泛域名证书无需提供。 多域名、多泛域名必填
        :type DomainList: list of str
        :param _KeyPassword: 私钥密码， 目前仅使用在生成jks、pfx格式证书时密码； 其他格式私钥证书未加密	
        :type KeyPassword: str
        :param _OrganizationName: 字段必传， 公司名称。
        :type OrganizationName: str
        :param _OrganizationDivision: 字段必传， 部门名称。
        :type OrganizationDivision: str
        :param _OrganizationAddress: 字段必传， 公司详细地址。
        :type OrganizationAddress: str
        :param _OrganizationCountry: 字段必传， 国家名称，传CN即可
        :type OrganizationCountry: str
        :param _OrganizationCity: 字段必传， 公司所在城市。
        :type OrganizationCity: str
        :param _OrganizationRegion: 字段必传， 公司所在省份。
        :type OrganizationRegion: str
        :param _PostalCode: 公司邮编。
        :type PostalCode: str
        :param _PhoneAreaCode: 字段必传， 公司座机区号。
        :type PhoneAreaCode: str
        :param _PhoneNumber: 字段必传， 公司座机号码。
        :type PhoneNumber: str
        :param _VerifyType: 证书验证方式。验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :type VerifyType: str
        :param _AdminFirstName: 字段必传，管理人名。
        :type AdminFirstName: str
        :param _AdminLastName: 字段必传，管理人姓。
        :type AdminLastName: str
        :param _AdminPhoneNum: 字段必传，管理人手机号码。
        :type AdminPhoneNum: str
        :param _AdminEmail: 字段必传，管理人邮箱地址。
        :type AdminEmail: str
        :param _AdminPosition: 字段必传，管理人职位。
        :type AdminPosition: str
        :param _ContactFirstName: 字段必传，联系人名。
        :type ContactFirstName: str
        :param _ContactLastName: 字段必传，联系人姓。
        :type ContactLastName: str
        :param _ContactEmail: 字段必传，联系人邮箱地址。
        :type ContactEmail: str
        :param _ContactNumber: 字段必传，联系人手机号码。
        :type ContactNumber: str
        :param _ContactPosition: 字段必传，联系人职位。
        :type ContactPosition: str
        :param _IsDV: 是否DV证书。默认false
        :type IsDV: bool
        """
        self._CertificateId = None
        self._CsrType = None
        self._CsrContent = None
        self._CertificateDomain = None
        self._DomainList = None
        self._KeyPassword = None
        self._OrganizationName = None
        self._OrganizationDivision = None
        self._OrganizationAddress = None
        self._OrganizationCountry = None
        self._OrganizationCity = None
        self._OrganizationRegion = None
        self._PostalCode = None
        self._PhoneAreaCode = None
        self._PhoneNumber = None
        self._VerifyType = None
        self._AdminFirstName = None
        self._AdminLastName = None
        self._AdminPhoneNum = None
        self._AdminEmail = None
        self._AdminPosition = None
        self._ContactFirstName = None
        self._ContactLastName = None
        self._ContactEmail = None
        self._ContactNumber = None
        self._ContactPosition = None
        self._IsDV = None

    @property
    def CertificateId(self):
        """待提交资料的付费证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CsrType(self):
        """此字段必传。 CSR 生成方式， 取值为：
online：腾讯云提交的填写的参数信息生成CSR和私钥， 并由腾讯云加密存储
parse：自行生成CSR和私钥， 并通过上传CSR申请证书
        :rtype: str
        """
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        """上传的 CSR 内容。
若CstType为parse， 则此字段必传。
        :rtype: str
        """
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        """证书绑定的通用名称， 若是上传的CSR，则该域名需与CSR解析的通用名称一致
        :rtype: str
        """
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        """证书绑定的其他域名， 单域名、泛域名证书无需提供。 多域名、多泛域名必填
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        """私钥密码， 目前仅使用在生成jks、pfx格式证书时密码； 其他格式私钥证书未加密	
        :rtype: str
        """
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        """字段必传， 公司名称。
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        """字段必传， 部门名称。
        :rtype: str
        """
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        """字段必传， 公司详细地址。
        :rtype: str
        """
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        """字段必传， 国家名称，传CN即可
        :rtype: str
        """
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        """字段必传， 公司所在城市。
        :rtype: str
        """
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        """字段必传， 公司所在省份。
        :rtype: str
        """
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        """公司邮编。
        :rtype: str
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        """字段必传， 公司座机区号。
        :rtype: str
        """
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        """字段必传， 公司座机号码。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def VerifyType(self):
        """证书验证方式。验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def AdminFirstName(self):
        """字段必传，管理人名。
        :rtype: str
        """
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        """字段必传，管理人姓。
        :rtype: str
        """
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        """字段必传，管理人手机号码。
        :rtype: str
        """
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        """字段必传，管理人邮箱地址。
        :rtype: str
        """
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        """字段必传，管理人职位。
        :rtype: str
        """
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        """字段必传，联系人名。
        :rtype: str
        """
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        """字段必传，联系人姓。
        :rtype: str
        """
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactEmail(self):
        """字段必传，联系人邮箱地址。
        :rtype: str
        """
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactNumber(self):
        """字段必传，联系人手机号码。
        :rtype: str
        """
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactPosition(self):
        """字段必传，联系人职位。
        :rtype: str
        """
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def IsDV(self):
        """是否DV证书。默认false
        :rtype: bool
        """
        return self._IsDV

    @IsDV.setter
    def IsDV(self, IsDV):
        self._IsDV = IsDV


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CertificateDomain = params.get("CertificateDomain")
        self._DomainList = params.get("DomainList")
        self._KeyPassword = params.get("KeyPassword")
        self._OrganizationName = params.get("OrganizationName")
        self._OrganizationDivision = params.get("OrganizationDivision")
        self._OrganizationAddress = params.get("OrganizationAddress")
        self._OrganizationCountry = params.get("OrganizationCountry")
        self._OrganizationCity = params.get("OrganizationCity")
        self._OrganizationRegion = params.get("OrganizationRegion")
        self._PostalCode = params.get("PostalCode")
        self._PhoneAreaCode = params.get("PhoneAreaCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._VerifyType = params.get("VerifyType")
        self._AdminFirstName = params.get("AdminFirstName")
        self._AdminLastName = params.get("AdminLastName")
        self._AdminPhoneNum = params.get("AdminPhoneNum")
        self._AdminEmail = params.get("AdminEmail")
        self._AdminPosition = params.get("AdminPosition")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ContactLastName = params.get("ContactLastName")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactNumber = params.get("ContactNumber")
        self._ContactPosition = params.get("ContactPosition")
        self._IsDV = params.get("IsDV")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCertificateInformationResponse(AbstractModel):
    """SubmitCertificateInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 SubmittedData 的内容。

    """

    def __init__(self):
        r"""
        :param _CsrType: CSR 类型，（online = 在线生成CSR，parse = 粘贴 CSR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrType: str
        :param _CsrContent: CSR 内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrContent: str
        :param _CertificateDomain: 域名信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateDomain: str
        :param _DomainList: DNS 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of str
        :param _KeyPassword: 私钥密码。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyPassword: str
        :param _OrganizationName: 企业或单位名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param _OrganizationDivision: 部门。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationDivision: str
        :param _OrganizationAddress: 地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationAddress: str
        :param _OrganizationCountry: 国家。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCountry: str
        :param _OrganizationCity: 市。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCity: str
        :param _OrganizationRegion: 省。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationRegion: str
        :param _PostalCode: 邮政编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostalCode: str
        :param _PhoneAreaCode: 座机区号。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneAreaCode: str
        :param _PhoneNumber: 座机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _AdminFirstName: 管理员名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminFirstName: str
        :param _AdminLastName: 管理员姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminLastName: str
        :param _AdminPhoneNum: 管理员电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPhoneNum: str
        :param _AdminEmail: 管理员邮箱地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminEmail: str
        :param _AdminPosition: 管理员职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPosition: str
        :param _ContactFirstName: 联系人名。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactFirstName: str
        :param _ContactLastName: 联系人姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactLastName: str
        :param _ContactNumber: 联系人电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactNumber: str
        :param _ContactEmail: 联系人邮箱地址，
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactEmail: str
        :param _ContactPosition: 联系人职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactPosition: str
        :param _VerifyType: 验证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        """
        self._CsrType = None
        self._CsrContent = None
        self._CertificateDomain = None
        self._DomainList = None
        self._KeyPassword = None
        self._OrganizationName = None
        self._OrganizationDivision = None
        self._OrganizationAddress = None
        self._OrganizationCountry = None
        self._OrganizationCity = None
        self._OrganizationRegion = None
        self._PostalCode = None
        self._PhoneAreaCode = None
        self._PhoneNumber = None
        self._AdminFirstName = None
        self._AdminLastName = None
        self._AdminPhoneNum = None
        self._AdminEmail = None
        self._AdminPosition = None
        self._ContactFirstName = None
        self._ContactLastName = None
        self._ContactNumber = None
        self._ContactEmail = None
        self._ContactPosition = None
        self._VerifyType = None

    @property
    def CsrType(self):
        """CSR 类型，（online = 在线生成CSR，parse = 粘贴 CSR）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        """CSR 内容。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        """域名信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        """DNS 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        """私钥密码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        """企业或单位名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        """部门。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        """地址。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        """国家。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        """市。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        """省。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        """邮政编码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        """座机区号。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        """座机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AdminFirstName(self):
        """管理员名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        """管理员姓。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        """管理员电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        """管理员邮箱地址。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        """管理员职位。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        """联系人名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        """联系人姓。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactNumber(self):
        """联系人电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactEmail(self):
        """联系人邮箱地址，
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPosition(self):
        """联系人职位。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def VerifyType(self):
        """验证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CertificateDomain = params.get("CertificateDomain")
        self._DomainList = params.get("DomainList")
        self._KeyPassword = params.get("KeyPassword")
        self._OrganizationName = params.get("OrganizationName")
        self._OrganizationDivision = params.get("OrganizationDivision")
        self._OrganizationAddress = params.get("OrganizationAddress")
        self._OrganizationCountry = params.get("OrganizationCountry")
        self._OrganizationCity = params.get("OrganizationCity")
        self._OrganizationRegion = params.get("OrganizationRegion")
        self._PostalCode = params.get("PostalCode")
        self._PhoneAreaCode = params.get("PhoneAreaCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AdminFirstName = params.get("AdminFirstName")
        self._AdminLastName = params.get("AdminLastName")
        self._AdminPhoneNum = params.get("AdminPhoneNum")
        self._AdminEmail = params.get("AdminEmail")
        self._AdminPosition = params.get("AdminPosition")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ContactLastName = params.get("ContactLastName")
        self._ContactNumber = params.get("ContactNumber")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactPosition = params.get("ContactPosition")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportDownloadType(AbstractModel):
    """支持下载的类型

    """

    def __init__(self):
        r"""
        :param _NGINX: 是否可以下载nginx可用格式
        :type NGINX: bool
        :param _APACHE: 是否可以下载apache可用格式
        :type APACHE: bool
        :param _TOMCAT: 是否可以下载tomcat可用格式
        :type TOMCAT: bool
        :param _IIS: 是否可以下载iis可用格式
        :type IIS: bool
        :param _JKS: 是否可以下载JKS可用格式
        :type JKS: bool
        :param _OTHER: 是否可以下载其他格式
        :type OTHER: bool
        :param _ROOT: 是否可以下载根证书
        :type ROOT: bool
        """
        self._NGINX = None
        self._APACHE = None
        self._TOMCAT = None
        self._IIS = None
        self._JKS = None
        self._OTHER = None
        self._ROOT = None

    @property
    def NGINX(self):
        """是否可以下载nginx可用格式
        :rtype: bool
        """
        return self._NGINX

    @NGINX.setter
    def NGINX(self, NGINX):
        self._NGINX = NGINX

    @property
    def APACHE(self):
        """是否可以下载apache可用格式
        :rtype: bool
        """
        return self._APACHE

    @APACHE.setter
    def APACHE(self, APACHE):
        self._APACHE = APACHE

    @property
    def TOMCAT(self):
        """是否可以下载tomcat可用格式
        :rtype: bool
        """
        return self._TOMCAT

    @TOMCAT.setter
    def TOMCAT(self, TOMCAT):
        self._TOMCAT = TOMCAT

    @property
    def IIS(self):
        """是否可以下载iis可用格式
        :rtype: bool
        """
        return self._IIS

    @IIS.setter
    def IIS(self, IIS):
        self._IIS = IIS

    @property
    def JKS(self):
        """是否可以下载JKS可用格式
        :rtype: bool
        """
        return self._JKS

    @JKS.setter
    def JKS(self, JKS):
        self._JKS = JKS

    @property
    def OTHER(self):
        """是否可以下载其他格式
        :rtype: bool
        """
        return self._OTHER

    @OTHER.setter
    def OTHER(self, OTHER):
        self._OTHER = OTHER

    @property
    def ROOT(self):
        """是否可以下载根证书
        :rtype: bool
        """
        return self._ROOT

    @ROOT.setter
    def ROOT(self, ROOT):
        self._ROOT = ROOT


    def _deserialize(self, params):
        self._NGINX = params.get("NGINX")
        self._APACHE = params.get("APACHE")
        self._TOMCAT = params.get("TOMCAT")
        self._IIS = params.get("IIS")
        self._JKS = params.get("JKS")
        self._OTHER = params.get("OTHER")
        self._ROOT = params.get("ROOT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncTaskBindResourceResult(AbstractModel):
    """异步任务证书关联云资源结果

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _BindResourceResult: 关联云资源结果
        :type BindResourceResult: list of BindResourceResult
        :param _Status: 关联云资源异步查询结果： 0表示查询中， 1表示查询成功。 2表示查询异常； 若状态为1，则查看BindResourceResult结果；若状态为2，则查看Error原因
        :type Status: int
        :param _Error: 关联云资源错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: :class:`tencentcloud.ssl.v20191205.models.Error`
        :param _CacheTime: 当前结果缓存时间
        :type CacheTime: str
        """
        self._TaskId = None
        self._BindResourceResult = None
        self._Status = None
        self._Error = None
        self._CacheTime = None

    @property
    def TaskId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def BindResourceResult(self):
        """关联云资源结果
        :rtype: list of BindResourceResult
        """
        return self._BindResourceResult

    @BindResourceResult.setter
    def BindResourceResult(self, BindResourceResult):
        self._BindResourceResult = BindResourceResult

    @property
    def Status(self):
        """关联云资源异步查询结果： 0表示查询中， 1表示查询成功。 2表示查询异常； 若状态为1，则查看BindResourceResult结果；若状态为2，则查看Error原因
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Error(self):
        """关联云资源错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.Error`
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error

    @property
    def CacheTime(self):
        """当前结果缓存时间
        :rtype: str
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        if params.get("BindResourceResult") is not None:
            self._BindResourceResult = []
            for item in params.get("BindResourceResult"):
                obj = BindResourceResult()
                obj._deserialize(item)
                self._BindResourceResult.append(obj)
        self._Status = params.get("Status")
        if params.get("Error") is not None:
            self._Error = Error()
            self._Error._deserialize(params.get("Error"))
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBAccessInstance(AbstractModel):
    """TCB访问服务实例

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Status: 状态
        :type Status: int
        :param _UnionStatus: 统一域名状态

        :type UnionStatus: int
        :param _IsPreempted: 是否被抢占, 被抢占表示域名被其他环境绑定了，需要解绑或者重新绑定。

        :type IsPreempted: bool
        :param _ICPStatus: icp黑名单封禁状态，0-未封禁，1-封禁

        :type ICPStatus: int
        :param _OldCertificateId: 已绑定证书ID
        :type OldCertificateId: str
        """
        self._Domain = None
        self._Status = None
        self._UnionStatus = None
        self._IsPreempted = None
        self._ICPStatus = None
        self._OldCertificateId = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        """状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UnionStatus(self):
        """统一域名状态

        :rtype: int
        """
        return self._UnionStatus

    @UnionStatus.setter
    def UnionStatus(self, UnionStatus):
        self._UnionStatus = UnionStatus

    @property
    def IsPreempted(self):
        """是否被抢占, 被抢占表示域名被其他环境绑定了，需要解绑或者重新绑定。

        :rtype: bool
        """
        return self._IsPreempted

    @IsPreempted.setter
    def IsPreempted(self, IsPreempted):
        self._IsPreempted = IsPreempted

    @property
    def ICPStatus(self):
        """icp黑名单封禁状态，0-未封禁，1-封禁

        :rtype: int
        """
        return self._ICPStatus

    @ICPStatus.setter
    def ICPStatus(self, ICPStatus):
        self._ICPStatus = ICPStatus

    @property
    def OldCertificateId(self):
        """已绑定证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._UnionStatus = params.get("UnionStatus")
        self._IsPreempted = params.get("IsPreempted")
        self._ICPStatus = params.get("ICPStatus")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBAccessService(AbstractModel):
    """TCB访问服务列表

    """

    def __init__(self):
        r"""
        :param _InstanceList: 实例列表
        :type InstanceList: list of TCBAccessInstance
        :param _TotalCount: 数量
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        """实例列表
        :rtype: list of TCBAccessInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TCBAccessInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBEnvironment(AbstractModel):
    """TCB环境

    """

    def __init__(self):
        r"""
        :param _ID: 唯一ID
        :type ID: str
        :param _Source: 来源
        :type Source: str
        :param _Name: 名称
        :type Name: str
        :param _Status: 状态
        :type Status: str
        """
        self._ID = None
        self._Source = None
        self._Name = None
        self._Status = None

    @property
    def ID(self):
        """唯一ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Source(self):
        """来源
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        """状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Source = params.get("Source")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBEnvironments(AbstractModel):
    """tcb环境实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _Environment: tcb环境	
注意：此字段可能返回 null，表示取不到有效值。
        :type Environment: :class:`tencentcloud.ssl.v20191205.models.TCBEnvironment`
        :param _AccessService: 访问服务	
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessService: :class:`tencentcloud.ssl.v20191205.models.TCBAccessService`
        :param _HostService: 静态托管	
注意：此字段可能返回 null，表示取不到有效值。
        :type HostService: :class:`tencentcloud.ssl.v20191205.models.TCBHostService`
        """
        self._Environment = None
        self._AccessService = None
        self._HostService = None

    @property
    def Environment(self):
        """tcb环境	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.TCBEnvironment`
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def AccessService(self):
        """访问服务	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.TCBAccessService`
        """
        return self._AccessService

    @AccessService.setter
    def AccessService(self, AccessService):
        self._AccessService = AccessService

    @property
    def HostService(self):
        """静态托管	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ssl.v20191205.models.TCBHostService`
        """
        return self._HostService

    @HostService.setter
    def HostService(self, HostService):
        self._HostService = HostService


    def _deserialize(self, params):
        if params.get("Environment") is not None:
            self._Environment = TCBEnvironment()
            self._Environment._deserialize(params.get("Environment"))
        if params.get("AccessService") is not None:
            self._AccessService = TCBAccessService()
            self._AccessService._deserialize(params.get("AccessService"))
        if params.get("HostService") is not None:
            self._HostService = TCBHostService()
            self._HostService._deserialize(params.get("HostService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBHostInstance(AbstractModel):
    """TCB静态托管服务实例

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Status: 状态
        :type Status: str
        :param _DNSStatus: 解析状态
        :type DNSStatus: str
        :param _OldCertificateId: 已绑定证书ID
        :type OldCertificateId: str
        """
        self._Domain = None
        self._Status = None
        self._DNSStatus = None
        self._OldCertificateId = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        """状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DNSStatus(self):
        """解析状态
        :rtype: str
        """
        return self._DNSStatus

    @DNSStatus.setter
    def DNSStatus(self, DNSStatus):
        self._DNSStatus = DNSStatus

    @property
    def OldCertificateId(self):
        """已绑定证书ID
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._DNSStatus = params.get("DNSStatus")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBHostService(AbstractModel):
    """TCB静态托管服务列表

    """

    def __init__(self):
        r"""
        :param _InstanceList: 实例列表
        :type InstanceList: list of TCBHostInstance
        :param _TotalCount: 数量
        :type TotalCount: int
        """
        self._InstanceList = None
        self._TotalCount = None

    @property
    def InstanceList(self):
        """实例列表
        :rtype: list of TCBHostInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TCBHostInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCBInstanceList(AbstractModel):
    """tcb地域实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _Environments: tcb环境实例详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Environments: list of TCBEnvironments
        :param _Error: 是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self._Region = None
        self._Environments = None
        self._Error = None

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Environments(self):
        """tcb环境实例详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TCBEnvironments
        """
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

    @property
    def Error(self):
        """是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("Environments") is not None:
            self._Environments = []
            for item in params.get("Environments"):
                obj = TCBEnvironments()
                obj._deserialize(item)
                self._Environments.append(obj)
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TSEInstanceDetail(AbstractModel):
    """tse实例详情

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _GatewayName: 网关名称
        :type GatewayName: str
        :param _CertificateList: 网关证书列表
        :type CertificateList: list of GatewayCertificate
        """
        self._GatewayId = None
        self._GatewayName = None
        self._CertificateList = None

    @property
    def GatewayId(self):
        """网关ID
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayName(self):
        """网关名称
        :rtype: str
        """
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def CertificateList(self):
        """网关证书列表
        :rtype: list of GatewayCertificate
        """
        return self._CertificateList

    @CertificateList.setter
    def CertificateList(self, CertificateList):
        self._CertificateList = CertificateList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GatewayName = params.get("GatewayName")
        if params.get("CertificateList") is not None:
            self._CertificateList = []
            for item in params.get("CertificateList"):
                obj = GatewayCertificate()
                obj._deserialize(item)
                self._CertificateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TSEInstanceList(AbstractModel):
    """TSE实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _InstanceList: TSE实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of TSEInstanceDetail
        :param _TotalCount: 该地域下TSE实例总数	
        :type TotalCount: int
        :param _Region: 地域	
        :type Region: str
        :param _Error: 是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._Region = None
        self._Error = None

    @property
    def InstanceList(self):
        """TSE实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TSEInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """该地域下TSE实例总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Region(self):
        """地域	
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Error(self):
        """是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TSEInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Region = params.get("Region")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeoInstanceDetail(AbstractModel):
    """teo实例详情

    """

    def __init__(self):
        r"""
        :param _Host: 域名
        :type Host: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _ZoneId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _Status: 域名状态
deployed：已部署；
processing：部署中；
applying：申请中；
failed：申请失败；
issued：绑定失败。
        :type Status: str
        """
        self._Host = None
        self._CertId = None
        self._ZoneId = None
        self._Status = None

    @property
    def Host(self):
        """域名
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def ZoneId(self):
        """区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        """域名状态
deployed：已部署；
processing：部署中；
applying：申请中；
failed：申请失败；
issued：绑定失败。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._CertId = params.get("CertId")
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeoInstanceList(AbstractModel):
    """edgeone实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _InstanceList: edgeone实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of TeoInstanceDetail
        :param _TotalCount: edgeone实例总数	
        :type TotalCount: int
        :param _Error: 是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def InstanceList(self):
        """edgeone实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TeoInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """edgeone实例总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TeoInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeIngressDetail(AbstractModel):
    """tke ingress实例详情

    """

    def __init__(self):
        r"""
        :param _IngressName: ingress名称
        :type IngressName: str
        :param _TlsDomains: tls域名列表
        :type TlsDomains: list of str
        :param _Domains: ingress域名列表
        :type Domains: list of str
        """
        self._IngressName = None
        self._TlsDomains = None
        self._Domains = None

    @property
    def IngressName(self):
        """ingress名称
        :rtype: str
        """
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def TlsDomains(self):
        """tls域名列表
        :rtype: list of str
        """
        return self._TlsDomains

    @TlsDomains.setter
    def TlsDomains(self, TlsDomains):
        self._TlsDomains = TlsDomains

    @property
    def Domains(self):
        """ingress域名列表
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._IngressName = params.get("IngressName")
        self._TlsDomains = params.get("TlsDomains")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeInstanceDetail(AbstractModel):
    """tke实例详情

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _NamespaceList: 集群命名空间列表
        :type NamespaceList: list of TkeNameSpaceDetail
        :param _ClusterType: 集群类型
        :type ClusterType: str
        :param _ClusterVersion: 集群版本
        :type ClusterVersion: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._NamespaceList = None
        self._ClusterType = None
        self._ClusterVersion = None

    @property
    def ClusterId(self):
        """集群ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        """集群名称
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def NamespaceList(self):
        """集群命名空间列表
        :rtype: list of TkeNameSpaceDetail
        """
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList

    @property
    def ClusterType(self):
        """集群类型
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterVersion(self):
        """集群版本
        :rtype: str
        """
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TkeNameSpaceDetail()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        self._ClusterType = params.get("ClusterType")
        self._ClusterVersion = params.get("ClusterVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeInstanceList(AbstractModel):
    """tke实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _InstanceList: tke实例详情
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of TkeInstanceDetail
        :param _TotalCount: 该地域下tke实例总数	
        :type TotalCount: int
        :param _Error: 是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """tke实例详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TkeInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """该地域下tke实例总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TkeInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeNameSpaceDetail(AbstractModel):
    """tke namespace详情

    """

    def __init__(self):
        r"""
        :param _Name: namespace名称
        :type Name: str
        :param _SecretList: secret列表
        :type SecretList: list of TkeSecretDetail
        """
        self._Name = None
        self._SecretList = None

    @property
    def Name(self):
        """namespace名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SecretList(self):
        """secret列表
        :rtype: list of TkeSecretDetail
        """
        return self._SecretList

    @SecretList.setter
    def SecretList(self, SecretList):
        self._SecretList = SecretList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("SecretList") is not None:
            self._SecretList = []
            for item in params.get("SecretList"):
                obj = TkeSecretDetail()
                obj._deserialize(item)
                self._SecretList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeSecretDetail(AbstractModel):
    """tke secret详情

    """

    def __init__(self):
        r"""
        :param _Name: secret名称
        :type Name: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _IngressList: ingress列表
        :type IngressList: list of TkeIngressDetail
        :param _NoMatchDomains: 和新证书不匹配的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoMatchDomains: list of str
        """
        self._Name = None
        self._CertId = None
        self._IngressList = None
        self._NoMatchDomains = None

    @property
    def Name(self):
        """secret名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def IngressList(self):
        """ingress列表
        :rtype: list of TkeIngressDetail
        """
        return self._IngressList

    @IngressList.setter
    def IngressList(self, IngressList):
        self._IngressList = IngressList

    @property
    def NoMatchDomains(self):
        """和新证书不匹配的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CertId = params.get("CertId")
        if params.get("IngressList") is not None:
            self._IngressList = []
            for item in params.get("IngressList"):
                obj = TkeIngressDetail()
                obj._deserialize(item)
                self._IngressList.append(obj)
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceRequest(AbstractModel):
    """UpdateCertificateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OldCertificateId: 一键更新的旧证书ID。 通过查询该证书ID绑定的云资源，然后使用新证书对这些云资源进行更新
        :type OldCertificateId: str
        :param _ResourceTypes: 需要部署的资源类型，参数值可选（小写）：clb、cdn、waf、live、ddos、teo、apigateway、vod、tke、tcb、tse、cos
        :type ResourceTypes: list of str
        :param _CertificateId: 一键更新的新证书ID。 不传该参数，则公钥证书和私钥证书必传
        :type CertificateId: str
        :param _Regions: 需要部署的地域列表（废弃）
        :type Regions: list of str
        :param _ResourceTypesRegions: 云资源需要部署的地域列表，支持地域的云资源类型必传，取值：clb、tke、apigateway、waf、tcb、tse、cos
        :type ResourceTypesRegions: list of ResourceTypeRegions
        :param _CertificatePublicKey: 公钥证书， 若上传公钥证书，那么私钥证书必传。  则CertificateId不用传
        :type CertificatePublicKey: str
        :param _CertificatePrivateKey: 私钥证书，若上传私钥证书， 那么公钥证书必传；  则CertificateId不用传
        :type CertificatePrivateKey: str
        :param _ExpiringNotificationSwitch: 旧证书是否忽略到期提醒  0:不忽略通知。1:忽略通知，忽略OldCertificateId到期提醒
        :type ExpiringNotificationSwitch: int
        :param _Repeatable: 相同的证书是否允许重复上传，若选择上传公钥私钥证书， 则可以配置该参数。 若存在相同重复证书，则更新任务会失败
        :type Repeatable: bool
        :param _AllowDownload: 是否允许下载，若选择上传公私钥证书， 则可以配置该参数
        :type AllowDownload: bool
        :param _Tags: 标签列表，若选择上传公私钥证书， 则可以配置该参数
        :type Tags: list of Tags
        :param _ProjectId: 项目 ID，若选择上传公私钥证书， 则可以配置该参数
        :type ProjectId: int
        """
        self._OldCertificateId = None
        self._ResourceTypes = None
        self._CertificateId = None
        self._Regions = None
        self._ResourceTypesRegions = None
        self._CertificatePublicKey = None
        self._CertificatePrivateKey = None
        self._ExpiringNotificationSwitch = None
        self._Repeatable = None
        self._AllowDownload = None
        self._Tags = None
        self._ProjectId = None

    @property
    def OldCertificateId(self):
        """一键更新的旧证书ID。 通过查询该证书ID绑定的云资源，然后使用新证书对这些云资源进行更新
        :rtype: str
        """
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def ResourceTypes(self):
        """需要部署的资源类型，参数值可选（小写）：clb、cdn、waf、live、ddos、teo、apigateway、vod、tke、tcb、tse、cos
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def CertificateId(self):
        """一键更新的新证书ID。 不传该参数，则公钥证书和私钥证书必传
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Regions(self):
        warnings.warn("parameter `Regions` is deprecated", DeprecationWarning) 

        """需要部署的地域列表（废弃）
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        warnings.warn("parameter `Regions` is deprecated", DeprecationWarning) 

        self._Regions = Regions

    @property
    def ResourceTypesRegions(self):
        """云资源需要部署的地域列表，支持地域的云资源类型必传，取值：clb、tke、apigateway、waf、tcb、tse、cos
        :rtype: list of ResourceTypeRegions
        """
        return self._ResourceTypesRegions

    @ResourceTypesRegions.setter
    def ResourceTypesRegions(self, ResourceTypesRegions):
        self._ResourceTypesRegions = ResourceTypesRegions

    @property
    def CertificatePublicKey(self):
        """公钥证书， 若上传公钥证书，那么私钥证书必传。  则CertificateId不用传
        :rtype: str
        """
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        """私钥证书，若上传私钥证书， 那么公钥证书必传；  则CertificateId不用传
        :rtype: str
        """
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def ExpiringNotificationSwitch(self):
        """旧证书是否忽略到期提醒  0:不忽略通知。1:忽略通知，忽略OldCertificateId到期提醒
        :rtype: int
        """
        return self._ExpiringNotificationSwitch

    @ExpiringNotificationSwitch.setter
    def ExpiringNotificationSwitch(self, ExpiringNotificationSwitch):
        self._ExpiringNotificationSwitch = ExpiringNotificationSwitch

    @property
    def Repeatable(self):
        """相同的证书是否允许重复上传，若选择上传公钥私钥证书， 则可以配置该参数。 若存在相同重复证书，则更新任务会失败
        :rtype: bool
        """
        return self._Repeatable

    @Repeatable.setter
    def Repeatable(self, Repeatable):
        self._Repeatable = Repeatable

    @property
    def AllowDownload(self):
        """是否允许下载，若选择上传公私钥证书， 则可以配置该参数
        :rtype: bool
        """
        return self._AllowDownload

    @AllowDownload.setter
    def AllowDownload(self, AllowDownload):
        self._AllowDownload = AllowDownload

    @property
    def Tags(self):
        """标签列表，若选择上传公私钥证书， 则可以配置该参数
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ProjectId(self):
        """项目 ID，若选择上传公私钥证书， 则可以配置该参数
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._OldCertificateId = params.get("OldCertificateId")
        self._ResourceTypes = params.get("ResourceTypes")
        self._CertificateId = params.get("CertificateId")
        self._Regions = params.get("Regions")
        if params.get("ResourceTypesRegions") is not None:
            self._ResourceTypesRegions = []
            for item in params.get("ResourceTypesRegions"):
                obj = ResourceTypeRegions()
                obj._deserialize(item)
                self._ResourceTypesRegions.append(obj)
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._ExpiringNotificationSwitch = params.get("ExpiringNotificationSwitch")
        self._Repeatable = params.get("Repeatable")
        self._AllowDownload = params.get("AllowDownload")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceResponse(AbstractModel):
    """UpdateCertificateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 云资源更新任务ID， DeployRecordId为0表示任务进行中， 重复请求这个接口， 当返回DeployRecordId大于0则表示任务创建成功。 未创建成功则会抛出异常
        :type DeployRecordId: int
        :param _DeployStatus: 更新任务创建状态；1表示创建成功； 0表示当前存在更新中的任务，未创建新的更新任务；返回值DeployRecordId为更新中的任务ID
        :type DeployStatus: int
        :param _UpdateSyncProgress: 更新异步创建任务进度详情
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateSyncProgress: list of UpdateSyncProgress
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._DeployStatus = None
        self._UpdateSyncProgress = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        """云资源更新任务ID， DeployRecordId为0表示任务进行中， 重复请求这个接口， 当返回DeployRecordId大于0则表示任务创建成功。 未创建成功则会抛出异常
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployStatus(self):
        """更新任务创建状态；1表示创建成功； 0表示当前存在更新中的任务，未创建新的更新任务；返回值DeployRecordId为更新中的任务ID
        :rtype: int
        """
        return self._DeployStatus

    @DeployStatus.setter
    def DeployStatus(self, DeployStatus):
        self._DeployStatus = DeployStatus

    @property
    def UpdateSyncProgress(self):
        """更新异步创建任务进度详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UpdateSyncProgress
        """
        return self._UpdateSyncProgress

    @UpdateSyncProgress.setter
    def UpdateSyncProgress(self, UpdateSyncProgress):
        self._UpdateSyncProgress = UpdateSyncProgress

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployStatus = params.get("DeployStatus")
        if params.get("UpdateSyncProgress") is not None:
            self._UpdateSyncProgress = []
            for item in params.get("UpdateSyncProgress"):
                obj = UpdateSyncProgress()
                obj._deserialize(item)
                self._UpdateSyncProgress.append(obj)
        self._RequestId = params.get("RequestId")


class UpdateCertificateRecordRetryRequest(AbstractModel):
    """UpdateCertificateRecordRetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待重试部署记录ID,通过UpdateCertificateInstance得到部署记录ID。 本参数不传的话，则DeployRecordDetailId必传
        :type DeployRecordId: int
        :param _DeployRecordDetailId: 待重试部署记录详情ID,通过DescribeHostUpdateRecordDetail接口获得， 本参数不传的话， 则DeployRecordId必传
        :type DeployRecordDetailId: int
        """
        self._DeployRecordId = None
        self._DeployRecordDetailId = None

    @property
    def DeployRecordId(self):
        """待重试部署记录ID,通过UpdateCertificateInstance得到部署记录ID。 本参数不传的话，则DeployRecordDetailId必传
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployRecordDetailId(self):
        """待重试部署记录详情ID,通过DescribeHostUpdateRecordDetail接口获得， 本参数不传的话， 则DeployRecordId必传
        :rtype: int
        """
        return self._DeployRecordDetailId

    @DeployRecordDetailId.setter
    def DeployRecordDetailId(self, DeployRecordDetailId):
        self._DeployRecordDetailId = DeployRecordDetailId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployRecordDetailId = params.get("DeployRecordDetailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRetryResponse(AbstractModel):
    """UpdateCertificateRecordRetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateCertificateRecordRollbackRequest(AbstractModel):
    """UpdateCertificateRecordRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 更新证书待回滚的记录ID, 通过UpdateCertificateInstance获得
        :type DeployRecordId: int
        """
        self._DeployRecordId = None

    @property
    def DeployRecordId(self):
        """更新证书待回滚的记录ID, 通过UpdateCertificateInstance获得
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRollbackResponse(AbstractModel):
    """UpdateCertificateRecordRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 新生成的回滚部署任务的记录ID
        :type DeployRecordId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        """新生成的回滚部署任务的记录ID
        :rtype: int
        """
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._RequestId = params.get("RequestId")


class UpdateRecordDetail(AbstractModel):
    """更新记录详情

    """

    def __init__(self):
        r"""
        :param _Id: 更新详情记录id
        :type Id: int
        :param _CertId: 新旧证书更新 - 新证书ID
        :type CertId: str
        :param _OldCertId: 新旧证书更新 - 旧证书ID
        :type OldCertId: str
        :param _Domains: 部署域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of str
        :param _ResourceType: 新旧证书更新云资源的云资源类型：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- tse
- tcb
        :type ResourceType: str
        :param _Region: 部署地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Status: 部署状态， 取值范围：
0：待部署
1：部署成功
2：部署失败
3：部署中
4：回滚成功
5：回滚失败
6：无资源，无需部署
        :type Status: int
        :param _ErrorMsg: 部署错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _CreateTime: 部署时间
        :type CreateTime: str
        :param _UpdateTime: 最后一次更新时间
        :type UpdateTime: str
        :param _InstanceId: 部署实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 部署实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _ListenerId: 部署监听器ID（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _ListenerName: 部署监听器名称（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _SniSwitch: 是否开启SNI（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type SniSwitch: int
        :param _Bucket: bucket名称（COS专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Namespace: 命名空间（TKE专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _SecretName: secret名称（TKE专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _TCBType: TCB部署类型
        :type TCBType: str
        :param _Url: 监听器Url(clb专属)
        :type Url: str
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._Domains = None
        self._ResourceType = None
        self._Region = None
        self._Status = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None
        self._InstanceId = None
        self._InstanceName = None
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._SniSwitch = None
        self._Bucket = None
        self._Port = None
        self._Namespace = None
        self._SecretName = None
        self._EnvId = None
        self._TCBType = None
        self._Url = None

    @property
    def Id(self):
        """更新详情记录id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        """新旧证书更新 - 新证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        """新旧证书更新 - 旧证书ID
        :rtype: str
        """
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def Domains(self):
        """部署域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ResourceType(self):
        """新旧证书更新云资源的云资源类型：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- tse
- tcb
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Region(self):
        """部署地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        """部署状态， 取值范围：
0：待部署
1：部署成功
2：部署失败
3：部署中
4：回滚成功
5：回滚失败
6：无资源，无需部署
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        """部署错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        """部署时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后一次更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InstanceId(self):
        """部署实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """部署实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ListenerId(self):
        """部署监听器ID（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """部署监听器名称（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        """协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SniSwitch(self):
        """是否开启SNI（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Bucket(self):
        """bucket名称（COS专用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Port(self):
        """端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Namespace(self):
        """命名空间（TKE专用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def SecretName(self):
        """secret名称（TKE专用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def EnvId(self):
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def TCBType(self):
        """TCB部署类型
        :rtype: str
        """
        return self._TCBType

    @TCBType.setter
    def TCBType(self, TCBType):
        self._TCBType = TCBType

    @property
    def Url(self):
        """监听器Url(clb专属)
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._Domains = params.get("Domains")
        self._ResourceType = params.get("ResourceType")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._SniSwitch = params.get("SniSwitch")
        self._Bucket = params.get("Bucket")
        self._Port = params.get("Port")
        self._Namespace = params.get("Namespace")
        self._SecretName = params.get("SecretName")
        self._EnvId = params.get("EnvId")
        self._TCBType = params.get("TCBType")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordDetails(AbstractModel):
    """更新记录详情

    """

    def __init__(self):
        r"""
        :param _ResourceType: 新旧证书更新云资源的云资源类型：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- tse
- tcb
        :type ResourceType: str
        :param _List: 该云资源更新详情
        :type List: list of UpdateRecordDetail
        :param _TotalCount: 该云资源更新资源总数
        :type TotalCount: int
        """
        self._ResourceType = None
        self._List = None
        self._TotalCount = None

    @property
    def ResourceType(self):
        """新旧证书更新云资源的云资源类型：
- clb
- cdn
- ddos
- live
- vod
- waf
- apigateway
- teo
- tke
- cos
- tse
- tcb
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def List(self):
        """该云资源更新详情
        :rtype: list of UpdateRecordDetail
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        """该云资源更新资源总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UpdateRecordDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordInfo(AbstractModel):
    """部署记录信息

    """

    def __init__(self):
        r"""
        :param _Id: 记录ID
        :type Id: int
        :param _CertId: 新证书ID
        :type CertId: str
        :param _OldCertId: 原证书ID
        :type OldCertId: str
        :param _ResourceTypes: 部署资源类型列表
        :type ResourceTypes: list of str
        :param _Regions: 部署地域列表
        :type Regions: list of str
        :param _Status: 部署状态
        :type Status: int
        :param _CreateTime: 部署时间
        :type CreateTime: str
        :param _UpdateTime: 最后一次更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._ResourceTypes = None
        self._Regions = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        """记录ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        """新证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        """原证书ID
        :rtype: str
        """
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def ResourceTypes(self):
        """部署资源类型列表
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        """部署地域列表
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Status(self):
        """部署状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """部署时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """最后一次更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._ResourceTypes = params.get("ResourceTypes")
        self._Regions = params.get("Regions")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSyncProgress(AbstractModel):
    """更新异步任务进度

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _UpdateSyncProgressRegions: 地域结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateSyncProgressRegions: list of UpdateSyncProgressRegion
        :param _Status: 异步更新进度状态：0， 待处理， 1 已处理， 3 处理中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._ResourceType = None
        self._UpdateSyncProgressRegions = None
        self._Status = None

    @property
    def ResourceType(self):
        """资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def UpdateSyncProgressRegions(self):
        """地域结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UpdateSyncProgressRegion
        """
        return self._UpdateSyncProgressRegions

    @UpdateSyncProgressRegions.setter
    def UpdateSyncProgressRegions(self, UpdateSyncProgressRegions):
        self._UpdateSyncProgressRegions = UpdateSyncProgressRegions

    @property
    def Status(self):
        """异步更新进度状态：0， 待处理， 1 已处理， 3 处理中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("UpdateSyncProgressRegions") is not None:
            self._UpdateSyncProgressRegions = []
            for item in params.get("UpdateSyncProgressRegions"):
                obj = UpdateSyncProgressRegion()
                obj._deserialize(item)
                self._UpdateSyncProgressRegions.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSyncProgressRegion(AbstractModel):
    """更新异步任务进度

    """

    def __init__(self):
        r"""
        :param _Region: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _OffsetCount: 执行完成数量
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetCount: int
        :param _Status: 异步更新进度状态：0， 待处理， 1 已处理， 3 处理中
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._Region = None
        self._TotalCount = None
        self._OffsetCount = None
        self._Status = None

    @property
    def Region(self):
        """资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TotalCount(self):
        """总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OffsetCount(self):
        """执行完成数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OffsetCount

    @OffsetCount.setter
    def OffsetCount(self, OffsetCount):
        self._OffsetCount = OffsetCount

    @property
    def Status(self):
        """异步更新进度状态：0， 待处理， 1 已处理， 3 处理中
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._TotalCount = params.get("TotalCount")
        self._OffsetCount = params.get("OffsetCount")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificatePublicKey: 证书内容。
        :type CertificatePublicKey: str
        :param _CertificatePrivateKey: 私钥内容，证书类型为 SVR 时必填，为 CA 时可不填。
        :type CertificatePrivateKey: str
        :param _CertificateType: 证书类型，默认 SVR。CA = CA证书，SVR = 服务器证书。
        :type CertificateType: str
        :param _Alias: 备注名称。
        :type Alias: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _CertificateUse: 证书用途/证书来源。“CLB，CDN，WAF，LIVE，DDOS”
        :type CertificateUse: str
        :param _Tags: 标签列表
        :type Tags: list of Tags
        :param _Repeatable: 相同的证书是否允许重复上传； true：允许上传相同指纹的证书；  false：不允许上传相同指纹的证书； 默认值：true
        :type Repeatable: bool
        """
        self._CertificatePublicKey = None
        self._CertificatePrivateKey = None
        self._CertificateType = None
        self._Alias = None
        self._ProjectId = None
        self._CertificateUse = None
        self._Tags = None
        self._Repeatable = None

    @property
    def CertificatePublicKey(self):
        """证书内容。
        :rtype: str
        """
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        """私钥内容，证书类型为 SVR 时必填，为 CA 时可不填。
        :rtype: str
        """
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificateType(self):
        """证书类型，默认 SVR。CA = CA证书，SVR = 服务器证书。
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def Alias(self):
        """备注名称。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def ProjectId(self):
        """项目 ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CertificateUse(self):
        """证书用途/证书来源。“CLB，CDN，WAF，LIVE，DDOS”
        :rtype: str
        """
        return self._CertificateUse

    @CertificateUse.setter
    def CertificateUse(self, CertificateUse):
        self._CertificateUse = CertificateUse

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Repeatable(self):
        """相同的证书是否允许重复上传； true：允许上传相同指纹的证书；  false：不允许上传相同指纹的证书； 默认值：true
        :rtype: bool
        """
        return self._Repeatable

    @Repeatable.setter
    def Repeatable(self, Repeatable):
        self._Repeatable = Repeatable


    def _deserialize(self, params):
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._CertificateType = params.get("CertificateType")
        self._Alias = params.get("Alias")
        self._ProjectId = params.get("ProjectId")
        self._CertificateUse = params.get("CertificateUse")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Repeatable = params.get("Repeatable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateResponse(AbstractModel):
    """UploadCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RepeatCertId: 重复证书的ID
        :type RepeatCertId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RepeatCertId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RepeatCertId(self):
        """重复证书的ID
        :rtype: str
        """
        return self._RepeatCertId

    @RepeatCertId.setter
    def RepeatCertId(self, RepeatCertId):
        self._RepeatCertId = RepeatCertId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RepeatCertId = params.get("RepeatCertId")
        self._RequestId = params.get("RequestId")


class UploadConfirmLetterRequest(AbstractModel):
    """UploadConfirmLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _ConfirmLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :type ConfirmLetter: str
        """
        self._CertificateId = None
        self._ConfirmLetter = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ConfirmLetter(self):
        """base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :rtype: str
        """
        return self._ConfirmLetter

    @ConfirmLetter.setter
    def ConfirmLetter(self, ConfirmLetter):
        self._ConfirmLetter = ConfirmLetter


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ConfirmLetter = params.get("ConfirmLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadConfirmLetterResponse(AbstractModel):
    """UploadConfirmLetter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _IsSuccess: 是否成功
        :type IsSuccess: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsSuccess(self):
        """是否成功
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class UploadRevokeLetterRequest(AbstractModel):
    """UploadRevokeLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RevokeLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :type RevokeLetter: str
        """
        self._CertificateId = None
        self._RevokeLetter = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RevokeLetter(self):
        """base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :rtype: str
        """
        return self._RevokeLetter

    @RevokeLetter.setter
    def RevokeLetter(self, RevokeLetter):
        self._RevokeLetter = RevokeLetter


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RevokeLetter = params.get("RevokeLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadRevokeLetterResponse(AbstractModel):
    """UploadRevokeLetter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _IsSuccess: 是否成功。
        :type IsSuccess: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsSuccess(self):
        """是否成功。
        :rtype: bool
        """
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class VODInstanceList(AbstractModel):
    """vod实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _InstanceList: vod实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of VodInstanceDetail
        :param _TotalCount: 该地域下vod实例总数	
        :type TotalCount: int
        :param _Error: 是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def InstanceList(self):
        """vod实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of VodInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """该地域下vod实例总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = VodInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyManagerRequest(AbstractModel):
    """VerifyManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        """
        self._ManagerId = None

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyManagerResponse(AbstractModel):
    """VerifyManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ManagerId = None
        self._RequestId = None

    @property
    def ManagerId(self):
        """管理人ID
        :rtype: int
        """
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._RequestId = params.get("RequestId")


class VodInstanceDetail(AbstractModel):
    """Vod实例

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 证书ID
        :type CertId: str
        """
        self._Domain = None
        self._CertId = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafInstanceDetail(AbstractModel):
    """waf实例详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _Keepalive: 是否保持长连接，1是，0 否
注意：此字段可能返回 null，表示取不到有效值。
        :type Keepalive: int
        """
        self._Domain = None
        self._CertId = None
        self._Keepalive = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        """证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Keepalive(self):
        """是否保持长连接，1是，0 否
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Keepalive

    @Keepalive.setter
    def Keepalive(self, Keepalive):
        self._Keepalive = Keepalive


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Keepalive = params.get("Keepalive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafInstanceList(AbstractModel):
    """waf实例详情 - 异步关联云资源数据结构

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _InstanceList: waf实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of WafInstanceDetail
        :param _TotalCount: 该地域下waf实例总数	
        :type TotalCount: int
        :param _Error: 是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Error: str
        """
        self._Region = None
        self._InstanceList = None
        self._TotalCount = None
        self._Error = None

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def InstanceList(self):
        """waf实例详情	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WafInstanceDetail
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        """该地域下waf实例总数	
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Error(self):
        """是否查询异常
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Error

    @Error.setter
    def Error(self, Error):
        self._Error = Error


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = WafInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        