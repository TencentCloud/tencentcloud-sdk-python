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


class CreateDataRepositoryTaskRequest(AbstractModel):
    """CreateDataRepositoryTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskType: 数据流通任务类型, FS_TO_COS(文件系统到COS Bucket),或者Bucket到文件系统(COS_TO_FS)
        :type TaskType: str
        :param Bucket: bucket名
        :type Bucket: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param TaskPath: 对于FS_TO_COS, TaskPath是Bucket映射目录的相对路径, 对于COS_TO_FS是COS上的路径。如果置位空, 则表示全部数据
        :type TaskPath: str
        :param TaskName: 任务名称
        :type TaskName: str
        """
        self.TaskType = None
        self.Bucket = None
        self.FileSystemId = None
        self.TaskPath = None
        self.TaskName = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Bucket = params.get("Bucket")
        self.FileSystemId = params.get("FileSystemId")
        self.TaskPath = params.get("TaskPath")
        self.TaskName = params.get("TaskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataRepositoryTaskResponse(AbstractModel):
    """CreateDataRepositoryTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")