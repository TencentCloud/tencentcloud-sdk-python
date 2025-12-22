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
from tencentcloud.lke.v20231130 import models
from typing import Dict


class LkeClient(AbstractClient):
    _apiVersion = '2023-11-30'
    _endpoint = 'lke.tencentcloudapi.com'
    _service = 'lke'

    async def CheckAttributeLabelExist(
            self,
            request: models.CheckAttributeLabelExistRequest,
            opts: Dict = None,
    ) -> models.CheckAttributeLabelExistResponse:
        """
        检查属性下的标签名是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAttributeLabelExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAttributeLabelExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAttributeLabelRefer(
            self,
            request: models.CheckAttributeLabelReferRequest,
            opts: Dict = None,
    ) -> models.CheckAttributeLabelReferResponse:
        """
        检查属性标签引用
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAttributeLabelRefer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAttributeLabelReferResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApp(
            self,
            request: models.CreateAppRequest,
            opts: Dict = None,
    ) -> models.CreateAppResponse:
        """
        创建知识引擎应用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAttributeLabel(
            self,
            request: models.CreateAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.CreateAttributeLabelResponse:
        """
        创建标签
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDocCate(
            self,
            request: models.CreateDocCateRequest,
            opts: Dict = None,
    ) -> models.CreateDocCateResponse:
        """
        创建Doc分类
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQA(
            self,
            request: models.CreateQARequest,
            opts: Dict = None,
    ) -> models.CreateQAResponse:
        """
        录入问答
        知识库相关背景知识介绍
        “知识库检索范围”文档：https://cloud.tencent.com/document/product/1759/112704
        “标签”文档：https://cloud.tencent.com/document/product/1759/112956
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateQACate(
            self,
            request: models.CreateQACateRequest,
            opts: Dict = None,
    ) -> models.CreateQACateResponse:
        """
        创建QA分类
        """
        
        kwargs = {}
        kwargs["action"] = "CreateQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateQACateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRejectedQuestion(
            self,
            request: models.CreateRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.CreateRejectedQuestionResponse:
        """
        创建拒答问题
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRelease(
            self,
            request: models.CreateReleaseRequest,
            opts: Dict = None,
    ) -> models.CreateReleaseResponse:
        """
        创建发布
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSharedKnowledge(
            self,
            request: models.CreateSharedKnowledgeRequest,
            opts: Dict = None,
    ) -> models.CreateSharedKnowledgeResponse:
        """
        创建共享知识库。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSharedKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSharedKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVar(
            self,
            request: models.CreateVarRequest,
            opts: Dict = None,
    ) -> models.CreateVarResponse:
        """
        创建变量
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVar"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVarResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflowRun(
            self,
            request: models.CreateWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowRunResponse:
        """
        本接口用来创建工作流的异步运行实例，创建成功后工作流会在后台异步运行，接口返回工作流运行实例ID（WorkflowRunId）等信息。后面可通过调用DescribeWorkflowRun接口查工作流运行的详情。
        注意：工作流的异步运行是基于应用的，需要先把对应的应用配置成“单工作流模式”，并且打开“异步调用”的开关，才能创建成功。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAgent(
            self,
            request: models.DeleteAgentRequest,
            opts: Dict = None,
    ) -> models.DeleteAgentResponse:
        """
        删除Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApp(
            self,
            request: models.DeleteAppRequest,
            opts: Dict = None,
    ) -> models.DeleteAppResponse:
        """
        删除应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAttributeLabel(
            self,
            request: models.DeleteAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.DeleteAttributeLabelResponse:
        """
        删除属性标签
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDoc(
            self,
            request: models.DeleteDocRequest,
            opts: Dict = None,
    ) -> models.DeleteDocResponse:
        """
        删除文档
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDocCate(
            self,
            request: models.DeleteDocCateRequest,
            opts: Dict = None,
    ) -> models.DeleteDocCateResponse:
        """
        Doc分类删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQA(
            self,
            request: models.DeleteQARequest,
            opts: Dict = None,
    ) -> models.DeleteQAResponse:
        """
        删除问答
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQACate(
            self,
            request: models.DeleteQACateRequest,
            opts: Dict = None,
    ) -> models.DeleteQACateResponse:
        """
        分类删除
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQACateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRejectedQuestion(
            self,
            request: models.DeleteRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.DeleteRejectedQuestionResponse:
        """
        删除拒答问题
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSharedKnowledge(
            self,
            request: models.DeleteSharedKnowledgeRequest,
            opts: Dict = None,
    ) -> models.DeleteSharedKnowledgeResponse:
        """
        删除共享知识库。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSharedKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSharedKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVar(
            self,
            request: models.DeleteVarRequest,
            opts: Dict = None,
    ) -> models.DeleteVarResponse:
        """
        删除变量
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVar"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVarResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApp(
            self,
            request: models.DescribeAppRequest,
            opts: Dict = None,
    ) -> models.DescribeAppResponse:
        """
        获取企业下应用详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppAgentList(
            self,
            request: models.DescribeAppAgentListRequest,
            opts: Dict = None,
    ) -> models.DescribeAppAgentListResponse:
        """
        查询指定应用下的Agent列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppAgentList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppAgentListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAttributeLabel(
            self,
            request: models.DescribeAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.DescribeAttributeLabelResponse:
        """
        查询属性标签详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallStatsGraph(
            self,
            request: models.DescribeCallStatsGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeCallStatsGraphResponse:
        """
        接口调用折线图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallStatsGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallStatsGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrencyUsage(
            self,
            request: models.DescribeConcurrencyUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrencyUsageResponse:
        """
        并发调用响应
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrencyUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrencyUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConcurrencyUsageGraph(
            self,
            request: models.DescribeConcurrencyUsageGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeConcurrencyUsageGraphResponse:
        """
        并发调用折线图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConcurrencyUsageGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConcurrencyUsageGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDoc(
            self,
            request: models.DescribeDocRequest,
            opts: Dict = None,
    ) -> models.DescribeDocResponse:
        """
        文档详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeUsage(
            self,
            request: models.DescribeKnowledgeUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeUsageResponse:
        """
        查询知识库用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKnowledgeUsagePieGraph(
            self,
            request: models.DescribeKnowledgeUsagePieGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeKnowledgeUsagePieGraphResponse:
        """
        查询企业知识库容量饼图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKnowledgeUsagePieGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKnowledgeUsagePieGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeRun(
            self,
            request: models.DescribeNodeRunRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeRunResponse:
        """
        通过DescribeWorkflowRun接口获取了工作流异步运行的整体内容，其中包含了基本的节点信息，再通过本接口可查看节点的运行详情（包括输入、输出、日志等）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQA(
            self,
            request: models.DescribeQARequest,
            opts: Dict = None,
    ) -> models.DescribeQAResponse:
        """
        问答详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRefer(
            self,
            request: models.DescribeReferRequest,
            opts: Dict = None,
    ) -> models.DescribeReferResponse:
        """
        获取来源详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRefer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReferResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelease(
            self,
            request: models.DescribeReleaseRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseResponse:
        """
        发布详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReleaseInfo(
            self,
            request: models.DescribeReleaseInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeReleaseInfoResponse:
        """
        拉取发布按钮状态、最后发布时间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReleaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReleaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRobotBizIDByAppKey(
            self,
            request: models.DescribeRobotBizIDByAppKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeRobotBizIDByAppKeyResponse:
        """
        通过appKey获取应用业务ID
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRobotBizIDByAppKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRobotBizIDByAppKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchStatsGraph(
            self,
            request: models.DescribeSearchStatsGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchStatsGraphResponse:
        """
        查询搜索服务调用折线图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchStatsGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchStatsGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSegments(
            self,
            request: models.DescribeSegmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeSegmentsResponse:
        """
        获取片段详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSegments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSegmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSharedKnowledge(
            self,
            request: models.DescribeSharedKnowledgeRequest,
            opts: Dict = None,
    ) -> models.DescribeSharedKnowledgeResponse:
        """
        查询共享知识库。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSharedKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSharedKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStorageCredential(
            self,
            request: models.DescribeStorageCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeStorageCredentialResponse:
        """
        获取文件上传临时密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStorageCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStorageCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenUsage(
            self,
            request: models.DescribeTokenUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenUsageResponse:
        """
        接口调用token详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenUsageGraph(
            self,
            request: models.DescribeTokenUsageGraphRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenUsageGraphResponse:
        """
        接口调用token折线图
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenUsageGraph"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenUsageGraphResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnsatisfiedReplyContext(
            self,
            request: models.DescribeUnsatisfiedReplyContextRequest,
            opts: Dict = None,
    ) -> models.DescribeUnsatisfiedReplyContextResponse:
        """
        获取不满意回复上下文
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnsatisfiedReplyContext"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnsatisfiedReplyContextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowRun(
            self,
            request: models.DescribeWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowRunResponse:
        """
        创建了工作流的异步运行实例后，通过本接口可以查询整体的运行详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportAttributeLabel(
            self,
            request: models.ExportAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.ExportAttributeLabelResponse:
        """
        导出标签
        """
        
        kwargs = {}
        kwargs["action"] = "ExportAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportQAList(
            self,
            request: models.ExportQAListRequest,
            opts: Dict = None,
    ) -> models.ExportQAListResponse:
        """
        导出QA列表
        """
        
        kwargs = {}
        kwargs["action"] = "ExportQAList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportQAListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportUnsatisfiedReply(
            self,
            request: models.ExportUnsatisfiedReplyRequest,
            opts: Dict = None,
    ) -> models.ExportUnsatisfiedReplyResponse:
        """
        导出不满意回复
        """
        
        kwargs = {}
        kwargs["action"] = "ExportUnsatisfiedReply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportUnsatisfiedReplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateQA(
            self,
            request: models.GenerateQARequest,
            opts: Dict = None,
    ) -> models.GenerateQAResponse:
        """
        文档生成问答
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAnswerTypeDataCount(
            self,
            request: models.GetAnswerTypeDataCountRequest,
            opts: Dict = None,
    ) -> models.GetAnswerTypeDataCountResponse:
        """
        回答类型数据统计
        """
        
        kwargs = {}
        kwargs["action"] = "GetAnswerTypeDataCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAnswerTypeDataCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAppKnowledgeCount(
            self,
            request: models.GetAppKnowledgeCountRequest,
            opts: Dict = None,
    ) -> models.GetAppKnowledgeCountResponse:
        """
        获取模型列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetAppKnowledgeCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAppKnowledgeCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAppSecret(
            self,
            request: models.GetAppSecretRequest,
            opts: Dict = None,
    ) -> models.GetAppSecretResponse:
        """
        获取应用密钥
        """
        
        kwargs = {}
        kwargs["action"] = "GetAppSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAppSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDocPreview(
            self,
            request: models.GetDocPreviewRequest,
            opts: Dict = None,
    ) -> models.GetDocPreviewResponse:
        """
        获取文档预览信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetDocPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDocPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetLikeDataCount(
            self,
            request: models.GetLikeDataCountRequest,
            opts: Dict = None,
    ) -> models.GetLikeDataCountResponse:
        """
        点赞点踩数据统计
        """
        
        kwargs = {}
        kwargs["action"] = "GetLikeDataCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetLikeDataCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMsgRecord(
            self,
            request: models.GetMsgRecordRequest,
            opts: Dict = None,
    ) -> models.GetMsgRecordResponse:
        """
        获取聊天历史
        根据会话session id获取聊天历史（仅保留180天内的历史对话数据）
        """
        
        kwargs = {}
        kwargs["action"] = "GetMsgRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMsgRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskStatus(
            self,
            request: models.GetTaskStatusRequest,
            opts: Dict = None,
    ) -> models.GetTaskStatusResponse:
        """
        获取任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetVarList(
            self,
            request: models.GetVarListRequest,
            opts: Dict = None,
    ) -> models.GetVarListResponse:
        """
        查询自定义变量列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetVarList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetVarListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWsToken(
            self,
            request: models.GetWsTokenRequest,
            opts: Dict = None,
    ) -> models.GetWsTokenResponse:
        """
        获取ws token
        """
        
        kwargs = {}
        kwargs["action"] = "GetWsToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWsTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GroupDoc(
            self,
            request: models.GroupDocRequest,
            opts: Dict = None,
    ) -> models.GroupDocResponse:
        """
        Doc分组
        """
        
        kwargs = {}
        kwargs["action"] = "GroupDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GroupDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GroupQA(
            self,
            request: models.GroupQARequest,
            opts: Dict = None,
    ) -> models.GroupQAResponse:
        """
        QA分组
        """
        
        kwargs = {}
        kwargs["action"] = "GroupQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GroupQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IgnoreUnsatisfiedReply(
            self,
            request: models.IgnoreUnsatisfiedReplyRequest,
            opts: Dict = None,
    ) -> models.IgnoreUnsatisfiedReplyResponse:
        """
        忽略不满意回复
        """
        
        kwargs = {}
        kwargs["action"] = "IgnoreUnsatisfiedReply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IgnoreUnsatisfiedReplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsTransferIntent(
            self,
            request: models.IsTransferIntentRequest,
            opts: Dict = None,
    ) -> models.IsTransferIntentResponse:
        """
        是否意图转人工
        """
        
        kwargs = {}
        kwargs["action"] = "IsTransferIntent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsTransferIntentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListApp(
            self,
            request: models.ListAppRequest,
            opts: Dict = None,
    ) -> models.ListAppResponse:
        """
        获取企业下应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAppKnowledgeDetail(
            self,
            request: models.ListAppKnowledgeDetailRequest,
            opts: Dict = None,
    ) -> models.ListAppKnowledgeDetailResponse:
        """
        列表查询知识库容量详情
        """
        
        kwargs = {}
        kwargs["action"] = "ListAppKnowledgeDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAppKnowledgeDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAttributeLabel(
            self,
            request: models.ListAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.ListAttributeLabelResponse:
        """
        查询属性标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListChannel(
            self,
            request: models.ListChannelRequest,
            opts: Dict = None,
    ) -> models.ListChannelResponse:
        """
        获取发布渠道列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDoc(
            self,
            request: models.ListDocRequest,
            opts: Dict = None,
    ) -> models.ListDocResponse:
        """
        文档列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDocCate(
            self,
            request: models.ListDocCateRequest,
            opts: Dict = None,
    ) -> models.ListDocCateResponse:
        """
        获取Doc分类
        """
        
        kwargs = {}
        kwargs["action"] = "ListDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListModel(
            self,
            request: models.ListModelRequest,
            opts: Dict = None,
    ) -> models.ListModelResponse:
        """
        获取模型列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListQA(
            self,
            request: models.ListQARequest,
            opts: Dict = None,
    ) -> models.ListQAResponse:
        """
        问答列表
        知识库相关背景知识介绍
        “知识库检索范围”文档：https://cloud.tencent.com/document/product/1759/112704
        “标签”文档：https://cloud.tencent.com/document/product/1759/112956
        """
        
        kwargs = {}
        kwargs["action"] = "ListQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListQACate(
            self,
            request: models.ListQACateRequest,
            opts: Dict = None,
    ) -> models.ListQACateResponse:
        """
        获取QA分类
        """
        
        kwargs = {}
        kwargs["action"] = "ListQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListQACateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReferShareKnowledge(
            self,
            request: models.ListReferShareKnowledgeRequest,
            opts: Dict = None,
    ) -> models.ListReferShareKnowledgeResponse:
        """
        查看应用引用了哪些共享知识库，可以看到共享知识库的基础信息，包括名称，id等
        """
        
        kwargs = {}
        kwargs["action"] = "ListReferShareKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReferShareKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRejectedQuestion(
            self,
            request: models.ListRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.ListRejectedQuestionResponse:
        """
        获取拒答问题
        """
        
        kwargs = {}
        kwargs["action"] = "ListRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRejectedQuestionPreview(
            self,
            request: models.ListRejectedQuestionPreviewRequest,
            opts: Dict = None,
    ) -> models.ListRejectedQuestionPreviewResponse:
        """
        发布拒答问题预览
        """
        
        kwargs = {}
        kwargs["action"] = "ListRejectedQuestionPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRejectedQuestionPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRelease(
            self,
            request: models.ListReleaseRequest,
            opts: Dict = None,
    ) -> models.ListReleaseResponse:
        """
        发布列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReleaseConfigPreview(
            self,
            request: models.ListReleaseConfigPreviewRequest,
            opts: Dict = None,
    ) -> models.ListReleaseConfigPreviewResponse:
        """
        发布配置项预览
        """
        
        kwargs = {}
        kwargs["action"] = "ListReleaseConfigPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseConfigPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReleaseDocPreview(
            self,
            request: models.ListReleaseDocPreviewRequest,
            opts: Dict = None,
    ) -> models.ListReleaseDocPreviewResponse:
        """
        发布文档预览
        """
        
        kwargs = {}
        kwargs["action"] = "ListReleaseDocPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseDocPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReleaseQAPreview(
            self,
            request: models.ListReleaseQAPreviewRequest,
            opts: Dict = None,
    ) -> models.ListReleaseQAPreviewResponse:
        """
        文档列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListReleaseQAPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReleaseQAPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSelectDoc(
            self,
            request: models.ListSelectDocRequest,
            opts: Dict = None,
    ) -> models.ListSelectDocResponse:
        """
        获取文档下拉列表。
        """
        
        kwargs = {}
        kwargs["action"] = "ListSelectDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSelectDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSharedKnowledge(
            self,
            request: models.ListSharedKnowledgeRequest,
            opts: Dict = None,
    ) -> models.ListSharedKnowledgeResponse:
        """
        列举共享知识库。
        """
        
        kwargs = {}
        kwargs["action"] = "ListSharedKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSharedKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUnsatisfiedReply(
            self,
            request: models.ListUnsatisfiedReplyRequest,
            opts: Dict = None,
    ) -> models.ListUnsatisfiedReplyResponse:
        """
        查询不满意回复列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListUnsatisfiedReply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUnsatisfiedReplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUsageCallDetail(
            self,
            request: models.ListUsageCallDetailRequest,
            opts: Dict = None,
    ) -> models.ListUsageCallDetailResponse:
        """
        列表查询单次调用明细
        """
        
        kwargs = {}
        kwargs["action"] = "ListUsageCallDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUsageCallDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflowRuns(
            self,
            request: models.ListWorkflowRunsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowRunsResponse:
        """
        此接口可查询已创建的所有工作流异步运行实例。
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApp(
            self,
            request: models.ModifyAppRequest,
            opts: Dict = None,
    ) -> models.ModifyAppResponse:
        """
        修改应用请求结构体
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAttributeLabel(
            self,
            request: models.ModifyAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.ModifyAttributeLabelResponse:
        """
        编辑属性标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDoc(
            self,
            request: models.ModifyDocRequest,
            opts: Dict = None,
    ) -> models.ModifyDocResponse:
        """
        修改文档
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDocAttrRange(
            self,
            request: models.ModifyDocAttrRangeRequest,
            opts: Dict = None,
    ) -> models.ModifyDocAttrRangeResponse:
        """
        批量修改文档适用范围
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDocAttrRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDocAttrRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDocCate(
            self,
            request: models.ModifyDocCateRequest,
            opts: Dict = None,
    ) -> models.ModifyDocCateResponse:
        """
        修改Doc分类
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDocCate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDocCateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQA(
            self,
            request: models.ModifyQARequest,
            opts: Dict = None,
    ) -> models.ModifyQAResponse:
        """
        更新问答
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQAAttrRange(
            self,
            request: models.ModifyQAAttrRangeRequest,
            opts: Dict = None,
    ) -> models.ModifyQAAttrRangeResponse:
        """
        批量修改问答适用范围
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQAAttrRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQAAttrRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyQACate(
            self,
            request: models.ModifyQACateRequest,
            opts: Dict = None,
    ) -> models.ModifyQACateResponse:
        """
        更新QA分类
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyQACate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyQACateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRejectedQuestion(
            self,
            request: models.ModifyRejectedQuestionRequest,
            opts: Dict = None,
    ) -> models.ModifyRejectedQuestionResponse:
        """
        修改拒答问题
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRejectedQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRejectedQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RateMsgRecord(
            self,
            request: models.RateMsgRecordRequest,
            opts: Dict = None,
    ) -> models.RateMsgRecordResponse:
        """
        点赞点踩消息
        """
        
        kwargs = {}
        kwargs["action"] = "RateMsgRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RateMsgRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReferShareKnowledge(
            self,
            request: models.ReferShareKnowledgeRequest,
            opts: Dict = None,
    ) -> models.ReferShareKnowledgeResponse:
        """
        应用引用共享知识库，可以引用一个或多个，每次都是全量覆盖
        """
        
        kwargs = {}
        kwargs["action"] = "ReferShareKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReferShareKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenameDoc(
            self,
            request: models.RenameDocRequest,
            opts: Dict = None,
    ) -> models.RenameDocResponse:
        """
        文档重命名
        """
        
        kwargs = {}
        kwargs["action"] = "RenameDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenameDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryDocAudit(
            self,
            request: models.RetryDocAuditRequest,
            opts: Dict = None,
    ) -> models.RetryDocAuditResponse:
        """
        文档解析重试
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDocAudit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDocAuditResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryDocParse(
            self,
            request: models.RetryDocParseRequest,
            opts: Dict = None,
    ) -> models.RetryDocParseResponse:
        """
        文档解析重试
        """
        
        kwargs = {}
        kwargs["action"] = "RetryDocParse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryDocParseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryRelease(
            self,
            request: models.RetryReleaseRequest,
            opts: Dict = None,
    ) -> models.RetryReleaseResponse:
        """
        发布暂停后重试
        """
        
        kwargs = {}
        kwargs["action"] = "RetryRelease"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryReleaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaveDoc(
            self,
            request: models.SaveDocRequest,
            opts: Dict = None,
    ) -> models.SaveDocResponse:
        """
        知识库文档问答保存。
        将文件存储到应用的知识库内需要三步：
        1.获取临时密钥，参考[接口文档](https://cloud.tencent.com/document/product/1759/105050)。获取临时密钥不同参数组合权限不一样，可参考 [智能体开发平台操作 cos 指南](https://cloud.tencent.com/document/product/1759/116238)
        2.调用腾讯云提供的 cos 存储接口，将文件存储到智能体开发平台 cos 中：具体可参考[ COS SDK 概览](https://cloud.tencent.com/document/product/436/6474), 注意使用的是临时密钥的方式操作 COS
        3.调用本接口，将文件的基础信息存储到智能体开发平台中。
        以上步骤可参考[文档](https://cloud.tencent.com/document/product/1759/108903)，文档最后有[代码demo](https://cloud.tencent.com/document/product/1759/108903#demo)，可作为参考。
        """
        
        kwargs = {}
        kwargs["action"] = "SaveDoc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaveDocResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopDocParse(
            self,
            request: models.StopDocParseRequest,
            opts: Dict = None,
    ) -> models.StopDocParseResponse:
        """
        终止文档解析
        """
        
        kwargs = {}
        kwargs["action"] = "StopDocParse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopDocParseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopWorkflowRun(
            self,
            request: models.StopWorkflowRunRequest,
            opts: Dict = None,
    ) -> models.StopWorkflowRunResponse:
        """
        此接口用来停止正在进行的工作流异步运行实例。
        """
        
        kwargs = {}
        kwargs["action"] = "StopWorkflowRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopWorkflowRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSharedKnowledge(
            self,
            request: models.UpdateSharedKnowledgeRequest,
            opts: Dict = None,
    ) -> models.UpdateSharedKnowledgeResponse:
        """
        更新共享知识库。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSharedKnowledge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSharedKnowledgeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateVar(
            self,
            request: models.UpdateVarRequest,
            opts: Dict = None,
    ) -> models.UpdateVarResponse:
        """
        更新变量
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateVar"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateVarResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadAttributeLabel(
            self,
            request: models.UploadAttributeLabelRequest,
            opts: Dict = None,
    ) -> models.UploadAttributeLabelResponse:
        """
        上传导入属性标签
        """
        
        kwargs = {}
        kwargs["action"] = "UploadAttributeLabel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadAttributeLabelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyQA(
            self,
            request: models.VerifyQARequest,
            opts: Dict = None,
    ) -> models.VerifyQAResponse:
        """
        校验问答
        知识库相关背景知识介绍
        “知识库检索范围”文档：https://cloud.tencent.com/document/product/1759/112704
        “标签”文档：https://cloud.tencent.com/document/product/1759/112956
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyQA"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyQAResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)