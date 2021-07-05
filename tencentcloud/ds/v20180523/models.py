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
        """
        :param Module: 模块名VerifyCode
        :type Module: str
        :param Operation: 操作名CheckVcode
        :type Operation: str
        :param AccountResId: 帐号ID
        :type AccountResId: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param VerifyCode: 验证码
        :type VerifyCode: str
        """
        self.Module = None
        self.Operation = None
        self.AccountResId = None
        self.ContractResId = None
        self.VerifyCode = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountResId = params.get("AccountResId")
        self.ContractResId = params.get("ContractResId")
        self.VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckVcodeResponse(AbstractModel):
    """CheckVcode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateContractByUploadRequest(AbstractModel):
    """CreateContractByUpload请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名ContractMng
        :type Module: str
        :param Operation: 操作名CreateContractByUpload
        :type Operation: str
        :param SignInfos: 签署人信息
        :type SignInfos: list of SignInfo
        :param ContractFile: 合同上传链接地址
        :type ContractFile: str
        :param ContractName: 合同名称
        :type ContractName: str
        :param Remarks: 备注
        :type Remarks: str
        :param Initiator: 合同发起方腾讯云帐号ID（由平台自动填写）
        :type Initiator: str
        :param ExpireTime: 合同长时间未签署的过期时间
        :type ExpireTime: str
        """
        self.Module = None
        self.Operation = None
        self.SignInfos = None
        self.ContractFile = None
        self.ContractName = None
        self.Remarks = None
        self.Initiator = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        if params.get("SignInfos") is not None:
            self.SignInfos = []
            for item in params.get("SignInfos"):
                obj = SignInfo()
                obj._deserialize(item)
                self.SignInfos.append(obj)
        self.ContractFile = params.get("ContractFile")
        self.ContractName = params.get("ContractName")
        self.Remarks = params.get("Remarks")
        self.Initiator = params.get("Initiator")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContractByUploadResponse(AbstractModel):
    """CreateContractByUpload返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateEnterpriseAccountRequest(AbstractModel):
    """CreateEnterpriseAccount请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名AccountMng
        :type Module: str
        :param Operation: 操作名CreateEnterpriseAccount
        :type Operation: str
        :param Name: 企业用户名称
        :type Name: str
        :param IdentType: 企业用户证件类型，8代表营业执照，详情请见常见问题
        :type IdentType: int
        :param IdentNo: 企业用户营业执照号码
        :type IdentNo: str
        :param MobilePhone: 企业联系人手机号
        :type MobilePhone: str
        :param TransactorName: 经办人姓名
        :type TransactorName: str
        :param TransactorIdentType: 经办人证件类型，0代表身份证
        :type TransactorIdentType: int
        :param TransactorIdentNo: 经办人证件号码
        :type TransactorIdentNo: str
        :param TransactorPhone: 经办人手机号
        :type TransactorPhone: str
        :param Email: 企业联系人邮箱
        :type Email: str
        """
        self.Module = None
        self.Operation = None
        self.Name = None
        self.IdentType = None
        self.IdentNo = None
        self.MobilePhone = None
        self.TransactorName = None
        self.TransactorIdentType = None
        self.TransactorIdentNo = None
        self.TransactorPhone = None
        self.Email = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Name = params.get("Name")
        self.IdentType = params.get("IdentType")
        self.IdentNo = params.get("IdentNo")
        self.MobilePhone = params.get("MobilePhone")
        self.TransactorName = params.get("TransactorName")
        self.TransactorIdentType = params.get("TransactorIdentType")
        self.TransactorIdentNo = params.get("TransactorIdentNo")
        self.TransactorPhone = params.get("TransactorPhone")
        self.Email = params.get("Email")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnterpriseAccountResponse(AbstractModel):
    """CreateEnterpriseAccount返回参数结构体

    """

    def __init__(self):
        """
        :param AccountResId: 帐号ID
        :type AccountResId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccountResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccountResId = params.get("AccountResId")
        self.RequestId = params.get("RequestId")


class CreatePersonalAccountRequest(AbstractModel):
    """CreatePersonalAccount请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名AccountMng
        :type Module: str
        :param Operation: 操作名CreatePersonalAccount
        :type Operation: str
        :param Name: 个人用户姓名
        :type Name: str
        :param IdentType: 个人用户证件类型，0代表身份证，详情请见常见问题
        :type IdentType: int
        :param IdentNo: 个人用户证件号码
        :type IdentNo: str
        :param MobilePhone: 个人用户手机号
        :type MobilePhone: str
        """
        self.Module = None
        self.Operation = None
        self.Name = None
        self.IdentType = None
        self.IdentNo = None
        self.MobilePhone = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Name = params.get("Name")
        self.IdentType = params.get("IdentType")
        self.IdentNo = params.get("IdentNo")
        self.MobilePhone = params.get("MobilePhone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonalAccountResponse(AbstractModel):
    """CreatePersonalAccount返回参数结构体

    """

    def __init__(self):
        """
        :param AccountResId: 账号ID
        :type AccountResId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccountResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccountResId = params.get("AccountResId")
        self.RequestId = params.get("RequestId")


class CreateSealRequest(AbstractModel):
    """CreateSeal请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名SealMng
        :type Module: str
        :param Operation: 操作名CreateSeal
        :type Operation: str
        :param AccountResId: 帐号ID
        :type AccountResId: str
        :param ImgUrl: 签章链接，图片必须为png格式
        :type ImgUrl: str
        :param ImgData: 图片数据，base64编码
        :type ImgData: str
        """
        self.Module = None
        self.Operation = None
        self.AccountResId = None
        self.ImgUrl = None
        self.ImgData = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountResId = params.get("AccountResId")
        self.ImgUrl = params.get("ImgUrl")
        self.ImgData = params.get("ImgData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealResponse(AbstractModel):
    """CreateSeal返回参数结构体

    """

    def __init__(self):
        """
        :param SealResId: 签章ID
        :type SealResId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SealResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealResId = params.get("SealResId")
        self.RequestId = params.get("RequestId")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名AccountMng
        :type Module: str
        :param Operation: 操作名DeleteAccount
        :type Operation: str
        :param AccountList: 帐号ID列表
        :type AccountList: list of str
        """
        self.Module = None
        self.Operation = None
        self.AccountList = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountList = params.get("AccountList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        """
        :param DelSuccessList: 删除成功帐号ID列表
        :type DelSuccessList: list of str
        :param DelFailedList: 删除失败帐号ID列表
        :type DelFailedList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DelSuccessList = None
        self.DelFailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DelSuccessList = params.get("DelSuccessList")
        self.DelFailedList = params.get("DelFailedList")
        self.RequestId = params.get("RequestId")


class DeleteSealRequest(AbstractModel):
    """DeleteSeal请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名SealMng
        :type Module: str
        :param Operation: 操作名DeleteSeal
        :type Operation: str
        :param AccountResId: 帐号ID
        :type AccountResId: str
        :param SealResId: 签章ID
        :type SealResId: str
        """
        self.Module = None
        self.Operation = None
        self.AccountResId = None
        self.SealResId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountResId = params.get("AccountResId")
        self.SealResId = params.get("SealResId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSealResponse(AbstractModel):
    """DeleteSeal返回参数结构体

    """

    def __init__(self):
        """
        :param SealResId: 签章ID
        :type SealResId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SealResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealResId = params.get("SealResId")
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名CommonMng
        :type Module: str
        :param Operation: 操作名DescribeTaskStatus
        :type Operation: str
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.Module = None
        self.Operation = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TaskResult: 任务结果
        :type TaskResult: str
        :param TaskType: 任务类型，010代表合同上传结果，020代表合同下载结果
        :type TaskType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.TaskType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskResult = params.get("TaskResult")
        self.TaskType = params.get("TaskType")
        self.RequestId = params.get("RequestId")


class DownloadContractRequest(AbstractModel):
    """DownloadContract请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名ContractMng
        :type Module: str
        :param Operation: 操作名DownloadContract
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadContractResponse(AbstractModel):
    """DownloadContract返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SendVcodeRequest(AbstractModel):
    """SendVcode请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名VerifyCode
        :type Module: str
        :param Operation: 操作名SendVcode
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param AccountResId: 帐号ID
        :type AccountResId: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None
        self.AccountResId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")
        self.AccountResId = params.get("AccountResId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendVcodeResponse(AbstractModel):
    """SendVcode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignContractByCoordinateRequest(AbstractModel):
    """SignContractByCoordinate请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名ContractMng
        :type Module: str
        :param Operation: 操作名SignContractByCoordinate
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param AccountResId: 帐户ID
        :type AccountResId: str
        :param SignLocations: 签署坐标，坐标原点在文件左下角，坐标单位为磅，坐标不得超过合同文件边界
        :type SignLocations: list of SignLocation
        :param AuthorizationTime: 授权时间（由平台自动填充）
        :type AuthorizationTime: str
        :param Position: 授权IP地址（由平台自动填充）
        :type Position: str
        :param SealResId: 签章ID
        :type SealResId: str
        :param CertType: 选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1
        :type CertType: int
        :param ImageData: 签名图片，base64编码
        :type ImageData: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None
        self.AccountResId = None
        self.SignLocations = None
        self.AuthorizationTime = None
        self.Position = None
        self.SealResId = None
        self.CertType = None
        self.ImageData = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")
        self.AccountResId = params.get("AccountResId")
        if params.get("SignLocations") is not None:
            self.SignLocations = []
            for item in params.get("SignLocations"):
                obj = SignLocation()
                obj._deserialize(item)
                self.SignLocations.append(obj)
        self.AuthorizationTime = params.get("AuthorizationTime")
        self.Position = params.get("Position")
        self.SealResId = params.get("SealResId")
        self.CertType = params.get("CertType")
        self.ImageData = params.get("ImageData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignContractByCoordinateResponse(AbstractModel):
    """SignContractByCoordinate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignContractByKeywordRequest(AbstractModel):
    """SignContractByKeyword请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名ContractMng
        :type Module: str
        :param Operation: 操作名SignContractByKeyword
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param AccountResId: 账户ID
        :type AccountResId: str
        :param SignKeyword: 签署关键字，偏移坐标原点为关键字中心
        :type SignKeyword: :class:`tencentcloud.ds.v20180523.models.SignKeyword`
        :param AuthorizationTime: 授权时间（由平台自动填充）
        :type AuthorizationTime: str
        :param Position: 授权IP地址（由平台自动填充）
        :type Position: str
        :param SealResId: 签章ID
        :type SealResId: str
        :param CertType: 选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1
        :type CertType: int
        :param ImageData: 签名图片，base64编码
        :type ImageData: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None
        self.AccountResId = None
        self.SignKeyword = None
        self.AuthorizationTime = None
        self.Position = None
        self.SealResId = None
        self.CertType = None
        self.ImageData = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")
        self.AccountResId = params.get("AccountResId")
        if params.get("SignKeyword") is not None:
            self.SignKeyword = SignKeyword()
            self.SignKeyword._deserialize(params.get("SignKeyword"))
        self.AuthorizationTime = params.get("AuthorizationTime")
        self.Position = params.get("Position")
        self.SealResId = params.get("SealResId")
        self.CertType = params.get("CertType")
        self.ImageData = params.get("ImageData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignContractByKeywordResponse(AbstractModel):
    """SignContractByKeyword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignInfo(AbstractModel):
    """签署人信息

    """

    def __init__(self):
        """
        :param AccountResId: 账户ID
        :type AccountResId: str
        :param AuthorizationTime: 授权时间（上传合同可不传该参数）
        :type AuthorizationTime: str
        :param Location: 授权IP地址（上传合同可不传该参数）
        :type Location: str
        :param SealId: 签章ID
        :type SealId: str
        :param ImageData: 签名图片，优先级比SealId高
        :type ImageData: str
        :param CertType: 默认值：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1
        :type CertType: int
        :param SignLocation: 签名域的标签值
        :type SignLocation: str
        """
        self.AccountResId = None
        self.AuthorizationTime = None
        self.Location = None
        self.SealId = None
        self.ImageData = None
        self.CertType = None
        self.SignLocation = None


    def _deserialize(self, params):
        self.AccountResId = params.get("AccountResId")
        self.AuthorizationTime = params.get("AuthorizationTime")
        self.Location = params.get("Location")
        self.SealId = params.get("SealId")
        self.ImageData = params.get("ImageData")
        self.CertType = params.get("CertType")
        self.SignLocation = params.get("SignLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignKeyword(AbstractModel):
    """签署关键字信息

    """

    def __init__(self):
        """
        :param Keyword: 关键字
        :type Keyword: str
        :param OffsetCoordX: X轴偏移坐标
        :type OffsetCoordX: str
        :param OffsetCoordY: Y轴偏移坐标
        :type OffsetCoordY: str
        :param ImageWidth: 签章图片宽度
        :type ImageWidth: str
        :param ImageHeight: 签章图片高度
        :type ImageHeight: str
        """
        self.Keyword = None
        self.OffsetCoordX = None
        self.OffsetCoordY = None
        self.ImageWidth = None
        self.ImageHeight = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.OffsetCoordX = params.get("OffsetCoordX")
        self.OffsetCoordY = params.get("OffsetCoordY")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignLocation(AbstractModel):
    """签署坐标对象

    """

    def __init__(self):
        """
        :param SignOnPage: 签名域页数
        :type SignOnPage: str
        :param SignLocationLBX: 签名域左下角X轴坐标轴
        :type SignLocationLBX: str
        :param SignLocationLBY: 签名域左下角Y轴坐标轴
        :type SignLocationLBY: str
        :param SignLocationRUX: 签名域右上角X轴坐标轴
        :type SignLocationRUX: str
        :param SignLocationRUY: 签名域右上角Y轴坐标轴
        :type SignLocationRUY: str
        """
        self.SignOnPage = None
        self.SignLocationLBX = None
        self.SignLocationLBY = None
        self.SignLocationRUX = None
        self.SignLocationRUY = None


    def _deserialize(self, params):
        self.SignOnPage = params.get("SignOnPage")
        self.SignLocationLBX = params.get("SignLocationLBX")
        self.SignLocationLBY = params.get("SignLocationLBY")
        self.SignLocationRUX = params.get("SignLocationRUX")
        self.SignLocationRUY = params.get("SignLocationRUY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        