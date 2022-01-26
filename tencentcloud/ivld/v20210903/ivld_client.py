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
from tencentcloud.ivld.v20210903 import models


class IvldClient(AbstractClient):
    _apiVersion = '2021-09-03'
    _endpoint = 'ivld.tencentcloudapi.com'
    _service = 'ivld'


    def AddCustomPersonImage(self, request):
        """增加自定义人脸图片，每个自定义人物最多可包含5张人脸图片

        请注意，与创建自定义人物一样，图片数据优先级优于图片URL优先级

        :param request: Request instance for AddCustomPersonImage.
        :type request: :class:`tencentcloud.ivld.v20210903.models.AddCustomPersonImageRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.AddCustomPersonImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddCustomPersonImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddCustomPersonImageResponse()
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


    def CreateCustomCategory(self, request):
        """创建自定义人物分类信息

        当L2Category为空时，将创建一级自定义分类。
        当L1Category与L2Category均不为空时，将创建二级自定义分类。请注意，**只有当一级自定义分类存在时，才可创建二级自定义分类**。

        :param request: Request instance for CreateCustomCategory.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateCustomCategoryRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateCustomCategoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCustomCategory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomCategoryResponse()
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


    def CreateCustomGroup(self, request):
        """创建自定义人物库

        Bucket的格式参考为 `bucketName-123456.cos.ap-shanghai.myqcloud.com`

        在调用CreateCustomPerson和AddCustomPersonImage接口之前，请先确保本接口成功调用。当前每个用户只支持一个自定义人物库，一旦自定义人物库创建成功，后续接口调用均会返回人物库已存在错误。

        由于人脸图片对于自定义人物识别至关重要，因此自定义人物识别功能需要用户显式指定COS存储桶方可使用。具体来说，自定义人物识别功能接口(主要是CreateCustomPerson和AddCustomPersonImage)会在此COS桶下面新建IVLDCustomPersonImage目录，并在此目录下存储自定义人物图片数据以支持后续潜在的特征更新。

        请注意：本接口指定的COS桶仅用于**备份存储自定义人物图片**，CreateCustomPerson和AddCustomPersonImage接口入参URL可使用任意COS存储桶下的任意图片。

        **重要**：请务必确保本接口指定的COS存储桶存在(不要手动删除COS桶)。COS存储桶一旦指定，将不能修改。

        :param request: Request instance for CreateCustomGroup.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateCustomGroupRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateCustomGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCustomGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomGroupResponse()
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


    def CreateCustomPerson(self, request):
        """创建自定义人物。

        输入人物名称，基本信息，分类信息与人脸图片，创建自定义人物

        人脸图片可使用图片数据(base64编码的图片数据)或者图片URL(推荐使用COS以减少下载时间，其他地址也支持)，原始图片优先，也即如果同时指定了图片数据和图片URL，接口将仅使用图片数据

        :param request: Request instance for CreateCustomPerson.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateCustomPersonRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateCustomPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCustomPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomPersonResponse()
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


    def CreateDefaultCategories(self, request):
        """创建默认自定义人物类型

        :param request: Request instance for CreateDefaultCategories.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateDefaultCategoriesRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateDefaultCategoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDefaultCategories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultCategoriesResponse()
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


    def CreateTask(self, request):
        """创建智能标签任务。

        请注意，本接口为异步接口，**返回TaskId只代表任务创建成功，不代表任务执行成功**。

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskResponse()
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


    def DeleteCustomCategory(self, request):
        """删除自定义分类信息

        :param request: Request instance for DeleteCustomCategory.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomCategoryRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomCategoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCustomCategory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCustomCategoryResponse()
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


    def DeleteCustomPerson(self, request):
        """删除自定义人物

        :param request: Request instance for DeleteCustomPerson.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCustomPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCustomPersonResponse()
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


    def DeleteCustomPersonImage(self, request):
        """删除自定义人脸数据

        :param request: Request instance for DeleteCustomPersonImage.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonImageRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCustomPersonImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCustomPersonImageResponse()
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


    def DeleteMedia(self, request):
        """将MediaId对应的媒资文件从系统中删除。

        **请注意，本接口仅删除媒资文件，媒资文件对应的视频分析结果不会被删除**。如您需要删除结构化分析结果，请调用DeleteTask接口。

        :param request: Request instance for DeleteMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaResponse()
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


    def DescribeCustomCategories(self, request):
        """批量描述自定义人物分类信息

        :param request: Request instance for DescribeCustomCategories.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomCategoriesRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomCategoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomCategories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomCategoriesResponse()
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


    def DescribeCustomGroup(self, request):
        """描述自定义人物库信息，当前库大小(库中有多少人脸)，以及库中的存储桶

        :param request: Request instance for DescribeCustomGroup.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomGroupRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomGroupResponse()
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


    def DescribeCustomPersonDetail(self, request):
        """描述自定义人物详细信息，包括人物信息与人物信息

        :param request: Request instance for DescribeCustomPersonDetail.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonDetailRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomPersonDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomPersonDetailResponse()
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


    def DescribeCustomPersons(self, request):
        """批量描述自定义人物


        :param request: Request instance for DescribeCustomPersons.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonsRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomPersons", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomPersonsResponse()
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


    def DescribeMedia(self, request):
        """描述媒资文件信息，包括媒资状态，分辨率，帧率等。

        如果媒资文件未完成导入，本接口将仅输出媒资文件的状态信息；导入完成后，本接口还将输出媒资文件的其他元信息。

        :param request: Request instance for DescribeMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaResponse()
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


    def DescribeMedias(self, request):
        """依照输入条件，描述命中的媒资文件信息，包括媒资状态，分辨率，帧率等。

        请注意，本接口最多支持同时描述**50**个媒资文件

        如果媒资文件未完成导入，本接口将仅输出媒资文件的状态信息；导入完成后，本接口还将输出媒资文件的其他元信息。

        :param request: Request instance for DescribeMedias.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeMediasRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeMediasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMedias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediasResponse()
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


    def DescribeTask(self, request):
        """描述智能标签任务进度。

        请注意，**此接口仅返回任务执行状态信息，不返回任务执行结果**


        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
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


    def DescribeTaskDetail(self, request):
        """描述任务信息，如果任务成功完成，还将返回任务结果

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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


    def DescribeTasks(self, request):
        """依照输入条件，描述命中的任务信息，包括任务创建时间，处理时间信息等。

        请注意，本接口最多支持同时描述**50**个任务信息

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def ImportMedia(self, request):
        """将URL指向的媒资视频文件导入系统之中。

        **请注意，本接口为异步接口**。接口返回MediaId仅代表导入视频任务发起，不代表任务完成，您可调用读接口(DescribeMedia/DescribeMedias)接口查询MediaId对应的媒资文件的状态。

        当前URL只支持COS地址，其形式为`https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${ObjectKey}`，其中`${Bucket}`为您的COS桶名称，Region为COS桶所在[可用区](https://cloud.tencent.com/document/product/213/6091)，`${ObjectKey}`为指向存储在COS桶内的待分析的视频的[ObjectKey](https://cloud.tencent.com/document/product/436/13324)

        分析完成后，本产品将在您的`${Bucket}`桶内创建名为`${ObjectKey}-${task-start-time}`的目录(`task-start-time`形式为1970-01-01T08:08:08)并将分析结果将回传回该目录，也即，结构化分析结果(包括图片，JSON等数据)将会写回`https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${ObjectKey}-${task-start-time}`目录

        :param request: Request instance for ImportMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.ImportMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImportMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportMediaResponse()
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


    def UpdateCustomCategory(self, request):
        """更新自定义人物分类

        当L2Category为空时，代表更新CategoryId对应的一级自定义人物类型以及所有二级自定义人物类型所从属的一级自定义人物类型；
        当L2Category非空时，仅更新CategoryId对应的二级自定义人物类型

        :param request: Request instance for UpdateCustomCategory.
        :type request: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomCategoryRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomCategoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCustomCategory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCustomCategoryResponse()
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


    def UpdateCustomPerson(self, request):
        """更新自定义人物信息，包括姓名，简要信息，分类信息等

        :param request: Request instance for UpdateCustomPerson.
        :type request: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomPersonRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCustomPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCustomPersonResponse()
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