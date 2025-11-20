# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.gs.v20191118 import models
from typing import Dict


class GsClient(AbstractClient):
    _apiVersion = '2019-11-18'
    _endpoint = 'gs.tencentcloudapi.com'
    _service = 'gs'

    async def BackUpAndroidInstance(
            self,
            request: models.BackUpAndroidInstanceRequest,
            opts: Dict = None,
    ) -> models.BackUpAndroidInstanceResponse:
        """
        备份安卓实例。该接口需要联系我们开通内网存储才能使用。
        """
        
        kwargs = {}
        kwargs["action"] = "BackUpAndroidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BackUpAndroidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BackUpAndroidInstanceToStorage(
            self,
            request: models.BackUpAndroidInstanceToStorageRequest,
            opts: Dict = None,
    ) -> models.BackUpAndroidInstanceToStorageResponse:
        """
        备份云手机数据到指定存储，支持 COS 和兼容 AWS S3 协议的对象存储服务。如果是备份到 COS 时，会使用公网流量，授权 COS bucket 请在控制台中操作。
        """
        
        kwargs = {}
        kwargs["action"] = "BackUpAndroidInstanceToStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BackUpAndroidInstanceToStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CleanAndroidInstancesAppData(
            self,
            request: models.CleanAndroidInstancesAppDataRequest,
            opts: Dict = None,
    ) -> models.CleanAndroidInstancesAppDataResponse:
        """
        批量清理安卓实例应用数据
        """
        
        kwargs = {}
        kwargs["action"] = "CleanAndroidInstancesAppData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CleanAndroidInstancesAppDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConnectAndroidInstance(
            self,
            request: models.ConnectAndroidInstanceRequest,
            opts: Dict = None,
    ) -> models.ConnectAndroidInstanceResponse:
        """
        连接安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "ConnectAndroidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConnectAndroidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyAndroidInstance(
            self,
            request: models.CopyAndroidInstanceRequest,
            opts: Dict = None,
    ) -> models.CopyAndroidInstanceResponse:
        """
        复制安卓实例：
        1. 排除和包含文件只能指定 /data 下的文件，不指定时复制整个 /data 目录
        2. 源实例和目的实例必须在同一区域
        3. 复制时，源实例和目的实例都会停机，复制完后实例会自动启动
        4. 复制时会产生大量内网流量，请限制并发
        """
        
        kwargs = {}
        kwargs["action"] = "CopyAndroidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyAndroidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidApp(
            self,
            request: models.CreateAndroidAppRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidAppResponse:
        """
        创建安卓应用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidAppVersion(
            self,
            request: models.CreateAndroidAppVersionRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidAppVersionResponse:
        """
        创建安卓应用版本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidAppVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidAppVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstanceADB(
            self,
            request: models.CreateAndroidInstanceADBRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstanceADBResponse:
        """
        创建云手机实例 ADB 连接信息，请将返回结果的 PrivateKey 字段保存为 pem 文件，并将 pem 文件权限设置为 600，再参考返回结果的 ConnectCommand 使用 adb 连接实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstanceADB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstanceADBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstanceAcceleratorToken(
            self,
            request: models.CreateAndroidInstanceAcceleratorTokenRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstanceAcceleratorTokenResponse:
        """
        创建安卓实例加速Token
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstanceAcceleratorToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstanceAcceleratorTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstanceImage(
            self,
            request: models.CreateAndroidInstanceImageRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstanceImageResponse:
        """
        使用指定的安卓实例创建镜像，创建镜像时指定的实例会关机，镜像创建完成后实例会自动开机。当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像创建完成处于可用状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstanceImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstanceImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstanceLabel(
            self,
            request: models.CreateAndroidInstanceLabelRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstanceLabelResponse:
        """
        创建安卓实例标签
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstanceLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstanceLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstanceSSH(
            self,
            request: models.CreateAndroidInstanceSSHRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstanceSSHResponse:
        """
        创建安卓实例 SSH 连接信息，请将返回结果的 PrivateKey 字段保存为 pem 文件，并将 pem 文件权限设置为 600，再参考返回结果的 ConnectCommand 使用 ssh 连接实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstanceSSH"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstanceSSHResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstanceWebShell(
            self,
            request: models.CreateAndroidInstanceWebShellRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstanceWebShellResponse:
        """
        创建安卓实例 WebShell 连接信息，返回的 ConnectUrl 可通过浏览器直接打开访问，链接有效期 1 小时，链接打开后可持续使用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstanceWebShell"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstanceWebShellResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstances(
            self,
            request: models.CreateAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstancesResponse:
        """
        创建安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstancesAccessToken(
            self,
            request: models.CreateAndroidInstancesAccessTokenRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstancesAccessTokenResponse:
        """
        创建安卓实例访问Token
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstancesAccessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstancesAccessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndroidInstancesScreenshot(
            self,
            request: models.CreateAndroidInstancesScreenshotRequest,
            opts: Dict = None,
    ) -> models.CreateAndroidInstancesScreenshotResponse:
        """
        安卓实例截图
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndroidInstancesScreenshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndroidInstancesScreenshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosCredential(
            self,
            request: models.CreateCosCredentialRequest,
            opts: Dict = None,
    ) -> models.CreateCosCredentialResponse:
        """
        用于创建 Cos 临时密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSession(
            self,
            request: models.CreateSessionRequest,
            opts: Dict = None,
    ) -> models.CreateSessionResponse:
        """
        创建会话
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAndroidApp(
            self,
            request: models.DeleteAndroidAppRequest,
            opts: Dict = None,
    ) -> models.DeleteAndroidAppResponse:
        """
        删除安卓应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAndroidApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAndroidAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAndroidAppVersion(
            self,
            request: models.DeleteAndroidAppVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteAndroidAppVersionResponse:
        """
        删除安卓应用版本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAndroidAppVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAndroidAppVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAndroidInstanceBackupFiles(
            self,
            request: models.DeleteAndroidInstanceBackupFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteAndroidInstanceBackupFilesResponse:
        """
        删除安卓实例备份文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAndroidInstanceBackupFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAndroidInstanceBackupFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAndroidInstanceBackups(
            self,
            request: models.DeleteAndroidInstanceBackupsRequest,
            opts: Dict = None,
    ) -> models.DeleteAndroidInstanceBackupsResponse:
        """
        批量删除安卓实例备份
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAndroidInstanceBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAndroidInstanceBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAndroidInstanceImages(
            self,
            request: models.DeleteAndroidInstanceImagesRequest,
            opts: Dict = None,
    ) -> models.DeleteAndroidInstanceImagesResponse:
        """
        删除安卓实例镜像
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAndroidInstanceImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAndroidInstanceImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAndroidInstanceLabel(
            self,
            request: models.DeleteAndroidInstanceLabelRequest,
            opts: Dict = None,
    ) -> models.DeleteAndroidInstanceLabelResponse:
        """
        删除安卓实例标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAndroidInstanceLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAndroidInstanceLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidApps(
            self,
            request: models.DescribeAndroidAppsRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidAppsResponse:
        """
        查询安卓应用信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstanceApps(
            self,
            request: models.DescribeAndroidInstanceAppsRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstanceAppsResponse:
        """
        查询安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstanceApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstanceAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstanceBackups(
            self,
            request: models.DescribeAndroidInstanceBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstanceBackupsResponse:
        """
        查询安卓实例备份列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstanceBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstanceBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstanceImages(
            self,
            request: models.DescribeAndroidInstanceImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstanceImagesResponse:
        """
        查询安卓实例镜像信息，当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像处于可用状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstanceImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstanceImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstanceLabels(
            self,
            request: models.DescribeAndroidInstanceLabelsRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstanceLabelsResponse:
        """
        查询安卓实例标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstanceLabels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstanceLabelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstanceTasksStatus(
            self,
            request: models.DescribeAndroidInstanceTasksStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstanceTasksStatusResponse:
        """
        查询安卓实例任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstanceTasksStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstanceTasksStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstances(
            self,
            request: models.DescribeAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstancesResponse:
        """
        查询安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstancesAppBlacklist(
            self,
            request: models.DescribeAndroidInstancesAppBlacklistRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstancesAppBlacklistResponse:
        """
        查询安卓实例黑名单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstancesAppBlacklist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstancesAppBlacklistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAndroidInstancesByApps(
            self,
            request: models.DescribeAndroidInstancesByAppsRequest,
            opts: Dict = None,
    ) -> models.DescribeAndroidInstancesByAppsResponse:
        """
        批量查询安装指定应用的安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAndroidInstancesByApps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAndroidInstancesByAppsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesCount(
            self,
            request: models.DescribeInstancesCountRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesCountResponse:
        """
        获取并发总数和运行数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyAndroidInstances(
            self,
            request: models.DestroyAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.DestroyAndroidInstancesResponse:
        """
        销毁安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableAndroidInstancesApp(
            self,
            request: models.DisableAndroidInstancesAppRequest,
            opts: Dict = None,
    ) -> models.DisableAndroidInstancesAppResponse:
        """
        批量禁用安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "DisableAndroidInstancesApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableAndroidInstancesAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisconnectAndroidInstance(
            self,
            request: models.DisconnectAndroidInstanceRequest,
            opts: Dict = None,
    ) -> models.DisconnectAndroidInstanceResponse:
        """
        断开安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "DisconnectAndroidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisconnectAndroidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisconnectAndroidInstanceAccelerator(
            self,
            request: models.DisconnectAndroidInstanceAcceleratorRequest,
            opts: Dict = None,
    ) -> models.DisconnectAndroidInstanceAcceleratorResponse:
        """
        断开安卓实例加速节点
        """
        
        kwargs = {}
        kwargs["action"] = "DisconnectAndroidInstanceAccelerator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisconnectAndroidInstanceAcceleratorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeAndroidInstanceImageToHosts(
            self,
            request: models.DistributeAndroidInstanceImageToHostsRequest,
            opts: Dict = None,
    ) -> models.DistributeAndroidInstanceImageToHostsResponse:
        """
        分发安卓实例镜像至宿主机
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeAndroidInstanceImageToHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeAndroidInstanceImageToHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributeFileToAndroidInstances(
            self,
            request: models.DistributeFileToAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.DistributeFileToAndroidInstancesResponse:
        """
        将一个文件批量分发到多个实例，一次接口调用触发一次文件分发，一次文件分发只会从公网下载一次，然后文件会走内网分发到实例列表中的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DistributeFileToAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributeFileToAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DistributePhotoToAndroidInstances(
            self,
            request: models.DistributePhotoToAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.DistributePhotoToAndroidInstancesResponse:
        """
        将一张照片批量分发到多个实例的相册中，一次接口调用触发一次照片分发，一次照片分发只会从公网下载一次，然后照片会走内网分发到实例列表中的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DistributePhotoToAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DistributePhotoToAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableAndroidInstancesApp(
            self,
            request: models.EnableAndroidInstancesAppRequest,
            opts: Dict = None,
    ) -> models.EnableAndroidInstancesAppResponse:
        """
        批量启用安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "EnableAndroidInstancesApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableAndroidInstancesAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteCommandOnAndroidInstances(
            self,
            request: models.ExecuteCommandOnAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.ExecuteCommandOnAndroidInstancesResponse:
        """
        在安卓实例上异步执行命令，命令输出结果如果内容过长会被截断
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteCommandOnAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteCommandOnAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchAndroidInstancesLogs(
            self,
            request: models.FetchAndroidInstancesLogsRequest,
            opts: Dict = None,
    ) -> models.FetchAndroidInstancesLogsResponse:
        """
        批量将实例的 logcat 日志文件上传到您已授权的 COS bucket 中，授权 COS bucket 请在控制台中操作。
        """
        
        kwargs = {}
        kwargs["action"] = "FetchAndroidInstancesLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchAndroidInstancesLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportAndroidInstanceImage(
            self,
            request: models.ImportAndroidInstanceImageRequest,
            opts: Dict = None,
    ) -> models.ImportAndroidInstanceImageResponse:
        """
        导入安卓实例镜像，当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像导入完成处于可用状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportAndroidInstanceImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportAndroidInstanceImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallAndroidInstancesApp(
            self,
            request: models.InstallAndroidInstancesAppRequest,
            opts: Dict = None,
    ) -> models.InstallAndroidInstancesAppResponse:
        """
        安装安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "InstallAndroidInstancesApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallAndroidInstancesAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallAndroidInstancesAppWithURL(
            self,
            request: models.InstallAndroidInstancesAppWithURLRequest,
            opts: Dict = None,
    ) -> models.InstallAndroidInstancesAppWithURLResponse:
        """
        通过 URL 安装安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "InstallAndroidInstancesAppWithURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallAndroidInstancesAppWithURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidApp(
            self,
            request: models.ModifyAndroidAppRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidAppResponse:
        """
        修改安卓应用信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidAppVersion(
            self,
            request: models.ModifyAndroidAppVersionRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidAppVersionResponse:
        """
        修改安卓应用版本
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidAppVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidAppVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstanceInformation(
            self,
            request: models.ModifyAndroidInstanceInformationRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstanceInformationResponse:
        """
        修改安卓实例的信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstanceInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstanceInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstanceResolution(
            self,
            request: models.ModifyAndroidInstanceResolutionRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstanceResolutionResponse:
        """
        修改安卓实例分辨率。需要注意的是该接口可能导致正在运行的应用出现闪退，所以建议在实例维护时期才进行调用。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstanceResolution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstanceResolutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstancesAppBlacklist(
            self,
            request: models.ModifyAndroidInstancesAppBlacklistRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstancesAppBlacklistResponse:
        """
        修改安卓实例应用黑名单
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstancesAppBlacklist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstancesAppBlacklistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstancesInformation(
            self,
            request: models.ModifyAndroidInstancesInformationRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstancesInformationResponse:
        """
        批量修改安卓实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstancesInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstancesInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstancesLabels(
            self,
            request: models.ModifyAndroidInstancesLabelsRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstancesLabelsResponse:
        """
        批量修改安卓实例的标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstancesLabels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstancesLabelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstancesProperties(
            self,
            request: models.ModifyAndroidInstancesPropertiesRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstancesPropertiesResponse:
        """
        批量修改安卓实例属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstancesProperties"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstancesPropertiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstancesResolution(
            self,
            request: models.ModifyAndroidInstancesResolutionRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstancesResolutionResponse:
        """
        修改安卓实例分辨率。需要注意的是该接口需要重启才能生效。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstancesResolution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstancesResolutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstancesResources(
            self,
            request: models.ModifyAndroidInstancesResourcesRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstancesResourcesResponse:
        """
        批量修改安卓实例资源限制
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstancesResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstancesResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAndroidInstancesUserId(
            self,
            request: models.ModifyAndroidInstancesUserIdRequest,
            opts: Dict = None,
    ) -> models.ModifyAndroidInstancesUserIdResponse:
        """
        批量修改安卓实例的用户ID
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAndroidInstancesUserId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAndroidInstancesUserIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootAndroidInstanceHosts(
            self,
            request: models.RebootAndroidInstanceHostsRequest,
            opts: Dict = None,
    ) -> models.RebootAndroidInstanceHostsResponse:
        """
        重启安卓实例宿主机。请注意：

        - 当前每 15 分钟只能重启一次
        - 一个宿主机可能有多个云手机实例，重启宿主机会影响运行在上面的所有实例，请确保该宿主机上的所有云手机实例未投入业务使用
        """
        
        kwargs = {}
        kwargs["action"] = "RebootAndroidInstanceHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootAndroidInstanceHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootAndroidInstances(
            self,
            request: models.RebootAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.RebootAndroidInstancesResponse:
        """
        重启安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "RebootAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewAndroidInstancesAccessToken(
            self,
            request: models.RenewAndroidInstancesAccessTokenRequest,
            opts: Dict = None,
    ) -> models.RenewAndroidInstancesAccessTokenResponse:
        """
        续期安卓实例访问Token
        """
        
        kwargs = {}
        kwargs["action"] = "RenewAndroidInstancesAccessToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewAndroidInstancesAccessTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAndroidInstances(
            self,
            request: models.ResetAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.ResetAndroidInstancesResponse:
        """
        重置安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartAndroidInstancesApp(
            self,
            request: models.RestartAndroidInstancesAppRequest,
            opts: Dict = None,
    ) -> models.RestartAndroidInstancesAppResponse:
        """
        重启安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "RestartAndroidInstancesApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartAndroidInstancesAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreAndroidInstance(
            self,
            request: models.RestoreAndroidInstanceRequest,
            opts: Dict = None,
    ) -> models.RestoreAndroidInstanceResponse:
        """
        还原安卓实例。该接口需要联系我们开通内网存储才能使用。
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreAndroidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreAndroidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreAndroidInstanceFromStorage(
            self,
            request: models.RestoreAndroidInstanceFromStorageRequest,
            opts: Dict = None,
    ) -> models.RestoreAndroidInstanceFromStorageResponse:
        """
        使用指定存储数据还原云手机，支持 COS 和兼容 AWS S3 协议的对象存储服务。如果还原数据来自 COS 时，会使用公网流量，授权 COS bucket 请在控制台中操作。
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreAndroidInstanceFromStorage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreAndroidInstanceFromStorageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaveGameArchive(
            self,
            request: models.SaveGameArchiveRequest,
            opts: Dict = None,
    ) -> models.SaveGameArchiveResponse:
        """
        保存游戏存档
        """
        
        kwargs = {}
        kwargs["action"] = "SaveGameArchive"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaveGameArchiveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAndroidInstancesBGAppKeepAlive(
            self,
            request: models.SetAndroidInstancesBGAppKeepAliveRequest,
            opts: Dict = None,
    ) -> models.SetAndroidInstancesBGAppKeepAliveResponse:
        """
        批量设置安卓实例应用后台保活，开启应用保活，只是降低应用被杀死或回收的优先级，并不能保证应用不会被杀死或回收（如出现内存不足等资源限制时，应用也有概率被杀死或回收）
        """
        
        kwargs = {}
        kwargs["action"] = "SetAndroidInstancesBGAppKeepAlive"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAndroidInstancesBGAppKeepAliveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAndroidInstancesFGAppKeepAlive(
            self,
            request: models.SetAndroidInstancesFGAppKeepAliveRequest,
            opts: Dict = None,
    ) -> models.SetAndroidInstancesFGAppKeepAliveResponse:
        """
        批量设置安卓实例应用前台保活，开启应用保活，只是降低应用被杀死或回收的优先级，并不能保证应用不会被杀死或回收（如出现内存不足等资源限制时，应用也有概率被杀死或回收）
        """
        
        kwargs = {}
        kwargs["action"] = "SetAndroidInstancesFGAppKeepAlive"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAndroidInstancesFGAppKeepAliveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAndroidInstances(
            self,
            request: models.StartAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.StartAndroidInstancesResponse:
        """
        开机安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "StartAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAndroidInstancesApp(
            self,
            request: models.StartAndroidInstancesAppRequest,
            opts: Dict = None,
    ) -> models.StartAndroidInstancesAppResponse:
        """
        启动安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "StartAndroidInstancesApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAndroidInstancesAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishStream(
            self,
            request: models.StartPublishStreamRequest,
            opts: Dict = None,
    ) -> models.StartPublishStreamResponse:
        """
        开始云端推流
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishStreamToCSS(
            self,
            request: models.StartPublishStreamToCSSRequest,
            opts: Dict = None,
    ) -> models.StartPublishStreamToCSSResponse:
        """
        开始云端推流
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishStreamToCSS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishStreamToCSSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAndroidInstances(
            self,
            request: models.StopAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.StopAndroidInstancesResponse:
        """
        关机安卓实例
        """
        
        kwargs = {}
        kwargs["action"] = "StopAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAndroidInstancesApp(
            self,
            request: models.StopAndroidInstancesAppRequest,
            opts: Dict = None,
    ) -> models.StopAndroidInstancesAppResponse:
        """
        停止安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "StopAndroidInstancesApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAndroidInstancesAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopGame(
            self,
            request: models.StopGameRequest,
            opts: Dict = None,
    ) -> models.StopGameResponse:
        """
        强制退出游戏
        """
        
        kwargs = {}
        kwargs["action"] = "StopGame"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopGameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopPublishStream(
            self,
            request: models.StopPublishStreamRequest,
            opts: Dict = None,
    ) -> models.StopPublishStreamResponse:
        """
        停止云端推流
        """
        
        kwargs = {}
        kwargs["action"] = "StopPublishStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopPublishStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchGameArchive(
            self,
            request: models.SwitchGameArchiveRequest,
            opts: Dict = None,
    ) -> models.SwitchGameArchiveResponse:
        """
        切换游戏存档
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchGameArchive"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchGameArchiveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncAndroidInstanceImage(
            self,
            request: models.SyncAndroidInstanceImageRequest,
            opts: Dict = None,
    ) -> models.SyncAndroidInstanceImageResponse:
        """
        同步安卓实例镜像到其他区域，当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像已经同步完成处于可用状态。
        """
        
        kwargs = {}
        kwargs["action"] = "SyncAndroidInstanceImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncAndroidInstanceImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncExecuteCommandOnAndroidInstances(
            self,
            request: models.SyncExecuteCommandOnAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.SyncExecuteCommandOnAndroidInstancesResponse:
        """
        在安卓实例上同步执行命令，仅支持1秒内可以返回结果的命令，例如：ls、cd。同时执行的实例数量不能过多，否则可能云api返回超时。不支持超过1秒无法返回或无法自主结束的命令，例如：top、vim，执行结果最大1KB
        """
        
        kwargs = {}
        kwargs["action"] = "SyncExecuteCommandOnAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncExecuteCommandOnAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrylockWorker(
            self,
            request: models.TrylockWorkerRequest,
            opts: Dict = None,
    ) -> models.TrylockWorkerResponse:
        """
        尝试锁定机器
        """
        
        kwargs = {}
        kwargs["action"] = "TrylockWorker"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrylockWorkerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallAndroidInstancesApp(
            self,
            request: models.UninstallAndroidInstancesAppRequest,
            opts: Dict = None,
    ) -> models.UninstallAndroidInstancesAppResponse:
        """
        卸载安卓实例应用
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallAndroidInstancesApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallAndroidInstancesAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFileToAndroidInstances(
            self,
            request: models.UploadFileToAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.UploadFileToAndroidInstancesResponse:
        """
        将文件下载到指定实例列表的实例上，每个实例都会从公网下载文件。如果您需要将同一个文件分发到多个实例，建议使用 DistributeFileToAndroidInstances 接口减少公网下载的流量。如果您需要将不同的文件下载到不同的实例，可考虑使用 UploadFilesToAndroidInstances 接口批量将不同文件下载到不同的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFileToAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFileToAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadFilesToAndroidInstances(
            self,
            request: models.UploadFilesToAndroidInstancesRequest,
            opts: Dict = None,
    ) -> models.UploadFilesToAndroidInstancesResponse:
        """
        批量将不同的文件下载到不同的实例，每个实例下载文件都是从公网下载，建议只用在文件下载使用一次的场景。如果您需要将同一个文件分发到不同实例，建议使用 DistributeFileToAndroidInstances 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadFilesToAndroidInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadFilesToAndroidInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)