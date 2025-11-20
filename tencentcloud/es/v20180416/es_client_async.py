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
from tencentcloud.es.v20180416 import models
from typing import Dict


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.tencentcloudapi.com'
    _service = 'es'

    async def CheckMigrateIndexMetaData(
            self,
            request: models.CheckMigrateIndexMetaDataRequest,
            opts: Dict = None,
    ) -> models.CheckMigrateIndexMetaDataResponse:
        """
        检查cos迁移索引元数据
        """
        
        kwargs = {}
        kwargs["action"] = "CheckMigrateIndexMetaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckMigrateIndexMetaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterSnapshot(
            self,
            request: models.CreateClusterSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateClusterSnapshotResponse:
        """
        集群快照手动创建
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosMigrateToServerlessInstance(
            self,
            request: models.CreateCosMigrateToServerlessInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateCosMigrateToServerlessInstanceResponse:
        """
        cos迁移流程
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosMigrateToServerlessInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosMigrateToServerlessInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIndex(
            self,
            request: models.CreateIndexRequest,
            opts: Dict = None,
    ) -> models.CreateIndexResponse:
        """
        创建索引
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        创建指定规格的ES集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogstashInstance(
            self,
            request: models.CreateLogstashInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateLogstashInstanceResponse:
        """
        用于创建Logstash实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogstashInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogstashInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServerlessInstance(
            self,
            request: models.CreateServerlessInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateServerlessInstanceResponse:
        """
        创建Serverless索引
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServerlessInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServerlessInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServerlessSpaceV2(
            self,
            request: models.CreateServerlessSpaceV2Request,
            opts: Dict = None,
    ) -> models.CreateServerlessSpaceV2Response:
        """
        创建Serverless索引空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServerlessSpaceV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServerlessSpaceV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterSnapshot(
            self,
            request: models.DeleteClusterSnapshotRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterSnapshotResponse:
        """
        删除快照仓库里备份的快照
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIndex(
            self,
            request: models.DeleteIndexRequest,
            opts: Dict = None,
    ) -> models.DeleteIndexResponse:
        """
        删除索引
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        销毁集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogstashInstance(
            self,
            request: models.DeleteLogstashInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteLogstashInstanceResponse:
        """
        用于删除Logstash实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogstashInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogstashInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogstashPipelines(
            self,
            request: models.DeleteLogstashPipelinesRequest,
            opts: Dict = None,
    ) -> models.DeleteLogstashPipelinesResponse:
        """
        用于批量删除Logstash管道
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogstashPipelines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogstashPipelinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServerlessInstance(
            self,
            request: models.DeleteServerlessInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteServerlessInstanceResponse:
        """
        删除Serverless索引
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServerlessInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServerlessInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServerlessSpaceUser(
            self,
            request: models.DeleteServerlessSpaceUserRequest,
            opts: Dict = None,
    ) -> models.DeleteServerlessSpaceUserResponse:
        """
        删除Serverless空间子用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServerlessSpaceUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServerlessSpaceUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSnapshot(
            self,
            request: models.DescribeClusterSnapshotRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSnapshotResponse:
        """
        获取快照备份列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiagnose(
            self,
            request: models.DescribeDiagnoseRequest,
            opts: Dict = None,
    ) -> models.DescribeDiagnoseResponse:
        """
        查询智能运维诊断结果报告
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiagnose"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiagnoseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexList(
            self,
            request: models.DescribeIndexListRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexListResponse:
        """
        获取索引列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndexMeta(
            self,
            request: models.DescribeIndexMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexMetaResponse:
        """
        获取索引元数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndexMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogs(
            self,
            request: models.DescribeInstanceLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogsResponse:
        """
        查询用户该地域下符合条件的ES集群的日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOperations(
            self,
            request: models.DescribeInstanceOperationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOperationsResponse:
        """
        查询实例指定条件下的操作记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancePluginList(
            self,
            request: models.DescribeInstancePluginListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancePluginListResponse:
        """
        查询实例插件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancePluginList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancePluginListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        查询用户该地域下符合条件的所有实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogstashInstanceLogs(
            self,
            request: models.DescribeLogstashInstanceLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogstashInstanceLogsResponse:
        """
        查询用户该地域下符合条件的Logstash实例的日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogstashInstanceLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogstashInstanceLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogstashInstanceOperations(
            self,
            request: models.DescribeLogstashInstanceOperationsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogstashInstanceOperationsResponse:
        """
        查询实例指定条件下的操作记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogstashInstanceOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogstashInstanceOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogstashInstances(
            self,
            request: models.DescribeLogstashInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeLogstashInstancesResponse:
        """
        查询用户该地域下符合条件的所有Logstash实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogstashInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogstashInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogstashPipelines(
            self,
            request: models.DescribeLogstashPipelinesRequest,
            opts: Dict = None,
    ) -> models.DescribeLogstashPipelinesResponse:
        """
        用于获取Logstash实例管道列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogstashPipelines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogstashPipelinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessInstances(
            self,
            request: models.DescribeServerlessInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessInstancesResponse:
        """
        Serverless获取索引列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessMetrics(
            self,
            request: models.DescribeServerlessMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessMetricsResponse:
        """
        获取serverless实例对应指标，获取space维度时不需要传入indexid，获取index时不需要传入spaceid
        获取一段时间时间范围内的指标数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessSpaceUser(
            self,
            request: models.DescribeServerlessSpaceUserRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessSpaceUserResponse:
        """
        查看Serverless空间子用户
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessSpaceUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessSpaceUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServerlessSpaces(
            self,
            request: models.DescribeServerlessSpacesRequest,
            opts: Dict = None,
    ) -> models.DescribeServerlessSpacesResponse:
        """
        获取Serverless索引空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServerlessSpaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServerlessSpacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpaceKibanaTools(
            self,
            request: models.DescribeSpaceKibanaToolsRequest,
            opts: Dict = None,
    ) -> models.DescribeSpaceKibanaToolsResponse:
        """
        space维度的kibana获取登录token
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpaceKibanaTools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpaceKibanaToolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserCosSnapshotList(
            self,
            request: models.DescribeUserCosSnapshotListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserCosSnapshotListResponse:
        """
        查询快照信息接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserCosSnapshotList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserCosSnapshotListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeViews(
            self,
            request: models.DescribeViewsRequest,
            opts: Dict = None,
    ) -> models.DescribeViewsResponse:
        """
        查询集群各视图数据，包括集群维度、节点维度、Kibana维度
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeViews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeViewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DiagnoseInstance(
            self,
            request: models.DiagnoseInstanceRequest,
            opts: Dict = None,
    ) -> models.DiagnoseInstanceResponse:
        """
        智能运维诊断集群
        """
        
        kwargs = {}
        kwargs["action"] = "DiagnoseInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DiagnoseInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportIpTraceLog(
            self,
            request: models.ExportIpTraceLogRequest,
            opts: Dict = None,
    ) -> models.ExportIpTraceLogResponse:
        """
        查询IP溯源日志原始数据
        """
        
        kwargs = {}
        kwargs["action"] = "ExportIpTraceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportIpTraceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDiagnoseSettings(
            self,
            request: models.GetDiagnoseSettingsRequest,
            opts: Dict = None,
    ) -> models.GetDiagnoseSettingsResponse:
        """
        查看智能运维配置
        """
        
        kwargs = {}
        kwargs["action"] = "GetDiagnoseSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDiagnoseSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetIpTraceStatus(
            self,
            request: models.GetIpTraceStatusRequest,
            opts: Dict = None,
    ) -> models.GetIpTraceStatusResponse:
        """
        查询IP溯源状态
        """
        
        kwargs = {}
        kwargs["action"] = "GetIpTraceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetIpTraceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRequestTargetNodeTypes(
            self,
            request: models.GetRequestTargetNodeTypesRequest,
            opts: Dict = None,
    ) -> models.GetRequestTargetNodeTypesResponse:
        """
        获取接收客户端请求的节点类型
        """
        
        kwargs = {}
        kwargs["action"] = "GetRequestTargetNodeTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRequestTargetNodeTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenewInstance(
            self,
            request: models.InquirePriceRenewInstanceRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewInstanceResponse:
        """
        集群续费询价接口，续费前通过调用该接口，可获取集群续费的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallInstanceModel(
            self,
            request: models.InstallInstanceModelRequest,
            opts: Dict = None,
    ) -> models.InstallInstanceModelResponse:
        """
        ES集群安装模型接口
        """
        
        kwargs = {}
        kwargs["action"] = "InstallInstanceModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallInstanceModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEsVipSecurityGroup(
            self,
            request: models.ModifyEsVipSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyEsVipSecurityGroupResponse:
        """
        修改绑定VIP的安全组，传安全组id列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEsVipSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEsVipSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryIpTraceLog(
            self,
            request: models.QueryIpTraceLogRequest,
            opts: Dict = None,
    ) -> models.QueryIpTraceLogResponse:
        """
        查询IP溯源日志
        """
        
        kwargs = {}
        kwargs["action"] = "QueryIpTraceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryIpTraceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartInstance(
            self,
            request: models.RestartInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartInstanceResponse:
        """
        重启ES集群实例(用于系统版本更新等操作)
        """
        
        kwargs = {}
        kwargs["action"] = "RestartInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartKibana(
            self,
            request: models.RestartKibanaRequest,
            opts: Dict = None,
    ) -> models.RestartKibanaResponse:
        """
        重启Kibana
        """
        
        kwargs = {}
        kwargs["action"] = "RestartKibana"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartKibanaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartLogstashInstance(
            self,
            request: models.RestartLogstashInstanceRequest,
            opts: Dict = None,
    ) -> models.RestartLogstashInstanceResponse:
        """
        用于重启Logstash实例
        """
        
        kwargs = {}
        kwargs["action"] = "RestartLogstashInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartLogstashInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartNodes(
            self,
            request: models.RestartNodesRequest,
            opts: Dict = None,
    ) -> models.RestartNodesResponse:
        """
        用于重启集群节点
        """
        
        kwargs = {}
        kwargs["action"] = "RestartNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreClusterSnapshot(
            self,
            request: models.RestoreClusterSnapshotRequest,
            opts: Dict = None,
    ) -> models.RestoreClusterSnapshotResponse:
        """
        快照备份恢复，从仓库中恢复快照到集群中
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreClusterSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreClusterSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaveAndDeployLogstashPipeline(
            self,
            request: models.SaveAndDeployLogstashPipelineRequest,
            opts: Dict = None,
    ) -> models.SaveAndDeployLogstashPipelineResponse:
        """
        用于下发并且部署管道
        """
        
        kwargs = {}
        kwargs["action"] = "SaveAndDeployLogstashPipeline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaveAndDeployLogstashPipelineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartLogstashPipelines(
            self,
            request: models.StartLogstashPipelinesRequest,
            opts: Dict = None,
    ) -> models.StartLogstashPipelinesResponse:
        """
        用于启动Logstash管道
        """
        
        kwargs = {}
        kwargs["action"] = "StartLogstashPipelines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartLogstashPipelinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLogstashPipelines(
            self,
            request: models.StopLogstashPipelinesRequest,
            opts: Dict = None,
    ) -> models.StopLogstashPipelinesResponse:
        """
        用于批量停止Logstash管道
        """
        
        kwargs = {}
        kwargs["action"] = "StopLogstashPipelines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLogstashPipelinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDiagnoseSettings(
            self,
            request: models.UpdateDiagnoseSettingsRequest,
            opts: Dict = None,
    ) -> models.UpdateDiagnoseSettingsResponse:
        """
        更新智能运维配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDiagnoseSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDiagnoseSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDictionaries(
            self,
            request: models.UpdateDictionariesRequest,
            opts: Dict = None,
    ) -> models.UpdateDictionariesResponse:
        """
        更新ES集群词典
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDictionaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDictionariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateIndex(
            self,
            request: models.UpdateIndexRequest,
            opts: Dict = None,
    ) -> models.UpdateIndexResponse:
        """
        更新索引
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateInstance(
            self,
            request: models.UpdateInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateInstanceResponse:
        """
        对集群进行节点规格变更，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作。参数中InstanceId为必传参数，ForceRestart为选填参数，剩余参数传递组合及含义如下：
        - InstanceName：修改实例名称(仅用于标识实例)
        - NodeInfoList: 修改节点配置（节点横向扩缩容，纵向扩缩容，增加主节点，增加冷节点等）
        - EsConfig：修改集群配置
        - Password：修改默认用户elastic的密码
        - EsAcl：修改访问控制列表
        - CosBackUp: 设置集群COS自动备份信息
        以上参数组合只能传递一种，多传或少传均会导致请求失败
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateIpTraceStatus(
            self,
            request: models.UpdateIpTraceStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateIpTraceStatusResponse:
        """
        更新ES集群IP溯源状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateIpTraceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateIpTraceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateJdk(
            self,
            request: models.UpdateJdkRequest,
            opts: Dict = None,
    ) -> models.UpdateJdkResponse:
        """
        更新实例Jdk配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateJdk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateJdkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateLogstashInstance(
            self,
            request: models.UpdateLogstashInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateLogstashInstanceResponse:
        """
        对集群进行节点规格变更，修改实例名称，修改配置，等操作。参数中InstanceId为必传参数，参数传递组合及含义如下：
        - InstanceName：修改实例名称(仅用于标识实例)
        - NodeNum: 修改实例节点数量（节点横向扩缩容，纵向扩缩容等）
        - YMLConfig: 修改实例YML配置
        - BindedES：修改绑定的ES集群配置
        以上参数组合只能传递一种，多传或少传均会导致请求失败
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateLogstashInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateLogstashInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateLogstashPipelineDesc(
            self,
            request: models.UpdateLogstashPipelineDescRequest,
            opts: Dict = None,
    ) -> models.UpdateLogstashPipelineDescResponse:
        """
        用于更新管道描述信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateLogstashPipelineDesc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateLogstashPipelineDescResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePlugins(
            self,
            request: models.UpdatePluginsRequest,
            opts: Dict = None,
    ) -> models.UpdatePluginsResponse:
        """
        变更插件列表
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRequestTargetNodeTypes(
            self,
            request: models.UpdateRequestTargetNodeTypesRequest,
            opts: Dict = None,
    ) -> models.UpdateRequestTargetNodeTypesResponse:
        """
        更新接收客户端请求的节点类型
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRequestTargetNodeTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRequestTargetNodeTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateServerlessInstance(
            self,
            request: models.UpdateServerlessInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateServerlessInstanceResponse:
        """
        更新Serverless索引
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateServerlessInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateServerlessInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateServerlessSpace(
            self,
            request: models.UpdateServerlessSpaceRequest,
            opts: Dict = None,
    ) -> models.UpdateServerlessSpaceResponse:
        """
        更新Serverless索引空间
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateServerlessSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateServerlessSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        升级ES集群版本
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeLicense(
            self,
            request: models.UpgradeLicenseRequest,
            opts: Dict = None,
    ) -> models.UpgradeLicenseResponse:
        """
        升级ES商业特性
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)