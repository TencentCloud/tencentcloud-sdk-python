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
from tencentcloud.tokenhub.v20260322 import models
from typing import Dict


class TokenhubClient(AbstractClient):
    _apiVersion = '2026-03-22'
    _endpoint = 'tokenhub.tencentcloudapi.com'
    _service = 'tokenhub'

    async def CreateGlossary(
            self,
            request: models.CreateGlossaryRequest,
            opts: Dict = None,
    ) -> models.CreateGlossaryResponse:
        """
        创建术语库。

        在当前应用下创建一个新的翻译术语库，用于自定义源语言到目标语言的术语映射。创建成功后返回术语库 ID，可通过该 ID 进一步管理术语条目。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlossary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlossaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlossaryEntries(
            self,
            request: models.CreateGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.CreateGlossaryEntriesResponse:
        """
        批量创建术语条目。

        在指定术语库下批量创建术语条目。单次最多创建 100 条。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTokenPlanApiKeys(
            self,
            request: models.CreateTokenPlanApiKeysRequest,
            opts: Dict = None,
    ) -> models.CreateTokenPlanApiKeysResponse:
        """
        批量创建 TokenPlan APIKey。

        传入名称前缀和数量，自动按 {ApiKeyName}-{序号} 格式生成名称（如 aaa-1, aaa-2）。允许同名。支持部分成功，最多 100 条。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTokenPlanApiKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTokenPlanApiKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTokenPlanTeamOrderAndBuy(
            self,
            request: models.CreateTokenPlanTeamOrderAndBuyRequest,
            opts: Dict = None,
    ) -> models.CreateTokenPlanTeamOrderAndBuyResponse:
        """
        购买套餐。

        发起 TokenPlan 套餐下单并完成支付，成功后返回大订单 ID 及关联的子订单、资源信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTokenPlanTeamOrderAndBuy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTokenPlanTeamOrderAndBuyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlossary(
            self,
            request: models.DeleteGlossaryRequest,
            opts: Dict = None,
    ) -> models.DeleteGlossaryResponse:
        """
        删除术语库。

        删除指定的术语库及其下所有术语条目。删除操作幂等，对不存在的术语库返回成功。调用接口后，若通过 DescribeGlossaries 接口查询不到对应术语库，则表示删除成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlossary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlossaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlossaryEntries(
            self,
            request: models.DeleteGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.DeleteGlossaryEntriesResponse:
        """
        批量删除术语条目。

        在指定术语库下批量删除术语条目。单次最多删除 200 条。若术语库不存在或不属于当前应用，返回 ResourceNotFound 错误。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTokenPlanApiKey(
            self,
            request: models.DeleteTokenPlanApiKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteTokenPlanApiKeyResponse:
        """
        删除 TokenPlan APIKey。

        同时删除额度中心子额度包并通知网关清除缓存。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTokenPlanApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTokenPlanApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKey(
            self,
            request: models.DescribeApiKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeyResponse:
        """
        根据 API 密钥 ID 或密钥值查询 API 密钥详情，返回明文密钥。ApiKeyId 和 ApiKey 至少需传入其一，优先使用 ApiKeyId。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApiKeyList(
            self,
            request: models.DescribeApiKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeApiKeyListResponse:
        """
        查询 API 密钥列表。

        查询当前用户的 API 密钥列表，密钥值脱敏展示。支持分页、过滤和排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApiKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApiKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlossaries(
            self,
            request: models.DescribeGlossariesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlossariesResponse:
        """
        查询术语库列表。

        查询当前应用下的术语库列表。支持分页、过滤和排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlossaries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlossariesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlossaryEntries(
            self,
            request: models.DescribeGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlossaryEntriesResponse:
        """
        查询术语条目列表。

        查询指定术语库下的术语条目。支持分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModelList(
            self,
            request: models.DescribeModelListRequest,
            opts: Dict = None,
    ) -> models.DescribeModelListResponse:
        """
        查询模型列表。

        支持按模型 ID、模型名称、模型能力等条件筛选，支持分页和排序。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlan(
            self,
            request: models.DescribeTokenPlanRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanResponse:
        """
        查询 TokenPlan 套餐详情。

        返回套餐基本信息及额度中心主额度包余量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKey(
            self,
            request: models.DescribeTokenPlanApiKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeyResponse:
        """
        查询 TokenPlan APIKey 详情。

        返回 APIKey 完整信息（含明文密钥）及子额度包余量。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKeyList(
            self,
            request: models.DescribeTokenPlanApiKeyListRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeyListResponse:
        """
        查询 TokenPlan APIKey 列表。

        返回指定套餐下的 APIKey 列表，密钥已脱敏。主账号可查看全部，子账号仅可查看自己创建的。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKeyList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeyListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKeySecret(
            self,
            request: models.DescribeTokenPlanApiKeySecretRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeySecretResponse:
        """
        查询 TokenPlan APIKey 密钥（明文）。

        返回指定 APIKey 的明文密钥值，请妥善保管。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKeySecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeySecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanApiKeyUsageDetail(
            self,
            request: models.DescribeTokenPlanApiKeyUsageDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanApiKeyUsageDetailResponse:
        """
        查询 TokenPlan APIKey 调用明细。

        从 CLS 日志服务查询套餐下的调用明细，按 pkg_id 过滤，支持游标分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanApiKeyUsageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanApiKeyUsageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTokenPlanList(
            self,
            request: models.DescribeTokenPlanListRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenPlanListResponse:
        """
        查询 TokenPlan 套餐列表。

        支持分页、过滤和排序。主账号可查看全部，子账号仅可查看自己创建的。返回结果包含每个套餐关联的额度中心主额度包详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTokenPlanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenPlanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsageRankList(
            self,
            request: models.DescribeUsageRankListRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageRankListResponse:
        """
        查询用量排行列表。

        按 apikey、endpoint、model 三个维度统计指定时间窗内的用量排行，返回顶部数据卡所需的 PageStats/TotalStats、左侧 Top 列表（含每对象整段累计值）、右侧色块趋势图所需的逐点曲线。前端通过 Offset 翻页、ShowAll 切换 CSV 全量导出模式。

        MetricType 字段用于切换指标族，本期支持 tokens；接口预留以支持后续指标族扩展。响应回显 MetricType 与 MetricKeys（实际参与渲染的 metric key 列表，顺序固定 [Total, Input, Output]），前端按此渲染顶部数据卡与趋势图，无需硬编码 key 名。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageRankList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageRankListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlossaryEntries(
            self,
            request: models.ModifyGlossaryEntriesRequest,
            opts: Dict = None,
    ) -> models.ModifyGlossaryEntriesResponse:
        """
        批量修改术语条目。

        在指定术语库下批量修改术语条目。单次最多修改 200 条。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlossaryEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlossaryEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTokenPlanApiKey(
            self,
            request: models.ModifyTokenPlanApiKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyTokenPlanApiKeyResponse:
        """
        修改 TokenPlan APIKey 配置（网关关注字段）。

        修改后自动通知网关更新缓存并同步额度中心。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTokenPlanApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTokenPlanApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTokenPlanApiKeySecret(
            self,
            request: models.ModifyTokenPlanApiKeySecretRequest,
            opts: Dict = None,
    ) -> models.ModifyTokenPlanApiKeySecretResponse:
        """
        重置 TokenPlan APIKey 密钥。

        重新生成密钥值，密钥版本号递增，旧密钥立即失效。APIKey ID 不变。重置后需通过 DescribeTokenPlanApiKeySecret 查询新密钥。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTokenPlanApiKeySecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTokenPlanApiKeySecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewTokenPlanTeamOrder(
            self,
            request: models.RenewTokenPlanTeamOrderRequest,
            opts: Dict = None,
    ) -> models.RenewTokenPlanTeamOrderResponse:
        """
        续费套餐。

        对已有的 TokenPlan 套餐发起续费下单并完成支付，成功后返回大订单 ID 及关联的子订单、资源信息。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewTokenPlanTeamOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewTokenPlanTeamOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeTokenPlanTeamOrder(
            self,
            request: models.UpgradeTokenPlanTeamOrderRequest,
            opts: Dict = None,
    ) -> models.UpgradeTokenPlanTeamOrderResponse:
        """
        升配套餐。

        对已有的 TokenPlan 套餐发起升配下单并完成支付，扩容积分或 Token 额度，成功后返回大订单 ID 及关联的子订单、资源信息。新额度必须大于当前额度。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeTokenPlanTeamOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeTokenPlanTeamOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)