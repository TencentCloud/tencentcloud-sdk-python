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
from tencentcloud.youmall.v20180228 import models


class YoumallClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'youmall.tencentcloudapi.com'
    _service = 'youmall'


    def CreateAccount(self, request):
        """创建集团门店管理员账号

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.youmall.v20180228.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFacePicture(self, request):
        """通过上传指定规格的人脸图片，创建黑名单用户或者白名单用户。

        :param request: Request instance for CreateFacePicture.
        :type request: :class:`tencentcloud.youmall.v20180228.models.CreateFacePictureRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.CreateFacePictureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFacePicture", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFacePictureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePersonFeature(self, request):
        """删除顾客特征，仅支持删除黑名单或者白名单用户特征。

        :param request: Request instance for DeletePersonFeature.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DeletePersonFeatureRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DeletePersonFeatureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePersonFeature", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePersonFeatureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCameraPerson(self, request):
        """通过指定设备ID和指定时段，获取该时段内中收银台摄像设备抓取到顾客头像及身份ID

        :param request: Request instance for DescribeCameraPerson.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeCameraPersonRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeCameraPersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCameraPerson", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCameraPersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPersonArrivedMall(self, request):
        """输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。停留时间为多次进出场的停留时间之和。

        :param request: Request instance for DescribeClusterPersonArrivedMall.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonArrivedMallRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonArrivedMallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPersonArrivedMall", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPersonArrivedMallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPersonTrace(self, request):
        """输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。

        :param request: Request instance for DescribeClusterPersonTrace.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonTraceRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPersonTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPersonTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFaceIdByTempId(self, request):
        """通过DescribeCameraPerson接口上报的收银台身份ID查询顾客的FaceID。查询最佳时间为收银台上报的次日1点后。

        :param request: Request instance for DescribeFaceIdByTempId.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeFaceIdByTempIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeFaceIdByTempIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFaceIdByTempId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFaceIdByTempIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryNetworkInfo(self, request):
        """返回当前门店历史网络状态数据

        :param request: Request instance for DescribeHistoryNetworkInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeHistoryNetworkInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeHistoryNetworkInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryNetworkInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryNetworkInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkInfo(self, request):
        """返回当前门店最新网络状态数据

        :param request: Request instance for DescribeNetworkInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeNetworkInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeNetworkInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePerson(self, request):
        """查询指定某一卖场的用户信息

        :param request: Request instance for DescribePerson.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePerson", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonArrivedMall(self, request):
        """输出开始时间到结束时间段内的进出场数据。不做按天聚合的情况下，每次进出场，产生一条进出场数据。


        :param request: Request instance for DescribePersonArrivedMall.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonArrivedMallRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonArrivedMallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonArrivedMall", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonArrivedMallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonInfo(self, request):
        """指定门店获取所有顾客详情列表，包含客户ID、图片、年龄、性别

        :param request: Request instance for DescribePersonInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonInfoByFacePicture(self, request):
        """通过上传人脸图片检索系统face id、顾客身份信息及底图

        :param request: Request instance for DescribePersonInfoByFacePicture.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonInfoByFacePictureRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonInfoByFacePictureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonInfoByFacePicture", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonInfoByFacePictureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonTrace(self, request):
        """输出开始时间到结束时间段内的进出场数据。

        :param request: Request instance for DescribePersonTrace.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonTraceDetail(self, request):
        """查询客户单次到场轨迹明细

        :param request: Request instance for DescribePersonTraceDetail.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceDetailRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonTraceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonTraceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePersonVisitInfo(self, request):
        """获取门店指定时间范围内的所有用户到访信息记录，支持的时间范围：过去365天，含当天。

        :param request: Request instance for DescribePersonVisitInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonVisitInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonVisitInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersonVisitInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonVisitInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShopHourTrafficInfo(self, request):
        """按小时提供查询日期范围内门店的每天每小时累计客流人数数据，支持的时间范围：过去365天，含当天。

        :param request: Request instance for DescribeShopHourTrafficInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeShopHourTrafficInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeShopHourTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShopHourTrafficInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShopHourTrafficInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShopInfo(self, request):
        """根据客户身份标识获取客户下所有的门店信息列表

        :param request: Request instance for DescribeShopInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeShopInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeShopInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShopInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShopInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShopTrafficInfo(self, request):
        """按天提供查询日期范围内门店的单日累计客流人数，支持的时间范围：过去365天，含当天。

        :param request: Request instance for DescribeShopTrafficInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeShopTrafficInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeShopTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShopTrafficInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShopTrafficInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrajectoryData(self, request):
        """获取动线轨迹信息

        :param request: Request instance for DescribeTrajectoryData.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeTrajectoryDataRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeTrajectoryDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrajectoryData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrajectoryDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneFlowAgeInfoByZoneId(self, request):
        """获取指定区域人流各年龄占比

        :param request: Request instance for DescribeZoneFlowAgeInfoByZoneId.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAgeInfoByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAgeInfoByZoneIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneFlowAgeInfoByZoneId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneFlowAgeInfoByZoneIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneFlowAndStayTime(self, request):
        """获取区域人流和停留时间

        :param request: Request instance for DescribeZoneFlowAndStayTime.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAndStayTimeRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAndStayTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneFlowAndStayTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneFlowAndStayTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneFlowDailyByZoneId(self, request):
        """获取指定区域每日客流量

        :param request: Request instance for DescribeZoneFlowDailyByZoneId.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowDailyByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowDailyByZoneIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneFlowDailyByZoneId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneFlowDailyByZoneIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneFlowGenderAvrStayTimeByZoneId(self, request):
        """获取指定区域不同年龄段男女平均停留时间

        :param request: Request instance for DescribeZoneFlowGenderAvrStayTimeByZoneId.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderAvrStayTimeByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneFlowGenderAvrStayTimeByZoneId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneFlowGenderInfoByZoneId(self, request):
        """获取指定区域性别占比

        :param request: Request instance for DescribeZoneFlowGenderInfoByZoneId.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderInfoByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderInfoByZoneIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneFlowGenderInfoByZoneId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneFlowGenderInfoByZoneIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneFlowHourlyByZoneId(self, request):
        """获取指定区域分时客流量

        :param request: Request instance for DescribeZoneFlowHourlyByZoneId.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowHourlyByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowHourlyByZoneIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneFlowHourlyByZoneId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneFlowHourlyByZoneIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneTrafficInfo(self, request):
        """按天提供查询日期范围内，客户指定门店下的所有区域（优Mall部署时已配置区域）的累计客流人次和平均停留时间。支持的时间范围：过去365天，含当天。

        :param request: Request instance for DescribeZoneTrafficInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneTrafficInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneTrafficInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneTrafficInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPersonFeatureInfo(self, request):
        """支持修改黑白名单类型的顾客特征

        :param request: Request instance for ModifyPersonFeatureInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonFeatureInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonFeatureInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPersonFeatureInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonFeatureInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPersonTagInfo(self, request):
        """标记到店顾客的身份类型，例如黑名单、白名单等

        :param request: Request instance for ModifyPersonTagInfo.
        :type request: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTagInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTagInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPersonTagInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonTagInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPersonType(self, request):
        """修改顾客身份类型接口

        :param request: Request instance for ModifyPersonType.
        :type request: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTypeRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPersonType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterCallback(self, request):
        """调用本接口在优Mall中注册自己集团的到店通知回调接口地址，接口协议为HTTP或HTTPS。注册后，若集团有特殊身份（例如老客）到店通知，优Mall后台将主动将到店信息push给该接口

        :param request: Request instance for RegisterCallback.
        :type request: :class:`tencentcloud.youmall.v20180228.models.RegisterCallbackRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.RegisterCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterCallback", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))