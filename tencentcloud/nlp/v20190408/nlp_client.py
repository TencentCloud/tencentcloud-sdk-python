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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.nlp.v20190408 import models


class NlpClient(AbstractClient):
    _apiVersion = '2019-04-08'
    _endpoint = 'nlp.tencentcloudapi.com'
    _service = 'nlp'


    def AutoSummarization(self, request):
        """利用人工智能算法，自动抽取文本中的关键信息并生成指定长度的文本摘要。可用于新闻标题生成、科技文献摘要生成和商品评论摘要等。

        :param request: Request instance for AutoSummarization.
        :type request: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AutoSummarization", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AutoSummarizationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChatBot(self, request):
        """闲聊服务基于腾讯领先的NLP引擎能力、数据运算能力和千亿级互联网语料数据的支持，同时集成了广泛的知识问答能力，可实现上百种自定义属性配置，以及儿童语言风格及说话方式，从而让聊天变得更睿智、简单和有趣。


        :param request: Request instance for ChatBot.
        :type request: :class:`tencentcloud.nlp.v20190408.models.ChatBotRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ChatBotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChatBot", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChatBotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDict(self, request):
        """根据指定的名称、描述创建自定义词库。

        :param request: Request instance for CreateDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.CreateDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.CreateDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDict", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDictResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWordItems(self, request):
        """向指定的词库中添加词条。

        :param request: Request instance for CreateWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.CreateWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.CreateWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWordItems", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWordItemsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDict(self, request):
        """删除自定义词库，会附带相应删除词库包含的所有词条。

        :param request: Request instance for DeleteDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DeleteDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DeleteDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDict", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDictResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWordItems(self, request):
        """用于删除自定义词库中的词条。

        :param request: Request instance for DeleteWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DeleteWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DeleteWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWordItems", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWordItemsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DependencyParsing(self, request):
        """句法依存分析接口能够分析出句子中词与词之间的相互依存关系，并揭示其句法结构，包括主谓关系、动宾关系、核心关系等等，可用于提取句子主干、提取句子核心词等，在机器翻译、自动问答、知识抽取等领域都有很好的应用。

        :param request: Request instance for DependencyParsing.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DependencyParsing", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DependencyParsingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDict(self, request):
        """根据id或名称查询自定义词库信息。

        :param request: Request instance for DescribeDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDict", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDictResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDicts(self, request):
        """返回属于当前用户的所有自定义词库列表。

        :param request: Request instance for DescribeDicts.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeDictsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeDictsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDicts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDictsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWordItems(self, request):
        """依据自定义词库的ID，查询对应的词条信息。

        :param request: Request instance for DescribeWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWordItems", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWordItemsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def KeywordsExtraction(self, request):
        """基于关键词提取平台，通过对文本内容进行深度分析，提取出文本内容中的关键信息，为用户实现诸如新闻内容关键词自动提取、评论关键词提取等提供基础服务。

        :param request: Request instance for KeywordsExtraction.
        :type request: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KeywordsExtraction", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.KeywordsExtractionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LexicalAnalysis(self, request):
        """词法分析接口提供以下三个功能：

        1、智能分词：将连续的自然语言文本，切分成具有语义合理性和完整性的词汇序列；

        2、词性标注：为每一个词附上对应的词性，例如名词、代词、形容词、动词等；

        3、命名实体识别：快速识别文本中的实体，例如人名、地名、机构名等。

        所有的功能均基于千亿级大规模互联网语料进行持续迭代更新，以保证效果不断提升，用户无需担心新词发现、歧义消除、调用性能等问题。目前词法分析已经在泛互联网、金融、政务等不同垂直领域提供业务支持，并取得良好的效果。

        :param request: Request instance for LexicalAnalysis.
        :type request: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LexicalAnalysis", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LexicalAnalysisResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchWordItems(self, request):
        """查询指定自定义词库中的词条是否存在。

        :param request: Request instance for SearchWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SearchWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SearchWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchWordItems", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchWordItemsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SentenceEmbedding(self, request):
        """句向量接口能够将输入的句子映射成一个固定维度的向量，用来表示这个句子的语义特征，可用于文本聚类、文本相似度、文本分类等任务，能够显著提高它们的效果。

        该句向量服务由腾讯云自然语言处理团队联合微信智言团队共同打造，基于千亿级大规模互联网语料并采用Bert等领先的深度神经网络模型训练而成，在腾讯内部诸多业务的NLP任务上实测效果显著。

        :param request: Request instance for SentenceEmbedding.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SentenceEmbedding", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentenceEmbeddingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SentimentAnalysis(self, request):
        """情感分析接口能够对带有情感色彩的主观性文本进行分析、处理、归纳和推理，识别出用户的情感倾向，是积极还是消极，并且提供各自概率。

        该功能基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升。

        :param request: Request instance for SentimentAnalysis.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SentimentAnalysis", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentimentAnalysisResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SimilarWords(self, request):
        """相似词接口能够基于同义词库及词向量技术，检索出与输入词语在语义上最相似的若干个词语，可广泛用于检索系统、问答系统、文档归档等场景。

        :param request: Request instance for SimilarWords.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SimilarWords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SimilarWordsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextClassification(self, request):
        """文本分类接口能够对用户输入的文本进行自动分类，将其映射到具体的类目上，用户只需要提供待分类的文本，而无需关注具体实现。

        该功能基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升。

        目前已提供：

        - 通用领域分类体系，二级分类，包括14个分类类目，分别是汽车、科技、健康、体育、旅行、教育、职业、文化、房产、娱乐、女性、奥运、财经以及其他，适用于通用的场景。

        :param request: Request instance for TextClassification.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextClassificationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextClassificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextClassification", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextClassificationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextCorrection(self, request):
        """提供对中文文本的自动纠错功能，能够识别输入文本中的错误片段，定位错误并给出正确的文本结果；支持长度不超过2000字符（含标点符号）的长文本纠错。

        此功能是基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升，是搜索引擎、语音识别、内容审核等功能更好运行的基础之一。

        :param request: Request instance for TextCorrection.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextCorrection", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextCorrectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextCorrectionPro(self, request):
        """提供对中文文本的自动纠错功能，能够识别输入文本中的错误片段，定位错误并给出正确的文本结果；支持长度不超过128字符（含标点符号）的长文本纠错。

        此功能是基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升，是搜索引擎、语音识别、内容审核等功能更好运行的基础之一。

        :param request: Request instance for TextCorrectionPro.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionProRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextCorrectionPro", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextCorrectionProResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextSimilarity(self, request):
        """句子相似度接口能够基于深度学习技术来计算一个源句子和多个目标句子的相似度，相似度分值越大的两个句子在语义上越相似。目前仅支持短文本（不超过500字符）的相似度计算，长文本的相似度计算也即将推出。

        鉴于句子相似度是一个应用非常广泛的功能，腾讯云自然语言处理团队在Bert等领先的深度神经网络模型的基础上，专门针对文本相似任务进行了优化，并持续迭代更新。基于句子相似度，可以轻松实现诸如文本去重、相似推荐等功能。

        接口将以句子数量为单位消耗资源包，而不是调用接口次数为单位。

        :param request: Request instance for TextSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextSimilarity", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextSimilarityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextSimilarityPro(self, request):
        """句子相似度接口能够基于深度学习技术来计算一个源句子和多个目标句子的相似度，相似度分值越大的两个句子在语义上越相似。目前仅支持短文本（不超过128字符）的相似度计算，长文本的相似度计算也即将推出。

        鉴于句子相似度是一个应用非常广泛的功能，腾讯云自然语言处理团队在Bert等领先的深度神经网络模型的基础上，专门针对文本相似任务进行了优化，并持续迭代更新。基于句子相似度，可以轻松实现诸如文本去重、相似推荐等功能。

        接口将以句子数量为单位消耗资源包，而不是调用接口次数为单位。

        :param request: Request instance for TextSimilarityPro.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityProRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextSimilarityPro", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextSimilarityProResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDict(self, request):
        """修改自定义词库元数据信息，包括名称、描述。

        :param request: Request instance for UpdateDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.UpdateDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.UpdateDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDict", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDictResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WordEmbedding(self, request):
        """词向量接口能够将输入的词语映射成一个固定维度的词向量，用来表示这个词语的语义特征。词向量是很多自然语言处理技术的基础，能够显著提高它们的效果。

        该词向量服务由腾讯知文自然语言处理团队联合腾讯AI Lab共同打造。使用的词向量基于千亿级大规模互联网语料并采用AI Lab自研的DSG算法训练而成，开源的词向量包含800多万中文词汇，在覆盖率、新鲜度及准确性等三方面性能突出。

        腾讯AI Lab词向量相关资料：

        https://ai.tencent.com/ailab/zh/news/detial?id=22

        https://ai.tencent.com/ailab/nlp/zh/embedding.html

        :param request: Request instance for WordEmbedding.
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WordEmbedding", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WordEmbeddingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WordSimilarity(self, request):
        """词相似度接口能够基于词向量技术来计算两个输入词语的余弦相似度，相似度数值越大的两个词语在语义上越相似。

        :param request: Request instance for WordSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WordSimilarity", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WordSimilarityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)