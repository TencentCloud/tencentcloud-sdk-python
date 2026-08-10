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


class AssetsInfo(AbstractModel):
    r"""资产列表数组

    """

    def __init__(self):
        r"""
        :param _AddTime: <p>创建时间</p>
        :type AddTime: int
        :param _Aid: <p>资产 ID</p>
        :type Aid: int
        :param _AssetsIp: <p>数据资产 IP</p>
        :type AssetsIp: str
        :param _AssetsName: <p>数据资产名称</p>
        :type AssetsName: str
        :param _AssetsPort: <p>数据资产端口</p>
        :type AssetsPort: int
        :param _AssetsType: <p>数据资产类型</p>
        :type AssetsType: str
        :param _AssetsVersion: <p>资产版本</p>
        :type AssetsVersion: str
        :param _AssetsAddType: <p>是否动态</p>
        :type AssetsAddType: int
        :param _Status: <p>是否删除</p>
        :type Status: int
        :param _UpdateTime: <p>最后一次修改时间</p>
        :type UpdateTime: int
        :param _VpcId: <p>资产的vpc</p>
        :type VpcId: str
        :param _RegionId: <p>地域</p>
        :type RegionId: str
        :param _Permission: <p>审计权限</p>
        :type Permission: int
        :param _InstanceId: <p>实例ID</p>
        :type InstanceId: str
        :param _InstanceName: <p>实例名称</p>
        :type InstanceName: str
        :param _AddType: <p>用来区分自建资产是已通过cvm还是添加ip的方式</p>
        :type AddType: int
        :param _AssetSubnetId: <p>子网Id</p>
        :type AssetSubnetId: str
        :param _UploadPem: <p>是否已上传数据库私钥（0 否，1 是）</p>
        :type UploadPem: int
        :param _AliveStatus: <p>资产状态栏 0:正常 1:已删除（目前仅对tencentDB有效）</p>
        :type AliveStatus: int
        :param _AgentOn: <p>开启agent(0:关闭;1:开启)</p>
        :type AgentOn: int
        :param _CasbOn: <p>开启agent(0:关闭;1:开启)</p>
        :type CasbOn: int
        :param _GroupId: <p>只读组/集群ID</p>
        :type GroupId: str
        :param _Available: <p>PROXY_OFF: 未开启Casb代理;PROXY_ERROR:Casb代理接口返回异常;PROXY_BOUND:已绑定;PROXY_UNBOUND:未绑定;UNPAID:未购买;UNSUPPORTED:类型不支持;METADATA_NOT_FOUND:元数据不存在;QUOTA_EXCEEDED:Casb额度不足</p>
        :type Available: str
        :param _CdbOn: <p>cdbOn</p>
        :type CdbOn: int
        :param _DbPlatform: <p>平台位数 32位 64位</p>
        :type DbPlatform: str
        :param _DbCharset: <p>编码</p>
        :type DbCharset: str
        :param _OsPolicy: <p>操作系统</p>
        :type OsPolicy: str
        :param _BidirectionOn: <p>是否开启双向审计</p>
        :type BidirectionOn: int
        :param _BidirectionMaxLine: <p>最大返回行数</p>
        :type BidirectionMaxLine: int
        :param _BidirectionMaxStorage: <p>最大返回大小</p>
        :type BidirectionMaxStorage: int
        :param _BidirectionAllow: <p>是否允许开通双向审计(1.允许；0不允许)</p>
        :type BidirectionAllow: int
        :param _BidirectionDelivery: <p>启双向审计的日志投递(1.开启;0.关闭)</p>
        :type BidirectionDelivery: int
        :param _RoStatus: <p>只读状态</p>
        :type RoStatus: str
        :param _AgentBound: <p>当前资产是否开启了对当前Agent的采集策略</p>
        :type AgentBound: bool
        :param _CdbErrorMsg: <p>错误信息</p>
        :type CdbErrorMsg: str
        :param _DsgcBindingInfo: <p>资产 DSGC 绑定信息</p>
        :type DsgcBindingInfo: :class:`tencentcloud.cds.v20180420.models.DsgcBindingInfo`
        :param _BindingRules: <p>绑定的规则Ids</p>
        :type BindingRules: list of IdWithName
        :param _BindingModels: <p>绑定的模型Ids</p>
        :type BindingModels: list of IdWithName
        :param _GroupName: <p>所属组名</p>
        :type GroupName: str
        :param _AssetGroupId: <p>资产组Id</p>
        :type AssetGroupId: int
        :param _IsNewCloudAudit: <p>是否是新云原生审计流程</p>
        :type IsNewCloudAudit: bool
        :param _AuditCapability: <p>审计功能支持说明</p>
        :type AuditCapability: list of AuditCapability
        :param _TrafficMirrorOn: <p>1</p><p>取值范围：[0, 1]</p>
        :type TrafficMirrorOn: int
        :param _AuditScope: <p>流量镜像审计范围</p><p>枚举值：</p><ul><li>ALL： 全地域</li><li>REGION： 资产所在地域</li><li>VPC： 资产所在VPC</li></ul><p>默认值：REGION</p>
        :type AuditScope: str
        :param _InstanceGroupId: <p>实例集群ID</p>
        :type InstanceGroupId: str
        """
        self._AddTime = None
        self._Aid = None
        self._AssetsIp = None
        self._AssetsName = None
        self._AssetsPort = None
        self._AssetsType = None
        self._AssetsVersion = None
        self._AssetsAddType = None
        self._Status = None
        self._UpdateTime = None
        self._VpcId = None
        self._RegionId = None
        self._Permission = None
        self._InstanceId = None
        self._InstanceName = None
        self._AddType = None
        self._AssetSubnetId = None
        self._UploadPem = None
        self._AliveStatus = None
        self._AgentOn = None
        self._CasbOn = None
        self._GroupId = None
        self._Available = None
        self._CdbOn = None
        self._DbPlatform = None
        self._DbCharset = None
        self._OsPolicy = None
        self._BidirectionOn = None
        self._BidirectionMaxLine = None
        self._BidirectionMaxStorage = None
        self._BidirectionAllow = None
        self._BidirectionDelivery = None
        self._RoStatus = None
        self._AgentBound = None
        self._CdbErrorMsg = None
        self._DsgcBindingInfo = None
        self._BindingRules = None
        self._BindingModels = None
        self._GroupName = None
        self._AssetGroupId = None
        self._IsNewCloudAudit = None
        self._AuditCapability = None
        self._TrafficMirrorOn = None
        self._AuditScope = None
        self._InstanceGroupId = None

    @property
    def AddTime(self):
        r"""<p>创建时间</p>
        :rtype: int
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def Aid(self):
        r"""<p>资产 ID</p>
        :rtype: int
        """
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid

    @property
    def AssetsIp(self):
        r"""<p>数据资产 IP</p>
        :rtype: str
        """
        return self._AssetsIp

    @AssetsIp.setter
    def AssetsIp(self, AssetsIp):
        self._AssetsIp = AssetsIp

    @property
    def AssetsName(self):
        r"""<p>数据资产名称</p>
        :rtype: str
        """
        return self._AssetsName

    @AssetsName.setter
    def AssetsName(self, AssetsName):
        self._AssetsName = AssetsName

    @property
    def AssetsPort(self):
        r"""<p>数据资产端口</p>
        :rtype: int
        """
        return self._AssetsPort

    @AssetsPort.setter
    def AssetsPort(self, AssetsPort):
        self._AssetsPort = AssetsPort

    @property
    def AssetsType(self):
        r"""<p>数据资产类型</p>
        :rtype: str
        """
        return self._AssetsType

    @AssetsType.setter
    def AssetsType(self, AssetsType):
        self._AssetsType = AssetsType

    @property
    def AssetsVersion(self):
        r"""<p>资产版本</p>
        :rtype: str
        """
        return self._AssetsVersion

    @AssetsVersion.setter
    def AssetsVersion(self, AssetsVersion):
        self._AssetsVersion = AssetsVersion

    @property
    def AssetsAddType(self):
        r"""<p>是否动态</p>
        :rtype: int
        """
        return self._AssetsAddType

    @AssetsAddType.setter
    def AssetsAddType(self, AssetsAddType):
        self._AssetsAddType = AssetsAddType

    @property
    def Status(self):
        r"""<p>是否删除</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UpdateTime(self):
        r"""<p>最后一次修改时间</p>
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def VpcId(self):
        r"""<p>资产的vpc</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def RegionId(self):
        r"""<p>地域</p>
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Permission(self):
        r"""<p>审计权限</p>
        :rtype: int
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def InstanceId(self):
        r"""<p>实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""<p>实例名称</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def AddType(self):
        r"""<p>用来区分自建资产是已通过cvm还是添加ip的方式</p>
        :rtype: int
        """
        return self._AddType

    @AddType.setter
    def AddType(self, AddType):
        self._AddType = AddType

    @property
    def AssetSubnetId(self):
        r"""<p>子网Id</p>
        :rtype: str
        """
        return self._AssetSubnetId

    @AssetSubnetId.setter
    def AssetSubnetId(self, AssetSubnetId):
        self._AssetSubnetId = AssetSubnetId

    @property
    def UploadPem(self):
        r"""<p>是否已上传数据库私钥（0 否，1 是）</p>
        :rtype: int
        """
        return self._UploadPem

    @UploadPem.setter
    def UploadPem(self, UploadPem):
        self._UploadPem = UploadPem

    @property
    def AliveStatus(self):
        r"""<p>资产状态栏 0:正常 1:已删除（目前仅对tencentDB有效）</p>
        :rtype: int
        """
        return self._AliveStatus

    @AliveStatus.setter
    def AliveStatus(self, AliveStatus):
        self._AliveStatus = AliveStatus

    @property
    def AgentOn(self):
        r"""<p>开启agent(0:关闭;1:开启)</p>
        :rtype: int
        """
        return self._AgentOn

    @AgentOn.setter
    def AgentOn(self, AgentOn):
        self._AgentOn = AgentOn

    @property
    def CasbOn(self):
        r"""<p>开启agent(0:关闭;1:开启)</p>
        :rtype: int
        """
        return self._CasbOn

    @CasbOn.setter
    def CasbOn(self, CasbOn):
        self._CasbOn = CasbOn

    @property
    def GroupId(self):
        r"""<p>只读组/集群ID</p>
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Available(self):
        r"""<p>PROXY_OFF: 未开启Casb代理;PROXY_ERROR:Casb代理接口返回异常;PROXY_BOUND:已绑定;PROXY_UNBOUND:未绑定;UNPAID:未购买;UNSUPPORTED:类型不支持;METADATA_NOT_FOUND:元数据不存在;QUOTA_EXCEEDED:Casb额度不足</p>
        :rtype: str
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def CdbOn(self):
        r"""<p>cdbOn</p>
        :rtype: int
        """
        return self._CdbOn

    @CdbOn.setter
    def CdbOn(self, CdbOn):
        self._CdbOn = CdbOn

    @property
    def DbPlatform(self):
        r"""<p>平台位数 32位 64位</p>
        :rtype: str
        """
        return self._DbPlatform

    @DbPlatform.setter
    def DbPlatform(self, DbPlatform):
        self._DbPlatform = DbPlatform

    @property
    def DbCharset(self):
        r"""<p>编码</p>
        :rtype: str
        """
        return self._DbCharset

    @DbCharset.setter
    def DbCharset(self, DbCharset):
        self._DbCharset = DbCharset

    @property
    def OsPolicy(self):
        r"""<p>操作系统</p>
        :rtype: str
        """
        return self._OsPolicy

    @OsPolicy.setter
    def OsPolicy(self, OsPolicy):
        self._OsPolicy = OsPolicy

    @property
    def BidirectionOn(self):
        r"""<p>是否开启双向审计</p>
        :rtype: int
        """
        return self._BidirectionOn

    @BidirectionOn.setter
    def BidirectionOn(self, BidirectionOn):
        self._BidirectionOn = BidirectionOn

    @property
    def BidirectionMaxLine(self):
        r"""<p>最大返回行数</p>
        :rtype: int
        """
        return self._BidirectionMaxLine

    @BidirectionMaxLine.setter
    def BidirectionMaxLine(self, BidirectionMaxLine):
        self._BidirectionMaxLine = BidirectionMaxLine

    @property
    def BidirectionMaxStorage(self):
        r"""<p>最大返回大小</p>
        :rtype: int
        """
        return self._BidirectionMaxStorage

    @BidirectionMaxStorage.setter
    def BidirectionMaxStorage(self, BidirectionMaxStorage):
        self._BidirectionMaxStorage = BidirectionMaxStorage

    @property
    def BidirectionAllow(self):
        r"""<p>是否允许开通双向审计(1.允许；0不允许)</p>
        :rtype: int
        """
        return self._BidirectionAllow

    @BidirectionAllow.setter
    def BidirectionAllow(self, BidirectionAllow):
        self._BidirectionAllow = BidirectionAllow

    @property
    def BidirectionDelivery(self):
        r"""<p>启双向审计的日志投递(1.开启;0.关闭)</p>
        :rtype: int
        """
        return self._BidirectionDelivery

    @BidirectionDelivery.setter
    def BidirectionDelivery(self, BidirectionDelivery):
        self._BidirectionDelivery = BidirectionDelivery

    @property
    def RoStatus(self):
        r"""<p>只读状态</p>
        :rtype: str
        """
        return self._RoStatus

    @RoStatus.setter
    def RoStatus(self, RoStatus):
        self._RoStatus = RoStatus

    @property
    def AgentBound(self):
        r"""<p>当前资产是否开启了对当前Agent的采集策略</p>
        :rtype: bool
        """
        return self._AgentBound

    @AgentBound.setter
    def AgentBound(self, AgentBound):
        self._AgentBound = AgentBound

    @property
    def CdbErrorMsg(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._CdbErrorMsg

    @CdbErrorMsg.setter
    def CdbErrorMsg(self, CdbErrorMsg):
        self._CdbErrorMsg = CdbErrorMsg

    @property
    def DsgcBindingInfo(self):
        r"""<p>资产 DSGC 绑定信息</p>
        :rtype: :class:`tencentcloud.cds.v20180420.models.DsgcBindingInfo`
        """
        return self._DsgcBindingInfo

    @DsgcBindingInfo.setter
    def DsgcBindingInfo(self, DsgcBindingInfo):
        self._DsgcBindingInfo = DsgcBindingInfo

    @property
    def BindingRules(self):
        r"""<p>绑定的规则Ids</p>
        :rtype: list of IdWithName
        """
        return self._BindingRules

    @BindingRules.setter
    def BindingRules(self, BindingRules):
        self._BindingRules = BindingRules

    @property
    def BindingModels(self):
        r"""<p>绑定的模型Ids</p>
        :rtype: list of IdWithName
        """
        return self._BindingModels

    @BindingModels.setter
    def BindingModels(self, BindingModels):
        self._BindingModels = BindingModels

    @property
    def GroupName(self):
        r"""<p>所属组名</p>
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def AssetGroupId(self):
        r"""<p>资产组Id</p>
        :rtype: int
        """
        return self._AssetGroupId

    @AssetGroupId.setter
    def AssetGroupId(self, AssetGroupId):
        self._AssetGroupId = AssetGroupId

    @property
    def IsNewCloudAudit(self):
        r"""<p>是否是新云原生审计流程</p>
        :rtype: bool
        """
        return self._IsNewCloudAudit

    @IsNewCloudAudit.setter
    def IsNewCloudAudit(self, IsNewCloudAudit):
        self._IsNewCloudAudit = IsNewCloudAudit

    @property
    def AuditCapability(self):
        r"""<p>审计功能支持说明</p>
        :rtype: list of AuditCapability
        """
        return self._AuditCapability

    @AuditCapability.setter
    def AuditCapability(self, AuditCapability):
        self._AuditCapability = AuditCapability

    @property
    def TrafficMirrorOn(self):
        r"""<p>1</p><p>取值范围：[0, 1]</p>
        :rtype: int
        """
        return self._TrafficMirrorOn

    @TrafficMirrorOn.setter
    def TrafficMirrorOn(self, TrafficMirrorOn):
        self._TrafficMirrorOn = TrafficMirrorOn

    @property
    def AuditScope(self):
        r"""<p>流量镜像审计范围</p><p>枚举值：</p><ul><li>ALL： 全地域</li><li>REGION： 资产所在地域</li><li>VPC： 资产所在VPC</li></ul><p>默认值：REGION</p>
        :rtype: str
        """
        return self._AuditScope

    @AuditScope.setter
    def AuditScope(self, AuditScope):
        self._AuditScope = AuditScope

    @property
    def InstanceGroupId(self):
        r"""<p>实例集群ID</p>
        :rtype: str
        """
        return self._InstanceGroupId

    @InstanceGroupId.setter
    def InstanceGroupId(self, InstanceGroupId):
        self._InstanceGroupId = InstanceGroupId


    def _deserialize(self, params):
        self._AddTime = params.get("AddTime")
        self._Aid = params.get("Aid")
        self._AssetsIp = params.get("AssetsIp")
        self._AssetsName = params.get("AssetsName")
        self._AssetsPort = params.get("AssetsPort")
        self._AssetsType = params.get("AssetsType")
        self._AssetsVersion = params.get("AssetsVersion")
        self._AssetsAddType = params.get("AssetsAddType")
        self._Status = params.get("Status")
        self._UpdateTime = params.get("UpdateTime")
        self._VpcId = params.get("VpcId")
        self._RegionId = params.get("RegionId")
        self._Permission = params.get("Permission")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._AddType = params.get("AddType")
        self._AssetSubnetId = params.get("AssetSubnetId")
        self._UploadPem = params.get("UploadPem")
        self._AliveStatus = params.get("AliveStatus")
        self._AgentOn = params.get("AgentOn")
        self._CasbOn = params.get("CasbOn")
        self._GroupId = params.get("GroupId")
        self._Available = params.get("Available")
        self._CdbOn = params.get("CdbOn")
        self._DbPlatform = params.get("DbPlatform")
        self._DbCharset = params.get("DbCharset")
        self._OsPolicy = params.get("OsPolicy")
        self._BidirectionOn = params.get("BidirectionOn")
        self._BidirectionMaxLine = params.get("BidirectionMaxLine")
        self._BidirectionMaxStorage = params.get("BidirectionMaxStorage")
        self._BidirectionAllow = params.get("BidirectionAllow")
        self._BidirectionDelivery = params.get("BidirectionDelivery")
        self._RoStatus = params.get("RoStatus")
        self._AgentBound = params.get("AgentBound")
        self._CdbErrorMsg = params.get("CdbErrorMsg")
        if params.get("DsgcBindingInfo") is not None:
            self._DsgcBindingInfo = DsgcBindingInfo()
            self._DsgcBindingInfo._deserialize(params.get("DsgcBindingInfo"))
        if params.get("BindingRules") is not None:
            self._BindingRules = []
            for item in params.get("BindingRules"):
                obj = IdWithName()
                obj._deserialize(item)
                self._BindingRules.append(obj)
        if params.get("BindingModels") is not None:
            self._BindingModels = []
            for item in params.get("BindingModels"):
                obj = IdWithName()
                obj._deserialize(item)
                self._BindingModels.append(obj)
        self._GroupName = params.get("GroupName")
        self._AssetGroupId = params.get("AssetGroupId")
        self._IsNewCloudAudit = params.get("IsNewCloudAudit")
        if params.get("AuditCapability") is not None:
            self._AuditCapability = []
            for item in params.get("AuditCapability"):
                obj = AuditCapability()
                obj._deserialize(item)
                self._AuditCapability.append(obj)
        self._TrafficMirrorOn = params.get("TrafficMirrorOn")
        self._AuditScope = params.get("AuditScope")
        self._InstanceGroupId = params.get("InstanceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditCapability(AbstractModel):
    r"""资产支持的审计能力

    """


class CdsAuditInstance(AbstractModel):
    r"""数据安全产品实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AppId: 用户AppId
        :type AppId: str
        :param _Uin: 用户Uin
        :type Uin: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _RenewFlag: 续费标识
        :type RenewFlag: int
        :param _Region: 所属地域
        :type Region: str
        :param _PayMode: 付费模式（数据安全审计只支持预付费：1）
        :type PayMode: int
        :param _Status: 实例状态： 0，未生效；1：正常运行； 2：被隔离； 3，已过期
        :type Status: int
        :param _IsolatedTimestamp: 实例被隔离时间，格式：yyyy-mm-dd HH:ii:ss
        :type IsolatedTimestamp: str
        :param _CreateTime: 实例创建时间，格式： yyyy-mm-dd HH:ii:ss
        :type CreateTime: str
        :param _ExpireTime: 实例过期时间，格式：yyyy-mm-dd HH:ii:ss
        :type ExpireTime: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _PublicIp: 实例公网IP
        :type PublicIp: str
        :param _PrivateIp: 实例私网IP
        :type PrivateIp: str
        :param _InstanceType: 实例类型（版本）
        :type InstanceType: str
        :param _Pdomain: 实例域名
        :type Pdomain: str
        """
        self._InstanceId = None
        self._AppId = None
        self._Uin = None
        self._ProjectId = None
        self._RenewFlag = None
        self._Region = None
        self._PayMode = None
        self._Status = None
        self._IsolatedTimestamp = None
        self._CreateTime = None
        self._ExpireTime = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._InstanceType = None
        self._Pdomain = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AppId(self):
        r"""用户AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""用户Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RenewFlag(self):
        r"""续费标识
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Region(self):
        r"""所属地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PayMode(self):
        r"""付费模式（数据安全审计只支持预付费：1）
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Status(self):
        r"""实例状态： 0，未生效；1：正常运行； 2：被隔离； 3，已过期
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsolatedTimestamp(self):
        r"""实例被隔离时间，格式：yyyy-mm-dd HH:ii:ss
        :rtype: str
        """
        return self._IsolatedTimestamp

    @IsolatedTimestamp.setter
    def IsolatedTimestamp(self, IsolatedTimestamp):
        self._IsolatedTimestamp = IsolatedTimestamp

    @property
    def CreateTime(self):
        r"""实例创建时间，格式： yyyy-mm-dd HH:ii:ss
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""实例过期时间，格式：yyyy-mm-dd HH:ii:ss
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        r"""实例公网IP
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""实例私网IP
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def InstanceType(self):
        r"""实例类型（版本）
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Pdomain(self):
        r"""实例域名
        :rtype: str
        """
        return self._Pdomain

    @Pdomain.setter
    def Pdomain(self, Pdomain):
        self._Pdomain = Pdomain


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._ProjectId = params.get("ProjectId")
        self._RenewFlag = params.get("RenewFlag")
        self._Region = params.get("Region")
        self._PayMode = params.get("PayMode")
        self._Status = params.get("Status")
        self._IsolatedTimestamp = params.get("IsolatedTimestamp")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._InstanceType = params.get("InstanceType")
        self._Pdomain = params.get("Pdomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReportPdfRequest(AbstractModel):
    r"""CreateReportPdf请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 报表 Id
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        r"""报表 Id
        :rtype: int
        """
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
        


class CreateReportPdfResponse(AbstractModel):
    r"""CreateReportPdf返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 下载地址
        :type Url: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        r"""下载地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

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
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class CreateTimerReportRequest(AbstractModel):
    r"""CreateTimerReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TplName: 任务名称 不变更为""
        :type TplName: str
        :param _CntTime: 执行日期 重复周期为天：无意义周：星期几1-7月每月几号 1-31
        :type CntTime: int
        :param _CntCycle: 重复周期
        :type CntCycle: int
        :param _Receivers: 发送目标
        :type Receivers: str
        :param _CntDay: 时间范围 1:24小时 7:近一周 30:近30天 90:近90天 180:近180天 不变更为0
        :type CntDay: int
        :param _CntDate: 执行时间 格式15:04 到分钟
        :type CntDate: str
        :param _Remark: 报告说明
        :type Remark: str
        :param _TemplateId: 模版Id
        :type TemplateId: int
        :param _ReportType: 报表类型
        :type ReportType: int
        :param _AssetsId: 关联的资产数组
        :type AssetsId: list of int
        :param _Notification: 报表通知 1关闭 2开启 不变更为0
        :type Notification: int
        :param _MissionStart: 任务起停 1:关闭 2:开启 单次报表默认为2
        :type MissionStart: int
        """
        self._TplName = None
        self._CntTime = None
        self._CntCycle = None
        self._Receivers = None
        self._CntDay = None
        self._CntDate = None
        self._Remark = None
        self._TemplateId = None
        self._ReportType = None
        self._AssetsId = None
        self._Notification = None
        self._MissionStart = None

    @property
    def TplName(self):
        r"""任务名称 不变更为""
        :rtype: str
        """
        return self._TplName

    @TplName.setter
    def TplName(self, TplName):
        self._TplName = TplName

    @property
    def CntTime(self):
        r"""执行日期 重复周期为天：无意义周：星期几1-7月每月几号 1-31
        :rtype: int
        """
        return self._CntTime

    @CntTime.setter
    def CntTime(self, CntTime):
        self._CntTime = CntTime

    @property
    def CntCycle(self):
        r"""重复周期
        :rtype: int
        """
        return self._CntCycle

    @CntCycle.setter
    def CntCycle(self, CntCycle):
        self._CntCycle = CntCycle

    @property
    def Receivers(self):
        r"""发送目标
        :rtype: str
        """
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def CntDay(self):
        r"""时间范围 1:24小时 7:近一周 30:近30天 90:近90天 180:近180天 不变更为0
        :rtype: int
        """
        return self._CntDay

    @CntDay.setter
    def CntDay(self, CntDay):
        self._CntDay = CntDay

    @property
    def CntDate(self):
        r"""执行时间 格式15:04 到分钟
        :rtype: str
        """
        return self._CntDate

    @CntDate.setter
    def CntDate(self, CntDate):
        self._CntDate = CntDate

    @property
    def Remark(self):
        r"""报告说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TemplateId(self):
        r"""模版Id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ReportType(self):
        r"""报表类型
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def AssetsId(self):
        r"""关联的资产数组
        :rtype: list of int
        """
        return self._AssetsId

    @AssetsId.setter
    def AssetsId(self, AssetsId):
        self._AssetsId = AssetsId

    @property
    def Notification(self):
        r"""报表通知 1关闭 2开启 不变更为0
        :rtype: int
        """
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification

    @property
    def MissionStart(self):
        r"""任务起停 1:关闭 2:开启 单次报表默认为2
        :rtype: int
        """
        return self._MissionStart

    @MissionStart.setter
    def MissionStart(self, MissionStart):
        self._MissionStart = MissionStart


    def _deserialize(self, params):
        self._TplName = params.get("TplName")
        self._CntTime = params.get("CntTime")
        self._CntCycle = params.get("CntCycle")
        self._Receivers = params.get("Receivers")
        self._CntDay = params.get("CntDay")
        self._CntDate = params.get("CntDate")
        self._Remark = params.get("Remark")
        self._TemplateId = params.get("TemplateId")
        self._ReportType = params.get("ReportType")
        self._AssetsId = params.get("AssetsId")
        self._Notification = params.get("Notification")
        self._MissionStart = params.get("MissionStart")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTimerReportResponse(AbstractModel):
    r"""CreateTimerReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DbauditTypesInfo(AbstractModel):
    r"""数据安全审计产品规格信息

    """

    def __init__(self):
        r"""
        :param _InstanceVersionName: 规格描述
        :type InstanceVersionName: str
        :param _InstanceVersionKey: 规格名称
        :type InstanceVersionKey: str
        :param _Qps: 最大吞吐量
        :type Qps: int
        :param _MaxInstances: 最大实例数
        :type MaxInstances: int
        :param _InsertSpeed: 入库速率（每小时）
        :type InsertSpeed: int
        :param _OnlineStorageCapacity: 最大在线存储量，单位：条
        :type OnlineStorageCapacity: int
        :param _ArchivingStorageCapacity: 最大归档存储量，单位：条
        :type ArchivingStorageCapacity: int
        """
        self._InstanceVersionName = None
        self._InstanceVersionKey = None
        self._Qps = None
        self._MaxInstances = None
        self._InsertSpeed = None
        self._OnlineStorageCapacity = None
        self._ArchivingStorageCapacity = None

    @property
    def InstanceVersionName(self):
        r"""规格描述
        :rtype: str
        """
        return self._InstanceVersionName

    @InstanceVersionName.setter
    def InstanceVersionName(self, InstanceVersionName):
        self._InstanceVersionName = InstanceVersionName

    @property
    def InstanceVersionKey(self):
        r"""规格名称
        :rtype: str
        """
        return self._InstanceVersionKey

    @InstanceVersionKey.setter
    def InstanceVersionKey(self, InstanceVersionKey):
        self._InstanceVersionKey = InstanceVersionKey

    @property
    def Qps(self):
        r"""最大吞吐量
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def MaxInstances(self):
        r"""最大实例数
        :rtype: int
        """
        return self._MaxInstances

    @MaxInstances.setter
    def MaxInstances(self, MaxInstances):
        self._MaxInstances = MaxInstances

    @property
    def InsertSpeed(self):
        r"""入库速率（每小时）
        :rtype: int
        """
        return self._InsertSpeed

    @InsertSpeed.setter
    def InsertSpeed(self, InsertSpeed):
        self._InsertSpeed = InsertSpeed

    @property
    def OnlineStorageCapacity(self):
        r"""最大在线存储量，单位：条
        :rtype: int
        """
        return self._OnlineStorageCapacity

    @OnlineStorageCapacity.setter
    def OnlineStorageCapacity(self, OnlineStorageCapacity):
        self._OnlineStorageCapacity = OnlineStorageCapacity

    @property
    def ArchivingStorageCapacity(self):
        r"""最大归档存储量，单位：条
        :rtype: int
        """
        return self._ArchivingStorageCapacity

    @ArchivingStorageCapacity.setter
    def ArchivingStorageCapacity(self, ArchivingStorageCapacity):
        self._ArchivingStorageCapacity = ArchivingStorageCapacity


    def _deserialize(self, params):
        self._InstanceVersionName = params.get("InstanceVersionName")
        self._InstanceVersionKey = params.get("InstanceVersionKey")
        self._Qps = params.get("Qps")
        self._MaxInstances = params.get("MaxInstances")
        self._InsertSpeed = params.get("InsertSpeed")
        self._OnlineStorageCapacity = params.get("OnlineStorageCapacity")
        self._ArchivingStorageCapacity = params.get("ArchivingStorageCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetsListRequest(AbstractModel):
    r"""DescribeAssetsList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: <p>限制数目</p>
        :type Limit: int
        :param _Offset: <p>偏移量</p>
        :type Offset: int
        :param _SearchValues: <p>实例Id/实例名称/资产名称</p>
        :type SearchValues: list of NameValueString
        :param _AssetsType: <p>数据资产类型</p>
        :type AssetsType: str
        :param _AssetsAddType: <p>查询的资产类型（1:cdb、2:cvm、3:others）</p>
        :type AssetsAddType: int
        :param _RegionId: <p>地域</p>
        :type RegionId: str
        :param _Permission: <p>审计权限</p>
        :type Permission: int
        :param _AliveStatus: <p>状态</p>
        :type AliveStatus: int
        :param _CasbOn: <p>1.代理开启 0.代理关闭 -1.全查</p>
        :type CasbOn: int
        :param _AgentOn: <p>1.Agent开启 0.Agent关闭 -1.全查</p>
        :type AgentOn: int
        :param _CdbOn: <p>0.关闭，1.开启，2.关闭中，3.开启中 -1.全查</p>
        :type CdbOn: int
        :param _ExtendCategory: <p>扩展分类，如sensitive，指定查询支持敏感数据识别的资产</p>
        :type ExtendCategory: str
        :param _GroupIds: <p>资产组Id（Id=0 暂未分组；id&gt;0 组Id）</p>
        :type GroupIds: list of int non-negative
        :param _Aids: <p>资产Id</p>
        :type Aids: list of int non-negative
        :param _BindingState: <p>查询绑定状态（1:查询规则绑定数量；2:查询模型绑定数量）</p>
        :type BindingState: int
        :param _TrafficMirrorOn: <p>网卡是否开启流量审计</p><p>取值范围：[-1, 1]</p>
        :type TrafficMirrorOn: int
        """
        self._Limit = None
        self._Offset = None
        self._SearchValues = None
        self._AssetsType = None
        self._AssetsAddType = None
        self._RegionId = None
        self._Permission = None
        self._AliveStatus = None
        self._CasbOn = None
        self._AgentOn = None
        self._CdbOn = None
        self._ExtendCategory = None
        self._GroupIds = None
        self._Aids = None
        self._BindingState = None
        self._TrafficMirrorOn = None

    @property
    def Limit(self):
        r"""<p>限制数目</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SearchValues(self):
        r"""<p>实例Id/实例名称/资产名称</p>
        :rtype: list of NameValueString
        """
        return self._SearchValues

    @SearchValues.setter
    def SearchValues(self, SearchValues):
        self._SearchValues = SearchValues

    @property
    def AssetsType(self):
        r"""<p>数据资产类型</p>
        :rtype: str
        """
        return self._AssetsType

    @AssetsType.setter
    def AssetsType(self, AssetsType):
        self._AssetsType = AssetsType

    @property
    def AssetsAddType(self):
        r"""<p>查询的资产类型（1:cdb、2:cvm、3:others）</p>
        :rtype: int
        """
        return self._AssetsAddType

    @AssetsAddType.setter
    def AssetsAddType(self, AssetsAddType):
        self._AssetsAddType = AssetsAddType

    @property
    def RegionId(self):
        r"""<p>地域</p>
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Permission(self):
        r"""<p>审计权限</p>
        :rtype: int
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def AliveStatus(self):
        r"""<p>状态</p>
        :rtype: int
        """
        return self._AliveStatus

    @AliveStatus.setter
    def AliveStatus(self, AliveStatus):
        self._AliveStatus = AliveStatus

    @property
    def CasbOn(self):
        r"""<p>1.代理开启 0.代理关闭 -1.全查</p>
        :rtype: int
        """
        return self._CasbOn

    @CasbOn.setter
    def CasbOn(self, CasbOn):
        self._CasbOn = CasbOn

    @property
    def AgentOn(self):
        r"""<p>1.Agent开启 0.Agent关闭 -1.全查</p>
        :rtype: int
        """
        return self._AgentOn

    @AgentOn.setter
    def AgentOn(self, AgentOn):
        self._AgentOn = AgentOn

    @property
    def CdbOn(self):
        r"""<p>0.关闭，1.开启，2.关闭中，3.开启中 -1.全查</p>
        :rtype: int
        """
        return self._CdbOn

    @CdbOn.setter
    def CdbOn(self, CdbOn):
        self._CdbOn = CdbOn

    @property
    def ExtendCategory(self):
        r"""<p>扩展分类，如sensitive，指定查询支持敏感数据识别的资产</p>
        :rtype: str
        """
        return self._ExtendCategory

    @ExtendCategory.setter
    def ExtendCategory(self, ExtendCategory):
        self._ExtendCategory = ExtendCategory

    @property
    def GroupIds(self):
        r"""<p>资产组Id（Id=0 暂未分组；id&gt;0 组Id）</p>
        :rtype: list of int non-negative
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def Aids(self):
        r"""<p>资产Id</p>
        :rtype: list of int non-negative
        """
        return self._Aids

    @Aids.setter
    def Aids(self, Aids):
        self._Aids = Aids

    @property
    def BindingState(self):
        r"""<p>查询绑定状态（1:查询规则绑定数量；2:查询模型绑定数量）</p>
        :rtype: int
        """
        return self._BindingState

    @BindingState.setter
    def BindingState(self, BindingState):
        self._BindingState = BindingState

    @property
    def TrafficMirrorOn(self):
        r"""<p>网卡是否开启流量审计</p><p>取值范围：[-1, 1]</p>
        :rtype: int
        """
        return self._TrafficMirrorOn

    @TrafficMirrorOn.setter
    def TrafficMirrorOn(self, TrafficMirrorOn):
        self._TrafficMirrorOn = TrafficMirrorOn


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("SearchValues") is not None:
            self._SearchValues = []
            for item in params.get("SearchValues"):
                obj = NameValueString()
                obj._deserialize(item)
                self._SearchValues.append(obj)
        self._AssetsType = params.get("AssetsType")
        self._AssetsAddType = params.get("AssetsAddType")
        self._RegionId = params.get("RegionId")
        self._Permission = params.get("Permission")
        self._AliveStatus = params.get("AliveStatus")
        self._CasbOn = params.get("CasbOn")
        self._AgentOn = params.get("AgentOn")
        self._CdbOn = params.get("CdbOn")
        self._ExtendCategory = params.get("ExtendCategory")
        self._GroupIds = params.get("GroupIds")
        self._Aids = params.get("Aids")
        self._BindingState = params.get("BindingState")
        self._TrafficMirrorOn = params.get("TrafficMirrorOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetsListResponse(AbstractModel):
    r"""DescribeAssetsList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数目</p>
        :type TotalCount: int
        :param _List: <p>数据列表</p>
        :type List: list of AssetsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数目</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""<p>数据列表</p>
        :rtype: list of AssetsInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AssetsInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbauditInstanceTypeRequest(AbstractModel):
    r"""DescribeDbauditInstanceType请求参数结构体

    """


class DescribeDbauditInstanceTypeResponse(AbstractModel):
    r"""DescribeDbauditInstanceType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DbauditTypesSet: 数据安全审计产品规格信息列表
        :type DbauditTypesSet: list of DbauditTypesInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DbauditTypesSet = None
        self._RequestId = None

    @property
    def DbauditTypesSet(self):
        r"""数据安全审计产品规格信息列表
        :rtype: list of DbauditTypesInfo
        """
        return self._DbauditTypesSet

    @DbauditTypesSet.setter
    def DbauditTypesSet(self, DbauditTypesSet):
        self._DbauditTypesSet = DbauditTypesSet

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
        if params.get("DbauditTypesSet") is not None:
            self._DbauditTypesSet = []
            for item in params.get("DbauditTypesSet"):
                obj = DbauditTypesInfo()
                obj._deserialize(item)
                self._DbauditTypesSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbauditInstancesRequest(AbstractModel):
    r"""DescribeDbauditInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SearchRegion: 查询条件地域
        :type SearchRegion: str
        :param _Limit: 限制数目，默认10， 最大50
        :type Limit: int
        :param _Offset: 偏移量，默认1
        :type Offset: int
        """
        self._SearchRegion = None
        self._Limit = None
        self._Offset = None

    @property
    def SearchRegion(self):
        r"""查询条件地域
        :rtype: str
        """
        return self._SearchRegion

    @SearchRegion.setter
    def SearchRegion(self, SearchRegion):
        self._SearchRegion = SearchRegion

    @property
    def Limit(self):
        r"""限制数目，默认10， 最大50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认1
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._SearchRegion = params.get("SearchRegion")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDbauditInstancesResponse(AbstractModel):
    r"""DescribeDbauditInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总实例数
        :type TotalCount: int
        :param _CdsAuditInstanceSet: 数据安全审计实例信息列表
        :type CdsAuditInstanceSet: list of CdsAuditInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CdsAuditInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总实例数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CdsAuditInstanceSet(self):
        r"""数据安全审计实例信息列表
        :rtype: list of CdsAuditInstance
        """
        return self._CdsAuditInstanceSet

    @CdsAuditInstanceSet.setter
    def CdsAuditInstanceSet(self, CdsAuditInstanceSet):
        self._CdsAuditInstanceSet = CdsAuditInstanceSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("CdsAuditInstanceSet") is not None:
            self._CdsAuditInstanceSet = []
            for item in params.get("CdsAuditInstanceSet"):
                obj = CdsAuditInstance()
                obj._deserialize(item)
                self._CdsAuditInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDbauditUsedRegionsRequest(AbstractModel):
    r"""DescribeDbauditUsedRegions请求参数结构体

    """


class DescribeDbauditUsedRegionsResponse(AbstractModel):
    r"""DescribeDbauditUsedRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 可售卖地域信息列表
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        r"""可售卖地域信息列表
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

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
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReportListRequest(AbstractModel):
    r"""DescribeReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 限制数目
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Name: 报告名称
        :type Name: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ReportType: 报告类型
        :type ReportType: int
        :param _ReportStatus: 报告状态
        :type ReportStatus: int
        :param _TemplateId: 报表模版id
        :type TemplateId: int
        :param _Field: 需要排序的字段
        :type Field: str
        :param _Sort: 排序顺序 asc desc
        :type Sort: str
        :param _CntDay: 时间范围 1:24小时 7:近一周 30:近30天 90:近90天 180:近180天 不变更为0
        :type CntDay: int
        """
        self._Limit = None
        self._Offset = None
        self._Name = None
        self._StartTime = None
        self._EndTime = None
        self._ReportType = None
        self._ReportStatus = None
        self._TemplateId = None
        self._Field = None
        self._Sort = None
        self._CntDay = None

    @property
    def Limit(self):
        r"""限制数目
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Name(self):
        r"""报告名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ReportType(self):
        r"""报告类型
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def ReportStatus(self):
        r"""报告状态
        :rtype: int
        """
        return self._ReportStatus

    @ReportStatus.setter
    def ReportStatus(self, ReportStatus):
        self._ReportStatus = ReportStatus

    @property
    def TemplateId(self):
        r"""报表模版id
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Field(self):
        r"""需要排序的字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Sort(self):
        r"""排序顺序 asc desc
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def CntDay(self):
        r"""时间范围 1:24小时 7:近一周 30:近30天 90:近90天 180:近180天 不变更为0
        :rtype: int
        """
        return self._CntDay

    @CntDay.setter
    def CntDay(self, CntDay):
        self._CntDay = CntDay


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReportType = params.get("ReportType")
        self._ReportStatus = params.get("ReportStatus")
        self._TemplateId = params.get("TemplateId")
        self._Field = params.get("Field")
        self._Sort = params.get("Sort")
        self._CntDay = params.get("CntDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportListResponse(AbstractModel):
    r"""DescribeReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数目
        :type TotalCount: int
        :param _List: 数据列表
        :type List: list of Reports
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""数据列表
        :rtype: list of Reports
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Reports()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReportMissionListRequest(AbstractModel):
    r"""DescribeReportMissionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TplName: 报表名 可模糊查询
        :type TplName: str
        :param _ReportType: 报表类型 1:单次报表 2:周期报表 0全查
        :type ReportType: int
        :param _TemplateId: 报表模板 1:综合分析报告 2:等保合规报告 0全查
        :type TemplateId: int
        :param _MissionStatus: 任务状态0全查 1:生成中 2:待生成 3:已生成 4:生成失败 5:已暂停
        :type MissionStatus: int
        :param _Field: 排序字段 支持“NextStartTime” 与 “MissionStatus”
        :type Field: str
        :param _Sort: ‘desc' | 'asc'
        :type Sort: str
        :param _Limit: 限制条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._TplName = None
        self._ReportType = None
        self._TemplateId = None
        self._MissionStatus = None
        self._Field = None
        self._Sort = None
        self._Limit = None
        self._Offset = None

    @property
    def TplName(self):
        r"""报表名 可模糊查询
        :rtype: str
        """
        return self._TplName

    @TplName.setter
    def TplName(self, TplName):
        self._TplName = TplName

    @property
    def ReportType(self):
        r"""报表类型 1:单次报表 2:周期报表 0全查
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def TemplateId(self):
        r"""报表模板 1:综合分析报告 2:等保合规报告 0全查
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def MissionStatus(self):
        r"""任务状态0全查 1:生成中 2:待生成 3:已生成 4:生成失败 5:已暂停
        :rtype: int
        """
        return self._MissionStatus

    @MissionStatus.setter
    def MissionStatus(self, MissionStatus):
        self._MissionStatus = MissionStatus

    @property
    def Field(self):
        r"""排序字段 支持“NextStartTime” 与 “MissionStatus”
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Sort(self):
        r"""‘desc' | 'asc'
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Limit(self):
        r"""限制条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._TplName = params.get("TplName")
        self._ReportType = params.get("ReportType")
        self._TemplateId = params.get("TemplateId")
        self._MissionStatus = params.get("MissionStatus")
        self._Field = params.get("Field")
        self._Sort = params.get("Sort")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportMissionListResponse(AbstractModel):
    r"""DescribeReportMissionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _List: 报表列表
        :type List: list of ReportMission
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""报表列表
        :rtype: list of ReportMission
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReportMission()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DsgcBindingInfo(AbstractModel):
    r"""资产 DSGC 绑定信息

    """

    def __init__(self):
        r"""
        :param _DspaId: dspa实例id
        :type DspaId: str
        :param _DspaCgId: dspa绑定模板/合规组 id ComplianceGroupId
        :type DspaCgId: int
        :param _DspaCgName: dspa绑定模板/合规组名称
        :type DspaCgName: str
        :param _DspaStatus: dspa实例状态 0 正常 1 隔离 2 销毁
        :type DspaStatus: int
        :param _DspaCgStatus: 模板状态 0: 正常   1: 已删除
        :type DspaCgStatus: int
        """
        self._DspaId = None
        self._DspaCgId = None
        self._DspaCgName = None
        self._DspaStatus = None
        self._DspaCgStatus = None

    @property
    def DspaId(self):
        r"""dspa实例id
        :rtype: str
        """
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def DspaCgId(self):
        r"""dspa绑定模板/合规组 id ComplianceGroupId
        :rtype: int
        """
        return self._DspaCgId

    @DspaCgId.setter
    def DspaCgId(self, DspaCgId):
        self._DspaCgId = DspaCgId

    @property
    def DspaCgName(self):
        r"""dspa绑定模板/合规组名称
        :rtype: str
        """
        return self._DspaCgName

    @DspaCgName.setter
    def DspaCgName(self, DspaCgName):
        self._DspaCgName = DspaCgName

    @property
    def DspaStatus(self):
        r"""dspa实例状态 0 正常 1 隔离 2 销毁
        :rtype: int
        """
        return self._DspaStatus

    @DspaStatus.setter
    def DspaStatus(self, DspaStatus):
        self._DspaStatus = DspaStatus

    @property
    def DspaCgStatus(self):
        r"""模板状态 0: 正常   1: 已删除
        :rtype: int
        """
        return self._DspaCgStatus

    @DspaCgStatus.setter
    def DspaCgStatus(self, DspaCgStatus):
        self._DspaCgStatus = DspaCgStatus


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._DspaCgId = params.get("DspaCgId")
        self._DspaCgName = params.get("DspaCgName")
        self._DspaStatus = params.get("DspaStatus")
        self._DspaCgStatus = params.get("DspaCgStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdWithName(AbstractModel):
    r"""IdWithName

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: int
        :param _Name: 名称
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        r"""id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceDbauditInstanceRequest(AbstractModel):
    r"""InquiryPriceDbauditInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceVersion: 实例规格，取值范围： cdsaudit，cdsaudit_adv， cdsaudit_ent 分别为合规版，高级版，企业版
        :type InstanceVersion: str
        :param _InquiryType: 询价类型： renew，续费；newbuy，新购
        :type InquiryType: str
        :param _TimeSpan: 购买实例的时长。取值范围：1（y/m），2（y/m）,，3（y/m），4（m）， 5（m），6（m）， 7（m），8（m），9（m）， 10（m）
        :type TimeSpan: int
        :param _TimeUnit: 购买时长单位，y：年；m：月
        :type TimeUnit: str
        :param _ServiceRegion: 实例所在地域
        :type ServiceRegion: str
        """
        self._InstanceVersion = None
        self._InquiryType = None
        self._TimeSpan = None
        self._TimeUnit = None
        self._ServiceRegion = None

    @property
    def InstanceVersion(self):
        r"""实例规格，取值范围： cdsaudit，cdsaudit_adv， cdsaudit_ent 分别为合规版，高级版，企业版
        :rtype: str
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def InquiryType(self):
        r"""询价类型： renew，续费；newbuy，新购
        :rtype: str
        """
        return self._InquiryType

    @InquiryType.setter
    def InquiryType(self, InquiryType):
        self._InquiryType = InquiryType

    @property
    def TimeSpan(self):
        r"""购买实例的时长。取值范围：1（y/m），2（y/m）,，3（y/m），4（m）， 5（m），6（m）， 7（m），8（m），9（m）， 10（m）
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def TimeUnit(self):
        r"""购买时长单位，y：年；m：月
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def ServiceRegion(self):
        r"""实例所在地域
        :rtype: str
        """
        return self._ServiceRegion

    @ServiceRegion.setter
    def ServiceRegion(self, ServiceRegion):
        self._ServiceRegion = ServiceRegion


    def _deserialize(self, params):
        self._InstanceVersion = params.get("InstanceVersion")
        self._InquiryType = params.get("InquiryType")
        self._TimeSpan = params.get("TimeSpan")
        self._TimeUnit = params.get("TimeUnit")
        self._ServiceRegion = params.get("ServiceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceDbauditInstanceResponse(AbstractModel):
    r"""InquiryPriceDbauditInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalPrice: 总价，单位：元
        :type TotalPrice: float
        :param _RealTotalCost: 真实价钱，预支费用的折扣价，单位：元
        :type RealTotalCost: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalPrice = None
        self._RealTotalCost = None
        self._RequestId = None

    @property
    def TotalPrice(self):
        r"""总价，单位：元
        :rtype: float
        """
        return self._TotalPrice

    @TotalPrice.setter
    def TotalPrice(self, TotalPrice):
        self._TotalPrice = TotalPrice

    @property
    def RealTotalCost(self):
        r"""真实价钱，预支费用的折扣价，单位：元
        :rtype: float
        """
        return self._RealTotalCost

    @RealTotalCost.setter
    def RealTotalCost(self, RealTotalCost):
        self._RealTotalCost = RealTotalCost

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
        self._TotalPrice = params.get("TotalPrice")
        self._RealTotalCost = params.get("RealTotalCost")
        self._RequestId = params.get("RequestId")


class ModifyDbauditInstancesRenewFlagRequest(AbstractModel):
    r"""ModifyDbauditInstancesRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _AutoRenewFlag: 0，表示默认状态(用户未设置，即初始状态)；1，表示自动续费；2，表示明确不自动续费
        :type AutoRenewFlag: int
        """
        self._InstanceId = None
        self._AutoRenewFlag = None

    @property
    def InstanceId(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoRenewFlag(self):
        r"""0，表示默认状态(用户未设置，即初始状态)；1，表示自动续费；2，表示明确不自动续费
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDbauditInstancesRenewFlagResponse(AbstractModel):
    r"""ModifyDbauditInstancesRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class NameValueString(AbstractModel):
    r"""Name and String Value

    """

    def __init__(self):
        r"""
        :param _Name: <p>名称</p>
        :type Name: str
        :param _Value: <p>值</p>
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""<p>名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""<p>值</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    r"""数盾地域信息

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: int
        :param _Region: 地域名称
        :type Region: str
        :param _RegionName: 地域描述
        :type RegionName: str
        :param _RegionState: 地域可用状态
        :type RegionState: int
        """
        self._RegionId = None
        self._Region = None
        self._RegionName = None
        self._RegionState = None

    @property
    def RegionId(self):
        r"""地域ID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Region(self):
        r"""地域名称
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""地域描述
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        r"""地域可用状态
        :rtype: int
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportMission(AbstractModel):
    r"""任务对象

    """

    def __init__(self):
        r"""
        :param _Id: 报表任务id
        :type Id: int
        :param _TplName: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TplName: str
        :param _ReportType: 报表类型 1:单次报表 2:周期报表
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportType: int
        :param _Remark: 报告说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _TemplateId: 报表模板 1:综合分析报告 2:等保合规报告
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: int
        :param _AssetsList: 包含资产
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetsList: list of AssetsInfo
        :param _NextStartTime: 下次启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type NextStartTime: int
        :param _MissionStatus: 任务状态 1:生成中 2:待生成3:已生成4:生成失败5:已暂停
注意：此字段可能返回 null，表示取不到有效值。
        :type MissionStatus: int
        :param _MissionStatusMessage: 任务状态说明 仅生成中和生成失败有效
注意：此字段可能返回 null，表示取不到有效值。
        :type MissionStatusMessage: str
        :param _ReportCount: 已生成报表数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportCount: int
        :param _MissionStart: 任务起停 1:关闭 2:开启 仅周期报表有效
注意：此字段可能返回 null，表示取不到有效值。
        :type MissionStart: int
        :param _CntDay: 统计周期 1:24小时 7:近一周 30:近30天 90:近90天 180:
注意：此字段可能返回 null，表示取不到有效值。
        :type CntDay: int
        :param _CntCycle: 重复周期 1:每天 2:每周 3:每月
注意：此字段可能返回 null，表示取不到有效值。
        :type CntCycle: int
        :param _CntTime: 执行日期 重复周期为天：无意义 周：星期几 1-7  月每月
注意：此字段可能返回 null，表示取不到有效值。
        :type CntTime: int
        :param _CntDate: 执行时间 格式15:04 到分钟
注意：此字段可能返回 null，表示取不到有效值。
        :type CntDate: str
        :param _Receivers: 创建者 0:内置 其余存放用户(uin)
注意：此字段可能返回 null，表示取不到有效值。
        :type Receivers: str
        :param _Notification: Notification  int  1关闭 2开启 不变更为0
注意：此字段可能返回 null，表示取不到有效值。
        :type Notification: int
        """
        self._Id = None
        self._TplName = None
        self._ReportType = None
        self._Remark = None
        self._TemplateId = None
        self._AssetsList = None
        self._NextStartTime = None
        self._MissionStatus = None
        self._MissionStatusMessage = None
        self._ReportCount = None
        self._MissionStart = None
        self._CntDay = None
        self._CntCycle = None
        self._CntTime = None
        self._CntDate = None
        self._Receivers = None
        self._Notification = None

    @property
    def Id(self):
        r"""报表任务id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TplName(self):
        r"""任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TplName

    @TplName.setter
    def TplName(self, TplName):
        self._TplName = TplName

    @property
    def ReportType(self):
        r"""报表类型 1:单次报表 2:周期报表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def Remark(self):
        r"""报告说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TemplateId(self):
        r"""报表模板 1:综合分析报告 2:等保合规报告
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AssetsList(self):
        r"""包含资产
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AssetsInfo
        """
        return self._AssetsList

    @AssetsList.setter
    def AssetsList(self, AssetsList):
        self._AssetsList = AssetsList

    @property
    def NextStartTime(self):
        r"""下次启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NextStartTime

    @NextStartTime.setter
    def NextStartTime(self, NextStartTime):
        self._NextStartTime = NextStartTime

    @property
    def MissionStatus(self):
        r"""任务状态 1:生成中 2:待生成3:已生成4:生成失败5:已暂停
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MissionStatus

    @MissionStatus.setter
    def MissionStatus(self, MissionStatus):
        self._MissionStatus = MissionStatus

    @property
    def MissionStatusMessage(self):
        r"""任务状态说明 仅生成中和生成失败有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MissionStatusMessage

    @MissionStatusMessage.setter
    def MissionStatusMessage(self, MissionStatusMessage):
        self._MissionStatusMessage = MissionStatusMessage

    @property
    def ReportCount(self):
        r"""已生成报表数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReportCount

    @ReportCount.setter
    def ReportCount(self, ReportCount):
        self._ReportCount = ReportCount

    @property
    def MissionStart(self):
        r"""任务起停 1:关闭 2:开启 仅周期报表有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MissionStart

    @MissionStart.setter
    def MissionStart(self, MissionStart):
        self._MissionStart = MissionStart

    @property
    def CntDay(self):
        r"""统计周期 1:24小时 7:近一周 30:近30天 90:近90天 180:
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CntDay

    @CntDay.setter
    def CntDay(self, CntDay):
        self._CntDay = CntDay

    @property
    def CntCycle(self):
        r"""重复周期 1:每天 2:每周 3:每月
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CntCycle

    @CntCycle.setter
    def CntCycle(self, CntCycle):
        self._CntCycle = CntCycle

    @property
    def CntTime(self):
        r"""执行日期 重复周期为天：无意义 周：星期几 1-7  月每月
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CntTime

    @CntTime.setter
    def CntTime(self, CntTime):
        self._CntTime = CntTime

    @property
    def CntDate(self):
        r"""执行时间 格式15:04 到分钟
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CntDate

    @CntDate.setter
    def CntDate(self, CntDate):
        self._CntDate = CntDate

    @property
    def Receivers(self):
        r"""创建者 0:内置 其余存放用户(uin)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def Notification(self):
        r"""Notification  int  1关闭 2开启 不变更为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TplName = params.get("TplName")
        self._ReportType = params.get("ReportType")
        self._Remark = params.get("Remark")
        self._TemplateId = params.get("TemplateId")
        if params.get("AssetsList") is not None:
            self._AssetsList = []
            for item in params.get("AssetsList"):
                obj = AssetsInfo()
                obj._deserialize(item)
                self._AssetsList.append(obj)
        self._NextStartTime = params.get("NextStartTime")
        self._MissionStatus = params.get("MissionStatus")
        self._MissionStatusMessage = params.get("MissionStatusMessage")
        self._ReportCount = params.get("ReportCount")
        self._MissionStart = params.get("MissionStart")
        self._CntDay = params.get("CntDay")
        self._CntCycle = params.get("CntCycle")
        self._CntTime = params.get("CntTime")
        self._CntDate = params.get("CntDate")
        self._Receivers = params.get("Receivers")
        self._Notification = params.get("Notification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Reports(AbstractModel):
    r"""报表列表字段数组

    """

    def __init__(self):
        r"""
        :param _AddTime: 生成时间
        :type AddTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Id: 报告 ID
        :type Id: int
        :param _InstanceId: 审计 ID
        :type InstanceId: int
        :param _IsDelete: 是否已删除
        :type IsDelete: int
        :param _Receivers: 发送目标
        :type Receivers: str
        :param _Remark: 报告说明
        :type Remark: str
        :param _ReportFile: 报告文件
        :type ReportFile: str
        :param _ReportStatus: 状态
        :type ReportStatus: int
        :param _ReportTmpStatus: 状态
        :type ReportTmpStatus: int
        :param _ReportType: 报告类型
        :type ReportType: int
        :param _SendResult: 发送结果
        :type SendResult: str
        :param _SendType: 发送类型
        :type SendType: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Title: 报告名称
        :type Title: str
        :param _TemplateId: 报表模板
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: int
        :param _AssetsList: 包含资产
注意：此字段可能返回 null，表示取不到有效值。
        :type AssetsList: list of AssetsInfo
        :param _CntDay: 时间范围 1:24小时 7:近一周 30:近30天 90:近90天 180:近180天 不变更为0
注意：此字段可能返回 null，表示取不到有效值。
        :type CntDay: int
        """
        self._AddTime = None
        self._EndTime = None
        self._Id = None
        self._InstanceId = None
        self._IsDelete = None
        self._Receivers = None
        self._Remark = None
        self._ReportFile = None
        self._ReportStatus = None
        self._ReportTmpStatus = None
        self._ReportType = None
        self._SendResult = None
        self._SendType = None
        self._StartTime = None
        self._Title = None
        self._TemplateId = None
        self._AssetsList = None
        self._CntDay = None

    @property
    def AddTime(self):
        r"""生成时间
        :rtype: int
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        r"""报告 ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        r"""审计 ID
        :rtype: int
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IsDelete(self):
        r"""是否已删除
        :rtype: int
        """
        return self._IsDelete

    @IsDelete.setter
    def IsDelete(self, IsDelete):
        self._IsDelete = IsDelete

    @property
    def Receivers(self):
        r"""发送目标
        :rtype: str
        """
        return self._Receivers

    @Receivers.setter
    def Receivers(self, Receivers):
        self._Receivers = Receivers

    @property
    def Remark(self):
        r"""报告说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReportFile(self):
        r"""报告文件
        :rtype: str
        """
        return self._ReportFile

    @ReportFile.setter
    def ReportFile(self, ReportFile):
        self._ReportFile = ReportFile

    @property
    def ReportStatus(self):
        r"""状态
        :rtype: int
        """
        return self._ReportStatus

    @ReportStatus.setter
    def ReportStatus(self, ReportStatus):
        self._ReportStatus = ReportStatus

    @property
    def ReportTmpStatus(self):
        r"""状态
        :rtype: int
        """
        return self._ReportTmpStatus

    @ReportTmpStatus.setter
    def ReportTmpStatus(self, ReportTmpStatus):
        self._ReportTmpStatus = ReportTmpStatus

    @property
    def ReportType(self):
        r"""报告类型
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def SendResult(self):
        r"""发送结果
        :rtype: str
        """
        return self._SendResult

    @SendResult.setter
    def SendResult(self, SendResult):
        self._SendResult = SendResult

    @property
    def SendType(self):
        r"""发送类型
        :rtype: str
        """
        return self._SendType

    @SendType.setter
    def SendType(self, SendType):
        self._SendType = SendType

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Title(self):
        r"""报告名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def TemplateId(self):
        r"""报表模板
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def AssetsList(self):
        r"""包含资产
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AssetsInfo
        """
        return self._AssetsList

    @AssetsList.setter
    def AssetsList(self, AssetsList):
        self._AssetsList = AssetsList

    @property
    def CntDay(self):
        r"""时间范围 1:24小时 7:近一周 30:近30天 90:近90天 180:近180天 不变更为0
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CntDay

    @CntDay.setter
    def CntDay(self, CntDay):
        self._CntDay = CntDay


    def _deserialize(self, params):
        self._AddTime = params.get("AddTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._IsDelete = params.get("IsDelete")
        self._Receivers = params.get("Receivers")
        self._Remark = params.get("Remark")
        self._ReportFile = params.get("ReportFile")
        self._ReportStatus = params.get("ReportStatus")
        self._ReportTmpStatus = params.get("ReportTmpStatus")
        self._ReportType = params.get("ReportType")
        self._SendResult = params.get("SendResult")
        self._SendType = params.get("SendType")
        self._StartTime = params.get("StartTime")
        self._Title = params.get("Title")
        self._TemplateId = params.get("TemplateId")
        if params.get("AssetsList") is not None:
            self._AssetsList = []
            for item in params.get("AssetsList"):
                obj = AssetsInfo()
                obj._deserialize(item)
                self._AssetsList.append(obj)
        self._CntDay = params.get("CntDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        