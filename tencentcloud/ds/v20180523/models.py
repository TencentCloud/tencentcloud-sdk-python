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
        :param Module: 模块名VerifyCode\n        :type Module: str\n        :param Operation: 操作名CheckVcode\n        :type Operation: str\n        :param AccountResId: 帐号ID\n        :type AccountResId: str\n        :param ContractResId: 合同ID\n        :type ContractResId: str\n        :param VerifyCode: 验证码\n        :type VerifyCode: str\n        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateContractByUploadRequest(AbstractModel):
    """CreateContractByUpload请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名ContractMng\n        :type Module: str\n        :param Operation: 操作名CreateContractByUpload\n        :type Operation: str\n        :param SignInfos: 签署人信息\n        :type SignInfos: list of SignInfo\n        :param ContractFile: 合同上传链接地址\n        :type ContractFile: str\n        :param ContractName: 合同名称\n        :type ContractName: str\n        :param Remarks: 备注\n        :type Remarks: str\n        :param Initiator: 合同发起方腾讯云帐号ID（由平台自动填写）\n        :type Initiator: str\n        :param ExpireTime: 合同长时间未签署的过期时间\n        :type ExpireTime: str\n        """
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
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名AccountMng\n        :type Module: str\n        :param Operation: 操作名CreateEnterpriseAccount\n        :type Operation: str\n        :param Name: 企业用户名称\n        :type Name: str\n        :param IdentType: 企业用户证件类型，8代表营业执照，详情请见常见问题\n        :type IdentType: int\n        :param IdentNo: 企业用户营业执照号码\n        :type IdentNo: str\n        :param MobilePhone: 企业联系人手机号\n        :type MobilePhone: str\n        :param TransactorName: 经办人姓名\n        :type TransactorName: str\n        :param TransactorIdentType: 经办人证件类型，0代表身份证\n        :type TransactorIdentType: int\n        :param TransactorIdentNo: 经办人证件号码\n        :type TransactorIdentNo: str\n        :param TransactorPhone: 经办人手机号\n        :type TransactorPhone: str\n        :param Email: 企业联系人邮箱\n        :type Email: str\n        """
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
        :param AccountResId: 帐号ID\n        :type AccountResId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名AccountMng\n        :type Module: str\n        :param Operation: 操作名CreatePersonalAccount\n        :type Operation: str\n        :param Name: 个人用户姓名\n        :type Name: str\n        :param IdentType: 个人用户证件类型，0代表身份证，详情请见常见问题\n        :type IdentType: int\n        :param IdentNo: 个人用户证件号码\n        :type IdentNo: str\n        :param MobilePhone: 个人用户手机号\n        :type MobilePhone: str\n        """
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
        :param AccountResId: 账号ID\n        :type AccountResId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名SealMng\n        :type Module: str\n        :param Operation: 操作名CreateSeal\n        :type Operation: str\n        :param AccountResId: 帐号ID\n        :type AccountResId: str\n        :param ImgUrl: 签章链接，图片必须为png格式\n        :type ImgUrl: str\n        :param ImgData: 图片数据，base64编码\n        :type ImgData: str\n        """
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
        :param SealResId: 签章ID\n        :type SealResId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名AccountMng\n        :type Module: str\n        :param Operation: 操作名DeleteAccount\n        :type Operation: str\n        :param AccountList: 帐号ID列表\n        :type AccountList: list of str\n        """
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
        :param DelSuccessList: 删除成功帐号ID列表\n        :type DelSuccessList: list of str\n        :param DelFailedList: 删除失败帐号ID列表\n        :type DelFailedList: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名SealMng\n        :type Module: str\n        :param Operation: 操作名DeleteSeal\n        :type Operation: str\n        :param AccountResId: 帐号ID\n        :type AccountResId: str\n        :param SealResId: 签章ID\n        :type SealResId: str\n        """
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
        :param SealResId: 签章ID\n        :type SealResId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名CommonMng\n        :type Module: str\n        :param Operation: 操作名DescribeTaskStatus\n        :type Operation: str\n        :param TaskId: 任务ID\n        :type TaskId: int\n        """
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
        :param TaskResult: 任务结果\n        :type TaskResult: str\n        :param TaskType: 任务类型，010代表合同上传结果，020代表合同下载结果\n        :type TaskType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名ContractMng\n        :type Module: str\n        :param Operation: 操作名DownloadContract\n        :type Operation: str\n        :param ContractResId: 合同ID\n        :type ContractResId: str\n        """
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
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Module: 模块名VerifyCode\n        :type Module: str\n        :param Operation: 操作名SendVcode\n        :type Operation: str\n        :param ContractResId: 合同ID\n        :type ContractResId: str\n        :param AccountResId: 帐号ID\n        :type AccountResId: str\n        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignContractByCoordinateRequest(AbstractModel):
    """SignContractByCoordinate请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名ContractMng\n        :type Module: str\n        :param Operation: 操作名SignContractByCoordinate\n        :type Operation: str\n        :param ContractResId: 合同ID\n        :type ContractResId: str\n        :param AccountResId: 帐户ID\n        :type AccountResId: str\n        :param SignLocations: 签署坐标，坐标原点在文件左下角，坐标单位为磅，坐标不得超过合同文件边界\n        :type SignLocations: list of SignLocation\n        :param AuthorizationTime: 授权时间（由平台自动填充）\n        :type AuthorizationTime: str\n        :param Position: 授权IP地址（由平台自动填充）\n        :type Position: str\n        :param SealResId: 签章ID\n        :type SealResId: str\n        :param CertType: 选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1\n        :type CertType: int\n        :param ImageData: 签名图片，base64编码\n        :type ImageData: str\n        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignContractByKeywordRequest(AbstractModel):
    """SignContractByKeyword请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名ContractMng\n        :type Module: str\n        :param Operation: 操作名SignContractByKeyword\n        :type Operation: str\n        :param ContractResId: 合同ID\n        :type ContractResId: str\n        :param AccountResId: 账户ID\n        :type AccountResId: str\n        :param SignKeyword: 签署关键字，偏移坐标原点为关键字中心\n        :type SignKeyword: :class:`tencentcloud.ds.v20180523.models.SignKeyword`\n        :param AuthorizationTime: 授权时间（由平台自动填充）\n        :type AuthorizationTime: str\n        :param Position: 授权IP地址（由平台自动填充）\n        :type Position: str\n        :param SealResId: 签章ID\n        :type SealResId: str\n        :param CertType: 选用证书类型：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1\n        :type CertType: int\n        :param ImageData: 签名图片，base64编码\n        :type ImageData: str\n        """
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignInfo(AbstractModel):
    """签署人信息

    """

    def __init__(self):
        """
        :param AccountResId: 账户ID\n        :type AccountResId: str\n        :param AuthorizationTime: 授权时间（上传合同可不传该参数）\n        :type AuthorizationTime: str\n        :param Location: 授权IP地址（上传合同可不传该参数）\n        :type Location: str\n        :param SealId: 签章ID\n        :type SealId: str\n        :param ImageData: 签名图片，优先级比SealId高\n        :type ImageData: str\n        :param CertType: 默认值：1  表示RSA证书， 2 表示国密证书， 参数不传时默认为1\n        :type CertType: int\n        :param SignLocation: 签名域的标签值\n        :type SignLocation: str\n        """
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
        :param Keyword: 关键字\n        :type Keyword: str\n        :param OffsetCoordX: X轴偏移坐标\n        :type OffsetCoordX: str\n        :param OffsetCoordY: Y轴偏移坐标\n        :type OffsetCoordY: str\n        :param ImageWidth: 签章图片宽度\n        :type ImageWidth: str\n        :param ImageHeight: 签章图片高度\n        :type ImageHeight: str\n        """
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
        :param SignOnPage: 签名域页数\n        :type SignOnPage: str\n        :param SignLocationLBX: 签名域左下角X轴坐标轴\n        :type SignLocationLBX: str\n        :param SignLocationLBY: 签名域左下角Y轴坐标轴\n        :type SignLocationLBY: str\n        :param SignLocationRUX: 签名域右上角X轴坐标轴\n        :type SignLocationRUX: str\n        :param SignLocationRUY: 签名域右上角Y轴坐标轴\n        :type SignLocationRUY: str\n        """
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
        