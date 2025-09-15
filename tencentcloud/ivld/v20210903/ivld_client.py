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
from tencentcloud.ivld.v20210903 import models


class IvldClient(AbstractClient):
    _apiVersion = '2021-09-03'
    _endpoint = 'ivld.tencentcloudapi.com'
    _service = 'ivld'


    def AddCustomPersonImage(self, request):
        r"""增加自定义人脸图片，每个自定义人物最多可包含10张人脸图片

        请注意，与创建自定义人物一样，图片数据优先级优于图片URL优先级

        :param request: Request instance for AddCustomPersonImage.
        :type request: :class:`tencentcloud.ivld.v20210903.models.AddCustomPersonImageRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.AddCustomPersonImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCustomPersonImage", params, headers=headers)
            response = json.loads(body)
            model = models.AddCustomPersonImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomCategory(self, request):
        r"""创建自定义人物分类信息

        当L2Category为空时，将创建一级自定义分类。
        当L1Category与L2Category均不为空时，将创建二级自定义分类。请注意，**只有当一级自定义分类存在时，才可创建二级自定义分类**。

        :param request: Request instance for CreateCustomCategory.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateCustomCategoryRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateCustomCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomCategory", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomGroup(self, request):
        r"""创建自定义人物库

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
            headers = request.headers
            body = self.call("CreateCustomGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomPerson(self, request):
        r"""创建自定义人物。

        输入人物名称，基本信息，分类信息与人脸图片，创建自定义人物

        人脸图片可使用图片数据(base64编码的图片数据)或者图片URL(推荐使用COS以减少下载时间，其他地址也支持)，原始图片优先，也即如果同时指定了图片数据和图片URL，接口将仅使用图片数据

        :param request: Request instance for CreateCustomPerson.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateCustomPersonRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateCustomPersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomPerson", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomPersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDefaultCategories(self, request):
        r"""创建默认自定义人物类型

        :param request: Request instance for CreateDefaultCategories.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateDefaultCategoriesRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateDefaultCategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefaultCategories", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDefaultCategoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        r"""创建智能标签任务。

        请注意，本接口为异步接口，**返回TaskId只代表任务创建成功，不代表任务执行成功**。

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoSummaryTask(self, request):
        r"""创建一个视频缩编任务。

        ### 回调事件消息通知协议

        #### 网络协议
        - 回调接口协议目前仅支持http/https协议；
        - 请求：HTTP POST 请求，包体内容为 JSON，每一种消息的具体包体内容参见后文。
        - 应答：HTTP STATUS CODE = 200，服务端忽略应答包具体内容，为了协议友好，建议客户应答内容携带 JSON： `{"code":0}`

        #### 通知可靠性

        事件通知服务具备重试能力，事件通知失败后会总计重试3次；
        为了避免重试对您的服务器以及网络带宽造成冲击，请保持正常回包。触发重试条件如下：
        - 长时间（5 秒）未回包应答。
        - 应答 HTTP STATUS 不为200。


        #### 回调接口协议

        ##### 分析任务完成消息回调
        | 参数名称 | 必选 | 类型 | 描述 |
        |---------|---------|---------|---------|
        | TaskId | 是 | String | 任务ID |
        | TaskStatus | 是 | Integer | 任务执行状态 |
        | FailedReason | 是 | String | 若任务失败，该字段为失败原因 |

        :param request: Request instance for CreateVideoSummaryTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.CreateVideoSummaryTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.CreateVideoSummaryTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoSummaryTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoSummaryTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomCategory(self, request):
        r"""删除自定义分类信息

        :param request: Request instance for DeleteCustomCategory.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomCategoryRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomCategory", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomPerson(self, request):
        r"""删除自定义人物

        :param request: Request instance for DeleteCustomPerson.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomPerson", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomPersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomPersonImage(self, request):
        r"""删除自定义人脸数据

        :param request: Request instance for DeleteCustomPersonImage.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonImageRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteCustomPersonImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomPersonImage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomPersonImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMedia(self, request):
        r"""将MediaId对应的媒资文件从系统中删除。

        **请注意，本接口仅删除媒资文件，媒资文件对应的视频分析结果不会被删除**。如您需要删除结构化分析结果，请调用DeleteTask接口。

        :param request: Request instance for DeleteMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMedia", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        r"""删除任务信息

        请注意，本接口**不会**删除媒资文件

        只有已完成(成功或者失败)的任务可以删除，**正在执行中的任务不支持删除**

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomCategories(self, request):
        r"""批量描述自定义人物分类信息

        :param request: Request instance for DescribeCustomCategories.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomCategoriesRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomCategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomCategories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomCategoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomGroup(self, request):
        r"""描述自定义人物库信息，当前库大小(库中有多少人脸)，以及库中的存储桶

        :param request: Request instance for DescribeCustomGroup.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomGroupRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomPersonDetail(self, request):
        r"""描述自定义人物详细信息，包括人物信息与人物信息

        :param request: Request instance for DescribeCustomPersonDetail.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonDetailRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomPersonDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomPersonDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomPersons(self, request):
        r"""批量描述自定义人物

        :param request: Request instance for DescribeCustomPersons.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonsRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeCustomPersonsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomPersons", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomPersonsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMedia(self, request):
        r"""描述媒资文件信息，包括媒资状态，分辨率，帧率等。

        如果媒资文件未完成导入，本接口将仅输出媒资文件的状态信息；导入完成后，本接口还将输出媒资文件的其他元信息。

        :param request: Request instance for DescribeMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMedia", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMedias(self, request):
        r"""依照输入条件，描述命中的媒资文件信息，包括媒资状态，分辨率，帧率等。

        请注意，本接口最多支持同时描述**50**个媒资文件

        如果媒资文件未完成导入，本接口将仅输出媒资文件的状态信息；导入完成后，本接口还将输出媒资文件的其他元信息。

        :param request: Request instance for DescribeMedias.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeMediasRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeMediasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMedias", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMediasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTask(self, request):
        r"""描述智能标签任务进度。

        请注意，**此接口仅返回任务执行状态信息，不返回任务执行结果**

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        r"""描述任务信息，如果任务成功完成，还将返回任务结果

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        r"""依照输入条件，描述命中的任务信息，包括任务创建时间，处理时间信息等。

        请注意，本接口最多支持同时描述**50**个任务信息

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsageAmount(self, request):
        r"""获取用户资源使用量

        :param request: Request instance for DescribeUsageAmount.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeUsageAmountRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeUsageAmountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsageAmount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageAmountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoSummaryDetail(self, request):
        r"""描述任务信息，如果任务成功完成，还将返回任务结果

        :param request: Request instance for DescribeVideoSummaryDetail.
        :type request: :class:`tencentcloud.ivld.v20210903.models.DescribeVideoSummaryDetailRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.DescribeVideoSummaryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoSummaryDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoSummaryDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportMedia(self, request):
        r"""将URL指向的媒资视频文件导入系统之中。

        **请注意，本接口为异步接口**。接口返回MediaId仅代表导入视频任务发起，不代表任务完成，您可调用读接口(DescribeMedia/DescribeMedias)接口查询MediaId

        URL字段推荐您使用COS地址，其形式为`https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${ObjectKey}`，其中`${Bucket}`为您的COS桶名称，Region为COS桶所在[可用区](https://cloud.tencent.com/document/product/213/6091)，`${ObjectKey}`为指向存储在COS桶内的待分析的视频的[ObjectKey](https://cloud.tencent.com/document/product/436/13324)

        另外，目前产品也支持使用外部URL地址，但是当传入URL为非COS地址时，需要您指定额外的WriteBackCosPath以供产品回写结果数据。

        分析完成后，本产品将在您的`${Bucket}`桶内创建名为`${ObjectKey}_${task-create-time}`的目录(`task-create-time`形式为1970-01-01T08:08:08)并将分析结果将回传回该目录，也即，结构化分析结果(包括图片，JSON等数据)将会写回`https://${Bucket}-${AppId}.cos.${Region}.myqcloud.com/${ObjectKey}_${task-create-time}`目录

        :param request: Request instance for ImportMedia.
        :type request: :class:`tencentcloud.ivld.v20210903.models.ImportMediaRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ImportMediaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportMedia", params, headers=headers)
            response = json.loads(body)
            model = models.ImportMediaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCallback(self, request):
        r"""用户设置对应事件的回调地址

        ### 回调事件消息通知协议

        #### 网络协议
        - 回调接口协议目前仅支持http/https协议；
        - 请求：HTTP POST 请求，包体内容为 JSON，每一种消息的具体包体内容参见后文。
        - 应答：HTTP STATUS CODE = 200，服务端忽略应答包具体内容，为了协议友好，建议客户应答内容携带 JSON： `{"code":0}`

        #### 通知可靠性

        事件通知服务具备重试能力，事件通知失败后会总计重试3次；
        为了避免重试对您的服务器以及网络带宽造成冲击，请保持正常回包。触发重试条件如下：
        - 长时间（5 秒）未回包应答。
        - 应答 HTTP STATUS 不为200。


        #### 回调接口协议

        ##### 分析任务完成消息回调
        | 参数名称 | 必选 | 类型 | 描述 |
        |---------|---------|---------|---------|
        | EventType | 是 | int | 回调时间类型，1-任务分析完成，2-媒资导入完成 |
        | TaskId | 是 | String | 任务ID |
        | TaskStatus | 是 | [TaskStatus](/document/product/1509/65063#TaskInfo) | 任务执行状态 |
        | FailedReason | 是 | String | 若任务失败，该字段为失败原因 |


        ##### 导入媒资完成消息回调
        | 参数名称 | 必选 | 类型 | 描述 |
        |---------|---------|---------|---------|
        | EventType | 是 | int | 回调时间类型，1-任务分析完成，2-媒资导入完成 |
        | MediaId | 是 | String | 媒资ID |
        | MediaStatus | 是 | [MediaStatus](/document/product/1509/65063#MediaInfo) | 媒资导入状态|
        | FailedReason | 是 | String | 若任务失败，该字段为失败原因 |

        :param request: Request instance for ModifyCallback.
        :type request: :class:`tencentcloud.ivld.v20210903.models.ModifyCallbackRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.ModifyCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCallback", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCallback(self, request):
        r"""查询用户回调设置

        :param request: Request instance for QueryCallback.
        :type request: :class:`tencentcloud.ivld.v20210903.models.QueryCallbackRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.QueryCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCallback", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCustomCategory(self, request):
        r"""更新自定义人物分类

        当L2Category为空时，代表更新CategoryId对应的一级自定义人物类型以及所有二级自定义人物类型所从属的一级自定义人物类型；
        当L2Category非空时，仅更新CategoryId对应的二级自定义人物类型

        :param request: Request instance for UpdateCustomCategory.
        :type request: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomCategoryRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCustomCategory", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCustomCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCustomPerson(self, request):
        r"""更新自定义人物信息，包括姓名，简要信息，分类信息等

        :param request: Request instance for UpdateCustomPerson.
        :type request: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomPersonRequest`
        :rtype: :class:`tencentcloud.ivld.v20210903.models.UpdateCustomPersonResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCustomPerson", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCustomPersonResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))