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


class ManageConfigRequest(AbstractModel):
    """ManageConfig请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Type: 配置中心类型（consul、zookeeper、apollo等）
        :type Type: str
        :param Command: 请求命名 PUT GET DELETE
        :type Command: str
        :param Key: 配置的Key
        :type Key: str
        :param Value: 配置的Value
        :type Value: str
        """
        self.InstanceId = None
        self.Type = None
        self.Command = None
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.Command = params.get("Command")
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class ManageConfigResponse(AbstractModel):
    """ManageConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 对配置中心操作配置之后的返回值
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")