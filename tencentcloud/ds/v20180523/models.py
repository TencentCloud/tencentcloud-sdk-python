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


class CheckVcodeRequest(AbstractModel):
    """CheckVcode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名VerifyCode
        :type Module: str
        :param _Operation: 操作名CheckVcode
        :type Operation: str
        :param _AccountResId: 帐号ID
        :type AccountResId: str
        :param _ContractResId: 合同ID
        :type ContractResId: str
        :param _VerifyCode: 验证码
        :type VerifyCode: str
        """
        self._Module = None
        self._Operation = None
        self._AccountResId = None
        self._ContractResId = None
        self._VerifyCode = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def ContractResId(self):
        return self._ContractResId

    @ContractResId.setter
    def ContractResId(self, ContractResId):
        self._ContractResId = ContractResId

    @property
    def VerifyCode(self):
        return self._VerifyCode

    @VerifyCode.setter
    def VerifyCode(self, VerifyCode):
        self._VerifyCode = VerifyCode


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._AccountResId = params.get("AccountResId")
        self._ContractResId = params.get("ContractResId")
        self._VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckVcodeResponse(AbstractModel):
    """CheckVcode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateContractByUploadRequest(AbstractModel):
    """CreateContractByUpload请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名ContractMng
        :type Module: str
        :param _Operation: 操作名CreateContractByUpload
        :type Operation: str
        :param _SignInfos: 签署人信息
        :type SignInfos: list of SignInfo
        :param _ContractFile: 合同上传链接地址
        :type ContractFile: str
        :param _ContractName: 合同名称
        :type ContractName: str
        :param _Remarks: 备注
        :type Remarks: str
        :param _Initiator: 合同发起方腾讯云帐号ID（由平台自动填写）
        :type Initiator: str
        :param _ExpireTime: 合同长时间未签署的过期时间
        :type ExpireTime: str
        """
        self._Module = None
        self._Operation = None
        self._SignInfos = None
        self._ContractFile = None
        self._ContractName = None
        self._Remarks = None
        self._Initiator = None
        self._ExpireTime = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def SignInfos(self):
        return self._SignInfos

    @SignInfos.setter
    def SignInfos(self, SignInfos):
        self._SignInfos = SignInfos

    @property
    def ContractFile(self):
        return self._ContractFile

    @ContractFile.setter
    def ContractFile(self, ContractFile):
        self._ContractFile = ContractFile

    @property
    def ContractName(self):
        return self._ContractName

    @ContractName.setter
    def ContractName(self, ContractName):
        self._ContractName = ContractName

    @property
    def Remarks(self):
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def Initiator(self):
        return self._Initiator

    @Initiator.setter
    def Initiator(self, Initiator):
        self._Initiator = Initiator

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        if params.get("SignInfos") is not None:
            self._SignInfos = []
            for item in params.get("SignInfos"):
                obj = SignInfo()
                obj._deserialize(item)
                self._SignInfos.append(obj)
        self._ContractFile = params.get("ContractFile")
        self._ContractName = params.get("ContractName")
        self._Remarks = params.get("Remarks")
        self._Initiator = params.get("Initiator")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContractByUploadResponse(AbstractModel):
    """CreateContractByUpload返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateEnterpriseAccountRequest(AbstractModel):
    """CreateEnterpriseAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名AccountMng
        :type Module: str
        :param _Operation: 操作名CreateEnterpriseAccount
        :type Operation: str
        :param _Name: 企业用户名称
        :type Name: str
        :param _IdentType: 企业用户证件类型，8代表营业执照，详情请见常见问题
        :type IdentType: int
        :param _IdentNo: 企业用户营业执照号码
        :type IdentNo: str
        :param _MobilePhone: 企业联系人手机号
        :type MobilePhone: str
        :param _TransactorName: 经办人姓名
        :type TransactorName: str
        :param _TransactorIdentType: 经办人证件类型，0代表身份证
        :type TransactorIdentType: int
        :param _TransactorIdentNo: 经办人证件号码
        :type TransactorIdentNo: str
        :param _TransactorPhone: 经办人手机号
        :type TransactorPhone: str
        :param _Email: 企业联系人邮箱
        :type Email: str
        """
        self._Module = None
        self._Operation = None
        self._Name = None
        self._IdentType = None
        self._IdentNo = None
        self._MobilePhone = None
        self._TransactorName = None
        self._TransactorIdentType = None
        self._TransactorIdentNo = None
        self._TransactorPhone = None
        self._Email = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdentType(self):
        return self._IdentType

    @IdentType.setter
    def IdentType(self, IdentType):
        self._IdentType = IdentType

    @property
    def IdentNo(self):
        return self._IdentNo

    @IdentNo.setter
    def IdentNo(self, IdentNo):
        self._IdentNo = IdentNo

    @property
    def MobilePhone(self):
        return self._MobilePhone

    @MobilePhone.setter
    def MobilePhone(self, MobilePhone):
        self._MobilePhone = MobilePhone

    @property
    def TransactorName(self):
        return self._TransactorName

    @TransactorName.setter
    def TransactorName(self, TransactorName):
        self._TransactorName = TransactorName

    @property
    def TransactorIdentType(self):
        return self._TransactorIdentType

    @TransactorIdentType.setter
    def TransactorIdentType(self, TransactorIdentType):
        self._TransactorIdentType = TransactorIdentType

    @property
    def TransactorIdentNo(self):
        return self._TransactorIdentNo

    @TransactorIdentNo.setter
    def TransactorIdentNo(self, TransactorIdentNo):
        self._TransactorIdentNo = TransactorIdentNo

    @property
    def TransactorPhone(self):
        return self._TransactorPhone

    @TransactorPhone.setter
    def TransactorPhone(self, TransactorPhone):
        self._TransactorPhone = TransactorPhone

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Name = params.get("Name")
        self._IdentType = params.get("IdentType")
        self._IdentNo = params.get("IdentNo")
        self._MobilePhone = params.get("MobilePhone")
        self._TransactorName = params.get("TransactorName")
        self._TransactorIdentType = params.get("TransactorIdentType")
        self._TransactorIdentNo = params.get("TransactorIdentNo")
        self._TransactorPhone = params.get("TransactorPhone")
        self._Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnterpriseAccountResponse(AbstractModel):
    """CreateEnterpriseAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountResId: 帐号ID
        :type AccountResId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountResId = None
        self._RequestId = None

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccountResId = params.get("AccountResId")
        self._RequestId = params.get("RequestId")


class CreatePersonalAccountRequest(AbstractModel):
    """CreatePersonalAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名AccountMng
        :type Module: str
        :param _Operation: 操作名CreatePersonalAccount
        :type Operation: str
        :param _Name: 个人用户姓名
        :type Name: str
        :param _IdentType: 个人用户证件类型，0代表身份证，详情请见常见问题
        :type IdentType: int
        :param _IdentNo: 个人用户证件号码
        :type IdentNo: str
        :param _MobilePhone: 个人用户手机号
        :type MobilePhone: str
        """
        self._Module = None
        self._Operation = None
        self._Name = None
        self._IdentType = None
        self._IdentNo = None
        self._MobilePhone = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdentType(self):
        return self._IdentType

    @IdentType.setter
    def IdentType(self, IdentType):
        self._IdentType = IdentType

    @property
    def IdentNo(self):
        return self._IdentNo

    @IdentNo.setter
    def IdentNo(self, IdentNo):
        self._IdentNo = IdentNo

    @property
    def MobilePhone(self):
        return self._MobilePhone

    @MobilePhone.setter
    def MobilePhone(self, MobilePhone):
        self._MobilePhone = MobilePhone


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._Name = params.get("Name")
        self._IdentType = params.get("IdentType")
        self._IdentNo = params.get("IdentNo")
        self._MobilePhone = params.get("MobilePhone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonalAccountResponse(AbstractModel):
    """CreatePersonalAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountResId: 账号ID
        :type AccountResId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountResId = None
        self._RequestId = None

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AccountResId = params.get("AccountResId")
        self._RequestId = params.get("RequestId")


class CreateSealRequest(AbstractModel):
    """CreateSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名SealMng
        :type Module: str
        :param _Operation: 操作名CreateSeal
        :type Operation: str
        :param _AccountResId: 帐号ID
        :type AccountResId: str
        :param _ImgUrl: 签章链接，图片必须为png格式
        :type ImgUrl: str
        :param _ImgData: 图片数据，base64编码
        :type ImgData: str
        """
        self._Module = None
        self._Operation = None
        self._AccountResId = None
        self._ImgUrl = None
        self._ImgData = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def ImgUrl(self):
        return self._ImgUrl

    @ImgUrl.setter
    def ImgUrl(self, ImgUrl):
        self._ImgUrl = ImgUrl

    @property
    def ImgData(self):
        return self._ImgData

    @ImgData.setter
    def ImgData(self, ImgData):
        self._ImgData = ImgData


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._AccountResId = params.get("AccountResId")
        self._ImgUrl = params.get("ImgUrl")
        self._ImgData = params.get("ImgData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealResponse(AbstractModel):
    """CreateSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealResId: 签章ID
        :type SealResId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealResId = None
        self._RequestId = None

    @property
    def SealResId(self):
        return self._SealResId

    @SealResId.setter
    def SealResId(self, SealResId):
        self._SealResId = SealResId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealResId = params.get("SealResId")
        self._RequestId = params.get("RequestId")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名AccountMng
        :type Module: str
        :param _Operation: 操作名DeleteAccount
        :type Operation: str
        :param _AccountList: 帐号ID列表
        :type AccountList: list of str
        """
        self._Module = None
        self._Operation = None
        self._AccountList = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def AccountList(self):
        return self._AccountList

    @AccountList.setter
    def AccountList(self, AccountList):
        self._AccountList = AccountList


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._AccountList = params.get("AccountList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DelSuccessList: 删除成功帐号ID列表
        :type DelSuccessList: list of str
        :param _DelFailedList: 删除失败帐号ID列表
        :type DelFailedList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DelSuccessList = None
        self._DelFailedList = None
        self._RequestId = None

    @property
    def DelSuccessList(self):
        return self._DelSuccessList

    @DelSuccessList.setter
    def DelSuccessList(self, DelSuccessList):
        self._DelSuccessList = DelSuccessList

    @property
    def DelFailedList(self):
        return self._DelFailedList

    @DelFailedList.setter
    def DelFailedList(self, DelFailedList):
        self._DelFailedList = DelFailedList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DelSuccessList = params.get("DelSuccessList")
        self._DelFailedList = params.get("DelFailedList")
        self._RequestId = params.get("RequestId")


class DeleteSealRequest(AbstractModel):
    """DeleteSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名SealMng
        :type Module: str
        :param _Operation: 操作名DeleteSeal
        :type Operation: str
        :param _AccountResId: 帐号ID
        :type AccountResId: str
        :param _SealResId: 签章ID
        :type SealResId: str
        """
        self._Module = None
        self._Operation = None
        self._AccountResId = None
        self._SealResId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def SealResId(self):
        return self._SealResId

    @SealResId.setter
    def SealResId(self, SealResId):
        self._SealResId = SealResId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._AccountResId = params.get("AccountResId")
        self._SealResId = params.get("SealResId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSealResponse(AbstractModel):
    """DeleteSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SealResId: 签章ID
        :type SealResId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SealResId = None
        self._RequestId = None

    @property
    def SealResId(self):
        return self._SealResId

    @SealResId.setter
    def SealResId(self, SealResId):
        self._SealResId = SealResId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SealResId = params.get("SealResId")
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名CommonMng
        :type Module: str
        :param _Operation: 操作名DescribeTaskStatus
        :type Operation: str
        :param _TaskId: 任务ID
        :type TaskId: int
        """
        self._Module = None
        self._Operation = None
        self._TaskId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskResult: 任务结果
        :type TaskResult: str
        :param _TaskType: 任务类型，010代表合同上传结果，020代表合同下载结果
        :type TaskType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskResult = None
        self._TaskType = None
        self._RequestId = None

    @property
    def TaskResult(self):
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskResult = params.get("TaskResult")
        self._TaskType = params.get("TaskType")
        self._RequestId = params.get("RequestId")


class DownloadContractRequest(AbstractModel):
    """DownloadContract请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名ContractMng
        :type Module: str
        :param _Operation: 操作名DownloadContract
        :type Operation: str
        :param _ContractResId: 合同ID
        :type ContractResId: str
        """
        self._Module = None
        self._Operation = None
        self._ContractResId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ContractResId(self):
        return self._ContractResId

    @ContractResId.setter
    def ContractResId(self, ContractResId):
        self._ContractResId = ContractResId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ContractResId = params.get("ContractResId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadContractResponse(AbstractModel):
    """DownloadContract返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class SendVcodeRequest(AbstractModel):
    """SendVcode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名VerifyCode
        :type Module: str
        :param _Operation: 操作名SendVcode
        :type Operation: str
        :param _ContractResId: 合同ID
        :type ContractResId: str
        :param _AccountResId: 帐号ID
        :type AccountResId: str
        """
        self._Module = None
        self._Operation = None
        self._ContractResId = None
        self._AccountResId = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ContractResId(self):
        return self._ContractResId

    @ContractResId.setter
    def ContractResId(self, ContractResId):
        self._ContractResId = ContractResId

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ContractResId = params.get("ContractResId")
        self._AccountResId = params.get("AccountResId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendVcodeResponse(AbstractModel):
    """SendVcode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SignContractByCoordinateRequest(AbstractModel):
    """SignContractByCoordinate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名ContractMng
        :type Module: str
        :param _Operation: 操作名SignContractByCoordinate
        :type Operation: str
        :param _ContractResId: 合同ID
        :type ContractResId: str
        :param _AccountResId: 帐户ID
        :type AccountResId: str
        :param _SignLocations: 签署坐标，坐标原点在文件左下角，坐标单位为磅，坐标不得超过合同文件边界
        :type SignLocations: list of SignLocation
        :param _AuthorizationTime: 授权时间（由平台自动填充）
        :type AuthorizationTime: str
        :param _Position: 授权IP地址（由平台自动填充）
        :type Position: str
        :param _SealResId: 签章ID
        :type SealResId: str
        :param _CertType: 选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1
        :type CertType: int
        :param _ImageData: 签名图片，base64编码
        :type ImageData: str
        """
        self._Module = None
        self._Operation = None
        self._ContractResId = None
        self._AccountResId = None
        self._SignLocations = None
        self._AuthorizationTime = None
        self._Position = None
        self._SealResId = None
        self._CertType = None
        self._ImageData = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ContractResId(self):
        return self._ContractResId

    @ContractResId.setter
    def ContractResId(self, ContractResId):
        self._ContractResId = ContractResId

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def SignLocations(self):
        return self._SignLocations

    @SignLocations.setter
    def SignLocations(self, SignLocations):
        self._SignLocations = SignLocations

    @property
    def AuthorizationTime(self):
        return self._AuthorizationTime

    @AuthorizationTime.setter
    def AuthorizationTime(self, AuthorizationTime):
        self._AuthorizationTime = AuthorizationTime

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def SealResId(self):
        return self._SealResId

    @SealResId.setter
    def SealResId(self, SealResId):
        self._SealResId = SealResId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def ImageData(self):
        return self._ImageData

    @ImageData.setter
    def ImageData(self, ImageData):
        self._ImageData = ImageData


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ContractResId = params.get("ContractResId")
        self._AccountResId = params.get("AccountResId")
        if params.get("SignLocations") is not None:
            self._SignLocations = []
            for item in params.get("SignLocations"):
                obj = SignLocation()
                obj._deserialize(item)
                self._SignLocations.append(obj)
        self._AuthorizationTime = params.get("AuthorizationTime")
        self._Position = params.get("Position")
        self._SealResId = params.get("SealResId")
        self._CertType = params.get("CertType")
        self._ImageData = params.get("ImageData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignContractByCoordinateResponse(AbstractModel):
    """SignContractByCoordinate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SignContractByKeywordRequest(AbstractModel):
    """SignContractByKeyword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块名ContractMng
        :type Module: str
        :param _Operation: 操作名SignContractByKeyword
        :type Operation: str
        :param _ContractResId: 合同ID
        :type ContractResId: str
        :param _AccountResId: 账户ID
        :type AccountResId: str
        :param _SignKeyword: 签署关键字，偏移坐标原点为关键字中心
        :type SignKeyword: :class:`tencentcloud.ds.v20180523.models.SignKeyword`
        :param _AuthorizationTime: 授权时间（由平台自动填充）
        :type AuthorizationTime: str
        :param _Position: 授权IP地址（由平台自动填充）
        :type Position: str
        :param _SealResId: 签章ID
        :type SealResId: str
        :param _CertType: 选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1
        :type CertType: int
        :param _ImageData: 签名图片，base64编码
        :type ImageData: str
        """
        self._Module = None
        self._Operation = None
        self._ContractResId = None
        self._AccountResId = None
        self._SignKeyword = None
        self._AuthorizationTime = None
        self._Position = None
        self._SealResId = None
        self._CertType = None
        self._ImageData = None

    @property
    def Module(self):
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def ContractResId(self):
        return self._ContractResId

    @ContractResId.setter
    def ContractResId(self, ContractResId):
        self._ContractResId = ContractResId

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def SignKeyword(self):
        return self._SignKeyword

    @SignKeyword.setter
    def SignKeyword(self, SignKeyword):
        self._SignKeyword = SignKeyword

    @property
    def AuthorizationTime(self):
        return self._AuthorizationTime

    @AuthorizationTime.setter
    def AuthorizationTime(self, AuthorizationTime):
        self._AuthorizationTime = AuthorizationTime

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def SealResId(self):
        return self._SealResId

    @SealResId.setter
    def SealResId(self, SealResId):
        self._SealResId = SealResId

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def ImageData(self):
        return self._ImageData

    @ImageData.setter
    def ImageData(self, ImageData):
        self._ImageData = ImageData


    def _deserialize(self, params):
        self._Module = params.get("Module")
        self._Operation = params.get("Operation")
        self._ContractResId = params.get("ContractResId")
        self._AccountResId = params.get("AccountResId")
        if params.get("SignKeyword") is not None:
            self._SignKeyword = SignKeyword()
            self._SignKeyword._deserialize(params.get("SignKeyword"))
        self._AuthorizationTime = params.get("AuthorizationTime")
        self._Position = params.get("Position")
        self._SealResId = params.get("SealResId")
        self._CertType = params.get("CertType")
        self._ImageData = params.get("ImageData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignContractByKeywordResponse(AbstractModel):
    """SignContractByKeyword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SignInfo(AbstractModel):
    """签署人信息

    """

    def __init__(self):
        r"""
        :param _AccountResId: 账户ID
        :type AccountResId: str
        :param _AuthorizationTime: 授权时间（上传合同可不传该参数）
        :type AuthorizationTime: str
        :param _Location: 授权IP地址（上传合同可不传该参数）
        :type Location: str
        :param _SealId: 签章ID
        :type SealId: str
        :param _ImageData: 签名图片，优先级比SealId高
        :type ImageData: str
        :param _CertType: 默认值：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1
        :type CertType: int
        :param _SignLocation: 签名域的标签值
        :type SignLocation: str
        """
        self._AccountResId = None
        self._AuthorizationTime = None
        self._Location = None
        self._SealId = None
        self._ImageData = None
        self._CertType = None
        self._SignLocation = None

    @property
    def AccountResId(self):
        return self._AccountResId

    @AccountResId.setter
    def AccountResId(self, AccountResId):
        self._AccountResId = AccountResId

    @property
    def AuthorizationTime(self):
        return self._AuthorizationTime

    @AuthorizationTime.setter
    def AuthorizationTime(self, AuthorizationTime):
        self._AuthorizationTime = AuthorizationTime

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def SealId(self):
        return self._SealId

    @SealId.setter
    def SealId(self, SealId):
        self._SealId = SealId

    @property
    def ImageData(self):
        return self._ImageData

    @ImageData.setter
    def ImageData(self, ImageData):
        self._ImageData = ImageData

    @property
    def CertType(self):
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SignLocation(self):
        return self._SignLocation

    @SignLocation.setter
    def SignLocation(self, SignLocation):
        self._SignLocation = SignLocation


    def _deserialize(self, params):
        self._AccountResId = params.get("AccountResId")
        self._AuthorizationTime = params.get("AuthorizationTime")
        self._Location = params.get("Location")
        self._SealId = params.get("SealId")
        self._ImageData = params.get("ImageData")
        self._CertType = params.get("CertType")
        self._SignLocation = params.get("SignLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignKeyword(AbstractModel):
    """签署关键字信息

    """

    def __init__(self):
        r"""
        :param _Keyword: 关键字
        :type Keyword: str
        :param _OffsetCoordX: X轴偏移坐标
        :type OffsetCoordX: str
        :param _OffsetCoordY: Y轴偏移坐标
        :type OffsetCoordY: str
        :param _ImageWidth: 签章图片宽度
        :type ImageWidth: str
        :param _ImageHeight: 签章图片高度
        :type ImageHeight: str
        """
        self._Keyword = None
        self._OffsetCoordX = None
        self._OffsetCoordY = None
        self._ImageWidth = None
        self._ImageHeight = None

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def OffsetCoordX(self):
        return self._OffsetCoordX

    @OffsetCoordX.setter
    def OffsetCoordX(self, OffsetCoordX):
        self._OffsetCoordX = OffsetCoordX

    @property
    def OffsetCoordY(self):
        return self._OffsetCoordY

    @OffsetCoordY.setter
    def OffsetCoordY(self, OffsetCoordY):
        self._OffsetCoordY = OffsetCoordY

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight


    def _deserialize(self, params):
        self._Keyword = params.get("Keyword")
        self._OffsetCoordX = params.get("OffsetCoordX")
        self._OffsetCoordY = params.get("OffsetCoordY")
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignLocation(AbstractModel):
    """签署坐标对象

    """

    def __init__(self):
        r"""
        :param _SignOnPage: 签名域页数
        :type SignOnPage: str
        :param _SignLocationLBX: 签名域左下角X轴坐标轴
        :type SignLocationLBX: str
        :param _SignLocationLBY: 签名域左下角Y轴坐标轴
        :type SignLocationLBY: str
        :param _SignLocationRUX: 签名域右上角X轴坐标轴
        :type SignLocationRUX: str
        :param _SignLocationRUY: 签名域右上角Y轴坐标轴
        :type SignLocationRUY: str
        """
        self._SignOnPage = None
        self._SignLocationLBX = None
        self._SignLocationLBY = None
        self._SignLocationRUX = None
        self._SignLocationRUY = None

    @property
    def SignOnPage(self):
        return self._SignOnPage

    @SignOnPage.setter
    def SignOnPage(self, SignOnPage):
        self._SignOnPage = SignOnPage

    @property
    def SignLocationLBX(self):
        return self._SignLocationLBX

    @SignLocationLBX.setter
    def SignLocationLBX(self, SignLocationLBX):
        self._SignLocationLBX = SignLocationLBX

    @property
    def SignLocationLBY(self):
        return self._SignLocationLBY

    @SignLocationLBY.setter
    def SignLocationLBY(self, SignLocationLBY):
        self._SignLocationLBY = SignLocationLBY

    @property
    def SignLocationRUX(self):
        return self._SignLocationRUX

    @SignLocationRUX.setter
    def SignLocationRUX(self, SignLocationRUX):
        self._SignLocationRUX = SignLocationRUX

    @property
    def SignLocationRUY(self):
        return self._SignLocationRUY

    @SignLocationRUY.setter
    def SignLocationRUY(self, SignLocationRUY):
        self._SignLocationRUY = SignLocationRUY


    def _deserialize(self, params):
        self._SignOnPage = params.get("SignOnPage")
        self._SignLocationLBX = params.get("SignLocationLBX")
        self._SignLocationLBY = params.get("SignLocationLBY")
        self._SignLocationRUX = params.get("SignLocationRUX")
        self._SignLocationRUY = params.get("SignLocationRUY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        