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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AddAlarmProcessRecordRequest(AbstractModel):
    """AddAlarmProcessRecord请求参数结构体

    """


class AddAlarmProcessRecordResponse(AbstractModel):
    """AddAlarmProcessRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchCreateDeviceRequest(AbstractModel):
    """BatchCreateDevice请求参数结构体

    """


class BatchCreateDeviceResponse(AbstractModel):
    """BatchCreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchKillAlarmRequest(AbstractModel):
    """BatchKillAlarm请求参数结构体

    """


class BatchKillAlarmResponse(AbstractModel):
    """BatchKillAlarm返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BatchReportAppMessageRequest(AbstractModel):
    """BatchReportAppMessage请求参数结构体

    """


class BatchReportAppMessageResponse(AbstractModel):
    """BatchReportAppMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ChangeAlarmStatusRequest(AbstractModel):
    """ChangeAlarmStatus请求参数结构体

    """


class ChangeAlarmStatusResponse(AbstractModel):
    """ChangeAlarmStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ControlCameraPTZRequest(AbstractModel):
    """ControlCameraPTZ请求参数结构体

    """


class ControlCameraPTZResponse(AbstractModel):
    """ControlCameraPTZ返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ControlDeviceRequest(AbstractModel):
    """ControlDevice请求参数结构体

    """


class ControlDeviceResponse(AbstractModel):
    """ControlDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateApplicationTokenRequest(AbstractModel):
    """CreateApplicationToken请求参数结构体

    """


class CreateApplicationTokenResponse(AbstractModel):
    """CreateApplicationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeActionListRequest(AbstractModel):
    """DescribeActionList请求参数结构体

    """


class DescribeActionListResponse(AbstractModel):
    """DescribeActionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAdministrationByTagRequest(AbstractModel):
    """DescribeAdministrationByTag请求参数结构体

    """


class DescribeAdministrationByTagResponse(AbstractModel):
    """DescribeAdministrationByTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAlarmLevelListRequest(AbstractModel):
    """DescribeAlarmLevelList请求参数结构体

    """


class DescribeAlarmLevelListResponse(AbstractModel):
    """DescribeAlarmLevelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAlarmListRequest(AbstractModel):
    """DescribeAlarmList请求参数结构体

    """


class DescribeAlarmListResponse(AbstractModel):
    """DescribeAlarmList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAlarmStatusListRequest(AbstractModel):
    """DescribeAlarmStatusList请求参数结构体

    """


class DescribeAlarmStatusListResponse(AbstractModel):
    """DescribeAlarmStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAlarmTypeListRequest(AbstractModel):
    """DescribeAlarmTypeList请求参数结构体

    """


class DescribeAlarmTypeListResponse(AbstractModel):
    """DescribeAlarmTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeApplicationListRequest(AbstractModel):
    """DescribeApplicationList请求参数结构体

    """


class DescribeApplicationListResponse(AbstractModel):
    """DescribeApplicationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeBuildingListRequest(AbstractModel):
    """DescribeBuildingList请求参数结构体

    """


class DescribeBuildingListResponse(AbstractModel):
    """DescribeBuildingList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeBuildingModelRequest(AbstractModel):
    """DescribeBuildingModel请求参数结构体

    """


class DescribeBuildingModelResponse(AbstractModel):
    """DescribeBuildingModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeBuildingProfileRequest(AbstractModel):
    """DescribeBuildingProfile请求参数结构体

    """


class DescribeBuildingProfileResponse(AbstractModel):
    """DescribeBuildingProfile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCameraExtendInfoRequest(AbstractModel):
    """DescribeCameraExtendInfo请求参数结构体

    """


class DescribeCameraExtendInfoResponse(AbstractModel):
    """DescribeCameraExtendInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCityWorkspaceListRequest(AbstractModel):
    """DescribeCityWorkspaceList请求参数结构体

    """


class DescribeCityWorkspaceListResponse(AbstractModel):
    """DescribeCityWorkspaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    """DescribeDeviceList请求参数结构体

    """


class DescribeDeviceListResponse(AbstractModel):
    """DescribeDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceShadowListRequest(AbstractModel):
    """DescribeDeviceShadowList请求参数结构体

    """


class DescribeDeviceShadowListResponse(AbstractModel):
    """DescribeDeviceShadowList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceStatusListRequest(AbstractModel):
    """DescribeDeviceStatusList请求参数结构体

    """


class DescribeDeviceStatusListResponse(AbstractModel):
    """DescribeDeviceStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceStatusStatRequest(AbstractModel):
    """DescribeDeviceStatusStat请求参数结构体

    """


class DescribeDeviceStatusStatResponse(AbstractModel):
    """DescribeDeviceStatusStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceTagListRequest(AbstractModel):
    """DescribeDeviceTagList请求参数结构体

    """


class DescribeDeviceTagListResponse(AbstractModel):
    """DescribeDeviceTagList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeviceTypeListRequest(AbstractModel):
    """DescribeDeviceTypeList请求参数结构体

    """


class DescribeDeviceTypeListResponse(AbstractModel):
    """DescribeDeviceTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeEdgeApplicationTokenRequest(AbstractModel):
    """DescribeEdgeApplicationToken请求参数结构体

    """


class DescribeEdgeApplicationTokenResponse(AbstractModel):
    """DescribeEdgeApplicationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeElementProfilePageRequest(AbstractModel):
    """DescribeElementProfilePage请求参数结构体

    """


class DescribeElementProfilePageResponse(AbstractModel):
    """DescribeElementProfilePage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeElementProfileTreeRequest(AbstractModel):
    """DescribeElementProfileTree请求参数结构体

    """


class DescribeElementProfileTreeResponse(AbstractModel):
    """DescribeElementProfileTree返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeEventListRequest(AbstractModel):
    """DescribeEventList请求参数结构体

    """


class DescribeEventListResponse(AbstractModel):
    """DescribeEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeFileDownloadURLRequest(AbstractModel):
    """DescribeFileDownloadURL请求参数结构体

    """


class DescribeFileDownloadURLResponse(AbstractModel):
    """DescribeFileDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeFileUploadURLRequest(AbstractModel):
    """DescribeFileUploadURL请求参数结构体

    """


class DescribeFileUploadURLResponse(AbstractModel):
    """DescribeFileUploadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeInterfaceListRequest(AbstractModel):
    """DescribeInterfaceList请求参数结构体

    """


class DescribeInterfaceListResponse(AbstractModel):
    """DescribeInterfaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeLinkRuleListRequest(AbstractModel):
    """DescribeLinkRuleList请求参数结构体

    """


class DescribeLinkRuleListResponse(AbstractModel):
    """DescribeLinkRuleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeModelListRequest(AbstractModel):
    """DescribeModelList请求参数结构体

    """


class DescribeModelListResponse(AbstractModel):
    """DescribeModelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeProductListRequest(AbstractModel):
    """DescribeProductList请求参数结构体

    """


class DescribeProductListResponse(AbstractModel):
    """DescribeProductList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribePropertyListRequest(AbstractModel):
    """DescribePropertyList请求参数结构体

    """


class DescribePropertyListResponse(AbstractModel):
    """DescribePropertyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeRuleDetailRequest(AbstractModel):
    """DescribeRuleDetail请求参数结构体

    """


class DescribeRuleDetailResponse(AbstractModel):
    """DescribeRuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeSceneListRequest(AbstractModel):
    """DescribeSceneList请求参数结构体

    """


class DescribeSceneListResponse(AbstractModel):
    """DescribeSceneList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeSpaceDeviceIdListRequest(AbstractModel):
    """DescribeSpaceDeviceIdList请求参数结构体

    """


class DescribeSpaceDeviceIdListResponse(AbstractModel):
    """DescribeSpaceDeviceIdList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeSpaceDeviceRelationListRequest(AbstractModel):
    """DescribeSpaceDeviceRelationList请求参数结构体

    """


class DescribeSpaceDeviceRelationListResponse(AbstractModel):
    """DescribeSpaceDeviceRelationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeSpaceInfoByDeviceIdRequest(AbstractModel):
    """DescribeSpaceInfoByDeviceId请求参数结构体

    """


class DescribeSpaceInfoByDeviceIdResponse(AbstractModel):
    """DescribeSpaceInfoByDeviceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeSpaceRelationByDeviceIdRequest(AbstractModel):
    """DescribeSpaceRelationByDeviceId请求参数结构体

    """


class DescribeSpaceRelationByDeviceIdResponse(AbstractModel):
    """DescribeSpaceRelationByDeviceId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeSpaceTypeListRequest(AbstractModel):
    """DescribeSpaceTypeList请求参数结构体

    """


class DescribeSpaceTypeListResponse(AbstractModel):
    """DescribeSpaceTypeList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeTenantBuildingCountAndAreaRequest(AbstractModel):
    """DescribeTenantBuildingCountAndArea请求参数结构体

    """


class DescribeTenantBuildingCountAndAreaResponse(AbstractModel):
    """DescribeTenantBuildingCountAndArea返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeTenantDepartmentListRequest(AbstractModel):
    """DescribeTenantDepartmentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 翻页页码
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _ApplicationToken: token
        :type ApplicationToken: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UpdateAt: 更新时间戳，单位秒
        :type UpdateAt: int
        :param _DepartmentId: 部门ID
        :type DepartmentId: str
        :param _Cursor: 用户id
        :type Cursor: str
        """
        self._Offset = None
        self._Limit = None
        self._ApplicationToken = None
        self._TenantId = None
        self._UpdateAt = None
        self._DepartmentId = None
        self._Cursor = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ApplicationToken(self):
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DepartmentId(self):
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TenantId = params.get("TenantId")
        self._UpdateAt = params.get("UpdateAt")
        self._DepartmentId = params.get("DepartmentId")
        self._Cursor = params.get("Cursor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTenantDepartmentListResponse(AbstractModel):
    """DescribeTenantDepartmentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回数据
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SsoDepartmentsResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = SsoDepartmentsResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeTenantUserListRequest(AbstractModel):
    """DescribeTenantUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 翻页页码
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _ApplicationToken: token
        :type ApplicationToken: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UpdateAt: 更新时间戳，单位秒
        :type UpdateAt: int
        :param _DepartmentId: 部门ID
        :type DepartmentId: str
        :param _Cursor: 用户id
        :type Cursor: str
        :param _Status: 状态，0，获取所有数据，1正常启用，2禁用
        :type Status: int
        :param _WorkspaceId: 项目空间id
        :type WorkspaceId: str
        :param _Keyword: 关键词
        :type Keyword: str
        :param _NoRecursive: 是否递归获取子级数据，0需要，1不需要，默认为0
        :type NoRecursive: str
        """
        self._Offset = None
        self._Limit = None
        self._ApplicationToken = None
        self._TenantId = None
        self._UpdateAt = None
        self._DepartmentId = None
        self._Cursor = None
        self._Status = None
        self._WorkspaceId = None
        self._Keyword = None
        self._NoRecursive = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ApplicationToken(self):
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DepartmentId(self):
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Cursor(self):
        return self._Cursor

    @Cursor.setter
    def Cursor(self, Cursor):
        self._Cursor = Cursor

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WorkspaceId(self):
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def NoRecursive(self):
        return self._NoRecursive

    @NoRecursive.setter
    def NoRecursive(self, NoRecursive):
        self._NoRecursive = NoRecursive


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TenantId = params.get("TenantId")
        self._UpdateAt = params.get("UpdateAt")
        self._DepartmentId = params.get("DepartmentId")
        self._Cursor = params.get("Cursor")
        self._Status = params.get("Status")
        self._WorkspaceId = params.get("WorkspaceId")
        self._Keyword = params.get("Keyword")
        self._NoRecursive = params.get("NoRecursive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTenantUserListResponse(AbstractModel):
    """DescribeTenantUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回数据
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SsoUserResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = SsoUserResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeVideoCloudRecordRequest(AbstractModel):
    """DescribeVideoCloudRecord请求参数结构体

    """


class DescribeVideoCloudRecordResponse(AbstractModel):
    """DescribeVideoCloudRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeVideoLiveStreamRequest(AbstractModel):
    """DescribeVideoLiveStream请求参数结构体

    """


class DescribeVideoLiveStreamResponse(AbstractModel):
    """DescribeVideoLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeVideoRecordStreamRequest(AbstractModel):
    """DescribeVideoRecordStream请求参数结构体

    """


class DescribeVideoRecordStreamResponse(AbstractModel):
    """DescribeVideoRecordStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeWorkSpaceBuildingCountAndAreaRequest(AbstractModel):
    """DescribeWorkSpaceBuildingCountAndArea请求参数结构体

    """


class DescribeWorkSpaceBuildingCountAndAreaResponse(AbstractModel):
    """DescribeWorkSpaceBuildingCountAndArea返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceListRequest(AbstractModel):
    """DescribeWorkspaceList请求参数结构体

    """


class DescribeWorkspaceListResponse(AbstractModel):
    """DescribeWorkspaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceUserListRequest(AbstractModel):
    """DescribeWorkspaceUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 翻页页码
        :type Offset: int
        :param _Limit: 翻页大小
        :type Limit: int
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        :param _ApplicationToken: token
        :type ApplicationToken: str
        :param _TenantId: 租户ID
        :type TenantId: str
        :param _UpdateAt: 更新时间戳，单位秒
        :type UpdateAt: int
        """
        self._Offset = None
        self._Limit = None
        self._WorkspaceId = None
        self._ApplicationToken = None
        self._TenantId = None
        self._UpdateAt = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def WorkspaceId(self):
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def ApplicationToken(self):
        return self._ApplicationToken

    @ApplicationToken.setter
    def ApplicationToken(self, ApplicationToken):
        self._ApplicationToken = ApplicationToken

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._WorkspaceId = params.get("WorkspaceId")
        self._ApplicationToken = params.get("ApplicationToken")
        self._TenantId = params.get("TenantId")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceUserListResponse(AbstractModel):
    """DescribeWorkspaceUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回数据
        :type Result: :class:`tencentcloud.weilingwith.v20230427.models.SsoTeamUserResult`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = SsoTeamUserResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyDeviceNameRequest(AbstractModel):
    """ModifyDeviceName请求参数结构体

    """


class ModifyDeviceNameResponse(AbstractModel):
    """ModifyDeviceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReportAppMessageRequest(AbstractModel):
    """ReportAppMessage请求参数结构体

    """


class ReportAppMessageResponse(AbstractModel):
    """ReportAppMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SsoDepartment(AbstractModel):
    """部门用户

    """

    def __init__(self):
        r"""
        :param _DepartmentId: 部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentId: str
        :param _Name: 部门名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ParentDepartmentId: 父级部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentDepartmentId: str
        """
        self._DepartmentId = None
        self._Name = None
        self._ParentDepartmentId = None

    @property
    def DepartmentId(self):
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentDepartmentId(self):
        return self._ParentDepartmentId

    @ParentDepartmentId.setter
    def ParentDepartmentId(self, ParentDepartmentId):
        self._ParentDepartmentId = ParentDepartmentId


    def _deserialize(self, params):
        self._DepartmentId = params.get("DepartmentId")
        self._Name = params.get("Name")
        self._ParentDepartmentId = params.get("ParentDepartmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoDepartmentsResult(AbstractModel):
    """部门用户结果

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Departments: 部门列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Departments: list of SsoDepartment
        """
        self._Total = None
        self._Departments = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Departments(self):
        return self._Departments

    @Departments.setter
    def Departments(self, Departments):
        self._Departments = Departments


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Departments") is not None:
            self._Departments = []
            for item in params.get("Departments"):
                obj = SsoDepartment()
                obj._deserialize(item)
                self._Departments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoTeamUser(AbstractModel):
    """部门用户

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _RealName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RealName: str
        :param _UserType: 用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _TenantId: 所属租户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantId: str
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Phone: 电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _Status: 用户状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: int
        :param _DepartmentId: 部门ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentId: str
        :param _DepartmentName: 部门名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentName: str
        :param _LinkFilter: 是否关联权限
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkFilter: int
        """
        self._UserId = None
        self._RealName = None
        self._UserType = None
        self._TenantId = None
        self._Email = None
        self._Phone = None
        self._Status = None
        self._CreateAt = None
        self._DepartmentId = None
        self._DepartmentName = None
        self._LinkFilter = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RealName(self):
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def DepartmentId(self):
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DepartmentName(self):
        return self._DepartmentName

    @DepartmentName.setter
    def DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName

    @property
    def LinkFilter(self):
        return self._LinkFilter

    @LinkFilter.setter
    def LinkFilter(self, LinkFilter):
        self._LinkFilter = LinkFilter


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RealName = params.get("RealName")
        self._UserType = params.get("UserType")
        self._TenantId = params.get("TenantId")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._Status = params.get("Status")
        self._CreateAt = params.get("CreateAt")
        self._DepartmentId = params.get("DepartmentId")
        self._DepartmentName = params.get("DepartmentName")
        self._LinkFilter = params.get("LinkFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoTeamUserResult(AbstractModel):
    """空间用户结果

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Users: 部门用户列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of SsoTeamUser
        """
        self._Total = None
        self._Users = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = SsoTeamUser()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoUser(AbstractModel):
    """用户结果

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _UserName: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _RealName: 用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RealName: str
        :param _UserType: 用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _TenantId: 所属租户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TenantId: str
        :param _UserGroup: 所属组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserGroup: str
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _Phone: 电话
注意：此字段可能返回 null，表示取不到有效值。
        :type Phone: str
        :param _Status: 用户状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateAt: int
        :param _UpdateAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateAt: int
        :param _BelongTeam: 是否属于团队
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongTeam: int
        :param _DepartmentId: ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentId: str
        :param _DepartmentName: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentName: str
        :param _DepartmentUserId: 子账户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DepartmentUserId: int
        :param _Password: 密码
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        """
        self._UserId = None
        self._UserName = None
        self._RealName = None
        self._UserType = None
        self._TenantId = None
        self._UserGroup = None
        self._Email = None
        self._Phone = None
        self._Status = None
        self._CreateAt = None
        self._UpdateAt = None
        self._BelongTeam = None
        self._DepartmentId = None
        self._DepartmentName = None
        self._DepartmentUserId = None
        self._Password = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def RealName(self):
        return self._RealName

    @RealName.setter
    def RealName(self, RealName):
        self._RealName = RealName

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def UserGroup(self):
        return self._UserGroup

    @UserGroup.setter
    def UserGroup(self, UserGroup):
        self._UserGroup = UserGroup

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateAt(self):
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def BelongTeam(self):
        return self._BelongTeam

    @BelongTeam.setter
    def BelongTeam(self, BelongTeam):
        self._BelongTeam = BelongTeam

    @property
    def DepartmentId(self):
        return self._DepartmentId

    @DepartmentId.setter
    def DepartmentId(self, DepartmentId):
        self._DepartmentId = DepartmentId

    @property
    def DepartmentName(self):
        return self._DepartmentName

    @DepartmentName.setter
    def DepartmentName(self, DepartmentName):
        self._DepartmentName = DepartmentName

    @property
    def DepartmentUserId(self):
        return self._DepartmentUserId

    @DepartmentUserId.setter
    def DepartmentUserId(self, DepartmentUserId):
        self._DepartmentUserId = DepartmentUserId

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._RealName = params.get("RealName")
        self._UserType = params.get("UserType")
        self._TenantId = params.get("TenantId")
        self._UserGroup = params.get("UserGroup")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._Status = params.get("Status")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._BelongTeam = params.get("BelongTeam")
        self._DepartmentId = params.get("DepartmentId")
        self._DepartmentName = params.get("DepartmentName")
        self._DepartmentUserId = params.get("DepartmentUserId")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SsoUserResult(AbstractModel):
    """租户人员结果

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Users: 租户人员数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Users: list of SsoUser
        """
        self._Total = None
        self._Users = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = SsoUser()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopVideoStreamingRequest(AbstractModel):
    """StopVideoStreaming请求参数结构体

    """


class StopVideoStreamingResponse(AbstractModel):
    """StopVideoStreaming返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateWorkspaceParkAttributesRequest(AbstractModel):
    """UpdateWorkspaceParkAttributes请求参数结构体

    """


class UpdateWorkspaceParkAttributesResponse(AbstractModel):
    """UpdateWorkspaceParkAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")