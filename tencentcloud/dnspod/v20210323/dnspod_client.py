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
from tencentcloud.dnspod.v20210323 import models


class DnspodClient(AbstractClient):
    _apiVersion = '2021-03-23'
    _endpoint = 'dnspod.tencentcloudapi.com'
    _service = 'dnspod'


    def CheckRecordSnapshotRollback(self, request):
        """回滚前检查单条记录

        :param request: Request instance for CheckRecordSnapshotRollback.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CheckRecordSnapshotRollbackRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CheckRecordSnapshotRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRecordSnapshotRollback", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRecordSnapshotRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckSnapshotRollback(self, request):
        """快照回滚前检查

        :param request: Request instance for CheckSnapshotRollback.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CheckSnapshotRollbackRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CheckSnapshotRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckSnapshotRollback", params, headers=headers)
            response = json.loads(body)
            model = models.CheckSnapshotRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeal(self, request):
        """DNSPod商品下单

        :param request: Request instance for CreateDeal.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDealRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomain(self, request):
        """添加域名

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainAlias(self, request):
        """创建域名别名

        :param request: Request instance for CreateDomainAlias.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainAliasRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainAlias", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainBatch(self, request):
        """批量添加域名

        :param request: Request instance for CreateDomainBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomainGroup(self, request):
        """创建域名分组

        :param request: Request instance for CreateDomainGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecord(self, request):
        """添加记录

        :param request: Request instance for CreateRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordBatch(self, request):
        """批量添加记录

        :param request: Request instance for CreateRecordBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordGroup(self, request):
        """添加记录分组

        :param request: Request instance for CreateRecordGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshot(self, request):
        """创建快照

        :param request: Request instance for CreateSnapshot.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateSnapshotRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomain(self, request):
        """删除域名

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainAlias(self, request):
        """删除域名别名

        :param request: Request instance for DeleteDomainAlias.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainAliasRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainAlias", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomainBatch(self, request):
        """批量删除域名

        :param request: Request instance for DeleteDomainBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainBatch", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecord(self, request):
        """删除记录

        :param request: Request instance for DeleteRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordBatch(self, request):
        """批量删除解析记录

        :param request: Request instance for DeleteRecordBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordBatch", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordGroup(self, request):
        """删除记录分组

        :param request: Request instance for DeleteRecordGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShareDomain(self, request):
        """删除域名共享

        :param request: Request instance for DeleteShareDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteShareDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteShareDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShareDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshot(self, request):
        """删除快照

        :param request: Request instance for DeleteSnapshot.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteSnapshotRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchTask(self, request):
        """获取任务详情

        :param request: Request instance for DescribeBatchTask.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeBatchTaskRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeBatchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomain(self, request):
        """获取域名信息

        :param request: Request instance for DescribeDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainAliasList(self, request):
        """获取域名别名列表

        :param request: Request instance for DescribeDomainAliasList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAliasListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAliasListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainAliasList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainAliasListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainAnalytics(self, request):
        """统计各个域名的解析量，帮助您了解流量情况、时间段分布。支持查看近 3 个月内的统计情况

        :param request: Request instance for DescribeDomainAnalytics.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAnalyticsRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAnalyticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainAnalytics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainAnalyticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainFilterList(self, request):
        """获取域名筛选列表

        :param request: Request instance for DescribeDomainFilterList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainFilterListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainFilterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainFilterList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainFilterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainGroupList(self, request):
        """获取域名分组列表

        :param request: Request instance for DescribeDomainGroupList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainGroupListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainList(self, request):
        """获取域名列表

        :param request: Request instance for DescribeDomainList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainLogList(self, request):
        """获取域名日志

        :param request: Request instance for DescribeDomainLogList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainLogListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainPreview(self, request):
        """获取域名概览信息

        :param request: Request instance for DescribeDomainPreview.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPreviewRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainPurview(self, request):
        """获取域名权限

        :param request: Request instance for DescribeDomainPurview.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPurviewRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPurviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainPurview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainPurviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainShareInfo(self, request):
        """获取域名共享信息

        :param request: Request instance for DescribeDomainShareInfo.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainShareInfoRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainShareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainShareInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainShareInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainWhois(self, request):
        """获取域名Whois信息

        :param request: Request instance for DescribeDomainWhois.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainWhoisRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainWhoisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainWhois", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainWhoisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePackageDetail(self, request):
        """获取各套餐配置详情

        :param request: Request instance for DescribePackageDetail.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribePackageDetailRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribePackageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecord(self, request):
        """获取记录信息

        :param request: Request instance for DescribeRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordExistExceptDefaultNS(self, request):
        """判断是否有除系统默认的@-NS记录之外的记录存在

        :param request: Request instance for DescribeRecordExistExceptDefaultNS.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordExistExceptDefaultNSRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordExistExceptDefaultNSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordExistExceptDefaultNS", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordExistExceptDefaultNSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordGroupList(self, request):
        """查询解析记录分组列表

        :param request: Request instance for DescribeRecordGroupList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordGroupListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordLineList(self, request):
        """获取等级允许的线路

        :param request: Request instance for DescribeRecordLineList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordLineListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordLineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordLineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordLineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordList(self, request):
        """获取某个域名下的解析记录列表

        :param request: Request instance for DescribeRecordList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordSnapshotRollbackResult(self, request):
        """查询解析记录重新回滚的结果

        :param request: Request instance for DescribeRecordSnapshotRollbackResult.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordSnapshotRollbackResultRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordSnapshotRollbackResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordSnapshotRollbackResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordSnapshotRollbackResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordType(self, request):
        """获取等级允许的记录类型

        :param request: Request instance for DescribeRecordType.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordTypeRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotConfig(self, request):
        """查询解析快照配置

        :param request: Request instance for DescribeSnapshotConfig.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotConfigRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotList(self, request):
        """查询快照列表

        :param request: Request instance for DescribeSnapshotList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotRollbackResult(self, request):
        """查询快照回滚结果

        :param request: Request instance for DescribeSnapshotRollbackResult.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotRollbackResultRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotRollbackResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotRollbackResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotRollbackResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotRollbackTask(self, request):
        """查询最近一次回滚

        :param request: Request instance for DescribeSnapshotRollbackTask.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotRollbackTaskRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeSnapshotRollbackTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotRollbackTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotRollbackTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubdomainAnalytics(self, request):
        """统计子域名的解析量，帮助您了解流量情况、时间段分布。支持查看近 3 个月内的统计情况。仅付费套餐域名可用。

        :param request: Request instance for DescribeSubdomainAnalytics.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeSubdomainAnalyticsRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeSubdomainAnalyticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubdomainAnalytics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubdomainAnalyticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDetail(self, request):
        """获取帐户信息

        :param request: Request instance for DescribeUserDetail.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeUserDetailRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeUserDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVASStatistic(self, request):
        """获取域名增值服务用量

        :param request: Request instance for DescribeVASStatistic.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeVASStatisticRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeVASStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVASStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVASStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadSnapshot(self, request):
        """下载快照

        :param request: Request instance for DownloadSnapshot.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DownloadSnapshotRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DownloadSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainLock(self, request):
        """锁定域名

        :param request: Request instance for ModifyDomainLock.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainLockRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainLockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainLock", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainLockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainOwner(self, request):
        """域名过户

        :param request: Request instance for ModifyDomainOwner.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainOwnerRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainOwner", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainRemark(self, request):
        """设置域名备注

        :param request: Request instance for ModifyDomainRemark.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainRemarkRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainStatus(self, request):
        """修改域名状态

        :param request: Request instance for ModifyDomainStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainUnlock(self, request):
        """域名锁定解锁

        :param request: Request instance for ModifyDomainUnlock.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainUnlockRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainUnlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainUnlock", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainUnlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDynamicDNS(self, request):
        """更新动态 DNS 记录

        :param request: Request instance for ModifyDynamicDNS.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDynamicDNSRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDynamicDNSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDynamicDNS", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDynamicDNSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPackageAutoRenew(self, request):
        """DNS 解析套餐自动续费设置

        :param request: Request instance for ModifyPackageAutoRenew.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyPackageAutoRenewRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyPackageAutoRenewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPackageAutoRenew", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPackageAutoRenewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecord(self, request):
        """修改记录

        :param request: Request instance for ModifyRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordBatch(self, request):
        """批量修改记录

        :param request: Request instance for ModifyRecordBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordFields(self, request):
        """修改记录可选字段

        :param request: Request instance for ModifyRecordFields.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordFieldsRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordFieldsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordFields", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordFieldsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordGroup(self, request):
        """修改记录分组

        :param request: Request instance for ModifyRecordGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordRemark(self, request):
        """设置记录备注

        :param request: Request instance for ModifyRecordRemark.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRemarkRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordStatus(self, request):
        """修改解析记录的状态

        :param request: Request instance for ModifyRecordStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordToGroup(self, request):
        """将记录添加到分组

        :param request: Request instance for ModifyRecordToGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordToGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordToGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordToGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordToGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotConfig(self, request):
        """修改快照配置

        :param request: Request instance for ModifySnapshotConfig.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifySnapshotConfigRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifySnapshotConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubdomainStatus(self, request):
        """暂停子域名的解析记录

        :param request: Request instance for ModifySubdomainStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifySubdomainStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifySubdomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubdomainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubdomainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVasAutoRenewStatus(self, request):
        """增值服务自动续费设置

        :param request: Request instance for ModifyVasAutoRenewStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyVasAutoRenewStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyVasAutoRenewStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVasAutoRenewStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVasAutoRenewStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PayOrderWithBalance(self, request):
        """DNSPod商品余额支付

        :param request: Request instance for PayOrderWithBalance.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.PayOrderWithBalanceRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.PayOrderWithBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PayOrderWithBalance", params, headers=headers)
            response = json.loads(body)
            model = models.PayOrderWithBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackRecordSnapshot(self, request):
        """重新回滚指定解析记录快照

        :param request: Request instance for RollbackRecordSnapshot.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.RollbackRecordSnapshotRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.RollbackRecordSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackRecordSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackRecordSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackSnapshot(self, request):
        """回滚快照

        :param request: Request instance for RollbackSnapshot.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.RollbackSnapshotRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.RollbackSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))