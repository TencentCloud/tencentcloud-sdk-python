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
from tencentcloud.weilingwith.v20230427 import models
from typing import Dict


class WeilingwithClient(AbstractClient):
    _apiVersion = '2023-04-27'
    _endpoint = 'weilingwith.tencentcloudapi.com'
    _service = 'weilingwith'

    async def AddAlarmProcessRecord(
            self,
            request: models.AddAlarmProcessRecordRequest,
            opts: Dict = None,
    ) -> models.AddAlarmProcessRecordResponse:
        """
        添加告警处理记录
        """
        
        kwargs = {}
        kwargs["action"] = "AddAlarmProcessRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAlarmProcessRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateDevice(
            self,
            request: models.BatchCreateDeviceRequest,
            opts: Dict = None,
    ) -> models.BatchCreateDeviceResponse:
        """
        单个/批量新增设备
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteDevice(
            self,
            request: models.BatchDeleteDeviceRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteDeviceResponse:
        """
        批量删除设备
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchKillAlarm(
            self,
            request: models.BatchKillAlarmRequest,
            opts: Dict = None,
    ) -> models.BatchKillAlarmResponse:
        """
        批量消警
        """
        
        kwargs = {}
        kwargs["action"] = "BatchKillAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchKillAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchReportAppMessage(
            self,
            request: models.BatchReportAppMessageRequest,
            opts: Dict = None,
    ) -> models.BatchReportAppMessageResponse:
        """
        批量上报应用消息
        """
        
        kwargs = {}
        kwargs["action"] = "BatchReportAppMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchReportAppMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeAlarmStatus(
            self,
            request: models.ChangeAlarmStatusRequest,
            opts: Dict = None,
    ) -> models.ChangeAlarmStatusResponse:
        """
        变更告警状态
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeAlarmStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeAlarmStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlCameraPTZ(
            self,
            request: models.ControlCameraPTZRequest,
            opts: Dict = None,
    ) -> models.ControlCameraPTZResponse:
        """
        云台控制
        """
        
        kwargs = {}
        kwargs["action"] = "ControlCameraPTZ"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlCameraPTZResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ControlDevice(
            self,
            request: models.ControlDeviceRequest,
            opts: Dict = None,
    ) -> models.ControlDeviceResponse:
        """
        设备控制（单个、批量控制）
        """
        
        kwargs = {}
        kwargs["action"] = "ControlDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationToken(
            self,
            request: models.CreateApplicationTokenRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationTokenResponse:
        """
        调用方应用，创建调用租户API的授权令牌。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDeviceGroup(
            self,
            request: models.DeleteDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteDeviceGroupResponse:
        """
        删除设备分组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActionList(
            self,
            request: models.DescribeActionListRequest,
            opts: Dict = None,
    ) -> models.DescribeActionListResponse:
        """
        动作列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAdministrationByTag(
            self,
            request: models.DescribeAdministrationByTagRequest,
            opts: Dict = None,
    ) -> models.DescribeAdministrationByTagResponse:
        """
        根据标签获取行政区划列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdministrationByTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdministrationByTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmLevelList(
            self,
            request: models.DescribeAlarmLevelListRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmLevelListResponse:
        """
        告警级别枚举获取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmLevelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmLevelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmList(
            self,
            request: models.DescribeAlarmListRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmListResponse:
        """
        告警列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmStatusList(
            self,
            request: models.DescribeAlarmStatusListRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmStatusListResponse:
        """
        用来查询系统中的告警状态列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmStatusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmStatusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmTypeList(
            self,
            request: models.DescribeAlarmTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmTypeListResponse:
        """
        告警类型获取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationList(
            self,
            request: models.DescribeApplicationListRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationListResponse:
        """
        查询指定空间关联的应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBuildingList(
            self,
            request: models.DescribeBuildingListRequest,
            opts: Dict = None,
    ) -> models.DescribeBuildingListResponse:
        """
        查询建筑列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBuildingList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBuildingListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBuildingModel(
            self,
            request: models.DescribeBuildingModelRequest,
            opts: Dict = None,
    ) -> models.DescribeBuildingModelResponse:
        """
        查询建筑三维模型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBuildingModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBuildingModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBuildingProfile(
            self,
            request: models.DescribeBuildingProfileRequest,
            opts: Dict = None,
    ) -> models.DescribeBuildingProfileResponse:
        """
        查询建筑信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBuildingProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBuildingProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCameraExtendInfo(
            self,
            request: models.DescribeCameraExtendInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCameraExtendInfoResponse:
        """
        获取视频扩展信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCameraExtendInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCameraExtendInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceGroupList(
            self,
            request: models.DescribeDeviceGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceGroupListResponse:
        """
        设备分组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceList(
            self,
            request: models.DescribeDeviceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceListResponse:
        """
        设备列表查询/单个查询（支持通过筛选条件查询，设备类型、标签、PID、空间）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceShadowList(
            self,
            request: models.DescribeDeviceShadowListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceShadowListResponse:
        """
        获取设备影子数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceShadowList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceShadowListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceStatusList(
            self,
            request: models.DescribeDeviceStatusListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceStatusListResponse:
        """
        设备状态获取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceStatusList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceStatusListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceStatusStat(
            self,
            request: models.DescribeDeviceStatusStatRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceStatusStatResponse:
        """
        设备状态统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceStatusStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceStatusStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceTagList(
            self,
            request: models.DescribeDeviceTagListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceTagListResponse:
        """
        标签列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceTagList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceTagListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeviceTypeList(
            self,
            request: models.DescribeDeviceTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeDeviceTypeListResponse:
        """
        拉取设备的设备类型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeviceTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeviceTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeApplicationToken(
            self,
            request: models.DescribeEdgeApplicationTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeApplicationTokenResponse:
        """
        查询边缘应用凭证
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeApplicationToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeApplicationTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeElementProfilePage(
            self,
            request: models.DescribeElementProfilePageRequest,
            opts: Dict = None,
    ) -> models.DescribeElementProfilePageResponse:
        """
        查询分页构件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeElementProfilePage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeElementProfilePageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeElementProfileTree(
            self,
            request: models.DescribeElementProfileTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeElementProfileTreeResponse:
        """
        查询构件树
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeElementProfileTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeElementProfileTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventList(
            self,
            request: models.DescribeEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeEventListResponse:
        """
        事件列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileDownloadURL(
            self,
            request: models.DescribeFileDownloadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeFileDownloadURLResponse:
        """
        获取文件下载URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileUploadURL(
            self,
            request: models.DescribeFileUploadURLRequest,
            opts: Dict = None,
    ) -> models.DescribeFileUploadURLResponse:
        """
        文件上传接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileUploadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileUploadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInterfaceList(
            self,
            request: models.DescribeInterfaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInterfaceListResponse:
        """
        查询接口列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInterfaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInterfaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLinkRuleList(
            self,
            request: models.DescribeLinkRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeLinkRuleListResponse:
        """
        联动规则列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLinkRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLinkRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelList(
            self,
            request: models.DescribeModelListRequest,
            opts: Dict = None,
    ) -> models.DescribeModelListResponse:
        """
        模型列表查询/单个查询（产品模型/标准模型）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductList(
            self,
            request: models.DescribeProductListRequest,
            opts: Dict = None,
    ) -> models.DescribeProductListResponse:
        """
        产品列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePropertyList(
            self,
            request: models.DescribePropertyListRequest,
            opts: Dict = None,
    ) -> models.DescribePropertyListResponse:
        """
        查询构件属性（详情）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePropertyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePropertyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleDetail(
            self,
            request: models.DescribeRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleDetailResponse:
        """
        联动规则详情查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSceneList(
            self,
            request: models.DescribeSceneListRequest,
            opts: Dict = None,
    ) -> models.DescribeSceneListResponse:
        """
        查询场景列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSceneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSceneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceDeviceIdList(
            self,
            request: models.DescribeSpaceDeviceIdListRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceDeviceIdListResponse:
        """
        查询指定空间设备编号列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceDeviceIdList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceDeviceIdListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceDeviceRelationList(
            self,
            request: models.DescribeSpaceDeviceRelationListRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceDeviceRelationListResponse:
        """
        查询指定空间下设备与构件绑定关系列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceDeviceRelationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceDeviceRelationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceInfoByDeviceId(
            self,
            request: models.DescribeSpaceInfoByDeviceIdRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceInfoByDeviceIdResponse:
        """
        查询设备绑定的空间信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceInfoByDeviceId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceInfoByDeviceIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceRelationByDeviceId(
            self,
            request: models.DescribeSpaceRelationByDeviceIdRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceRelationByDeviceIdResponse:
        """
        查询设备绑定的空间层级关系
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceRelationByDeviceId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceRelationByDeviceIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceTypeList(
            self,
            request: models.DescribeSpaceTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceTypeListResponse:
        """
        查询空间分类
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTenantBuildingCountAndArea(
            self,
            request: models.DescribeTenantBuildingCountAndAreaRequest,
            opts: Dict = None,
    ) -> models.DescribeTenantBuildingCountAndAreaResponse:
        """
        查询租户楼栋数量和楼栋建筑面积
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTenantBuildingCountAndArea"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTenantBuildingCountAndAreaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTenantDepartmentList(
            self,
            request: models.DescribeTenantDepartmentListRequest,
            opts: Dict = None,
    ) -> models.DescribeTenantDepartmentListResponse:
        """
        查询租户组织部门列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTenantDepartmentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTenantDepartmentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTenantUserList(
            self,
            request: models.DescribeTenantUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeTenantUserListResponse:
        """
        查询租户人员列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTenantUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTenantUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoCloudRecord(
            self,
            request: models.DescribeVideoCloudRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoCloudRecordResponse:
        """
        云录像接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoCloudRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoCloudRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoLiveStream(
            self,
            request: models.DescribeVideoLiveStreamRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoLiveStreamResponse:
        """
        实时流接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoLiveStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoLiveStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoRecordStream(
            self,
            request: models.DescribeVideoRecordStreamRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoRecordStreamResponse:
        """
        历史流接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoRecordStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoRecordStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkSpaceBuildingCountAndArea(
            self,
            request: models.DescribeWorkSpaceBuildingCountAndAreaRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkSpaceBuildingCountAndAreaResponse:
        """
        查询项目空间楼栋数量与建筑面积
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkSpaceBuildingCountAndArea"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkSpaceBuildingCountAndAreaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaceList(
            self,
            request: models.DescribeWorkspaceListRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspaceListResponse:
        """
        获取租户下的空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspaceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaceUserList(
            self,
            request: models.DescribeWorkspaceUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspaceUserListResponse:
        """
        查询项目空间人员列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaceUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspaceUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceField(
            self,
            request: models.ModifyDeviceFieldRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceFieldResponse:
        """
        批量修改设备自定义字段值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceField"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceFieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceGroup(
            self,
            request: models.ModifyDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceGroupResponse:
        """
        批量修改设备组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceName(
            self,
            request: models.ModifyDeviceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceNameResponse:
        """
        批量修改设备名字
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDeviceTag(
            self,
            request: models.ModifyDeviceTagRequest,
            opts: Dict = None,
    ) -> models.ModifyDeviceTagResponse:
        """
        批量修改设备标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDeviceTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDeviceTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportAppMessage(
            self,
            request: models.ReportAppMessageRequest,
            opts: Dict = None,
    ) -> models.ReportAppMessageResponse:
        """
        上报应用消息
        """
        
        kwargs = {}
        kwargs["action"] = "ReportAppMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportAppMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaveDeviceGroup(
            self,
            request: models.SaveDeviceGroupRequest,
            opts: Dict = None,
    ) -> models.SaveDeviceGroupResponse:
        """
        设备分组新增/修改
        """
        
        kwargs = {}
        kwargs["action"] = "SaveDeviceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaveDeviceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopVideoStreaming(
            self,
            request: models.StopVideoStreamingRequest,
            opts: Dict = None,
    ) -> models.StopVideoStreamingResponse:
        """
        断流接口
        """
        
        kwargs = {}
        kwargs["action"] = "StopVideoStreaming"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopVideoStreamingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkspaceParkAttributes(
            self,
            request: models.UpdateWorkspaceParkAttributesRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkspaceParkAttributesResponse:
        """
        修改工作空间园区属性
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkspaceParkAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkspaceParkAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)