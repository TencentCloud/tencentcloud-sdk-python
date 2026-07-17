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

    async def CreateApiKey(
            self,
            request: models.CreateApiKeyRequest,
            opts: Dict = None,
    ) -> models.CreateApiKeyResponse:
        """
        创建 API 密钥。

        创建一个新的 API 密钥，创建成功后返回 API 密钥 ID。需指定平台类型、绑定方式和初始状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEndpoint(
            self,
            request: models.CreateEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateEndpointResponse:
        """
        创建推理服务。

        创建一个在线推理服务，创建成功后返回推理服务 ID。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlossary(
            self,
            request: models.CreateGlossaryRequest,
            opts: Dict = None,
    ) -> models.CreateGlossaryResponse:
        """
        创建术语库。(单个用户默认最多可以创建50个术语库，支持加白)

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
        单个术语库默认最多总共可以创建10000个术语对
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
        购买套餐（重新开通过期的套餐续费也通过该接口实现，需要额外传已过期套餐teamId。注：续费成功后套餐包总周期数（TotalCycles）会包含历史周期数，实际套餐包生效周期以生效时间（StartTime）和到期时间（ExpireTime）为准）。

        发起 TokenPlan 套餐下单并完成支付，成功后返回大订单 ID 及关联的子订单、资源信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTokenPlanTeamOrderAndBuy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTokenPlanTeamOrderAndBuyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApiKey(
            self,
            request: models.DeleteApiKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteApiKeyResponse:
        """
        删除指定的 API 密钥，同时清理关联的模型绑定关系。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApiKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApiKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEndpoint(
            self,
            request: models.DeleteEndpointRequest,
            opts: Dict = None,
    ) -> models.DeleteEndpointResponse:
        """
        删除推理服务。

        删除指定的推理服务端点，操作不可逆。调用接口后，若通过 DescribeEndpoint 接口查询不到对应的端点，则表示删除成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEndpointResponse
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
        
    async def DescribeEndpoint(
            self,
            request: models.DescribeEndpointRequest,
            opts: Dict = None,
    ) -> models.DescribeEndpointResponse:
        """
        查询推理服务详情。

        根据推理服务 ID 查询推理服务的详细信息，包括计费信息、免费额度、API 调用地址等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndpointResponse
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
        
    async def DescribeModelEndpointList(
            self,
            request: models.DescribeModelEndpointListRequest,
            opts: Dict = None,
    ) -> models.DescribeModelEndpointListResponse:
        """
        查询模型接入点列表。

        以模型为基准展示所有在线文本类型模型的接入点概览，支持按状态、计费方式、创建来源等条件筛选，使用 Offset/Limit 分页。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModelEndpointList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelEndpointListResponse
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

        从 CLS 日志服务查询套餐下的调用明细，按 team_id 过滤，支持游标分页。
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

        指标族（MetricType）
        - `tokens`（默认）：Token 用量统计。支持 Dimension = apikey / endpoint / model。
          返回指标：TotalToken（总）/ InputTotalToken（输入）/ OutputTotalToken（输出）/ CacheTotalToken（读缓存）。
        - `search`：【待上线】联网搜索用量统计。支持 Dimension = apikey / endpoint / model。
          返回指标：SearchRequestCount（搜索请求数）/ SearchCount（搜索引擎调用次数）。

        响应内容
        - MetricType 字段用于切换指标族，响应回显 MetricType 与 MetricKeys。
        - TotalStats：时间窗内全部对象的整段聚合值。
        - PageStats：当前翻页内对象的整段聚合值。
        - TopList：按MetricKeys[0]降序的对象列表，含整段聚合值与逐时间点曲线。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageRankList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageRankListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiKeyInfo(
            self,
            request: models.ModifyApiKeyInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyApiKeyInfoResponse:
        """
        更新 API 密钥信息。

        更新 API 密钥的备注信息、 IP 白名单和 Token 限额（修改限额推荐使用QuotaDesired参数）。所有可选参数不传表示不修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiKeyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiKeyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApiKeyStatus(
            self,
            request: models.ModifyApiKeyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApiKeyStatusResponse:
        """
        更新 API 密钥的启用或禁用状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApiKeyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApiKeyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEndpoint(
            self,
            request: models.ModifyEndpointRequest,
            opts: Dict = None,
    ) -> models.ModifyEndpointResponse:
        """
        修改推理服务。

        修改推理服务的属性，支持修改服务名称、QPM/TPM 限流上限、TPM 包续费设置、智能路由开关和手动重试 TPM 购买。

        注意事项：
        - 不支持通过本接口切换计费类型（ChargeType），计费类型仅可在创建推理服务（CreateEndpoint）时指定。
        - 不支持通过本接口修改 TPM 预付费保障包的 quota（TpmInputLimit/TpmOutputLimit/TimeSpan），这些值仅可在创建推理服务时指定。
        - 当 RetryTPMPurchase 为 true 时，系统会异步重试 TPM 包购买，调用后需轮询推理服务状态确认结果。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEndpointResponse
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