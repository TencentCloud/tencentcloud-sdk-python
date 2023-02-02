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
from tencentcloud.tci.v20190318 import models


class TciClient(AbstractClient):
    _apiVersion = '2019-03-18'
    _endpoint = 'tci.tencentcloudapi.com'
    _service = 'tci'


    def AIAssistant(self, request):
        """提供 AI 助教基础版本功能接口

        :param request: Request instance for AIAssistant.
        :type request: :class:`tencentcloud.tci.v20190318.models.AIAssistantRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.AIAssistantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AIAssistant", params, headers=headers)
            response = json.loads(body)
            model = models.AIAssistantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelTask(self, request):
        """用于取消已经提交的任务，目前只支持图像任务。

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckFacePhoto(self, request):
        """检查人脸图片是否合法

        :param request: Request instance for CheckFacePhoto.
        :type request: :class:`tencentcloud.tci.v20190318.models.CheckFacePhotoRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CheckFacePhotoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFacePhoto", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFacePhotoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFace(self, request):
        """创建人脸

        :param request: Request instance for CreateFace.
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateFaceRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLibrary(self, request):
        """创建人员库

        :param request: Request instance for CreateLibrary.
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateLibraryRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePerson(self, request):
        """创建人员

        :param request: Request instance for CreatePerson.
        :type request: :class:`tencentcloud.tci.v20190318.models.CreatePersonRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreatePersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePerson", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVocab(self, request):
        """创建词汇

        :param request: Request instance for CreateVocab.
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateVocabRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVocab", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVocabLib(self, request):
        """建立词汇库

        :param request: Request instance for CreateVocabLib.
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateVocabLibRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateVocabLibResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVocabLib", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVocabLibResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFace(self, request):
        """删除人脸

        :param request: Request instance for DeleteFace.
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteFaceRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteFaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLibrary(self, request):
        """删除人员库

        :param request: Request instance for DeleteLibrary.
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteLibraryRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePerson(self, request):
        """删除人员

        :param request: Request instance for DeletePerson.
        :type request: :class:`tencentcloud.tci.v20190318.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeletePersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePerson", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVocab(self, request):
        """删除词汇

        :param request: Request instance for DeleteVocab.
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteVocabRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVocab", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVocabLib(self, request):
        """删除词汇库

        :param request: Request instance for DeleteVocabLib.
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteVocabLibRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteVocabLibResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVocabLib", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVocabLibResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAITaskResult(self, request):
        """获取标准化接口任务结果

        :param request: Request instance for DescribeAITaskResult.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeAITaskResultRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeAITaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAITaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAITaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAttendanceResult(self, request):
        """人脸考勤查询结果

        :param request: Request instance for DescribeAttendanceResult.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeAttendanceResultRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeAttendanceResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttendanceResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttendanceResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAudioTask(self, request):
        """音频评估任务信息查询接口，异步查询客户提交的请求的结果。

        :param request: Request instance for DescribeAudioTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeAudioTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeAudioTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAudioTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAudioTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConversationTask(self, request):
        """音频对话任务评估任务信息查询接口，异步查询客户提交的请求的结果。

        :param request: Request instance for DescribeConversationTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeConversationTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeConversationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConversationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConversationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHighlightResult(self, request):
        """视频精彩集锦结果查询接口，异步查询客户提交的请求的结果。

        :param request: Request instance for DescribeHighlightResult.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeHighlightResultRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeHighlightResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHighlightResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHighlightResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageTask(self, request):
        """拉取任务详情

        :param request: Request instance for DescribeImageTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageTaskStatistic(self, request):
        """获取图像任务统计信息

        :param request: Request instance for DescribeImageTaskStatistic.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskStatisticRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageTaskStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageTaskStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLibraries(self, request):
        """获取人员库列表

        :param request: Request instance for DescribeLibraries.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeLibrariesRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeLibrariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLibraries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLibrariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePerson(self, request):
        """获取人员详情

        :param request: Request instance for DescribePerson.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribePersonRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribePersonResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersons(self, request):
        """拉取人员列表

        :param request: Request instance for DescribePersons.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribePersonsRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribePersonsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePersons", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePersonsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVocab(self, request):
        """查询词汇

        :param request: Request instance for DescribeVocab.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeVocabRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVocab", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVocabLib(self, request):
        """查询词汇库

        :param request: Request instance for DescribeVocabLib.
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeVocabLibRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeVocabLibResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVocabLib", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVocabLibResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLibrary(self, request):
        """修改人员库信息

        :param request: Request instance for ModifyLibrary.
        :type request: :class:`tencentcloud.tci.v20190318.models.ModifyLibraryRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.ModifyLibraryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLibrary", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLibraryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPerson(self, request):
        """修改人员信息

        :param request: Request instance for ModifyPerson.
        :type request: :class:`tencentcloud.tci.v20190318.models.ModifyPersonRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.ModifyPersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPerson", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitAudioTask(self, request):
        """音频任务提交接口

        :param request: Request instance for SubmitAudioTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitAudioTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitAudioTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitAudioTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitAudioTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitCheckAttendanceTask(self, request):
        """提交人员考勤任务，支持包括点播和直播资源；支持通过DescribeAttendanceResult查询结果，也支持通过NoticeUrl设置考勤回调结果，回调结果结构如下：
        ##### 回调事件结构
         | 参数名称 | 类型 | 描述 |
         | ----  | ---  | ------  |
         | jobid | Integer | 任务ID |
         | person_info | array of PersonInfo | 识别到的人员列表 |
        #####子结构PersonInfo
         | 参数名称 | 类型 | 描述 |
         | ----  | ---  | ------  |
         | traceid | String | 可用于区分同一路视频流下的不同陌生人 |
         | personid | String | 识别到的人员ID，如果是陌生人则返回空串 |
         | libid | String | 识别到的人员所在的库ID，如果是陌生人则返回空串 |
         | timestamp | uint64 | 识别到人脸的绝对时间戳，单位ms |
         | image_url | string | 识别到人脸的事件抓图的下载地址，不长期保存，需要请及时下载 |

        :param request: Request instance for SubmitCheckAttendanceTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitCheckAttendanceTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitCheckAttendanceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitCheckAttendanceTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitCheckAttendanceTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitCheckAttendanceTaskPlus(self, request):
        """支持多路视频流，提交高级人员考勤任务

        :param request: Request instance for SubmitCheckAttendanceTaskPlus.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitCheckAttendanceTaskPlusRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitCheckAttendanceTaskPlusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitCheckAttendanceTaskPlus", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitCheckAttendanceTaskPlusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitConversationTask(self, request):
        """对话任务分析接口

        :param request: Request instance for SubmitConversationTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitConversationTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitConversationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitConversationTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitConversationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitDoubleVideoHighlights(self, request):
        """发起双路视频生成精彩集锦接口。该接口可以通过客户传入的学生音视频及老师视频两路Url，自动生成一堂课程的精彩集锦。需要通过DescribeHighlightResult
        接口获取生成结果。

        :param request: Request instance for SubmitDoubleVideoHighlights.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitDoubleVideoHighlightsRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitDoubleVideoHighlightsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitDoubleVideoHighlights", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitDoubleVideoHighlightsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitFullBodyClassTask(self, request):
        """**传统课堂授课任务**：在此场景中，老师为站立授课，有白板或投影供老师展示课程内容，摄像头可以拍摄到老师的半身或者全身。拍摄视频为一路全局画面，且背景不动，要求画面稳定清晰。通过此接口可分析老师授课的行为及语音，以支持AI评教。

        **提供的功能接口有：**老师人脸识别、老师表情识别、老师肢体动作识别、语音识别。  可分析的指标维度包括：身份识别、正脸、侧脸、人脸坐标、人脸尺寸、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、正面讲解、写板书、指黑板、语音转文字、发音时长、非发音时长、音量、语速、指定关键词的使用等

        **对场景的要求为：**真实场景老师1人出现在画面中，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。

        **结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。

        :param request: Request instance for SubmitFullBodyClassTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitFullBodyClassTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitFullBodyClassTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitFullBodyClassTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitFullBodyClassTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitHighlights(self, request):
        """发起视频生成精彩集锦接口。该接口可以通过客户传入的课程音频数据及相关策略（如微笑抽取，专注抽取等），自动生成一堂课程的精彩集锦。需要通过QueryHighlightResult接口获取生成结果。

        :param request: Request instance for SubmitHighlights.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitHighlightsRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitHighlightsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHighlights", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHighlightsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitImageTask(self, request):
        """提交图像分析任务

        :param request: Request instance for SubmitImageTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitImageTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitImageTaskPlus(self, request):
        """高级图像分析任务，开放了图像任务里的所有开关，可以根据场景深度定制图像分析任务。支持的图像类别有，图片链接、图片二进制数据、点播链接和直播链接。

        :param request: Request instance for SubmitImageTaskPlus.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitImageTaskPlusRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitImageTaskPlusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitImageTaskPlus", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitImageTaskPlusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitOneByOneClassTask(self, request):
        """**提交在线1对1课堂任务**
        对于在线1对1课堂，老师通过视频向学生授课，并且学生人数为1人。通过上传学生端的图像信息，可以获取学生的听课情况分析。 具体指一路全局画面且背景不动，有1位学生的头像或上半身的画面，要求画面稳定清晰。

        **提供的功能接口有：**学生人脸识别、学生表情识别、语音识别。可分析的指标维度包括：学生身份识别、正脸、侧脸、抬头、低头、人脸坐标、人脸尺寸、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、语音转文字、发音时长、非发音时长、音量、语速等。

        **对场景的要求为：**真实常规1v1授课场景，学生2人以下，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。

        **结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。

        :param request: Request instance for SubmitOneByOneClassTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitOneByOneClassTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitOneByOneClassTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitOneByOneClassTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitOneByOneClassTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitOpenClassTask(self, request):
        """**提交线下小班（无课桌）课任务**
        线下小班课是指有学生无课桌的课堂，满座15人以下，全局画面且背景不动，能清晰看到。

        **提供的功能接口有：**学生人脸识别、学生表情识别、学生肢体动作识别。  可分析的指标维度包括：身份识别、正脸、侧脸、抬头、低头、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、站立、举手、坐着等。

        **对场景的要求为：**真实常规教室，满座15人以下，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上但是图像整体质量不能超过1080p。

        **结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。

        :param request: Request instance for SubmitOpenClassTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitOpenClassTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitOpenClassTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitOpenClassTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitOpenClassTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitPartialBodyClassTask(self, request):
        """**在线小班课任务**：此场景是在线授课场景，老师一般为坐着授课，摄像头可以拍摄到老师的头部及上半身。拍摄视频为一路全局画面，且背景不动，要求画面稳定清晰。通过此接口可分析老师授课的行为及语音，以支持AI评教。

        **提供的功能接口有：**老师人脸识别、老师表情识别、老师手势识别、光线识别、语音识别。 可分析的指标维度包括：身份识别、正脸、侧脸、人脸坐标、人脸尺寸、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、点赞手势、听你说手势、听我说手势、拿教具行为、语音转文字、发音时长、非发音时长、音量、语速、指定关键词的使用等

        **对场景的要求为：**在线常规授课场景，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。

        **结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。

        :param request: Request instance for SubmitPartialBodyClassTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitPartialBodyClassTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitPartialBodyClassTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitPartialBodyClassTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitPartialBodyClassTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitTraditionalClassTask(self, request):
        """**提交线下传统面授大班课（含课桌）任务。**
        传统教室课堂是指有学生课堂有课桌的课堂，满座20-50人，全局画面且背景不动。

        **提供的功能接口有：**学生人脸识别、学生表情识别、学生肢体动作识别。可分析的指标维度包括：学生身份识别、正脸、侧脸、抬头、低头、高兴、中性、高兴、中性、惊讶、厌恶、恐惧、愤怒、蔑视、悲伤、举手、站立、坐着、趴桌子、玩手机等

        **对场景的要求为：**传统的学生上课教室，满座20-50人，全局画面且背景不动；人脸上下角度在20度以内，左右角度在15度以内，歪头角度在15度以内；光照均匀，无遮挡，人脸清晰可见；像素最好在 100X100 像素以上，但是图像整体质量不能超过1080p。

        **结果查询方式：**图像任务直接返回结果，点播及直播任务通过DescribeAITaskResult查询结果。


        :param request: Request instance for SubmitTraditionalClassTask.
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitTraditionalClassTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitTraditionalClassTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTraditionalClassTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTraditionalClassTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransmitAudioStream(self, request):
        """分析音频信息

        :param request: Request instance for TransmitAudioStream.
        :type request: :class:`tencentcloud.tci.v20190318.models.TransmitAudioStreamRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.TransmitAudioStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransmitAudioStream", params, headers=headers)
            response = json.loads(body)
            model = models.TransmitAudioStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)