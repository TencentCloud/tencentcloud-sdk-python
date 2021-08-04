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


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 创建的项目名(不为空且最长为 200)
        :type Name: str
        :param InstanceID: 项目对应实例 id
        :type InstanceID: str
        :param Rate: 项目抽样率(大于等于 0)
        :type Rate: str
        :param EnableURLGroup: 是否开启聚类
        :type EnableURLGroup: int
        :param Type: 项目类型("web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param Repo: 项目对应仓库地址(可选，最长为 256)
        :type Repo: str
        :param URL: 项目对应网页地址(可选，最长为 256)
        :type URL: str
        :param Desc: 创建的项目描述(可选，最长为 1000)
        :type Desc: str
        """
        self.Name = None
        self.InstanceID = None
        self.Rate = None
        self.EnableURLGroup = None
        self.Type = None
        self.Repo = None
        self.URL = None
        self.Desc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.InstanceID = params.get("InstanceID")
        self.Rate = params.get("Rate")
        self.EnableURLGroup = params.get("EnableURLGroup")
        self.Type = params.get("Type")
        self.Repo = params.get("Repo")
        self.URL = params.get("URL")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        """
        :param ID: 项目 id
        :type ID: int
        :param Key: 项目唯一key
        :type Key: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.Key = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Key = params.get("Key")
        self.RequestId = params.get("RequestId")