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
from tencentcloud.tcbr.v20220217 import models


class TcbrClient(AbstractClient):
    _apiVersion = '2022-02-17'
    _endpoint = 'tcbr.tencentcloudapi.com'
    _service = 'tcbr'


    def CreateCloudRunEnv(self, request):
        r"""创建云托管环境，并开通资源。

        :param request: Request instance for CreateCloudRunEnv.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunEnvRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudRunEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudRunEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudRunServer(self, request):
        r"""创建云托管服务接口

        :param request: Request instance for CreateCloudRunServer.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunServerRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.CreateCloudRunServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudRunServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudRunServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudRunServer(self, request):
        r"""删除云托管服务：包括服务下的版本，镜像，流水线

        :param request: Request instance for DeleteCloudRunServer.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DeleteCloudRunServerRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DeleteCloudRunServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudRunServer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudRunServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudRunVersions(self, request):
        r"""批量删除版本

        :param request: Request instance for DeleteCloudRunVersions.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DeleteCloudRunVersionsRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DeleteCloudRunVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudRunVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudRunVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRunDeployRecord(self, request):
        r"""查询云托管部署记录

        :param request: Request instance for DescribeCloudRunDeployRecord.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunDeployRecordRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunDeployRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunDeployRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunDeployRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRunEnvs(self, request):
        r"""获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数

        :param request: Request instance for DescribeCloudRunEnvs.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunEnvsRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRunPodList(self, request):
        r"""查询云托管Pod实例列表

        :param request: Request instance for DescribeCloudRunPodList.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunPodListRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunPodListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunPodList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunPodListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRunProcessLog(self, request):
        r"""查询运行日志

        :param request: Request instance for DescribeCloudRunProcessLog.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunProcessLogRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunProcessLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunProcessLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunProcessLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRunServerDetail(self, request):
        r"""查询云托管服务详情

        :param request: Request instance for DescribeCloudRunServerDetail.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServerDetailRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunServerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunServerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRunServers(self, request):
        r"""查询云托管服务列表接口

        :param request: Request instance for DescribeCloudRunServers.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServersRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeCloudRunServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRunServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRunServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvBaseInfo(self, request):
        r"""查询环境基础信息

        :param request: Request instance for DescribeEnvBaseInfo.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeEnvBaseInfoRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeEnvBaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvBaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvBaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseOrder(self, request):
        r"""查询发布单

        :param request: Request instance for DescribeReleaseOrder.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeReleaseOrderRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeReleaseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServerManageTask(self, request):
        r"""查询服务管理任务信息

        :param request: Request instance for DescribeServerManageTask.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeServerManageTaskRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeServerManageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerManageTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerManageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVersionDetail(self, request):
        r"""查询版本详情

        :param request: Request instance for DescribeVersionDetail.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.DescribeVersionDetailRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.DescribeVersionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVersionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OperateServerManage(self, request):
        r"""操作发布单

        :param request: Request instance for OperateServerManage.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.OperateServerManageRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.OperateServerManageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateServerManage", params, headers=headers)
            response = json.loads(body)
            model = models.OperateServerManageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseGray(self, request):
        r"""灰度发布

        :param request: Request instance for ReleaseGray.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.ReleaseGrayRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.ReleaseGrayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseGray", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseGrayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClsLog(self, request):
        r"""查询日志信息

        :param request: Request instance for SearchClsLog.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.SearchClsLogRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.SearchClsLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClsLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClsLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitServerRollback(self, request):
        r"""回滚版本

        :param request: Request instance for SubmitServerRollback.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.SubmitServerRollbackRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.SubmitServerRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitServerRollback", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitServerRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCloudRunServer(self, request):
        r"""更新云托管服务

        :param request: Request instance for UpdateCloudRunServer.
        :type request: :class:`tencentcloud.tcbr.v20220217.models.UpdateCloudRunServerRequest`
        :rtype: :class:`tencentcloud.tcbr.v20220217.models.UpdateCloudRunServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCloudRunServer", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCloudRunServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))