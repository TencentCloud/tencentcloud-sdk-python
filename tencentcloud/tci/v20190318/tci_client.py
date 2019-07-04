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
from tencentcloud.tci.v20190318 import models


class TciClient(AbstractClient):
    _apiVersion = '2019-03-18'
    _endpoint = 'tci.tencentcloudapi.com'


    def AIAssistant(self, request):
        """提供 AI 助教基础版本功能接口

        :param request: 调用AIAssistant所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.AIAssistantRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.AIAssistantResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AIAssistant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AIAssistantResponse()
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


    def CancelTask(self, request):
        """用于取消已经提交的任务

        :param request: 调用CancelTask所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
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


    def CheckAttendance(self, request):
        """人员考勤

        :param request: 调用CheckAttendance所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.CheckAttendanceRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CheckAttendanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckAttendance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAttendanceResponse()
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


    def CheckFacePhoto(self, request):
        """检查人脸图片是否合法

        :param request: 调用CheckFacePhoto所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.CheckFacePhotoRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CheckFacePhotoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckFacePhoto", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckFacePhotoResponse()
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


    def CreateFace(self, request):
        """创建人脸

        :param request: 调用CreateFace所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateFaceRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFaceResponse()
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


    def CreateLibrary(self, request):
        """创建人员库

        :param request: 调用CreateLibrary所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateLibraryRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateLibraryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLibrary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLibraryResponse()
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


    def CreateVocab(self, request):
        """创建词汇

        :param request: 调用CreateVocab所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateVocabRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVocabResponse()
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


    def CreateVocabLib(self, request):
        """建立词汇库

        :param request: 调用CreateVocabLib所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.CreateVocabLibRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.CreateVocabLibResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVocabLib", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVocabLibResponse()
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


    def DeleteFace(self, request):
        """删除人脸

        :param request: 调用DeleteFace所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteFaceRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFaceResponse()
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


    def DeleteLibrary(self, request):
        """删除人员库

        :param request: 调用DeleteLibrary所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteLibraryRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteLibraryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLibrary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLibraryResponse()
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


    def DeletePerson(self, request):
        """删除人员

        :param request: 调用DeletePerson所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeletePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonResponse()
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


    def DeleteVocab(self, request):
        """删除词汇

        :param request: 调用DeleteVocab所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteVocabRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVocabResponse()
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


    def DeleteVocabLib(self, request):
        """删除词汇库

        :param request: 调用DeleteVocabLib所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DeleteVocabLibRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DeleteVocabLibResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVocabLib", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVocabLibResponse()
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


    def DescribeAITaskResult(self, request):
        """获取标准化接口任务结果

        :param request: 调用DescribeAITaskResult所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeAITaskResultRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeAITaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAITaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAITaskResultResponse()
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


    def DescribeAttendanceResult(self, request):
        """人脸考勤查询结果

        :param request: 调用DescribeAttendanceResult所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeAttendanceResultRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeAttendanceResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAttendanceResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAttendanceResultResponse()
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


    def DescribeAudioTask(self, request):
        """音频评估任务信息查询接口，异步查询客户提交的请求的结果。

        :param request: 调用DescribeAudioTask所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeAudioTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeAudioTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAudioTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAudioTaskResponse()
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


    def DescribeConversationTask(self, request):
        """音频对话任务评估任务信息查询接口，异步查询客户提交的请求的结果。

        :param request: 调用DescribeConversationTask所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeConversationTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeConversationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConversationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConversationTaskResponse()
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


    def DescribeHighlightResult(self, request):
        """视频精彩集锦结果查询接口，异步查询客户提交的请求的结果。

        :param request: 调用DescribeHighlightResult所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeHighlightResultRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeHighlightResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHighlightResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHighlightResultResponse()
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


    def DescribeImageTask(self, request):
        """拉取任务详情

        :param request: 调用DescribeImageTask所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageTaskResponse()
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


    def DescribeImageTaskStatistic(self, request):
        """获取图像任务统计信息

        :param request: 调用DescribeImageTaskStatistic所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskStatisticRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeImageTaskStatisticResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageTaskStatistic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageTaskStatisticResponse()
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


    def DescribeLibraries(self, request):
        """获取人员库列表

        :param request: 调用DescribeLibraries所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeLibrariesRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeLibrariesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLibraries", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLibrariesResponse()
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


    def DescribePerson(self, request):
        """获取人员详情

        :param request: 调用DescribePerson所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribePersonRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribePersonResponse`

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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersons(self, request):
        """拉取人员列表

        :param request: 调用DescribePersons所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribePersonsRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribePersonsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersons", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonsResponse()
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


    def DescribeVocab(self, request):
        """查询词汇

        :param request: 调用DescribeVocab所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeVocabRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVocabResponse()
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


    def DescribeVocabLib(self, request):
        """查询词汇库

        :param request: 调用DescribeVocabLib所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.DescribeVocabLibRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.DescribeVocabLibResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVocabLib", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVocabLibResponse()
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


    def ModifyLibrary(self, request):
        """修改人员库信息

        :param request: 调用ModifyLibrary所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.ModifyLibraryRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.ModifyLibraryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLibrary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLibraryResponse()
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


    def ModifyPerson(self, request):
        """修改人员信息

        :param request: 调用ModifyPerson所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.ModifyPersonRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.ModifyPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonResponse()
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


    def SubmitAudioTask(self, request):
        """音频任务提交接口

        :param request: 调用SubmitAudioTask所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitAudioTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitAudioTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitAudioTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitAudioTaskResponse()
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


    def SubmitCheckAttendanceTask(self, request):
        """提交人员考勤任务

        :param request: 调用SubmitCheckAttendanceTask所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitCheckAttendanceTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitCheckAttendanceTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitCheckAttendanceTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitCheckAttendanceTaskResponse()
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


    def SubmitDoubleVideoHighlights(self, request):
        """发起双路视频生成精彩集锦接口。该接口可以通过客户传入的学生音视频及老师视频两路Url，自动生成一堂课程的精彩集锦。需要通过SubmitDoubleVideoHighlights接口获取生成结果。

        :param request: 调用SubmitDoubleVideoHighlights所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitDoubleVideoHighlightsRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitDoubleVideoHighlightsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitDoubleVideoHighlights", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitDoubleVideoHighlightsResponse()
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


    def SubmitHighlights(self, request):
        """发起视频生成精彩集锦接口。该接口可以通过客户传入的课程音频数据及相关策略（如微笑抽取，专注抽取等），自动生成一堂课程的精彩集锦。需要通过QueryHighlightResult接口获取生成结果。

        :param request: 调用SubmitHighlights所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitHighlightsRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitHighlightsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitHighlights", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitHighlightsResponse()
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


    def SubmitImageTask(self, request):
        """提交图像分析任务

        :param request: 调用SubmitImageTask所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.SubmitImageTaskRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.SubmitImageTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitImageTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitImageTaskResponse()
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


    def TransmitAudioStream(self, request):
        """分析音频信息

        :param request: 调用TransmitAudioStream所需参数的结构体。
        :type request: :class:`tencentcloud.tci.v20190318.models.TransmitAudioStreamRequest`
        :rtype: :class:`tencentcloud.tci.v20190318.models.TransmitAudioStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransmitAudioStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransmitAudioStreamResponse()
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