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
from tencentcloud.youmall.v20180228 import models


class YoumallClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'youmall.tencentcloudapi.com'


    def CreateAccount(self, request):
        """创建集团门店管理员账号

        :param request: 调用CreateAccount所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFacePicture(self, request):
        """通过上传指定规格的人脸图片，创建黑名单用户或者白名单用户。

        :param request: 调用CreateFacePicture所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.CreateFacePictureRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.CreateFacePictureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFacePicture", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFacePictureResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePersonFeature(self, request):
        """删除顾客特征，仅支持删除黑名单或者白名单用户特征。

        :param request: 调用DeletePersonFeature所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DeletePersonFeatureRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DeletePersonFeatureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePersonFeature", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonFeatureResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCameraPerson(self, request):
        """通过指定设备ID和指定时段，获取该时段内中收银台摄像设备抓取到顾客头像及身份ID

        :param request: 调用DescribeCameraPerson所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeCameraPersonRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeCameraPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCameraPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCameraPersonResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterPersonArrivedMall(self, request):
        """输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。停留时间为多次进出场的停留时间之和。

        :param request: 调用DescribeClusterPersonArrivedMall所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonArrivedMallRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonArrivedMallResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterPersonArrivedMall", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterPersonArrivedMallResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterPersonTrace(self, request):
        """输出开始时间到结束时间段内的进出场数据。按天聚合的情况下，每天多次进出场算一次，以最初进场时间为进场时间，最后离场时间为离场时间。

        :param request: 调用DescribeClusterPersonTrace所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonTraceRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeClusterPersonTraceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterPersonTrace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterPersonTraceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFaceIdByTempId(self, request):
        """通过DescribeCameraPerson接口上报的收银台身份ID查询顾客的FaceID。查询最佳时间为收银台上报的次日1点后。

        :param request: 调用DescribeFaceIdByTempId所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeFaceIdByTempIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeFaceIdByTempIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFaceIdByTempId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFaceIdByTempIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHistoryNetworkInfo(self, request):
        """返回当前门店历史网络状态数据

        :param request: 调用DescribeHistoryNetworkInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeHistoryNetworkInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeHistoryNetworkInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHistoryNetworkInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHistoryNetworkInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkInfo(self, request):
        """返回当前门店最新网络状态数据

        :param request: 调用DescribeNetworkInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeNetworkInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeNetworkInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePerson(self, request):
        """查询指定某一卖场的用户信息

        :param request: 调用DescribePerson所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersonArrivedMall(self, request):
        """输出开始时间到结束时间段内的进出场数据。不做按天聚合的情况下，每次进出场，产生一条进出场数据。


        :param request: 调用DescribePersonArrivedMall所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonArrivedMallRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonArrivedMallResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonArrivedMall", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonArrivedMallResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersonInfo(self, request):
        """指定门店获取所有顾客详情列表，包含客户ID、图片、年龄、性别

        :param request: 调用DescribePersonInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersonTrace(self, request):
        """输出开始时间到结束时间段内的进出场数据。

        :param request: 调用DescribePersonTrace所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonTrace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonTraceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersonTraceDetail(self, request):
        """查询客户单次到场轨迹明细

        :param request: 调用DescribePersonTraceDetail所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceDetailRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonTraceDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonTraceDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonTraceDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersonVisitInfo(self, request):
        """获取门店指定时间范围内的所有用户到访信息记录，支持的时间范围：过去365天，含当天。

        :param request: 调用DescribePersonVisitInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribePersonVisitInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribePersonVisitInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonVisitInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonVisitInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeShopHourTrafficInfo(self, request):
        """按小时提供查询日期范围内门店的每天每小时累计客流人数数据，支持的时间范围：过去365天，含当天。

        :param request: 调用DescribeShopHourTrafficInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeShopHourTrafficInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeShopHourTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShopHourTrafficInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShopHourTrafficInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeShopInfo(self, request):
        """根据客户身份标识获取客户下所有的门店信息列表

        :param request: 调用DescribeShopInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeShopInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeShopInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShopInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShopInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeShopTrafficInfo(self, request):
        """按天提供查询日期范围内门店的单日累计客流人数，支持的时间范围：过去365天，含当天。

        :param request: 调用DescribeShopTrafficInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeShopTrafficInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeShopTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShopTrafficInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShopTrafficInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTrajectoryData(self, request):
        """获取动线轨迹信息

        :param request: 调用DescribeTrajectoryData所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeTrajectoryDataRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeTrajectoryDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrajectoryData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrajectoryDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneFlowAgeInfoByZoneId(self, request):
        """获取指定区域人流各年龄占比

        :param request: 调用DescribeZoneFlowAgeInfoByZoneId所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAgeInfoByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAgeInfoByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowAgeInfoByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowAgeInfoByZoneIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneFlowAndStayTime(self, request):
        """获取区域人流和停留时间

        :param request: 调用DescribeZoneFlowAndStayTime所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAndStayTimeRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowAndStayTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowAndStayTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowAndStayTimeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneFlowDailyByZoneId(self, request):
        """获取指定区域每日客流量

        :param request: 调用DescribeZoneFlowDailyByZoneId所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowDailyByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowDailyByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowDailyByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowDailyByZoneIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneFlowGenderAvrStayTimeByZoneId(self, request):
        """获取指定区域不同年龄段男女平均停留时间

        :param request: 调用DescribeZoneFlowGenderAvrStayTimeByZoneId所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderAvrStayTimeByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowGenderAvrStayTimeByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneFlowGenderInfoByZoneId(self, request):
        """获取指定区域性别占比

        :param request: 调用DescribeZoneFlowGenderInfoByZoneId所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderInfoByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowGenderInfoByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowGenderInfoByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowGenderInfoByZoneIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneFlowHourlyByZoneId(self, request):
        """获取指定区域分时客流量

        :param request: 调用DescribeZoneFlowHourlyByZoneId所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowHourlyByZoneIdRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneFlowHourlyByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowHourlyByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowHourlyByZoneIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneTrafficInfo(self, request):
        """按天提供查询日期范围内，客户指定门店下的所有区域（优Mall部署时已配置区域）的累计客流人次和平均停留时间。支持的时间范围：过去365天，含当天。

        :param request: 调用DescribeZoneTrafficInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneTrafficInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.DescribeZoneTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneTrafficInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneTrafficInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPersonTagInfo(self, request):
        """标记到店顾客的身份类型，例如黑名单、白名单等

        :param request: 调用ModifyPersonTagInfo所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTagInfoRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTagInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonTagInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonTagInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPersonType(self, request):
        """修改顾客身份类型接口

        :param request: 调用ModifyPersonType所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTypeRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.ModifyPersonTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterCallback(self, request):
        """调用本接口在优Mall中注册自己集团的到店通知回调接口地址，接口协议为HTTP或HTTPS。注册后，若集团有特殊身份（例如老客）到店通知，优Mall后台将主动将到店信息push给该接口

        :param request: 调用RegisterCallback所需参数的结构体。
        :type request: :class:`tencentcloud.youmall.v20180228.models.RegisterCallbackRequest`
        :rtype: :class:`tencentcloud.youmall.v20180228.models.RegisterCallbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterCallback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterCallbackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)