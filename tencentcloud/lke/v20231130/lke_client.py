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
from tencentcloud.lke.v20231130 import models


class LkeClient(AbstractClient):
    _apiVersion = '2023-11-30'
    _endpoint = 'lke.tencentcloudapi.com'
    _service = 'lke'


    def CheckAttributeLabelExist(self, request):
        """检查属性下的标签名是否存在

        :param request: Request instance for CheckAttributeLabelExist.
        :type request: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelExistRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAttributeLabelExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAttributeLabelExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAttributeLabelRefer(self, request):
        """检查属性标签引用

        :param request: Request instance for CheckAttributeLabelRefer.
        :type request: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelReferRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CheckAttributeLabelReferResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAttributeLabelRefer", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAttributeLabelReferResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConvertDocument(self, request):
        """产品规划

        接口支持图片和PDF转可编辑word格式文件，将文件中的图片、文本、表格等元素识别，并根据位置进行还原。

        :param request: Request instance for ConvertDocument.
        :type request: :class:`tencentcloud.lke.v20231130.models.ConvertDocumentRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ConvertDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConvertDocument", params, headers=headers)
            response = json.loads(body)
            model = models.ConvertDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApp(self, request):
        """创建知识引擎应用。

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAttributeLabel(self, request):
        """创建标签

        :param request: Request instance for CreateAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCorp(self, request):
        """创建企业

        :param request: Request instance for CreateCorp.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateCorpRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateCorpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCorp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCorpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDocCate(self, request):
        """创建Doc分类

        :param request: Request instance for CreateDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQA(self, request):
        """录入问答

        :param request: Request instance for CreateQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQA", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateQACate(self, request):
        """创建QA分类

        :param request: Request instance for CreateQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQACate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRejectedQuestion(self, request):
        """创建拒答问题

        :param request: Request instance for CreateRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRelease(self, request):
        """创建发布

        :param request: Request instance for CreateRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRelease", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSharedKnowledge(self, request):
        """创建共享知识库。

        :param request: Request instance for CreateSharedKnowledge.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateSharedKnowledgeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateSharedKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSharedKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSharedKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVar(self, request):
        """创建变量

        :param request: Request instance for CreateVar.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateVarRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateVarResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVar", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVarResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflowRun(self, request):
        """本接口用来创建工作流的异步运行实例，创建成功后工作流会在后台异步运行，接口返回工作流运行实例ID（WorkflowRunId）等信息。后面可通过调用DescribeWorkflowRun接口查工作流运行的详情。
        注意：工作流的异步运行是基于应用的，需要先把对应的应用配置成“单工作流模式”，并且打开“异步调用”的开关，才能创建成功。

        :param request: Request instance for CreateWorkflowRun.
        :type request: :class:`tencentcloud.lke.v20231130.models.CreateWorkflowRunRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.CreateWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApp(self, request):
        """删除应用

        :param request: Request instance for DeleteApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAttributeLabel(self, request):
        """删除属性标签

        :param request: Request instance for DeleteAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDoc(self, request):
        """删除文档

        :param request: Request instance for DeleteDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDoc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDocCate(self, request):
        """Doc分类删除

        :param request: Request instance for DeleteDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQA(self, request):
        """删除问答

        :param request: Request instance for DeleteQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQA", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteQACate(self, request):
        """分类删除

        :param request: Request instance for DeleteQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQACate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRejectedQuestion(self, request):
        """删除拒答问题

        :param request: Request instance for DeleteRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSharedKnowledge(self, request):
        """删除共享知识库。

        :param request: Request instance for DeleteSharedKnowledge.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteSharedKnowledgeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteSharedKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSharedKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSharedKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVar(self, request):
        """删除变量

        :param request: Request instance for DeleteVar.
        :type request: :class:`tencentcloud.lke.v20231130.models.DeleteVarRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DeleteVarResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVar", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVarResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApp(self, request):
        """获取企业下应用详情

        :param request: Request instance for DescribeApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttributeLabel(self, request):
        """查询属性标签详情

        :param request: Request instance for DescribeAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallStatsGraph(self, request):
        """接口调用折线图

        :param request: Request instance for DescribeCallStatsGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeCallStatsGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeCallStatsGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallStatsGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallStatsGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrencyUsage(self, request):
        """并发调用响应

        :param request: Request instance for DescribeConcurrencyUsage.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrencyUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrencyUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConcurrencyUsageGraph(self, request):
        """并发调用折线图

        :param request: Request instance for DescribeConcurrencyUsageGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeConcurrencyUsageGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConcurrencyUsageGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConcurrencyUsageGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCorp(self, request):
        """企业详情

        :param request: Request instance for DescribeCorp.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeCorpRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeCorpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCorp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCorpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDoc(self, request):
        """文档详情

        :param request: Request instance for DescribeDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDoc", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeUsage(self, request):
        """查询知识库用量

        :param request: Request instance for DescribeKnowledgeUsage.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsageRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKnowledgeUsagePieGraph(self, request):
        """查询企业知识库容量饼图

        :param request: Request instance for DescribeKnowledgeUsagePieGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsagePieGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeKnowledgeUsagePieGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKnowledgeUsagePieGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKnowledgeUsagePieGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNodeRun(self, request):
        """通过DescribeWorkflowRun接口获取了工作流异步运行的整体内容，其中包含了基本的节点信息，再通用本接口可查看节点的运行详情（包括输入、输出、日志等）。

        :param request: Request instance for DescribeNodeRun.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeNodeRunRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeNodeRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNodeRun", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQA(self, request):
        """问答详情

        :param request: Request instance for DescribeQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQA", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRefer(self, request):
        """获取来源详情列表

        :param request: Request instance for DescribeRefer.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeReferRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeReferResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRefer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReferResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRelease(self, request):
        """发布详情

        :param request: Request instance for DescribeRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelease", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReleaseInfo(self, request):
        """拉取发布按钮状态、最后发布时间

        :param request: Request instance for DescribeReleaseInfo.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseInfoRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeReleaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReleaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReleaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRobotBizIDByAppKey(self, request):
        """通过appKey获取应用业务ID

        :param request: Request instance for DescribeRobotBizIDByAppKey.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeRobotBizIDByAppKeyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeRobotBizIDByAppKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRobotBizIDByAppKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRobotBizIDByAppKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchStatsGraph(self, request):
        """查询搜索服务调用折线图

        :param request: Request instance for DescribeSearchStatsGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeSearchStatsGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeSearchStatsGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchStatsGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchStatsGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSegments(self, request):
        """获取片段详情

        :param request: Request instance for DescribeSegments.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeSegmentsRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeSegmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSegments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSegmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSharedKnowledge(self, request):
        """查询共享知识库。

        :param request: Request instance for DescribeSharedKnowledge.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeSharedKnowledgeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeSharedKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSharedKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSharedKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorageCredential(self, request):
        """获取文件上传临时密钥

        :param request: Request instance for DescribeStorageCredential.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeStorageCredentialRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeStorageCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorageCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenUsage(self, request):
        """接口调用token详情

        :param request: Request instance for DescribeTokenUsage.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenUsageGraph(self, request):
        """接口调用token折线图

        :param request: Request instance for DescribeTokenUsageGraph.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageGraphRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeTokenUsageGraphResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenUsageGraph", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenUsageGraphResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnsatisfiedReplyContext(self, request):
        """获取不满意回复上下文

        :param request: Request instance for DescribeUnsatisfiedReplyContext.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeUnsatisfiedReplyContextRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeUnsatisfiedReplyContextResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnsatisfiedReplyContext", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnsatisfiedReplyContextResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowRun(self, request):
        """创建了工作流的异步运行实例后，通过本接口可以查询整体的运行详情。

        :param request: Request instance for DescribeWorkflowRun.
        :type request: :class:`tencentcloud.lke.v20231130.models.DescribeWorkflowRunRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.DescribeWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAttributeLabel(self, request):
        """导出属性标签

        :param request: Request instance for ExportAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ExportAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExportAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportQAList(self, request):
        """导出QA列表

        :param request: Request instance for ExportQAList.
        :type request: :class:`tencentcloud.lke.v20231130.models.ExportQAListRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExportQAListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportQAList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportQAListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportUnsatisfiedReply(self, request):
        """导出不满意回复

        :param request: Request instance for ExportUnsatisfiedReply.
        :type request: :class:`tencentcloud.lke.v20231130.models.ExportUnsatisfiedReplyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ExportUnsatisfiedReplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportUnsatisfiedReply", params, headers=headers)
            response = json.loads(body)
            model = models.ExportUnsatisfiedReplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateQA(self, request):
        """文档生成问答

        :param request: Request instance for GenerateQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.GenerateQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GenerateQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateQA", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAnswerTypeDataCount(self, request):
        """回答类型数据统计

        :param request: Request instance for GetAnswerTypeDataCount.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetAnswerTypeDataCountRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetAnswerTypeDataCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAnswerTypeDataCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAnswerTypeDataCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAppKnowledgeCount(self, request):
        """获取模型列表

        :param request: Request instance for GetAppKnowledgeCount.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetAppKnowledgeCountRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetAppKnowledgeCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAppKnowledgeCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAppKnowledgeCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAppSecret(self, request):
        """获取应用密钥

        :param request: Request instance for GetAppSecret.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetAppSecretRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetAppSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAppSecret", params, headers=headers)
            response = json.loads(body)
            model = models.GetAppSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDocPreview(self, request):
        """获取文档预览信息

        :param request: Request instance for GetDocPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetDocPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetDocPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDocPreview", params, headers=headers)
            response = json.loads(body)
            model = models.GetDocPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmbedding(self, request):
        """本接口（GetEmbedding）调用文本表示模型，将文本转化为用数值表示的向量形式，可用于文本检索、信息推荐、知识挖掘等场景。
        开通[产品体验](https://lke.cloud.tencent.com/lke/#/trialProduct)后可获得50wtoken体验额度。
        本接口（GetEmbedding）有单账号调用上限控制，如您有提高并发限制的需求请 [联系我们](https://cloud.tencent.com/act/event/Online_service) 。

        :param request: Request instance for GetEmbedding.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetEmbeddingRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.GetEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLikeDataCount(self, request):
        """点赞点踩数据统计

        :param request: Request instance for GetLikeDataCount.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetLikeDataCountRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetLikeDataCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLikeDataCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetLikeDataCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMsgRecord(self, request):
        """获取聊天历史
        根据会话session id获取聊天历史（仅保留180天内的历史对话数据）

        :param request: Request instance for GetMsgRecord.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetMsgRecordRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetMsgRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMsgRecord", params, headers=headers)
            response = json.loads(body)
            model = models.GetMsgRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetReconstructDocumentResult(self, request):
        """本接口为异步接口的查询结果接口，用于获取文档解析处理结果。

        :param request: Request instance for GetReconstructDocumentResult.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetReconstructDocumentResultRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetReconstructDocumentResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetReconstructDocumentResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetReconstructDocumentResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskStatus(self, request):
        """获取任务状态

        :param request: Request instance for GetTaskStatus.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetTaskStatusRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetVarList(self, request):
        """查询自定义变量列表

        :param request: Request instance for GetVarList.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetVarListRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetVarListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetVarList", params, headers=headers)
            response = json.loads(body)
            model = models.GetVarListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetWsToken(self, request):
        """获取ws token

        :param request: Request instance for GetWsToken.
        :type request: :class:`tencentcloud.lke.v20231130.models.GetWsTokenRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GetWsTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetWsToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetWsTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GroupDoc(self, request):
        """Doc分组

        :param request: Request instance for GroupDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.GroupDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GroupDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GroupDoc", params, headers=headers)
            response = json.loads(body)
            model = models.GroupDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GroupQA(self, request):
        """QA分组

        :param request: Request instance for GroupQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.GroupQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.GroupQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GroupQA", params, headers=headers)
            response = json.loads(body)
            model = models.GroupQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnoreUnsatisfiedReply(self, request):
        """忽略不满意回复

        :param request: Request instance for IgnoreUnsatisfiedReply.
        :type request: :class:`tencentcloud.lke.v20231130.models.IgnoreUnsatisfiedReplyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.IgnoreUnsatisfiedReplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreUnsatisfiedReply", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreUnsatisfiedReplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsTransferIntent(self, request):
        """是否意图转人工

        :param request: Request instance for IsTransferIntent.
        :type request: :class:`tencentcloud.lke.v20231130.models.IsTransferIntentRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.IsTransferIntentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsTransferIntent", params, headers=headers)
            response = json.loads(body)
            model = models.IsTransferIntentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListApp(self, request):
        """获取企业下应用列表

        :param request: Request instance for ListApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListApp", params, headers=headers)
            response = json.loads(body)
            model = models.ListAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAppCategory(self, request):
        """应用类型列表

        :param request: Request instance for ListAppCategory.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAppCategoryRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAppCategoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAppCategory", params, headers=headers)
            response = json.loads(body)
            model = models.ListAppCategoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAppKnowledgeDetail(self, request):
        """列表查询知识库容量详情

        :param request: Request instance for ListAppKnowledgeDetail.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAppKnowledgeDetailRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAppKnowledgeDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAppKnowledgeDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ListAppKnowledgeDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAttributeLabel(self, request):
        """查询属性标签列表

        :param request: Request instance for ListAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ListAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDoc(self, request):
        """文档列表

        :param request: Request instance for ListDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ListDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDocCate(self, request):
        """获取Doc分类

        :param request: Request instance for ListDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.ListDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListModel(self, request):
        """获取模型列表

        :param request: Request instance for ListModel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListModelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListModel", params, headers=headers)
            response = json.loads(body)
            model = models.ListModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListQA(self, request):
        """问答列表

        :param request: Request instance for ListQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListQA", params, headers=headers)
            response = json.loads(body)
            model = models.ListQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListQACate(self, request):
        """获取QA分类

        :param request: Request instance for ListQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListQACate", params, headers=headers)
            response = json.loads(body)
            model = models.ListQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReferShareKnowledge(self, request):
        """查看应用引用了哪些共享知识库，可以看到共享知识库的基础信息，包括名称，id等

        :param request: Request instance for ListReferShareKnowledge.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReferShareKnowledgeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReferShareKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReferShareKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.ListReferShareKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRejectedQuestion(self, request):
        """获取拒答问题

        :param request: Request instance for ListRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.ListRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRejectedQuestionPreview(self, request):
        """发布拒答问题预览

        :param request: Request instance for ListRejectedQuestionPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListRejectedQuestionPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRejectedQuestionPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListRejectedQuestionPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRelease(self, request):
        """发布列表

        :param request: Request instance for ListRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRelease", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReleaseConfigPreview(self, request):
        """发布配置项预览

        :param request: Request instance for ListReleaseConfigPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseConfigPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseConfigPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReleaseConfigPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseConfigPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReleaseDocPreview(self, request):
        """发布文档预览

        :param request: Request instance for ListReleaseDocPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseDocPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseDocPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReleaseDocPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseDocPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReleaseQAPreview(self, request):
        """文档列表

        :param request: Request instance for ListReleaseQAPreview.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListReleaseQAPreviewRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListReleaseQAPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReleaseQAPreview", params, headers=headers)
            response = json.loads(body)
            model = models.ListReleaseQAPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSelectDoc(self, request):
        """获取账户信息

        :param request: Request instance for ListSelectDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListSelectDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListSelectDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSelectDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ListSelectDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSharedKnowledge(self, request):
        """列举共享知识库。

        :param request: Request instance for ListSharedKnowledge.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListSharedKnowledgeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListSharedKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSharedKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.ListSharedKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUnsatisfiedReply(self, request):
        """查询不满意回复列表

        :param request: Request instance for ListUnsatisfiedReply.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListUnsatisfiedReplyRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListUnsatisfiedReplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUnsatisfiedReply", params, headers=headers)
            response = json.loads(body)
            model = models.ListUnsatisfiedReplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListUsageCallDetail(self, request):
        """列表查询单次调用明细

        :param request: Request instance for ListUsageCallDetail.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListUsageCallDetailRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListUsageCallDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListUsageCallDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ListUsageCallDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListWorkflowRuns(self, request):
        """此接口可查询已创建的所有工作流异步运行实例。

        :param request: Request instance for ListWorkflowRuns.
        :type request: :class:`tencentcloud.lke.v20231130.models.ListWorkflowRunsRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ListWorkflowRunsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListWorkflowRuns", params, headers=headers)
            response = json.loads(body)
            model = models.ListWorkflowRunsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApp(self, request):
        """修改应用请求结构体

        :param request: Request instance for ModifyApp.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyAppRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyAppResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAttributeLabel(self, request):
        """编辑属性标签

        :param request: Request instance for ModifyAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDoc(self, request):
        """修改文档

        :param request: Request instance for ModifyDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDocAttrRange(self, request):
        """批量修改文档适用范围

        :param request: Request instance for ModifyDocAttrRange.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyDocAttrRangeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyDocAttrRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDocAttrRange", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDocAttrRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDocCate(self, request):
        """修改Doc分类

        :param request: Request instance for ModifyDocCate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyDocCateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyDocCateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDocCate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDocCateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQA(self, request):
        """更新问答

        :param request: Request instance for ModifyQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQA", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQAAttrRange(self, request):
        """批量修改问答适用范围

        :param request: Request instance for ModifyQAAttrRange.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyQAAttrRangeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyQAAttrRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQAAttrRange", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQAAttrRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyQACate(self, request):
        """更新QA分类

        :param request: Request instance for ModifyQACate.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyQACateRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyQACateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyQACate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyQACateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRejectedQuestion(self, request):
        """修改拒答问题

        :param request: Request instance for ModifyRejectedQuestion.
        :type request: :class:`tencentcloud.lke.v20231130.models.ModifyRejectedQuestionRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ModifyRejectedQuestionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRejectedQuestion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRejectedQuestionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryRewrite(self, request):
        """多轮改写（QueryRewrite）主要用于多轮对话中，进行指代消解和省略补全。使用本接口，无需输入prompt描述，根据对话历史即可生成更精确的用户查询。在应用场景上，本接口可应用于智能问答、对话式搜索等多种场景。
        开通[产品体验](https://lke.cloud.tencent.com/lke/#/trialProduct)后可获得50wtoken体验额度。本接口（QueryRewrite）有单账号调用上限控制，如您有提高并发限制的需求请 [联系我们](https://cloud.tencent.com/act/event/Online_service) 。

        :param request: Request instance for QueryRewrite.
        :type request: :class:`tencentcloud.lke.v20231130.models.QueryRewriteRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.QueryRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.QueryRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RateMsgRecord(self, request):
        """点赞点踩消息

        :param request: Request instance for RateMsgRecord.
        :type request: :class:`tencentcloud.lke.v20231130.models.RateMsgRecordRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RateMsgRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RateMsgRecord", params, headers=headers)
            response = json.loads(body)
            model = models.RateMsgRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReconstructDocument(self, request):
        """支持将图片或PDF文件转换成Markdown格式文件，可解析包括表格、公式、图片、标题、段落、页眉、页脚等内容元素，并将内容智能转换成阅读顺序。

        体验期间单账号限制qps仅为1，若有正式接入需要请与产研团队沟通开放。

        :param request: Request instance for ReconstructDocument.
        :type request: :class:`tencentcloud.lke.v20231130.models.ReconstructDocumentRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ReconstructDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReconstructDocument", params, headers=headers)
            response = json.loads(body)
            model = models.ReconstructDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReferShareKnowledge(self, request):
        """应用引用共享知识库，可以引用一个或多个，每次都是全量覆盖

        :param request: Request instance for ReferShareKnowledge.
        :type request: :class:`tencentcloud.lke.v20231130.models.ReferShareKnowledgeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.ReferShareKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReferShareKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.ReferShareKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameDoc(self, request):
        """文档重命名

        :param request: Request instance for RenameDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.RenameDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RenameDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameDoc", params, headers=headers)
            response = json.loads(body)
            model = models.RenameDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryDocAudit(self, request):
        """文档解析重试

        :param request: Request instance for RetryDocAudit.
        :type request: :class:`tencentcloud.lke.v20231130.models.RetryDocAuditRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RetryDocAuditResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDocAudit", params, headers=headers)
            response = json.loads(body)
            model = models.RetryDocAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryDocParse(self, request):
        """文档解析重试

        :param request: Request instance for RetryDocParse.
        :type request: :class:`tencentcloud.lke.v20231130.models.RetryDocParseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RetryDocParseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryDocParse", params, headers=headers)
            response = json.loads(body)
            model = models.RetryDocParseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryRelease(self, request):
        """发布暂停后重试

        :param request: Request instance for RetryRelease.
        :type request: :class:`tencentcloud.lke.v20231130.models.RetryReleaseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RetryReleaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryRelease", params, headers=headers)
            response = json.loads(body)
            model = models.RetryReleaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunReRank(self, request):
        """基于知识引擎精调模型技术的rerank模型，支持对多路召回的结果进行重排序，根据query与切片内容的相关性，按分数由高到低对切片进行排序，并输出对应的打分结果。（这个接口已下线，请使用新接口，接口文档：https://cloud.tencent.com/document/product/1772/115339）。

        :param request: Request instance for RunReRank.
        :type request: :class:`tencentcloud.lke.v20231130.models.RunReRankRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.RunReRankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunReRank", params, headers=headers)
            response = json.loads(body)
            model = models.RunReRankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SaveDoc(self, request):
        """知识库文档问答保存。
        将文件存储到应用的知识库内需要三步：
        1.获取临时密钥，参考[接口文档](https://cloud.tencent.com/document/product/1759/105050)。获取临时密钥不同参数组合权限不一样，可参考 [智能体开发平台操作 cos 指南](https://cloud.tencent.com/document/product/1759/116238)
        2.调用腾讯云提供的 cos 存储接口，将文件存储到智能体开发平台 cos 中：具体可参考[ COS SDK 概览](https://cloud.tencent.com/document/product/436/6474), 注意使用的是临时密钥的方式操作 COS
        3.调用本接口，将文件的基础信息存储到智能体开发平台中。
        以上步骤可参考[文档](https://cloud.tencent.com/document/product/1759/108903)，文档最后有[代码demo](https://cloud.tencent.com/document/product/1759/108903#demo)，可作为参考。

        :param request: Request instance for SaveDoc.
        :type request: :class:`tencentcloud.lke.v20231130.models.SaveDocRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.SaveDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveDoc", params, headers=headers)
            response = json.loads(body)
            model = models.SaveDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDocParse(self, request):
        """终止文档解析

        :param request: Request instance for StopDocParse.
        :type request: :class:`tencentcloud.lke.v20231130.models.StopDocParseRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.StopDocParseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopDocParse", params, headers=headers)
            response = json.loads(body)
            model = models.StopDocParseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopWorkflowRun(self, request):
        """此接口用来停止正在进行的工作流异步运行实例。

        :param request: Request instance for StopWorkflowRun.
        :type request: :class:`tencentcloud.lke.v20231130.models.StopWorkflowRunRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.StopWorkflowRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopWorkflowRun", params, headers=headers)
            response = json.loads(body)
            model = models.StopWorkflowRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateSharedKnowledge(self, request):
        """更新共享知识库。

        :param request: Request instance for UpdateSharedKnowledge.
        :type request: :class:`tencentcloud.lke.v20231130.models.UpdateSharedKnowledgeRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.UpdateSharedKnowledgeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSharedKnowledge", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSharedKnowledgeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateVar(self, request):
        """更新变量

        :param request: Request instance for UpdateVar.
        :type request: :class:`tencentcloud.lke.v20231130.models.UpdateVarRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.UpdateVarResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateVar", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateVarResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadAttributeLabel(self, request):
        """上传导入属性标签

        :param request: Request instance for UploadAttributeLabel.
        :type request: :class:`tencentcloud.lke.v20231130.models.UploadAttributeLabelRequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.UploadAttributeLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadAttributeLabel", params, headers=headers)
            response = json.loads(body)
            model = models.UploadAttributeLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyQA(self, request):
        """校验问答

        :param request: Request instance for VerifyQA.
        :type request: :class:`tencentcloud.lke.v20231130.models.VerifyQARequest`
        :rtype: :class:`tencentcloud.lke.v20231130.models.VerifyQAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyQA", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyQAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))