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
from tencentcloud.cat.v20180409 import models
from typing import Dict


class CatClient(AbstractClient):
    _apiVersion = '2018-04-09'
    _endpoint = 'cat.tencentcloudapi.com'
    _service = 'cat'

    async def CreateProbeTasks(
            self,
            request: models.CreateProbeTasksRequest,
            opts: Dict = None,
    ) -> models.CreateProbeTasksResponse:
        """
        批量创建拨测任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProbeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProbeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProbeTask(
            self,
            request: models.DeleteProbeTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteProbeTaskResponse:
        """
        删除拨测任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProbeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProbeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDetailedSingleProbeData(
            self,
            request: models.DescribeDetailedSingleProbeDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDetailedSingleProbeDataResponse:
        """
        根据时间范围、任务ID、运营商等条件查询单次拨测详情数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDetailedSingleProbeData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDetailedSingleProbeDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstantTasks(
            self,
            request: models.DescribeInstantTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeInstantTasksResponse:
        """
        获取历史即时拨测任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstantTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstantTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeGroups(
            self,
            request: models.DescribeNodeGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeGroupsResponse:
        """
        获取拨测点组（可用性拨测点组、高级拨测点组、我的拨测点组）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodes(
            self,
            request: models.DescribeNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeNodesResponse:
        """
        获取拨测节点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProbeMetricData(
            self,
            request: models.DescribeProbeMetricDataRequest,
            opts: Dict = None,
    ) -> models.DescribeProbeMetricDataResponse:
        """
        查询云拨测指标数据，指标支持使用sum,avg,max,min聚合函数进行指标数据查询
        拨测频率与groupby聚合时间设置关联，如拨测频率为 30 分钟，则 grouby 聚合时间建议设置为大于30分钟，避免出现查询数据为空的情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProbeMetricData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProbeMetricDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProbeMetricTagValues(
            self,
            request: models.DescribeProbeMetricTagValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeProbeMetricTagValuesResponse:
        """
        查询同个任务类型下的维度标签值，包括查询用户任务信息，具体任务下的多个维度标签信息。（通过为DescribeProbeMetricData接口的Filters参数添加维度筛选条件，可实现多维数据分析）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProbeMetricTagValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProbeMetricTagValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProbeNodes(
            self,
            request: models.DescribeProbeNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeProbeNodesResponse:
        """
        查询拨测节点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProbeNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProbeNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProbeTasks(
            self,
            request: models.DescribeProbeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeProbeTasksResponse:
        """
        查询拨测任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProbeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProbeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeProbeTask(
            self,
            request: models.ResumeProbeTaskRequest,
            opts: Dict = None,
    ) -> models.ResumeProbeTaskResponse:
        """
        恢复拨测任务
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeProbeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeProbeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SuspendProbeTask(
            self,
            request: models.SuspendProbeTaskRequest,
            opts: Dict = None,
    ) -> models.SuspendProbeTaskResponse:
        """
        暂停任务
        """
        
        kwargs = {}
        kwargs["action"] = "SuspendProbeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SuspendProbeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProbeTaskAttributes(
            self,
            request: models.UpdateProbeTaskAttributesRequest,
            opts: Dict = None,
    ) -> models.UpdateProbeTaskAttributesResponse:
        """
        更新探测任务属性
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProbeTaskAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProbeTaskAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProbeTaskConfigurationList(
            self,
            request: models.UpdateProbeTaskConfigurationListRequest,
            opts: Dict = None,
    ) -> models.UpdateProbeTaskConfigurationListResponse:
        """
        批量更新拨测任务配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProbeTaskConfigurationList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProbeTaskConfigurationListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)