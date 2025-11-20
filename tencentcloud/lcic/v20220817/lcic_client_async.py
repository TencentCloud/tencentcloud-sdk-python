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
from tencentcloud.lcic.v20220817 import models
from typing import Dict


class LcicClient(AbstractClient):
    _apiVersion = '2022-08-17'
    _endpoint = 'lcic.tencentcloudapi.com'
    _service = 'lcic'

    async def AddGroupMember(
            self,
            request: models.AddGroupMemberRequest,
            opts: Dict = None,
    ) -> models.AddGroupMemberResponse:
        """
        此接口用于添加成员列表到指定群组
        """
        
        kwargs = {}
        kwargs["action"] = "AddGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchAddGroupMember(
            self,
            request: models.BatchAddGroupMemberRequest,
            opts: Dict = None,
    ) -> models.BatchAddGroupMemberResponse:
        """
        此接口用于批量添加成员列表到指定群组
        """
        
        kwargs = {}
        kwargs["action"] = "BatchAddGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchAddGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateGroupWithMembers(
            self,
            request: models.BatchCreateGroupWithMembersRequest,
            opts: Dict = None,
    ) -> models.BatchCreateGroupWithMembersResponse:
        """
        此接口用于批量创建群组
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateGroupWithMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateGroupWithMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateRoom(
            self,
            request: models.BatchCreateRoomRequest,
            opts: Dict = None,
    ) -> models.BatchCreateRoomResponse:
        """
        批量创建房间接口
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteGroupMember(
            self,
            request: models.BatchDeleteGroupMemberRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteGroupMemberResponse:
        """
        此接口用于批量删除成员列表到指定群组列表
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteRecord(
            self,
            request: models.BatchDeleteRecordRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteRecordResponse:
        """
        批量删除多个房间的录制文件
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDescribeDocument(
            self,
            request: models.BatchDescribeDocumentRequest,
            opts: Dict = None,
    ) -> models.BatchDescribeDocumentResponse:
        """
        批量获取文档详情
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDescribeDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDescribeDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRegister(
            self,
            request: models.BatchRegisterRequest,
            opts: Dict = None,
    ) -> models.BatchRegisterResponse:
        """
        如果批量注册的用户已存在，则会被覆盖。一次最多注册1000个用户。默认请求频率限制：10次/秒
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRegister"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRegisterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindDocumentToRoom(
            self,
            request: models.BindDocumentToRoomRequest,
            opts: Dict = None,
    ) -> models.BindDocumentToRoomResponse:
        """
        功能概述
        本接口提供教学场景下的课程文档预绑定能力，支持将课件课堂ID进行关联映射，实现课件的自动化预加载。

        应用场景建议

        绑定时机
        推荐在创建课堂预约阶段同步完成文档绑定操作，确保课件资源在课堂开始前完成上传。

        接口限制与频控策略

        频控维度
        开发者账号维度限频
        默认频控阈值为20 QPS（每秒请求次数）

        最佳实践建议

        重试策略
        当触发限频错误时，建议采用以下策略：
        启用退避重试机制（建议使用指数退避算法）
        初始重试间隔不低于500ms
        最大重试次数不超过3次
        """
        
        kwargs = {}
        kwargs["action"] = "BindDocumentToRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindDocumentToRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDocument(
            self,
            request: models.CreateDocumentRequest,
            opts: Dict = None,
    ) -> models.CreateDocumentResponse:
        """
        创建房间内可以使用的文档。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroupWithMembers(
            self,
            request: models.CreateGroupWithMembersRequest,
            opts: Dict = None,
    ) -> models.CreateGroupWithMembersResponse:
        """
        此接口根据成员列表创建群组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroupWithMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupWithMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroupWithSubGroup(
            self,
            request: models.CreateGroupWithSubGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupWithSubGroupResponse:
        """
        此接口会聚合子群组创建联合群组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroupWithSubGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupWithSubGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoom(
            self,
            request: models.CreateRoomRequest,
            opts: Dict = None,
    ) -> models.CreateRoomResponse:
        """
        创建课堂
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSupervisor(
            self,
            request: models.CreateSupervisorRequest,
            opts: Dict = None,
    ) -> models.CreateSupervisorResponse:
        """
        创建巡课
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSupervisor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSupervisorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAppCustomContent(
            self,
            request: models.DeleteAppCustomContentRequest,
            opts: Dict = None,
    ) -> models.DeleteAppCustomContentResponse:
        """
        删除设置自定义元素。如果参数scenes为空则删除所有自定义元素，否则删除指定的scene自定义元素。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAppCustomContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppCustomContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDocument(
            self,
            request: models.DeleteDocumentRequest,
            opts: Dict = None,
    ) -> models.DeleteDocumentResponse:
        """
        删除文档
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        此接口用于删除指定群组，支持批量操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroupMember(
            self,
            request: models.DeleteGroupMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupMemberResponse:
        """
        此接口用于删除群组中指定成员
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroupMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecord(
            self,
            request: models.DeleteRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordResponse:
        """
        删除指定房间的录制文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoom(
            self,
            request: models.DeleteRoomRequest,
            opts: Dict = None,
    ) -> models.DeleteRoomResponse:
        """
        删除房间
        删除课堂前，请先删除该课堂下的各类资源（包括录制文件、板书等），并解绑相关课件。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSupervisor(
            self,
            request: models.DeleteSupervisorRequest,
            opts: Dict = None,
    ) -> models.DeleteSupervisorResponse:
        """
        删除巡课
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSupervisor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSupervisorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        删除已注册用户。注：如果该成员已被添加到群组，请先在群组中删除该成员。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWhiteBoardSnapshot(
            self,
            request: models.DeleteWhiteBoardSnapshotRequest,
            opts: Dict = None,
    ) -> models.DeleteWhiteBoardSnapshotResponse:
        """
        删除白板板书截图
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWhiteBoardSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWhiteBoardSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAnswerList(
            self,
            request: models.DescribeAnswerListRequest,
            opts: Dict = None,
    ) -> models.DescribeAnswerListResponse:
        """
        获取房间答题详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAnswerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAnswerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppDetail(
            self,
            request: models.DescribeAppDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAppDetailResponse:
        """
        获取应用详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCurrentMemberList(
            self,
            request: models.DescribeCurrentMemberListRequest,
            opts: Dict = None,
    ) -> models.DescribeCurrentMemberListResponse:
        """
        获取当前房间的成员列表，房间结束或过期后无法使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCurrentMemberList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCurrentMemberListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeveloper(
            self,
            request: models.DescribeDeveloperRequest,
            opts: Dict = None,
    ) -> models.DescribeDeveloperResponse:
        """
        开发商信息获取
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeveloper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeveloperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDocument(
            self,
            request: models.DescribeDocumentRequest,
            opts: Dict = None,
    ) -> models.DescribeDocumentResponse:
        """
        获取文档信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDocuments(
            self,
            request: models.DescribeDocumentsRequest,
            opts: Dict = None,
    ) -> models.DescribeDocumentsResponse:
        """
        有新接口替换

        批量获取文档信息（已废弃，替代接口BatchDescribeDocument）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDocuments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocumentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDocumentsByRoom(
            self,
            request: models.DescribeDocumentsByRoomRequest,
            opts: Dict = None,
    ) -> models.DescribeDocumentsByRoomResponse:
        """
        此接口获取指定房间下课件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDocumentsByRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocumentsByRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroup(
            self,
            request: models.DescribeGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupResponse:
        """
        此接口用于获取群组详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupList(
            self,
            request: models.DescribeGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupListResponse:
        """
        获取群组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupMemberList(
            self,
            request: models.DescribeGroupMemberListRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupMemberListResponse:
        """
        此接口用于获取群组成员列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupMemberList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupMemberListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMarquee(
            self,
            request: models.DescribeMarqueeRequest,
            opts: Dict = None,
    ) -> models.DescribeMarqueeResponse:
        """
        查询跑马灯配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMarquee"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMarqueeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuestionList(
            self,
            request: models.DescribeQuestionListRequest,
            opts: Dict = None,
    ) -> models.DescribeQuestionListResponse:
        """
        获取房间提问列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuestionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuestionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecord(
            self,
            request: models.DescribeRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordResponse:
        """
        查询录制信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordStream(
            self,
            request: models.DescribeRecordStreamRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordStreamResponse:
        """
        录制流查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordTask(
            self,
            request: models.DescribeRecordTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordTaskResponse:
        """
        查询录制任务ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoom(
            self,
            request: models.DescribeRoomRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomResponse:
        """
        获取房间配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoomForbiddenUser(
            self,
            request: models.DescribeRoomForbiddenUserRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomForbiddenUserResponse:
        """
        根据房间ID获取群组中被禁言的用户列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoomForbiddenUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomForbiddenUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoomStatistics(
            self,
            request: models.DescribeRoomStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomStatisticsResponse:
        """
        获取房间统计信息，仅可在房间结束后调用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoomStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScoreList(
            self,
            request: models.DescribeScoreListRequest,
            opts: Dict = None,
    ) -> models.DescribeScoreListResponse:
        """
        获取课堂评分列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScoreList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScoreListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSdkAppIdUsers(
            self,
            request: models.DescribeSdkAppIdUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeSdkAppIdUsersResponse:
        """
        此接口用于获取指定应用ID下用户列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSdkAppIdUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSdkAppIdUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupervisors(
            self,
            request: models.DescribeSupervisorsRequest,
            opts: Dict = None,
    ) -> models.DescribeSupervisorsResponse:
        """
        获取巡课列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupervisors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupervisorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        获取用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDetail(
            self,
            request: models.DescribeUserDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDetailResponse:
        """
        获取用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoardSnapshot(
            self,
            request: models.DescribeWhiteBoardSnapshotRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoardSnapshotResponse:
        """
        查询白板板书截图
        课程结束后，可以查询和以图片的形式导出这些内容，方便后续查看、整理与分享。
        注意：不支持屏幕共享中的板书导出。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoardSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoardSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EndRoom(
            self,
            request: models.EndRoomRequest,
            opts: Dict = None,
    ) -> models.EndRoomResponse:
        """
        结束房间的直播
        """
        
        kwargs = {}
        kwargs["action"] = "EndRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EndRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForbidSendMsg(
            self,
            request: models.ForbidSendMsgRequest,
            opts: Dict = None,
    ) -> models.ForbidSendMsgResponse:
        """
        禁止指定房间中某些用户在一段时间内发言。
        取消对某些用户的禁言。
        被禁言用户退出房间之后再进入同一房间，禁言仍然有效。
        """
        
        kwargs = {}
        kwargs["action"] = "ForbidSendMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForbidSendMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRoomEvent(
            self,
            request: models.GetRoomEventRequest,
            opts: Dict = None,
    ) -> models.GetRoomEventResponse:
        """
        获取房间事件,仅在课堂结束1小时内有效。
        """
        
        kwargs = {}
        kwargs["action"] = "GetRoomEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoomEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRoomMessage(
            self,
            request: models.GetRoomMessageRequest,
            opts: Dict = None,
    ) -> models.GetRoomMessageResponse:
        """
        获取房间历史消息(房间历史消息保存7天)
        """
        
        kwargs = {}
        kwargs["action"] = "GetRoomMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoomMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRooms(
            self,
            request: models.GetRoomsRequest,
            opts: Dict = None,
    ) -> models.GetRoomsResponse:
        """
        获取房间列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetRooms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRoomsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWatermark(
            self,
            request: models.GetWatermarkRequest,
            opts: Dict = None,
    ) -> models.GetWatermarkResponse:
        """
        获取水印设置
        """
        
        kwargs = {}
        kwargs["action"] = "GetWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KickUserFromRoom(
            self,
            request: models.KickUserFromRoomRequest,
            opts: Dict = None,
    ) -> models.KickUserFromRoomResponse:
        """
        从房间里面踢出用户
        """
        
        kwargs = {}
        kwargs["action"] = "KickUserFromRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KickUserFromRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LoginOriginId(
            self,
            request: models.LoginOriginIdRequest,
            opts: Dict = None,
    ) -> models.LoginOriginIdResponse:
        """
        使用源账号登录，源账号为注册时填入的originId
        """
        
        kwargs = {}
        kwargs["action"] = "LoginOriginId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LoginOriginIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LoginUser(
            self,
            request: models.LoginUserRequest,
            opts: Dict = None,
    ) -> models.LoginUserResponse:
        """
        登录
        """
        
        kwargs = {}
        kwargs["action"] = "LoginUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LoginUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApp(
            self,
            request: models.ModifyAppRequest,
            opts: Dict = None,
    ) -> models.ModifyAppResponse:
        """
        修改应用
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroup(
            self,
            request: models.ModifyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupResponse:
        """
        此接口修改群组信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoom(
            self,
            request: models.ModifyRoomRequest,
            opts: Dict = None,
    ) -> models.ModifyRoomResponse:
        """
        修改房间
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserProfile(
            self,
            request: models.ModifyUserProfileRequest,
            opts: Dict = None,
    ) -> models.ModifyUserProfileResponse:
        """
        此接口用于修改用户信息，例如头像、昵称（用户名）等。注意，课中的用户信息不会立即同步修改，需待下次上课时，修改后的信息才会更新显示。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserProfile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserProfileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterUser(
            self,
            request: models.RegisterUserRequest,
            opts: Dict = None,
    ) -> models.RegisterUserResponse:
        """
        注册用户
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendRoomNormalMessage(
            self,
            request: models.SendRoomNormalMessageRequest,
            opts: Dict = None,
    ) -> models.SendRoomNormalMessageResponse:
        """
        1、按照指定身份发送消息，目前支持表情消息、图片消息、文本消息。
        """
        
        kwargs = {}
        kwargs["action"] = "SendRoomNormalMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendRoomNormalMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendRoomNotificationMessage(
            self,
            request: models.SendRoomNotificationMessageRequest,
            opts: Dict = None,
    ) -> models.SendRoomNotificationMessageResponse:
        """
        App 管理员可以通过该接口在群组中发送通知、公告等。目前仅支持文本消息。
        """
        
        kwargs = {}
        kwargs["action"] = "SendRoomNotificationMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendRoomNotificationMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAppCustomContent(
            self,
            request: models.SetAppCustomContentRequest,
            opts: Dict = None,
    ) -> models.SetAppCustomContentResponse:
        """
        设置应用的自定义内容，包括应用图标，自定义的代码等。如果已存在，则为更新。更新js、css内容后，要生效也需要调用该接口
        """
        
        kwargs = {}
        kwargs["action"] = "SetAppCustomContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAppCustomContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetMarquee(
            self,
            request: models.SetMarqueeRequest,
            opts: Dict = None,
    ) -> models.SetMarqueeResponse:
        """
        设置跑马灯参数设置
        """
        
        kwargs = {}
        kwargs["action"] = "SetMarquee"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetMarqueeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetWatermark(
            self,
            request: models.SetWatermarkRequest,
            opts: Dict = None,
    ) -> models.SetWatermarkResponse:
        """
        设置水印
        """
        
        kwargs = {}
        kwargs["action"] = "SetWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartRecord(
            self,
            request: models.StartRecordRequest,
            opts: Dict = None,
    ) -> models.StartRecordResponse:
        """
        开始录制
        """
        
        kwargs = {}
        kwargs["action"] = "StartRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartRoom(
            self,
            request: models.StartRoomRequest,
            opts: Dict = None,
    ) -> models.StartRoomResponse:
        """
        开始房间的直播。 说明：开始房间接口调用之前需要有用户进入课堂初始化课堂信息。
        """
        
        kwargs = {}
        kwargs["action"] = "StartRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRecord(
            self,
            request: models.StopRecordRequest,
            opts: Dict = None,
    ) -> models.StopRecordResponse:
        """
        停止录制
        """
        
        kwargs = {}
        kwargs["action"] = "StopRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindDocumentFromRoom(
            self,
            request: models.UnbindDocumentFromRoomRequest,
            opts: Dict = None,
    ) -> models.UnbindDocumentFromRoomResponse:
        """
        文档从房间解绑
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindDocumentFromRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindDocumentFromRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnblockKickedUser(
            self,
            request: models.UnblockKickedUserRequest,
            opts: Dict = None,
    ) -> models.UnblockKickedUserResponse:
        """
        解禁从房间里面踢出的用户
        """
        
        kwargs = {}
        kwargs["action"] = "UnblockKickedUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnblockKickedUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)