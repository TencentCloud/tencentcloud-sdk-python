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


class CreateBlockNodeRecordsRequest(AbstractModel):
    """CreateBlockNodeRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 盘查组id，可在“盘查组概览”功能中获取。
        :type GroupId: str
        :param NodeId: 节点id，可在“数据接入管理”中获取。
        :type NodeId: str
        :param Records: 节点数据json，具体demo请参考输入示例，其中key为数据接入管理中节点内创建的属性变量名，value为期望的推送值。
        :type Records: str
        """
        self.GroupId = None
        self.NodeId = None
        self.Records = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.NodeId = params.get("NodeId")
        self.Records = params.get("Records")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlockNodeRecordsResponse(AbstractModel):
    """CreateBlockNodeRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")