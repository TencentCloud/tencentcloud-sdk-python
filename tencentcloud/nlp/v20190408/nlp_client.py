# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def AutoSummarization(self, request):
        """利用人工智能算法，自动抽取文本中的关键信息并生成指定长度的文本摘要。可用于新闻标题生成、科技文献摘要生成和商品评论摘要等。

        :param request: 调用AutoSummarization所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AutoSummarization", params)
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


    def ContentApproval(self, request):
        """文本审核接口能够识别文本信息中的色情、政治等有害内容，帮助用户及时、精准地防范违规风险，可用于内容审核、敏感信息过滤、舆情监控等场景。

        该功能基于10万级大规模敏感词库，结合多种文本对抗方法、政策权威指令等，并运用了深度学习技术，高效识别高危有害内容。同时我们会根据大规模语料和实时反误杀系统，不断更新迭代，确保效果持续提升。

        文本审核接口目前提供以下三个功能：

        1、文本恶意级别：将文本分为3个级别，包括正常、恶意、可疑送审；

        2、文本恶意类型：把文本分为9个类别，包括正常、政治、色情、辱骂/低俗、暴恐/毒品、广告/灌水、迷信/邪教、其他违法、综合；

        3、恶意关键词：文本中所有涉嫌恶意的关键词。

        :param request: 调用ContentApproval所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.ContentApprovalRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ContentApprovalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ContentApproval", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ContentApprovalResponse()
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

        :param request: 调用DependencyParsing所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DependencyParsing", params)
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


    def KeywordsExtraction(self, request):
        """基于关键词提取平台，通过对文本内容进行深度分析，提取出文本内容中的关键信息，为用户实现诸如新闻内容关键词自动提取、评论关键词提取等提供基础服务。

        :param request: 调用KeywordsExtraction所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("KeywordsExtraction", params)
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

        3、命名实体识别：快速识别文本中的实体，例如人名、地名、机构名、时间日期等。

        所有的功能均基于千亿级大规模互联网语料进行持续迭代更新，以保证效果不断提升，用户无需担心新词发现、歧义消除、调用性能等问题。目前词法分析已经在泛互联网、金融、政务等不同垂直领域提供业务支持，并取得良好的效果。

        :param request: 调用LexicalAnalysis所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LexicalAnalysis", params)
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


    def SensitiveWordsRecognition(self, request):
        """敏感词识别接口能够识别出文本中的所有敏感词，帮助用户及时、精准地防范违规风险，广泛用于各种高危涉敏场景（如资讯、评论、聊天室）的敏感信息过滤。

        该功能基于10万级大规模敏感词库，结合多种文本对抗方法、政策权威指令等，高效识别敏感词及其各类变种。同时我们会根据大规模语料和实时反误杀系统，不断更新迭代，确保效果持续提升。

        目前能够支持对政治、色情、辱骂/低俗、暴恐/毒品、广告/灌水、迷信/邪教、其他违法、综合等8大类敏感信息的识别。

        :param request: 调用SensitiveWordsRecognition所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.SensitiveWordsRecognitionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SensitiveWordsRecognitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SensitiveWordsRecognition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SensitiveWordsRecognitionResponse()
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

        该句向量服务由腾讯知文自然语言处理团队联合腾讯AI Lab共同打造，基于千亿级大规模互联网语料并采用AI Lab自研的DSG算法训练而成，在腾讯内部诸多业务的NLP任务上实测效果显著。

        :param request: 调用SentenceEmbedding所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentenceEmbedding", params)
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


    def SentenceSimilarity(self, request):
        """文本相似度接口能够基于深度学习技术来计算两个输入文本的相似度，相似度数值越大的两个文本在语义上越相似。目前仅支持短文本的相似度计算，长文本的相似度计算也即将推出。

        鉴于文本相似度是一个应用非常广泛的功能，腾讯知文自然语言处理团队在深度神经网络模型的基础上，专门针对文本相似任务进行了优化，并持续迭代更新。基于文本相似度，可以轻松实现诸如文本去重、相似推荐等功能。

        :param request: 调用SentenceSimilarity所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentenceSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentenceSimilarityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentenceSimilarity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentenceSimilarityResponse()
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

        该功能基于基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升。

        :param request: 调用SentimentAnalysis所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentimentAnalysis", params)
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

        :param request: 调用SimilarWords所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SimilarWords", params)
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

        该功能基于基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升。

        目前已提供：

        - 通用领域分类体系，包括15个分类类目，分别是汽车、科技、健康、体育、旅行、教育、职业、文化、军事、房产、娱乐、女性、奥运、财经以及其他，适用于通用的场景。

        - 新闻领域分类体系，包括37个一级分类类目，285个二级分类，已应用于腾讯新闻的文章分类。

        更多垂直领域的分类体系即将推出，敬请期待。

        :param request: 调用TextClassification所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextClassificationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextClassificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextClassification", params)
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
        """提供对中文文本的自动纠错功能，能够识别输入文本中的错误片段，定位错误并给出正确的文本结果。目前仅支持短文本的自动纠错，长文本的自动纠错也即将推出。

        此功能是基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升，是搜索引擎、语音识别、内容审核等功能更好运行的基础之一。

        :param request: 调用TextCorrection所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextCorrection", params)
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


    def WordEmbedding(self, request):
        """词向量接口能够将输入的词语映射成一个固定维度的词向量，用来表示这个词语的语义特征。词向量是很多自然语言处理技术的基础，能够显著提高它们的效果。

        该词向量服务由腾讯知文自然语言处理团队联合腾讯AI Lab共同打造。使用的词向量基于千亿级大规模互联网语料并采用AI Lab自研的DSG算法训练而成，开源的词向量包含800多万中文词汇，在覆盖率、新鲜度及准确性等三方面性能突出。

        腾讯AI Lab词向量相关资料：

        https://ai.tencent.com/ailab/zh/news/detial?id=22

        https://ai.tencent.com/ailab/nlp/embedding.html

        :param request: 调用WordEmbedding所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WordEmbedding", params)
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

        :param request: 调用WordSimilarity所需参数的结构体。
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WordSimilarity", params)
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