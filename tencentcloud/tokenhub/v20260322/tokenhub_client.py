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
from tencentcloud.tokenhub.v20260322 import models


class TokenhubClient(AbstractClient):
    _apiVersion = '2026-03-22'
    _endpoint = 'tokenhub.tencentcloudapi.com'
    _service = 'tokenhub'


    def CreateGlossary(self, request):
        r"""创建术语库。

        在当前应用下创建一个新的翻译术语库，用于自定义源语言到目标语言的术语映射。创建成功后返回术语库 ID，可通过该 ID 进一步管理术语条目。

        :param request: Request instance for CreateGlossary.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlossary", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlossaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlossaryEntries(self, request):
        r"""批量创建术语条目。

        在指定术语库下批量创建术语条目。单次最多创建 100 条。

        :param request: Request instance for CreateGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTokenPlanApiKeys(self, request):
        r"""批量创建 TokenPlan APIKey。

        传入名称前缀和数量，自动按 {ApiKeyName}-{序号} 格式生成名称（如 aaa-1, aaa-2）。允许同名。支持部分成功，最多 100 条。

        :param request: Request instance for CreateTokenPlanApiKeys.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanApiKeysRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanApiKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTokenPlanApiKeys", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTokenPlanApiKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTokenPlanTeamOrderAndBuy(self, request):
        r"""购买套餐。

        发起 TokenPlan 套餐下单并完成支付，成功后返回大订单 ID 及关联的子订单、资源信息。

        :param request: Request instance for CreateTokenPlanTeamOrderAndBuy.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanTeamOrderAndBuyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.CreateTokenPlanTeamOrderAndBuyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTokenPlanTeamOrderAndBuy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTokenPlanTeamOrderAndBuyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlossary(self, request):
        r"""删除术语库。

        删除指定的术语库及其下所有术语条目。删除操作幂等，对不存在的术语库返回成功。调用接口后，若通过 DescribeGlossaries 接口查询不到对应术语库，则表示删除成功。

        :param request: Request instance for DeleteGlossary.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlossary", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlossaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlossaryEntries(self, request):
        r"""批量删除术语条目。

        在指定术语库下批量删除术语条目。单次最多删除 200 条。若术语库不存在或不属于当前应用，返回 ResourceNotFound 错误。

        :param request: Request instance for DeleteGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTokenPlanApiKey(self, request):
        r"""删除 TokenPlan APIKey。

        同时删除额度中心子额度包并通知网关清除缓存。

        :param request: Request instance for DeleteTokenPlanApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DeleteTokenPlanApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DeleteTokenPlanApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTokenPlanApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTokenPlanApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiKey(self, request):
        r"""根据 API 密钥 ID 或密钥值查询 API 密钥详情，返回明文密钥。ApiKeyId 和 ApiKey 至少需传入其一，优先使用 ApiKeyId。

        :param request: Request instance for DescribeApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiKeyList(self, request):
        r"""查询 API 密钥列表。

        查询当前用户的 API 密钥列表，密钥值脱敏展示。支持分页、过滤和排序。

        :param request: Request instance for DescribeApiKeyList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeApiKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlossaries(self, request):
        r"""查询术语库列表。

        查询当前应用下的术语库列表。支持分页、过滤和排序。

        :param request: Request instance for DescribeGlossaries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossariesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlossaries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlossariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlossaryEntries(self, request):
        r"""查询术语条目列表。

        查询指定术语库下的术语条目。支持分页。

        :param request: Request instance for DescribeGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelList(self, request):
        r"""查询模型列表。

        支持按模型 ID、模型名称、模型能力等条件筛选，支持分页和排序。

        :param request: Request instance for DescribeModelList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeModelListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeModelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlan(self, request):
        r"""查询 TokenPlan 套餐详情。

        返回套餐基本信息及额度中心主额度包余量。

        :param request: Request instance for DescribeTokenPlan.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKey(self, request):
        r"""查询 TokenPlan APIKey 详情。

        返回 APIKey 完整信息（含明文密钥）及子额度包余量。

        :param request: Request instance for DescribeTokenPlanApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKeyList(self, request):
        r"""查询 TokenPlan APIKey 列表。

        返回指定套餐下的 APIKey 列表，密钥已脱敏。主账号可查看全部，子账号仅可查看自己创建的。

        :param request: Request instance for DescribeTokenPlanApiKeyList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKeyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKeySecret(self, request):
        r"""查询 TokenPlan APIKey 密钥（明文）。

        返回指定 APIKey 的明文密钥值，请妥善保管。

        :param request: Request instance for DescribeTokenPlanApiKeySecret.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeySecretRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeySecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKeySecret", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeySecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanApiKeyUsageDetail(self, request):
        r"""查询 TokenPlan APIKey 调用明细。

        从 CLS 日志服务查询套餐下的调用明细，按 pkg_id 过滤，支持游标分页。

        :param request: Request instance for DescribeTokenPlanApiKeyUsageDetail.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyUsageDetailRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanApiKeyUsageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanApiKeyUsageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanApiKeyUsageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTokenPlanList(self, request):
        r"""查询 TokenPlan 套餐列表。

        支持分页、过滤和排序。主账号可查看全部，子账号仅可查看自己创建的。返回结果包含每个套餐关联的额度中心主额度包详情。

        :param request: Request instance for DescribeTokenPlanList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeTokenPlanListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTokenPlanList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenPlanListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsageRankList(self, request):
        r"""查询用量排行列表。

        按 apikey、endpoint、model 三个维度统计指定时间窗内的用量排行，返回顶部数据卡所需的 PageStats/TotalStats、左侧 Top 列表（含每对象整段累计值）、右侧色块趋势图所需的逐点曲线。前端通过 Offset 翻页、ShowAll 切换 CSV 全量导出模式。

        MetricType 字段用于切换指标族，本期支持 tokens；接口预留以支持后续指标族扩展。响应回显 MetricType 与 MetricKeys（实际参与渲染的 metric key 列表，顺序固定 [Total, Input, Output]），前端按此渲染顶部数据卡与趋势图，无需硬编码 key 名。

        :param request: Request instance for DescribeUsageRankList.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.DescribeUsageRankListRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.DescribeUsageRankListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsageRankList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageRankListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlossaryEntries(self, request):
        r"""批量修改术语条目。

        在指定术语库下批量修改术语条目。单次最多修改 200 条。

        :param request: Request instance for ModifyGlossaryEntries.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyGlossaryEntriesRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyGlossaryEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlossaryEntries", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlossaryEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTokenPlanApiKey(self, request):
        r"""修改 TokenPlan APIKey 配置（网关关注字段）。

        修改后自动通知网关更新缓存并同步额度中心。

        :param request: Request instance for ModifyTokenPlanApiKey.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeyRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTokenPlanApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTokenPlanApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTokenPlanApiKeySecret(self, request):
        r"""重置 TokenPlan APIKey 密钥。

        重新生成密钥值，密钥版本号递增，旧密钥立即失效。APIKey ID 不变。重置后需通过 DescribeTokenPlanApiKeySecret 查询新密钥。

        :param request: Request instance for ModifyTokenPlanApiKeySecret.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeySecretRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.ModifyTokenPlanApiKeySecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTokenPlanApiKeySecret", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTokenPlanApiKeySecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewTokenPlanTeamOrder(self, request):
        r"""续费套餐。

        对已有的 TokenPlan 套餐发起续费下单并完成支付，成功后返回大订单 ID 及关联的子订单、资源信息。

        :param request: Request instance for RenewTokenPlanTeamOrder.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.RenewTokenPlanTeamOrderRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.RenewTokenPlanTeamOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewTokenPlanTeamOrder", params, headers=headers)
            response = json.loads(body)
            model = models.RenewTokenPlanTeamOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeTokenPlanTeamOrder(self, request):
        r"""升配套餐。

        对已有的 TokenPlan 套餐发起升配下单并完成支付，扩容积分或 Token 额度，成功后返回大订单 ID 及关联的子订单、资源信息。新额度必须大于当前额度。

        :param request: Request instance for UpgradeTokenPlanTeamOrder.
        :type request: :class:`tencentcloud.tokenhub.v20260322.models.UpgradeTokenPlanTeamOrderRequest`
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UpgradeTokenPlanTeamOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeTokenPlanTeamOrder", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeTokenPlanTeamOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))