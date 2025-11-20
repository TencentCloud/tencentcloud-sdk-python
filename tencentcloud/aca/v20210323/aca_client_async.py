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
from tencentcloud.aca.v20210323 import models
from typing import Dict


class AcaClient(AbstractClient):
    _apiVersion = '2021-03-23'
    _endpoint = 'aca.tencentcloudapi.com'
    _service = 'aca'

    async def GetDrugIndications(
            self,
            request: models.GetDrugIndicationsRequest,
            opts: Dict = None,
    ) -> models.GetDrugIndicationsResponse:
        """
        药品适应症接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetDrugIndications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDrugIndicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LoginHisTool(
            self,
            request: models.LoginHisToolRequest,
            opts: Dict = None,
    ) -> models.LoginHisToolResponse:
        """
        登录获取token
        """
        
        kwargs = {}
        kwargs["action"] = "LoginHisTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LoginHisToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LoginOutHisTool(
            self,
            request: models.LoginOutHisToolRequest,
            opts: Dict = None,
    ) -> models.LoginOutHisToolResponse:
        """
        登出
        """
        
        kwargs = {}
        kwargs["action"] = "LoginOutHisTool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LoginOutHisToolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SmartDrugInfo(
            self,
            request: models.SmartDrugInfoRequest,
            opts: Dict = None,
    ) -> models.SmartDrugInfoResponse:
        """
        智能用药接口
        """
        
        kwargs = {}
        kwargs["action"] = "SmartDrugInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SmartDrugInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SmartPredict(
            self,
            request: models.SmartPredictRequest,
            opts: Dict = None,
    ) -> models.SmartPredictResponse:
        """
        辅诊智能预测接口
        """
        
        kwargs = {}
        kwargs["action"] = "SmartPredict"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SmartPredictResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncDepartment(
            self,
            request: models.SyncDepartmentRequest,
            opts: Dict = None,
    ) -> models.SyncDepartmentResponse:
        """
        用于院方科室管理，获取科室列表和状态、新增或修改科室信息、删除科室。
        """
        
        kwargs = {}
        kwargs["action"] = "SyncDepartment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncDepartmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncStandardDict(
            self,
            request: models.SyncStandardDictRequest,
            opts: Dict = None,
    ) -> models.SyncStandardDictResponse:
        """
        同步标准字典，如给药频次、给药途径、科室、诊断等
        """
        
        kwargs = {}
        kwargs["action"] = "SyncStandardDict"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncStandardDictResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadDrugs(
            self,
            request: models.UploadDrugsRequest,
            opts: Dict = None,
    ) -> models.UploadDrugsResponse:
        """
        药品同步，一次同步数据不要超过500个
        """
        
        kwargs = {}
        kwargs["action"] = "UploadDrugs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadDrugsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)