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


class Account(AbstractModel):
    """子账号信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param AccountName: 账号名称（如果是主账号，名称为root）
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccountName: str\n        :param Remark: 账号描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        :param Privilege: 读写策略：r-只读，w-只写，rw-读写
注意：此字段可能返回 null，表示取不到有效值。\n        :type Privilege: str\n        :param ReadonlyPolicy: 路由策略：master-主节点，replication-从节点
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReadonlyPolicy: list of str\n        :param Status: 子账号状态：1-账号变更中，2-账号有效，-4-账号已删除
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        """
        self.InstanceId = None
        self.AccountName = None
        self.Remark = None
        self.Privilege = None
        self.ReadonlyPolicy = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        self.Remark = params.get("Remark")
        self.Privilege = params.get("Privilege")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyParamsTemplateRequest(AbstractModel):
    """ApplyParamsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID列表\n        :type InstanceIds: list of str\n        :param TemplateId: 应用的参数模板ID\n        :type TemplateId: str\n        """
        self.InstanceIds = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyParamsTemplateResponse(AbstractModel):
    """ApplyParamsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TaskIds: 任务ID\n        :type TaskIds: list of int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb 等。\n        :type Product: str\n        :param SecurityGroupId: 要绑定的安全组ID，类似sg-efil73jd。\n        :type SecurityGroupId: str\n        :param InstanceIds: 被绑定的实例ID，类似ins-lesecurk，支持指定多个实例。\n        :type InstanceIds: list of str\n        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BackupDownloadInfo(AbstractModel):
    """备份文件下载信息

    """

    def __init__(self):
        """
        :param FileName: 备份文件名称\n        :type FileName: str\n        :param FileSize: 备份文件大小，单位B，如果为0，表示无效\n        :type FileSize: int\n        :param DownloadUrl: 备份文件外网下载地址（6小时）\n        :type DownloadUrl: str\n        :param InnerDownloadUrl: 备份文件内网下载地址（6小时）\n        :type InnerDownloadUrl: str\n        """
        self.FileName = None
        self.FileSize = None
        self.DownloadUrl = None
        self.InnerDownloadUrl = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.DownloadUrl = params.get("DownloadUrl")
        self.InnerDownloadUrl = params.get("InnerDownloadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BigKeyInfo(AbstractModel):
    """大Key详情

    """

    def __init__(self):
        """
        :param DB: 所属的database\n        :type DB: int\n        :param Key: 大Key\n        :type Key: str\n        :param Type: 类型\n        :type Type: str\n        :param Size: 大小\n        :type Size: int\n        :param Updatetime: 数据时间戳\n        :type Updatetime: int\n        """
        self.DB = None
        self.Key = None
        self.Type = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.DB = params.get("DB")
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BigKeyTypeInfo(AbstractModel):
    """大Key类型分布详情

    """

    def __init__(self):
        """
        :param Type: 类型\n        :type Type: str\n        :param Count: 数量\n        :type Count: int\n        :param Size: 大小\n        :type Size: int\n        :param Updatetime: 时间戳\n        :type Updatetime: int\n        """
        self.Type = None
        self.Count = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Count = params.get("Count")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeReplicaToMasterRequest(AbstractModel):
    """ChangeReplicaToMaster请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param GroupId: 副本Id\n        :type GroupId: int\n        """
        self.InstanceId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChangeReplicaToMasterResponse(AbstractModel):
    """ChangeReplicaToMaster返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CleanUpInstanceRequest(AbstractModel):
    """CleanUpInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CleanUpInstanceResponse(AbstractModel):
    """CleanUpInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ClearInstanceRequest(AbstractModel):
    """ClearInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Password: redis的实例密码（免密实例不需要传密码，非免密实例必传）\n        :type Password: str\n        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearInstanceResponse(AbstractModel):
    """ClearInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CommandTake(AbstractModel):
    """命令耗时

    """

    def __init__(self):
        """
        :param Cmd: 命令\n        :type Cmd: str\n        :param Took: 耗时\n        :type Took: int\n        """
        self.Cmd = None
        self.Took = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.Took = params.get("Took")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceAccountRequest(AbstractModel):
    """CreateInstanceAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param AccountName: 子账号名称\n        :type AccountName: str\n        :param AccountPassword: 1.长度8-30位,推荐使用12位以上的密码
2.不能以"/"开头
3.至少包含两项
    a.小写字母a-z
    b.大写字母A-Z
    c.数字0-9
    d.()`~!@#$%^&*-+=_|{}[]:;<>,.?/\n        :type AccountPassword: str\n        :param ReadonlyPolicy: 路由策略：填写master或者replication，表示主节点或者从节点\n        :type ReadonlyPolicy: list of str\n        :param Privilege: 读写策略：填写r、rw，表示只读、读写\n        :type Privilege: str\n        :param Remark: 子账号描述信息\n        :type Remark: str\n        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None
        self.ReadonlyPolicy = None
        self.Privilege = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        self.Privilege = params.get("Privilege")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceAccountResponse(AbstractModel):
    """CreateInstanceAccount返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances请求参数结构体

    """

    def __init__(self):
        """
        :param TypeId: 实例类型：2 – Redis2.8内存版(标准架构)，3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，6 – Redis4.0内存版(标准架构)，7 – Redis4.0内存版(集群架构)，8 – Redis5.0内存版(标准架构)，9 – Redis5.0内存版(集群架构)。\n        :type TypeId: int\n        :param MemSize: 内存容量，单位为MB， 数值需为1024的整数倍，具体规格以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
TypeId为标准架构时，MemSize是实例总内存容量；TypeId为集群架构时，MemSize是单分片内存容量。\n        :type MemSize: int\n        :param GoodsNum: 实例数量，单次购买实例数量以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。\n        :type GoodsNum: int\n        :param Period: 购买时长，在创建包年包月实例的时候需要填写，按量计费实例填1即可，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。\n        :type Period: int\n        :param BillingMode: 付费方式:0-按量计费，1-包年包月。\n        :type BillingMode: int\n        :param ZoneId: 实例所属的可用区ID，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。\n        :type ZoneId: int\n        :param Password: 实例密码，当输入参数NoAuth为true且使用私有网络VPC时，Password为非必填，否则Password为必填参数。
当实例类型TypeId为Redis2.8、4.0和5.0时，其密码格式为：8-30个字符，至少包含小写字母、大写字母、数字和字符 ()`~!@#$%^&*-+=_|{}[]:;<>,.?/ 中的2种，不能以"/"开头；
当实例类型TypeId为CKV 3.2时，其密码格式为：8-30个字符，必须包含字母和数字 且 不包含其他字符。\n        :type Password: str\n        :param VpcId: 私有网络ID，如果不传则默认选择基础网络，请使用私有网络列表查询，如：vpc-sad23jfdfk。\n        :type VpcId: str\n        :param SubnetId: 基础网络下， subnetId无效； vpc子网下，取值以查询子网列表，如：subnet-fdj24n34j2。\n        :type SubnetId: str\n        :param ProjectId: 项目id，取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准。\n        :type ProjectId: int\n        :param AutoRenew: 自动续费标识。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费。\n        :type AutoRenew: int\n        :param SecurityGroupIdList: 安全组id数组。\n        :type SecurityGroupIdList: list of str\n        :param VPort: 用户自定义的端口 不填则默认为6379，范围[1024,65535]。\n        :type VPort: int\n        :param RedisShardNum: 实例分片数量，购买标准版实例不需要填写，集群版分片数量范围[3,5,8,12,16,24,32,64,96,128]。\n        :type RedisShardNum: int\n        :param RedisReplicasNum: 实例副本数量，Redis 2.8标准版、CKV标准版只支持1副本，4.0、5.0标准版和集群版支持1-5个副本。\n        :type RedisReplicasNum: int\n        :param ReplicasReadonly: 是否支持副本只读，Redis 2.8标准版、CKV标准版不支持副本只读，开启副本只读，实例将自动读写分离，写请求路由到主节点，读请求路由到副本节点，如需开启副本只读建议副本数>=2。\n        :type ReplicasReadonly: bool\n        :param InstanceName: 实例名称，长度小于60的中文/英文/数字/"-"/"_"。\n        :type InstanceName: str\n        :param NoAuth: 是否支持免密，true-免密实例，false-非免密实例，默认为非免密实例，仅VPC网络的实例支持免密码访问。\n        :type NoAuth: bool\n        :param NodeSet: 实例的节点信息，目前支持传入节点的类型（主节点或者副本节点），节点的可用区。单可用区部署不需要传递此参数。\n        :type NodeSet: list of RedisNodeInfo\n        :param ResourceTags: 购买实例绑定标签\n        :type ResourceTags: list of ResourceTag\n        :param ZoneName: 实例所属的可用区名称，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。\n        :type ZoneName: str\n        :param TemplateId: 创建实例需要应用的参数模板ID，不传则应用默认的参数模板\n        :type TemplateId: str\n        """
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.BillingMode = None
        self.ZoneId = None
        self.Password = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AutoRenew = None
        self.SecurityGroupIdList = None
        self.VPort = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.ReplicasReadonly = None
        self.InstanceName = None
        self.NoAuth = None
        self.NodeSet = None
        self.ResourceTags = None
        self.ZoneName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.BillingMode = params.get("BillingMode")
        self.ZoneId = params.get("ZoneId")
        self.Password = params.get("Password")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenew = params.get("AutoRenew")
        self.SecurityGroupIdList = params.get("SecurityGroupIdList")
        self.VPort = params.get("VPort")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.ReplicasReadonly = params.get("ReplicasReadonly")
        self.InstanceName = params.get("InstanceName")
        self.NoAuth = params.get("NoAuth")
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.ZoneName = params.get("ZoneName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 交易的ID\n        :type DealId: str\n        :param InstanceIds: 实例ID\n        :type InstanceIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 参数模板名称。\n        :type Name: str\n        :param Description: 参数模板描述。\n        :type Description: str\n        :param ProductType: 产品类型：1 – Redis2.8内存版（集群架构），2 – Redis2.8内存版（标准架构），3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版（单机），6 – Redis4.0内存版（标准架构），7 – Redis4.0内存版（集群架构），8 – Redis5.0内存版（标准架构），9 – Redis5.0内存版（集群架构）。创建模板时必填，从源模板复制则不需要传入该参数。\n        :type ProductType: int\n        :param TemplateId: 源参数模板 ID。\n        :type TemplateId: str\n        :param ParamList: 参数列表。\n        :type ParamList: list of InstanceParam\n        """
        self.Name = None
        self.Description = None
        self.ProductType = None
        self.TemplateId = None
        self.ParamList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ProductType = params.get("ProductType")
        self.TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = InstanceParam()
                obj._deserialize(item)
                self.ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 参数模板 ID。\n        :type TemplateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class DelayDistribution(AbstractModel):
    """延时分布详情

    """

    def __init__(self):
        """
        :param Ladder: 分布阶梯，延时和Ladder值的对应关系：
[0ms,1ms]: 1；
[1ms,5ms]: 5；
[5ms,10ms]: 10；
[10ms,50ms]: 50；
[50ms,200ms]: 200；
[200ms,∞]: -1。\n        :type Ladder: int\n        :param Size: 延时处于当前分布阶梯的命令数量，个。\n        :type Size: int\n        :param Updatetime: 修改时间。\n        :type Updatetime: int\n        """
        self.Ladder = None
        self.Size = None
        self.Updatetime = None


    def _deserialize(self, params):
        self.Ladder = params.get("Ladder")
        self.Size = params.get("Size")
        self.Updatetime = params.get("Updatetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceAccountRequest(AbstractModel):
    """DeleteInstanceAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param AccountName: 子账号名称\n        :type AccountName: str\n        """
        self.InstanceId = None
        self.AccountName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceAccountResponse(AbstractModel):
    """DeleteInstanceAccount返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 参数模板 ID。\n        :type TemplateId: str\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoBackupConfigResponse(AbstractModel):
    """DescribeAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param AutoBackupType: 备份类型。自动备份类型： 1 “定时回档”\n        :type AutoBackupType: int\n        :param WeekDays: Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。\n        :type WeekDays: list of str\n        :param TimePeriod: 时间段。\n        :type TimePeriod: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class DescribeBackupUrlRequest(AbstractModel):
    """DescribeBackupUrl请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param BackupId: 备份ID，通过DescribeInstanceBackups接口可查\n        :type BackupId: str\n        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupUrlResponse(AbstractModel):
    """DescribeBackupUrl返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 外网下载地址（6小时）\n        :type DownloadUrl: list of str\n        :param InnerDownloadUrl: 内网下载地址（6小时）\n        :type InnerDownloadUrl: list of str\n        :param Filenames: 文件名称（仅tendis实例有值）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Filenames: list of str\n        :param BackupInfos: 备份文件信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupInfos: list of BackupDownloadInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DownloadUrl = None
        self.InnerDownloadUrl = None
        self.Filenames = None
        self.BackupInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.InnerDownloadUrl = params.get("InnerDownloadUrl")
        self.Filenames = params.get("Filenames")
        if params.get("BackupInfos") is not None:
            self.BackupInfos = []
            for item in params.get("BackupInfos"):
                obj = BackupDownloadInfo()
                obj._deserialize(item)
                self.BackupInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCommonDBInstancesRequest(AbstractModel):
    """DescribeCommonDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: 实例Vip信息列表\n        :type VpcIds: list of int\n        :param SubnetIds: 子网id信息列表\n        :type SubnetIds: list of int\n        :param PayMode: 计费类型过滤列表；0表示包年包月，1表示按量计费\n        :type PayMode: int\n        :param InstanceIds: 实例id过滤信息列表\n        :type InstanceIds: list of str\n        :param InstanceNames: 实例名称过滤信息列表\n        :type InstanceNames: list of str\n        :param Status: 实例状态信息过滤列表\n        :type Status: list of str\n        :param OrderBy: 排序字段\n        :type OrderBy: str\n        :param OrderByType: 排序方式\n        :type OrderByType: str\n        :param Vips: 实例vip信息列表\n        :type Vips: list of str\n        :param UniqVpcIds: vpc网络ID信息列表\n        :type UniqVpcIds: list of str\n        :param UniqSubnetIds: 子网统一ID列表\n        :type UniqSubnetIds: list of str\n        :param Limit: 数量限制，默认推荐100\n        :type Limit: int\n        :param Offset: 偏移量，默认0\n        :type Offset: int\n        """
        self.VpcIds = None
        self.SubnetIds = None
        self.PayMode = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Status = None
        self.OrderBy = None
        self.OrderByType = None
        self.Vips = None
        self.UniqVpcIds = None
        self.UniqSubnetIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        self.SubnetIds = params.get("SubnetIds")
        self.PayMode = params.get("PayMode")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Status = params.get("Status")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Vips = params.get("Vips")
        self.UniqVpcIds = params.get("UniqVpcIds")
        self.UniqSubnetIds = params.get("UniqSubnetIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCommonDBInstancesResponse(AbstractModel):
    """DescribeCommonDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例数\n        :type TotalCount: int\n        :param InstanceDetails: 实例信息\n        :type InstanceDetails: list of RedisCommonInstanceList\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = RedisCommonInstanceList()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称，本接口取值：redis。\n        :type Product: str\n        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。\n        :type InstanceId: str\n        """
        self.Product = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Groups: 安全组规则\n        :type Groups: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceAccountRequest(AbstractModel):
    """DescribeInstanceAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Limit: 分页大小\n        :type Limit: int\n        :param Offset: 分页偏移量\n        :type Offset: int\n        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAccountResponse(AbstractModel):
    """DescribeInstanceAccount返回参数结构体

    """

    def __init__(self):
        """
        :param Accounts: 账号详细信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Accounts: list of Account\n        :param TotalCount: 账号个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Accounts = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceBackupsRequest(AbstractModel):
    """DescribeInstanceBackups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的实例ID，可通过 DescribeInstance 接口返回值中的 InstanceId 获取。\n        :type InstanceId: str\n        :param Limit: 实例列表大小，默认大小20\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍\n        :type Offset: int\n        :param BeginTime: 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。\n        :type BeginTime: str\n        :param EndTime: 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。\n        :type EndTime: str\n        :param Status: 1：备份在流程中，2：备份正常，3：备份转RDB文件处理中，4：已完成RDB转换，-1：备份已过期，-2：备份已删除。\n        :type Status: list of int\n        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceBackupsResponse(AbstractModel):
    """DescribeInstanceBackups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 备份总数\n        :type TotalCount: int\n        :param BackupSet: 实例的备份数组\n        :type BackupSet: list of RedisBackupSet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.BackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self.BackupSet = []
            for item in params.get("BackupSet"):
                obj = RedisBackupSet()
                obj._deserialize(item)
                self.BackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceDTSInfoRequest(AbstractModel):
    """DescribeInstanceDTSInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDTSInfoResponse(AbstractModel):
    """DescribeInstanceDTSInfo返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: DTS任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type JobId: str\n        :param JobName: DTS任务名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type JobName: str\n        :param Status: 任务状态,取值为：1-创建中(Creating),3-校验中(Checking)4-校验通过(CheckPass),5-校验不通过（CheckNotPass）,7-任务运行(Running),8-准备完成（ReadyComplete）,9-任务成功（Success）,10-任务失败（Failed）,11-撤销中（Stopping）,12-完成中（Completing）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusDesc: str\n        :param Offset: 同步时延，单位：字节
注意：此字段可能返回 null，表示取不到有效值。\n        :type Offset: int\n        :param CutDownTime: 断开时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CutDownTime: str\n        :param SrcInfo: 源实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SrcInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`\n        :param DstInfo: 目标实例信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type DstInfo: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInstanceInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.JobId = None
        self.JobName = None
        self.Status = None
        self.StatusDesc = None
        self.Offset = None
        self.CutDownTime = None
        self.SrcInfo = None
        self.DstInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Offset = params.get("Offset")
        self.CutDownTime = params.get("CutDownTime")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = DescribeInstanceDTSInstanceInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DescribeInstanceDTSInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceDTSInstanceInfo(AbstractModel):
    """详细DTS实例信息

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: int\n        :param InstanceId: 实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param SetId: 仓库ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SetId: int\n        :param ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneId: int\n        :param Type: 实例类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: int\n        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param Vip: 实例访问地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vip: str\n        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        """
        self.RegionId = None
        self.InstanceId = None
        self.SetId = None
        self.ZoneId = None
        self.Type = None
        self.InstanceName = None
        self.Vip = None
        self.Status = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.InstanceId = params.get("InstanceId")
        self.SetId = params.get("SetId")
        self.ZoneId = params.get("ZoneId")
        self.Type = params.get("Type")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailRequest(AbstractModel):
    """DescribeInstanceDealDetail请求参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 订单交易ID数组，即 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的输出参数DealId。\n        :type DealIds: list of str\n        """
        self.DealIds = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDealDetailResponse(AbstractModel):
    """DescribeInstanceDealDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DealDetails: 订单详细信息\n        :type DealDetails: list of TradeDealDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DealDetails") is not None:
            self.DealDetails = []
            for item in params.get("DealDetails"):
                obj = TradeDealDetail()
                obj._deserialize(item)
                self.DealDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyRequest(AbstractModel):
    """DescribeInstanceMonitorBigKey请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param ReqType: 请求类型：1——string类型，2——所有类型\n        :type ReqType: int\n        :param Date: 时间；例如："20190219"\n        :type Date: str\n        """
        self.InstanceId = None
        self.ReqType = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReqType = params.get("ReqType")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyResponse(AbstractModel):
    """DescribeInstanceMonitorBigKey返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 大Key详细信息\n        :type Data: list of BigKeyInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BigKeyInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeySizeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Date: 时间；例如："20190219"\n        :type Date: str\n        """
        self.InstanceId = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeySizeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeySizeDist返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 大Key大小分布详情\n        :type Data: list of DelayDistribution\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorBigKeyTypeDistRequest(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Date: 时间；例如："20190219"\n        :type Date: str\n        """
        self.InstanceId = None
        self.Date = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorBigKeyTypeDistResponse(AbstractModel):
    """DescribeInstanceMonitorBigKeyTypeDist返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 大Key类型分布详细信息\n        :type Data: list of BigKeyTypeInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BigKeyTypeInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorHotKeyRequest(AbstractModel):
    """DescribeInstanceMonitorHotKey请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时\n        :type SpanType: int\n        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorHotKeyResponse(AbstractModel):
    """DescribeInstanceMonitorHotKey返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 热Key详细信息\n        :type Data: list of HotKeyInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = HotKeyInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorSIPRequest(AbstractModel):
    """DescribeInstanceMonitorSIP请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorSIPResponse(AbstractModel):
    """DescribeInstanceMonitorSIP返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 访问来源信息\n        :type Data: list of SourceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SourceInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTookDistRequest(AbstractModel):
    """DescribeInstanceMonitorTookDist请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Date: 时间；例如："20190219"\n        :type Date: str\n        :param SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时\n        :type SpanType: int\n        """
        self.InstanceId = None
        self.Date = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Date = params.get("Date")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTookDistResponse(AbstractModel):
    """DescribeInstanceMonitorTookDist返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 时延分布信息\n        :type Data: list of DelayDistribution\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DelayDistribution()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmd请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时\n        :type SpanType: int\n        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmd返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 访问命令信息\n        :type Data: list of SourceCommand\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SourceCommand()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceMonitorTopNCmdTookRequest(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param SpanType: 时间范围：1——实时，2——近30分钟，3——近6小时，4——近24小时\n        :type SpanType: int\n        """
        self.InstanceId = None
        self.SpanType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SpanType = params.get("SpanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceMonitorTopNCmdTookResponse(AbstractModel):
    """DescribeInstanceMonitorTopNCmdTook返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 耗时详细信息\n        :type Data: list of CommandTake\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CommandTake()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceNodeInfoRequest(AbstractModel):
    """DescribeInstanceNodeInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Limit: 列表大小\n        :type Limit: int\n        :param Offset: 偏移量\n        :type Offset: int\n        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNodeInfoResponse(AbstractModel):
    """DescribeInstanceNodeInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ProxyCount: proxy节点数量\n        :type ProxyCount: int\n        :param Proxy: proxy节点信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Proxy: list of ProxyNodes\n        :param RedisCount: redis节点数量\n        :type RedisCount: int\n        :param Redis: redis节点信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Redis: list of RedisNodes\n        :param TendisCount: tendis节点数量\n        :type TendisCount: int\n        :param Tendis: tendis节点信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tendis: list of TendisNodes\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProxyCount = None
        self.Proxy = None
        self.RedisCount = None
        self.Redis = None
        self.TendisCount = None
        self.Tendis = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyCount = params.get("ProxyCount")
        if params.get("Proxy") is not None:
            self.Proxy = []
            for item in params.get("Proxy"):
                obj = ProxyNodes()
                obj._deserialize(item)
                self.Proxy.append(obj)
        self.RedisCount = params.get("RedisCount")
        if params.get("Redis") is not None:
            self.Redis = []
            for item in params.get("Redis"):
                obj = RedisNodes()
                obj._deserialize(item)
                self.Redis.append(obj)
        self.TendisCount = params.get("TendisCount")
        if params.get("Tendis") is not None:
            self.Tendis = []
            for item in params.get("Tendis"):
                obj = TendisNodes()
                obj._deserialize(item)
                self.Tendis.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Limit: 分页大小\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍\n        :type Offset: int\n        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总的修改历史记录数。\n        :type TotalCount: int\n        :param InstanceParamHistory: 修改历史记录信息。\n        :type InstanceParamHistory: list of InstanceParamHistory\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceParamHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceParamHistory") is not None:
            self.InstanceParamHistory = []
            for item in params.get("InstanceParamHistory"):
                obj = InstanceParamHistory()
                obj._deserialize(item)
                self.InstanceParamHistory.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例参数个数\n        :type TotalCount: int\n        :param InstanceEnumParam: 实例枚举类型参数\n        :type InstanceEnumParam: list of InstanceEnumParam\n        :param InstanceIntegerParam: 实例整型参数\n        :type InstanceIntegerParam: list of InstanceIntegerParam\n        :param InstanceTextParam: 实例字符型参数\n        :type InstanceTextParam: list of InstanceTextParam\n        :param InstanceMultiParam: 实例多选项型参数\n        :type InstanceMultiParam: list of InstanceMultiParam\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceEnumParam = None
        self.InstanceIntegerParam = None
        self.InstanceTextParam = None
        self.InstanceMultiParam = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceEnumParam") is not None:
            self.InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self.InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self.InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self.InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self.InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self.InstanceTextParam.append(obj)
        if params.get("InstanceMultiParam") is not None:
            self.InstanceMultiParam = []
            for item in params.get("InstanceMultiParam"):
                obj = InstanceMultiParam()
                obj._deserialize(item)
                self.InstanceMultiParam.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceSecurityGroupRequest(AbstractModel):
    """DescribeInstanceSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例列表\n        :type InstanceIds: list of str\n        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSecurityGroupResponse(AbstractModel):
    """DescribeInstanceSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceSecurityGroupsDetail: 实例安全组信息\n        :type InstanceSecurityGroupsDetail: list of InstanceSecurityGroupDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceSecurityGroupsDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSecurityGroupsDetail") is not None:
            self.InstanceSecurityGroupsDetail = []
            for item in params.get("InstanceSecurityGroupsDetail"):
                obj = InstanceSecurityGroupDetail()
                obj._deserialize(item)
                self.InstanceSecurityGroupsDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceShardsRequest(AbstractModel):
    """DescribeInstanceShards请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param FilterSlave: 是否过滤掉从节信息\n        :type FilterSlave: bool\n        """
        self.InstanceId = None
        self.FilterSlave = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FilterSlave = params.get("FilterSlave")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceShardsResponse(AbstractModel):
    """DescribeInstanceShards返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceShards: 实例分片列表信息\n        :type InstanceShards: list of InstanceClusterShard\n        :param TotalCount: 实例分片节点总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceShards = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceShards") is not None:
            self.InstanceShards = []
            for item in params.get("InstanceShards"):
                obj = InstanceClusterShard()
                obj._deserialize(item)
                self.InstanceShards.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceZoneInfoRequest(AbstractModel):
    """DescribeInstanceZoneInfo请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id，如：crs-6ubhgouj\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceZoneInfoResponse(AbstractModel):
    """DescribeInstanceZoneInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例节点组的个数\n        :type TotalCount: int\n        :param ReplicaGroups: 实例节点组列表\n        :type ReplicaGroups: list of ReplicaGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ReplicaGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReplicaGroups") is not None:
            self.ReplicaGroups = []
            for item in params.get("ReplicaGroups"):
                obj = ReplicaGroup()
                obj._deserialize(item)
                self.ReplicaGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 实例列表的大小，参数默认值20\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍\n        :type Offset: int\n        :param InstanceId: 实例Id，如：crs-6ubhgouj\n        :type InstanceId: str\n        :param OrderBy: 枚举范围： projectId,createtime,instancename,type,curDeadline\n        :type OrderBy: str\n        :param OrderType: 1倒序，0顺序，默认倒序\n        :type OrderType: int\n        :param VpcIds: 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：47525\n        :type VpcIds: list of str\n        :param SubnetIds: 子网ID数组，数组下标从0开始，如：56854\n        :type SubnetIds: list of str\n        :param ProjectIds: 项目ID 组成的数组，数组下标从0开始\n        :type ProjectIds: list of int\n        :param SearchKey: 查找实例的ID。\n        :type SearchKey: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param UniqVpcIds: 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：vpc-sad23jfdfk\n        :type UniqVpcIds: list of str\n        :param UniqSubnetIds: 子网ID数组，数组下标从0开始，如：subnet-fdj24n34j2\n        :type UniqSubnetIds: list of str\n        :param RegionIds: 地域ID，已经弃用，可通过公共参数Region查询对应地域\n        :type RegionIds: list of int\n        :param Status: 实例状态：0-待初始化，1-流程中，2-运行中，-2-已隔离，-3-待删除\n        :type Status: list of int\n        :param TypeVersion: 类型版本：1-单机版,2-主从版,3-集群版\n        :type TypeVersion: int\n        :param EngineName: 引擎信息：Redis-2.8，Redis-4.0，CKV\n        :type EngineName: str\n        :param AutoRenew: 续费模式：0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费\n        :type AutoRenew: list of int\n        :param BillingMode: 计费模式：postpaid-按量计费；prepaid-包年包月\n        :type BillingMode: str\n        :param Type: 实例类型：1-Redis老集群版；2-Redis 2.8主从版；3-CKV主从版；4-CKV集群版；5-Redis 2.8单机版；6-Redis 4.0主从版；7-Redis 4.0集群版；8 – Redis5.0主从版，9 – Redis5.0集群版，\n        :type Type: int\n        :param SearchKeys: 搜索关键词：支持实例Id、实例名称、完整IP\n        :type SearchKeys: list of str\n        :param TypeList: 内部参数，用户可忽略\n        :type TypeList: list of int\n        :param MonitorVersion: 内部参数，用户可忽略\n        :type MonitorVersion: str\n        """
        self.Limit = None
        self.Offset = None
        self.InstanceId = None
        self.OrderBy = None
        self.OrderType = None
        self.VpcIds = None
        self.SubnetIds = None
        self.ProjectIds = None
        self.SearchKey = None
        self.InstanceName = None
        self.UniqVpcIds = None
        self.UniqSubnetIds = None
        self.RegionIds = None
        self.Status = None
        self.TypeVersion = None
        self.EngineName = None
        self.AutoRenew = None
        self.BillingMode = None
        self.Type = None
        self.SearchKeys = None
        self.TypeList = None
        self.MonitorVersion = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstanceId = params.get("InstanceId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.VpcIds = params.get("VpcIds")
        self.SubnetIds = params.get("SubnetIds")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")
        self.InstanceName = params.get("InstanceName")
        self.UniqVpcIds = params.get("UniqVpcIds")
        self.UniqSubnetIds = params.get("UniqSubnetIds")
        self.RegionIds = params.get("RegionIds")
        self.Status = params.get("Status")
        self.TypeVersion = params.get("TypeVersion")
        self.EngineName = params.get("EngineName")
        self.AutoRenew = params.get("AutoRenew")
        self.BillingMode = params.get("BillingMode")
        self.Type = params.get("Type")
        self.SearchKeys = params.get("SearchKeys")
        self.TypeList = params.get("TypeList")
        self.MonitorVersion = params.get("MonitorVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例数\n        :type TotalCount: int\n        :param InstanceSet: 实例详细信息列表\n        :type InstanceSet: list of InstanceSet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceSet()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaintenanceWindowRequest(AbstractModel):
    """DescribeMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintenanceWindowResponse(AbstractModel):
    """DescribeMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 维护时间窗起始时间，如：17:00\n        :type StartTime: str\n        :param EndTime: 维护时间窗结束时间，如：19:00\n        :type EndTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 参数模板 ID。\n        :type TemplateId: str\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplateInfoResponse(AbstractModel):
    """DescribeParamTemplateInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例参数个数\n        :type TotalCount: int\n        :param TemplateId: 参数模板 ID。\n        :type TemplateId: str\n        :param Name: 参数模板名称。\n        :type Name: str\n        :param ProductType: 产品类型：1 – Redis2.8内存版（集群架构），2 – Redis2.8内存版（标准架构），3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版（单机），6 – Redis4.0内存版（标准架构），7 – Redis4.0内存版（集群架构），8 – Redis5.0内存版（标准架构），9 – Redis5.0内存版（集群架构）\n        :type ProductType: int\n        :param Description: 参数模板描述\n        :type Description: str\n        :param Items: 参数详情\n        :type Items: list of ParameterDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TemplateId = None
        self.Name = None
        self.ProductType = None
        self.Description = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.ProductType = params.get("ProductType")
        self.Description = params.get("Description")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param ProductTypes: 产品类型数组。产品类型：1 – Redis2.8内存版（集群架构），2 – Redis2.8内存版（标准架构），3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版（单机），6 – Redis4.0内存版（标准架构），7 – Redis4.0内存版（集群架构），8 – Redis5.0内存版（标准架构），9 – Redis5.0内存版（集群架构）\n        :type ProductTypes: list of int\n        :param TemplateNames: 模板名称数组。\n        :type TemplateNames: list of str\n        :param TemplateIds: 模板ID数组。\n        :type TemplateIds: list of str\n        """
        self.ProductTypes = None
        self.TemplateNames = None
        self.TemplateIds = None


    def _deserialize(self, params):
        self.ProductTypes = params.get("ProductTypes")
        self.TemplateNames = params.get("TemplateNames")
        self.TemplateIds = params.get("TemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 该用户的参数模板数量。\n        :type TotalCount: int\n        :param Items: 参数模板详情。\n        :type Items: list of ParamTemplateInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo请求参数结构体

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RegionSet: 地域售卖信息\n        :type RegionSet: list of RegionConf\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionConf()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupRequest(AbstractModel):
    """DescribeProjectSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 0:默认项目；-1 所有项目; >0: 特定项目\n        :type ProjectId: int\n        :param SecurityGroupId: 安全组Id\n        :type SecurityGroupId: str\n        """
        self.ProjectId = None
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupResponse(AbstractModel):
    """DescribeProjectSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupDetails: 项目安全组\n        :type SecurityGroupDetails: list of SecurityGroupDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroupDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupDetails") is not None:
            self.SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self.SecurityGroupDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb\n        :type Product: str\n        :param ProjectId: 项目Id。\n        :type ProjectId: int\n        :param Offset: 偏移量。\n        :type Offset: int\n        :param Limit: 拉取数量限制。\n        :type Limit: int\n        :param SearchKey: 搜索条件，支持安全组id或者安全组名称。\n        :type SearchKey: str\n        """
        self.Product = None
        self.ProjectId = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.ProjectId = params.get("ProjectId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param Groups: 安全组规则。\n        :type Groups: list of SecurityGroup\n        :param Total: 符合条件的安全组总数量。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Groups = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeProxySlowLogRequest(AbstractModel):
    """DescribeProxySlowLog请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param BeginTime: 开始时间\n        :type BeginTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param MinQueryTime: 慢查询阈值（单位：毫秒）\n        :type MinQueryTime: int\n        :param Limit: 页面大小\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍\n        :type Offset: int\n        """
        self.InstanceId = None
        self.BeginTime = None
        self.EndTime = None
        self.MinQueryTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.MinQueryTime = params.get("MinQueryTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxySlowLogResponse(AbstractModel):
    """DescribeProxySlowLog返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 慢查询总数\n        :type TotalCount: int\n        :param InstanceProxySlowLogDetail: 慢查询详情\n        :type InstanceProxySlowLogDetail: list of InstanceProxySlowlogDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceProxySlowLogDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceProxySlowLogDetail") is not None:
            self.InstanceProxySlowLogDetail = []
            for item in params.get("InstanceProxySlowLogDetail"):
                obj = InstanceProxySlowlogDetail()
                obj._deserialize(item)
                self.InstanceProxySlowLogDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogRequest(AbstractModel):
    """DescribeSlowLog请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param BeginTime: 开始时间\n        :type BeginTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param MinQueryTime: 慢查询阈值（单位：微秒）\n        :type MinQueryTime: int\n        :param Limit: 页面大小\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍\n        :type Offset: int\n        """
        self.InstanceId = None
        self.BeginTime = None
        self.EndTime = None
        self.MinQueryTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.MinQueryTime = params.get("MinQueryTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSlowLogResponse(AbstractModel):
    """DescribeSlowLog返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 慢查询总数\n        :type TotalCount: int\n        :param InstanceSlowlogDetail: 慢查询详情\n        :type InstanceSlowlogDetail: list of InstanceSlowlogDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceSlowlogDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSlowlogDetail") is not None:
            self.InstanceSlowlogDetail = []
            for item in params.get("InstanceSlowlogDetail"):
                obj = InstanceSlowlogDetail()
                obj._deserialize(item)
                self.InstanceSlowlogDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态preparing:待执行，running：执行中，succeed：成功，failed：失败，error 执行出错\n        :type Status: str\n        :param StartTime: 任务开始时间\n        :type StartTime: str\n        :param TaskType: 任务类型\n        :type TaskType: str\n        :param InstanceId: 实例的ID\n        :type InstanceId: str\n        :param TaskMessage: 任务信息，错误时显示错误信息。执行中与成功则为空\n        :type TaskMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.StartTime = None
        self.TaskType = None
        self.InstanceId = None
        self.TaskMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.InstanceId = params.get("InstanceId")
        self.TaskMessage = params.get("TaskMessage")
        self.RequestId = params.get("RequestId")


class DescribeTaskListRequest(AbstractModel):
    """DescribeTaskList请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param Limit: 分页大小\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍（自动向下取整）\n        :type Offset: int\n        :param ProjectIds: 项目Id\n        :type ProjectIds: list of int\n        :param TaskTypes: 任务类型\n        :type TaskTypes: list of str\n        :param BeginTime: 起始时间\n        :type BeginTime: str\n        :param EndTime: 终止时间\n        :type EndTime: str\n        :param TaskStatus: 任务状态\n        :type TaskStatus: list of int\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Limit = None
        self.Offset = None
        self.ProjectIds = None
        self.TaskTypes = None
        self.BeginTime = None
        self.EndTime = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProjectIds = params.get("ProjectIds")
        self.TaskTypes = params.get("TaskTypes")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskListResponse(AbstractModel):
    """DescribeTaskList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务总数\n        :type TotalCount: int\n        :param Tasks: 任务详细信息\n        :type Tasks: list of TaskInfoDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfoDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTendisSlowLogRequest(AbstractModel):
    """DescribeTendisSlowLog请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id：crs-ngvou0i1\n        :type InstanceId: str\n        :param BeginTime: 开始时间：2019-09-08 12:12:41\n        :type BeginTime: str\n        :param EndTime: 结束时间：2019-09-09 12:12:41\n        :type EndTime: str\n        :param MinQueryTime: 慢查询阈值（毫秒）\n        :type MinQueryTime: int\n        :param Limit: 页面大小：20\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍\n        :type Offset: int\n        """
        self.InstanceId = None
        self.BeginTime = None
        self.EndTime = None
        self.MinQueryTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.MinQueryTime = params.get("MinQueryTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTendisSlowLogResponse(AbstractModel):
    """DescribeTendisSlowLog返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 慢查询总数\n        :type TotalCount: int\n        :param TendisSlowLogDetail: 慢查询详情\n        :type TendisSlowLogDetail: list of TendisSlowLogDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TendisSlowLogDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TendisSlowLogDetail") is not None:
            self.TendisSlowLogDetail = []
            for item in params.get("TendisSlowLogDetail"):
                obj = TendisSlowLogDetail()
                obj._deserialize(item)
                self.TendisSlowLogDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyPostpaidInstanceRequest(AbstractModel):
    """DestroyPostpaidInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPostpaidInstanceResponse(AbstractModel):
    """DestroyPostpaidInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务Id\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DestroyPrepaidInstanceRequest(AbstractModel):
    """DestroyPrepaidInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyPrepaidInstanceResponse(AbstractModel):
    """DestroyPrepaidInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单Id\n        :type DealId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class DisableReplicaReadonlyRequest(AbstractModel):
    """DisableReplicaReadonly请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例序号ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableReplicaReadonlyResponse(AbstractModel):
    """DisableReplicaReadonly返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 失败:ERROR，成功:OK\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb 等。\n        :type Product: str\n        :param SecurityGroupId: 安全组Id。\n        :type SecurityGroupId: str\n        :param InstanceIds: 实例ID列表，一个或者多个实例Id组成的数组。\n        :type InstanceIds: list of str\n        """
        self.Product = None
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableReplicaReadonlyRequest(AbstractModel):
    """EnableReplicaReadonly请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例序号ID\n        :type InstanceId: str\n        :param ReadonlyPolicy: 账号路由策略：填写master或者replication，表示路由主节点，从节点；不填路由策略默认为写主节点，读从节点\n        :type ReadonlyPolicy: list of str\n        """
        self.InstanceId = None
        self.ReadonlyPolicy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableReplicaReadonlyResponse(AbstractModel):
    """EnableReplicaReadonly返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 错误：ERROR，正确OK。\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class HotKeyInfo(AbstractModel):
    """热Key详细信息

    """

    def __init__(self):
        """
        :param Key: 热Key\n        :type Key: str\n        :param Type: 类型\n        :type Type: str\n        :param Count: 数量\n        :type Count: int\n        """
        self.Key = None
        self.Type = None
        self.Count = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Inbound(AbstractModel):
    """安全组入站规则

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT或者DROP。\n        :type Action: str\n        :param AddressModule: 地址组id代表的地址集合。\n        :type AddressModule: str\n        :param CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。\n        :type CidrIp: str\n        :param Desc: 描述。\n        :type Desc: str\n        :param IpProtocol: 网络协议，支持udp、tcp等。\n        :type IpProtocol: str\n        :param PortRange: 端口。\n        :type PortRange: str\n        :param ServiceModule: 服务组id代表的协议和端口集合。\n        :type ServiceModule: str\n        :param Id: 安全组id代表的地址集合。\n        :type Id: str\n        """
        self.Action = None
        self.AddressModule = None
        self.CidrIp = None
        self.Desc = None
        self.IpProtocol = None
        self.PortRange = None
        self.ServiceModule = None
        self.Id = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.AddressModule = params.get("AddressModule")
        self.CidrIp = params.get("CidrIp")
        self.Desc = params.get("Desc")
        self.IpProtocol = params.get("IpProtocol")
        self.PortRange = params.get("PortRange")
        self.ServiceModule = params.get("ServiceModule")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance请求参数结构体

    """

    def __init__(self):
        """
        :param TypeId: 实例类型：2 – Redis2.8内存版(标准架构)，3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，6 – Redis4.0内存版(标准架构)，7 – Redis4.0内存版(集群架构)，8 – Redis5.0内存版(标准架构)，9 – Redis5.0内存版(集群架构)。\n        :type TypeId: int\n        :param MemSize: 内存容量，单位为MB， 数值需为1024的整数倍，具体规格以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。
TypeId为标准架构时，MemSize是实例总内存容量；TypeId为集群架构时，MemSize是单分片内存容量。\n        :type MemSize: int\n        :param GoodsNum: 实例数量，单次购买实例数量以 [查询产品售卖规格](https://cloud.tencent.com/document/api/239/30600) 返回的规格为准。\n        :type GoodsNum: int\n        :param Period: 购买时长，在创建包年包月实例的时候需要填写，按量计费实例填1即可，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。\n        :type Period: int\n        :param BillingMode: 付费方式:0-按量计费，1-包年包月。\n        :type BillingMode: int\n        :param ZoneId: 实例所属的可用区ID，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。\n        :type ZoneId: int\n        :param RedisShardNum: 实例分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版、Redis4.0主从版不需要填写。\n        :type RedisShardNum: int\n        :param RedisReplicasNum: 实例副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写。\n        :type RedisReplicasNum: int\n        :param ReplicasReadonly: 是否支持副本只读，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写。\n        :type ReplicasReadonly: bool\n        :param ZoneName: 实例所属的可用区名称，可参考[地域和可用区](https://cloud.tencent.com/document/product/239/4106)  。\n        :type ZoneName: str\n        """
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.BillingMode = None
        self.ZoneId = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.ReplicasReadonly = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.BillingMode = params.get("BillingMode")
        self.ZoneId = params.get("ZoneId")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.ReplicasReadonly = params.get("ReplicasReadonly")
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格，单位：分
注意：此字段可能返回 null，表示取不到有效值。\n        :type Price: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Period: 购买时长，单位：月\n        :type Period: int\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.Period = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格，单位：分
注意：此字段可能返回 null，表示取不到有效值。\n        :type Price: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param MemSize: 分片大小 单位 MB\n        :type MemSize: int\n        :param RedisShardNum: 分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写\n        :type RedisShardNum: int\n        :param RedisReplicasNum: 副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写\n        :type RedisReplicasNum: int\n        """
        self.InstanceId = None
        self.MemSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MemSize = params.get("MemSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceUpgradeInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 价格，单位：分
注意：此字段可能返回 null，表示取不到有效值。\n        :type Price: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InstanceClusterNode(AbstractModel):
    """实例节点类型

    """

    def __init__(self):
        """
        :param Name: 节点名称\n        :type Name: str\n        :param RunId: 实例运行时节点Id\n        :type RunId: str\n        :param Role: 集群角色：0-master；1-slave\n        :type Role: int\n        :param Status: 节点状态：0-readwrite, 1-read, 2-backup\n        :type Status: int\n        :param Connected: 服务状态：0-down；1-on\n        :type Connected: int\n        :param CreateTime: 节点创建时间\n        :type CreateTime: str\n        :param DownTime: 节点下线时间\n        :type DownTime: str\n        :param Slots: 节点slot分布\n        :type Slots: str\n        :param Keys: 节点key分布\n        :type Keys: int\n        :param Qps: 节点qps\n        :type Qps: int\n        :param QpsSlope: 节点qps倾斜度\n        :type QpsSlope: float\n        :param Storage: 节点存储\n        :type Storage: int\n        :param StorageSlope: 节点存储倾斜度\n        :type StorageSlope: float\n        """
        self.Name = None
        self.RunId = None
        self.Role = None
        self.Status = None
        self.Connected = None
        self.CreateTime = None
        self.DownTime = None
        self.Slots = None
        self.Keys = None
        self.Qps = None
        self.QpsSlope = None
        self.Storage = None
        self.StorageSlope = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RunId = params.get("RunId")
        self.Role = params.get("Role")
        self.Status = params.get("Status")
        self.Connected = params.get("Connected")
        self.CreateTime = params.get("CreateTime")
        self.DownTime = params.get("DownTime")
        self.Slots = params.get("Slots")
        self.Keys = params.get("Keys")
        self.Qps = params.get("Qps")
        self.QpsSlope = params.get("QpsSlope")
        self.Storage = params.get("Storage")
        self.StorageSlope = params.get("StorageSlope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceClusterShard(AbstractModel):
    """实例分片列表信息

    """

    def __init__(self):
        """
        :param ShardName: 分片节点名称\n        :type ShardName: str\n        :param ShardId: 分片节点Id\n        :type ShardId: str\n        :param Role: 角色\n        :type Role: int\n        :param Keys: Key数量\n        :type Keys: int\n        :param Slots: slot信息\n        :type Slots: str\n        :param Storage: 使用容量\n        :type Storage: int\n        :param StorageSlope: 容量倾斜率\n        :type StorageSlope: float\n        :param Runid: 实例运行时节点Id\n        :type Runid: str\n        :param Connected: 服务状态：0-down；1-on\n        :type Connected: int\n        """
        self.ShardName = None
        self.ShardId = None
        self.Role = None
        self.Keys = None
        self.Slots = None
        self.Storage = None
        self.StorageSlope = None
        self.Runid = None
        self.Connected = None


    def _deserialize(self, params):
        self.ShardName = params.get("ShardName")
        self.ShardId = params.get("ShardId")
        self.Role = params.get("Role")
        self.Keys = params.get("Keys")
        self.Slots = params.get("Slots")
        self.Storage = params.get("Storage")
        self.StorageSlope = params.get("StorageSlope")
        self.Runid = params.get("Runid")
        self.Connected = params.get("Connected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceEnumParam(AbstractModel):
    """实例枚举类型参数描述

    """

    def __init__(self):
        """
        :param ParamName: 参数名\n        :type ParamName: str\n        :param ValueType: 参数类型：enum\n        :type ValueType: str\n        :param NeedRestart: 修改后是否需要重启：true，false\n        :type NeedRestart: str\n        :param DefaultValue: 参数默认值\n        :type DefaultValue: str\n        :param CurrentValue: 当前运行参数值\n        :type CurrentValue: str\n        :param Tips: 参数说明\n        :type Tips: str\n        :param EnumValue: 参数可取值\n        :type EnumValue: list of str\n        :param Status: 参数状态, 1: 修改中， 2：修改完成\n        :type Status: int\n        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.EnumValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.EnumValue = params.get("EnumValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceIntegerParam(AbstractModel):
    """实例整型参数描述

    """

    def __init__(self):
        """
        :param ParamName: 参数名\n        :type ParamName: str\n        :param ValueType: 参数类型：integer\n        :type ValueType: str\n        :param NeedRestart: 修改后是否需要重启：true，false\n        :type NeedRestart: str\n        :param DefaultValue: 参数默认值\n        :type DefaultValue: str\n        :param CurrentValue: 当前运行参数值\n        :type CurrentValue: str\n        :param Tips: 参数说明\n        :type Tips: str\n        :param Min: 参数最小值\n        :type Min: str\n        :param Max: 参数最大值\n        :type Max: str\n        :param Status: 参数状态, 1: 修改中， 2：修改完成\n        :type Status: int\n        :param Unit: 参数单位
注意：此字段可能返回 null，表示取不到有效值。\n        :type Unit: str\n        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.Min = None
        self.Max = None
        self.Status = None
        self.Unit = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.Min = params.get("Min")
        self.Max = params.get("Max")
        self.Status = params.get("Status")
        self.Unit = params.get("Unit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMultiParam(AbstractModel):
    """实例多选项类型参数描述

    """

    def __init__(self):
        """
        :param ParamName: 参数名\n        :type ParamName: str\n        :param ValueType: 参数类型：multi\n        :type ValueType: str\n        :param NeedRestart: 修改后是否需要重启：true，false\n        :type NeedRestart: str\n        :param DefaultValue: 参数默认值\n        :type DefaultValue: str\n        :param CurrentValue: 当前运行参数值\n        :type CurrentValue: str\n        :param Tips: 参数说明\n        :type Tips: str\n        :param EnumValue: 参数说明\n        :type EnumValue: list of str\n        :param Status: 参数状态, 1: 修改中， 2：修改完成\n        :type Status: int\n        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.EnumValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.EnumValue = params.get("EnumValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNode(AbstractModel):
    """实例节点

    """

    def __init__(self):
        """
        :param Id: Id\n        :type Id: int\n        :param InstanceClusterNode: 节点详细信息\n        :type InstanceClusterNode: list of InstanceClusterNode\n        """
        self.Id = None
        self.InstanceClusterNode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("InstanceClusterNode") is not None:
            self.InstanceClusterNode = []
            for item in params.get("InstanceClusterNode"):
                obj = InstanceClusterNode()
                obj._deserialize(item)
                self.InstanceClusterNode.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParam(AbstractModel):
    """实例参数

    """

    def __init__(self):
        """
        :param Key: 设置参数的名字\n        :type Key: str\n        :param Value: 设置参数的值\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParamHistory(AbstractModel):
    """实例参数修改历史

    """

    def __init__(self):
        """
        :param ParamName: 参数名称\n        :type ParamName: str\n        :param PreValue: 修改前值\n        :type PreValue: str\n        :param NewValue: 修改后值\n        :type NewValue: str\n        :param Status: 状态：1-参数配置修改中；2-参数配置修改成功；3-参数配置修改失败\n        :type Status: int\n        :param ModifyTime: 修改时间\n        :type ModifyTime: str\n        """
        self.ParamName = None
        self.PreValue = None
        self.NewValue = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.PreValue = params.get("PreValue")
        self.NewValue = params.get("NewValue")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceProxySlowlogDetail(AbstractModel):
    """代理慢查询详情

    """

    def __init__(self):
        """
        :param Duration: 慢查询耗时\n        :type Duration: int\n        :param Client: 客户端地址\n        :type Client: str\n        :param Command: 命令\n        :type Command: str\n        :param CommandLine: 详细命令行信息\n        :type CommandLine: str\n        :param ExecuteTime: 执行时间\n        :type ExecuteTime: str\n        """
        self.Duration = None
        self.Client = None
        self.Command = None
        self.CommandLine = None
        self.ExecuteTime = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.Client = params.get("Client")
        self.Command = params.get("Command")
        self.CommandLine = params.get("CommandLine")
        self.ExecuteTime = params.get("ExecuteTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSecurityGroupDetail(AbstractModel):
    """实例安全组信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param SecurityGroupDetails: 安全组信息\n        :type SecurityGroupDetails: list of SecurityGroupDetail\n        """
        self.InstanceId = None
        self.SecurityGroupDetails = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("SecurityGroupDetails") is not None:
            self.SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self.SecurityGroupDetails.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSet(AbstractModel):
    """实例详细信息列表

    """

    def __init__(self):
        """
        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param InstanceId: 实例Id\n        :type InstanceId: str\n        :param Appid: 用户的Appid\n        :type Appid: int\n        :param ProjectId: 项目Id\n        :type ProjectId: int\n        :param RegionId: 地域id 1--广州 4--上海 5-- 中国香港 6--多伦多 7--上海金融 8--北京 9-- 新加坡 11--深圳金融 15--美西（硅谷）16--成都 17--德国 18--韩国 19--重庆 21--印度 22--美东（弗吉尼亚）23--泰国 24--俄罗斯 25--日本\n        :type RegionId: int\n        :param ZoneId: 区域id\n        :type ZoneId: int\n        :param VpcId: vpc网络id 如：75101\n        :type VpcId: int\n        :param SubnetId: vpc网络下子网id 如：46315\n        :type SubnetId: int\n        :param Status: 实例当前状态，0：待初始化；1：实例在流程中；2：实例运行中；-2：实例已隔离；-3：实例待删除\n        :type Status: int\n        :param WanIp: 实例vip\n        :type WanIp: str\n        :param Port: 实例端口号\n        :type Port: int\n        :param Createtime: 实例创建时间\n        :type Createtime: str\n        :param Size: 实例容量大小，单位：MB\n        :type Size: float\n        :param SizeUsed: 该字段已废弃\n        :type SizeUsed: float\n        :param Type: 实例类型：1 – Redis2.8内存版（集群架构），2 – Redis2.8内存版（标准架构），3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版（单机），6 – Redis4.0内存版（标准架构），7 – Redis4.0内存版（集群架构），8 – Redis5.0内存版（标准架构），9 – Redis5.0内存版（集群架构）\n        :type Type: int\n        :param AutoRenewFlag: 实例是否设置自动续费标识，1：设置自动续费；0：未设置自动续费\n        :type AutoRenewFlag: int\n        :param DeadlineTime: 实例到期时间\n        :type DeadlineTime: str\n        :param Engine: 引擎：社区版Redis、腾讯云CKV\n        :type Engine: str\n        :param ProductType: 产品类型：standalone – 标准版，cluster – 集群版\n        :type ProductType: str\n        :param UniqVpcId: vpc网络id 如：vpc-fk33jsf43kgv\n        :type UniqVpcId: str\n        :param UniqSubnetId: vpc网络下子网id 如：subnet-fd3j6l35mm0\n        :type UniqSubnetId: str\n        :param BillingMode: 计费模式：0-按量计费，1-包年包月\n        :type BillingMode: int\n        :param InstanceTitle: 实例运行状态描述：如”实例运行中“\n        :type InstanceTitle: str\n        :param OfflineTime: 计划下线时间\n        :type OfflineTime: str\n        :param SubStatus: 流程中的实例，返回子状态\n        :type SubStatus: int\n        :param Tags: 反亲和性标签\n        :type Tags: list of str\n        :param InstanceNode: 实例节点信息\n        :type InstanceNode: list of InstanceNode\n        :param RedisShardSize: 分片大小\n        :type RedisShardSize: int\n        :param RedisShardNum: 分片数量\n        :type RedisShardNum: int\n        :param RedisReplicasNum: 副本数量\n        :type RedisReplicasNum: int\n        :param PriceId: 计费Id\n        :type PriceId: int\n        :param CloseTime: 隔离时间\n        :type CloseTime: str\n        :param SlaveReadWeight: 从节点读取权重\n        :type SlaveReadWeight: int\n        :param InstanceTags: 实例关联的标签信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceTags: list of InstanceTagInfo\n        :param ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectName: str\n        :param NoAuth: 是否为免密实例，true-免密实例；false-非免密实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type NoAuth: bool\n        :param ClientLimit: 客户端连接数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientLimit: int\n        :param DtsStatus: DTS状态（内部参数，用户可忽略）
注意：此字段可能返回 null，表示取不到有效值。\n        :type DtsStatus: int\n        :param NetLimit: 分片带宽上限，单位MB
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetLimit: int\n        :param PasswordFree: 免密实例标识（内部参数，用户可忽略）
注意：此字段可能返回 null，表示取不到有效值。\n        :type PasswordFree: int\n        :param ReadOnly: 实例只读标识（内部参数，用户可忽略）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReadOnly: int\n        :param Vip6: 内部参数，用户可忽略
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vip6: str\n        :param RemainBandwidthDuration: 内部参数，用户可忽略
注意：此字段可能返回 null，表示取不到有效值。\n        :type RemainBandwidthDuration: str\n        :param DiskSize: Tendis实例的磁盘大小
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskSize: int\n        :param MonitorVersion: 监控版本: 1m-分钟粒度监控，5s-5秒粒度监控
注意：此字段可能返回 null，表示取不到有效值。\n        :type MonitorVersion: str\n        :param ClientLimitMin: 客户端最大连接数可设置的最小值
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientLimitMin: int\n        :param ClientLimitMax: 客户端最大连接数可设置的最大值
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientLimitMax: int\n        :param NodeSet: 实例的节点详细信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeSet: list of RedisNodeInfo\n        :param Region: 实例所在的地域信息，比如ap-guangzhou
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        """
        self.InstanceName = None
        self.InstanceId = None
        self.Appid = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.WanIp = None
        self.Port = None
        self.Createtime = None
        self.Size = None
        self.SizeUsed = None
        self.Type = None
        self.AutoRenewFlag = None
        self.DeadlineTime = None
        self.Engine = None
        self.ProductType = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.BillingMode = None
        self.InstanceTitle = None
        self.OfflineTime = None
        self.SubStatus = None
        self.Tags = None
        self.InstanceNode = None
        self.RedisShardSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.PriceId = None
        self.CloseTime = None
        self.SlaveReadWeight = None
        self.InstanceTags = None
        self.ProjectName = None
        self.NoAuth = None
        self.ClientLimit = None
        self.DtsStatus = None
        self.NetLimit = None
        self.PasswordFree = None
        self.ReadOnly = None
        self.Vip6 = None
        self.RemainBandwidthDuration = None
        self.DiskSize = None
        self.MonitorVersion = None
        self.ClientLimitMin = None
        self.ClientLimitMax = None
        self.NodeSet = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.Appid = params.get("Appid")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.WanIp = params.get("WanIp")
        self.Port = params.get("Port")
        self.Createtime = params.get("Createtime")
        self.Size = params.get("Size")
        self.SizeUsed = params.get("SizeUsed")
        self.Type = params.get("Type")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Engine = params.get("Engine")
        self.ProductType = params.get("ProductType")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.BillingMode = params.get("BillingMode")
        self.InstanceTitle = params.get("InstanceTitle")
        self.OfflineTime = params.get("OfflineTime")
        self.SubStatus = params.get("SubStatus")
        self.Tags = params.get("Tags")
        if params.get("InstanceNode") is not None:
            self.InstanceNode = []
            for item in params.get("InstanceNode"):
                obj = InstanceNode()
                obj._deserialize(item)
                self.InstanceNode.append(obj)
        self.RedisShardSize = params.get("RedisShardSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.PriceId = params.get("PriceId")
        self.CloseTime = params.get("CloseTime")
        self.SlaveReadWeight = params.get("SlaveReadWeight")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.ProjectName = params.get("ProjectName")
        self.NoAuth = params.get("NoAuth")
        self.ClientLimit = params.get("ClientLimit")
        self.DtsStatus = params.get("DtsStatus")
        self.NetLimit = params.get("NetLimit")
        self.PasswordFree = params.get("PasswordFree")
        self.ReadOnly = params.get("ReadOnly")
        self.Vip6 = params.get("Vip6")
        self.RemainBandwidthDuration = params.get("RemainBandwidthDuration")
        self.DiskSize = params.get("DiskSize")
        self.MonitorVersion = params.get("MonitorVersion")
        self.ClientLimitMin = params.get("ClientLimitMin")
        self.ClientLimitMax = params.get("ClientLimitMax")
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSlowlogDetail(AbstractModel):
    """慢查询详情

    """

    def __init__(self):
        """
        :param Duration: 慢查询耗时\n        :type Duration: int\n        :param Client: 客户端地址\n        :type Client: str\n        :param Command: 命令\n        :type Command: str\n        :param CommandLine: 详细命令行信息\n        :type CommandLine: str\n        :param ExecuteTime: 执行时间\n        :type ExecuteTime: str\n        :param Node: 节点ID\n        :type Node: str\n        """
        self.Duration = None
        self.Client = None
        self.Command = None
        self.CommandLine = None
        self.ExecuteTime = None
        self.Node = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.Client = params.get("Client")
        self.Command = params.get("Command")
        self.CommandLine = params.get("CommandLine")
        self.ExecuteTime = params.get("ExecuteTime")
        self.Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    """实例标签信息

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTextParam(AbstractModel):
    """实例字符型参数描述

    """

    def __init__(self):
        """
        :param ParamName: 参数名\n        :type ParamName: str\n        :param ValueType: 参数类型：text\n        :type ValueType: str\n        :param NeedRestart: 修改后是否需要重启：true，false\n        :type NeedRestart: str\n        :param DefaultValue: 参数默认值\n        :type DefaultValue: str\n        :param CurrentValue: 当前运行参数值\n        :type CurrentValue: str\n        :param Tips: 参数说明\n        :type Tips: str\n        :param TextValue: 参数可取值\n        :type TextValue: list of str\n        :param Status: 参数状态, 1: 修改中， 2：修改完成\n        :type Status: int\n        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.TextValue = None
        self.Status = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.TextValue = params.get("TextValue")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMasterGroupRequest(AbstractModel):
    """KillMasterGroup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Password: 1.长度8-30位,推荐使用12位以上的密码
2.不能以"/"开头
3.至少包含两项
    a.小写字母a-z
    b.大写字母A-Z
    c.数字0-9
    d.()`~!@#$%^&*-+=_|{}[]:;<>,.?/\n        :type Password: str\n        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KillMasterGroupResponse(AbstractModel):
    """KillMasterGroup返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ManualBackupInstanceRequest(AbstractModel):
    """ManualBackupInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的实例ID，可通过 DescribeInstance接口返回值中的 InstanceId 获取。\n        :type InstanceId: str\n        :param Remark: 备份的备注信息\n        :type Remark: str\n        """
        self.InstanceId = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualBackupInstanceResponse(AbstractModel):
    """ManualBackupInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModfiyInstancePasswordRequest(AbstractModel):
    """ModfiyInstancePassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param OldPassword: 实例旧密码\n        :type OldPassword: str\n        :param Password: 实例新密码\n        :type Password: str\n        """
        self.InstanceId = None
        self.OldPassword = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldPassword = params.get("OldPassword")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModfiyInstancePasswordResponse(AbstractModel):
    """ModfiyInstancePassword返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param WeekDays: 日期 Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday\n        :type WeekDays: list of str\n        :param TimePeriod: 时间段 00:00-01:00, 01:00-02:00...... 23:00-00:00\n        :type TimePeriod: str\n        :param AutoBackupType: 自动备份类型： 1 “定时回档”\n        :type AutoBackupType: int\n        """
        self.InstanceId = None
        self.WeekDays = None
        self.TimePeriod = None
        self.AutoBackupType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.AutoBackupType = params.get("AutoBackupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig返回参数结构体

    """

    def __init__(self):
        """
        :param AutoBackupType: 自动备份类型： 1 “定时回档”\n        :type AutoBackupType: int\n        :param WeekDays: 日期Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。\n        :type WeekDays: list of str\n        :param TimePeriod: 时间段 00:00-01:00, 01:00-02:00...... 23:00-00:00\n        :type TimePeriod: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class ModifyConnectionConfigRequest(AbstractModel):
    """ModifyConnectionConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例的ID，长度在12-36之间。\n        :type InstanceId: str\n        :param Bandwidth: 附加带宽，大于0，单位MB。\n        :type Bandwidth: int\n        :param ClientLimit: 单分片的总连接数。
未开启副本只读时，下限为10000，上限为40000；
开启副本只读时，下限为10000，上限为10000×(只读副本数+3)。\n        :type ClientLimit: int\n        """
        self.InstanceId = None
        self.Bandwidth = None
        self.ClientLimit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Bandwidth = params.get("Bandwidth")
        self.ClientLimit = params.get("ClientLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConnectionConfigResponse(AbstractModel):
    """ModifyConnectionConfig返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 数据库引擎名称：mariadb,cdb,cynosdb,dcdb,redis,mongodb 等。\n        :type Product: str\n        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组Id组成的数组。\n        :type SecurityGroupIds: list of str\n        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同\n        :type InstanceId: str\n        """
        self.Product = None
        self.SecurityGroupIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceAccountRequest(AbstractModel):
    """ModifyInstanceAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param AccountName: 子账号名称，如果要修改主账号，填root\n        :type AccountName: str\n        :param AccountPassword: 子账号密码\n        :type AccountPassword: str\n        :param Remark: 子账号描述信息\n        :type Remark: str\n        :param ReadonlyPolicy: 子账号路由策略：填写master或者slave，表示路由主节点，从节点\n        :type ReadonlyPolicy: list of str\n        :param Privilege: 子账号读写策略：填写r、w、rw，表示只读，只写，读写策略\n        :type Privilege: str\n        :param NoAuth: true表示将主账号切换为免密账号，这里只适用于主账号，子账号不可免密\n        :type NoAuth: bool\n        """
        self.InstanceId = None
        self.AccountName = None
        self.AccountPassword = None
        self.Remark = None
        self.ReadonlyPolicy = None
        self.Privilege = None
        self.NoAuth = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        self.Remark = params.get("Remark")
        self.ReadonlyPolicy = params.get("ReadonlyPolicy")
        self.Privilege = params.get("Privilege")
        self.NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAccountResponse(AbstractModel):
    """ModifyInstanceAccount返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamsRequest(AbstractModel):
    """ModifyInstanceParams请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceParams: 实例修改的参数列表\n        :type InstanceParams: list of InstanceParam\n        """
        self.InstanceId = None
        self.InstanceParams = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self.InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self.InstanceParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceParamsResponse(AbstractModel):
    """ModifyInstanceParams返回参数结构体

    """

    def __init__(self):
        """
        :param Changed: 修改是否成功。\n        :type Changed: bool\n        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Changed = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Changed = params.get("Changed")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Operation: 修改实例操作，如填写：rename-表示实例重命名；modifyProject-修改实例所属项目；modifyAutoRenew-修改实例续费标记\n        :type Operation: str\n        :param InstanceIds: 实例Id\n        :type InstanceIds: list of str\n        :param InstanceNames: 实例的新名称\n        :type InstanceNames: list of str\n        :param ProjectId: 项目Id\n        :type ProjectId: int\n        :param AutoRenews: 自动续费标识。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费\n        :type AutoRenews: list of int\n        :param InstanceId: 已经废弃\n        :type InstanceId: str\n        :param InstanceName: 已经废弃\n        :type InstanceName: str\n        :param AutoRenew: 已经废弃\n        :type AutoRenew: int\n        """
        self.Operation = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.ProjectId = None
        self.AutoRenews = None
        self.InstanceId = None
        self.InstanceName = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenews = params.get("AutoRenews")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMaintenanceWindowRequest(AbstractModel):
    """ModifyMaintenanceWindow请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param StartTime: 维护时间窗起始时间，如：17:00\n        :type StartTime: str\n        :param EndTime: 维护时间窗结束时间，如：19:00\n        :type EndTime: str\n        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintenanceWindowResponse(AbstractModel):
    """ModifyMaintenanceWindow返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 修改状态：success 或者 failed\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    """ModifyNetworkConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param Operation: 操作类型：changeVip——修改实例VIP；changeVpc——修改实例子网；changeBaseToVpc——基础网络转VPC网络\n        :type Operation: str\n        :param Vip: VIP地址，changeVip的时候填写，不填则默认分配\n        :type Vip: str\n        :param VpcId: 私有网络ID，changeVpc、changeBaseToVpc的时候需要提供\n        :type VpcId: str\n        :param SubnetId: 子网ID，changeVpc、changeBaseToVpc的时候需要提供\n        :type SubnetId: str\n        """
        self.InstanceId = None
        self.Operation = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Operation = params.get("Operation")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkConfigResponse(AbstractModel):
    """ModifyNetworkConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 执行状态：true|false\n        :type Status: bool\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        :param VpcId: 私有网络ID\n        :type VpcId: str\n        :param Vip: VIP地址\n        :type Vip: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.SubnetId = None
        self.VpcId = None
        self.Vip = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Vip = params.get("Vip")
        self.RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 源参数模板 ID。\n        :type TemplateId: str\n        :param Name: 参数模板名称。\n        :type Name: str\n        :param Description: 参数模板描述。\n        :type Description: str\n        :param ParamList: 参数列表。\n        :type ParamList: list of InstanceParam\n        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.ParamList = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = InstanceParam()
                obj._deserialize(item)
                self.ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """安全组出站规则

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT或者DROP。\n        :type Action: str\n        :param AddressModule: 地址组id代表的地址集合。\n        :type AddressModule: str\n        :param CidrIp: 来源Ip或Ip段，例如192.168.0.0/16。\n        :type CidrIp: str\n        :param Desc: 描述。\n        :type Desc: str\n        :param IpProtocol: 网络协议，支持udp、tcp等。\n        :type IpProtocol: str\n        :param PortRange: 端口。\n        :type PortRange: str\n        :param ServiceModule: 服务组id代表的协议和端口集合。\n        :type ServiceModule: str\n        :param Id: 安全组id代表的地址集合。\n        :type Id: str\n        """
        self.Action = None
        self.AddressModule = None
        self.CidrIp = None
        self.Desc = None
        self.IpProtocol = None
        self.PortRange = None
        self.ServiceModule = None
        self.Id = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.AddressModule = params.get("AddressModule")
        self.CidrIp = params.get("CidrIp")
        self.Desc = params.get("Desc")
        self.IpProtocol = params.get("IpProtocol")
        self.PortRange = params.get("PortRange")
        self.ServiceModule = params.get("ServiceModule")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateInfo(AbstractModel):
    """参数模板信息

    """

    def __init__(self):
        """
        :param TemplateId: 参数模板ID\n        :type TemplateId: str\n        :param Name: 参数模板名称\n        :type Name: str\n        :param Description: 参数模板描述\n        :type Description: str\n        :param ProductType: 产品类型：1 – Redis2.8内存版（集群架构），2 – Redis2.8内存版（标准架构），3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版（单机），6 – Redis4.0内存版（标准架构），7 – Redis4.0内存版（集群架构），8 – Redis5.0内存版（标准架构），9 – Redis5.0内存版（集群架构）\n        :type ProductType: int\n        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.ProductType = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ProductType = params.get("ProductType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterDetail(AbstractModel):
    """Redis参数模板参数详情

    """

    def __init__(self):
        """
        :param Name: 参数名称\n        :type Name: str\n        :param ParamType: 参数类型\n        :type ParamType: str\n        :param Default: 参数默认值\n        :type Default: str\n        :param Description: 参数描述\n        :type Description: str\n        :param CurrentValue: 参数当前值\n        :type CurrentValue: str\n        :param NeedReboot: 修改参数后，是否需要重启数据库以使参数生效。可能的值包括：0-不需要重启；1-需要重启\n        :type NeedReboot: int\n        :param Max: 参数允许的最大值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Max: str\n        :param Min: 参数允许的最小值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Min: str\n        :param EnumValue: 参数的可选枚举值。如果为非枚举参数，则为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnumValue: list of str\n        """
        self.Name = None
        self.ParamType = None
        self.Default = None
        self.Description = None
        self.CurrentValue = None
        self.NeedReboot = None
        self.Max = None
        self.Min = None
        self.EnumValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ParamType = params.get("ParamType")
        self.Default = params.get("Default")
        self.Description = params.get("Description")
        self.CurrentValue = params.get("CurrentValue")
        self.NeedReboot = params.get("NeedReboot")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.EnumValue = params.get("EnumValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductConf(AbstractModel):
    """产品信息

    """

    def __init__(self):
        """
        :param Type: 产品类型，2 – Redis2.8内存版(标准架构)，3 – CKV 3.2内存版(标准架构)，4 – CKV 3.2内存版(集群架构)，5 – Redis2.8内存版(单机版)，6 – Redis4.0内存版(标准架构)，7 – Redis4.0内存版(集群架构)，8 – Redis5.0内存版(标准架构)，9 – Redis5.0内存版(集群架构)，10 – Redis4.0混合存储版Tendis\n        :type Type: int\n        :param TypeName: 产品名称，Redis主从版，CKV主从版，CKV集群版，Redis单机版，Redis集群版，混合存储版Tendis\n        :type TypeName: str\n        :param MinBuyNum: 购买时的最小数量\n        :type MinBuyNum: int\n        :param MaxBuyNum: 购买时的最大数量\n        :type MaxBuyNum: int\n        :param Saleout: 产品是否售罄\n        :type Saleout: bool\n        :param Engine: 产品引擎，腾讯云CKV或者社区版Redis\n        :type Engine: str\n        :param Version: 兼容版本，Redis-2.8，Redis-3.2，Redis-4.0\n        :type Version: str\n        :param TotalSize: 规格总大小，单位G\n        :type TotalSize: list of str\n        :param ShardSize: 每个分片大小，单位G\n        :type ShardSize: list of str\n        :param ReplicaNum: 副本数量\n        :type ReplicaNum: list of str\n        :param ShardNum: 分片数量\n        :type ShardNum: list of str\n        :param PayMode: 支持的计费模式，1-包年包月，0-按量计费\n        :type PayMode: str\n        :param EnableRepicaReadOnly: 是否支持副本只读\n        :type EnableRepicaReadOnly: bool\n        """
        self.Type = None
        self.TypeName = None
        self.MinBuyNum = None
        self.MaxBuyNum = None
        self.Saleout = None
        self.Engine = None
        self.Version = None
        self.TotalSize = None
        self.ShardSize = None
        self.ReplicaNum = None
        self.ShardNum = None
        self.PayMode = None
        self.EnableRepicaReadOnly = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        self.MinBuyNum = params.get("MinBuyNum")
        self.MaxBuyNum = params.get("MaxBuyNum")
        self.Saleout = params.get("Saleout")
        self.Engine = params.get("Engine")
        self.Version = params.get("Version")
        self.TotalSize = params.get("TotalSize")
        self.ShardSize = params.get("ShardSize")
        self.ReplicaNum = params.get("ReplicaNum")
        self.ShardNum = params.get("ShardNum")
        self.PayMode = params.get("PayMode")
        self.EnableRepicaReadOnly = params.get("EnableRepicaReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyNodes(AbstractModel):
    """Proxy节点信息

    """

    def __init__(self):
        """
        :param NodeId: 节点ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeId: str\n        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisBackupSet(AbstractModel):
    """实例的备份数组

    """

    def __init__(self):
        """
        :param StartTime: 开始备份的时间\n        :type StartTime: str\n        :param BackupId: 备份ID\n        :type BackupId: str\n        :param BackupType: 备份类型。 manualBackupInstance：用户发起的手动备份； systemBackupInstance：凌晨系统发起的备份\n        :type BackupType: str\n        :param Status: 备份状态。  1:"备份被其它流程锁定";  2:"备份正常，没有被任何流程锁定";  -1:"备份已过期"； 3:"备份正在被导出";  4:"备份导出成功"\n        :type Status: int\n        :param Remark: 备份的备注信息\n        :type Remark: str\n        :param Locked: 备份是否被锁定，0：未被锁定；1：已被锁定\n        :type Locked: int\n        """
        self.StartTime = None
        self.BackupId = None
        self.BackupType = None
        self.Status = None
        self.Remark = None
        self.Locked = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.BackupId = params.get("BackupId")
        self.BackupType = params.get("BackupType")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.Locked = params.get("Locked")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisCommonInstanceList(AbstractModel):
    """单个实例信息

    """

    def __init__(self):
        """
        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param AppId: 用户id\n        :type AppId: int\n        :param ProjectId: 实例所属项目id\n        :type ProjectId: int\n        :param Region: 实例接入区域\n        :type Region: str\n        :param Zone: 实例接入zone\n        :type Zone: str\n        :param VpcId: 实例网络id\n        :type VpcId: str\n        :param SubnetId: 子网id\n        :type SubnetId: str\n        :param Status: 实例状态信息，1-流程中 ,2-运行中, -2-实例已隔离 ,-3-实例待回收, -4-实例已删除\n        :type Status: str\n        :param Vips: 实例网络ip\n        :type Vips: list of str\n        :param Vport: 实例网络端口\n        :type Vport: int\n        :param Createtime: 实例创建时间\n        :type Createtime: str\n        :param PayMode: 计费类型，0-按量计费，1-包年包月\n        :type PayMode: int\n        :param NetType: 网络类型，0-基础网络，1-VPC网络\n        :type NetType: int\n        """
        self.InstanceName = None
        self.InstanceId = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vips = None
        self.Vport = None
        self.Createtime = None
        self.PayMode = None
        self.NetType = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vips = params.get("Vips")
        self.Vport = params.get("Vport")
        self.Createtime = params.get("Createtime")
        self.PayMode = params.get("PayMode")
        self.NetType = params.get("NetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNode(AbstractModel):
    """Redis节点的运行信息

    """

    def __init__(self):
        """
        :param Keys: 节点key的个数\n        :type Keys: int\n        :param Slot: 节点slot分布\n        :type Slot: str\n        :param NodeId: 节点的序列ID\n        :type NodeId: str\n        :param Status: 节点的状态\n        :type Status: str\n        :param Role: 节点角色\n        :type Role: str\n        """
        self.Keys = None
        self.Slot = None
        self.NodeId = None
        self.Status = None
        self.Role = None


    def _deserialize(self, params):
        self.Keys = params.get("Keys")
        self.Slot = params.get("Slot")
        self.NodeId = params.get("NodeId")
        self.Status = params.get("Status")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodeInfo(AbstractModel):
    """描述Redis实例的主节点或者副本节点信息

    """

    def __init__(self):
        """
        :param NodeType: 节点类型，0 为主节点，1 为副本节点\n        :type NodeType: int\n        :param NodeId: 主节点或者副本节点的ID，创建时不需要传递此参数。\n        :type NodeId: int\n        :param ZoneId: 主节点或者副本节点的可用区ID\n        :type ZoneId: int\n        :param ZoneName: 主节点或者副本节点的可用区名称\n        :type ZoneName: str\n        """
        self.NodeType = None
        self.NodeId = None
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.NodeType = params.get("NodeType")
        self.NodeId = params.get("NodeId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedisNodes(AbstractModel):
    """Redis节点信息

    """

    def __init__(self):
        """
        :param NodeId: 节点ID\n        :type NodeId: str\n        :param NodeRole: 节点角色\n        :type NodeRole: str\n        :param ClusterId: 分片ID\n        :type ClusterId: int\n        :param ZoneId: 可用区ID\n        :type ZoneId: int\n        """
        self.NodeId = None
        self.NodeRole = None
        self.ClusterId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeRole = params.get("NodeRole")
        self.ClusterId = params.get("ClusterId")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionConf(AbstractModel):
    """地域信息

    """

    def __init__(self):
        """
        :param RegionId: 地域ID\n        :type RegionId: str\n        :param RegionName: 地域名称\n        :type RegionName: str\n        :param RegionShortName: 地域简称\n        :type RegionShortName: str\n        :param Area: 地域所在大区名称\n        :type Area: str\n        :param ZoneSet: 可用区信息\n        :type ZoneSet: list of ZoneCapacityConf\n        """
        self.RegionId = None
        self.RegionName = None
        self.RegionShortName = None
        self.Area = None
        self.ZoneSet = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RegionShortName = params.get("RegionShortName")
        self.Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceRequest(AbstractModel):
    """RenewInstance请求参数结构体

    """

    def __init__(self):
        """
        :param Period: 购买时长，单位：月\n        :type Period: int\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.Period = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 交易ID\n        :type DealId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ReplicaGroup(AbstractModel):
    """实例节点信息

    """

    def __init__(self):
        """
        :param GroupId: 节点组ID\n        :type GroupId: int\n        :param GroupName: 节点组的名称，主节点为空\n        :type GroupName: str\n        :param ZoneId: 节点的可用区ID，比如ap-guangzhou-1\n        :type ZoneId: str\n        :param Role: 节点组类型，master为主节点，replica为副本节点\n        :type Role: str\n        :param RedisNodes: 节点组节点列表\n        :type RedisNodes: list of RedisNode\n        """
        self.GroupId = None
        self.GroupName = None
        self.ZoneId = None
        self.Role = None
        self.RedisNodes = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ZoneId = params.get("ZoneId")
        self.Role = params.get("Role")
        if params.get("RedisNodes") is not None:
            self.RedisNodes = []
            for item in params.get("RedisNodes"):
                obj = RedisNode()
                obj._deserialize(item)
                self.RedisNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: Redis实例ID\n        :type InstanceId: str\n        :param Password: 重置的密码（切换为免密实例时，可不传；其他情况必传）\n        :type Password: str\n        :param NoAuth: 是否切换免密实例，false-切换为非免密码实例，true-切换为免密码实例；默认false\n        :type NoAuth: bool\n        """
        self.InstanceId = None
        self.Password = None
        self.NoAuth = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        self.NoAuth = params.get("NoAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID（修改密码时的任务ID，如果时切换免密码或者非免密码实例，则无需关注此返回值）\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResourceTag(AbstractModel):
    """API购买实例绑定标签

    """

    def __init__(self):
        """
        :param TagKey: 标签key\n        :type TagKey: str\n        :param TagValue: 标签value\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。\n        :type InstanceId: str\n        :param BackupId: 备份ID，可通过 GetRedisBackupList 接口返回值中的 backupId 获取\n        :type BackupId: str\n        :param Password: 实例密码，恢复实例时，需要校验实例密码（免密实例不需要传密码）\n        :type Password: str\n        """
        self.InstanceId = None
        self.BackupId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，可通过 DescribeTaskInfo 接口查询任务执行状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        """
        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss。\n        :type CreateTime: str\n        :param ProjectId: 项目ID。\n        :type ProjectId: int\n        :param SecurityGroupId: 安全组ID。\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称。\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: 安全组备注。\n        :type SecurityGroupRemark: str\n        :param Outbound: 出站规则。\n        :type Outbound: list of Outbound\n        :param Inbound: 入站规则。\n        :type Inbound: list of Inbound\n        """
        self.CreateTime = None
        self.ProjectId = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.Outbound = None
        self.Inbound = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self.Outbound.append(obj)
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupDetail(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目Id\n        :type ProjectId: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param SecurityGroupId: 安全组Id\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称\n        :type SecurityGroupName: str\n        :param SecurityGroupRemark: 安全组标记\n        :type SecurityGroupRemark: str\n        :param InboundRule: 安全组入站规则\n        :type InboundRule: list of SecurityGroupsInboundAndOutbound\n        :param OutboundRule: 安全组出站规则\n        :type OutboundRule: list of SecurityGroupsInboundAndOutbound\n        """
        self.ProjectId = None
        self.CreateTime = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.InboundRule = None
        self.OutboundRule = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("InboundRule") is not None:
            self.InboundRule = []
            for item in params.get("InboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self.InboundRule.append(obj)
        if params.get("OutboundRule") is not None:
            self.OutboundRule = []
            for item in params.get("OutboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self.OutboundRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupsInboundAndOutbound(AbstractModel):
    """安全组出入规则

    """

    def __init__(self):
        """
        :param Action: 执行动作\n        :type Action: str\n        :param Ip: IP地址\n        :type Ip: str\n        :param Port: 端口号\n        :type Port: str\n        :param Proto: 协议类型\n        :type Proto: str\n        """
        self.Action = None
        self.Ip = None
        self.Port = None
        self.Proto = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceCommand(AbstractModel):
    """访问命令

    """

    def __init__(self):
        """
        :param Cmd: 命令\n        :type Cmd: str\n        :param Count: 执行次数\n        :type Count: int\n        """
        self.Cmd = None
        self.Count = None


    def _deserialize(self, params):
        self.Cmd = params.get("Cmd")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInfo(AbstractModel):
    """访问来源信息

    """

    def __init__(self):
        """
        :param Ip: 来源IP\n        :type Ip: str\n        :param Conn: 连接数\n        :type Conn: int\n        :param Cmd: 命令\n        :type Cmd: int\n        """
        self.Ip = None
        self.Conn = None
        self.Cmd = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Conn = params.get("Conn")
        self.Cmd = params.get("Cmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartupInstanceRequest(AbstractModel):
    """StartupInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartupInstanceResponse(AbstractModel):
    """StartupInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务id\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SwitchInstanceVipRequest(AbstractModel):
    """SwitchInstanceVip请求参数结构体

    """

    def __init__(self):
        """
        :param SrcInstanceId: 源实例ID\n        :type SrcInstanceId: str\n        :param DstInstanceId: 目标实例ID\n        :type DstInstanceId: str\n        :param TimeDelay: 单位为秒。源实例与目标实例间DTS已断开时间，如果DTS断开时间大于TimeDelay，则不切换VIP，建议尽量根据业务设置一个可接受的值。\n        :type TimeDelay: int\n        :param ForceSwitch: 在DTS断开的情况下是否强制切换。1：强制切换，0：不强制切换\n        :type ForceSwitch: int\n        :param SwitchTime: now: 立即切换，syncComplete：等待同步完成后切换\n        :type SwitchTime: str\n        """
        self.SrcInstanceId = None
        self.DstInstanceId = None
        self.TimeDelay = None
        self.ForceSwitch = None
        self.SwitchTime = None


    def _deserialize(self, params):
        self.SrcInstanceId = params.get("SrcInstanceId")
        self.DstInstanceId = params.get("DstInstanceId")
        self.TimeDelay = params.get("TimeDelay")
        self.ForceSwitch = params.get("ForceSwitch")
        self.SwitchTime = params.get("SwitchTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchInstanceVipResponse(AbstractModel):
    """SwitchInstanceVip返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class TaskInfoDetail(AbstractModel):
    """任务信息详情

    """

    def __init__(self):
        """
        :param TaskId: 任务Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: int\n        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTime: str\n        :param TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskType: str\n        :param InstanceName: 实例名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param InstanceId: 实例Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: int\n        :param Progress: 任务进度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Progress: float\n        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndTime: str\n        :param Result: 任务状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: int\n        """
        self.TaskId = None
        self.StartTime = None
        self.TaskType = None
        self.InstanceName = None
        self.InstanceId = None
        self.ProjectId = None
        self.Progress = None
        self.EndTime = None
        self.Result = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.ProjectId = params.get("ProjectId")
        self.Progress = params.get("Progress")
        self.EndTime = params.get("EndTime")
        self.Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisNodes(AbstractModel):
    """tendis节点信息

    """

    def __init__(self):
        """
        :param NodeId: 节点ID\n        :type NodeId: str\n        :param NodeRole: 节点角色\n        :type NodeRole: str\n        """
        self.NodeId = None
        self.NodeRole = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.NodeRole = params.get("NodeRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TendisSlowLogDetail(AbstractModel):
    """Tendis慢查询详情

    """

    def __init__(self):
        """
        :param ExecuteTime: 执行时间\n        :type ExecuteTime: str\n        :param Duration: 慢查询耗时（毫秒）\n        :type Duration: int\n        :param Command: 命令\n        :type Command: str\n        :param CommandLine: 详细命令行信息\n        :type CommandLine: str\n        :param Node: 节点ID\n        :type Node: str\n        """
        self.ExecuteTime = None
        self.Duration = None
        self.Command = None
        self.CommandLine = None
        self.Node = None


    def _deserialize(self, params):
        self.ExecuteTime = params.get("ExecuteTime")
        self.Duration = params.get("Duration")
        self.Command = params.get("Command")
        self.CommandLine = params.get("CommandLine")
        self.Node = params.get("Node")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradeDealDetail(AbstractModel):
    """订单交易信息

    """

    def __init__(self):
        """
        :param DealId: 订单号ID，调用云API时使用此ID\n        :type DealId: str\n        :param DealName: 长订单ID，反馈订单问题给官方客服使用此ID\n        :type DealName: str\n        :param ZoneId: 可用区id\n        :type ZoneId: int\n        :param GoodsNum: 订单关联的实例数\n        :type GoodsNum: int\n        :param Creater: 创建用户uin\n        :type Creater: str\n        :param CreatTime: 订单创建时间\n        :type CreatTime: str\n        :param OverdueTime: 订单超时时间\n        :type OverdueTime: str\n        :param EndTime: 订单完成时间\n        :type EndTime: str\n        :param Status: 订单状态 1：未支付 2:已支付，未发货 3:发货中 4:发货成功 5:发货失败 6:已退款 7:已关闭订单 8:订单过期 9:订单已失效 10:产品已失效 11:代付拒绝 12:支付中\n        :type Status: int\n        :param Description: 订单状态描述\n        :type Description: str\n        :param Price: 订单实际总价，单位：分\n        :type Price: int\n        :param InstanceIds: 实例ID\n        :type InstanceIds: list of str\n        """
        self.DealId = None
        self.DealName = None
        self.ZoneId = None
        self.GoodsNum = None
        self.Creater = None
        self.CreatTime = None
        self.OverdueTime = None
        self.EndTime = None
        self.Status = None
        self.Description = None
        self.Price = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.ZoneId = params.get("ZoneId")
        self.GoodsNum = params.get("GoodsNum")
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.OverdueTime = params.get("OverdueTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Price = params.get("Price")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param MemSize: 分片大小 单位 MB\n        :type MemSize: int\n        :param RedisShardNum: 分片数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写\n        :type RedisShardNum: int\n        :param RedisReplicasNum: 副本数量，Redis2.8主从版、CKV主从版和Redis2.8单机版不需要填写\n        :type RedisReplicasNum: int\n        :param NodeSet: 多AZ实例增加副本时的附带信息，非多AZ实例不需要传此参数。多AZ增加副本时此参数为必传参数，传入要增加的副本的信息，包括副本的可用区和副本的类型（NodeType为1）\n        :type NodeSet: list of RedisNodeInfo\n        """
        self.InstanceId = None
        self.MemSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.NodeSet = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MemSize = params.get("MemSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = RedisNodeInfo()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID\n        :type DealId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class UpgradeInstanceVersionRequest(AbstractModel):
    """UpgradeInstanceVersion请求参数结构体

    """

    def __init__(self):
        """
        :param TargetInstanceType: 目标实例类型，同 [CreateInstances](https://cloud.tencent.com/document/api/239/20026) 的Type，即实例要变更的目标类型\n        :type TargetInstanceType: str\n        :param SwitchOption: 切换模式：1-维护时间窗切换，2-立即切换\n        :type SwitchOption: int\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.TargetInstanceType = None
        self.SwitchOption = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.TargetInstanceType = params.get("TargetInstanceType")
        self.SwitchOption = params.get("SwitchOption")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceVersionResponse(AbstractModel):
    """UpgradeInstanceVersion返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID\n        :type DealId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class UpgradeVersionToMultiAvailabilityZonesRequest(AbstractModel):
    """UpgradeVersionToMultiAvailabilityZones请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeVersionToMultiAvailabilityZonesResponse(AbstractModel):
    """UpgradeVersionToMultiAvailabilityZones返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务ID\n        :type FlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ZoneCapacityConf(AbstractModel):
    """可用区内产品信息

    """

    def __init__(self):
        """
        :param ZoneId: 可用区ID：如ap-guangzhou-3\n        :type ZoneId: str\n        :param ZoneName: 可用区名称\n        :type ZoneName: str\n        :param IsSaleout: 可用区是否售罄\n        :type IsSaleout: bool\n        :param IsDefault: 是否为默认可用区\n        :type IsDefault: bool\n        :param NetWorkType: 网络类型：basenet -- 基础网络；vpcnet -- VPC网络\n        :type NetWorkType: list of str\n        :param ProductSet: 可用区内产品规格等信息\n        :type ProductSet: list of ProductConf\n        :param OldZoneId: 可用区ID：如100003\n        :type OldZoneId: int\n        """
        self.ZoneId = None
        self.ZoneName = None
        self.IsSaleout = None
        self.IsDefault = None
        self.NetWorkType = None
        self.ProductSet = None
        self.OldZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.IsSaleout = params.get("IsSaleout")
        self.IsDefault = params.get("IsDefault")
        self.NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self.ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self.ProductSet.append(obj)
        self.OldZoneId = params.get("OldZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        