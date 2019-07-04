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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tsf.v20180326 import models


class TsfClient(AbstractClient):
    _apiVersion = '2018-03-26'
    _endpoint = 'tsf.tencentcloudapi.com'


    def AddInstances(self, request):
        """添加云主机节点至TSF集群

        :param request: 调用AddInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.AddInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApplication(self, request):
        """创建应用

        :param request: 调用CreateApplication所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCluster(self, request):
        """创建集群

        :param request: 调用CreateCluster所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateContainGroup(self, request):
        """创建容器部署组

        :param request: 调用CreateContainGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateContainGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateContainGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContainGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContainGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGroup(self, request):
        """创建容器部署组

        :param request: 调用CreateGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMicroservice(self, request):
        """新增微服务

        :param request: 调用CreateMicroservice所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMicroserviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNamespace(self, request):
        """创建命名空间

        :param request: 调用CreateNamespace所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApplication(self, request):
        """删除应用

        :param request: 调用DeleteApplication所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteContainerGroup(self, request):
        """删除容器部署组

        :param request: 调用DeleteContainerGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteContainerGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGroup(self, request):
        """删除容器部署组

        :param request: 调用DeleteGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteImageTags(self, request):
        """批量删除镜像版本

        :param request: 调用DeleteImageTags所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteImageTagsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteImageTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImageTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMicroservice(self, request):
        """删除微服务

        :param request: 调用DeleteMicroservice所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMicroserviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNamespace(self, request):
        """删除命名空间

        :param request: 调用DeleteNamespace所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNamespaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePkgs(self, request):
        """从软件仓库批量删除程序包。
        一次最多支持删除1000个包，数量超过1000，返回UpperDeleteLimit错误。

        :param request: 调用DeletePkgs所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeletePkgsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeletePkgsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePkgs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePkgsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeployContainerGroup(self, request):
        """部署容器应用

        :param request: 调用DeployContainerGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeployContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeployContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployContainerGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeployGroup(self, request):
        """部署虚拟机部署组应用

        :param request: 调用DeployGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeployGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeployGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplication(self, request):
        """获取应用详情

        :param request: 调用DescribeApplication所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationAttribute(self, request):
        """获取应用列表其它字段，如实例数量信息等

        :param request: 调用DescribeApplicationAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationAttributeRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplicationAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplications(self, request):
        """获取应用列表

        :param request: 调用DescribeApplications所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterInstances(self, request):
        """查询集群实例

        :param request: 调用DescribeClusterInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContainerGroupDetail(self, request):
        """容器部署组详情

        :param request: 调用DescribeContainerGroupDetail所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerGroupDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerGroupDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContainerGroups(self, request):
        """容器部署组列表

        :param request: 调用DescribeContainerGroups所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDownloadInfo(self, request):
        """TSF上传的程序包存放在腾讯云对象存储（COS）中，通过该API可以获取从COS下载程序包需要的信息，包括包所在的桶、存储路径、鉴权信息等，之后使用COS API（或SDK）进行下载。
        COS相关文档请查阅：https://cloud.tencent.com/document/product/436

        :param request: 调用DescribeDownloadInfo所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeDownloadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeDownloadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDownloadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDownloadInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroup(self, request):
        """查询虚拟机部署组详情

        :param request: 调用DescribeGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupInstances(self, request):
        """查询虚拟机部署组云主机列表

        :param request: 调用DescribeGroupInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroups(self, request):
        """获取虚拟机部署组列表

        :param request: 调用DescribeGroups所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageTags(self, request):
        """镜像版本列表

        :param request: 调用DescribeImageTags所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeImageTagsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeImageTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMicroservice(self, request):
        """查询微服务详情

        :param request: 调用DescribeMicroservice所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMicroserviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMicroservices(self, request):
        """获取微服务列表

        :param request: 调用DescribeMicroservices所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroservicesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroservicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMicroservices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMicroservicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePkgs(self, request):
        """无

        :param request: 调用DescribePkgs所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePkgsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePkgsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePkgs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePkgsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSimpleApplications(self, request):
        """查询简单应用列表

        :param request: 调用DescribeSimpleApplications所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleApplicationsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleApplicationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleApplicationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSimpleClusters(self, request):
        """查询简单集群列表

        :param request: 调用DescribeSimpleClusters所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleClustersRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleClusters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleClustersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSimpleGroups(self, request):
        """查询简单部署组列表

        :param request: 调用DescribeSimpleGroups所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSimpleNamespaces(self, request):
        """查询简单命名空间列表

        :param request: 调用DescribeSimpleNamespaces所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleNamespacesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUploadInfo(self, request):
        """TSF会将软件包上传到腾讯云对象存储（COS）。调用此接口获取上传信息，如目标地域，桶，包Id，存储路径，鉴权信息等，之后请使用COS API（或SDK）进行上传。
        COS相关文档请查阅：https://cloud.tencent.com/document/product/436

        :param request: 调用DescribeUploadInfo所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUploadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUploadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUploadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUploadInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExpandGroup(self, request):
        """虚拟机部署组添加实例

        :param request: 调用ExpandGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.ExpandGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ExpandGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExpandGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExpandGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyContainerGroup(self, request):
        """修改容器部署组

        :param request: 调用ModifyContainerGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContainerGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyContainerReplicas(self, request):
        """修改容器部署组实例数

        :param request: 调用ModifyContainerReplicas所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerReplicasRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerReplicasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContainerReplicas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContainerReplicasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMicroservice(self, request):
        """修改微服务详情

        :param request: 调用ModifyMicroservice所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMicroserviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUploadInfo(self, request):
        """调用该接口和COS的上传接口后，需要调用此接口更新TSF中保存的程序包状态。
        调用此接口完成后，才标志上传包流程结束。

        :param request: 调用ModifyUploadInfo所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyUploadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyUploadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUploadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUploadInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveInstances(self, request):
        """从 TSF 集群中批量移除云主机节点

        :param request: 调用RemoveInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.RemoveInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ShrinkGroup(self, request):
        """下线部署组所有机器实例

        :param request: 调用ShrinkGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.ShrinkGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ShrinkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShrinkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShrinkGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ShrinkInstances(self, request):
        """虚拟机部署组下线实例

        :param request: 调用ShrinkInstances所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.ShrinkInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ShrinkInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShrinkInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShrinkInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartContainerGroup(self, request):
        """启动容器部署组

        :param request: 调用StartContainerGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.StartContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StartContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartContainerGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartGroup(self, request):
        """启动分组

        :param request: 调用StartGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.StartGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StartGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopContainerGroup(self, request):
        """停止容器部署组

        :param request: 调用StopContainerGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopContainerGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopGroup(self, request):
        """停止虚拟机部署组

        :param request: 调用StopGroup所需参数的结构体。
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)