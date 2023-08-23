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


class CreateDSPADbMetaResourcesRequest(AbstractModel):
    """CreateDSPADbMetaResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _MetaType: 资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :type MetaType: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _UpdateStatus: 用来标记本次更新是否已经是最后一次，可选值：continue（后续还需要更新）、finished（本次是最后一次更新）。
        :type UpdateStatus: str
        :param _UpdateId: 本次更新的ID号，用来标记一次完整的更新过程。
        :type UpdateId: str
        :param _Items: 云上资源列表。
        :type Items: list of DspaCloudResourceMeta
        """
        self._DspaId = None
        self._MetaType = None
        self._ResourceRegion = None
        self._UpdateStatus = None
        self._UpdateId = None
        self._Items = None

    @property
    def DspaId(self):
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def UpdateStatus(self):
        return self._UpdateStatus

    @UpdateStatus.setter
    def UpdateStatus(self, UpdateStatus):
        self._UpdateStatus = UpdateStatus

    @property
    def UpdateId(self):
        return self._UpdateId

    @UpdateId.setter
    def UpdateId(self, UpdateId):
        self._UpdateId = UpdateId

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        self._DspaId = params.get("DspaId")
        self._MetaType = params.get("MetaType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._UpdateStatus = params.get("UpdateStatus")
        self._UpdateId = params.get("UpdateId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DspaCloudResourceMeta()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDSPADbMetaResourcesResponse(AbstractModel):
    """CreateDSPADbMetaResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UpdateId: 本次更新的ID号，用来标记一次完整的更新过程。
        :type UpdateId: str
        :param _MetaType: 资源类型，支持：cdb（云数据库 MySQL）、dcdb（TDSQL MySQL版）、mariadb（云数据库 MariaDB）、postgres（云数据库 PostgreSQL）、cynosdbpg（TDSQL-C PostgreSQL版）、cynosdbmysql（TDSQL-C MySQL版）
        :type MetaType: str
        :param _DspaId: DSPA实例ID。
        :type DspaId: str
        :param _ResourceRegion: 资源所处地域。
        :type ResourceRegion: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UpdateId = None
        self._MetaType = None
        self._DspaId = None
        self._ResourceRegion = None
        self._RequestId = None

    @property
    def UpdateId(self):
        return self._UpdateId

    @UpdateId.setter
    def UpdateId(self, UpdateId):
        self._UpdateId = UpdateId

    @property
    def MetaType(self):
        return self._MetaType

    @MetaType.setter
    def MetaType(self, MetaType):
        self._MetaType = MetaType

    @property
    def DspaId(self):
        return self._DspaId

    @DspaId.setter
    def DspaId(self, DspaId):
        self._DspaId = DspaId

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UpdateId = params.get("UpdateId")
        self._MetaType = params.get("MetaType")
        self._DspaId = params.get("DspaId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._RequestId = params.get("RequestId")


class DspaCloudResourceMeta(AbstractModel):
    """云上资源元数据

    """

    def __init__(self):
        r"""
        :param _ResourceId: 用户资源ID。
        :type ResourceId: str
        :param _ResourceName: 资源名称。
        :type ResourceName: str
        :param _ResourceVip: 资源VIP。
        :type ResourceVip: str
        :param _ResourceVPort: 资源端口。
        :type ResourceVPort: int
        :param _ResourceCreateTime: 资源被创建时间。
        :type ResourceCreateTime: str
        :param _ResourceUniqueVpcId: 用户资源VPC ID 字符串。
        :type ResourceUniqueVpcId: str
        :param _ResourceUniqueSubnetId: 用户资源Subnet ID 字符串。
        :type ResourceUniqueSubnetId: str
        """
        self._ResourceId = None
        self._ResourceName = None
        self._ResourceVip = None
        self._ResourceVPort = None
        self._ResourceCreateTime = None
        self._ResourceUniqueVpcId = None
        self._ResourceUniqueSubnetId = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceVip(self):
        return self._ResourceVip

    @ResourceVip.setter
    def ResourceVip(self, ResourceVip):
        self._ResourceVip = ResourceVip

    @property
    def ResourceVPort(self):
        return self._ResourceVPort

    @ResourceVPort.setter
    def ResourceVPort(self, ResourceVPort):
        self._ResourceVPort = ResourceVPort

    @property
    def ResourceCreateTime(self):
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def ResourceUniqueVpcId(self):
        return self._ResourceUniqueVpcId

    @ResourceUniqueVpcId.setter
    def ResourceUniqueVpcId(self, ResourceUniqueVpcId):
        self._ResourceUniqueVpcId = ResourceUniqueVpcId

    @property
    def ResourceUniqueSubnetId(self):
        return self._ResourceUniqueSubnetId

    @ResourceUniqueSubnetId.setter
    def ResourceUniqueSubnetId(self, ResourceUniqueSubnetId):
        self._ResourceUniqueSubnetId = ResourceUniqueSubnetId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceName = params.get("ResourceName")
        self._ResourceVip = params.get("ResourceVip")
        self._ResourceVPort = params.get("ResourceVPort")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        self._ResourceUniqueVpcId = params.get("ResourceUniqueVpcId")
        self._ResourceUniqueSubnetId = params.get("ResourceUniqueSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        