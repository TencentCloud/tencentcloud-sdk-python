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
from tencentcloud.dnspod.v20210323 import models
from typing import Dict


class DnspodClient(AbstractClient):
    _apiVersion = '2021-03-23'
    _endpoint = 'dnspod.tencentcloudapi.com'
    _service = 'dnspod'

    async def CheckRecordSnapshotRollback(
            self,
            request: models.CheckRecordSnapshotRollbackRequest,
            opts: Dict = None,
    ) -> models.CheckRecordSnapshotRollbackResponse:
        """
        回滚前检查单条记录
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRecordSnapshotRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRecordSnapshotRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckSnapshotRollback(
            self,
            request: models.CheckSnapshotRollbackRequest,
            opts: Dict = None,
    ) -> models.CheckSnapshotRollbackResponse:
        """
        快照回滚前检查
        """
        
        kwargs = {}
        kwargs["action"] = "CheckSnapshotRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckSnapshotRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeal(
            self,
            request: models.CreateDealRequest,
            opts: Dict = None,
    ) -> models.CreateDealResponse:
        """
        DNSPod商品下单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomain(
            self,
            request: models.CreateDomainRequest,
            opts: Dict = None,
    ) -> models.CreateDomainResponse:
        """
        添加域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainAlias(
            self,
            request: models.CreateDomainAliasRequest,
            opts: Dict = None,
    ) -> models.CreateDomainAliasResponse:
        """
        创建域名别名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainBatch(
            self,
            request: models.CreateDomainBatchRequest,
            opts: Dict = None,
    ) -> models.CreateDomainBatchResponse:
        """
        批量添加域名
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainCustomLine(
            self,
            request: models.CreateDomainCustomLineRequest,
            opts: Dict = None,
    ) -> models.CreateDomainCustomLineResponse:
        """
        创建域名的自定义线路
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainCustomLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainCustomLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainGroup(
            self,
            request: models.CreateDomainGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDomainGroupResponse:
        """
        创建域名分组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainsAnalyticsFile(
            self,
            request: models.CreateDomainsAnalyticsFileRequest,
            opts: Dict = None,
    ) -> models.CreateDomainsAnalyticsFileResponse:
        """
        批量导出域名解析量
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainsAnalyticsFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainsAnalyticsFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLineGroup(
            self,
            request: models.CreateLineGroupRequest,
            opts: Dict = None,
    ) -> models.CreateLineGroupResponse:
        """
        创建域名的线路分组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLineGroupCopy(
            self,
            request: models.CreateLineGroupCopyRequest,
            opts: Dict = None,
    ) -> models.CreateLineGroupCopyResponse:
        """
        复制域名的线路分组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLineGroupCopy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLineGroupCopyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecord(
            self,
            request: models.CreateRecordRequest,
            opts: Dict = None,
    ) -> models.CreateRecordResponse:
        """
        添加记录
        备注：新添加的解析记录存在短暂的索引延迟，如果查询不到新增记录，请在 30 秒后重试
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordBatch(
            self,
            request: models.CreateRecordBatchRequest,
            opts: Dict = None,
    ) -> models.CreateRecordBatchResponse:
        """
        批量添加记录
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordGroup(
            self,
            request: models.CreateRecordGroupRequest,
            opts: Dict = None,
    ) -> models.CreateRecordGroupResponse:
        """
        添加记录分组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshot(
            self,
            request: models.CreateSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotResponse:
        """
        创建快照
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubDomainsAnalyticsFile(
            self,
            request: models.CreateSubDomainsAnalyticsFileRequest,
            opts: Dict = None,
    ) -> models.CreateSubDomainsAnalyticsFileResponse:
        """
        批量导出子域名解析量
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubDomainsAnalyticsFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubDomainsAnalyticsFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubdomainValidateTXTValue(
            self,
            request: models.CreateSubdomainValidateTXTValueRequest,
            opts: Dict = None,
    ) -> models.CreateSubdomainValidateTXTValueResponse:
        """
        创建添加子域名 Zone 域解析时所需要的 TXT 记录值
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubdomainValidateTXTValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubdomainValidateTXTValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTXTRecord(
            self,
            request: models.CreateTXTRecordRequest,
            opts: Dict = None,
    ) -> models.CreateTXTRecordResponse:
        """
        添加TXT记录
        备注：新添加的解析记录存在短暂的索引延迟，如果查询不到新增记录，请在 30 秒后重试
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTXTRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTXTRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomain(
            self,
            request: models.DeleteDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainResponse:
        """
        删除域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainAlias(
            self,
            request: models.DeleteDomainAliasRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainAliasResponse:
        """
        删除域名别名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainBatch(
            self,
            request: models.DeleteDomainBatchRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainBatchResponse:
        """
        批量删除域名
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainCustomLine(
            self,
            request: models.DeleteDomainCustomLineRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainCustomLineResponse:
        """
        删除域名的自定义线路
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainCustomLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainCustomLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLineGroup(
            self,
            request: models.DeleteLineGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteLineGroupResponse:
        """
        删除域名的线路分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecord(
            self,
            request: models.DeleteRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordResponse:
        """
        删除记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordBatch(
            self,
            request: models.DeleteRecordBatchRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordBatchResponse:
        """
        批量删除解析记录
        备注：因存储限制， 建议一次批量删除最多2000条
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordGroup(
            self,
            request: models.DeleteRecordGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordGroupResponse:
        """
        删除记录分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareDomain(
            self,
            request: models.DeleteShareDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteShareDomainResponse:
        """
        按账号删除域名共享
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshot(
            self,
            request: models.DeleteSnapshotRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotResponse:
        """
        删除快照
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchTask(
            self,
            request: models.DescribeBatchTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchTaskResponse:
        """
        获取批量操作任务执行详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomain(
            self,
            request: models.DescribeDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainResponse:
        """
        获取域名信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainAliasList(
            self,
            request: models.DescribeDomainAliasListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainAliasListResponse:
        """
        获取域名别名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainAliasList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainAliasListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainAnalytics(
            self,
            request: models.DescribeDomainAnalyticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainAnalyticsResponse:
        """
        统计各个域名的解析量，帮助您了解流量情况、时间段分布。支持查看近 3 个月内的统计情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainAnalytics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainAnalyticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainAndRecordList(
            self,
            request: models.DescribeDomainAndRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainAndRecordListResponse:
        """
        批量操作中搜索域名
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainAndRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainAndRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainCustomLineList(
            self,
            request: models.DescribeDomainCustomLineListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainCustomLineListResponse:
        """
        获取域名的自定义线路列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainCustomLineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainCustomLineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainFilterList(
            self,
            request: models.DescribeDomainFilterListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainFilterListResponse:
        """
        获取域名筛选列表
        备注：新添加的解析记录存在短暂的索引延迟，如果查询不到新增记录，请在 30 秒后重试
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainFilterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainFilterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainGroupList(
            self,
            request: models.DescribeDomainGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainGroupListResponse:
        """
        获取域名分组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainList(
            self,
            request: models.DescribeDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainListResponse:
        """
        获取域名列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainLogList(
            self,
            request: models.DescribeDomainLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainLogListResponse:
        """
        获取域名日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainPreview(
            self,
            request: models.DescribeDomainPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainPreviewResponse:
        """
        获取域名概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainPurview(
            self,
            request: models.DescribeDomainPurviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainPurviewResponse:
        """
        获取域名权限
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainPurview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainPurviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainShareInfo(
            self,
            request: models.DescribeDomainShareInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainShareInfoResponse:
        """
        获取域名共享信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainShareInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainShareInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainShareUserList(
            self,
            request: models.DescribeDomainShareUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainShareUserListResponse:
        """
        获取指定域名的已共享列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainShareUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainShareUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainVipList(
            self,
            request: models.DescribeDomainVipListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainVipListResponse:
        """
        获取套餐列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainVipList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainVipListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainWhois(
            self,
            request: models.DescribeDomainWhoisRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainWhoisResponse:
        """
        获取域名Whois信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainWhois"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainWhoisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileInfoByJobId(
            self,
            request: models.DescribeFileInfoByJobIdRequest,
            opts: Dict = None,
    ) -> models.DescribeFileInfoByJobIdResponse:
        """
        根据批量任务ID获取生成文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileInfoByJobId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileInfoByJobIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLineGroupList(
            self,
            request: models.DescribeLineGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeLineGroupListResponse:
        """
        获取域名的线路分组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLineGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLineGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackageDetail(
            self,
            request: models.DescribePackageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePackageDetailResponse:
        """
        获取各套餐配置详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecord(
            self,
            request: models.DescribeRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordResponse:
        """
        获取记录信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordExistExceptDefaultNS(
            self,
            request: models.DescribeRecordExistExceptDefaultNSRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordExistExceptDefaultNSResponse:
        """
        判断是否有除系统默认的@-NS记录之外的记录存在
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordExistExceptDefaultNS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordExistExceptDefaultNSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordFilterList(
            self,
            request: models.DescribeRecordFilterListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordFilterListResponse:
        """
        获取某个域名下的解析记录列表
        备注：
        1. 新添加的解析记录存在短暂的索引延迟，如果查询不到新增记录，请在 30 秒后重试
        2.  API获取的记录总条数会比控制台多2条，原因是： 为了防止用户误操作导致解析服务不可用，对2021-10-29 14:24:26之后添加的域名，在控制台都不显示这2条NS记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordFilterList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordFilterListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordGroupList(
            self,
            request: models.DescribeRecordGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordGroupListResponse:
        """
        查询解析记录分组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordLineCategoryList(
            self,
            request: models.DescribeRecordLineCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordLineCategoryListResponse:
        """
        按分类返回线路列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordLineCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordLineCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordLineList(
            self,
            request: models.DescribeRecordLineListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordLineListResponse:
        """
        获取等级允许的线路
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordLineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordLineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordList(
            self,
            request: models.DescribeRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordListResponse:
        """
        获取某个域名下的解析记录列表
        备注：
        1. 新添加的解析记录存在短暂的索引延迟，如果查询不到新增记录，请在 30 秒后重试
        2.  API获取的记录总条数会比控制台多2条，原因是： 为了防止用户误操作导致解析服务不可用，对2021-10-29 14:24:26之后添加的域名，在控制台都不显示这2条NS记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordSnapshotRollbackResult(
            self,
            request: models.DescribeRecordSnapshotRollbackResultRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordSnapshotRollbackResultResponse:
        """
        查询解析记录重新回滚的结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordSnapshotRollbackResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordSnapshotRollbackResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordType(
            self,
            request: models.DescribeRecordTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordTypeResponse:
        """
        获取等级允许的记录类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResolveCount(
            self,
            request: models.DescribeResolveCountRequest,
            opts: Dict = None,
    ) -> models.DescribeResolveCountResponse:
        """
        查看域名的解析量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResolveCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResolveCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotConfig(
            self,
            request: models.DescribeSnapshotConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotConfigResponse:
        """
        查询解析快照配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotList(
            self,
            request: models.DescribeSnapshotListRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotListResponse:
        """
        查询快照列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotRollbackResult(
            self,
            request: models.DescribeSnapshotRollbackResultRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotRollbackResultResponse:
        """
        查询快照回滚结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotRollbackResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotRollbackResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotRollbackTask(
            self,
            request: models.DescribeSnapshotRollbackTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotRollbackTaskResponse:
        """
        查询最近一次回滚
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotRollbackTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotRollbackTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubdomainAnalytics(
            self,
            request: models.DescribeSubdomainAnalyticsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubdomainAnalyticsResponse:
        """
        统计子域名的解析量，帮助您了解流量情况、时间段分布。支持查看近 3 个月内的统计情况。仅付费套餐域名可用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubdomainAnalytics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubdomainAnalyticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubdomainValidateStatus(
            self,
            request: models.DescribeSubdomainValidateStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSubdomainValidateStatusResponse:
        """
        查看添加子域名 Zone 域解析 TXT 记录值验证状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubdomainValidateStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubdomainValidateStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDetail(
            self,
            request: models.DescribeUserDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDetailResponse:
        """
        获取账户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVASStatistic(
            self,
            request: models.DescribeVASStatisticRequest,
            opts: Dict = None,
    ) -> models.DescribeVASStatisticResponse:
        """
        获取域名增值服务用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVASStatistic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVASStatisticResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVasList(
            self,
            request: models.DescribeVasListRequest,
            opts: Dict = None,
    ) -> models.DescribeVasListResponse:
        """
        获取增值服务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVasList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVasListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadSnapshot(
            self,
            request: models.DownloadSnapshotRequest,
            opts: Dict = None,
    ) -> models.DownloadSnapshotResponse:
        """
        下载快照
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainCNAMESpeedupStatusBatch(
            self,
            request: models.ModifyDomainCNAMESpeedupStatusBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainCNAMESpeedupStatusBatchResponse:
        """
        批量修改域名CNAME加速状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainCNAMESpeedupStatusBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainCNAMESpeedupStatusBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainCustomLine(
            self,
            request: models.ModifyDomainCustomLineRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainCustomLineResponse:
        """
        修改域名的自定义线路
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainCustomLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainCustomLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainLock(
            self,
            request: models.ModifyDomainLockRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainLockResponse:
        """
        锁定域名
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainLock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainLockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainOwner(
            self,
            request: models.ModifyDomainOwnerRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainOwnerResponse:
        """
        域名过户
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainRecursiveStatusBatch(
            self,
            request: models.ModifyDomainRecursiveStatusBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainRecursiveStatusBatchResponse:
        """
        批量修改域名递归解析加速状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainRecursiveStatusBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainRecursiveStatusBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainRemark(
            self,
            request: models.ModifyDomainRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainRemarkResponse:
        """
        设置域名备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainStatus(
            self,
            request: models.ModifyDomainStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainStatusResponse:
        """
        修改域名状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainToGroup(
            self,
            request: models.ModifyDomainToGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainToGroupResponse:
        """
        修改域名所属分组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainToGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainToGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainUnlock(
            self,
            request: models.ModifyDomainUnlockRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainUnlockResponse:
        """
        域名锁定解锁
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainUnlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainUnlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDynamicDNS(
            self,
            request: models.ModifyDynamicDNSRequest,
            opts: Dict = None,
    ) -> models.ModifyDynamicDNSResponse:
        """
        更新动态 DNS 记录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDynamicDNS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDynamicDNSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLineGroup(
            self,
            request: models.ModifyLineGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyLineGroupResponse:
        """
        修改域名的线路分组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPackageAutoRenew(
            self,
            request: models.ModifyPackageAutoRenewRequest,
            opts: Dict = None,
    ) -> models.ModifyPackageAutoRenewResponse:
        """
        DNS 解析套餐自动续费设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPackageAutoRenew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPackageAutoRenewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPackageDomain(
            self,
            request: models.ModifyPackageDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyPackageDomainResponse:
        """
        套餐绑定、解绑、更换域名
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPackageDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPackageDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecord(
            self,
            request: models.ModifyRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordResponse:
        """
        修改记录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordBatch(
            self,
            request: models.ModifyRecordBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordBatchResponse:
        """
        批量修改记录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordFields(
            self,
            request: models.ModifyRecordFieldsRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordFieldsResponse:
        """
        修改记录可选字段
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordFields"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordFieldsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordGroup(
            self,
            request: models.ModifyRecordGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordGroupResponse:
        """
        修改记录分组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordRemark(
            self,
            request: models.ModifyRecordRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordRemarkResponse:
        """
        设置记录备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordStatus(
            self,
            request: models.ModifyRecordStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordStatusResponse:
        """
        修改解析记录的状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordToGroup(
            self,
            request: models.ModifyRecordToGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordToGroupResponse:
        """
        将记录添加到分组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordToGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordToGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotConfig(
            self,
            request: models.ModifySnapshotConfigRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotConfigResponse:
        """
        修改快照配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubdomainStatus(
            self,
            request: models.ModifySubdomainStatusRequest,
            opts: Dict = None,
    ) -> models.ModifySubdomainStatusResponse:
        """
        暂停子域名的解析记录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubdomainStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubdomainStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTXTRecord(
            self,
            request: models.ModifyTXTRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyTXTRecordResponse:
        """
        修改TXT记录
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTXTRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTXTRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVasAutoRenewStatus(
            self,
            request: models.ModifyVasAutoRenewStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyVasAutoRenewStatusResponse:
        """
        增值服务自动续费设置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVasAutoRenewStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVasAutoRenewStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PayOrderWithBalance(
            self,
            request: models.PayOrderWithBalanceRequest,
            opts: Dict = None,
    ) -> models.PayOrderWithBalanceResponse:
        """
        DNSPod商品余额支付
        """
        
        kwargs = {}
        kwargs["action"] = "PayOrderWithBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PayOrderWithBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackRecordSnapshot(
            self,
            request: models.RollbackRecordSnapshotRequest,
            opts: Dict = None,
    ) -> models.RollbackRecordSnapshotResponse:
        """
        重新回滚指定解析记录快照
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackRecordSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackRecordSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackSnapshot(
            self,
            request: models.RollbackSnapshotRequest,
            opts: Dict = None,
    ) -> models.RollbackSnapshotResponse:
        """
        回滚快照
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)