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


class ActionHistory(AbstractModel):
    """查询设备历史

    """

    def __init__(self):
        """
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param ActionId: 动作Id
        :type ActionId: str
        :param ActionName: 动作名称
        :type ActionName: str
        :param ReqTime: 请求时间
        :type ReqTime: int
        :param RspTime: 响应时间
        :type RspTime: int
        :param InputParams: 输入参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InputParams: str
        :param OutputParams: 输出参数
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param Calling: 调用方式
        :type Calling: str
        :param ClientToken: 调用Id
        :type ClientToken: str
        :param Status: 调用状态
        :type Status: str
        """
        self.DeviceName = None
        self.ActionId = None
        self.ActionName = None
        self.ReqTime = None
        self.RspTime = None
        self.InputParams = None
        self.OutputParams = None
        self.Calling = None
        self.ClientToken = None
        self.Status = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.ActionName = params.get("ActionName")
        self.ReqTime = params.get("ReqTime")
        self.RspTime = params.get("RspTime")
        self.InputParams = params.get("InputParams")
        self.OutputParams = params.get("OutputParams")
        self.Calling = params.get("Calling")
        self.ClientToken = params.get("ClientToken")
        self.Status = params.get("Status")


class CheckForwardAuthRequest(AbstractModel):
    """CheckForwardAuth请求参数结构体

    """

    def __init__(self):
        """
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 队列类型
        :type QueueType: int
        """
        self.Skey = None
        self.QueueType = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")


class CheckForwardAuthResponse(AbstractModel):
    """CheckForwardAuth返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param Result: 结果
        :type Result: int
        :param Productid: 产品ID
        :type Productid: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Endpoint = None
        self.Result = None
        self.Productid = None
        self.ErrMsg = None
        self.QueueType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.Result = params.get("Result")
        self.Productid = params.get("Productid")
        self.ErrMsg = params.get("ErrMsg")
        self.QueueType = params.get("QueueType")
        self.RequestId = params.get("RequestId")


class CreateBatchRequest(AbstractModel):
    """CreateBatch请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DevNum: 批次创建的设备数量
        :type DevNum: int
        :param DevPre: 批次创建的设备前缀。不超过24个字符
        :type DevPre: str
        """
        self.ProductId = None
        self.DevNum = None
        self.DevPre = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DevNum = params.get("DevNum")
        self.DevPre = params.get("DevPre")


class CreateBatchResponse(AbstractModel):
    """CreateBatch返回参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID
        :type BatchId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.RequestId = params.get("RequestId")


class CreateForwardRuleRequest(AbstractModel):
    """CreateForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueRegion: 队列区域
        :type QueueRegion: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param Consecretid: 临时密钥
        :type Consecretid: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param QueueID: 队列或主题ID
        :type QueueID: str
        :param QueueName: 队列或主题名称
        :type QueueName: str
        """
        self.ProductID = None
        self.MsgType = None
        self.Skey = None
        self.QueueRegion = None
        self.QueueType = None
        self.Consecretid = None
        self.InstanceId = None
        self.InstanceName = None
        self.QueueID = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Skey = params.get("Skey")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.Consecretid = params.get("Consecretid")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.QueueID = params.get("QueueID")
        self.QueueName = params.get("QueueName")


class CreateForwardRuleResponse(AbstractModel):
    """CreateForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param QueueName: 队列名
        :type QueueName: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Result: 结果
        :type Result: int
        :param RoleName: 角色名称
        :type RoleName: str
        :param RoleID: 角色ID
        :type RoleID: int
        :param QueueRegion: 队列区
        :type QueueRegion: str
        :param QueueType: 消息队列的类型。 0：CMQ，1：CKafaka
        :type QueueType: int
        :param InstanceId: 实例id， 目前只有Ckafaka会用到
        :type InstanceId: str
        :param InstanceName: 实例名称，目前只有Ckafaka会用到
        :type InstanceName: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Endpoint = None
        self.QueueName = None
        self.ProductID = None
        self.MsgType = None
        self.Result = None
        self.RoleName = None
        self.RoleID = None
        self.QueueRegion = None
        self.QueueType = None
        self.InstanceId = None
        self.InstanceName = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.QueueName = params.get("QueueName")
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Result = params.get("Result")
        self.RoleName = params.get("RoleName")
        self.RoleID = params.get("RoleID")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductName: 产品名称
        :type ProductName: str
        :param DeviceType: 产品设备类型
        :type DeviceType: int
        :param ProductVaildYears: 产品有效期
        :type ProductVaildYears: int
        :param Features: 设备功能码
        :type Features: list of str
        :param ChipOs: 设备操作系统
        :type ChipOs: str
        :param ChipManufactureId: 芯片厂商id
        :type ChipManufactureId: str
        :param ChipId: 芯片id
        :type ChipId: str
        :param ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param EncryptionType: 认证方式。2 PSK
        :type EncryptionType: int
        """
        self.ProductName = None
        self.DeviceType = None
        self.ProductVaildYears = None
        self.Features = None
        self.ChipOs = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductDescription = None
        self.EncryptionType = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.DeviceType = params.get("DeviceType")
        self.ProductVaildYears = params.get("ProductVaildYears")
        self.Features = params.get("Features")
        self.ChipOs = params.get("ChipOs")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")


class CreateProductResponse(AbstractModel):
    """CreateProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoProduct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID。
        :type ProductId: str
        :param DeviceName: 设备名称。
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteForwardRuleRequest(AbstractModel):
    """DeleteForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param QueueName: 队列名称
        :type QueueName: str
        """
        self.ProductID = None
        self.Skey = None
        self.QueueType = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")
        self.QueueName = params.get("QueueName")


class DeleteForwardRuleResponse(AbstractModel):
    """DeleteForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param QueueName: 队列名称
        :type QueueName: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param Result: 删除结果
        :type Result: int
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Endpoint = None
        self.QueueName = None
        self.ProductID = None
        self.Result = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.QueueName = params.get("QueueName")
        self.ProductID = params.get("ProductID")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBatchRequest(AbstractModel):
    """DescribeBatch请求参数结构体

    """

    def __init__(self):
        """
        :param BatchId: 批次ID
        :type BatchId: int
        """
        self.BatchId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")


class DescribeBatchResponse(AbstractModel):
    """DescribeBatch返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 批次详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoBatch`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoBatch()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeBatchsRequest(AbstractModel):
    """DescribeBatchs请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param Limit: 分页的大小，最大100
        :type Limit: int
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        """
        self.ProductId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeBatchsResponse(AbstractModel):
    """DescribeBatchs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 批次数量
        :type TotalCount: int
        :param Data: 批次列表详情
        :type Data: list of VideoBatch
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VideoBatch()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCategoryRequest(AbstractModel):
    """DescribeCategory请求参数结构体

    """

    def __init__(self):
        """
        :param Id: Category ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DescribeCategoryResponse(AbstractModel):
    """DescribeCategory返回参数结构体

    """

    def __init__(self):
        """
        :param Data: Category详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.ProductTemplate`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ProductTemplate()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDeviceActionHistoryRequest(AbstractModel):
    """DescribeDeviceActionHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品Id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param MinTime: 开始范围的 unix 毫秒时间戳
        :type MinTime: int
        :param MaxTime: 结束范围的 unix 毫秒时间戳
        :type MaxTime: int
        :param ActionId: 动作Id
        :type ActionId: str
        :param Limit: 查询条数
        :type Limit: int
        :param Context: 游标，标识查询位置。
        :type Context: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.MinTime = None
        self.MaxTime = None
        self.ActionId = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ActionId = params.get("ActionId")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")


class DescribeDeviceActionHistoryResponse(AbstractModel):
    """DescribeDeviceActionHistory返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCounts: 总条数
        :type TotalCounts: int
        :param ActionHistories: 动作历史
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionHistories: list of ActionHistory
        :param Context: 用于标识查询结果的上下文，翻页用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Listover: 搜索结果是否已经结束。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCounts = None
        self.ActionHistories = None
        self.Context = None
        self.Listover = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCounts = params.get("TotalCounts")
        if params.get("ActionHistories") is not None:
            self.ActionHistories = []
            for item in params.get("ActionHistories"):
                obj = ActionHistory()
                obj._deserialize(item)
                self.ActionHistories.append(obj)
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        self.RequestId = params.get("RequestId")


class DescribeDeviceCommLogRequest(AbstractModel):
    """DescribeDeviceCommLog请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 开始时间
        :type MinTime: int
        :param MaxTime: 结束时间
        :type MaxTime: int
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Limit: 返回条数
        :type Limit: int
        :param Context: 检索上下文
        :type Context: str
        :param Type: 类型：shadow 下行，device 上行
        :type Type: str
        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.Limit = None
        self.Context = None
        self.Type = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")
        self.Type = params.get("Type")


class DescribeDeviceCommLogResponse(AbstractModel):
    """DescribeDeviceCommLog返回参数结构体

    """

    def __init__(self):
        """
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
        :type Listover: bool
        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
        :type Context: str
        :param Results: 日志数据结果数组，返回对应时间点及取值。
        :type Results: list of DeviceCommLogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceCommLogItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory请求参数结构体

    """

    def __init__(self):
        """
        :param MinTime: 区间开始时间（Unix 时间戳，毫秒级）
        :type MinTime: int
        :param MaxTime: 区间结束时间（Unix 时间戳，毫秒级）
        :type MaxTime: int
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
        :type FieldName: str
        :param Limit: 返回条数
        :type Limit: list of int non-negative
        :param Context: 检索上下文
        :type Context: str
        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.FieldName = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.FieldName = params.get("FieldName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回参数结构体

    """

    def __init__(self):
        """
        :param FieldName: 属性字段名称，对应数据模板中功能属性的标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param Listover: 数据是否已全部返回，true 表示数据全部返回，false 表示还有数据待返回，可将 Context 作为入参，继续查询返回结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param Context: 检索上下文，当 ListOver 为false时，可以用此上下文，继续读取后续数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Results: 历史数据结果数组，返回对应时间点及取值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FieldName = None
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 设备数据
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDeviceEventHistoryRequest(AbstractModel):
    """DescribeDeviceEventHistory请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param Type: 搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件
        :type Type: str
        :param StartTime: 起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h
        :type StartTime: int
        :param EndTime: 结束时间（Unix 时间戳，秒级）, 为0 表示当前时间
        :type EndTime: int
        :param Context: 搜索上下文, 用作查询游标
        :type Context: str
        :param Size: 单次获取的历史数据项目的最大数量, 缺省10
        :type Size: int
        :param EventId: 事件标识符，可以用来指定查询特定的事件，如果不指定，则查询所有事件。
        :type EventId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Context = None
        self.Size = None
        self.EventId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Context = params.get("Context")
        self.Size = params.get("Size")
        self.EventId = params.get("EventId")


class DescribeDeviceEventHistoryResponse(AbstractModel):
    """DescribeDeviceEventHistory返回参数结构体

    """

    def __init__(self):
        """
        :param Context: 搜索上下文, 用作查询游标
注意：此字段可能返回 null，表示取不到有效值。
        :type Context: str
        :param Total: 搜索结果数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Listover: 搜索结果是否已经结束
注意：此字段可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param EventHistory: 搜集结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type EventHistory: list of EventHistoryItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Total = None
        self.Listover = None
        self.EventHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Total = params.get("Total")
        self.Listover = params.get("Listover")
        if params.get("EventHistory") is not None:
            self.EventHistory = []
            for item in params.get("EventHistory"):
                obj = EventHistoryItem()
                obj._deserialize(item)
                self.EventHistory.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param DeviceName: 设备名
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活
        :type Online: int
        :param LoginTime: 设备最后上线时间
        :type LoginTime: int
        :param DevicePsk: 设备密钥
        :type DevicePsk: str
        :param EnableState: 设备启用状态
        :type EnableState: int
        :param ExpireTime: 设备过期时间
        :type ExpireTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.DevicePsk = None
        self.EnableState = None
        self.ExpireTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.DevicePsk = params.get("DevicePsk")
        self.EnableState = params.get("EnableState")
        self.ExpireTime = params.get("ExpireTime")
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 需要查看设备列表的产品 ID
        :type ProductId: str
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        :param Limit: 分页的大小，最大100
        :type Limit: int
        :param DeviceName: 需要过滤的设备名称
        :type DeviceName: str
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DeviceName = params.get("DeviceName")


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 设备总数
        :type TotalCount: int
        :param Devices: 设备详细信息列表
        :type Devices: list of DeviceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeForwardRuleRequest(AbstractModel):
    """DescribeForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 队列类型，0：CMQ，1：Ckafka
        :type QueueType: int
        :param Consecretid: 临时密钥
        :type Consecretid: str
        """
        self.ProductID = None
        self.Skey = None
        self.QueueType = None
        self.Consecretid = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")
        self.Consecretid = params.get("Consecretid")


class DescribeForwardRuleResponse(AbstractModel):
    """DescribeForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param QueueName: 队列名称
        :type QueueName: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Result: 结果
        :type Result: int
        :param RoleName: 角色名
        :type RoleName: str
        :param RoleID: 角色ID
        :type RoleID: int
        :param QueueRegion: 队列区域
        :type QueueRegion: str
        :param QueueType: 队列类型，0：CMQ，1：Ckafka
        :type QueueType: int
        :param InstanceId: 实例id， 目前只有Ckafaka会用到
        :type InstanceId: str
        :param InstanceName: 实例名称，目前只有Ckafaka会用到
        :type InstanceName: str
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Endpoint = None
        self.QueueName = None
        self.ProductID = None
        self.MsgType = None
        self.Result = None
        self.RoleName = None
        self.RoleID = None
        self.QueueRegion = None
        self.QueueType = None
        self.InstanceId = None
        self.InstanceName = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.QueueName = params.get("QueueName")
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Result = params.get("Result")
        self.RoleName = params.get("RoleName")
        self.RoleID = params.get("RoleID")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param Model: 产品数据模板
        :type Model: :class:`tencentcloud.iotvideo.v20201215.models.ProductModelDefinition`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = ProductModelDefinition()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 产品详情
        :type Data: :class:`tencentcloud.iotvideo.v20201215.models.VideoProduct`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VideoProduct()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页的大小，最大100
        :type Limit: int
        :param Offset: 偏移量，Offset从0开始
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param Data: 产品详情列表
        :type Data: list of VideoProduct
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VideoProduct()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceCommLogItem(AbstractModel):
    """设备通讯日志查询返回条目

    """

    def __init__(self):
        """
        :param Time: 时间
        :type Time: str
        :param Type: 日志类型，device 设备上行，shadow 服务端下行。
        :type Type: str
        :param Data: 通讯数据。
        :type Data: str
        """
        self.Time = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Type = params.get("Type")
        self.Data = params.get("Data")


class DeviceDataHistoryItem(AbstractModel):
    """设备历史数据结构

    """

    def __init__(self):
        """
        :param Time: 时间点，毫秒时间戳
        :type Time: str
        :param Value: 字段取值
        :type Value: str
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class DeviceInfo(AbstractModel):
    """设备详细信息

    """

    def __init__(self):
        """
        :param DeviceName: 设备名
        :type DeviceName: str
        :param Online: 设备是否在线，0不在线，1在线，2获取失败，3未激活
        :type Online: int
        :param LoginTime: 设备最后上线时间
        :type LoginTime: int
        :param DevicePsk: 设备密钥
        :type DevicePsk: str
        :param EnableState: 设备启用状态
        :type EnableState: int
        :param ExpireTime: 设备过期时间
        :type ExpireTime: int
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.DevicePsk = None
        self.EnableState = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.DevicePsk = params.get("DevicePsk")
        self.EnableState = params.get("EnableState")
        self.ExpireTime = params.get("ExpireTime")


class EventHistoryItem(AbstractModel):
    """设备事件的搜索结果项

    """

    def __init__(self):
        """
        :param TimeStamp: 事件的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        :param ProductId: 事件的产品ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param DeviceName: 事件的设备名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param EventId: 事件的标识符ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param Type: 事件的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Data: 事件的数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self.TimeStamp = None
        self.ProductId = None
        self.DeviceName = None
        self.EventId = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.TimeStamp = params.get("TimeStamp")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EventId = params.get("EventId")
        self.Type = params.get("Type")
        self.Data = params.get("Data")


class ImportModelDefinitionRequest(AbstractModel):
    """ImportModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")


class ImportModelDefinitionResponse(AbstractModel):
    """ImportModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceRequest(AbstractModel):
    """ModifyDevice请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 设备所属产品id
        :type ProductId: str
        :param DeviceName: 设备名称
        :type DeviceName: str
        :param EnableState: 要设置的设备状态，1为启用，0为禁用
        :type EnableState: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.EnableState = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EnableState = params.get("EnableState")


class ModifyDeviceResponse(AbstractModel):
    """ModifyDevice返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyForwardRuleRequest(AbstractModel):
    """ModifyForwardRule请求参数结构体

    """

    def __init__(self):
        """
        :param ProductID: 产品ID
        :type ProductID: str
        :param MsgType: 消息类型
        :type MsgType: int
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueRegion: 队列区域
        :type QueueRegion: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param Consecretid: 临时密钥
        :type Consecretid: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param QueueID: 队列或主题ID
        :type QueueID: str
        :param QueueName: 队列或主题名称
        :type QueueName: str
        """
        self.ProductID = None
        self.MsgType = None
        self.Skey = None
        self.QueueRegion = None
        self.QueueType = None
        self.Consecretid = None
        self.InstanceId = None
        self.InstanceName = None
        self.QueueID = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.MsgType = params.get("MsgType")
        self.Skey = params.get("Skey")
        self.QueueRegion = params.get("QueueRegion")
        self.QueueType = params.get("QueueType")
        self.Consecretid = params.get("Consecretid")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.QueueID = params.get("QueueID")
        self.QueueName = params.get("QueueName")


class ModifyForwardRuleResponse(AbstractModel):
    """ModifyForwardRule返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param ProductID: 产品ID
        :type ProductID: str
        :param Result: 结果
        :type Result: int
        :param ErrMsg: 错误信息
        :type ErrMsg: str
        :param QueueType: 队列类型
        :type QueueType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Endpoint = None
        self.ProductID = None
        self.Result = None
        self.ErrMsg = None
        self.QueueType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.ProductID = params.get("ProductID")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")
        self.QueueType = params.get("QueueType")
        self.RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelSchema: 数据模板定义
        :type ModelSchema: str
        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 产品id
        :type ProductId: str
        :param ProductName: 修改的产品名称
        :type ProductName: str
        :param ProductDescription: 修改的产品描述
        :type ProductDescription: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDescription = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProductModelDefinition(AbstractModel):
    """产品模型定义

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ModelDefine: 模型定义
        :type ModelDefine: str
        :param UpdateTime: 更新时间，秒级时间戳
        :type UpdateTime: int
        :param CreateTime: 创建时间，秒级时间戳
        :type CreateTime: int
        :param CategoryModel: 产品所属分类的模型快照（产品创建时刻的）
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryModel: str
        :param NetTypeModel: 产品的连接类型的模型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetTypeModel: str
        """
        self.ProductId = None
        self.ModelDefine = None
        self.UpdateTime = None
        self.CreateTime = None
        self.CategoryModel = None
        self.NetTypeModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelDefine = params.get("ModelDefine")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.CategoryModel = params.get("CategoryModel")
        self.NetTypeModel = params.get("NetTypeModel")


class ProductTemplate(AbstractModel):
    """产品分类实体

    """

    def __init__(self):
        """
        :param Id: 实体ID
        :type Id: int
        :param CategoryKey: 分类字段
        :type CategoryKey: str
        :param CategoryName: 分类名称
        :type CategoryName: str
        :param ParentId: 上层实体ID
        :type ParentId: int
        :param ModelTemplate: 物模型
        :type ModelTemplate: str
        :param ListOrder: 排列顺序
注意：此字段可能返回 null，表示取不到有效值。
        :type ListOrder: int
        :param IconUrl: 分类图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param IconUrlGrid: 九宫格图片地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrlGrid: str
        """
        self.Id = None
        self.CategoryKey = None
        self.CategoryName = None
        self.ParentId = None
        self.ModelTemplate = None
        self.ListOrder = None
        self.IconUrl = None
        self.IconUrlGrid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CategoryKey = params.get("CategoryKey")
        self.CategoryName = params.get("CategoryName")
        self.ParentId = params.get("ParentId")
        self.ModelTemplate = params.get("ModelTemplate")
        self.ListOrder = params.get("ListOrder")
        self.IconUrl = params.get("IconUrl")
        self.IconUrlGrid = params.get("IconUrlGrid")


class SetForwardAuthRequest(AbstractModel):
    """SetForwardAuth请求参数结构体

    """

    def __init__(self):
        """
        :param Skey: 控制台Skey
        :type Skey: str
        :param QueueType: 消息队列类型
        :type QueueType: int
        """
        self.Skey = None
        self.QueueType = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.QueueType = params.get("QueueType")


class SetForwardAuthResponse(AbstractModel):
    """SetForwardAuth返回参数结构体

    """

    def __init__(self):
        """
        :param Endpoint: 腾讯云账号
        :type Endpoint: str
        :param Result: 结果
        :type Result: int
        :param RoleName: 角色名
        :type RoleName: str
        :param RoleID: 角色ID
        :type RoleID: int
        :param QueueType: 消息队列类型
        :type QueueType: int
        :param ErrMsg: 错误消息
        :type ErrMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Endpoint = None
        self.Result = None
        self.RoleName = None
        self.RoleID = None
        self.QueueType = None
        self.ErrMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Endpoint = params.get("Endpoint")
        self.Result = params.get("Result")
        self.RoleName = params.get("RoleName")
        self.RoleID = params.get("RoleID")
        self.QueueType = params.get("QueueType")
        self.ErrMsg = params.get("ErrMsg")
        self.RequestId = params.get("RequestId")


class VideoBatch(AbstractModel):
    """批次元数据

    """

    def __init__(self):
        """
        :param Id: 批次ID
        :type Id: int
        :param UserId: 用户ID
        :type UserId: str
        :param ProductId: 产品ID
        :type ProductId: str
        :param Status: 状态：1：待创建设备 2：创建中 3：已完成
        :type Status: int
        :param DevPre: 设备前缀
        :type DevPre: str
        :param DevNum: 设备数量
        :type DevNum: int
        :param DevNumCreated: 已创建设备数量
        :type DevNumCreated: int
        :param BatchURL: 批次下载地址
        :type BatchURL: str
        :param CreateTime: 创建时间。unix时间戳
        :type CreateTime: int
        :param UpdateTime: 修改时间。unix时间戳
        :type UpdateTime: int
        """
        self.Id = None
        self.UserId = None
        self.ProductId = None
        self.Status = None
        self.DevPre = None
        self.DevNum = None
        self.DevNumCreated = None
        self.BatchURL = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.UserId = params.get("UserId")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.DevPre = params.get("DevPre")
        self.DevNum = params.get("DevNum")
        self.DevNumCreated = params.get("DevNumCreated")
        self.BatchURL = params.get("BatchURL")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class VideoProduct(AbstractModel):
    """video产品元数据

    """

    def __init__(self):
        """
        :param ProductId: 产品ID
        :type ProductId: str
        :param ProductName: 产品名称
        :type ProductName: str
        :param DeviceType: 产品设备类型（普通设备)	1.普通设备
        :type DeviceType: int
        :param EncryptionType: 认证方式：2：PSK
        :type EncryptionType: int
        :param Features: 设备功能码
        :type Features: list of str
        :param ChipOs: 操作系统
        :type ChipOs: str
        :param ChipManufactureId: 芯片厂商id
        :type ChipManufactureId: str
        :param ChipId: 芯片id
        :type ChipId: str
        :param ProductDescription: 产品描述信息
        :type ProductDescription: str
        :param CreateTime: 创建时间unix时间戳
        :type CreateTime: int
        :param UpdateTime: 修改时间unix时间戳
        :type UpdateTime: int
        """
        self.ProductId = None
        self.ProductName = None
        self.DeviceType = None
        self.EncryptionType = None
        self.Features = None
        self.ChipOs = None
        self.ChipManufactureId = None
        self.ChipId = None
        self.ProductDescription = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.DeviceType = params.get("DeviceType")
        self.EncryptionType = params.get("EncryptionType")
        self.Features = params.get("Features")
        self.ChipOs = params.get("ChipOs")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")
        self.ProductDescription = params.get("ProductDescription")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")