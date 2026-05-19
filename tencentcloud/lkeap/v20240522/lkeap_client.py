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
from tencentcloud.lkeap.v20240522 import models


class LkeapClient(AbstractClient):
    _apiVersion = '2024-05-22'
    _endpoint = 'lkeap.tencentcloudapi.com'
    _service = 'lkeap'


    def CancelTask(self, request):
        r"""文档解析任务取消

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChatCompletions(self, request):
        r"""### 接口功能

        调用接口，发起一次对话请求。默认该接口下的单账号QPM上限为15000 ，TPM上限为1200000
        如需使用OpenAI兼容接口， 请参考文档：[Deepseek OpenAI对话接口](https://cloud.tencent.com/document/product/1772/115969)

        #### 在线体验
        如您希望在网页内直接体验 DeepSeek 模型对话，推荐您前往[腾讯云智能体开发平台](https://cloud.tencent.com/product/lke)，使用[ DeepSeek 联网助手](https://lke.cloud.tencent.com/webim_exp/#/chat/wQrAwR)。

        #### 已支持的模型
        - DeepSeek-V3-0324（model 参数值为**deepseek-v3-0324**）
            - DeepSeek-V3-0324为671B参数MoE模型，在编程与技术能力、上下文理解与长文本处理等方面优势突出。
            - 支持128K上下文长度，最大输出16k（不含思维链）。
            - 注意：相比于DeepSeek-V3，DeepSeek-V3-0324仅更新了模型权重，未增加参数量。总模型大小为685B，其中包括671B的主模型权重和 14B 的多令牌预测（MTP）模块权重，后续均描述主模型参数量。
        - DeepSeek-R1-0528（model 参数值为**deepseek-r1-0528**）
            - DeepSeek-R1-0528为671B 模型，架构优化与训练策略升级后，相比上一版本在代码生成、长文本处理和复杂推理领域提升明显。
            -  支持128K上下文长度，最大输入长度96k，最大输出16k（默认4k），最大思维链输出长度32k。
        - DeepSeek-V3.1-Terminus（model 参数值为 deepseek-v3.1-terminus）
            - DeepSeek-V3.1-Terminus 为685B 参数 MoE 模型，在保持模型原有能力的基础上，优化了语言一致性，Agent 能力等问题，输出效果相比前一版本更加稳定。
            -  支持128K上下文长度，最大输入长度96k，最大输出32k（默认4k），最大思维链输出长度32k。
        - DeepSeek-V3.2（model 参数值为 deepseek-v3.2）
            - DeepSeek-V3.2 为685B 参数 MoE 模型，其引入的稀疏注意力架构使长文本处理更高效，并在推理评测中达到GPT-5水平。
            -  支持128K上下文长度，最大输入长度96k，最大输出32k（默认4k），最大思维链输出长度32k。
            -  默认单账号下 DeepSeek-V3.2 模型的限制为：QPM：15,000 ，TPM：300,000
        ### 计费说明

        - 标准计费（2025年2月26日起生效），计费模式为后付费小时结，为保证您账户资源的正常使用，请提前[开通后付费](https://console.cloud.tencent.com/lkeap/settings)并及时[充值](https://console.cloud.tencent.com/expense/recharge)。

            -  DeepSeek-R1-0528 模型   | 输入：0.004元/千token | 输出（含思维链）：0.016元/千token

            - DeepSeek-V3-0324 模型 | 输入：0.002元/千token | 输出：0.008元/千token

            - DeepSeek-V3.1-Terminus 模型 | 输入：0.004元/千token | 输出：0.012元/千token

            - DeepSeek-V3.2 模型 | 输入：0.002元/千token | 输出：0.003元/千token


        ### Openai兼容协议接口
        知识引擎原子能力大模型对话 API 兼容了 OpenAI 的接口规范，这意味着您可以直接使用 OpenAI 官方提供的 SDK 来调用大模型对话接口。您仅需要将 base_url 和 [api_key](https://cloud.tencent.com/document/product/1772/115970) 替换成相关配置，不需要对应用做额外修改，即可无缝将您的应用切换到相应的大模型。请参考文档：[Deepseek OpenAI对话接口](https://cloud.tencent.com/document/product/1772/115969)。
        > base_url：  https://api.lkeap.cloud.tencent.com/v1

        > api_key的获取请参考[API KEY管理](https://cloud.tencent.com/document/product/1772/115970)


        ### 快速接入
        1. 完成[实名认证](https://console.cloud.tencent.com/developer/auth)。
        2. 主账户前往[控制台](https://console.cloud.tencent.com/lkeap)开通服务。若为子账户，需由主账号在[权限管理](https://console.cloud.tencent.com/cam)中为子账号授权，关联预设策略，策略名称：QcloudLKEAPFullAccess。
        3. 通过API Explorer[在线调试](https://console.cloud.tencent.com/api/explorer?Product=lkeap&Version=2024-05-22&Action=ChatCompletions)。
        4. 使用[官方 SDK ](https://cloud.tencent.com/document/product/1772/115963#SDK)调用本接口（支持Python/Java/PHP/Go/Node.js/.NET等语言）。

        -----------

        ### SDK调用示例
        通过本地代码调用本接口（支持Python/Java/PHP/Go/Node.js/.NET等语言）：下面的代码以 Python 语言为例，展示如何访问腾讯云上的DeepSeek模型API的样例。
        （1）安装环境
        ```
        python3 -m pip install --upgrade tencentcloud-sdk-python-common
        python3 -m pip install --upgrade tencentcloud-sdk-python-lkeap
        ```

        （2）示例代码

        - 其中SecretKey和SecretID需要从腾讯云控制台获取

        - 参数params中模型Model字段可以选择“deepseek-r1-0528“和“deepseek-v3-0324”

        ```
        # -*- coding: utf-8 -*-
        import json

        from tencentcloud.common.common_client import CommonClient
        from tencentcloud.common import credential
        from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
        from tencentcloud.common.profile.client_profile import ClientProfile
        from tencentcloud.common.profile.http_profile import HttpProfile

        class NonStreamResponse(object):
            def __init__(self):
                self.response = ""

            def _deserialize(self, obj):
                self.response = json.dumps(obj)

        try:
            # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
            # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
            # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
            cred = credential.Credential("", "")

            httpProfile = HttpProfile()
            httpProfile.endpoint = "lkeap.tencentcloudapi.com"
            httpProfile.reqTimeout = 40000  # 流式接口可能耗时较长
            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile

            params = "{\"Model\":\"deepseek-r1-0528\",\"Messages\":[{\"Role\":\"user\",\"Content\":\"你好\"}],\"Stream\":true}";
            common_client = CommonClient("lkeap", "2024-05-22", cred, "ap-guangzhou", profile=clientProfile)
            resp = common_client._call_and_deserialize("ChatCompletions", json.loads(params), NonStreamResponse)
            if isinstance(resp, NonStreamResponse):  # 非流式响应
                print(resp.response)
            else:  # 流式响应
                for event in resp:
                    print(event)
        except TencentCloudSDKException as err:
            print(err)

        ```

        **DeepSeek-R1-0528使用建议**

        1. 将温度设置在 0.5-0.7 范围内（建议为0.6），以防止无休止的重复或不连贯的输出。
        2. 避免添加system prompt，所有说明都应包含在user prompt中。

        :param request: Request instance for ChatCompletions.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.ChatCompletionsRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ChatCompletionsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ChatCompletions", params, models.ChatCompletionsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReconstructDocumentFlow(self, request):
        r"""本接口为异步接口的发起请求接口，用于发起文档解析任务。
        文档解析支持将图片或PDF、DOCX、PPTX、EXCEL等文件转换成Markdown格式文件，可解析包括表格、公式、图片、标题、段落、页眉、页脚等内容元素，并将内容智能转换成阅读顺序。具体支持文件类型请查看下方输入参数列表。

        体验期间单账号限制qps仅为1，若有正式接入需要请与产研团队沟通开放。

        :param request: Request instance for CreateReconstructDocumentFlow.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReconstructDocumentFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReconstructDocumentFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSplitDocumentFlow(self, request):
        r"""用于创建一个文档拆分任务，支持多种文件类型，具备mllm能力，能够解析并深入理解图表中的信息。

        :param request: Request instance for CreateSplitDocumentFlow.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSplitDocumentFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSplitDocumentFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCharacterUsage(self, request):
        r"""获取字符使用量统计

        :param request: Request instance for GetCharacterUsage.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.GetCharacterUsageRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.GetCharacterUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCharacterUsage", params, headers=headers)
            response = json.loads(body)
            model = models.GetCharacterUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmbedding(self, request):
        r"""本接口（GetEmbedding）调用文本表示模型，将文本转化为用数值表示的向量形式，可用于文本检索、信息推荐、知识挖掘等场景。
        本接口（GetEmbedding）有单账号调用上限控制，如您有提高并发限制的需求请 [联系我们](https://cloud.tencent.com/act/event/Online_service) 。

        :param request: Request instance for GetEmbedding.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.GetEmbeddingRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.GetEmbeddingResponse`

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


    def GetReconstructDocumentResult(self, request):
        r"""本接口为异步接口的查询结果接口，用于获取文档解析处理结果。

        :param request: Request instance for GetReconstructDocumentResult.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.GetReconstructDocumentResultRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.GetReconstructDocumentResultResponse`

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


    def GetSplitDocumentResult(self, request):
        r"""查询文档拆分任务结果

        :param request: Request instance for GetSplitDocumentResult.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.GetSplitDocumentResultRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.GetSplitDocumentResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSplitDocumentResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetSplitDocumentResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryRewrite(self, request):
        r"""多轮改写（QueryRewrite）主要用于多轮对话中，进行指代消解和省略补全。使用本接口，无需输入prompt描述，根据对话历史即可生成更精确的用户查询。在应用场景上，本接口可应用于智能问答、对话式搜索等多种场景。
        开通[产品体验](https://lke.cloud.tencent.com/lke/#/trialProduct)后可获得50wtoken体验额度。本接口（QueryRewrite）有单账号调用上限控制，如您有提高并发限制的需求请 [联系我们](https://cloud.tencent.com/act/event/Online_service) 。

        :param request: Request instance for QueryRewrite.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.QueryRewriteRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.QueryRewriteResponse`

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


    def ReconstructDocumentSSE(self, request):
        r"""准实时文档解析接口，使用HTTP SSE 协议通信。
        支持将图片或PDF文件转换成Markdown格式文件，可解析包括表格、公式、图片、标题、段落、页眉、页脚等内容元素，并将内容智能转换成阅读顺序。
        输入：pdf、ppt、docx、doc、jpg等
        输出：正常阅读顺序的md文件、识别结果的json（可选）等

        :param request: Request instance for ReconstructDocumentSSE.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSERequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSEResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ReconstructDocumentSSE", params, models.ReconstructDocumentSSEResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunRerank(self, request):
        r"""基于知识引擎精调模型技术的rerank模型，支持对多路召回的结果进行重排序，根据query与切片内容的相关性，按照顺序给出每一条结果和query的相关性分数。

        :param request: Request instance for RunRerank.
        :type request: :class:`tencentcloud.lkeap.v20240522.models.RunRerankRequest`
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.RunRerankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunRerank", params, headers=headers)
            response = json.loads(body)
            model = models.RunRerankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))