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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 枚举范围： AddTimeStamp, InstanceName, ProjectId
        :type OrderBy: str
        :param _SearchKeys: 查找的关键字
        :type SearchKeys: list of str
        :param _UniqSubnetIds: 子网ID列表
        :type UniqSubnetIds: list of str
        :param _Vips: VIP列表
        :type Vips: list of str
        :param _OrderType: 0倒序，1正序，默认倒序
        :type OrderType: int
        :param _InstanceNames: 实例名称列表
        :type InstanceNames: list of str
        :param _UniqVpcIds: VPC ID列表
        :type UniqVpcIds: list of str
        :param _ProjectIds: 项目ID列表
        :type ProjectIds: list of int
        :param _Offset: 偏移量，取Limit整数倍
        :type Offset: int
        :param _Limit: 实例列表的大小，参数默认值100
        :type Limit: int
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        """
        self._OrderBy = None
        self._SearchKeys = None
        self._UniqSubnetIds = None
        self._Vips = None
        self._OrderType = None
        self._InstanceNames = None
        self._UniqVpcIds = None
        self._ProjectIds = None
        self._Offset = None
        self._Limit = None
        self._InstanceIds = None

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def SearchKeys(self):
        return self._SearchKeys

    @SearchKeys.setter
    def SearchKeys(self, SearchKeys):
        self._SearchKeys = SearchKeys

    @property
    def UniqSubnetIds(self):
        return self._UniqSubnetIds

    @UniqSubnetIds.setter
    def UniqSubnetIds(self, UniqSubnetIds):
        self._UniqSubnetIds = UniqSubnetIds

    @property
    def Vips(self):
        return self._Vips

    @Vips.setter
    def Vips(self, Vips):
        self._Vips = Vips

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def InstanceNames(self):
        return self._InstanceNames

    @InstanceNames.setter
    def InstanceNames(self, InstanceNames):
        self._InstanceNames = InstanceNames

    @property
    def UniqVpcIds(self):
        return self._UniqVpcIds

    @UniqVpcIds.setter
    def UniqVpcIds(self, UniqVpcIds):
        self._UniqVpcIds = UniqVpcIds

    @property
    def ProjectIds(self):
        return self._ProjectIds

    @ProjectIds.setter
    def ProjectIds(self, ProjectIds):
        self._ProjectIds = ProjectIds

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._SearchKeys = params.get("SearchKeys")
        self._UniqSubnetIds = params.get("UniqSubnetIds")
        self._Vips = params.get("Vips")
        self._OrderType = params.get("OrderType")
        self._InstanceNames = params.get("InstanceNames")
        self._UniqVpcIds = params.get("UniqVpcIds")
        self._ProjectIds = params.get("ProjectIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: 实例详细信息列表
        :type InstanceList: list of InstanceListInfo
        :param _TotalNum: 实例数量
        :type TotalNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceListInfo()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class InstanceListInfo(AbstractModel):
    """实例详细信息列表

    """

    def __init__(self):
        r"""
        :param _ModTimeStamp: 实例修改时间
        :type ModTimeStamp: str
        :param _IsolateTimeStamp: 实例隔离时间
        :type IsolateTimeStamp: str
        :param _AutoRenewFlag: 实例是否设置自动续费标识，1：设置自动续费；0：未设置自动续费
        :type AutoRenewFlag: int
        :param _SetId: 仓库ID
        :type SetId: int
        :param _Status: 实例当前状态，0：发货中；1：运行中；2：创建失败；4：销毁中；5：隔离中；6：下线中
        :type Status: int
        :param _CmemId: 实例内置ID
        :type CmemId: int
        :param _Tags: 实例关联的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RegionId: 地域id 1--广州 4--上海 5-- 香港 6--多伦多 7--上海金融 8--北京 9-- 新加坡 11--深圳金融 15--美西（硅谷）16--成都 17--德国 18--韩国 19--重庆 21--印度 22--美东（弗吉尼亚）23--泰国   25--日本
        :type RegionId: int
        :param _InstanceDesc: 实例描述信息
        :type InstanceDesc: str
        :param _Expire: 过期策略
        :type Expire: int
        :param _SubnetId: vpc网络下子网id 如：46315
        :type SubnetId: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _AddTimeStamp: 实例创建时间
        :type AddTimeStamp: str
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _PayMode: 计费模式：0-按量计费，1-包年包月
        :type PayMode: int
        :param _VpcId: vpc网络id 如：75101
        :type VpcId: int
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _DeadlineTimeStamp: 实例截止时间
        :type DeadlineTimeStamp: str
        :param _UniqVpcId: vpc网络id 如：vpc-fk33jsf43kgv
        :type UniqVpcId: str
        :param _Vip: 实例vip
        :type Vip: str
        :param _UniqSubnetId: vpc网络下子网id 如：subnet-fd3j6l35mm0
        :type UniqSubnetId: str
        :param _AppId: 用户AppID
        :type AppId: int
        :param _Vport: 实例端口号
        :type Vport: int
        """
        self._ModTimeStamp = None
        self._IsolateTimeStamp = None
        self._AutoRenewFlag = None
        self._SetId = None
        self._Status = None
        self._CmemId = None
        self._Tags = None
        self._InstanceId = None
        self._RegionId = None
        self._InstanceDesc = None
        self._Expire = None
        self._SubnetId = None
        self._ProjectId = None
        self._AddTimeStamp = None
        self._ZoneId = None
        self._PayMode = None
        self._VpcId = None
        self._InstanceName = None
        self._DeadlineTimeStamp = None
        self._UniqVpcId = None
        self._Vip = None
        self._UniqSubnetId = None
        self._AppId = None
        self._Vport = None

    @property
    def ModTimeStamp(self):
        return self._ModTimeStamp

    @ModTimeStamp.setter
    def ModTimeStamp(self, ModTimeStamp):
        self._ModTimeStamp = ModTimeStamp

    @property
    def IsolateTimeStamp(self):
        return self._IsolateTimeStamp

    @IsolateTimeStamp.setter
    def IsolateTimeStamp(self, IsolateTimeStamp):
        self._IsolateTimeStamp = IsolateTimeStamp

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CmemId(self):
        return self._CmemId

    @CmemId.setter
    def CmemId(self, CmemId):
        self._CmemId = CmemId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def InstanceDesc(self):
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc

    @property
    def Expire(self):
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AddTimeStamp(self):
        return self._AddTimeStamp

    @AddTimeStamp.setter
    def AddTimeStamp(self, AddTimeStamp):
        self._AddTimeStamp = AddTimeStamp

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def DeadlineTimeStamp(self):
        return self._DeadlineTimeStamp

    @DeadlineTimeStamp.setter
    def DeadlineTimeStamp(self, DeadlineTimeStamp):
        self._DeadlineTimeStamp = DeadlineTimeStamp

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._ModTimeStamp = params.get("ModTimeStamp")
        self._IsolateTimeStamp = params.get("IsolateTimeStamp")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._SetId = params.get("SetId")
        self._Status = params.get("Status")
        self._CmemId = params.get("CmemId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._RegionId = params.get("RegionId")
        self._InstanceDesc = params.get("InstanceDesc")
        self._Expire = params.get("Expire")
        self._SubnetId = params.get("SubnetId")
        self._ProjectId = params.get("ProjectId")
        self._AddTimeStamp = params.get("AddTimeStamp")
        self._ZoneId = params.get("ZoneId")
        self._PayMode = params.get("PayMode")
        self._VpcId = params.get("VpcId")
        self._InstanceName = params.get("InstanceName")
        self._DeadlineTimeStamp = params.get("DeadlineTimeStamp")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Vip = params.get("Vip")
        self._UniqSubnetId = params.get("UniqSubnetId")
        self._AppId = params.get("AppId")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        