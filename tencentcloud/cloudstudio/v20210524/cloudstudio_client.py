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
from tencentcloud.cloudstudio.v20210524 import models


class CloudstudioClient(AbstractClient):
    _apiVersion = '2021-05-24'
    _endpoint = 'cloudstudio.tencentcloudapi.com'
    _service = 'cloudstudio'


    def CreateCustomizeTemplates(self, request):
        """添加自定义模板

        :param request: Request instance for CreateCustomizeTemplates.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.CreateCustomizeTemplatesRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.CreateCustomizeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomizeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomizeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWorkspaceByAgent(self, request):
        """云服务器方式创建工作空间

        :param request: Request instance for CreateWorkspaceByAgent.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.CreateWorkspaceByAgentRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.CreateWorkspaceByAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspaceByAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceByAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWorkspaceByTemplate(self, request):
        """快速开始, 基于模板创建工作空间

        :param request: Request instance for CreateWorkspaceByTemplate.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.CreateWorkspaceByTemplateRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.CreateWorkspaceByTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspaceByTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceByTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWorkspaceByVersionControl(self, request):
        """根据模板创建工作空间

        :param request: Request instance for CreateWorkspaceByVersionControl.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.CreateWorkspaceByVersionControlRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.CreateWorkspaceByVersionControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkspaceByVersionControl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkspaceByVersionControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCustomizeTemplatesById(self, request):
        """删除自定义模板

        :param request: Request instance for DeleteCustomizeTemplatesById.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DeleteCustomizeTemplatesByIdRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DeleteCustomizeTemplatesByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomizeTemplatesById", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomizeTemplatesByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomizeTemplates(self, request):
        """获取所有模板列表

        :param request: Request instance for DescribeCustomizeTemplates.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeCustomizeTemplatesRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeCustomizeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomizeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomizeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomizeTemplatesById(self, request):
        """获取特定模板信息

        :param request: Request instance for DescribeCustomizeTemplatesById.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeCustomizeTemplatesByIdRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeCustomizeTemplatesByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomizeTemplatesById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomizeTemplatesByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomizeTemplatesPresets(self, request):
        """获取创建模板的预置参数

        :param request: Request instance for DescribeCustomizeTemplatesPresets.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeCustomizeTemplatesPresetsRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeCustomizeTemplatesPresetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomizeTemplatesPresets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomizeTemplatesPresetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWorkspaceEnvList(self, request):
        """环境列表接口返回信息

        :param request: Request instance for DescribeWorkspaceEnvList.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceEnvListRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceEnvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceEnvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceEnvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWorkspaceNameExist(self, request):
        """检查工作空间是否存在

        :param request: Request instance for DescribeWorkspaceNameExist.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceNameExistRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceNameExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceNameExist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceNameExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWorkspaceStatus(self, request):
        """获取工作空间元信息

        :param request: Request instance for DescribeWorkspaceStatus.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceStatusRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWorkspaceStatusList(self, request):
        """获取用户工作空间列表

        :param request: Request instance for DescribeWorkspaceStatusList.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceStatusListRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.DescribeWorkspaceStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceStatusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceStatusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCustomizeTemplateVersionControl(self, request):
        """修改模板默认代码仓库

        :param request: Request instance for ModifyCustomizeTemplateVersionControl.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyCustomizeTemplateVersionControlRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyCustomizeTemplateVersionControlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomizeTemplateVersionControl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomizeTemplateVersionControlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCustomizeTemplatesFullById(self, request):
        """全量修改自定义模板，不忽略空

        :param request: Request instance for ModifyCustomizeTemplatesFullById.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyCustomizeTemplatesFullByIdRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyCustomizeTemplatesFullByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomizeTemplatesFullById", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomizeTemplatesFullByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCustomizeTemplatesPartById(self, request):
        """全量修改自定义模板，忽略空

        :param request: Request instance for ModifyCustomizeTemplatesPartById.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyCustomizeTemplatesPartByIdRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyCustomizeTemplatesPartByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomizeTemplatesPartById", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomizeTemplatesPartByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWorkspaceAttributes(self, request):
        """修改工作空间的名称和描述

        :param request: Request instance for ModifyWorkspaceAttributes.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyWorkspaceAttributesRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.ModifyWorkspaceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkspaceAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkspaceAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecoverWorkspace(self, request):
        """恢复工作空间

        :param request: Request instance for RecoverWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.RecoverWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.RecoverWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveWorkspace(self, request):
        """删除工作空间

        :param request: Request instance for RemoveWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.RemoveWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.RemoveWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunWorkspace(self, request):
        """运行空间

        :param request: Request instance for RunWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.RunWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.RunWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.RunWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopWorkspace(self, request):
        """停止运行空间

        :param request: Request instance for StopWorkspace.
        :type request: :class:`tencentcloud.cloudstudio.v20210524.models.StopWorkspaceRequest`
        :rtype: :class:`tencentcloud.cloudstudio.v20210524.models.StopWorkspaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopWorkspace", params, headers=headers)
            response = json.loads(body)
            model = models.StopWorkspaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)