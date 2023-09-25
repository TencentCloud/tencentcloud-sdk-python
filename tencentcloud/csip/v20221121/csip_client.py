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
from tencentcloud.csip.v20221121 import models


class CsipClient(AbstractClient):
    _apiVersion = '2022-11-21'
    _endpoint = 'csip.tencentcloudapi.com'
    _service = 'csip'


    def AddNewBindRoleUser(self, request):
        """csip角色授权绑定接口

        :param request: Request instance for AddNewBindRoleUser.
        :type request: :class:`tencentcloud.csip.v20221121.models.AddNewBindRoleUserRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.AddNewBindRoleUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNewBindRoleUser", params, headers=headers)
            response = json.loads(body)
            model = models.AddNewBindRoleUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainAndIp(self, request):
        """创建域名、ip相关信息

        :param request: Request instance for CreateDomainAndIp.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateDomainAndIpRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateDomainAndIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainAndIp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainAndIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRiskCenterScanTask(self, request):
        """创建风险中心扫描任务

        :param request: Request instance for CreateRiskCenterScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.CreateRiskCenterScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.CreateRiskCenterScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRiskCenterScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRiskCenterScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainAndIp(self, request):
        """删除域名和ip请求

        :param request: Request instance for DeleteDomainAndIp.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteDomainAndIpRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteDomainAndIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainAndIp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainAndIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRiskScanTask(self, request):
        """删除风险中心扫描任务

        :param request: Request instance for DeleteRiskScanTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.DeleteRiskScanTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DeleteRiskScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRiskScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCVMAssetInfo(self, request):
        """cvm详情

        :param request: Request instance for DescribeCVMAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCVMAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCVMAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCVMAssets(self, request):
        """cvm列表

        :param request: Request instance for DescribeCVMAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeCVMAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCVMAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCVMAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPodAssets(self, request):
        """集群pod列表

        :param request: Request instance for DescribeClusterPodAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeClusterPodAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPodAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPodAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbAssetInfo(self, request):
        """db资产详情

        :param request: Request instance for DescribeDbAssetInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDbAssets(self, request):
        """资产列表

        :param request: Request instance for DescribeDbAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDbAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDbAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDbAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainAssets(self, request):
        """域名列表

        :param request: Request instance for DescribeDomainAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeDomainAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeDomainAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerList(self, request):
        """查询clb监听器列表

        :param request: Request instance for DescribeListenerList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeListenerListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeListenerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicIpAssets(self, request):
        """ip公网列表

        :param request: Request instance for DescribePublicIpAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribePublicIpAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribePublicIpAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicIpAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicIpAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewCFGRiskList(self, request):
        """获取资产视角的配置风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewCFGRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewCFGRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewCFGRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewCFGRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewCFGRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewPortRiskList(self, request):
        """获取资产视角的端口风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewPortRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewPortRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewPortRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewPortRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewPortRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewVULRiskList(self, request):
        """获取资产视角的漏洞风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewVULRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewVULRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewVULRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewVULRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewVULRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterAssetViewWeakPasswordRiskList(self, request):
        """获取资产视角的弱口令风险列表

        :param request: Request instance for DescribeRiskCenterAssetViewWeakPasswordRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewWeakPasswordRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterAssetViewWeakPasswordRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterAssetViewWeakPasswordRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterServerRiskList(self, request):
        """获取风险服务列表

        :param request: Request instance for DescribeRiskCenterServerRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterServerRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterServerRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterServerRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterServerRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskCenterWebsiteRiskList(self, request):
        """获取网站风险列表

        :param request: Request instance for DescribeRiskCenterWebsiteRiskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterWebsiteRiskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeRiskCenterWebsiteRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskCenterWebsiteRiskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskCenterWebsiteRiskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanReportList(self, request):
        """获取扫描报告列表

        :param request: Request instance for DescribeScanReportList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanReportListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanReportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanReportList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanReportListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskList(self, request):
        """获取扫描任务列表

        :param request: Request instance for DescribeScanTaskList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeScanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchBugInfo(self, request):
        """立体防护中心查询漏洞信息

        :param request: Request instance for DescribeSearchBugInfo.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSearchBugInfoRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSearchBugInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchBugInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchBugInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetAssets(self, request):
        """获取子网列表

        :param request: Request instance for DescribeSubnetAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeSubnetAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeSubnetAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLogList(self, request):
        """获取任务扫描报告列表

        :param request: Request instance for DescribeTaskLogList.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogListRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLogURL(self, request):
        """获取报告下载的临时链接

        :param request: Request instance for DescribeTaskLogURL.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogURLRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeTaskLogURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcAssets(self, request):
        """获取vpc列表

        :param request: Request instance for DescribeVpcAssets.
        :type request: :class:`tencentcloud.csip.v20221121.models.DescribeVpcAssetsRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.DescribeVpcAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRiskCenterTask(self, request):
        """停止扫风险中心扫描任务

        :param request: Request instance for StopRiskCenterTask.
        :type request: :class:`tencentcloud.csip.v20221121.models.StopRiskCenterTaskRequest`
        :rtype: :class:`tencentcloud.csip.v20221121.models.StopRiskCenterTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRiskCenterTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopRiskCenterTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))