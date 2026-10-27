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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cvd.v20201104 import models


class CvdClient(AbstractClient):
    _apiVersion = '2020-11-04'
    _endpoint = 'cvd.tencentcloudapi.com'
    _service = 'cvd'


    def AssociateSecurityGroup(self, request):
        r"""安全组批量关联云桌面

        :param request: Request instance for AssociateSecurityGroup.
        :type request: :class:`tencentcloud.cvd.v20201104.models.AssociateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.AssociateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindInstances(self, request):
        r"""绑定桌面

        :param request: Request instance for BindInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.BindInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.BindInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BindInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCommandTask(self, request):
        r"""创建批量脚本任务

        :param request: Request instance for CreateCommandTask.
        :type request: :class:`tencentcloud.cvd.v20201104.models.CreateCommandTaskRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.CreateCommandTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCommandTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCommandTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataDisk(self, request):
        r"""实例新增数据盘

        :param request: Request instance for CreateDataDisk.
        :type request: :class:`tencentcloud.cvd.v20201104.models.CreateDataDiskRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.CreateDataDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataDisk", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainControlPolicy(self, request):
        r"""新建域名访问控制策略

        :param request: Request instance for CreateDomainControlPolicy.
        :type request: :class:`tencentcloud.cvd.v20201104.models.CreateDomainControlPolicyRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.CreateDomainControlPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainControlPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainControlPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImage(self, request):
        r"""创建自定义镜像。

        :param request: Request instance for CreateImage.
        :type request: :class:`tencentcloud.cvd.v20201104.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstances(self, request):
        r"""创建云桌面实例

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePolicy(self, request):
        r"""创建策略

        :param request: Request instance for CreatePolicy.
        :type request: :class:`tencentcloud.cvd.v20201104.models.CreatePolicyRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.CreatePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCommandTasks(self, request):
        r"""删除命令任务

        :param request: Request instance for DeleteCommandTasks.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DeleteCommandTasksRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DeleteCommandTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCommandTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCommandTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainControlPolicy(self, request):
        r"""删除域名访问控制策略

        :param request: Request instance for DeleteDomainControlPolicy.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DeleteDomainControlPolicyRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DeleteDomainControlPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainControlPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainControlPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImages(self, request):
        r"""用于删除一个或多个自定义镜像。单次最大删除5个。

        :param request: Request instance for DeleteImages.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DeleteImagesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DeleteImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImages", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCommandTasks(self, request):
        r"""拉取命令任务详情

        :param request: Request instance for DescribeCommandTasks.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeCommandTasksRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeCommandTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCommandTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCommandTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImages(self, request):
        r"""获取云桌面镜像详细信息

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceFetchMsg(self, request):
        r"""获取指定实例的登录Fetch信息

        :param request: Request instance for DescribeInstanceFetchMsg.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceFetchMsgRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceFetchMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceFetchMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceFetchMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceGraphData(self, request):
        r"""获取实例磁盘分区监控数据

        :param request: Request instance for DescribeInstanceGraphData.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceGraphDataRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceGraphDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceGraphData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceGraphDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLoginMsg(self, request):
        r"""获取指定实例的登录login信息

        :param request: Request instance for DescribeInstanceLoginMsg.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceLoginMsgRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceLoginMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLoginMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLoginMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceMonitorData(self, request):
        r"""查询实例监控数据

        :param request: Request instance for DescribeInstanceMonitorData.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceMonitorDataRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceMonitorData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceMonitorDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceRegionDistribution(self, request):
        r"""获取用户在各个区域云桌面实例个数

        :param request: Request instance for DescribeInstanceRegionDistribution.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceRegionDistributionRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstanceRegionDistributionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceRegionDistribution", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceRegionDistributionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        r"""获取云桌面实例详细信息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesBindStatus(self, request):
        r"""获取桌面实例绑定状态

        :param request: Request instance for DescribeInstancesBindStatus.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstancesBindStatusRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstancesBindStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesBindStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesBindStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesStatus(self, request):
        r"""获取桌面实例状态

        :param request: Request instance for DescribeInstancesStatus.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInstancesStatusRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInstancesStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocationDetail(self, request):
        r"""查询脚本任务执行的详细情况。

        :param request: Request instance for DescribeInvocationDetail.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInvocationDetailRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInvocationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInvocations(self, request):
        r"""查询指定云桌面上的任务列表。

        :param request: Request instance for DescribeInvocations.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeInvocationsRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeInvocationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInvocationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePolicyDetail(self, request):
        r"""拉取租户策略列表

        :param request: Request instance for DescribePolicyDetail.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribePolicyDetailRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribePolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePolicyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroups(self, request):
        r"""拉取云桌面关联的安全组信息

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshots(self, request):
        r"""拉取快照列表

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsage(self, request):
        r"""拉取实例使用时长详情

        :param request: Request instance for DescribeUsage.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeUsageRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsers(self, request):
        r"""拉取用户列表

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DescribeUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroup(self, request):
        r"""安全组批量解关联云桌面

        :param request: Request instance for DisassociateSecurityGroup.
        :type request: :class:`tencentcloud.cvd.v20201104.models.DisassociateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.DisassociateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDiskConfiguration(self, request):
        r"""实例硬盘扩容

        :param request: Request instance for ModifyDiskConfiguration.
        :type request: :class:`tencentcloud.cvd.v20201104.models.ModifyDiskConfigurationRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ModifyDiskConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiskConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDiskConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageAttrs(self, request):
        r"""修改镜像属性

        :param request: Request instance for ModifyImageAttrs.
        :type request: :class:`tencentcloud.cvd.v20201104.models.ModifyImageAttrsRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ModifyImageAttrsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageAttrs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageAttrsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceBasicAttribute(self, request):
        r"""修改桌面实例属性

        :param request: Request instance for ModifyInstanceBasicAttribute.
        :type request: :class:`tencentcloud.cvd.v20201104.models.ModifyInstanceBasicAttributeRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ModifyInstanceBasicAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceBasicAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceBasicAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesType(self, request):
        r"""调整实例机型配置

        :param request: Request instance for ModifyInstancesType.
        :type request: :class:`tencentcloud.cvd.v20201104.models.ModifyInstancesTypeRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ModifyInstancesTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesVpc(self, request):
        r"""调整实例私有网络

        :param request: Request instance for ModifyInstancesVpc.
        :type request: :class:`tencentcloud.cvd.v20201104.models.ModifyInstancesVpcRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ModifyInstancesVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesVpc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootInstances(self, request):
        r"""重启实例

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RebootInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveDataDisks(self, request):
        r"""卸载实例数据盘

        :param request: Request instance for RemoveDataDisks.
        :type request: :class:`tencentcloud.cvd.v20201104.models.RemoveDataDisksRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.RemoveDataDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveDataDisks", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveDataDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemovePolicy(self, request):
        r"""删除策略

        :param request: Request instance for RemovePolicy.
        :type request: :class:`tencentcloud.cvd.v20201104.models.RemovePolicyRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.RemovePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemovePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.RemovePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstances(self, request):
        r"""实例续费

        :param request: Request instance for RenewInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.RenewInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.RenewInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstances(self, request):
        r"""实例重置

        :param request: Request instance for ResetInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.ResetInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.ResetInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunCommand(self, request):
        r"""在指定的云桌面实例上执行脚本任务。

        :param request: Request instance for RunCommand.
        :type request: :class:`tencentcloud.cvd.v20201104.models.RunCommandRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.RunCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunCommand", params, headers=headers)
            response = json.loads(body)
            model = models.RunCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartInstances(self, request):
        r"""开启实例

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCommandTasks(self, request):
        r"""停止命令任务

        :param request: Request instance for StopCommandTasks.
        :type request: :class:`tencentcloud.cvd.v20201104.models.StopCommandTasksRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.StopCommandTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCommandTasks", params, headers=headers)
            response = json.loads(body)
            model = models.StopCommandTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInstances(self, request):
        r"""关闭实例

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInvocation(self, request):
        r"""停止脚本任务的执行。

        :param request: Request instance for StopInvocation.
        :type request: :class:`tencentcloud.cvd.v20201104.models.StopInvocationRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.StopInvocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInvocation", params, headers=headers)
            response = json.loads(body)
            model = models.StopInvocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSession(self, request):
        r"""注销或者断开机器当前会话

        :param request: Request instance for StopSession.
        :type request: :class:`tencentcloud.cvd.v20201104.models.StopSessionRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.StopSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSession", params, headers=headers)
            response = json.loads(body)
            model = models.StopSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstances(self, request):
        r"""主动退还、销毁退还实例。
        <li>包年包月实例首次调用本接口，且参数DestroyImmediately为false时，实例进入隔离期，再次调用本接口，实例将被销毁，且不可恢复。</li>
        <li>包年包月实例，如果参数DestroyImmediately为true来调用此接口，则实例将被直接销毁，且不可恢复。</li>
        <li>按量计费实例调用本接口将被直接销毁，且不可恢复。</li>

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindInstances(self, request):
        r"""解除用户和机器绑定关系

        :param request: Request instance for UnbindInstances.
        :type request: :class:`tencentcloud.cvd.v20201104.models.UnbindInstancesRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.UnbindInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindInstances", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePolicy(self, request):
        r"""更新策略

        :param request: Request instance for UpdatePolicy.
        :type request: :class:`tencentcloud.cvd.v20201104.models.UpdatePolicyRequest`
        :rtype: :class:`tencentcloud.cvd.v20201104.models.UpdatePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))