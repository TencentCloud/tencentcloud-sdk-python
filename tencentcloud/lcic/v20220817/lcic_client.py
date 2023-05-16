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
from tencentcloud.lcic.v20220817 import models


class LcicClient(AbstractClient):
    _apiVersion = '2022-08-17'
    _endpoint = 'lcic.tencentcloudapi.com'
    _service = 'lcic'


    def AddGroupMember(self, request):
        """此接口用于添加成员列表到指定群组

        :param request: Request instance for AddGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.AddGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.AddGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.AddGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchAddGroupMember(self, request):
        """此接口用于批量添加成员列表到指定群组

        :param request: Request instance for BatchAddGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchAddGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchAddGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchAddGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.BatchAddGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchCreateGroupWithMembers(self, request):
        """此接口用于批量创建群组

        :param request: Request instance for BatchCreateGroupWithMembers.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchCreateGroupWithMembersRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchCreateGroupWithMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateGroupWithMembers", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateGroupWithMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchCreateRoom(self, request):
        """批量创建房间接口

        :param request: Request instance for BatchCreateRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchCreateRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchCreateRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateRoom", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDeleteGroupMember(self, request):
        """此接口用于批量删除成员列表到指定群组列表

        :param request: Request instance for BatchDeleteGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDeleteRecord(self, request):
        """批量删除多个房间的录制文件

        :param request: Request instance for BatchDeleteRecord.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteRecordRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchDeleteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteRecord", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDescribeDocument(self, request):
        """批量获取文档详情

        :param request: Request instance for BatchDescribeDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchDescribeDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchDescribeDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDescribeDocument", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDescribeDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchRegister(self, request):
        """如果批量注册的用户已存在，则会被覆盖。一次最多注册1000个用户。默认请求频率限制：10次/秒

        :param request: Request instance for BatchRegister.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BatchRegisterRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BatchRegisterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRegister", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRegisterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindDocumentToRoom(self, request):
        """绑定文档到房间

        :param request: Request instance for BindDocumentToRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BindDocumentToRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BindDocumentToRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDocumentToRoom", params, headers=headers)
            response = json.loads(body)
            model = models.BindDocumentToRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDocument(self, request):
        """创建房间内可以使用的文档。

        :param request: Request instance for CreateDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDocument", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGroupWithMembers(self, request):
        """此接口根据成员列表创建群组

        :param request: Request instance for CreateGroupWithMembers.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithMembersRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithMembersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroupWithMembers", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupWithMembersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGroupWithSubGroup(self, request):
        """此接口会聚合子群组创建联合群组

        :param request: Request instance for CreateGroupWithSubGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithSubGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateGroupWithSubGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGroupWithSubGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGroupWithSubGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRoom(self, request):
        """创建房间

        :param request: Request instance for CreateRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoom", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSupervisor(self, request):
        """创建巡课

        :param request: Request instance for CreateSupervisor.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateSupervisorRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateSupervisorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSupervisor", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSupervisorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAppCustomContent(self, request):
        """删除设置自定义元素。如果参数scenes为空则删除所有自定义元素，否则删除指定的scene自定义元素。

        :param request: Request instance for DeleteAppCustomContent.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteAppCustomContentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteAppCustomContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAppCustomContent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppCustomContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDocument(self, request):
        """删除文档

        :param request: Request instance for DeleteDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDocument", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGroup(self, request):
        """此接口用于删除指定群组，支持批量操作。

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGroupMember(self, request):
        """此接口用于删除群组中指定成员

        :param request: Request instance for DeleteGroupMember.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupMemberRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteGroupMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroupMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRecord(self, request):
        """删除指定房间的录制文件

        :param request: Request instance for DeleteRecord.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteRecordRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteRecordResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRoom(self, request):
        """删除房间

        :param request: Request instance for DeleteRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSupervisor(self, request):
        """删除巡课

        :param request: Request instance for DeleteSupervisor.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteSupervisorRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteSupervisorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSupervisor", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSupervisorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAnswerList(self, request):
        """获取房间答题详情

        :param request: Request instance for DescribeAnswerList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeAnswerListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeAnswerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAnswerList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAnswerListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAppDetail(self, request):
        """获取应用详情

        :param request: Request instance for DescribeAppDetail.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeAppDetailRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeAppDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCurrentMemberList(self, request):
        """获取当前房间的成员列表，房间结束或过期后无法使用。

        :param request: Request instance for DescribeCurrentMemberList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeCurrentMemberListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeCurrentMemberListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurrentMemberList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCurrentMemberListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeveloper(self, request):
        """开发商信息获取

        :param request: Request instance for DescribeDeveloper.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDeveloperRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDeveloperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeveloper", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeveloperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDocument(self, request):
        """获取文档信息

        :param request: Request instance for DescribeDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDocument", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDocuments(self, request):
        """有新接口替换

        批量获取文档信息（已废弃，替代接口BatchDescribeDocument）

        :param request: Request instance for DescribeDocuments.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDocuments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocumentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDocumentsByRoom(self, request):
        """此接口获取指定房间下课件列表

        :param request: Request instance for DescribeDocumentsByRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsByRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeDocumentsByRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDocumentsByRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocumentsByRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroup(self, request):
        """此接口用于获取群组详情

        :param request: Request instance for DescribeGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupList(self, request):
        """获取群组列表

        :param request: Request instance for DescribeGroupList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGroupMemberList(self, request):
        """此接口用于获取群组成员列表

        :param request: Request instance for DescribeGroupMemberList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupMemberListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeGroupMemberListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupMemberList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupMemberListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeQuestionList(self, request):
        """获取房间提问列表

        :param request: Request instance for DescribeQuestionList.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeQuestionListRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeQuestionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuestionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuestionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRoom(self, request):
        """获取房间信息

        :param request: Request instance for DescribeRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRoomStatistics(self, request):
        """获取房间统计信息，仅可在房间结束后调用。

        :param request: Request instance for DescribeRoomStatistics.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomStatisticsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSdkAppIdUsers(self, request):
        """此接口用于获取指定应用ID下用户列表

        :param request: Request instance for DescribeSdkAppIdUsers.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeSdkAppIdUsersRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeSdkAppIdUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSdkAppIdUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSdkAppIdUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSupervisors(self, request):
        """获取巡课列表

        :param request: Request instance for DescribeSupervisors.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeSupervisorsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeSupervisorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupervisors", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupervisorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUser(self, request):
        """获取用户信息

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EndRoom(self, request):
        """结束房间的直播

        :param request: Request instance for EndRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.EndRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.EndRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EndRoom", params, headers=headers)
            response = json.loads(body)
            model = models.EndRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRoomEvent(self, request):
        """获取房间事件,仅在课堂结束1小时内有效。

        :param request: Request instance for GetRoomEvent.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetRoomEventRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetRoomEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRoomEvent", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoomEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRoomMessage(self, request):
        """获取房间历史消息(房间历史消息保存7天)

        :param request: Request instance for GetRoomMessage.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetRoomMessageRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetRoomMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRoomMessage", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoomMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRooms(self, request):
        """获取房间列表

        :param request: Request instance for GetRooms.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetRoomsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetRoomsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRooms", params, headers=headers)
            response = json.loads(body)
            model = models.GetRoomsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetWatermark(self, request):
        """获取水印设置

        :param request: Request instance for GetWatermark.
        :type request: :class:`tencentcloud.lcic.v20220817.models.GetWatermarkRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.GetWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.GetWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def KickUserFromRoom(self, request):
        """从房间里面踢出用户

        :param request: Request instance for KickUserFromRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.KickUserFromRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.KickUserFromRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KickUserFromRoom", params, headers=headers)
            response = json.loads(body)
            model = models.KickUserFromRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LoginOriginId(self, request):
        """使用源账号登录，源账号为注册时填入的originId

        :param request: Request instance for LoginOriginId.
        :type request: :class:`tencentcloud.lcic.v20220817.models.LoginOriginIdRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.LoginOriginIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginOriginId", params, headers=headers)
            response = json.loads(body)
            model = models.LoginOriginIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LoginUser(self, request):
        """登录

        :param request: Request instance for LoginUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.LoginUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.LoginUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginUser", params, headers=headers)
            response = json.loads(body)
            model = models.LoginUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApp(self, request):
        """修改应用

        :param request: Request instance for ModifyApp.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyAppRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGroup(self, request):
        """此接口修改群组信息

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRoom(self, request):
        """修改房间

        :param request: Request instance for ModifyRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoom", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUserProfile(self, request):
        """此接口用于修改用户配置，如头像，昵称/用户名等。

        :param request: Request instance for ModifyUserProfile.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyUserProfileRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyUserProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserProfile", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserProfileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterUser(self, request):
        """注册用户

        :param request: Request instance for RegisterUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.RegisterUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.RegisterUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterUser", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetAppCustomContent(self, request):
        """设置应用的自定义内容，包括应用图标，自定义的代码等。如果已存在，则为更新。更新js、css内容后，要生效也需要调用该接口

        :param request: Request instance for SetAppCustomContent.
        :type request: :class:`tencentcloud.lcic.v20220817.models.SetAppCustomContentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.SetAppCustomContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAppCustomContent", params, headers=headers)
            response = json.loads(body)
            model = models.SetAppCustomContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetWatermark(self, request):
        """设置水印

        :param request: Request instance for SetWatermark.
        :type request: :class:`tencentcloud.lcic.v20220817.models.SetWatermarkRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.SetWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.SetWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartRoom(self, request):
        """开始房间的直播。 说明：开始房间接口调用之前需要有用户进入课堂初始化课堂信息。

        :param request: Request instance for StartRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.StartRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.StartRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartRoom", params, headers=headers)
            response = json.loads(body)
            model = models.StartRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindDocumentFromRoom(self, request):
        """文档从房间解绑

        :param request: Request instance for UnbindDocumentFromRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.UnbindDocumentFromRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.UnbindDocumentFromRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindDocumentFromRoom", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindDocumentFromRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)