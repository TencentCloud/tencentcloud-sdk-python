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
        :param TaskType: 数据流通任务类型, FS_TO_COS(文件系统到COS Bucket),或者COS_TO_FS(COS Bucket到文件系统)
        :type TaskType: str
        :param Bucket: COS存储桶名
        :type Bucket: str
        :param FileSystemId: 文件系统ID
        :type FileSystemId: str
        :param TaskPath: 对于FS_TO_COS, TaskPath是Bucket映射目录的相对路径, 对于COS_TO_FS是COS上的路径。如果置为空, 则表示全部数据
        :type TaskPath: str
        :param TaskName: 任务名称
        :type TaskName: str
        :param RepositoryType: 数据流通方式 MSP_AFM 手动加载  RAW_AFM 按需加载
        :type RepositoryType: str
        :param TextLocation: 文件列表下载地址，以http开头
        :type TextLocation: str
        """
        self.TaskType = None
        self.Bucket = None
        self.FileSystemId = None
        self.TaskPath = None
        self.TaskName = None
        self.RepositoryType = None
        self.TextLocation = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Bucket = params.get("Bucket")
        self.FileSystemId = params.get("FileSystemId")
        self.TaskPath = params.get("TaskPath")
        self.TaskName = params.get("TaskName")
        self.RepositoryType = params.get("RepositoryType")
        self.TextLocation = params.get("TextLocation")
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


class DescribeDataRepositoryTaskStatusRequest(AbstractModel):
    """DescribeDataRepositoryTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: task id
        :type TaskId: str
        :param FileSystemId: file system id
        :type FileSystemId: str
        """
        self.TaskId = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.FileSystemId = params.get("FileSystemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataRepositoryTaskStatusResponse(AbstractModel):
    """DescribeDataRepositoryTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务id
        :type TaskId: str
        :param Status: 任务状态 0(初始化中), 1(运行中), 2(已完成), 3(任务失败)
        :type Status: int
        :param FinishedFileNumber: 已完成的文件数量
        :type FinishedFileNumber: int
        :param FinishedCapacity: 已完成的数据量
        :type FinishedCapacity: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Status = None
        self.FinishedFileNumber = None
        self.FinishedCapacity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.FinishedFileNumber = params.get("FinishedFileNumber")
        self.FinishedCapacity = params.get("FinishedCapacity")
        self.RequestId = params.get("RequestId")