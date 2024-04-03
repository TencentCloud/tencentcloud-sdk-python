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
from tencentcloud.weilingwith.v20230427 import models


class WeilingwithClient(AbstractClient):
    _apiVersion = '2023-04-27'
    _endpoint = 'weilingwith.tencentcloudapi.com'
    _service = 'weilingwith'


    def AddAlarmProcessRecord(self, request):
        """添加告警处理记录

        :param request: Request instance for AddAlarmProcessRecord.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.AddAlarmProcessRecordRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.AddAlarmProcessRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAlarmProcessRecord", params, headers=headers)
            response = json.loads(body)
            model = models.AddAlarmProcessRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateDevice(self, request):
        """单个/批量新增设备

        :param request: Request instance for BatchCreateDevice.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.BatchCreateDeviceRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BatchCreateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateDevice", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteDevice(self, request):
        """批量删除设备

        :param request: Request instance for BatchDeleteDevice.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.BatchDeleteDeviceRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BatchDeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteDevice", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchKillAlarm(self, request):
        """批量消警

        :param request: Request instance for BatchKillAlarm.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.BatchKillAlarmRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BatchKillAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchKillAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.BatchKillAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchReportAppMessage(self, request):
        """批量上报应用消息

        :param request: Request instance for BatchReportAppMessage.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.BatchReportAppMessageRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.BatchReportAppMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchReportAppMessage", params, headers=headers)
            response = json.loads(body)
            model = models.BatchReportAppMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeAlarmStatus(self, request):
        """变更告警状态

        :param request: Request instance for ChangeAlarmStatus.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ChangeAlarmStatusRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ChangeAlarmStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeAlarmStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeAlarmStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlCameraPTZ(self, request):
        """云台控制

        :param request: Request instance for ControlCameraPTZ.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ControlCameraPTZRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ControlCameraPTZResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlCameraPTZ", params, headers=headers)
            response = json.loads(body)
            model = models.ControlCameraPTZResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ControlDevice(self, request):
        """设备控制（单个、批量控制）

        :param request: Request instance for ControlDevice.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ControlDeviceRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ControlDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlDevice", params, headers=headers)
            response = json.loads(body)
            model = models.ControlDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationToken(self, request):
        """调用方应用，创建调用租户API的授权令牌。

        :param request: Request instance for CreateApplicationToken.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.CreateApplicationTokenRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.CreateApplicationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeviceGroup(self, request):
        """删除设备分组

        :param request: Request instance for DeleteDeviceGroup.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DeleteDeviceGroupRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DeleteDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeviceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeviceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeActionList(self, request):
        """动作列表查询

        :param request: Request instance for DescribeActionList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeActionListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeActionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeActionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeActionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAdministrationByTag(self, request):
        """根据标签获取行政区划列表

        :param request: Request instance for DescribeAdministrationByTag.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAdministrationByTagRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAdministrationByTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAdministrationByTag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAdministrationByTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmLevelList(self, request):
        """告警级别枚举获取

        :param request: Request instance for DescribeAlarmLevelList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmLevelListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmLevelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmLevelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmLevelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmList(self, request):
        """告警列表查询

        :param request: Request instance for DescribeAlarmList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmStatusList(self, request):
        """用来查询系统中的告警状态列表

        :param request: Request instance for DescribeAlarmStatusList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmStatusListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmStatusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmStatusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmTypeList(self, request):
        """告警类型获取

        :param request: Request instance for DescribeAlarmTypeList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmTypeListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeAlarmTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationList(self, request):
        """查询指定空间关联的应用列表

        :param request: Request instance for DescribeApplicationList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeApplicationListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeApplicationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBuildingList(self, request):
        """查询建筑列表

        :param request: Request instance for DescribeBuildingList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeBuildingListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeBuildingListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBuildingList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBuildingListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBuildingModel(self, request):
        """查询建筑三维模型

        :param request: Request instance for DescribeBuildingModel.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeBuildingModelRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeBuildingModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBuildingModel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBuildingModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBuildingProfile(self, request):
        """查询建筑信息

        :param request: Request instance for DescribeBuildingProfile.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeBuildingProfileRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeBuildingProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBuildingProfile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBuildingProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCameraExtendInfo(self, request):
        """获取视频扩展信息

        :param request: Request instance for DescribeCameraExtendInfo.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeCameraExtendInfoRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeCameraExtendInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCameraExtendInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCameraExtendInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCityWorkspaceList(self, request):
        """通过城市id查询工作空间列表

        :param request: Request instance for DescribeCityWorkspaceList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeCityWorkspaceListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeCityWorkspaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCityWorkspaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCityWorkspaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceGroupList(self, request):
        """设备分组列表

        :param request: Request instance for DescribeDeviceGroupList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceGroupListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceList(self, request):
        """设备列表查询/单个查询（支持通过筛选条件查询，设备类型、标签、PID、空间）

        :param request: Request instance for DescribeDeviceList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceShadowList(self, request):
        """获取设备影子数据

        :param request: Request instance for DescribeDeviceShadowList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceShadowListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceShadowListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceShadowList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceShadowListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceStatusList(self, request):
        """设备状态获取

        :param request: Request instance for DescribeDeviceStatusList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceStatusListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceStatusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceStatusList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceStatusListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceStatusStat(self, request):
        """设备状态统计

        :param request: Request instance for DescribeDeviceStatusStat.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceStatusStatRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceStatusStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceStatusStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceStatusStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceTagList(self, request):
        """标签列表查询

        :param request: Request instance for DescribeDeviceTagList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceTagListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceTagListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceTagList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceTagListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceTypeList(self, request):
        """拉取设备的设备类型列表

        :param request: Request instance for DescribeDeviceTypeList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceTypeListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeDeviceTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeApplicationToken(self, request):
        """查询边缘应用凭证

        :param request: Request instance for DescribeEdgeApplicationToken.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEdgeApplicationTokenRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEdgeApplicationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeApplicationToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeApplicationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeElementProfilePage(self, request):
        """查询分页构件信息

        :param request: Request instance for DescribeElementProfilePage.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeElementProfilePageRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeElementProfilePageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeElementProfilePage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeElementProfilePageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeElementProfileTree(self, request):
        """查询构件树

        :param request: Request instance for DescribeElementProfileTree.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeElementProfileTreeRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeElementProfileTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeElementProfileTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeElementProfileTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventList(self, request):
        """事件列表查询

        :param request: Request instance for DescribeEventList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEventListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileDownloadURL(self, request):
        """获取文件下载URL

        :param request: Request instance for DescribeFileDownloadURL.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeFileDownloadURLRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeFileDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileUploadURL(self, request):
        """文件上传接口

        :param request: Request instance for DescribeFileUploadURL.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeFileUploadURLRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeFileUploadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileUploadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileUploadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInterfaceList(self, request):
        """查询接口列表

        :param request: Request instance for DescribeInterfaceList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeInterfaceListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeInterfaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInterfaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInterfaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLinkRuleList(self, request):
        """联动规则列表查询

        :param request: Request instance for DescribeLinkRuleList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeLinkRuleListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeLinkRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLinkRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLinkRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelList(self, request):
        """模型列表查询/单个查询（产品模型/标准模型）

        :param request: Request instance for DescribeModelList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeModelListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductList(self, request):
        """产品列表查询

        :param request: Request instance for DescribeProductList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeProductListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeProductListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePropertyList(self, request):
        """查询构件属性（详情）

        :param request: Request instance for DescribePropertyList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribePropertyListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribePropertyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePropertyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePropertyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleDetail(self, request):
        """联动规则详情查询

        :param request: Request instance for DescribeRuleDetail.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeRuleDetailRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSceneList(self, request):
        """查询场景列表

        :param request: Request instance for DescribeSceneList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSceneListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSceneListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSceneList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSceneListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceDeviceIdList(self, request):
        """查询指定空间设备编号列表

        :param request: Request instance for DescribeSpaceDeviceIdList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceDeviceIdListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceDeviceIdListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceDeviceIdList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceDeviceIdListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceDeviceRelationList(self, request):
        """查询指定空间下设备与构件绑定关系列表

        :param request: Request instance for DescribeSpaceDeviceRelationList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceDeviceRelationListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceDeviceRelationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceDeviceRelationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceDeviceRelationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceInfoByDeviceId(self, request):
        """查询设备绑定的空间信息

        :param request: Request instance for DescribeSpaceInfoByDeviceId.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceInfoByDeviceIdRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceInfoByDeviceIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceInfoByDeviceId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceInfoByDeviceIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceRelationByDeviceId(self, request):
        """查询设备绑定的空间层级关系

        :param request: Request instance for DescribeSpaceRelationByDeviceId.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceRelationByDeviceIdRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceRelationByDeviceIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceRelationByDeviceId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceRelationByDeviceIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpaceTypeList(self, request):
        """查询空间分类

        :param request: Request instance for DescribeSpaceTypeList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceTypeListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeSpaceTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpaceTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpaceTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTenantBuildingCountAndArea(self, request):
        """查询租户楼栋数量和楼栋建筑面积

        :param request: Request instance for DescribeTenantBuildingCountAndArea.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeTenantBuildingCountAndAreaRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeTenantBuildingCountAndAreaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTenantBuildingCountAndArea", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTenantBuildingCountAndAreaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTenantDepartmentList(self, request):
        """查询租户组织部门列表

        :param request: Request instance for DescribeTenantDepartmentList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeTenantDepartmentListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeTenantDepartmentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTenantDepartmentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTenantDepartmentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTenantUserList(self, request):
        """查询租户人员列表

        :param request: Request instance for DescribeTenantUserList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeTenantUserListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeTenantUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTenantUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTenantUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoCloudRecord(self, request):
        """云录像接口

        :param request: Request instance for DescribeVideoCloudRecord.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeVideoCloudRecordRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeVideoCloudRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoCloudRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoCloudRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoLiveStream(self, request):
        """实时流接口

        :param request: Request instance for DescribeVideoLiveStream.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeVideoLiveStreamRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeVideoLiveStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoLiveStream", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoLiveStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoRecordStream(self, request):
        """历史流接口

        :param request: Request instance for DescribeVideoRecordStream.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeVideoRecordStreamRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeVideoRecordStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoRecordStream", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoRecordStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkSpaceBuildingCountAndArea(self, request):
        """查询项目空间楼栋数量与建筑面积

        :param request: Request instance for DescribeWorkSpaceBuildingCountAndArea.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkSpaceBuildingCountAndAreaRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkSpaceBuildingCountAndAreaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkSpaceBuildingCountAndArea", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkSpaceBuildingCountAndAreaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaceList(self, request):
        """获取租户下的空间列表

        :param request: Request instance for DescribeWorkspaceList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkspaceUserList(self, request):
        """查询项目空间人员列表

        :param request: Request instance for DescribeWorkspaceUserList.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceUserListRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.DescribeWorkspaceUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkspaceUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkspaceUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceField(self, request):
        """批量修改设备自定义字段值

        :param request: Request instance for ModifyDeviceField.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceFieldRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceFieldResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceField", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceFieldResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceGroup(self, request):
        """批量修改设备组

        :param request: Request instance for ModifyDeviceGroup.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceGroupRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceName(self, request):
        """批量修改设备名字

        :param request: Request instance for ModifyDeviceName.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceNameRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDeviceTag(self, request):
        """批量修改设备标签

        :param request: Request instance for ModifyDeviceTag.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceTagRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ModifyDeviceTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDeviceTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDeviceTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportAppMessage(self, request):
        """上报应用消息

        :param request: Request instance for ReportAppMessage.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.ReportAppMessageRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.ReportAppMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportAppMessage", params, headers=headers)
            response = json.loads(body)
            model = models.ReportAppMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SaveDeviceGroup(self, request):
        """设备分组新增/修改

        :param request: Request instance for SaveDeviceGroup.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.SaveDeviceGroupRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.SaveDeviceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveDeviceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.SaveDeviceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopVideoStreaming(self, request):
        """断流接口

        :param request: Request instance for StopVideoStreaming.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.StopVideoStreamingRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.StopVideoStreamingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopVideoStreaming", params, headers=headers)
            response = json.loads(body)
            model = models.StopVideoStreamingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkspaceParkAttributes(self, request):
        """修改工作空间园区属性

        :param request: Request instance for UpdateWorkspaceParkAttributes.
        :type request: :class:`tencentcloud.weilingwith.v20230427.models.UpdateWorkspaceParkAttributesRequest`
        :rtype: :class:`tencentcloud.weilingwith.v20230427.models.UpdateWorkspaceParkAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkspaceParkAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkspaceParkAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))