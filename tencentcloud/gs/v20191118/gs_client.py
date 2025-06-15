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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.gs.v20191118 import models


class GsClient(AbstractClient):
    _apiVersion = '2019-11-18'
    _endpoint = 'gs.tencentcloudapi.com'
    _service = 'gs'


    def BackUpAndroidInstanceToStorage(self, request):
        """备份云手机数据到指定存储，支持 COS 和兼容 AWS S3 协议的对象存储服务。如果是备份到 COS 时，会使用公网流量，授权 COS bucket 请在控制台中操作。

        :param request: Request instance for BackUpAndroidInstanceToStorage.
        :type request: :class:`tencentcloud.gs.v20191118.models.BackUpAndroidInstanceToStorageRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.BackUpAndroidInstanceToStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BackUpAndroidInstanceToStorage", params, headers=headers)
            response = json.loads(body)
            model = models.BackUpAndroidInstanceToStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CleanAndroidInstancesAppData(self, request):
        """批量清理安卓实例应用数据

        :param request: Request instance for CleanAndroidInstancesAppData.
        :type request: :class:`tencentcloud.gs.v20191118.models.CleanAndroidInstancesAppDataRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CleanAndroidInstancesAppDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CleanAndroidInstancesAppData", params, headers=headers)
            response = json.loads(body)
            model = models.CleanAndroidInstancesAppDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConnectAndroidInstance(self, request):
        """连接安卓实例

        :param request: Request instance for ConnectAndroidInstance.
        :type request: :class:`tencentcloud.gs.v20191118.models.ConnectAndroidInstanceRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ConnectAndroidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConnectAndroidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ConnectAndroidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyAndroidInstance(self, request):
        """复制安卓实例：
        1. 排除和包含文件只能指定 /data 下的文件，不指定时复制整个 /data 目录
        2. 源实例和目的实例必须在同一区域
        3. 复制时，源实例和目的实例都会停机，复制完后实例会自动启动
        4. 复制时会产生大量内网流量，请限制并发

        :param request: Request instance for CopyAndroidInstance.
        :type request: :class:`tencentcloud.gs.v20191118.models.CopyAndroidInstanceRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CopyAndroidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyAndroidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CopyAndroidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidApp(self, request):
        """创建安卓应用

        :param request: Request instance for CreateAndroidApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidAppVersion(self, request):
        """创建安卓应用版本

        :param request: Request instance for CreateAndroidAppVersion.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidAppVersionRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidAppVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidAppVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidAppVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstanceADB(self, request):
        """创建云手机实例 ADB 连接信息，请将返回结果的 PrivateKey 字段保存为 pem 文件，并将 pem 文件权限设置为 600，再参考返回结果的 ConnectCommand 使用 adb 连接实例。

        :param request: Request instance for CreateAndroidInstanceADB.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceADBRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceADBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstanceADB", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstanceADBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstanceImage(self, request):
        """使用指定的安卓实例创建镜像，创建镜像时指定的实例会关机，镜像创建完成后实例会自动开机。当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像创建完成处于可用状态。

        :param request: Request instance for CreateAndroidInstanceImage.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceImageRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstanceImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstanceImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstanceLabel(self, request):
        """创建安卓实例标签

        :param request: Request instance for CreateAndroidInstanceLabel.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceLabelRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstanceLabel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstanceLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstanceSSH(self, request):
        """创建安卓实例 SSH 连接信息，请将返回结果的 PrivateKey 字段保存为 pem 文件，并将 pem 文件权限设置为 600，再参考返回结果的 ConnectCommand 使用 ssh 连接实例。

        :param request: Request instance for CreateAndroidInstanceSSH.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceSSHRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceSSHResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstanceSSH", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstanceSSHResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstanceWebShell(self, request):
        """创建安卓实例 WebShell 连接信息，返回的 ConnectUrl 可通过浏览器直接打开访问，链接有效期 1 小时，链接打开后可持续使用。

        :param request: Request instance for CreateAndroidInstanceWebShell.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceWebShellRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstanceWebShellResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstanceWebShell", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstanceWebShellResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstances(self, request):
        """创建安卓实例

        :param request: Request instance for CreateAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstancesAccessToken(self, request):
        """创建安卓实例访问Token

        :param request: Request instance for CreateAndroidInstancesAccessToken.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstancesAccessTokenRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstancesAccessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstancesAccessToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstancesAccessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndroidInstancesScreenshot(self, request):
        """安卓实例截图

        :param request: Request instance for CreateAndroidInstancesScreenshot.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstancesScreenshotRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateAndroidInstancesScreenshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndroidInstancesScreenshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndroidInstancesScreenshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosCredential(self, request):
        """用于创建 Cos 临时密钥

        :param request: Request instance for CreateCosCredential.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateCosCredentialRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateCosCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosCredential", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSession(self, request):
        """创建会话

        :param request: Request instance for CreateSession.
        :type request: :class:`tencentcloud.gs.v20191118.models.CreateSessionRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.CreateSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAndroidApp(self, request):
        """删除安卓应用

        :param request: Request instance for DeleteAndroidApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAndroidApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAndroidAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAndroidAppVersion(self, request):
        """删除安卓应用版本

        :param request: Request instance for DeleteAndroidAppVersion.
        :type request: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidAppVersionRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidAppVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAndroidAppVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAndroidAppVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAndroidInstanceBackupFiles(self, request):
        """删除安卓实例备份文件

        :param request: Request instance for DeleteAndroidInstanceBackupFiles.
        :type request: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidInstanceBackupFilesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidInstanceBackupFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAndroidInstanceBackupFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAndroidInstanceBackupFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAndroidInstanceImages(self, request):
        """删除安卓实例镜像

        :param request: Request instance for DeleteAndroidInstanceImages.
        :type request: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidInstanceImagesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidInstanceImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAndroidInstanceImages", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAndroidInstanceImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAndroidInstanceLabel(self, request):
        """删除安卓实例标签

        :param request: Request instance for DeleteAndroidInstanceLabel.
        :type request: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidInstanceLabelRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DeleteAndroidInstanceLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAndroidInstanceLabel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAndroidInstanceLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidApps(self, request):
        """查询安卓应用信息

        :param request: Request instance for DescribeAndroidApps.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidAppsRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidApps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidInstanceApps(self, request):
        """查询安卓实例应用

        :param request: Request instance for DescribeAndroidInstanceApps.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceAppsRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidInstanceApps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidInstanceAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidInstanceImages(self, request):
        """查询安卓实例镜像信息，当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像处于可用状态。

        :param request: Request instance for DescribeAndroidInstanceImages.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceImagesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidInstanceImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidInstanceImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidInstanceLabels(self, request):
        """查询安卓实例标签

        :param request: Request instance for DescribeAndroidInstanceLabels.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceLabelsRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceLabelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidInstanceLabels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidInstanceLabelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidInstanceTasksStatus(self, request):
        """查询安卓实例任务状态

        :param request: Request instance for DescribeAndroidInstanceTasksStatus.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceTasksStatusRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstanceTasksStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidInstanceTasksStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidInstanceTasksStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidInstances(self, request):
        """查询安卓实例

        :param request: Request instance for DescribeAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidInstancesAppBlacklist(self, request):
        """查询安卓实例黑名单

        :param request: Request instance for DescribeAndroidInstancesAppBlacklist.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstancesAppBlacklistRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstancesAppBlacklistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidInstancesAppBlacklist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidInstancesAppBlacklistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAndroidInstancesByApps(self, request):
        """查询安装指定应用的安卓实例

        :param request: Request instance for DescribeAndroidInstancesByApps.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstancesByAppsRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeAndroidInstancesByAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAndroidInstancesByApps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAndroidInstancesByAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesCount(self, request):
        """获取并发总数和运行数

        :param request: Request instance for DescribeInstancesCount.
        :type request: :class:`tencentcloud.gs.v20191118.models.DescribeInstancesCountRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DescribeInstancesCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyAndroidInstances(self, request):
        """销毁安卓实例

        :param request: Request instance for DestroyAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.DestroyAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DestroyAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableAndroidInstancesApp(self, request):
        """批量禁用安卓实例应用

        :param request: Request instance for DisableAndroidInstancesApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.DisableAndroidInstancesAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DisableAndroidInstancesAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableAndroidInstancesApp", params, headers=headers)
            response = json.loads(body)
            model = models.DisableAndroidInstancesAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DistributeFileToAndroidInstances(self, request):
        """将一个文件批量分发到多个实例，一次接口调用触发一次文件分发，一次文件分发只会从公网下载一次，然后文件会走内网分发到实例列表中的实例。

        :param request: Request instance for DistributeFileToAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.DistributeFileToAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DistributeFileToAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributeFileToAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DistributeFileToAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DistributePhotoToAndroidInstances(self, request):
        """将一张照片批量分发到多个实例的相册中，一次接口调用触发一次照片分发，一次照片分发只会从公网下载一次，然后照片会走内网分发到实例列表中的实例。

        :param request: Request instance for DistributePhotoToAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.DistributePhotoToAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.DistributePhotoToAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DistributePhotoToAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DistributePhotoToAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableAndroidInstancesApp(self, request):
        """批量启用安卓实例应用

        :param request: Request instance for EnableAndroidInstancesApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.EnableAndroidInstancesAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.EnableAndroidInstancesAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableAndroidInstancesApp", params, headers=headers)
            response = json.loads(body)
            model = models.EnableAndroidInstancesAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteCommandOnAndroidInstances(self, request):
        """在安卓实例上异步执行命令，命令输出结果如果内容过长会被截断

        :param request: Request instance for ExecuteCommandOnAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.ExecuteCommandOnAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ExecuteCommandOnAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteCommandOnAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteCommandOnAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchAndroidInstancesLogs(self, request):
        """批量将实例的 logcat 日志文件上传到您已授权的 COS bucket 中，授权 COS bucket 请在控制台中操作。

        :param request: Request instance for FetchAndroidInstancesLogs.
        :type request: :class:`tencentcloud.gs.v20191118.models.FetchAndroidInstancesLogsRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.FetchAndroidInstancesLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchAndroidInstancesLogs", params, headers=headers)
            response = json.loads(body)
            model = models.FetchAndroidInstancesLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportAndroidInstanceImage(self, request):
        """导入安卓实例镜像，当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像导入完成处于可用状态。

        :param request: Request instance for ImportAndroidInstanceImage.
        :type request: :class:`tencentcloud.gs.v20191118.models.ImportAndroidInstanceImageRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ImportAndroidInstanceImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportAndroidInstanceImage", params, headers=headers)
            response = json.loads(body)
            model = models.ImportAndroidInstanceImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallAndroidInstancesApp(self, request):
        """安装安卓实例应用

        :param request: Request instance for InstallAndroidInstancesApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.InstallAndroidInstancesAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.InstallAndroidInstancesAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallAndroidInstancesApp", params, headers=headers)
            response = json.loads(body)
            model = models.InstallAndroidInstancesAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallAndroidInstancesAppWithURL(self, request):
        """通过 URL 安装安卓实例应用

        :param request: Request instance for InstallAndroidInstancesAppWithURL.
        :type request: :class:`tencentcloud.gs.v20191118.models.InstallAndroidInstancesAppWithURLRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.InstallAndroidInstancesAppWithURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallAndroidInstancesAppWithURL", params, headers=headers)
            response = json.loads(body)
            model = models.InstallAndroidInstancesAppWithURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidApp(self, request):
        """修改安卓应用信息

        :param request: Request instance for ModifyAndroidApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidAppVersion(self, request):
        """修改安卓应用版本

        :param request: Request instance for ModifyAndroidAppVersion.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidAppVersionRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidAppVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidAppVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidAppVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstanceInformation(self, request):
        """修改安卓实例的信息

        :param request: Request instance for ModifyAndroidInstanceInformation.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstanceInformationRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstanceInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstanceInformation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstanceInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstanceResolution(self, request):
        """修改安卓实例分辨率。需要注意的是该接口可能导致正在运行的应用出现闪退，所以建议在实例维护时期才进行调用。

        :param request: Request instance for ModifyAndroidInstanceResolution.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstanceResolutionRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstanceResolutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstanceResolution", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstanceResolutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstancesAppBlacklist(self, request):
        """修改安卓实例应用黑名单

        :param request: Request instance for ModifyAndroidInstancesAppBlacklist.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesAppBlacklistRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesAppBlacklistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstancesAppBlacklist", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstancesAppBlacklistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstancesInformation(self, request):
        """批量修改安卓实例信息

        :param request: Request instance for ModifyAndroidInstancesInformation.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesInformationRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstancesInformation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstancesInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstancesLabels(self, request):
        """批量修改安卓实例的标签

        :param request: Request instance for ModifyAndroidInstancesLabels.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesLabelsRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesLabelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstancesLabels", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstancesLabelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstancesProperties(self, request):
        """批量修改安卓实例属性

        :param request: Request instance for ModifyAndroidInstancesProperties.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesPropertiesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesPropertiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstancesProperties", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstancesPropertiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstancesResolution(self, request):
        """修改安卓实例分辨率。需要注意的是该接口需要重启才能生效。

        :param request: Request instance for ModifyAndroidInstancesResolution.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesResolutionRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesResolutionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstancesResolution", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstancesResolutionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstancesResources(self, request):
        """批量修改安卓实例资源限制

        :param request: Request instance for ModifyAndroidInstancesResources.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesResourcesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstancesResources", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstancesResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAndroidInstancesUserId(self, request):
        """批量修改安卓实例的用户ID

        :param request: Request instance for ModifyAndroidInstancesUserId.
        :type request: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesUserIdRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ModifyAndroidInstancesUserIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAndroidInstancesUserId", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAndroidInstancesUserIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootAndroidInstanceHosts(self, request):
        """重启安卓实例宿主机。请注意：

        - 当前每 15 分钟只能重启一次
        - 一个宿主机可能有多个云手机实例，重启宿主机会影响运行在上面的所有实例，请确保该宿主机上的所有云手机实例未投入业务使用

        :param request: Request instance for RebootAndroidInstanceHosts.
        :type request: :class:`tencentcloud.gs.v20191118.models.RebootAndroidInstanceHostsRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.RebootAndroidInstanceHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootAndroidInstanceHosts", params, headers=headers)
            response = json.loads(body)
            model = models.RebootAndroidInstanceHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootAndroidInstances(self, request):
        """重启安卓实例

        :param request: Request instance for RebootAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.RebootAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.RebootAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RebootAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewAndroidInstancesAccessToken(self, request):
        """续期安卓实例访问Token

        :param request: Request instance for RenewAndroidInstancesAccessToken.
        :type request: :class:`tencentcloud.gs.v20191118.models.RenewAndroidInstancesAccessTokenRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.RenewAndroidInstancesAccessTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewAndroidInstancesAccessToken", params, headers=headers)
            response = json.loads(body)
            model = models.RenewAndroidInstancesAccessTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAndroidInstances(self, request):
        """重置安卓实例

        :param request: Request instance for ResetAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.ResetAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.ResetAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartAndroidInstancesApp(self, request):
        """重启安卓实例应用

        :param request: Request instance for RestartAndroidInstancesApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.RestartAndroidInstancesAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.RestartAndroidInstancesAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartAndroidInstancesApp", params, headers=headers)
            response = json.loads(body)
            model = models.RestartAndroidInstancesAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreAndroidInstanceFromStorage(self, request):
        """使用指定存储数据还原云手机，支持 COS 和兼容 AWS S3 协议的对象存储服务。如果还原数据来自 COS 时，会使用公网流量，授权 COS bucket 请在控制台中操作。

        :param request: Request instance for RestoreAndroidInstanceFromStorage.
        :type request: :class:`tencentcloud.gs.v20191118.models.RestoreAndroidInstanceFromStorageRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.RestoreAndroidInstanceFromStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreAndroidInstanceFromStorage", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreAndroidInstanceFromStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SaveGameArchive(self, request):
        """保存游戏存档

        :param request: Request instance for SaveGameArchive.
        :type request: :class:`tencentcloud.gs.v20191118.models.SaveGameArchiveRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.SaveGameArchiveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveGameArchive", params, headers=headers)
            response = json.loads(body)
            model = models.SaveGameArchiveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAndroidInstancesBGAppKeepAlive(self, request):
        """批量设置安卓实例应用后台保活，开启应用保活，只是降低应用被杀死或回收的优先级，并不能保证应用不会被杀死或回收（如出现内存不足等资源限制时，应用也有概率被杀死或回收）

        :param request: Request instance for SetAndroidInstancesBGAppKeepAlive.
        :type request: :class:`tencentcloud.gs.v20191118.models.SetAndroidInstancesBGAppKeepAliveRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.SetAndroidInstancesBGAppKeepAliveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAndroidInstancesBGAppKeepAlive", params, headers=headers)
            response = json.loads(body)
            model = models.SetAndroidInstancesBGAppKeepAliveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAndroidInstancesFGAppKeepAlive(self, request):
        """批量设置安卓实例应用前台保活，开启应用保活，只是降低应用被杀死或回收的优先级，并不能保证应用不会被杀死或回收（如出现内存不足等资源限制时，应用也有概率被杀死或回收）

        :param request: Request instance for SetAndroidInstancesFGAppKeepAlive.
        :type request: :class:`tencentcloud.gs.v20191118.models.SetAndroidInstancesFGAppKeepAliveRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.SetAndroidInstancesFGAppKeepAliveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAndroidInstancesFGAppKeepAlive", params, headers=headers)
            response = json.loads(body)
            model = models.SetAndroidInstancesFGAppKeepAliveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAndroidInstances(self, request):
        """开机安卓实例

        :param request: Request instance for StartAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.StartAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StartAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAndroidInstancesApp(self, request):
        """启动安卓实例应用

        :param request: Request instance for StartAndroidInstancesApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.StartAndroidInstancesAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StartAndroidInstancesAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAndroidInstancesApp", params, headers=headers)
            response = json.loads(body)
            model = models.StartAndroidInstancesAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishStream(self, request):
        """开始云端推流

        :param request: Request instance for StartPublishStream.
        :type request: :class:`tencentcloud.gs.v20191118.models.StartPublishStreamRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StartPublishStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishStream", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishStreamToCSS(self, request):
        """开始云端推流

        :param request: Request instance for StartPublishStreamToCSS.
        :type request: :class:`tencentcloud.gs.v20191118.models.StartPublishStreamToCSSRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StartPublishStreamToCSSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishStreamToCSS", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishStreamToCSSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAndroidInstances(self, request):
        """关机安卓实例

        :param request: Request instance for StopAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.StopAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StopAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAndroidInstancesApp(self, request):
        """停止安卓实例应用

        :param request: Request instance for StopAndroidInstancesApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.StopAndroidInstancesAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StopAndroidInstancesAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAndroidInstancesApp", params, headers=headers)
            response = json.loads(body)
            model = models.StopAndroidInstancesAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopGame(self, request):
        """强制退出游戏

        :param request: Request instance for StopGame.
        :type request: :class:`tencentcloud.gs.v20191118.models.StopGameRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StopGameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopGame", params, headers=headers)
            response = json.loads(body)
            model = models.StopGameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPublishStream(self, request):
        """停止云端推流

        :param request: Request instance for StopPublishStream.
        :type request: :class:`tencentcloud.gs.v20191118.models.StopPublishStreamRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.StopPublishStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPublishStream", params, headers=headers)
            response = json.loads(body)
            model = models.StopPublishStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchGameArchive(self, request):
        """切换游戏存档

        :param request: Request instance for SwitchGameArchive.
        :type request: :class:`tencentcloud.gs.v20191118.models.SwitchGameArchiveRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.SwitchGameArchiveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchGameArchive", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchGameArchiveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncAndroidInstanceImage(self, request):
        """同步安卓实例镜像到其他区域，当镜像的 AndroidInstanceImageState 为 NORMAL 时，镜像已经同步完成处于可用状态。

        :param request: Request instance for SyncAndroidInstanceImage.
        :type request: :class:`tencentcloud.gs.v20191118.models.SyncAndroidInstanceImageRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.SyncAndroidInstanceImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncAndroidInstanceImage", params, headers=headers)
            response = json.loads(body)
            model = models.SyncAndroidInstanceImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncExecuteCommandOnAndroidInstances(self, request):
        """在安卓实例上同步执行命令，仅支持1秒内可以返回结果的命令，例如：ls、cd。同时执行的实例数量不能过多，否则可能云api返回超时。不支持超过1秒无法返回或无法自主结束的命令，例如：top、vim，执行结果最大1KB

        :param request: Request instance for SyncExecuteCommandOnAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.SyncExecuteCommandOnAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.SyncExecuteCommandOnAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncExecuteCommandOnAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.SyncExecuteCommandOnAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TrylockWorker(self, request):
        """尝试锁定机器

        :param request: Request instance for TrylockWorker.
        :type request: :class:`tencentcloud.gs.v20191118.models.TrylockWorkerRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.TrylockWorkerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrylockWorker", params, headers=headers)
            response = json.loads(body)
            model = models.TrylockWorkerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UninstallAndroidInstancesApp(self, request):
        """卸载安卓实例应用

        :param request: Request instance for UninstallAndroidInstancesApp.
        :type request: :class:`tencentcloud.gs.v20191118.models.UninstallAndroidInstancesAppRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.UninstallAndroidInstancesAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallAndroidInstancesApp", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallAndroidInstancesAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadFileToAndroidInstances(self, request):
        """将文件下载到指定实例列表的实例上，每个实例都会从公网下载文件。如果您需要将同一个文件分发到多个实例，建议使用 DistributeFileToAndroidInstances 接口减少公网下载的流量。如果您需要将不同的文件下载到不同的实例，可考虑使用 UploadFilesToAndroidInstances 接口批量将不同文件下载到不同的实例。

        :param request: Request instance for UploadFileToAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.UploadFileToAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.UploadFileToAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFileToAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFileToAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadFilesToAndroidInstances(self, request):
        """批量将不同的文件下载到不同的实例，每个实例下载文件都是从公网下载，建议只用在文件下载使用一次的场景。如果您需要将同一个文件分发到不同实例，建议使用 DistributeFileToAndroidInstances 接口。

        :param request: Request instance for UploadFilesToAndroidInstances.
        :type request: :class:`tencentcloud.gs.v20191118.models.UploadFilesToAndroidInstancesRequest`
        :rtype: :class:`tencentcloud.gs.v20191118.models.UploadFilesToAndroidInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFilesToAndroidInstances", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFilesToAndroidInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))