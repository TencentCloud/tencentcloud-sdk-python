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
from tencentcloud.wav.v20210129 import models
from typing import Dict


class WavClient(AbstractClient):
    _apiVersion = '2021-01-29'
    _endpoint = 'wav.tencentcloudapi.com'
    _service = 'wav'

    async def CreateChannelCode(
            self,
            request: models.CreateChannelCodeRequest,
            opts: Dict = None,
    ) -> models.CreateChannelCodeResponse:
        """
        新增渠道活码接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateChannelCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateChannelCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCorpTag(
            self,
            request: models.CreateCorpTagRequest,
            opts: Dict = None,
    ) -> models.CreateCorpTagResponse:
        """
        该接口用户设置标签库, 每个企业最多可配置3000个企业标签。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCorpTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCorpTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLead(
            self,
            request: models.CreateLeadRequest,
            opts: Dict = None,
    ) -> models.CreateLeadResponse:
        """
        线索回收接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLead"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLeadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryActivityJoinList(
            self,
            request: models.QueryActivityJoinListRequest,
            opts: Dict = None,
    ) -> models.QueryActivityJoinListResponse:
        """
        根据游标拉取活动参与列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryActivityJoinList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryActivityJoinListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryActivityList(
            self,
            request: models.QueryActivityListRequest,
            opts: Dict = None,
    ) -> models.QueryActivityListResponse:
        """
        根据游标拉取活动列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryActivityList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryActivityListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryActivityLiveCodeList(
            self,
            request: models.QueryActivityLiveCodeListRequest,
            opts: Dict = None,
    ) -> models.QueryActivityLiveCodeListResponse:
        """
        根据游标拉取活动活码列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryActivityLiveCodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryActivityLiveCodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryArrivalList(
            self,
            request: models.QueryArrivalListRequest,
            opts: Dict = None,
    ) -> models.QueryArrivalListResponse:
        """
        查询指定时间范围内发生过到店的潜客到店信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryArrivalList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryArrivalListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChannelCodeList(
            self,
            request: models.QueryChannelCodeListRequest,
            opts: Dict = None,
    ) -> models.QueryChannelCodeListResponse:
        """
        根据游标拉取渠道活码列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChannelCodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChannelCodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryChatArchivingList(
            self,
            request: models.QueryChatArchivingListRequest,
            opts: Dict = None,
    ) -> models.QueryChatArchivingListResponse:
        """
        根据游标拉取会话存档列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryChatArchivingList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryChatArchivingListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryClueInfoList(
            self,
            request: models.QueryClueInfoListRequest,
            opts: Dict = None,
    ) -> models.QueryClueInfoListResponse:
        """
        企业可通过此接口获取线索列表。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryClueInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryClueInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCrmStatistics(
            self,
            request: models.QueryCrmStatisticsRequest,
            opts: Dict = None,
    ) -> models.QueryCrmStatisticsResponse:
        """
        通过接口拉取租户/指定成员/部门在指定日期范围内的CRM跟进统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCrmStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCrmStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCustomerEventDetailStatistics(
            self,
            request: models.QueryCustomerEventDetailStatisticsRequest,
            opts: Dict = None,
    ) -> models.QueryCustomerEventDetailStatisticsResponse:
        """
        通过接口拉取SaaS内C端外部联系人在指定时间范围内的行为事件明细。此接口提供的数据以天为维度，查询的时间范围为[start_time,end_time]，即前后均为闭区间，支持的最大查询跨度为365天。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCustomerEventDetailStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCustomerEventDetailStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryCustomerProfileList(
            self,
            request: models.QueryCustomerProfileListRequest,
            opts: Dict = None,
    ) -> models.QueryCustomerProfileListResponse:
        """
        通过接口拉取租户已有潜客客户档案列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryCustomerProfileList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryCustomerProfileListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryDealerInfoList(
            self,
            request: models.QueryDealerInfoListRequest,
            opts: Dict = None,
    ) -> models.QueryDealerInfoListResponse:
        """
        企业可通过此接口获取录入在企微SaaS平台上的经销商信息。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryDealerInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryDealerInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryExternalContactDetail(
            self,
            request: models.QueryExternalContactDetailRequest,
            opts: Dict = None,
    ) -> models.QueryExternalContactDetailResponse:
        """
        企业可通过此接口，根据外部联系人的userid，拉取外部联系人详情
        """
        
        kwargs = {}
        kwargs["action"] = "QueryExternalContactDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryExternalContactDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryExternalContactDetailByDate(
            self,
            request: models.QueryExternalContactDetailByDateRequest,
            opts: Dict = None,
    ) -> models.QueryExternalContactDetailByDateResponse:
        """
        企业可通过传入起始和结束时间，获取该时间段的外部联系人详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "QueryExternalContactDetailByDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryExternalContactDetailByDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryExternalContactList(
            self,
            request: models.QueryExternalContactListRequest,
            opts: Dict = None,
    ) -> models.QueryExternalContactListResponse:
        """
        企业可通过此接口基于外部联系人获取指定成员添加的客户列表。客户是指配置了客户联系功能的成员所添加的外部联系人。没有配置客户联系功能的成员，所添加的外部联系人将不会作为客户返回。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryExternalContactList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryExternalContactListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryExternalUserEventList(
            self,
            request: models.QueryExternalUserEventListRequest,
            opts: Dict = None,
    ) -> models.QueryExternalUserEventListResponse:
        """
        通过接口拉取租户在指定时间范围内的外部联系人添加/删除明细，此接口提供的数据以天为维度，查询的时间范围为[StarTime, EndTime]，即前后均为闭区间，支持的最大查询跨度为365天；
        """
        
        kwargs = {}
        kwargs["action"] = "QueryExternalUserEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryExternalUserEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryExternalUserMappingInfo(
            self,
            request: models.QueryExternalUserMappingInfoRequest,
            opts: Dict = None,
    ) -> models.QueryExternalUserMappingInfoResponse:
        """
        企业可通过此接口将企业主体对应的外部联系人id转换为乐销车应用主体对应的外部联系人。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryExternalUserMappingInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryExternalUserMappingInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFollowList(
            self,
            request: models.QueryFollowListRequest,
            opts: Dict = None,
    ) -> models.QueryFollowListResponse:
        """
        查询指定时间范围内发生过跟进的潜客信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFollowList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFollowListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryLicenseInfo(
            self,
            request: models.QueryLicenseInfoRequest,
            opts: Dict = None,
    ) -> models.QueryLicenseInfoResponse:
        """
        该接口获取license对应的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryLicenseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryLicenseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMaterialList(
            self,
            request: models.QueryMaterialListRequest,
            opts: Dict = None,
    ) -> models.QueryMaterialListResponse:
        """
        通过接口按类型拉取租户当前的素材列表及关键信息
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMaterialList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMaterialListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMiniAppCodeList(
            self,
            request: models.QueryMiniAppCodeListRequest,
            opts: Dict = None,
    ) -> models.QueryMiniAppCodeListResponse:
        """
        查询小程序码列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMiniAppCodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMiniAppCodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryStaffEventDetailStatistics(
            self,
            request: models.QueryStaffEventDetailStatisticsRequest,
            opts: Dict = None,
    ) -> models.QueryStaffEventDetailStatisticsResponse:
        """
        通过接口拉取SaaS内企业成员在指定时间范围内的行为事件明细。此接口提供的数据以天为维度，查询的时间范围为[start_time,end_time]，即前后均为闭区间，支持的最大查询跨度为365天。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryStaffEventDetailStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryStaffEventDetailStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryUserInfoList(
            self,
            request: models.QueryUserInfoListRequest,
            opts: Dict = None,
    ) -> models.QueryUserInfoListResponse:
        """
        查询企业成员信息列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "QueryUserInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryUserInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryVehicleInfoList(
            self,
            request: models.QueryVehicleInfoListRequest,
            opts: Dict = None,
    ) -> models.QueryVehicleInfoListResponse:
        """
        企业可通过此接口获取企微SaaS平台上的车系车型信息。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryVehicleInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryVehicleInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)