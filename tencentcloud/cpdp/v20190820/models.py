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


class Acct(AbstractModel):
    """账户信息

    """

    def __init__(self):
        r"""
        :param SubAcctNo: STRING(50)，见证子账户的账号（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctProperty: STRING(10)，见证子账户的属性（可重复。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctProperty: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctName: STRING(150)，见证子账户的名称（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param AcctAvailBal: STRING(20)，见证子账户可用余额（可重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctAvailBal: str
        :param CashAmt: STRING(20)，见证子账户可提现金额（可重复。开户日期或修改日期）
注意：此字段可能返回 null，表示取不到有效值。
        :type CashAmt: str
        :param MaintenanceDate: STRING(8)，维护日期
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintenanceDate: str
        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.TranNetMemberCode = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddContractRequest(AbstractModel):
    """AddContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param OutContractId: 机构合同主键（系统有唯一性校验），建议使用合同表的主键ID，防止重复添加合同
        :type OutContractId: str
        :param Code: 合同编号（系统有唯一性校验）
        :type Code: str
        :param PaymentId: 支付方式编号
        :type PaymentId: str
        :param PaymentClassificationId: 支付方式行业分类编号
        :type PaymentClassificationId: str
        :param PaymentClassificationLimit: 封顶值（分为单位，无封顶填0）
        :type PaymentClassificationLimit: str
        :param MerchantNo: 商户编号
        :type MerchantNo: str
        :param Fee: 签约扣率百分比（如：0.32）
        :type Fee: str
        :param StartDate: 合同生效日期（yyyy-mm-dd）
        :type StartDate: str
        :param EndDate: 合同过期日期（yyyy-mm-dd）
        :type EndDate: str
        :param SignMan: 合同签约人
        :type SignMan: str
        :param SignName: 签购单名称，建议使用商户招牌名称
        :type SignName: str
        :param SignDate: 合同签署日期（yyyy-mm-dd）
        :type SignDate: str
        :param AutoSign: 是否自动续签（1是，0否）
        :type AutoSign: str
        :param Contact: 联系人
        :type Contact: str
        :param ContactTelephone: 联系人电话
        :type ContactTelephone: str
        :param PictureOne: 合同照片【私密区】
        :type PictureOne: str
        :param PictureTwo: 合同照片【私密区】
        :type PictureTwo: str
        :param ChannelExtJson: 渠道扩展字段，json格式
        :type ChannelExtJson: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        :param PaymentOptionOne: 合同选项1（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionOne: str
        :param PaymentOptionTwo: 合同选项2（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionTwo: str
        :param PaymentOptionThree: 合同选项3（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionThree: str
        :param PaymentOptionFour: 合同选项4（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionFour: str
        :param PaymentOptionFive: 合同证书选项1（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionFive: str
        :param PaymentOptionSix: 合同证书选项2（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionSix: str
        :param PaymentOptionSeven: 合同选项5（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionSeven: str
        :param PaymentOptionOther: 合同选项6（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionOther: str
        :param PaymentOptionTen: 合同选项8
        :type PaymentOptionTen: str
        :param PaymentOptionNine: 合同选项7（不同支付方式规则不一样，请以支付方式规定的格式传值）
        :type PaymentOptionNine: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OutContractId = None
        self.Code = None
        self.PaymentId = None
        self.PaymentClassificationId = None
        self.PaymentClassificationLimit = None
        self.MerchantNo = None
        self.Fee = None
        self.StartDate = None
        self.EndDate = None
        self.SignMan = None
        self.SignName = None
        self.SignDate = None
        self.AutoSign = None
        self.Contact = None
        self.ContactTelephone = None
        self.PictureOne = None
        self.PictureTwo = None
        self.ChannelExtJson = None
        self.Profile = None
        self.PaymentOptionOne = None
        self.PaymentOptionTwo = None
        self.PaymentOptionThree = None
        self.PaymentOptionFour = None
        self.PaymentOptionFive = None
        self.PaymentOptionSix = None
        self.PaymentOptionSeven = None
        self.PaymentOptionOther = None
        self.PaymentOptionTen = None
        self.PaymentOptionNine = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OutContractId = params.get("OutContractId")
        self.Code = params.get("Code")
        self.PaymentId = params.get("PaymentId")
        self.PaymentClassificationId = params.get("PaymentClassificationId")
        self.PaymentClassificationLimit = params.get("PaymentClassificationLimit")
        self.MerchantNo = params.get("MerchantNo")
        self.Fee = params.get("Fee")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.SignMan = params.get("SignMan")
        self.SignName = params.get("SignName")
        self.SignDate = params.get("SignDate")
        self.AutoSign = params.get("AutoSign")
        self.Contact = params.get("Contact")
        self.ContactTelephone = params.get("ContactTelephone")
        self.PictureOne = params.get("PictureOne")
        self.PictureTwo = params.get("PictureTwo")
        self.ChannelExtJson = params.get("ChannelExtJson")
        self.Profile = params.get("Profile")
        self.PaymentOptionOne = params.get("PaymentOptionOne")
        self.PaymentOptionTwo = params.get("PaymentOptionTwo")
        self.PaymentOptionThree = params.get("PaymentOptionThree")
        self.PaymentOptionFour = params.get("PaymentOptionFour")
        self.PaymentOptionFive = params.get("PaymentOptionFive")
        self.PaymentOptionSix = params.get("PaymentOptionSix")
        self.PaymentOptionSeven = params.get("PaymentOptionSeven")
        self.PaymentOptionOther = params.get("PaymentOptionOther")
        self.PaymentOptionTen = params.get("PaymentOptionTen")
        self.PaymentOptionNine = params.get("PaymentOptionNine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddContractResponse(AbstractModel):
    """AddContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 添加合同响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.AddContractResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = AddContractResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class AddContractResult(AbstractModel):
    """添加合同响应对象

    """

    def __init__(self):
        r"""
        :param ContractId: 合同主键
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractId: str
        """
        self.ContractId = None


    def _deserialize(self, params):
        self.ContractId = params.get("ContractId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMerchantRequest(AbstractModel):
    """AddMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param OutMerchantId: 机构商户主键（系统有唯一性校验），建议使用商户表的主键ID，防止重复添加商户
        :type OutMerchantId: str
        :param MerchantName: 商户名称，小微商户命名要符合“”商户_名字” （例如：商户_张三）
        :type MerchantName: str
        :param BusinessLicenseType: 营业执照类型（1三证合一，2非三证合一）
        :type BusinessLicenseType: str
        :param BusinessLicenseNo: 营业执照编号（系统有唯一性校验），（小微商户不效验，随意传要有值，公司/个体户必传）
        :type BusinessLicenseNo: str
        :param BusinessLicensePicture: 营业执照图片【私密区】（系统返回的图片路径），（小微商户不效验，随意传要有值，公司/个体户必传）
        :type BusinessLicensePicture: str
        :param BusinessLicenseStartDate: 营业执照生效时间（yyyy-mm-dd），（小微商户不效验，随意传要有值，公司/个体户必传）
        :type BusinessLicenseStartDate: str
        :param BusinessLicenseEndDate: 营业执照过期时间（yyyy-mm-dd），（小微商户不效验，随意传要有值，公司/个体户必传）
        :type BusinessLicenseEndDate: str
        :param ClassificationIds: 行业分类编号列表（第一个分类编号为主分类，后面的为二级分类）
        :type ClassificationIds: list of str
        :param BrandName: 招牌名称
        :type BrandName: str
        :param Telephone: 联系电话
        :type Telephone: str
        :param CityId: 城市编号
        :type CityId: str
        :param Address: 详细地址，不含省市区县名称，长度需要大于5。
        :type Address: str
        :param OpenHours: 营业时间，多个以小写逗号分开(9:00-12:00,13:00-18:00)
        :type OpenHours: str
        :param AccountType: 结算账户类型（2对私，1对公）
        :type AccountType: str
        :param BankNo: 清算联行号，开户行行号
        :type BankNo: str
        :param BankName: 开户行名称
        :type BankName: str
        :param AccountNo: 银行账号
        :type AccountNo: str
        :param AccountName: 银行户名
        :type AccountName: str
        :param BossIdType: 法人证件类型（1居民身份证,2临时居民身份证,3居民户口簿,4护照,5港澳居民来往内地通行证,6回乡证,7军人证,8武警身份证,9其他法定文件）
        :type BossIdType: str
        :param BossIdNo: 法人证件号码
        :type BossIdNo: str
        :param BossName: 法人姓名
        :type BossName: str
        :param BossSex: 法人性别（1男，2女）
        :type BossSex: str
        :param BossIdCountry: 法人证件国别/地区（中国CHN，香港HKG，澳门MAC，台湾CTN）
        :type BossIdCountry: str
        :param BossPositive: 法人身份证正面【私密区】（系统返回的图片路径）
        :type BossPositive: str
        :param BossBack: 法人身份证背面【私密区】（系统返回的图片路径）
        :type BossBack: str
        :param BossStartDate: 法人证件生效时间（yyyy-mm-dd）
        :type BossStartDate: str
        :param BossEndDate: 法人证件过期时间（yyyy-mm-dd）
        :type BossEndDate: str
        :param LicencePicture: 许可证图片【私密区】，（小微商户不效验，随意传要有值，公司/个体户必传）
        :type LicencePicture: str
        :param Type: 商户类型：1-个体，2-小微，3-企业。不传默认为2-小微商户。
        :type Type: str
        :param OrganizationNo: 组织机构代码证号
        :type OrganizationNo: str
        :param OrganizationStartDate: 组织机构代码证生效时间（yyyy-mm-dd）
        :type OrganizationStartDate: str
        :param OrganizationPicture: 组织机构代码证图片【私密区】
        :type OrganizationPicture: str
        :param OrganizationEndDate: 组织机构代码证过期时间（yyyy-mm-dd）
        :type OrganizationEndDate: str
        :param Intro: 商户简介
        :type Intro: str
        :param Logo: 商户logo【公共区】
        :type Logo: str
        :param Tag: 商户标记，自定义参数
        :type Tag: str
        :param FinancialTelephone: 财务联系人电话
        :type FinancialTelephone: str
        :param FinancialContact: 财务联系人
        :type FinancialContact: str
        :param TaxRegistrationNo: 税务登记证号
        :type TaxRegistrationNo: str
        :param TaxRegistrationPicture: 税务登记证图片【私密区】
        :type TaxRegistrationPicture: str
        :param TaxRegistrationStartDate: 税务登记证生效时间（yyyy-mm-dd）
        :type TaxRegistrationStartDate: str
        :param TaxRegistrationEndDate: 税务登记证过期时间（yyyy-mm-dd）
        :type TaxRegistrationEndDate: str
        :param AccountBoss: 结算账户人身份（1法人，2法人亲属），结算帐户为对私时必填
        :type AccountBoss: str
        :param AccountManagerName: 客户经理姓名，必须为系统后台的管理员真实姓名
        :type AccountManagerName: str
        :param BossTelephone: 法人电话
        :type BossTelephone: str
        :param BossJob: 法人职业
        :type BossJob: str
        :param BossEmail: 法人邮箱
        :type BossEmail: str
        :param BossAddress: 法人住址
        :type BossAddress: str
        :param AccountIdType: 法人亲属证件类型（1居民身份证,2临时居民身份证,3居民户口簿,4护照,5港澳居民来往内地通行证,6回乡证,7军人证,8武警身份证,9其他法定文件）结算账户人身份为法人亲属时必填
        :type AccountIdType: str
        :param AccountIdNo: 法人亲属证件号码
        :type AccountIdNo: str
        :param LicencePictureTwo: 授权文件【私密区】
        :type LicencePictureTwo: str
        :param OtherPictureOne: 其他资料1
        :type OtherPictureOne: str
        :param OtherPictureTwo: 其他资料2
        :type OtherPictureTwo: str
        :param OtherPictureThree: 其他资料3
        :type OtherPictureThree: str
        :param OtherPictureFour: 其他资料4
        :type OtherPictureFour: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OutMerchantId = None
        self.MerchantName = None
        self.BusinessLicenseType = None
        self.BusinessLicenseNo = None
        self.BusinessLicensePicture = None
        self.BusinessLicenseStartDate = None
        self.BusinessLicenseEndDate = None
        self.ClassificationIds = None
        self.BrandName = None
        self.Telephone = None
        self.CityId = None
        self.Address = None
        self.OpenHours = None
        self.AccountType = None
        self.BankNo = None
        self.BankName = None
        self.AccountNo = None
        self.AccountName = None
        self.BossIdType = None
        self.BossIdNo = None
        self.BossName = None
        self.BossSex = None
        self.BossIdCountry = None
        self.BossPositive = None
        self.BossBack = None
        self.BossStartDate = None
        self.BossEndDate = None
        self.LicencePicture = None
        self.Type = None
        self.OrganizationNo = None
        self.OrganizationStartDate = None
        self.OrganizationPicture = None
        self.OrganizationEndDate = None
        self.Intro = None
        self.Logo = None
        self.Tag = None
        self.FinancialTelephone = None
        self.FinancialContact = None
        self.TaxRegistrationNo = None
        self.TaxRegistrationPicture = None
        self.TaxRegistrationStartDate = None
        self.TaxRegistrationEndDate = None
        self.AccountBoss = None
        self.AccountManagerName = None
        self.BossTelephone = None
        self.BossJob = None
        self.BossEmail = None
        self.BossAddress = None
        self.AccountIdType = None
        self.AccountIdNo = None
        self.LicencePictureTwo = None
        self.OtherPictureOne = None
        self.OtherPictureTwo = None
        self.OtherPictureThree = None
        self.OtherPictureFour = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OutMerchantId = params.get("OutMerchantId")
        self.MerchantName = params.get("MerchantName")
        self.BusinessLicenseType = params.get("BusinessLicenseType")
        self.BusinessLicenseNo = params.get("BusinessLicenseNo")
        self.BusinessLicensePicture = params.get("BusinessLicensePicture")
        self.BusinessLicenseStartDate = params.get("BusinessLicenseStartDate")
        self.BusinessLicenseEndDate = params.get("BusinessLicenseEndDate")
        self.ClassificationIds = params.get("ClassificationIds")
        self.BrandName = params.get("BrandName")
        self.Telephone = params.get("Telephone")
        self.CityId = params.get("CityId")
        self.Address = params.get("Address")
        self.OpenHours = params.get("OpenHours")
        self.AccountType = params.get("AccountType")
        self.BankNo = params.get("BankNo")
        self.BankName = params.get("BankName")
        self.AccountNo = params.get("AccountNo")
        self.AccountName = params.get("AccountName")
        self.BossIdType = params.get("BossIdType")
        self.BossIdNo = params.get("BossIdNo")
        self.BossName = params.get("BossName")
        self.BossSex = params.get("BossSex")
        self.BossIdCountry = params.get("BossIdCountry")
        self.BossPositive = params.get("BossPositive")
        self.BossBack = params.get("BossBack")
        self.BossStartDate = params.get("BossStartDate")
        self.BossEndDate = params.get("BossEndDate")
        self.LicencePicture = params.get("LicencePicture")
        self.Type = params.get("Type")
        self.OrganizationNo = params.get("OrganizationNo")
        self.OrganizationStartDate = params.get("OrganizationStartDate")
        self.OrganizationPicture = params.get("OrganizationPicture")
        self.OrganizationEndDate = params.get("OrganizationEndDate")
        self.Intro = params.get("Intro")
        self.Logo = params.get("Logo")
        self.Tag = params.get("Tag")
        self.FinancialTelephone = params.get("FinancialTelephone")
        self.FinancialContact = params.get("FinancialContact")
        self.TaxRegistrationNo = params.get("TaxRegistrationNo")
        self.TaxRegistrationPicture = params.get("TaxRegistrationPicture")
        self.TaxRegistrationStartDate = params.get("TaxRegistrationStartDate")
        self.TaxRegistrationEndDate = params.get("TaxRegistrationEndDate")
        self.AccountBoss = params.get("AccountBoss")
        self.AccountManagerName = params.get("AccountManagerName")
        self.BossTelephone = params.get("BossTelephone")
        self.BossJob = params.get("BossJob")
        self.BossEmail = params.get("BossEmail")
        self.BossAddress = params.get("BossAddress")
        self.AccountIdType = params.get("AccountIdType")
        self.AccountIdNo = params.get("AccountIdNo")
        self.LicencePictureTwo = params.get("LicencePictureTwo")
        self.OtherPictureOne = params.get("OtherPictureOne")
        self.OtherPictureTwo = params.get("OtherPictureTwo")
        self.OtherPictureThree = params.get("OtherPictureThree")
        self.OtherPictureFour = params.get("OtherPictureFour")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddMerchantResponse(AbstractModel):
    """AddMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码，0表示成功，其他表示失败。
        :type ErrCode: str
        :param Result: 添加商户响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.AddMerchantResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = AddMerchantResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class AddMerchantResult(AbstractModel):
    """添加商户响应对象

    """

    def __init__(self):
        r"""
        :param MerchantNo: 系统商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        """
        self.MerchantNo = None


    def _deserialize(self, params):
        self.MerchantNo = params.get("MerchantNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddShopRequest(AbstractModel):
    """AddShop请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param OutShopId: 机构门店主键（系统有唯一性校验），建议使用门店表的主键ID，防止重复添加门店
        :type OutShopId: str
        :param ShopName: 门店简称（例如：南山店）
        :type ShopName: str
        :param ShopFullName: 门店全称（例如：江山小厨（南山店））
        :type ShopFullName: str
        :param MerchantNo: 商户编号
        :type MerchantNo: str
        :param Telephone: 门店电话
        :type Telephone: str
        :param OpenHours: 营业时间，多个以小写逗号分开(9:00-12:00,13:00-18:00)
        :type OpenHours: str
        :param CityId: 门店所在的城市编码
        :type CityId: str
        :param Address: 门店详细地址，不含省市区县名称
        :type Address: str
        :param PictureOne: 整体门面（含招牌）图片【公共区】
        :type PictureOne: str
        :param PictureTwo: 整体门面（含招牌）图片【公共区】
        :type PictureTwo: str
        :param PictureThree: 店内环境图片【公共区】
        :type PictureThree: str
        :param FinancialTelephone: 负责人手机号码
        :type FinancialTelephone: str
        :param Contact: 门店负责人
        :type Contact: str
        :param Latitude: 百度地图纬度
        :type Latitude: str
        :param LatitudeTwo: 高德地图纬度
        :type LatitudeTwo: str
        :param Longitude: 百度地图经度
        :type Longitude: str
        :param LongitudeTwo: 高德地图经度
        :type LongitudeTwo: str
        :param OtherPicture: 其他照片【公共区】
        :type OtherPicture: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OutShopId = None
        self.ShopName = None
        self.ShopFullName = None
        self.MerchantNo = None
        self.Telephone = None
        self.OpenHours = None
        self.CityId = None
        self.Address = None
        self.PictureOne = None
        self.PictureTwo = None
        self.PictureThree = None
        self.FinancialTelephone = None
        self.Contact = None
        self.Latitude = None
        self.LatitudeTwo = None
        self.Longitude = None
        self.LongitudeTwo = None
        self.OtherPicture = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OutShopId = params.get("OutShopId")
        self.ShopName = params.get("ShopName")
        self.ShopFullName = params.get("ShopFullName")
        self.MerchantNo = params.get("MerchantNo")
        self.Telephone = params.get("Telephone")
        self.OpenHours = params.get("OpenHours")
        self.CityId = params.get("CityId")
        self.Address = params.get("Address")
        self.PictureOne = params.get("PictureOne")
        self.PictureTwo = params.get("PictureTwo")
        self.PictureThree = params.get("PictureThree")
        self.FinancialTelephone = params.get("FinancialTelephone")
        self.Contact = params.get("Contact")
        self.Latitude = params.get("Latitude")
        self.LatitudeTwo = params.get("LatitudeTwo")
        self.Longitude = params.get("Longitude")
        self.LongitudeTwo = params.get("LongitudeTwo")
        self.OtherPicture = params.get("OtherPicture")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddShopResponse(AbstractModel):
    """AddShop返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 添加申请响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.AddShopResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = AddShopResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class AddShopResult(AbstractModel):
    """添加门店响应对象

    """

    def __init__(self):
        r"""
        :param ShopNo: 门店编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopNo: str
        """
        self.ShopNo = None


    def _deserialize(self, params):
        self.ShopNo = params.get("ShopNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgencyClientInfo(AbstractModel):
    """经办人信息

    """

    def __init__(self):
        r"""
        :param AgencyClientName: 经办人姓名，存在经办人必输
        :type AgencyClientName: str
        :param AgencyClientGlobalType: 经办人证件类型，存在经办人必输
        :type AgencyClientGlobalType: str
        :param AgencyClientGlobalId: 经办人证件号，存在经办人必输
        :type AgencyClientGlobalId: str
        :param AgencyClientMobile: 经办人手机号，存在经办人必输
        :type AgencyClientMobile: str
        """
        self.AgencyClientName = None
        self.AgencyClientGlobalType = None
        self.AgencyClientGlobalId = None
        self.AgencyClientMobile = None


    def _deserialize(self, params):
        self.AgencyClientName = params.get("AgencyClientName")
        self.AgencyClientGlobalType = params.get("AgencyClientGlobalType")
        self.AgencyClientGlobalId = params.get("AgencyClientGlobalId")
        self.AgencyClientMobile = params.get("AgencyClientMobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTaxPayment(AbstractModel):
    """代理商完税证明

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播银行账号
        :type AnchorId: str
        :param AnchorName: 主播姓名
        :type AnchorName: str
        :param AnchorIDCard: 主播身份证
        :type AnchorIDCard: str
        :param StartTime: 纳税的开始时间，格式yyyy-MM-dd
        :type StartTime: str
        :param EndTime: 纳税的结束时间，格式yyyy-MM-dd
        :type EndTime: str
        :param Amount: 流水金额。以“分”为单位
        :type Amount: int
        :param Tax: 应缴税款。以“分”为单位
        :type Tax: int
        """
        self.AnchorId = None
        self.AnchorName = None
        self.AnchorIDCard = None
        self.StartTime = None
        self.EndTime = None
        self.Amount = None
        self.Tax = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.AnchorName = params.get("AnchorName")
        self.AnchorIDCard = params.get("AnchorIDCard")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Amount = params.get("Amount")
        self.Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTaxPaymentBatch(AbstractModel):
    """代理商完税证明批次信息

    """

    def __init__(self):
        r"""
        :param StatusMsg: 状态消息
        :type StatusMsg: str
        :param BatchNum: 批次号
        :type BatchNum: int
        :param InfoNum: 录入记录的条数
        :type InfoNum: int
        :param RawElectronicCertUrl: 源电子凭证下载地址
        :type RawElectronicCertUrl: str
        :param AgentId: 代理商账号
        :type AgentId: str
        :param FileName: 文件名
        :type FileName: str
        :param StatusCode: 状态码。0表示下载成功
        :type StatusCode: int
        :param Channel: 渠道号
        :type Channel: int
        :param Type: 0-视同，1-个体工商户
        :type Type: int
        """
        self.StatusMsg = None
        self.BatchNum = None
        self.InfoNum = None
        self.RawElectronicCertUrl = None
        self.AgentId = None
        self.FileName = None
        self.StatusCode = None
        self.Channel = None
        self.Type = None


    def _deserialize(self, params):
        self.StatusMsg = params.get("StatusMsg")
        self.BatchNum = params.get("BatchNum")
        self.InfoNum = params.get("InfoNum")
        self.RawElectronicCertUrl = params.get("RawElectronicCertUrl")
        self.AgentId = params.get("AgentId")
        self.FileName = params.get("FileName")
        self.StatusCode = params.get("StatusCode")
        self.Channel = params.get("Channel")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AmountBeforeTaxResult(AbstractModel):
    """税前金额结果

    """

    def __init__(self):
        r"""
        :param AmountBeforeTax: 税前金额
注意：此字段可能返回 null，表示取不到有效值。
        :type AmountBeforeTax: str
        """
        self.AmountBeforeTax = None


    def _deserialize(self, params):
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnchorContractInfo(AbstractModel):
    """主播签约信息

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播ID
        :type AnchorId: str
        :param AnchorName: 主播名称
        :type AnchorName: str
        :param AgentId: 代理商ID
        :type AgentId: str
        :param AgentName: 代理商名称
        :type AgentName: str
        :param IdNo: 主播身份证号
        :type IdNo: str
        """
        self.AnchorId = None
        self.AnchorName = None
        self.AgentId = None
        self.AgentName = None
        self.IdNo = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.AnchorName = params.get("AnchorName")
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        self.IdNo = params.get("IdNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnchorExtendInfo(AbstractModel):
    """主播扩展信息

    """

    def __init__(self):
        r"""
        :param Type: 扩展信息类型
__id_card_no__:身份证号码
__id_card_name__:身份证姓名
__id_card_front__:身份证图片正面
__id_card_back__:身份证图片反面
__tax_type__:完税类型:0-自然人,1-个体工商户
__channel_account__:渠道账号(_敏感信息_ 使用 __AES128-CBC-PKCS#7__ 加密)
        :type Type: str
        :param Value: 扩展信息
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyApplicationMaterialRequest(AbstractModel):
    """ApplyApplicationMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param TradeCode: 贸易编码
        :type TradeCode: str
        :param OriginalDeclareId: 原申报流水号
        :type OriginalDeclareId: str
        :param SourceAmount: 源金额
        :type SourceAmount: int
        :param TargetAmount: 目的金额
        :type TargetAmount: int
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.TransactionId = None
        self.DeclareId = None
        self.PayerId = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.TradeCode = None
        self.OriginalDeclareId = None
        self.SourceAmount = None
        self.TargetAmount = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.DeclareId = params.get("DeclareId")
        self.PayerId = params.get("PayerId")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TradeCode = params.get("TradeCode")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetAmount = params.get("TargetAmount")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyApplicationMaterialResponse(AbstractModel):
    """ApplyApplicationMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 提交申报材料结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyDeclareResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyDeclareData(AbstractModel):
    """提交申报材料结果

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 第三方指令编号
        :type TransactionId: str
        :param Status: 受理状态
        :type Status: str
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param OriginalDeclareId: 原申报流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalDeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.Status = None
        self.DeclareId = None
        self.OriginalDeclareId = None
        self.PayerId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.Status = params.get("Status")
        self.DeclareId = params.get("DeclareId")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.PayerId = params.get("PayerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyDeclareResult(AbstractModel):
    """提交申报材料结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码
        :type Code: str
        :param Data: 提交申报材料数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyDeclareData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyFlexPaymentRequest(AbstractModel):
    """ApplyFlexPayment请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param OutOrderId: 外部订单ID
        :type OutOrderId: str
        :param FundingAccountInfo: 资金账户信息
        :type FundingAccountInfo: :class:`tencentcloud.cpdp.v20190820.models.FlexFundingAccountInfo`
        :param Remark: 提现备注
        :type Remark: str
        """
        self.PayeeId = None
        self.IncomeType = None
        self.AmountBeforeTax = None
        self.OutOrderId = None
        self.FundingAccountInfo = None
        self.Remark = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.IncomeType = params.get("IncomeType")
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.OutOrderId = params.get("OutOrderId")
        if params.get("FundingAccountInfo") is not None:
            self.FundingAccountInfo = FlexFundingAccountInfo()
            self.FundingAccountInfo._deserialize(params.get("FundingAccountInfo"))
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyFlexPaymentResponse(AbstractModel):
    """ApplyFlexPayment返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexPaymentResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = ApplyFlexPaymentResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyFlexPaymentResult(AbstractModel):
    """付款结果

    """

    def __init__(self):
        r"""
        :param OrderId: 订单ID
        :type OrderId: str
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param AmountAfterTax: 税后金额
        :type AmountAfterTax: str
        :param Tax: 税金
        :type Tax: str
        """
        self.OrderId = None
        self.AmountBeforeTax = None
        self.AmountAfterTax = None
        self.Tax = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.AmountAfterTax = params.get("AmountAfterTax")
        self.Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyFlexSettlementRequest(AbstractModel):
    """ApplyFlexSettlement请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param OutOrderId: 外部订单ID
        :type OutOrderId: str
        :param Remark: 备注
        :type Remark: str
        """
        self.PayeeId = None
        self.IncomeType = None
        self.AmountBeforeTax = None
        self.OutOrderId = None
        self.Remark = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.IncomeType = params.get("IncomeType")
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.OutOrderId = params.get("OutOrderId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyFlexSettlementResponse(AbstractModel):
    """ApplyFlexSettlement返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyFlexSettlementResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = ApplyFlexSettlementResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyFlexSettlementResult(AbstractModel):
    """结算结果

    """

    def __init__(self):
        r"""
        :param OrderId: 订单ID
        :type OrderId: str
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param AmountAfterTax: 税后金额
        :type AmountAfterTax: str
        :param Tax: 税金
        :type Tax: str
        """
        self.OrderId = None
        self.AmountBeforeTax = None
        self.AmountAfterTax = None
        self.Tax = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.AmountAfterTax = params.get("AmountAfterTax")
        self.Tax = params.get("Tax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOpenBankOrderDetailReceiptRequest(AbstractModel):
    """ApplyOpenBankOrderDetailReceipt请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutApplyId: 外部回单申请编号
        :type OutApplyId: str
        :param ChannelMerchantId: 渠道商户ID
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称，目前只支持ALIPAY
        :type ChannelName: str
        :param PaymentMethod: 支付方式，目前只支持SAFT_ISV
        :type PaymentMethod: str
        :param ChannelOrderId: 云企付平台订单号
        :type ChannelOrderId: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.OutApplyId = None
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.ChannelOrderId = None
        self.Environment = None


    def _deserialize(self, params):
        self.OutApplyId = params.get("OutApplyId")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOpenBankOrderDetailReceiptResponse(AbstractModel):
    """ApplyOpenBankOrderDetailReceipt返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
        :type ErrCode: str
        :param ErrMessage: 错误消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyOpenBankOrderDetailReceiptResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = ApplyOpenBankOrderDetailReceiptResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyOpenBankOrderDetailReceiptResult(AbstractModel):
    """申请单笔交易回单结果

    """

    def __init__(self):
        r"""
        :param ChannelApplyId: 渠道回单申请ID
        :type ChannelApplyId: str
        :param ReceiptStatus: 申请状态。
SUCCESS：申请成功；
FAILED：申请失败；
PROCESSING：申请中。
注意：若返回申请中，需要再次调用回单申请结果查询接口，查询结果。
        :type ReceiptStatus: str
        :param ReceiptMessage: 申请返回描述，例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiptMessage: str
        :param DownloadUrl: 回单下载链接，申请成功时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param ExpireTime: 过期时间，yyyy-MM-dd HH:mm:ss格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        """
        self.ChannelApplyId = None
        self.ReceiptStatus = None
        self.ReceiptMessage = None
        self.DownloadUrl = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.ReceiptStatus = params.get("ReceiptStatus")
        self.ReceiptMessage = params.get("ReceiptMessage")
        self.DownloadUrl = params.get("DownloadUrl")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOutwardOrderData(AbstractModel):
    """汇出指令申请数据

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param Status: 受理状态
        :type Status: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOutwardOrderRequest(AbstractModel):
    """ApplyOutwardOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param PricingCurrency: 定价币种
        :type PricingCurrency: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param PayeeType: 收款人类型（银行卡填"BANK_ACCOUNT"）
        :type PayeeType: str
        :param PayeeAccount: 收款人账号
        :type PayeeAccount: str
        :param SourceAmount: 源币种金额
        :type SourceAmount: float
        :param TargetAmount: 目的金额
        :type TargetAmount: float
        :param PayeeName: 收款人姓名（PayeeType为"BANK_COUNT"时必填）
        :type PayeeName: str
        :param PayeeAddress: 收款人地址（PayeeType为"BANK_COUNT"时必填）
        :type PayeeAddress: str
        :param PayeeBankAccountType: 收款人银行账号类型（PayeeType为"BANK_COUNT"时必填）
个人填"INDIVIDUAL"
企业填"CORPORATE"
        :type PayeeBankAccountType: str
        :param PayeeCountryCode: 收款人国家或地区编码（PayeeType为"BANK_COUNT"时必填）
        :type PayeeCountryCode: str
        :param PayeeBankName: 收款人开户银行名称（PayeeType为"BANK_COUNT"时必填）
        :type PayeeBankName: str
        :param PayeeBankAddress: 收款人开户银行地址（PayeeType为"BANK_COUNT"时必填）
        :type PayeeBankAddress: str
        :param PayeeBankDistrict: 收款人开户银行所在国家或地区编码（PayeeType为"BANK_COUNT"时必填）
        :type PayeeBankDistrict: str
        :param PayeeBankSwiftCode: 收款银行SwiftCode（PayeeType为"BANK_COUNT"时必填）
        :type PayeeBankSwiftCode: str
        :param PayeeBankType: 收款银行国际编码类型
        :type PayeeBankType: str
        :param PayeeBankCode: 收款银行国际编码
        :type PayeeBankCode: str
        :param ReferenceForBeneficiary: 收款人附言
        :type ReferenceForBeneficiary: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.TransactionId = None
        self.PricingCurrency = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.PayeeType = None
        self.PayeeAccount = None
        self.SourceAmount = None
        self.TargetAmount = None
        self.PayeeName = None
        self.PayeeAddress = None
        self.PayeeBankAccountType = None
        self.PayeeCountryCode = None
        self.PayeeBankName = None
        self.PayeeBankAddress = None
        self.PayeeBankDistrict = None
        self.PayeeBankSwiftCode = None
        self.PayeeBankType = None
        self.PayeeBankCode = None
        self.ReferenceForBeneficiary = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.PricingCurrency = params.get("PricingCurrency")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.PayeeType = params.get("PayeeType")
        self.PayeeAccount = params.get("PayeeAccount")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetAmount = params.get("TargetAmount")
        self.PayeeName = params.get("PayeeName")
        self.PayeeAddress = params.get("PayeeAddress")
        self.PayeeBankAccountType = params.get("PayeeBankAccountType")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.PayeeBankName = params.get("PayeeBankName")
        self.PayeeBankAddress = params.get("PayeeBankAddress")
        self.PayeeBankDistrict = params.get("PayeeBankDistrict")
        self.PayeeBankSwiftCode = params.get("PayeeBankSwiftCode")
        self.PayeeBankType = params.get("PayeeBankType")
        self.PayeeBankCode = params.get("PayeeBankCode")
        self.ReferenceForBeneficiary = params.get("ReferenceForBeneficiary")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyOutwardOrderResponse(AbstractModel):
    """ApplyOutwardOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 汇出指令申请
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyOutwardOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyOutwardOrderResult(AbstractModel):
    """汇出指令申请结果

    """

    def __init__(self):
        r"""
        :param Data: 汇出指令申请数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderData`
        :param Code: 错误码
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplyOutwardOrderData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPayerInfoRequest(AbstractModel):
    """ApplyPayerInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayerType: 付款人类型 (个人: INDIVIDUAL, 企业: CORPORATE)
        :type PayerType: str
        :param PayerName: 付款人姓名
        :type PayerName: str
        :param PayerIdType: 付款人证件类型 (身份证: ID_CARD, 统一社会信用代码: UNIFIED_CREDIT_CODE)
        :type PayerIdType: str
        :param PayerIdNo: 付款人证件号
        :type PayerIdNo: str
        :param PayerCountryCode: 付款人常驻国家或地区编码 (见常见问题-国家/地区编码)
        :type PayerCountryCode: str
        :param PayerContactName: 付款人联系人名称
        :type PayerContactName: str
        :param PayerContactNumber: 付款人联系电话
        :type PayerContactNumber: str
        :param PayerEmailAddress: 付款人联系邮箱
        :type PayerEmailAddress: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.PayerId = None
        self.PayerType = None
        self.PayerName = None
        self.PayerIdType = None
        self.PayerIdNo = None
        self.PayerCountryCode = None
        self.PayerContactName = None
        self.PayerContactNumber = None
        self.PayerEmailAddress = None
        self.Profile = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.PayerType = params.get("PayerType")
        self.PayerName = params.get("PayerName")
        self.PayerIdType = params.get("PayerIdType")
        self.PayerIdNo = params.get("PayerIdNo")
        self.PayerCountryCode = params.get("PayerCountryCode")
        self.PayerContactName = params.get("PayerContactName")
        self.PayerContactNumber = params.get("PayerContactNumber")
        self.PayerEmailAddress = params.get("PayerEmailAddress")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPayerInfoResponse(AbstractModel):
    """ApplyPayerInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 付款人申请结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyPayerinfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyPayerinfoData(AbstractModel):
    """付款人申请结果

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        """
        self.MerchantId = None
        self.PayerId = None
        self.Status = None
        self.FailReason = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyPayerinfoResult(AbstractModel):
    """付款人申请结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码
        :type Code: str
        :param Data: 数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyPayerinfoData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyReWithdrawalRequest(AbstractModel):
    """ApplyReWithdrawal请求参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessType: 聚鑫业务类型
        :type BusinessType: int
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param Body: 提现信息
        :type Body: :class:`tencentcloud.cpdp.v20190820.models.WithdrawBill`
        :param MidasAppId: 聚鑫业务ID
        :type MidasAppId: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.BusinessType = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Body = None
        self.MidasAppId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.BusinessType = params.get("BusinessType")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        if params.get("Body") is not None:
            self.Body = WithdrawBill()
            self.Body._deserialize(params.get("Body"))
        self.MidasAppId = params.get("MidasAppId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyReWithdrawalResponse(AbstractModel):
    """ApplyReWithdrawal返回参数结构体

    """

    def __init__(self):
        r"""
        :param WithdrawOrderId: 重新提现业务订单号
        :type WithdrawOrderId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WithdrawOrderId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        self.RequestId = params.get("RequestId")


class ApplyReconciliationFileRequest(AbstractModel):
    """ApplyReconciliationFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplyFileType: 申请的文件类型。
__CZ__：充值文件
__TX__：提现文件
__JY__：交易文件
__YE__：余额文件
        :type ApplyFileType: str
        :param ApplyFileDate: 申请的对账文件日期，格式：yyyyMMdd。
        :type ApplyFileDate: str
        :param BankAccountNumber: 父账户账号。
_平安渠道为资金汇总账号_
        :type BankAccountNumber: str
        :param MidasEnvironment: 环境名。
__release__: 现网环境
__sandbox__: 沙箱环境
__development__: 开发环境
_缺省: release_
        :type MidasEnvironment: str
        """
        self.ApplyFileType = None
        self.ApplyFileDate = None
        self.BankAccountNumber = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.ApplyFileType = params.get("ApplyFileType")
        self.ApplyFileDate = params.get("ApplyFileDate")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyReconciliationFileResponse(AbstractModel):
    """ApplyReconciliationFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyReconciliationFileResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = ApplyReconciliationFileResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyReconciliationFileResult(AbstractModel):
    """申请对账文件结果

    """

    def __init__(self):
        r"""
        :param ApplyFileId: 申请对账文件的任务ID。
        :type ApplyFileId: str
        :param ApplyStatus: 对账文件申请状态。
__I__：申请中
__S__：申请成功
__F__：申请失败
        :type ApplyStatus: str
        :param ApplyMessage: 申请结果描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyMessage: str
        """
        self.ApplyFileId = None
        self.ApplyStatus = None
        self.ApplyMessage = None


    def _deserialize(self, params):
        self.ApplyFileId = params.get("ApplyFileId")
        self.ApplyStatus = params.get("ApplyStatus")
        self.ApplyMessage = params.get("ApplyMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTradeData(AbstractModel):
    """提交贸易材料结果

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param TradeCurrency: 交易币种
        :type TradeCurrency: str
        :param TradeAmount: 交易金额
        :type TradeAmount: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 状态
        :type Status: str
        """
        self.MerchantId = None
        self.TradeFileId = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.PayerId = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TradeFileId = params.get("TradeFileId")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTradeRequest(AbstractModel):
    """ApplyTrade请求参数结构体

    """

    def __init__(self):
        r"""
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param TradeOrderId: 贸易材料订单号
        :type TradeOrderId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayeeName: 收款人姓名
        :type PayeeName: str
        :param PayeeCountryCode: 收款人常驻国家或地区编码 (见常见问题)
        :type PayeeCountryCode: str
        :param TradeType: 贸易类型 (GOODS: 商品, SERVICE: 服务)
        :type TradeType: str
        :param TradeTime: 交易时间 (格式: yyyyMMdd)
        :type TradeTime: str
        :param TradeCurrency: 交易币种
        :type TradeCurrency: str
        :param TradeAmount: 交易金额
        :type TradeAmount: float
        :param TradeName: 交易名称 
(TradeType=GOODS时填写物品名称，可填写多个，格式无要求；
TradeType=SERVICE时填写贸易类别，见常见问题-贸易类别)
        :type TradeName: str
        :param TradeCount: 交易数量 (TradeType=GOODS 填写物品数量, TradeType=SERVICE填写服务次数)
        :type TradeCount: int
        :param GoodsCarrier: 货贸承运人 (TradeType=GOODS 必填)
        :type GoodsCarrier: str
        :param ServiceDetail: 服贸交易细节 (TradeType=GOODS 必填, 见常见问题-交易细节)
        :type ServiceDetail: str
        :param ServiceTime: 服贸服务时间 (TradeType=GOODS 必填, 见常见问题-服务时间)
        :type ServiceTime: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.TradeFileId = None
        self.TradeOrderId = None
        self.PayerId = None
        self.PayeeName = None
        self.PayeeCountryCode = None
        self.TradeType = None
        self.TradeTime = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.TradeName = None
        self.TradeCount = None
        self.GoodsCarrier = None
        self.ServiceDetail = None
        self.ServiceTime = None
        self.Profile = None


    def _deserialize(self, params):
        self.TradeFileId = params.get("TradeFileId")
        self.TradeOrderId = params.get("TradeOrderId")
        self.PayerId = params.get("PayerId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.TradeType = params.get("TradeType")
        self.TradeTime = params.get("TradeTime")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.TradeName = params.get("TradeName")
        self.TradeCount = params.get("TradeCount")
        self.GoodsCarrier = params.get("GoodsCarrier")
        self.ServiceDetail = params.get("ServiceDetail")
        self.ServiceTime = params.get("ServiceTime")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyTradeResponse(AbstractModel):
    """ApplyTrade返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 提交贸易材料结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyTradeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyTradeResult(AbstractModel):
    """提交贸易材料结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码
        :type Code: str
        :param Data: 提交贸易材料数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyTradeData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyWithdrawalRequest(AbstractModel):
    """ApplyWithdrawal请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SettleAcctNo: str
        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SettleAcctName: str
        :param CurrencyType: 币种 RMB
        :type CurrencyType: str
        :param CurrencyUnit: 单位，1：元，2：角，3：分
        :type CurrencyUnit: int
        :param CurrencyAmt: 金额
        :type CurrencyAmt: str
        :param TranWebName: 交易网名称
        :type TranWebName: str
        :param IdType: 会员证件类型
        :type IdType: str
        :param IdCode: 会员证件号码
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type IdCode: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param CommissionAmount: 手续费金额
        :type CommissionAmount: str
        :param WithdrawOrderId: 提现单号，长度32字节
        :type WithdrawOrderId: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None
        self.TranWebName = None
        self.IdType = None
        self.IdCode = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None
        self.CommissionAmount = None
        self.WithdrawOrderId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")
        self.TranWebName = params.get("TranWebName")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.CommissionAmount = params.get("CommissionAmount")
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyWithdrawalResponse(AbstractModel):
    """ApplyWithdrawal返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssignmentData(AbstractModel):
    """分配关系

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播ID
        :type AnchorId: str
        :param AnchorName: 主播名称
        :type AnchorName: str
        :param AgentId: 代理商ID
        :type AgentId: str
        :param AgentName: 代理商名称
        :type AgentName: str
        """
        self.AnchorId = None
        self.AnchorName = None
        self.AgentId = None
        self.AgentName = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.AnchorName = params.get("AnchorName")
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankBranchInfo(AbstractModel):
    """支行信息

    """

    def __init__(self):
        r"""
        :param BankName: 银行名称。
        :type BankName: str
        :param BankAbbreviation: 银行简称。
        :type BankAbbreviation: str
        :param BankBranchName: 支行名。
        :type BankBranchName: str
        :param BankBranchId: 联行号。
        :type BankBranchId: str
        """
        self.BankName = None
        self.BankAbbreviation = None
        self.BankBranchName = None
        self.BankBranchId = None


    def _deserialize(self, params):
        self.BankName = params.get("BankName")
        self.BankAbbreviation = params.get("BankAbbreviation")
        self.BankBranchName = params.get("BankBranchName")
        self.BankBranchId = params.get("BankBranchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BankCardItem(AbstractModel):
    """绑卡列表

    """

    def __init__(self):
        r"""
        :param EiconBankBranchId: 超级网银行号
        :type EiconBankBranchId: str
        :param CnapsBranchId: 大小额行号
        :type CnapsBranchId: str
        :param SettleAcctType: 结算账户类型
1 – 本行账户
2 – 他行账户
        :type SettleAcctType: int
        :param SettleAcctName: 结算账户户名
<敏感信息>
        :type SettleAcctName: str
        :param AcctBranchName: 开户行名称
        :type AcctBranchName: str
        :param SettleAcctNo: 用于提现
<敏感信息>
        :type SettleAcctNo: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 验证类型
1 – 小额转账验证
2 – 短信验证
        :type BindType: int
        :param Mobile: 用于短信验证
BindType==2时必填
<敏感信息>
        :type Mobile: str
        :param IdType: 证件类型
        :type IdType: str
        :param IdCode: 证件号码
<敏感信息>
        :type IdCode: str
        """
        self.EiconBankBranchId = None
        self.CnapsBranchId = None
        self.SettleAcctType = None
        self.SettleAcctName = None
        self.AcctBranchName = None
        self.SettleAcctNo = None
        self.SubAppId = None
        self.BindType = None
        self.Mobile = None
        self.IdType = None
        self.IdCode = None


    def _deserialize(self, params):
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.SettleAcctType = params.get("SettleAcctType")
        self.SettleAcctName = params.get("SettleAcctName")
        self.AcctBranchName = params.get("AcctBranchName")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.Mobile = params.get("Mobile")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDownloadUrlResult(AbstractModel):
    """机构账单文件下载地址响应对象

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 对账单下载地址。GET方式访问，返回zip包，解压后为csv格式文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        """
        self.DownloadUrl = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAccountRequest(AbstractModel):
    """BindAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播Id
        :type AnchorId: str
        :param TransferType: 1 微信企业付款 
2 支付宝转账 
3 平安银企直连代发转账
        :type TransferType: int
        :param AccountNo: 收款方标识。
微信为open_id；
支付宝为会员alipay_user_id;
平安为收款方银行账号;
        :type AccountNo: str
        :param PhoneNum: 手机号
        :type PhoneNum: str
        """
        self.AnchorId = None
        self.TransferType = None
        self.AccountNo = None
        self.PhoneNum = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.TransferType = params.get("TransferType")
        self.AccountNo = params.get("AccountNo")
        self.PhoneNum = params.get("PhoneNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAccountResponse(AbstractModel):
    """BindAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMessage: 响应消息。
        :type ErrMessage: str
        :param Result: 该字段为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindAcctRequest(AbstractModel):
    """BindAcct请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 1 – 小额转账验证
2 – 短信验证
3 - 一分钱转账验证，无需再调CheckAcct验证绑卡
4 - 银行四要素验证，无需再调CheckAcct验证绑卡
每个结算账户每天只能使用一次小额转账验证
        :type BindType: int
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SettleAcctNo: str
        :param SettleAcctName: 结算账户户名
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SettleAcctName: str
        :param SettleAcctType: 1 – 本行账户
2 – 他行账户
        :type SettleAcctType: int
        :param IdType: 证件类型，见《证件类型》表
        :type IdType: str
        :param IdCode: 证件号码
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type IdCode: str
        :param AcctBranchName: 开户行名称
        :type AcctBranchName: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param Mobile: 用于短信验证
BindType==2时必填
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type Mobile: str
        :param CnapsBranchId: 大小额行号，超级网银行号和大小额行号
二选一
        :type CnapsBranchId: str
        :param EiconBankBranchId: 超级网银行号，超级网银行号和大小额行号
二选一
        :type EiconBankBranchId: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param AgencyClientInfo: 经办人信息
        :type AgencyClientInfo: :class:`tencentcloud.cpdp.v20190820.models.AgencyClientInfo`
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.SettleAcctType = None
        self.IdType = None
        self.IdCode = None
        self.AcctBranchName = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.EncryptType = None
        self.MidasEnvironment = None
        self.AgencyClientInfo = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.SettleAcctType = params.get("SettleAcctType")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.AcctBranchName = params.get("AcctBranchName")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        if params.get("AgencyClientInfo") is not None:
            self.AgencyClientInfo = AgencyClientInfo()
            self.AgencyClientInfo._deserialize(params.get("AgencyClientInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAcctResponse(AbstractModel):
    """BindAcct返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindOpenBankExternalSubMerchantBankAccountRequest(AbstractModel):
    """BindOpenBankExternalSubMerchantBankAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
        :type PaymentMethod: str
        :param ExternalSubMerchantBindBankAccountData: 第三方渠道子商户收款方银行卡信息, 为JSON格式字符串。详情见附录-复杂类型。
        :type ExternalSubMerchantBindBankAccountData: str
        :param OutApplyId: 外部申请编号。
        :type OutApplyId: str
        :param NotifyUrl: 通知地址。
        :type NotifyUrl: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.ExternalSubMerchantBindBankAccountData = None
        self.OutApplyId = None
        self.NotifyUrl = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.ExternalSubMerchantBindBankAccountData = params.get("ExternalSubMerchantBindBankAccountData")
        self.OutApplyId = params.get("OutApplyId")
        self.NotifyUrl = params.get("NotifyUrl")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOpenBankExternalSubMerchantBankAccountResponse(AbstractModel):
    """BindOpenBankExternalSubMerchantBankAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.BindOpenBankExternalSubMerchantBankAccountResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = BindOpenBankExternalSubMerchantBankAccountResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class BindOpenBankExternalSubMerchantBankAccountResult(AbstractModel):
    """第三方子商户银行卡绑定返回结果

    """

    def __init__(self):
        r"""
        :param ChannelApplyId: 渠道申请编号。
        :type ChannelApplyId: str
        :param BindStatus: 绑定状态。
__SUCCESS__: 绑定成功
__FAILED__: 绑定失败
__PROCESSING__: 绑定中。
注意：若返回绑定中，需要再次调用绑定结果查询接口,查询结果。
        :type BindStatus: str
        :param BindMessage: 绑定返回描述, 例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindMessage: str
        :param ExternalSubMerchantBankAccountReturnData: 渠道子商户银行账户信息, 为JSON格式字符串（绑定成功状态下返回）。详情见附录-复杂类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalSubMerchantBankAccountReturnData: str
        :param BindSerialNo: 绑卡序列号。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindSerialNo: str
        """
        self.ChannelApplyId = None
        self.BindStatus = None
        self.BindMessage = None
        self.ExternalSubMerchantBankAccountReturnData = None
        self.BindSerialNo = None


    def _deserialize(self, params):
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.BindStatus = params.get("BindStatus")
        self.BindMessage = params.get("BindMessage")
        self.ExternalSubMerchantBankAccountReturnData = params.get("ExternalSubMerchantBankAccountReturnData")
        self.BindSerialNo = params.get("BindSerialNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRelateAccReUnionPayRequest(AbstractModel):
    """BindRelateAccReUnionPay请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctUnionPay接口中的“会员的待绑定账户的账号”）
        :type MemberAcctNo: str
        :param MessageCheckCode: STRING(20)，短信验证码（即 BindRelateAcctUnionPay接口中的手机所接收到的短信验证码）
        :type MessageCheckCode: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.MessageCheckCode = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.MessageCheckCode = params.get("MessageCheckCode")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRelateAccReUnionPayResponse(AbstractModel):
    """BindRelateAccReUnionPay返回参数结构体

    """

    def __init__(self):
        r"""
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class BindRelateAcctSmallAmountRequest(AbstractModel):
    """BindRelateAcctSmallAmount请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）
        :type Mobile: str
        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，转账方式（1: 往账鉴权(默认值); 2: 来账鉴权）
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRelateAcctSmallAmountResponse(AbstractModel):
    """BindRelateAcctSmallAmount返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域（来账鉴权的方式下，此字段的值为客户需往监管账户转入的金额。在同名子账户绑定的场景下，若返回""VERIFIED""则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class BindRelateAcctUnionPayRequest(AbstractModel):
    """BindRelateAcctUnionPay请求参数结构体

    """

    def __init__(self):
        r"""
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”（右侧）进行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，见证子账户的户名（首次绑定的情况下，此字段即为待绑定的提现账户的户名。非首次绑定的情况下，须注意带绑定的提现账户的户名须与留存在后台系统的会员户名一致）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员的待绑定账户的账号（提现的银行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员的待绑定账户的本他行类型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员的待绑定账户的开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，会员的手机号（手机号须由长度为11位的数字构成）
        :type Mobile: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param CnapsBranchId: STRING(20)，会员的待绑定账户的开户行的联行号（本他行类型为他行的情况下，此字段和下一个字段至少一个不为空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员的待绑定账户的开户行的超级网银行号（本他行类型为他行的情况下，此字段和上一个字段至少一个不为空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.MrchCode = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRelateAcctUnionPayResponse(AbstractModel):
    """BindRelateAcctUnionPay返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReservedMsg: STRING(1027)，保留域（在同名子账户绑定的场景下，若返回"VERIFIED"则说明无需验证直接绑定成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class BusinessLicenseInfo(AbstractModel):
    """营业证件信息

    """

    def __init__(self):
        r"""
        :param BusinessLicenseType: 营业证件类型
 IDCARD：身份证
 CREDITCODE：统一社会信用代码
        :type BusinessLicenseType: str
        :param BusinessLicenseNumber: 营业证件号码 非个人商户上送统一社会信用代码，个人商户上送身份证号码
        :type BusinessLicenseNumber: str
        :param BusinessLicenseValidityType: 营业证件有效期类型 
LONGTERM：长期有效
OTHER：非长期有效
        :type BusinessLicenseValidityType: str
        :param BusinessLicenseEffectiveDate: 营业证件生效日期，yyyy-MM-dd
        :type BusinessLicenseEffectiveDate: str
        :param BusinessLicenseExpireDate: 营业证件失效日期，yyyy-MM-dd
        :type BusinessLicenseExpireDate: str
        """
        self.BusinessLicenseType = None
        self.BusinessLicenseNumber = None
        self.BusinessLicenseValidityType = None
        self.BusinessLicenseEffectiveDate = None
        self.BusinessLicenseExpireDate = None


    def _deserialize(self, params):
        self.BusinessLicenseType = params.get("BusinessLicenseType")
        self.BusinessLicenseNumber = params.get("BusinessLicenseNumber")
        self.BusinessLicenseValidityType = params.get("BusinessLicenseValidityType")
        self.BusinessLicenseEffectiveDate = params.get("BusinessLicenseEffectiveDate")
        self.BusinessLicenseExpireDate = params.get("BusinessLicenseExpireDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelContractInfo(AbstractModel):
    """米大师内部存放的合约信息

    """

    def __init__(self):
        r"""
        :param OutContractCode: 外部合约协议号
        :type OutContractCode: str
        :param ChannelContractCode: 米大师内部生成的合约协议号
        :type ChannelContractCode: str
        """
        self.OutContractCode = None
        self.ChannelContractCode = None


    def _deserialize(self, params):
        self.OutContractCode = params.get("OutContractCode")
        self.ChannelContractCode = params.get("ChannelContractCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelReturnContractInfo(AbstractModel):
    """米大师内部生成的合约信息

    """

    def __init__(self):
        r"""
        :param ContractStatus: 平台合约状态
协议状态，枚举值：
CONTRACT_STATUS_SIGNED：已签约
CONTRACT_STATUS_TERMINATED：未签约
CONTRACT_STATUS_PENDING：签约进行中
        :type ContractStatus: str
        :param ChannelContractInfo: 米大师内部存放的合约信息
        :type ChannelContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ChannelContractInfo`
        """
        self.ContractStatus = None
        self.ChannelContractInfo = None


    def _deserialize(self, params):
        self.ContractStatus = params.get("ContractStatus")
        if params.get("ChannelContractInfo") is not None:
            self.ChannelContractInfo = ChannelContractInfo()
            self.ChannelContractInfo._deserialize(params.get("ChannelContractInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAcctRequest(AbstractModel):
    """CheckAcct请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param BindType: 1 – 小额转账验证
2 – 短信验证
每个结算账户每天只能使用一次小额转账验证
        :type BindType: int
        :param SettleAcctNo: 结算账户账号
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param CheckCode: 短信验证码或指令号
BindType==2必填，平安渠道必填
        :type CheckCode: str
        :param CurrencyType: 币种 RMB
BindType==1必填
        :type CurrencyType: str
        :param CurrencyUnit: 单位
1：元，2：角，3：分
BindType==1必填
        :type CurrencyUnit: int
        :param CurrencyAmt: 金额
BindType==1必填
        :type CurrencyAmt: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CheckCode = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CheckCode = params.get("CheckCode")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAcctResponse(AbstractModel):
    """CheckAcct返回参数结构体

    """

    def __init__(self):
        r"""
        :param FrontSeqNo: 前置流水号，请保存
        :type FrontSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.RequestId = params.get("RequestId")


class CheckAmountRequest(AbstractModel):
    """CheckAmount请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param TakeCashAcctNo: STRING(50)，会员的待绑定账户的账号（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户的账号”）
        :type TakeCashAcctNo: str
        :param AuthAmt: STRING(20)，鉴权验证金额（即 BindRelateAcctSmallAmount接口中的“会员的待绑定账户收到的验证金额。原小额转账鉴权方式为来账鉴权的情况下此字段须赋值为0.00）
        :type AuthAmt: str
        :param Ccy: STRING(3)，币种（默认为RMB）
        :type Ccy: str
        :param ReservedMsg: STRING(1027)，原小额转账方式（1: 往账鉴权，此为默认值; 2: 来账鉴权）
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.TakeCashAcctNo = None
        self.AuthAmt = None
        self.Ccy = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.AuthAmt = params.get("AuthAmt")
        self.Ccy = params.get("Ccy")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAmountResponse(AbstractModel):
    """CheckAmount返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class CityCodeResult(AbstractModel):
    """查询城市编码响应对象

    """

    def __init__(self):
        r"""
        :param CityId: 城市编码cityid，数字与字母的结合
注意：此字段可能返回 null，表示取不到有效值。
        :type CityId: str
        :param Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param District: 县区
注意：此字段可能返回 null，表示取不到有效值。
        :type District: str
        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        """
        self.CityId = None
        self.Province = None
        self.District = None
        self.City = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.Province = params.get("Province")
        self.District = params.get("District")
        self.City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearItem(AbstractModel):
    """银行在途清算结果信息

    """

    def __init__(self):
        r"""
        :param Date: STRING(8)，日期（格式: 20190101）
注意：此字段可能返回 null，表示取不到有效值。
        :type Date: str
        :param SubAcctType: STRING(40)，子账号类型（子帐号类型。1: 普通会员子账号; 2: 挂账子账号; 3: 手续费子账号; 4: 利息子账号; 5: 平台担保子账号; 7: 在途; 8: 理财购买子帐号; 9: 理财赎回子帐号; 10: 平台子拥有结算子帐号）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctType: str
        :param ReconcileStatus: STRING(3)，对账状态（0: 成功; 1: 失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReconcileStatus: str
        :param ReconcileReturnMsg: STRING(300)，对账返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReconcileReturnMsg: str
        :param ClearingStatus: STRING(20)，清算状态（0: 成功; 1: 失败; 2: 异常; 3: 待处理）
注意：此字段可能返回 null，表示取不到有效值。
        :type ClearingStatus: str
        :param ClearingReturnMsg: STRING(2)，清算返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClearingReturnMsg: str
        :param TotalAmt: STRING(300)，待清算总金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAmt: str
        """
        self.Date = None
        self.SubAcctType = None
        self.ReconcileStatus = None
        self.ReconcileReturnMsg = None
        self.ClearingStatus = None
        self.ClearingReturnMsg = None
        self.TotalAmt = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.SubAcctType = params.get("SubAcctType")
        self.ReconcileStatus = params.get("ReconcileStatus")
        self.ReconcileReturnMsg = params.get("ReconcileReturnMsg")
        self.ClearingStatus = params.get("ClearingStatus")
        self.ClearingReturnMsg = params.get("ClearingReturnMsg")
        self.TotalAmt = params.get("TotalAmt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCloudOrderRequest(AbstractModel):
    """CloseCloudOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 米大师分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户Id，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param OutTradeNo: 开发者订单号
        :type OutTradeNo: str
        :param MidasEnvironment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.OutTradeNo = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseCloudOrderResponse(AbstractModel):
    """CloseCloudOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CloseOpenBankPaymentOrderRequest(AbstractModel):
    """CloseOpenBankPaymentOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID，云企付平台下发给外部接入平台。
        :type ChannelMerchantId: str
        :param OutOrderId: 外部商户订单号，与ChannelOrderId不能同时为空
        :type OutOrderId: str
        :param ChannelOrderId: 云企付平台订单号，与OutOrderId不能同时为空
        :type ChannelOrderId: str
        :param Environment: 接入环境。沙箱环境填 sandbox。缺省默认调用生产环境
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.OutOrderId = None
        self.ChannelOrderId = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutOrderId = params.get("OutOrderId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseOpenBankPaymentOrderResponse(AbstractModel):
    """CloseOpenBankPaymentOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息
        :type ErrMessage: str
        :param Result: 关单响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CloseOpenBankPaymentOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CloseOpenBankPaymentOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CloseOpenBankPaymentOrderResult(AbstractModel):
    """云企付-关单响应

    """

    def __init__(self):
        r"""
        :param OutOrderId: 外部商户订单号
        :type OutOrderId: str
        :param ChannelOrderId: 云企付平台订单号
        :type ChannelOrderId: str
        :param OrderStatus: 订单状态。关单成功CLOSED
        :type OrderStatus: str
        """
        self.OutOrderId = None
        self.ChannelOrderId = None
        self.OrderStatus = None


    def _deserialize(self, params):
        self.OutOrderId = params.get("OutOrderId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.OrderStatus = params.get("OrderStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseOrderRequest(AbstractModel):
    """CloseOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param OutTradeNo: 业务订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫订单号，OutTradeNo ， TransactionId二选一，不能都为空,优先使用 OutTradeNo
        :type TransactionId: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.TransactionId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseOrderResponse(AbstractModel):
    """CloseOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CloudAttachmentInfo(AbstractModel):
    """附加项信息对象

    """

    def __init__(self):
        r"""
        :param AttachmentAmount: 附加项金额。
附加项的金额（必须是正数，单位：分），代表积分的数量、抵扣的金额、溢价的金额、补贴的金额
        :type AttachmentAmount: int
        :param AttachmentType: 附加项类型。
Add：加项；
Sub：减项；
Point：积分项；
Subsidy：补贴项。
        :type AttachmentType: str
        :param AttachmentName: 附加项名称。
当银行作为收单机构可能会对该字段有要求，请向米大师确认。
        :type AttachmentName: str
        :param AttachmentCode: 附加项编号。
当银行作为收单机构可能会对该字段有要求，请向米大师确认。
        :type AttachmentCode: str
        """
        self.AttachmentAmount = None
        self.AttachmentType = None
        self.AttachmentName = None
        self.AttachmentCode = None


    def _deserialize(self, params):
        self.AttachmentAmount = params.get("AttachmentAmount")
        self.AttachmentType = params.get("AttachmentType")
        self.AttachmentName = params.get("AttachmentName")
        self.AttachmentCode = params.get("AttachmentCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudChannelExternalUserInfo(AbstractModel):
    """渠道方用户信息

    """

    def __init__(self):
        r"""
        :param ChannelExternalUserType: 渠道方用户类型，枚举值:
WX_OPENID 微信支付类型
ALIPAY_BUYERID 支付宝支付类型
        :type ChannelExternalUserType: str
        :param ChannelExternalUserId: 渠道方用户Id
        :type ChannelExternalUserId: str
        """
        self.ChannelExternalUserType = None
        self.ChannelExternalUserId = None


    def _deserialize(self, params):
        self.ChannelExternalUserType = params.get("ChannelExternalUserType")
        self.ChannelExternalUserId = params.get("ChannelExternalUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudClientInfo(AbstractModel):
    """客户端信息

    """

    def __init__(self):
        r"""
        :param ClientType: 场景类型。
wechat_ecommerce渠道 - h5支付方式，此字段必填；
枚举值：
CLIENT_TYPE_UNKNOWN 未知;
CLIENT_TYPE_IOS ios系统;
CLIENT_TYPE_ANDROID 安卓系统;
CLIENT_TYPE_WAP WAP场景;
CLIENT_TYPE_H5 H5场景;
        :type ClientType: str
        :param AppName: 应用名称。
        :type AppName: str
        :param AppUrl: 网站URL。
        :type AppUrl: str
        :param BundleId: IOS平台BundleID。
        :type BundleId: str
        :param PackageName: Android平台PackageName
        :type PackageName: str
        """
        self.ClientType = None
        self.AppName = None
        self.AppUrl = None
        self.BundleId = None
        self.PackageName = None


    def _deserialize(self, params):
        self.ClientType = params.get("ClientType")
        self.AppName = params.get("AppName")
        self.AppUrl = params.get("AppUrl")
        self.BundleId = params.get("BundleId")
        self.PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudExternalChannelData(AbstractModel):
    """第三方渠道数据信息

    """

    def __init__(self):
        r"""
        :param ExternalChannelDataName: 第三方渠道数据名。
PAYMENT_ORDER_EXTERNAL_REQUEST_DATA: 支付下单请求数据
PAYMENT_ORDER_EXTERNAL_RETURN_DATA: 支付下单返回数据
PAYMENT_ORDER_EXTERNAL_NOTIFY_DATA: 支付通知数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalChannelDataName: str
        :param ExternalChannelDataValue: 第三方渠道数据值。
当ExternalChannelDataType=PAYMENT时，反序列化格式请参考[ExternalChannelPaymentDataValue](https://dev.tke.midas.qq.com/juxin-doc-next/apidocs/external-channel-data/QueryExternalChannelData.html#externalchannelpaymentdatavalue)
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalChannelDataValue: str
        """
        self.ExternalChannelDataName = None
        self.ExternalChannelDataValue = None


    def _deserialize(self, params):
        self.ExternalChannelDataName = params.get("ExternalChannelDataName")
        self.ExternalChannelDataValue = params.get("ExternalChannelDataValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudExternalPromptGroup(AbstractModel):
    """渠道扩展促销信息

    """

    def __init__(self):
        r"""
        :param ChannelName: 渠道名。
为米大师定义的枚举值：
wechat 微信渠道
        :type ChannelName: str
        :param ExternalPromptInfoList: 渠道扩展促销信息列表，由各个渠道自行定义。
ChannelName为wechat时，组成为 <Wechat-ExternalPromptInfo>
        :type ExternalPromptInfoList: list of CloudExternalPromptInfo
        """
        self.ChannelName = None
        self.ExternalPromptInfoList = None


    def _deserialize(self, params):
        self.ChannelName = params.get("ChannelName")
        if params.get("ExternalPromptInfoList") is not None:
            self.ExternalPromptInfoList = []
            for item in params.get("ExternalPromptInfoList"):
                obj = CloudExternalPromptInfo()
                obj._deserialize(item)
                self.ExternalPromptInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudExternalPromptInfo(AbstractModel):
    """渠道扩展促销信息

    """

    def __init__(self):
        r"""
        :param ExternalPromptType: 优惠商品信息类型。
        :type ExternalPromptType: str
        :param ExternalPromptValue: 优惠商品信息数据。
        :type ExternalPromptValue: str
        :param ExternalPromptName: 优惠商品名称。
        :type ExternalPromptName: str
        """
        self.ExternalPromptType = None
        self.ExternalPromptValue = None
        self.ExternalPromptName = None


    def _deserialize(self, params):
        self.ExternalPromptType = params.get("ExternalPromptType")
        self.ExternalPromptValue = params.get("ExternalPromptValue")
        self.ExternalPromptName = params.get("ExternalPromptName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudGlobalPayTimeInfo(AbstractModel):
    """全局支付时间信息

    """

    def __init__(self):
        r"""
        :param StartTimestamp: 订单开始时间。
不指定时默认为当前时间。
        :type StartTimestamp: int
        :param ExpireTimestamp: 订单结束时间。
逾期将会拒绝下单。不指定时默认为当前时间的7天后结束。
        :type ExpireTimestamp: int
        :param TimeOffset: 时区。
不指定时默认为28800，表示北京时间（东八区）。
        :type TimeOffset: int
        """
        self.StartTimestamp = None
        self.ExpireTimestamp = None
        self.TimeOffset = None


    def _deserialize(self, params):
        self.StartTimestamp = params.get("StartTimestamp")
        self.ExpireTimestamp = params.get("ExpireTimestamp")
        self.TimeOffset = params.get("TimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudOrderReturn(AbstractModel):
    """返回订单信息

    """

    def __init__(self):
        r"""
        :param AppId: 米大师分配的支付主MidasAppId
        :type AppId: str
        :param OutTradeNo: 开发者支付订单号
        :type OutTradeNo: str
        :param SubOrderList: 调用下单接口传进来的子单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubOrderList: list of CloudSubOrderReturn
        :param TransactionId: 调用下单接口获取的米大师交易订单号
        :type TransactionId: str
        :param UserId: 用户Id
        :type UserId: str
        :param Channel: 支付渠道
wechat:微信支付
        :type Channel: str
        :param ProductId: 物品Id
        :type ProductId: str
        :param Metadata: 发货标识，由开发者在调用下单接口的时候传入
        :type Metadata: str
        :param CurrencyType: ISO货币代码
        :type CurrencyType: str
        :param Amt: 支付金额，单位：分
        :type Amt: int
        :param OrderState: 订单状态
0:初始状态，获取米大师交易订单成功
1:拉起米大师支付页面成功，用户未支付
2:用户支付成功，正在发货
3:用户支付成功，发货失败
4:用户支付成功，发货成功
5:关单中
6:已关单
        :type OrderState: str
        :param OrderTime: 下单时间，unix时间戳
        :type OrderTime: str
        :param PayTime: 支付时间，unix时间戳
        :type PayTime: str
        :param CallBackTime: 支付回调时间，unix时间戳
        :type CallBackTime: str
        :param ChannelExternalOrderId: 支付机构订单号
        :type ChannelExternalOrderId: str
        :param ChannelOrderId: 米大师内部渠道订单号
        :type ChannelOrderId: str
        :param RefundFlag: 是否曾退款
        :type RefundFlag: str
        :param CashAmt: 用户支付金额
        :type CashAmt: str
        :param CouponAmt: 抵扣券金额
        :type CouponAmt: str
        :param ProductName: 商品名称
        :type ProductName: str
        :param SettleInfo: 结算信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SettleInfo: :class:`tencentcloud.cpdp.v20190820.models.CloudSettleInfo`
        :param AttachmentInfoList: 附加项信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachmentInfoList: list of CloudAttachmentInfo
        :param ChannelExternalUserInfoList: 渠道方返回的用户信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelExternalUserInfoList: list of CloudChannelExternalUserInfo
        :param ExternalReturnPromptGroupList: 渠道扩展促销列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnPromptGroupList: list of CloudExternalPromptGroup
        :param SceneInfo: 场景扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneInfo: str
        """
        self.AppId = None
        self.OutTradeNo = None
        self.SubOrderList = None
        self.TransactionId = None
        self.UserId = None
        self.Channel = None
        self.ProductId = None
        self.Metadata = None
        self.CurrencyType = None
        self.Amt = None
        self.OrderState = None
        self.OrderTime = None
        self.PayTime = None
        self.CallBackTime = None
        self.ChannelExternalOrderId = None
        self.ChannelOrderId = None
        self.RefundFlag = None
        self.CashAmt = None
        self.CouponAmt = None
        self.ProductName = None
        self.SettleInfo = None
        self.AttachmentInfoList = None
        self.ChannelExternalUserInfoList = None
        self.ExternalReturnPromptGroupList = None
        self.SceneInfo = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.OutTradeNo = params.get("OutTradeNo")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = CloudSubOrderReturn()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.TransactionId = params.get("TransactionId")
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.ProductId = params.get("ProductId")
        self.Metadata = params.get("Metadata")
        self.CurrencyType = params.get("CurrencyType")
        self.Amt = params.get("Amt")
        self.OrderState = params.get("OrderState")
        self.OrderTime = params.get("OrderTime")
        self.PayTime = params.get("PayTime")
        self.CallBackTime = params.get("CallBackTime")
        self.ChannelExternalOrderId = params.get("ChannelExternalOrderId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.RefundFlag = params.get("RefundFlag")
        self.CashAmt = params.get("CashAmt")
        self.CouponAmt = params.get("CouponAmt")
        self.ProductName = params.get("ProductName")
        if params.get("SettleInfo") is not None:
            self.SettleInfo = CloudSettleInfo()
            self.SettleInfo._deserialize(params.get("SettleInfo"))
        if params.get("AttachmentInfoList") is not None:
            self.AttachmentInfoList = []
            for item in params.get("AttachmentInfoList"):
                obj = CloudAttachmentInfo()
                obj._deserialize(item)
                self.AttachmentInfoList.append(obj)
        if params.get("ChannelExternalUserInfoList") is not None:
            self.ChannelExternalUserInfoList = []
            for item in params.get("ChannelExternalUserInfoList"):
                obj = CloudChannelExternalUserInfo()
                obj._deserialize(item)
                self.ChannelExternalUserInfoList.append(obj)
        if params.get("ExternalReturnPromptGroupList") is not None:
            self.ExternalReturnPromptGroupList = []
            for item in params.get("ExternalReturnPromptGroupList"):
                obj = CloudExternalPromptGroup()
                obj._deserialize(item)
                self.ExternalReturnPromptGroupList.append(obj)
        self.SceneInfo = params.get("SceneInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSettleInfo(AbstractModel):
    """结算信息对象

    """

    def __init__(self):
        r"""
        :param NeedToBeConfirmed: 是否需要支付确认。
0: 不需要支付确认
1: 需要支付确认
传1时，需要在支付完成后成功调用了《支付确认》接口，该笔订单才会被清分出去
        :type NeedToBeConfirmed: int
        :param ProfitSharing: 是否指定分账。
0: 不指定分账
1: 指定分账
        :type ProfitSharing: int
        """
        self.NeedToBeConfirmed = None
        self.ProfitSharing = None


    def _deserialize(self, params):
        self.NeedToBeConfirmed = params.get("NeedToBeConfirmed")
        self.ProfitSharing = params.get("ProfitSharing")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStoreInfo(AbstractModel):
    """门店信息

    """

    def __init__(self):
        r"""
        :param StoreId: 门店ID。
        :type StoreId: str
        :param StoreName: 门店名称。
        :type StoreName: str
        :param StoreAddress: 门店地址。
        :type StoreAddress: str
        :param StoreAreaCode: 门店地区代码。
        :type StoreAreaCode: str
        :param StoreDeviceId: 设备ID。
wechat_ecommerce渠道 - h5支付方式，此字段必填。
        :type StoreDeviceId: str
        """
        self.StoreId = None
        self.StoreName = None
        self.StoreAddress = None
        self.StoreAreaCode = None
        self.StoreDeviceId = None


    def _deserialize(self, params):
        self.StoreId = params.get("StoreId")
        self.StoreName = params.get("StoreName")
        self.StoreAddress = params.get("StoreAddress")
        self.StoreAreaCode = params.get("StoreAreaCode")
        self.StoreDeviceId = params.get("StoreDeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSubOrder(AbstractModel):
    """子订单对象

    """

    def __init__(self):
        r"""
        :param SubOutTradeNo: 子订单号。
长度32个字符供参考，部分渠道存在长度更短的情况接入时请联系开发咨询。
        :type SubOutTradeNo: str
        :param SubAppId: 支付子商户ID。
米大师计费SubAppId，代表子商户。
        :type SubAppId: str
        :param ProductName: 商品名称。
业务自定义的子订单商品名称，无需URL编码，长度限制以具体所接入渠道为准。
        :type ProductName: str
        :param ProductDetail: 商品详情。
业务自定义的子订单商品详情，无需URL编码，长度限制以具体所接入渠道为准。
        :type ProductDetail: str
        :param PlatformIncome: 平台应收。
子订单平台应收金额，单位：分，需要注意的是Amt = PlatformIncome+SubMchIncome。
        :type PlatformIncome: int
        :param SubMchIncome: 商户应收。
子订单结算应收金额，单位：分，需要注意的是Amt = PlatformIncome+SubMchIncome。
        :type SubMchIncome: int
        :param Metadata: 透传字段。
发货标识，由开发者在调用米大师下单接口的 时候下发。
        :type Metadata: str
        :param Amt: 支付金额。
子订单支付金额，需要注意的是Amt = PlatformIncome+SubMchIncome。
        :type Amt: int
        :param OriginalAmt: 原始金额。
子订单原始金额，OriginalAmt>=Amt。
        :type OriginalAmt: int
        :param WxSubMchId: 微信子商户号。
        :type WxSubMchId: str
        :param SettleInfo: 结算信息。
例如是否需要分账、是否需要支付确认等。
        :type SettleInfo: :class:`tencentcloud.cpdp.v20190820.models.CloudSettleInfo`
        :param AttachmentInfoList: 附加项信息列表。
例如溢价信息、抵扣信息、积分信息、补贴信息
通过该字段可以实现渠道方的优惠抵扣补贴等营销功能。
        :type AttachmentInfoList: list of CloudAttachmentInfo
        """
        self.SubOutTradeNo = None
        self.SubAppId = None
        self.ProductName = None
        self.ProductDetail = None
        self.PlatformIncome = None
        self.SubMchIncome = None
        self.Metadata = None
        self.Amt = None
        self.OriginalAmt = None
        self.WxSubMchId = None
        self.SettleInfo = None
        self.AttachmentInfoList = None


    def _deserialize(self, params):
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubAppId = params.get("SubAppId")
        self.ProductName = params.get("ProductName")
        self.ProductDetail = params.get("ProductDetail")
        self.PlatformIncome = params.get("PlatformIncome")
        self.SubMchIncome = params.get("SubMchIncome")
        self.Metadata = params.get("Metadata")
        self.Amt = params.get("Amt")
        self.OriginalAmt = params.get("OriginalAmt")
        self.WxSubMchId = params.get("WxSubMchId")
        if params.get("SettleInfo") is not None:
            self.SettleInfo = CloudSettleInfo()
            self.SettleInfo._deserialize(params.get("SettleInfo"))
        if params.get("AttachmentInfoList") is not None:
            self.AttachmentInfoList = []
            for item in params.get("AttachmentInfoList"):
                obj = CloudAttachmentInfo()
                obj._deserialize(item)
                self.AttachmentInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSubOrderRefund(AbstractModel):
    """退款子单

    """

    def __init__(self):
        r"""
        :param RefundAmt: 子订单退款金额
        :type RefundAmt: int
        :param PlatformRefundAmt: 平台应退金额
        :type PlatformRefundAmt: int
        :param SubMchRefundAmt: 商家应退金额
        :type SubMchRefundAmt: int
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param SubRefundId: 子退款单号，调用方需要保证全局唯一性
        :type SubRefundId: str
        """
        self.RefundAmt = None
        self.PlatformRefundAmt = None
        self.SubMchRefundAmt = None
        self.SubOutTradeNo = None
        self.SubRefundId = None


    def _deserialize(self, params):
        self.RefundAmt = params.get("RefundAmt")
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        self.SubMchRefundAmt = params.get("SubMchRefundAmt")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubRefundId = params.get("SubRefundId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSubOrderReturn(AbstractModel):
    """子订单详情

    """

    def __init__(self):
        r"""
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param SubAppId: 米大师计费SubAppId，代表子商户
        :type SubAppId: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param SubMchIncome: 子订单结算应收金额，单位：分
        :type SubMchIncome: int
        :param Amt: 子订单支付金额
        :type Amt: int
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        :param SettleCheck: 核销状态，1表示核销，0表示未核销
        :type SettleCheck: int
        :param SettleInfo: 结算信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SettleInfo: :class:`tencentcloud.cpdp.v20190820.models.CloudSettleInfo`
        :param Metadata: 透传字段，由开发者在调用米大师下单接口的时候下发
        :type Metadata: str
        :param AttachmentInfoList: 附加项信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachmentInfoList: :class:`tencentcloud.cpdp.v20190820.models.CloudAttachmentInfo`
        :param ChannelExternalSubOrderId: 渠道方应答的订单号，透传处理
        :type ChannelExternalSubOrderId: str
        :param WxSubMchId: 微信子商户号
        :type WxSubMchId: str
        """
        self.SubOutTradeNo = None
        self.SubAppId = None
        self.ProductName = None
        self.ProductDetail = None
        self.PlatformIncome = None
        self.SubMchIncome = None
        self.Amt = None
        self.OriginalAmt = None
        self.SettleCheck = None
        self.SettleInfo = None
        self.Metadata = None
        self.AttachmentInfoList = None
        self.ChannelExternalSubOrderId = None
        self.WxSubMchId = None


    def _deserialize(self, params):
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubAppId = params.get("SubAppId")
        self.ProductName = params.get("ProductName")
        self.ProductDetail = params.get("ProductDetail")
        self.PlatformIncome = params.get("PlatformIncome")
        self.SubMchIncome = params.get("SubMchIncome")
        self.Amt = params.get("Amt")
        self.OriginalAmt = params.get("OriginalAmt")
        self.SettleCheck = params.get("SettleCheck")
        if params.get("SettleInfo") is not None:
            self.SettleInfo = CloudSettleInfo()
            self.SettleInfo._deserialize(params.get("SettleInfo"))
        self.Metadata = params.get("Metadata")
        if params.get("AttachmentInfoList") is not None:
            self.AttachmentInfoList = CloudAttachmentInfo()
            self.AttachmentInfoList._deserialize(params.get("AttachmentInfoList"))
        self.ChannelExternalSubOrderId = params.get("ChannelExternalSubOrderId")
        self.WxSubMchId = params.get("WxSubMchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSubRefundItem(AbstractModel):
    """子单退款信息

    """

    def __init__(self):
        r"""
        :param ChannelExternalRefundId: 渠道方应答的退款ID，透传处理
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelExternalRefundId: str
        :param ChannelExternalOrderId: 渠道方应答的订单号，透传处理
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelExternalOrderId: str
        :param RefundAmt: 子单退款金额
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundAmt: int
        :param SubOutTradeNo: 子单订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubOutTradeNo: str
        :param SubRefundId: 子单退款id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubRefundId: str
        :param SubAppId: 子应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAppId: str
        :param ChannelSubOrderId: 渠道子单支付订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelSubOrderId: str
        :param ChannelSubRefundId: 渠道子退款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelSubRefundId: str
        """
        self.ChannelExternalRefundId = None
        self.ChannelExternalOrderId = None
        self.RefundAmt = None
        self.SubOutTradeNo = None
        self.SubRefundId = None
        self.SubAppId = None
        self.ChannelSubOrderId = None
        self.ChannelSubRefundId = None


    def _deserialize(self, params):
        self.ChannelExternalRefundId = params.get("ChannelExternalRefundId")
        self.ChannelExternalOrderId = params.get("ChannelExternalOrderId")
        self.RefundAmt = params.get("RefundAmt")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubRefundId = params.get("SubRefundId")
        self.SubAppId = params.get("SubAppId")
        self.ChannelSubOrderId = params.get("ChannelSubOrderId")
        self.ChannelSubRefundId = params.get("ChannelSubRefundId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmOrderRequest(AbstractModel):
    """ConfirmOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 分配给商户的AppId
        :type MerchantAppId: str
        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。
        :type OrderNo: str
        """
        self.MerchantAppId = None
        self.OrderNo = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfirmOrderResponse(AbstractModel):
    """ConfirmOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 分配给商户的AppId
        :type MerchantAppId: str
        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。
        :type OrderNo: str
        :param Status: 订单确认状态。0-确认失败
1-确认成功 
2-可疑状态
        :type Status: str
        :param Description: 订单确认状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantAppId = None
        self.OrderNo = None
        self.Status = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class ContractInfo(AbstractModel):
    """合约信息

    """

    def __init__(self):
        r"""
        :param ChannelContractMerchantId: 米大师内部签约商户号
        :type ChannelContractMerchantId: str
        :param ChannelContractSubMerchantId: 米大师内部签约子商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelContractSubMerchantId: str
        :param ChannelContractAppId: 米大师内部签约应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelContractAppId: str
        :param ChannelContractSubAppId: 米大师内部签约子应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelContractSubAppId: str
        :param OutContractCode: 业务合约协议号
        :type OutContractCode: str
        :param ExternalContractUserInfoList: 第三方渠道用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalContractUserInfoList: list of ExternalContractUserInfo
        :param ContractMethod: 签约方式，如 wechat_app ，使用app方式下的微信签
        :type ContractMethod: str
        :param ContractSceneId: 合约场景id
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractSceneId: str
        :param UserInfo: 用户信息
        :type UserInfo: :class:`tencentcloud.cpdp.v20190820.models.ContractUserInfo`
        :param ExternalContractData: 第三方渠道签约数据
        :type ExternalContractData: str
        """
        self.ChannelContractMerchantId = None
        self.ChannelContractSubMerchantId = None
        self.ChannelContractAppId = None
        self.ChannelContractSubAppId = None
        self.OutContractCode = None
        self.ExternalContractUserInfoList = None
        self.ContractMethod = None
        self.ContractSceneId = None
        self.UserInfo = None
        self.ExternalContractData = None


    def _deserialize(self, params):
        self.ChannelContractMerchantId = params.get("ChannelContractMerchantId")
        self.ChannelContractSubMerchantId = params.get("ChannelContractSubMerchantId")
        self.ChannelContractAppId = params.get("ChannelContractAppId")
        self.ChannelContractSubAppId = params.get("ChannelContractSubAppId")
        self.OutContractCode = params.get("OutContractCode")
        if params.get("ExternalContractUserInfoList") is not None:
            self.ExternalContractUserInfoList = []
            for item in params.get("ExternalContractUserInfoList"):
                obj = ExternalContractUserInfo()
                obj._deserialize(item)
                self.ExternalContractUserInfoList.append(obj)
        self.ContractMethod = params.get("ContractMethod")
        self.ContractSceneId = params.get("ContractSceneId")
        if params.get("UserInfo") is not None:
            self.UserInfo = ContractUserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.ExternalContractData = params.get("ExternalContractData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractOrderInSubOrder(AbstractModel):
    """支付中签约子订单列表

    """

    def __init__(self):
        r"""
        :param SubMchIncome: 子订单结算应收金额，单位： 分
        :type SubMchIncome: int
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param Amt: 子订单支付金额
        :type Amt: int
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        :param Metadata: 发货标识，由业务在调用聚鑫下单接口的 时候下发
        :type Metadata: str
        """
        self.SubMchIncome = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SubAppId = None
        self.SubOutTradeNo = None
        self.Amt = None
        self.OriginalAmt = None
        self.Metadata = None


    def _deserialize(self, params):
        self.SubMchIncome = params.get("SubMchIncome")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.Amt = params.get("Amt")
        self.OriginalAmt = params.get("OriginalAmt")
        self.Metadata = params.get("Metadata")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractOrderRequest(AbstractModel):
    """ContractOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param CurrencyType: ISO 货币代码，CNY
        :type CurrencyType: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param OutTradeNo: 支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type OutTradeNo: str
        :param ProductDetail: 商品详情，需要URL编码
        :type ProductDetail: str
        :param ProductId: 商品ID，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type ProductId: str
        :param ProductName: 商品名称，需要URL编码
        :type ProductName: str
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param RealChannel: 银行真实渠道.如:bank_pingan
        :type RealChannel: str
        :param OriginalAmt: 原始金额
        :type OriginalAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param ContractNotifyUrl: 签约通知地址
        :type ContractNotifyUrl: str
        :param CallbackUrl: Web端回调地址
        :type CallbackUrl: str
        :param Channel: 指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定
        :type Channel: str
        :param Metadata: 透传字段，支付成功回调透传给应用，用于业务透传自定义内容
        :type Metadata: str
        :param Quantity: 购买数量，不传默认为1
        :type Quantity: int
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOrderList: 子订单信息列表，格式：子订单号、子应用ID、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)
注：接入银行或其他支付渠道服务商模式下，必传
        :type SubOrderList: list of ContractOrderInSubOrder
        :param TotalMchIncome: 结算应收金额，单位：分
        :type TotalMchIncome: int
        :param TotalPlatformIncome: 平台应收金额，单位：分
        :type TotalPlatformIncome: int
        :param WxOpenId: 微信公众号/小程序支付时为必选，需要传微信下的openid
        :type WxOpenId: str
        :param WxSubOpenId: 在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一
        :type WxSubOpenId: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param WxAppId: 微信商户应用ID
        :type WxAppId: str
        :param WxSubAppId: 微信商户子应用ID
        :type WxSubAppId: str
        :param PaymentNotifyUrl: 支付通知地址
        :type PaymentNotifyUrl: str
        :param ContractSceneId: 传入调用方在Midas注册签约信息时获得的ContractSceneId。若未在Midas注册签约信息，则传入ExternalContractData。注意：ContractSceneId与ExternalContractData必须二选一传入其中一个
        :type ContractSceneId: str
        :param ExternalContractData: 需要按照各个渠道的扩展签约信息规范组装好该字段。若未在Midas注册签约信息，则传入该字段。注意：ContractSceneId与ExternalContractData必须二选一传入其中一个
        :type ExternalContractData: str
        :param OutContractCode: 外部签约协议号，唯一标记一个签约关系。仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type OutContractCode: str
        :param AttachData: 透传给第三方渠道的附加数据
        :type AttachData: str
        :param ContractDisplayName: 展示用的签约用户名称，若不传入时，默认取UserId
        :type ContractDisplayName: str
        """
        self.CurrencyType = None
        self.MidasAppId = None
        self.OutTradeNo = None
        self.ProductDetail = None
        self.ProductId = None
        self.ProductName = None
        self.TotalAmt = None
        self.UserId = None
        self.RealChannel = None
        self.OriginalAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.ContractNotifyUrl = None
        self.CallbackUrl = None
        self.Channel = None
        self.Metadata = None
        self.Quantity = None
        self.SubAppId = None
        self.SubOrderList = None
        self.TotalMchIncome = None
        self.TotalPlatformIncome = None
        self.WxOpenId = None
        self.WxSubOpenId = None
        self.MidasEnvironment = None
        self.WxAppId = None
        self.WxSubAppId = None
        self.PaymentNotifyUrl = None
        self.ContractSceneId = None
        self.ExternalContractData = None
        self.OutContractCode = None
        self.AttachData = None
        self.ContractDisplayName = None


    def _deserialize(self, params):
        self.CurrencyType = params.get("CurrencyType")
        self.MidasAppId = params.get("MidasAppId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.TotalAmt = params.get("TotalAmt")
        self.UserId = params.get("UserId")
        self.RealChannel = params.get("RealChannel")
        self.OriginalAmt = params.get("OriginalAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.ContractNotifyUrl = params.get("ContractNotifyUrl")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Channel = params.get("Channel")
        self.Metadata = params.get("Metadata")
        self.Quantity = params.get("Quantity")
        self.SubAppId = params.get("SubAppId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = ContractOrderInSubOrder()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.TotalMchIncome = params.get("TotalMchIncome")
        self.TotalPlatformIncome = params.get("TotalPlatformIncome")
        self.WxOpenId = params.get("WxOpenId")
        self.WxSubOpenId = params.get("WxSubOpenId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.WxAppId = params.get("WxAppId")
        self.WxSubAppId = params.get("WxSubAppId")
        self.PaymentNotifyUrl = params.get("PaymentNotifyUrl")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ExternalContractData = params.get("ExternalContractData")
        self.OutContractCode = params.get("OutContractCode")
        self.AttachData = params.get("AttachData")
        self.ContractDisplayName = params.get("ContractDisplayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractOrderResponse(AbstractModel):
    """ContractOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param OutTradeNo: 应用支付订单号
        :type OutTradeNo: str
        :param PayInfo: 支付参数透传给聚鑫SDK（原文透传给SDK即可，不需要解码）
        :type PayInfo: str
        :param TransactionId: 聚鑫的交易订单号
        :type TransactionId: str
        :param OutContractCode: 外部签约协议号
        :type OutContractCode: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalAmt = None
        self.OutTradeNo = None
        self.PayInfo = None
        self.TransactionId = None
        self.OutContractCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAmt = params.get("TotalAmt")
        self.OutTradeNo = params.get("OutTradeNo")
        self.PayInfo = params.get("PayInfo")
        self.TransactionId = params.get("TransactionId")
        self.OutContractCode = params.get("OutContractCode")
        self.RequestId = params.get("RequestId")


class ContractPayListResult(AbstractModel):
    """合同-支付方式列表响应对象

    """

    def __init__(self):
        r"""
        :param PaymentId: 支付方式编号
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentId: str
        :param PaymentType: 支持的交易类型（多个以小写逗号分开，0现金，1刷卡，2主扫，3被扫，4JSPAY，5预授权）
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentType: str
        :param PaymentTag: 支付标签
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentTag: str
        :param PaymentIcon: 支付方式图片url路径
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentIcon: str
        :param PaymentName: 付款方式名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentName: str
        :param PaymentInternalName: 付款方式名称（内部名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentInternalName: str
        :param PaymentOptionOne: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionOne: str
        :param PaymentOptionTwo: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionTwo: str
        :param PaymentOptionThree: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionThree: str
        :param PaymentOptionFour: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionFour: str
        :param PaymentOptionFive: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionFive: str
        :param PaymentOptionSix: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionSix: str
        :param PaymentOptionSeven: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionSeven: str
        :param PaymentOptionOther: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionOther: str
        :param PaymentOptionNine: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionNine: str
        :param PaymentOptionTen: 支付方式
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionTen: str
        """
        self.PaymentId = None
        self.PaymentType = None
        self.PaymentTag = None
        self.PaymentIcon = None
        self.PaymentName = None
        self.PaymentInternalName = None
        self.PaymentOptionOne = None
        self.PaymentOptionTwo = None
        self.PaymentOptionThree = None
        self.PaymentOptionFour = None
        self.PaymentOptionFive = None
        self.PaymentOptionSix = None
        self.PaymentOptionSeven = None
        self.PaymentOptionOther = None
        self.PaymentOptionNine = None
        self.PaymentOptionTen = None


    def _deserialize(self, params):
        self.PaymentId = params.get("PaymentId")
        self.PaymentType = params.get("PaymentType")
        self.PaymentTag = params.get("PaymentTag")
        self.PaymentIcon = params.get("PaymentIcon")
        self.PaymentName = params.get("PaymentName")
        self.PaymentInternalName = params.get("PaymentInternalName")
        self.PaymentOptionOne = params.get("PaymentOptionOne")
        self.PaymentOptionTwo = params.get("PaymentOptionTwo")
        self.PaymentOptionThree = params.get("PaymentOptionThree")
        self.PaymentOptionFour = params.get("PaymentOptionFour")
        self.PaymentOptionFive = params.get("PaymentOptionFive")
        self.PaymentOptionSix = params.get("PaymentOptionSix")
        self.PaymentOptionSeven = params.get("PaymentOptionSeven")
        self.PaymentOptionOther = params.get("PaymentOptionOther")
        self.PaymentOptionNine = params.get("PaymentOptionNine")
        self.PaymentOptionTen = params.get("PaymentOptionTen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractSyncInfo(AbstractModel):
    """签约同步信息

    """

    def __init__(self):
        r"""
        :param ExternalReturnContractInfo: 第三方渠道合约信息
        :type ExternalReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ExternalReturnContractInfo`
        :param ExternalContractUserInfo: 第三方渠道用户信息
        :type ExternalContractUserInfo: list of ExternalContractUserInfo
        :param ContractMethod: 签约方式，枚举值，
<br/>CONTRACT_METHOD_WECHAT_INVALID: 无效
CONTRACT_METHOD_WECHAT_APP: 微信APP
CONTRACT_METHOD_WECHAT_PUBLIC: 微信公众号
CONTRACT_METHOD_WECHAT_MINIPROGRAM: 微信小程序
CONTRACT_METHOD_WECHAT_H5: 微信H5
        :type ContractMethod: str
        :param ContractSceneId: 在米大师侧分配的场景id
        :type ContractSceneId: str
        :param ExternalReturnContractData: 调用方从第三方渠道查询到的签约数据，由各个渠道定义
        :type ExternalReturnContractData: str
        """
        self.ExternalReturnContractInfo = None
        self.ExternalContractUserInfo = None
        self.ContractMethod = None
        self.ContractSceneId = None
        self.ExternalReturnContractData = None


    def _deserialize(self, params):
        if params.get("ExternalReturnContractInfo") is not None:
            self.ExternalReturnContractInfo = ExternalReturnContractInfo()
            self.ExternalReturnContractInfo._deserialize(params.get("ExternalReturnContractInfo"))
        if params.get("ExternalContractUserInfo") is not None:
            self.ExternalContractUserInfo = []
            for item in params.get("ExternalContractUserInfo"):
                obj = ExternalContractUserInfo()
                obj._deserialize(item)
                self.ExternalContractUserInfo.append(obj)
        self.ContractMethod = params.get("ContractMethod")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ExternalReturnContractData = params.get("ExternalReturnContractData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContractUserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param UserType: USER_ID: 用户ID
ANONYMOUS: 匿名类型用户ID
        :type UserType: str
        :param UserId: 用户类型
        :type UserId: str
        """
        self.UserType = None
        self.UserId = None


    def _deserialize(self, params):
        self.UserType = params.get("UserType")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcctRequest(AbstractModel):
    """CreateAcct请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId
        :type MidasAppId: str
        :param SubMchId: 业务平台的子商户ID，唯一
        :type SubMchId: str
        :param SubMchName: 子商户名称
        :type SubMchName: str
        :param Address: 子商户地址
        :type Address: str
        :param Contact: 子商户联系人
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type Contact: str
        :param Mobile: 联系人手机号
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type Mobile: str
        :param Email: 邮箱 
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type Email: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param SubMchType: 子商户类型：
个人: personal
企业: enterprise
个体工商户: individual
缺省: enterprise
        :type SubMchType: str
        :param ShortName: 不填则默认子商户名称
        :type ShortName: str
        :param SubMerchantMemberType: 子商户会员类型：
general: 普通子账户
merchant: 商户子账户
缺省: general
        :type SubMerchantMemberType: str
        :param SubMerchantKey: 子商户密钥
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SubMerchantKey: str
        :param SubMerchantPrivateKey: 子商户私钥
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SubMerchantPrivateKey: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param SubAcctNo: 银行生成的子商户账户，已开户的场景需要录入
        :type SubAcctNo: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param SubMerchantStoreName: 店铺名称
企业、个体工商户必输
        :type SubMerchantStoreName: str
        :param OrganizationInfo: 公司信息
        :type OrganizationInfo: :class:`tencentcloud.cpdp.v20190820.models.OrganizationInfo`
        """
        self.MidasAppId = None
        self.SubMchId = None
        self.SubMchName = None
        self.Address = None
        self.Contact = None
        self.Mobile = None
        self.Email = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.SubMchType = None
        self.ShortName = None
        self.SubMerchantMemberType = None
        self.SubMerchantKey = None
        self.SubMerchantPrivateKey = None
        self.EncryptType = None
        self.SubAcctNo = None
        self.MidasEnvironment = None
        self.SubMerchantStoreName = None
        self.OrganizationInfo = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.SubMchName = params.get("SubMchName")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.SubMchType = params.get("SubMchType")
        self.ShortName = params.get("ShortName")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")
        self.SubMerchantKey = params.get("SubMerchantKey")
        self.SubMerchantPrivateKey = params.get("SubMerchantPrivateKey")
        self.EncryptType = params.get("EncryptType")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.SubMerchantStoreName = params.get("SubMerchantStoreName")
        if params.get("OrganizationInfo") is not None:
            self.OrganizationInfo = OrganizationInfo()
            self.OrganizationInfo._deserialize(params.get("OrganizationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAcctResponse(AbstractModel):
    """CreateAcct返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubAcctNo: 银行生成的子商户账户
        :type SubAcctNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.SubAcctNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.RequestId = params.get("RequestId")


class CreateAgentTaxPaymentInfosRequest(AbstractModel):
    """CreateAgentTaxPaymentInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param AgentId: 代理商ID
        :type AgentId: str
        :param Channel: 平台渠道
        :type Channel: int
        :param Type: 类型。0-视同，1-个体工商户
        :type Type: int
        :param RawElectronicCertUrl: 源电子凭证下载地址
        :type RawElectronicCertUrl: str
        :param FileName: 文件名
        :type FileName: str
        :param AgentTaxPaymentInfos: 完税信息
        :type AgentTaxPaymentInfos: list of AgentTaxPayment
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.AgentId = None
        self.Channel = None
        self.Type = None
        self.RawElectronicCertUrl = None
        self.FileName = None
        self.AgentTaxPaymentInfos = None
        self.Profile = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.Channel = params.get("Channel")
        self.Type = params.get("Type")
        self.RawElectronicCertUrl = params.get("RawElectronicCertUrl")
        self.FileName = params.get("FileName")
        if params.get("AgentTaxPaymentInfos") is not None:
            self.AgentTaxPaymentInfos = []
            for item in params.get("AgentTaxPaymentInfos"):
                obj = AgentTaxPayment()
                obj._deserialize(item)
                self.AgentTaxPaymentInfos.append(obj)
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentTaxPaymentInfosResponse(AbstractModel):
    """CreateAgentTaxPaymentInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param AgentTaxPaymentBatch: 代理商完税证明批次信息
        :type AgentTaxPaymentBatch: :class:`tencentcloud.cpdp.v20190820.models.AgentTaxPaymentBatch`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AgentTaxPaymentBatch = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentTaxPaymentBatch") is not None:
            self.AgentTaxPaymentBatch = AgentTaxPaymentBatch()
            self.AgentTaxPaymentBatch._deserialize(params.get("AgentTaxPaymentBatch"))
        self.RequestId = params.get("RequestId")


class CreateAnchorRequest(AbstractModel):
    """CreateAnchor请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorUid: 主播业务ID，唯一
        :type AnchorUid: str
        :param AnchorName: 主播姓名
        :type AnchorName: str
        :param AnchorPhone: 主播电话
_敏感信息_ 使用 __AES128-CBC-PKCS#7__ 加密
        :type AnchorPhone: str
        :param AnchorEmail: 主播邮箱
_敏感信息_ 使用 __AES128-CBC-PKCS#7__ 加密
        :type AnchorEmail: str
        :param AnchorAddress: 主播地址
_敏感信息_ 使用 __AES128-CBC-PKCS#7__ 加密
        :type AnchorAddress: str
        :param AnchorIdNo: 主播身份证号
_敏感信息_ 使用 __AES128-CBC-PKCS#7__ 加密
        :type AnchorIdNo: str
        :param AnchorType: 主播类型
__KMusic__:全民K歌
__QMusic__:QQ音乐
__WeChat__:微信视频号
        :type AnchorType: str
        :param AnchorExtendInfo: 主播扩展信息
        :type AnchorExtendInfo: list of AnchorExtendInfo
        """
        self.AnchorUid = None
        self.AnchorName = None
        self.AnchorPhone = None
        self.AnchorEmail = None
        self.AnchorAddress = None
        self.AnchorIdNo = None
        self.AnchorType = None
        self.AnchorExtendInfo = None


    def _deserialize(self, params):
        self.AnchorUid = params.get("AnchorUid")
        self.AnchorName = params.get("AnchorName")
        self.AnchorPhone = params.get("AnchorPhone")
        self.AnchorEmail = params.get("AnchorEmail")
        self.AnchorAddress = params.get("AnchorAddress")
        self.AnchorIdNo = params.get("AnchorIdNo")
        self.AnchorType = params.get("AnchorType")
        if params.get("AnchorExtendInfo") is not None:
            self.AnchorExtendInfo = []
            for item in params.get("AnchorExtendInfo"):
                obj = AnchorExtendInfo()
                obj._deserialize(item)
                self.AnchorExtendInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnchorResponse(AbstractModel):
    """CreateAnchor返回参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播ID
        :type AnchorId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AnchorId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.RequestId = params.get("RequestId")


class CreateBatchPaymentBatchData(AbstractModel):
    """CreateBatchPayment接口BatchInfo对象

    """

    def __init__(self):
        r"""
        :param OrderId: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param TradeSerialNo: 交易流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeSerialNo: str
        :param Status: 交易状态。
0 处理中  
1 预占成功 
2 交易成功 
3 交易失败 
4 未知渠道异常 
5 预占额度失败
6 提交成功
7 提交失败
8 订单重复提交
99 未知系统异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param AgentId: 代理商ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param AgentName: 代理商名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        """
        self.OrderId = None
        self.TradeSerialNo = None
        self.Status = None
        self.StatusDesc = None
        self.AgentId = None
        self.AgentName = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchPaymentData(AbstractModel):
    """CreateBatchPayment接口返回响应

    """

    def __init__(self):
        r"""
        :param BatchId: 批次号
        :type BatchId: str
        :param BatchInfoList: 批次列表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchInfoList: list of CreateBatchPaymentBatchData
        """
        self.BatchId = None
        self.BatchInfoList = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        if params.get("BatchInfoList") is not None:
            self.BatchInfoList = []
            for item in params.get("BatchInfoList"):
                obj = CreateBatchPaymentBatchData()
                obj._deserialize(item)
                self.BatchInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchPaymentRecipient(AbstractModel):
    """CreateBatchPayment转账明细

    """

    def __init__(self):
        r"""
        :param TransferAmount: 转账金额
        :type TransferAmount: int
        :param OrderId: 订单号
        :type OrderId: str
        :param AnchorId: 主播ID（与主播业务ID不能同时为空，两者都填取主播ID）
        :type AnchorId: str
        :param Uid: 主播业务ID（与主播业务ID不能同时为空，两者都填取主播ID）
        :type Uid: str
        :param AnchorName: 主播名称。如果该字段填入，则会对AnchorName和AnchorId/Uid进行校验。
        :type AnchorName: str
        :param Remark: 业务备注
        :type Remark: str
        :param ReqReserved: 子单请求预留字段
        :type ReqReserved: str
        """
        self.TransferAmount = None
        self.OrderId = None
        self.AnchorId = None
        self.Uid = None
        self.AnchorName = None
        self.Remark = None
        self.ReqReserved = None


    def _deserialize(self, params):
        self.TransferAmount = params.get("TransferAmount")
        self.OrderId = params.get("OrderId")
        self.AnchorId = params.get("AnchorId")
        self.Uid = params.get("Uid")
        self.AnchorName = params.get("AnchorName")
        self.Remark = params.get("Remark")
        self.ReqReserved = params.get("ReqReserved")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchPaymentRequest(AbstractModel):
    """CreateBatchPayment请求参数结构体

    """

    def __init__(self):
        r"""
        :param TransferType: 1 微信企业付款 
2 支付宝转账 
3 平安银企直连代发转账
        :type TransferType: int
        :param RecipientList: 转账详情
        :type RecipientList: list of CreateBatchPaymentRecipient
        :param ReqReserved: 请求预留字段
        :type ReqReserved: str
        :param NotifyUrl: 回调Url
        :type NotifyUrl: str
        """
        self.TransferType = None
        self.RecipientList = None
        self.ReqReserved = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.TransferType = params.get("TransferType")
        if params.get("RecipientList") is not None:
            self.RecipientList = []
            for item in params.get("RecipientList"):
                obj = CreateBatchPaymentRecipient()
                obj._deserialize(item)
                self.RecipientList.append(obj)
        self.ReqReserved = params.get("ReqReserved")
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchPaymentResponse(AbstractModel):
    """CreateBatchPayment返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMessage: 响应消息。
        :type ErrMessage: str
        :param Result: 返回响应
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateBatchPaymentData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateBatchPaymentData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateCloudSubMerchantRequest(AbstractModel):
    """CreateCloudSubMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 米大师分配的支付主MidasAppId，根应用Id。
        :type MidasAppId: str
        :param ParentAppId: 父应用Id。
        :type ParentAppId: str
        :param SubMchName: 子商户名。
        :type SubMchName: str
        :param SubMchDescription: 子商户描述。
        :type SubMchDescription: str
        :param MidasEnvironment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type MidasEnvironment: str
        :param SubAppId: 子应用Id，为空则自动创建子应用id。
        :type SubAppId: str
        :param SubMchShortName: 子商户名缩写。
        :type SubMchShortName: str
        :param OutSubMerchantId: 业务平台自定义的子商户Id，唯一。
        :type OutSubMerchantId: str
        """
        self.MidasAppId = None
        self.ParentAppId = None
        self.SubMchName = None
        self.SubMchDescription = None
        self.MidasEnvironment = None
        self.SubAppId = None
        self.SubMchShortName = None
        self.OutSubMerchantId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.ParentAppId = params.get("ParentAppId")
        self.SubMchName = params.get("SubMchName")
        self.SubMchDescription = params.get("SubMchDescription")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.SubAppId = params.get("SubAppId")
        self.SubMchShortName = params.get("SubMchShortName")
        self.OutSubMerchantId = params.get("OutSubMerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudSubMerchantResponse(AbstractModel):
    """CreateCloudSubMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubAppId: 子应用Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAppId: str
        :param ChannelSubMerchantId: 渠道子商户Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelSubMerchantId: str
        :param Level: 层级，从0开始。
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.ChannelSubMerchantId = None
        self.Level = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.Level = params.get("Level")
        self.RequestId = params.get("RequestId")


class CreateCustAcctIdRequest(AbstractModel):
    """CreateCustAcctId请求参数结构体

    """

    def __init__(self):
        r"""
        :param FunctionFlag: STRING(2)，功能标志（1: 开户; 3: 销户）
        :type FunctionFlag: str
        :param FundSummaryAcctNo: STRING(50)，资金汇总账号（即收单资金归集入账的账号）
        :type FundSummaryAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（平台端的用户ID，需要保证唯一性，可数字字母混合，如HY_120）
        :type TranNetMemberCode: str
        :param MemberProperty: STRING(10)，会员属性（00-普通子账户(默认); SH-商户子账户）
        :type MemberProperty: str
        :param Mobile: STRING(30)，手机号码
        :type Mobile: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SelfBusiness: String(2)，是否为自营业务（0位非自营，1为自营）
        :type SelfBusiness: bool
        :param ContactName: String(64)，联系人
        :type ContactName: str
        :param SubAcctName: String(64)，子账户名称
        :type SubAcctName: str
        :param SubAcctShortName: String(64)，子账户简称
        :type SubAcctShortName: str
        :param SubAcctType: String(4)，子账户类型（0: 个人子账户; 1: 企业子账户）
        :type SubAcctType: int
        :param UserNickname: STRING(150)，用户昵称
        :type UserNickname: str
        :param Email: STRING(150)，邮箱
        :type Email: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.FunctionFlag = None
        self.FundSummaryAcctNo = None
        self.TranNetMemberCode = None
        self.MemberProperty = None
        self.Mobile = None
        self.MrchCode = None
        self.SelfBusiness = None
        self.ContactName = None
        self.SubAcctName = None
        self.SubAcctShortName = None
        self.SubAcctType = None
        self.UserNickname = None
        self.Email = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.FunctionFlag = params.get("FunctionFlag")
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberProperty = params.get("MemberProperty")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.SelfBusiness = params.get("SelfBusiness")
        self.ContactName = params.get("ContactName")
        self.SubAcctName = params.get("SubAcctName")
        self.SubAcctShortName = params.get("SubAcctShortName")
        self.SubAcctType = params.get("SubAcctType")
        self.UserNickname = params.get("UserNickname")
        self.Email = params.get("Email")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustAcctIdResponse(AbstractModel):
    """CreateCustAcctId返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubAcctNo: STRING(50)，见证子账户的账号（平台需要记录下来，后续所有接口交互都会用到）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域（需要开通智能收款，此处返回智能收款账号，正常情况下返回空）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class CreateExternalAccountBookResult(AbstractModel):
    """创建第三方电子记账本返回值

    """

    def __init__(self):
        r"""
        :param DealStatus: 处理状态。
__SUCCESS__: 成功
__FAILED__: 失败
__PROCESSING__: 进行中。
        :type DealStatus: str
        :param DealMessage: 处理返回描述，例如失败原因等
注意：此字段可能返回 null，表示取不到有效值。
        :type DealMessage: str
        :param ChannelAccountBookId: 渠道电子记账本ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelAccountBookId: str
        :param CollectMoneyAccountInfo: 电子记账本对外收款的账户信息。为JSON格式字符串（成功状态下返回）。详情见附录-复杂类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectMoneyAccountInfo: str
        """
        self.DealStatus = None
        self.DealMessage = None
        self.ChannelAccountBookId = None
        self.CollectMoneyAccountInfo = None


    def _deserialize(self, params):
        self.DealStatus = params.get("DealStatus")
        self.DealMessage = params.get("DealMessage")
        self.ChannelAccountBookId = params.get("ChannelAccountBookId")
        self.CollectMoneyAccountInfo = params.get("CollectMoneyAccountInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExternalAnchorData(AbstractModel):
    """CreateExternalAnchor接口返回参数

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播Id
        :type AnchorId: str
        """
        self.AnchorId = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExternalAnchorRequest(AbstractModel):
    """CreateExternalAnchor请求参数结构体

    """

    def __init__(self):
        r"""
        :param Uid: 平台业务系统唯一标示的主播id
        :type Uid: str
        :param Name: 主播名称
        :type Name: str
        :param IdNo: 身份证号
        :type IdNo: str
        :param IdCardFront: 身份证正面图片下载链接
        :type IdCardFront: str
        :param IdCardReverse: 身份证反面图片下载链接
        :type IdCardReverse: str
        :param AgentId: 指定分配的代理商ID
        :type AgentId: str
        """
        self.Uid = None
        self.Name = None
        self.IdNo = None
        self.IdCardFront = None
        self.IdCardReverse = None
        self.AgentId = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Name = params.get("Name")
        self.IdNo = params.get("IdNo")
        self.IdCardFront = params.get("IdCardFront")
        self.IdCardReverse = params.get("IdCardReverse")
        self.AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateExternalAnchorResponse(AbstractModel):
    """CreateExternalAnchor返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMessage: 响应消息。
        :type ErrMessage: str
        :param Result: 返回响应
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateExternalAnchorData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateExternalAnchorData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateFlexPayeeRequest(AbstractModel):
    """CreateFlexPayee请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutUserId: 用户外部业务ID
        :type OutUserId: str
        :param Name: 姓名
        :type Name: str
        :param IdNo: 证件号
        :type IdNo: str
        :param AccountName: 账户名称
        :type AccountName: str
        :param ServiceProviderId: 服务商ID
        :type ServiceProviderId: str
        :param TaxInfo: 计税信息
        :type TaxInfo: :class:`tencentcloud.cpdp.v20190820.models.PayeeTaxInfo`
        :param IdType: 证件类型
0:身份证
1:社会信用代码
        :type IdType: int
        :param Remark: 备注
        :type Remark: str
        """
        self.OutUserId = None
        self.Name = None
        self.IdNo = None
        self.AccountName = None
        self.ServiceProviderId = None
        self.TaxInfo = None
        self.IdType = None
        self.Remark = None


    def _deserialize(self, params):
        self.OutUserId = params.get("OutUserId")
        self.Name = params.get("Name")
        self.IdNo = params.get("IdNo")
        self.AccountName = params.get("AccountName")
        self.ServiceProviderId = params.get("ServiceProviderId")
        if params.get("TaxInfo") is not None:
            self.TaxInfo = PayeeTaxInfo()
            self.TaxInfo._deserialize(params.get("TaxInfo"))
        self.IdType = params.get("IdType")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlexPayeeResponse(AbstractModel):
    """CreateFlexPayee返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateFlexPayeeResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateFlexPayeeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateFlexPayeeResult(AbstractModel):
    """账户开立结果

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        """
        self.PayeeId = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceItem(AbstractModel):
    """发票开具明细

    """

    def __init__(self):
        r"""
        :param Name: 商品名称
        :type Name: str
        :param TaxCode: 税收商品编码
        :type TaxCode: str
        :param TotalPrice: 不含税商品总价（商品含税价总额/（1+税率））。InvoicePlatformId 为1时，该金额为含税总金额。单位为分。
        :type TotalPrice: int
        :param TaxRate: 商品税率
        :type TaxRate: int
        :param TaxAmount: 商品税额（不含税商品总价*税率）。单位为分
        :type TaxAmount: int
        :param TaxType: 税收商品类别
        :type TaxType: str
        :param Models: 商品规格
        :type Models: str
        :param Unit: 商品单位
        :type Unit: str
        :param Total: 商品数量
        :type Total: str
        :param Price: 不含税商品单价。InvoicePlatformId 为1时，该金额为含税单价。
        :type Price: str
        :param Discount: 含税折扣总额。单位为分
        :type Discount: int
        :param PreferentialPolicyFlag: 优惠政策标志。0：不使用优惠政策；1：使用优惠政策。
        :type PreferentialPolicyFlag: str
        :param ZeroTaxFlag: 零税率标识：
空：非零税率；
0：出口零税率；
1：免税；
2：不征税；
3：普通零税率。
        :type ZeroTaxFlag: str
        :param VatSpecialManagement: 增值税特殊管理。PreferentialPolicyFlag字段为1时，必填。目前仅支持5%(3%，2%，1.5%)简易征税、免税、不征税。
        :type VatSpecialManagement: str
        """
        self.Name = None
        self.TaxCode = None
        self.TotalPrice = None
        self.TaxRate = None
        self.TaxAmount = None
        self.TaxType = None
        self.Models = None
        self.Unit = None
        self.Total = None
        self.Price = None
        self.Discount = None
        self.PreferentialPolicyFlag = None
        self.ZeroTaxFlag = None
        self.VatSpecialManagement = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TaxCode = params.get("TaxCode")
        self.TotalPrice = params.get("TotalPrice")
        self.TaxRate = params.get("TaxRate")
        self.TaxAmount = params.get("TaxAmount")
        self.TaxType = params.get("TaxType")
        self.Models = params.get("Models")
        self.Unit = params.get("Unit")
        self.Total = params.get("Total")
        self.Price = params.get("Price")
        self.Discount = params.get("Discount")
        self.PreferentialPolicyFlag = params.get("PreferentialPolicyFlag")
        self.ZeroTaxFlag = params.get("ZeroTaxFlag")
        self.VatSpecialManagement = params.get("VatSpecialManagement")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceRequest(AbstractModel):
    """CreateInvoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID。0：高灯，1：票易通
        :type InvoicePlatformId: int
        :param TitleType: 抬头类型：1：个人/政府事业单位；2：企业
        :type TitleType: int
        :param BuyerTitle: 购方名称
        :type BuyerTitle: str
        :param OrderId: 业务开票号
        :type OrderId: str
        :param AmountHasTax: 含税总金额（单位为分）
        :type AmountHasTax: int
        :param TaxAmount: 总税额（单位为分）
        :type TaxAmount: int
        :param AmountWithoutTax: 不含税总金额（单位为分）。InvoicePlatformId 为1时，传默认值-1
        :type AmountWithoutTax: int
        :param SellerTaxpayerNum: 销方纳税人识别号
        :type SellerTaxpayerNum: str
        :param SellerName: 销方名称。（不填默认读取商户注册时输入的信息）
        :type SellerName: str
        :param SellerAddress: 销方地址。（不填默认读取商户注册时输入的信息）
        :type SellerAddress: str
        :param SellerPhone: 销方电话。（不填默认读取商户注册时输入的信息）
        :type SellerPhone: str
        :param SellerBankName: 销方银行名称。（不填默认读取商户注册时输入的信息）
        :type SellerBankName: str
        :param SellerBankAccount: 销方银行账号。（不填默认读取商户注册时输入的信息）
        :type SellerBankAccount: str
        :param BuyerTaxpayerNum: 购方纳税人识别号（购方票面信息）,若抬头类型为2时，必传
        :type BuyerTaxpayerNum: str
        :param BuyerAddress: 购方地址。开具专用发票时必填
        :type BuyerAddress: str
        :param BuyerBankName: 购方银行名称。开具专用发票时必填
        :type BuyerBankName: str
        :param BuyerBankAccount: 购方银行账号。开具专用发票时必填
        :type BuyerBankAccount: str
        :param BuyerPhone: 购方电话。开具专用发票时必填
        :type BuyerPhone: str
        :param BuyerEmail: 收票人邮箱。若填入，会收到发票推送邮件
        :type BuyerEmail: str
        :param TakerPhone: 收票人手机号。若填入，会收到发票推送短信
        :type TakerPhone: str
        :param InvoiceType: 开票类型：
1：增值税专用发票；
2：增值税普通发票；
3：增值税电子发票；
4：增值税卷式发票；
5：区块链电子发票。
若该字段不填，或值不为1-5，则认为开具”增值税电子发票”
        :type InvoiceType: int
        :param CallbackUrl: 发票结果回传地址
        :type CallbackUrl: str
        :param Drawer: 开票人姓名。（不填默认读取商户注册时输入的信息）
        :type Drawer: str
        :param Payee: 收款人姓名。（不填默认读取商户注册时输入的信息）
        :type Payee: str
        :param Checker: 复核人姓名。（不填默认读取商户注册时输入的信息）
        :type Checker: str
        :param TerminalCode: 税盘号
        :type TerminalCode: str
        :param LevyMethod: 征收方式。开具差额征税发票时必填2。开具普通征税发票时为空
        :type LevyMethod: str
        :param Deduction: 差额征税扣除额（单位为分）
        :type Deduction: int
        :param Remark: 备注（票面信息）
        :type Remark: str
        :param Items: 项目商品明细
        :type Items: list of CreateInvoiceItem
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        :param UndoPart: 撤销部分商品。0-不撤销，1-撤销
        :type UndoPart: int
        :param OrderDate: 订单下单时间（格式 YYYYMMDD）
        :type OrderDate: str
        :param Discount: 订单级别折扣（单位为分）
        :type Discount: int
        :param StoreNo: 门店编码
        :type StoreNo: str
        :param InvoiceChannel: 开票渠道。0：APP渠道，1：线下渠道，2：小程序渠道。不填默认为APP渠道
        :type InvoiceChannel: int
        """
        self.InvoicePlatformId = None
        self.TitleType = None
        self.BuyerTitle = None
        self.OrderId = None
        self.AmountHasTax = None
        self.TaxAmount = None
        self.AmountWithoutTax = None
        self.SellerTaxpayerNum = None
        self.SellerName = None
        self.SellerAddress = None
        self.SellerPhone = None
        self.SellerBankName = None
        self.SellerBankAccount = None
        self.BuyerTaxpayerNum = None
        self.BuyerAddress = None
        self.BuyerBankName = None
        self.BuyerBankAccount = None
        self.BuyerPhone = None
        self.BuyerEmail = None
        self.TakerPhone = None
        self.InvoiceType = None
        self.CallbackUrl = None
        self.Drawer = None
        self.Payee = None
        self.Checker = None
        self.TerminalCode = None
        self.LevyMethod = None
        self.Deduction = None
        self.Remark = None
        self.Items = None
        self.Profile = None
        self.UndoPart = None
        self.OrderDate = None
        self.Discount = None
        self.StoreNo = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TitleType = params.get("TitleType")
        self.BuyerTitle = params.get("BuyerTitle")
        self.OrderId = params.get("OrderId")
        self.AmountHasTax = params.get("AmountHasTax")
        self.TaxAmount = params.get("TaxAmount")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        self.SellerName = params.get("SellerName")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerPhone = params.get("SellerPhone")
        self.SellerBankName = params.get("SellerBankName")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.BuyerTaxpayerNum = params.get("BuyerTaxpayerNum")
        self.BuyerAddress = params.get("BuyerAddress")
        self.BuyerBankName = params.get("BuyerBankName")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.BuyerPhone = params.get("BuyerPhone")
        self.BuyerEmail = params.get("BuyerEmail")
        self.TakerPhone = params.get("TakerPhone")
        self.InvoiceType = params.get("InvoiceType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Drawer = params.get("Drawer")
        self.Payee = params.get("Payee")
        self.Checker = params.get("Checker")
        self.TerminalCode = params.get("TerminalCode")
        self.LevyMethod = params.get("LevyMethod")
        self.Deduction = params.get("Deduction")
        self.Remark = params.get("Remark")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CreateInvoiceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Profile = params.get("Profile")
        self.UndoPart = params.get("UndoPart")
        self.OrderDate = params.get("OrderDate")
        self.Discount = params.get("Discount")
        self.StoreNo = params.get("StoreNo")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceResponse(AbstractModel):
    """CreateInvoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 发票开具结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateInvoiceResult(AbstractModel):
    """发票结果

    """

    def __init__(self):
        r"""
        :param Message: 错误消息
        :type Message: str
        :param Code: 错误码
        :type Code: int
        :param Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResultData`
        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = CreateInvoiceResultData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceResultData(AbstractModel):
    """蓝票结果数据

    """

    def __init__(self):
        r"""
        :param State: 开票状态
        :type State: int
        :param InvoiceId: 发票ID
        :type InvoiceId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        """
        self.State = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceResultV2(AbstractModel):
    """发票结果V2

    """

    def __init__(self):
        r"""
        :param InvoiceId: 发票ID
        :type InvoiceId: str
        """
        self.InvoiceId = None


    def _deserialize(self, params):
        self.InvoiceId = params.get("InvoiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceV2Request(AbstractModel):
    """CreateInvoiceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID。0：高灯，1：票易通
        :type InvoicePlatformId: int
        :param TitleType: 抬头类型：1：个人/政府事业单位；2：企业
        :type TitleType: int
        :param BuyerTitle: 购方名称
        :type BuyerTitle: str
        :param OrderId: 业务开票号
        :type OrderId: str
        :param AmountHasTax: 含税总金额（单位为分）
        :type AmountHasTax: int
        :param TaxAmount: 总税额（单位为分）
        :type TaxAmount: int
        :param AmountWithoutTax: 不含税总金额（单位为分）。InvoicePlatformId 为1时，传默认值-1
        :type AmountWithoutTax: int
        :param SellerTaxpayerNum: 销方纳税人识别号
        :type SellerTaxpayerNum: str
        :param SellerName: 销方名称。（不填默认读取商户注册时输入的信息）
        :type SellerName: str
        :param SellerAddress: 销方地址。（不填默认读取商户注册时输入的信息）
        :type SellerAddress: str
        :param SellerPhone: 销方电话。（不填默认读取商户注册时输入的信息）
        :type SellerPhone: str
        :param SellerBankName: 销方银行名称。（不填默认读取商户注册时输入的信息）
        :type SellerBankName: str
        :param SellerBankAccount: 销方银行账号。（不填默认读取商户注册时输入的信息）
        :type SellerBankAccount: str
        :param BuyerTaxpayerNum: 购方纳税人识别号（购方票面信息）,若抬头类型为2时，必传
        :type BuyerTaxpayerNum: str
        :param BuyerAddress: 购方地址。开具专用发票时必填
        :type BuyerAddress: str
        :param BuyerBankName: 购方银行名称。开具专用发票时必填
        :type BuyerBankName: str
        :param BuyerBankAccount: 购方银行账号。开具专用发票时必填
        :type BuyerBankAccount: str
        :param BuyerPhone: 购方电话。开具专用发票时必填
        :type BuyerPhone: str
        :param BuyerEmail: 收票人邮箱。若填入，会收到发票推送邮件
        :type BuyerEmail: str
        :param TakerPhone: 收票人手机号。若填入，会收到发票推送短信
        :type TakerPhone: str
        :param InvoiceType: 开票类型：
1：增值税专用发票；
2：增值税普通发票；
3：增值税电子发票；
4：增值税卷式发票；
5：区块链电子发票。
若该字段不填，或值不为1-5，则认为开具”增值税电子发票”
        :type InvoiceType: int
        :param CallbackUrl: 发票结果回传地址
        :type CallbackUrl: str
        :param Drawer: 开票人姓名。（不填默认读取商户注册时输入的信息）
        :type Drawer: str
        :param Payee: 收款人姓名。（不填默认读取商户注册时输入的信息）
        :type Payee: str
        :param Checker: 复核人姓名。（不填默认读取商户注册时输入的信息）
        :type Checker: str
        :param TerminalCode: 税盘号
        :type TerminalCode: str
        :param LevyMethod: 征收方式。开具差额征税发票时必填2。开具普通征税发票时为空
        :type LevyMethod: str
        :param Deduction: 差额征税扣除额（单位为分）
        :type Deduction: int
        :param Remark: 备注（票面信息）
        :type Remark: str
        :param Items: 项目商品明细
        :type Items: list of CreateInvoiceItem
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        :param UndoPart: 撤销部分商品。0-不撤销，1-撤销
        :type UndoPart: int
        :param OrderDate: 订单下单时间（格式 YYYYMMDD）
        :type OrderDate: str
        :param Discount: 订单级别折扣（单位为分）
        :type Discount: int
        :param StoreNo: 门店编码
        :type StoreNo: str
        :param InvoiceChannel: 开票渠道。0：APP渠道，1：线下渠道，2：小程序渠道。不填默认为APP渠道
        :type InvoiceChannel: int
        """
        self.InvoicePlatformId = None
        self.TitleType = None
        self.BuyerTitle = None
        self.OrderId = None
        self.AmountHasTax = None
        self.TaxAmount = None
        self.AmountWithoutTax = None
        self.SellerTaxpayerNum = None
        self.SellerName = None
        self.SellerAddress = None
        self.SellerPhone = None
        self.SellerBankName = None
        self.SellerBankAccount = None
        self.BuyerTaxpayerNum = None
        self.BuyerAddress = None
        self.BuyerBankName = None
        self.BuyerBankAccount = None
        self.BuyerPhone = None
        self.BuyerEmail = None
        self.TakerPhone = None
        self.InvoiceType = None
        self.CallbackUrl = None
        self.Drawer = None
        self.Payee = None
        self.Checker = None
        self.TerminalCode = None
        self.LevyMethod = None
        self.Deduction = None
        self.Remark = None
        self.Items = None
        self.Profile = None
        self.UndoPart = None
        self.OrderDate = None
        self.Discount = None
        self.StoreNo = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TitleType = params.get("TitleType")
        self.BuyerTitle = params.get("BuyerTitle")
        self.OrderId = params.get("OrderId")
        self.AmountHasTax = params.get("AmountHasTax")
        self.TaxAmount = params.get("TaxAmount")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        self.SellerName = params.get("SellerName")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerPhone = params.get("SellerPhone")
        self.SellerBankName = params.get("SellerBankName")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.BuyerTaxpayerNum = params.get("BuyerTaxpayerNum")
        self.BuyerAddress = params.get("BuyerAddress")
        self.BuyerBankName = params.get("BuyerBankName")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.BuyerPhone = params.get("BuyerPhone")
        self.BuyerEmail = params.get("BuyerEmail")
        self.TakerPhone = params.get("TakerPhone")
        self.InvoiceType = params.get("InvoiceType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Drawer = params.get("Drawer")
        self.Payee = params.get("Payee")
        self.Checker = params.get("Checker")
        self.TerminalCode = params.get("TerminalCode")
        self.LevyMethod = params.get("LevyMethod")
        self.Deduction = params.get("Deduction")
        self.Remark = params.get("Remark")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CreateInvoiceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Profile = params.get("Profile")
        self.UndoPart = params.get("UndoPart")
        self.OrderDate = params.get("OrderDate")
        self.Discount = params.get("Discount")
        self.StoreNo = params.get("StoreNo")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvoiceV2Response(AbstractModel):
    """CreateInvoiceV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 发票开具结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResultV2`
        :param ErrCode: 错误码
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.ErrCode = None
        self.ErrMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInvoiceResultV2()
            self.Result._deserialize(params.get("Result"))
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.RequestId = params.get("RequestId")


class CreateMerchantRequest(AbstractModel):
    """CreateMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID
        :type InvoicePlatformId: int
        :param TaxpayerName: 企业名称
        :type TaxpayerName: str
        :param TaxpayerNum: 销方纳税人识别号
        :type TaxpayerNum: str
        :param LegalPersonName: 注册企业法定代表人名称
        :type LegalPersonName: str
        :param ContactsName: 联系人
        :type ContactsName: str
        :param Phone: 联系人手机号
        :type Phone: str
        :param Address: 不包含省市名称的地址
        :type Address: str
        :param RegionCode: 地区编码
        :type RegionCode: int
        :param CityName: 市（地区）名称
        :type CityName: str
        :param Drawer: 开票人
        :type Drawer: str
        :param TaxRegistrationCertificate: 税务登记证图片（Base64）字符串，需小于 3M
        :type TaxRegistrationCertificate: str
        :param Email: 联系人邮箱地址
        :type Email: str
        :param BusinessMobile: 企业电话
        :type BusinessMobile: str
        :param BankName: 银行名称
        :type BankName: str
        :param BankAccount: 银行账号
        :type BankAccount: str
        :param Reviewer: 复核人
        :type Reviewer: str
        :param Payee: 收款人
        :type Payee: str
        :param RegisterCode: 注册邀请码
        :type RegisterCode: str
        :param State: 不填默认为1，有效状态
0：表示无效；
1:表示有效；
2:表示禁止开蓝票；
3:表示禁止冲红。
        :type State: str
        :param CallbackUrl: 接收推送的消息地址
        :type CallbackUrl: str
        :param Profile: 接入环境。沙箱环境填 sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.TaxpayerName = None
        self.TaxpayerNum = None
        self.LegalPersonName = None
        self.ContactsName = None
        self.Phone = None
        self.Address = None
        self.RegionCode = None
        self.CityName = None
        self.Drawer = None
        self.TaxRegistrationCertificate = None
        self.Email = None
        self.BusinessMobile = None
        self.BankName = None
        self.BankAccount = None
        self.Reviewer = None
        self.Payee = None
        self.RegisterCode = None
        self.State = None
        self.CallbackUrl = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TaxpayerName = params.get("TaxpayerName")
        self.TaxpayerNum = params.get("TaxpayerNum")
        self.LegalPersonName = params.get("LegalPersonName")
        self.ContactsName = params.get("ContactsName")
        self.Phone = params.get("Phone")
        self.Address = params.get("Address")
        self.RegionCode = params.get("RegionCode")
        self.CityName = params.get("CityName")
        self.Drawer = params.get("Drawer")
        self.TaxRegistrationCertificate = params.get("TaxRegistrationCertificate")
        self.Email = params.get("Email")
        self.BusinessMobile = params.get("BusinessMobile")
        self.BankName = params.get("BankName")
        self.BankAccount = params.get("BankAccount")
        self.Reviewer = params.get("Reviewer")
        self.Payee = params.get("Payee")
        self.RegisterCode = params.get("RegisterCode")
        self.State = params.get("State")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMerchantResponse(AbstractModel):
    """CreateMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 商户注册结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateMerchantResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateMerchantResult(AbstractModel):
    """创建商户结果

    """

    def __init__(self):
        r"""
        :param Code: 状态码
        :type Code: int
        :param Message: 响应消息
        :type Message: str
        :param Data: 创建商户结果数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResultData`
        """
        self.Code = None
        self.Message = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Data") is not None:
            self.Data = CreateMerchantResultData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMerchantResultData(AbstractModel):
    """创建商户结果数据

    """

    def __init__(self):
        r"""
        :param TaxpayerName: 企业名称
        :type TaxpayerName: str
        :param SerialNo: 请求流水号
        :type SerialNo: str
        :param TaxpayerNum: 纳税号
        :type TaxpayerNum: str
        """
        self.TaxpayerName = None
        self.SerialNo = None
        self.TaxpayerNum = None


    def _deserialize(self, params):
        self.TaxpayerName = params.get("TaxpayerName")
        self.SerialNo = params.get("SerialNo")
        self.TaxpayerNum = params.get("TaxpayerNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankAggregatedSubMerchantRegistrationRequest(AbstractModel):
    """CreateOpenBankAggregatedSubMerchantRegistration请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutRegistrationNo: 外部进件序列号。
        :type OutRegistrationNo: str
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param OutSubMerchantId: 外部子商户ID。
        :type OutSubMerchantId: str
        :param ChannelName: 渠道名称。详见附录-云企付枚举类说明-ChannelName。
TENPAY: 商企付
WECHAT: 微信支付
ALIPAY: 支付宝
HELIPAY:合利宝
        :type ChannelName: str
        :param OutSubMerchantType: 外部子商户类型。
ENTERPRISE：企业商户 
INSTITUTION：事业单位商户 
INDIVIDUALBISS：个体工商户 
PERSON：个人商户(小微商户) 
SUBJECT_TYPE_OTHERS：其他组织
        :type OutSubMerchantType: str
        :param OutSubMerchantName: 外部子商户名称。
HELIPAY渠道(长度不能小于5大于150)。
        :type OutSubMerchantName: str
        :param LegalPersonInfo: 商户法人代表信息。
        :type LegalPersonInfo: :class:`tencentcloud.cpdp.v20190820.models.LegalPersonInfo`
        :param BusinessLicenseInfo: 营业证件信息。
        :type BusinessLicenseInfo: :class:`tencentcloud.cpdp.v20190820.models.BusinessLicenseInfo`
        :param InterConnectionSubMerchantData: 支付渠道子商户进件信息。
json字符串，详情见附录-复杂类型-InterConnectionSubMerchantData。
        :type InterConnectionSubMerchantData: str
        :param PaymentMethod: 支付方式。详见附录-云企付枚举类说明-PaymentMethod。
合利宝渠道不需要传。
        :type PaymentMethod: str
        :param OutSubMerchantShortName: 外部子商户简称。
HELIPAY渠道必传(长度不能小于2大于20)。
        :type OutSubMerchantShortName: str
        :param OutSubMerchantDescription: 外部子商户描述。
        :type OutSubMerchantDescription: str
        :param NotifyUrl: 通知地址。
        :type NotifyUrl: str
        :param NaturalPersonList: 相关自然人信息列表。
HELIPAY渠道必传业务联系人。
        :type NaturalPersonList: list of NaturalPersonInfo
        :param SettleInfo: 商户结算信息。
HELIPAY渠道必传。
        :type SettleInfo: :class:`tencentcloud.cpdp.v20190820.models.SettleInfo`
        :param OutSubMerchantExtensionInfo: 外部子商户其他公用扩展信息。
HELIPAY渠道必传。
        :type OutSubMerchantExtensionInfo: :class:`tencentcloud.cpdp.v20190820.models.OutSubMerchantExtensionInfo`
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.OutRegistrationNo = None
        self.ChannelMerchantId = None
        self.OutSubMerchantId = None
        self.ChannelName = None
        self.OutSubMerchantType = None
        self.OutSubMerchantName = None
        self.LegalPersonInfo = None
        self.BusinessLicenseInfo = None
        self.InterConnectionSubMerchantData = None
        self.PaymentMethod = None
        self.OutSubMerchantShortName = None
        self.OutSubMerchantDescription = None
        self.NotifyUrl = None
        self.NaturalPersonList = None
        self.SettleInfo = None
        self.OutSubMerchantExtensionInfo = None
        self.Environment = None


    def _deserialize(self, params):
        self.OutRegistrationNo = params.get("OutRegistrationNo")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutSubMerchantId = params.get("OutSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.OutSubMerchantType = params.get("OutSubMerchantType")
        self.OutSubMerchantName = params.get("OutSubMerchantName")
        if params.get("LegalPersonInfo") is not None:
            self.LegalPersonInfo = LegalPersonInfo()
            self.LegalPersonInfo._deserialize(params.get("LegalPersonInfo"))
        if params.get("BusinessLicenseInfo") is not None:
            self.BusinessLicenseInfo = BusinessLicenseInfo()
            self.BusinessLicenseInfo._deserialize(params.get("BusinessLicenseInfo"))
        self.InterConnectionSubMerchantData = params.get("InterConnectionSubMerchantData")
        self.PaymentMethod = params.get("PaymentMethod")
        self.OutSubMerchantShortName = params.get("OutSubMerchantShortName")
        self.OutSubMerchantDescription = params.get("OutSubMerchantDescription")
        self.NotifyUrl = params.get("NotifyUrl")
        if params.get("NaturalPersonList") is not None:
            self.NaturalPersonList = []
            for item in params.get("NaturalPersonList"):
                obj = NaturalPersonInfo()
                obj._deserialize(item)
                self.NaturalPersonList.append(obj)
        if params.get("SettleInfo") is not None:
            self.SettleInfo = SettleInfo()
            self.SettleInfo._deserialize(params.get("SettleInfo"))
        if params.get("OutSubMerchantExtensionInfo") is not None:
            self.OutSubMerchantExtensionInfo = OutSubMerchantExtensionInfo()
            self.OutSubMerchantExtensionInfo._deserialize(params.get("OutSubMerchantExtensionInfo"))
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankAggregatedSubMerchantRegistrationResponse(AbstractModel):
    """CreateOpenBankAggregatedSubMerchantRegistration返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankExternalAggregatedSubMerchantRegistrationResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateOpenBankExternalAggregatedSubMerchantRegistrationResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOpenBankExternalAggregatedSubMerchantRegistrationResult(AbstractModel):
    """聚合支付子商户线上入驻结果

    """

    def __init__(self):
        r"""
        :param RegistrationStatus: 进件状态 
SUCCESS: 进件成功 
FAILED: 进件失败
PROCESSING: 进件中 
注意：若返回进件中，需要再次调用进件结果查询接口，查询结果。
        :type RegistrationStatus: str
        :param RegistrationMessage: 进件返回描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistrationMessage: str
        :param ChannelRegistrationNo: 渠道进件序列号
        :type ChannelRegistrationNo: str
        :param ChannelSubMerchantId: 渠道子商户ID
        :type ChannelSubMerchantId: str
        """
        self.RegistrationStatus = None
        self.RegistrationMessage = None
        self.ChannelRegistrationNo = None
        self.ChannelSubMerchantId = None


    def _deserialize(self, params):
        self.RegistrationStatus = params.get("RegistrationStatus")
        self.RegistrationMessage = params.get("RegistrationMessage")
        self.ChannelRegistrationNo = params.get("ChannelRegistrationNo")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankExternalSubMerchantAccountBookRequest(AbstractModel):
    """CreateOpenBankExternalSubMerchantAccountBook请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutAccountBookId: 外部账本ID
        :type OutAccountBookId: str
        :param ChannelMerchantId: 渠道商户ID
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。目前只支持支付宝
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。目前只支持安心发支付
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
__SAFT_ISV__: 安心发支付
        :type PaymentMethod: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.OutAccountBookId = None
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.Environment = None


    def _deserialize(self, params):
        self.OutAccountBookId = params.get("OutAccountBookId")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankExternalSubMerchantAccountBookResponse(AbstractModel):
    """CreateOpenBankExternalSubMerchantAccountBook返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateExternalAccountBookResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateExternalAccountBookResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOpenBankExternalSubMerchantRegistrationRequest(AbstractModel):
    """CreateOpenBankExternalSubMerchantRegistration请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutRegistrationNo: 外部进件序列号。
        :type OutRegistrationNo: str
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param OutSubMerchantId: 外部子商户ID,平台侧商户唯一ID。
        :type OutSubMerchantId: str
        :param ChannelName: 渠道名称。详见附录-云企付枚举类说明-ChannelName。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。详见附录-云企付枚举类说明-PaymentMethod。
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
        :type PaymentMethod: str
        :param BusinessLicenseNumber: 社会信用代码。
        :type BusinessLicenseNumber: str
        :param OutSubMerchantName: 外部子商户名称。
        :type OutSubMerchantName: str
        :param LegalName: 法人姓名。
        :type LegalName: str
        :param OutSubMerchantShortName: 外部子商户简称。
        :type OutSubMerchantShortName: str
        :param OutSubMerchantDescription: 外部子商户描述。
        :type OutSubMerchantDescription: str
        :param ExternalSubMerchantRegistrationData: 第三方子商户进件信息，为JSON格式字符串。详情见附录-复杂类型。
        :type ExternalSubMerchantRegistrationData: str
        :param NotifyUrl: 通知地址。
        :type NotifyUrl: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.OutRegistrationNo = None
        self.ChannelMerchantId = None
        self.OutSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.BusinessLicenseNumber = None
        self.OutSubMerchantName = None
        self.LegalName = None
        self.OutSubMerchantShortName = None
        self.OutSubMerchantDescription = None
        self.ExternalSubMerchantRegistrationData = None
        self.NotifyUrl = None
        self.Environment = None


    def _deserialize(self, params):
        self.OutRegistrationNo = params.get("OutRegistrationNo")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutSubMerchantId = params.get("OutSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.BusinessLicenseNumber = params.get("BusinessLicenseNumber")
        self.OutSubMerchantName = params.get("OutSubMerchantName")
        self.LegalName = params.get("LegalName")
        self.OutSubMerchantShortName = params.get("OutSubMerchantShortName")
        self.OutSubMerchantDescription = params.get("OutSubMerchantDescription")
        self.ExternalSubMerchantRegistrationData = params.get("ExternalSubMerchantRegistrationData")
        self.NotifyUrl = params.get("NotifyUrl")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankExternalSubMerchantRegistrationResponse(AbstractModel):
    """CreateOpenBankExternalSubMerchantRegistration返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankExternalSubMerchantRegistrationResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateOpenBankExternalSubMerchantRegistrationResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOpenBankExternalSubMerchantRegistrationResult(AbstractModel):
    """子商户进件返回结果

    """

    def __init__(self):
        r"""
        :param RegistrationStatus: 进件状态。
__SUCCESS__: 进件成功
__FAILED__: 进件失败
__PROCESSING__: 进件中
注意：若返回进件中，需要再次调用进件结果查询接口，查询结果。
        :type RegistrationStatus: str
        :param RegistrationMessage: 进件返回描述, 例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistrationMessage: str
        :param ChannelRegistrationNo: 渠道进件序列号。
        :type ChannelRegistrationNo: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ExternalReturnData: 第三方渠道返回信息, 为JSON格式字符串。详情见附录-复杂类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnData: str
        """
        self.RegistrationStatus = None
        self.RegistrationMessage = None
        self.ChannelRegistrationNo = None
        self.ChannelSubMerchantId = None
        self.ExternalReturnData = None


    def _deserialize(self, params):
        self.RegistrationStatus = params.get("RegistrationStatus")
        self.RegistrationMessage = params.get("RegistrationMessage")
        self.ChannelRegistrationNo = params.get("ChannelRegistrationNo")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ExternalReturnData = params.get("ExternalReturnData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankMerchantRequest(AbstractModel):
    """CreateOpenBankMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutMerchantId: 外部商户ID。
        :type OutMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param OutMerchantName: 外部商户名称。
        :type OutMerchantName: str
        :param ExternalMerchantInfo: 第三方渠道商户信息。详情见附录-复杂类型。
        :type ExternalMerchantInfo: str
        :param OutMerchantShortName: 外部商户简称。
        :type OutMerchantShortName: str
        :param OutMerchantDescription: 外部商户描述
        :type OutMerchantDescription: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.OutMerchantId = None
        self.ChannelName = None
        self.OutMerchantName = None
        self.ExternalMerchantInfo = None
        self.OutMerchantShortName = None
        self.OutMerchantDescription = None
        self.Environment = None


    def _deserialize(self, params):
        self.OutMerchantId = params.get("OutMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.OutMerchantName = params.get("OutMerchantName")
        self.ExternalMerchantInfo = params.get("ExternalMerchantInfo")
        self.OutMerchantShortName = params.get("OutMerchantShortName")
        self.OutMerchantDescription = params.get("OutMerchantDescription")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankMerchantResponse(AbstractModel):
    """CreateOpenBankMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankMerchantResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateOpenBankMerchantResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOpenBankMerchantResult(AbstractModel):
    """创建渠道商户返回结果

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        """
        self.ChannelMerchantId = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankOrderPaymentResult(AbstractModel):
    """云企付-支付下单返回响应

    """

    def __init__(self):
        r"""
        :param ChannelOrderId: 云企付平台订单号。
        :type ChannelOrderId: str
        :param ThirdPayOrderId: 第三方支付平台返回支付订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type ThirdPayOrderId: str
        :param RedirectInfo: 小程序跳转参数渠道为TENPAY，付款方式为EBANK_PAYMENT时必选。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankRedirectInfo`
        :param OutOrderId: 外部商户订单号，只能是数字、大小写字母，且在同一个接入平台下唯一。
        :type OutOrderId: str
        """
        self.ChannelOrderId = None
        self.ThirdPayOrderId = None
        self.RedirectInfo = None
        self.OutOrderId = None


    def _deserialize(self, params):
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.ThirdPayOrderId = params.get("ThirdPayOrderId")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = OpenBankRedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        self.OutOrderId = params.get("OutOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankOrderRechargeResult(AbstractModel):
    """云企付-充值下单返回响应

    """

    def __init__(self):
        r"""
        :param ChannelOrderId: 云企付平台订单号。
        :type ChannelOrderId: str
        :param ThirdPayOrderId: 第三方支付平台返回支付订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type ThirdPayOrderId: str
        :param RedirectInfo: 跳转参数
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankRechargeRedirectInfo`
        :param OutOrderId: 外部商户订单号，只能是数字、大小写字母，且在同一个接入平台下唯一。
        :type OutOrderId: str
        """
        self.ChannelOrderId = None
        self.ThirdPayOrderId = None
        self.RedirectInfo = None
        self.OutOrderId = None


    def _deserialize(self, params):
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.ThirdPayOrderId = params.get("ThirdPayOrderId")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = OpenBankRechargeRedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        self.OutOrderId = params.get("OutOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankPaymentOrderRequest(AbstractModel):
    """CreateOpenBankPaymentOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 云企付渠道商户号。外部接入平台入驻云企付平台后下发。
        :type ChannelMerchantId: str
        :param ChannelName: 渠道名称。详见附录-云企付枚举类说明-ChannelName。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
__WECHAT__: 微信支付
        :type ChannelName: str
        :param PaymentMethod: 付款方式。详见附录-云企付枚举类说明-PaymentMethod。
__EBANK_PAYMENT__:B2B EBank付款
__OPENBANK_PAYMENT__:B2C  openbank付款
__SAFT_ISV__:支付宝安心发
__TRANS_TO_CHANGE__: 微信支付转账到零钱v2
        :type PaymentMethod: str
        :param PaymentMode: 付款模式。默认直接支付，如
__DIRECT__:直接支付
__FREEZE__:担保支付
        :type PaymentMode: str
        :param OutOrderId: 外部订单号,只能是数字、大小写字母，且在同一个接入平台下唯一，限定长度40位。
        :type OutOrderId: str
        :param TotalAmount: 付款金额，单位分。
        :type TotalAmount: int
        :param Currency: 固定值CNY。
        :type Currency: str
        :param PayerInfo: 付款方信息。
        :type PayerInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankPayerInfo`
        :param PayeeInfo: 收款方信息。
        :type PayeeInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankPayeeInfo`
        :param NotifyUrl: 通知地址，如www.test.com。
        :type NotifyUrl: str
        :param ExpireTime: 订单过期时间，yyyy-MM-dd HH:mm:ss格式。
        :type ExpireTime: str
        :param FrontUrl: 前端成功回调URL。条件可选。
        :type FrontUrl: str
        :param RefreshUrl: 前端刷新 URL。条件可选。
        :type RefreshUrl: str
        :param SceneInfo: 设备信息，条件可选。
        :type SceneInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankSceneInfo`
        :param GoodsInfo: 商品信息，条件可选。
        :type GoodsInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankGoodsInfo`
        :param Attachment: 附加信息，查询时原样返回。
        :type Attachment: str
        :param ProfitShareFlag: 若不上传，即使用默认值无需分润
__NO_NEED_SHARE__：无需分润；
__SHARE_BY_INFO__：分润时指定金额，此时如果分润信息 ProfitShareInfo为空，只冻结，不分账给其他商户；需要调用解冻接口。
__SHARE_BY_API__：后续调用分润接口决定分润金额
        :type ProfitShareFlag: str
        :param ProfitShareInfoList: 分润信息，配合ProfitShareFlag使用。
        :type ProfitShareInfoList: list of OpenBankProfitShareInfo
        :param Remark: 备注信息。
        :type Remark: str
        :param Environment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
缺省默认为生产环境
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.PaymentMode = None
        self.OutOrderId = None
        self.TotalAmount = None
        self.Currency = None
        self.PayerInfo = None
        self.PayeeInfo = None
        self.NotifyUrl = None
        self.ExpireTime = None
        self.FrontUrl = None
        self.RefreshUrl = None
        self.SceneInfo = None
        self.GoodsInfo = None
        self.Attachment = None
        self.ProfitShareFlag = None
        self.ProfitShareInfoList = None
        self.Remark = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.PaymentMode = params.get("PaymentMode")
        self.OutOrderId = params.get("OutOrderId")
        self.TotalAmount = params.get("TotalAmount")
        self.Currency = params.get("Currency")
        if params.get("PayerInfo") is not None:
            self.PayerInfo = OpenBankPayerInfo()
            self.PayerInfo._deserialize(params.get("PayerInfo"))
        if params.get("PayeeInfo") is not None:
            self.PayeeInfo = OpenBankPayeeInfo()
            self.PayeeInfo._deserialize(params.get("PayeeInfo"))
        self.NotifyUrl = params.get("NotifyUrl")
        self.ExpireTime = params.get("ExpireTime")
        self.FrontUrl = params.get("FrontUrl")
        self.RefreshUrl = params.get("RefreshUrl")
        if params.get("SceneInfo") is not None:
            self.SceneInfo = OpenBankSceneInfo()
            self.SceneInfo._deserialize(params.get("SceneInfo"))
        if params.get("GoodsInfo") is not None:
            self.GoodsInfo = OpenBankGoodsInfo()
            self.GoodsInfo._deserialize(params.get("GoodsInfo"))
        self.Attachment = params.get("Attachment")
        self.ProfitShareFlag = params.get("ProfitShareFlag")
        if params.get("ProfitShareInfoList") is not None:
            self.ProfitShareInfoList = []
            for item in params.get("ProfitShareInfoList"):
                obj = OpenBankProfitShareInfo()
                obj._deserialize(item)
                self.ProfitShareInfoList.append(obj)
        self.Remark = params.get("Remark")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankPaymentOrderResponse(AbstractModel):
    """CreateOpenBankPaymentOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 统一下单响应对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankOrderPaymentResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateOpenBankOrderPaymentResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOpenBankRechargeOrderRequest(AbstractModel):
    """CreateOpenBankRechargeOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 云企付渠道商户号。外部接入平台入驻云企付平台后下发。
        :type ChannelMerchantId: str
        :param OutOrderId: 外部订单号,只能是数字、大小写字母，且在同一个接入平台下唯一，限定长度40位。
        :type OutOrderId: str
        :param TotalAmount: 付款金额，单位分。
        :type TotalAmount: int
        :param Currency: 固定值CNY。
        :type Currency: str
        :param ExpireTime: 订单过期时间，yyyy-MM-dd HH:mm:ss格式。
        :type ExpireTime: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type PaymentMethod: str
        :param PayeeInfo: 收款方信息。
        :type PayeeInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankRechargePayeeInfo`
        :param ChannelSubMerchantId: 渠道子商户号
        :type ChannelSubMerchantId: str
        :param NotifyUrl: 通知地址，如www.test.com。
        :type NotifyUrl: str
        :param Remark: 备注信息。
        :type Remark: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.OutOrderId = None
        self.TotalAmount = None
        self.Currency = None
        self.ExpireTime = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.PayeeInfo = None
        self.ChannelSubMerchantId = None
        self.NotifyUrl = None
        self.Remark = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutOrderId = params.get("OutOrderId")
        self.TotalAmount = params.get("TotalAmount")
        self.Currency = params.get("Currency")
        self.ExpireTime = params.get("ExpireTime")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        if params.get("PayeeInfo") is not None:
            self.PayeeInfo = OpenBankRechargePayeeInfo()
            self.PayeeInfo._deserialize(params.get("PayeeInfo"))
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.NotifyUrl = params.get("NotifyUrl")
        self.Remark = params.get("Remark")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankRechargeOrderResponse(AbstractModel):
    """CreateOpenBankRechargeOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 充值响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankOrderRechargeResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateOpenBankOrderRechargeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOpenBankSubMerchantRateConfigureRequest(AbstractModel):
    """CreateOpenBankSubMerchantRateConfigure请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelRegistrationNo: 渠道进件序列号。
填写子商户进件返回的渠道进件编号。
        :type ChannelRegistrationNo: str
        :param OutProductFeeNo: 外部产品费率申请序列号。
        :type OutProductFeeNo: str
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。详见附录-云企付枚举类说明-ChannelName。
        :type ChannelName: str
        :param PayType: 支付类型。
SWIPE:刷卡
SCAN:扫码
WAP:WAP
PUBLIC:公众号支付
SDK:SDK
MINI_PROGRAM:小程序
注意：HELIPAY渠道传SDK。
        :type PayType: str
        :param PayChannel: 支付渠道。
ALIPAY：支付宝 
WXPAY：微信支付 
UNIONPAY：银联
        :type PayChannel: str
        :param FeeMode: 计费模式。
SINGLE：按单笔金额计费
RATIO：按单笔费率计费 
RANGE：按分段区间计费
        :type FeeMode: str
        :param FeeValue: 费用值，单位（0.01%或分）。
        :type FeeValue: int
        :param PaymentMethod: 支付方式。详见附录-云企付枚举类说明-PaymentMethod。
HELIPAY渠道不需要传入。
        :type PaymentMethod: str
        :param MinFee: 最低收费金额，单位（分）。
        :type MinFee: int
        :param MaxFee: 最高收费金额，单位（分）。
        :type MaxFee: int
        :param NotifyUrl: 通知地址。
        :type NotifyUrl: str
        :param FeeRangeList: 分段计费区间列表。
        :type FeeRangeList: list of FeeRangInfo
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelRegistrationNo = None
        self.OutProductFeeNo = None
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PayType = None
        self.PayChannel = None
        self.FeeMode = None
        self.FeeValue = None
        self.PaymentMethod = None
        self.MinFee = None
        self.MaxFee = None
        self.NotifyUrl = None
        self.FeeRangeList = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelRegistrationNo = params.get("ChannelRegistrationNo")
        self.OutProductFeeNo = params.get("OutProductFeeNo")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PayType = params.get("PayType")
        self.PayChannel = params.get("PayChannel")
        self.FeeMode = params.get("FeeMode")
        self.FeeValue = params.get("FeeValue")
        self.PaymentMethod = params.get("PaymentMethod")
        self.MinFee = params.get("MinFee")
        self.MaxFee = params.get("MaxFee")
        self.NotifyUrl = params.get("NotifyUrl")
        if params.get("FeeRangeList") is not None:
            self.FeeRangeList = []
            for item in params.get("FeeRangeList"):
                obj = FeeRangInfo()
                obj._deserialize(item)
                self.FeeRangeList.append(obj)
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankSubMerchantRateConfigureResponse(AbstractModel):
    """CreateOpenBankSubMerchantRateConfigure返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankSubMerchantRateConfigureResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateOpenBankSubMerchantRateConfigureResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOpenBankSubMerchantRateConfigureResult(AbstractModel):
    """聚合支付子商户费率配置结果

    """

    def __init__(self):
        r"""
        :param DealStatus: 处理状态 
SUCCESS: 开通成功 
FAILED: 开通失败
PROCESSING: 开通中 
注意：若返回开通中，需要再次调用费率配置结果查询接口，查询结果。
        :type DealStatus: str
        :param DealMessage: 处理描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DealMessage: str
        :param ChannelProductFeeNo: 渠道产品费率序列号
        :type ChannelProductFeeNo: str
        """
        self.DealStatus = None
        self.DealMessage = None
        self.ChannelProductFeeNo = None


    def _deserialize(self, params):
        self.DealStatus = params.get("DealStatus")
        self.DealMessage = params.get("DealMessage")
        self.ChannelProductFeeNo = params.get("ChannelProductFeeNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankUnifiedOrderRequest(AbstractModel):
    """CreateOpenBankUnifiedOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户号。
        :type ChannelMerchantId: str
        :param ChannelName: 渠道名称。
        :type ChannelName: str
        :param PayType: 支付产品类型。
被扫（扫码）：SWIPE, 主扫（刷卡）：SCAN, 
H5：WAP, 公众号：PUBLIC, 
APP-SDK：SDK, 小程序：MINI_PROGRAM, 
快捷支付：QUICK, 网银支付：ONLINE_BANK。
        :type PayType: str
        :param OutOrderId: 外部商户订单号。
只能是数字、大小写字母，且在同一个接入平台下唯一。
        :type OutOrderId: str
        :param TotalAmount: 交易金额，单位分。
        :type TotalAmount: int
        :param Currency: 币种。固定：CNY。
        :type Currency: str
        :param ChannelSubMerchantId: 渠道子商户号。
        :type ChannelSubMerchantId: str
        :param PayChannel: 实际支付渠道。没有则无需填写。如
支付宝 ALIPAY
微信支付 WXPAY
银联 UNIONPAY
一般在间连模式下使用。
        :type PayChannel: str
        :param SceneInfo: 设备信息。
        :type SceneInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankSceneInfo`
        :param ProfitShareInfoList: 分账信息列表。
        :type ProfitShareInfoList: list of OpenBankProfitShareInfo
        :param OrderSubject: 订单标题。
        :type OrderSubject: str
        :param GoodsDetail: 商品信息。
        :type GoodsDetail: str
        :param ExpireTime: 超时时间。
        :type ExpireTime: str
        :param NotifyUrl: 支付成功回调地址。
        :type NotifyUrl: str
        :param FrontUrl: 支付成功前端跳转URL。
        :type FrontUrl: str
        :param Attachment: 订单附加信息，查询或者回调的时候原样返回。
        :type Attachment: str
        :param ExternalPaymentData: 第三方渠道扩展字段。见附录-复杂类型。
未作特殊说明，则无需传入。
        :type ExternalPaymentData: str
        :param Remark: 备注。
        :type Remark: str
        :param StoreInfo: 门店信息。
        :type StoreInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankStoreInfo`
        :param PayLimitInfo: 支付限制。
        :type PayLimitInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankPayLimitInfo`
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelName = None
        self.PayType = None
        self.OutOrderId = None
        self.TotalAmount = None
        self.Currency = None
        self.ChannelSubMerchantId = None
        self.PayChannel = None
        self.SceneInfo = None
        self.ProfitShareInfoList = None
        self.OrderSubject = None
        self.GoodsDetail = None
        self.ExpireTime = None
        self.NotifyUrl = None
        self.FrontUrl = None
        self.Attachment = None
        self.ExternalPaymentData = None
        self.Remark = None
        self.StoreInfo = None
        self.PayLimitInfo = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PayType = params.get("PayType")
        self.OutOrderId = params.get("OutOrderId")
        self.TotalAmount = params.get("TotalAmount")
        self.Currency = params.get("Currency")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.PayChannel = params.get("PayChannel")
        if params.get("SceneInfo") is not None:
            self.SceneInfo = OpenBankSceneInfo()
            self.SceneInfo._deserialize(params.get("SceneInfo"))
        if params.get("ProfitShareInfoList") is not None:
            self.ProfitShareInfoList = []
            for item in params.get("ProfitShareInfoList"):
                obj = OpenBankProfitShareInfo()
                obj._deserialize(item)
                self.ProfitShareInfoList.append(obj)
        self.OrderSubject = params.get("OrderSubject")
        self.GoodsDetail = params.get("GoodsDetail")
        self.ExpireTime = params.get("ExpireTime")
        self.NotifyUrl = params.get("NotifyUrl")
        self.FrontUrl = params.get("FrontUrl")
        self.Attachment = params.get("Attachment")
        self.ExternalPaymentData = params.get("ExternalPaymentData")
        self.Remark = params.get("Remark")
        if params.get("StoreInfo") is not None:
            self.StoreInfo = OpenBankStoreInfo()
            self.StoreInfo._deserialize(params.get("StoreInfo"))
        if params.get("PayLimitInfo") is not None:
            self.PayLimitInfo = OpenBankPayLimitInfo()
            self.PayLimitInfo._deserialize(params.get("PayLimitInfo"))
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOpenBankUnifiedOrderResponse(AbstractModel):
    """CreateOpenBankUnifiedOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 统一下单响应对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateOpenBankOrderPaymentResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateOpenBankOrderPaymentResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateOrderRequest(AbstractModel):
    """CreateOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelCode: 渠道编号。ZSB2B：招商银行B2B。
        :type ChannelCode: str
        :param MerchantAppId: 进件成功后返给商户方的 AppId。
        :type MerchantAppId: str
        :param Amount: 交易金额。单位：元
        :type Amount: str
        :param TraceNo: 商户流水号。商户唯一订单号由字母或数字组成。
        :type TraceNo: str
        :param NotifyUrl: 通知地址。商户接收交易结果的通知地址。
        :type NotifyUrl: str
        :param ReturnUrl: 返回地址。支付成功后，页面将跳 转返回到商户的该地址。
        :type ReturnUrl: str
        """
        self.ChannelCode = None
        self.MerchantAppId = None
        self.Amount = None
        self.TraceNo = None
        self.NotifyUrl = None
        self.ReturnUrl = None


    def _deserialize(self, params):
        self.ChannelCode = params.get("ChannelCode")
        self.MerchantAppId = params.get("MerchantAppId")
        self.Amount = params.get("Amount")
        self.TraceNo = params.get("TraceNo")
        self.NotifyUrl = params.get("NotifyUrl")
        self.ReturnUrl = params.get("ReturnUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderResponse(AbstractModel):
    """CreateOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 进件成功后返给商户方的AppId。
        :type MerchantAppId: str
        :param TraceNo: 商户流水号，商户唯一订单号由字母或数字组成。
        :type TraceNo: str
        :param OrderNo: 平台流水号，若下单成功则返回。
        :type OrderNo: str
        :param PayUrl: 支付页面跳转地址，若下单成功则返回。
        :type PayUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantAppId = None
        self.TraceNo = None
        self.OrderNo = None
        self.PayUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.TraceNo = params.get("TraceNo")
        self.OrderNo = params.get("OrderNo")
        self.PayUrl = params.get("PayUrl")
        self.RequestId = params.get("RequestId")


class CreatePayMerchantRequest(AbstractModel):
    """CreatePayMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param PlatformCode: 平台编号
        :type PlatformCode: str
        :param ChannelMerchantNo: 渠道方收款商户编号，由渠道方(银行)提 供。
        :type ChannelMerchantNo: str
        :param ChannelCheckFlag: 是否需要向渠道进行 商户信息验证 1:验证
0:不验证
        :type ChannelCheckFlag: str
        :param MerchantName: 收款商户名称
        :type MerchantName: str
        :param BusinessPayFlag: 是否开通 B2B 支付 1:开通 0:不开通 缺省:1
        :type BusinessPayFlag: str
        """
        self.PlatformCode = None
        self.ChannelMerchantNo = None
        self.ChannelCheckFlag = None
        self.MerchantName = None
        self.BusinessPayFlag = None


    def _deserialize(self, params):
        self.PlatformCode = params.get("PlatformCode")
        self.ChannelMerchantNo = params.get("ChannelMerchantNo")
        self.ChannelCheckFlag = params.get("ChannelCheckFlag")
        self.MerchantName = params.get("MerchantName")
        self.BusinessPayFlag = params.get("BusinessPayFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayMerchantResponse(AbstractModel):
    """CreatePayMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 分配给商户的 AppId。该 AppId 为后续各项 交易的商户标识。
        :type MerchantAppId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantAppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.RequestId = params.get("RequestId")


class CreatePayRollPreOrderRequest(AbstractModel):
    """CreatePayRollPreOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param AuthNumber: 商户系统内部的商家核身单号，要求此参数只能由数字、大小写字母组成，在服务商内部唯一
        :type AuthNumber: str
        :param ProjectName: 该劳务活动的项目名称
        :type ProjectName: str
        :param CompanyName: 该工人所属的用工企业
        :type CompanyName: str
        :param WechatAppId: 是服务商在微信申请公众号/小程序或移动应用成功后分配的账号ID（与服务商主体一致）
当输入服务商Appid时，会校验其与服务商商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatAppId: str
        :param WechatSubAppId: 特约商户在微信申请公众号/小程序或移动应用成功后分配的账号ID（与特约商户主体一致）
当输入特约商户Appid时，会校验其与特约商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatSubAppId: str
        """
        self.OpenId = None
        self.SubMerchantId = None
        self.AuthNumber = None
        self.ProjectName = None
        self.CompanyName = None
        self.WechatAppId = None
        self.WechatSubAppId = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.AuthNumber = params.get("AuthNumber")
        self.ProjectName = params.get("ProjectName")
        self.CompanyName = params.get("CompanyName")
        self.WechatAppId = params.get("WechatAppId")
        self.WechatSubAppId = params.get("WechatSubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayRollPreOrderResponse(AbstractModel):
    """CreatePayRollPreOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param AuthNumber: 商户系统内部的商家核身单号，要求此参数只能由数字、大小写字母组成，在服务商内部唯一
        :type AuthNumber: str
        :param ExpireTime: Token有效时间，单位秒
        :type ExpireTime: int
        :param MerchantId: 微信服务商商户的商户号，由微信支付生成并下发
        :type MerchantId: str
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param Token: Token值
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuthNumber = None
        self.ExpireTime = None
        self.MerchantId = None
        self.OpenId = None
        self.SubMerchantId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuthNumber = params.get("AuthNumber")
        self.ExpireTime = params.get("ExpireTime")
        self.MerchantId = params.get("MerchantId")
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class CreatePayRollPreOrderWithAuthRequest(AbstractModel):
    """CreatePayRollPreOrderWithAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param AuthNumber: 商户系统内部的商家核身单号，要求此参数只能由数字、大小写字母组成，在服务商内部唯一
        :type AuthNumber: str
        :param ProjectName: 该劳务活动的项目名称
        :type ProjectName: str
        :param CompanyName: 该工人所属的用工企业
        :type CompanyName: str
        :param UserName: 用户实名信息，该字段需进行加密处理，加密方法详见[敏感信息加密说明](https://pay.weixin.qq.com/wiki/doc/apiv3_partner/wechatpay/wechatpay4_3.shtml)
        :type UserName: str
        :param IdNo: 用户证件号，该字段需进行加密处理，加密方法详见[敏感信息加密说明](https://pay.weixin.qq.com/wiki/doc/apiv3_partner/wechatpay/wechatpay4_3.shtml)
        :type IdNo: str
        :param EmploymentType: 微工卡服务仅支持用于与商户有用工关系的用户，需明确用工类型；参考值：
LONG_TERM_EMPLOYMENT：长期用工，
SHORT_TERM_EMPLOYMENT： 短期用工，
COOPERATION_EMPLOYMENT：合作关系
        :type EmploymentType: str
        :param WechatAppId: 是服务商在微信申请公众号/小程序或移动应用成功后分配的账号ID（与服务商主体一致）
当输入服务商Appid时，会校验其与服务商商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatAppId: str
        :param WechatSubAppId: 特约商户在微信申请公众号/小程序或移动应用成功后分配的账号ID（与特约商户主体一致）
当输入特约商户Appid时，会校验其与特约商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatSubAppId: str
        """
        self.OpenId = None
        self.SubMerchantId = None
        self.AuthNumber = None
        self.ProjectName = None
        self.CompanyName = None
        self.UserName = None
        self.IdNo = None
        self.EmploymentType = None
        self.WechatAppId = None
        self.WechatSubAppId = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.AuthNumber = params.get("AuthNumber")
        self.ProjectName = params.get("ProjectName")
        self.CompanyName = params.get("CompanyName")
        self.UserName = params.get("UserName")
        self.IdNo = params.get("IdNo")
        self.EmploymentType = params.get("EmploymentType")
        self.WechatAppId = params.get("WechatAppId")
        self.WechatSubAppId = params.get("WechatSubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayRollPreOrderWithAuthResponse(AbstractModel):
    """CreatePayRollPreOrderWithAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param AuthNumber: 商户系统内部的商家核身单号，要求此参数只能由数字、大小写字母组成，在服务商内部唯一
        :type AuthNumber: str
        :param ExpireTime: Token有效时间，单位秒
        :type ExpireTime: int
        :param MerchantId: 微信服务商商户的商户号，由微信支付生成并下发
        :type MerchantId: str
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param Token: Token值
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuthNumber = None
        self.ExpireTime = None
        self.MerchantId = None
        self.OpenId = None
        self.SubMerchantId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuthNumber = params.get("AuthNumber")
        self.ExpireTime = params.get("ExpireTime")
        self.MerchantId = params.get("MerchantId")
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class CreatePayRollTokenRequest(AbstractModel):
    """CreatePayRollToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param UserName: 用户实名信息，该字段需进行加密处理，加密方法详见[敏感信息加密说明](https://pay.weixin.qq.com/wiki/doc/apiv3_partner/wechatpay/wechatpay4_3.shtml)
        :type UserName: str
        :param IdNo: 用户证件号，该字段需进行加密处理，加密方法详见[敏感信息加密说明](https://pay.weixin.qq.com/wiki/doc/apiv3_partner/wechatpay/wechatpay4_3.shtml)
        :type IdNo: str
        :param EmploymentType: 微工卡服务仅支持用于与商户有用工关系的用户，需明确用工类型；参考值：
LONG_TERM_EMPLOYMENT：长期用工，
SHORT_TERM_EMPLOYMENT： 短期用工，
COOPERATION_EMPLOYMENT：合作关系
        :type EmploymentType: str
        :param WechatAppId: 是服务商在微信申请公众号/小程序或移动应用成功后分配的账号ID（与服务商主体一致）
当输入服务商Appid时，会校验其与服务商商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatAppId: str
        :param WechatSubAppId: 特约商户在微信申请公众号/小程序或移动应用成功后分配的账号ID（与特约商户主体一致）
当输入特约商户Appid时，会校验其与特约商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatSubAppId: str
        """
        self.OpenId = None
        self.SubMerchantId = None
        self.UserName = None
        self.IdNo = None
        self.EmploymentType = None
        self.WechatAppId = None
        self.WechatSubAppId = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.UserName = params.get("UserName")
        self.IdNo = params.get("IdNo")
        self.EmploymentType = params.get("EmploymentType")
        self.WechatAppId = params.get("WechatAppId")
        self.WechatSubAppId = params.get("WechatSubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePayRollTokenResponse(AbstractModel):
    """CreatePayRollToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param ExpireTime: Token有效时间，单位秒
        :type ExpireTime: int
        :param MerchantId: 微信服务商商户的商户号，由微信支付生成并下发
        :type MerchantId: str
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param Token: Token值
        :type Token: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExpireTime = None
        self.MerchantId = None
        self.OpenId = None
        self.SubMerchantId = None
        self.Token = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ExpireTime = params.get("ExpireTime")
        self.MerchantId = params.get("MerchantId")
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.Token = params.get("Token")
        self.RequestId = params.get("RequestId")


class CreateRedInvoiceItem(AbstractModel):
    """创建红票明细

    """

    def __init__(self):
        r"""
        :param OrderId: 订单号
        :type OrderId: str
        :param CallbackUrl: 发票结果回传地址
        :type CallbackUrl: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        :param RedSerialNo: 红字信息表编码
        :type RedSerialNo: str
        :param StoreNo: 门店编号
        :type StoreNo: str
        """
        self.OrderId = None
        self.CallbackUrl = None
        self.OrderSn = None
        self.RedSerialNo = None
        self.StoreNo = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.CallbackUrl = params.get("CallbackUrl")
        self.OrderSn = params.get("OrderSn")
        self.RedSerialNo = params.get("RedSerialNo")
        self.StoreNo = params.get("StoreNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceRequest(AbstractModel):
    """CreateRedInvoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID
0 : 高灯
1 : 票易通
        :type InvoicePlatformId: int
        :param Invoices: 红冲明细
        :type Invoices: list of CreateRedInvoiceItem
        :param Profile: 接入环境。沙箱环境填 sandbox。
        :type Profile: str
        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道
        :type InvoiceChannel: int
        """
        self.InvoicePlatformId = None
        self.Invoices = None
        self.Profile = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        if params.get("Invoices") is not None:
            self.Invoices = []
            for item in params.get("Invoices"):
                obj = CreateRedInvoiceItem()
                obj._deserialize(item)
                self.Invoices.append(obj)
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceResponse(AbstractModel):
    """CreateRedInvoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 红冲结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateRedInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateRedInvoiceResult(AbstractModel):
    """红票结果

    """

    def __init__(self):
        r"""
        :param Message: 错误消息
        :type Message: str
        :param Code: 错误码
        :type Code: int
        :param Data: 红票数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CreateRedInvoiceResultData
        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CreateRedInvoiceResultData()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceResultData(AbstractModel):
    """红票结果数据

    """

    def __init__(self):
        r"""
        :param Code: 红冲状态码
        :type Code: int
        :param Message: 红冲状态消息
        :type Message: str
        :param InvoiceId: 发票ID
        :type InvoiceId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        """
        self.Code = None
        self.Message = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceResultV2(AbstractModel):
    """红票结果V2

    """

    def __init__(self):
        r"""
        :param InvoiceId: 红票ID
        :type InvoiceId: str
        """
        self.InvoiceId = None


    def _deserialize(self, params):
        self.InvoiceId = params.get("InvoiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceV2Request(AbstractModel):
    """CreateRedInvoiceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID
0 : 高灯
1 : 票易通
        :type InvoicePlatformId: int
        :param OrderId: 订单号
        :type OrderId: str
        :param Profile: 接入环境。沙箱环境填 sandbox。
        :type Profile: str
        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道
        :type InvoiceChannel: int
        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.Profile = None
        self.InvoiceChannel = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRedInvoiceV2Response(AbstractModel):
    """CreateRedInvoiceV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 红冲结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceResultV2`
        :param ErrCode: 错误码
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.ErrCode = None
        self.ErrMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateRedInvoiceResultV2()
            self.Result._deserialize(params.get("Result"))
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.RequestId = params.get("RequestId")


class CreateSinglePayRequest(AbstractModel):
    """CreateSinglePay请求参数结构体

    """

    def __init__(self):
        r"""
        :param SerialNumber: 业务流水号，历史唯一
        :type SerialNumber: str
        :param PayAccountNumber: 付方账户号
        :type PayAccountNumber: str
        :param PayAccountName: 付方账户名称
        :type PayAccountName: str
        :param Amount: 金额
        :type Amount: int
        :param RecvAccountNumber: 收方账户号
        :type RecvAccountNumber: str
        :param RecvAccountName: 收方账户名称
        :type RecvAccountName: str
        :param PayBankCnaps: 付方账户CNAPS号
        :type PayBankCnaps: str
        :param PayBankType: 付方账户银行大类，PayBankCnaps为空时必传（见常见问题-银企直连银行类型）
        :type PayBankType: str
        :param PayBankProvince: 付方账户银行所在省，PayBankCnaps为空时必传（见常见问题-银企直连省份枚举信息）
        :type PayBankProvince: str
        :param PayBankCity: 付方账户银行所在地区，PayBankCnaps为空时必传（见常见问题-银企直连城市枚举信息）
        :type PayBankCity: str
        :param RecvBankCnaps: 收方账户CNAPS号
        :type RecvBankCnaps: str
        :param RecvBankType: 收方账户银行大类，RecvBankCnaps为空时必传（见常见问题-银企直连银行类型）
        :type RecvBankType: str
        :param RecvBankProvince: 收方账户银行所在省，RecvBankCnaps为空时必传（见常见问题-银企直连省份枚举信息）
        :type RecvBankProvince: str
        :param RecvBankCity: 收方账户银行所在地区，RecvBankCnaps为空时必传（见常见问题-银企直连城市枚举信息）
        :type RecvBankCity: str
        :param RecvCertType: 收款方证件类型（见常见问题-银企直连证件类型枚举信息）
        :type RecvCertType: str
        :param RecvCertNo: 收款方证件号码
        :type RecvCertNo: str
        :param Summary: 摘要信息
        :type Summary: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.SerialNumber = None
        self.PayAccountNumber = None
        self.PayAccountName = None
        self.Amount = None
        self.RecvAccountNumber = None
        self.RecvAccountName = None
        self.PayBankCnaps = None
        self.PayBankType = None
        self.PayBankProvince = None
        self.PayBankCity = None
        self.RecvBankCnaps = None
        self.RecvBankType = None
        self.RecvBankProvince = None
        self.RecvBankCity = None
        self.RecvCertType = None
        self.RecvCertNo = None
        self.Summary = None
        self.Profile = None


    def _deserialize(self, params):
        self.SerialNumber = params.get("SerialNumber")
        self.PayAccountNumber = params.get("PayAccountNumber")
        self.PayAccountName = params.get("PayAccountName")
        self.Amount = params.get("Amount")
        self.RecvAccountNumber = params.get("RecvAccountNumber")
        self.RecvAccountName = params.get("RecvAccountName")
        self.PayBankCnaps = params.get("PayBankCnaps")
        self.PayBankType = params.get("PayBankType")
        self.PayBankProvince = params.get("PayBankProvince")
        self.PayBankCity = params.get("PayBankCity")
        self.RecvBankCnaps = params.get("RecvBankCnaps")
        self.RecvBankType = params.get("RecvBankType")
        self.RecvBankProvince = params.get("RecvBankProvince")
        self.RecvBankCity = params.get("RecvBankCity")
        self.RecvCertType = params.get("RecvCertType")
        self.RecvCertNo = params.get("RecvCertNo")
        self.Summary = params.get("Summary")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSinglePayResponse(AbstractModel):
    """CreateSinglePay返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateSinglePayResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateSinglePayResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateSinglePayResult(AbstractModel):
    """银企直连-单笔支付响应结果

    """

    def __init__(self):
        r"""
        :param HandleStatus: 受理状态（S：处理成功；F：处理失败）
        :type HandleStatus: str
        :param HandleMsg: 受理状态描述
        :type HandleMsg: str
        :param SerialNo: 业务流水号，历史唯一
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param BankSerialNo: 银行指令流水
注意：此字段可能返回 null，表示取不到有效值。
        :type BankSerialNo: str
        :param PayStatus: 付款状态
注意：此字段可能返回 null，表示取不到有效值。
        :type PayStatus: str
        :param BankRetCode: 银行原始返回码
注意：此字段可能返回 null，表示取不到有效值。
        :type BankRetCode: str
        :param BankRetMsg: 银行原始返回
注意：此字段可能返回 null，表示取不到有效值。
        :type BankRetMsg: str
        """
        self.HandleStatus = None
        self.HandleMsg = None
        self.SerialNo = None
        self.BankSerialNo = None
        self.PayStatus = None
        self.BankRetCode = None
        self.BankRetMsg = None


    def _deserialize(self, params):
        self.HandleStatus = params.get("HandleStatus")
        self.HandleMsg = params.get("HandleMsg")
        self.SerialNo = params.get("SerialNo")
        self.BankSerialNo = params.get("BankSerialNo")
        self.PayStatus = params.get("PayStatus")
        self.BankRetCode = params.get("BankRetCode")
        self.BankRetMsg = params.get("BankRetMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSinglePaymentData(AbstractModel):
    """CreateSinglePayment接口返回响应

    """

    def __init__(self):
        r"""
        :param TradeSerialNo: 平台交易流水号，唯一
        :type TradeSerialNo: str
        """
        self.TradeSerialNo = None


    def _deserialize(self, params):
        self.TradeSerialNo = params.get("TradeSerialNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSinglePaymentRequest(AbstractModel):
    """CreateSinglePayment请求参数结构体

    """

    def __init__(self):
        r"""
        :param TransferType: 转账类型
        :type TransferType: int
        :param OrderId: 订单流水号
        :type OrderId: str
        :param TransferAmount: 转账金额
        :type TransferAmount: int
        :param AnchorId: 主播ID（与主播业务ID不能同时为空，两者都填取主播ID）
        :type AnchorId: str
        :param ReqReserved: 请求预留字段，原样透传返回
        :type ReqReserved: str
        :param Remark: 业务备注
        :type Remark: str
        :param AnchorName: 主播名称。如果该字段填入，则会对AnchorName和AnchorId/Uid进行校验。
        :type AnchorName: str
        :param Uid: 主播业务ID（与主播ID不能同时为空，两者都填取主播ID）
        :type Uid: str
        :param NotifyUrl: 转账结果回调通知URL。若不填，则不进行回调。
        :type NotifyUrl: str
        """
        self.TransferType = None
        self.OrderId = None
        self.TransferAmount = None
        self.AnchorId = None
        self.ReqReserved = None
        self.Remark = None
        self.AnchorName = None
        self.Uid = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.TransferType = params.get("TransferType")
        self.OrderId = params.get("OrderId")
        self.TransferAmount = params.get("TransferAmount")
        self.AnchorId = params.get("AnchorId")
        self.ReqReserved = params.get("ReqReserved")
        self.Remark = params.get("Remark")
        self.AnchorName = params.get("AnchorName")
        self.Uid = params.get("Uid")
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSinglePaymentResponse(AbstractModel):
    """CreateSinglePayment返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码
        :type ErrCode: str
        :param ErrMessage: 响应消息
        :type ErrMessage: str
        :param Result: 返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateSinglePaymentData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = CreateSinglePaymentData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTransferBatchRequest(AbstractModel):
    """CreateTransferBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号。
示例值：129284394
        :type MerchantId: str
        :param TransferDetails: 转账明细列表。
发起批量转账的明细列表，最多三千笔
        :type TransferDetails: list of TransferDetailRequest
        :param MerchantAppId: 直连商户appId。
即商户号绑定的appid。
示例值：wxf636efh567hg4356
        :type MerchantAppId: str
        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013
        :type MerchantBatchNo: str
        :param BatchName: 批次名称。
批量转账的名称。
示例值：2019年1月深圳分部报销单
        :type BatchName: str
        :param BatchRemark: 转账说明。
UTF8编码，最多32个字符。
示例值：2019年深圳分部报销单
        :type BatchRemark: str
        :param TotalAmount: 转账总金额。
转账金额，单位为分。
示例值：4000000
        :type TotalAmount: int
        :param TotalNum: 转账总笔数。
一个转账批次最多允许发起三千笔转账。
示例值：200
        :type TotalNum: int
        :param Profile: 环境名。
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type Profile: str
        """
        self.MerchantId = None
        self.TransferDetails = None
        self.MerchantAppId = None
        self.MerchantBatchNo = None
        self.BatchName = None
        self.BatchRemark = None
        self.TotalAmount = None
        self.TotalNum = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        if params.get("TransferDetails") is not None:
            self.TransferDetails = []
            for item in params.get("TransferDetails"):
                obj = TransferDetailRequest()
                obj._deserialize(item)
                self.TransferDetails.append(obj)
        self.MerchantAppId = params.get("MerchantAppId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchName = params.get("BatchName")
        self.BatchRemark = params.get("BatchRemark")
        self.TotalAmount = params.get("TotalAmount")
        self.TotalNum = params.get("TotalNum")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTransferBatchResponse(AbstractModel):
    """CreateTransferBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013
        :type MerchantBatchNo: str
        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
示例值：1030000071100999991182020050700019480001
        :type BatchId: str
        :param CreateTime: 批次受理成功时返回，遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
        :type CreateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantBatchNo = None
        self.BatchId = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DeduceQuotaRequest(AbstractModel):
    """DeduceQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播ID
        :type AnchorId: str
        :param Amount: 提现金额，单位为"分"
        :type Amount: int
        :param OrderId: 外部业务订单号
        :type OrderId: str
        """
        self.AnchorId = None
        self.Amount = None
        self.OrderId = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.Amount = params.get("Amount")
        self.OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeduceQuotaResponse(AbstractModel):
    """DeduceQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMsg: 响应消息
        :type ErrMsg: str
        :param Result: 返回响应
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.AssignmentData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMsg = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("Result") is not None:
            self.Result = AssignmentData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAgentTaxPaymentInfoRequest(AbstractModel):
    """DeleteAgentTaxPaymentInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchNum: 批次号
        :type BatchNum: int
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.BatchNum = None
        self.Profile = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentTaxPaymentInfoResponse(AbstractModel):
    """DeleteAgentTaxPaymentInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAgentTaxPaymentInfosRequest(AbstractModel):
    """DeleteAgentTaxPaymentInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchNum: 批次号
        :type BatchNum: int
        """
        self.BatchNum = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentTaxPaymentInfosResponse(AbstractModel):
    """DeleteAgentTaxPaymentInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeChargeDetailRequest(AbstractModel):
    """DescribeChargeDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型
        :type RequestType: str
        :param MerchantCode: 商户号
        :type MerchantCode: str
        :param PayChannel: 支付渠道
        :type PayChannel: str
        :param PayChannelSubId: 子渠道
        :type PayChannelSubId: int
        :param OrderId: 原始交易订单号或者流水号
        :type OrderId: str
        :param BankAccountNumber: 父账户账号，资金汇总账号
        :type BankAccountNumber: str
        :param AcquiringChannelType: 收单渠道类型
        :type AcquiringChannelType: str
        :param PlatformShortNumber: 平台短号(银行分配)
        :type PlatformShortNumber: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param TransSequenceNumber: 交易流水号
        :type TransSequenceNumber: str
        :param MidasEnvironment: Midas环境参数
        :type MidasEnvironment: str
        :param ReservedMessage: 保留域
        :type ReservedMessage: str
        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.AcquiringChannelType = None
        self.PlatformShortNumber = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.MidasEnvironment = None
        self.ReservedMessage = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.AcquiringChannelType = params.get("AcquiringChannelType")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChargeDetailResponse(AbstractModel):
    """DescribeChargeDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param OrderStatus: 交易状态 （0：成功，1：失败，2：异常,3:冲正，5：待处理）
        :type OrderStatus: str
        :param OrderAmount: 交易金额
        :type OrderAmount: str
        :param CommissionAmount: 佣金费
        :type CommissionAmount: str
        :param PayMode: 支付方式  0-冻结支付 1-普通支付
        :type PayMode: str
        :param OrderDate: 交易日期
        :type OrderDate: str
        :param OrderTime: 交易时间
        :type OrderTime: str
        :param OrderActualInSubAccountName: 订单实际转入见证子账户的名称
        :type OrderActualInSubAccountName: str
        :param OrderActualInSubAccountNumber: 订单实际转入见证子账户的帐号
        :type OrderActualInSubAccountNumber: str
        :param OrderInSubAccountName: 订单实际转入见证子账户的帐号
        :type OrderInSubAccountName: str
        :param OrderInSubAccountNumber: 订单转入见证子账户的帐号
        :type OrderInSubAccountNumber: str
        :param FrontSequenceNumber: 银行流水号
        :type FrontSequenceNumber: str
        :param FailMessage: 当充值失败时，返回交易失败原因
        :type FailMessage: str
        :param RequestType: 请求类型
        :type RequestType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrderStatus = None
        self.OrderAmount = None
        self.CommissionAmount = None
        self.PayMode = None
        self.OrderDate = None
        self.OrderTime = None
        self.OrderActualInSubAccountName = None
        self.OrderActualInSubAccountNumber = None
        self.OrderInSubAccountName = None
        self.OrderInSubAccountNumber = None
        self.FrontSequenceNumber = None
        self.FailMessage = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderStatus = params.get("OrderStatus")
        self.OrderAmount = params.get("OrderAmount")
        self.CommissionAmount = params.get("CommissionAmount")
        self.PayMode = params.get("PayMode")
        self.OrderDate = params.get("OrderDate")
        self.OrderTime = params.get("OrderTime")
        self.OrderActualInSubAccountName = params.get("OrderActualInSubAccountName")
        self.OrderActualInSubAccountNumber = params.get("OrderActualInSubAccountNumber")
        self.OrderInSubAccountName = params.get("OrderInSubAccountName")
        self.OrderInSubAccountNumber = params.get("OrderInSubAccountNumber")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.FailMessage = params.get("FailMessage")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class DescribeOrderStatusRequest(AbstractModel):
    """DescribeOrderStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型，此接口固定填：QueryOrderStatusReq
        :type RequestType: str
        :param MerchantCode: 商户号
        :type MerchantCode: str
        :param PayChannel: 支付渠道
        :type PayChannel: str
        :param PayChannelSubId: 子渠道
        :type PayChannelSubId: int
        :param OrderId: 交易订单号或流水号，提现，充值或会员交易请求时的CnsmrSeqNo值
        :type OrderId: str
        :param BankAccountNumber: 父账户账号，资金汇总账号
        :type BankAccountNumber: str
        :param PlatformShortNumber: 平台短号(银行分配)
        :type PlatformShortNumber: str
        :param QueryType: 功能标志 0：会员间交易 1：提现 2：充值
        :type QueryType: str
        :param TransSequenceNumber: 银行流水号
        :type TransSequenceNumber: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasEnvironment: Midas环境参数
        :type MidasEnvironment: str
        :param ReservedMessage: 保留字段
        :type ReservedMessage: str
        :param BankSubAccountNumber: 子账户账号 暂未使用
        :type BankSubAccountNumber: str
        :param TransDate: 交易日期 暂未使用
        :type TransDate: str
        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.PlatformShortNumber = None
        self.QueryType = None
        self.TransSequenceNumber = None
        self.MidasSignature = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasEnvironment = None
        self.ReservedMessage = None
        self.BankSubAccountNumber = None
        self.TransDate = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.QueryType = params.get("QueryType")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        self.BankSubAccountNumber = params.get("BankSubAccountNumber")
        self.TransDate = params.get("TransDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrderStatusResponse(AbstractModel):
    """DescribeOrderStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param OrderStatus: 交易状态 （0：成功，1：失败，2：待确认, 5：待处理，6：处理中）
        :type OrderStatus: str
        :param OrderAmount: 交易金额
        :type OrderAmount: str
        :param OrderDate: 交易日期
        :type OrderDate: str
        :param OrderTime: 交易时间
        :type OrderTime: str
        :param OutSubAccountNumber: 转出子账户账号
        :type OutSubAccountNumber: str
        :param InSubAccountNumber: 转入子账户账号
        :type InSubAccountNumber: str
        :param BookingFlag: 记账标志（1：登记挂账 2：支付 3：提现 4：清分5:下单预支付 6：确认并付款 7：退款 8：支付到平台 N:其他）
        :type BookingFlag: str
        :param FailMessage: 当交易失败时，返回交易失败原因
        :type FailMessage: str
        :param RequestType: 请求类型
        :type RequestType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrderStatus = None
        self.OrderAmount = None
        self.OrderDate = None
        self.OrderTime = None
        self.OutSubAccountNumber = None
        self.InSubAccountNumber = None
        self.BookingFlag = None
        self.FailMessage = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderStatus = params.get("OrderStatus")
        self.OrderAmount = params.get("OrderAmount")
        self.OrderDate = params.get("OrderDate")
        self.OrderTime = params.get("OrderTime")
        self.OutSubAccountNumber = params.get("OutSubAccountNumber")
        self.InSubAccountNumber = params.get("InSubAccountNumber")
        self.BookingFlag = params.get("BookingFlag")
        self.FailMessage = params.get("FailMessage")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class DistributeAccreditQueryRequest(AbstractModel):
    """DistributeAccreditQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeAccreditQueryResponse(AbstractModel):
    """DistributeAccreditQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 查询授权申请结果响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeAccreditQueryResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeAccreditQueryResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DistributeAccreditQueryResult(AbstractModel):
    """分账授权申请查询响应对象

    """

    def __init__(self):
        r"""
        :param Status: 状态（0-未开通，1-已开通，2-商户主动关闭，3-待审核，4-冻结，5-注销，6-待签合同）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ContractUrl: 合同h5地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractUrl: str
        :param Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.Status = None
        self.ContractUrl = None
        self.Remark = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ContractUrl = params.get("ContractUrl")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeAccreditResult(AbstractModel):
    """授权申请响应对象

    """

    def __init__(self):
        r"""
        :param ContractUrl: 合同h5地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractUrl: str
        :param MerchantNo: 系统商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        """
        self.ContractUrl = None
        self.MerchantNo = None


    def _deserialize(self, params):
        self.ContractUrl = params.get("ContractUrl")
        self.MerchantNo = params.get("MerchantNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeAccreditTlinxRequest(AbstractModel):
    """DistributeAccreditTlinx请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param AuthType: 验证方式，传1手机验证(验证码时效60S)传2结算卡验证(时效6小时)，多种方式用逗号隔开
        :type AuthType: str
        :param Percent: 分账比例（500=5%）不传默认百分之10
        :type Percent: str
        :param FullName: 营业执照商户全称
        :type FullName: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.AuthType = None
        self.Percent = None
        self.FullName = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.AuthType = params.get("AuthType")
        self.Percent = params.get("Percent")
        self.FullName = params.get("FullName")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeAccreditTlinxResponse(AbstractModel):
    """DistributeAccreditTlinx返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 授权申请响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeAccreditResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeAccreditResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DistributeAddReceiverRequest(AbstractModel):
    """DistributeAddReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param MerchantNo: 商户编号
        :type MerchantNo: str
        :param Remark: 备注
        :type Remark: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.MerchantNo = None
        self.Remark = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.MerchantNo = params.get("MerchantNo")
        self.Remark = params.get("Remark")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeAddReceiverResponse(AbstractModel):
    """DistributeAddReceiver返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 添加分账接收方响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeReceiverResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeReceiverResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DistributeApplyRequest(AbstractModel):
    """DistributeApply请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param OutDistributeNo: 商户分账单号
        :type OutDistributeNo: str
        :param Details: 分账明细
        :type Details: list of MultiApplyDetail
        :param DeveloperNo: 商户交易订单号，和OrderNo二者传其一
        :type DeveloperNo: str
        :param OrderNo: 平台交易订单号，和DeveloperNo二者传其一
        :type OrderNo: str
        :param Remark: 说明
        :type Remark: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OutDistributeNo = None
        self.Details = None
        self.DeveloperNo = None
        self.OrderNo = None
        self.Remark = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OutDistributeNo = params.get("OutDistributeNo")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = MultiApplyDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.DeveloperNo = params.get("DeveloperNo")
        self.OrderNo = params.get("OrderNo")
        self.Remark = params.get("Remark")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeApplyResponse(AbstractModel):
    """DistributeApply返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 分账申请响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeMultiApplyResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeMultiApplyResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DistributeCancelRequest(AbstractModel):
    """DistributeCancel请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param OrderNo: 平台交易订单号
        :type OrderNo: str
        :param OutDistributeNo: 商户分账单号，type为2时，和DistributeNo二者传其一
        :type OutDistributeNo: str
        :param DistributeNo: 平台分账单号，type为2时，和OutDistributeNo二者传其一
        :type DistributeNo: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OrderNo = None
        self.OutDistributeNo = None
        self.DistributeNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OrderNo = params.get("OrderNo")
        self.OutDistributeNo = params.get("OutDistributeNo")
        self.DistributeNo = params.get("DistributeNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeCancelResponse(AbstractModel):
    """DistributeCancel返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 分账撤销响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeCancelResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeCancelResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DistributeCancelResult(AbstractModel):
    """分账撤销响应对象

    """

    def __init__(self):
        r"""
        :param Status: 分账订单状态（0初始1成功2失败3撤销）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param OrderNo: 平台交易订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param OutDistributeNo: 商户分账单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutDistributeNo: str
        :param DistributeNo: 平台分账单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributeNo: str
        """
        self.Status = None
        self.OrderNo = None
        self.OutDistributeNo = None
        self.DistributeNo = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.OrderNo = params.get("OrderNo")
        self.OutDistributeNo = params.get("OutDistributeNo")
        self.DistributeNo = params.get("DistributeNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeMultiApplyResult(AbstractModel):
    """分账申请响应对象

    """

    def __init__(self):
        r"""
        :param Status: 分账状态（0分账初始 1分账成功 2分账失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param DistributeNo: 平台分账单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributeNo: str
        :param InDate: 入账日期，yyyy-MM-dd格式
注意：此字段可能返回 null，表示取不到有效值。
        :type InDate: str
        :param Amount: 分账金额
注意：此字段可能返回 null，表示取不到有效值。
        :type Amount: str
        :param OutDistributeNo: 商户分账单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutDistributeNo: str
        :param OrderNo: 平台支付单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        """
        self.Status = None
        self.DistributeNo = None
        self.InDate = None
        self.Amount = None
        self.OutDistributeNo = None
        self.OrderNo = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.DistributeNo = params.get("DistributeNo")
        self.InDate = params.get("InDate")
        self.Amount = params.get("Amount")
        self.OutDistributeNo = params.get("OutDistributeNo")
        self.OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeQueryReceiverRequest(AbstractModel):
    """DistributeQueryReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeQueryReceiverResponse(AbstractModel):
    """DistributeQueryReceiver返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 查询询已添加分账接收方响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeReceiverResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeReceiverResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DistributeQueryRequest(AbstractModel):
    """DistributeQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param Type: 查询类型（1-全部，2-单笔）
        :type Type: str
        :param OutDistributeNo: 商户分账单号，type为2时，和DistributeNo二者传其一
        :type OutDistributeNo: str
        :param DistributeNo: 平台分账单号，type为2时，和OutDistributeNo二者传其一
        :type DistributeNo: str
        :param OrderNo: 平台交易订单号
        :type OrderNo: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Type = None
        self.OutDistributeNo = None
        self.DistributeNo = None
        self.OrderNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Type = params.get("Type")
        self.OutDistributeNo = params.get("OutDistributeNo")
        self.DistributeNo = params.get("DistributeNo")
        self.OrderNo = params.get("OrderNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeQueryResponse(AbstractModel):
    """DistributeQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 分账结果响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeQueryResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeQueryResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DistributeQueryResult(AbstractModel):
    """分账结果响应对象

    """

    def __init__(self):
        r"""
        :param Orders: 分账订单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Orders: list of MultiApplyOrder
        """
        self.Orders = None


    def _deserialize(self, params):
        if params.get("Orders") is not None:
            self.Orders = []
            for item in params.get("Orders"):
                obj = MultiApplyOrder()
                obj._deserialize(item)
                self.Orders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeReceiverResult(AbstractModel):
    """分账接收方响应对象

    """

    def __init__(self):
        r"""
        :param MerchantNo: 商户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        """
        self.MerchantNo = None


    def _deserialize(self, params):
        self.MerchantNo = params.get("MerchantNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeRemoveReceiverRequest(AbstractModel):
    """DistributeRemoveReceiver请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param MerchantNo: 商户编号
        :type MerchantNo: str
        :param Remark: 备注
        :type Remark: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.MerchantNo = None
        self.Remark = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.MerchantNo = params.get("MerchantNo")
        self.Remark = params.get("Remark")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DistributeRemoveReceiverResponse(AbstractModel):
    """DistributeRemoveReceiver返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 解除分账接收方响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DistributeReceiverResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DistributeReceiverResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DownloadBillRequest(AbstractModel):
    """DownloadBill请求参数结构体

    """

    def __init__(self):
        r"""
        :param StateDate: 请求下载对账单日期
        :type StateDate: str
        :param MidasAppId: 聚鑫分配的MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的SecretId
        :type MidasSecretId: str
        :param MidasSignature: 使用聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.StateDate = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.StateDate = params.get("StateDate")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadBillResponse(AbstractModel):
    """DownloadBill返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileName: 账单文件名
        :type FileName: str
        :param FileMD5: 账单文件的MD5值
        :type FileMD5: str
        :param DownloadUrl: 账单文件的真实下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileName = None
        self.FileMD5 = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileMD5 = params.get("FileMD5")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DownloadFileResult(AbstractModel):
    """上传下载响应对象

    """

    def __init__(self):
        r"""
        :param Content: 文件内容（base64加密的二进制内容）
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param Storage: 存储区域（0私密区，1公共区），请严格按文件要求，上传到不同的区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Storage: str
        """
        self.Content = None
        self.Storage = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Storage = params.get("Storage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadOrgFileRequest(AbstractModel):
    """DownloadOrgFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param Storage: 存储区域（0私密区，1公共区），请严格按文件要求，上传到不同的区域
        :type Storage: str
        :param FilePath: 文件路径
        :type FilePath: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Storage = None
        self.FilePath = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Storage = params.get("Storage")
        self.FilePath = params.get("FilePath")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadOrgFileResponse(AbstractModel):
    """DownloadOrgFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 下载机构文件响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.DownloadFileResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = DownloadFileResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DownloadReconciliationUrlRequest(AbstractModel):
    """DownloadReconciliationUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param MainAppId: 平台应用ID
        :type MainAppId: str
        :param AppCode: 平台代码
        :type AppCode: str
        :param BillDate: 账单日期，yyyy-MM-dd
        :type BillDate: str
        :param SubAppId: 商户或者代理商ID
        :type SubAppId: str
        """
        self.MainAppId = None
        self.AppCode = None
        self.BillDate = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.MainAppId = params.get("MainAppId")
        self.AppCode = params.get("AppCode")
        self.BillDate = params.get("BillDate")
        self.SubAppId = params.get("SubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadReconciliationUrlResponse(AbstractModel):
    """DownloadReconciliationUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param HashType: hash类型
注意：此字段可能返回 null，表示取不到有效值。
        :type HashType: str
        :param HashValue: hash值
        :type HashValue: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.HashType = None
        self.HashValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.HashType = params.get("HashType")
        self.HashValue = params.get("HashValue")
        self.RequestId = params.get("RequestId")


class ExecuteMemberTransactionRequest(AbstractModel):
    """ExecuteMemberTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型此接口固定填：MemberTransactionReq
        :type RequestType: str
        :param MerchantCode: 银行注册商户号
        :type MerchantCode: str
        :param PayChannel: 支付渠道
        :type PayChannel: str
        :param PayChannelSubId: 子渠道
        :type PayChannelSubId: int
        :param OutTransNetMemberCode: 转出交易网会员代码
        :type OutTransNetMemberCode: str
        :param OutSubAccountName: 转出见证子账户的户名
        :type OutSubAccountName: str
        :param InSubAccountName: 转入见证子账户的户名
        :type InSubAccountName: str
        :param OutSubAccountNumber: 转出子账户账号
        :type OutSubAccountNumber: str
        :param InSubAccountNumber: 转入子账户账号
        :type InSubAccountNumber: str
        :param BankAccountNumber: 父账户账号，资金汇总账号
        :type BankAccountNumber: str
        :param CurrencyUnit: 货币单位 单位，1：元，2：角，3：分
        :type CurrencyUnit: str
        :param CurrencyType: 币种
        :type CurrencyType: str
        :param CurrencyAmount: 交易金额
        :type CurrencyAmount: str
        :param OrderId: 订单号
        :type OrderId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param TransSequenceNumber: 交易流水号 
生成方式：用户短号+日期（6位）+ 随机编号（10位）例如：F088722005120904930798
短号：F08872  日期： 200512   随机编号：0904930798
        :type TransSequenceNumber: str
        :param InTransNetMemberCode: 转入交易网会员代码
        :type InTransNetMemberCode: str
        :param MidasEnvironment: Midas环境标识 release 现网环境 sandbox 沙箱环境
development 开发环境
        :type MidasEnvironment: str
        :param PlatformShortNumber: 平台短号(银行分配)
        :type PlatformShortNumber: str
        :param TransType: 1：下单预支付 
2：确认并付款
3：退款
6：直接支付T+1
9：直接支付T+0
        :type TransType: str
        :param TransFee: 交易手续费
        :type TransFee: str
        :param ReservedMessage: 保留域
        :type ReservedMessage: str
        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OutTransNetMemberCode = None
        self.OutSubAccountName = None
        self.InSubAccountName = None
        self.OutSubAccountNumber = None
        self.InSubAccountNumber = None
        self.BankAccountNumber = None
        self.CurrencyUnit = None
        self.CurrencyType = None
        self.CurrencyAmount = None
        self.OrderId = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.InTransNetMemberCode = None
        self.MidasEnvironment = None
        self.PlatformShortNumber = None
        self.TransType = None
        self.TransFee = None
        self.ReservedMessage = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OutTransNetMemberCode = params.get("OutTransNetMemberCode")
        self.OutSubAccountName = params.get("OutSubAccountName")
        self.InSubAccountName = params.get("InSubAccountName")
        self.OutSubAccountNumber = params.get("OutSubAccountNumber")
        self.InSubAccountNumber = params.get("InSubAccountNumber")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.OrderId = params.get("OrderId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.InTransNetMemberCode = params.get("InTransNetMemberCode")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.TransType = params.get("TransType")
        self.TransFee = params.get("TransFee")
        self.ReservedMessage = params.get("ReservedMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteMemberTransactionResponse(AbstractModel):
    """ExecuteMemberTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型
        :type RequestType: str
        :param FrontSequenceNumber: 银行流水号
        :type FrontSequenceNumber: str
        :param ReservedMessage: 保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestType = None
        self.FrontSequenceNumber = None
        self.ReservedMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.ReservedMessage = params.get("ReservedMessage")
        self.RequestId = params.get("RequestId")


class ExternalContractUserInfo(AbstractModel):
    """第三方渠道用户信息

    """

    def __init__(self):
        r"""
        :param ExternalUserType: 第三方用户类型，例如:  WX_OPENID, WX_SUB_OPENID,WX_PAYER_OPENID
        :type ExternalUserType: str
        :param ExternalUserId: 第三方用户ID
        :type ExternalUserId: str
        """
        self.ExternalUserType = None
        self.ExternalUserId = None


    def _deserialize(self, params):
        self.ExternalUserType = params.get("ExternalUserType")
        self.ExternalUserId = params.get("ExternalUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalReturnContractInfo(AbstractModel):
    """第三方渠道合约信息

    """

    def __init__(self):
        r"""
        :param ExternalReturnAgreementId: 第三方渠道协议id
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnAgreementId: str
        :param ExternalReturnContractEffectiveTimestamp: 第三方渠道协议生效时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractEffectiveTimestamp: str
        :param ExternalReturnContractTerminationTimestamp: 第三方渠道协议解约时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractTerminationTimestamp: str
        :param ExternalReturnContractStatus: 平台合约状态
协议状态，枚举值：
CONTRACT_STATUS_SIGNED：已签约
CONTRACT_STATUS_TERMINATED：未签约
CONTRACT_STATUS_PENDING：签约进行中
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractStatus: str
        :param ExternalReturnRequestId: 第三方渠道请求序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnRequestId: str
        :param ExternalReturnContractSignedTimestamp: 第三方渠道协议签署时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractSignedTimestamp: str
        :param ExternalReturnContractExpiredTimestamp: 第三方渠道协议到期时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractExpiredTimestamp: str
        :param ExternalReturnContractData: 第三方渠道返回的合约数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractData: str
        :param ExternalReturnContractTerminationRemark: 第三方渠道解约备注
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractTerminationRemark: str
        :param ExternalReturnContractTerminationMode: 第三方渠道协议解约方式
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnContractTerminationMode: str
        """
        self.ExternalReturnAgreementId = None
        self.ExternalReturnContractEffectiveTimestamp = None
        self.ExternalReturnContractTerminationTimestamp = None
        self.ExternalReturnContractStatus = None
        self.ExternalReturnRequestId = None
        self.ExternalReturnContractSignedTimestamp = None
        self.ExternalReturnContractExpiredTimestamp = None
        self.ExternalReturnContractData = None
        self.ExternalReturnContractTerminationRemark = None
        self.ExternalReturnContractTerminationMode = None


    def _deserialize(self, params):
        self.ExternalReturnAgreementId = params.get("ExternalReturnAgreementId")
        self.ExternalReturnContractEffectiveTimestamp = params.get("ExternalReturnContractEffectiveTimestamp")
        self.ExternalReturnContractTerminationTimestamp = params.get("ExternalReturnContractTerminationTimestamp")
        self.ExternalReturnContractStatus = params.get("ExternalReturnContractStatus")
        self.ExternalReturnRequestId = params.get("ExternalReturnRequestId")
        self.ExternalReturnContractSignedTimestamp = params.get("ExternalReturnContractSignedTimestamp")
        self.ExternalReturnContractExpiredTimestamp = params.get("ExternalReturnContractExpiredTimestamp")
        self.ExternalReturnContractData = params.get("ExternalReturnContractData")
        self.ExternalReturnContractTerminationRemark = params.get("ExternalReturnContractTerminationRemark")
        self.ExternalReturnContractTerminationMode = params.get("ExternalReturnContractTerminationMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeeRangInfo(AbstractModel):
    """分段计费区间信息

    """

    def __init__(self):
        r"""
        :param CardType: 卡类型，银联产品使用 
DEBIT：借记卡 
CREDIT：贷记卡
        :type CardType: str
        :param RangeStartValue: 区间起始金额，单位（分）
        :type RangeStartValue: int
        :param RangeEndValue: 区间结束金额，单位（分）
        :type RangeEndValue: int
        :param RangeFeeMode: 分段计费模式 
SINGLE：按金额计费 
RATIO：按费率计费
        :type RangeFeeMode: str
        :param FeeValue: 费用值，单位（0.01%或分）
        :type FeeValue: int
        :param MinFee: 最低收费金额，单位（分）
        :type MinFee: int
        :param MaxFee: 最高收费金额，单位（分）
        :type MaxFee: int
        """
        self.CardType = None
        self.RangeStartValue = None
        self.RangeEndValue = None
        self.RangeFeeMode = None
        self.FeeValue = None
        self.MinFee = None
        self.MaxFee = None


    def _deserialize(self, params):
        self.CardType = params.get("CardType")
        self.RangeStartValue = params.get("RangeStartValue")
        self.RangeEndValue = params.get("RangeEndValue")
        self.RangeFeeMode = params.get("RangeFeeMode")
        self.FeeValue = params.get("FeeValue")
        self.MinFee = params.get("MinFee")
        self.MaxFee = params.get("MaxFee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileItem(AbstractModel):
    """对账文件信息

    """

    def __init__(self):
        r"""
        :param FileName: STRING(256)，文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param RandomPassword: STRING(120)，随机密码
注意：此字段可能返回 null，表示取不到有效值。
        :type RandomPassword: str
        :param FilePath: STRING(512)，文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param DrawCode: STRING(64)，提取码
注意：此字段可能返回 null，表示取不到有效值。
        :type DrawCode: str
        """
        self.FileName = None
        self.RandomPassword = None
        self.FilePath = None
        self.DrawCode = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.RandomPassword = params.get("RandomPassword")
        self.FilePath = params.get("FilePath")
        self.DrawCode = params.get("DrawCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlexFundingAccountInfo(AbstractModel):
    """灵云V2-银行信息

    """

    def __init__(self):
        r"""
        :param FundingAccountNo: 资金账户号
        :type FundingAccountNo: str
        :param FundingAccountType: 资金账户类型
        :type FundingAccountType: str
        :param FundingAccountBindSerialNo: 资金账户绑定序列号
        :type FundingAccountBindSerialNo: str
        """
        self.FundingAccountNo = None
        self.FundingAccountType = None
        self.FundingAccountBindSerialNo = None


    def _deserialize(self, params):
        self.FundingAccountNo = params.get("FundingAccountNo")
        self.FundingAccountType = params.get("FundingAccountType")
        self.FundingAccountBindSerialNo = params.get("FundingAccountBindSerialNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeFlexBalanceRequest(AbstractModel):
    """FreezeFlexBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        :param OutOrderId: 外部订单ID
        :type OutOrderId: str
        :param OperationType: 操作类型
FREEZE:冻结
UNFREEZE:解冻
        :type OperationType: str
        :param Remark: 冻结备注
        :type Remark: str
        """
        self.PayeeId = None
        self.AmountBeforeTax = None
        self.IncomeType = None
        self.OutOrderId = None
        self.OperationType = None
        self.Remark = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.IncomeType = params.get("IncomeType")
        self.OutOrderId = params.get("OutOrderId")
        self.OperationType = params.get("OperationType")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeFlexBalanceResponse(AbstractModel):
    """FreezeFlexBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.FreezeFlexBalanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = FreezeFlexBalanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class FreezeFlexBalanceResult(AbstractModel):
    """冻结余额结果

    """

    def __init__(self):
        r"""
        :param OrderId: 冻结订单ID
        :type OrderId: str
        """
        self.OrderId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeOrderResult(AbstractModel):
    """冻结单结果

    """

    def __init__(self):
        r"""
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        :param OutOrderId: 外部订单ID
        :type OutOrderId: str
        :param OrderId: 订单ID
        :type OrderId: str
        :param OperationType: 操作类型
FREEZE:冻结
UNFREEZE:解冻
        :type OperationType: str
        :param InitiateTime: 发起时间
        :type InitiateTime: str
        :param FinishTime: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        :param Status: 状态
ACCEPTED:已受理
ACCOUNTED:已记账
SUCCEED:已成功
FAILED:已失败
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        :param Remark: 冻结备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.AmountBeforeTax = None
        self.IncomeType = None
        self.OutOrderId = None
        self.OrderId = None
        self.OperationType = None
        self.InitiateTime = None
        self.FinishTime = None
        self.Status = None
        self.StatusDesc = None
        self.Remark = None


    def _deserialize(self, params):
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.IncomeType = params.get("IncomeType")
        self.OutOrderId = params.get("OutOrderId")
        self.OrderId = params.get("OrderId")
        self.OperationType = params.get("OperationType")
        self.InitiateTime = params.get("InitiateTime")
        self.FinishTime = params.get("FinishTime")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FreezeOrders(AbstractModel):
    """冻结订单列表

    """

    def __init__(self):
        r"""
        :param List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of FreezeOrderResult
        :param Count: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.List = None
        self.Count = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = FreezeOrderResult()
                obj._deserialize(item)
                self.List.append(obj)
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FundsTransactionItem(AbstractModel):
    """会员资金交易明细信息

    """

    def __init__(self):
        r"""
        :param TransType: 资金交易类型。
__1__：提现/退款
__2__：清分/充值
        :type TransType: str
        :param BankBookingMessage: 银行记账说明。
注意：此字段可能返回 null，表示取不到有效值。
        :type BankBookingMessage: str
        :param TranStatus: 交易状态。
__0__：成功
        :type TranStatus: str
        :param TransNetMemberCode: 业务方会员标识。
_平安渠道为交易网会员代码_
注意：此字段可能返回 null，表示取不到有效值。
        :type TransNetMemberCode: str
        :param SubAccountNumber: 子账户账号。
_平安渠道为见证子账户的账号_
        :type SubAccountNumber: str
        :param SubAccountName: 子账户名称。
_平安渠道为见证子账户的户名_
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountName: str
        :param TransAmount: 交易金额。
        :type TransAmount: str
        :param TransFee: 交易手续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransFee: str
        :param TransDate: 交易日期，格式：yyyyMMdd。
        :type TransDate: str
        :param TransTime: 交易时间，格式：HHmmss。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransTime: str
        :param BankSequenceNumber: 银行系统流水号。
_平安渠道为见证系统流水号_
        :type BankSequenceNumber: str
        :param Remark: 备注。
_平安渠道，如果是见证+收单的交易，返回交易订单号_
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.TransType = None
        self.BankBookingMessage = None
        self.TranStatus = None
        self.TransNetMemberCode = None
        self.SubAccountNumber = None
        self.SubAccountName = None
        self.TransAmount = None
        self.TransFee = None
        self.TransDate = None
        self.TransTime = None
        self.BankSequenceNumber = None
        self.Remark = None


    def _deserialize(self, params):
        self.TransType = params.get("TransType")
        self.BankBookingMessage = params.get("BankBookingMessage")
        self.TranStatus = params.get("TranStatus")
        self.TransNetMemberCode = params.get("TransNetMemberCode")
        self.SubAccountNumber = params.get("SubAccountNumber")
        self.SubAccountName = params.get("SubAccountName")
        self.TransAmount = params.get("TransAmount")
        self.TransFee = params.get("TransFee")
        self.TransDate = params.get("TransDate")
        self.TransTime = params.get("TransTime")
        self.BankSequenceNumber = params.get("BankSequenceNumber")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBillDownloadUrlRequest(AbstractModel):
    """GetBillDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param Day: 清算日期（YYYYMMDD，今天传昨天的日期，每日下午1点后出前一日的账单）
        :type Day: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Day = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Day = params.get("Day")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetBillDownloadUrlResponse(AbstractModel):
    """GetBillDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 账单文件下载地址响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.BillDownloadUrlResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = BillDownloadUrlResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class GetDistributeBillDownloadUrlRequest(AbstractModel):
    """GetDistributeBillDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param Day: 分账日期（YYYYMMDD，今天传昨天的日期）
        :type Day: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Day = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Day = params.get("Day")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDistributeBillDownloadUrlResponse(AbstractModel):
    """GetDistributeBillDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 账单文件下载地址响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.BillDownloadUrlResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = BillDownloadUrlResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class GetPayRollAuthListRequest(AbstractModel):
    """GetPayRollAuthList请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param AuthDate: 核身日期，一次只能查询一天，最久可查询90天内的记录，格式为YYYY-MM-DD
        :type AuthDate: str
        :param Offset: 非负整数，表示该次请求资源的起始位置，从0开始计数
        :type Offset: int
        :param Limit: 非0非负的整数，该次请求可返回的最大资源条数，默认值为10，最大支持10条
        :type Limit: int
        :param WechatAppId: 是服务商在微信申请公众号/小程序或移动应用成功后分配的账号ID（与服务商主体一致）
当输入服务商Appid时，会校验其与服务商商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatAppId: str
        :param WechatSubAppId: 特约商户在微信申请公众号/小程序或移动应用成功后分配的账号ID（与特约商户主体一致）
当输入特约商户Appid时，会校验其与特约商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatSubAppId: str
        :param AuthStatus: 核身状态，列表查询仅提供成功状态的核身记录查询，故此字段固定AUTHENTICATE_SUCCESS即可
        :type AuthStatus: str
        """
        self.OpenId = None
        self.SubMerchantId = None
        self.AuthDate = None
        self.Offset = None
        self.Limit = None
        self.WechatAppId = None
        self.WechatSubAppId = None
        self.AuthStatus = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.AuthDate = params.get("AuthDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.WechatAppId = params.get("WechatAppId")
        self.WechatSubAppId = params.get("WechatSubAppId")
        self.AuthStatus = params.get("AuthStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPayRollAuthListResponse(AbstractModel):
    """GetPayRollAuthList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Results: 核身结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of PayRollAuthResult
        :param Total: 总记录条数
        :type Total: int
        :param Offset: 记录起始位置，该次请求资源的起始位置，请求中包含偏移量时应答消息返回相同偏移量，否则返回默认值0
        :type Offset: int
        :param Limit: 本次返回条数
        :type Limit: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.Total = None
        self.Offset = None
        self.Limit = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = PayRollAuthResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.Total = params.get("Total")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RequestId = params.get("RequestId")


class GetPayRollAuthRequest(AbstractModel):
    """GetPayRollAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param WechatAppId: 是服务商在微信申请公众号/小程序或移动应用成功后分配的账号ID（与服务商主体一致）
当输入服务商Appid时，会校验其与服务商商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatAppId: str
        :param WechatSubAppId: 特约商户在微信申请公众号/小程序或移动应用成功后分配的账号ID（与特约商户主体一致）
当输入特约商户Appid时，会校验其与特约商户号的绑定关系。服务商APPID和与特约商户APPID至少输入一个，且必须要有拉起领薪卡小程序时使用的APPID
        :type WechatSubAppId: str
        """
        self.OpenId = None
        self.SubMerchantId = None
        self.WechatAppId = None
        self.WechatSubAppId = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.WechatAppId = params.get("WechatAppId")
        self.WechatSubAppId = params.get("WechatSubAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPayRollAuthResponse(AbstractModel):
    """GetPayRollAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param AuthStatus: 授权状态：
UNAUTHORIZED：未授权
AUTHORIZED：已授权
DEAUTHORIZED：已取消授权
        :type AuthStatus: str
        :param AuthTime: 授权时间，遵循[rfc3339](https://datatracker.ietf.org/doc/html/rfc3339)标准格式，格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，空字符串等同null
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthTime: str
        :param CancelAuthTime: 授权时间，遵循[rfc3339](https://datatracker.ietf.org/doc/html/rfc3339)标准格式，格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，空字符串等同null
注意：此字段可能返回 null，表示取不到有效值。
        :type CancelAuthTime: str
        :param MerchantId: 微信服务商商户的商户号，由微信支付生成并下发
        :type MerchantId: str
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AuthStatus = None
        self.AuthTime = None
        self.CancelAuthTime = None
        self.MerchantId = None
        self.OpenId = None
        self.SubMerchantId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuthStatus = params.get("AuthStatus")
        self.AuthTime = params.get("AuthTime")
        self.CancelAuthTime = params.get("CancelAuthTime")
        self.MerchantId = params.get("MerchantId")
        self.OpenId = params.get("OpenId")
        self.SubMerchantId = params.get("SubMerchantId")
        self.RequestId = params.get("RequestId")


class GetPayRollAuthResultRequest(AbstractModel):
    """GetPayRollAuthResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param AuthNumber: 商户系统内部的商家核身单号，要求此参数只能由数字、大小写字母组成，在服务商内部唯一
        :type AuthNumber: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        """
        self.AuthNumber = None
        self.SubMerchantId = None


    def _deserialize(self, params):
        self.AuthNumber = params.get("AuthNumber")
        self.SubMerchantId = params.get("SubMerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPayRollAuthResultResponse(AbstractModel):
    """GetPayRollAuthResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 核身结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PayRollAuthResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PayRollAuthResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class LegalPersonInfo(AbstractModel):
    """商户法人代表信息

    """

    def __init__(self):
        r"""
        :param IdType: 证件类型 
IDCARD：身份证 
PASSPORT：护照 SOLDIERSCERTIFICATE：士兵证 OFFICERSCERTIFICATE：军官证 GATXCERTIFICATE：香港居民来往内地通行证 TWNDCERTIFICATE：台湾同胞来往内地通行证 
MACAOCERTIFICATE：澳门来往内地通行证
        :type IdType: str
        :param IdNumber: 证件号码
        :type IdNumber: str
        :param PersonName: 姓名
        :type PersonName: str
        :param IdValidityType: 证件有效期类型 
LONGTERM：长期有效 
OTHER：非长期有效
        :type IdValidityType: str
        :param IdEffectiveDate: 证件生效日期，yyyy-MM-dd
        :type IdEffectiveDate: str
        :param ContactPhone: 联系电话
        :type ContactPhone: str
        :param IdExpireDate: 证件失效日期，yyyy-MM-dd
        :type IdExpireDate: str
        :param ContactAddress: 联系地址
        :type ContactAddress: str
        :param EmailAddress: 邮箱地址
        :type EmailAddress: str
        """
        self.IdType = None
        self.IdNumber = None
        self.PersonName = None
        self.IdValidityType = None
        self.IdEffectiveDate = None
        self.ContactPhone = None
        self.IdExpireDate = None
        self.ContactAddress = None
        self.EmailAddress = None


    def _deserialize(self, params):
        self.IdType = params.get("IdType")
        self.IdNumber = params.get("IdNumber")
        self.PersonName = params.get("PersonName")
        self.IdValidityType = params.get("IdValidityType")
        self.IdEffectiveDate = params.get("IdEffectiveDate")
        self.ContactPhone = params.get("ContactPhone")
        self.IdExpireDate = params.get("IdExpireDate")
        self.ContactAddress = params.get("ContactAddress")
        self.EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemberTransactionItem(AbstractModel):
    """会员间交易明细信息

    """

    def __init__(self):
        r"""
        :param TransType: 交易类型。
__1__：转出
__2__：转入
        :type TransType: str
        :param TranStatus: 交易状态。
__0__：成功
        :type TranStatus: str
        :param TransAmount: 交易金额。
        :type TransAmount: str
        :param TransDate: 交易日期，格式：yyyyMMdd。
        :type TransDate: str
        :param TransTime: 交易时间，格式：HHmmss。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransTime: str
        :param BankSequenceNumber: 银行系统流水号。
_平安渠道为见证系统流水号_
        :type BankSequenceNumber: str
        :param BankBookingType: 银行记账类型。
_平安渠道为：_
_1：会员支付_
_2：会员冻结_
_3：会员解冻_
_4：登记挂账_
_6：下单预支付_
_7：确认并付款_
_8：会员退款_
_22：见证+收单平台调账_
_23：见证+收单资金冻结_
_24：见证+收单资金解冻_
_25：会员间交易退款_
注意：此字段可能返回 null，表示取不到有效值。
        :type BankBookingType: str
        :param InSubAccountNumber: 转入方子账户账号。
_平安渠道为转入见证子账户的账号_
        :type InSubAccountNumber: str
        :param OutSubAccountNumber: 转出方子账户账号。
_平安渠道为转出见证子账户的账号_
        :type OutSubAccountNumber: str
        :param Remark: 备注。
_平安渠道，如果是见证+收单的交易，返回交易订单号_
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.TransType = None
        self.TranStatus = None
        self.TransAmount = None
        self.TransDate = None
        self.TransTime = None
        self.BankSequenceNumber = None
        self.BankBookingType = None
        self.InSubAccountNumber = None
        self.OutSubAccountNumber = None
        self.Remark = None


    def _deserialize(self, params):
        self.TransType = params.get("TransType")
        self.TranStatus = params.get("TranStatus")
        self.TransAmount = params.get("TransAmount")
        self.TransDate = params.get("TransDate")
        self.TransTime = params.get("TransTime")
        self.BankSequenceNumber = params.get("BankSequenceNumber")
        self.BankBookingType = params.get("BankBookingType")
        self.InSubAccountNumber = params.get("InSubAccountNumber")
        self.OutSubAccountNumber = params.get("OutSubAccountNumber")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MerchantClassificationId(AbstractModel):
    """商户分类

    """

    def __init__(self):
        r"""
        :param Code: 分类编号
        :type Code: str
        :param Name: 分类名称
        :type Name: str
        :param Parent: 父级编号（0为一级编号，大于0为父级分类编号）
        :type Parent: str
        """
        self.Code = None
        self.Name = None
        self.Parent = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Name = params.get("Name")
        self.Parent = params.get("Parent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MerchantManagementList(AbstractModel):
    """商户查询管理端列表

    """

    def __init__(self):
        r"""
        :param TaxpayerName: 企业名称。
        :type TaxpayerName: str
        :param TaxpayerNum: 纳税人识别号(税号)	。
        :type TaxpayerNum: str
        :param SerialNo: 请求流水号。
        :type SerialNo: str
        :param InvoicePlatformId: 开票系统ID
        :type InvoicePlatformId: int
        """
        self.TaxpayerName = None
        self.TaxpayerNum = None
        self.SerialNo = None
        self.InvoicePlatformId = None


    def _deserialize(self, params):
        self.TaxpayerName = params.get("TaxpayerName")
        self.TaxpayerNum = params.get("TaxpayerNum")
        self.SerialNo = params.get("SerialNo")
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MerchantManagementResult(AbstractModel):
    """商户管理端结果

    """

    def __init__(self):
        r"""
        :param Total: 总数。
        :type Total: int
        :param List: 商户列表。
        :type List: list of MerchantManagementList
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = MerchantManagementList()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MerchantPayWayData(AbstractModel):
    """商户支付方式数据

    """

    def __init__(self):
        r"""
        :param PayCurrency: 支付币种
注意：此字段可能返回 null，表示取不到有效值。
        :type PayCurrency: str
        :param PayIcon: 支付图标
注意：此字段可能返回 null，表示取不到有效值。
        :type PayIcon: str
        :param PayInternalName: 支付名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayInternalName: str
        :param PayName: 支付简称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param PaySplitRefund: 是否支持退款
注意：此字段可能返回 null，表示取不到有效值。
        :type PaySplitRefund: str
        :param PayTag: 支付标签
注意：此字段可能返回 null，表示取不到有效值。
        :type PayTag: str
        :param PayTicketIcon: 支付凭证图标
注意：此字段可能返回 null，表示取不到有效值。
        :type PayTicketIcon: str
        :param PayType: 支付类型，逗号分隔
注意：此字段可能返回 null，表示取不到有效值。
        :type PayType: str
        :param TicketName: 凭证名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketName: str
        """
        self.PayCurrency = None
        self.PayIcon = None
        self.PayInternalName = None
        self.PayName = None
        self.PaySplitRefund = None
        self.PayTag = None
        self.PayTicketIcon = None
        self.PayType = None
        self.TicketName = None


    def _deserialize(self, params):
        self.PayCurrency = params.get("PayCurrency")
        self.PayIcon = params.get("PayIcon")
        self.PayInternalName = params.get("PayInternalName")
        self.PayName = params.get("PayName")
        self.PaySplitRefund = params.get("PaySplitRefund")
        self.PayTag = params.get("PayTag")
        self.PayTicketIcon = params.get("PayTicketIcon")
        self.PayType = params.get("PayType")
        self.TicketName = params.get("TicketName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MerchantRiskInfo(AbstractModel):
    """商户风险信息

    """

    def __init__(self):
        r"""
        :param RiskLevel: 恶意注册等级，0-9级，9级最高
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param RiskTypes: 恶意注册代码，代码以|分割，如"G001|T002"
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskTypes: str
        """
        self.RiskLevel = None
        self.RiskTypes = None


    def _deserialize(self, params):
        self.RiskLevel = params.get("RiskLevel")
        self.RiskTypes = params.get("RiskTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOrderRefundQueryRequest(AbstractModel):
    """MigrateOrderRefundQuery请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param PayChannel: 支付渠道，ALIPAY对应支付宝渠道；UNIONPAY对应银联渠道
        :type PayChannel: str
        :param RefundOrderId: 退款订单号，最长64位，仅支持数字、 字母
        :type RefundOrderId: str
        :param TradeSerialNo: 退款流水号
        :type TradeSerialNo: str
        :param Profile: 接入环境。沙箱环境填 sandbox。
        :type Profile: str
        """
        self.MerchantId = None
        self.PayChannel = None
        self.RefundOrderId = None
        self.TradeSerialNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayChannel = params.get("PayChannel")
        self.RefundOrderId = params.get("RefundOrderId")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOrderRefundQueryResponse(AbstractModel):
    """MigrateOrderRefundQuery返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsSuccess: 请求成功状态
        :type IsSuccess: bool
        :param TradeSerialNo: 交易流水号
        :type TradeSerialNo: str
        :param TradeMsg: 交易备注
        :type TradeMsg: str
        :param TradeStatus: 交易状态：0=交易待处理；1=交易处理中；2=交易处理成功；3=交易失败；4=状态未知
        :type TradeStatus: int
        :param ThirdChannelOrderId: 第三方支付机构支付交易号
注意：此字段可能返回 null，表示取不到有效值。
        :type ThirdChannelOrderId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.TradeSerialNo = None
        self.TradeMsg = None
        self.TradeStatus = None
        self.ThirdChannelOrderId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.TradeMsg = params.get("TradeMsg")
        self.TradeStatus = params.get("TradeStatus")
        self.ThirdChannelOrderId = params.get("ThirdChannelOrderId")
        self.RequestId = params.get("RequestId")


class MigrateOrderRefundRequest(AbstractModel):
    """MigrateOrderRefund请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户代码
        :type MerchantId: str
        :param PayChannel: 支付渠道，ALIPAY对应支付宝渠道；UNIONPAY对应银联渠道
        :type PayChannel: str
        :param PayOrderId: 正向支付商户订单号
        :type PayOrderId: str
        :param RefundOrderId: 退款订单号，最长64位，仅支持数字、 字母
        :type RefundOrderId: str
        :param RefundAmt: 退款金额，单位：分。备注：改字段必须大于0 和小于10000000000的整数。
        :type RefundAmt: int
        :param ThirdChannelOrderId: 第三方支付机构支付交易号
        :type ThirdChannelOrderId: str
        :param PayAmt: 原始支付金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额
        :type PayAmt: int
        :param Profile: 接入环境。沙箱环境填 sandbox。
        :type Profile: str
        :param RefundReason: 退款原因
        :type RefundReason: str
        """
        self.MerchantId = None
        self.PayChannel = None
        self.PayOrderId = None
        self.RefundOrderId = None
        self.RefundAmt = None
        self.ThirdChannelOrderId = None
        self.PayAmt = None
        self.Profile = None
        self.RefundReason = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayChannel = params.get("PayChannel")
        self.PayOrderId = params.get("PayOrderId")
        self.RefundOrderId = params.get("RefundOrderId")
        self.RefundAmt = params.get("RefundAmt")
        self.ThirdChannelOrderId = params.get("ThirdChannelOrderId")
        self.PayAmt = params.get("PayAmt")
        self.Profile = params.get("Profile")
        self.RefundReason = params.get("RefundReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateOrderRefundResponse(AbstractModel):
    """MigrateOrderRefund返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsSuccess: 请求成功状态
        :type IsSuccess: bool
        :param TradeSerialNo: 退款流水号
        :type TradeSerialNo: str
        :param TradeMsg: 交易备注
        :type TradeMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.TradeSerialNo = None
        self.TradeMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.TradeMsg = params.get("TradeMsg")
        self.RequestId = params.get("RequestId")


class ModifyAgentTaxPaymentInfoRequest(AbstractModel):
    """ModifyAgentTaxPaymentInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchNum: 批次号
        :type BatchNum: int
        :param RawElectronicCertUrl: 新源电子凭证地址
        :type RawElectronicCertUrl: str
        :param FileName: 新的文件名
        :type FileName: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.BatchNum = None
        self.RawElectronicCertUrl = None
        self.FileName = None
        self.Profile = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        self.RawElectronicCertUrl = params.get("RawElectronicCertUrl")
        self.FileName = params.get("FileName")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentTaxPaymentInfoResponse(AbstractModel):
    """ModifyAgentTaxPaymentInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param AgentTaxPaymentBatch: 代理商完税证明批次信息
        :type AgentTaxPaymentBatch: :class:`tencentcloud.cpdp.v20190820.models.AgentTaxPaymentBatch`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AgentTaxPaymentBatch = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentTaxPaymentBatch") is not None:
            self.AgentTaxPaymentBatch = AgentTaxPaymentBatch()
            self.AgentTaxPaymentBatch._deserialize(params.get("AgentTaxPaymentBatch"))
        self.RequestId = params.get("RequestId")


class ModifyBindedAccountRequest(AbstractModel):
    """ModifyBindedAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播Id
        :type AnchorId: str
        :param TransferType: 1 微信企业付款 
2 支付宝转账 
3 平安银企直连代发转账
        :type TransferType: int
        :param AccountNo: 收款方标识。
微信为open_id；
支付宝为会员alipay_user_id;
平安为收款方银行账号;
        :type AccountNo: str
        :param PhoneNum: 手机号
        :type PhoneNum: str
        """
        self.AnchorId = None
        self.TransferType = None
        self.AccountNo = None
        self.PhoneNum = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.TransferType = params.get("TransferType")
        self.AccountNo = params.get("AccountNo")
        self.PhoneNum = params.get("PhoneNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBindedAccountResponse(AbstractModel):
    """ModifyBindedAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMessage: 响应消息。
        :type ErrMessage: str
        :param Result: 该字段为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyFlexPayeeAccountRightStatusRequest(AbstractModel):
    """ModifyFlexPayeeAccountRightStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param AccountRightType: 账户权益类型
SETTLEMENT:结算权益
PAYMENT:付款权益
        :type AccountRightType: str
        :param AccountRightStatus: 账户权益状态
ENABLE:启用
DISABLE:停用
        :type AccountRightStatus: str
        """
        self.PayeeId = None
        self.AccountRightType = None
        self.AccountRightStatus = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.AccountRightType = params.get("AccountRightType")
        self.AccountRightStatus = params.get("AccountRightStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFlexPayeeAccountRightStatusResponse(AbstractModel):
    """ModifyFlexPayeeAccountRightStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果。默认为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyMerchantRequest(AbstractModel):
    """ModifyMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 进件成功后返给商户的AppId
        :type MerchantAppId: str
        :param MerchantName: 收款商户名称
        :type MerchantName: str
        :param BusinessPayFlag: B2B 支付标志。是否开通 B2B支付， 1:开通 0:不开通。
        :type BusinessPayFlag: str
        """
        self.MerchantAppId = None
        self.MerchantName = None
        self.BusinessPayFlag = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.MerchantName = params.get("MerchantName")
        self.BusinessPayFlag = params.get("BusinessPayFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMerchantResponse(AbstractModel):
    """ModifyMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMntMbrBindRelateAcctBankCodeRequest(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
        :type SubAcctNo: str
        :param MemberBindAcctNo: STRING(50)，会员绑定账号
        :type MemberBindAcctNo: str
        :param AcctOpenBranchName: STRING(150)，开户行名称（若大小额行号不填则送超级网银号对应的银行名称，若填大小额行号则送大小额行号对应的银行名称）
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，大小额行号（CnapsBranchId和EiconBankBranchId两者二选一必填）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，超级网银行号
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberBindAcctNo = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberBindAcctNo = params.get("MemberBindAcctNo")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMntMbrBindRelateAcctBankCodeResponse(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class MultiApplyDetail(AbstractModel):
    """分账明细

    """

    def __init__(self):
        r"""
        :param MerchantNo: 商户编号
        :type MerchantNo: str
        :param Amount: 分账金额
        :type Amount: str
        :param Remark: 备注
        :type Remark: str
        """
        self.MerchantNo = None
        self.Amount = None
        self.Remark = None


    def _deserialize(self, params):
        self.MerchantNo = params.get("MerchantNo")
        self.Amount = params.get("Amount")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiApplyOrder(AbstractModel):
    """分账订单信息

    """

    def __init__(self):
        r"""
        :param OutDistributeNo: 商户分账单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutDistributeNo: str
        :param DistributeNo: 平台分账单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributeNo: str
        :param OrderNo: 平台交易订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param Status: 分账订单状态（0初始1成功2失败3撤销）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param InDate: 入账日期，格式yyyy-MM-dd
注意：此字段可能返回 null，表示取不到有效值。
        :type InDate: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param Details: 分账明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of MultiApplyDetail
        """
        self.OutDistributeNo = None
        self.DistributeNo = None
        self.OrderNo = None
        self.Status = None
        self.InDate = None
        self.Remark = None
        self.Details = None


    def _deserialize(self, params):
        self.OutDistributeNo = params.get("OutDistributeNo")
        self.DistributeNo = params.get("DistributeNo")
        self.OrderNo = params.get("OrderNo")
        self.Status = params.get("Status")
        self.InDate = params.get("InDate")
        self.Remark = params.get("Remark")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = MultiApplyDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NaturalPersonInfo(AbstractModel):
    """自然人信息

    """

    def __init__(self):
        r"""
        :param PersonType: 自然人类型 
2：商户负责人 
3：授权经办人
4：业务联系人 
5：实际控制人 
6：控股股东 
7：受益人 
8：结算人
注意：HELIPAY渠道必传业务联系人
        :type PersonType: str
        :param IdType: 证件类型 
IDCARD：身份证 
PASSPORT：护照 SOLDIERSCERTIFICATE：士兵证 OFFICERSCERTIFICATE：军官证 GATXCERTIFICATE：香港居民来往内地通行证 TWNDCERTIFICATE：台湾同胞来往内地通行证 MACAOCERTIFICATE：澳门来往内地通行证
        :type IdType: str
        :param IdNumber: 证件号码
        :type IdNumber: str
        :param PersonName: 姓名
        :type PersonName: str
        :param IdValidityType: 证件有效期类型 
LONGTERM：长期有效 
OTHER：非长期有效
        :type IdValidityType: str
        :param IdEffectiveDate: 证件生效日期，yyyy-MM-dd
        :type IdEffectiveDate: str
        :param IdExpireDate: 证件失效日期，yyyy-MM-dd
        :type IdExpireDate: str
        :param ContactPhone: 联系电话，HELIPAY渠道业务联系人必传
        :type ContactPhone: str
        :param ContactAddress: 联系地址
        :type ContactAddress: str
        :param EmailAddress: 邮箱地址
        :type EmailAddress: str
        """
        self.PersonType = None
        self.IdType = None
        self.IdNumber = None
        self.PersonName = None
        self.IdValidityType = None
        self.IdEffectiveDate = None
        self.IdExpireDate = None
        self.ContactPhone = None
        self.ContactAddress = None
        self.EmailAddress = None


    def _deserialize(self, params):
        self.PersonType = params.get("PersonType")
        self.IdType = params.get("IdType")
        self.IdNumber = params.get("IdNumber")
        self.PersonName = params.get("PersonName")
        self.IdValidityType = params.get("IdValidityType")
        self.IdEffectiveDate = params.get("IdEffectiveDate")
        self.IdExpireDate = params.get("IdExpireDate")
        self.ContactPhone = params.get("ContactPhone")
        self.ContactAddress = params.get("ContactAddress")
        self.EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankApprovalGuideInfo(AbstractModel):
    """银行复核指引。银行侧返回网银授权指引链接，一般PC网银，手机网银链接

    """

    def __init__(self):
        r"""
        :param PcGuideUrl: PC网银指引
        :type PcGuideUrl: str
        :param MobileGuideUrl: 手机网银指引
注意：此字段可能返回 null，表示取不到有效值。
        :type MobileGuideUrl: str
        """
        self.PcGuideUrl = None
        self.MobileGuideUrl = None


    def _deserialize(self, params):
        self.PcGuideUrl = params.get("PcGuideUrl")
        self.MobileGuideUrl = params.get("MobileGuideUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankGoodsInfo(AbstractModel):
    """云企付-商品信息

    """

    def __init__(self):
        r"""
        :param GoodsName: 商品标题。默认值“商品支付”。
        :type GoodsName: str
        :param GoodsDetail: 商品详细描述（商品列表）。
        :type GoodsDetail: str
        :param GoodsDescription: 银行附言。不可以有以下字符：<>+{}()%*&';"[]等特殊符号
        :type GoodsDescription: str
        :param GoodsBizType: 业务类型。汇付渠道必填，汇付渠道传入固定值100099。
        :type GoodsBizType: str
        """
        self.GoodsName = None
        self.GoodsDetail = None
        self.GoodsDescription = None
        self.GoodsBizType = None


    def _deserialize(self, params):
        self.GoodsName = params.get("GoodsName")
        self.GoodsDetail = params.get("GoodsDetail")
        self.GoodsDescription = params.get("GoodsDescription")
        self.GoodsBizType = params.get("GoodsBizType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankPayLimitInfo(AbstractModel):
    """云企付-支付限制

    """

    def __init__(self):
        r"""
        :param PayLimitType: 限制类型
        :type PayLimitType: str
        :param PayLimitValue: 限制类型值
        :type PayLimitValue: str
        """
        self.PayLimitType = None
        self.PayLimitValue = None


    def _deserialize(self, params):
        self.PayLimitType = params.get("PayLimitType")
        self.PayLimitValue = params.get("PayLimitValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankPayeeInfo(AbstractModel):
    """云企付-收款人信息

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款方唯一标识。
当渠道为TENPAY，付款方式为EBANK_PAYMENT，必填，上送收款方入驻云企付商户ID；
付款方式为OPENBANK_PAYMENT时，非必填，输入外部收款方的标识ID
渠道为WECHAT，付款方式为TRANS_TO_CHANGE时，上送微信OPEN_ID；
        :type PayeeId: str
        :param BankBranchName: 支行名称。
        :type BankBranchName: str
        :param BankAccountNumber: 银行账号。渠道为TENPAY，付款方式为OPENBANK_PAYMENT时必选
        :type BankAccountNumber: str
        :param PayeeName: 收款方名称。
当渠道为TENPAY，付款方式为EBANK_PAYMENT时，上送收款方入驻云企付的商户名称；
渠道为TENPAY，付款方式为OPENBANK_PAYMENT时必选，上送收款方账户名称；
渠道为ALIPAY，付款方式为SAFT_ISV时，收款账户标识类型为ALIPAY_LOGON_ID时必传，上送收款方真实姓名。
渠道为WECHAT，付款方式为TRANS_TO_CHANGE时，上送收款人姓名。
        :type PayeeName: str
        :param BankBranchId: 联行号。渠道为TENPAY，付款方式为OPENBANK_PAYMENT时必选
        :type BankBranchId: str
        :param BindSerialNo: 收款方绑卡序列号。
当渠道为TENPAY，付款方式为EBANK_PAYMENT时，必填，上送收款方入驻云企付平台时，下发的绑卡序列号；当渠道为ALIPAY，付款方式为SAFT_ISV时，必填，根据收款账户标识类型上送。
        :type BindSerialNo: str
        :param AccountType: 收款账户标识类型
BANK_ACCOUNT：绑定银行账户
ACCOUNT_BOOK_ID：电子记账本ID
ALIPAY_USER_ID：支付宝的会员ID
ALIPAY_LOGON_ID：支付宝登录号。
付款方式为SAFT_ISV时，必填。
        :type AccountType: str
        """
        self.PayeeId = None
        self.BankBranchName = None
        self.BankAccountNumber = None
        self.PayeeName = None
        self.BankBranchId = None
        self.BindSerialNo = None
        self.AccountType = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.BankBranchName = params.get("BankBranchName")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.PayeeName = params.get("PayeeName")
        self.BankBranchId = params.get("BankBranchId")
        self.BindSerialNo = params.get("BindSerialNo")
        self.AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankPayerInfo(AbstractModel):
    """云企付-付款人信息

    """

    def __init__(self):
        r"""
        :param PayerId: 付款方唯一标识。当TENPAY时，必填上送
付款方入驻云企付商户ID。
        :type PayerId: str
        :param PayerName: 付款方名称。当TENPAY上送付款方入驻云企付的商户名称。
        :type PayerName: str
        :param BindSerialNo: 付款方付款账户标识。
当付款方式为OPENBANK_PAYMENT时，必输表示企业账户ID；当付款方式为SAFT_ISV时，必须上送付款方的渠道电子记账本ID；当付款方式为ONLINEBANK，上送付款方银行编号BankId。
        :type BindSerialNo: str
        :param AccountType: 付款账户标识类型
BANK_ACCOUNT：绑定银行账户
ACCOUNT_BOOK_ID：电子记账本ID。
当付款方式为SAFT_ISV时，必须上送类型为ACCOUNT_BOOK_ID。
        :type AccountType: str
        :param BankCardType: 付款卡类型。汇付渠道必填。
DEBIT_CARD：借记卡
CREDIT_CARD：信用卡
        :type BankCardType: str
        """
        self.PayerId = None
        self.PayerName = None
        self.BindSerialNo = None
        self.AccountType = None
        self.BankCardType = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.PayerName = params.get("PayerName")
        self.BindSerialNo = params.get("BindSerialNo")
        self.AccountType = params.get("AccountType")
        self.BankCardType = params.get("BankCardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankProfitShareInfo(AbstractModel):
    """云企付-分润信息

    """

    def __init__(self):
        r"""
        :param RecvId: 分润接收方，渠道商户号ID
        :type RecvId: str
        :param ProfitShareFee: 分润金额，单位分
        :type ProfitShareFee: int
        """
        self.RecvId = None
        self.ProfitShareFee = None


    def _deserialize(self, params):
        self.RecvId = params.get("RecvId")
        self.ProfitShareFee = params.get("ProfitShareFee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankQueryRefundOrderResult(AbstractModel):
    """云企付-退款查询结果

    """

    def __init__(self):
        r"""
        :param OutRefundId: 外部商户退款单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutRefundId: str
        :param ChannelRefundId: 渠道退款单号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelRefundId: str
        :param RefundReason: 退款原因
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundReason: str
        :param RefundAmount: 退款金额，单位分
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundAmount: int
        :param RealRefundAmount: 实际退款金额，单位分
注意：此字段可能返回 null，表示取不到有效值。
        :type RealRefundAmount: int
        :param TotalAmount: 原支付订单总金额，单位分
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAmount: int
        :param TimeFinish: 退款完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFinish: str
        :param RefundStatus: 退款订单状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundStatus: str
        :param RefundInfo: 退款明细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundInfo: str
        :param FeeAmount: 退款手续费金额
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeAmount: int
        :param RefundMessage: 退款返回描述，比如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundMessage: str
        """
        self.OutRefundId = None
        self.ChannelRefundId = None
        self.RefundReason = None
        self.RefundAmount = None
        self.RealRefundAmount = None
        self.TotalAmount = None
        self.TimeFinish = None
        self.RefundStatus = None
        self.RefundInfo = None
        self.FeeAmount = None
        self.RefundMessage = None


    def _deserialize(self, params):
        self.OutRefundId = params.get("OutRefundId")
        self.ChannelRefundId = params.get("ChannelRefundId")
        self.RefundReason = params.get("RefundReason")
        self.RefundAmount = params.get("RefundAmount")
        self.RealRefundAmount = params.get("RealRefundAmount")
        self.TotalAmount = params.get("TotalAmount")
        self.TimeFinish = params.get("TimeFinish")
        self.RefundStatus = params.get("RefundStatus")
        self.RefundInfo = params.get("RefundInfo")
        self.FeeAmount = params.get("FeeAmount")
        self.RefundMessage = params.get("RefundMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankRechargePayeeInfo(AbstractModel):
    """云企付-充值单收款人信息

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款方标识
收款方类型为电子记账本时，上送渠道电子记账本ID
        :type PayeeId: str
        :param PayeeIdType: 收款方标识类型
ACCOUNT_BOOK_ID：电子记账本ID
        :type PayeeIdType: str
        :param PayeeName: 收款方名称
        :type PayeeName: str
        """
        self.PayeeId = None
        self.PayeeIdType = None
        self.PayeeName = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.PayeeIdType = params.get("PayeeIdType")
        self.PayeeName = params.get("PayeeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankRechargeRedirectInfo(AbstractModel):
    """云企付-充值跳转参数

    """

    def __init__(self):
        r"""
        :param Url: 跳转URL
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankRedirectInfo(AbstractModel):
    """云企付-跳转参数，用于小程序前端跳转

    """

    def __init__(self):
        r"""
        :param QRCodeUrl: 生成二维码，引导用户扫码
        :type QRCodeUrl: str
        :param QRCodeKey: 二维码凭证
        :type QRCodeKey: str
        :param Url: 跳转 URL,用于客户端跳转，订单未支付时返回该参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param ExpireTime: 跳转凭证过期时间,yyyy-MM-dd HH:mm:ss
        :type ExpireTime: str
        :param MpAppId: 小程序 appid
        :type MpAppId: str
        :param MpPath: 小程序路径
        :type MpPath: str
        :param MpUserName: 小程序原始 id
        :type MpUserName: str
        """
        self.QRCodeUrl = None
        self.QRCodeKey = None
        self.Url = None
        self.ExpireTime = None
        self.MpAppId = None
        self.MpPath = None
        self.MpUserName = None


    def _deserialize(self, params):
        self.QRCodeUrl = params.get("QRCodeUrl")
        self.QRCodeKey = params.get("QRCodeKey")
        self.Url = params.get("Url")
        self.ExpireTime = params.get("ExpireTime")
        self.MpAppId = params.get("MpAppId")
        self.MpPath = params.get("MpPath")
        self.MpUserName = params.get("MpUserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankRefundOrderApplyResult(AbstractModel):
    """云企付-退款申请结果

    """

    def __init__(self):
        r"""
        :param ChannelOrderId: 云企付订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelOrderId: str
        :param ChannelRefundId: 云企付退款流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelRefundId: str
        :param OutRefundId: 外部商户退款单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutRefundId: str
        :param OutOrderId: 外部商户订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutOrderId: str
        :param RefundMessage: 退款返回描述，比如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundMessage: str
        :param RefundAmount: 退款金额
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundAmount: int
        :param FeeAmount: 退款手续费金额
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeAmount: int
        :param RefundStatus: 退款状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundStatus: str
        """
        self.ChannelOrderId = None
        self.ChannelRefundId = None
        self.OutRefundId = None
        self.OutOrderId = None
        self.RefundMessage = None
        self.RefundAmount = None
        self.FeeAmount = None
        self.RefundStatus = None


    def _deserialize(self, params):
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.ChannelRefundId = params.get("ChannelRefundId")
        self.OutRefundId = params.get("OutRefundId")
        self.OutOrderId = params.get("OutOrderId")
        self.RefundMessage = params.get("RefundMessage")
        self.RefundAmount = params.get("RefundAmount")
        self.FeeAmount = params.get("FeeAmount")
        self.RefundStatus = params.get("RefundStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankSceneInfo(AbstractModel):
    """云企付-设备信息

    """

    def __init__(self):
        r"""
        :param PayerClientIp: 用户端实际 ip。汇付渠道必填。
        :type PayerClientIp: str
        :param PayerUa: 浏览器 User-Agent。
        :type PayerUa: str
        :param OrderTime: 用户下单时间。若不上送，服务端默认当前时间。
        :type OrderTime: str
        :param DeviceId: 终端设备号（门店号或收银设备 ID），示例值：POS1:1。
        :type DeviceId: str
        :param DeviceType: 终端设备类型。MOBILE_BROWSER:手机浏览器，MOBILE_APP:手机应用程序，TABLET:平板；WATCH:手表，PC:电脑PC，OTHER:其他。
汇付渠道必填。
        :type DeviceType: str
        """
        self.PayerClientIp = None
        self.PayerUa = None
        self.OrderTime = None
        self.DeviceId = None
        self.DeviceType = None


    def _deserialize(self, params):
        self.PayerClientIp = params.get("PayerClientIp")
        self.PayerUa = params.get("PayerUa")
        self.OrderTime = params.get("OrderTime")
        self.DeviceId = params.get("DeviceId")
        self.DeviceType = params.get("DeviceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenBankStoreInfo(AbstractModel):
    """云企付-门店信息

    """

    def __init__(self):
        r"""
        :param Name: 门店名称
        :type Name: str
        :param AreaCode: 地区编码
        :type AreaCode: str
        :param Address: 详细地址
        :type Address: str
        :param Id: 门店编号
        :type Id: str
        """
        self.Name = None
        self.AreaCode = None
        self.Address = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AreaCode = params.get("AreaCode")
        self.Address = params.get("Address")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Order(AbstractModel):
    """线下查票-订单信息

    """

    def __init__(self):
        r"""
        :param AmountHasTax: 含税金额
注意：此字段可能返回 null，表示取不到有效值。
        :type AmountHasTax: float
        :param Discount: 优惠金额
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param SellerName: 销方名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SellerName: str
        :param InvoiceType: 发票类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InvoiceType: int
        :param Name: 默认“”
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Amount: 支付金额
注意：此字段可能返回 null，表示取不到有效值。
        :type Amount: float
        :param OrderDate: 下单日期
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderDate: str
        :param OrderId: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param StoreNo: 门店号
注意：此字段可能返回 null，表示取不到有效值。
        :type StoreNo: str
        :param Items: 明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrderItem
        """
        self.AmountHasTax = None
        self.Discount = None
        self.SellerName = None
        self.InvoiceType = None
        self.Name = None
        self.Amount = None
        self.OrderDate = None
        self.OrderId = None
        self.StoreNo = None
        self.Items = None


    def _deserialize(self, params):
        self.AmountHasTax = params.get("AmountHasTax")
        self.Discount = params.get("Discount")
        self.SellerName = params.get("SellerName")
        self.InvoiceType = params.get("InvoiceType")
        self.Name = params.get("Name")
        self.Amount = params.get("Amount")
        self.OrderDate = params.get("OrderDate")
        self.OrderId = params.get("OrderId")
        self.StoreNo = params.get("StoreNo")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = OrderItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrderItem(AbstractModel):
    """线下查票-订单明细

    """

    def __init__(self):
        r"""
        :param AmountHasTax: 明细金额
注意：此字段可能返回 null，表示取不到有效值。
        :type AmountHasTax: float
        :param Discount: 优惠金额
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param Name: 商品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Models: 型号
注意：此字段可能返回 null，表示取不到有效值。
        :type Models: str
        :param Total: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Unit: 数量单位
注意：此字段可能返回 null，表示取不到有效值。
        :type Unit: str
        :param Status: 默认“0”
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Price: 单价
注意：此字段可能返回 null，表示取不到有效值。
        :type Price: float
        :param TaxCode: 商品编码
注意：此字段可能返回 null，表示取不到有效值。
        :type TaxCode: str
        """
        self.AmountHasTax = None
        self.Discount = None
        self.Name = None
        self.Models = None
        self.Total = None
        self.Unit = None
        self.Status = None
        self.Price = None
        self.TaxCode = None


    def _deserialize(self, params):
        self.AmountHasTax = params.get("AmountHasTax")
        self.Discount = params.get("Discount")
        self.Name = params.get("Name")
        self.Models = params.get("Models")
        self.Total = params.get("Total")
        self.Unit = params.get("Unit")
        self.Status = params.get("Status")
        self.Price = params.get("Price")
        self.TaxCode = params.get("TaxCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationInfo(AbstractModel):
    """公司信息

    """

    def __init__(self):
        r"""
        :param OrganizationName: 公司名称，个体工商户必输
        :type OrganizationName: str
        :param OrganizationType: 公司证件类型，个体工商户必输，证件类型仅支持73
        :type OrganizationType: str
        :param OrganizationCode: 公司证件号码，个体工商户必输
        :type OrganizationCode: str
        :param LegalPersonName: 法人名称，如果SubMchName不是法人，需要另外送入法人信息（企业必输）
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type LegalPersonName: str
        :param LegalPersonIdType: 法人证件类型，如果SubMchName不是法人，需要另外送入法人信息（企业必输）
        :type LegalPersonIdType: str
        :param LegalPersonIdCode: 法人证件号码，如果SubMchName不是法人，需要另外送入法人信息（企业必输）
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type LegalPersonIdCode: str
        """
        self.OrganizationName = None
        self.OrganizationType = None
        self.OrganizationCode = None
        self.LegalPersonName = None
        self.LegalPersonIdType = None
        self.LegalPersonIdCode = None


    def _deserialize(self, params):
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationType = params.get("OrganizationType")
        self.OrganizationCode = params.get("OrganizationCode")
        self.LegalPersonName = params.get("LegalPersonName")
        self.LegalPersonIdType = params.get("LegalPersonIdType")
        self.LegalPersonIdCode = params.get("LegalPersonIdCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutSubMerchantExtensionInfo(AbstractModel):
    """外部子商户扩展信息

    """

    def __init__(self):
        r"""
        :param RegionCode: 地区代码，国标码
HELIPAY渠道必传
        :type RegionCode: str
        :param RegisterAddress: 注册地址
        :type RegisterAddress: str
        :param MailingAddress: 通讯地址
HELIPAY渠道必传
        :type MailingAddress: str
        :param BusinessAddress: 营业地址/经营地址
        :type BusinessAddress: str
        :param ServicePhone: 客服电话
        :type ServicePhone: str
        :param WebSiteUrl: 网站url
        :type WebSiteUrl: str
        :param EmailAddress: 邮箱地址
        :type EmailAddress: str
        """
        self.RegionCode = None
        self.RegisterAddress = None
        self.MailingAddress = None
        self.BusinessAddress = None
        self.ServicePhone = None
        self.WebSiteUrl = None
        self.EmailAddress = None


    def _deserialize(self, params):
        self.RegionCode = params.get("RegionCode")
        self.RegisterAddress = params.get("RegisterAddress")
        self.MailingAddress = params.get("MailingAddress")
        self.BusinessAddress = params.get("BusinessAddress")
        self.ServicePhone = params.get("ServicePhone")
        self.WebSiteUrl = params.get("WebSiteUrl")
        self.EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """分页参数

    """

    def __init__(self):
        r"""
        :param Index: 页码
        :type Index: int
        :param Count: 页长
        :type Count: int
        """
        self.Index = None
        self.Count = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayDataResult(AbstractModel):
    """pay支付方式json数据

    """

    def __init__(self):
        r"""
        :param PaymentTag: 支付标签（唯一性）
        :type PaymentTag: str
        :param PaymentOptionHide: 添加合同时需要隐藏的选项（多个以小写逗号分开）
        :type PaymentOptionHide: str
        :param PaymentIcon: 支付方式图片url路径
        :type PaymentIcon: str
        :param PaymentOptionSix: 合同选项名称6
        :type PaymentOptionSix: str
        :param PaymentName: 付款方式名称
        :type PaymentName: str
        :param PaymentOptionSeven: 合同选项名称7
        :type PaymentOptionSeven: str
        :param PaymentOptionOther: 合同选项名称8
        :type PaymentOptionOther: str
        :param PaymentOptionTwo: 合同选项名称2
        :type PaymentOptionTwo: str
        :param PaymentOptionOne: 合同选项名称1
        :type PaymentOptionOne: str
        :param PaymentDiscountFee: 是否开启智能扣率（1是，0否）
        :type PaymentDiscountFee: str
        :param PaymentType: 支持的交易类型（多个以小写逗号分开，0现金，1刷卡，2主扫，3被扫，4JSPAY，5预授权）
        :type PaymentType: str
        :param PaymentOptionFive: 合同选项名称5
        :type PaymentOptionFive: str
        :param PaymentOptionNine: 合同选项名称9
        :type PaymentOptionNine: str
        :param PaymentId: 支付方式编号
        :type PaymentId: str
        :param PaymentOptionThree: 合同选项名称3
        :type PaymentOptionThree: str
        :param PaymentInternalName: 付款方式名称（内部名称）
        :type PaymentInternalName: str
        :param PaymentOptionFour: 合同选项名称4
        :type PaymentOptionFour: str
        :param PaymentOptionTen: 合同选项名称10
        :type PaymentOptionTen: str
        """
        self.PaymentTag = None
        self.PaymentOptionHide = None
        self.PaymentIcon = None
        self.PaymentOptionSix = None
        self.PaymentName = None
        self.PaymentOptionSeven = None
        self.PaymentOptionOther = None
        self.PaymentOptionTwo = None
        self.PaymentOptionOne = None
        self.PaymentDiscountFee = None
        self.PaymentType = None
        self.PaymentOptionFive = None
        self.PaymentOptionNine = None
        self.PaymentId = None
        self.PaymentOptionThree = None
        self.PaymentInternalName = None
        self.PaymentOptionFour = None
        self.PaymentOptionTen = None


    def _deserialize(self, params):
        self.PaymentTag = params.get("PaymentTag")
        self.PaymentOptionHide = params.get("PaymentOptionHide")
        self.PaymentIcon = params.get("PaymentIcon")
        self.PaymentOptionSix = params.get("PaymentOptionSix")
        self.PaymentName = params.get("PaymentName")
        self.PaymentOptionSeven = params.get("PaymentOptionSeven")
        self.PaymentOptionOther = params.get("PaymentOptionOther")
        self.PaymentOptionTwo = params.get("PaymentOptionTwo")
        self.PaymentOptionOne = params.get("PaymentOptionOne")
        self.PaymentDiscountFee = params.get("PaymentDiscountFee")
        self.PaymentType = params.get("PaymentType")
        self.PaymentOptionFive = params.get("PaymentOptionFive")
        self.PaymentOptionNine = params.get("PaymentOptionNine")
        self.PaymentId = params.get("PaymentId")
        self.PaymentOptionThree = params.get("PaymentOptionThree")
        self.PaymentInternalName = params.get("PaymentInternalName")
        self.PaymentOptionFour = params.get("PaymentOptionFour")
        self.PaymentOptionTen = params.get("PaymentOptionTen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayFeeDataResult(AbstractModel):
    """pay_fee支付方式行业分类费率json数据

    """

    def __init__(self):
        r"""
        :param OrganizationFee: 机构的分佣扣率扣率
        :type OrganizationFee: str
        :param PaymentClassificationLimit: 商户手续费封顶值，0为不限封顶
        :type PaymentClassificationLimit: str
        :param OrganizationFeeType: 机构的分佣扣率类型(1按签约扣率，2按收单收益)
        :type OrganizationFeeType: str
        :param PaymentClassificationMaxFee: 商户扣率最大值
        :type PaymentClassificationMaxFee: str
        :param PaymentClassificationMinFee: 商户扣率最小值
        :type PaymentClassificationMinFee: str
        :param PaymentClassificationId: 行业会类编号
        :type PaymentClassificationId: str
        :param PaymentClassificationName: 行业分类名称
        :type PaymentClassificationName: str
        """
        self.OrganizationFee = None
        self.PaymentClassificationLimit = None
        self.OrganizationFeeType = None
        self.PaymentClassificationMaxFee = None
        self.PaymentClassificationMinFee = None
        self.PaymentClassificationId = None
        self.PaymentClassificationName = None


    def _deserialize(self, params):
        self.OrganizationFee = params.get("OrganizationFee")
        self.PaymentClassificationLimit = params.get("PaymentClassificationLimit")
        self.OrganizationFeeType = params.get("OrganizationFeeType")
        self.PaymentClassificationMaxFee = params.get("PaymentClassificationMaxFee")
        self.PaymentClassificationMinFee = params.get("PaymentClassificationMinFee")
        self.PaymentClassificationId = params.get("PaymentClassificationId")
        self.PaymentClassificationName = params.get("PaymentClassificationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayOrderResult(AbstractModel):
    """订单支付响应对象

    """

    def __init__(self):
        r"""
        :param OrderNo: 付款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param DeveloperNo: 开发者流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type DeveloperNo: str
        :param TradeDiscountAmount: 交易优惠金额（免充值券）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeDiscountAmount: str
        :param PayName: 付款方式名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param OrderMerchantId: 商户流水号（从1开始自增长不重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderMerchantId: str
        :param TradeAccount: 交易帐号（银行卡号、支付宝帐号、微信帐号等，某些收单机构没有此数据）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeAccount: str
        :param TradeAmount: 实际交易金额（以分为单位，没有小数点）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeAmount: str
        :param CurrencySign: 币种签名
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrencySign: str
        :param TradePayTime: 付款完成时间（以收单机构为准）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradePayTime: str
        :param ShopOrderId: 门店流水号（从1开始自增长不重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopOrderId: str
        :param PayTag: 支付标签
注意：此字段可能返回 null，表示取不到有效值。
        :type PayTag: str
        :param Status: 订单状态（1交易成功，2待支付，4已取消，9等待用户输入密码确认
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param OrderCurrency: 币种代码
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderCurrency: str
        :param TradeQrcode: 二维码字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeQrcode: str
        :param WechatAppId: 微信返回调起小程序/原生JS支付的appid参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatAppId: str
        :param WechatTimeStamp: 微信返回调起小程序/原生JS支付的timeStamp参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatTimeStamp: str
        :param WechatNonceStr: 微信返回调起小程序/原生JS支付的nonceStr参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatNonceStr: str
        :param WechatSignType: 微信返回调起小程序/原生JS支付的signType参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatSignType: str
        :param WechatPackage: 微信返回调起小程序/原生JS支付的package参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatPackage: str
        :param WechatPaySign: 微信返回调起小程序/原生JS支付的paySign参数
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatPaySign: str
        """
        self.OrderNo = None
        self.DeveloperNo = None
        self.TradeDiscountAmount = None
        self.PayName = None
        self.OrderMerchantId = None
        self.TradeAccount = None
        self.TradeAmount = None
        self.CurrencySign = None
        self.TradePayTime = None
        self.ShopOrderId = None
        self.PayTag = None
        self.Status = None
        self.OrderCurrency = None
        self.TradeQrcode = None
        self.WechatAppId = None
        self.WechatTimeStamp = None
        self.WechatNonceStr = None
        self.WechatSignType = None
        self.WechatPackage = None
        self.WechatPaySign = None


    def _deserialize(self, params):
        self.OrderNo = params.get("OrderNo")
        self.DeveloperNo = params.get("DeveloperNo")
        self.TradeDiscountAmount = params.get("TradeDiscountAmount")
        self.PayName = params.get("PayName")
        self.OrderMerchantId = params.get("OrderMerchantId")
        self.TradeAccount = params.get("TradeAccount")
        self.TradeAmount = params.get("TradeAmount")
        self.CurrencySign = params.get("CurrencySign")
        self.TradePayTime = params.get("TradePayTime")
        self.ShopOrderId = params.get("ShopOrderId")
        self.PayTag = params.get("PayTag")
        self.Status = params.get("Status")
        self.OrderCurrency = params.get("OrderCurrency")
        self.TradeQrcode = params.get("TradeQrcode")
        self.WechatAppId = params.get("WechatAppId")
        self.WechatTimeStamp = params.get("WechatTimeStamp")
        self.WechatNonceStr = params.get("WechatNonceStr")
        self.WechatSignType = params.get("WechatSignType")
        self.WechatPackage = params.get("WechatPackage")
        self.WechatPaySign = params.get("WechatPaySign")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayRollAuthResult(AbstractModel):
    """微工卡核身结果

    """

    def __init__(self):
        r"""
        :param AuthFailedReason: 结果为核身失败时的原因描述，仅在失败记录返回，空字符串等同null
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthFailedReason: str
        :param AuthNumber: 商户系统内部的商家核身单号，要求此参数只能由数字、大小写字母组成，在服务商内部唯一
        :type AuthNumber: str
        :param AuthScene: 核身渠道，发起核身时的来源渠道，如通过小程序，硬件设备等
FROM_MINI_APP：来自小程序方式核身
FROM_HARDWARE：来自硬件设备方式核身
        :type AuthScene: str
        :param AuthSource: 核身渠道标识，用于定位渠道具体来源，如果是扫码打卡渠道标识就是具体的小程序appid，若是硬件设备，则是设备的序列号等
        :type AuthSource: str
        :param AuthStatus: 核身状态
AUTHENTICATE_PROCESSING：核身中
AUTHENTICATE_SUCCESS：核身成功
AUTHENTICATE_FAILED：核身失败
        :type AuthStatus: str
        :param AuthTime: 核身时间，遵循[rfc3339](https://datatracker.ietf.org/doc/html/rfc3339)标准格式，格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE
        :type AuthTime: str
        :param CompanyName: 该用户所属的单位名称
        :type CompanyName: str
        :param MerchantId: 微信服务商商户的商户号，由微信支付生成并下发
        :type MerchantId: str
        :param OpenId: 用户在商户对应appid下的唯一标识
        :type OpenId: str
        :param ProjectName: 该项目的名称
        :type ProjectName: str
        :param SubMerchantId: 微信服务商下特约商户的商户号，由微信支付生成并下发
        :type SubMerchantId: str
        """
        self.AuthFailedReason = None
        self.AuthNumber = None
        self.AuthScene = None
        self.AuthSource = None
        self.AuthStatus = None
        self.AuthTime = None
        self.CompanyName = None
        self.MerchantId = None
        self.OpenId = None
        self.ProjectName = None
        self.SubMerchantId = None


    def _deserialize(self, params):
        self.AuthFailedReason = params.get("AuthFailedReason")
        self.AuthNumber = params.get("AuthNumber")
        self.AuthScene = params.get("AuthScene")
        self.AuthSource = params.get("AuthSource")
        self.AuthStatus = params.get("AuthStatus")
        self.AuthTime = params.get("AuthTime")
        self.CompanyName = params.get("CompanyName")
        self.MerchantId = params.get("MerchantId")
        self.OpenId = params.get("OpenId")
        self.ProjectName = params.get("ProjectName")
        self.SubMerchantId = params.get("SubMerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeAccountBalanceResult(AbstractModel):
    """账户余额信息

    """

    def __init__(self):
        r"""
        :param AccountId: 账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountId: str
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
注意：此字段可能返回 null，表示取不到有效值。
        :type IncomeType: int
        :param Balance: 总余额
注意：此字段可能返回 null，表示取不到有效值。
        :type Balance: str
        :param SystemFreezeBalance: 系统冻结余额
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemFreezeBalance: str
        :param ManualFreezeBalance: 人工冻结余额
注意：此字段可能返回 null，表示取不到有效值。
        :type ManualFreezeBalance: str
        :param PayableBalance: 可提现余额
注意：此字段可能返回 null，表示取不到有效值。
        :type PayableBalance: str
        :param PaidBalance: 已提现余额
注意：此字段可能返回 null，表示取不到有效值。
        :type PaidBalance: str
        :param InPayBalance: 提现中余额
注意：此字段可能返回 null，表示取不到有效值。
        :type InPayBalance: str
        """
        self.AccountId = None
        self.IncomeType = None
        self.Balance = None
        self.SystemFreezeBalance = None
        self.ManualFreezeBalance = None
        self.PayableBalance = None
        self.PaidBalance = None
        self.InPayBalance = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.IncomeType = params.get("IncomeType")
        self.Balance = params.get("Balance")
        self.SystemFreezeBalance = params.get("SystemFreezeBalance")
        self.ManualFreezeBalance = params.get("ManualFreezeBalance")
        self.PayableBalance = params.get("PayableBalance")
        self.PaidBalance = params.get("PaidBalance")
        self.InPayBalance = params.get("InPayBalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeAccountInfoResult(AbstractModel):
    """账户信息结果

    """

    def __init__(self):
        r"""
        :param AccountId: 账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountId: str
        :param AccountName: 账户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UserInfo: 用户信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: :class:`tencentcloud.cpdp.v20190820.models.PayeeAccountUserInfo`
        :param PropertyInfo: 属性信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PropertyInfo: :class:`tencentcloud.cpdp.v20190820.models.PayeeAccountPropertyInfo`
        """
        self.AccountId = None
        self.AccountName = None
        self.Remark = None
        self.CreateTime = None
        self.UserInfo = None
        self.PropertyInfo = None


    def _deserialize(self, params):
        self.AccountId = params.get("AccountId")
        self.AccountName = params.get("AccountName")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        if params.get("UserInfo") is not None:
            self.UserInfo = PayeeAccountUserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        if params.get("PropertyInfo") is not None:
            self.PropertyInfo = PayeeAccountPropertyInfo()
            self.PropertyInfo._deserialize(params.get("PropertyInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeAccountInfos(AbstractModel):
    """账户信息列表

    """

    def __init__(self):
        r"""
        :param List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of PayeeAccountInfoResult
        :param Count: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.List = None
        self.Count = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PayeeAccountInfoResult()
                obj._deserialize(item)
                self.List.append(obj)
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeAccountPropertyInfo(AbstractModel):
    """账户属性信息

    """

    def __init__(self):
        r"""
        :param SettleRightStatus: 结算权益状态
ENABLE:启用
DISABLE:停用
注意：此字段可能返回 null，表示取不到有效值。
        :type SettleRightStatus: str
        :param PaymentRightStatus: 付款权益状态
ENABLE:启用
DISABLE:停用
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentRightStatus: str
        """
        self.SettleRightStatus = None
        self.PaymentRightStatus = None


    def _deserialize(self, params):
        self.SettleRightStatus = params.get("SettleRightStatus")
        self.PaymentRightStatus = params.get("PaymentRightStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeAccountUserInfo(AbstractModel):
    """账户用户信息

    """

    def __init__(self):
        r"""
        :param OutUserId: 外部用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OutUserId: str
        :param UserType: 用户类型
0:B端用户
1:C端用户
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: int
        :param IdType: 证件类型
0:身份证
1:社会信用代码
注意：此字段可能返回 null，表示取不到有效值。
        :type IdType: int
        :param IdNo: 证件号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdNo: str
        :param Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self.OutUserId = None
        self.UserType = None
        self.IdType = None
        self.IdNo = None
        self.Name = None


    def _deserialize(self, params):
        self.OutUserId = params.get("OutUserId")
        self.UserType = params.get("UserType")
        self.IdType = params.get("IdType")
        self.IdNo = params.get("IdNo")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeInfoResult(AbstractModel):
    """收款用户信息结果

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param OutUserId: 用户外部业务ID
        :type OutUserId: str
        :param Name: 姓名
        :type Name: str
        :param IdType: 证件类型
0:身份证
1:社会信用代码
        :type IdType: int
        :param IdNo: 证件号
        :type IdNo: str
        :param ServiceProviderId: 服务商ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceProviderId: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.PayeeId = None
        self.OutUserId = None
        self.Name = None
        self.IdType = None
        self.IdNo = None
        self.ServiceProviderId = None
        self.Remark = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.OutUserId = params.get("OutUserId")
        self.Name = params.get("Name")
        self.IdType = params.get("IdType")
        self.IdNo = params.get("IdNo")
        self.ServiceProviderId = params.get("ServiceProviderId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeTaxInfo(AbstractModel):
    """计税信息

    """

    def __init__(self):
        r"""
        :param TaxTemplateInfoList: 计税模板列表
        :type TaxTemplateInfoList: list of PayeeTaxTemplateInfo
        :param TaxpayerIdNo: 纳税人识别号
        :type TaxpayerIdNo: str
        :param TaxEntityType: 纳税主体类型
NATURAL:自然人
NON_NATURAL:非自然人
        :type TaxEntityType: str
        :param TaxServiceProviderId: 财税服务商ID
        :type TaxServiceProviderId: str
        """
        self.TaxTemplateInfoList = None
        self.TaxpayerIdNo = None
        self.TaxEntityType = None
        self.TaxServiceProviderId = None


    def _deserialize(self, params):
        if params.get("TaxTemplateInfoList") is not None:
            self.TaxTemplateInfoList = []
            for item in params.get("TaxTemplateInfoList"):
                obj = PayeeTaxTemplateInfo()
                obj._deserialize(item)
                self.TaxTemplateInfoList.append(obj)
        self.TaxpayerIdNo = params.get("TaxpayerIdNo")
        self.TaxEntityType = params.get("TaxEntityType")
        self.TaxServiceProviderId = params.get("TaxServiceProviderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PayeeTaxTemplateInfo(AbstractModel):
    """收款用户计税模板信息

    """

    def __init__(self):
        r"""
        :param IncomeType: 收入类型
LABOR: 劳务所得
OCCASION: 偶然所得
        :type IncomeType: str
        :param TaxTemplateId: 计税模板ID
        :type TaxTemplateId: str
        """
        self.IncomeType = None
        self.TaxTemplateId = None


    def _deserialize(self, params):
        self.IncomeType = params.get("IncomeType")
        self.TaxTemplateId = params.get("TaxTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentOrderResult(AbstractModel):
    """付款订单结果

    """

    def __init__(self):
        r"""
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param AmountAfterTax: 税后金额
        :type AmountAfterTax: str
        :param Tax: 税金
        :type Tax: str
        :param OutOrderId: 外部订单ID
        :type OutOrderId: str
        :param OrderId: 订单ID
        :type OrderId: str
        :param InitiateTime: 发起时间
        :type InitiateTime: str
        :param FinishTime: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        :param Status: 状态
ACCEPTED:已受理
ACCOUNTED:已记账
PAYING:付款中
PAYED:完成付款渠道调用
SUCCEED:已成功
FAILED:已失败
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        :param Remark: 提现备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.IncomeType = None
        self.AmountBeforeTax = None
        self.AmountAfterTax = None
        self.Tax = None
        self.OutOrderId = None
        self.OrderId = None
        self.InitiateTime = None
        self.FinishTime = None
        self.Status = None
        self.StatusDesc = None
        self.Remark = None


    def _deserialize(self, params):
        self.IncomeType = params.get("IncomeType")
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.AmountAfterTax = params.get("AmountAfterTax")
        self.Tax = params.get("Tax")
        self.OutOrderId = params.get("OutOrderId")
        self.OrderId = params.get("OrderId")
        self.InitiateTime = params.get("InitiateTime")
        self.FinishTime = params.get("FinishTime")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentOrderStatusResult(AbstractModel):
    """付款订单状态结果

    """

    def __init__(self):
        r"""
        :param Status: 状态
ACCEPTED:已受理
ACCOUNTED:已记账
PAYING:付款中
PAYED:完成付款渠道调用
SUCCEED:已成功
FAILED:已失败
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        """
        self.Status = None
        self.StatusDesc = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PaymentOrders(AbstractModel):
    """付款订单列表

    """

    def __init__(self):
        r"""
        :param List: 列表
        :type List: list of PaymentOrderResult
        :param Count: 总数
        :type Count: int
        """
        self.List = None
        self.Count = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PaymentOrderResult()
                obj._deserialize(item)
                self.List.append(obj)
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctBindingRequest(AbstractModel):
    """QueryAcctBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctBindingResponse(AbstractModel):
    """QueryAcctBinding返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总行数
        :type TotalCount: int
        :param BankCardItems: 银行卡信息列表
        :type BankCardItems: list of BankCardItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BankCardItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BankCardItems") is not None:
            self.BankCardItems = []
            for item in params.get("BankCardItems"):
                obj = BankCardItem()
                obj._deserialize(item)
                self.BankCardItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryAcctInfoListRequest(AbstractModel):
    """QueryAcctInfoList请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param QueryAcctBeginTime: 查询开始时间(以开户时间为准)
        :type QueryAcctBeginTime: str
        :param QueryAcctEndTime: 查询结束时间(以开户时间为准)
        :type QueryAcctEndTime: str
        :param PageOffset: 分页号,  起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照开户时间的先后
        :type PageOffset: str
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.QueryAcctBeginTime = None
        self.QueryAcctEndTime = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.QueryAcctBeginTime = params.get("QueryAcctBeginTime")
        self.QueryAcctEndTime = params.get("QueryAcctEndTime")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctInfoListResponse(AbstractModel):
    """QueryAcctInfoList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultCount: 本次交易返回查询结果记录数
        :type ResultCount: int
        :param TotalCount: 符合业务查询条件的记录总数
        :type TotalCount: int
        :param QueryAcctItems: 查询结果项 [object,object]
        :type QueryAcctItems: list of QueryAcctItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCount = None
        self.TotalCount = None
        self.QueryAcctItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.TotalCount = params.get("TotalCount")
        if params.get("QueryAcctItems") is not None:
            self.QueryAcctItems = []
            for item in params.get("QueryAcctItems"):
                obj = QueryAcctItem()
                obj._deserialize(item)
                self.QueryAcctItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryAcctInfoRequest(AbstractModel):
    """QueryAcctInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId
        :type MidasAppId: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param MidasSecretId: 由平台客服提供的计费密钥Id
        :type MidasSecretId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.SubMchId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAcctInfoResponse(AbstractModel):
    """QueryAcctInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubMchName: 子商户名称
        :type SubMchName: str
        :param SubMchType: 子商户类型：
个人: personal
企业：enterprise
缺省： enterprise
        :type SubMchType: str
        :param ShortName: 不填则默认子商户名称
        :type ShortName: str
        :param Address: 子商户地址
        :type Address: str
        :param Contact: 子商户联系人子商户联系人
<敏感信息>
        :type Contact: str
        :param Mobile: 联系人手机号
<敏感信息>
        :type Mobile: str
        :param Email: 邮箱 
<敏感信息>
        :type Email: str
        :param SubMchId: 子商户id
        :type SubMchId: str
        :param SubAcctNo: 子账户
        :type SubAcctNo: str
        :param SubMerchantMemberType: 子商户会员类型：
general:普通子账户
merchant:商户子账户
缺省： general
注意：此字段可能返回 null，表示取不到有效值。
        :type SubMerchantMemberType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.SubMchName = None
        self.SubMchType = None
        self.ShortName = None
        self.Address = None
        self.Contact = None
        self.Mobile = None
        self.Email = None
        self.SubMchId = None
        self.SubAcctNo = None
        self.SubMerchantMemberType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubMchName = params.get("SubMchName")
        self.SubMchType = params.get("SubMchType")
        self.ShortName = params.get("ShortName")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SubMchId = params.get("SubMchId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")
        self.RequestId = params.get("RequestId")


class QueryAcctItem(AbstractModel):
    """查询账户列表接口

    """

    def __init__(self):
        r"""
        :param SubMchType: 子商户类型：
个人: personal
企业：enterprise
缺省： enterprise
        :type SubMchType: str
        :param SubMchName: 子商户名称
        :type SubMchName: str
        :param SubAcctNo: 子账号
        :type SubAcctNo: str
        :param ShortName: 不填则默认子商户名称
        :type ShortName: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param Contact: 子商户联系人
<敏感信息>
        :type Contact: str
        :param Address: 子商户地址
        :type Address: str
        :param Mobile: 联系人手机号
<敏感信息>
        :type Mobile: str
        :param Email: 邮箱 
<敏感信息>
        :type Email: str
        :param SubMerchantMemberType: 子商户会员类型：
general:普通子账户
merchant:商户子账户
缺省： general
注意：此字段可能返回 null，表示取不到有效值。
        :type SubMerchantMemberType: str
        """
        self.SubMchType = None
        self.SubMchName = None
        self.SubAcctNo = None
        self.ShortName = None
        self.SubMchId = None
        self.SubAppId = None
        self.Contact = None
        self.Address = None
        self.Mobile = None
        self.Email = None
        self.SubMerchantMemberType = None


    def _deserialize(self, params):
        self.SubMchType = params.get("SubMchType")
        self.SubMchName = params.get("SubMchName")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ShortName = params.get("ShortName")
        self.SubMchId = params.get("SubMchId")
        self.SubAppId = params.get("SubAppId")
        self.Contact = params.get("Contact")
        self.Address = params.get("Address")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAgentStatementsRequest(AbstractModel):
    """QueryAgentStatements请求参数结构体

    """

    def __init__(self):
        r"""
        :param Date: 结算单日期，月结算单填每月1日
        :type Date: str
        :param Type: 日结算单:daily
月结算单:monthly
        :type Type: str
        """
        self.Date = None
        self.Type = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAgentStatementsResponse(AbstractModel):
    """QueryAgentStatements返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrl: 文件下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.RequestId = params.get("RequestId")


class QueryAgentTaxPaymentBatchRequest(AbstractModel):
    """QueryAgentTaxPaymentBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchNum: 批次号
        :type BatchNum: int
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.BatchNum = None
        self.Profile = None


    def _deserialize(self, params):
        self.BatchNum = params.get("BatchNum")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAgentTaxPaymentBatchResponse(AbstractModel):
    """QueryAgentTaxPaymentBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param AgentTaxPaymentBatch: 代理商完税证明批次信息
        :type AgentTaxPaymentBatch: :class:`tencentcloud.cpdp.v20190820.models.AgentTaxPaymentBatch`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AgentTaxPaymentBatch = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentTaxPaymentBatch") is not None:
            self.AgentTaxPaymentBatch = AgentTaxPaymentBatch()
            self.AgentTaxPaymentBatch._deserialize(params.get("AgentTaxPaymentBatch"))
        self.RequestId = params.get("RequestId")


class QueryAnchorContractInfoRequest(AbstractModel):
    """QueryAnchorContractInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginTime: 起始时间，格式为yyyy-MM-dd
        :type BeginTime: str
        :param EndTime: 起始时间，格式为yyyy-MM-dd
        :type EndTime: str
        """
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAnchorContractInfoResponse(AbstractModel):
    """QueryAnchorContractInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorContractInfoList: 签约主播数据
        :type AnchorContractInfoList: list of AnchorContractInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AnchorContractInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AnchorContractInfoList") is not None:
            self.AnchorContractInfoList = []
            for item in params.get("AnchorContractInfoList"):
                obj = AnchorContractInfo()
                obj._deserialize(item)
                self.AnchorContractInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryApplicationMaterialRequest(AbstractModel):
    """QueryApplicationMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.DeclareId = None
        self.Profile = None


    def _deserialize(self, params):
        self.DeclareId = params.get("DeclareId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryApplicationMaterialResponse(AbstractModel):
    """QueryApplicationMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 成功申报材料查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryDeclareResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryAssignmentRequest(AbstractModel):
    """QueryAssignment请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播ID
        :type AnchorId: str
        """
        self.AnchorId = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryAssignmentResponse(AbstractModel):
    """QueryAssignment返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMsg: 响应消息
        :type ErrMsg: str
        :param Result: 返回响应
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.AssignmentData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMsg = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("Result") is not None:
            self.Result = AssignmentData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryBalanceRequest(AbstractModel):
    """QueryBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param QueryFlag: 2：普通会员子账号
3：功能子账号
        :type QueryFlag: str
        :param PageOffset: 起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后
        :type PageOffset: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.QueryFlag = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.QueryFlag = params.get("QueryFlag")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBalanceResponse(AbstractModel):
    """QueryBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultCount: 本次交易返回查询结果记录数
        :type ResultCount: str
        :param StartRecordOffset: 起始记录号
        :type StartRecordOffset: str
        :param EndFlag: 结束标志
        :type EndFlag: str
        :param TotalCount: 符合业务查询条件的记录总数
        :type TotalCount: str
        :param QueryItems: 查询结果项
        :type QueryItems: list of QueryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultCount = None
        self.StartRecordOffset = None
        self.EndFlag = None
        self.TotalCount = None
        self.QueryItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.StartRecordOffset = params.get("StartRecordOffset")
        self.EndFlag = params.get("EndFlag")
        self.TotalCount = params.get("TotalCount")
        if params.get("QueryItems") is not None:
            self.QueryItems = []
            for item in params.get("QueryItems"):
                obj = QueryItem()
                obj._deserialize(item)
                self.QueryItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryBankClearRequest(AbstractModel):
    """QueryBankClear请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 全部; 2: 指定时间段）
        :type FunctionFlag: str
        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param StartDate: STRING(8)，开始日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式: 20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（若是指定时间段查询，则必输，当查询全部时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBankClearResponse(AbstractModel):
    """QueryBankClear返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数, 一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of ClearItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = ClearItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankTransactionDetailsRequest(AbstractModel):
    """QueryBankTransactionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查询标志（1: 全部; 2: 转出; 3: 转入 ）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param StartDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBankTransactionDetailsResponse(AbstractModel):
    """QueryBankTransactionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransactionItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransactionItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankWithdrawCashDetailsRequest(AbstractModel):
    """QueryBankWithdrawCashDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 当日; 2: 历史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查询标志（2: 提现; 3: 清分）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param BeginDate: STRING(8)，开始日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type BeginDate: str
        :param EndDate: STRING(8)，结束日期（若是历史查询，则必输，当日查询时，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.BeginDate = None
        self.EndDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBankWithdrawCashDetailsResponse(AbstractModel):
    """QueryBankWithdrawCashDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0:否; 1:是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of WithdrawItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = WithdrawItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBatchPaymentResultData(AbstractModel):
    """QueryBatchPaymentResult接口返回响应

    """

    def __init__(self):
        r"""
        :param BatchId: 批次号
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchId: str
        :param TotalAmount: 批次总额
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAmount: int
        :param TotalCount: 批次总量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ReqReserved: 批次预留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ReqReserved: str
        :param Remark: 批次备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param TransferType: 渠道类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferType: int
        :param TransferInfoList: 转账明细
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferInfoList: list of QueryBatchPaymentResultDataInfo
        """
        self.BatchId = None
        self.TotalAmount = None
        self.TotalCount = None
        self.ReqReserved = None
        self.Remark = None
        self.TransferType = None
        self.TransferInfoList = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.TotalAmount = params.get("TotalAmount")
        self.TotalCount = params.get("TotalCount")
        self.ReqReserved = params.get("ReqReserved")
        self.Remark = params.get("Remark")
        self.TransferType = params.get("TransferType")
        if params.get("TransferInfoList") is not None:
            self.TransferInfoList = []
            for item in params.get("TransferInfoList"):
                obj = QueryBatchPaymentResultDataInfo()
                obj._deserialize(item)
                self.TransferInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBatchPaymentResultDataInfo(AbstractModel):
    """QueryBatchPaymentResultData复杂类型中的TransferInfoList

    """

    def __init__(self):
        r"""
        :param OrderId: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param AgentId: 代理商ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param AgentName: 代理商名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        :param Status: 交易状态。
0 处理中  
1 预占成功 
2 交易成功 
3 交易失败 
4 未知渠道异常 
5 预占额度失败
6 提交成功
7 提交失败
8 订单重复提交
99 未知系统异常
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param TransferAmount: 转账金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferAmount: int
        """
        self.OrderId = None
        self.AgentId = None
        self.AgentName = None
        self.Status = None
        self.StatusDesc = None
        self.TransferAmount = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.TransferAmount = params.get("TransferAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBatchPaymentResultRequest(AbstractModel):
    """QueryBatchPaymentResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param BatchId: 批次号
        :type BatchId: str
        """
        self.BatchId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBatchPaymentResultResponse(AbstractModel):
    """QueryBatchPaymentResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMessage: 响应消息。
        :type ErrMessage: str
        :param Result: 返回响应
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryBatchPaymentResultData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryBatchPaymentResultData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryBillDownloadURLData(AbstractModel):
    """智能代发-单笔代发转账对账单返回数据

    """

    def __init__(self):
        r"""
        :param BillDownloadURL: 统一对账单下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type BillDownloadURL: str
        :param OriginalBillDownloadURL: 渠道原始对账单下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalBillDownloadURL: str
        """
        self.BillDownloadURL = None
        self.OriginalBillDownloadURL = None


    def _deserialize(self, params):
        self.BillDownloadURL = params.get("BillDownloadURL")
        self.OriginalBillDownloadURL = params.get("OriginalBillDownloadURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBillDownloadURLRequest(AbstractModel):
    """QueryBillDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransferType: 代发类型：
1、 微信企业付款 
2、 支付宝转账 
3、 平安银企直联代发转账
        :type TransferType: int
        :param BillDate: 账单日期，格式yyyy-MM-dd
        :type BillDate: str
        """
        self.MerchantId = None
        self.TransferType = None
        self.BillDate = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransferType = params.get("TransferType")
        self.BillDate = params.get("BillDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryBillDownloadURLResponse(AbstractModel):
    """QueryBillDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功
        :type ErrCode: str
        :param ErrMessage: 响应消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryBillDownloadURLData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryBillDownloadURLData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryCityCodeRequest(AbstractModel):
    """QueryCityCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCityCodeResponse(AbstractModel):
    """QueryCityCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 查询城市编码响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of CityCodeResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = CityCodeResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCloudChannelDataRequest(AbstractModel):
    """QueryCloudChannelData请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 米大师分配的支付主MidasAppId
        :type MidasAppId: str
        :param OutOrderNo: 业务订单号，外部订单号
        :type OutOrderNo: str
        :param ExternalChannelDataType: 数据类型
PAYMENT:支付
        :type ExternalChannelDataType: str
        :param MidasEnvironment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type MidasEnvironment: str
        :param SubAppId: 子应用ID
        :type SubAppId: str
        :param ChannelOrderId: 渠道订单号
        :type ChannelOrderId: str
        :param Channel: 渠道名称，指定渠道查询
wechat:微信支付
        :type Channel: str
        """
        self.MidasAppId = None
        self.OutOrderNo = None
        self.ExternalChannelDataType = None
        self.MidasEnvironment = None
        self.SubAppId = None
        self.ChannelOrderId = None
        self.Channel = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.OutOrderNo = params.get("OutOrderNo")
        self.ExternalChannelDataType = params.get("ExternalChannelDataType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.SubAppId = params.get("SubAppId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCloudChannelDataResponse(AbstractModel):
    """QueryCloudChannelData返回参数结构体

    """

    def __init__(self):
        r"""
        :param OutOrderNo: 外部订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutOrderNo: str
        :param ChannelOrderId: 渠道订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelOrderId: str
        :param ExternalChannelDataType: 第三方渠道数据类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalChannelDataType: str
        :param Channel: 渠道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: str
        :param ExternalChannelDataList: 第三方渠道数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalChannelDataList: list of CloudExternalChannelData
        :param SubAppId: 子应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAppId: str
        :param AppId: 米大师分配的支付主MidasAppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OutOrderNo = None
        self.ChannelOrderId = None
        self.ExternalChannelDataType = None
        self.Channel = None
        self.ExternalChannelDataList = None
        self.SubAppId = None
        self.AppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OutOrderNo = params.get("OutOrderNo")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.ExternalChannelDataType = params.get("ExternalChannelDataType")
        self.Channel = params.get("Channel")
        if params.get("ExternalChannelDataList") is not None:
            self.ExternalChannelDataList = []
            for item in params.get("ExternalChannelDataList"):
                obj = CloudExternalChannelData()
                obj._deserialize(item)
                self.ExternalChannelDataList.append(obj)
        self.SubAppId = params.get("SubAppId")
        self.AppId = params.get("AppId")
        self.RequestId = params.get("RequestId")


class QueryCloudOrderRequest(AbstractModel):
    """QueryCloudOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 米大师分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户Id，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param Type: 查询类型
by_order:根据订单号查订单
        :type Type: str
        :param MidasEnvironment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type MidasEnvironment: str
        :param OutTradeNo: 开发者的主订单号
        :type OutTradeNo: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.Type = None
        self.MidasEnvironment = None
        self.OutTradeNo = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Type = params.get("Type")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.OutTradeNo = params.get("OutTradeNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCloudOrderResponse(AbstractModel):
    """QueryCloudOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 订单数量
        :type TotalNum: int
        :param OrderList: 订单列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderList: list of CloudOrderReturn
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.OrderList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("OrderList") is not None:
            self.OrderList = []
            for item in params.get("OrderList"):
                obj = CloudOrderReturn()
                obj._deserialize(item)
                self.OrderList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryCloudRefundOrderRequest(AbstractModel):
    """QueryCloudRefundOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 米大师分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户Id，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type RefundId: str
        :param MidasEnvironment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.RefundId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCloudRefundOrderResponse(AbstractModel):
    """QueryCloudRefundOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param OutTradeNo: 该笔退款订单对应的UnifiedOrder下单时传入的OutTradeNo
        :type OutTradeNo: str
        :param ChannelExternalOrderId: 该笔退款订单对应的支付成功后支付机构返回的支付订单号
        :type ChannelExternalOrderId: str
        :param ChannelExternalRefundId: 该笔退款订单退款后支付机构返回的退款单号
        :type ChannelExternalRefundId: str
        :param ChannelOrderId: 内部请求微信支付、银行等支付机构的订单号
        :type ChannelOrderId: str
        :param RefundId: 请求退款时传的退款ID后查询退款时传的RefundId
        :type RefundId: str
        :param UsedRefundId: 被使用的RefundId，业务可忽略该字段
        :type UsedRefundId: str
        :param TotalRefundAmt: 退款总金额
        :type TotalRefundAmt: int
        :param CurrencyType: ISO货币代码
        :type CurrencyType: str
        :param State: 退款状态码，退款提交成功后返回
1:退款中
2:退款成功
3:退款失败
        :type State: str
        :param SubRefundList: 子单退款信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubRefundList: list of CloudSubRefundItem
        :param Metadata: 透传字段，退款成功回调透传给应用，用于开发者透传自定义内容
        :type Metadata: str
        :param AppId: 米大师分配的支付主MidasAppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param ChannelRefundId: 该笔退款订单退款后内部返回的退款单号
        :type ChannelRefundId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OutTradeNo = None
        self.ChannelExternalOrderId = None
        self.ChannelExternalRefundId = None
        self.ChannelOrderId = None
        self.RefundId = None
        self.UsedRefundId = None
        self.TotalRefundAmt = None
        self.CurrencyType = None
        self.State = None
        self.SubRefundList = None
        self.Metadata = None
        self.AppId = None
        self.ChannelRefundId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OutTradeNo = params.get("OutTradeNo")
        self.ChannelExternalOrderId = params.get("ChannelExternalOrderId")
        self.ChannelExternalRefundId = params.get("ChannelExternalRefundId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.RefundId = params.get("RefundId")
        self.UsedRefundId = params.get("UsedRefundId")
        self.TotalRefundAmt = params.get("TotalRefundAmt")
        self.CurrencyType = params.get("CurrencyType")
        self.State = params.get("State")
        if params.get("SubRefundList") is not None:
            self.SubRefundList = []
            for item in params.get("SubRefundList"):
                obj = CloudSubRefundItem()
                obj._deserialize(item)
                self.SubRefundList.append(obj)
        self.Metadata = params.get("Metadata")
        self.AppId = params.get("AppId")
        self.ChannelRefundId = params.get("ChannelRefundId")
        self.RequestId = params.get("RequestId")


class QueryCommonTransferRechargeRequest(AbstractModel):
    """QueryCommonTransferRecharge请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1为查询当日数据，0查询历史数据）
        :type FunctionFlag: str
        :param StartDate: STRING(8)，开始日期（格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，终止日期（格式：20190101）
        :type EndDate: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.StartDate = None
        self.EndDate = None
        self.PageNum = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.PageNum = params.get("PageNum")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCommonTransferRechargeResponse(AbstractModel):
    """QueryCommonTransferRecharge返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransferItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransferItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryContractPayFeeRequest(AbstractModel):
    """QueryContractPayFee请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param PaymentId: 支付方式编号
        :type PaymentId: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.PaymentId = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.PaymentId = params.get("PaymentId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryContractPayFeeResponse(AbstractModel):
    """QueryContractPayFee返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码，0表示成功，其他表示失败。
        :type ErrCode: str
        :param Result: 查询支付方式费率及自定义表单项响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryContractPayFeeResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = QueryContractPayFeeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryContractPayFeeResult(AbstractModel):
    """支付方式费率及自定义表单项

    """

    def __init__(self):
        r"""
        :param Pay: pay支付方式json数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Pay: :class:`tencentcloud.cpdp.v20190820.models.PayDataResult`
        :param ExtraInput: 合同扩展自定义字段
        :type ExtraInput: list of str
        :param PayFee: pay_fee支付方式行业分类费率json数据
注意：此字段可能返回 null，表示取不到有效值。
        :type PayFee: list of PayFeeDataResult
        """
        self.Pay = None
        self.ExtraInput = None
        self.PayFee = None


    def _deserialize(self, params):
        if params.get("Pay") is not None:
            self.Pay = PayDataResult()
            self.Pay._deserialize(params.get("Pay"))
        self.ExtraInput = params.get("ExtraInput")
        if params.get("PayFee") is not None:
            self.PayFee = []
            for item in params.get("PayFee"):
                obj = PayFeeDataResult()
                obj._deserialize(item)
                self.PayFee.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryContractPayWayListRequest(AbstractModel):
    """QueryContractPayWayList请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryContractPayWayListResponse(AbstractModel):
    """QueryContractPayWayList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 查询合同支付方式响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of ContractPayListResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ContractPayListResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class QueryContractRelateShopRequest(AbstractModel):
    """QueryContractRelateShop请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param ContractId: 合同主键
        :type ContractId: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.ContractId = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.ContractId = params.get("ContractId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryContractRelateShopResponse(AbstractModel):
    """QueryContractRelateShop返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 查询合同可关联门店响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of QueryContractRelateShopResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = QueryContractRelateShopResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class QueryContractRelateShopResult(AbstractModel):
    """合同可关联门店响应对象

    """

    def __init__(self):
        r"""
        :param Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param CityId: 城市编码
注意：此字段可能返回 null，表示取不到有效值。
        :type CityId: str
        :param ShopName: 门店简称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopName: str
        :param TerminalCount: 终端数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminalCount: str
        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param ShopStatus: 门店状态（0未审核，1已审核，2审核未通过，3待审核，4已删除，5初审通过）
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopStatus: str
        :param AliPayOnline: 若是支付宝合同，支付宝上线状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AliPayOnline: str
        :param ShopNo: 门店编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopNo: str
        :param Country: 县/区
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param AliPayStatus: 若是支付宝合同，支付宝审核状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AliPayStatus: str
        :param IsChecked: 为空或者0表示未关联，大于0表示已关联
注意：此字段可能返回 null，表示取不到有效值。
        :type IsChecked: str
        :param Address: 详细地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param AliPayDesc: 若是支付宝合同，支付宝审核描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AliPayDesc: str
        """
        self.Province = None
        self.CityId = None
        self.ShopName = None
        self.TerminalCount = None
        self.City = None
        self.ShopStatus = None
        self.AliPayOnline = None
        self.ShopNo = None
        self.Country = None
        self.AliPayStatus = None
        self.IsChecked = None
        self.Address = None
        self.AliPayDesc = None


    def _deserialize(self, params):
        self.Province = params.get("Province")
        self.CityId = params.get("CityId")
        self.ShopName = params.get("ShopName")
        self.TerminalCount = params.get("TerminalCount")
        self.City = params.get("City")
        self.ShopStatus = params.get("ShopStatus")
        self.AliPayOnline = params.get("AliPayOnline")
        self.ShopNo = params.get("ShopNo")
        self.Country = params.get("Country")
        self.AliPayStatus = params.get("AliPayStatus")
        self.IsChecked = params.get("IsChecked")
        self.Address = params.get("Address")
        self.AliPayDesc = params.get("AliPayDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryContractRequest(AbstractModel):
    """QueryContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param Channel: 指定渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定
        :type Channel: str
        :param ContractQueryMode: 枚举值：
CONTRACT_QUERY_MODE_BY_OUT_CONTRACT_CODE：按 OutContractCode + ContractSceneId 查询
CONTRACT_QUERY_MODE_BY_CHANNEL_CONTRACT_CODE：按ChannelContractCode查询
        :type ContractQueryMode: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param OutContractCode: 业务签约合同协议号 当 ContractQueryMode=CONTRACT_QUERY_MODE_BY_OUT_CONTRACT_CODE 时 ，必填
        :type OutContractCode: str
        :param ContractSceneId: 签约场景ID，当 ContractQueryMode=CONTRACT_QUERY_MODE_BY_OUT_CONTRACT_CODE 时 必填，在米大师侧托管后生成
        :type ContractSceneId: str
        :param ChannelContractCode: 米大师生成的协议号 ，当 ContractQueryMode=CONTRACT_QUERY_MODE_BY_CHANNEL_CONTRACT_CODE 时必填
        :type ChannelContractCode: str
        :param ExternalContractData: 第三方渠道合约数据，为json字符串，与特定渠道有关
        :type ExternalContractData: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param UserType: USER_ID: 用户ID
ANONYMOUS: 匿名类型 USER_ID
默认值为 USER_ID
        :type UserType: str
        :param MigrateMode: 签约代扣穿透查询存量数据迁移模式
        :type MigrateMode: str
        :param ContractMethod: 签约方式
        :type ContractMethod: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.Channel = None
        self.ContractQueryMode = None
        self.MidasSignature = None
        self.MidasSecretId = None
        self.SubAppId = None
        self.OutContractCode = None
        self.ContractSceneId = None
        self.ChannelContractCode = None
        self.ExternalContractData = None
        self.MidasEnvironment = None
        self.UserType = None
        self.MigrateMode = None
        self.ContractMethod = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.ContractQueryMode = params.get("ContractQueryMode")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasSecretId = params.get("MidasSecretId")
        self.SubAppId = params.get("SubAppId")
        self.OutContractCode = params.get("OutContractCode")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ChannelContractCode = params.get("ChannelContractCode")
        self.ExternalContractData = params.get("ExternalContractData")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.UserType = params.get("UserType")
        self.MigrateMode = params.get("MigrateMode")
        self.ContractMethod = params.get("ContractMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryContractResponse(AbstractModel):
    """QueryContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContractData: 签约数据
        :type ContractData: :class:`tencentcloud.cpdp.v20190820.models.ResponseQueryContract`
        :param Msg: 请求处理信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContractData = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContractData") is not None:
            self.ContractData = ResponseQueryContract()
            self.ContractData._deserialize(params.get("ContractData"))
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class QueryCustAcctIdBalanceRequest(AbstractModel):
    """QueryCustAcctIdBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查询标志（2: 普通会员子账号; 3: 功能子账号）
        :type QueryFlag: str
        :param PageNum: STRING(10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2时，子账号必输）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryCustAcctIdBalanceResponse(AbstractModel):
    """QueryCustAcctIdBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param AcctArray: 账户信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctArray: list of Acct
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.AcctArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("AcctArray") is not None:
            self.AcctArray = []
            for item in params.get("AcctArray"):
                obj = Acct()
                obj._deserialize(item)
                self.AcctArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryDeclareData(AbstractModel):
    """成功申报材料查询数据

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param DeclareId: 申报流水号
        :type DeclareId: str
        :param OriginalDeclareId: 原申报流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalDeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param SourceAmount: 源金额
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAmount: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param TargetAmount: 目的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAmount: str
        :param TradeCode: 交易编码
        :type TradeCode: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.DeclareId = None
        self.OriginalDeclareId = None
        self.PayerId = None
        self.SourceCurrency = None
        self.SourceAmount = None
        self.TargetCurrency = None
        self.TargetAmount = None
        self.TradeCode = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.DeclareId = params.get("DeclareId")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.PayerId = params.get("PayerId")
        self.SourceCurrency = params.get("SourceCurrency")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TargetAmount = params.get("TargetAmount")
        self.TradeCode = params.get("TradeCode")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDeclareResult(AbstractModel):
    """成功申报材料查询结果

    """

    def __init__(self):
        r"""
        :param Data: 成功申报材料查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareData`
        :param Code: 错误码
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryDeclareData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDownloadBillURLRequest(AbstractModel):
    """QueryDownloadBillURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 分配给商户的AppId。进件成功后返给商户方的AppId。
        :type MerchantAppId: str
        :param ChannelCode: 渠道编号。固定值：ZSB2B
        :type ChannelCode: str
        :param BillDate: 对账单日期，格式yyyyMMdd
        :type BillDate: str
        """
        self.MerchantAppId = None
        self.ChannelCode = None
        self.BillDate = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.ChannelCode = params.get("ChannelCode")
        self.BillDate = params.get("BillDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDownloadBillURLResponse(AbstractModel):
    """QueryDownloadBillURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 分配给商户的AppId。进件成功后返给商户方的AppId。
        :type MerchantAppId: str
        :param DownloadUrl: 对账单下载地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantAppId = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class QueryExceedingInfoData(AbstractModel):
    """超额信息数据

    """

    def __init__(self):
        r"""
        :param AgentId: 代理商ID。
        :type AgentId: str
        :param AgentName: 代理商名称。
        :type AgentName: str
        :param AnchorId: 主播ID。当入参Dimension为ANCHOR或ORDER时，该字段才会有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnchorId: str
        :param AnchorName: 主播名称。当入参Dimension为ANCHOR或ORDER时，该字段才会有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type AnchorName: str
        :param OrderId: 订单号。当入参Dimension为ORDER时，该字段才会有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param ExceedingType: 超额类型。目前支持 AGENT_EXCEED_100 和 ANCHOR_EXCEED_100_12 两种类型。
        :type ExceedingType: str
        """
        self.AgentId = None
        self.AgentName = None
        self.AnchorId = None
        self.AnchorName = None
        self.OrderId = None
        self.ExceedingType = None


    def _deserialize(self, params):
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        self.AnchorId = params.get("AnchorId")
        self.AnchorName = params.get("AnchorName")
        self.OrderId = params.get("OrderId")
        self.ExceedingType = params.get("ExceedingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExceedingInfoRequest(AbstractModel):
    """QueryExceedingInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param TimeStr: 超额日期。格式为yyyy-MM-dd。
        :type TimeStr: str
        :param Dimension: 维度。目前支持三个维度: AGENT, ANCHOR, ORDER。不填默认使用AGENT维度。
        :type Dimension: str
        :param PageNumber: 分页信息。不填默认Index为1，Count为100。
        :type PageNumber: :class:`tencentcloud.cpdp.v20190820.models.Paging`
        """
        self.TimeStr = None
        self.Dimension = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.TimeStr = params.get("TimeStr")
        self.Dimension = params.get("Dimension")
        if params.get("PageNumber") is not None:
            self.PageNumber = Paging()
            self.PageNumber._deserialize(params.get("PageNumber"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExceedingInfoResponse(AbstractModel):
    """QueryExceedingInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 超额信息结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryExceedingInfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryExceedingInfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryExceedingInfoResult(AbstractModel):
    """超额信息结果

    """

    def __init__(self):
        r"""
        :param Count: 记录总数。
        :type Count: int
        :param Data: 超额信息数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of QueryExceedingInfoData
        """
        self.Count = None
        self.Data = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryExceedingInfoData()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExchangeRateRequest(AbstractModel):
    """QueryExchangeRate请求参数结构体

    """

    def __init__(self):
        r"""
        :param SourceCurrency: 源币种 (默认CNY)
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种 (见常见问题-汇出币种)
        :type TargetCurrency: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.Profile = None


    def _deserialize(self, params):
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExchangeRateResponse(AbstractModel):
    """QueryExchangeRate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 查询汇率结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryExchangerateResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryExchangerateResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryExchangerateData(AbstractModel):
    """查询汇率数据

    """

    def __init__(self):
        r"""
        :param Rate: 汇率
        :type Rate: str
        :param SourceCurrency: 源币种
        :type SourceCurrency: str
        :param TargetCurrency: 目的币种
        :type TargetCurrency: str
        :param RateTime: 汇率时间
        :type RateTime: str
        :param BaseCurrency: 基准币种
        :type BaseCurrency: str
        """
        self.Rate = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.RateTime = None
        self.BaseCurrency = None


    def _deserialize(self, params):
        self.Rate = params.get("Rate")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.RateTime = params.get("RateTime")
        self.BaseCurrency = params.get("BaseCurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExchangerateResult(AbstractModel):
    """查询汇率结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码
        :type Code: str
        :param Data: 查询汇率数据数组
        :type Data: list of QueryExchangerateData
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryExchangerateData()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryExternalAccountBookResult(AbstractModel):
    """查询第三方电子记账本余额返回值

    """

    def __init__(self):
        r"""
        :param ChannelAccountBookId: 渠道记账本ID
        :type ChannelAccountBookId: str
        :param AvailableBalance: 可用余额。
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableBalance: str
        :param CollectMoneyAccountInfo: 电子记账本对外收款的账户信息。为JSON格式字符串（成功状态下返回）。详情见附录-复杂类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type CollectMoneyAccountInfo: str
        """
        self.ChannelAccountBookId = None
        self.AvailableBalance = None
        self.CollectMoneyAccountInfo = None


    def _deserialize(self, params):
        self.ChannelAccountBookId = params.get("ChannelAccountBookId")
        self.AvailableBalance = params.get("AvailableBalance")
        self.CollectMoneyAccountInfo = params.get("CollectMoneyAccountInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexAmountBeforeTaxRequest(AbstractModel):
    """QueryFlexAmountBeforeTax请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        :param AmountAfterTax: 税后金额
        :type AmountAfterTax: str
        """
        self.PayeeId = None
        self.IncomeType = None
        self.AmountAfterTax = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.IncomeType = params.get("IncomeType")
        self.AmountAfterTax = params.get("AmountAfterTax")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexAmountBeforeTaxResponse(AbstractModel):
    """QueryFlexAmountBeforeTax返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.AmountBeforeTaxResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = AmountBeforeTaxResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexFreezeOrderListRequest(AbstractModel):
    """QueryFlexFreezeOrderList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param OperationType: 操作类型
FREEZE:冻结
UNFREEZE:解冻
        :type OperationType: str
        :param StartTime: 开始时间，格式"yyyy-MM-dd hh:mm:ss"
        :type StartTime: str
        :param EndTime: 结束时间，格式"yyyy-MM-dd hh:mm:ss"
        :type EndTime: str
        :param PageNumber: 分页
        :type PageNumber: :class:`tencentcloud.cpdp.v20190820.models.Paging`
        """
        self.PayeeId = None
        self.OperationType = None
        self.StartTime = None
        self.EndTime = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.OperationType = params.get("OperationType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("PageNumber") is not None:
            self.PageNumber = Paging()
            self.PageNumber._deserialize(params.get("PageNumber"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexFreezeOrderListResponse(AbstractModel):
    """QueryFlexFreezeOrderList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.FreezeOrders`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = FreezeOrders()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexPayeeAccountBalanceRequest(AbstractModel):
    """QueryFlexPayeeAccountBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        """
        self.PayeeId = None
        self.IncomeType = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.IncomeType = params.get("IncomeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexPayeeAccountBalanceResponse(AbstractModel):
    """QueryFlexPayeeAccountBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PayeeAccountBalanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = PayeeAccountBalanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexPayeeAccountInfoRequest(AbstractModel):
    """QueryFlexPayeeAccountInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param OutUserId: 外部用户ID
        :type OutUserId: str
        """
        self.PayeeId = None
        self.OutUserId = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.OutUserId = params.get("OutUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexPayeeAccountInfoResponse(AbstractModel):
    """QueryFlexPayeeAccountInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PayeeAccountInfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = PayeeAccountInfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexPayeeAccountListRequest(AbstractModel):
    """QueryFlexPayeeAccountList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PropertyInfo: 账户属性信息
        :type PropertyInfo: :class:`tencentcloud.cpdp.v20190820.models.PayeeAccountPropertyInfo`
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param PageNumber: 分页
        :type PageNumber: :class:`tencentcloud.cpdp.v20190820.models.Paging`
        """
        self.PropertyInfo = None
        self.StartTime = None
        self.EndTime = None
        self.PageNumber = None


    def _deserialize(self, params):
        if params.get("PropertyInfo") is not None:
            self.PropertyInfo = PayeeAccountPropertyInfo()
            self.PropertyInfo._deserialize(params.get("PropertyInfo"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("PageNumber") is not None:
            self.PageNumber = Paging()
            self.PageNumber._deserialize(params.get("PageNumber"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexPayeeAccountListResponse(AbstractModel):
    """QueryFlexPayeeAccountList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PayeeAccountInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = PayeeAccountInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexPayeeInfoRequest(AbstractModel):
    """QueryFlexPayeeInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param OutUserId: 外部用户ID
        :type OutUserId: str
        """
        self.PayeeId = None
        self.OutUserId = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.OutUserId = params.get("OutUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexPayeeInfoResponse(AbstractModel):
    """QueryFlexPayeeInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PayeeInfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = PayeeInfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexPaymentOrderListRequest(AbstractModel):
    """QueryFlexPaymentOrderList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param StartTime: 开始时间，格式"yyyy-MM-dd hh:mm:ss"
        :type StartTime: str
        :param EndTime: 结束时间，格式"yyyy-MM-dd hh:mm:ss"
        :type EndTime: str
        :param PageNumber: 分页
        :type PageNumber: :class:`tencentcloud.cpdp.v20190820.models.Paging`
        """
        self.PayeeId = None
        self.StartTime = None
        self.EndTime = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("PageNumber") is not None:
            self.PageNumber = Paging()
            self.PageNumber._deserialize(params.get("PageNumber"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexPaymentOrderListResponse(AbstractModel):
    """QueryFlexPaymentOrderList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PaymentOrders`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = PaymentOrders()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexPaymentOrderStatusRequest(AbstractModel):
    """QueryFlexPaymentOrderStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutOrderId: 外部订单ID
        :type OutOrderId: str
        :param OrderId: 订单ID
        :type OrderId: str
        """
        self.OutOrderId = None
        self.OrderId = None


    def _deserialize(self, params):
        self.OutOrderId = params.get("OutOrderId")
        self.OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexPaymentOrderStatusResponse(AbstractModel):
    """QueryFlexPaymentOrderStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PaymentOrderStatusResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = PaymentOrderStatusResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFlexSettlementOrderListRequest(AbstractModel):
    """QueryFlexSettlementOrderList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayeeId: 收款用户ID
        :type PayeeId: str
        :param StartTime: 开始时间，格式"yyyy-MM-dd hh:mm:ss"
        :type StartTime: str
        :param EndTime: 结束时间，格式"yyyy-MM-dd hh:mm:ss"
        :type EndTime: str
        :param PageNumber: 分页
        :type PageNumber: :class:`tencentcloud.cpdp.v20190820.models.Paging`
        """
        self.PayeeId = None
        self.StartTime = None
        self.EndTime = None
        self.PageNumber = None


    def _deserialize(self, params):
        self.PayeeId = params.get("PayeeId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("PageNumber") is not None:
            self.PageNumber = Paging()
            self.PageNumber._deserialize(params.get("PageNumber"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFlexSettlementOrderListResponse(AbstractModel):
    """QueryFlexSettlementOrderList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。SUCCESS为成功，其他为失败
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.SettlementOrders`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = SettlementOrders()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFundsTransactionDetailsRequest(AbstractModel):
    """QueryFundsTransactionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param QueryDateType: 查询的交易发生时间类型。
__1__：当日
__2__：历史
        :type QueryDateType: str
        :param QueryTranType: 查询的交易类型。
__2__：提现/退款
__3__：清分/充值
        :type QueryTranType: str
        :param BankAccountNumber: 父账户账号。
_平安渠道为资金汇总账号_
        :type BankAccountNumber: str
        :param SubAccountNumber: 子账户账号。
_平安渠道为见证子账户的账号_
        :type SubAccountNumber: str
        :param PageOffSet: 分页号, 起始值为1。
        :type PageOffSet: str
        :param QueryStartDate: 查询开始日期，格式：yyyyMMdd。
__若是历史查询，则必输，当日查询时，不起作用；开始日期不能超过当前日期__
        :type QueryStartDate: str
        :param QueryEndDate: 查询终止日期，格式：yyyyMMdd。
__若是历史查询，则必输，当日查询时，不起作用；终止日期不能超过当前日期__
        :type QueryEndDate: str
        :param MidasEnvironment: 环境名。
__release__: 现网环境
__sandbox__: 沙箱环境
__development__: 开发环境
_缺省: release_
        :type MidasEnvironment: str
        """
        self.QueryDateType = None
        self.QueryTranType = None
        self.BankAccountNumber = None
        self.SubAccountNumber = None
        self.PageOffSet = None
        self.QueryStartDate = None
        self.QueryEndDate = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.QueryDateType = params.get("QueryDateType")
        self.QueryTranType = params.get("QueryTranType")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.SubAccountNumber = params.get("SubAccountNumber")
        self.PageOffSet = params.get("PageOffSet")
        self.QueryStartDate = params.get("QueryStartDate")
        self.QueryEndDate = params.get("QueryEndDate")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFundsTransactionDetailsResponse(AbstractModel):
    """QueryFundsTransactionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryFundsTransactionDetailsResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryFundsTransactionDetailsResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryFundsTransactionDetailsResult(AbstractModel):
    """查询会员资金交易信息列表结果

    """

    def __init__(self):
        r"""
        :param ResultCount: 本次交易返回查询结果记录数。
        :type ResultCount: int
        :param TotalCount: 符合业务查询条件的记录总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param EndFlag: 结束标志。
__0__：否
__1__：是
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TranItemArray: 会员资金交易信息数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of FundsTransactionItem
        """
        self.ResultCount = None
        self.TotalCount = None
        self.EndFlag = None
        self.TranItemArray = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.TotalCount = params.get("TotalCount")
        self.EndFlag = params.get("EndFlag")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = FundsTransactionItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceRequest(AbstractModel):
    """QueryInvoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID
0 : 高灯
1 : 票易通
        :type InvoicePlatformId: int
        :param OrderId: 订单号
        :type OrderId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        :param IsRed: 发票种类：
0：蓝票
1：红票【该字段默认为0， 如果需要查询红票信息，本字段必须传1，否则可能查询不到需要的发票信息】。
        :type IsRed: int
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道
        :type InvoiceChannel: int
        :param SellerTaxpayerNum: 当渠道为线下渠道时，必填
        :type SellerTaxpayerNum: str
        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.OrderSn = None
        self.IsRed = None
        self.Profile = None
        self.InvoiceChannel = None
        self.SellerTaxpayerNum = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.OrderSn = params.get("OrderSn")
        self.IsRed = params.get("IsRed")
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceResponse(AbstractModel):
    """QueryInvoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 发票查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryInvoiceResult(AbstractModel):
    """查询发票结果

    """

    def __init__(self):
        r"""
        :param Message: 错误消息
        :type Message: str
        :param Code: 错误码
        :type Code: int
        :param Data: 查询发票数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResultData`
        :param Order: 订单数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: :class:`tencentcloud.cpdp.v20190820.models.Order`
        """
        self.Message = None
        self.Code = None
        self.Data = None
        self.Order = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryInvoiceResultData()
            self.Data._deserialize(params.get("Data"))
        if params.get("Order") is not None:
            self.Order = Order()
            self.Order._deserialize(params.get("Order"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceResultData(AbstractModel):
    """查询发票结果数据

    """

    def __init__(self):
        r"""
        :param OrderId: 订单号
        :type OrderId: str
        :param OrderSn: 业务开票号
        :type OrderSn: str
        :param Status: 发票状态
        :type Status: int
        :param Message: 开票描述
        :type Message: str
        :param TicketDate: 开票日期
        :type TicketDate: str
        :param TicketSn: 发票号码
        :type TicketSn: str
        :param TicketCode: 发票代码
        :type TicketCode: str
        :param CheckCode: 检验码
        :type CheckCode: str
        :param AmountWithTax: 含税金额(元)
        :type AmountWithTax: str
        :param AmountWithoutTax: 不含税金额(元)
        :type AmountWithoutTax: str
        :param TaxAmount: 税额(元)
        :type TaxAmount: str
        :param IsRedWashed: 是否被红冲
        :type IsRedWashed: int
        :param PdfUrl: pdf地址
        :type PdfUrl: str
        :param ImageUrl: png地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: str
        """
        self.OrderId = None
        self.OrderSn = None
        self.Status = None
        self.Message = None
        self.TicketDate = None
        self.TicketSn = None
        self.TicketCode = None
        self.CheckCode = None
        self.AmountWithTax = None
        self.AmountWithoutTax = None
        self.TaxAmount = None
        self.IsRedWashed = None
        self.PdfUrl = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.OrderSn = params.get("OrderSn")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.TicketDate = params.get("TicketDate")
        self.TicketSn = params.get("TicketSn")
        self.TicketCode = params.get("TicketCode")
        self.CheckCode = params.get("CheckCode")
        self.AmountWithTax = params.get("AmountWithTax")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.TaxAmount = params.get("TaxAmount")
        self.IsRedWashed = params.get("IsRedWashed")
        self.PdfUrl = params.get("PdfUrl")
        self.ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceV2Request(AbstractModel):
    """QueryInvoiceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID
0 : 高灯
1 : 票易通
        :type InvoicePlatformId: int
        :param OrderId: 订单号
        :type OrderId: str
        :param IsRed: 发票种类：
0：蓝票
1：红票【该字段默认为0， 如果需要查询红票信息，本字段必须传1，否则可能查询不到需要的发票信息】。
        :type IsRed: int
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        :param InvoiceChannel: 开票渠道。0：线上渠道，1：线下渠道。不填默认为线上渠道
        :type InvoiceChannel: int
        :param SellerTaxpayerNum: 当渠道为线下渠道时，必填
        :type SellerTaxpayerNum: str
        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.IsRed = None
        self.Profile = None
        self.InvoiceChannel = None
        self.SellerTaxpayerNum = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.IsRed = params.get("IsRed")
        self.Profile = params.get("Profile")
        self.InvoiceChannel = params.get("InvoiceChannel")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInvoiceV2Response(AbstractModel):
    """QueryInvoiceV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 发票查询结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResultData`
        :param ErrCode: 错误码
        :type ErrCode: str
        :param ErrMessage: 错误消息
        :type ErrMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.ErrCode = None
        self.ErrMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryInvoiceResultData()
            self.Result._deserialize(params.get("Result"))
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.RequestId = params.get("RequestId")


class QueryItem(AbstractModel):
    """聚鑫商户余额查询输出项

    """

    def __init__(self):
        r"""
        :param SubAcctNo: 子商户账户
        :type SubAcctNo: str
        :param SubAcctProperty: 子账户属性 
1：普通会员子账号 
2：挂账子账号 
3：手续费子账号 
4：利息子账号
5：平台担保子账号
        :type SubAcctProperty: str
        :param SubMchId: 业务平台的子商户Id，唯一
        :type SubMchId: str
        :param SubAcctName: 子账户名称
        :type SubAcctName: str
        :param AcctAvailBal: 账户可用余额
        :type AcctAvailBal: str
        :param CashAmt: 可提现金额
        :type CashAmt: str
        :param MaintenanceDate: 维护日期 开户日期或修改日期
        :type MaintenanceDate: str
        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.SubMchId = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.SubMchId = params.get("SubMchId")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMaliciousRegistrationRequest(AbstractModel):
    """QueryMaliciousRegistration请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户ID，调用方使用的商户号信息，与商户主体一一对应
        :type MerchantId: str
        :param MerchantName: 商户名称
        :type MerchantName: str
        :param CompanyName: 企业工商注册标准名称
        :type CompanyName: str
        :param RegAddress: 注册地址
        :type RegAddress: str
        :param RegTime: 商户进件Unix时间，单位秒（非企业注册工商时间)
        :type RegTime: int
        :param USCI: 统一社会信用代码
        :type USCI: str
        :param RegNumber: 工商注册码，匹配优先级为Usci>RegNumber>CompanyName
        :type RegNumber: str
        :param EncryptedPhoneNumber: 手机号码32位MD5加密结果，全大写，格式为0086-13812345678
        :type EncryptedPhoneNumber: str
        :param EncryptedEmailAddress: 邮箱32位MD5加密结果，全大写
        :type EncryptedEmailAddress: str
        :param EncryptedPersonId: 身份证MD5加密结果，最后一位x大写
        :type EncryptedPersonId: str
        :param Ip: 填写信息设备的IP地址
        :type Ip: str
        :param Channel: 进件渠道号，客户自行编码即可
        :type Channel: str
        """
        self.MerchantId = None
        self.MerchantName = None
        self.CompanyName = None
        self.RegAddress = None
        self.RegTime = None
        self.USCI = None
        self.RegNumber = None
        self.EncryptedPhoneNumber = None
        self.EncryptedEmailAddress = None
        self.EncryptedPersonId = None
        self.Ip = None
        self.Channel = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantName = params.get("MerchantName")
        self.CompanyName = params.get("CompanyName")
        self.RegAddress = params.get("RegAddress")
        self.RegTime = params.get("RegTime")
        self.USCI = params.get("USCI")
        self.RegNumber = params.get("RegNumber")
        self.EncryptedPhoneNumber = params.get("EncryptedPhoneNumber")
        self.EncryptedEmailAddress = params.get("EncryptedEmailAddress")
        self.EncryptedPersonId = params.get("EncryptedPersonId")
        self.Ip = params.get("Ip")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMaliciousRegistrationResponse(AbstractModel):
    """QueryMaliciousRegistration返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码
        :type ErrCode: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param Result: 商户风险信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.MerchantRiskInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMsg = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("Result") is not None:
            self.Result = MerchantRiskInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryMemberBindRequest(AbstractModel):
    """QueryMemberBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查询标志（1: 全部会员; 2: 单个会员; 3: 单个会员的证件信息）
        :type QueryFlag: str
        :param PageNum: STRING (10)，页码（起始值为1，每次最多返回20条记录，第二页返回的记录数为第21至40条记录，第三页为41至60条记录，顺序均按照建立时间的先后）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，见证子账户的账号（若SelectFlag为2或3时，子账户账号必输）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemberBindResponse(AbstractModel):
    """QueryMemberBind返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResultNum: STRING (10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始记录号
注意：此字段可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，结束标志（0: 否; 1: 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合业务查询条件的记录总数（重复次数，一次最多返回20条记录）
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TranItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TranItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class QueryMemberTransactionDetailsRequest(AbstractModel):
    """QueryMemberTransactionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param QueryDateType: 查询的交易发生时间类型。
__1__：当日
__2__：历史
        :type QueryDateType: str
        :param QueryTranType: 查询的交易类型。
__1__：全部
__2__：转出
__3__：转入
        :type QueryTranType: str
        :param BankAccountNumber: 父账户账号。
_平安渠道为资金汇总账号_
        :type BankAccountNumber: str
        :param SubAccountNumber: 子账户账号。
_平安渠道为见证子账户的账号_
        :type SubAccountNumber: str
        :param PageOffSet: 分页号, 起始值为1。
        :type PageOffSet: str
        :param QueryStartDate: 查询开始日期，格式：yyyyMMdd。
__若是历史查询，则必输，当日查询时，不起作用；开始日期不能超过当前日期__
        :type QueryStartDate: str
        :param QueryEndDate: 查询终止日期，格式：yyyyMMdd。
__若是历史查询，则必输，当日查询时，不起作用；终止日期不能超过当前日期__
        :type QueryEndDate: str
        :param MidasEnvironment: 环境名。
__release__: 现网环境
__sandbox__: 沙箱环境
__development__: 开发环境
_缺省: release_
        :type MidasEnvironment: str
        """
        self.QueryDateType = None
        self.QueryTranType = None
        self.BankAccountNumber = None
        self.SubAccountNumber = None
        self.PageOffSet = None
        self.QueryStartDate = None
        self.QueryEndDate = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.QueryDateType = params.get("QueryDateType")
        self.QueryTranType = params.get("QueryTranType")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.SubAccountNumber = params.get("SubAccountNumber")
        self.PageOffSet = params.get("PageOffSet")
        self.QueryStartDate = params.get("QueryStartDate")
        self.QueryEndDate = params.get("QueryEndDate")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemberTransactionDetailsResponse(AbstractModel):
    """QueryMemberTransactionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryMemberTransactionDetailsResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryMemberTransactionDetailsResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryMemberTransactionDetailsResult(AbstractModel):
    """聚鑫-查询会员间交易信息列表结果

    """

    def __init__(self):
        r"""
        :param ResultCount: 本次交易返回查询结果记录数。
        :type ResultCount: int
        :param TotalCount: 符合业务查询条件的记录总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param EndFlag: 结束标志。
__0__：否
__1__：是
注意：此字段可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TranItemArray: 会员间交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of MemberTransactionItem
        """
        self.ResultCount = None
        self.TotalCount = None
        self.EndFlag = None
        self.TranItemArray = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.TotalCount = params.get("TotalCount")
        self.EndFlag = params.get("EndFlag")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = MemberTransactionItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemberTransactionRequest(AbstractModel):
    """QueryMemberTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 下单预支付; 2: 确认并付款; 3: 退款; 6: 直接支付T+1; 9: 直接支付T+0）
        :type FunctionFlag: str
        :param OutSubAcctNo: STRING(50)，转出方的见证子账户的账号（付款方）
        :type OutSubAcctNo: str
        :param OutMemberCode: STRING(32)，转出方的交易网会员代码
        :type OutMemberCode: str
        :param OutSubAcctName: STRING(150)，转出方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）
        :type OutSubAcctName: str
        :param InSubAcctNo: STRING(50)，转入方的见证子账户的账号（收款方）
        :type InSubAcctNo: str
        :param InMemberCode: STRING(32)，转入方的交易网会员代码
        :type InMemberCode: str
        :param InSubAcctName: STRING(150)，转入方的见证子账户的户名（户名是绑卡时上送的账户名称，如果未绑卡，就送OpenCustAcctId接口上送的用户昵称UserNickname）
        :type InSubAcctName: str
        :param TranAmt: STRING(20)，交易金额
        :type TranAmt: str
        :param TranFee: STRING(20)，交易费用（平台收取交易费用）
        :type TranFee: str
        :param TranType: STRING(20)，交易类型（01: 普通交易）
        :type TranType: str
        :param Ccy: STRING(3)，币种（默认: RMB）
        :type Ccy: str
        :param OrderNo: STRING(50)，订单号（功能标志为1,2,3时必输）
        :type OrderNo: str
        :param OrderContent: STRING(500)，订单内容
        :type OrderContent: str
        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域（若需短信验证码则此项必输短信指令号）
        :type ReservedMsg: str
        :param WebSign: STRING(300)，网银签名（若需短信验证码则此项必输）
        :type WebSign: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.OutSubAcctNo = None
        self.OutMemberCode = None
        self.OutSubAcctName = None
        self.InSubAcctNo = None
        self.InMemberCode = None
        self.InSubAcctName = None
        self.TranAmt = None
        self.TranFee = None
        self.TranType = None
        self.Ccy = None
        self.OrderNo = None
        self.OrderContent = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.OutMemberCode = params.get("OutMemberCode")
        self.OutSubAcctName = params.get("OutSubAcctName")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.InMemberCode = params.get("InMemberCode")
        self.InSubAcctName = params.get("InSubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.TranFee = params.get("TranFee")
        self.TranType = params.get("TranType")
        self.Ccy = params.get("Ccy")
        self.OrderNo = params.get("OrderNo")
        self.OrderContent = params.get("OrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMemberTransactionResponse(AbstractModel):
    """QueryMemberTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryMerchantBalanceData(AbstractModel):
    """对接账户余额查询数据

    """

    def __init__(self):
        r"""
        :param Currency: 余额币种
        :type Currency: str
        :param Balance: 账户余额
        :type Balance: str
        :param MerchantId: 商户ID
        :type MerchantId: str
        """
        self.Currency = None
        self.Balance = None
        self.MerchantId = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Balance = params.get("Balance")
        self.MerchantId = params.get("MerchantId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantBalanceRequest(AbstractModel):
    """QueryMerchantBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param Currency: 余额币种
        :type Currency: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.Currency = None
        self.Profile = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantBalanceResponse(AbstractModel):
    """QueryMerchantBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 对接方账户余额查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryMerchantBalanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryMerchantBalanceResult(AbstractModel):
    """对接账户余额查询结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码
        :type Code: str
        :param Data: 对接账户余额查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryMerchantBalanceData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantClassificationRequest(AbstractModel):
    """QueryMerchantClassification请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantClassificationResponse(AbstractModel):
    """QueryMerchantClassification返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 查询商户分类响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of MerchantClassificationId
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = MerchantClassificationId()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class QueryMerchantInfoForManagementRequest(AbstractModel):
    """QueryMerchantInfoForManagement请求参数结构体

    """

    def __init__(self):
        r"""
        :param InvoicePlatformId: 开票平台ID
        :type InvoicePlatformId: int
        :param Offset: 页码
        :type Offset: int
        :param Limit: 页大小
        :type Limit: int
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.Offset = None
        self.Limit = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantInfoForManagementResponse(AbstractModel):
    """QueryMerchantInfoForManagement返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 商户结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.MerchantManagementResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = MerchantManagementResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryMerchantOrderRequest(AbstractModel):
    """QueryMerchantOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 进件成功后返给商户方的AppId。
        :type MerchantAppId: str
        :param OrderNo: 平台流水号。平台唯一订单号。
        :type OrderNo: str
        """
        self.MerchantAppId = None
        self.OrderNo = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantOrderResponse(AbstractModel):
    """QueryMerchantOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 进件成功后返给商户方的AppId。
        :type MerchantAppId: str
        :param OrderNo: 平台流水号。平台唯一订单号。
        :type OrderNo: str
        :param Status: 订单支付状态。0-下单失败 1-下单成功未支付 2-支付成功 3-支付失败 4-退款中 5-退款成功 6-退款失败 7-待付款 8-待确认。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantAppId = None
        self.OrderNo = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class QueryMerchantPayWayListRequest(AbstractModel):
    """QueryMerchantPayWayList请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param PayType: 支付类型，逗号分隔。1-现金，2-主扫，3-被扫，4-JSAPI。
        :type PayType: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.PayType = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.PayType = params.get("PayType")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantPayWayListResponse(AbstractModel):
    """QueryMerchantPayWayList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，0表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 查询商户支付方式列表结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of MerchantPayWayData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = MerchantPayWayData()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class QueryMerchantRequest(AbstractModel):
    """QueryMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 进件成功后返给商户方的 AppId
        :type MerchantAppId: str
        """
        self.MerchantAppId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryMerchantResponse(AbstractModel):
    """QueryMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 分配给商户的 AppId，该 AppId 为后续各项 交易的商户标识。
        :type MerchantAppId: str
        :param MerchantName: 收款商户名称。
        :type MerchantName: str
        :param BusinessPayFlag: B2B 支付标志。是否开通 B2B 支付， 1:开通 0:不开通。
        :type BusinessPayFlag: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantAppId = None
        self.MerchantName = None
        self.BusinessPayFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.MerchantName = params.get("MerchantName")
        self.BusinessPayFlag = params.get("BusinessPayFlag")
        self.RequestId = params.get("RequestId")


class QueryOpenBankBankAccountBalanceRequest(AbstractModel):
    """QueryOpenBankBankAccountBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 云企付渠道商户号。外部接入平台入驻云企付平台后下发。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 云企付渠道子商户号。入驻在渠道商户下的子商户ID，如付款方的商户ID，对应创建支付订单中接口参数中的PayerInfo中的payerId。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式，如
__EBANK_PAYMENT__:ebank付款
__OPENBANK_PAYMENT__: openbank付款
        :type PaymentMethod: str
        :param BindSerialNo: 绑卡序列号，银行账户唯一ID，区分多卡或多账户的场景
        :type BindSerialNo: str
        :param Environment: 环境类型
release:生产环境
sandbox:沙箱环境
缺省默认为生产环境
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.BindSerialNo = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.BindSerialNo = params.get("BindSerialNo")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBankAccountBalanceResponse(AbstractModel):
    """QueryOpenBankBankAccountBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 账户余额查询响应对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBankAccountBalanceResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankBankAccountBalanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankBankAccountBalanceResult(AbstractModel):
    """云企付-查询账户余额

    """

    def __init__(self):
        r"""
        :param TotalBalance: 总余额，单位分
        :type TotalBalance: str
        :param YesterdayBalance: 昨日余额，单位分
        :type YesterdayBalance: str
        """
        self.TotalBalance = None
        self.YesterdayBalance = None


    def _deserialize(self, params):
        self.TotalBalance = params.get("TotalBalance")
        self.YesterdayBalance = params.get("YesterdayBalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBankBranchListRequest(AbstractModel):
    """QueryOpenBankBankBranchList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。
__EBANK_PAYMENT__:ebank付款
__OPENBANK_PAYMENT__: openbank付款
        :type PaymentMethod: str
        :param BankBranchName: 支行名称。
        :type BankBranchName: str
        :param BankAbbreviation: 银行简称。
        :type BankAbbreviation: str
        :param PageNumber: 页码。Index和Count必须大于等于1。
        :type PageNumber: :class:`tencentcloud.cpdp.v20190820.models.Paging`
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.BankBranchName = None
        self.BankAbbreviation = None
        self.PageNumber = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.BankBranchName = params.get("BankBranchName")
        self.BankAbbreviation = params.get("BankAbbreviation")
        if params.get("PageNumber") is not None:
            self.PageNumber = Paging()
            self.PageNumber._deserialize(params.get("PageNumber"))
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBankBranchListResponse(AbstractModel):
    """QueryOpenBankBankBranchList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBankBranchListResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankBankBranchListResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankBankBranchListResult(AbstractModel):
    """查询联行号返回结果

    """

    def __init__(self):
        r"""
        :param BankBranchList: 支行列表。
        :type BankBranchList: list of BankBranchInfo
        :param Count: 列表总数。
        :type Count: int
        """
        self.BankBranchList = None
        self.Count = None


    def _deserialize(self, params):
        if params.get("BankBranchList") is not None:
            self.BankBranchList = []
            for item in params.get("BankBranchList"):
                obj = BankBranchInfo()
                obj._deserialize(item)
                self.BankBranchList.append(obj)
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBillData(AbstractModel):
    """云企付-分页查询对账单数据结果

    """

    def __init__(self):
        r"""
        :param BillDate: 交易日期
        :type BillDate: str
        :param Channel: 渠道编码
        :type Channel: str
        :param SubChannel: 二级渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type SubChannel: str
        :param ParentMerchantId: 系统父商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentMerchantId: str
        :param OutMerchantId: 外部商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutMerchantId: str
        :param MerchantId: 系统商户号
        :type MerchantId: str
        :param EndMerchantId: 第三方商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type EndMerchantId: str
        :param OutTradeNo: 外部订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutTradeNo: str
        :param TradeNo: 系统订单号
        :type TradeNo: str
        :param EndTradeNo: 第三方订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTradeNo: str
        :param PaymentType: 收付类型，PAYMENT:付款，INCOME:收款
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentType: str
        :param BusinessType: 业务类型，WITHDRAW:提现，PAY:支付，RECHARGE:充值，TRANSFER:转账，REFUND:退款
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessType: str
        :param TradeTime: 发起交易时间，格式yyyy-MM-dd HH:mm:ss
        :type TradeTime: str
        :param FinishTime: 交易完成时间，格式yyyy-MM-dd HH:mm:ss
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        :param TradeStatus: 交易状态，0:未知，1:成功，2:失败
        :type TradeStatus: str
        :param CheckStatus: 对账状态，1:成功，2:失败 3:长账 4:短账
        :type CheckStatus: str
        :param CheckFailReason: 对账失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckFailReason: str
        :param OrderAmount: 交易金额（元）
        :type OrderAmount: str
        :param ServiceFee: 服务费（元）
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceFee: str
        :param PayeeAccount: 收款人账号
注意：此字段可能返回 null，表示取不到有效值。
        :type PayeeAccount: str
        :param PayeeName: 收款人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayeeName: str
        :param PayerAccount: 付款人账号
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerAccount: str
        :param PayerName: 付款人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerName: str
        :param Description: 支付信息描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.BillDate = None
        self.Channel = None
        self.SubChannel = None
        self.ParentMerchantId = None
        self.OutMerchantId = None
        self.MerchantId = None
        self.EndMerchantId = None
        self.OutTradeNo = None
        self.TradeNo = None
        self.EndTradeNo = None
        self.PaymentType = None
        self.BusinessType = None
        self.TradeTime = None
        self.FinishTime = None
        self.TradeStatus = None
        self.CheckStatus = None
        self.CheckFailReason = None
        self.OrderAmount = None
        self.ServiceFee = None
        self.PayeeAccount = None
        self.PayeeName = None
        self.PayerAccount = None
        self.PayerName = None
        self.Description = None


    def _deserialize(self, params):
        self.BillDate = params.get("BillDate")
        self.Channel = params.get("Channel")
        self.SubChannel = params.get("SubChannel")
        self.ParentMerchantId = params.get("ParentMerchantId")
        self.OutMerchantId = params.get("OutMerchantId")
        self.MerchantId = params.get("MerchantId")
        self.EndMerchantId = params.get("EndMerchantId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TradeNo = params.get("TradeNo")
        self.EndTradeNo = params.get("EndTradeNo")
        self.PaymentType = params.get("PaymentType")
        self.BusinessType = params.get("BusinessType")
        self.TradeTime = params.get("TradeTime")
        self.FinishTime = params.get("FinishTime")
        self.TradeStatus = params.get("TradeStatus")
        self.CheckStatus = params.get("CheckStatus")
        self.CheckFailReason = params.get("CheckFailReason")
        self.OrderAmount = params.get("OrderAmount")
        self.ServiceFee = params.get("ServiceFee")
        self.PayeeAccount = params.get("PayeeAccount")
        self.PayeeName = params.get("PayeeName")
        self.PayerAccount = params.get("PayerAccount")
        self.PayerName = params.get("PayerName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBillDataPageRequest(AbstractModel):
    """QueryOpenBankBillDataPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户号，外部接入平台方入驻云企付平台后下发。
EBANK_PAYMENT支付方式下，填写渠道商户号；
SAFT_ISV支付方式下，填写渠道子商户号;
HELIPAY渠道下，填写渠道子商户号。
        :type ChannelMerchantId: str
        :param BillDate: 账单日期,yyyy-MM-dd。
        :type BillDate: str
        :param ChannelName: 渠道名称。详见附录-云企付枚举类说明-ChannelName。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
HELIPAY：合利宝
        :type ChannelName: str
        :param PageNo: 分页页码。
        :type PageNo: int
        :param PageSize: 分页大小，最大1000。
        :type PageSize: int
        :param BillType: 账单类型，默认交易账单。
        :type BillType: str
        :param PaymentMethod: 支付方式。详见附录-云企付枚举类说明-PaymentMethod。
        :type PaymentMethod: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.BillDate = None
        self.ChannelName = None
        self.PageNo = None
        self.PageSize = None
        self.BillType = None
        self.PaymentMethod = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.BillDate = params.get("BillDate")
        self.ChannelName = params.get("ChannelName")
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.BillType = params.get("BillType")
        self.PaymentMethod = params.get("PaymentMethod")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBillDataPageResponse(AbstractModel):
    """QueryOpenBankBillDataPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBillDataPageResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankBillDataPageResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankBillDataPageResult(AbstractModel):
    """云企付-分页查询对账单数据结果

    """

    def __init__(self):
        r"""
        :param PageNo: 页码
        :type PageNo: int
        :param PageSize: 分页大小
        :type PageSize: int
        :param Count: 总数
        :type Count: int
        :param DataList: 账单数据明细
注意：此字段可能返回 null，表示取不到有效值。
        :type DataList: list of QueryOpenBankBillData
        """
        self.PageNo = None
        self.PageSize = None
        self.Count = None
        self.DataList = None


    def _deserialize(self, params):
        self.PageNo = params.get("PageNo")
        self.PageSize = params.get("PageSize")
        self.Count = params.get("Count")
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = QueryOpenBankBillData()
                obj._deserialize(item)
                self.DataList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBindExternalSubMerchantBankAccountRequest(AbstractModel):
    """QueryOpenBankBindExternalSubMerchantBankAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelApplyId: 渠道申请编号，与外部申请编号二者选填其一。
        :type ChannelApplyId: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        :param OutApplyId: 外部申请编号，与渠道申请编号二者选填其一。
        :type OutApplyId: str
        """
        self.ChannelSubMerchantId = None
        self.ChannelMerchantId = None
        self.ChannelApplyId = None
        self.Environment = None
        self.OutApplyId = None


    def _deserialize(self, params):
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.Environment = params.get("Environment")
        self.OutApplyId = params.get("OutApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankBindExternalSubMerchantBankAccountResponse(AbstractModel):
    """QueryOpenBankBindExternalSubMerchantBankAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankBindExternalSubMerchantBankAccountResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankBindExternalSubMerchantBankAccountResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankBindExternalSubMerchantBankAccountResult(AbstractModel):
    """子商户银行卡绑定结果查询返回结果

    """

    def __init__(self):
        r"""
        :param ExternalSubMerchantBankAccountReturnData: 渠道子商户收款方银行卡信息, 为JSON格式字符串（绑定成功状态下返回）。详情见附录-复杂类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalSubMerchantBankAccountReturnData: str
        :param ChannelApplyId: 渠道申请编号。
        :type ChannelApplyId: str
        :param BindStatus: 绑定状态。
__SUCCESS__: 绑定成功
__FAILED__: 绑定失败
__PROCESSING__: 绑定中
        :type BindStatus: str
        :param BindMessage: 绑定返回描述, 例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindMessage: str
        :param BindSerialNo: 绑卡序列号。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindSerialNo: str
        """
        self.ExternalSubMerchantBankAccountReturnData = None
        self.ChannelApplyId = None
        self.BindStatus = None
        self.BindMessage = None
        self.BindSerialNo = None


    def _deserialize(self, params):
        self.ExternalSubMerchantBankAccountReturnData = params.get("ExternalSubMerchantBankAccountReturnData")
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.BindStatus = params.get("BindStatus")
        self.BindMessage = params.get("BindMessage")
        self.BindSerialNo = params.get("BindSerialNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankDailyReceiptDownloadUrlRequest(AbstractModel):
    """QueryOpenBankDailyReceiptDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 云企付渠道商户号。外部接入平台入驻云企付平台后下发。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 云企付渠道子商户号。入驻在渠道商户下的子商户ID，如付款方的商户ID，对应创建支付订单中接口参数中的PayerInfo中的payerId。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 付款方式。如
__EBANK_PAYMENT__:ebank付款
__OPENBANK_PAYMENT__: openbank付款
        :type PaymentMethod: str
        :param BindSerialNo: 绑卡序列号，银行卡唯一标记，资金账户ID，用于区分商户绑定多卡或多账户场景
        :type BindSerialNo: str
        :param QueryDate: 查询日期，D日查询D-1日的回单文件
        :type QueryDate: str
        :param Environment: 环境类型
release:生产环境
sandbox:沙箱环境
缺省默认为生产环境
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.BindSerialNo = None
        self.QueryDate = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.BindSerialNo = params.get("BindSerialNo")
        self.QueryDate = params.get("QueryDate")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankDailyReceiptDownloadUrlResponse(AbstractModel):
    """QueryOpenBankDailyReceiptDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 按日期查询回单下载地址响应对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankDailyReceiptDownloadUrlResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankDailyReceiptDownloadUrlResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankDailyReceiptDownloadUrlResult(AbstractModel):
    """云企付-按日期查询回单下载地址

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 回单文件下载链接
        :type DownloadUrl: str
        :param ExpireTime: 过期时间
        :type ExpireTime: str
        :param ReceiptStatus: 回单状态
PENDING: 处理中
READY: 可以下载
        :type ReceiptStatus: str
        """
        self.DownloadUrl = None
        self.ExpireTime = None
        self.ReceiptStatus = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.ExpireTime = params.get("ExpireTime")
        self.ReceiptStatus = params.get("ReceiptStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankDownLoadUrlRequest(AbstractModel):
    """QueryOpenBankDownLoadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户号，外部接入平台方入驻云企付平台后下发。
EBANK_PAYMENT支付方式下，填写渠道商户号；
SAFT_ISV支付方式下，填写渠道子商户号。
        :type ChannelMerchantId: str
        :param BillDate: 账单日期,yyyy-MM-dd。
        :type BillDate: str
        :param BillType: 账单类型，默认交易账单。
        :type BillType: str
        :param Environment: 接入环境。沙箱环境填 sandbox。缺省默认调用生产环境。
        :type Environment: str
        :param ChannelName: 渠道名称。不填默认为商企付。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。不填默认为ebank支付。
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
__SAFT_ISV__: 人资ISV支付
        :type PaymentMethod: str
        """
        self.ChannelMerchantId = None
        self.BillDate = None
        self.BillType = None
        self.Environment = None
        self.ChannelName = None
        self.PaymentMethod = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.BillDate = params.get("BillDate")
        self.BillType = params.get("BillType")
        self.Environment = params.get("Environment")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankDownLoadUrlResponse(AbstractModel):
    """QueryOpenBankDownLoadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息。
        :type ErrMessage: str
        :param Result: 查询对账文件下载响应对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankDownLoadUrlResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankDownLoadUrlResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankDownLoadUrlResult(AbstractModel):
    """云企付-查询对账单文件下载url

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 供下一步请求账单文件的下载地址。
        :type DownloadUrl: str
        :param HashValue: 从 download_url 下载的文件的哈希值，用于校验文件的完整性。
        :type HashValue: str
        :param HashType: 从 download_url 下载的文件的哈希类型，用于校验文件的完整性。
        :type HashType: str
        """
        self.DownloadUrl = None
        self.HashValue = None
        self.HashType = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.HashValue = params.get("HashValue")
        self.HashType = params.get("HashType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankExternalSubAccountBookBalanceRequest(AbstractModel):
    """QueryOpenBankExternalSubAccountBookBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。目前只支持支付宝
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。目前只支持安心发支付
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
__SAFT_ISV__: 安心发支付
        :type PaymentMethod: str
        :param OutAccountBookId: 外部账本号ID。与ChannelAccountBookId二者选填其一。
        :type OutAccountBookId: str
        :param ChannelAccountBookId: 渠道账本号ID。与OutAccountBookId二者选填其一。
        :type ChannelAccountBookId: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.OutAccountBookId = None
        self.ChannelAccountBookId = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.OutAccountBookId = params.get("OutAccountBookId")
        self.ChannelAccountBookId = params.get("ChannelAccountBookId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankExternalSubAccountBookBalanceResponse(AbstractModel):
    """QueryOpenBankExternalSubAccountBookBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryExternalAccountBookResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryExternalAccountBookResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankExternalSubMerchantBankAccountData(AbstractModel):
    """第三方子商户银行卡列表查询返回数据

    """

    def __init__(self):
        r"""
        :param AccountBank: 开户银行。
        :type AccountBank: str
        :param BindSerialNo: 绑卡序列号。
        :type BindSerialNo: str
        :param AccountType: 账号类型。
__COLLECT_MONEY__: 收款卡
__PAYMENT__: 付款卡
        :type AccountType: str
        :param BankBranchId: 支行号。
注意：此字段可能返回 null，表示取不到有效值。
        :type BankBranchId: str
        :param AccountNumberLastFour: 银行卡卡后四位。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountNumberLastFour: str
        """
        self.AccountBank = None
        self.BindSerialNo = None
        self.AccountType = None
        self.BankBranchId = None
        self.AccountNumberLastFour = None


    def _deserialize(self, params):
        self.AccountBank = params.get("AccountBank")
        self.BindSerialNo = params.get("BindSerialNo")
        self.AccountType = params.get("AccountType")
        self.BankBranchId = params.get("BankBranchId")
        self.AccountNumberLastFour = params.get("AccountNumberLastFour")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankExternalSubMerchantBankAccountRequest(AbstractModel):
    """QueryOpenBankExternalSubMerchantBankAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
        :type PaymentMethod: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankExternalSubMerchantBankAccountResponse(AbstractModel):
    """QueryOpenBankExternalSubMerchantBankAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubMerchantBankAccountResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankExternalSubMerchantBankAccountResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankExternalSubMerchantBankAccountResult(AbstractModel):
    """第三方子商户银行卡列表查询返回结果

    """

    def __init__(self):
        r"""
        :param AccountList: 第三方渠道子商户查询银行账户返回。
        :type AccountList: list of QueryOpenBankExternalSubMerchantBankAccountData
        """
        self.AccountList = None


    def _deserialize(self, params):
        if params.get("AccountList") is not None:
            self.AccountList = []
            for item in params.get("AccountList"):
                obj = QueryOpenBankExternalSubMerchantBankAccountData()
                obj._deserialize(item)
                self.AccountList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankExternalSubMerchantRegistrationRequest(AbstractModel):
    """QueryOpenBankExternalSubMerchantRegistration请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户号。
        :type ChannelMerchantId: str
        :param ChannelRegistrationNo: 渠道进件号，与外部进件号二者选填其一。
        :type ChannelRegistrationNo: str
        :param OutRegistrationNo: 外部进件号，与渠道进件号二者选填其一。
        :type OutRegistrationNo: str
        :param Environment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelRegistrationNo = None
        self.OutRegistrationNo = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelRegistrationNo = params.get("ChannelRegistrationNo")
        self.OutRegistrationNo = params.get("OutRegistrationNo")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankExternalSubMerchantRegistrationResponse(AbstractModel):
    """QueryOpenBankExternalSubMerchantRegistration返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankExternalSubMerchantRegistrationResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankExternalSubMerchantRegistrationResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankExternalSubMerchantRegistrationResult(AbstractModel):
    """第三方子商户进件结果查询返回结果

    """

    def __init__(self):
        r"""
        :param RegistrationStatus: 进件状态。
__SUCCESS__: 进件成功
__FAILED__: 进件失败
__PROCESSING__: 进件中
        :type RegistrationStatus: str
        :param RegistrationMessage: 进件返回描述, 例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistrationMessage: str
        :param ChannelRegistrationNo: 渠道进件号。
        :type ChannelRegistrationNo: str
        :param ChannelSubMerchantId: 渠道子商户ID（进件成功返回）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelSubMerchantId: str
        :param OutSubMerchantName: 外部子商户名称（进件成功返回）。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSubMerchantName: str
        :param ChannelName: 渠道名称（进件成功返回）。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param PaymentMethod: 支付方式（进件成功返回）。
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentMethod: str
        :param BusinessLicenseNumber: 社会信用代码。
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessLicenseNumber: str
        :param LegalName: 法人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type LegalName: str
        :param ExternalReturnData: 第三方渠道查询进件返回数据。详情见附录-复杂类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnData: str
        """
        self.RegistrationStatus = None
        self.RegistrationMessage = None
        self.ChannelRegistrationNo = None
        self.ChannelSubMerchantId = None
        self.OutSubMerchantName = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.BusinessLicenseNumber = None
        self.LegalName = None
        self.ExternalReturnData = None


    def _deserialize(self, params):
        self.RegistrationStatus = params.get("RegistrationStatus")
        self.RegistrationMessage = params.get("RegistrationMessage")
        self.ChannelRegistrationNo = params.get("ChannelRegistrationNo")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.OutSubMerchantName = params.get("OutSubMerchantName")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.BusinessLicenseNumber = params.get("BusinessLicenseNumber")
        self.LegalName = params.get("LegalName")
        self.ExternalReturnData = params.get("ExternalReturnData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankOrderDetailReceiptInfoRequest(AbstractModel):
    """QueryOpenBankOrderDetailReceiptInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称，目前只支持ALIPAY
        :type ChannelName: str
        :param PaymentMethod: 支付方式，目前只支持SAFT_ISV
        :type PaymentMethod: str
        :param OutApplyId: 外部回单申请ID，与渠道回单申请ID二者选填其一
        :type OutApplyId: str
        :param ChannelApplyId: 渠道回单申请ID，与外部回单申请ID二者选填其一
        :type ChannelApplyId: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.OutApplyId = None
        self.ChannelApplyId = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.OutApplyId = params.get("OutApplyId")
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankOrderDetailReceiptInfoResponse(AbstractModel):
    """QueryOpenBankOrderDetailReceiptInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
        :type ErrCode: str
        :param ErrMessage: 错误消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankOrderDetailReceiptInfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankOrderDetailReceiptInfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankOrderDetailReceiptInfoResult(AbstractModel):
    """单笔交易回单申请结果查询

    """

    def __init__(self):
        r"""
        :param ChannelApplyId: 渠道回单申请ID
        :type ChannelApplyId: str
        :param ReceiptStatus: 申请状态。
SUCCESS：申请成功；
FAILED：申请失败；
PROCESSING：申请中。
注意：若返回申请中，需要再次调用回单申请结果查询接口，查询结果。
        :type ReceiptStatus: str
        :param ReceiptMessage: 申请返回描述，例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiptMessage: str
        :param DownloadUrl: 回单下载链接，申请成功时返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param ExpireTime: 过期时间，yyyy-MM-dd HH:mm:ss格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        """
        self.ChannelApplyId = None
        self.ReceiptStatus = None
        self.ReceiptMessage = None
        self.DownloadUrl = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.ReceiptStatus = params.get("ReceiptStatus")
        self.ReceiptMessage = params.get("ReceiptMessage")
        self.DownloadUrl = params.get("DownloadUrl")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankPaymentOrderRequest(AbstractModel):
    """QueryOpenBankPaymentOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户号。外部接入平台入驻云企付平台下发。
        :type ChannelMerchantId: str
        :param OutOrderId: 外部商户订单号。与ChannelOrderId不能同时为空。
        :type OutOrderId: str
        :param ChannelOrderId: 云平台订单号。与OutOrderId不能同时为空。
        :type ChannelOrderId: str
        :param Environment: 接入环境。沙箱环境填 sandbox。缺省默认调用生产环境。
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.OutOrderId = None
        self.ChannelOrderId = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutOrderId = params.get("OutOrderId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankPaymentOrderResponse(AbstractModel):
    """QueryOpenBankPaymentOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，SUCCESS表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息。
        :type ErrMessage: str
        :param Result: 查询支付结果响应对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankPaymentOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankPaymentOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankPaymentOrderResult(AbstractModel):
    """云企付-查询订单支付结果

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户号。外部接入平台入驻云企付平台下发
        :type ChannelMerchantId: str
        :param OutOrderId: 外部商户订单号
        :type OutOrderId: str
        :param ChannelOrderId: 云企付平台订单号
        :type ChannelOrderId: str
        :param ThirdPayOrderId: 第三方支付平台订单号
        :type ThirdPayOrderId: str
        :param OrderStatus: 订单状态。
INIT：初始化
PAYING：支付中
ACCEPTED：支付受理成功
SUCCESS：支付成功
CLOSED：关单
PAY_FAIL：支付失败
REVOKE：退票
        :type OrderStatus: str
        :param ChannelName: 支付渠道名称，如TENPAY
        :type ChannelName: str
        :param PaymentMethod: 付款方式。如EBANK_PAYMENT
OPENBANK_PAYMENT
        :type PaymentMethod: str
        :param TotalAmount: 订单金额。单位分
        :type TotalAmount: int
        :param PayAmount: 实际支付金额。单位分，支付成功时返回
        :type PayAmount: int
        :param FailReason: 失败原因，若失败的返回
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param Attachment: 附加信息，查询时原样透传
注意：此字段可能返回 null，表示取不到有效值。
        :type Attachment: str
        :param RedirectInfo: 重定向参数，用于客户端跳转，订单未支付时返回该参数
渠道为TENPAY，付款方式为EBANK_PAYMENT时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankRedirectInfo`
        :param ExternalReturnData: 第三方渠道返回信息，见渠道特殊说明,详情见附录-复杂类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnData: str
        :param BankApprovalGuideInfo: 银行复核指引。当TENPAY下OPENBANT_PAYMENT时，下单受理成功是返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type BankApprovalGuideInfo: :class:`tencentcloud.cpdp.v20190820.models.OpenBankApprovalGuideInfo`
        :param FeeAmount: 手续费金额
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeAmount: int
        :param FeeRate: 手续费费率
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeRate: int
        """
        self.ChannelMerchantId = None
        self.OutOrderId = None
        self.ChannelOrderId = None
        self.ThirdPayOrderId = None
        self.OrderStatus = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.TotalAmount = None
        self.PayAmount = None
        self.FailReason = None
        self.Attachment = None
        self.RedirectInfo = None
        self.ExternalReturnData = None
        self.BankApprovalGuideInfo = None
        self.FeeAmount = None
        self.FeeRate = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutOrderId = params.get("OutOrderId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.ThirdPayOrderId = params.get("ThirdPayOrderId")
        self.OrderStatus = params.get("OrderStatus")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.TotalAmount = params.get("TotalAmount")
        self.PayAmount = params.get("PayAmount")
        self.FailReason = params.get("FailReason")
        self.Attachment = params.get("Attachment")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = OpenBankRedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        self.ExternalReturnData = params.get("ExternalReturnData")
        if params.get("BankApprovalGuideInfo") is not None:
            self.BankApprovalGuideInfo = OpenBankApprovalGuideInfo()
            self.BankApprovalGuideInfo._deserialize(params.get("BankApprovalGuideInfo"))
        self.FeeAmount = params.get("FeeAmount")
        self.FeeRate = params.get("FeeRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankRefundOrderRequest(AbstractModel):
    """QueryOpenBankRefundOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户号。
        :type ChannelMerchantId: str
        :param OutRefundId: 外部商户退单号，与渠道退款单号二者选填其一。
        :type OutRefundId: str
        :param ChannelRefundId: 渠道退款订单号，与外部商户退款单号二者选填其一。
        :type ChannelRefundId: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.OutRefundId = None
        self.ChannelRefundId = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutRefundId = params.get("OutRefundId")
        self.ChannelRefundId = params.get("ChannelRefundId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankRefundOrderResponse(AbstractModel):
    """QueryOpenBankRefundOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码
        :type ErrCode: str
        :param ErrMessage: 错误消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.OpenBankQueryRefundOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = OpenBankQueryRefundOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankSubMerchantCredentialRequest(AbstractModel):
    """QueryOpenBankSubMerchantCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。详见附录-枚举类型-ChannelName。
        :type ChannelName: str
        :param PaymentMethod: 支付方式。
合利宝渠道不需要传。
        :type PaymentMethod: str
        :param OutApplyId: 外部申请流水号。
外部申请流水号与渠道申请流水号两者选填其一。
        :type OutApplyId: str
        :param ChannelApplyId: 渠道申请流水号。
外部申请流水号与渠道申请流水号两者选填其一。
        :type ChannelApplyId: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.OutApplyId = None
        self.ChannelApplyId = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.OutApplyId = params.get("OutApplyId")
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankSubMerchantCredentialResponse(AbstractModel):
    """QueryOpenBankSubMerchantCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantCredentialResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankSubMerchantCredentialResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankSubMerchantCredentialResult(AbstractModel):
    """子商户资质文件查询

    """

    def __init__(self):
        r"""
        :param UploadStatus: 上传状态
        :type UploadStatus: str
        :param UploadMessage: 上传描述
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadMessage: str
        """
        self.UploadStatus = None
        self.UploadMessage = None


    def _deserialize(self, params):
        self.UploadStatus = params.get("UploadStatus")
        self.UploadMessage = params.get("UploadMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankSubMerchantRateConfigureRequest(AbstractModel):
    """QueryOpenBankSubMerchantRateConfigure请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelRegistrationNo: 渠道进件序列号。
        :type ChannelRegistrationNo: str
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。详见附录-云企付枚举类说明-ChannelName。
TENPAY: 商企付
WECHAT: 微信支付
ALIPAY: 支付宝
HELIPAY:合利宝
        :type ChannelName: str
        :param ChannelProductFeeNo: 渠道产品费率序列号。与外部产品费率序列号二者选填其一。
        :type ChannelProductFeeNo: str
        :param OutProductFeeNo: 外部产品费率序列号。与渠道产品费率序列号二者选填其一。
        :type OutProductFeeNo: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelRegistrationNo = None
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.ChannelProductFeeNo = None
        self.OutProductFeeNo = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelRegistrationNo = params.get("ChannelRegistrationNo")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.ChannelProductFeeNo = params.get("ChannelProductFeeNo")
        self.OutProductFeeNo = params.get("OutProductFeeNo")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankSubMerchantRateConfigureResponse(AbstractModel):
    """QueryOpenBankSubMerchantRateConfigure返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSubMerchantRateConfigureResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankSubMerchantRateConfigureResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankSubMerchantRateConfigureResult(AbstractModel):
    """子商户费率配置查询结果

    """

    def __init__(self):
        r"""
        :param DealStatus: 处理状态 
SUCCESS: 开通成功 
FAILED: 开通失败
PROCESSING: 开通中
        :type DealStatus: str
        :param DealMessage: 处理描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DealMessage: str
        """
        self.DealStatus = None
        self.DealMessage = None


    def _deserialize(self, params):
        self.DealStatus = params.get("DealStatus")
        self.DealMessage = params.get("DealMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankSupportBankListRequest(AbstractModel):
    """QueryOpenBankSupportBankList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。
__EBANK_PAYMENT__:ebank付款
__OPENBANK_PAYMENT__: openbank付款
        :type PaymentMethod: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankSupportBankListResponse(AbstractModel):
    """QueryOpenBankSupportBankList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankSupportBankListResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankSupportBankListResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankSupportBankListResult(AbstractModel):
    """查询支持的银行列表返回结果

    """

    def __init__(self):
        r"""
        :param SupportBankList: 支持的银行列表
        :type SupportBankList: list of SupportBankInfo
        """
        self.SupportBankList = None


    def _deserialize(self, params):
        if params.get("SupportBankList") is not None:
            self.SupportBankList = []
            for item in params.get("SupportBankList"):
                obj = SupportBankInfo()
                obj._deserialize(item)
                self.SupportBankList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankUnbindExternalSubMerchantBankAccountRequest(AbstractModel):
    """QueryOpenBankUnbindExternalSubMerchantBankAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelApplyId: 渠道申请编号，与外部申请编号二者选填其一。
        :type ChannelApplyId: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        :param OutApplyId: 外部申请编号，与渠道申请编号二者选填其一。
        :type OutApplyId: str
        """
        self.ChannelSubMerchantId = None
        self.ChannelMerchantId = None
        self.ChannelApplyId = None
        self.Environment = None
        self.OutApplyId = None


    def _deserialize(self, params):
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.Environment = params.get("Environment")
        self.OutApplyId = params.get("OutApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOpenBankUnbindExternalSubMerchantBankAccountResponse(AbstractModel):
    """QueryOpenBankUnbindExternalSubMerchantBankAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOpenBankUnbindExternalSubMerchantBankAccountResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOpenBankUnbindExternalSubMerchantBankAccountResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOpenBankUnbindExternalSubMerchantBankAccountResult(AbstractModel):
    """第三方子商户银行卡解绑结果查询返回结果

    """

    def __init__(self):
        r"""
        :param ChannelApplyId: 渠道申请编号。
        :type ChannelApplyId: str
        :param UnbindStatus: 解绑状态。
__SUCCESS__: 解绑成功
__FAILED__: 解绑失败
__PROCESSING__: 解绑中
        :type UnbindStatus: str
        :param UnbindMessage: 解绑返回描述, 例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnbindMessage: str
        """
        self.ChannelApplyId = None
        self.UnbindStatus = None
        self.UnbindMessage = None


    def _deserialize(self, params):
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.UnbindStatus = params.get("UnbindStatus")
        self.UnbindMessage = params.get("UnbindMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderOutOrderList(AbstractModel):
    """查询订单接口的出参，订单列表

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param Amt: 支付金额，单位：分
        :type Amt: int
        :param UserId: 用户Id
        :type UserId: str
        :param CashAmt: 现金支付金额
        :type CashAmt: str
        :param Metadata: 发货标识，由业务在调用聚鑫下单 接口的时候下发
        :type Metadata: str
        :param PayTime: 支付时间unix时间戳
        :type PayTime: str
        :param CouponAmt: 抵扣券金额
        :type CouponAmt: str
        :param OrderTime: 下单时间unix时间戳
        :type OrderTime: str
        :param ProductId: 物品id
        :type ProductId: str
        :param SceneInfo: 高速场景信息
        :type SceneInfo: str
        :param OrderState: 当前订单的订单状态 
0：初始状态，获取聚鑫交易订单成功；  
1：拉起聚鑫支付页面成功，用户未 支付；
2：用户支付成功，正在发货；
3：用户支付成功，发货失败；
4：用户支付成功，发货成功；
5：聚鑫支付页面正在失效中；
6：聚鑫支付页面已经失效；
        :type OrderState: str
        :param Channel: 支付渠道：wechat：微信支付;
qqwallet：QQ钱包;
bank：网银
        :type Channel: str
        :param RefundFlag: 是否曾退款
        :type RefundFlag: str
        :param OutTradeNo: 务支付订单号
        :type OutTradeNo: str
        :param ProductName: 商品名称
        :type ProductName: str
        :param CallBackTime: 支付回调时间，unix时间戳
        :type CallBackTime: str
        :param CurrencyType: ISO 货币代码，CNY
        :type CurrencyType: str
        :param AcctSubAppId: 微校场景账户Id
        :type AcctSubAppId: str
        :param TransactionId: 调用下单接口获取的聚鑫交易订单
        :type TransactionId: str
        :param ChannelOrderId: 聚鑫内部渠道订单号
        :type ChannelOrderId: str
        :param SubOrderList: 调用下单接口传进来的 SubOutTradeNoList
        :type SubOrderList: list of QueryOrderOutSubOrderList
        :param ChannelExternalOrderId: 支付机构订单号
        :type ChannelExternalOrderId: str
        """
        self.MidasAppId = None
        self.Amt = None
        self.UserId = None
        self.CashAmt = None
        self.Metadata = None
        self.PayTime = None
        self.CouponAmt = None
        self.OrderTime = None
        self.ProductId = None
        self.SceneInfo = None
        self.OrderState = None
        self.Channel = None
        self.RefundFlag = None
        self.OutTradeNo = None
        self.ProductName = None
        self.CallBackTime = None
        self.CurrencyType = None
        self.AcctSubAppId = None
        self.TransactionId = None
        self.ChannelOrderId = None
        self.SubOrderList = None
        self.ChannelExternalOrderId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.Amt = params.get("Amt")
        self.UserId = params.get("UserId")
        self.CashAmt = params.get("CashAmt")
        self.Metadata = params.get("Metadata")
        self.PayTime = params.get("PayTime")
        self.CouponAmt = params.get("CouponAmt")
        self.OrderTime = params.get("OrderTime")
        self.ProductId = params.get("ProductId")
        self.SceneInfo = params.get("SceneInfo")
        self.OrderState = params.get("OrderState")
        self.Channel = params.get("Channel")
        self.RefundFlag = params.get("RefundFlag")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductName = params.get("ProductName")
        self.CallBackTime = params.get("CallBackTime")
        self.CurrencyType = params.get("CurrencyType")
        self.AcctSubAppId = params.get("AcctSubAppId")
        self.TransactionId = params.get("TransactionId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = QueryOrderOutSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.ChannelExternalOrderId = params.get("ChannelExternalOrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderOutSubOrderList(AbstractModel):
    """子订单列表

    """

    def __init__(self):
        r"""
        :param Amt: 子订单支付金额
        :type Amt: int
        :param SubMchIncome: 子订单结算应收金额，单位：分
        :type SubMchIncome: int
        :param Metadata: 发货标识，由业务在调用Midas下单接口的时候下发。
        :type Metadata: str
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param SettleCheck: 核销状态，1表示核销，0表示未核销
        :type SettleCheck: int
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        """
        self.Amt = None
        self.SubMchIncome = None
        self.Metadata = None
        self.OriginalAmt = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SettleCheck = None
        self.SubAppId = None
        self.SubOutTradeNo = None


    def _deserialize(self, params):
        self.Amt = params.get("Amt")
        self.SubMchIncome = params.get("SubMchIncome")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SettleCheck = params.get("SettleCheck")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderRequest(AbstractModel):
    """QueryOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主 MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param Type: type=by_order根据订单号 查订单；
type=by_user根据用户id 查订单 。
        :type Type: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param Count: 每页返回的记录数。根据用户 号码查询订单列表时需要传。 用于分页展示。Type=by_order时必填
        :type Count: int
        :param Offset: 记录数偏移量，默认从0开 始。根据用户号码查询订单列 表时需要传。用于分页展示。Type=by_order时必填
        :type Offset: int
        :param StartTime: 查询开始时间，Unix时间戳。Type=by_order时必填
        :type StartTime: str
        :param EndTime: 查询结束时间，Unix时间戳。Type=by_order时必填
        :type EndTime: str
        :param OutTradeNo: 业务订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫订单号，OutTradeNo与 TransactionId不能同时为 空，都传优先使用 OutTradeNo
        :type TransactionId: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.Type = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Count = None
        self.Offset = None
        self.StartTime = None
        self.EndTime = None
        self.OutTradeNo = None
        self.TransactionId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Type = params.get("Type")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Count = params.get("Count")
        self.Offset = params.get("Offset")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderResponse(AbstractModel):
    """QueryOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalNum: 返回订单数
        :type TotalNum: int
        :param OrderList: 查询结果的订单列表
        :type OrderList: list of QueryOrderOutOrderList
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.OrderList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("OrderList") is not None:
            self.OrderList = []
            for item in params.get("OrderList"):
                obj = QueryOrderOutOrderList()
                obj._deserialize(item)
                self.OrderList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryOrderStatusRequest(AbstractModel):
    """QueryOrderStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param DeveloperNo: 开发者流水号
        :type DeveloperNo: str
        :param OrderNo: 付款订单号
        :type OrderNo: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.DeveloperNo = None
        self.OrderNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.DeveloperNo = params.get("DeveloperNo")
        self.OrderNo = params.get("OrderNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOrderStatusResponse(AbstractModel):
    """QueryOrderStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，0表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 查询订单付款状态结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOrderStatusResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryOrderStatusResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOrderStatusResult(AbstractModel):
    """查询订单付款状态响应对象

    """

    def __init__(self):
        r"""
        :param OrderNo: 付款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param DeveloperNo: 开发者流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type DeveloperNo: str
        :param TradeDiscountAmount: 交易优惠金额（免充值券）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeDiscountAmount: str
        :param PayName: 付款方式名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param OrderMerchantId: 商户流水号（从1开始自增长不重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderMerchantId: str
        :param TradeAccount: 交易帐号（银行卡号、支付宝帐号、微信帐号等，某些收单机构没有此数据）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeAccount: str
        :param TradeAmount: 实际交易金额（以分为单位，没有小数点）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeAmount: str
        :param CurrencySign: 币种签名
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrencySign: str
        :param TradePayTime: 付款完成时间（以收单机构为准）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradePayTime: str
        :param ShopOrderId: 门店流水号（从1开始自增长不重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopOrderId: str
        :param PayTag: 支付标签
注意：此字段可能返回 null，表示取不到有效值。
        :type PayTag: str
        :param Status: 订单状态（1交易成功，2待支付，4已取消，9等待用户输入密码确认
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param OrderCurrency: 币种代码
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderCurrency: str
        :param TradeQrcode: 二维码字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeQrcode: str
        :param TradeTime: 开始交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeTime: str
        :param DiscountAmount: 折扣金额（以分为单位，没有小数点）
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountAmount: str
        :param MerchantNo: 商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        :param Remark: 订单备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param OrderName: 订单标题
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderName: str
        :param OriginalAmount: 原始金额（以分为单位，没有小数点）
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalAmount: str
        :param ShopNo: 门店编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopNo: str
        :param TradeResult: 收单机构原始交易数据，如果返回非标准json数据，请自行转换
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeResult: str
        :param OrderId: 订单流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param OrderType: 订单类型（1消费，2辙单）
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderType: str
        :param TradeNo: 收单机构交易号
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeNo: str
        :param OriginalOrderNo: 原始订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalOrderNo: str
        :param Tag: 订单标记，订单附加数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param AddTime: 下单时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param CashierId: 收银员编号
注意：此字段可能返回 null，表示取不到有效值。
        :type CashierId: str
        :param CashierRealName: 收银员名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CashierRealName: str
        :param ShopFullName: 店铺全称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopFullName: str
        :param ShopName: 店铺名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopName: str
        """
        self.OrderNo = None
        self.DeveloperNo = None
        self.TradeDiscountAmount = None
        self.PayName = None
        self.OrderMerchantId = None
        self.TradeAccount = None
        self.TradeAmount = None
        self.CurrencySign = None
        self.TradePayTime = None
        self.ShopOrderId = None
        self.PayTag = None
        self.Status = None
        self.OrderCurrency = None
        self.TradeQrcode = None
        self.TradeTime = None
        self.DiscountAmount = None
        self.MerchantNo = None
        self.Remark = None
        self.OrderName = None
        self.OriginalAmount = None
        self.ShopNo = None
        self.TradeResult = None
        self.OrderId = None
        self.OrderType = None
        self.TradeNo = None
        self.OriginalOrderNo = None
        self.Tag = None
        self.AddTime = None
        self.CashierId = None
        self.CashierRealName = None
        self.ShopFullName = None
        self.ShopName = None


    def _deserialize(self, params):
        self.OrderNo = params.get("OrderNo")
        self.DeveloperNo = params.get("DeveloperNo")
        self.TradeDiscountAmount = params.get("TradeDiscountAmount")
        self.PayName = params.get("PayName")
        self.OrderMerchantId = params.get("OrderMerchantId")
        self.TradeAccount = params.get("TradeAccount")
        self.TradeAmount = params.get("TradeAmount")
        self.CurrencySign = params.get("CurrencySign")
        self.TradePayTime = params.get("TradePayTime")
        self.ShopOrderId = params.get("ShopOrderId")
        self.PayTag = params.get("PayTag")
        self.Status = params.get("Status")
        self.OrderCurrency = params.get("OrderCurrency")
        self.TradeQrcode = params.get("TradeQrcode")
        self.TradeTime = params.get("TradeTime")
        self.DiscountAmount = params.get("DiscountAmount")
        self.MerchantNo = params.get("MerchantNo")
        self.Remark = params.get("Remark")
        self.OrderName = params.get("OrderName")
        self.OriginalAmount = params.get("OriginalAmount")
        self.ShopNo = params.get("ShopNo")
        self.TradeResult = params.get("TradeResult")
        self.OrderId = params.get("OrderId")
        self.OrderType = params.get("OrderType")
        self.TradeNo = params.get("TradeNo")
        self.OriginalOrderNo = params.get("OriginalOrderNo")
        self.Tag = params.get("Tag")
        self.AddTime = params.get("AddTime")
        self.CashierId = params.get("CashierId")
        self.CashierRealName = params.get("CashierRealName")
        self.ShopFullName = params.get("ShopFullName")
        self.ShopName = params.get("ShopName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOutwardOrderData(AbstractModel):
    """查询汇出数据

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param AcctDate: 财务日期
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctDate: str
        :param PricingCurrency: 定价币种
注意：此字段可能返回 null，表示取不到有效值。
        :type PricingCurrency: str
        :param SourceCurrency: 源币种
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCurrency: str
        :param SourceAmount: 源金额
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceAmount: str
        :param TargetCurrency: 目的币种
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetCurrency: str
        :param TargetAmount: 目的金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetAmount: str
        :param FxRate: 汇率
注意：此字段可能返回 null，表示取不到有效值。
        :type FxRate: str
        :param Status: 指令状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param RefundAmount: 退汇金额
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundAmount: str
        :param RefundCurrency: 退汇币种
注意：此字段可能返回 null，表示取不到有效值。
        :type RefundCurrency: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.AcctDate = None
        self.PricingCurrency = None
        self.SourceCurrency = None
        self.SourceAmount = None
        self.TargetCurrency = None
        self.TargetAmount = None
        self.FxRate = None
        self.Status = None
        self.FailReason = None
        self.RefundAmount = None
        self.RefundCurrency = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.AcctDate = params.get("AcctDate")
        self.PricingCurrency = params.get("PricingCurrency")
        self.SourceCurrency = params.get("SourceCurrency")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TargetAmount = params.get("TargetAmount")
        self.FxRate = params.get("FxRate")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.RefundAmount = params.get("RefundAmount")
        self.RefundCurrency = params.get("RefundCurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOutwardOrderRequest(AbstractModel):
    """QueryOutwardOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param TransactionId: 对接方汇出指令编号
        :type TransactionId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.TransactionId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryOutwardOrderResponse(AbstractModel):
    """QueryOutwardOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 查询汇出结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryOutwardOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOutwardOrderResult(AbstractModel):
    """查询汇出结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码
        :type Code: str
        :param Data: 查询汇出数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryOutwardOrderData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPayerInfoRequest(AbstractModel):
    """QueryPayerInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.PayerId = None
        self.Profile = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPayerInfoResponse(AbstractModel):
    """QueryPayerInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 付款人查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryPayerinfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryPayerinfoData(AbstractModel):
    """付款人查询数据

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 审核状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param PayerType: 付款人类型
        :type PayerType: str
        :param PayerName: 付款人姓名
        :type PayerName: str
        :param PayerIdType: 付款人证件类型
        :type PayerIdType: str
        :param PayerIdNo: 付款人证件号
        :type PayerIdNo: str
        :param PayerContactNumber: 付款人联系电话
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerContactNumber: str
        :param PayerEmailAddress: 付款人联系邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerEmailAddress: str
        :param PayerCountryCode: 付款人常驻国家或地区编码
        :type PayerCountryCode: str
        :param PayerContactName: 付款人联系名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayerContactName: str
        """
        self.MerchantId = None
        self.PayerId = None
        self.Status = None
        self.FailReason = None
        self.PayerType = None
        self.PayerName = None
        self.PayerIdType = None
        self.PayerIdNo = None
        self.PayerContactNumber = None
        self.PayerEmailAddress = None
        self.PayerCountryCode = None
        self.PayerContactName = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.PayerType = params.get("PayerType")
        self.PayerName = params.get("PayerName")
        self.PayerIdType = params.get("PayerIdType")
        self.PayerIdNo = params.get("PayerIdNo")
        self.PayerContactNumber = params.get("PayerContactNumber")
        self.PayerEmailAddress = params.get("PayerEmailAddress")
        self.PayerCountryCode = params.get("PayerCountryCode")
        self.PayerContactName = params.get("PayerContactName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryPayerinfoResult(AbstractModel):
    """付款人查询结果

    """

    def __init__(self):
        r"""
        :param Code: 错误码
        :type Code: str
        :param Data: 付款人查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryPayerinfoData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryReconciliationDocumentRequest(AbstractModel):
    """QueryReconciliationDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param FileType: STRING(10)，文件类型（充值文件-CZ; 提现文件-TX; 交易文件-JY; 余额文件-YE; 合约文件-HY）
        :type FileType: str
        :param FileDate: STRING(8)，文件日期（格式：20190101）
        :type FileDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FileType = None
        self.FileDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FileType = params.get("FileType")
        self.FileDate = params.get("FileDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryReconciliationDocumentResponse(AbstractModel):
    """QueryReconciliationDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查询结果记录数
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param TranItemArray: 交易信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type TranItemArray: list of FileItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = FileItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryReconciliationFileApplyInfoRequest(AbstractModel):
    """QueryReconciliationFileApplyInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplyFileId: 申请对账文件的任务ID。
        :type ApplyFileId: str
        :param MidasEnvironment: 环境名。
__release__: 现网环境
__sandbox__: 沙箱环境
__development__: 开发环境
_缺省: release_
        :type MidasEnvironment: str
        """
        self.ApplyFileId = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.ApplyFileId = params.get("ApplyFileId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryReconciliationFileApplyInfoResponse(AbstractModel):
    """QueryReconciliationFileApplyInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryReconciliationFileApplyInfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryReconciliationFileApplyInfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryReconciliationFileApplyInfoResult(AbstractModel):
    """查询对账文件申请结果

    """

    def __init__(self):
        r"""
        :param ApplyFileId: 申请对账文件的任务ID。
        :type ApplyFileId: str
        :param ApplyStatus: 对账文件申请状态。
__I__：申请中
__S__：申请成功
__F__：申请失败
        :type ApplyStatus: str
        :param ApplyMessage: 申请结果描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyMessage: str
        :param FileUrlArray: 对账文件下载地址列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrlArray: list of str
        """
        self.ApplyFileId = None
        self.ApplyStatus = None
        self.ApplyMessage = None
        self.FileUrlArray = None


    def _deserialize(self, params):
        self.ApplyFileId = params.get("ApplyFileId")
        self.ApplyStatus = params.get("ApplyStatus")
        self.ApplyMessage = params.get("ApplyMessage")
        self.FileUrlArray = params.get("FileUrlArray")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRefundRequest(AbstractModel):
    """QueryRefund请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合。
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合。
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRefundResponse(AbstractModel):
    """QueryRefund返回参数结构体

    """

    def __init__(self):
        r"""
        :param State: 退款状态码，退款提交成功后返回  1：退款中；  2：退款成功；  3：退款失败。
        :type State: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class QueryShopOpenIdRequest(AbstractModel):
    """QueryShopOpenId请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param ShopNo: 门店编号
        :type ShopNo: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.ShopNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.ShopNo = params.get("ShopNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryShopOpenIdResponse(AbstractModel):
    """QueryShopOpenId返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 获取门店OpenId响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryShopOpenIdResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = QueryShopOpenIdResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryShopOpenIdResult(AbstractModel):
    """获取门店OpenId响应对象

    """

    def __init__(self):
        r"""
        :param Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param ShopName: 门店简称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopName: str
        :param MerchantNo: 商户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        :param CityId: 城市编码
注意：此字段可能返回 null，表示取不到有效值。
        :type CityId: str
        :param OpenId: open_id
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Telephone: 门店电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Telephone: str
        :param ShopNo: 门店编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopNo: str
        :param County: 县/区
注意：此字段可能返回 null，表示取不到有效值。
        :type County: str
        :param ShopFullName: 门店全称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopFullName: str
        :param BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param Address: 详细地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param OpenKey: open_key
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenKey: str
        :param MerchantName: 商户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        """
        self.Province = None
        self.City = None
        self.ShopName = None
        self.MerchantNo = None
        self.CityId = None
        self.OpenId = None
        self.Telephone = None
        self.ShopNo = None
        self.County = None
        self.ShopFullName = None
        self.BrandName = None
        self.Address = None
        self.OpenKey = None
        self.MerchantName = None


    def _deserialize(self, params):
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.ShopName = params.get("ShopName")
        self.MerchantNo = params.get("MerchantNo")
        self.CityId = params.get("CityId")
        self.OpenId = params.get("OpenId")
        self.Telephone = params.get("Telephone")
        self.ShopNo = params.get("ShopNo")
        self.County = params.get("County")
        self.ShopFullName = params.get("ShopFullName")
        self.BrandName = params.get("BrandName")
        self.Address = params.get("Address")
        self.OpenKey = params.get("OpenKey")
        self.MerchantName = params.get("MerchantName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePayItem(AbstractModel):
    """银企直连-查询单笔支付状态条目

    """

    def __init__(self):
        r"""
        :param PayStatus: 付款状态（S：支付成功；P：支付处理中；F：支付失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type PayStatus: str
        :param PlatformMsg: 平台信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PlatformMsg: str
        :param BankRetCode: 银行原始返回码
注意：此字段可能返回 null，表示取不到有效值。
        :type BankRetCode: str
        :param BankRetMsg: 银行原始返回
注意：此字段可能返回 null，表示取不到有效值。
        :type BankRetMsg: str
        """
        self.PayStatus = None
        self.PlatformMsg = None
        self.BankRetCode = None
        self.BankRetMsg = None


    def _deserialize(self, params):
        self.PayStatus = params.get("PayStatus")
        self.PlatformMsg = params.get("PlatformMsg")
        self.BankRetCode = params.get("BankRetCode")
        self.BankRetMsg = params.get("BankRetMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePayRequest(AbstractModel):
    """QuerySinglePay请求参数结构体

    """

    def __init__(self):
        r"""
        :param SerialNumber: 业务流水号
        :type SerialNumber: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.SerialNumber = None
        self.Profile = None


    def _deserialize(self, params):
        self.SerialNumber = params.get("SerialNumber")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePayResponse(AbstractModel):
    """QuerySinglePay返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QuerySinglePayResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QuerySinglePayResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QuerySinglePayResult(AbstractModel):
    """银企直连-查询单笔支付状态结果

    """

    def __init__(self):
        r"""
        :param HandleStatus: 受理状态（S：处理成功；F：处理失败）
        :type HandleStatus: str
        :param HandleMsg: 受理状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type HandleMsg: str
        :param SerialNo: 业务流水号
        :type SerialNo: str
        :param Items: 支付明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of QuerySinglePayItem
        """
        self.HandleStatus = None
        self.HandleMsg = None
        self.SerialNo = None
        self.Items = None


    def _deserialize(self, params):
        self.HandleStatus = params.get("HandleStatus")
        self.HandleMsg = params.get("HandleMsg")
        self.SerialNo = params.get("SerialNo")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = QuerySinglePayItem()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePaymentResultData(AbstractModel):
    """QuerySinglePaymentResult接口返回响应

    """

    def __init__(self):
        r"""
        :param TradeSerialNo: 平台交易流水号，唯一
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeSerialNo: str
        :param OrderId: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param TradeStatus: 交易状态。
0 处理中  
1 预占成功 
2 交易成功 
3 交易失败 
4 未知渠道异常 
5 预占额度失败
6 提交成功
7 提交失败
8 订单重复提交
99 未知系统异常
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeStatus: int
        :param Remark: 业务备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param AgentId: 代理商ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentId: str
        :param AgentName: 代理商名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        :param TradeStatusDesc: 交易状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeStatusDesc: str
        """
        self.TradeSerialNo = None
        self.OrderId = None
        self.TradeStatus = None
        self.Remark = None
        self.AgentId = None
        self.AgentName = None
        self.TradeStatusDesc = None


    def _deserialize(self, params):
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.OrderId = params.get("OrderId")
        self.TradeStatus = params.get("TradeStatus")
        self.Remark = params.get("Remark")
        self.AgentId = params.get("AgentId")
        self.AgentName = params.get("AgentName")
        self.TradeStatusDesc = params.get("TradeStatusDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePaymentResultRequest(AbstractModel):
    """QuerySinglePaymentResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param TransferType: 转账类型
        :type TransferType: int
        :param TradeSerialNo: 交易流水流水号，唯一
        :type TradeSerialNo: str
        :param OrderId: 订单号，与TradeSerialNo不能同时为空
        :type OrderId: str
        """
        self.TransferType = None
        self.TradeSerialNo = None
        self.OrderId = None


    def _deserialize(self, params):
        self.TransferType = params.get("TransferType")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.OrderId = params.get("OrderId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySinglePaymentResultResponse(AbstractModel):
    """QuerySinglePaymentResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功
        :type ErrCode: str
        :param ErrMessage: 响应消息。
        :type ErrMessage: str
        :param Result: 返回响应
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QuerySinglePaymentResultData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QuerySinglePaymentResultData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QuerySingleTransactionStatusRequest(AbstractModel):
    """QuerySingleTransactionStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（2: 会员间交易; 3: 提现; 4: 充值）
        :type FunctionFlag: str
        :param TranNetSeqNo: STRING(52)，交易网流水号（提现，充值或会员交易请求时的CnsmrSeqNo值）
        :type TranNetSeqNo: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号（未启用）
        :type SubAcctNo: str
        :param TranDate: STRING(8)，交易日期（未启用）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetSeqNo = None
        self.SubAcctNo = None
        self.TranDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetSeqNo = params.get("TranNetSeqNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySingleTransactionStatusResponse(AbstractModel):
    """QuerySingleTransactionStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param BookingFlag: STRING(2)，记账标志（记账标志。1: 登记挂账; 2: 支付; 3: 提现; 4: 清分; 5: 下单预支付; 6: 确认并付款; 7: 退款; 8: 支付到平台; N: 其他）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功; 1: 失败; 2: 待确认; 5: 待处理; 6: 处理中。0和1是终态，2、5、6是中间态，其中2是特指提现后待确认提现是否成功，5是银行收到交易等待处理，6是交易正在处理）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param InSubAcctNo: STRING(50)，转入子账户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，转出子账户账号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param FailMsg: STRING(300)，失败信息（当提现失败时，返回交易失败原因）
注意：此字段可能返回 null，表示取不到有效值。
        :type FailMsg: str
        :param OldTranFrontSeqNo: STRING(50)，原前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type OldTranFrontSeqNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.FailMsg = None
        self.OldTranFrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.FailMsg = params.get("FailMsg")
        self.OldTranFrontSeqNo = params.get("OldTranFrontSeqNo")
        self.RequestId = params.get("RequestId")


class QuerySmallAmountTransferRequest(AbstractModel):
    """QuerySmallAmountTransfer请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param OldTranSeqNo: STRING(52)，原交易流水号（小额鉴权交易请求时的CnsmrSeqNo值）
        :type OldTranSeqNo: str
        :param TranDate: STRING(8)，交易日期（格式：20190101）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.OldTranSeqNo = None
        self.TranDate = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.OldTranSeqNo = params.get("OldTranSeqNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuerySmallAmountTransferResponse(AbstractModel):
    """QuerySmallAmountTransfer返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReturnStatus: STRING(10)，返回状态（0: 成功; 1: 失败; 2: 待确认）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnStatus: str
        :param ReturnMsg: STRING(512)，返回信息（失败返回具体信息）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReturnStatus = None
        self.ReturnMsg = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReturnStatus = params.get("ReturnStatus")
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryTradeData(AbstractModel):
    """贸易材料明细查询数据

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param TradeOrderId: 贸易材料订单号
        :type TradeOrderId: str
        :param Status: 审核状态
        :type Status: str
        :param FailReason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayeeName: 收款人姓名
        :type PayeeName: str
        :param PayeeCountryCode: 收款人常驻国家或地区编码
        :type PayeeCountryCode: str
        :param TradeType: 交易类型
        :type TradeType: str
        :param TradeTime: 交易日期
        :type TradeTime: str
        :param TradeCurrency: 交易币种
        :type TradeCurrency: str
        :param TradeAmount: 交易金额
        :type TradeAmount: str
        :param TradeName: 交易名称
        :type TradeName: str
        :param TradeCount: 交易数量
        :type TradeCount: int
        :param GoodsCarrier: 货贸承运人
注意：此字段可能返回 null，表示取不到有效值。
        :type GoodsCarrier: str
        :param ServiceDetail: 服贸交易细节
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDetail: str
        :param ServiceTime: 服贸服务时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTime: str
        """
        self.MerchantId = None
        self.TradeFileId = None
        self.TradeOrderId = None
        self.Status = None
        self.FailReason = None
        self.PayerId = None
        self.PayeeName = None
        self.PayeeCountryCode = None
        self.TradeType = None
        self.TradeTime = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.TradeName = None
        self.TradeCount = None
        self.GoodsCarrier = None
        self.ServiceDetail = None
        self.ServiceTime = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TradeFileId = params.get("TradeFileId")
        self.TradeOrderId = params.get("TradeOrderId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.PayerId = params.get("PayerId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.TradeType = params.get("TradeType")
        self.TradeTime = params.get("TradeTime")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.TradeName = params.get("TradeName")
        self.TradeCount = params.get("TradeCount")
        self.GoodsCarrier = params.get("GoodsCarrier")
        self.ServiceDetail = params.get("ServiceDetail")
        self.ServiceTime = params.get("ServiceTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTradeRequest(AbstractModel):
    """QueryTrade请求参数结构体

    """

    def __init__(self):
        r"""
        :param TradeFileId: 贸易材料流水号
        :type TradeFileId: str
        :param Profile: 接入环境。沙箱环境填sandbox
        :type Profile: str
        """
        self.TradeFileId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TradeFileId = params.get("TradeFileId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTradeResponse(AbstractModel):
    """QueryTrade返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 贸易材料明细查询结果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryTradeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryTradeResult(AbstractModel):
    """贸易材料明细查询结果

    """

    def __init__(self):
        r"""
        :param Data: 贸易材料明细查询数据
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeData`
        :param Code: 错误码
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryTradeData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferBatchRequest(AbstractModel):
    """QueryTransferBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号。
示例值：129284394
        :type MerchantId: str
        :param NeedQueryDetail: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480101
        :type NeedQueryDetail: bool
        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013
        :type MerchantBatchNo: str
        :param BatchId: 是否查询账单明细。
true-是；
false-否，默认否。
商户可选择是否查询指定状态的转账明细单，当转账批次单状态为“FINISHED”（已完成）时，才会返回满足条件的转账明细单。
示例值：true
        :type BatchId: str
        :param Profile: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type Profile: str
        :param Offset: 请求资源起始位置。
从0开始，默认值为0。
示例值：20
        :type Offset: int
        :param Limit: 最大资源条数。
该次请求可返回的最大资源（转账明细单）条数，最小20条，最大100条，不传则默认20条。不足20条按实际条数返回
示例值：20
        :type Limit: int
        :param DetailStatus: 明细状态。
ALL：全部，需要同时查询转账成功喝失败的明细单；
SUCCESS：转账成功，只查询成功的明细单；
FAIL：转账失败，只查询转账失败的明细单。
示例值：FAIL
        :type DetailStatus: str
        """
        self.MerchantId = None
        self.NeedQueryDetail = None
        self.MerchantBatchNo = None
        self.BatchId = None
        self.Profile = None
        self.Offset = None
        self.Limit = None
        self.DetailStatus = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.NeedQueryDetail = params.get("NeedQueryDetail")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.Profile = params.get("Profile")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DetailStatus = params.get("DetailStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferBatchResponse(AbstractModel):
    """QueryTransferBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号。
示例值：19300009329
        :type MerchantId: str
        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013
        :type MerchantBatchNo: str
        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
示例值：1030000071100999991182020050700019480001
        :type BatchId: str
        :param MerchantAppId: 直连商户appId。
商户号绑定的appid。
示例值：wxf636efh567hg4356
        :type MerchantAppId: str
        :param BatchStatus: 批次状态。
ACCEPTED:已受理，批次已受理成功，若发起批量转账的30分钟后，转账批次单仍处于该状态，可能原因是商户账户余额不足等。商户可查询账户资金流水，若该笔转账批次单的扣款已经发生，则表示批次已经进入转账中，请再次查单确认；
PROCESSING:转账中，已开始处理批次内的转账明细单；
FINISHED:已完成，批次内的所有转账明细单都已处理完成；
CLOSED:已关闭，可查询具体的批次关闭原因确认；
示例值：ACCEPTED
        :type BatchStatus: str
        :param CloseReason: 批次关闭原因。
如果批次单状态为“CLOSED”（已关闭），则有关闭原因；
MERCHANT_REVOCATION：商户主动撤销；
OVERDUE_CLOSE：系统超时关闭。
示例值：OVERDUE_CLOSE
注意：此字段可能返回 null，表示取不到有效值。
        :type CloseReason: str
        :param TotalAmount: 转账总金额。
转账金额，单位为分。
示例值：4000000
        :type TotalAmount: int
        :param TotalNum: 转账总笔数。
一个转账批次最多允许发起三千笔转账。
示例值：200
        :type TotalNum: int
        :param CreateTime: 批次受理成功时返回，遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 批次最近一次更新时间，遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param SuccessAmount: 转账成功金额。
转账成功的金额，单位为分，可能随时变化。
示例值：4000000
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessAmount: int
        :param SuccessNum: 转账成功的笔数。
可能随时变化。
示例值：200
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessNum: int
        :param FailAmount: 转账失败金额。
转账失败的金额，单位为分，可能随时变化。
示例值：4000000
注意：此字段可能返回 null，表示取不到有效值。
        :type FailAmount: int
        :param FailNum: 转账失败笔数。
可能随时变化。
示例值：200
注意：此字段可能返回 null，表示取不到有效值。
        :type FailNum: int
        :param TransferDetails: 转账明细列表。
返回明细详情
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferDetails: list of TransferDetailResponse
        :param BatchType: 批次类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchType: str
        :param BatchName: 批次名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchName: str
        :param BatchRemark: 批次标注。
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchRemark: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantId = None
        self.MerchantBatchNo = None
        self.BatchId = None
        self.MerchantAppId = None
        self.BatchStatus = None
        self.CloseReason = None
        self.TotalAmount = None
        self.TotalNum = None
        self.CreateTime = None
        self.UpdateTime = None
        self.SuccessAmount = None
        self.SuccessNum = None
        self.FailAmount = None
        self.FailNum = None
        self.TransferDetails = None
        self.BatchType = None
        self.BatchName = None
        self.BatchRemark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.MerchantAppId = params.get("MerchantAppId")
        self.BatchStatus = params.get("BatchStatus")
        self.CloseReason = params.get("CloseReason")
        self.TotalAmount = params.get("TotalAmount")
        self.TotalNum = params.get("TotalNum")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.SuccessAmount = params.get("SuccessAmount")
        self.SuccessNum = params.get("SuccessNum")
        self.FailAmount = params.get("FailAmount")
        self.FailNum = params.get("FailNum")
        if params.get("TransferDetails") is not None:
            self.TransferDetails = []
            for item in params.get("TransferDetails"):
                obj = TransferDetailResponse()
                obj._deserialize(item)
                self.TransferDetails.append(obj)
        self.BatchType = params.get("BatchType")
        self.BatchName = params.get("BatchName")
        self.BatchRemark = params.get("BatchRemark")
        self.RequestId = params.get("RequestId")


class QueryTransferDetailRequest(AbstractModel):
    """QueryTransferDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号。
示例值：129284394
        :type MerchantId: str
        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013
        :type MerchantBatchNo: str
        :param MerchantDetailNo: 商家明细单号。
商户系统内部的商家明细单号
示例值：plfk2020042013
        :type MerchantDetailNo: str
        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
商家单号（包含批次号和明细单号）和微信单号（包含批次号和明细单号）二者必填其一。
示例值：1030000071100999991182020050700019480001
        :type BatchId: str
        :param DetailId: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480001
        :type DetailId: str
        :param Profile: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type Profile: str
        """
        self.MerchantId = None
        self.MerchantBatchNo = None
        self.MerchantDetailNo = None
        self.BatchId = None
        self.DetailId = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.BatchId = params.get("BatchId")
        self.DetailId = params.get("DetailId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferDetailResponse(AbstractModel):
    """QueryTransferDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号。
示例值：19300009329
        :type MerchantId: str
        :param MerchantBatchNo: 商家批次单号。
商户系统内部的商家批次单号，此参数只能由数字、字母组成，商户系统内部唯一，UTF8编码，最多32个字符。
示例值：plfk2020042013
        :type MerchantBatchNo: str
        :param BatchId: 微信批次单号。
微信商家转账系统返回的唯一标识。
示例值：1030000071100999991182020050700019480001
        :type BatchId: str
        :param MerchantDetailNo: 商家明细单号。
商户系统内部的商家明细单号
示例值：plfk2020042013
        :type MerchantDetailNo: str
        :param DetailId: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480001
        :type DetailId: str
        :param DetailStatus: 明细状态。
PROCESSING：转账中，正在处理，结果未明；
SUCCESS：转账成功；
FAIL：转账失败，需要确认失败原因以后，再决定是否重新发起地该笔明细的转账。
示例值：SUCCESS
        :type DetailStatus: str
        :param TransferAmount: 转账金额。
单位为分。
示例值：200
        :type TransferAmount: int
        :param FailReason: 失败原因。
如果转账失败则有失败原因
ACCOUNT_FROZEN：账户冻结
REAL_NAME_CHECK_FAIL：用户未实名
NAME_NOT_CORRECT：用户姓名校验失败
OPENID_INVALID：Openid校验失败
TRANSFER_QUOTA_EXCEED：超过用户单笔收款额度
DAY_RECEIVED_QUOTA_EXCEED：超过用户单日收款额度
MONTH_RECEIVED_QUOTA_EXCEED：超过用户单月收款额度
DAY_RECEIVED_COUNT_EXCEED：超过用户单日收款次数
PRODUCT_AUTH_CHECK_FAIL：产品权限校验失败
OVERDUE_CLOSE：转账关闭
ID_CARD_NOT_CORRECT：用户身份证校验失败
ACCOUNT_NOT_EXIST：用户账户不存在
TRANSFER_RISK：转账存在风险
示例值：ACCOUNT_FROZEN
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param InitiateTime: 转账发起时间。
遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。
        :type InitiateTime: str
        :param UpdateTime: 转账更新时间。
遵循rfc3339标准格式。格式为YYYY-MM-DDTHH:mm:ss.sss+TIMEZONE，YYYY-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.sss表示时分秒毫秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35.120+08:00表示北京时间2015年05月20日13点29分35秒。
示例值：2015-05-20T13:29:35.120+08:00
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param UserName: 用户名。
示例值：张三
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param TransferRemark: 转账备注。
单条转账备注（微信用户会收到该备注）。UTF8编码，最多32字符。
示例值：2020年4月报销
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferRemark: str
        :param MerchantAppId: 商家绑定公众号APPID。
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantAppId: str
        :param OpenId: 用户openId。
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantId = None
        self.MerchantBatchNo = None
        self.BatchId = None
        self.MerchantDetailNo = None
        self.DetailId = None
        self.DetailStatus = None
        self.TransferAmount = None
        self.FailReason = None
        self.InitiateTime = None
        self.UpdateTime = None
        self.UserName = None
        self.TransferRemark = None
        self.MerchantAppId = None
        self.OpenId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantBatchNo = params.get("MerchantBatchNo")
        self.BatchId = params.get("BatchId")
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.DetailId = params.get("DetailId")
        self.DetailStatus = params.get("DetailStatus")
        self.TransferAmount = params.get("TransferAmount")
        self.FailReason = params.get("FailReason")
        self.InitiateTime = params.get("InitiateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.UserName = params.get("UserName")
        self.TransferRemark = params.get("TransferRemark")
        self.MerchantAppId = params.get("MerchantAppId")
        self.OpenId = params.get("OpenId")
        self.RequestId = params.get("RequestId")


class QueryTransferResultData(AbstractModel):
    """智能代发-单笔代发转账查询接口返回内容

    """

    def __init__(self):
        r"""
        :param TradeSerialNo: 平台交易流水号
        :type TradeSerialNo: str
        :param OrderId: 订单号
        :type OrderId: str
        :param TradeStatus: 交易状态。
0 处理中  
1 提交成功 
2 交易成功 
3 交易失败 
4 未知渠道异常 
99 未知系统异常
        :type TradeStatus: int
        :param Remark: 业务备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.TradeSerialNo = None
        self.OrderId = None
        self.TradeStatus = None
        self.Remark = None


    def _deserialize(self, params):
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.OrderId = params.get("OrderId")
        self.TradeStatus = params.get("TradeStatus")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferResultRequest(AbstractModel):
    """QueryTransferResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param MerchantAppId: 申请商户号的appid或者商户号绑定的appid
        :type MerchantAppId: str
        :param TransferType: 1、 微信企业付款 
2、 支付宝转账 
3、 平安银企直联代发转账
        :type TransferType: int
        :param TradeSerialNo: 交易流水流水号（与 OrderId 不能同时为空）
        :type TradeSerialNo: str
        :param OrderId: 订单号（与 TradeSerialNo 不能同时为空）
        :type OrderId: str
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        """
        self.MerchantId = None
        self.MerchantAppId = None
        self.TransferType = None
        self.TradeSerialNo = None
        self.OrderId = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantAppId = params.get("MerchantAppId")
        self.TransferType = params.get("TransferType")
        self.TradeSerialNo = params.get("TradeSerialNo")
        self.OrderId = params.get("OrderId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryTransferResultResponse(AbstractModel):
    """QueryTransferResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功
        :type ErrCode: str
        :param ErrMessage: 响应消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryTransferResultData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = QueryTransferResultData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class RechargeByThirdPayRequest(AbstractModel):
    """RechargeByThirdPay请求参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型 此接口固定填：MemberRechargeThirdPayReq
        :type RequestType: str
        :param MerchantCode: 商户号
        :type MerchantCode: str
        :param PayChannel: 支付渠道
        :type PayChannel: str
        :param PayChannelSubId: 子渠道
        :type PayChannelSubId: int
        :param OrderId: 交易订单号
        :type OrderId: str
        :param BankAccountNumber: 父账户账号，资金汇总账号
        :type BankAccountNumber: str
        :param PlatformShortNumber: 平台短号(银行分配)
        :type PlatformShortNumber: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param TransSequenceNumber: 交易流水号
        :type TransSequenceNumber: str
        :param BankSubAccountNumber: 子账户账号
        :type BankSubAccountNumber: str
        :param TransFee: 交易手续费，以元为单位
        :type TransFee: str
        :param ThirdPayChannel: 第三方支付渠道类型 0001-微信 0002-支付宝 0003-京东支付
        :type ThirdPayChannel: str
        :param ThirdPayChannelMerchantCode: 第三方渠道商户号
        :type ThirdPayChannelMerchantCode: str
        :param ThirdPayChannelOrderId: 第三方渠道订单号或流水号
        :type ThirdPayChannelOrderId: str
        :param CurrencyAmount: 交易金额
        :type CurrencyAmount: str
        :param CurrencyUnit: 单位，1：元，2：角，3：分
        :type CurrencyUnit: str
        :param CurrencyType: 币种
        :type CurrencyType: str
        :param TransNetMemberCode: 交易网会员代码
        :type TransNetMemberCode: str
        :param MidasEnvironment: midas环境参数
        :type MidasEnvironment: str
        :param ReservedMessage: 保留域
        :type ReservedMessage: str
        :param Remark: 备注
        :type Remark: str
        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.PlatformShortNumber = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.BankSubAccountNumber = None
        self.TransFee = None
        self.ThirdPayChannel = None
        self.ThirdPayChannelMerchantCode = None
        self.ThirdPayChannelOrderId = None
        self.CurrencyAmount = None
        self.CurrencyUnit = None
        self.CurrencyType = None
        self.TransNetMemberCode = None
        self.MidasEnvironment = None
        self.ReservedMessage = None
        self.Remark = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.BankSubAccountNumber = params.get("BankSubAccountNumber")
        self.TransFee = params.get("TransFee")
        self.ThirdPayChannel = params.get("ThirdPayChannel")
        self.ThirdPayChannelMerchantCode = params.get("ThirdPayChannelMerchantCode")
        self.ThirdPayChannelOrderId = params.get("ThirdPayChannelOrderId")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyType = params.get("CurrencyType")
        self.TransNetMemberCode = params.get("TransNetMemberCode")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeByThirdPayResponse(AbstractModel):
    """RechargeByThirdPay返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReservedMessage: 保留字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMessage: str
        :param FrontSequenceNumber: 银行流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSequenceNumber: str
        :param RequestType: 请求类型
        :type RequestType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReservedMessage = None
        self.FrontSequenceNumber = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMessage = params.get("ReservedMessage")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class RechargeMemberThirdPayRequest(AbstractModel):
    """RechargeMemberThirdPay请求参数结构体

    """

    def __init__(self):
        r"""
        :param TranNetMemberCode: STRING(32)，交易网会代码
        :type TranNetMemberCode: str
        :param MemberFillAmt: STRING(20)，会员充值金额
        :type MemberFillAmt: str
        :param Commission: STRING(20)，手续费金额
        :type Commission: str
        :param Ccy: STRING(3)，币种。如RMB
        :type Ccy: str
        :param PayChannelType: STRING(20)，支付渠道类型。
0001-微信
0002-支付宝
0003-京东支付
        :type PayChannelType: str
        :param PayChannelAssignMerNo: STRING(50)，支付渠道所分配的商户号
        :type PayChannelAssignMerNo: str
        :param PayChannelTranSeqNo: STRING(52)，支付渠道交易流水号
        :type PayChannelTranSeqNo: str
        :param EjzbOrderNo: STRING(52)，电商见证宝订单号
        :type EjzbOrderNo: str
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param EjzbOrderContent: STRING(500)，电商见证宝订单内容
        :type EjzbOrderContent: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.TranNetMemberCode = None
        self.MemberFillAmt = None
        self.Commission = None
        self.Ccy = None
        self.PayChannelType = None
        self.PayChannelAssignMerNo = None
        self.PayChannelTranSeqNo = None
        self.EjzbOrderNo = None
        self.MrchCode = None
        self.EjzbOrderContent = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberFillAmt = params.get("MemberFillAmt")
        self.Commission = params.get("Commission")
        self.Ccy = params.get("Ccy")
        self.PayChannelType = params.get("PayChannelType")
        self.PayChannelAssignMerNo = params.get("PayChannelAssignMerNo")
        self.PayChannelTranSeqNo = params.get("PayChannelTranSeqNo")
        self.EjzbOrderNo = params.get("EjzbOrderNo")
        self.MrchCode = params.get("MrchCode")
        self.EjzbOrderContent = params.get("EjzbOrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RechargeMemberThirdPayResponse(AbstractModel):
    """RechargeMemberThirdPay返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param MemberSubAcctPreAvailBal: STRING(20)，会员子账户交易前可用余额
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberSubAcctPreAvailBal: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.MemberSubAcctPreAvailBal = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.MemberSubAcctPreAvailBal = params.get("MemberSubAcctPreAvailBal")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class RefundCloudOrderRequest(AbstractModel):
    """RefundCloudOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 米大师分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户Id，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type RefundId: str
        :param TotalRefundAmt: 退款金额，单位：分
当该字段为空或者为0时，系统会默认使用订单当实付金额作为退款金额
        :type TotalRefundAmt: int
        :param OutTradeNo: 商品订单，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type OutTradeNo: str
        :param MidasEnvironment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type MidasEnvironment: str
        :param PlatformRefundAmt: 平台应收金额，单位：分
        :type PlatformRefundAmt: int
        :param MchRefundAmt: 结算应收金额，单位：分
        :type MchRefundAmt: int
        :param SubOrderRefundList: 支持多个子订单批量退款单个子订单退款支持传SubOutTradeNo
也支持传SubOrderRefundList，都传的时候以SubOrderRefundList为准。
如果传了子单退款细节，外部不需要再传退款金额，平台应退，商户应退金额
        :type SubOrderRefundList: list of CloudSubOrderRefund
        :param ChannelOrderId: 渠道订单号，当出现重复支付时，可以将重复支付订单的渠道订单号传入，以进行退款（注意：目前该重复支付订单的渠道订单号仅能通过米大师内部获取），更多重复支付订单退款说明，请参考[重复支付订单退款说明](https://dev.tke.midas.qq.com/juxin-doc-next/apidocs/receive-order/Refund.html#%E9%87%8D%E5%A4%8D%E6%94%AF%E4%BB%98%E8%AE%A2%E5%8D%95%E9%80%80%E6%AC%BE%E8%AF%B4%E6%98%8E)
        :type ChannelOrderId: str
        :param RefundNotifyUrl: 通知地址
        :type RefundNotifyUrl: str
        :param Metadata: 透传字段，退款成功回调透传给应用，用于开发者透传自定义内容
        :type Metadata: str
        :param ExternalRefundPromptGroupList: 渠道扩展退款促销列表，可将各个渠道的退款促销信息放于该列表
        :type ExternalRefundPromptGroupList: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.RefundId = None
        self.TotalRefundAmt = None
        self.OutTradeNo = None
        self.MidasEnvironment = None
        self.PlatformRefundAmt = None
        self.MchRefundAmt = None
        self.SubOrderRefundList = None
        self.ChannelOrderId = None
        self.RefundNotifyUrl = None
        self.Metadata = None
        self.ExternalRefundPromptGroupList = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.TotalRefundAmt = params.get("TotalRefundAmt")
        self.OutTradeNo = params.get("OutTradeNo")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        self.MchRefundAmt = params.get("MchRefundAmt")
        if params.get("SubOrderRefundList") is not None:
            self.SubOrderRefundList = []
            for item in params.get("SubOrderRefundList"):
                obj = CloudSubOrderRefund()
                obj._deserialize(item)
                self.SubOrderRefundList.append(obj)
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.RefundNotifyUrl = params.get("RefundNotifyUrl")
        self.Metadata = params.get("Metadata")
        self.ExternalRefundPromptGroupList = params.get("ExternalRefundPromptGroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundCloudOrderResponse(AbstractModel):
    """RefundCloudOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RefundMemberTransactionRequest(AbstractModel):
    """RefundMemberTransaction请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutSubAccountName: 转出见证子账户的户名
        :type OutSubAccountName: str
        :param InSubAccountName: 转入见证子账户的户名
        :type InSubAccountName: str
        :param PayChannelSubId: 子渠道
        :type PayChannelSubId: int
        :param OutSubAccountNumber: 转出见证子账户账号
        :type OutSubAccountNumber: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param InSubAccountNumber: 转入见证子账户账号
        :type InSubAccountNumber: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param BankAccountNumber: 父账户账号，资金汇总账号
        :type BankAccountNumber: str
        :param OldTransSequenceNumber: 原老订单流水号
        :type OldTransSequenceNumber: str
        :param MerchantCode: 银行注册商户号
        :type MerchantCode: str
        :param RequestType: 请求类型，固定为MemberTransactionRefundReq
        :type RequestType: str
        :param CurrencyAmount: 交易金额
        :type CurrencyAmount: str
        :param TransSequenceNumber: 交易流水号
        :type TransSequenceNumber: str
        :param PayChannel: 渠道
        :type PayChannel: str
        :param OldOrderId: 原订单号
        :type OldOrderId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param OrderId: 订单号
        :type OrderId: str
        :param MidasEnvironment: Midas环境标识 release 现网环境 sandbox 沙箱环境
development 开发环境
        :type MidasEnvironment: str
        :param OutTransNetMemberCode: 转出子账户交易网会员代码
        :type OutTransNetMemberCode: str
        :param InTransNetMemberCode: 转入子账户交易网会员代码
        :type InTransNetMemberCode: str
        :param ReservedMessage: 保留域
        :type ReservedMessage: str
        :param PlatformShortNumber: 平台短号(银行分配)
        :type PlatformShortNumber: str
        :param TransType: 0-登记挂账，1-撤销挂账
        :type TransType: str
        :param TransFee: 交易手续费
        :type TransFee: str
        """
        self.OutSubAccountName = None
        self.InSubAccountName = None
        self.PayChannelSubId = None
        self.OutSubAccountNumber = None
        self.MidasSignature = None
        self.InSubAccountNumber = None
        self.MidasSecretId = None
        self.BankAccountNumber = None
        self.OldTransSequenceNumber = None
        self.MerchantCode = None
        self.RequestType = None
        self.CurrencyAmount = None
        self.TransSequenceNumber = None
        self.PayChannel = None
        self.OldOrderId = None
        self.MidasAppId = None
        self.OrderId = None
        self.MidasEnvironment = None
        self.OutTransNetMemberCode = None
        self.InTransNetMemberCode = None
        self.ReservedMessage = None
        self.PlatformShortNumber = None
        self.TransType = None
        self.TransFee = None


    def _deserialize(self, params):
        self.OutSubAccountName = params.get("OutSubAccountName")
        self.InSubAccountName = params.get("InSubAccountName")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OutSubAccountNumber = params.get("OutSubAccountNumber")
        self.MidasSignature = params.get("MidasSignature")
        self.InSubAccountNumber = params.get("InSubAccountNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.OldTransSequenceNumber = params.get("OldTransSequenceNumber")
        self.MerchantCode = params.get("MerchantCode")
        self.RequestType = params.get("RequestType")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.PayChannel = params.get("PayChannel")
        self.OldOrderId = params.get("OldOrderId")
        self.MidasAppId = params.get("MidasAppId")
        self.OrderId = params.get("OrderId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.OutTransNetMemberCode = params.get("OutTransNetMemberCode")
        self.InTransNetMemberCode = params.get("InTransNetMemberCode")
        self.ReservedMessage = params.get("ReservedMessage")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.TransType = params.get("TransType")
        self.TransFee = params.get("TransFee")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundMemberTransactionResponse(AbstractModel):
    """RefundMemberTransaction返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型
        :type RequestType: str
        :param FrontSequenceNumber: 银行流水号
        :type FrontSequenceNumber: str
        :param ReservedMessage: 保留域
        :type ReservedMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestType = None
        self.FrontSequenceNumber = None
        self.ReservedMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.ReservedMessage = params.get("ReservedMessage")
        self.RequestId = params.get("RequestId")


class RefundOpenBankOrderRequest(AbstractModel):
    """RefundOpenBankOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param OutRefundId: 外部商户退款单号。
        :type OutRefundId: str
        :param RefundAmount: 退款金额。单位分。
        :type RefundAmount: int
        :param ChannelMerchantId: 渠道商户号。
        :type ChannelMerchantId: str
        :param OutOrderId: 外部商户订单号，与云企付渠道订单号二者选填其一。
        :type OutOrderId: str
        :param ChannelOrderId: 云企付渠道订单号，与外部订单号二者选填其一。
        :type ChannelOrderId: str
        :param NotifyUrl: 退款通知地址。
        :type NotifyUrl: str
        :param RefundReason: 退款原因。
        :type RefundReason: str
        :param ExternalRefundData: 第三方渠道退款附加信息。详见附录-复杂类型。
若未作特殊说明，则无需传入。
        :type ExternalRefundData: str
        :param Remark: 备注信息
        :type Remark: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.OutRefundId = None
        self.RefundAmount = None
        self.ChannelMerchantId = None
        self.OutOrderId = None
        self.ChannelOrderId = None
        self.NotifyUrl = None
        self.RefundReason = None
        self.ExternalRefundData = None
        self.Remark = None
        self.Environment = None


    def _deserialize(self, params):
        self.OutRefundId = params.get("OutRefundId")
        self.RefundAmount = params.get("RefundAmount")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.OutOrderId = params.get("OutOrderId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        self.NotifyUrl = params.get("NotifyUrl")
        self.RefundReason = params.get("RefundReason")
        self.ExternalRefundData = params.get("ExternalRefundData")
        self.Remark = params.get("Remark")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundOpenBankOrderResponse(AbstractModel):
    """RefundOpenBankOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码
        :type ErrCode: str
        :param ErrMessage: 错误消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.OpenBankRefundOrderApplyResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = OpenBankRefundOrderApplyResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class RefundOrderRequest(AbstractModel):
    """RefundOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 进件成功后返给商户方的AppId
        :type MerchantAppId: str
        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。
        :type OrderNo: str
        """
        self.MerchantAppId = None
        self.OrderNo = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundOrderResponse(AbstractModel):
    """RefundOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantAppId: 进件成功后返给商户方的AppId
        :type MerchantAppId: str
        :param OrderNo: 平台流水号。消费订单发起成功后，返回的平台唯一订单号。
        :type OrderNo: str
        :param Status: 订单退款状态。0-退款失败
1-退款成功 
2-可疑状态
        :type Status: str
        :param Description: 订单退款状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MerchantAppId = None
        self.OrderNo = None
        self.Status = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MerchantAppId = params.get("MerchantAppId")
        self.OrderNo = params.get("OrderNo")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class RefundOrderResult(AbstractModel):
    """订单退款响应对象

    """

    def __init__(self):
        r"""
        :param OrderNo: 付款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param DeveloperNo: 开发者流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type DeveloperNo: str
        :param TradeDiscountAmount: 交易优惠金额（免充值券）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeDiscountAmount: str
        :param PayName: 付款方式名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PayName: str
        :param OrderMerchantId: 商户流水号（从1开始自增长不重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderMerchantId: str
        :param TradeAmount: 实际交易金额（以分为单位，没有小数点）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeAmount: str
        :param CurrencySign: 币种签名
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrencySign: str
        :param TradePayTime: 付款完成时间（以收单机构为准）
注意：此字段可能返回 null，表示取不到有效值。
        :type TradePayTime: str
        :param ShopOrderId: 门店流水号（从1开始自增长不重复）
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopOrderId: str
        :param PayTag: 支付标签
注意：此字段可能返回 null，表示取不到有效值。
        :type PayTag: str
        :param Status: 订单状态（1交易成功，2待支付，4已取消，9等待用户输入密码确认
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param OrderCurrency: 币种代码
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderCurrency: str
        :param TradeTime: 开始交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeTime: str
        :param DiscountAmount: 折扣金额（以分为单位，没有小数点）
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountAmount: str
        :param OriginalOrderNo: 原始订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalOrderNo: str
        """
        self.OrderNo = None
        self.DeveloperNo = None
        self.TradeDiscountAmount = None
        self.PayName = None
        self.OrderMerchantId = None
        self.TradeAmount = None
        self.CurrencySign = None
        self.TradePayTime = None
        self.ShopOrderId = None
        self.PayTag = None
        self.Status = None
        self.OrderCurrency = None
        self.TradeTime = None
        self.DiscountAmount = None
        self.OriginalOrderNo = None


    def _deserialize(self, params):
        self.OrderNo = params.get("OrderNo")
        self.DeveloperNo = params.get("DeveloperNo")
        self.TradeDiscountAmount = params.get("TradeDiscountAmount")
        self.PayName = params.get("PayName")
        self.OrderMerchantId = params.get("OrderMerchantId")
        self.TradeAmount = params.get("TradeAmount")
        self.CurrencySign = params.get("CurrencySign")
        self.TradePayTime = params.get("TradePayTime")
        self.ShopOrderId = params.get("ShopOrderId")
        self.PayTag = params.get("PayTag")
        self.Status = params.get("Status")
        self.OrderCurrency = params.get("OrderCurrency")
        self.TradeTime = params.get("TradeTime")
        self.DiscountAmount = params.get("DiscountAmount")
        self.OriginalOrderNo = params.get("OriginalOrderNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundOutSubOrderRefundList(AbstractModel):
    """退款子订单列表

    """

    def __init__(self):
        r"""
        :param PlatformRefundAmt: 平台应退金额
        :type PlatformRefundAmt: int
        :param RefundAmt: 子订单退款金额
        :type RefundAmt: int
        :param SubMchRefundAmt: 商家应退金额
        :type SubMchRefundAmt: int
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param SubRefundId: 子退款单号，调用方需要保证 全局唯一性
        :type SubRefundId: str
        """
        self.PlatformRefundAmt = None
        self.RefundAmt = None
        self.SubMchRefundAmt = None
        self.SubOutTradeNo = None
        self.SubRefundId = None


    def _deserialize(self, params):
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        self.RefundAmt = params.get("RefundAmt")
        self.SubMchRefundAmt = params.get("SubMchRefundAmt")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubRefundId = params.get("SubRefundId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundRequest(AbstractModel):
    """Refund请求参数结构体

    """

    def __init__(self):
        r"""
        :param UserId: 用户ID，长度不小于5位， 仅支持字母和数字的组合
        :type UserId: str
        :param RefundId: 退款订单号，仅支持数字、 字母、下划线（_）、横杠字 符（-）、点（.）的组合
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param TotalRefundAmt: 退款金额，单位：分。备注：当该字段为空或者为0 时，系统会默认使用订单当 实付金额作为退款金额
        :type TotalRefundAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param OutTradeNo: 商品订单，仅支持数字、字 母、下划线（_）、横杠字符 （-）、点（.）的组合。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo
        :type OutTradeNo: str
        :param MchRefundAmt: 结算应收金额，单位：分
        :type MchRefundAmt: int
        :param TransactionId: 调用下单接口获取的聚鑫交 易订单。  OutTradeNo ,TransactionId 二选一,不能都为空,优先使用 OutTradeNo
        :type TransactionId: str
        :param PlatformRefundAmt: 平台应收金额，单位：分
        :type PlatformRefundAmt: int
        :param SubOrderRefundList: 支持多个子订单批量退款单 个子订单退款支持传 SubOutTradeNo ，也支持传 SubOutTradeNoList ，都传的时候以 SubOutTradeNoList 为准。  如果传了子单退款细节，外 部不需要再传退款金额，平 台应退，商户应退金额，我 们可以直接根据子单退款算出来总和。
        :type SubOrderRefundList: list of RefundOutSubOrderRefundList
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.TotalRefundAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.MchRefundAmt = None
        self.TransactionId = None
        self.PlatformRefundAmt = None
        self.SubOrderRefundList = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.TotalRefundAmt = params.get("TotalRefundAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.MchRefundAmt = params.get("MchRefundAmt")
        self.TransactionId = params.get("TransactionId")
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        if params.get("SubOrderRefundList") is not None:
            self.SubOrderRefundList = []
            for item in params.get("SubOrderRefundList"):
                obj = RefundOutSubOrderRefundList()
                obj._deserialize(item)
                self.SubOrderRefundList.append(obj)
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundResponse(AbstractModel):
    """Refund返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RefundTlinxOrderRequest(AbstractModel):
    """RefundTlinxOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param DeveloperNo: 原始订单的开发者交易流水号
        :type DeveloperNo: str
        :param RefundOutNo: 新退款订单的开发者流水号，同一门店内唯一
        :type RefundOutNo: str
        :param RefundOrderName: 退款订单名称，可以为空
        :type RefundOrderName: str
        :param RefundAmount: 退款金额（以分为单位，没有小数点）
        :type RefundAmount: str
        :param ShopPassword: 主管密码，对密码进行SHA-1加密，默认为123456
        :type ShopPassword: str
        :param Remark: 退款备注
        :type Remark: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.DeveloperNo = None
        self.RefundOutNo = None
        self.RefundOrderName = None
        self.RefundAmount = None
        self.ShopPassword = None
        self.Remark = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.DeveloperNo = params.get("DeveloperNo")
        self.RefundOutNo = params.get("RefundOutNo")
        self.RefundOrderName = params.get("RefundOrderName")
        self.RefundAmount = params.get("RefundAmount")
        self.ShopPassword = params.get("ShopPassword")
        self.Remark = params.get("Remark")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefundTlinxOrderResponse(AbstractModel):
    """RefundTlinxOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 业务系统返回码，0表示成功，其他表示失败。
        :type ErrCode: str
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param Result: 退款响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.RefundOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = RefundOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class RegisterBehaviorRequest(AbstractModel):
    """RegisterBehavior请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param FunctionFlag: 功能标志
1：登记行为记录信息
2：查询补录信息
        :type FunctionFlag: int
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param OperationClickTime: 操作点击时间
yyyyMMddHHmmss
功能标志FunctionFlag=1时必输
        :type OperationClickTime: str
        :param IpAddress: IP地址
功能标志FunctionFlag=1时必输
        :type IpAddress: str
        :param MacAddress: MAC地址
功能标志FunctionFlag=1时必输
        :type MacAddress: str
        :param SignChannel: 签约渠道
1:  App
2:  平台H5网页
3：公众号
4：小程序
功能标志FunctionFlag=1时必输
        :type SignChannel: int
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.FunctionFlag = None
        self.MidasEnvironment = None
        self.OperationClickTime = None
        self.IpAddress = None
        self.MacAddress = None
        self.SignChannel = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.FunctionFlag = params.get("FunctionFlag")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.OperationClickTime = params.get("OperationClickTime")
        self.IpAddress = params.get("IpAddress")
        self.MacAddress = params.get("MacAddress")
        self.SignChannel = params.get("SignChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterBehaviorResponse(AbstractModel):
    """RegisterBehavior返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReplenishSuccessFlag: 补录是否成功标志
功能标志为2时存在。
S：成功
F：失败
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplenishSuccessFlag: str
        :param RegisterInfo: 签约信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisterInfo: :class:`tencentcloud.cpdp.v20190820.models.RegisterInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReplenishSuccessFlag = None
        self.RegisterInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplenishSuccessFlag = params.get("ReplenishSuccessFlag")
        if params.get("RegisterInfo") is not None:
            self.RegisterInfo = RegisterInfo()
            self.RegisterInfo._deserialize(params.get("RegisterInfo"))
        self.RequestId = params.get("RequestId")


class RegisterBillRequest(AbstractModel):
    """RegisterBill请求参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型此接口固定填：RegBillSupportWithdrawReq
        :type RequestType: str
        :param MerchantCode: 商户号
        :type MerchantCode: str
        :param PayChannel: 支付渠道
        :type PayChannel: str
        :param PayChannelSubId: 子渠道
        :type PayChannelSubId: int
        :param OrderId: 交易订单号
        :type OrderId: str
        :param BankAccountNo: 父账户账号，资金汇总账号
        :type BankAccountNo: str
        :param PlatformShortNo: 平台短号(银行分配)
        :type PlatformShortNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param TransSeqNo: 交易流水号
        :type TransSeqNo: str
        :param TranFee: 暂未使用，默认传0.0
        :type TranFee: str
        :param OrderAmt: 挂账金额，以元为单位
        :type OrderAmt: str
        :param BankSubAccountNo: 子账户账号
        :type BankSubAccountNo: str
        :param TranNetMemberCode: 交易网会员代码
        :type TranNetMemberCode: str
        :param TranType: 0,登记挂账，1，撤销挂账
        :type TranType: str
        :param ReservedMessage: 保留域
        :type ReservedMessage: str
        :param Remark: 备注
        :type Remark: str
        :param MidasEnvironment: Midas环境参数
        :type MidasEnvironment: str
        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNo = None
        self.PlatformShortNo = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSeqNo = None
        self.TranFee = None
        self.OrderAmt = None
        self.BankSubAccountNo = None
        self.TranNetMemberCode = None
        self.TranType = None
        self.ReservedMessage = None
        self.Remark = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNo = params.get("BankAccountNo")
        self.PlatformShortNo = params.get("PlatformShortNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSeqNo = params.get("TransSeqNo")
        self.TranFee = params.get("TranFee")
        self.OrderAmt = params.get("OrderAmt")
        self.BankSubAccountNo = params.get("BankSubAccountNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.TranType = params.get("TranType")
        self.ReservedMessage = params.get("ReservedMessage")
        self.Remark = params.get("Remark")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterBillResponse(AbstractModel):
    """RegisterBill返回参数结构体

    """

    def __init__(self):
        r"""
        :param FrontSeqNo: 银行流水号
        :type FrontSeqNo: str
        :param ReservedMessage: 保留字段
        :type ReservedMessage: str
        :param RequestType: 请求类型
        :type RequestType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FrontSeqNo = None
        self.ReservedMessage = None
        self.RequestType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMessage = params.get("ReservedMessage")
        self.RequestType = params.get("RequestType")
        self.RequestId = params.get("RequestId")


class RegisterBillSupportWithdrawRequest(AbstractModel):
    """RegisterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        r"""
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param OrderNo: STRING(50)，订单号
        :type OrderNo: str
        :param SuspendAmt: STRING(20)，挂账金额（包含交易费用）
        :type SuspendAmt: str
        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）
        :type TranFee: str
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.TranNetMemberCode = None
        self.OrderNo = None
        self.SuspendAmt = None
        self.TranFee = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OrderNo = params.get("OrderNo")
        self.SuspendAmt = params.get("SuspendAmt")
        self.TranFee = params.get("TranFee")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterBillSupportWithdrawResponse(AbstractModel):
    """RegisterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param CnsmrSeqNo: String(22)，交易流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.FrontSeqNo = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RegisterInfo(AbstractModel):
    """签约信息

    """

    def __init__(self):
        r"""
        :param LegalPersonIdCode: 法人证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type LegalPersonIdCode: str
        :param LegalPersonIdType: 法人证件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LegalPersonIdType: str
        :param LegalPersonName: 法人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LegalPersonName: str
        :param OrganizationCode: 公司证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCode: str
        :param OrganizationName: 公司名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param OrganizationType: 公司证件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationType: str
        """
        self.LegalPersonIdCode = None
        self.LegalPersonIdType = None
        self.LegalPersonName = None
        self.OrganizationCode = None
        self.OrganizationName = None
        self.OrganizationType = None


    def _deserialize(self, params):
        self.LegalPersonIdCode = params.get("LegalPersonIdCode")
        self.LegalPersonIdType = params.get("LegalPersonIdType")
        self.LegalPersonName = params.get("LegalPersonName")
        self.OrganizationCode = params.get("OrganizationCode")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationType = params.get("OrganizationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseQueryContract(AbstractModel):
    """签约数据

    """

    def __init__(self):
        r"""
        :param ExternalReturnCode: 第三方渠道错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnCode: str
        :param ExternalReturnMessage: 第三方渠道错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnMessage: str
        :param ExternalReturnData: 第三方渠道返回的原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnData: str
        :param ChannelMerchantId: 米大师内部商户号
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 米大师内部子商户号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelSubMerchantId: str
        :param ChannelAppId: 米大师内部应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelAppId: str
        :param ChannelSubAppId: 米大师内部子应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelSubAppId: str
        :param ChannelName: 渠道名称
        :type ChannelName: str
        :param ReturnContractInfo: 返回的合约信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ReturnContractInfo`
        :param NotifyUrl: 签约通知地址
        :type NotifyUrl: str
        """
        self.ExternalReturnCode = None
        self.ExternalReturnMessage = None
        self.ExternalReturnData = None
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelAppId = None
        self.ChannelSubAppId = None
        self.ChannelName = None
        self.ReturnContractInfo = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.ExternalReturnCode = params.get("ExternalReturnCode")
        self.ExternalReturnMessage = params.get("ExternalReturnMessage")
        self.ExternalReturnData = params.get("ExternalReturnData")
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelAppId = params.get("ChannelAppId")
        self.ChannelSubAppId = params.get("ChannelSubAppId")
        self.ChannelName = params.get("ChannelName")
        if params.get("ReturnContractInfo") is not None:
            self.ReturnContractInfo = ReturnContractInfo()
            self.ReturnContractInfo._deserialize(params.get("ReturnContractInfo"))
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseTerminateContract(AbstractModel):
    """解约数据

    """

    def __init__(self):
        r"""
        :param ExternalReturnCode: 第三方渠道错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnCode: str
        :param ExternalReturnMessage: 第三方渠道错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnMessage: str
        :param ExternalReturnData: 第三方渠道返回的原始数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalReturnData: str
        """
        self.ExternalReturnCode = None
        self.ExternalReturnMessage = None
        self.ExternalReturnData = None


    def _deserialize(self, params):
        self.ExternalReturnCode = params.get("ExternalReturnCode")
        self.ExternalReturnMessage = params.get("ExternalReturnMessage")
        self.ExternalReturnData = params.get("ExternalReturnData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReturnContractInfo(AbstractModel):
    """返回的合约信息

    """

    def __init__(self):
        r"""
        :param ContractInfo: 合约信息
        :type ContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ContractInfo`
        :param ChannelReturnContractInfo: 米大师内部生成的合约信息
        :type ChannelReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ChannelReturnContractInfo`
        :param ExternalReturnContractInfo: 第三方渠道合约信息
        :type ExternalReturnContractInfo: :class:`tencentcloud.cpdp.v20190820.models.ExternalReturnContractInfo`
        """
        self.ContractInfo = None
        self.ChannelReturnContractInfo = None
        self.ExternalReturnContractInfo = None


    def _deserialize(self, params):
        if params.get("ContractInfo") is not None:
            self.ContractInfo = ContractInfo()
            self.ContractInfo._deserialize(params.get("ContractInfo"))
        if params.get("ChannelReturnContractInfo") is not None:
            self.ChannelReturnContractInfo = ChannelReturnContractInfo()
            self.ChannelReturnContractInfo._deserialize(params.get("ChannelReturnContractInfo"))
        if params.get("ExternalReturnContractInfo") is not None:
            self.ExternalReturnContractInfo = ExternalReturnContractInfo()
            self.ExternalReturnContractInfo._deserialize(params.get("ExternalReturnContractInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevResigterBillSupportWithdrawRequest(AbstractModel):
    """RevResigterBillSupportWithdraw请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param OldOrderNo: STRING(30)，原订单号（RegisterBillSupportWithdraw接口中的订单号）
        :type OldOrderNo: str
        :param CancelAmt: STRING(20)，撤销金额（支持部分撤销，不能大于原订单可用金额，包含交易费用）
        :type CancelAmt: str
        :param TranFee: STRING(20)，交易费用（暂未使用，默认传0.0）
        :type TranFee: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.OldOrderNo = None
        self.CancelAmt = None
        self.TranFee = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OldOrderNo = params.get("OldOrderNo")
        self.CancelAmt = params.get("CancelAmt")
        self.TranFee = params.get("TranFee")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevResigterBillSupportWithdrawResponse(AbstractModel):
    """RevResigterBillSupportWithdraw返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class ReviseMbrPropertyRequest(AbstractModel):
    """ReviseMbrProperty请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
        :type SubAcctNo: str
        :param MemberProperty: STRING(10)，会员属性（00-普通子账号; SH-商户子账户。暂时只支持00-普通子账号改为SH-商户子账户）
        :type MemberProperty: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberProperty = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberProperty = params.get("MemberProperty")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReviseMbrPropertyResponse(AbstractModel):
    """ReviseMbrProperty返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RevokeMemberRechargeThirdPayRequest(AbstractModel):
    """RevokeMemberRechargeThirdPay请求参数结构体

    """

    def __init__(self):
        r"""
        :param OldFillFrontSeqNo: STRING(52)，原充值的前置流水号
        :type OldFillFrontSeqNo: str
        :param OldFillPayChannelType: STRING(20)，原充值的支付渠道类型
        :type OldFillPayChannelType: str
        :param OldPayChannelTranSeqNo: STRING(52)，原充值的支付渠道交易流水号
        :type OldPayChannelTranSeqNo: str
        :param OldFillEjzbOrderNo: STRING(52)，原充值的电商见证宝订单号
        :type OldFillEjzbOrderNo: str
        :param ApplyCancelMemberAmt: STRING(20)，申请撤销的会员金额
        :type ApplyCancelMemberAmt: str
        :param ApplyCancelCommission: STRING(20)，申请撤销的手续费金额
        :type ApplyCancelCommission: str
        :param MrchCode: String(22)，商户号
        :type MrchCode: str
        :param Remark: STRING(300)，备注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.OldFillFrontSeqNo = None
        self.OldFillPayChannelType = None
        self.OldPayChannelTranSeqNo = None
        self.OldFillEjzbOrderNo = None
        self.ApplyCancelMemberAmt = None
        self.ApplyCancelCommission = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None
        self.Profile = None


    def _deserialize(self, params):
        self.OldFillFrontSeqNo = params.get("OldFillFrontSeqNo")
        self.OldFillPayChannelType = params.get("OldFillPayChannelType")
        self.OldPayChannelTranSeqNo = params.get("OldPayChannelTranSeqNo")
        self.OldFillEjzbOrderNo = params.get("OldFillEjzbOrderNo")
        self.ApplyCancelMemberAmt = params.get("ApplyCancelMemberAmt")
        self.ApplyCancelCommission = params.get("ApplyCancelCommission")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeMemberRechargeThirdPayResponse(AbstractModel):
    """RevokeMemberRechargeThirdPay返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class RevokeRechargeByThirdPayRequest(AbstractModel):
    """RevokeRechargeByThirdPay请求参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型此接口固定填：RevokeMemberRechargeThirdPayReq
        :type RequestType: str
        :param MerchantCode: 商户号
        :type MerchantCode: str
        :param PayChannel: 支付渠道
        :type PayChannel: str
        :param PayChannelSubId: 子渠道
        :type PayChannelSubId: int
        :param OrderId: 原始充值交易订单号
        :type OrderId: str
        :param BankAccountNumber: 父账户账号，资金汇总账号
        :type BankAccountNumber: str
        :param PlatformShortNumber: 平台短号(银行分配)
        :type PlatformShortNumber: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSignature: 计费签名
        :type MidasSignature: str
        :param TransSequenceNumber: 交易流水号
        :type TransSequenceNumber: str
        :param TransFee: 申请撤销的手续费金额,以元为单位
        :type TransFee: str
        :param ThirdPayChannel: 第三方支付渠道类型 0001-微信 0002-支付宝 0003-京东支付
        :type ThirdPayChannel: str
        :param ThirdPayChannelOrderId: 第三方渠道订单号或流水号
        :type ThirdPayChannelOrderId: str
        :param OldFrontSequenceNumber: 充值接口银行返回的流水号(FrontSeqNo)
        :type OldFrontSequenceNumber: str
        :param CurrencyAmount: 申请撤销的金额
        :type CurrencyAmount: str
        :param CurrencyUnit: 单位，1：元，2：角，3：分 目前固定填1
        :type CurrencyUnit: str
        :param CurrencyType: 币种 目前固定填RMB
        :type CurrencyType: str
        :param MidasEnvironment: Midas环境标识
        :type MidasEnvironment: str
        :param ReservedMessage: 保留域
        :type ReservedMessage: str
        :param Remark: 备注
        :type Remark: str
        """
        self.RequestType = None
        self.MerchantCode = None
        self.PayChannel = None
        self.PayChannelSubId = None
        self.OrderId = None
        self.BankAccountNumber = None
        self.PlatformShortNumber = None
        self.MidasSecretId = None
        self.MidasAppId = None
        self.MidasSignature = None
        self.TransSequenceNumber = None
        self.TransFee = None
        self.ThirdPayChannel = None
        self.ThirdPayChannelOrderId = None
        self.OldFrontSequenceNumber = None
        self.CurrencyAmount = None
        self.CurrencyUnit = None
        self.CurrencyType = None
        self.MidasEnvironment = None
        self.ReservedMessage = None
        self.Remark = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.MerchantCode = params.get("MerchantCode")
        self.PayChannel = params.get("PayChannel")
        self.PayChannelSubId = params.get("PayChannelSubId")
        self.OrderId = params.get("OrderId")
        self.BankAccountNumber = params.get("BankAccountNumber")
        self.PlatformShortNumber = params.get("PlatformShortNumber")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSignature = params.get("MidasSignature")
        self.TransSequenceNumber = params.get("TransSequenceNumber")
        self.TransFee = params.get("TransFee")
        self.ThirdPayChannel = params.get("ThirdPayChannel")
        self.ThirdPayChannelOrderId = params.get("ThirdPayChannelOrderId")
        self.OldFrontSequenceNumber = params.get("OldFrontSequenceNumber")
        self.CurrencyAmount = params.get("CurrencyAmount")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyType = params.get("CurrencyType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.ReservedMessage = params.get("ReservedMessage")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeRechargeByThirdPayResponse(AbstractModel):
    """RevokeRechargeByThirdPay返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestType: 请求类型
        :type RequestType: str
        :param ReservedMessage: 保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMessage: str
        :param FrontSequenceNumber: 银行流水号
        :type FrontSequenceNumber: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestType = None
        self.ReservedMessage = None
        self.FrontSequenceNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestType = params.get("RequestType")
        self.ReservedMessage = params.get("ReservedMessage")
        self.FrontSequenceNumber = params.get("FrontSequenceNumber")
        self.RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    """场景信息

    """

    def __init__(self):
        r"""
        :param LocaleCode: 语言代码
注意：此字段可能返回 null，表示取不到有效值。
        :type LocaleCode: str
        :param RegionCode: 地区代码
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionCode: str
        :param UserClientIp: 用户IP
注意：此字段可能返回 null，表示取不到有效值。
        :type UserClientIp: str
        """
        self.LocaleCode = None
        self.RegionCode = None
        self.UserClientIp = None


    def _deserialize(self, params):
        self.LocaleCode = params.get("LocaleCode")
        self.RegionCode = params.get("RegionCode")
        self.UserClientIp = params.get("UserClientIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SettleInfo(AbstractModel):
    """商户结算信息

    """

    def __init__(self):
        r"""
        :param SettleAccountType: 结算账户类型 
PRIVATE：对私 
BUSINESS：对公
HELIPAY渠道必传
        :type SettleAccountType: str
        :param SettleAccountNumber: 结算账号
HELIPAY渠道必传
        :type SettleAccountNumber: str
        :param SettleAccountName: 结算账户名称
HELIPAY渠道必传
        :type SettleAccountName: str
        :param BankBranchId: 支行号
HELIPAY渠道必传
        :type BankBranchId: str
        :param BankBranchName: 支行名称
        :type BankBranchName: str
        :param SettleMode: 结算方式 
AUTO：自动结算 
SELF：自主结算
HELIPAY渠道必传
        :type SettleMode: str
        :param SettlePeriod: 结算周期 
T1：工作日隔天结算 
D1：自然日隔天结算 
D0：当日结算
HELIPAY渠道必传
        :type SettlePeriod: str
        """
        self.SettleAccountType = None
        self.SettleAccountNumber = None
        self.SettleAccountName = None
        self.BankBranchId = None
        self.BankBranchName = None
        self.SettleMode = None
        self.SettlePeriod = None


    def _deserialize(self, params):
        self.SettleAccountType = params.get("SettleAccountType")
        self.SettleAccountNumber = params.get("SettleAccountNumber")
        self.SettleAccountName = params.get("SettleAccountName")
        self.BankBranchId = params.get("BankBranchId")
        self.BankBranchName = params.get("BankBranchName")
        self.SettleMode = params.get("SettleMode")
        self.SettlePeriod = params.get("SettlePeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SettlementOrderResult(AbstractModel):
    """结算订单结果

    """

    def __init__(self):
        r"""
        :param IncomeType: 收入类型
LABOR:劳务所得
OCCASION:偶然所得
        :type IncomeType: str
        :param AmountBeforeTax: 税前金额
        :type AmountBeforeTax: str
        :param AmountAfterTax: 税后金额
注意：此字段可能返回 null，表示取不到有效值。
        :type AmountAfterTax: str
        :param Tax: 税金
注意：此字段可能返回 null，表示取不到有效值。
        :type Tax: str
        :param OutOrderId: 外部订单ID
        :type OutOrderId: str
        :param OrderId: 订单ID
        :type OrderId: str
        :param InitiateTime: 发起时间
        :type InitiateTime: str
        :param FinishTime: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        :param Status: 状态
ACCEPTED:已受理
ACCOUNTED:已记账
SUCCEED:已成功
FAILED:已失败
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        :param Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.IncomeType = None
        self.AmountBeforeTax = None
        self.AmountAfterTax = None
        self.Tax = None
        self.OutOrderId = None
        self.OrderId = None
        self.InitiateTime = None
        self.FinishTime = None
        self.Status = None
        self.StatusDesc = None
        self.Remark = None


    def _deserialize(self, params):
        self.IncomeType = params.get("IncomeType")
        self.AmountBeforeTax = params.get("AmountBeforeTax")
        self.AmountAfterTax = params.get("AmountAfterTax")
        self.Tax = params.get("Tax")
        self.OutOrderId = params.get("OutOrderId")
        self.OrderId = params.get("OrderId")
        self.InitiateTime = params.get("InitiateTime")
        self.FinishTime = params.get("FinishTime")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SettlementOrders(AbstractModel):
    """结算订单列表

    """

    def __init__(self):
        r"""
        :param List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of SettlementOrderResult
        :param Count: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.List = None
        self.Count = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SettlementOrderResult()
                obj._deserialize(item)
                self.List.append(obj)
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportBankInfo(AbstractModel):
    """支持的银行信息

    """

    def __init__(self):
        r"""
        :param BankCode: 银行简称。
        :type BankCode: str
        :param BankName: 银行名称。
        :type BankName: str
        :param MaintainStatus: 状态。
__MAINTAINING__: 维护中
__WORKING__: 正常工作
注意：此字段可能返回 null，表示取不到有效值。
        :type MaintainStatus: str
        :param BankNotice: 银行渠道维护公告。
注意：此字段可能返回 null，表示取不到有效值。
        :type BankNotice: str
        :param BankId: 支持银行代码
注意：此字段可能返回 null，表示取不到有效值。
        :type BankId: str
        :param CardType: 卡类型。
D：借记卡，C：信用卡，Z：借贷合一卡。
注意：此字段可能返回 null，表示取不到有效值。
        :type CardType: str
        """
        self.BankCode = None
        self.BankName = None
        self.MaintainStatus = None
        self.BankNotice = None
        self.BankId = None
        self.CardType = None


    def _deserialize(self, params):
        self.BankCode = params.get("BankCode")
        self.BankName = params.get("BankName")
        self.MaintainStatus = params.get("MaintainStatus")
        self.BankNotice = params.get("BankNotice")
        self.BankId = params.get("BankId")
        self.CardType = params.get("CardType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncContractDataRequest(AbstractModel):
    """SyncContractData请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param Channel: 签约使用的渠道
        :type Channel: str
        :param OutContractCode: 业务签约合同协议号
        :type OutContractCode: str
        :param ContractStatus: 签约状态，枚举值
CONTRACT_STATUS_INVALID=无效状态
CONTRACT_STATUS_SIGNED=已签约
CONTRACT_STATUS_TERMINATED=已解约
CONTRACT_STATUS_PENDING=签约进行中
        :type ContractStatus: str
        :param ContractSyncInfo: 签约同步信息
        :type ContractSyncInfo: :class:`tencentcloud.cpdp.v20190820.models.ContractSyncInfo`
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param UserType: 用户类型，枚举值
USER_ID: 用户ID
ANONYMOUS: 匿名类型 USER_ID
默认值为 USER_ID
        :type UserType: str
        :param SceneInfo: 场景信息
        :type SceneInfo: :class:`tencentcloud.cpdp.v20190820.models.SceneInfo`
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.Channel = None
        self.OutContractCode = None
        self.ContractStatus = None
        self.ContractSyncInfo = None
        self.MidasSignature = None
        self.MidasSecretId = None
        self.SubAppId = None
        self.UserType = None
        self.SceneInfo = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.OutContractCode = params.get("OutContractCode")
        self.ContractStatus = params.get("ContractStatus")
        if params.get("ContractSyncInfo") is not None:
            self.ContractSyncInfo = ContractSyncInfo()
            self.ContractSyncInfo._deserialize(params.get("ContractSyncInfo"))
        self.MidasSignature = params.get("MidasSignature")
        self.MidasSecretId = params.get("MidasSecretId")
        self.SubAppId = params.get("SubAppId")
        self.UserType = params.get("UserType")
        if params.get("SceneInfo") is not None:
            self.SceneInfo = SceneInfo()
            self.SceneInfo._deserialize(params.get("SceneInfo"))
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncContractDataResponse(AbstractModel):
    """SyncContractData返回参数结构体

    """

    def __init__(self):
        r"""
        :param Msg: 请求处理信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class TerminateContractRequest(AbstractModel):
    """TerminateContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param Channel: 指定渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定
        :type Channel: str
        :param TerminateMode: 枚举值：
CONTRACT_TERMINATION_MODE_BY_OUT_CONTRACT_CODE: 按OutContractCode+ContractSceneId解约
CONTRACT_TERMINATION_MODE_BY_CHANNEL_CONTRACT_CODE：按ChannelContractCode解约
        :type TerminateMode: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param OutContractCode: 业务签约合同协议号 当TerminateMode=CONTRACT_TERMINATION_MODE_BY_OUT_CONTRACT_CODE 时 必填
        :type OutContractCode: str
        :param ContractSceneId: 签约场景ID，当 TerminateMode=CONTRACT_TERMINATION_MODE_BY_OUT_CONTRACT_CODE 时 必填，在米大师侧托管后生成
        :type ContractSceneId: str
        :param ChannelContractCode: 米大师生成的协议号 当 TerminateMode=CONTRACT_TERMINATION_MODE_BY_CHANNEL_CONTRACT_CODE 时 必填
        :type ChannelContractCode: str
        :param ExternalContractData: 第三方渠道合约数据，json字符串，与特定渠道有关
        :type ExternalContractData: str
        :param TerminationReason: 终止合约原因
        :type TerminationReason: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param UserType: USER_ID: 用户ID
ANONYMOUS: 匿名类型 USER_ID
默认值为 USER_ID
        :type UserType: str
        :param ContractMethod: 签约方式
        :type ContractMethod: str
        :param MigrateMode: 签约代扣穿透查询存量数据迁移模式
        :type MigrateMode: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.Channel = None
        self.TerminateMode = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.SubAppId = None
        self.OutContractCode = None
        self.ContractSceneId = None
        self.ChannelContractCode = None
        self.ExternalContractData = None
        self.TerminationReason = None
        self.MidasEnvironment = None
        self.UserType = None
        self.ContractMethod = None
        self.MigrateMode = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.TerminateMode = params.get("TerminateMode")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.SubAppId = params.get("SubAppId")
        self.OutContractCode = params.get("OutContractCode")
        self.ContractSceneId = params.get("ContractSceneId")
        self.ChannelContractCode = params.get("ChannelContractCode")
        self.ExternalContractData = params.get("ExternalContractData")
        self.TerminationReason = params.get("TerminationReason")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.UserType = params.get("UserType")
        self.ContractMethod = params.get("ContractMethod")
        self.MigrateMode = params.get("MigrateMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateContractResponse(AbstractModel):
    """TerminateContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContractTerminateData: 解约数据
        :type ContractTerminateData: :class:`tencentcloud.cpdp.v20190820.models.ResponseTerminateContract`
        :param Msg: 请求处理信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContractTerminateData = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContractTerminateData") is not None:
            self.ContractTerminateData = ResponseTerminateContract()
            self.ContractTerminateData._deserialize(params.get("ContractTerminateData"))
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class TranItem(AbstractModel):
    """交易信息

    """

    def __init__(self):
        r"""
        :param FundSummaryAcctNo: STRING(50)，资金汇总账号
注意：此字段可能返回 null，表示取不到有效值。
        :type FundSummaryAcctNo: str
        :param SubAcctNo: STRING(50)，见证子账户的账号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，会员名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，会员绑定账户的账号（提现的银行卡）
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberAcctNo: str
        :param BankType: STRING(10)，会员绑定账户的本他行类型（1: 本行; 2: 他行）
注意：此字段可能返回 null，表示取不到有效值。
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，会员绑定账户的开户行名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，会员绑定账户的开户行的联行号
注意：此字段可能返回 null，表示取不到有效值。
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，会员绑定账户的开户行的超级网银行号
注意：此字段可能返回 null，表示取不到有效值。
        :type EiconBankBranchId: str
        :param Mobile: STRING(30)，会员的手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
        self.FundSummaryAcctNo = None
        self.SubAcctNo = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.Mobile = None


    def _deserialize(self, params):
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionItem(AbstractModel):
    """交易明细信息

    """

    def __init__(self):
        r"""
        :param BookingFlag: STRING(2)，记账标志（1: 转出; 2: 转入）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param BookingType: STRING(20)，记账类型（详情见“常见问题”）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingType: str
        :param InSubAcctNo: STRING(50)，转入见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，转出见证子账户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param Remark: STRING(300)，备注（返回交易订单号）
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.BookingType = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.BookingType = params.get("BookingType")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferDetailRequest(AbstractModel):
    """批量转账明细实体

    """

    def __init__(self):
        r"""
        :param MerchantDetailNo: 商家明细单号。
商户系统内部区分转账批次单下不同转账明细单的唯一标识，要求此参数只能由数字、大小写字母组成。
示例值：x23zy545Bd5436
        :type MerchantDetailNo: str
        :param TransferAmount: 转账金额。
转账金额单位为分。
示例值：200000
        :type TransferAmount: int
        :param TransferRemark: 转账备注。
单条转账备注（微信用户会收到该备注）。UTF8编码，最多32字符。
示例值：2020年4月报销
        :type TransferRemark: str
        :param OpenId: 用户在直连商户下的唯一标识。
示例值：o-MYE42l80oelYMDE34nYD456Xoy
        :type OpenId: str
        :param UserName: 收款用户姓名。
收款方姓名。
示例值：张三
        :type UserName: str
        """
        self.MerchantDetailNo = None
        self.TransferAmount = None
        self.TransferRemark = None
        self.OpenId = None
        self.UserName = None


    def _deserialize(self, params):
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.TransferAmount = params.get("TransferAmount")
        self.TransferRemark = params.get("TransferRemark")
        self.OpenId = params.get("OpenId")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferDetailResponse(AbstractModel):
    """批量转账查询返回批次明细实体

    """

    def __init__(self):
        r"""
        :param MerchantDetailNo: 商家明细单号。
商户系统内部的商家明细单号
示例值：plfk2020042013
        :type MerchantDetailNo: str
        :param DetailId: 微信明细单号。
微信区分明细单返回的唯一标识。
示例值：1030000071100999991182020050700019480001
        :type DetailId: str
        :param DetailStatus: 明细状态。
PROCESSING：转账中，正在处理，结果未明；
SUCCESS：转账成功；
FAIL：转账失败，需要确认失败原因以后，再决定是否重新发起地该笔明细的转账。
示例值：SUCCESS
        :type DetailStatus: str
        """
        self.MerchantDetailNo = None
        self.DetailId = None
        self.DetailStatus = None


    def _deserialize(self, params):
        self.MerchantDetailNo = params.get("MerchantDetailNo")
        self.DetailId = params.get("DetailId")
        self.DetailStatus = params.get("DetailStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferItem(AbstractModel):
    """转账充值明细信息

    """

    def __init__(self):
        r"""
        :param InAcctType: STRING(10)，入账类型（02: 会员充值; 03: 资金挂账）
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctType: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranAmt: STRING(20)，入金金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param InAcctNo: STRING(50)，入金账号
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctNo: str
        :param InAcctName: STRING(150)，入金账户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InAcctName: str
        :param Ccy: STRING(3)，币种
注意：此字段可能返回 null，表示取不到有效值。
        :type Ccy: str
        :param AccountingDate: STRING(8)，会计日期（即银行主机记账日期）
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountingDate: str
        :param BankName: STRING(150)，银行名称（付款账户银行名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type BankName: str
        :param Remark: STRING(300)，转账备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        """
        self.InAcctType = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.TranAmt = None
        self.InAcctNo = None
        self.InAcctName = None
        self.Ccy = None
        self.AccountingDate = None
        self.BankName = None
        self.Remark = None
        self.FrontSeqNo = None


    def _deserialize(self, params):
        self.InAcctType = params.get("InAcctType")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranAmt = params.get("TranAmt")
        self.InAcctNo = params.get("InAcctNo")
        self.InAcctName = params.get("InAcctName")
        self.Ccy = params.get("Ccy")
        self.AccountingDate = params.get("AccountingDate")
        self.BankName = params.get("BankName")
        self.Remark = params.get("Remark")
        self.FrontSeqNo = params.get("FrontSeqNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferSinglePayData(AbstractModel):
    """智能代发-单笔代发转账接口返回数据

    """

    def __init__(self):
        r"""
        :param TradeSerialNo: 平台交易流水号，唯一
        :type TradeSerialNo: str
        """
        self.TradeSerialNo = None


    def _deserialize(self, params):
        self.TradeSerialNo = params.get("TradeSerialNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferSinglePayRequest(AbstractModel):
    """TransferSinglePay请求参数结构体

    """

    def __init__(self):
        r"""
        :param MerchantId: 商户号
        :type MerchantId: str
        :param MerchantAppId: 微信申请商户号的appid或者商户号绑定的appid
支付宝、平安填入MerchantId
        :type MerchantAppId: str
        :param TransferType: 1、 微信企业付款 
2、 支付宝转账 
3、 平安银企直联代发转账
        :type TransferType: int
        :param OrderId: 订单流水号，唯一，不能包含特殊字符，长度最大限制64位，推荐使用字母，数字组合，"_","-"组合
        :type OrderId: str
        :param TransferAmount: 转账金额，单位分
        :type TransferAmount: int
        :param PayeeId: 收款方标识。
微信为open_id；
支付宝为会员alipay_user_id;
平安为收款方银行账号
        :type PayeeId: str
        :param PayeeName: 收款方姓名。支付宝可选；微信，平安模式下必传
        :type PayeeName: str
        :param PayeeExtends: 收款方附加信息，平安接入使用。需要以JSON格式提供以下字段：
PayeeBankName：收款人开户行名称
 CcyCode：货币类型（RMB-人民币）
 UnionFlag：行内跨行标志（1：行内转账，0：跨行转账）。
        :type PayeeExtends: str
        :param ReqReserved: 请求预留字段，原样透传返回
        :type ReqReserved: str
        :param Remark: 业务备注
        :type Remark: str
        :param NotifyUrl: 转账结果回调通知URL。若不填，则不进行回调。
        :type NotifyUrl: str
        :param Profile: 接入环境。沙箱环境填sandbox。
        :type Profile: str
        """
        self.MerchantId = None
        self.MerchantAppId = None
        self.TransferType = None
        self.OrderId = None
        self.TransferAmount = None
        self.PayeeId = None
        self.PayeeName = None
        self.PayeeExtends = None
        self.ReqReserved = None
        self.Remark = None
        self.NotifyUrl = None
        self.Profile = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.MerchantAppId = params.get("MerchantAppId")
        self.TransferType = params.get("TransferType")
        self.OrderId = params.get("OrderId")
        self.TransferAmount = params.get("TransferAmount")
        self.PayeeId = params.get("PayeeId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeExtends = params.get("PayeeExtends")
        self.ReqReserved = params.get("ReqReserved")
        self.Remark = params.get("Remark")
        self.NotifyUrl = params.get("NotifyUrl")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferSinglePayResponse(AbstractModel):
    """TransferSinglePay返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功
        :type ErrCode: str
        :param ErrMessage: 响应消息
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.TransferSinglePayData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = TransferSinglePayData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UnBindAcctRequest(AbstractModel):
    """UnBindAcct请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SettleAcctNo: 用于提现
<敏感信息>加密详见<a href="https://cloud.tencent.com/document/product/1122/48979" target="_blank">《商户端接口敏感信息加密说明》</a>
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param EncryptType: 敏感信息加密类型:
RSA: rsa非对称加密，使用RSA-PKCS1-v1_5
AES: aes对称加密，使用AES256-CBC-PCKS7padding
缺省: RSA
        :type EncryptType: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.EncryptType = None
        self.MidasEnvironment = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.EncryptType = params.get("EncryptType")
        self.MidasEnvironment = params.get("MidasEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindAcctResponse(AbstractModel):
    """UnBindAcct返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindOpenBankExternalSubMerchantBankAccountRequest(AbstractModel):
    """UnbindOpenBankExternalSubMerchantBankAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。
__TENPAY__: 商企付
__WECHAT__: 微信支付
__ALIPAY__: 支付宝
        :type ChannelName: str
        :param PaymentMethod: 支付方式。
__EBANK_PAYMENT__: ebank支付
__OPENBANK_PAYMENT__: openbank支付
        :type PaymentMethod: str
        :param BindSerialNo: 绑卡序列号。
        :type BindSerialNo: str
        :param OutApplyId: 外部申请编号。
        :type OutApplyId: str
        :param NotifyUrl: 通知地址。
        :type NotifyUrl: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.PaymentMethod = None
        self.BindSerialNo = None
        self.OutApplyId = None
        self.NotifyUrl = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.PaymentMethod = params.get("PaymentMethod")
        self.BindSerialNo = params.get("BindSerialNo")
        self.OutApplyId = params.get("OutApplyId")
        self.NotifyUrl = params.get("NotifyUrl")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindOpenBankExternalSubMerchantBankAccountResponse(AbstractModel):
    """UnbindOpenBankExternalSubMerchantBankAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
__SUCCESS__: 成功
__其他__: 见附录-错误码表
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.UnbindOpenBankExternalSubMerchantBankAccountResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = UnbindOpenBankExternalSubMerchantBankAccountResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UnbindOpenBankExternalSubMerchantBankAccountResult(AbstractModel):
    """第三方子商户银行卡解绑返回结果

    """

    def __init__(self):
        r"""
        :param ChannelApplyId: 渠道申请编号。
        :type ChannelApplyId: str
        :param UnbindStatus: 解绑状态。
__SUCCESS__: 解绑成功
__FAILED__: 解绑失败
__PROCESSING__: 解绑中
注意：若返回解绑中，需要再次调用解绑结果查询接口查询结果。
        :type UnbindStatus: str
        :param UnbindMessage: 解绑返回描述, 例如失败原因等。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnbindMessage: str
        """
        self.ChannelApplyId = None
        self.UnbindStatus = None
        self.UnbindMessage = None


    def _deserialize(self, params):
        self.ChannelApplyId = params.get("ChannelApplyId")
        self.UnbindStatus = params.get("UnbindStatus")
        self.UnbindMessage = params.get("UnbindMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindRelateAcctRequest(AbstractModel):
    """UnbindRelateAcct请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 解绑）
        :type FunctionFlag: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码（若需要把一个待绑定账户关联到两个会员名下，此字段可上送两个会员的交易网代码，并且须用“|::|”(右侧)进行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，待解绑的提现账户的账号（提现账号）
        :type MemberAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.ReservedMsg = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindRelateAcctResponse(AbstractModel):
    """UnbindRelateAcct返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号（即电商见证宝系统生成的流水号，可关联具体一笔请求）
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class UnifiedCloudOrderRequest(AbstractModel):
    """UnifiedCloudOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param MidasAppId: 米大师分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用户ID
长度不小于5位，仅支持字母和数字的组合，长度限制以具体接入渠道为准
        :type UserId: str
        :param OutTradeNo: 开发者主订单号
支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合，长度供参考，部分渠道存在长度更短的情况接入时请联系开发咨询
        :type OutTradeNo: str
        :param CurrencyType: 货币类型
ISO货币代码，CNY
        :type CurrencyType: str
        :param ProductId: 商品ID
业务自定义的商品id，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合。
        :type ProductId: str
        :param ProductName: 商品名称
业务自定义的商品名称，无需URL编码，长度限制以具体所接入渠道为准。
        :type ProductName: str
        :param ProductDetail: 商品详情
业务自定义的商品详情，无需URL编码，长度限制以具体所接入渠道为准。
        :type ProductDetail: str
        :param OriginalAmt: 原始金额
单位：分，需要注意的是，OriginalAmt>=TotalAmt
        :type OriginalAmt: int
        :param TotalAmt: 支付金额
单位：分，需要注意的是，TotalAmt=TotalPlatformIncome+TotalMchIncome。
        :type TotalAmt: int
        :param MidasEnvironment: 环境类型
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type MidasEnvironment: str
        :param SubAppId: 支付SubAppId
米大师计费SubAppId，代表子商户。指定使用该商户的商户号下单时必传。
        :type SubAppId: str
        :param RealChannel: 顶层支付渠道
银行收单:
openbank_ccb: 建设银行
openbank_icbc: 工商银行
openbank_cmb: 招商银行
openbank_ping: 平安银行
openbank_icbc_jft：工商银行聚付通
非银行收单，可以为空
        :type RealChannel: str
        :param Channel: 支付渠道
wechat：微信支付
wechat_ecommerce: 微信电商收付通
open_alipay: 支付宝
open_quickpass: 银联云闪付
icbc_epay: 工银e支付
foreign_cardpay: 外卡支付
icbc_jft_wechat: 工行聚付通-微信
icbc_jft_alipay: 工行聚付通-支付宝
icbc_jft_epay: 工行聚付通-e支付
指定渠道下单时必传
        :type Channel: str
        :param Metadata: 透传字段
支付成功回调透传给应用，用于开发者透传自定义内容。
        :type Metadata: str
        :param Quantity: 数量
购买数量,不传默认为1。
        :type Quantity: int
        :param CallbackUrl: Web端回调地址
Web端网页回调地址，仅当Web端SDK使用页面跳转方式时有效。
        :type CallbackUrl: str
        :param CancelUrl: 支付取消地址
        :type CancelUrl: str
        :param WxAppId: 微信AppId
wechat渠道或wchat_ecommerce渠道可以指定下单时的wxappid。
        :type WxAppId: str
        :param WxSubAppId: 微信SubAppId
wechat渠道可以指定下单时的sub_appid。
        :type WxSubAppId: str
        :param WxOpenId: 微信公众号/小程序OpenId
微信公众号/小程序支付时为必选，需要传微信下的openid。
        :type WxOpenId: str
        :param WxSubOpenId: 微信公众号/小程序SubOpenId
在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一。
        :type WxSubOpenId: str
        :param TotalPlatformIncome: 平台应收金额
单位：分，需要注意的是，TotalAmt=TotalPlatformIncome+TotalMchIncome
        :type TotalPlatformIncome: int
        :param TotalMchIncome: 结算应收金额
单位：分，需要注意的是，TotalAmt=TotalPlatformIncome+TotalMchIncome
        :type TotalMchIncome: int
        :param SubOrderList: 子订单列表
格式：子订单号、子应用Id、金额。压缩后最长不可超过32K字节(去除空格，换行，制表符等无意义字符)。
        :type SubOrderList: list of CloudSubOrder
        :param SettleInfo: 结算信息
例如是否需要分账、是否需要支付确认等，
注意：如果子单列表中传入了SettleInfo，在主单中不可再传入SettleInfo字段。
        :type SettleInfo: :class:`tencentcloud.cpdp.v20190820.models.CloudSettleInfo`
        :param AttachmentInfoList: 附加项信息列表
例如溢价信息、抵扣信息、积分信息、补贴信息
通过该字段可以实现渠道方的优惠抵扣补贴等营销功能
注意：当传SubOrderList时，请在子单信息中传附加项信息，不要在主单中传该字段。
        :type AttachmentInfoList: list of CloudAttachmentInfo
        :param PaymentNotifyUrl: 支付通知地址
调用方可通过该字段传入自定义支付通知地址。
        :type PaymentNotifyUrl: str
        :param PayScene: 支付场景
需要结合 RealChannel和Channel字段使用可选值:
wechat-app 微信APP支付方式
wechat-mini 微信小程序支付，示例：当 RealChannel=wechat Channel=wechat PayScene=wechat-mini时，内部会直接以小程序方式调用微信统一下单接口。
        :type PayScene: str
        :param LocaleCode: 语言代码
取值请参考[ISO 639-1代码表](https://zh.wikipedia.org/zh-cn/ISO_639-1%E4%BB%A3%E7%A0%81%E8%A1%A8)
        :type LocaleCode: str
        :param RegionCode: 地区代码
取值请参考[ISO 3166-1二位字母代码表](https://zh.wikipedia.org/zh-cn/ISO_3166-1%E4%BA%8C%E4%BD%8D%E5%AD%97%E6%AF%8D%E4%BB%A3%E7%A0%81#%E6%AD%A3%E5%BC%8F%E5%88%86%E9%85%8D%E4%BB%A3%E7%A0%81)
        :type RegionCode: str
        :param UserClientIp: 用户IP
请求用户的IP地址，特定的渠道或特定的支付方式，此字段为必填
wechat_ecommerce渠道 - h5支付方式，此字段必填。
        :type UserClientIp: str
        :param ChannelOrderIdMode: 渠道订单号生成模式
枚举值。决定请求渠道方时的订单号的生成模式，详情请联系米大师沟通。不指定时默认为由米大师自行生成。
        :type ChannelOrderIdMode: str
        :param GlobalPayTimeInfo: 全局支付时间信息
        :type GlobalPayTimeInfo: :class:`tencentcloud.cpdp.v20190820.models.CloudGlobalPayTimeInfo`
        :param ChannelAppIdPolicy: 渠道应用ID取用方式
USE_APPID 使用渠道应用Id;
USE_SUB_APPID 使用子渠道应用Id;
USE_APPID_AND_SUB_APPID 既使用渠道应用Id也使用子渠道应用ID。
        :type ChannelAppIdPolicy: str
        :param StoreInfo: 门店信息
特定的渠道或特定的支付方式，此字段为必填
wechat_ecommerce渠道 - h5支付方式，此字段必填
        :type StoreInfo: :class:`tencentcloud.cpdp.v20190820.models.CloudStoreInfo`
        :param ClientInfo: 客户端信息
特定的渠道或特定的支付方式，此字段为必填
wechat_ecommerce渠道 - h5支付方式，此字段必填
        :type ClientInfo: :class:`tencentcloud.cpdp.v20190820.models.CloudClientInfo`
        :param ExternalPromptGroupList: 渠道扩展促销列表
可将各个渠道的促销信息放于该列表。
        :type ExternalPromptGroupList: list of CloudExternalPromptGroup
        :param OrderReceiveMode: 收单模式
ORDER_RECEIVE_MODE_COMMON - 普通支付
ORDER_RECEIVE_MODE_COMBINE - 合单支付
ORDER_RECEIVE_MODE_V_COMBINE - 虚拟合单支付
若不传入该字段，则会根据是否传入子单来判断是 普通支付 还是 合单支付
        :type OrderReceiveMode: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.OutTradeNo = None
        self.CurrencyType = None
        self.ProductId = None
        self.ProductName = None
        self.ProductDetail = None
        self.OriginalAmt = None
        self.TotalAmt = None
        self.MidasEnvironment = None
        self.SubAppId = None
        self.RealChannel = None
        self.Channel = None
        self.Metadata = None
        self.Quantity = None
        self.CallbackUrl = None
        self.CancelUrl = None
        self.WxAppId = None
        self.WxSubAppId = None
        self.WxOpenId = None
        self.WxSubOpenId = None
        self.TotalPlatformIncome = None
        self.TotalMchIncome = None
        self.SubOrderList = None
        self.SettleInfo = None
        self.AttachmentInfoList = None
        self.PaymentNotifyUrl = None
        self.PayScene = None
        self.LocaleCode = None
        self.RegionCode = None
        self.UserClientIp = None
        self.ChannelOrderIdMode = None
        self.GlobalPayTimeInfo = None
        self.ChannelAppIdPolicy = None
        self.StoreInfo = None
        self.ClientInfo = None
        self.ExternalPromptGroupList = None
        self.OrderReceiveMode = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.CurrencyType = params.get("CurrencyType")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDetail = params.get("ProductDetail")
        self.OriginalAmt = params.get("OriginalAmt")
        self.TotalAmt = params.get("TotalAmt")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.SubAppId = params.get("SubAppId")
        self.RealChannel = params.get("RealChannel")
        self.Channel = params.get("Channel")
        self.Metadata = params.get("Metadata")
        self.Quantity = params.get("Quantity")
        self.CallbackUrl = params.get("CallbackUrl")
        self.CancelUrl = params.get("CancelUrl")
        self.WxAppId = params.get("WxAppId")
        self.WxSubAppId = params.get("WxSubAppId")
        self.WxOpenId = params.get("WxOpenId")
        self.WxSubOpenId = params.get("WxSubOpenId")
        self.TotalPlatformIncome = params.get("TotalPlatformIncome")
        self.TotalMchIncome = params.get("TotalMchIncome")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = CloudSubOrder()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        if params.get("SettleInfo") is not None:
            self.SettleInfo = CloudSettleInfo()
            self.SettleInfo._deserialize(params.get("SettleInfo"))
        if params.get("AttachmentInfoList") is not None:
            self.AttachmentInfoList = []
            for item in params.get("AttachmentInfoList"):
                obj = CloudAttachmentInfo()
                obj._deserialize(item)
                self.AttachmentInfoList.append(obj)
        self.PaymentNotifyUrl = params.get("PaymentNotifyUrl")
        self.PayScene = params.get("PayScene")
        self.LocaleCode = params.get("LocaleCode")
        self.RegionCode = params.get("RegionCode")
        self.UserClientIp = params.get("UserClientIp")
        self.ChannelOrderIdMode = params.get("ChannelOrderIdMode")
        if params.get("GlobalPayTimeInfo") is not None:
            self.GlobalPayTimeInfo = CloudGlobalPayTimeInfo()
            self.GlobalPayTimeInfo._deserialize(params.get("GlobalPayTimeInfo"))
        self.ChannelAppIdPolicy = params.get("ChannelAppIdPolicy")
        if params.get("StoreInfo") is not None:
            self.StoreInfo = CloudStoreInfo()
            self.StoreInfo._deserialize(params.get("StoreInfo"))
        if params.get("ClientInfo") is not None:
            self.ClientInfo = CloudClientInfo()
            self.ClientInfo._deserialize(params.get("ClientInfo"))
        if params.get("ExternalPromptGroupList") is not None:
            self.ExternalPromptGroupList = []
            for item in params.get("ExternalPromptGroupList"):
                obj = CloudExternalPromptGroup()
                obj._deserialize(item)
                self.ExternalPromptGroupList.append(obj)
        self.OrderReceiveMode = params.get("OrderReceiveMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnifiedCloudOrderResponse(AbstractModel):
    """UnifiedCloudOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param TransactionId: 米大师的交易订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionId: str
        :param OutTradeNo: 开发者的支付订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type OutTradeNo: str
        :param PayInfo: SDK的支付参数。
支付参数透传给米大师SDK（原文透传给SDK即可，不需要解码）
注意：此字段可能返回 null，表示取不到有效值。
        :type PayInfo: str
        :param TotalAmt: 支付金额，单位：分。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalAmt: int
        :param ChannelInfo: 渠道信息，用于拉起渠道支付。j
son字符串，注意此字段仅会在传入正确的PayScene入参时才会有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TransactionId = None
        self.OutTradeNo = None
        self.PayInfo = None
        self.TotalAmt = None
        self.ChannelInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.PayInfo = params.get("PayInfo")
        self.TotalAmt = params.get("TotalAmt")
        self.ChannelInfo = params.get("ChannelInfo")
        self.RequestId = params.get("RequestId")


class UnifiedOrderInSubOrderList(AbstractModel):
    """子订单列表

    """

    def __init__(self):
        r"""
        :param SubMchIncome: 子订单结算应收金额，单位： 分
        :type SubMchIncome: int
        :param PlatformIncome: 子订单平台应收金额，单位：分
        :type PlatformIncome: int
        :param ProductDetail: 子订单商品详情
        :type ProductDetail: str
        :param ProductName: 子订单商品名称
        :type ProductName: str
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOutTradeNo: 子订单号
        :type SubOutTradeNo: str
        :param Amt: 子订单支付金额
        :type Amt: int
        :param Metadata: 发货标识，由业务在调用聚鑫下单接口的 时候下发
        :type Metadata: str
        :param OriginalAmt: 子订单原始金额
        :type OriginalAmt: int
        """
        self.SubMchIncome = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SubAppId = None
        self.SubOutTradeNo = None
        self.Amt = None
        self.Metadata = None
        self.OriginalAmt = None


    def _deserialize(self, params):
        self.SubMchIncome = params.get("SubMchIncome")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.Amt = params.get("Amt")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnifiedOrderRequest(AbstractModel):
    """UnifiedOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param CurrencyType: ISO 货币代码，CNY
        :type CurrencyType: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param OutTradeNo: 支付订单号，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type OutTradeNo: str
        :param ProductDetail: 商品详情，需要URL编码
        :type ProductDetail: str
        :param ProductId: 商品ID，仅支持数字、字母、下划线（_）、横杠字符（-）、点（.）的组合
        :type ProductId: str
        :param ProductName: 商品名称，需要URL编码
        :type ProductName: str
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param UserId: 用户ID，长度不小于5位，仅支持字母和数字的组合
        :type UserId: str
        :param RealChannel: 银行真实渠道.如:bank_pingan
        :type RealChannel: str
        :param OriginalAmt: 原始金额
        :type OriginalAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全密钥计算的签名
        :type MidasSignature: str
        :param CallbackUrl: Web端回调地址
        :type CallbackUrl: str
        :param Channel: 指定支付渠道：  wechat：微信支付  qqwallet：QQ钱包 
 bank：网银支付  只有一个渠道时需要指定
        :type Channel: str
        :param Metadata: 透传字段，支付成功回调透传给应用，用于业务透传自定义内容
        :type Metadata: str
        :param Quantity: 购买数量，不传默认为1
        :type Quantity: int
        :param SubAppId: 聚鑫计费SubAppId，代表子商户
        :type SubAppId: str
        :param SubOrderList: 子订单信息列表，格式：子订单号、子应用ID、金额。 压缩后最长不可超过65535字节(去除空格，换行，制表符等无意义字符)
注：接入银行或其他支付渠道服务商模式下，必传
        :type SubOrderList: list of UnifiedOrderInSubOrderList
        :param TotalMchIncome: 结算应收金额，单位：分
        :type TotalMchIncome: int
        :param TotalPlatformIncome: 平台应收金额，单位：分
        :type TotalPlatformIncome: int
        :param WxOpenId: 微信公众号/小程序支付时为必选，需要传微信下的openid
        :type WxOpenId: str
        :param WxSubOpenId: 在服务商模式下，微信公众号/小程序支付时wx_sub_openid和wx_openid二选一
        :type WxSubOpenId: str
        :param MidasEnvironment: 环境名:
release: 现网环境
sandbox: 沙箱环境
development: 开发环境
缺省: release
        :type MidasEnvironment: str
        :param WxAppId: 微信商户应用ID
        :type WxAppId: str
        :param WxSubAppId: 微信商户子应用ID
        :type WxSubAppId: str
        :param PaymentNotifyUrl: 支付通知地址
        :type PaymentNotifyUrl: str
        """
        self.CurrencyType = None
        self.MidasAppId = None
        self.OutTradeNo = None
        self.ProductDetail = None
        self.ProductId = None
        self.ProductName = None
        self.TotalAmt = None
        self.UserId = None
        self.RealChannel = None
        self.OriginalAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CallbackUrl = None
        self.Channel = None
        self.Metadata = None
        self.Quantity = None
        self.SubAppId = None
        self.SubOrderList = None
        self.TotalMchIncome = None
        self.TotalPlatformIncome = None
        self.WxOpenId = None
        self.WxSubOpenId = None
        self.MidasEnvironment = None
        self.WxAppId = None
        self.WxSubAppId = None
        self.PaymentNotifyUrl = None


    def _deserialize(self, params):
        self.CurrencyType = params.get("CurrencyType")
        self.MidasAppId = params.get("MidasAppId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.TotalAmt = params.get("TotalAmt")
        self.UserId = params.get("UserId")
        self.RealChannel = params.get("RealChannel")
        self.OriginalAmt = params.get("OriginalAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Channel = params.get("Channel")
        self.Metadata = params.get("Metadata")
        self.Quantity = params.get("Quantity")
        self.SubAppId = params.get("SubAppId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = UnifiedOrderInSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.TotalMchIncome = params.get("TotalMchIncome")
        self.TotalPlatformIncome = params.get("TotalPlatformIncome")
        self.WxOpenId = params.get("WxOpenId")
        self.WxSubOpenId = params.get("WxSubOpenId")
        self.MidasEnvironment = params.get("MidasEnvironment")
        self.WxAppId = params.get("WxAppId")
        self.WxSubAppId = params.get("WxSubAppId")
        self.PaymentNotifyUrl = params.get("PaymentNotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnifiedOrderResponse(AbstractModel):
    """UnifiedOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalAmt: 支付金额，单位： 分
        :type TotalAmt: int
        :param OutTradeNo: 应用支付订单号
        :type OutTradeNo: str
        :param PayInfo: 支付参数透传给聚鑫SDK（原文透传给SDK即可，不需要解码）
        :type PayInfo: str
        :param TransactionId: 聚鑫的交易订单
        :type TransactionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalAmt = None
        self.OutTradeNo = None
        self.PayInfo = None
        self.TransactionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAmt = params.get("TotalAmt")
        self.OutTradeNo = params.get("OutTradeNo")
        self.PayInfo = params.get("PayInfo")
        self.TransactionId = params.get("TransactionId")
        self.RequestId = params.get("RequestId")


class UnifiedTlinxOrderRequest(AbstractModel):
    """UnifiedTlinxOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 使用门店OpenId
        :type OpenId: str
        :param OpenKey: 使用门店OpenKey
        :type OpenKey: str
        :param DeveloperNo: 开发者流水号
        :type DeveloperNo: str
        :param PayTag: 支付标签
        :type PayTag: str
        :param TradeAmount: 实际交易金额（以分为单位，没有小数点）
        :type TradeAmount: str
        :param NotifyUrl: 交易结果异步通知url地址
        :type NotifyUrl: str
        :param PayName: 付款方式名称(当PayTag为Diy时，PayName不能为空)
        :type PayName: str
        :param JumpUrl: 公众号支付时，支付成功后跳转url地址
        :type JumpUrl: str
        :param OrderName: 订单名称（描述）
        :type OrderName: str
        :param OriginalAmount: 原始交易金额（以分为单位，没有小数点）
        :type OriginalAmount: str
        :param IgnoreAmount: 抹零金额（以分为单位，没有小数点）
        :type IgnoreAmount: str
        :param DiscountAmount: 折扣金额（以分为单位，没有小数点）
        :type DiscountAmount: str
        :param TradeAccount: 交易帐号（银行卡号）
        :type TradeAccount: str
        :param TradeNo: 交易号（收单机构交易号）
        :type TradeNo: str
        :param AuthCode: 条码支付的授权码（条码抢扫手机扫到的一串数字）
        :type AuthCode: str
        :param Tag: 订单标记，订单附加数据。
        :type Tag: str
        :param Remark: 订单备注
        :type Remark: str
        :param TradeResult: 收单机构原始交易报文，请转换为json
        :type TradeResult: str
        :param Royalty: 0-不分账，1-需分账。为1时标记为待分账订单，待分账订单不会进行清算。不传默认为不分账。
        :type Royalty: str
        :param Jsapi: 小程序支付参数：填默认值 1
        :type Jsapi: str
        :param SubAppId: 小程序支付参数：
当前调起支付的小程序APPID
        :type SubAppId: str
        :param SubOpenId: 小程序支付参数:
用户在子商户appid下的唯一标识。
        :type SubOpenId: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.DeveloperNo = None
        self.PayTag = None
        self.TradeAmount = None
        self.NotifyUrl = None
        self.PayName = None
        self.JumpUrl = None
        self.OrderName = None
        self.OriginalAmount = None
        self.IgnoreAmount = None
        self.DiscountAmount = None
        self.TradeAccount = None
        self.TradeNo = None
        self.AuthCode = None
        self.Tag = None
        self.Remark = None
        self.TradeResult = None
        self.Royalty = None
        self.Jsapi = None
        self.SubAppId = None
        self.SubOpenId = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.DeveloperNo = params.get("DeveloperNo")
        self.PayTag = params.get("PayTag")
        self.TradeAmount = params.get("TradeAmount")
        self.NotifyUrl = params.get("NotifyUrl")
        self.PayName = params.get("PayName")
        self.JumpUrl = params.get("JumpUrl")
        self.OrderName = params.get("OrderName")
        self.OriginalAmount = params.get("OriginalAmount")
        self.IgnoreAmount = params.get("IgnoreAmount")
        self.DiscountAmount = params.get("DiscountAmount")
        self.TradeAccount = params.get("TradeAccount")
        self.TradeNo = params.get("TradeNo")
        self.AuthCode = params.get("AuthCode")
        self.Tag = params.get("Tag")
        self.Remark = params.get("Remark")
        self.TradeResult = params.get("TradeResult")
        self.Royalty = params.get("Royalty")
        self.Jsapi = params.get("Jsapi")
        self.SubAppId = params.get("SubAppId")
        self.SubOpenId = params.get("SubOpenId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnifiedTlinxOrderResponse(AbstractModel):
    """UnifiedTlinxOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码，0表示成功，其他表示失败。
        :type ErrCode: str
        :param Result: 统一下单响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.PayOrderResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = PayOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UploadExternalAnchorInfoRequest(AbstractModel):
    """UploadExternalAnchorInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param AnchorId: 主播Id
        :type AnchorId: str
        :param IdCardFront: 身份证正面图片下载链接
        :type IdCardFront: str
        :param IdCardReverse: 身份证反面图片下载链接
        :type IdCardReverse: str
        """
        self.AnchorId = None
        self.IdCardFront = None
        self.IdCardReverse = None


    def _deserialize(self, params):
        self.AnchorId = params.get("AnchorId")
        self.IdCardFront = params.get("IdCardFront")
        self.IdCardReverse = params.get("IdCardReverse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadExternalAnchorInfoResponse(AbstractModel):
    """UploadExternalAnchorInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。响应成功："SUCCESS"，其他为不成功。
        :type ErrCode: str
        :param ErrMessage: 响应消息。
        :type ErrMessage: str
        :param Result: 该字段为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UploadFileRequest(AbstractModel):
    """UploadFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param FileName: 文件名
        :type FileName: str
        :param FileType: 文件类型
__IdCard__:身份证
__IdCardCheck__:身份证加验证(只支持人像面)
        :type FileType: str
        :param FileUrl: 文件链接
__FileUrl和FileContent二选一__
        :type FileUrl: str
        :param FileContent: 文件内容，Base64编码
__FileUrl和FileContent二选一__
        :type FileContent: str
        :param FileExtendInfo: 文件扩展信息
        :type FileExtendInfo: list of AnchorExtendInfo
        """
        self.FileName = None
        self.FileType = None
        self.FileUrl = None
        self.FileContent = None
        self.FileExtendInfo = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileUrl = params.get("FileUrl")
        self.FileContent = params.get("FileContent")
        if params.get("FileExtendInfo") is not None:
            self.FileExtendInfo = []
            for item in params.get("FileExtendInfo"):
                obj = AnchorExtendInfo()
                obj._deserialize(item)
                self.FileExtendInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileResponse(AbstractModel):
    """UploadFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileId: 文件ID
        :type FileId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.RequestId = params.get("RequestId")


class UploadFileResult(AbstractModel):
    """上传文件响应对象

    """

    def __init__(self):
        r"""
        :param Storage: 存储区域（0私密区，1公共区），请严格按文件要求，上传到不同的区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Storage: str
        :param FilePath: 文件路径
注意：此字段可能返回 null，表示取不到有效值。
        :type FilePath: str
        """
        self.Storage = None
        self.FilePath = None


    def _deserialize(self, params):
        self.Storage = params.get("Storage")
        self.FilePath = params.get("FilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadOpenBankSubMerchantCredentialRequest(AbstractModel):
    """UploadOpenBankSubMerchantCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param ChannelMerchantId: 渠道商户ID。
        :type ChannelMerchantId: str
        :param ChannelSubMerchantId: 渠道子商户ID。
        :type ChannelSubMerchantId: str
        :param ChannelName: 渠道名称。详见附录-枚举类型-ChannelName。
        :type ChannelName: str
        :param OutApplyId: 外部序列进件号。
        :type OutApplyId: str
        :param CredentialType: 资质类型，详见附录-枚举类型-CredentialType。
        :type CredentialType: str
        :param FileType: 文件类型。
合利宝渠道，文件类型为PNG/JPG格式。
        :type FileType: str
        :param PaymentMethod: 支付方式。
合利宝渠道不需要传。
        :type PaymentMethod: str
        :param CredentialContent: 资质文件内容。Base64编码，资质文件内容和链接二选一。
合利宝渠道，文件限制大小5M以内。
        :type CredentialContent: str
        :param CredentialUrl: 资质文件链接。资质文件内容和链接二选一。
合利宝渠道，文件限制大小5M以内。
        :type CredentialUrl: str
        :param Environment: 环境类型。
__release__:生产环境
__sandbox__:沙箱环境
_不填默认为生产环境_
        :type Environment: str
        """
        self.ChannelMerchantId = None
        self.ChannelSubMerchantId = None
        self.ChannelName = None
        self.OutApplyId = None
        self.CredentialType = None
        self.FileType = None
        self.PaymentMethod = None
        self.CredentialContent = None
        self.CredentialUrl = None
        self.Environment = None


    def _deserialize(self, params):
        self.ChannelMerchantId = params.get("ChannelMerchantId")
        self.ChannelSubMerchantId = params.get("ChannelSubMerchantId")
        self.ChannelName = params.get("ChannelName")
        self.OutApplyId = params.get("OutApplyId")
        self.CredentialType = params.get("CredentialType")
        self.FileType = params.get("FileType")
        self.PaymentMethod = params.get("PaymentMethod")
        self.CredentialContent = params.get("CredentialContent")
        self.CredentialUrl = params.get("CredentialUrl")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadOpenBankSubMerchantCredentialResponse(AbstractModel):
    """UploadOpenBankSubMerchantCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrCode: 错误码。
        :type ErrCode: str
        :param ErrMessage: 错误消息。
        :type ErrMessage: str
        :param Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.UploadOpenBankSubMerchantCredentialResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrCode = None
        self.ErrMessage = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMessage = params.get("ErrMessage")
        if params.get("Result") is not None:
            self.Result = UploadOpenBankSubMerchantCredentialResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UploadOpenBankSubMerchantCredentialResult(AbstractModel):
    """上传子商户资质文件返回值

    """

    def __init__(self):
        r"""
        :param UploadStatus: 上传状态
SUCCESS：上传成功
FAILED：上传失败
PROCESSING:上传中
        :type UploadStatus: str
        :param UploadMessage: 上传描述
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadMessage: str
        :param ChannelApplyId: 渠道上传流水号
        :type ChannelApplyId: str
        """
        self.UploadStatus = None
        self.UploadMessage = None
        self.ChannelApplyId = None


    def _deserialize(self, params):
        self.UploadStatus = params.get("UploadStatus")
        self.UploadMessage = params.get("UploadMessage")
        self.ChannelApplyId = params.get("ChannelApplyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadOrgFileRequest(AbstractModel):
    """UploadOrgFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param Storage: 存储区域（0私密区，1公共区），请严格按文件要求，上传到不同的区域
        :type Storage: str
        :param FileMd5: 文件的md5值（为防止平台多次上传重复文件，文件名为文件md5,且不会覆盖，重复上传返回第一次上传成功的文件路径）
        :type FileMd5: str
        :param FileContent: 文件内容（先将图片转换成二进制，再进行base64加密）
        :type FileContent: str
        :param FileExtension: 文件扩展名（png,jpg,gif）
        :type FileExtension: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.Storage = None
        self.FileMd5 = None
        self.FileContent = None
        self.FileExtension = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.Storage = params.get("Storage")
        self.FileMd5 = params.get("FileMd5")
        self.FileContent = params.get("FileContent")
        self.FileExtension = params.get("FileExtension")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadOrgFileResponse(AbstractModel):
    """UploadOrgFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 上传机构文件响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.UploadFileResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = UploadFileResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UploadTaxListRequest(AbstractModel):
    """UploadTaxList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Channel: 平台渠道
        :type Channel: int
        :param BeginMonth: 起始月份，YYYY-MM
        :type BeginMonth: str
        :param EndMonth: 结束月份。如果只上传一个月，结束月份等于起始月份
        :type EndMonth: str
        :param FileUrl: 完税列表下载地址
        :type FileUrl: str
        """
        self.Channel = None
        self.BeginMonth = None
        self.EndMonth = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")
        self.BeginMonth = params.get("BeginMonth")
        self.EndMonth = params.get("EndMonth")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadTaxListResponse(AbstractModel):
    """UploadTaxList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaxId: 完税ID
        :type TaxId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaxId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaxId = params.get("TaxId")
        self.RequestId = params.get("RequestId")


class UploadTaxPaymentRequest(AbstractModel):
    """UploadTaxPayment请求参数结构体

    """

    def __init__(self):
        r"""
        :param Channel: 平台渠道
        :type Channel: int
        :param TaxId: 完税ID
        :type TaxId: str
        :param FileUrl: 完税列表下载地址
        :type FileUrl: str
        """
        self.Channel = None
        self.TaxId = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")
        self.TaxId = params.get("TaxId")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadTaxPaymentResponse(AbstractModel):
    """UploadTaxPayment返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ViewContractRequest(AbstractModel):
    """ViewContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param OutContractId: 外部合同主键编号（ContractId或OutContractId必须传一个）
        :type OutContractId: str
        :param ContractId: 合同主键（ContractId或OutContractId必须传一个）
        :type ContractId: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OutContractId = None
        self.ContractId = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OutContractId = params.get("OutContractId")
        self.ContractId = params.get("ContractId")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewContractResponse(AbstractModel):
    """ViewContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 合同明细响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ViewContractResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = ViewContractResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ViewContractResult(AbstractModel):
    """合同明细响应对象

    """

    def __init__(self):
        r"""
        :param PaymentTag: 支付标签（唯一性）
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentTag: str
        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param AgentNo: 机构编号
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentNo: str
        :param ContractOptionFour: 合同选项值4
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionFour: str
        :param ContractOptionTwo: 合同选项值2
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionTwo: str
        :param Status: 合同状态（0未审核，1已审核，2审核未通过，3待审核，4已删除，5初审通过）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param PaymentId: 支付方式编号
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentId: str
        :param Fee: 商户签约扣率
注意：此字段可能返回 null，表示取不到有效值。
        :type Fee: str
        :param PaymentOptionFive: 合同选项名称5
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionFive: str
        :param OutContractId: 机构合同主键
注意：此字段可能返回 null，表示取不到有效值。
        :type OutContractId: str
        :param ChannelExtJson: 不同的支付方式对于进件有不同的个性化需求，支付方式字段都是以双下划写开头的字段名称，请以支付方式规定的格式传值
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelExtJson: str
        :param ContractOptionFive: 合同选项值5
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionFive: str
        :param Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param StartDate: 生效日期
注意：此字段可能返回 null，表示取不到有效值。
        :type StartDate: str
        :param Address: 详细地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param EndDate: 过期日期
注意：此字段可能返回 null，表示取不到有效值。
        :type EndDate: str
        :param ContractOptionSix: 合同选项值6
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionSix: str
        :param PaymentOptionSeven: 合同选项名称7
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionSeven: str
        :param PictureTwo: 合同照片补充【私密区】
注意：此字段可能返回 null，表示取不到有效值。
        :type PictureTwo: str
        :param MerchantNo: 商户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        :param AgentName: 机构名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        :param ContractOptionOther: 合同选项值8
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionOther: str
        :param ContractOptionThree: 合同选项值3
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionThree: str
        :param Country: 县/区
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param ShopCount: 合同关联的门店数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopCount: str
        :param PaymentOptionThree: 合同选项名称3
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionThree: str
        :param PaymentClassificationName: 支付方式行业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentClassificationName: str
        :param ContractOptionSeven: 合同选项值7
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionSeven: str
        :param PaymentOptionFour: 合同选项名称4
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionFour: str
        :param PaymentClassificationLimit: 商户签约扣率封顶值（分为单位）
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentClassificationLimit: str
        :param Remark: 审核备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param PaymentOptionSix: 合同选项名称6
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionSix: str
        :param MerchantName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param ContractOptionOne: 合同选项值1
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionOne: str
        :param PaymentOptionOther: 合同选项名称8
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionOther: str
        :param PaymentOptionTwo: 合同选项名称2
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionTwo: str
        :param PaymentOptionOne: 合同选项名称1
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionOne: str
        :param UpdateTime: 更新时间（yyyy-mm-dd hh:ii:ss）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ContactTelephone: 联系人电话
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactTelephone: str
        :param Contact: 联系人
注意：此字段可能返回 null，表示取不到有效值。
        :type Contact: str
        :param SignDate: 签约日期
注意：此字段可能返回 null，表示取不到有效值。
        :type SignDate: str
        :param PaymentOptionNine: 合同选项名称9
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionNine: str
        :param PaymentName: 付款方式名称
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentName: str
        :param PaymentInternalName: 付款方式名称（内部名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentInternalName: str
        :param ContractOptionTen: 合同选项值10
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionTen: str
        :param Code: 合同编号
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param PictureOne: 合同照片【私密区】
注意：此字段可能返回 null，表示取不到有效值。
        :type PictureOne: str
        :param SignMan: 签约人
注意：此字段可能返回 null，表示取不到有效值。
        :type SignMan: str
        :param ChannelNo: 渠道号
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelNo: str
        :param AddTime: 添加时间（yyyy-mm-dd hh:ii:ss）
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param AutoSign: 是否自动续签（1是，0否）
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSign: str
        :param ContractOptionNine: 合同选项值9
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractOptionNine: str
        :param CityId: 城市编码
注意：此字段可能返回 null，表示取不到有效值。
        :type CityId: str
        :param PaymentType: 交易类型（多个以小写逗号分开，0现金，1刷卡，2主扫，3被扫，4JSPAY，5预授权）
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentType: str
        :param PaymentClassificationId: 支付方式行业编号
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentClassificationId: str
        :param BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param PaymentOptionTen: 合同选项名称10
注意：此字段可能返回 null，表示取不到有效值。
        :type PaymentOptionTen: str
        :param ContractId: 合同主键
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractId: str
        """
        self.PaymentTag = None
        self.City = None
        self.AgentNo = None
        self.ContractOptionFour = None
        self.ContractOptionTwo = None
        self.Status = None
        self.PaymentId = None
        self.Fee = None
        self.PaymentOptionFive = None
        self.OutContractId = None
        self.ChannelExtJson = None
        self.ContractOptionFive = None
        self.Province = None
        self.StartDate = None
        self.Address = None
        self.EndDate = None
        self.ContractOptionSix = None
        self.PaymentOptionSeven = None
        self.PictureTwo = None
        self.MerchantNo = None
        self.AgentName = None
        self.ContractOptionOther = None
        self.ContractOptionThree = None
        self.Country = None
        self.ShopCount = None
        self.PaymentOptionThree = None
        self.PaymentClassificationName = None
        self.ContractOptionSeven = None
        self.PaymentOptionFour = None
        self.PaymentClassificationLimit = None
        self.Remark = None
        self.PaymentOptionSix = None
        self.MerchantName = None
        self.ContractOptionOne = None
        self.PaymentOptionOther = None
        self.PaymentOptionTwo = None
        self.PaymentOptionOne = None
        self.UpdateTime = None
        self.ContactTelephone = None
        self.Contact = None
        self.SignDate = None
        self.PaymentOptionNine = None
        self.PaymentName = None
        self.PaymentInternalName = None
        self.ContractOptionTen = None
        self.Code = None
        self.PictureOne = None
        self.SignMan = None
        self.ChannelNo = None
        self.AddTime = None
        self.AutoSign = None
        self.ContractOptionNine = None
        self.CityId = None
        self.PaymentType = None
        self.PaymentClassificationId = None
        self.BrandName = None
        self.PaymentOptionTen = None
        self.ContractId = None


    def _deserialize(self, params):
        self.PaymentTag = params.get("PaymentTag")
        self.City = params.get("City")
        self.AgentNo = params.get("AgentNo")
        self.ContractOptionFour = params.get("ContractOptionFour")
        self.ContractOptionTwo = params.get("ContractOptionTwo")
        self.Status = params.get("Status")
        self.PaymentId = params.get("PaymentId")
        self.Fee = params.get("Fee")
        self.PaymentOptionFive = params.get("PaymentOptionFive")
        self.OutContractId = params.get("OutContractId")
        self.ChannelExtJson = params.get("ChannelExtJson")
        self.ContractOptionFive = params.get("ContractOptionFive")
        self.Province = params.get("Province")
        self.StartDate = params.get("StartDate")
        self.Address = params.get("Address")
        self.EndDate = params.get("EndDate")
        self.ContractOptionSix = params.get("ContractOptionSix")
        self.PaymentOptionSeven = params.get("PaymentOptionSeven")
        self.PictureTwo = params.get("PictureTwo")
        self.MerchantNo = params.get("MerchantNo")
        self.AgentName = params.get("AgentName")
        self.ContractOptionOther = params.get("ContractOptionOther")
        self.ContractOptionThree = params.get("ContractOptionThree")
        self.Country = params.get("Country")
        self.ShopCount = params.get("ShopCount")
        self.PaymentOptionThree = params.get("PaymentOptionThree")
        self.PaymentClassificationName = params.get("PaymentClassificationName")
        self.ContractOptionSeven = params.get("ContractOptionSeven")
        self.PaymentOptionFour = params.get("PaymentOptionFour")
        self.PaymentClassificationLimit = params.get("PaymentClassificationLimit")
        self.Remark = params.get("Remark")
        self.PaymentOptionSix = params.get("PaymentOptionSix")
        self.MerchantName = params.get("MerchantName")
        self.ContractOptionOne = params.get("ContractOptionOne")
        self.PaymentOptionOther = params.get("PaymentOptionOther")
        self.PaymentOptionTwo = params.get("PaymentOptionTwo")
        self.PaymentOptionOne = params.get("PaymentOptionOne")
        self.UpdateTime = params.get("UpdateTime")
        self.ContactTelephone = params.get("ContactTelephone")
        self.Contact = params.get("Contact")
        self.SignDate = params.get("SignDate")
        self.PaymentOptionNine = params.get("PaymentOptionNine")
        self.PaymentName = params.get("PaymentName")
        self.PaymentInternalName = params.get("PaymentInternalName")
        self.ContractOptionTen = params.get("ContractOptionTen")
        self.Code = params.get("Code")
        self.PictureOne = params.get("PictureOne")
        self.SignMan = params.get("SignMan")
        self.ChannelNo = params.get("ChannelNo")
        self.AddTime = params.get("AddTime")
        self.AutoSign = params.get("AutoSign")
        self.ContractOptionNine = params.get("ContractOptionNine")
        self.CityId = params.get("CityId")
        self.PaymentType = params.get("PaymentType")
        self.PaymentClassificationId = params.get("PaymentClassificationId")
        self.BrandName = params.get("BrandName")
        self.PaymentOptionTen = params.get("PaymentOptionTen")
        self.ContractId = params.get("ContractId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewMerchantRequest(AbstractModel):
    """ViewMerchant请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param OutMerchantId: 外部商户主键编号（MerchantNo或OutMerchantId必须传一个）
        :type OutMerchantId: str
        :param MerchantNo: 商户编号（MerchantNo或OutMerchantId必须传一个）
        :type MerchantNo: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OutMerchantId = None
        self.MerchantNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OutMerchantId = params.get("OutMerchantId")
        self.MerchantNo = params.get("MerchantNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewMerchantResponse(AbstractModel):
    """ViewMerchant返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 商户明细响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ViewMerchantResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = ViewMerchantResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ViewMerchantResult(AbstractModel):
    """商户明细响应对象

    """

    def __init__(self):
        r"""
        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param TaxCollectionPicture: 税务登记证图片【私密区】
注意：此字段可能返回 null，表示取不到有效值。
        :type TaxCollectionPicture: str
        :param BossIdNo: 法人证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type BossIdNo: str
        :param AccountIdNo: 法人亲属证件号码
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountIdNo: str
        :param OtherPictureThree: 其他资料3
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherPictureThree: str
        :param AccountIdType: 法人亲属证件类型（1居民身份证,2临时居民身份证,3居民户口簿,4护照,5港澳居民来往内地通行证,6回乡证,7军人证,8武警身份证,9其他法定文件）结算账户人身份为法人亲属时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountIdType: str
        :param Status: 商户状态（0未审核，1已审核，2审核未通过，3待审核，4已删除，5初审通过）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param BusinessLicensePicture: 营业执照图片【私密区】（系统返回的图片路径）
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessLicensePicture: str
        :param BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param BossPositive: 法人身份证正面【私密区】（系统返回的图片路径）
注意：此字段可能返回 null，表示取不到有效值。
        :type BossPositive: str
        :param AppCount: 开通应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AppCount: str
        :param BossBack: 法人身份证背面【私密区】（系统返回的图片路径）
注意：此字段可能返回 null，表示取不到有效值。
        :type BossBack: str
        :param OrganizationCodePicture: 组织机构代码证图片【私密区】
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCodePicture: str
        :param BusinessLicenseEndDate: 营业执照过期时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessLicenseEndDate: str
        :param OrganizationCodeNo: 组织机构代码证号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCodeNo: str
        :param AgentNo: 机构编号
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentNo: str
        :param Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param BossStartDate: 法人证件生效时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type BossStartDate: str
        :param UpdateTime: 更新时间（yyyy-mm-dd hh:ii:ss）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param BankNo: 清算联行号，开户行行号
注意：此字段可能返回 null，表示取不到有效值。
        :type BankNo: str
        :param TaxCollectionStartDate: 税务登记证生效时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type TaxCollectionStartDate: str
        :param BusinessLicenseStartDate: 营业执照生效时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessLicenseStartDate: str
        :param AccountManagerId: 客户经理用户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountManagerId: str
        :param ClassificationIds: 分类编号(多个以小写逗号分开)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationIds: str
        :param BusinessLicenseType: 营业执照类型（1三证合一，2非三证合一）
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessLicenseType: str
        :param BossEndDate: 法人证件过期时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type BossEndDate: str
        :param BusinessLicenseNo: 营业执照编号（系统有唯一性校验）
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessLicenseNo: str
        :param AgentName: 机构名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        :param Intro: 商户简介
注意：此字段可能返回 null，表示取不到有效值。
        :type Intro: str
        :param BossIdType: 法人证件类型（1居民身份证,2临时居民身份证,3居民户口簿,4护照,5港澳居民来往内地通行证,6回乡证,7军人证,8武警身份证,9其他法定文件）
注意：此字段可能返回 null，表示取不到有效值。
        :type BossIdType: str
        :param AddTime: 添加时间（yyyy-mm-dd hh:ii:ss）
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param ShopCount: 门店数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopCount: str
        :param AccountBoss: 结算账户人身份（1法人，2法人亲属），结算帐户为对私时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountBoss: str
        :param ClassificationNames: 分类名称(多个以小写逗号分开)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationNames: str
        :param BossTelephone: 法人电话
注意：此字段可能返回 null，表示取不到有效值。
        :type BossTelephone: str
        :param AccountManagerName: 客户经理姓名，必须为系统后台的管理员真实姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountManagerName: str
        :param TerminalCount: 终端数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminalCount: str
        :param Remark: 审核备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param FinancialContact: 财务联系人
注意：此字段可能返回 null，表示取不到有效值。
        :type FinancialContact: str
        :param MerchantName: 商户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param BossSex: 法人性别（1男，2女）
注意：此字段可能返回 null，表示取不到有效值。
        :type BossSex: str
        :param MerchantNo: 商户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        :param BossAddress: 法人住址
注意：此字段可能返回 null，表示取不到有效值。
        :type BossAddress: str
        :param Country: 县/区
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param Address: 详细地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param BossJob: 法人职业
注意：此字段可能返回 null，表示取不到有效值。
        :type BossJob: str
        :param LicencePicture: 许可证图片【私密区】
注意：此字段可能返回 null，表示取不到有效值。
        :type LicencePicture: str
        :param OrganizationCodeEndDate: 组织机构代码证过期时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCodeEndDate: str
        :param OpenHours: 营业时间，多个以小写逗号分开(9:00-12:00,13:00-18:00)
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenHours: str
        :param OtherPictureTwo: 其他资料2
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherPictureTwo: str
        :param OtherPictureOne: 其他资料1
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherPictureOne: str
        :param AccountName: 银行户名
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param ContractCount: 合同数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ContractCount: str
        :param LicencePictureTwo: 授权文件【私密区】（当结算帐户身份为法人亲属时必传）
注意：此字段可能返回 null，表示取不到有效值。
        :type LicencePictureTwo: str
        :param AccountNo: 银行账号
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountNo: str
        :param BossEmail: 法人邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type BossEmail: str
        :param AccountType: 结算账户类型（2对私，1对公）
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountType: str
        :param TaxCollectionEndDate: 税务登记证过期时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type TaxCollectionEndDate: str
        :param BankName: 开户行名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BankName: str
        :param Telephone: 联系电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Telephone: str
        :param OutMerchantId: 外部商户主键编号
注意：此字段可能返回 null，表示取不到有效值。
        :type OutMerchantId: str
        :param CityId: 城市编码
注意：此字段可能返回 null，表示取不到有效值。
        :type CityId: str
        :param BossIdCount: 法人证件国别/地区（中国CHN，香港HKG，澳门MAC，台湾CTN）
注意：此字段可能返回 null，表示取不到有效值。
        :type BossIdCount: str
        :param Tag: 商户标记，自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: str
        :param FinancialTelephone: 财务联系人电话
注意：此字段可能返回 null，表示取不到有效值。
        :type FinancialTelephone: str
        :param BossName: 法人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type BossName: str
        :param OrganizationCodeStartDate: 组织机构代码证生效时间（yyyy-mm-dd）
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCodeStartDate: str
        :param Logo: 商户logo【公共区】
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param OtherPictureFour: 其他资料4
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherPictureFour: str
        :param TaxCollectionNo: 税务登记证号
注意：此字段可能返回 null，表示取不到有效值。
        :type TaxCollectionNo: str
        """
        self.City = None
        self.TaxCollectionPicture = None
        self.BossIdNo = None
        self.AccountIdNo = None
        self.OtherPictureThree = None
        self.AccountIdType = None
        self.Status = None
        self.BusinessLicensePicture = None
        self.BrandName = None
        self.BossPositive = None
        self.AppCount = None
        self.BossBack = None
        self.OrganizationCodePicture = None
        self.BusinessLicenseEndDate = None
        self.OrganizationCodeNo = None
        self.AgentNo = None
        self.Province = None
        self.BossStartDate = None
        self.UpdateTime = None
        self.BankNo = None
        self.TaxCollectionStartDate = None
        self.BusinessLicenseStartDate = None
        self.AccountManagerId = None
        self.ClassificationIds = None
        self.BusinessLicenseType = None
        self.BossEndDate = None
        self.BusinessLicenseNo = None
        self.AgentName = None
        self.Intro = None
        self.BossIdType = None
        self.AddTime = None
        self.ShopCount = None
        self.AccountBoss = None
        self.ClassificationNames = None
        self.BossTelephone = None
        self.AccountManagerName = None
        self.TerminalCount = None
        self.Remark = None
        self.FinancialContact = None
        self.MerchantName = None
        self.BossSex = None
        self.MerchantNo = None
        self.BossAddress = None
        self.Country = None
        self.Address = None
        self.BossJob = None
        self.LicencePicture = None
        self.OrganizationCodeEndDate = None
        self.OpenHours = None
        self.OtherPictureTwo = None
        self.OtherPictureOne = None
        self.AccountName = None
        self.ContractCount = None
        self.LicencePictureTwo = None
        self.AccountNo = None
        self.BossEmail = None
        self.AccountType = None
        self.TaxCollectionEndDate = None
        self.BankName = None
        self.Telephone = None
        self.OutMerchantId = None
        self.CityId = None
        self.BossIdCount = None
        self.Tag = None
        self.FinancialTelephone = None
        self.BossName = None
        self.OrganizationCodeStartDate = None
        self.Logo = None
        self.OtherPictureFour = None
        self.TaxCollectionNo = None


    def _deserialize(self, params):
        self.City = params.get("City")
        self.TaxCollectionPicture = params.get("TaxCollectionPicture")
        self.BossIdNo = params.get("BossIdNo")
        self.AccountIdNo = params.get("AccountIdNo")
        self.OtherPictureThree = params.get("OtherPictureThree")
        self.AccountIdType = params.get("AccountIdType")
        self.Status = params.get("Status")
        self.BusinessLicensePicture = params.get("BusinessLicensePicture")
        self.BrandName = params.get("BrandName")
        self.BossPositive = params.get("BossPositive")
        self.AppCount = params.get("AppCount")
        self.BossBack = params.get("BossBack")
        self.OrganizationCodePicture = params.get("OrganizationCodePicture")
        self.BusinessLicenseEndDate = params.get("BusinessLicenseEndDate")
        self.OrganizationCodeNo = params.get("OrganizationCodeNo")
        self.AgentNo = params.get("AgentNo")
        self.Province = params.get("Province")
        self.BossStartDate = params.get("BossStartDate")
        self.UpdateTime = params.get("UpdateTime")
        self.BankNo = params.get("BankNo")
        self.TaxCollectionStartDate = params.get("TaxCollectionStartDate")
        self.BusinessLicenseStartDate = params.get("BusinessLicenseStartDate")
        self.AccountManagerId = params.get("AccountManagerId")
        self.ClassificationIds = params.get("ClassificationIds")
        self.BusinessLicenseType = params.get("BusinessLicenseType")
        self.BossEndDate = params.get("BossEndDate")
        self.BusinessLicenseNo = params.get("BusinessLicenseNo")
        self.AgentName = params.get("AgentName")
        self.Intro = params.get("Intro")
        self.BossIdType = params.get("BossIdType")
        self.AddTime = params.get("AddTime")
        self.ShopCount = params.get("ShopCount")
        self.AccountBoss = params.get("AccountBoss")
        self.ClassificationNames = params.get("ClassificationNames")
        self.BossTelephone = params.get("BossTelephone")
        self.AccountManagerName = params.get("AccountManagerName")
        self.TerminalCount = params.get("TerminalCount")
        self.Remark = params.get("Remark")
        self.FinancialContact = params.get("FinancialContact")
        self.MerchantName = params.get("MerchantName")
        self.BossSex = params.get("BossSex")
        self.MerchantNo = params.get("MerchantNo")
        self.BossAddress = params.get("BossAddress")
        self.Country = params.get("Country")
        self.Address = params.get("Address")
        self.BossJob = params.get("BossJob")
        self.LicencePicture = params.get("LicencePicture")
        self.OrganizationCodeEndDate = params.get("OrganizationCodeEndDate")
        self.OpenHours = params.get("OpenHours")
        self.OtherPictureTwo = params.get("OtherPictureTwo")
        self.OtherPictureOne = params.get("OtherPictureOne")
        self.AccountName = params.get("AccountName")
        self.ContractCount = params.get("ContractCount")
        self.LicencePictureTwo = params.get("LicencePictureTwo")
        self.AccountNo = params.get("AccountNo")
        self.BossEmail = params.get("BossEmail")
        self.AccountType = params.get("AccountType")
        self.TaxCollectionEndDate = params.get("TaxCollectionEndDate")
        self.BankName = params.get("BankName")
        self.Telephone = params.get("Telephone")
        self.OutMerchantId = params.get("OutMerchantId")
        self.CityId = params.get("CityId")
        self.BossIdCount = params.get("BossIdCount")
        self.Tag = params.get("Tag")
        self.FinancialTelephone = params.get("FinancialTelephone")
        self.BossName = params.get("BossName")
        self.OrganizationCodeStartDate = params.get("OrganizationCodeStartDate")
        self.Logo = params.get("Logo")
        self.OtherPictureFour = params.get("OtherPictureFour")
        self.TaxCollectionNo = params.get("TaxCollectionNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewShopRequest(AbstractModel):
    """ViewShop请求参数结构体

    """

    def __init__(self):
        r"""
        :param OpenId: 收单系统分配的开放ID
        :type OpenId: str
        :param OpenKey: 收单系统分配的密钥
        :type OpenKey: str
        :param OutShopId: 外部商户主键编号（ShopNo或OutShopId必须传一个）
        :type OutShopId: str
        :param ShopNo: 门店编号（ShopNo或OutShopId必须传一个）
        :type ShopNo: str
        :param Profile: 沙箱环境填sandbox，正式环境不填
        :type Profile: str
        """
        self.OpenId = None
        self.OpenKey = None
        self.OutShopId = None
        self.ShopNo = None
        self.Profile = None


    def _deserialize(self, params):
        self.OpenId = params.get("OpenId")
        self.OpenKey = params.get("OpenKey")
        self.OutShopId = params.get("OutShopId")
        self.ShopNo = params.get("ShopNo")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewShopResponse(AbstractModel):
    """ViewShop返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrMessage: 业务系统返回消息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMessage: str
        :param ErrCode: 业务系统返回码
        :type ErrCode: str
        :param Result: 门店明细响应对象
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ViewShopResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrMessage = None
        self.ErrCode = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMessage = params.get("ErrMessage")
        self.ErrCode = params.get("ErrCode")
        if params.get("Result") is not None:
            self.Result = ViewShopResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ViewShopResult(AbstractModel):
    """门店明细响应对象

    """

    def __init__(self):
        r"""
        :param City: 城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param ShopName: 门店简称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopName: str
        :param Latitude: 百度地图纬度
注意：此字段可能返回 null，表示取不到有效值。
        :type Latitude: str
        :param BrandName: 品牌名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BrandName: str
        :param AppCount: 开通应用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type AppCount: str
        :param ContactTelephone: 负责人手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactTelephone: str
        :param MerchantName: 商户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantName: str
        :param Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param County: 县/区
注意：此字段可能返回 null，表示取不到有效值。
        :type County: str
        :param UpdateTime: 更新时间（yyyy-mm-dd hh:ii:ss）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param TerminalCount: 终端数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TerminalCount: str
        :param PictureTwo: 收银台图片【公共区】
注意：此字段可能返回 null，表示取不到有效值。
        :type PictureTwo: str
        :param LatitudeTwo: 高德地图纬度
注意：此字段可能返回 null，表示取不到有效值。
        :type LatitudeTwo: str
        :param AgentName: 机构名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentName: str
        :param PictureFour: 其他照片【公共区】
注意：此字段可能返回 null，表示取不到有效值。
        :type PictureFour: str
        :param LongitudeTwo: 高德地图经度
注意：此字段可能返回 null，表示取不到有效值。
        :type LongitudeTwo: str
        :param Status: 门店状态（0未审核，1已审核，2审核未通过，3待审核，4已删除，5初审通过）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Remark: 审核备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param AgentNo: 机构编号
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentNo: str
        :param MerchantNo: 商户编号
注意：此字段可能返回 null，表示取不到有效值。
        :type MerchantNo: str
        :param AddTime: 添加时间（yyyy-mm-dd hh:ii:ss）
注意：此字段可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param Address: 详细地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Address: str
        :param Longitude: 百度地图经度
注意：此字段可能返回 null，表示取不到有效值。
        :type Longitude: str
        :param ShopNo: 门店编号
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopNo: str
        :param ShopFullName: 门店全称
注意：此字段可能返回 null，表示取不到有效值。
        :type ShopFullName: str
        :param Contact: 门店负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type Contact: str
        :param PictureThree: 店内环境图片【公共区】
注意：此字段可能返回 null，表示取不到有效值。
        :type PictureThree: str
        :param PictureOne: 整体门面（含招牌）图片【公共区】
注意：此字段可能返回 null，表示取不到有效值。
        :type PictureOne: str
        :param Telephone: 门店电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Telephone: str
        :param OutShopId: 机构门店主键
注意：此字段可能返回 null，表示取不到有效值。
        :type OutShopId: str
        :param CityId: 城市编码
注意：此字段可能返回 null，表示取不到有效值。
        :type CityId: str
        """
        self.City = None
        self.ShopName = None
        self.Latitude = None
        self.BrandName = None
        self.AppCount = None
        self.ContactTelephone = None
        self.MerchantName = None
        self.Province = None
        self.County = None
        self.UpdateTime = None
        self.TerminalCount = None
        self.PictureTwo = None
        self.LatitudeTwo = None
        self.AgentName = None
        self.PictureFour = None
        self.LongitudeTwo = None
        self.Status = None
        self.Remark = None
        self.AgentNo = None
        self.MerchantNo = None
        self.AddTime = None
        self.Address = None
        self.Longitude = None
        self.ShopNo = None
        self.ShopFullName = None
        self.Contact = None
        self.PictureThree = None
        self.PictureOne = None
        self.Telephone = None
        self.OutShopId = None
        self.CityId = None


    def _deserialize(self, params):
        self.City = params.get("City")
        self.ShopName = params.get("ShopName")
        self.Latitude = params.get("Latitude")
        self.BrandName = params.get("BrandName")
        self.AppCount = params.get("AppCount")
        self.ContactTelephone = params.get("ContactTelephone")
        self.MerchantName = params.get("MerchantName")
        self.Province = params.get("Province")
        self.County = params.get("County")
        self.UpdateTime = params.get("UpdateTime")
        self.TerminalCount = params.get("TerminalCount")
        self.PictureTwo = params.get("PictureTwo")
        self.LatitudeTwo = params.get("LatitudeTwo")
        self.AgentName = params.get("AgentName")
        self.PictureFour = params.get("PictureFour")
        self.LongitudeTwo = params.get("LongitudeTwo")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.AgentNo = params.get("AgentNo")
        self.MerchantNo = params.get("MerchantNo")
        self.AddTime = params.get("AddTime")
        self.Address = params.get("Address")
        self.Longitude = params.get("Longitude")
        self.ShopNo = params.get("ShopNo")
        self.ShopFullName = params.get("ShopFullName")
        self.Contact = params.get("Contact")
        self.PictureThree = params.get("PictureThree")
        self.PictureOne = params.get("PictureOne")
        self.Telephone = params.get("Telephone")
        self.OutShopId = params.get("OutShopId")
        self.CityId = params.get("CityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawBill(AbstractModel):
    """聚鑫提现订单内容

    """

    def __init__(self):
        r"""
        :param WithdrawOrderId: 业务提现订单号
        :type WithdrawOrderId: str
        :param Date: 提现日期
        :type Date: str
        :param PayAmt: 提现金额，单位： 分
        :type PayAmt: str
        :param InSubAppId: 聚鑫分配转入账户appid
        :type InSubAppId: str
        :param OutSubAppId: 聚鑫分配转出账户appid
        :type OutSubAppId: str
        :param CurrencyType: ISO货币代码
        :type CurrencyType: str
        :param MetaData: 透传字段
        :type MetaData: str
        :param ExtendFieldData: 扩展字段
        :type ExtendFieldData: str
        """
        self.WithdrawOrderId = None
        self.Date = None
        self.PayAmt = None
        self.InSubAppId = None
        self.OutSubAppId = None
        self.CurrencyType = None
        self.MetaData = None
        self.ExtendFieldData = None


    def _deserialize(self, params):
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        self.Date = params.get("Date")
        self.PayAmt = params.get("PayAmt")
        self.InSubAppId = params.get("InSubAppId")
        self.OutSubAppId = params.get("OutSubAppId")
        self.CurrencyType = params.get("CurrencyType")
        self.MetaData = params.get("MetaData")
        self.ExtendFieldData = params.get("ExtendFieldData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawCashMembershipRequest(AbstractModel):
    """WithdrawCashMembership请求参数结构体

    """

    def __init__(self):
        r"""
        :param MrchCode: String(22)，商户号（签约客户号）
        :type MrchCode: str
        :param TranWebName: STRING(150)，交易网名称（市场名称）
        :type TranWebName: str
        :param MemberGlobalType: STRING(5)，会员证件类型（详情见“常见问题”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，会员证件号码
        :type MemberGlobalId: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，会员名称
        :type MemberName: str
        :param TakeCashAcctNo: STRING(50)，提现账号（银行卡）
        :type TakeCashAcctNo: str
        :param OutAmtAcctName: STRING(150)，出金账户名称（银行卡户名）
        :type OutAmtAcctName: str
        :param Ccy: STRING(3)，币种（默认为RMB）
        :type Ccy: str
        :param CashAmt: STRING(20)，可提现金额
        :type CashAmt: str
        :param Remark: STRING(300)，备注（建议可送订单号，可在对账文件的备注字段获取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param WebSign: STRING(300)，网银签名
        :type WebSign: str
        :param Profile: STRING(12)，接入环境，默认接入沙箱环境。接入正式环境填"prod"
        :type Profile: str
        """
        self.MrchCode = None
        self.TranWebName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.TakeCashAcctNo = None
        self.OutAmtAcctName = None
        self.Ccy = None
        self.CashAmt = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None
        self.Profile = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranWebName = params.get("TranWebName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.OutAmtAcctName = params.get("OutAmtAcctName")
        self.Ccy = params.get("Ccy")
        self.CashAmt = params.get("CashAmt")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")
        self.Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawCashMembershipResponse(AbstractModel):
    """WithdrawCashMembership返回参数结构体

    """

    def __init__(self):
        r"""
        :param TxnReturnCode: String(20)，返回码
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回信息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param TransferFee: STRING(20)，转账手续费（固定返回0.00）
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferFee: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.TransferFee = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.TransferFee = params.get("TransferFee")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class WithdrawItem(AbstractModel):
    """清分提现明细信息

    """

    def __init__(self):
        r"""
        :param BookingFlag: STRING(2)，记账标志（01: 提现; 02: 清分 ）
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易状态（0: 成功）
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param BookingMsg: STRING(200)，记账说明
注意：此字段可能返回 null，表示取不到有效值。
        :type BookingMsg: str
        :param TranNetMemberCode: STRING(32)，交易网会员代码
注意：此字段可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，见证子帐户的帐号
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctName: STRING(150)，见证子账户的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param TranAmt: STRING(20)，交易金额
注意：此字段可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param Commission: STRING(20)，手续费
注意：此字段可能返回 null，表示取不到有效值。
        :type Commission: str
        :param TranDate: STRING(8)，交易日期
注意：此字段可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，见证系统流水号
注意：此字段可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param Remark: STRING(300)，备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.BookingFlag = None
        self.TranStatus = None
        self.BookingMsg = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.SubAcctName = None
        self.TranAmt = None
        self.Commission = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.BookingMsg = params.get("BookingMsg")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctName = params.get("SubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.Commission = params.get("Commission")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        