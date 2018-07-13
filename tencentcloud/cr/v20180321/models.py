# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.Module = None
        self.Operation = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TaskResult: 任务结果
        :type TaskResult: str
        :param TaskType: 任务类型，010代表上传任务
        :type TaskType: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.TaskType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskResult = params.get("TaskResult")
        self.TaskType = params.get("TaskType")
        self.RequestId = params.get("RequestId")


class DownloadReportRequest(AbstractModel):
    """DownloadReport请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param ReportDate: 报告日期
        :type ReportDate: str
        """
        self.Module = None
        self.Operation = None
        self.ReportDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ReportDate = params.get("ReportDate")


class DownloadReportResponse(AbstractModel):
    """DownloadReport返回参数结构体

    """

    def __init__(self):
        """
        :param ReportUrl: 报告下载地址
        :type ReportUrl: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ReportUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportUrl = params.get("ReportUrl")
        self.RequestId = params.get("RequestId")


class UploadFileRequest(AbstractModel):
    """UploadFile请求参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param FileUrl: 文件上传地址，要求地址协议为HTTPS，且URL端口必须为443
        :type FileUrl: str
        :param FileName: 文件名
        :type FileName: str
        :param FileDate: 文件日期
        :type FileDate: str
        """
        self.Module = None
        self.Operation = None
        self.FileUrl = None
        self.FileName = None
        self.FileDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.FileUrl = params.get("FileUrl")
        self.FileName = params.get("FileName")
        self.FileDate = params.get("FileDate")


class UploadFileResponse(AbstractModel):
    """UploadFile返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")