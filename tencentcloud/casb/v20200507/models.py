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
        :param CasbId: 实例Id
        :type CasbId: str
        :param MetaDataId: 元数据id
        :type MetaDataId: str
        :param DstCasbId: 目标实例Id 如果和实例Id相同则为同CasbId下的策略复制
        :type DstCasbId: str
        :param DstMetaDataId: 目标实例Id 如果和[元数据id]相同则为同元数据下的策略复制
        :type DstMetaDataId: str
        :param SrcTableFilter: 筛选来源数据库的表
        :type SrcTableFilter: list of CryptoCopyColumnPolicyTableFilter
        :param DstDatabaseName: 复制同元数据下的策略，需要填写目标数据库名
        :type DstDatabaseName: str
        """
        self.CasbId = None
        self.MetaDataId = None
        self.DstCasbId = None
        self.DstMetaDataId = None
        self.SrcTableFilter = None
        self.DstDatabaseName = None


    def _deserialize(self, params):
        self.CasbId = params.get("CasbId")
        self.MetaDataId = params.get("MetaDataId")
        self.DstCasbId = params.get("DstCasbId")
        self.DstMetaDataId = params.get("DstMetaDataId")
        if params.get("SrcTableFilter") is not None:
            self.SrcTableFilter = []
            for item in params.get("SrcTableFilter"):
                obj = CryptoCopyColumnPolicyTableFilter()
                obj._deserialize(item)
                self.SrcTableFilter.append(obj)
        self.DstDatabaseName = params.get("DstDatabaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyCryptoColumnPolicyResponse(AbstractModel):
    """CopyCryptoColumnPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CryptoCopyColumnPolicyTableFilter(AbstractModel):
    """策略迁移表信息筛选

    """

    def __init__(self):
        r"""
        :param DatabaseName: 数据库名称
        :type DatabaseName: str
        :param TableNameSet: 表名称
        :type TableNameSet: list of str
        """
        self.DatabaseName = None
        self.TableNameSet = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.TableNameSet = params.get("TableNameSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        