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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class ActivateServiceRequest(AbstractModel):
    """ActivateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PayMode: 开通之后，是否关闭后付费；默认为0，不关闭；1为关闭
        :type PayMode: int
        """
        self._PayMode = None

    @property
    def PayMode(self):
        """开通之后，是否关闭后付费；默认为0，不关闭；1为关闭
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateServiceResponse(AbstractModel):
    """ActivateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Character(AbstractModel):
    """人物描述

    """

    def __init__(self):
        r"""
        :param _Name: 人物名称
        :type Name: str
        :param _SystemPrompt: 人物对应SystemPrompt
        :type SystemPrompt: str
        """
        self._Name = None
        self._SystemPrompt = None

    @property
    def Name(self):
        """人物名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SystemPrompt(self):
        """人物对应SystemPrompt
        :rtype: str
        """
        return self._SystemPrompt

    @SystemPrompt.setter
    def SystemPrompt(self, SystemPrompt):
        self._SystemPrompt = SystemPrompt


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SystemPrompt = params.get("SystemPrompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionsRequest(AbstractModel):
    """ChatCompletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型名称，可选值包括 hunyuan-lite、hunyuan-standard、hunyuan-standard-256K、hunyuan-code、hunyuan-role、hunyuan-functioncall、hunyuan-vision、hunyuan-turbo、hunyuan-turbo-latest、hunyuan-turbo-20241223、hunyuan-turbo-20241120、hunyuan-large、hunyuan-large-longcontext、hunyuan-turbo-vision、hunyuan-standard-vision、hunyuan-lite-vision、hunyuan-turbos-20250226、hunyuan-turbos-latest、hunyuan-t1-20250321、hunyuan-t1-latest、hunyuan-turbos-role-plus。各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。注意：不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :type Model: str
        :param _Messages: 聊天上下文信息。
说明：
1. 长度最多为 40，按对话时间从旧到新在数组中排列。
2. Message.Role 可选值：system、user、assistant、 tool（functioncall场景）。
其中，system 角色可选，如存在则必须位于列表的最开始。user（tool） 和 assistant 需交替出现（一问一答），以 user 提问开始，user（tool）提问结束，其中tool可以连续出现多次，且 Content 不能为空。Role 的顺序示例：[system（可选） user assistant user（tool tool ...） assistant user（tool tool ...） ...]。
3. Messages 中 Content 总长度不能超过模型输入长度上限（可参考 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 文档），超过则会截断最前面的内容，只保留尾部内容。
        :type Messages: list of Message
        :param _Stream: 流式调用开关。
说明：
1. 未传值时默认为非流式调用（false）。
2. 流式调用时以 SSE 协议增量返回结果（返回值取 Choices[n].Delta 中的值，需要拼接增量数据才能获得完整结果）。
3. 非流式调用时：
调用方式与普通 HTTP 请求无异。
接口响应耗时较长，**如需更低时延建议设置为 true**。
只返回一次最终结果（返回值取 Choices[n].Message 中的值）。

注意：
通过 SDK 调用时，流式和非流式调用需用**不同的方式**获取返回值，具体参考 SDK 中的注释或示例（在各语言 SDK 代码仓库的 examples/hunyuan/v20230901/ 目录中）。
        :type Stream: bool
        :param _StreamModeration: 流式输出审核开关。
说明：
1. 当使用流式输出（Stream 字段值为 true）时，该字段生效。
2. 输出审核有流式和同步两种模式，**流式模式首包响应更快**。未传值时默认为流式模式（true）。
3. 如果值为 true，将对输出内容进行分段审核，审核通过的内容流式输出返回。如果出现审核不过，响应中的 FinishReason 值为 sensitive。
4. 如果值为 false，则不使用流式输出审核，需要审核完所有输出内容后再返回结果。

注意：
当选择流式输出审核时，可能会出现部分内容已输出，但中间某一段响应中的 FinishReason 值为 sensitive，此时说明安全审核未通过。如果业务场景有实时文字上屏的需求，需要自行撤回已上屏的内容，并建议自定义替换为一条提示语，如 “这个问题我不方便回答，不如我们换个话题试试”，以保障终端体验。
        :type StreamModeration: bool
        :param _TopP: 说明：
1. 影响输出文本的多样性。模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。
2. 取值区间为 [0.0, 1.0]。取值越大，生成文本的多样性越强。
        :type TopP: float
        :param _Temperature: 说明：
1. 影响模型输出多样性，模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。
2. 取值区间为 [0.0, 2.0]。较高的数值会使输出更加多样化和不可预测，而较低的数值会使其更加集中和确定。
        :type Temperature: float
        :param _EnableEnhancement: 功能增强（如搜索）开关。
说明：
1. hunyuan-lite 无功能增强（如搜索）能力，该参数对 hunyuan-lite 版本不生效。
2. 未传值时默认打开开关。
3. 关闭时将直接由主模型生成回复内容，可以降低响应时延（对于流式输出时的首字时延尤为明显）。但在少数场景里，回复效果可能会下降。
4. 安全审核能力不属于功能增强范围，不受此字段影响。
5. 2025-04-20 00:00:00起，由默认开启状态转为默认关闭状态。
        :type EnableEnhancement: bool
        :param _Tools: 可调用的工具列表，仅对 hunyuan-turbo、hunyuan-functioncall 模型生效。
        :type Tools: list of Tool
        :param _ToolChoice: 工具使用选项，可选值包括 none、auto、custom。说明：1. 仅对 hunyuan-turbo、hunyuan-functioncall 模型生效。2. none：不调用工具；auto：模型自行选择生成回复或调用工具；custom：强制模型调用指定的工具。3. 未设置时，默认值为auto
        :type ToolChoice: str
        :param _CustomTool: 强制模型调用指定的工具，当参数ToolChoice为custom时，此参数为必填
        :type CustomTool: :class:`tencentcloud.hunyuan.v20230901.models.Tool`
        :param _SearchInfo: 默认是false，在值为true且命中搜索时，接口会返回SearchInfo
        :type SearchInfo: bool
        :param _Citation: 搜索引文角标开关。
说明：
1. 配合EnableEnhancement和SearchInfo参数使用。打开后，回答中命中搜索的结果会在片段后增加角标标志，对应SearchInfo列表中的链接。
2. false：开关关闭，true：开关打开。
3. 未传值时默认开关关闭（false）。
        :type Citation: bool
        :param _EnableSpeedSearch: 是否开启极速版搜索，默认false，不开启；在开启且命中搜索时，会启用极速版搜索，流式输出首字返回更快。
        :type EnableSpeedSearch: bool
        :param _EnableMultimedia: 多媒体开关。
详细介绍请阅读 [多媒体介绍](https://cloud.tencent.com/document/product/1729/111178) 中的说明。
说明：
1. 该参数目前仅对白名单内用户生效，如您想体验该功能请 [联系我们](https://cloud.tencent.com/act/event/Online_service)。
2. 该参数仅在功能增强（如搜索）开关开启（EnableEnhancement=true）并且极速版搜索开关关闭（EnableSpeedSearch=false）时生效。
3. hunyuan-lite 无多媒体能力，该参数对 hunyuan-lite 版本不生效。
4. 未传值时默认关闭。
5. 开启并搜索到对应的多媒体信息时，会输出对应的多媒体地址，可以定制个性化的图文消息。
        :type EnableMultimedia: bool
        :param _EnableDeepSearch: 是否开启深度研究该问题，默认是false，在值为true且命中深度研究该问题时，会返回深度研究该问题信息。
        :type EnableDeepSearch: bool
        :param _Seed: 说明： 1. 确保模型的输出是可复现的。 2. 取值区间为非0正整数，最大值10000。 3. 非必要不建议使用，不合理的取值会影响效果。
        :type Seed: int
        :param _ForceSearchEnhancement: 强制搜索增强开关。
说明：
1. 未传值时默认关闭。
2. 开启后，将强制走AI搜索，当AI搜索结果为空时，由大模型回复兜底话术。
        :type ForceSearchEnhancement: bool
        :param _Stop: 自定义结束生成字符串

调用 OpenAI 的接口时，如果您指定了 `stop` 参数, 模型会停止在匹配到 `stop` 的内容之前。
在调用混元接口时，会停止在匹配到 `stop` 的内容之后。

**说明：**
未来我们可能会修改此行为以便和 OpenAI 保持一致。
但是目前有使用该参数的情况下，开发者需要注意该参数是否会对应用造成影响，以及未来该行为调整时带来的影响。
        :type Stop: list of str
        :param _EnableRecommendedQuestions: 推荐问答开关。
说明：
1. 未传值时默认关闭。
2. 开启后，在返回值的最后一个包中会增加 RecommendedQuestions 字段表示推荐问答， 最多返回3条。
        :type EnableRecommendedQuestions: bool
        :param _EnableDeepRead: 是否开启深度阅读，默认是false，在值为true时，会返回深度阅读的结果信息。说明:1.深度阅读需要开启插件增强,即设置EnableEnhancement为true,当设置EnableDeepRead为true时EnableEnhancement默认为true；2.目前暂时只支持单文档单轮的深度阅读；3.深度阅读功能的文件上传可以使用FilesUploads接口，具体参数详见FilesUploads接口文档
        :type EnableDeepRead: bool
        """
        self._Model = None
        self._Messages = None
        self._Stream = None
        self._StreamModeration = None
        self._TopP = None
        self._Temperature = None
        self._EnableEnhancement = None
        self._Tools = None
        self._ToolChoice = None
        self._CustomTool = None
        self._SearchInfo = None
        self._Citation = None
        self._EnableSpeedSearch = None
        self._EnableMultimedia = None
        self._EnableDeepSearch = None
        self._Seed = None
        self._ForceSearchEnhancement = None
        self._Stop = None
        self._EnableRecommendedQuestions = None
        self._EnableDeepRead = None

    @property
    def Model(self):
        """模型名称，可选值包括 hunyuan-lite、hunyuan-standard、hunyuan-standard-256K、hunyuan-code、hunyuan-role、hunyuan-functioncall、hunyuan-vision、hunyuan-turbo、hunyuan-turbo-latest、hunyuan-turbo-20241223、hunyuan-turbo-20241120、hunyuan-large、hunyuan-large-longcontext、hunyuan-turbo-vision、hunyuan-standard-vision、hunyuan-lite-vision、hunyuan-turbos-20250226、hunyuan-turbos-latest、hunyuan-t1-20250321、hunyuan-t1-latest、hunyuan-turbos-role-plus。各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。注意：不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Messages(self):
        """聊天上下文信息。
说明：
1. 长度最多为 40，按对话时间从旧到新在数组中排列。
2. Message.Role 可选值：system、user、assistant、 tool（functioncall场景）。
其中，system 角色可选，如存在则必须位于列表的最开始。user（tool） 和 assistant 需交替出现（一问一答），以 user 提问开始，user（tool）提问结束，其中tool可以连续出现多次，且 Content 不能为空。Role 的顺序示例：[system（可选） user assistant user（tool tool ...） assistant user（tool tool ...） ...]。
3. Messages 中 Content 总长度不能超过模型输入长度上限（可参考 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 文档），超过则会截断最前面的内容，只保留尾部内容。
        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Stream(self):
        """流式调用开关。
说明：
1. 未传值时默认为非流式调用（false）。
2. 流式调用时以 SSE 协议增量返回结果（返回值取 Choices[n].Delta 中的值，需要拼接增量数据才能获得完整结果）。
3. 非流式调用时：
调用方式与普通 HTTP 请求无异。
接口响应耗时较长，**如需更低时延建议设置为 true**。
只返回一次最终结果（返回值取 Choices[n].Message 中的值）。

注意：
通过 SDK 调用时，流式和非流式调用需用**不同的方式**获取返回值，具体参考 SDK 中的注释或示例（在各语言 SDK 代码仓库的 examples/hunyuan/v20230901/ 目录中）。
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def StreamModeration(self):
        """流式输出审核开关。
说明：
1. 当使用流式输出（Stream 字段值为 true）时，该字段生效。
2. 输出审核有流式和同步两种模式，**流式模式首包响应更快**。未传值时默认为流式模式（true）。
3. 如果值为 true，将对输出内容进行分段审核，审核通过的内容流式输出返回。如果出现审核不过，响应中的 FinishReason 值为 sensitive。
4. 如果值为 false，则不使用流式输出审核，需要审核完所有输出内容后再返回结果。

注意：
当选择流式输出审核时，可能会出现部分内容已输出，但中间某一段响应中的 FinishReason 值为 sensitive，此时说明安全审核未通过。如果业务场景有实时文字上屏的需求，需要自行撤回已上屏的内容，并建议自定义替换为一条提示语，如 “这个问题我不方便回答，不如我们换个话题试试”，以保障终端体验。
        :rtype: bool
        """
        return self._StreamModeration

    @StreamModeration.setter
    def StreamModeration(self, StreamModeration):
        self._StreamModeration = StreamModeration

    @property
    def TopP(self):
        """说明：
1. 影响输出文本的多样性。模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。
2. 取值区间为 [0.0, 1.0]。取值越大，生成文本的多样性越强。
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Temperature(self):
        """说明：
1. 影响模型输出多样性，模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。
2. 取值区间为 [0.0, 2.0]。较高的数值会使输出更加多样化和不可预测，而较低的数值会使其更加集中和确定。
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def EnableEnhancement(self):
        """功能增强（如搜索）开关。
说明：
1. hunyuan-lite 无功能增强（如搜索）能力，该参数对 hunyuan-lite 版本不生效。
2. 未传值时默认打开开关。
3. 关闭时将直接由主模型生成回复内容，可以降低响应时延（对于流式输出时的首字时延尤为明显）。但在少数场景里，回复效果可能会下降。
4. 安全审核能力不属于功能增强范围，不受此字段影响。
5. 2025-04-20 00:00:00起，由默认开启状态转为默认关闭状态。
        :rtype: bool
        """
        return self._EnableEnhancement

    @EnableEnhancement.setter
    def EnableEnhancement(self, EnableEnhancement):
        self._EnableEnhancement = EnableEnhancement

    @property
    def Tools(self):
        """可调用的工具列表，仅对 hunyuan-turbo、hunyuan-functioncall 模型生效。
        :rtype: list of Tool
        """
        return self._Tools

    @Tools.setter
    def Tools(self, Tools):
        self._Tools = Tools

    @property
    def ToolChoice(self):
        """工具使用选项，可选值包括 none、auto、custom。说明：1. 仅对 hunyuan-turbo、hunyuan-functioncall 模型生效。2. none：不调用工具；auto：模型自行选择生成回复或调用工具；custom：强制模型调用指定的工具。3. 未设置时，默认值为auto
        :rtype: str
        """
        return self._ToolChoice

    @ToolChoice.setter
    def ToolChoice(self, ToolChoice):
        self._ToolChoice = ToolChoice

    @property
    def CustomTool(self):
        """强制模型调用指定的工具，当参数ToolChoice为custom时，此参数为必填
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Tool`
        """
        return self._CustomTool

    @CustomTool.setter
    def CustomTool(self, CustomTool):
        self._CustomTool = CustomTool

    @property
    def SearchInfo(self):
        """默认是false，在值为true且命中搜索时，接口会返回SearchInfo
        :rtype: bool
        """
        return self._SearchInfo

    @SearchInfo.setter
    def SearchInfo(self, SearchInfo):
        self._SearchInfo = SearchInfo

    @property
    def Citation(self):
        """搜索引文角标开关。
说明：
1. 配合EnableEnhancement和SearchInfo参数使用。打开后，回答中命中搜索的结果会在片段后增加角标标志，对应SearchInfo列表中的链接。
2. false：开关关闭，true：开关打开。
3. 未传值时默认开关关闭（false）。
        :rtype: bool
        """
        return self._Citation

    @Citation.setter
    def Citation(self, Citation):
        self._Citation = Citation

    @property
    def EnableSpeedSearch(self):
        """是否开启极速版搜索，默认false，不开启；在开启且命中搜索时，会启用极速版搜索，流式输出首字返回更快。
        :rtype: bool
        """
        return self._EnableSpeedSearch

    @EnableSpeedSearch.setter
    def EnableSpeedSearch(self, EnableSpeedSearch):
        self._EnableSpeedSearch = EnableSpeedSearch

    @property
    def EnableMultimedia(self):
        """多媒体开关。
详细介绍请阅读 [多媒体介绍](https://cloud.tencent.com/document/product/1729/111178) 中的说明。
说明：
1. 该参数目前仅对白名单内用户生效，如您想体验该功能请 [联系我们](https://cloud.tencent.com/act/event/Online_service)。
2. 该参数仅在功能增强（如搜索）开关开启（EnableEnhancement=true）并且极速版搜索开关关闭（EnableSpeedSearch=false）时生效。
3. hunyuan-lite 无多媒体能力，该参数对 hunyuan-lite 版本不生效。
4. 未传值时默认关闭。
5. 开启并搜索到对应的多媒体信息时，会输出对应的多媒体地址，可以定制个性化的图文消息。
        :rtype: bool
        """
        return self._EnableMultimedia

    @EnableMultimedia.setter
    def EnableMultimedia(self, EnableMultimedia):
        self._EnableMultimedia = EnableMultimedia

    @property
    def EnableDeepSearch(self):
        """是否开启深度研究该问题，默认是false，在值为true且命中深度研究该问题时，会返回深度研究该问题信息。
        :rtype: bool
        """
        return self._EnableDeepSearch

    @EnableDeepSearch.setter
    def EnableDeepSearch(self, EnableDeepSearch):
        self._EnableDeepSearch = EnableDeepSearch

    @property
    def Seed(self):
        """说明： 1. 确保模型的输出是可复现的。 2. 取值区间为非0正整数，最大值10000。 3. 非必要不建议使用，不合理的取值会影响效果。
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def ForceSearchEnhancement(self):
        """强制搜索增强开关。
说明：
1. 未传值时默认关闭。
2. 开启后，将强制走AI搜索，当AI搜索结果为空时，由大模型回复兜底话术。
        :rtype: bool
        """
        return self._ForceSearchEnhancement

    @ForceSearchEnhancement.setter
    def ForceSearchEnhancement(self, ForceSearchEnhancement):
        self._ForceSearchEnhancement = ForceSearchEnhancement

    @property
    def Stop(self):
        """自定义结束生成字符串

调用 OpenAI 的接口时，如果您指定了 `stop` 参数, 模型会停止在匹配到 `stop` 的内容之前。
在调用混元接口时，会停止在匹配到 `stop` 的内容之后。

**说明：**
未来我们可能会修改此行为以便和 OpenAI 保持一致。
但是目前有使用该参数的情况下，开发者需要注意该参数是否会对应用造成影响，以及未来该行为调整时带来的影响。
        :rtype: list of str
        """
        return self._Stop

    @Stop.setter
    def Stop(self, Stop):
        self._Stop = Stop

    @property
    def EnableRecommendedQuestions(self):
        """推荐问答开关。
说明：
1. 未传值时默认关闭。
2. 开启后，在返回值的最后一个包中会增加 RecommendedQuestions 字段表示推荐问答， 最多返回3条。
        :rtype: bool
        """
        return self._EnableRecommendedQuestions

    @EnableRecommendedQuestions.setter
    def EnableRecommendedQuestions(self, EnableRecommendedQuestions):
        self._EnableRecommendedQuestions = EnableRecommendedQuestions

    @property
    def EnableDeepRead(self):
        """是否开启深度阅读，默认是false，在值为true时，会返回深度阅读的结果信息。说明:1.深度阅读需要开启插件增强,即设置EnableEnhancement为true,当设置EnableDeepRead为true时EnableEnhancement默认为true；2.目前暂时只支持单文档单轮的深度阅读；3.深度阅读功能的文件上传可以使用FilesUploads接口，具体参数详见FilesUploads接口文档
        :rtype: bool
        """
        return self._EnableDeepRead

    @EnableDeepRead.setter
    def EnableDeepRead(self, EnableDeepRead):
        self._EnableDeepRead = EnableDeepRead


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Stream = params.get("Stream")
        self._StreamModeration = params.get("StreamModeration")
        self._TopP = params.get("TopP")
        self._Temperature = params.get("Temperature")
        self._EnableEnhancement = params.get("EnableEnhancement")
        if params.get("Tools") is not None:
            self._Tools = []
            for item in params.get("Tools"):
                obj = Tool()
                obj._deserialize(item)
                self._Tools.append(obj)
        self._ToolChoice = params.get("ToolChoice")
        if params.get("CustomTool") is not None:
            self._CustomTool = Tool()
            self._CustomTool._deserialize(params.get("CustomTool"))
        self._SearchInfo = params.get("SearchInfo")
        self._Citation = params.get("Citation")
        self._EnableSpeedSearch = params.get("EnableSpeedSearch")
        self._EnableMultimedia = params.get("EnableMultimedia")
        self._EnableDeepSearch = params.get("EnableDeepSearch")
        self._Seed = params.get("Seed")
        self._ForceSearchEnhancement = params.get("ForceSearchEnhancement")
        self._Stop = params.get("Stop")
        self._EnableRecommendedQuestions = params.get("EnableRecommendedQuestions")
        self._EnableDeepRead = params.get("EnableDeepRead")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionsResponse(AbstractModel):
    """ChatCompletions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Created: Unix 时间戳，单位为秒。
        :type Created: int
        :param _Usage: Token 统计信息。
按照总 Token 数量计费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        :param _Note: 免责声明。
        :type Note: str
        :param _Id: 本次请求的 RequestId。
        :type Id: str
        :param _Choices: 回复内容。
        :type Choices: list of Choice
        :param _ErrorMsg: 错误信息。
如果流式返回中服务处理异常，返回该错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        :param _ModerationLevel: 多轮会话风险审核，值为1时，表明存在信息安全风险，建议终止客户多轮会话。
        :type ModerationLevel: str
        :param _SearchInfo: 搜索结果信息
        :type SearchInfo: :class:`tencentcloud.hunyuan.v20230901.models.SearchInfo`
        :param _Replaces: 多媒体信息。
说明：
1. 可以用多媒体信息替换回复内容里的占位符，得到完整的消息。
2. 可能会出现回复内容里存在占位符，但是因为审核等原因没有返回多媒体信息。
        :type Replaces: list of Replace
        :param _RecommendedQuestions: 推荐问答。
        :type RecommendedQuestions: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Created = None
        self._Usage = None
        self._Note = None
        self._Id = None
        self._Choices = None
        self._ErrorMsg = None
        self._ModerationLevel = None
        self._SearchInfo = None
        self._Replaces = None
        self._RecommendedQuestions = None
        self._RequestId = None

    @property
    def Created(self):
        """Unix 时间戳，单位为秒。
        :rtype: int
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        """Token 统计信息。
按照总 Token 数量计费。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Note(self):
        """免责声明。
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Id(self):
        """本次请求的 RequestId。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        """回复内容。
        :rtype: list of Choice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def ErrorMsg(self):
        """错误信息。
如果流式返回中服务处理异常，返回该错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ModerationLevel(self):
        warnings.warn("parameter `ModerationLevel` is deprecated", DeprecationWarning) 

        """多轮会话风险审核，值为1时，表明存在信息安全风险，建议终止客户多轮会话。
        :rtype: str
        """
        return self._ModerationLevel

    @ModerationLevel.setter
    def ModerationLevel(self, ModerationLevel):
        warnings.warn("parameter `ModerationLevel` is deprecated", DeprecationWarning) 

        self._ModerationLevel = ModerationLevel

    @property
    def SearchInfo(self):
        """搜索结果信息
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SearchInfo`
        """
        return self._SearchInfo

    @SearchInfo.setter
    def SearchInfo(self, SearchInfo):
        self._SearchInfo = SearchInfo

    @property
    def Replaces(self):
        """多媒体信息。
说明：
1. 可以用多媒体信息替换回复内容里的占位符，得到完整的消息。
2. 可能会出现回复内容里存在占位符，但是因为审核等原因没有返回多媒体信息。
        :rtype: list of Replace
        """
        return self._Replaces

    @Replaces.setter
    def Replaces(self, Replaces):
        self._Replaces = Replaces

    @property
    def RecommendedQuestions(self):
        """推荐问答。
        :rtype: list of str
        """
        return self._RecommendedQuestions

    @RecommendedQuestions.setter
    def RecommendedQuestions(self, RecommendedQuestions):
        self._RecommendedQuestions = RecommendedQuestions

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._Note = params.get("Note")
        self._Id = params.get("Id")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        if params.get("ErrorMsg") is not None:
            self._ErrorMsg = ErrorMsg()
            self._ErrorMsg._deserialize(params.get("ErrorMsg"))
        self._ModerationLevel = params.get("ModerationLevel")
        if params.get("SearchInfo") is not None:
            self._SearchInfo = SearchInfo()
            self._SearchInfo._deserialize(params.get("SearchInfo"))
        if params.get("Replaces") is not None:
            self._Replaces = []
            for item in params.get("Replaces"):
                obj = Replace()
                obj._deserialize(item)
                self._Replaces.append(obj)
        self._RecommendedQuestions = params.get("RecommendedQuestions")
        self._RequestId = params.get("RequestId")


class ChatTranslationsRequest(AbstractModel):
    """ChatTranslations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型名称，可选值包括 hunyuan-translation、hunyuan-translation-lite。
各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。

注意：
不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :type Model: str
        :param _Stream: 流式调用开关。
说明：
1. 未传值时默认为非流式调用（false）。
2. 流式调用时以 SSE 协议增量返回结果（返回值取 Choices[n].Delta 中的值，需要拼接增量数据才能获得完整结果）。
3. 非流式调用时：
调用方式与普通 HTTP 请求无异。
接口响应耗时较长，**如需更低时延建议设置为 true**。
只返回一次最终结果（返回值取 Choices[n].Message 中的值）。

注意：
通过 SDK 调用时，流式和非流式调用需用**不同的方式**获取返回值，具体参考 SDK 中的注释或示例（在各语言 SDK 代码仓库的 examples/hunyuan/v20230901/ 目录中）。
        :type Stream: bool
        :param _Text: 待翻译的文本
        :type Text: str
        :param _Source: 源语言。
支持语言列表: 1. 简体中文：zh，2. 粤语：yue，3. 英语：en，4. 法语：fr，5. 葡萄牙语：pt，6. 西班牙语：es，7. 日语：ja，8. 土耳其语：tr，9. 俄语：ru，10. 阿拉伯语：ar，11. 韩语：ko，12. 泰语：th，13. 意大利语：it，14. 德语：de，15. 越南语：vi，16. 马来语：ms，17. 印尼语：id
        :type Source: str
        :param _Target: 目标语言。
支持语言列表: 1. 简体中文：zh，2. 粤语：yue，3. 英语：en，4. 法语：fr，5. 葡萄牙语：pt，6. 西班牙语：es，7. 日语：ja，8. 土耳其语：tr，9. 俄语：ru，10. 阿拉伯语：ar，11. 韩语：ko，12. 泰语：th，13. 意大利语：it，14. 德语：de，15. 越南语：vi，16. 马来语：ms，17. 印尼语：id
        :type Target: str
        :param _Field: 待翻译文本所属领域，例如游戏剧情等
        :type Field: str
        :param _References: 参考示例，最多10个
        :type References: list of Reference
        """
        self._Model = None
        self._Stream = None
        self._Text = None
        self._Source = None
        self._Target = None
        self._Field = None
        self._References = None

    @property
    def Model(self):
        """模型名称，可选值包括 hunyuan-translation、hunyuan-translation-lite。
各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。

注意：
不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Stream(self):
        """流式调用开关。
说明：
1. 未传值时默认为非流式调用（false）。
2. 流式调用时以 SSE 协议增量返回结果（返回值取 Choices[n].Delta 中的值，需要拼接增量数据才能获得完整结果）。
3. 非流式调用时：
调用方式与普通 HTTP 请求无异。
接口响应耗时较长，**如需更低时延建议设置为 true**。
只返回一次最终结果（返回值取 Choices[n].Message 中的值）。

注意：
通过 SDK 调用时，流式和非流式调用需用**不同的方式**获取返回值，具体参考 SDK 中的注释或示例（在各语言 SDK 代码仓库的 examples/hunyuan/v20230901/ 目录中）。
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def Text(self):
        """待翻译的文本
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Source(self):
        """源语言。
支持语言列表: 1. 简体中文：zh，2. 粤语：yue，3. 英语：en，4. 法语：fr，5. 葡萄牙语：pt，6. 西班牙语：es，7. 日语：ja，8. 土耳其语：tr，9. 俄语：ru，10. 阿拉伯语：ar，11. 韩语：ko，12. 泰语：th，13. 意大利语：it，14. 德语：de，15. 越南语：vi，16. 马来语：ms，17. 印尼语：id
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        """目标语言。
支持语言列表: 1. 简体中文：zh，2. 粤语：yue，3. 英语：en，4. 法语：fr，5. 葡萄牙语：pt，6. 西班牙语：es，7. 日语：ja，8. 土耳其语：tr，9. 俄语：ru，10. 阿拉伯语：ar，11. 韩语：ko，12. 泰语：th，13. 意大利语：it，14. 德语：de，15. 越南语：vi，16. 马来语：ms，17. 印尼语：id
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Field(self):
        """待翻译文本所属领域，例如游戏剧情等
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def References(self):
        """参考示例，最多10个
        :rtype: list of Reference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Stream = params.get("Stream")
        self._Text = params.get("Text")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._Field = params.get("Field")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = Reference()
                obj._deserialize(item)
                self._References.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatTranslationsResponse(AbstractModel):
    """ChatTranslations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 本次请求的 RequestId。
        :type Id: str
        :param _Note: 免责声明。
        :type Note: str
        :param _Created: Unix 时间戳，单位为秒。
        :type Created: int
        :param _Usage: Token 统计信息。
按照总 Token 数量计费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        :param _Choices: 回复内容。
        :type Choices: list of TranslationChoice
        :param _ErrorMsg: 错误信息。
如果流式返回中服务处理异常，返回该错误信息。
        :type ErrorMsg: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Id = None
        self._Note = None
        self._Created = None
        self._Usage = None
        self._Choices = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Id(self):
        """本次请求的 RequestId。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Note(self):
        """免责声明。
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Created(self):
        """Unix 时间戳，单位为秒。
        :rtype: int
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        """Token 统计信息。
按照总 Token 数量计费。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Choices(self):
        """回复内容。
        :rtype: list of TranslationChoice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def ErrorMsg(self):
        """错误信息。
如果流式返回中服务处理异常，返回该错误信息。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Note = params.get("Note")
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = TranslationChoice()
                obj._deserialize(item)
                self._Choices.append(obj)
        if params.get("ErrorMsg") is not None:
            self._ErrorMsg = ErrorMsg()
            self._ErrorMsg._deserialize(params.get("ErrorMsg"))
        self._RequestId = params.get("RequestId")


class Choice(AbstractModel):
    """返回的回复, 支持多个

    """

    def __init__(self):
        r"""
        :param _FinishReason: 结束标志位，可能为 stop、 sensitive或者tool_calls。
stop 表示输出正常结束。
sensitive 只在开启流式输出审核时会出现，表示安全审核未通过。
tool_calls 标识函数调用。
        :type FinishReason: str
        :param _Delta: 增量返回值，流式调用时使用该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Delta: :class:`tencentcloud.hunyuan.v20230901.models.Delta`
        :param _Message: 返回值，非流式调用时使用该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: :class:`tencentcloud.hunyuan.v20230901.models.Message`
        :param _Index: 索引值，流式调用时使用该字段。
        :type Index: int
        :param _ModerationLevel: 多轮会话风险审核，值为1时，表明存在信息安全风险，建议终止客户多轮会话。
        :type ModerationLevel: str
        """
        self._FinishReason = None
        self._Delta = None
        self._Message = None
        self._Index = None
        self._ModerationLevel = None

    @property
    def FinishReason(self):
        """结束标志位，可能为 stop、 sensitive或者tool_calls。
stop 表示输出正常结束。
sensitive 只在开启流式输出审核时会出现，表示安全审核未通过。
tool_calls 标识函数调用。
        :rtype: str
        """
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def Delta(self):
        """增量返回值，流式调用时使用该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Delta`
        """
        return self._Delta

    @Delta.setter
    def Delta(self, Delta):
        self._Delta = Delta

    @property
    def Message(self):
        """返回值，非流式调用时使用该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Message`
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Index(self):
        """索引值，流式调用时使用该字段。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def ModerationLevel(self):
        """多轮会话风险审核，值为1时，表明存在信息安全风险，建议终止客户多轮会话。
        :rtype: str
        """
        return self._ModerationLevel

    @ModerationLevel.setter
    def ModerationLevel(self, ModerationLevel):
        self._ModerationLevel = ModerationLevel


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        if params.get("Delta") is not None:
            self._Delta = Delta()
            self._Delta._deserialize(params.get("Delta"))
        if params.get("Message") is not None:
            self._Message = Message()
            self._Message._deserialize(params.get("Message"))
        self._Index = params.get("Index")
        self._ModerationLevel = params.get("ModerationLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Content(AbstractModel):
    """可以传入多种类型的内容，如图片或文本。

    """

    def __init__(self):
        r"""
        :param _Type: 内容类型
注意：
需包含至少一个 Type 为"text"的参数及至少一个 Type 为"image_url"的参数。
参数值可选范围：[text", "image_url"]
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Text: 当 Type 为 text 时使用，表示具体的文本内容。当 Type 为 image_url 时，当前字段内容需保持为空，传递内容不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _ImageUrl: 图片的url，当 Type 为 image_url 时使用，表示具体的图片内容
如"https://example.com/1.png" 或 图片的base64（注意 "data:image/jpeg;base64," 为必要部分）："data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAA......"。当 Type 为 text 时，当前字段内容需保持为空，传递内容不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: :class:`tencentcloud.hunyuan.v20230901.models.ImageUrl`
        """
        self._Type = None
        self._Text = None
        self._ImageUrl = None

    @property
    def Type(self):
        """内容类型
注意：
需包含至少一个 Type 为"text"的参数及至少一个 Type 为"image_url"的参数。
参数值可选范围：[text", "image_url"]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Text(self):
        """当 Type 为 text 时使用，表示具体的文本内容。当 Type 为 image_url 时，当前字段内容需保持为空，传递内容不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def ImageUrl(self):
        """图片的url，当 Type 为 image_url 时使用，表示具体的图片内容
如"https://example.com/1.png" 或 图片的base64（注意 "data:image/jpeg;base64," 为必要部分）："data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAA......"。当 Type 为 text 时，当前字段内容需保持为空，传递内容不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ImageUrl`
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Text = params.get("Text")
        if params.get("ImageUrl") is not None:
            self._ImageUrl = ImageUrl()
            self._ImageUrl._deserialize(params.get("ImageUrl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateThreadRequest(AbstractModel):
    """CreateThread请求参数结构体

    """


class CreateThreadResponse(AbstractModel):
    """CreateThread返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 会话 ID
        :type ID: str
        :param _Object: 对象类型
        :type Object: str
        :param _CreatedAt: 创建时间，Unix 时间戳，单位为秒。
        :type CreatedAt: int
        :param _ToolResources: 提供给工具的资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolResources: :class:`tencentcloud.hunyuan.v20230901.models.ThreadToolResources`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._ID = None
        self._Object = None
        self._CreatedAt = None
        self._ToolResources = None
        self._RequestId = None

    @property
    def ID(self):
        """会话 ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Object(self):
        """对象类型
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def CreatedAt(self):
        """创建时间，Unix 时间戳，单位为秒。
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ToolResources(self):
        """提供给工具的资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ThreadToolResources`
        """
        return self._ToolResources

    @ToolResources.setter
    def ToolResources(self, ToolResources):
        self._ToolResources = ToolResources

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Object = params.get("Object")
        self._CreatedAt = params.get("CreatedAt")
        if params.get("ToolResources") is not None:
            self._ToolResources = ThreadToolResources()
            self._ToolResources._deserialize(params.get("ToolResources"))
        self._RequestId = params.get("RequestId")


class Delta(AbstractModel):
    """返回的内容（流式返回）

    """

    def __init__(self):
        r"""
        :param _Role: 角色名称。
        :type Role: str
        :param _Content: 内容详情。
        :type Content: str
        :param _ToolCalls: 模型生成的工具调用，仅 hunyuan-functioncall 模型支持
说明：
对于每一次的输出值应该以Id为标识对Type、Name、Arguments字段进行合并。

注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCalls: list of ToolCall
        """
        self._Role = None
        self._Content = None
        self._ToolCalls = None

    @property
    def Role(self):
        """角色名称。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """内容详情。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ToolCalls(self):
        """模型生成的工具调用，仅 hunyuan-functioncall 模型支持
说明：
对于每一次的输出值应该以Id为标识对Type、Name、Arguments字段进行合并。

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ToolCall
        """
        return self._ToolCalls

    @ToolCalls.setter
    def ToolCalls(self, ToolCalls):
        self._ToolCalls = ToolCalls


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        if params.get("ToolCalls") is not None:
            self._ToolCalls = []
            for item in params.get("ToolCalls"):
                obj = ToolCall()
                obj._deserialize(item)
                self._ToolCalls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingData(AbstractModel):
    """Embedding 信息。

    """

    def __init__(self):
        r"""
        :param _Embedding: Embedding 信息，目前为 1024 维浮点数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Embedding: list of float
        :param _Index: 下标，目前不支持批量，因此固定为 0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Object: 目前固定为 "embedding"。
注意：此字段可能返回 null，表示取不到有效值。
        :type Object: str
        """
        self._Embedding = None
        self._Index = None
        self._Object = None

    @property
    def Embedding(self):
        """Embedding 信息，目前为 1024 维浮点数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of float
        """
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding

    @property
    def Index(self):
        """下标，目前不支持批量，因此固定为 0。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Object(self):
        """目前固定为 "embedding"。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object


    def _deserialize(self, params):
        self._Embedding = params.get("Embedding")
        self._Index = params.get("Index")
        self._Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingUsage(AbstractModel):
    """Token 使用计数。

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入 Token 数。
        :type PromptTokens: int
        :param _TotalTokens: 总 Token 数。
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        """输入 Token 数。
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def TotalTokens(self):
        """总 Token 数。
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PromptTokens = params.get("PromptTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorMsg(AbstractModel):
    """运行时异常信息。

    """

    def __init__(self):
        r"""
        :param _Msg: 错误提示信息。
        :type Msg: str
        :param _Code: 错误码。
4000 服务内部异常。
4001 请求模型超时。

        :type Code: int
        """
        self._Msg = None
        self._Code = None

    @property
    def Msg(self):
        """错误提示信息。
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        """错误码。
4000 服务内部异常。
4001 请求模型超时。

        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class File3D(AbstractModel):
    """3D文件

    """

    def __init__(self):
        r"""
        :param _Type: 3D文件的格式。取值范围：GIF, OBJ
        :type Type: str
        :param _Url: 文件的Url
        :type Url: str
        """
        self._Type = None
        self._Url = None

    @property
    def Type(self):
        """3D文件的格式。取值范围：GIF, OBJ
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        """文件的Url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class File3Ds(AbstractModel):
    """3D文件列表

    """

    def __init__(self):
        r"""
        :param _File3D: 3D文件列表
        :type File3D: list of File3D
        """
        self._File3D = None

    @property
    def File3D(self):
        """3D文件列表
        :rtype: list of File3D
        """
        return self._File3D

    @File3D.setter
    def File3D(self, File3D):
        self._File3D = File3D


    def _deserialize(self, params):
        if params.get("File3D") is not None:
            self._File3D = []
            for item in params.get("File3D"):
                obj = File3D()
                obj._deserialize(item)
                self._File3D.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileObject(AbstractModel):
    """已上传的文件对象。

    """

    def __init__(self):
        r"""
        :param _ID: 文件标识符，可在各个API中引用。
        :type ID: str
        :param _Object: 对象类型，始终为 file。
        :type Object: str
        :param _Bytes: 文件大小，单位为字节。
        :type Bytes: int
        :param _CreatedAt: 文件创建时的 Unix 时间戳（秒）。
        :type CreatedAt: int
        :param _Filename: 文件名。
        :type Filename: str
        :param _Purpose: 上传文件的用途。
        :type Purpose: str
        """
        self._ID = None
        self._Object = None
        self._Bytes = None
        self._CreatedAt = None
        self._Filename = None
        self._Purpose = None

    @property
    def ID(self):
        """文件标识符，可在各个API中引用。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Object(self):
        """对象类型，始终为 file。
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def Bytes(self):
        """文件大小，单位为字节。
        :rtype: int
        """
        return self._Bytes

    @Bytes.setter
    def Bytes(self, Bytes):
        self._Bytes = Bytes

    @property
    def CreatedAt(self):
        """文件创建时的 Unix 时间戳（秒）。
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Filename(self):
        """文件名。
        :rtype: str
        """
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def Purpose(self):
        """上传文件的用途。
        :rtype: str
        """
        return self._Purpose

    @Purpose.setter
    def Purpose(self, Purpose):
        self._Purpose = Purpose


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Object = params.get("Object")
        self._Bytes = params.get("Bytes")
        self._CreatedAt = params.get("CreatedAt")
        self._Filename = params.get("Filename")
        self._Purpose = params.get("Purpose")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilesDeletionsRequest(AbstractModel):
    """FilesDeletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 文件标识符。
        :type ID: str
        """
        self._ID = None

    @property
    def ID(self):
        """文件标识符。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilesDeletionsResponse(AbstractModel):
    """FilesDeletions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 文件标识符。
        :type ID: str
        :param _Object: 对象类型，始终为 file。
        :type Object: str
        :param _Deleted: 是否删除成功。
        :type Deleted: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._ID = None
        self._Object = None
        self._Deleted = None
        self._RequestId = None

    @property
    def ID(self):
        """文件标识符。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Object(self):
        """对象类型，始终为 file。
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def Deleted(self):
        """是否删除成功。
        :rtype: bool
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Object = params.get("Object")
        self._Deleted = params.get("Deleted")
        self._RequestId = params.get("RequestId")


class FilesListRequest(AbstractModel):
    """FilesList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _Limit: 每页数量，最大 100。
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """分页偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页数量，最大 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilesListResponse(AbstractModel):
    """FilesList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文件数量。
        :type Total: int
        :param _Object: 对象类型，始终为 list。
        :type Object: str
        :param _Data: FileObject 列表。
        :type Data: list of FileObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Total = None
        self._Object = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """文件数量。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Object(self):
        """对象类型，始终为 list。
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def Data(self):
        """FileObject 列表。
        :rtype: list of FileObject
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Object = params.get("Object")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = FileObject()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class FilesUploadsRequest(AbstractModel):
    """FilesUploads请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 文件名。
        :type Name: str
        :param _URL: 文件链接。目前支持 csv, doc, docx, pdf, ppt, pptx, txt, xls, xlsx 格式，单文件大小限制为100M。
        :type URL: str
        """
        self._Name = None
        self._URL = None

    @property
    def Name(self):
        """文件名。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def URL(self):
        """文件链接。目前支持 csv, doc, docx, pdf, ppt, pptx, txt, xls, xlsx 格式，单文件大小限制为100M。
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._URL = params.get("URL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilesUploadsResponse(AbstractModel):
    """FilesUploads返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 文件标识符，可在各个API中引用。
        :type ID: str
        :param _Object: 对象类型，始终为 file。
        :type Object: str
        :param _Bytes: 文件大小，单位为字节。
        :type Bytes: int
        :param _CreatedAt: 文件创建时的 Unix 时间戳（秒）。
        :type CreatedAt: int
        :param _Filename: 文件名。
        :type Filename: str
        :param _Purpose: 上传文件的用途。
        :type Purpose: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._ID = None
        self._Object = None
        self._Bytes = None
        self._CreatedAt = None
        self._Filename = None
        self._Purpose = None
        self._RequestId = None

    @property
    def ID(self):
        """文件标识符，可在各个API中引用。
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Object(self):
        """对象类型，始终为 file。
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def Bytes(self):
        """文件大小，单位为字节。
        :rtype: int
        """
        return self._Bytes

    @Bytes.setter
    def Bytes(self, Bytes):
        self._Bytes = Bytes

    @property
    def CreatedAt(self):
        """文件创建时的 Unix 时间戳（秒）。
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Filename(self):
        """文件名。
        :rtype: str
        """
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def Purpose(self):
        """上传文件的用途。
        :rtype: str
        """
        return self._Purpose

    @Purpose.setter
    def Purpose(self, Purpose):
        self._Purpose = Purpose

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Object = params.get("Object")
        self._Bytes = params.get("Bytes")
        self._CreatedAt = params.get("CreatedAt")
        self._Filename = params.get("Filename")
        self._Purpose = params.get("Purpose")
        self._RequestId = params.get("RequestId")


class GetEmbeddingRequest(AbstractModel):
    """GetEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Input: 输入文本。总长度不超过 1024 个 Token，超过则会截断最后面的内容。
        :type Input: str
        :param _InputList: 输入文本数组。输入数组总长度不超过 50 。
        :type InputList: list of str
        """
        self._Input = None
        self._InputList = None

    @property
    def Input(self):
        """输入文本。总长度不超过 1024 个 Token，超过则会截断最后面的内容。
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def InputList(self):
        """输入文本数组。输入数组总长度不超过 50 。
        :rtype: list of str
        """
        return self._InputList

    @InputList.setter
    def InputList(self, InputList):
        self._InputList = InputList


    def _deserialize(self, params):
        self._Input = params.get("Input")
        self._InputList = params.get("InputList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmbeddingResponse(AbstractModel):
    """GetEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回的 Embedding 信息。
        :type Data: list of EmbeddingData
        :param _Usage: Token 使用计数，按照总 Token 数量收费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.EmbeddingUsage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        """返回的 Embedding 信息。
        :rtype: list of EmbeddingData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        """Token 使用计数，按照总 Token 数量收费。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.EmbeddingUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EmbeddingData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = EmbeddingUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetThreadMessageListRequest(AbstractModel):
    """GetThreadMessageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ThreadID: 会话 ID
        :type ThreadID: str
        :param _Limit: 返回的消息条数，1 - 100 条
        :type Limit: int
        :param _Order: 排序方式，按创建时间升序（asc）或降序（desc），默认为 desc
        :type Order: str
        """
        self._ThreadID = None
        self._Limit = None
        self._Order = None

    @property
    def ThreadID(self):
        """会话 ID
        :rtype: str
        """
        return self._ThreadID

    @ThreadID.setter
    def ThreadID(self, ThreadID):
        self._ThreadID = ThreadID

    @property
    def Limit(self):
        """返回的消息条数，1 - 100 条
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        """排序方式，按创建时间升序（asc）或降序（desc），默认为 desc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._ThreadID = params.get("ThreadID")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetThreadMessageListResponse(AbstractModel):
    """GetThreadMessageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 消息列表
        :type Data: list of ThreadMessage
        :param _FirstID: 第一条消息 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstID: str
        :param _LastID: 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type LastID: int
        :param _HasMore: 是否还有更多消息
        :type HasMore: bool
        :param _Object: 对象类型
        :type Object: str
        :param _FirstMsgID: 第一条消息 ID
        :type FirstMsgID: str
        :param _LastMsgID: 最后一条消息 ID
        :type LastMsgID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Data = None
        self._FirstID = None
        self._LastID = None
        self._HasMore = None
        self._Object = None
        self._FirstMsgID = None
        self._LastMsgID = None
        self._RequestId = None

    @property
    def Data(self):
        """消息列表
        :rtype: list of ThreadMessage
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def FirstID(self):
        warnings.warn("parameter `FirstID` is deprecated", DeprecationWarning) 

        """第一条消息 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FirstID

    @FirstID.setter
    def FirstID(self, FirstID):
        warnings.warn("parameter `FirstID` is deprecated", DeprecationWarning) 

        self._FirstID = FirstID

    @property
    def LastID(self):
        warnings.warn("parameter `LastID` is deprecated", DeprecationWarning) 

        """已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastID

    @LastID.setter
    def LastID(self, LastID):
        warnings.warn("parameter `LastID` is deprecated", DeprecationWarning) 

        self._LastID = LastID

    @property
    def HasMore(self):
        """是否还有更多消息
        :rtype: bool
        """
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def Object(self):
        """对象类型
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def FirstMsgID(self):
        """第一条消息 ID
        :rtype: str
        """
        return self._FirstMsgID

    @FirstMsgID.setter
    def FirstMsgID(self, FirstMsgID):
        self._FirstMsgID = FirstMsgID

    @property
    def LastMsgID(self):
        """最后一条消息 ID
        :rtype: str
        """
        return self._LastMsgID

    @LastMsgID.setter
    def LastMsgID(self, LastMsgID):
        self._LastMsgID = LastMsgID

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ThreadMessage()
                obj._deserialize(item)
                self._Data.append(obj)
        self._FirstID = params.get("FirstID")
        self._LastID = params.get("LastID")
        self._HasMore = params.get("HasMore")
        self._Object = params.get("Object")
        self._FirstMsgID = params.get("FirstMsgID")
        self._LastMsgID = params.get("LastMsgID")
        self._RequestId = params.get("RequestId")


class GetThreadMessageRequest(AbstractModel):
    """GetThreadMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ThreadID: 会话 ID
        :type ThreadID: str
        :param _MessageID: 消息 ID
        :type MessageID: str
        """
        self._ThreadID = None
        self._MessageID = None

    @property
    def ThreadID(self):
        """会话 ID
        :rtype: str
        """
        return self._ThreadID

    @ThreadID.setter
    def ThreadID(self, ThreadID):
        self._ThreadID = ThreadID

    @property
    def MessageID(self):
        """消息 ID
        :rtype: str
        """
        return self._MessageID

    @MessageID.setter
    def MessageID(self, MessageID):
        self._MessageID = MessageID


    def _deserialize(self, params):
        self._ThreadID = params.get("ThreadID")
        self._MessageID = params.get("MessageID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetThreadMessageResponse(AbstractModel):
    """GetThreadMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 消息 ID
        :type ID: str
        :param _Object: 对象类型
        :type Object: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: int
        :param _ThreadID: 会话 ID
        :type ThreadID: str
        :param _Status: 状态，处理中 in_progress，已完成 completed，未完成 incomplete。 
        :type Status: str
        :param _InCompleteDetails: 未完成原因
注意：此字段可能返回 null，表示取不到有效值。
        :type InCompleteDetails: :class:`tencentcloud.hunyuan.v20230901.models.ThreadMessageInCompleteDetailsObject`
        :param _CompletedAt: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CompletedAt: int
        :param _InCompleteAt: 未完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InCompleteAt: int
        :param _Role: 角色
        :type Role: str
        :param _Content: 内容
        :type Content: str
        :param _AssistantID: 助手 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AssistantID: str
        :param _RunID: 运行 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RunID: str
        :param _Attachments: 附件
注意：此字段可能返回 null，表示取不到有效值。
        :type Attachments: list of ThreadMessageAttachmentObject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._ID = None
        self._Object = None
        self._CreatedAt = None
        self._ThreadID = None
        self._Status = None
        self._InCompleteDetails = None
        self._CompletedAt = None
        self._InCompleteAt = None
        self._Role = None
        self._Content = None
        self._AssistantID = None
        self._RunID = None
        self._Attachments = None
        self._RequestId = None

    @property
    def ID(self):
        """消息 ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Object(self):
        """对象类型
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def CreatedAt(self):
        """创建时间
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ThreadID(self):
        """会话 ID
        :rtype: str
        """
        return self._ThreadID

    @ThreadID.setter
    def ThreadID(self, ThreadID):
        self._ThreadID = ThreadID

    @property
    def Status(self):
        """状态，处理中 in_progress，已完成 completed，未完成 incomplete。 
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InCompleteDetails(self):
        """未完成原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ThreadMessageInCompleteDetailsObject`
        """
        return self._InCompleteDetails

    @InCompleteDetails.setter
    def InCompleteDetails(self, InCompleteDetails):
        self._InCompleteDetails = InCompleteDetails

    @property
    def CompletedAt(self):
        """完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CompletedAt

    @CompletedAt.setter
    def CompletedAt(self, CompletedAt):
        self._CompletedAt = CompletedAt

    @property
    def InCompleteAt(self):
        """未完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InCompleteAt

    @InCompleteAt.setter
    def InCompleteAt(self, InCompleteAt):
        self._InCompleteAt = InCompleteAt

    @property
    def Role(self):
        """角色
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def AssistantID(self):
        """助手 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssistantID

    @AssistantID.setter
    def AssistantID(self, AssistantID):
        self._AssistantID = AssistantID

    @property
    def RunID(self):
        """运行 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunID

    @RunID.setter
    def RunID(self, RunID):
        self._RunID = RunID

    @property
    def Attachments(self):
        """附件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ThreadMessageAttachmentObject
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Object = params.get("Object")
        self._CreatedAt = params.get("CreatedAt")
        self._ThreadID = params.get("ThreadID")
        self._Status = params.get("Status")
        if params.get("InCompleteDetails") is not None:
            self._InCompleteDetails = ThreadMessageInCompleteDetailsObject()
            self._InCompleteDetails._deserialize(params.get("InCompleteDetails"))
        self._CompletedAt = params.get("CompletedAt")
        self._InCompleteAt = params.get("InCompleteAt")
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._AssistantID = params.get("AssistantID")
        self._RunID = params.get("RunID")
        if params.get("Attachments") is not None:
            self._Attachments = []
            for item in params.get("Attachments"):
                obj = ThreadMessageAttachmentObject()
                obj._deserialize(item)
                self._Attachments.append(obj)
        self._RequestId = params.get("RequestId")


class GetThreadRequest(AbstractModel):
    """GetThread请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ThreadID: 会话 ID
        :type ThreadID: str
        """
        self._ThreadID = None

    @property
    def ThreadID(self):
        """会话 ID
        :rtype: str
        """
        return self._ThreadID

    @ThreadID.setter
    def ThreadID(self, ThreadID):
        self._ThreadID = ThreadID


    def _deserialize(self, params):
        self._ThreadID = params.get("ThreadID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetThreadResponse(AbstractModel):
    """GetThread返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 会话 ID
        :type ID: str
        :param _Object: 对象类型
        :type Object: str
        :param _CreatedAt: 创建时间，Unix 时间戳，单位为秒。
        :type CreatedAt: int
        :param _ToolResources: 提供给工具的资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolResources: :class:`tencentcloud.hunyuan.v20230901.models.ThreadToolResources`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._ID = None
        self._Object = None
        self._CreatedAt = None
        self._ToolResources = None
        self._RequestId = None

    @property
    def ID(self):
        """会话 ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Object(self):
        """对象类型
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def CreatedAt(self):
        """创建时间，Unix 时间戳，单位为秒。
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ToolResources(self):
        """提供给工具的资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ThreadToolResources`
        """
        return self._ToolResources

    @ToolResources.setter
    def ToolResources(self, ToolResources):
        self._ToolResources = ToolResources

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Object = params.get("Object")
        self._CreatedAt = params.get("CreatedAt")
        if params.get("ToolResources") is not None:
            self._ToolResources = ThreadToolResources()
            self._ToolResources._deserialize(params.get("ToolResources"))
        self._RequestId = params.get("RequestId")


class GetTokenCountRequest(AbstractModel):
    """GetTokenCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 输入文本
        :type Prompt: str
        """
        self._Prompt = None

    @property
    def Prompt(self):
        """输入文本
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTokenCountResponse(AbstractModel):
    """GetTokenCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TokenCount: token计数
        :type TokenCount: int
        :param _CharacterCount: 字符计数
        :type CharacterCount: int
        :param _Tokens: 切分后的列表
        :type Tokens: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TokenCount = None
        self._CharacterCount = None
        self._Tokens = None
        self._RequestId = None

    @property
    def TokenCount(self):
        """token计数
        :rtype: int
        """
        return self._TokenCount

    @TokenCount.setter
    def TokenCount(self, TokenCount):
        self._TokenCount = TokenCount

    @property
    def CharacterCount(self):
        """字符计数
        :rtype: int
        """
        return self._CharacterCount

    @CharacterCount.setter
    def CharacterCount(self, CharacterCount):
        self._CharacterCount = CharacterCount

    @property
    def Tokens(self):
        """切分后的列表
        :rtype: list of str
        """
        return self._Tokens

    @Tokens.setter
    def Tokens(self, Tokens):
        self._Tokens = Tokens

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TokenCount = params.get("TokenCount")
        self._CharacterCount = params.get("CharacterCount")
        self._Tokens = params.get("Tokens")
        self._RequestId = params.get("RequestId")


class GroupChatCompletionsRequest(AbstractModel):
    """GroupChatCompletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型名称，可选值包括 hunyuan-large-role-group。各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。注意：不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :type Model: str
        :param _Messages: 聊天上下文信息。
        :type Messages: list of GroupMessage
        :param _Stream: 流式调用开关。
说明：
1. 未传值时默认为非流式调用（false）。
2. 流式调用时以 SSE 协议增量返回结果（返回值取 Choices[n].Delta 中的值，需要拼接增量数据才能获得完整结果）。
3. 非流式调用时：
调用方式与普通 HTTP 请求无异。
接口响应耗时较长，**如需更低时延建议设置为 true**。
只返回一次最终结果（返回值取 Choices[n].Message 中的值）。

注意：
通过 SDK 调用时，流式和非流式调用需用**不同的方式**获取返回值，具体参考 SDK 中的注释或示例（在各语言 SDK 代码仓库的 examples/hunyuan/v20230901/ 目录中）。
        :type Stream: bool
        :param _TargetCharacterName: 目标人物名称
        :type TargetCharacterName: str
        :param _GroupChatConfig: 角色描述
        :type GroupChatConfig: :class:`tencentcloud.hunyuan.v20230901.models.GroupChatConfig`
        :param _UserId: 用户ID
        :type UserId: str
        :param _SessionId: 对话接口
        :type SessionId: str
        """
        self._Model = None
        self._Messages = None
        self._Stream = None
        self._TargetCharacterName = None
        self._GroupChatConfig = None
        self._UserId = None
        self._SessionId = None

    @property
    def Model(self):
        """模型名称，可选值包括 hunyuan-large-role-group。各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。注意：不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Messages(self):
        """聊天上下文信息。
        :rtype: list of GroupMessage
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Stream(self):
        """流式调用开关。
说明：
1. 未传值时默认为非流式调用（false）。
2. 流式调用时以 SSE 协议增量返回结果（返回值取 Choices[n].Delta 中的值，需要拼接增量数据才能获得完整结果）。
3. 非流式调用时：
调用方式与普通 HTTP 请求无异。
接口响应耗时较长，**如需更低时延建议设置为 true**。
只返回一次最终结果（返回值取 Choices[n].Message 中的值）。

注意：
通过 SDK 调用时，流式和非流式调用需用**不同的方式**获取返回值，具体参考 SDK 中的注释或示例（在各语言 SDK 代码仓库的 examples/hunyuan/v20230901/ 目录中）。
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def TargetCharacterName(self):
        """目标人物名称
        :rtype: str
        """
        return self._TargetCharacterName

    @TargetCharacterName.setter
    def TargetCharacterName(self, TargetCharacterName):
        self._TargetCharacterName = TargetCharacterName

    @property
    def GroupChatConfig(self):
        """角色描述
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.GroupChatConfig`
        """
        return self._GroupChatConfig

    @GroupChatConfig.setter
    def GroupChatConfig(self, GroupChatConfig):
        self._GroupChatConfig = GroupChatConfig

    @property
    def UserId(self):
        """用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SessionId(self):
        """对话接口
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = GroupMessage()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Stream = params.get("Stream")
        self._TargetCharacterName = params.get("TargetCharacterName")
        if params.get("GroupChatConfig") is not None:
            self._GroupChatConfig = GroupChatConfig()
            self._GroupChatConfig._deserialize(params.get("GroupChatConfig"))
        self._UserId = params.get("UserId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupChatCompletionsResponse(AbstractModel):
    """GroupChatCompletions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Created: Unix 时间戳，单位为秒。
        :type Created: int
        :param _Usage: Token 统计信息。
按照总 Token 数量计费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        :param _Note: 免责声明。
        :type Note: str
        :param _Id: 本次请求的 RequestId。
        :type Id: str
        :param _Choices: 回复内容。
        :type Choices: list of Choice
        :param _ErrorMsg: 错误信息。
如果流式返回中服务处理异常，返回该错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        :param _SearchInfo: 搜索结果信息
        :type SearchInfo: :class:`tencentcloud.hunyuan.v20230901.models.SearchInfo`
        :param _Replaces: 多媒体信息。
说明：
1. 可以用多媒体信息替换回复内容里的占位符，得到完整的消息。
2. 可能会出现回复内容里存在占位符，但是因为审核等原因没有返回多媒体信息。
        :type Replaces: list of Replace
        :param _RecommendedQuestions: 推荐问答。
        :type RecommendedQuestions: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Created = None
        self._Usage = None
        self._Note = None
        self._Id = None
        self._Choices = None
        self._ErrorMsg = None
        self._SearchInfo = None
        self._Replaces = None
        self._RecommendedQuestions = None
        self._RequestId = None

    @property
    def Created(self):
        """Unix 时间戳，单位为秒。
        :rtype: int
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        """Token 统计信息。
按照总 Token 数量计费。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Note(self):
        """免责声明。
        :rtype: str
        """
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Id(self):
        """本次请求的 RequestId。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        """回复内容。
        :rtype: list of Choice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def ErrorMsg(self):
        """错误信息。
如果流式返回中服务处理异常，返回该错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def SearchInfo(self):
        """搜索结果信息
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SearchInfo`
        """
        return self._SearchInfo

    @SearchInfo.setter
    def SearchInfo(self, SearchInfo):
        self._SearchInfo = SearchInfo

    @property
    def Replaces(self):
        """多媒体信息。
说明：
1. 可以用多媒体信息替换回复内容里的占位符，得到完整的消息。
2. 可能会出现回复内容里存在占位符，但是因为审核等原因没有返回多媒体信息。
        :rtype: list of Replace
        """
        return self._Replaces

    @Replaces.setter
    def Replaces(self, Replaces):
        self._Replaces = Replaces

    @property
    def RecommendedQuestions(self):
        """推荐问答。
        :rtype: list of str
        """
        return self._RecommendedQuestions

    @RecommendedQuestions.setter
    def RecommendedQuestions(self, RecommendedQuestions):
        self._RecommendedQuestions = RecommendedQuestions

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._Note = params.get("Note")
        self._Id = params.get("Id")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        if params.get("ErrorMsg") is not None:
            self._ErrorMsg = ErrorMsg()
            self._ErrorMsg._deserialize(params.get("ErrorMsg"))
        if params.get("SearchInfo") is not None:
            self._SearchInfo = SearchInfo()
            self._SearchInfo._deserialize(params.get("SearchInfo"))
        if params.get("Replaces") is not None:
            self._Replaces = []
            for item in params.get("Replaces"):
                obj = Replace()
                obj._deserialize(item)
                self._Replaces.append(obj)
        self._RecommendedQuestions = params.get("RecommendedQuestions")
        self._RequestId = params.get("RequestId")


class GroupChatConfig(AbstractModel):
    """群聊配置

    """

    def __init__(self):
        r"""
        :param _UserName: 人物名称
        :type UserName: str
        :param _Description: ### 主题：\n武道修炼与科技创新的碰撞\n\n### 地点：\n布尔玛的实验室\n\n### 故事背景：\n布尔玛正在研发一种新型的龙珠雷达，旨在更精确地定位龙珠的位置。她邀请了孙悟空、天津饭、饺子和雅木茶前来测试新设备。然而，这些武道家们对科技的理解有限，导致了一系列有趣的误解和互动。\n\n### 人物关系：\n- **布尔玛**：天才科学家，负责研发和解释新设备。\n- **孙悟空**：纯粹的战斗狂，对科技一窍不通，但对新事物充满好奇。\n- **天津饭**：严肃自律的武道家，对科技持谨慎态度，但愿意尝试。\n- **饺子**：内向单纯，依赖天津饭，对科技感到困惑和害怕。\n- **雅木茶**：幽默自嘲的前沙漠强盗，对科技有一定了解，但更倾向于轻松调侃。\n\n### 人物目标：\n- **布尔玛**：希望新龙珠雷达能够得到有效测试，并得到反馈以改进。\n- **孙悟空**：希望通过新设备找到更强的对手进行战斗。\n- **天津饭**：希望通过测试新设备提升自己的武道修炼。\n- **饺子**：希望在不引起麻烦的情况下完成任务，并得到天津饭的认可。\n- **雅木茶**：希望通过参与测试证明自己的价值，同时享受与朋友们的互动。\n\n### 场景描述：\n布尔玛在实验室中展示她的新龙珠雷达，解释其工作原理和优势。孙悟空对设备的功能感到兴奋，但完全无法理解技术细节，不断提出天真的问题。天津饭则严肃地询问设备的安全性和可靠性，表现出对科技的谨慎态度。饺子对复杂的设备感到害怕，不断向天津饭寻求确认和安慰。雅木茶则在一旁调侃大家的反应，试图缓解紧张气氛。布尔玛在解释过程中不断被孙悟空的问题打断，感到无奈，但也被他的热情所感染。最终，大家决定一起外出测试新设备，展开一场充满欢笑和冒险的旅程。
        :type Description: str
        :param _Characters: 角色描述
        :type Characters: list of Character
        """
        self._UserName = None
        self._Description = None
        self._Characters = None

    @property
    def UserName(self):
        """人物名称
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Description(self):
        """### 主题：\n武道修炼与科技创新的碰撞\n\n### 地点：\n布尔玛的实验室\n\n### 故事背景：\n布尔玛正在研发一种新型的龙珠雷达，旨在更精确地定位龙珠的位置。她邀请了孙悟空、天津饭、饺子和雅木茶前来测试新设备。然而，这些武道家们对科技的理解有限，导致了一系列有趣的误解和互动。\n\n### 人物关系：\n- **布尔玛**：天才科学家，负责研发和解释新设备。\n- **孙悟空**：纯粹的战斗狂，对科技一窍不通，但对新事物充满好奇。\n- **天津饭**：严肃自律的武道家，对科技持谨慎态度，但愿意尝试。\n- **饺子**：内向单纯，依赖天津饭，对科技感到困惑和害怕。\n- **雅木茶**：幽默自嘲的前沙漠强盗，对科技有一定了解，但更倾向于轻松调侃。\n\n### 人物目标：\n- **布尔玛**：希望新龙珠雷达能够得到有效测试，并得到反馈以改进。\n- **孙悟空**：希望通过新设备找到更强的对手进行战斗。\n- **天津饭**：希望通过测试新设备提升自己的武道修炼。\n- **饺子**：希望在不引起麻烦的情况下完成任务，并得到天津饭的认可。\n- **雅木茶**：希望通过参与测试证明自己的价值，同时享受与朋友们的互动。\n\n### 场景描述：\n布尔玛在实验室中展示她的新龙珠雷达，解释其工作原理和优势。孙悟空对设备的功能感到兴奋，但完全无法理解技术细节，不断提出天真的问题。天津饭则严肃地询问设备的安全性和可靠性，表现出对科技的谨慎态度。饺子对复杂的设备感到害怕，不断向天津饭寻求确认和安慰。雅木茶则在一旁调侃大家的反应，试图缓解紧张气氛。布尔玛在解释过程中不断被孙悟空的问题打断，感到无奈，但也被他的热情所感染。最终，大家决定一起外出测试新设备，展开一场充满欢笑和冒险的旅程。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Characters(self):
        """角色描述
        :rtype: list of Character
        """
        return self._Characters

    @Characters.setter
    def Characters(self, Characters):
        self._Characters = Characters


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Description = params.get("Description")
        if params.get("Characters") is not None:
            self._Characters = []
            for item in params.get("Characters"):
                obj = Character()
                obj._deserialize(item)
                self._Characters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupMessage(AbstractModel):
    """群聊会话内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色，可选值包括 system、user、assistant、 tool。
        :type Role: str
        :param _Content: 文本内容
        :type Content: str
        :param _Name: 角色名称
        :type Name: str
        """
        self._Role = None
        self._Content = None
        self._Name = None

    @property
    def Role(self):
        """角色，可选值包括 system、user、assistant、 tool。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """文本内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Name(self):
        """角色名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class History(AbstractModel):
    """混元生图多轮对话历史记录。

    """

    def __init__(self):
        r"""
        :param _ChatId: 对话的 ID，用于唯一标识一轮对话
注意：此字段可能返回 null，表示取不到有效值。
        :type ChatId: str
        :param _Prompt: 原始输入的 Prompt 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Prompt: str
        :param _RevisedPrompt: 扩写后的 Prompt 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type RevisedPrompt: str
        :param _Seed: 生成图的随机种子
注意：此字段可能返回 null，表示取不到有效值。
        :type Seed: int
        """
        self._ChatId = None
        self._Prompt = None
        self._RevisedPrompt = None
        self._Seed = None

    @property
    def ChatId(self):
        """对话的 ID，用于唯一标识一轮对话
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def Prompt(self):
        """原始输入的 Prompt 文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def RevisedPrompt(self):
        """扩写后的 Prompt 文本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RevisedPrompt

    @RevisedPrompt.setter
    def RevisedPrompt(self, RevisedPrompt):
        self._RevisedPrompt = RevisedPrompt

    @property
    def Seed(self):
        """生成图的随机种子
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed


    def _deserialize(self, params):
        self._ChatId = params.get("ChatId")
        self._Prompt = params.get("Prompt")
        self._RevisedPrompt = params.get("RevisedPrompt")
        self._Seed = params.get("Seed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """图片信息

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片Url。
        :type ImageUrl: str
        :param _ImageBase64: 图片Base64。
        :type ImageBase64: str
        """
        self._ImageUrl = None
        self._ImageBase64 = None

    @property
    def ImageUrl(self):
        """图片Url。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        """图片Base64。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageUrl(AbstractModel):
    """具体的图片内容

    """

    def __init__(self):
        r"""
        :param _Url: 图片的 Url（以 http:// 或 https:// 开头）
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """图片的 Url（以 http:// 或 https:// 开头）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoParam(AbstractModel):
    """logo参数

    """

    def __init__(self):
        r"""
        :param _LogoUrl: 水印url
        :type LogoUrl: str
        :param _LogoImage: 水印base64，url和base64二选一传入
        :type LogoImage: str
        :param _LogoRect: 水印图片位于融合结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
        :type LogoRect: :class:`tencentcloud.hunyuan.v20230901.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        """水印url
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        """水印base64，url和base64二选一传入
        :rtype: str
        """
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        """水印图片位于融合结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.LogoRect`
        """
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect


    def _deserialize(self, params):
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        if params.get("LogoRect") is not None:
            self._LogoRect = LogoRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoRect(AbstractModel):
    """输入框

    """

    def __init__(self):
        r"""
        :param _X: 左上角X坐标
        :type X: int
        :param _Y: 左上角Y坐标
        :type Y: int
        :param _Width: 方框宽度
        :type Width: int
        :param _Height: 方框高度
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        """左上角X坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        """左上角Y坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        """方框宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """方框高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Message(AbstractModel):
    """会话内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色，可选值包括 system、user、assistant、 tool。
        :type Role: str
        :param _Content: 文本内容
        :type Content: str
        :param _Contents: 多种类型内容（目前支持图片和文本），仅 hunyuan-vision 和 hunyuan-turbo-vision 模型支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Contents: list of Content
        :param _ToolCallId: 当role为tool时传入，标识具体的函数调用
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCallId: str
        :param _ToolCalls: 模型生成的工具调用，仅 hunyuan-pro 或者 hunyuan-functioncall 模型支持
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCalls: list of ToolCall
        :param _FileIDs: 文件标识符。单次最大 50 个文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileIDs: list of str
        :param _ReasoningContent: 思维链内容。用于展示模型思考过程，仅 Hunyuan-T1 系列模型可用。注意：在进行多轮对话时，请**不要**将此字段拼接到 messages 中。请求 messages 的请求参数中包含 reasoning_content，接口将报错。
        :type ReasoningContent: str
        """
        self._Role = None
        self._Content = None
        self._Contents = None
        self._ToolCallId = None
        self._ToolCalls = None
        self._FileIDs = None
        self._ReasoningContent = None

    @property
    def Role(self):
        """角色，可选值包括 system、user、assistant、 tool。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """文本内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Contents(self):
        """多种类型内容（目前支持图片和文本），仅 hunyuan-vision 和 hunyuan-turbo-vision 模型支持
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Content
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def ToolCallId(self):
        """当role为tool时传入，标识具体的函数调用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ToolCallId

    @ToolCallId.setter
    def ToolCallId(self, ToolCallId):
        self._ToolCallId = ToolCallId

    @property
    def ToolCalls(self):
        """模型生成的工具调用，仅 hunyuan-pro 或者 hunyuan-functioncall 模型支持
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ToolCall
        """
        return self._ToolCalls

    @ToolCalls.setter
    def ToolCalls(self, ToolCalls):
        self._ToolCalls = ToolCalls

    @property
    def FileIDs(self):
        """文件标识符。单次最大 50 个文件。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FileIDs

    @FileIDs.setter
    def FileIDs(self, FileIDs):
        self._FileIDs = FileIDs

    @property
    def ReasoningContent(self):
        """思维链内容。用于展示模型思考过程，仅 Hunyuan-T1 系列模型可用。注意：在进行多轮对话时，请**不要**将此字段拼接到 messages 中。请求 messages 的请求参数中包含 reasoning_content，接口将报错。
        :rtype: str
        """
        return self._ReasoningContent

    @ReasoningContent.setter
    def ReasoningContent(self, ReasoningContent):
        self._ReasoningContent = ReasoningContent


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = Content()
                obj._deserialize(item)
                self._Contents.append(obj)
        self._ToolCallId = params.get("ToolCallId")
        if params.get("ToolCalls") is not None:
            self._ToolCalls = []
            for item in params.get("ToolCalls"):
                obj = ToolCall()
                obj._deserialize(item)
                self._ToolCalls.append(obj)
        self._FileIDs = params.get("FileIDs")
        self._ReasoningContent = params.get("ReasoningContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Mindmap(AbstractModel):
    """脑图

    """

    def __init__(self):
        r"""
        :param _ThumbUrl: 脑图缩略图链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ThumbUrl: str
        :param _Url: 脑图图片链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self._ThumbUrl = None
        self._Url = None

    @property
    def ThumbUrl(self):
        """脑图缩略图链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ThumbUrl

    @ThumbUrl.setter
    def ThumbUrl(self, ThumbUrl):
        self._ThumbUrl = ThumbUrl

    @property
    def Url(self):
        """脑图图片链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._ThumbUrl = params.get("ThumbUrl")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Multimedia(AbstractModel):
    """多媒体详情

    """

    def __init__(self):
        r"""
        :param _Type: 多媒体类型，可选值包括 image、music、album、playlist。
说明：
1. image：图片；music：单曲，类型为单曲时，会返回详细歌手和歌曲信息；album：专辑；playlist：歌单。
2. 当 type 为 music、album、playlist 时，需要配合 [QQ音乐SDK](https://developer.y.qq.com/) 使用。
        :type Type: str
        :param _Url: 多媒体地址。
说明：
1. type 为 image 时，地址为图片的预览地址；其他类型时，地址为封面图地址。
        :type Url: str
        :param _JumpUrl: 多媒体详情地址。
说明：
1. 仅 type 为 image 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type JumpUrl: str
        :param _Title: 名称。
说明：
1. type 为 image 时，该字段为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Desc: 描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Singer: 歌手名称。
说明：
1. 仅 type 为 music 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Singer: str
        :param _Ext: 歌曲详情。
说明：
1. 仅 type 为 music 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ext: :class:`tencentcloud.hunyuan.v20230901.models.SongExt`
        """
        self._Type = None
        self._Url = None
        self._JumpUrl = None
        self._Title = None
        self._Desc = None
        self._Singer = None
        self._Ext = None

    @property
    def Type(self):
        """多媒体类型，可选值包括 image、music、album、playlist。
说明：
1. image：图片；music：单曲，类型为单曲时，会返回详细歌手和歌曲信息；album：专辑；playlist：歌单。
2. 当 type 为 music、album、playlist 时，需要配合 [QQ音乐SDK](https://developer.y.qq.com/) 使用。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        """多媒体地址。
说明：
1. type 为 image 时，地址为图片的预览地址；其他类型时，地址为封面图地址。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def JumpUrl(self):
        """多媒体详情地址。
说明：
1. 仅 type 为 image 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def Title(self):
        """名称。
说明：
1. type 为 image 时，该字段为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Desc(self):
        """描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Singer(self):
        """歌手名称。
说明：
1. 仅 type 为 music 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Singer

    @Singer.setter
    def Singer(self, Singer):
        self._Singer = Singer

    @property
    def Ext(self):
        """歌曲详情。
说明：
1. 仅 type 为 music 时，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SongExt`
        """
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._JumpUrl = params.get("JumpUrl")
        self._Title = params.get("Title")
        self._Desc = params.get("Desc")
        self._Singer = params.get("Singer")
        if params.get("Ext") is not None:
            self._Ext = SongExt()
            self._Ext._deserialize(params.get("Ext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanImageChatJobRequest(AbstractModel):
    """QueryHunyuanImageChatJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanImageChatJobResponse(AbstractModel):
    """QueryHunyuanImageChatJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 当前任务状态：排队中、处理中、处理失败或者处理完成。

        :type JobStatusMsg: str
        :param _JobErrorCode: 任务处理失败错误码。

        :type JobErrorCode: str
        :param _JobErrorMsg: 任务处理失败错误信息。

        :type JobErrorMsg: str
        :param _ChatId: 本轮对话的 ChatId，ChatId 用于唯一标识一轮对话。
一个对话组中，最多支持进行100轮对话。
每轮对话数据有效期为7天，到期后 ChatId 失效，有效期内的历史对话数据可通过 History 查询，如有长期使用需求请及时保存输入输出数据。
        :type ChatId: str
        :param _ResultImage: 生成图 URL 列表，有效期7天，请及时保存。
        :type ResultImage: list of str
        :param _ResultDetails: 结果 detail 数组，Success 代表成功。

        :type ResultDetails: list of str
        :param _History: 本轮对话前置的历史对话数据（不含生成图）。
        :type History: list of History
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ChatId = None
        self._ResultImage = None
        self._ResultDetails = None
        self._History = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        """当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        """当前任务状态：排队中、处理中、处理失败或者处理完成。

        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        """任务处理失败错误码。

        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        """任务处理失败错误信息。

        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ChatId(self):
        """本轮对话的 ChatId，ChatId 用于唯一标识一轮对话。
一个对话组中，最多支持进行100轮对话。
每轮对话数据有效期为7天，到期后 ChatId 失效，有效期内的历史对话数据可通过 History 查询，如有长期使用需求请及时保存输入输出数据。
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def ResultImage(self):
        """生成图 URL 列表，有效期7天，请及时保存。
        :rtype: list of str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultDetails(self):
        """结果 detail 数组，Success 代表成功。

        :rtype: list of str
        """
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

    @property
    def History(self):
        """本轮对话前置的历史对话数据（不含生成图）。
        :rtype: list of History
        """
        return self._History

    @History.setter
    def History(self, History):
        self._History = History

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ChatId = params.get("ChatId")
        self._ResultImage = params.get("ResultImage")
        self._ResultDetails = params.get("ResultDetails")
        if params.get("History") is not None:
            self._History = []
            for item in params.get("History"):
                obj = History()
                obj._deserialize(item)
                self._History.append(obj)
        self._RequestId = params.get("RequestId")


class QueryHunyuanImageJobRequest(AbstractModel):
    """QueryHunyuanImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanImageJobResponse(AbstractModel):
    """QueryHunyuanImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 当前任务状态：排队中、处理中、处理失败或者处理完成。

        :type JobStatusMsg: str
        :param _JobErrorCode: 任务处理失败错误码。

        :type JobErrorCode: str
        :param _JobErrorMsg: 任务处理失败错误信息。

        :type JobErrorMsg: str
        :param _ResultImage: 生成图 URL 列表，有效期1小时，请及时保存。

        :type ResultImage: list of str
        :param _ResultDetails: 结果 detail 数组，Success 代表成功。

        :type ResultDetails: list of str
        :param _RevisedPrompt: 对应 SubmitHunyuanImageJob 接口中 Revise 参数。开启扩写时，返回扩写后的 prompt 文本。 如果关闭扩写，将直接返回原始输入的 prompt。
        :type RevisedPrompt: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultImage = None
        self._ResultDetails = None
        self._RevisedPrompt = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        """当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :rtype: str
        """
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        """当前任务状态：排队中、处理中、处理失败或者处理完成。

        :rtype: str
        """
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        """任务处理失败错误码。

        :rtype: str
        """
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        """任务处理失败错误信息。

        :rtype: str
        """
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultImage(self):
        """生成图 URL 列表，有效期1小时，请及时保存。

        :rtype: list of str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultDetails(self):
        """结果 detail 数组，Success 代表成功。

        :rtype: list of str
        """
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

    @property
    def RevisedPrompt(self):
        """对应 SubmitHunyuanImageJob 接口中 Revise 参数。开启扩写时，返回扩写后的 prompt 文本。 如果关闭扩写，将直接返回原始输入的 prompt。
        :rtype: list of str
        """
        return self._RevisedPrompt

    @RevisedPrompt.setter
    def RevisedPrompt(self, RevisedPrompt):
        self._RevisedPrompt = RevisedPrompt

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultImage = params.get("ResultImage")
        self._ResultDetails = params.get("ResultDetails")
        self._RevisedPrompt = params.get("RevisedPrompt")
        self._RequestId = params.get("RequestId")


class QueryHunyuanTo3DJobRequest(AbstractModel):
    """QueryHunyuanTo3DJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanTo3DJobResponse(AbstractModel):
    """QueryHunyuanTo3DJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ResultFile3Ds: 生成的3D文件数组
        :type ResultFile3Ds: list of File3Ds
        :param _ErrorCode: 错误码
        :type ErrorCode: str
        :param _ErrorMessage: 错误信息
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ResultFile3Ds = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        """任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultFile3Ds(self):
        """生成的3D文件数组
        :rtype: list of File3Ds
        """
        return self._ResultFile3Ds

    @ResultFile3Ds.setter
    def ResultFile3Ds(self, ResultFile3Ds):
        self._ResultFile3Ds = ResultFile3Ds

    @property
    def ErrorCode(self):
        """错误码
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        """错误信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        if params.get("ResultFile3Ds") is not None:
            self._ResultFile3Ds = []
            for item in params.get("ResultFile3Ds"):
                obj = File3Ds()
                obj._deserialize(item)
                self._ResultFile3Ds.append(obj)
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class Reference(AbstractModel):
    """翻译对话参考示例

    """

    def __init__(self):
        r"""
        :param _Type: 翻译文本类型，枚举"sentence"表示句子, "term"表示术语
        :type Type: str
        :param _Text: 原文
        :type Text: str
        :param _Translation: 译文
        :type Translation: str
        """
        self._Type = None
        self._Text = None
        self._Translation = None

    @property
    def Type(self):
        """翻译文本类型，枚举"sentence"表示句子, "term"表示术语
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Text(self):
        """原文
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Translation(self):
        """译文
        :rtype: str
        """
        return self._Translation

    @Translation.setter
    def Translation(self, Translation):
        self._Translation = Translation


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Text = params.get("Text")
        self._Translation = params.get("Translation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelevantEntity(AbstractModel):
    """相关组织及人物

    """

    def __init__(self):
        r"""
        :param _Name: 相关组织及人物名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Content: 相关组织及人物内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Reference: 相关事件引用文章标号
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: list of int
        """
        self._Name = None
        self._Content = None
        self._Reference = None

    @property
    def Name(self):
        """相关组织及人物名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        """相关组织及人物内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Reference(self):
        """相关事件引用文章标号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Reference = params.get("Reference")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelevantEvent(AbstractModel):
    """相关事件

    """

    def __init__(self):
        r"""
        :param _Title: 相关事件标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Content: 相关事件内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Datetime: 相关事件时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Datetime: str
        :param _Reference: 相关事件引用文章标号
注意：此字段可能返回 null，表示取不到有效值。
        :type Reference: list of int
        """
        self._Title = None
        self._Content = None
        self._Datetime = None
        self._Reference = None

    @property
    def Title(self):
        """相关事件标题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        """相关事件内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Datetime(self):
        """相关事件时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Datetime

    @Datetime.setter
    def Datetime(self, Datetime):
        self._Datetime = Datetime

    @property
    def Reference(self):
        """相关事件引用文章标号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._Datetime = params.get("Datetime")
        self._Reference = params.get("Reference")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Replace(AbstractModel):
    """多媒体占位符替换信息

    """

    def __init__(self):
        r"""
        :param _Id: 占位符序号
        :type Id: str
        :param _Multimedia: 多媒体详情
        :type Multimedia: list of Multimedia
        """
        self._Id = None
        self._Multimedia = None

    @property
    def Id(self):
        """占位符序号
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Multimedia(self):
        """多媒体详情
        :rtype: list of Multimedia
        """
        return self._Multimedia

    @Multimedia.setter
    def Multimedia(self, Multimedia):
        self._Multimedia = Multimedia


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("Multimedia") is not None:
            self._Multimedia = []
            for item in params.get("Multimedia"):
                obj = Multimedia()
                obj._deserialize(item)
                self._Multimedia.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunThreadRequest(AbstractModel):
    """RunThread请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ThreadID: 会话 ID
        :type ThreadID: str
        :param _AssistantID: 助手 ID（目前未使用，留空）
        :type AssistantID: str
        :param _Model: 模型名称，可选值包括 hunyuan-lite、hunyuan-standard、hunyuan-standard-256K、hunyuan-pro、 hunyuan-code、 hunyuan-role、 hunyuan-functioncall、 hunyuan-vision、 hunyuan-turbo。各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。注意：不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :type Model: str
        :param _AdditionalMessages: 附加消息
        :type AdditionalMessages: list of ThreadAdditionalMessage
        :param _Temperature: 说明：1. 影响模型输出多样性，模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。2. 取值区间为 [0.0, 2.0]。较高的数值会使输出更加多样化和不可预测，而较低的数值会使其更加集中和确定。
        :type Temperature: float
        :param _TopP: 说明：1. 影响输出文本的多样性。模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。2. 取值区间为 [0.0, 1.0]。取值越大，生成文本的多样性越强。
        :type TopP: float
        :param _Stream: 是否流式输出，当前只允许 true
        :type Stream: bool
        :param _MaxPromptTokens: 运行过程中可使用的 token 最大数量。
        :type MaxPromptTokens: int
        :param _MaxCompletionTokens: 运行过程中可使用的完成 token 的最大数量。
        :type MaxCompletionTokens: int
        :param _Tools: 可调用的工具列表，仅对 hunyuan-pro、hunyuan-turbo、hunyuan-functioncall 模型生效。
        :type Tools: list of Tool
        :param _ToolChoice: 工具使用选项，可选值包括 none、auto、custom。说明：1. 仅对 hunyuan-pro、hunyuan-turbo、hunyuan-functioncall 模型生效。2. none：不调用工具；auto：模型自行选择生成回复或调用工具；custom：强制模型调用指定的工具。3. 未设置时，默认值为auto
        :type ToolChoice: str
        """
        self._ThreadID = None
        self._AssistantID = None
        self._Model = None
        self._AdditionalMessages = None
        self._Temperature = None
        self._TopP = None
        self._Stream = None
        self._MaxPromptTokens = None
        self._MaxCompletionTokens = None
        self._Tools = None
        self._ToolChoice = None

    @property
    def ThreadID(self):
        """会话 ID
        :rtype: str
        """
        return self._ThreadID

    @ThreadID.setter
    def ThreadID(self, ThreadID):
        self._ThreadID = ThreadID

    @property
    def AssistantID(self):
        """助手 ID（目前未使用，留空）
        :rtype: str
        """
        return self._AssistantID

    @AssistantID.setter
    def AssistantID(self, AssistantID):
        self._AssistantID = AssistantID

    @property
    def Model(self):
        """模型名称，可选值包括 hunyuan-lite、hunyuan-standard、hunyuan-standard-256K、hunyuan-pro、 hunyuan-code、 hunyuan-role、 hunyuan-functioncall、 hunyuan-vision、 hunyuan-turbo。各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。注意：不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def AdditionalMessages(self):
        """附加消息
        :rtype: list of ThreadAdditionalMessage
        """
        return self._AdditionalMessages

    @AdditionalMessages.setter
    def AdditionalMessages(self, AdditionalMessages):
        self._AdditionalMessages = AdditionalMessages

    @property
    def Temperature(self):
        """说明：1. 影响模型输出多样性，模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。2. 取值区间为 [0.0, 2.0]。较高的数值会使输出更加多样化和不可预测，而较低的数值会使其更加集中和确定。
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        """说明：1. 影响输出文本的多样性。模型已有默认参数，不传值时使用各模型推荐值，不推荐用户修改。2. 取值区间为 [0.0, 1.0]。取值越大，生成文本的多样性越强。
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Stream(self):
        """是否流式输出，当前只允许 true
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def MaxPromptTokens(self):
        """运行过程中可使用的 token 最大数量。
        :rtype: int
        """
        return self._MaxPromptTokens

    @MaxPromptTokens.setter
    def MaxPromptTokens(self, MaxPromptTokens):
        self._MaxPromptTokens = MaxPromptTokens

    @property
    def MaxCompletionTokens(self):
        """运行过程中可使用的完成 token 的最大数量。
        :rtype: int
        """
        return self._MaxCompletionTokens

    @MaxCompletionTokens.setter
    def MaxCompletionTokens(self, MaxCompletionTokens):
        self._MaxCompletionTokens = MaxCompletionTokens

    @property
    def Tools(self):
        """可调用的工具列表，仅对 hunyuan-pro、hunyuan-turbo、hunyuan-functioncall 模型生效。
        :rtype: list of Tool
        """
        return self._Tools

    @Tools.setter
    def Tools(self, Tools):
        self._Tools = Tools

    @property
    def ToolChoice(self):
        """工具使用选项，可选值包括 none、auto、custom。说明：1. 仅对 hunyuan-pro、hunyuan-turbo、hunyuan-functioncall 模型生效。2. none：不调用工具；auto：模型自行选择生成回复或调用工具；custom：强制模型调用指定的工具。3. 未设置时，默认值为auto
        :rtype: str
        """
        return self._ToolChoice

    @ToolChoice.setter
    def ToolChoice(self, ToolChoice):
        self._ToolChoice = ToolChoice


    def _deserialize(self, params):
        self._ThreadID = params.get("ThreadID")
        self._AssistantID = params.get("AssistantID")
        self._Model = params.get("Model")
        if params.get("AdditionalMessages") is not None:
            self._AdditionalMessages = []
            for item in params.get("AdditionalMessages"):
                obj = ThreadAdditionalMessage()
                obj._deserialize(item)
                self._AdditionalMessages.append(obj)
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._Stream = params.get("Stream")
        self._MaxPromptTokens = params.get("MaxPromptTokens")
        self._MaxCompletionTokens = params.get("MaxCompletionTokens")
        if params.get("Tools") is not None:
            self._Tools = []
            for item in params.get("Tools"):
                obj = Tool()
                obj._deserialize(item)
                self._Tools.append(obj)
        self._ToolChoice = params.get("ToolChoice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunThreadResponse(AbstractModel):
    """RunThread返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SearchInfo(AbstractModel):
    """搜索结果信息

    """

    def __init__(self):
        r"""
        :param _SearchResults: 搜索引文信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchResults: list of SearchResult
        :param _Mindmap: 脑图（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type Mindmap: :class:`tencentcloud.hunyuan.v20230901.models.Mindmap`
        :param _RelevantEvents: 相关事件（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回，深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantEvents: list of RelevantEvent
        :param _RelevantEntities: 相关组织及人物（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回，深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantEntities: list of RelevantEntity
        :param _Timeline: 时间线（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回，深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeline: list of Timeline
        :param _SupportDeepSearch: 是否命中搜索深度模式
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportDeepSearch: bool
        :param _Outline: 搜索回复大纲（深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type Outline: list of str
        """
        self._SearchResults = None
        self._Mindmap = None
        self._RelevantEvents = None
        self._RelevantEntities = None
        self._Timeline = None
        self._SupportDeepSearch = None
        self._Outline = None

    @property
    def SearchResults(self):
        """搜索引文信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SearchResult
        """
        return self._SearchResults

    @SearchResults.setter
    def SearchResults(self, SearchResults):
        self._SearchResults = SearchResults

    @property
    def Mindmap(self):
        """脑图（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Mindmap`
        """
        return self._Mindmap

    @Mindmap.setter
    def Mindmap(self, Mindmap):
        self._Mindmap = Mindmap

    @property
    def RelevantEvents(self):
        """相关事件（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回，深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RelevantEvent
        """
        return self._RelevantEvents

    @RelevantEvents.setter
    def RelevantEvents(self, RelevantEvents):
        self._RelevantEvents = RelevantEvents

    @property
    def RelevantEntities(self):
        """相关组织及人物（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回，深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RelevantEntity
        """
        return self._RelevantEntities

    @RelevantEntities.setter
    def RelevantEntities(self, RelevantEntities):
        self._RelevantEntities = RelevantEntities

    @property
    def Timeline(self):
        """时间线（回复中不一定存在，流式协议中，仅在最后一条流式数据中返回，深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Timeline
        """
        return self._Timeline

    @Timeline.setter
    def Timeline(self, Timeline):
        self._Timeline = Timeline

    @property
    def SupportDeepSearch(self):
        """是否命中搜索深度模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._SupportDeepSearch

    @SupportDeepSearch.setter
    def SupportDeepSearch(self, SupportDeepSearch):
        self._SupportDeepSearch = SupportDeepSearch

    @property
    def Outline(self):
        """搜索回复大纲（深度模式下返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Outline

    @Outline.setter
    def Outline(self, Outline):
        self._Outline = Outline


    def _deserialize(self, params):
        if params.get("SearchResults") is not None:
            self._SearchResults = []
            for item in params.get("SearchResults"):
                obj = SearchResult()
                obj._deserialize(item)
                self._SearchResults.append(obj)
        if params.get("Mindmap") is not None:
            self._Mindmap = Mindmap()
            self._Mindmap._deserialize(params.get("Mindmap"))
        if params.get("RelevantEvents") is not None:
            self._RelevantEvents = []
            for item in params.get("RelevantEvents"):
                obj = RelevantEvent()
                obj._deserialize(item)
                self._RelevantEvents.append(obj)
        if params.get("RelevantEntities") is not None:
            self._RelevantEntities = []
            for item in params.get("RelevantEntities"):
                obj = RelevantEntity()
                obj._deserialize(item)
                self._RelevantEntities.append(obj)
        if params.get("Timeline") is not None:
            self._Timeline = []
            for item in params.get("Timeline"):
                obj = Timeline()
                obj._deserialize(item)
                self._Timeline.append(obj)
        self._SupportDeepSearch = params.get("SupportDeepSearch")
        self._Outline = params.get("Outline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResult(AbstractModel):
    """搜索引文信息

    """

    def __init__(self):
        r"""
        :param _Index: 搜索引文序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Title: 搜索引文标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Url: 搜索引文链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Text: 搜索引文站点名
        :type Text: str
        :param _Icon: 搜索引文图标
        :type Icon: str
        """
        self._Index = None
        self._Title = None
        self._Url = None
        self._Text = None
        self._Icon = None

    @property
    def Index(self):
        """搜索引文序号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Title(self):
        """搜索引文标题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Url(self):
        """搜索引文链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Text(self):
        """搜索引文站点名
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Icon(self):
        """搜索引文图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Title = params.get("Title")
        self._Url = params.get("Url")
        self._Text = params.get("Text")
        self._Icon = params.get("Icon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPayModeRequest(AbstractModel):
    """SetPayMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PayMode: 设置后付费状态，0：后付费打开；1：后付费关闭
        :type PayMode: int
        """
        self._PayMode = None

    @property
    def PayMode(self):
        """设置后付费状态，0：后付费打开；1：后付费关闭
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPayModeResponse(AbstractModel):
    """SetPayMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SongExt(AbstractModel):
    """歌曲详情。具体含义参考  [QQ音乐SDK](https://developer.y.qq.com/)

    """

    def __init__(self):
        r"""
        :param _SongId: 歌曲id
        :type SongId: int
        :param _SongMid: 歌曲mid
        :type SongMid: str
        :param _Vip: 歌曲是否为vip。1：vip歌曲； 0：普通歌曲。
        :type Vip: int
        """
        self._SongId = None
        self._SongMid = None
        self._Vip = None

    @property
    def SongId(self):
        """歌曲id
        :rtype: int
        """
        return self._SongId

    @SongId.setter
    def SongId(self, SongId):
        self._SongId = SongId

    @property
    def SongMid(self):
        """歌曲mid
        :rtype: str
        """
        return self._SongMid

    @SongMid.setter
    def SongMid(self, SongMid):
        self._SongMid = SongMid

    @property
    def Vip(self):
        """歌曲是否为vip。1：vip歌曲； 0：普通歌曲。
        :rtype: int
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._SongId = params.get("SongId")
        self._SongMid = params.get("SongMid")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanImageChatJobRequest(AbstractModel):
    """SubmitHunyuanImageChatJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 本轮对话的文本描述。
提交一个任务请求对应发起一轮生图对话，每轮对话中可输入一条 Prompt，生成一张图像，支持通过多轮输入 Prompt 来不断调整图像内容。
推荐使用中文，最多可传1024个 utf-8 字符。
输入示例：
<li> 第一轮对话：一颗红色的苹果 </li>
<li> 第二轮对话：将苹果改为绿色 </li>
<li> 第三轮对话：苹果放在桌子上 </li>
        :type Prompt: str
        :param _ChatId: 上传上一轮对话的 ChatId，本轮对话将在指定的上一轮对话结果基础上继续生成图像。
如果不传代表新建一个对话组，重新开启一轮新的对话。
一个对话组中，最多支持进行100轮对话。
        :type ChatId: str
        :param _LogoAdd: 为生成结果图添加显式水印标识的开关，默认为1。  
1：添加。  
0：不添加。  
其他数值：默认按1处理。  
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        """
        self._Prompt = None
        self._ChatId = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        """本轮对话的文本描述。
提交一个任务请求对应发起一轮生图对话，每轮对话中可输入一条 Prompt，生成一张图像，支持通过多轮输入 Prompt 来不断调整图像内容。
推荐使用中文，最多可传1024个 utf-8 字符。
输入示例：
<li> 第一轮对话：一颗红色的苹果 </li>
<li> 第二轮对话：将苹果改为绿色 </li>
<li> 第三轮对话：苹果放在桌子上 </li>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def ChatId(self):
        """上传上一轮对话的 ChatId，本轮对话将在指定的上一轮对话结果基础上继续生成图像。
如果不传代表新建一个对话组，重新开启一轮新的对话。
一个对话组中，最多支持进行100轮对话。
        :rtype: str
        """
        return self._ChatId

    @ChatId.setter
    def ChatId(self, ChatId):
        self._ChatId = ChatId

    @property
    def LogoAdd(self):
        """为生成结果图添加显式水印标识的开关，默认为1。  
1：添加。  
0：不添加。  
其他数值：默认按1处理。  
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        """标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._ChatId = params.get("ChatId")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanImageChatJobResponse(AbstractModel):
    """SubmitHunyuanImageChatJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHunyuanImageJobRequest(AbstractModel):
    """SubmitHunyuanImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本描述。 
算法将根据输入的文本智能生成与之相关的图像。 
不能为空，推荐使用中文。最多可传1024个 utf-8 字符。
        :type Prompt: str
        :param _NegativePrompt: 反向提示词。 
推荐使用中文。最多可传1024个 utf-8 字符。
        :type NegativePrompt: str
        :param _Style: 绘画风格。
请在 [混元生图风格列表](https://cloud.tencent.com/document/product/1729/105846) 中选择期望的风格，传入风格编号。
不传默认不指定风格。
        :type Style: str
        :param _Resolution: 生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3），不传默认使用1024:1024。
如果上传 ContentImage 参考图，分辨率仅支持：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1），不传将自动适配分辨率。如果参考图被用于做风格转换，将生成保持原图长宽比例且长边为1024的图片，指定的分辨率不生效。
        :type Resolution: str
        :param _Num: 图片生成数量。
支持1 ~ 4张，默认生成1张。
        :type Num: int
        :param _Clarity: 超分选项，默认不做超分，可选开启。
 x2：2倍超分
 x4：4倍超分
在 Resolution 的基础上按比例提高分辨率，例如1024:1024开启2倍超分后将得到2048:2048。
        :type Clarity: str
        :param _ContentImage: 用于引导内容的参考图。
图片限制：单边分辨率小于5000，转成 Base64 字符串后小于 8MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。
        :type ContentImage: :class:`tencentcloud.hunyuan.v20230901.models.Image`
        :param _Revise: prompt 扩写开关。1为开启，0为关闭，不传默认开启。
开启扩写后，将自动扩写原始输入的 prompt 并使用扩写后的 prompt 生成图片，返回生成图片结果时将一并返回扩写后的 prompt 文本。
如果关闭扩写，将直接使用原始输入的 prompt 生成图片。如果上传了参考图，扩写关闭不生效，将保持开启。
建议开启，在多数场景下可提升生成图片效果、丰富生成图片细节。
        :type Revise: int
        :param _Seed: 随机种子，默认随机。
不传：随机种子生成。
正数：固定种子生成。
扩写开启时固定种子不生效，将保持随机。
        :type Seed: int
        :param _LogoAdd: 为生成结果图添加显式水印标识的开关，默认为1。  
1：添加。  
0：不添加。  
其他数值：默认按1处理。  
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        """
        self._Prompt = None
        self._NegativePrompt = None
        self._Style = None
        self._Resolution = None
        self._Num = None
        self._Clarity = None
        self._ContentImage = None
        self._Revise = None
        self._Seed = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        """文本描述。 
算法将根据输入的文本智能生成与之相关的图像。 
不能为空，推荐使用中文。最多可传1024个 utf-8 字符。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        """反向提示词。 
推荐使用中文。最多可传1024个 utf-8 字符。
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Style(self):
        """绘画风格。
请在 [混元生图风格列表](https://cloud.tencent.com/document/product/1729/105846) 中选择期望的风格，传入风格编号。
不传默认不指定风格。
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Resolution(self):
        """生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3），不传默认使用1024:1024。
如果上传 ContentImage 参考图，分辨率仅支持：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1），不传将自动适配分辨率。如果参考图被用于做风格转换，将生成保持原图长宽比例且长边为1024的图片，指定的分辨率不生效。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Num(self):
        """图片生成数量。
支持1 ~ 4张，默认生成1张。
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Clarity(self):
        """超分选项，默认不做超分，可选开启。
 x2：2倍超分
 x4：4倍超分
在 Resolution 的基础上按比例提高分辨率，例如1024:1024开启2倍超分后将得到2048:2048。
        :rtype: str
        """
        return self._Clarity

    @Clarity.setter
    def Clarity(self, Clarity):
        self._Clarity = Clarity

    @property
    def ContentImage(self):
        """用于引导内容的参考图。
图片限制：单边分辨率小于5000，转成 Base64 字符串后小于 8MB，格式支持 jpg、jpeg、png、bmp、tiff、webp。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.Image`
        """
        return self._ContentImage

    @ContentImage.setter
    def ContentImage(self, ContentImage):
        self._ContentImage = ContentImage

    @property
    def Revise(self):
        """prompt 扩写开关。1为开启，0为关闭，不传默认开启。
开启扩写后，将自动扩写原始输入的 prompt 并使用扩写后的 prompt 生成图片，返回生成图片结果时将一并返回扩写后的 prompt 文本。
如果关闭扩写，将直接使用原始输入的 prompt 生成图片。如果上传了参考图，扩写关闭不生效，将保持开启。
建议开启，在多数场景下可提升生成图片效果、丰富生成图片细节。
        :rtype: int
        """
        return self._Revise

    @Revise.setter
    def Revise(self, Revise):
        self._Revise = Revise

    @property
    def Seed(self):
        """随机种子，默认随机。
不传：随机种子生成。
正数：固定种子生成。
扩写开启时固定种子不生效，将保持随机。
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def LogoAdd(self):
        """为生成结果图添加显式水印标识的开关，默认为1。  
1：添加。  
0：不添加。  
其他数值：默认按1处理。  
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        """标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Style = params.get("Style")
        self._Resolution = params.get("Resolution")
        self._Num = params.get("Num")
        self._Clarity = params.get("Clarity")
        if params.get("ContentImage") is not None:
            self._ContentImage = Image()
            self._ContentImage._deserialize(params.get("ContentImage"))
        self._Revise = params.get("Revise")
        self._Seed = params.get("Seed")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanImageJobResponse(AbstractModel):
    """SubmitHunyuanImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """任务 ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHunyuanTo3DJobRequest(AbstractModel):
    """SubmitHunyuanTo3DJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 3D内容的描述，中文正向提示词。最多支持200个 utf-8 字符，ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type Prompt: str
        :param _ImageBase64: 输入图 Base64 数据。最多支持200个 utf-8 字符，ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type ImageBase64: str
        :param _ImageUrl: 输入图Url。最多支持200个 utf-8 字符，ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :type ImageUrl: str
        :param _Num: 生成数量。默认1，当前限制只能为1。
        :type Num: int
        """
        self._Prompt = None
        self._ImageBase64 = None
        self._ImageUrl = None
        self._Num = None

    @property
    def Prompt(self):
        """3D内容的描述，中文正向提示词。最多支持200个 utf-8 字符，ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def ImageBase64(self):
        """输入图 Base64 数据。最多支持200个 utf-8 字符，ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def ImageUrl(self):
        """输入图Url。最多支持200个 utf-8 字符，ImageBase64、ImageUrl和 Prompt必填其一，且Prompt和ImageBase64/ImageUrl不能同时存在。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Num(self):
        """生成数量。默认1，当前限制只能为1。
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._ImageBase64 = params.get("ImageBase64")
        self._ImageUrl = params.get("ImageUrl")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanTo3DJobResponse(AbstractModel):
    """SubmitHunyuanTo3DJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务id
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        """任务id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class TextToImageLiteRequest(AbstractModel):
    """TextToImageLite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本描述。
算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。
不能为空，推荐使用中文。最多可传256个 utf-8 字符。
        :type Prompt: str
        :param _NegativePrompt: 反向文本描述。
用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。
推荐使用中文。最多可传256个 utf-8 字符。
        :type NegativePrompt: str
        :param _Style: 绘画风格。
请在 [文生图轻量版风格列表](https://cloud.tencent.com/document/product/1729/108992) 中选择期望的风格，传入风格编号。不传默认使用201（日系动漫风格）。
        :type Style: str
        :param _Resolution: 生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3）、1080:1920（9:16）、1920:1080（16:9），不传默认使用768:768。
        :type Resolution: str
        :param _LogoAdd: 为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按0处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        :param _RspImgType: 返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。
        :type RspImgType: str
        """
        self._Prompt = None
        self._NegativePrompt = None
        self._Style = None
        self._Resolution = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def Prompt(self):
        """文本描述。
算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。
不能为空，推荐使用中文。最多可传256个 utf-8 字符。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        """反向文本描述。
用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。
推荐使用中文。最多可传256个 utf-8 字符。
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Style(self):
        """绘画风格。
请在 [文生图轻量版风格列表](https://cloud.tencent.com/document/product/1729/108992) 中选择期望的风格，传入风格编号。不传默认使用201（日系动漫风格）。
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Resolution(self):
        """生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3）、1080:1920（9:16）、1920:1080（16:9），不传默认使用768:768。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        """为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按0处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        """标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        """返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。
        :rtype: str
        """
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Style = params.get("Style")
        self._Resolution = params.get("Resolution")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageLiteResponse(AbstractModel):
    """TextToImageLite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 根据入参 RspImgType 填入不同，返回不同的内容。
如果传入 base64 则返回生成图 Base64 编码。
如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        """根据入参 RspImgType 填入不同，返回不同的内容。
如果传入 base64 则返回生成图 Base64 编码。
如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。
        :rtype: str
        """
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class ThreadAdditionalMessage(AbstractModel):
    """会话额外消息

    """

    def __init__(self):
        r"""
        :param _Role: 角色
        :type Role: str
        :param _Content: 内容
        :type Content: str
        :param _Attachments: 附件
注意：此字段可能返回 null，表示取不到有效值。
        :type Attachments: list of ThreadMessageAttachmentObject
        """
        self._Role = None
        self._Content = None
        self._Attachments = None

    @property
    def Role(self):
        """角色
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Attachments(self):
        """附件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ThreadMessageAttachmentObject
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        if params.get("Attachments") is not None:
            self._Attachments = []
            for item in params.get("Attachments"):
                obj = ThreadMessageAttachmentObject()
                obj._deserialize(item)
                self._Attachments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThreadMessage(AbstractModel):
    """会话消息

    """

    def __init__(self):
        r"""
        :param _ID: 消息 ID
        :type ID: str
        :param _Object: 对象类型
        :type Object: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: int
        :param _ThreadID: 会话 ID
        :type ThreadID: str
        :param _Status: 状态，处理中 in_progress，已完成 completed，未完成 incomplete。 
        :type Status: str
        :param _InCompleteDetails: 未完成原因
注意：此字段可能返回 null，表示取不到有效值。
        :type InCompleteDetails: :class:`tencentcloud.hunyuan.v20230901.models.ThreadMessageInCompleteDetailsObject`
        :param _CompletedAt: 完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CompletedAt: int
        :param _InCompleteAt: 未完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InCompleteAt: int
        :param _Role: 角色
        :type Role: str
        :param _Content: 内容
        :type Content: str
        :param _AssistantID: 助手 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AssistantID: str
        :param _RunID: 运行 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RunID: str
        :param _Attachments: 附件
注意：此字段可能返回 null，表示取不到有效值。
        :type Attachments: list of ThreadMessageAttachmentObject
        """
        self._ID = None
        self._Object = None
        self._CreatedAt = None
        self._ThreadID = None
        self._Status = None
        self._InCompleteDetails = None
        self._CompletedAt = None
        self._InCompleteAt = None
        self._Role = None
        self._Content = None
        self._AssistantID = None
        self._RunID = None
        self._Attachments = None

    @property
    def ID(self):
        """消息 ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Object(self):
        """对象类型
        :rtype: str
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def CreatedAt(self):
        """创建时间
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def ThreadID(self):
        """会话 ID
        :rtype: str
        """
        return self._ThreadID

    @ThreadID.setter
    def ThreadID(self, ThreadID):
        self._ThreadID = ThreadID

    @property
    def Status(self):
        """状态，处理中 in_progress，已完成 completed，未完成 incomplete。 
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InCompleteDetails(self):
        """未完成原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ThreadMessageInCompleteDetailsObject`
        """
        return self._InCompleteDetails

    @InCompleteDetails.setter
    def InCompleteDetails(self, InCompleteDetails):
        self._InCompleteDetails = InCompleteDetails

    @property
    def CompletedAt(self):
        """完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CompletedAt

    @CompletedAt.setter
    def CompletedAt(self, CompletedAt):
        self._CompletedAt = CompletedAt

    @property
    def InCompleteAt(self):
        """未完成时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InCompleteAt

    @InCompleteAt.setter
    def InCompleteAt(self, InCompleteAt):
        self._InCompleteAt = InCompleteAt

    @property
    def Role(self):
        """角色
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def AssistantID(self):
        """助手 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AssistantID

    @AssistantID.setter
    def AssistantID(self, AssistantID):
        self._AssistantID = AssistantID

    @property
    def RunID(self):
        """运行 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RunID

    @RunID.setter
    def RunID(self, RunID):
        self._RunID = RunID

    @property
    def Attachments(self):
        """附件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ThreadMessageAttachmentObject
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Object = params.get("Object")
        self._CreatedAt = params.get("CreatedAt")
        self._ThreadID = params.get("ThreadID")
        self._Status = params.get("Status")
        if params.get("InCompleteDetails") is not None:
            self._InCompleteDetails = ThreadMessageInCompleteDetailsObject()
            self._InCompleteDetails._deserialize(params.get("InCompleteDetails"))
        self._CompletedAt = params.get("CompletedAt")
        self._InCompleteAt = params.get("InCompleteAt")
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._AssistantID = params.get("AssistantID")
        self._RunID = params.get("RunID")
        if params.get("Attachments") is not None:
            self._Attachments = []
            for item in params.get("Attachments"):
                obj = ThreadMessageAttachmentObject()
                obj._deserialize(item)
                self._Attachments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThreadMessageAttachmentObject(AbstractModel):
    """会话消息附件

    """

    def __init__(self):
        r"""
        :param _FileID: 文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FileID: str
        """
        self._FileID = None

    @property
    def FileID(self):
        """文件 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileID

    @FileID.setter
    def FileID(self, FileID):
        self._FileID = FileID


    def _deserialize(self, params):
        self._FileID = params.get("FileID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThreadMessageInCompleteDetailsObject(AbstractModel):
    """会话消息未完成原因

    """

    def __init__(self):
        r"""
        :param _Reason: 会话消息未完成原因
        :type Reason: str
        """
        self._Reason = None

    @property
    def Reason(self):
        """会话消息未完成原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThreadToolResources(AbstractModel):
    """在会话中提供给助手工具的一系列资源。不同类型的工具会有各自对应的资源。比如代码解释器需要一个文件 ID 的列表，而文件搜索工具则需要一个向量存储 ID 的列表。

    """

    def __init__(self):
        r"""
        :param _CodeInterpreter: 文件 ID 列表
        :type CodeInterpreter: list of str
        :param _VectorStoreIDs: 向量存储 ID 列表
        :type VectorStoreIDs: list of str
        """
        self._CodeInterpreter = None
        self._VectorStoreIDs = None

    @property
    def CodeInterpreter(self):
        """文件 ID 列表
        :rtype: list of str
        """
        return self._CodeInterpreter

    @CodeInterpreter.setter
    def CodeInterpreter(self, CodeInterpreter):
        self._CodeInterpreter = CodeInterpreter

    @property
    def VectorStoreIDs(self):
        """向量存储 ID 列表
        :rtype: list of str
        """
        return self._VectorStoreIDs

    @VectorStoreIDs.setter
    def VectorStoreIDs(self, VectorStoreIDs):
        self._VectorStoreIDs = VectorStoreIDs


    def _deserialize(self, params):
        self._CodeInterpreter = params.get("CodeInterpreter")
        self._VectorStoreIDs = params.get("VectorStoreIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Timeline(AbstractModel):
    """时间线

    """

    def __init__(self):
        r"""
        :param _Title: 标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Datetime: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Datetime: str
        :param _Url: 相关网页链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self._Title = None
        self._Datetime = None
        self._Url = None

    @property
    def Title(self):
        """标题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Datetime(self):
        """时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Datetime

    @Datetime.setter
    def Datetime(self, Datetime):
        self._Datetime = Datetime

    @property
    def Url(self):
        """相关网页链接
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Datetime = params.get("Datetime")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tool(AbstractModel):
    """用户指定模型使用的工具

    """

    def __init__(self):
        r"""
        :param _Type: 工具类型，当前只支持function
        :type Type: str
        :param _Function: 具体要调用的function
        :type Function: :class:`tencentcloud.hunyuan.v20230901.models.ToolFunction`
        """
        self._Type = None
        self._Function = None

    @property
    def Type(self):
        """工具类型，当前只支持function
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Function(self):
        """具体要调用的function
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ToolFunction`
        """
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Function") is not None:
            self._Function = ToolFunction()
            self._Function._deserialize(params.get("Function"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolCall(AbstractModel):
    """模型生成的工具调用

    """

    def __init__(self):
        r"""
        :param _Id: 工具调用id
        :type Id: str
        :param _Type: 工具调用类型，当前只支持function
        :type Type: str
        :param _Function: 具体的function调用
        :type Function: :class:`tencentcloud.hunyuan.v20230901.models.ToolCallFunction`
        :param _Index: 索引值
        :type Index: int
        """
        self._Id = None
        self._Type = None
        self._Function = None
        self._Index = None

    @property
    def Id(self):
        """工具调用id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """工具调用类型，当前只支持function
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Function(self):
        """具体的function调用
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ToolCallFunction`
        """
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function

    @property
    def Index(self):
        """索引值
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        if params.get("Function") is not None:
            self._Function = ToolCallFunction()
            self._Function._deserialize(params.get("Function"))
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolCallFunction(AbstractModel):
    """具体的function调用

    """

    def __init__(self):
        r"""
        :param _Name: function名称
        :type Name: str
        :param _Arguments: function参数，一般为json字符串
        :type Arguments: str
        """
        self._Name = None
        self._Arguments = None

    @property
    def Name(self):
        """function名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Arguments(self):
        """function参数，一般为json字符串
        :rtype: str
        """
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Arguments = params.get("Arguments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolFunction(AbstractModel):
    """function定义

    """

    def __init__(self):
        r"""
        :param _Name: function名称，只能包含a-z，A-Z，0-9，\_或-
        :type Name: str
        :param _Parameters: function参数，一般为json字符串
        :type Parameters: str
        :param _Description: function的简单描述
        :type Description: str
        """
        self._Name = None
        self._Parameters = None
        self._Description = None

    @property
    def Name(self):
        """function名称，只能包含a-z，A-Z，0-9，\_或-
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Parameters(self):
        """function参数，一般为json字符串
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Description(self):
        """function的简单描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Parameters = params.get("Parameters")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationChoice(AbstractModel):
    """翻译接口返回的回复，支持多个

    """

    def __init__(self):
        r"""
        :param _FinishReason: 结束标志位，可能为 stop、 sensitive。
stop 表示输出正常结束。
sensitive 只在开启流式输出审核时会出现，表示安全审核未通过。
        :type FinishReason: str
        :param _Index: 索引值，流式调用时使用该字段。
        :type Index: int
        :param _Delta: 增量返回值，流式调用时使用该字段。
        :type Delta: :class:`tencentcloud.hunyuan.v20230901.models.TranslationDelta`
        :param _Message: 返回值，非流式调用时使用该字段。
        :type Message: :class:`tencentcloud.hunyuan.v20230901.models.TranslationMessage`
        """
        self._FinishReason = None
        self._Index = None
        self._Delta = None
        self._Message = None

    @property
    def FinishReason(self):
        """结束标志位，可能为 stop、 sensitive。
stop 表示输出正常结束。
sensitive 只在开启流式输出审核时会出现，表示安全审核未通过。
        :rtype: str
        """
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def Index(self):
        """索引值，流式调用时使用该字段。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Delta(self):
        """增量返回值，流式调用时使用该字段。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.TranslationDelta`
        """
        return self._Delta

    @Delta.setter
    def Delta(self, Delta):
        self._Delta = Delta

    @property
    def Message(self):
        """返回值，非流式调用时使用该字段。
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.TranslationMessage`
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        self._Index = params.get("Index")
        if params.get("Delta") is not None:
            self._Delta = TranslationDelta()
            self._Delta._deserialize(params.get("Delta"))
        if params.get("Message") is not None:
            self._Message = TranslationMessage()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationDelta(AbstractModel):
    """翻译接口返回的内容（流式返回）

    """

    def __init__(self):
        r"""
        :param _Role: 角色名称。
        :type Role: str
        :param _Content: 内容详情。
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        """角色名称。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """内容详情。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranslationMessage(AbstractModel):
    """翻译接口会话内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色，可选值包括 system、user、assistant、 tool。
        :type Role: str
        :param _Content: 文本内容
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        """角色，可选值包括 system、user、assistant、 tool。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """文本内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    """Token 数量

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入 Token 数量。
        :type PromptTokens: int
        :param _CompletionTokens: 输出 Token 数量。
        :type CompletionTokens: int
        :param _TotalTokens: 总 Token 数量。
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._CompletionTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        """输入 Token 数量。
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        """输出 Token 数量。
        :rtype: int
        """
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        """总 Token 数量。
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PromptTokens = params.get("PromptTokens")
        self._CompletionTokens = params.get("CompletionTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        