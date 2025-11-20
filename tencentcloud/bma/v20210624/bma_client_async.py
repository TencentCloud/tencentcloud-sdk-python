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
from tencentcloud.bma.v20210624 import models
from typing import Dict


class BmaClient(AbstractClient):
    _apiVersion = '2021-06-24'
    _endpoint = 'bma.tencentcloudapi.com'
    _service = 'bma'

    async def CreateBPFakeURL(
            self,
            request: models.CreateBPFakeURLRequest,
            opts: Dict = None,
    ) -> models.CreateBPFakeURLResponse:
        """
        添加仿冒链接（举报）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPFakeURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPFakeURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPFalseTicket(
            self,
            request: models.CreateBPFalseTicketRequest,
            opts: Dict = None,
    ) -> models.CreateBPFalseTicketResponse:
        """
        添加误报工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPFalseTicket"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPFalseTicketResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPOfflineAttachment(
            self,
            request: models.CreateBPOfflineAttachmentRequest,
            opts: Dict = None,
    ) -> models.CreateBPOfflineAttachmentResponse:
        """
        添加下线材料
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPOfflineAttachment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPOfflineAttachmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPOfflineTicket(
            self,
            request: models.CreateBPOfflineTicketRequest,
            opts: Dict = None,
    ) -> models.CreateBPOfflineTicketResponse:
        """
        添加下线工单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPOfflineTicket"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPOfflineTicketResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBPProtectURLs(
            self,
            request: models.CreateBPProtectURLsRequest,
            opts: Dict = None,
    ) -> models.CreateBPProtectURLsResponse:
        """
        添加保护网站
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBPProtectURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBPProtectURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRBlock(
            self,
            request: models.CreateCRBlockRequest,
            opts: Dict = None,
    ) -> models.CreateCRBlockResponse:
        """
        新建协查处置
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRCompanyVerify(
            self,
            request: models.CreateCRCompanyVerifyRequest,
            opts: Dict = None,
    ) -> models.CreateCRCompanyVerifyResponse:
        """
        本接口用于企业认证，新接入用户必须认证后才可以进行后续操作（个人认证和企业认证二选一），只需认证一次即可
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRCompanyVerify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRCompanyVerifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRDesktopCode(
            self,
            request: models.CreateCRDesktopCodeRequest,
            opts: Dict = None,
    ) -> models.CreateCRDesktopCodeResponse:
        """
        新建过程取证码
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRDesktopCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRDesktopCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRRight(
            self,
            request: models.CreateCRRightRequest,
            opts: Dict = None,
    ) -> models.CreateCRRightResponse:
        """
        版权保护-新建发函接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRRight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRRightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRRightFile(
            self,
            request: models.CreateCRRightFileRequest,
            opts: Dict = None,
    ) -> models.CreateCRRightFileResponse:
        """
        权属文件添加
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRRightFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRRightFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRTort(
            self,
            request: models.CreateCRTortRequest,
            opts: Dict = None,
    ) -> models.CreateCRTortResponse:
        """
        举报侵权链接
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRTort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRTortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRUserVerify(
            self,
            request: models.CreateCRUserVerifyRequest,
            opts: Dict = None,
    ) -> models.CreateCRUserVerifyResponse:
        """
        本接口用于个人认证，新接入用户必须认证后才可以进行后续操作（个人认证和企业认证二选一），只需认证一次即可
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRUserVerify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRUserVerifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCRWork(
            self,
            request: models.CreateCRWorkRequest,
            opts: Dict = None,
    ) -> models.CreateCRWorkResponse:
        """
        新建作品
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCRWork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCRWorkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPCompanyInfo(
            self,
            request: models.DescribeBPCompanyInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBPCompanyInfoResponse:
        """
        查询企业信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPCompanyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPCompanyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPFakeURLs(
            self,
            request: models.DescribeBPFakeURLsRequest,
            opts: Dict = None,
    ) -> models.DescribeBPFakeURLsResponse:
        """
        查询仿冒链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPFakeURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPFakeURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPProtectURLs(
            self,
            request: models.DescribeBPProtectURLsRequest,
            opts: Dict = None,
    ) -> models.DescribeBPProtectURLsResponse:
        """
        查询保护网站
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPProtectURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPProtectURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBPReportFakeURLs(
            self,
            request: models.DescribeBPReportFakeURLsRequest,
            opts: Dict = None,
    ) -> models.DescribeBPReportFakeURLsResponse:
        """
        查询举报列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBPReportFakeURLs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBPReportFakeURLsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCRMonitorDetail(
            self,
            request: models.DescribeCRMonitorDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCRMonitorDetailResponse:
        """
        版权保护-查询作品监测详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCRMonitorDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCRMonitorDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCRMonitors(
            self,
            request: models.DescribeCRMonitorsRequest,
            opts: Dict = None,
    ) -> models.DescribeCRMonitorsResponse:
        """
        版权保护-查询监测列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCRMonitors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCRMonitorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCRObtainDetail(
            self,
            request: models.DescribeCRObtainDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCRObtainDetailResponse:
        """
        查询取证详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCRObtainDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCRObtainDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCRWorkInfo(
            self,
            request: models.DescribeCRWorkInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCRWorkInfoResponse:
        """
        查询作品基本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCRWorkInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCRWorkInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBPOfflineAttachment(
            self,
            request: models.ModifyBPOfflineAttachmentRequest,
            opts: Dict = None,
    ) -> models.ModifyBPOfflineAttachmentResponse:
        """
        修改下线材料
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBPOfflineAttachment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBPOfflineAttachmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCRBlockStatus(
            self,
            request: models.ModifyCRBlockStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCRBlockStatusResponse:
        """
        协查处置申请
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCRBlockStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCRBlockStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCRMonitor(
            self,
            request: models.ModifyCRMonitorRequest,
            opts: Dict = None,
    ) -> models.ModifyCRMonitorResponse:
        """
        开启/关闭监测
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCRMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCRMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCRObtainStatus(
            self,
            request: models.ModifyCRObtainStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCRObtainStatusResponse:
        """
        取证申请
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCRObtainStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCRObtainStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCRRightStatus(
            self,
            request: models.ModifyCRRightStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyCRRightStatusResponse:
        """
        发函申请
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCRRightStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCRRightStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCRWhiteList(
            self,
            request: models.ModifyCRWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyCRWhiteListResponse:
        """
        修改白名单列表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCRWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCRWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCRWork(
            self,
            request: models.UpdateCRWorkRequest,
            opts: Dict = None,
    ) -> models.UpdateCRWorkResponse:
        """
        更新作品
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCRWork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCRWorkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)