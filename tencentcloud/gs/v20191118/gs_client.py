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
        """备份云手机到指定存储

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
        1. 排除和包含文件只能指定/data下的文件，不指定时复制整个/data目录
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


    def CreateAndroidInstanceImage(self, request):
        """创建安卓实例镜像

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
        """创建安卓实例

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
        """创建安卓实例 SSH 连接

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
        """创建安卓实例 WebShell 连接

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
        """创建安卓实例

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
        """查询安卓实例镜像

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
        """创建安卓实例

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


    def ModifyAndroidInstancesLabels(self, request):
        """修改安卓实例分辨率。需要注意的是该接口可能导致正在运行的应用出现闪退，所以建议在实例维护时期才进行调用。

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
        """启动安卓实例应用

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
        """指定存储还原云手机

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


    def StartAndroidInstances(self, request):
        """重启安卓实例

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
        """重启安卓实例

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
        """同步安卓实例镜像

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
        """上传文件到安卓实例

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