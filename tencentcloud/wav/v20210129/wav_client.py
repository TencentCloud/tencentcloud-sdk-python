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
from tencentcloud.wav.v20210129 import models


class WavClient(AbstractClient):
    _apiVersion = '2021-01-29'
    _endpoint = 'wav.tencentcloudapi.com'
    _service = 'wav'


    def CreateChannelCode(self, request):
        """新增渠道活码接口

        :param request: Request instance for CreateChannelCode.
        :type request: :class:`tencentcloud.wav.v20210129.models.CreateChannelCodeRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.CreateChannelCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChannelCode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChannelCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCorpTag(self, request):
        """该接口用户设置标签库, 每个企业最多可配置3000个企业标签。

        :param request: Request instance for CreateCorpTag.
        :type request: :class:`tencentcloud.wav.v20210129.models.CreateCorpTagRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.CreateCorpTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCorpTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCorpTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLead(self, request):
        """线索回收接口

        :param request: Request instance for CreateLead.
        :type request: :class:`tencentcloud.wav.v20210129.models.CreateLeadRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.CreateLeadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLead", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLeadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryActivityJoinList(self, request):
        """根据游标拉取活动参与列表信息

        :param request: Request instance for QueryActivityJoinList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryActivityJoinListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryActivityJoinListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryActivityJoinList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryActivityJoinListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryActivityList(self, request):
        """根据游标拉取活动列表信息

        :param request: Request instance for QueryActivityList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryActivityListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryActivityListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryActivityList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryActivityListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryActivityLiveCodeList(self, request):
        """根据游标拉取活动活码列表信息

        :param request: Request instance for QueryActivityLiveCodeList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryActivityLiveCodeListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryActivityLiveCodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryActivityLiveCodeList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryActivityLiveCodeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryArrivalList(self, request):
        """查询指定时间范围内发生过到店的潜客到店信息

        :param request: Request instance for QueryArrivalList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryArrivalListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryArrivalListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryArrivalList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryArrivalListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryChannelCodeList(self, request):
        """根据游标拉取渠道活码列表信息

        :param request: Request instance for QueryChannelCodeList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryChannelCodeListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryChannelCodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChannelCodeList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChannelCodeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryChatArchivingList(self, request):
        """根据游标拉取会话存档列表信息

        :param request: Request instance for QueryChatArchivingList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryChatArchivingListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryChatArchivingListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChatArchivingList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryChatArchivingListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryClueInfoList(self, request):
        """企业可通过此接口获取线索列表。

        :param request: Request instance for QueryClueInfoList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryClueInfoListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryClueInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryClueInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryClueInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCrmStatistics(self, request):
        """通过接口拉取租户/指定成员/部门在指定日期范围内的CRM跟进统计数据

        :param request: Request instance for QueryCrmStatistics.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryCrmStatisticsRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryCrmStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCrmStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCrmStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCustomerEventDetailStatistics(self, request):
        """通过接口拉取SaaS内C端外部联系人在指定时间范围内的行为事件明细。此接口提供的数据以天为维度，查询的时间范围为[start_time,end_time]，即前后均为闭区间，支持的最大查询跨度为365天。

        :param request: Request instance for QueryCustomerEventDetailStatistics.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryCustomerEventDetailStatisticsRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryCustomerEventDetailStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCustomerEventDetailStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCustomerEventDetailStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCustomerProfileList(self, request):
        """通过接口拉取租户已有潜客客户档案列表信息

        :param request: Request instance for QueryCustomerProfileList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryCustomerProfileListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryCustomerProfileListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCustomerProfileList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCustomerProfileListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDealerInfoList(self, request):
        """企业可通过此接口获取录入在企微SaaS平台上的经销商信息。

        :param request: Request instance for QueryDealerInfoList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryDealerInfoListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryDealerInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDealerInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDealerInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryExternalContactDetail(self, request):
        """企业可通过此接口，根据外部联系人的userid，拉取外部联系人详情

        :param request: Request instance for QueryExternalContactDetail.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryExternalContactDetailRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryExternalContactDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryExternalContactDetail", params, headers=headers)
            response = json.loads(body)
            model = models.QueryExternalContactDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryExternalContactDetailByDate(self, request):
        """企业可通过传入起始和结束时间，获取该时间段的外部联系人详情列表

        :param request: Request instance for QueryExternalContactDetailByDate.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryExternalContactDetailByDateRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryExternalContactDetailByDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryExternalContactDetailByDate", params, headers=headers)
            response = json.loads(body)
            model = models.QueryExternalContactDetailByDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryExternalContactList(self, request):
        """企业可通过此接口基于外部联系人获取指定成员添加的客户列表。客户是指配置了客户联系功能的成员所添加的外部联系人。没有配置客户联系功能的成员，所添加的外部联系人将不会作为客户返回。

        :param request: Request instance for QueryExternalContactList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryExternalContactListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryExternalContactListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryExternalContactList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryExternalContactListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryExternalUserEventList(self, request):
        """通过接口拉取租户在指定时间范围内的外部联系人添加/删除明细，此接口提供的数据以天为维度，查询的时间范围为[StarTime, EndTime]，即前后均为闭区间，支持的最大查询跨度为365天；

        :param request: Request instance for QueryExternalUserEventList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryExternalUserEventListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryExternalUserEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryExternalUserEventList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryExternalUserEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryExternalUserMappingInfo(self, request):
        """企业可通过此接口将企业主体对应的外部联系人id转换为乐销车应用主体对应的外部联系人。

        :param request: Request instance for QueryExternalUserMappingInfo.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryExternalUserMappingInfoRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryExternalUserMappingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryExternalUserMappingInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryExternalUserMappingInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryFollowList(self, request):
        """查询指定时间范围内发生过跟进的潜客信息

        :param request: Request instance for QueryFollowList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryFollowListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryFollowListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryFollowList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryFollowListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryLicenseInfo(self, request):
        """该接口获取license对应的详细信息

        :param request: Request instance for QueryLicenseInfo.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryLicenseInfoRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryLicenseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryLicenseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.QueryLicenseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryMaterialList(self, request):
        """通过接口按类型拉取租户当前的素材列表及关键信息

        :param request: Request instance for QueryMaterialList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryMaterialListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryMaterialListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMaterialList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMaterialListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryMiniAppCodeList(self, request):
        """查询小程序码列表接口

        :param request: Request instance for QueryMiniAppCodeList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryMiniAppCodeListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryMiniAppCodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMiniAppCodeList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMiniAppCodeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryStaffEventDetailStatistics(self, request):
        """通过接口拉取SaaS内企业成员在指定时间范围内的行为事件明细。此接口提供的数据以天为维度，查询的时间范围为[start_time,end_time]，即前后均为闭区间，支持的最大查询跨度为365天。

        :param request: Request instance for QueryStaffEventDetailStatistics.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryStaffEventDetailStatisticsRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryStaffEventDetailStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryStaffEventDetailStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.QueryStaffEventDetailStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryUserInfoList(self, request):
        """查询企业成员信息列表接口

        :param request: Request instance for QueryUserInfoList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryUserInfoListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryUserInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryUserInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryUserInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryVehicleInfoList(self, request):
        """企业可通过此接口获取企微SaaS平台上的车系车型信息。

        :param request: Request instance for QueryVehicleInfoList.
        :type request: :class:`tencentcloud.wav.v20210129.models.QueryVehicleInfoListRequest`
        :rtype: :class:`tencentcloud.wav.v20210129.models.QueryVehicleInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryVehicleInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryVehicleInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))