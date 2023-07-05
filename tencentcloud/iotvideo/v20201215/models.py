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


class AIModelApplication(AbstractModel):
    """AI模型申请信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _Status: 申请状态：1-已申请；2-已取消；3-已拒绝；4-已通过
        :type Status: int
        """
        self._ProductId = None
        self._ProductName = None
        self._Status = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIModelInfo(AbstractModel):
    """AI模型信息

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _Status: 申请状态：1-已申请；2-已取消；3-已拒绝；4-已通过
        :type Status: int
        :param _Total: 可调用数量
        :type Total: int
        :param _Used: 已调用数量
        :type Used: int
        :param _ApplyTime: 申请时间
        :type ApplyTime: int
        :param _ApprovalTime: 审批通过时间
        :type ApprovalTime: int
        """
        self._ProductId = None
        self._ProductName = None
        self._Status = None
        self._Total = None
        self._Used = None
        self._ApplyTime = None
        self._ApprovalTime = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def ApplyTime(self):
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def ApprovalTime(self):
        return self._ApprovalTime

    @ApprovalTime.setter
    def ApprovalTime(self, ApprovalTime):
        self._ApprovalTime = ApprovalTime


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._Status = params.get("Status")
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._ApplyTime = params.get("ApplyTime")
        self._ApprovalTime = params.get("ApprovalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIModelUsageInfo(AbstractModel):
    """AI模型资源使用信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 开通时间
        :type CreateTime: int
        :param _Total: 资源总量
        :type Total: int
        :param _Used: 已使用资源数量
        :type Used: int
        """
        self._CreateTime = None
        self._Total = None
        self._Used = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionHistory(AbstractModel):
    """查询设备历史

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ActionId: 动作Id
        :type ActionId: str
        :param _ActionName: 动作名称
        :type ActionName: str
        :param _ReqTime: 请求时间
        :type ReqTime: int
        :param _RspTime: 响应时间
        :type RspTime: int
        :param _InputParams: 输入参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InputParams: str
        :param _OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param _Calling: 调用方式
        :type Calling: str
        :param _ClientToken: 调用Id
        :type ClientToken: str
        :param _Status: 调用状态
        :type Status: str
        """
        self._DeviceName = None
        self._ActionId = None
        self._ActionName = None
        self._ReqTime = None
        self._RspTime = None
        self._InputParams = None
        self._OutputParams = None
        self._Calling = None
        self._ClientToken = None
        self._Status = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ActionId(self):
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def ActionName(self):
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def ReqTime(self):
        return self._ReqTime

    @ReqTime.setter
    def ReqTime(self, ReqTime):
        self._ReqTime = ReqTime

    @property
    def RspTime(self):
        return self._RspTime

    @RspTime.setter
    def RspTime(self, RspTime):
        self._RspTime = RspTime

    @property
    def InputParams(self):
        return self._InputParams

    @InputParams.setter
    def InputParams(self, InputParams):
        self._InputParams = InputParams

    @property
    def OutputParams(self):
        return self._OutputParams

    @OutputParams.setter
    def OutputParams(self, OutputParams):
        self._OutputParams = OutputParams

    @property
    def Calling(self):
        return self._Calling

    @Calling.setter
    def Calling(self, Calling):
        self._Calling = Calling

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._ActionId = params.get("ActionId")
        self._ActionName = params.get("ActionName")
        self._ReqTime = params.get("ReqTime")
        self._RspTime = params.get("RspTime")
        self._InputParams = params.get("InputParams")
        self._OutputParams = params.get("OutputParams")
        self._Calling = params.get("Calling")
        self._ClientToken = params.get("ClientToken")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyAIModelRequest(AbstractModel):
    """ApplyAIModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: AI模型ID
        :type ModelId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ModelId = None
        self._ProductId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyAIModelResponse(AbstractModel):
    """ApplyAIModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class BalanceTransaction(AbstractModel):
    """账户流水

    """

    def __init__(self):
        r"""
        :param _AccountType: 账户类型：1-设备接入 2-云存。
        :type AccountType: int
        :param _Operation: 账户变更类型：Rechareg-充值；CreateOrder-新购。
        :type Operation: str
        :param _DealId: 流水ID。
        :type DealId: str
        :param _Amount: 变更金额，单位：分（人民币）。
        :type Amount: int
        :param _Balance: 变更后账户余额，单位：分（人民币）。
        :type Balance: int
        :param _OperationTime: 变更时间。
        :type OperationTime: int
        """
        self._AccountType = None
        self._Operation = None
        self._DealId = None
        self._Amount = None
        self._Balance = None
        self._OperationTime = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def DealId(self):
        return self._DealId

    @DealId.setter
    def DealId(self, DealId):
        self._DealId = DealId

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def OperationTime(self):
        return self._OperationTime

    @OperationTime.setter
    def OperationTime(self, OperationTime):
        self._OperationTime = OperationTime


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Operation = params.get("Operation")
        self._DealId = params.get("DealId")
        self._Amount = params.get("Amount")
        self._Balance = params.get("Balance")
        self._OperationTime = params.get("OperationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareRequest(AbstractModel):
    """BatchUpdateFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件新版本号
        :type FirmwareVersion: str
        :param _FirmwareOriVersion: 固件原版本号，根据文件列表升级固件不需要填写此参数
        :type FirmwareOriVersion: str
        :param _UpgradeMethod: 升级方式，0 静默升级  1 用户确认升级。 不填默认为静默升级方式
        :type UpgradeMethod: int
        :param _FileName: 设备列表文件名称，根据文件列表升级固件需要填写此参数
        :type FileName: str
        :param _FileMd5: 设备列表的文件md5值
        :type FileMd5: str
        :param _FileSize: 设备列表的文件大小值
        :type FileSize: int
        :param _DeviceNames: 需要升级的设备名称列表
        :type DeviceNames: list of str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._FirmwareOriVersion = None
        self._UpgradeMethod = None
        self._FileName = None
        self._FileMd5 = None
        self._FileSize = None
        self._DeviceNames = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareOriVersion(self):
        return self._FirmwareOriVersion

    @FirmwareOriVersion.setter
    def FirmwareOriVersion(self, FirmwareOriVersion):
        self._FirmwareOriVersion = FirmwareOriVersion

    @property
    def UpgradeMethod(self):
        return self._UpgradeMethod

    @UpgradeMethod.setter
    def UpgradeMethod(self, UpgradeMethod):
        self._UpgradeMethod = UpgradeMethod

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileMd5(self):
        return self._FileMd5

    @FileMd5.setter
    def FileMd5(self, FileMd5):
        self._FileMd5 = FileMd5

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def DeviceNames(self):
        return self._DeviceNames

    @DeviceNames.setter
    def DeviceNames(self, DeviceNames):
        self._DeviceNames = DeviceNames


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FirmwareOriVersion = params.get("FirmwareOriVersion")
        self._UpgradeMethod = params.get("UpgradeMethod")
        self._FileName = params.get("FileName")
        self._FileMd5 = params.get("FileMd5")
        self._FileSize = params.get("FileSize")
        self._DeviceNames = params.get("DeviceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchUpdateFirmwareResponse(AbstractModel):
    """BatchUpdateFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class BindCloudStorageUserRequest(AbstractModel):
    """BindCloudStorageUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudStorageUserResponse(AbstractModel):
    """BindCloudStorageUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CancelAIModelApplicationRequest(AbstractModel):
    """CancelAIModelApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: AI模型ID
        :type ModelId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ModelId = None
        self._ProductId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelAIModelApplicationResponse(AbstractModel):
    """CancelAIModelApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CancelDeviceFirmwareTaskRequest(AbstractModel):
    """CancelDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._DeviceName = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelDeviceFirmwareTaskResponse(AbstractModel):
    """CancelDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CheckForwardAuthRequest(AbstractModel):
    """CheckForwardAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Skey: 控制台Skey
        :type Skey: str
        :param _QueueType: 队列类型 0.CMQ  1.Ckafka
        :type QueueType: int
        """
        self._Skey = None
        self._QueueType = None

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType


    def _deserialize(self, params):
        self._Skey = params.get("Skey")
        self._QueueType = params.get("QueueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckForwardAuthResponse(AbstractModel):
    """CheckForwardAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoint: 腾讯云账号
        :type Endpoint: str
        :param _Result: 结果
        :type Result: int
        :param _Productid: 产品ID
        :type Productid: str
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        :param _QueueType: 队列类型 0.CMQ  1.Ckafka
        :type QueueType: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoint = None
        self._Result = None
        self._Productid = None
        self._ErrMsg = None
        self._QueueType = None
        self._RequestId = None

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Productid(self):
        return self._Productid

    @Productid.setter
    def Productid(self, Productid):
        self._Productid = Productid

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._Result = params.get("Result")
        self._Productid = params.get("Productid")
        self._ErrMsg = params.get("ErrMsg")
        self._QueueType = params.get("QueueType")
        self._RequestId = params.get("RequestId")


class CloudStorageEvent(AbstractModel):
    """云存事件

    """

    def __init__(self):
        r"""
        :param _StartTime: 事件起始时间（Unix 时间戳，秒级
        :type StartTime: int
        :param _EndTime: 事件结束时间（Unix 时间戳，秒级
        :type EndTime: int
        :param _Thumbnail: 事件缩略图
        :type Thumbnail: str
        :param _EventId: 事件ID
        :type EventId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Thumbnail = None
        self._EventId = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Thumbnail(self):
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Thumbnail = params.get("Thumbnail")
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageTimeData(AbstractModel):
    """云存时间轴接口返回数据

    """

    def __init__(self):
        r"""
        :param _TimeList: 云存时间轴信息列表
        :type TimeList: list of CloudStorageTimeInfo
        :param _VideoURL: 播放地址
        :type VideoURL: str
        """
        self._TimeList = None
        self._VideoURL = None

    @property
    def TimeList(self):
        return self._TimeList

    @TimeList.setter
    def TimeList(self, TimeList):
        self._TimeList = TimeList

    @property
    def VideoURL(self):
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL


    def _deserialize(self, params):
        if params.get("TimeList") is not None:
            self._TimeList = []
            for item in params.get("TimeList"):
                obj = CloudStorageTimeInfo()
                obj._deserialize(item)
                self._TimeList.append(obj)
        self._VideoURL = params.get("VideoURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageTimeInfo(AbstractModel):
    """云存时间轴信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorageUserInfo(AbstractModel):
    """云存用户信息

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceDataRequest(AbstractModel):
    """ControlDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Data: 属性数据, JSON格式字符串, 注意字段需要在物模型属性里定义
        :type Data: str
        :param _Method: 请求类型 , 不填该参数或者 desired 表示下发属性给设备,  reported 表示模拟设备上报属性
        :type Method: str
        :param _DataTimestamp: 上报数据UNIX时间戳(毫秒), 仅对Method:reported有效
        :type DataTimestamp: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Data = None
        self._Method = None
        self._DataTimestamp = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DataTimestamp(self):
        return self._DataTimestamp

    @DataTimestamp.setter
    def DataTimestamp(self, DataTimestamp):
        self._DataTimestamp = DataTimestamp


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Data = params.get("Data")
        self._Method = params.get("Method")
        self._DataTimestamp = params.get("DataTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回信息
        :type Data: str
        :param _Result: JSON字符串， 返回下发控制的结果信息, 
Sent = 1 表示设备已经在线并且订阅了控制下发的mqtt topic
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Result = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateAIDetectionRequest(AbstractModel):
    """CreateAIDetection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ModelId: AI模型ID
        :type ModelId: str
        :param _StartTime: 图片上传的开始时间
        :type StartTime: int
        :param _EndTime: 图片上传的结束时间
        :type EndTime: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._ModelId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ModelId = params.get("ModelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIDetectionResponse(AbstractModel):
    """CreateAIDetection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreateBatchRequest(AbstractModel):
    """CreateBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DevNum: 批次创建的设备数量
        :type DevNum: int
        :param _DevPre: 批次创建的设备前缀。不超过24个字符
        :type DevPre: str
        """
        self._ProductId = None
        self._DevNum = None
        self._DevPre = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DevNum(self):
        return self._DevNum

    @DevNum.setter
    def DevNum(self, DevNum):
        self._DevNum = DevNum

    @property
    def DevPre(self):
        return self._DevPre

    @DevPre.setter
    def DevPre(self, DevPre):
        self._DevPre = DevPre


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DevNum = params.get("DevNum")
        self._DevPre = params.get("DevPre")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchResponse(AbstractModel):
    """CreateBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BatchId = None
        self._RequestId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        self._RequestId = params.get("RequestId")


class CreateCOSCredentialsRequest(AbstractModel):
    """CreateCOSCredentials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCOSCredentialsResponse(AbstractModel):
    """CreateCOSCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StorageBucket: COS存储桶名称
        :type StorageBucket: str
        :param _StorageRegion: COS存储桶区域
        :type StorageRegion: str
        :param _StoragePath: COS存储桶路径
        :type StoragePath: str
        :param _SecretID: COS上传用的SecretID
        :type SecretID: str
        :param _SecretKey: COS上传用的SecretKey
        :type SecretKey: str
        :param _Token: COS上传用的Token
        :type Token: str
        :param _ExpiredTime: 密钥信息过期时间
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StorageBucket = None
        self._StorageRegion = None
        self._StoragePath = None
        self._SecretID = None
        self._SecretKey = None
        self._Token = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def StorageBucket(self):
        return self._StorageBucket

    @StorageBucket.setter
    def StorageBucket(self, StorageBucket):
        self._StorageBucket = StorageBucket

    @property
    def StorageRegion(self):
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def StoragePath(self):
        return self._StoragePath

    @StoragePath.setter
    def StoragePath(self, StoragePath):
        self._StoragePath = StoragePath

    @property
    def SecretID(self):
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._StorageBucket = params.get("StorageBucket")
        self._StorageRegion = params.get("StorageRegion")
        self._StoragePath = params.get("StoragePath")
        self._SecretID = params.get("SecretID")
        self._SecretKey = params.get("SecretKey")
        self._Token = params.get("Token")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class CreateCloudStorageRequest(AbstractModel):
    """CreateCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _PackageId: 云存套餐ID：
yc1m3d ： 全时3天存储月套餐。
yc1m7d ： 全时7天存储月套餐。
yc1m30d ：全时30天存储月套餐。
yc1y3d ：全时3天存储年套餐。
yc1y7d ：全时7天存储年套餐。
yc1y30d ：全时30天存储年套餐。
ye1m3d ：事件3天存储月套餐。
ye1m7d ：事件7天存储月套餐。
ye1m30d ：事件30天存储月套餐 。
ye1y3d ：事件3天存储年套餐。
ye1y7d ：事件7天存储年套餐。
ye1y30d ：事件30天存储年套餐。
yc1w7d : 全时7天存储周套餐。
ye1w7d : 事件7天存储周套餐。
        :type PackageId: str
        :param _Override: 如果当前设备已开启云存套餐，Override=1会使用新套餐覆盖原有套餐。不传此参数则默认为0。
        :type Override: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._PackageId = None
        self._Override = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Override(self):
        return self._Override

    @Override.setter
    def Override(self, Override):
        self._Override = Override


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._PackageId = params.get("PackageId")
        self._Override = params.get("Override")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudStorageResponse(AbstractModel):
    """CreateCloudStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreateDataForwardRequest(AbstractModel):
    """CreateDataForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _ForwardAddr: 转发地址。如果有鉴权Token，则需要自行传入，例如 [{\"forward\":{\"api\":\"http://123.207.117.108:1080/sub.php\",\"token\":\"testtoken\"}}]
        :type ForwardAddr: str
        :param _DataChose: 1-数据信息转发 2-设备上下线状态转发 3-数据信息转发&设备上下线状态转发
        :type DataChose: int
        """
        self._ProductId = None
        self._ForwardAddr = None
        self._DataChose = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ForwardAddr(self):
        return self._ForwardAddr

    @ForwardAddr.setter
    def ForwardAddr(self, ForwardAddr):
        self._ForwardAddr = ForwardAddr

    @property
    def DataChose(self):
        return self._DataChose

    @DataChose.setter
    def DataChose(self, DataChose):
        self._DataChose = DataChose


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ForwardAddr = params.get("ForwardAddr")
        self._DataChose = params.get("DataChose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataForwardResponse(AbstractModel):
    """CreateDataForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CreateForwardRuleRequest(AbstractModel):
    """CreateForwardRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _MsgType: 消息类型
        :type MsgType: int
        :param _Skey: 控制台Skey
        :type Skey: str
        :param _QueueRegion: 队列区域
        :type QueueRegion: str
        :param _QueueType: 队列类型 0.CMQ  1.Ckafka
        :type QueueType: int
        :param _Consecretid: 临时密钥
        :type Consecretid: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _QueueID: 队列或主题ID
        :type QueueID: str
        :param _QueueName: 队列或主题名称
        :type QueueName: str
        """
        self._ProductID = None
        self._MsgType = None
        self._Skey = None
        self._QueueRegion = None
        self._QueueType = None
        self._Consecretid = None
        self._InstanceId = None
        self._InstanceName = None
        self._QueueID = None
        self._QueueName = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def MsgType(self):
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def QueueRegion(self):
        return self._QueueRegion

    @QueueRegion.setter
    def QueueRegion(self, QueueRegion):
        self._QueueRegion = QueueRegion

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def Consecretid(self):
        return self._Consecretid

    @Consecretid.setter
    def Consecretid(self, Consecretid):
        self._Consecretid = Consecretid

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
    def QueueID(self):
        return self._QueueID

    @QueueID.setter
    def QueueID(self, QueueID):
        self._QueueID = QueueID

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._MsgType = params.get("MsgType")
        self._Skey = params.get("Skey")
        self._QueueRegion = params.get("QueueRegion")
        self._QueueType = params.get("QueueType")
        self._Consecretid = params.get("Consecretid")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._QueueID = params.get("QueueID")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardRuleResponse(AbstractModel):
    """CreateForwardRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoint: 腾讯云账号
        :type Endpoint: str
        :param _QueueName: 队列名
        :type QueueName: str
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _MsgType: 消息类型
        :type MsgType: int
        :param _Result: 结果
        :type Result: int
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _RoleID: 角色ID
        :type RoleID: int
        :param _QueueRegion: 队列区
        :type QueueRegion: str
        :param _QueueType: 消息队列的类型。 0：CMQ，1：Ckafka
        :type QueueType: int
        :param _InstanceId: 实例id， 目前只有Ckafka会用到
        :type InstanceId: str
        :param _InstanceName: 实例名称，目前只有Ckafka会用到
        :type InstanceName: str
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoint = None
        self._QueueName = None
        self._ProductID = None
        self._MsgType = None
        self._Result = None
        self._RoleName = None
        self._RoleID = None
        self._QueueRegion = None
        self._QueueType = None
        self._InstanceId = None
        self._InstanceName = None
        self._ErrMsg = None
        self._RequestId = None

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def MsgType(self):
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleID(self):
        return self._RoleID

    @RoleID.setter
    def RoleID(self, RoleID):
        self._RoleID = RoleID

    @property
    def QueueRegion(self):
        return self._QueueRegion

    @QueueRegion.setter
    def QueueRegion(self, QueueRegion):
        self._QueueRegion = QueueRegion

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

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
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._QueueName = params.get("QueueName")
        self._ProductID = params.get("ProductID")
        self._MsgType = params.get("MsgType")
        self._Result = params.get("Result")
        self._RoleName = params.get("RoleName")
        self._RoleID = params.get("RoleID")
        self._QueueRegion = params.get("QueueRegion")
        self._QueueType = params.get("QueueType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ErrMsg = params.get("ErrMsg")
        self._RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _DeviceType: 产品设备类型 1.普通设备 2.NVR设备
        :type DeviceType: int
        :param _ProductVaildYears: 产品有效期
        :type ProductVaildYears: int
        :param _Features: 设备功能码 ypsxth音频双向通话 spdxth视频单向通话
        :type Features: list of str
        :param _ChipOs: 设备操作系统，通用设备填default
        :type ChipOs: str
        :param _ChipManufactureId: 芯片厂商id，通用设备填default
        :type ChipManufactureId: str
        :param _ChipId: 芯片id，通用设备填default
        :type ChipId: str
        :param _ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param _EncryptionType: 认证方式 只支持取值为2 psk认证
        :type EncryptionType: int
        :param _NetType: 连接类型，wifi表示WIFI连接，cellular表示4G连接
        :type NetType: str
        """
        self._ProductName = None
        self._DeviceType = None
        self._ProductVaildYears = None
        self._Features = None
        self._ChipOs = None
        self._ChipManufactureId = None
        self._ChipId = None
        self._ProductDescription = None
        self._EncryptionType = None
        self._NetType = None

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ProductVaildYears(self):
        return self._ProductVaildYears

    @ProductVaildYears.setter
    def ProductVaildYears(self, ProductVaildYears):
        self._ProductVaildYears = ProductVaildYears

    @property
    def Features(self):
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def ChipOs(self):
        return self._ChipOs

    @ChipOs.setter
    def ChipOs(self, ChipOs):
        self._ChipOs = ChipOs

    @property
    def ChipManufactureId(self):
        return self._ChipManufactureId

    @ChipManufactureId.setter
    def ChipManufactureId(self, ChipManufactureId):
        self._ChipManufactureId = ChipManufactureId

    @property
    def ChipId(self):
        return self._ChipId

    @ChipId.setter
    def ChipId(self, ChipId):
        self._ChipId = ChipId

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def EncryptionType(self):
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._DeviceType = params.get("DeviceType")
        self._ProductVaildYears = params.get("ProductVaildYears")
        self._Features = params.get("Features")
        self._ChipOs = params.get("ChipOs")
        self._ChipManufactureId = params.get("ChipManufactureId")
        self._ChipId = params.get("ChipId")
        self._ProductDescription = params.get("ProductDescription")
        self._EncryptionType = params.get("EncryptionType")
        self._NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 产品详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`
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
            self._Data = VideoProduct()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateTaskFileUrlRequest(AbstractModel):
    """CreateTaskFileUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTaskFileUrlResponse(AbstractModel):
    """CreateTaskFileUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 任务文件上传链接
        :type Url: str
        :param _FileName: 任务文件名
        :type FileName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._FileName = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._FileName = params.get("FileName")
        self._RequestId = params.get("RequestId")


class DataForward(AbstractModel):
    """数据转发描述

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _ForwardAddr: 转发地址。
        :type ForwardAddr: str
        :param _Status: 转发状态。
        :type Status: int
        :param _CreateTime: 创建时间。
        :type CreateTime: int
        :param _UpdateTime: 更新时间。
        :type UpdateTime: int
        :param _DataChose: 1-数据信息转发 2-设备上下线状态转发 3-数据信息转发&设备上下线状态转发
注意：此字段可能返回 null，表示取不到有效值。
        :type DataChose: int
        """
        self._ProductId = None
        self._ForwardAddr = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DataChose = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ForwardAddr(self):
        return self._ForwardAddr

    @ForwardAddr.setter
    def ForwardAddr(self, ForwardAddr):
        self._ForwardAddr = ForwardAddr

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DataChose(self):
        return self._DataChose

    @DataChose.setter
    def DataChose(self, DataChose):
        self._DataChose = DataChose


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ForwardAddr = params.get("ForwardAddr")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DataChose = params.get("DataChose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _DeviceName: 设备名称。
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteFirmwareRequest(AbstractModel):
    """DeleteFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        """
        self._ProductID = None
        self._FirmwareVersion = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFirmwareResponse(AbstractModel):
    """DeleteFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DeleteForwardRuleRequest(AbstractModel):
    """DeleteForwardRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Skey: 控制台Skey
        :type Skey: str
        :param _QueueType: 队列类型
        :type QueueType: int
        :param _QueueName: 队列名称
        :type QueueName: str
        """
        self._ProductID = None
        self._Skey = None
        self._QueueType = None
        self._QueueName = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._Skey = params.get("Skey")
        self._QueueType = params.get("QueueType")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardRuleResponse(AbstractModel):
    """DeleteForwardRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoint: 腾讯云账号
        :type Endpoint: str
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Result: 删除结果 0成功 其他不成功
        :type Result: int
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoint = None
        self._QueueName = None
        self._ProductID = None
        self._Result = None
        self._ErrMsg = None
        self._RequestId = None

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._QueueName = params.get("QueueName")
        self._ProductID = params.get("ProductID")
        self._Result = params.get("Result")
        self._ErrMsg = params.get("ErrMsg")
        self._RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeAIModelApplicationsRequest(AbstractModel):
    """DescribeAIModelApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _Limit: 分页的大小，最大100
        :type Limit: int
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ModelId = None
        self._Limit = None
        self._Offset = None
        self._ProductId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelApplicationsResponse(AbstractModel):
    """DescribeAIModelApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 申请记录数量
        :type TotalCount: int
        :param _Applications: 申请记录数组
        :type Applications: list of AIModelApplication
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Applications = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Applications(self):
        return self._Applications

    @Applications.setter
    def Applications(self, Applications):
        self._Applications = Applications

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Applications") is not None:
            self._Applications = []
            for item in params.get("Applications"):
                obj = AIModelApplication()
                obj._deserialize(item)
                self._Applications.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAIModelChannelRequest(AbstractModel):
    """DescribeAIModelChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ModelId = None
        self._ProductId = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelChannelResponse(AbstractModel):
    """DescribeAIModelChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 推送类型。ckafka：消息队列；forward：http/https推送
        :type Type: str
        :param _ForwardAddress: 第三方推送地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardAddress: str
        :param _ForwardKey: 第三方推送密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardKey: str
        :param _CKafkaRegion: ckafka地域
注意：此字段可能返回 null，表示取不到有效值。
        :type CKafkaRegion: str
        :param _CKafkaInstance: ckafka实例
注意：此字段可能返回 null，表示取不到有效值。
        :type CKafkaInstance: str
        :param _CKafkaTopic: ckafka订阅主题
注意：此字段可能返回 null，表示取不到有效值。
        :type CKafkaTopic: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Type = None
        self._ForwardAddress = None
        self._ForwardKey = None
        self._CKafkaRegion = None
        self._CKafkaInstance = None
        self._CKafkaTopic = None
        self._RequestId = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ForwardAddress(self):
        return self._ForwardAddress

    @ForwardAddress.setter
    def ForwardAddress(self, ForwardAddress):
        self._ForwardAddress = ForwardAddress

    @property
    def ForwardKey(self):
        return self._ForwardKey

    @ForwardKey.setter
    def ForwardKey(self, ForwardKey):
        self._ForwardKey = ForwardKey

    @property
    def CKafkaRegion(self):
        return self._CKafkaRegion

    @CKafkaRegion.setter
    def CKafkaRegion(self, CKafkaRegion):
        self._CKafkaRegion = CKafkaRegion

    @property
    def CKafkaInstance(self):
        return self._CKafkaInstance

    @CKafkaInstance.setter
    def CKafkaInstance(self, CKafkaInstance):
        self._CKafkaInstance = CKafkaInstance

    @property
    def CKafkaTopic(self):
        return self._CKafkaTopic

    @CKafkaTopic.setter
    def CKafkaTopic(self, CKafkaTopic):
        self._CKafkaTopic = CKafkaTopic

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ForwardAddress = params.get("ForwardAddress")
        self._ForwardKey = params.get("ForwardKey")
        self._CKafkaRegion = params.get("CKafkaRegion")
        self._CKafkaInstance = params.get("CKafkaInstance")
        self._CKafkaTopic = params.get("CKafkaTopic")
        self._RequestId = params.get("RequestId")


class DescribeAIModelUsageRequest(AbstractModel):
    """DescribeAIModelUsage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Offset: 偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页的大小，最大100
        :type Limit: int
        """
        self._ModelId = None
        self._ProductId = None
        self._Offset = None
        self._Limit = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelUsageResponse(AbstractModel):
    """DescribeAIModelUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: AI模型资源包总量
        :type TotalCount: int
        :param _UsageInfo: AI模型资源包信息数组
        :type UsageInfo: list of AIModelUsageInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UsageInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UsageInfo(self):
        return self._UsageInfo

    @UsageInfo.setter
    def UsageInfo(self, UsageInfo):
        self._UsageInfo = UsageInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UsageInfo") is not None:
            self._UsageInfo = []
            for item in params.get("UsageInfo"):
                obj = AIModelUsageInfo()
                obj._deserialize(item)
                self._UsageInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAIModelsRequest(AbstractModel):
    """DescribeAIModels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _Status: 申请状态：1-已申请；2-已取消；3-已拒绝；4-已通过
        :type Status: int
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _Limit: 分页的大小，最大100
        :type Limit: int
        """
        self._ModelId = None
        self._Status = None
        self._Offset = None
        self._Limit = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIModelsResponse(AbstractModel):
    """DescribeAIModels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: AI模型数量
        :type TotalCount: int
        :param _Models: AI模型信息数组
        :type Models: list of AIModelInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Models = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Models(self):
        return self._Models

    @Models.setter
    def Models(self, Models):
        self._Models = Models

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Models") is not None:
            self._Models = []
            for item in params.get("Models"):
                obj = AIModelInfo()
                obj._deserialize(item)
                self._Models.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBalanceRequest(AbstractModel):
    """DescribeBalance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 账户类型：1-设备接入；2-云存。
        :type AccountType: int
        """
        self._AccountType = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBalanceResponse(AbstractModel):
    """DescribeBalance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Balance: 账户余额，单位：分（人民币）。
        :type Balance: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Balance = None
        self._RequestId = None

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Balance = params.get("Balance")
        self._RequestId = params.get("RequestId")


class DescribeBalanceTransactionsRequest(AbstractModel):
    """DescribeBalanceTransactions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountType: 账户类型：1-设备接入；2-云存。
        :type AccountType: int
        :param _Offset: 分页游标开始，默认为0开始拉取第一条。
        :type Offset: int
        :param _Limit: 分页每页数量。
        :type Limit: int
        :param _Operation: 流水类型：All-全部类型；Recharge-充值；CreateOrder-新购。默认为All
        :type Operation: str
        """
        self._AccountType = None
        self._Offset = None
        self._Limit = None
        self._Operation = None

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

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
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._AccountType = params.get("AccountType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBalanceTransactionsResponse(AbstractModel):
    """DescribeBalanceTransactions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 账户流水总数。
        :type TotalCount: int
        :param _Transactions: 账户流水详情数组。
        :type Transactions: list of BalanceTransaction
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Transactions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Transactions(self):
        return self._Transactions

    @Transactions.setter
    def Transactions(self, Transactions):
        self._Transactions = Transactions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Transactions") is not None:
            self._Transactions = []
            for item in params.get("Transactions"):
                obj = BalanceTransaction()
                obj._deserialize(item)
                self._Transactions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBatchRequest(AbstractModel):
    """DescribeBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BatchId: 批次ID
        :type BatchId: int
        """
        self._BatchId = None

    @property
    def BatchId(self):
        return self._BatchId

    @BatchId.setter
    def BatchId(self, BatchId):
        self._BatchId = BatchId


    def _deserialize(self, params):
        self._BatchId = params.get("BatchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchResponse(AbstractModel):
    """DescribeBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 批次详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoBatch`
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
            self._Data = VideoBatch()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeBatchsRequest(AbstractModel):
    """DescribeBatchs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Limit: 分页的大小，最大100
        :type Limit: int
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        """
        self._ProductId = None
        self._Limit = None
        self._Offset = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchsResponse(AbstractModel):
    """DescribeBatchs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 批次数量
        :type TotalCount: int
        :param _Data: 批次列表详情
        :type Data: list of VideoBatch
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VideoBatch()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCategoryRequest(AbstractModel):
    """DescribeCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: Category ID。
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCategoryResponse(AbstractModel):
    """DescribeCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: Category详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.ProductTemplate`
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
            self._Data = ProductTemplate()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageDateRequest(AbstractModel):
    """DescribeCloudStorageDate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageDateResponse(AbstractModel):
    """DescribeCloudStorageDate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 云存日期数组，["2021-01-05","2021-01-06"]
        :type Data: list of str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageEventsRequest(AbstractModel):
    """DescribeCloudStorageEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param _EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param _Context: 请求上下文, 用作查询游标
        :type Context: str
        :param _Size: 查询数据项目的最大数量, 默认为10。假设传Size=10，返回的实际事件数量为N，则 5 <= N <= 10。
        :type Size: int
        :param _EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _ChannelId: 通道ID 非NVR设备则不填 NVR设备则必填 默认为无
        :type ChannelId: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._Size = None
        self._EventId = None
        self._UserId = None
        self._ChannelId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Context = params.get("Context")
        self._Size = params.get("Size")
        self._EventId = params.get("EventId")
        self._UserId = params.get("UserId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageEventsResponse(AbstractModel):
    """DescribeCloudStorageEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: 云存事件列表
        :type Events: list of CloudStorageEvent
        :param _Context: 请求上下文, 用作查询游标
        :type Context: str
        :param _Listover: 拉取结果是否已经结束
        :type Listover: bool
        :param _Total: 内部结果数量，并不等同于事件总数。
        :type Total: int
        :param _VideoURL: 视频播放URL
        :type VideoURL: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._Context = None
        self._Listover = None
        self._Total = None
        self._VideoURL = None
        self._RequestId = None

    @property
    def Events(self):
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def VideoURL(self):
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = CloudStorageEvent()
                obj._deserialize(item)
                self._Events.append(obj)
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        self._Total = params.get("Total")
        self._VideoURL = params.get("VideoURL")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageRequest(AbstractModel):
    """DescribeCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 云存用户ID
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageResponse(AbstractModel):
    """DescribeCloudStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 云存开启状态，1为开启，0为未开启或已过期
        :type Status: int
        :param _Type: 云存类型，1为全时云存，2为事件云存
        :type Type: int
        :param _ExpireTime: 云存套餐过期时间
        :type ExpireTime: int
        :param _ShiftDuration: 云存回看时长
        :type ShiftDuration: int
        :param _UserId: 云存用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Type = None
        self._ExpireTime = None
        self._ShiftDuration = None
        self._UserId = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ShiftDuration(self):
        return self._ShiftDuration

    @ShiftDuration.setter
    def ShiftDuration(self, ShiftDuration):
        self._ShiftDuration = ShiftDuration

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._ExpireTime = params.get("ExpireTime")
        self._ShiftDuration = params.get("ShiftDuration")
        self._UserId = params.get("UserId")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageThumbnailRequest(AbstractModel):
    """DescribeCloudStorageThumbnail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Thumbnail: 缩略图文件名
        :type Thumbnail: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Thumbnail = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Thumbnail(self):
        return self._Thumbnail

    @Thumbnail.setter
    def Thumbnail(self, Thumbnail):
        self._Thumbnail = Thumbnail


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageThumbnailResponse(AbstractModel):
    """DescribeCloudStorageThumbnail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ThumbnailURL: 缩略图访问地址
        :type ThumbnailURL: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ThumbnailURL = None
        self._RequestId = None

    @property
    def ThumbnailURL(self):
        return self._ThumbnailURL

    @ThumbnailURL.setter
    def ThumbnailURL(self, ThumbnailURL):
        self._ThumbnailURL = ThumbnailURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ThumbnailURL = params.get("ThumbnailURL")
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageTimeRequest(AbstractModel):
    """DescribeCloudStorageTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Date: 云存日期，例如"2020-01-05"
        :type Date: str
        :param _StartTime: 开始时间，unix时间
        :type StartTime: int
        :param _EndTime: 结束时间，unix时间
        :type EndTime: int
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Date = None
        self._StartTime = None
        self._EndTime = None
        self._UserId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Date = params.get("Date")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageTimeResponse(AbstractModel):
    """DescribeCloudStorageTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 接口返回数据
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.CloudStorageTimeData`
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
            self._Data = CloudStorageTimeData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCloudStorageUsersRequest(AbstractModel):
    """DescribeCloudStorageUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Limit: 分页拉取数量
        :type Limit: int
        :param _Offset: 分页拉取偏移
        :type Offset: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._Limit = None
        self._Offset = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudStorageUsersResponse(AbstractModel):
    """DescribeCloudStorageUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 用户总数
        :type TotalCount: int
        :param _Users: 用户信息
        :type Users: list of CloudStorageUserInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Users = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = CloudStorageUserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDataForwardListRequest(AbstractModel):
    """DescribeDataForwardList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductIds: 产品ID列表
        :type ProductIds: str
        """
        self._ProductIds = None

    @property
    def ProductIds(self):
        return self._ProductIds

    @ProductIds.setter
    def ProductIds(self, ProductIds):
        self._ProductIds = ProductIds


    def _deserialize(self, params):
        self._ProductIds = params.get("ProductIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataForwardListResponse(AbstractModel):
    """DescribeDataForwardList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataForwardList: 数据转发列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataForwardList: list of DataForward
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataForwardList = None
        self._RequestId = None

    @property
    def DataForwardList(self):
        return self._DataForwardList

    @DataForwardList.setter
    def DataForwardList(self, DataForwardList):
        self._DataForwardList = DataForwardList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DataForwardList") is not None:
            self._DataForwardList = []
            for item in params.get("DataForwardList"):
                obj = DataForward()
                obj._deserialize(item)
                self._DataForwardList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceActionHistoryRequest(AbstractModel):
    """DescribeDeviceActionHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _MinTime: 开始范围的 unix 毫秒时间戳
        :type MinTime: int
        :param _MaxTime: 结束范围的 unix 毫秒时间戳
        :type MaxTime: int
        :param _ActionId: 动作Id
        :type ActionId: str
        :param _Limit: 查询条数 默认为0 最大不超过500
        :type Limit: int
        :param _Context: 游标，标识查询位置。
        :type Context: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._MinTime = None
        self._MaxTime = None
        self._ActionId = None
        self._Limit = None
        self._Context = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def ActionId(self):
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._ActionId = params.get("ActionId")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceActionHistoryResponse(AbstractModel):
    """DescribeDeviceActionHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCounts: 总条数
        :type TotalCounts: int
        :param _ActionHistories: 动作历史
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionHistories: list of ActionHistory
        :param _Context: 用于标识查询结果的上下文，翻页用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _Listover: 搜索结果是否已经结束。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCounts = None
        self._ActionHistories = None
        self._Context = None
        self._Listover = None
        self._RequestId = None

    @property
    def TotalCounts(self):
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def ActionHistories(self):
        return self._ActionHistories

    @ActionHistories.setter
    def ActionHistories(self, ActionHistories):
        self._ActionHistories = ActionHistories

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCounts = params.get("TotalCounts")
        if params.get("ActionHistories") is not None:
            self._ActionHistories = []
            for item in params.get("ActionHistories"):
                obj = ActionHistory()
                obj._deserialize(item)
                self._ActionHistories.append(obj)
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        self._RequestId = params.get("RequestId")


class DescribeDeviceCommLogRequest(AbstractModel):
    """DescribeDeviceCommLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 开始时间 13位时间戳 单位毫秒
        :type MinTime: int
        :param _MaxTime: 结束时间 13位时间戳 单位毫秒
        :type MaxTime: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Limit: 返回条数 默认为50
        :type Limit: int
        :param _Context: 检索上下文
        :type Context: str
        :param _Type: 类型：shadow 下行，device 上行 默认为空则全部查询
        :type Type: str
        """
        self._MinTime = None
        self._MaxTime = None
        self._ProductId = None
        self._DeviceName = None
        self._Limit = None
        self._Context = None
        self._Type = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceCommLogResponse(AbstractModel):
    """DescribeDeviceCommLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
        :type Listover: bool
        :param _Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
        :type Context: str
        :param _Results: 日志数据结果数组，返回对应时间点及取值。
        :type Results: list of DeviceCommLogItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listover = None
        self._Context = None
        self._Results = None
        self._RequestId = None

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Listover = params.get("Listover")
        self._Context = params.get("Context")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DeviceCommLogItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 区间开始时间（Unix 时间戳，毫秒级）
        :type MinTime: int
        :param _MaxTime: 区间结束时间（Unix 时间戳，毫秒级）
        :type MaxTime: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FieldName: 属性字段名称，对应数据模板中功能属性的标识符
        :type FieldName: str
        :param _Limit: 返回条数
        :type Limit: list of int non-negative
        :param _Context: 检索上下文
        :type Context: str
        """
        self._MinTime = None
        self._MaxTime = None
        self._ProductId = None
        self._DeviceName = None
        self._FieldName = None
        self._Limit = None
        self._Context = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._FieldName = params.get("FieldName")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FieldName: 属性字段名称，对应数据模板中功能属性的标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param _Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param _Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FieldName = None
        self._Listover = None
        self._Context = None
        self._Results = None
        self._RequestId = None

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._Listover = params.get("Listover")
        self._Context = params.get("Context")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 设备数据
        :type Data: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDeviceEventHistoryRequest(AbstractModel):
    """DescribeDeviceEventHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Type: 搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件
        :type Type: str
        :param _StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param _EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param _Context: 搜索上下文, 用作查询游标
        :type Context: str
        :param _Size: 单次获取的历史数据项目的最大数量, 缺省10
        :type Size: int
        :param _EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._Context = None
        self._Size = None
        self._EventId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Context = params.get("Context")
        self._Size = params.get("Size")
        self._EventId = params.get("EventId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceEventHistoryResponse(AbstractModel):
    """DescribeDeviceEventHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param _EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type EventHistory: list of EventHistoryItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Total = None
        self._Listover = None
        self._EventHistory = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def EventHistory(self):
        return self._EventHistory

    @EventHistory.setter
    def EventHistory(self, EventHistory):
        self._EventHistory = EventHistory

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Total = params.get("Total")
        self._Listover = params.get("Listover")
        if params.get("EventHistory") is not None:
            self._EventHistory = []
            for item in params.get("EventHistory"):
                obj = EventHistoryItem()
                obj._deserialize(item)
                self._EventHistory.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活
        :type Online: int
        :param _LoginTime: 设备最后上线时间
        :type LoginTime: int
        :param _DevicePsk: 设备密钥
        :type DevicePsk: str
        :param _EnableState: 设备启用状态
        :type EnableState: int
        :param _ExpireTime: 设备过期时间
        :type ExpireTime: int
        :param _LogLevel: 设备的sdk日志等级，0：关闭，1：错误，2：告警，3：信息，4：调试
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceName = None
        self._Online = None
        self._LoginTime = None
        self._DevicePsk = None
        self._EnableState = None
        self._ExpireTime = None
        self._LogLevel = None
        self._RequestId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Online = params.get("Online")
        self._LoginTime = params.get("LoginTime")
        self._DevicePsk = params.get("DevicePsk")
        self._EnableState = params.get("EnableState")
        self._ExpireTime = params.get("ExpireTime")
        self._LogLevel = params.get("LogLevel")
        self._RequestId = params.get("RequestId")


class DescribeDeviceStatusLogRequest(AbstractModel):
    """DescribeDeviceStatusLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 开始时间（毫秒）
        :type MinTime: int
        :param _MaxTime: 结束时间（毫秒）
        :type MaxTime: int
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Limit: 返回条数
        :type Limit: int
        :param _Context: 检索上下文
        :type Context: str
        """
        self._MinTime = None
        self._MaxTime = None
        self._ProductId = None
        self._DeviceName = None
        self._Limit = None
        self._Context = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceStatusLogResponse(AbstractModel):
    """DescribeDeviceStatusLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param _Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param _Results: 日志数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of DeviceStatusLogItem
        :param _TotalCount: 日志数据结果总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listover = None
        self._Context = None
        self._Results = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Listover = params.get("Listover")
        self._Context = params.get("Context")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = DeviceStatusLogItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param _Limit: 分页的大小，最大100
        :type Limit: int
        :param _DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._Offset = None
        self._Limit = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

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
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 设备总数
        :type TotalCount: int
        :param _Devices: 设备详细信息列表
        :type Devices: list of DeviceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Devices = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirmwareRequest(AbstractModel):
    """DescribeFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self._ProductID = None
        self._FirmwareVersion = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareResponse(AbstractModel):
    """DescribeFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: 固件版本号
        :type Version: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Name: 固件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 固件描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Md5sum: 固件Md5值
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5sum: str
        :param _Createtime: 固件上传的秒级时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type Createtime: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._ProductId = None
        self._Name = None
        self._Description = None
        self._Md5sum = None
        self._Createtime = None
        self._ProductName = None
        self._RequestId = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Md5sum(self):
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def Createtime(self):
        return self._Createtime

    @Createtime.setter
    def Createtime(self, Createtime):
        self._Createtime = Createtime

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._ProductId = params.get("ProductId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Md5sum = params.get("Md5sum")
        self._Createtime = params.get("Createtime")
        self._ProductName = params.get("ProductName")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskDevicesRequest(AbstractModel):
    """DescribeFirmwareTaskDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        :param _Filters: 筛选条件
        :type Filters: list of SearchKeyword
        :param _Offset: 查询偏移量 默认为0
        :type Offset: int
        :param _Limit: 查询的数量 默认为50
        :type Limit: int
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDevicesResponse(AbstractModel):
    """DescribeFirmwareTaskDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 固件升级任务的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Devices: 固件升级任务的设备列表
        :type Devices: list of DeviceUpdateStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Devices = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Devices(self):
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceUpdateStatus()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskDistributionRequest(AbstractModel):
    """DescribeFirmwareTaskDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskDistributionResponse(AbstractModel):
    """DescribeFirmwareTaskDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatusInfos: 固件升级任务状态分布信息
        :type StatusInfos: list of StatusStatistic
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatusInfos = None
        self._RequestId = None

    @property
    def StatusInfos(self):
        return self._StatusInfos

    @StatusInfos.setter
    def StatusInfos(self, StatusInfos):
        self._StatusInfos = StatusInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatusInfos") is not None:
            self._StatusInfos = []
            for item in params.get("StatusInfos"):
                obj = StatusStatistic()
                obj._deserialize(item)
                self._StatusInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskRequest(AbstractModel):
    """DescribeFirmwareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskResponse(AbstractModel):
    """DescribeFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 固件任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _Status: 固件任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 固件任务创建时间，单位:秒
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _Type: 固件任务升级类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _UpgradeMode: 固件任务升级模式。originalVersion（按版本号升级）、filename（提交文件升级）、devicenames（按设备名称升级）
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeMode: str
        :param _ProductId: 产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _OriginalVersion: 原始固件版本号，在UpgradeMode是originalVersion升级模式下会返回
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginalVersion: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._CreateTime = None
        self._Type = None
        self._ProductName = None
        self._UpgradeMode = None
        self._ProductId = None
        self._OriginalVersion = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def UpgradeMode(self):
        return self._UpgradeMode

    @UpgradeMode.setter
    def UpgradeMode(self, UpgradeMode):
        self._UpgradeMode = UpgradeMode

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def OriginalVersion(self):
        return self._OriginalVersion

    @OriginalVersion.setter
    def OriginalVersion(self, OriginalVersion):
        self._OriginalVersion = OriginalVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Type = params.get("Type")
        self._ProductName = params.get("ProductName")
        self._UpgradeMode = params.get("UpgradeMode")
        self._ProductId = params.get("ProductId")
        self._OriginalVersion = params.get("OriginalVersion")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTaskStatisticsRequest(AbstractModel):
    """DescribeFirmwareTaskStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        """
        self._ProductID = None
        self._FirmwareVersion = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTaskStatisticsResponse(AbstractModel):
    """DescribeFirmwareTaskStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessTotal: 升级成功的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotal: int
        :param _FailureTotal: 升级失败的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureTotal: int
        :param _UpgradingTotal: 正在升级的设备总数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradingTotal: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessTotal = None
        self._FailureTotal = None
        self._UpgradingTotal = None
        self._RequestId = None

    @property
    def SuccessTotal(self):
        return self._SuccessTotal

    @SuccessTotal.setter
    def SuccessTotal(self, SuccessTotal):
        self._SuccessTotal = SuccessTotal

    @property
    def FailureTotal(self):
        return self._FailureTotal

    @FailureTotal.setter
    def FailureTotal(self, FailureTotal):
        self._FailureTotal = FailureTotal

    @property
    def UpgradingTotal(self):
        return self._UpgradingTotal

    @UpgradingTotal.setter
    def UpgradingTotal(self, UpgradingTotal):
        self._UpgradingTotal = UpgradingTotal

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessTotal = params.get("SuccessTotal")
        self._FailureTotal = params.get("FailureTotal")
        self._UpgradingTotal = params.get("UpgradingTotal")
        self._RequestId = params.get("RequestId")


class DescribeFirmwareTasksRequest(AbstractModel):
    """DescribeFirmwareTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 返回查询结果条数
        :type Limit: int
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirmwareTasksResponse(AbstractModel):
    """DescribeFirmwareTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskInfos: 固件升级任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskInfos: list of FirmwareTaskInfo
        :param _Total: 固件升级任务总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskInfos = None
        self._Total = None
        self._RequestId = None

    @property
    def TaskInfos(self):
        return self._TaskInfos

    @TaskInfos.setter
    def TaskInfos(self, TaskInfos):
        self._TaskInfos = TaskInfos

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self._TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = FirmwareTaskInfo()
                obj._deserialize(item)
                self._TaskInfos.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeForwardRuleRequest(AbstractModel):
    """DescribeForwardRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Skey: 控制台Skey
        :type Skey: str
        :param _QueueType: 队列类型，0：CMQ，1：Ckafka
        :type QueueType: int
        :param _Consecretid: 临时密钥
        :type Consecretid: str
        """
        self._ProductID = None
        self._Skey = None
        self._QueueType = None
        self._Consecretid = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def Consecretid(self):
        return self._Consecretid

    @Consecretid.setter
    def Consecretid(self, Consecretid):
        self._Consecretid = Consecretid


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._Skey = params.get("Skey")
        self._QueueType = params.get("QueueType")
        self._Consecretid = params.get("Consecretid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeForwardRuleResponse(AbstractModel):
    """DescribeForwardRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoint: 腾讯云账号
        :type Endpoint: str
        :param _QueueName: 队列名称
        :type QueueName: str
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _MsgType: 消息类型 1设备上报信息 2设备状态变化通知 3为全选
        :type MsgType: int
        :param _Result: 结果 2表示禁用 其他为成功
        :type Result: int
        :param _RoleName: 角色名
        :type RoleName: str
        :param _RoleID: 角色ID
        :type RoleID: int
        :param _QueueRegion: 队列区域
        :type QueueRegion: str
        :param _QueueType: 队列类型，0：CMQ，1：Ckafka
        :type QueueType: int
        :param _InstanceId: 实例id， 目前只有Ckafka会用到
        :type InstanceId: str
        :param _InstanceName: 实例名称，目前只有Ckafka会用到
        :type InstanceName: str
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoint = None
        self._QueueName = None
        self._ProductID = None
        self._MsgType = None
        self._Result = None
        self._RoleName = None
        self._RoleID = None
        self._QueueRegion = None
        self._QueueType = None
        self._InstanceId = None
        self._InstanceName = None
        self._ErrMsg = None
        self._RequestId = None

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def MsgType(self):
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleID(self):
        return self._RoleID

    @RoleID.setter
    def RoleID(self, RoleID):
        self._RoleID = RoleID

    @property
    def QueueRegion(self):
        return self._QueueRegion

    @QueueRegion.setter
    def QueueRegion(self, QueueRegion):
        self._QueueRegion = QueueRegion

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

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
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._QueueName = params.get("QueueName")
        self._ProductID = params.get("ProductID")
        self._MsgType = params.get("MsgType")
        self._Result = params.get("Result")
        self._RoleName = params.get("RoleName")
        self._RoleID = params.get("RoleID")
        self._QueueRegion = params.get("QueueRegion")
        self._QueueType = params.get("QueueType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ErrMsg = params.get("ErrMsg")
        self._RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 产品数据模板
        :type Model: :class:`tencentcloud.iotvideo.v20201215.models.ProductModelDefinition`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Model = None
        self._RequestId = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ProductModelDefinition()
            self._Model._deserialize(params.get("Model"))
        self._RequestId = params.get("RequestId")


class DescribeProductDynamicRegisterRequest(AbstractModel):
    """DescribeProductDynamicRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductDynamicRegisterResponse(AbstractModel):
    """DescribeProductDynamicRegister返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterType: 动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :type RegisterType: int
        :param _ProductSecret: 动态注册产品密钥
        :type ProductSecret: str
        :param _RegisterLimit: 动态注册设备上限
        :type RegisterLimit: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegisterType = None
        self._ProductSecret = None
        self._RegisterLimit = None
        self._RequestId = None

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegisterType = params.get("RegisterType")
        self._ProductSecret = params.get("ProductSecret")
        self._RegisterLimit = params.get("RegisterLimit")
        self._RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: str
        """
        self._ProductId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 产品详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`
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
            self._Data = VideoProduct()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页的大小，最大100
        :type Limit: int
        :param _Offset: 偏移量，Offset从0开始
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 产品详情列表
        :type Data: list of VideoProduct
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VideoProduct()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSDKLogRequest(AbstractModel):
    """DescribeSDKLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MinTime: 日志开始时间
        :type MinTime: int
        :param _MaxTime: 日志结束时间
        :type MaxTime: int
        :param _Keywords: 查询关键字，可以同时支持键值查询和文本查询，
例如，查询某key的值为value，并且包含某word的日志，该参数为：key:value word。
键值或文本可以包含多个，以空格隔开。
其中可以索引的key包括：productid、devicename、loglevel
一个典型的查询示例：productid:7JK1G72JNE devicename:name publish loglevel:WARN一个典型的查询示例：productid:ABCDE12345 devicename:test scene:SHADOW publish
        :type Keywords: str
        :param _Context: 日志检索上下文
        :type Context: str
        :param _MaxNum: 查询条数
        :type MaxNum: int
        """
        self._MinTime = None
        self._MaxTime = None
        self._Keywords = None
        self._Context = None
        self._MaxNum = None

    @property
    def MinTime(self):
        return self._MinTime

    @MinTime.setter
    def MinTime(self, MinTime):
        self._MinTime = MinTime

    @property
    def MaxTime(self):
        return self._MaxTime

    @MaxTime.setter
    def MaxTime(self, MaxTime):
        self._MaxTime = MaxTime

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def MaxNum(self):
        return self._MaxNum

    @MaxNum.setter
    def MaxNum(self, MaxNum):
        self._MaxNum = MaxNum


    def _deserialize(self, params):
        self._MinTime = params.get("MinTime")
        self._MaxTime = params.get("MaxTime")
        self._Keywords = params.get("Keywords")
        self._Context = params.get("Context")
        self._MaxNum = params.get("MaxNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSDKLogResponse(AbstractModel):
    """DescribeSDKLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 日志检索上下文
        :type Context: str
        :param _Listover: 是否还有日志，如有仍有日志，下次查询的请求带上当前请求返回的Context
        :type Listover: bool
        :param _Results: 日志列表
        :type Results: list of SDKLogItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._Listover = None
        self._Results = None
        self._RequestId = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = SDKLogItem()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceCommLogItem(AbstractModel):
    """设备通讯日志查询返回条目

    """

    def __init__(self):
        r"""
        :param _Time: 时间
        :type Time: str
        :param _Type: 日志类型，device 设备上行，shadow 服务端下行。
        :type Type: str
        :param _Data: 通讯数据。
        :type Data: str
        """
        self._Time = None
        self._Type = None
        self._Data = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Type = params.get("Type")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        r"""
        :param _Time: 时间点，毫秒时间戳
        :type Time: str
        :param _Value: 字段取值
        :type Value: str
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活
        :type Online: int
        :param _LoginTime: 设备最后上线时间
        :type LoginTime: int
        :param _DevicePsk: 设备密钥
        :type DevicePsk: str
        :param _EnableState: 设备启用状态 0为停用 1为可用
        :type EnableState: int
        :param _ExpireTime: 设备过期时间
        :type ExpireTime: int
        :param _LogLevel: 设备的sdk日志等级，0：关闭，1：错误，2：告警，3：信息，4：调试
注意：此字段可能返回 null，表示取不到有效值。
        :type LogLevel: int
        """
        self._DeviceName = None
        self._Online = None
        self._LoginTime = None
        self._DevicePsk = None
        self._EnableState = None
        self._ExpireTime = None
        self._LogLevel = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def LoginTime(self):
        return self._LoginTime

    @LoginTime.setter
    def LoginTime(self, LoginTime):
        self._LoginTime = LoginTime

    @property
    def DevicePsk(self):
        return self._DevicePsk

    @DevicePsk.setter
    def DevicePsk(self, DevicePsk):
        self._DevicePsk = DevicePsk

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._Online = params.get("Online")
        self._LoginTime = params.get("LoginTime")
        self._DevicePsk = params.get("DevicePsk")
        self._EnableState = params.get("EnableState")
        self._ExpireTime = params.get("ExpireTime")
        self._LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceStatusLogItem(AbstractModel):
    """设备上下线日志记录

    """

    def __init__(self):
        r"""
        :param _Time: 时间
        :type Time: str
        :param _Type: 状态类型： Online 上线，Offline 下线
        :type Type: str
        :param _Data: 日志信息
        :type Data: str
        """
        self._Time = None
        self._Type = None
        self._Data = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Type = params.get("Type")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceUpdateStatus(AbstractModel):
    """设备固件更新状态

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名
        :type DeviceName: str
        :param _LastProcessTime: 最后处理时间
        :type LastProcessTime: int
        :param _Status: 状态
        :type Status: int
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        :param _Retcode: 返回码
        :type Retcode: int
        :param _DstVersion: 目标更新版本
        :type DstVersion: str
        :param _Percent: 下载中状态时的下载进度
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: int
        :param _OriVersion: 原版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type OriVersion: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        """
        self._DeviceName = None
        self._LastProcessTime = None
        self._Status = None
        self._ErrMsg = None
        self._Retcode = None
        self._DstVersion = None
        self._Percent = None
        self._OriVersion = None
        self._TaskId = None

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LastProcessTime(self):
        return self._LastProcessTime

    @LastProcessTime.setter
    def LastProcessTime(self, LastProcessTime):
        self._LastProcessTime = LastProcessTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Retcode(self):
        return self._Retcode

    @Retcode.setter
    def Retcode(self, Retcode):
        self._Retcode = Retcode

    @property
    def DstVersion(self):
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def OriVersion(self):
        return self._OriVersion

    @OriVersion.setter
    def OriVersion(self, OriVersion):
        self._OriVersion = OriVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._LastProcessTime = params.get("LastProcessTime")
        self._Status = params.get("Status")
        self._ErrMsg = params.get("ErrMsg")
        self._Retcode = params.get("Retcode")
        self._DstVersion = params.get("DstVersion")
        self._Percent = params.get("Percent")
        self._OriVersion = params.get("OriVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditFirmwareRequest(AbstractModel):
    """EditFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID。
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号。
        :type FirmwareVersion: str
        :param _FirmwareName: 固件名称。
        :type FirmwareName: str
        :param _FirmwareDescription: 固件描述。
        :type FirmwareDescription: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._FirmwareName = None
        self._FirmwareDescription = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def FirmwareName(self):
        return self._FirmwareName

    @FirmwareName.setter
    def FirmwareName(self, FirmwareName):
        self._FirmwareName = FirmwareName

    @property
    def FirmwareDescription(self):
        return self._FirmwareDescription

    @FirmwareDescription.setter
    def FirmwareDescription(self, FirmwareDescription):
        self._FirmwareDescription = FirmwareDescription


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._FirmwareName = params.get("FirmwareName")
        self._FirmwareDescription = params.get("FirmwareDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditFirmwareResponse(AbstractModel):
    """EditFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        r"""
        :param _TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        :param _ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param _DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param _EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param _Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self._TimeStamp = None
        self._ProductId = None
        self._DeviceName = None
        self._EventId = None
        self._Type = None
        self._Data = None

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._TimeStamp = params.get("TimeStamp")
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._EventId = params.get("EventId")
        self._Type = params.get("Type")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirmwareInfo(AbstractModel):
    """设备固件详细信息

    """

    def __init__(self):
        r"""
        :param _Version: 固件版本
        :type Version: str
        :param _Md5sum: 固件MD5值
        :type Md5sum: str
        :param _CreateTime: 固件创建时间
        :type CreateTime: int
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _Name: 固件名称
        :type Name: str
        :param _Description: 固件描述
        :type Description: str
        :param _ProductId: 产品ID
        :type ProductId: str
        """
        self._Version = None
        self._Md5sum = None
        self._CreateTime = None
        self._ProductName = None
        self._Name = None
        self._Description = None
        self._ProductId = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Md5sum(self):
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Md5sum = params.get("Md5sum")
        self._CreateTime = params.get("CreateTime")
        self._ProductName = params.get("ProductName")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ProductId = params.get("ProductId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FirmwareTaskInfo(AbstractModel):
    """固件升级任务信息

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param _Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _CreateTime: 任务创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        """
        self._TaskId = None
        self._Status = None
        self._Type = None
        self._CreateTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateSignedVideoURLRequest(AbstractModel):
    """GenerateSignedVideoURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoURL: 视频播放原始URL地址
        :type VideoURL: str
        :param _ExpireTime: 播放链接过期时间
        :type ExpireTime: int
        """
        self._VideoURL = None
        self._ExpireTime = None

    @property
    def VideoURL(self):
        return self._VideoURL

    @VideoURL.setter
    def VideoURL(self, VideoURL):
        self._VideoURL = VideoURL

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._VideoURL = params.get("VideoURL")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateSignedVideoURLResponse(AbstractModel):
    """GenerateSignedVideoURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignedVideoURL: 视频防盗链播放URL
        :type SignedVideoURL: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignedVideoURL = None
        self._RequestId = None

    @property
    def SignedVideoURL(self):
        return self._SignedVideoURL

    @SignedVideoURL.setter
    def SignedVideoURL(self, SignedVideoURL):
        self._SignedVideoURL = SignedVideoURL

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignedVideoURL = params.get("SignedVideoURL")
        self._RequestId = params.get("RequestId")


class GetAllFirmwareVersionRequest(AbstractModel):
    """GetAllFirmwareVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        """
        self._ProductID = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAllFirmwareVersionResponse(AbstractModel):
    """GetAllFirmwareVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: 固件可用版本列表
        :type Version: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._RequestId = params.get("RequestId")


class GetFirmwareURLRequest(AbstractModel):
    """GetFirmwareURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本
        :type FirmwareVersion: str
        """
        self._ProductID = None
        self._FirmwareVersion = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFirmwareURLResponse(AbstractModel):
    """GetFirmwareURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 固件URL
        :type Url: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class ImportModelDefinitionRequest(AbstractModel):
    """ImportModelDefinition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
        self._ProductId = None
        self._ModelSchema = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ModelSchema(self):
        return self._ModelSchema

    @ModelSchema.setter
    def ModelSchema(self, ModelSchema):
        self._ModelSchema = ModelSchema


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ModelSchema = params.get("ModelSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportModelDefinitionResponse(AbstractModel):
    """ImportModelDefinition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class InheritCloudStorageUserRequest(AbstractModel):
    """InheritCloudStorageUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _UserId: 原始用户ID
        :type UserId: str
        :param _ToUserId: 目标用户ID
        :type ToUserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._UserId = None
        self._ToUserId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ToUserId(self):
        return self._ToUserId

    @ToUserId.setter
    def ToUserId(self, ToUserId):
        self._ToUserId = ToUserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._UserId = params.get("UserId")
        self._ToUserId = params.get("ToUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InheritCloudStorageUserResponse(AbstractModel):
    """InheritCloudStorageUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ListFirmwaresRequest(AbstractModel):
    """ListFirmwares请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 获取的页数
        :type PageNum: int
        :param _PageSize: 分页的大小
        :type PageSize: int
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Filters: 搜索过滤条件
        :type Filters: list of SearchKeyword
        """
        self._PageNum = None
        self._PageSize = None
        self._ProductID = None
        self._Filters = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProductID = params.get("ProductID")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = SearchKeyword()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFirmwaresResponse(AbstractModel):
    """ListFirmwares返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 固件总数
        :type TotalCount: int
        :param _Firmwares: 固件列表
        :type Firmwares: list of FirmwareInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Firmwares = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Firmwares(self):
        return self._Firmwares

    @Firmwares.setter
    def Firmwares(self, Firmwares):
        self._Firmwares = Firmwares

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Firmwares") is not None:
            self._Firmwares = []
            for item in params.get("Firmwares"):
                obj = FirmwareInfo()
                obj._deserialize(item)
                self._Firmwares.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyDataForwardRequest(AbstractModel):
    """ModifyDataForward请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _ForwardAddr: 转发地址。如果有鉴权Token，则需要自行传入，例如 [{\"forward\":{\"api\":\"http://123.207.117.108:1080/sub.php\",\"token\":\"testtoken\"}}]
        :type ForwardAddr: str
        :param _DataChose: 1-数据信息转发 2-设备上下线状态转发 3-数据信息转发&设备上下线状态转发
        :type DataChose: int
        """
        self._ProductId = None
        self._ForwardAddr = None
        self._DataChose = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ForwardAddr(self):
        return self._ForwardAddr

    @ForwardAddr.setter
    def ForwardAddr(self, ForwardAddr):
        self._ForwardAddr = ForwardAddr

    @property
    def DataChose(self):
        return self._DataChose

    @DataChose.setter
    def DataChose(self, DataChose):
        self._DataChose = DataChose


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ForwardAddr = params.get("ForwardAddr")
        self._DataChose = params.get("DataChose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataForwardResponse(AbstractModel):
    """ModifyDataForward返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDataForwardStatusRequest(AbstractModel):
    """ModifyDataForwardStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID。
        :type ProductId: str
        :param _Status: 转发状态，1启用，0禁用。
        :type Status: int
        """
        self._ProductId = None
        self._Status = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDataForwardStatusResponse(AbstractModel):
    """ModifyDataForwardStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDeviceLogLevelRequest(AbstractModel):
    """ModifyDeviceLogLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _LogLevel: 日志级别，0：关闭，1：错误，2：告警，3：信息，4：调试
        :type LogLevel: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._LogLevel = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LogLevel(self):
        return self._LogLevel

    @LogLevel.setter
    def LogLevel(self, LogLevel):
        self._LogLevel = LogLevel


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._LogLevel = params.get("LogLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceLogLevelResponse(AbstractModel):
    """ModifyDeviceLogLevel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 设备所属产品id
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _EnableState: 要设置的设备状态，1为启用，0为禁用
        :type EnableState: int
        """
        self._ProductId = None
        self._DeviceName = None
        self._EnableState = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def EnableState(self):
        return self._EnableState

    @EnableState.setter
    def EnableState(self, EnableState):
        self._EnableState = EnableState


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._EnableState = params.get("EnableState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyForwardRuleRequest(AbstractModel):
    """ModifyForwardRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _MsgType: 消息类型
        :type MsgType: int
        :param _Skey: 控制台Skey
        :type Skey: str
        :param _QueueRegion: 队列区域
        :type QueueRegion: str
        :param _QueueType: 队列类型 0.CMQ 1.CKafka
        :type QueueType: int
        :param _Consecretid: 临时密钥
        :type Consecretid: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _QueueID: 队列或主题ID
        :type QueueID: str
        :param _QueueName: 队列或主题名称
        :type QueueName: str
        """
        self._ProductID = None
        self._MsgType = None
        self._Skey = None
        self._QueueRegion = None
        self._QueueType = None
        self._Consecretid = None
        self._InstanceId = None
        self._InstanceName = None
        self._QueueID = None
        self._QueueName = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def MsgType(self):
        return self._MsgType

    @MsgType.setter
    def MsgType(self, MsgType):
        self._MsgType = MsgType

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def QueueRegion(self):
        return self._QueueRegion

    @QueueRegion.setter
    def QueueRegion(self, QueueRegion):
        self._QueueRegion = QueueRegion

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def Consecretid(self):
        return self._Consecretid

    @Consecretid.setter
    def Consecretid(self, Consecretid):
        self._Consecretid = Consecretid

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
    def QueueID(self):
        return self._QueueID

    @QueueID.setter
    def QueueID(self, QueueID):
        self._QueueID = QueueID

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._MsgType = params.get("MsgType")
        self._Skey = params.get("Skey")
        self._QueueRegion = params.get("QueueRegion")
        self._QueueType = params.get("QueueType")
        self._Consecretid = params.get("Consecretid")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._QueueID = params.get("QueueID")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardRuleResponse(AbstractModel):
    """ModifyForwardRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoint: 腾讯云账号
        :type Endpoint: str
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _Result: 结果
        :type Result: int
        :param _ErrMsg: 错误信息
        :type ErrMsg: str
        :param _QueueType: 队列类型 0.CMQ 1.CKafka
        :type QueueType: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoint = None
        self._ProductID = None
        self._Result = None
        self._ErrMsg = None
        self._QueueType = None
        self._RequestId = None

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._ProductID = params.get("ProductID")
        self._Result = params.get("Result")
        self._ErrMsg = params.get("ErrMsg")
        self._QueueType = params.get("QueueType")
        self._RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
        self._ProductId = None
        self._ModelSchema = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ModelSchema(self):
        return self._ModelSchema

    @ModelSchema.setter
    def ModelSchema(self, ModelSchema):
        self._ModelSchema = ModelSchema


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ModelSchema = params.get("ModelSchema")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ModifyProductDynamicRegisterRequest(AbstractModel):
    """ModifyProductDynamicRegister请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _RegisterType: 动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :type RegisterType: int
        :param _RegisterLimit: 动态注册设备上限
        :type RegisterLimit: int
        """
        self._ProductId = None
        self._RegisterType = None
        self._RegisterLimit = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._RegisterType = params.get("RegisterType")
        self._RegisterLimit = params.get("RegisterLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProductDynamicRegisterResponse(AbstractModel):
    """ModifyProductDynamicRegister返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterType: 动态注册类型，0-关闭 1-预创建设备 2-自动创建设备
        :type RegisterType: int
        :param _ProductSecret: 动态注册产品密钥
        :type ProductSecret: str
        :param _RegisterLimit: 动态注册设备上限
        :type RegisterLimit: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegisterType = None
        self._ProductSecret = None
        self._RegisterLimit = None
        self._RequestId = None

    @property
    def RegisterType(self):
        return self._RegisterType

    @RegisterType.setter
    def RegisterType(self, RegisterType):
        self._RegisterType = RegisterType

    @property
    def ProductSecret(self):
        return self._ProductSecret

    @ProductSecret.setter
    def ProductSecret(self, ProductSecret):
        self._ProductSecret = ProductSecret

    @property
    def RegisterLimit(self):
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegisterType = params.get("RegisterType")
        self._ProductSecret = params.get("ProductSecret")
        self._RegisterLimit = params.get("RegisterLimit")
        self._RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品id
        :type ProductId: str
        :param _ProductName: 修改的产品名称 （支持中文、英文、数字、下划线组合，最多不超过20个字符）
        :type ProductName: str
        :param _ProductDescription: 修改的产品描述 （最多不超过128个字符）
        :type ProductDescription: str
        """
        self._ProductId = None
        self._ProductName = None
        self._ProductDescription = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._ProductDescription = params.get("ProductDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ModelDefine: 模型定义
        :type ModelDefine: str
        :param _UpdateTime: 更新时间，秒级时间戳
        :type UpdateTime: int
        :param _CreateTime: 创建时间，秒级时间戳
        :type CreateTime: int
        :param _CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryModel: str
        :param _NetTypeModel: 产品的连接类型的模型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetTypeModel: str
        """
        self._ProductId = None
        self._ModelDefine = None
        self._UpdateTime = None
        self._CreateTime = None
        self._CategoryModel = None
        self._NetTypeModel = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ModelDefine(self):
        return self._ModelDefine

    @ModelDefine.setter
    def ModelDefine(self, ModelDefine):
        self._ModelDefine = ModelDefine

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CategoryModel(self):
        return self._CategoryModel

    @CategoryModel.setter
    def CategoryModel(self, CategoryModel):
        self._CategoryModel = CategoryModel

    @property
    def NetTypeModel(self):
        return self._NetTypeModel

    @NetTypeModel.setter
    def NetTypeModel(self, NetTypeModel):
        self._NetTypeModel = NetTypeModel


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ModelDefine = params.get("ModelDefine")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._CategoryModel = params.get("CategoryModel")
        self._NetTypeModel = params.get("NetTypeModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductTemplate(AbstractModel):
    """产品分类实体

    """

    def __init__(self):
        r"""
        :param _Id: 实体ID
        :type Id: int
        :param _CategoryKey: 分类字段
        :type CategoryKey: str
        :param _CategoryName: 分类名称
        :type CategoryName: str
        :param _ParentId: 上层实体ID
        :type ParentId: int
        :param _ModelTemplate: 物模型
        :type ModelTemplate: str
        :param _ListOrder: 排列顺序
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOrder: int
        :param _IconUrl: 分类图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param _IconUrlGrid: 九宫格图片地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrlGrid: str
        """
        self._Id = None
        self._CategoryKey = None
        self._CategoryName = None
        self._ParentId = None
        self._ModelTemplate = None
        self._ListOrder = None
        self._IconUrl = None
        self._IconUrlGrid = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CategoryKey(self):
        return self._CategoryKey

    @CategoryKey.setter
    def CategoryKey(self, CategoryKey):
        self._CategoryKey = CategoryKey

    @property
    def CategoryName(self):
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def ParentId(self):
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def ModelTemplate(self):
        return self._ModelTemplate

    @ModelTemplate.setter
    def ModelTemplate(self, ModelTemplate):
        self._ModelTemplate = ModelTemplate

    @property
    def ListOrder(self):
        return self._ListOrder

    @ListOrder.setter
    def ListOrder(self, ListOrder):
        self._ListOrder = ListOrder

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def IconUrlGrid(self):
        return self._IconUrlGrid

    @IconUrlGrid.setter
    def IconUrlGrid(self, IconUrlGrid):
        self._IconUrlGrid = IconUrlGrid


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CategoryKey = params.get("CategoryKey")
        self._CategoryName = params.get("CategoryName")
        self._ParentId = params.get("ParentId")
        self._ModelTemplate = params.get("ModelTemplate")
        self._ListOrder = params.get("ListOrder")
        self._IconUrl = params.get("IconUrl")
        self._IconUrlGrid = params.get("IconUrlGrid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Topic: 消息发往的主题
        :type Topic: str
        :param _Payload: 云端下发到设备的控制报文
        :type Payload: str
        :param _Qos: 消息服务质量等级，取值为0或1
        :type Qos: int
        :param _PayloadEncoding: Payload的内容编码格式，取值为base64或空。base64表示云端将接收到的base64编码后的报文再转换成二进制报文下发至设备，为空表示不作转换，透传下发至设备
        :type PayloadEncoding: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._Topic = None
        self._Payload = None
        self._Qos = None
        self._PayloadEncoding = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def Qos(self):
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def PayloadEncoding(self):
        return self._PayloadEncoding

    @PayloadEncoding.setter
    def PayloadEncoding(self, PayloadEncoding):
        self._PayloadEncoding = PayloadEncoding


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._Topic = params.get("Topic")
        self._Payload = params.get("Payload")
        self._Qos = params.get("Qos")
        self._PayloadEncoding = params.get("PayloadEncoding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ReportAliveDeviceRequest(AbstractModel):
    """ReportAliveDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportAliveDeviceResponse(AbstractModel):
    """ReportAliveDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class ResetCloudStorageRequest(AbstractModel):
    """ResetCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _ChannelId: 通道ID 非NVR设备则不填 NVR设备则必填 默认为无
        :type ChannelId: int
        :param _UserId: 云存用户Id，为空则为默认云存空间。
        :type UserId: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ChannelId = None
        self._UserId = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetCloudStorageResponse(AbstractModel):
    """ResetCloudStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class RetryDeviceFirmwareTaskRequest(AbstractModel):
    """RetryDeviceFirmwareTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _TaskId: 固件升级任务ID
        :type TaskId: int
        """
        self._ProductID = None
        self._DeviceName = None
        self._FirmwareVersion = None
        self._TaskId = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDeviceFirmwareTaskResponse(AbstractModel):
    """RetryDeviceFirmwareTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class SDKLogItem(AbstractModel):
    """SDK日志项

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _Level: 日志等级
        :type Level: str
        :param _DateTime: 日志时间
        :type DateTime: str
        :param _Content: 日志内容
        :type Content: str
        """
        self._ProductID = None
        self._DeviceName = None
        self._Level = None
        self._DateTime = None
        self._Content = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def DateTime(self):
        return self._DateTime

    @DateTime.setter
    def DateTime(self, DateTime):
        self._DateTime = DateTime

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._DeviceName = params.get("DeviceName")
        self._Level = params.get("Level")
        self._DateTime = params.get("DateTime")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKeyword(AbstractModel):
    """搜索关键词

    """

    def __init__(self):
        r"""
        :param _Key: 搜索条件的Key
        :type Key: str
        :param _Value: 搜索条件的值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetForwardAuthRequest(AbstractModel):
    """SetForwardAuth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Skey: 控制台Skey
        :type Skey: str
        :param _QueueType: 消息队列类型  0.CMQ 1.CKafka
        :type QueueType: int
        """
        self._Skey = None
        self._QueueType = None

    @property
    def Skey(self):
        return self._Skey

    @Skey.setter
    def Skey(self, Skey):
        self._Skey = Skey

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType


    def _deserialize(self, params):
        self._Skey = params.get("Skey")
        self._QueueType = params.get("QueueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetForwardAuthResponse(AbstractModel):
    """SetForwardAuth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoint: 腾讯云账号
        :type Endpoint: str
        :param _Result: 结果
        :type Result: int
        :param _RoleName: 角色名
        :type RoleName: str
        :param _RoleID: 角色ID
        :type RoleID: int
        :param _QueueType: 消息队列类型  0.CMQ 1.CKafka
        :type QueueType: int
        :param _ErrMsg: 错误消息
        :type ErrMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoint = None
        self._Result = None
        self._RoleName = None
        self._RoleID = None
        self._QueueType = None
        self._ErrMsg = None
        self._RequestId = None

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleID(self):
        return self._RoleID

    @RoleID.setter
    def RoleID(self, RoleID):
        self._RoleID = RoleID

    @property
    def QueueType(self):
        return self._QueueType

    @QueueType.setter
    def QueueType(self, QueueType):
        self._QueueType = QueueType

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._Result = params.get("Result")
        self._RoleName = params.get("RoleName")
        self._RoleID = params.get("RoleID")
        self._QueueType = params.get("QueueType")
        self._ErrMsg = params.get("ErrMsg")
        self._RequestId = params.get("RequestId")


class StatusStatistic(AbstractModel):
    """状态统计信息

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Total: 统计总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._Status = None
        self._Total = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferCloudStorageRequest(AbstractModel):
    """TransferCloudStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 已开通云存的设备名称
        :type DeviceName: str
        :param _ToDeviceName: 未开通云存的设备名称
        :type ToDeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None
        self._ToDeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ToDeviceName(self):
        return self._ToDeviceName

    @ToDeviceName.setter
    def ToDeviceName(self, ToDeviceName):
        self._ToDeviceName = ToDeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        self._ToDeviceName = params.get("ToDeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferCloudStorageResponse(AbstractModel):
    """TransferCloudStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class UpdateAIModelChannelRequest(AbstractModel):
    """UpdateAIModelChannel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Type: 推送类型。ckafka：消息队列；forward：http/https推送
        :type Type: str
        :param _ForwardAddress: 第三方推送地址
        :type ForwardAddress: str
        :param _ForwardKey: 第三方推送密钥，不填写则腾讯云自动生成。
        :type ForwardKey: str
        :param _CKafkaRegion: ckafka地域
        :type CKafkaRegion: str
        :param _CKafkaInstance: ckafka实例
        :type CKafkaInstance: str
        :param _CKafkaTopic: ckafka订阅主题
        :type CKafkaTopic: str
        """
        self._ModelId = None
        self._ProductId = None
        self._Type = None
        self._ForwardAddress = None
        self._ForwardKey = None
        self._CKafkaRegion = None
        self._CKafkaInstance = None
        self._CKafkaTopic = None

    @property
    def ModelId(self):
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ForwardAddress(self):
        return self._ForwardAddress

    @ForwardAddress.setter
    def ForwardAddress(self, ForwardAddress):
        self._ForwardAddress = ForwardAddress

    @property
    def ForwardKey(self):
        return self._ForwardKey

    @ForwardKey.setter
    def ForwardKey(self, ForwardKey):
        self._ForwardKey = ForwardKey

    @property
    def CKafkaRegion(self):
        return self._CKafkaRegion

    @CKafkaRegion.setter
    def CKafkaRegion(self, CKafkaRegion):
        self._CKafkaRegion = CKafkaRegion

    @property
    def CKafkaInstance(self):
        return self._CKafkaInstance

    @CKafkaInstance.setter
    def CKafkaInstance(self, CKafkaInstance):
        self._CKafkaInstance = CKafkaInstance

    @property
    def CKafkaTopic(self):
        return self._CKafkaTopic

    @CKafkaTopic.setter
    def CKafkaTopic(self, CKafkaTopic):
        self._CKafkaTopic = CKafkaTopic


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._ProductId = params.get("ProductId")
        self._Type = params.get("Type")
        self._ForwardAddress = params.get("ForwardAddress")
        self._ForwardKey = params.get("ForwardKey")
        self._CKafkaRegion = params.get("CKafkaRegion")
        self._CKafkaInstance = params.get("CKafkaInstance")
        self._CKafkaTopic = params.get("CKafkaTopic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIModelChannelResponse(AbstractModel):
    """UpdateAIModelChannel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ForwardKey: 第三方推送密钥，如果选择自动生成则会返回此字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ForwardKey = None
        self._RequestId = None

    @property
    def ForwardKey(self):
        return self._ForwardKey

    @ForwardKey.setter
    def ForwardKey(self, ForwardKey):
        self._ForwardKey = ForwardKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ForwardKey = params.get("ForwardKey")
        self._RequestId = params.get("RequestId")


class UploadFirmwareRequest(AbstractModel):
    """UploadFirmware请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductID: 产品ID
        :type ProductID: str
        :param _FirmwareVersion: 固件版本号
        :type FirmwareVersion: str
        :param _Md5sum: 固件的MD5值
        :type Md5sum: str
        :param _FileSize: 固件的大小
        :type FileSize: int
        :param _FirmwareName: 固件名称
        :type FirmwareName: str
        :param _FirmwareDescription: 固件描述
        :type FirmwareDescription: str
        """
        self._ProductID = None
        self._FirmwareVersion = None
        self._Md5sum = None
        self._FileSize = None
        self._FirmwareName = None
        self._FirmwareDescription = None

    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self, ProductID):
        self._ProductID = ProductID

    @property
    def FirmwareVersion(self):
        return self._FirmwareVersion

    @FirmwareVersion.setter
    def FirmwareVersion(self, FirmwareVersion):
        self._FirmwareVersion = FirmwareVersion

    @property
    def Md5sum(self):
        return self._Md5sum

    @Md5sum.setter
    def Md5sum(self, Md5sum):
        self._Md5sum = Md5sum

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FirmwareName(self):
        return self._FirmwareName

    @FirmwareName.setter
    def FirmwareName(self, FirmwareName):
        self._FirmwareName = FirmwareName

    @property
    def FirmwareDescription(self):
        return self._FirmwareDescription

    @FirmwareDescription.setter
    def FirmwareDescription(self, FirmwareDescription):
        self._FirmwareDescription = FirmwareDescription


    def _deserialize(self, params):
        self._ProductID = params.get("ProductID")
        self._FirmwareVersion = params.get("FirmwareVersion")
        self._Md5sum = params.get("Md5sum")
        self._FileSize = params.get("FileSize")
        self._FirmwareName = params.get("FirmwareName")
        self._FirmwareDescription = params.get("FirmwareDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFirmwareResponse(AbstractModel):
    """UploadFirmware返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class VideoBatch(AbstractModel):
    """批次元数据

    """

    def __init__(self):
        r"""
        :param _Id: 批次ID
        :type Id: int
        :param _UserId: 用户ID
        :type UserId: str
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _Status: 状态：1：待创建设备 2：创建中 3：已完成
        :type Status: int
        :param _DevPre: 设备前缀
        :type DevPre: str
        :param _DevNum: 设备数量
        :type DevNum: int
        :param _DevNumCreated: 已创建设备数量
        :type DevNumCreated: int
        :param _BatchURL: 批次下载地址
        :type BatchURL: str
        :param _CreateTime: 创建时间。unix时间戳
        :type CreateTime: int
        :param _UpdateTime: 修改时间。unix时间戳
        :type UpdateTime: int
        """
        self._Id = None
        self._UserId = None
        self._ProductId = None
        self._Status = None
        self._DevPre = None
        self._DevNum = None
        self._DevNumCreated = None
        self._BatchURL = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DevPre(self):
        return self._DevPre

    @DevPre.setter
    def DevPre(self, DevPre):
        self._DevPre = DevPre

    @property
    def DevNum(self):
        return self._DevNum

    @DevNum.setter
    def DevNum(self, DevNum):
        self._DevNum = DevNum

    @property
    def DevNumCreated(self):
        return self._DevNumCreated

    @DevNumCreated.setter
    def DevNumCreated(self, DevNumCreated):
        self._DevNumCreated = DevNumCreated

    @property
    def BatchURL(self):
        return self._BatchURL

    @BatchURL.setter
    def BatchURL(self, BatchURL):
        self._BatchURL = BatchURL

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._UserId = params.get("UserId")
        self._ProductId = params.get("ProductId")
        self._Status = params.get("Status")
        self._DevPre = params.get("DevPre")
        self._DevNum = params.get("DevNum")
        self._DevNumCreated = params.get("DevNumCreated")
        self._BatchURL = params.get("BatchURL")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoProduct(AbstractModel):
    """video产品元数据

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _ProductName: 产品名称
        :type ProductName: str
        :param _DeviceType: 产品设备类型（普通设备)	1.普通设备
        :type DeviceType: int
        :param _EncryptionType: 认证方式：2：PSK
        :type EncryptionType: int
        :param _Features: 设备功能码
        :type Features: list of str
        :param _ChipOs: 操作系统
        :type ChipOs: str
        :param _ChipManufactureId: 芯片厂商id
        :type ChipManufactureId: str
        :param _ChipId: 芯片id
        :type ChipId: str
        :param _ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param _CreateTime: 创建时间unix时间戳
        :type CreateTime: int
        :param _UpdateTime: 修改时间unix时间戳
        :type UpdateTime: int
        :param _NetType: 连接类型，wifi表示WIFI连接，cellular表示4G连接
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        """
        self._ProductId = None
        self._ProductName = None
        self._DeviceType = None
        self._EncryptionType = None
        self._Features = None
        self._ChipOs = None
        self._ChipManufactureId = None
        self._ChipId = None
        self._ProductDescription = None
        self._CreateTime = None
        self._UpdateTime = None
        self._NetType = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ProductName(self):
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def EncryptionType(self):
        return self._EncryptionType

    @EncryptionType.setter
    def EncryptionType(self, EncryptionType):
        self._EncryptionType = EncryptionType

    @property
    def Features(self):
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def ChipOs(self):
        return self._ChipOs

    @ChipOs.setter
    def ChipOs(self, ChipOs):
        self._ChipOs = ChipOs

    @property
    def ChipManufactureId(self):
        return self._ChipManufactureId

    @ChipManufactureId.setter
    def ChipManufactureId(self, ChipManufactureId):
        self._ChipManufactureId = ChipManufactureId

    @property
    def ChipId(self):
        return self._ChipId

    @ChipId.setter
    def ChipId(self, ChipId):
        self._ChipId = ChipId

    @property
    def ProductDescription(self):
        return self._ProductDescription

    @ProductDescription.setter
    def ProductDescription(self, ProductDescription):
        self._ProductDescription = ProductDescription

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ProductName = params.get("ProductName")
        self._DeviceType = params.get("DeviceType")
        self._EncryptionType = params.get("EncryptionType")
        self._Features = params.get("Features")
        self._ChipOs = params.get("ChipOs")
        self._ChipManufactureId = params.get("ChipManufactureId")
        self._ChipId = params.get("ChipId")
        self._ProductDescription = params.get("ProductDescription")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WakeUpDeviceRequest(AbstractModel):
    """WakeUpDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品ID
        :type ProductId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        """
        self._ProductId = None
        self._DeviceName = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DeviceName(self):
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DeviceName = params.get("DeviceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WakeUpDeviceResponse(AbstractModel):
    """WakeUpDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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