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


class CopyCryptoColumnPolicyRequest(AbstractModel):
    """CopyCryptoColumnPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CasbId: 实例Id
        :type CasbId: str
        :param _MetaDataId: 元数据id
        :type MetaDataId: str
        :param _DstCasbId: 目标实例Id 如果和实例Id相同则为同CasbId下的策略复制
        :type DstCasbId: str
        :param _DstMetaDataId: 目标实例Id 如果和[元数据id]相同则为同元数据下的策略复制
        :type DstMetaDataId: str
        :param _SrcTableFilter: 筛选来源数据库的表
        :type SrcTableFilter: list of CryptoCopyColumnPolicyTableFilter
        :param _DstDatabaseName: 复制同元数据下的策略，需要填写目标数据库名
        :type DstDatabaseName: str
        """
        self._CasbId = None
        self._MetaDataId = None
        self._DstCasbId = None
        self._DstMetaDataId = None
        self._SrcTableFilter = None
        self._DstDatabaseName = None

    @property
    def CasbId(self):
        return self._CasbId

    @CasbId.setter
    def CasbId(self, CasbId):
        self._CasbId = CasbId

    @property
    def MetaDataId(self):
        return self._MetaDataId

    @MetaDataId.setter
    def MetaDataId(self, MetaDataId):
        self._MetaDataId = MetaDataId

    @property
    def DstCasbId(self):
        return self._DstCasbId

    @DstCasbId.setter
    def DstCasbId(self, DstCasbId):
        self._DstCasbId = DstCasbId

    @property
    def DstMetaDataId(self):
        return self._DstMetaDataId

    @DstMetaDataId.setter
    def DstMetaDataId(self, DstMetaDataId):
        self._DstMetaDataId = DstMetaDataId

    @property
    def SrcTableFilter(self):
        return self._SrcTableFilter

    @SrcTableFilter.setter
    def SrcTableFilter(self, SrcTableFilter):
        self._SrcTableFilter = SrcTableFilter

    @property
    def DstDatabaseName(self):
        return self._DstDatabaseName

    @DstDatabaseName.setter
    def DstDatabaseName(self, DstDatabaseName):
        self._DstDatabaseName = DstDatabaseName


    def _deserialize(self, params):
        self._CasbId = params.get("CasbId")
        self._MetaDataId = params.get("MetaDataId")
        self._DstCasbId = params.get("DstCasbId")
        self._DstMetaDataId = params.get("DstMetaDataId")
        if params.get("SrcTableFilter") is not None:
            self._SrcTableFilter = []
            for item in params.get("SrcTableFilter"):
                obj = CryptoCopyColumnPolicyTableFilter()
                obj._deserialize(item)
                self._SrcTableFilter.append(obj)
        self._DstDatabaseName = params.get("DstDatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyCryptoColumnPolicyResponse(AbstractModel):
    """CopyCryptoColumnPolicy返回参数结构体

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


class CryptoCopyColumnPolicyTableFilter(AbstractModel):
    """策略迁移表信息筛选

    """

    def __init__(self):
        r"""
        :param _DatabaseName: 数据库名称
        :type DatabaseName: str
        :param _TableNameSet: 表名称
        :type TableNameSet: list of str
        """
        self._DatabaseName = None
        self._TableNameSet = None

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @DatabaseName.setter
    def DatabaseName(self, DatabaseName):
        self._DatabaseName = DatabaseName

    @property
    def TableNameSet(self):
        return self._TableNameSet

    @TableNameSet.setter
    def TableNameSet(self, TableNameSet):
        self._TableNameSet = TableNameSet


    def _deserialize(self, params):
        self._DatabaseName = params.get("DatabaseName")
        self._TableNameSet = params.get("TableNameSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        