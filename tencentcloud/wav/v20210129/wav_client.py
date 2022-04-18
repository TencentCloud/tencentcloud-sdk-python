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
            if "Error" not in response["Response"]:
                model = models.CreateChannelCodeResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateCorpTagResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateLeadResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryActivityJoinListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryActivityListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryActivityLiveCodeListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryChannelCodeListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryChatArchivingListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryClueInfoListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryCrmStatisticsResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryCustomerEventDetailStatisticsResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryDealerInfoListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryExternalContactDetailResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryExternalContactListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryExternalUserEventListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryExternalUserMappingInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryLicenseInfoResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryMaterialListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryMiniAppCodeListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryStaffEventDetailStatisticsResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryUserInfoListResponse()
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
            if "Error" not in response["Response"]:
                model = models.QueryVehicleInfoListResponse()
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