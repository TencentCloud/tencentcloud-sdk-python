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
        """
        :param InstanceIds: 实例ID组成的数组，数组下标从0开始\n        :type InstanceIds: list of str\n        :param InstanceNames: 实例名称组成的数组，数组下标从0开始\n        :type InstanceNames: list of str\n        :param Limit: 实例列表的大小，参数默认值100\n        :type Limit: int\n        :param Offset: 偏移量，取Limit整数倍\n        :type Offset: int\n        :param OrderBy: 枚举范围： AddTimeStamp, InstanceName, ProjectId\n        :type OrderBy: str\n        :param OrderType: 0倒序，1正序，默认倒序\n        :type OrderType: int\n        :param ProjectIds: 项目ID组成的数组，数组下标从0开始\n        :type ProjectIds: list of int\n        :param SearchKeys: 搜索关键词：支持实例ID、实例名称、完整IP\n        :type SearchKeys: list of str\n        :param UniqSubnetIds: 子网ID数组，数组下标从0开始，如：subnet-fdj24n34j2\n        :type UniqSubnetIds: list of str\n        :param UniqVpcIds: 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：vpc-sad23jfdfk\n        :type UniqVpcIds: list of str\n        :param Vips: 实例服务IP组成的数组，数组下标从0开始\n        :type Vips: list of str\n        """
        self.InstanceIds = None
        self.InstanceNames = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderType = None
        self.ProjectIds = None
        self.SearchKeys = None
        self.UniqSubnetIds = None
        self.UniqVpcIds = None
        self.Vips = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKeys = params.get("SearchKeys")
        self.UniqSubnetIds = params.get("UniqSubnetIds")
        self.UniqVpcIds = params.get("UniqVpcIds")
        self.Vips = params.get("Vips")
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
        :param InstanceList: 实例详细信息列表\n        :type InstanceList: list of InstanceListInfo\n        :param TotalNum: 实例数量\n        :type TotalNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceList = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceListInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class InstanceListInfo(AbstractModel):
    """实例详细信息列表

    """

    def __init__(self):
        """
        :param Tags: 实例关联的标签信息\n        :type Tags: list of TagInfo\n        :param AddTimeStamp: 实例创建时间\n        :type AddTimeStamp: str\n        :param AppId: 用户AppID\n        :type AppId: int\n        :param AutoRenewFlag: 实例是否设置自动续费标识，1：设置自动续费；0：未设置自动续费\n        :type AutoRenewFlag: int\n        :param CmemId: 实例内置ID\n        :type CmemId: int\n        :param DeadlineTimeStamp: 实例截止时间\n        :type DeadlineTimeStamp: str\n        :param Expire: 过期策略\n        :type Expire: int\n        :param InstanceDesc: 实例描述信息\n        :type InstanceDesc: str\n        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceName: 实例名称\n        :type InstanceName: str\n        :param IsolateTimeStamp: 实例隔离时间\n        :type IsolateTimeStamp: str\n        :param ModTimeStamp: 实例修改时间\n        :type ModTimeStamp: str\n        :param PayMode: 计费模式：0-按量计费，1-包年包月\n        :type PayMode: int\n        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param RegionId: 地域id 1--广州 4--上海 5-- 香港 6--多伦多 7--上海金融 8--北京 9-- 新加坡 11--深圳金融 15--美西（硅谷）16--成都 17--德国 18--韩国 19--重庆 21--印度 22--美东（弗吉尼亚）23--泰国 24--俄罗斯 25--日本\n        :type RegionId: int\n        :param SetId: 仓库ID\n        :type SetId: int\n        :param Status: 实例当前状态，0：待初始化；1：实例在流程中；2：实例运行中；-2：实例已隔离；-3：实例待删除\n        :type Status: int\n        :param SubnetId: vpc网络下子网id 如：46315\n        :type SubnetId: int\n        :param UniqSubnetId: vpc网络下子网id 如：subnet-fd3j6l35mm0\n        :type UniqSubnetId: str\n        :param UniqVpcId: vpc网络id 如：vpc-fk33jsf43kgv\n        :type UniqVpcId: str\n        :param Vip: 实例vip\n        :type Vip: str\n        :param VpcId: vpc网络id 如：75101\n        :type VpcId: int\n        :param Vport: 实例端口号\n        :type Vport: int\n        :param ZoneId: 区域ID\n        :type ZoneId: int\n        """
        self.Tags = None
        self.AddTimeStamp = None
        self.AppId = None
        self.AutoRenewFlag = None
        self.CmemId = None
        self.DeadlineTimeStamp = None
        self.Expire = None
        self.InstanceDesc = None
        self.InstanceId = None
        self.InstanceName = None
        self.IsolateTimeStamp = None
        self.ModTimeStamp = None
        self.PayMode = None
        self.ProjectId = None
        self.RegionId = None
        self.SetId = None
        self.Status = None
        self.SubnetId = None
        self.UniqSubnetId = None
        self.UniqVpcId = None
        self.Vip = None
        self.VpcId = None
        self.Vport = None
        self.ZoneId = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AddTimeStamp = params.get("AddTimeStamp")
        self.AppId = params.get("AppId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.CmemId = params.get("CmemId")
        self.DeadlineTimeStamp = params.get("DeadlineTimeStamp")
        self.Expire = params.get("Expire")
        self.InstanceDesc = params.get("InstanceDesc")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.IsolateTimeStamp = params.get("IsolateTimeStamp")
        self.ModTimeStamp = params.get("ModTimeStamp")
        self.PayMode = params.get("PayMode")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.SetId = params.get("SetId")
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.Vport = params.get("Vport")
        self.ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息

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
        