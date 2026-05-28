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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class DescribeIgOrderListRequest(AbstractModel):
    r"""DescribeIgOrderList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数目</p>
        :type PageSize: int
        :param _ProductType: <p>产品类型</p><p>枚举值：</p><ul><li>ig： 导诊</li><li>ipc： 预问诊</li></ul><p>默认值：ig</p>
        :type ProductType: str
        :param _OrderStatus: <p>订单状态</p><p>枚举值：</p><ul><li>0： 无状态</li><li>1： 未激活</li><li>2： 使用中</li><li>3： 暂停使用</li><li>4： 已到期</li><li>5： 已删除</li><li>6： 已失效</li></ul><p>默认值：0</p>
        :type OrderStatus: int
        :param _KeyWord: <p>搜索关键字</p>
        :type KeyWord: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._ProductType = None
        self._OrderStatus = None
        self._KeyWord = None

    @property
    def PageNumber(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数目</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProductType(self):
        r"""<p>产品类型</p><p>枚举值：</p><ul><li>ig： 导诊</li><li>ipc： 预问诊</li></ul><p>默认值：ig</p>
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def OrderStatus(self):
        r"""<p>订单状态</p><p>枚举值：</p><ul><li>0： 无状态</li><li>1： 未激活</li><li>2： 使用中</li><li>3： 暂停使用</li><li>4： 已到期</li><li>5： 已删除</li><li>6： 已失效</li></ul><p>默认值：0</p>
        :rtype: int
        """
        return self._OrderStatus

    @OrderStatus.setter
    def OrderStatus(self, OrderStatus):
        self._OrderStatus = OrderStatus

    @property
    def KeyWord(self):
        r"""<p>搜索关键字</p>
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ProductType = params.get("ProductType")
        self._OrderStatus = params.get("OrderStatus")
        self._KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIgOrderListResponse(AbstractModel):
    r"""DescribeIgOrderList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DrugCardInfo(AbstractModel):
    r"""药品卡片信息

    """

    def __init__(self):
        r"""
        :param _DrugId: 药品id
        :type DrugId: str
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _TradeName: 商品名称
        :type TradeName: str
        :param _Specification: 规格
        :type Specification: str
        :param _Manufacturer: 生产厂商
        :type Manufacturer: str
        :param _DrugRxType: 是否处方药，0:非处方药，1:处方药
        :type DrugRxType: int
        :param _DocUrl: 药品说明书URL
        :type DocUrl: str
        :param _IdentifySource: 识别来源，1:药品图片，2:用户输入
        :type IdentifySource: int
        """
        self._DrugId = None
        self._DrugName = None
        self._TradeName = None
        self._Specification = None
        self._Manufacturer = None
        self._DrugRxType = None
        self._DocUrl = None
        self._IdentifySource = None

    @property
    def DrugId(self):
        r"""药品id
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def TradeName(self):
        r"""商品名称
        :rtype: str
        """
        return self._TradeName

    @TradeName.setter
    def TradeName(self, TradeName):
        self._TradeName = TradeName

    @property
    def Specification(self):
        r"""规格
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Manufacturer(self):
        r"""生产厂商
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def DrugRxType(self):
        r"""是否处方药，0:非处方药，1:处方药
        :rtype: int
        """
        return self._DrugRxType

    @DrugRxType.setter
    def DrugRxType(self, DrugRxType):
        self._DrugRxType = DrugRxType

    @property
    def DocUrl(self):
        r"""药品说明书URL
        :rtype: str
        """
        return self._DocUrl

    @DocUrl.setter
    def DocUrl(self, DocUrl):
        self._DocUrl = DocUrl

    @property
    def IdentifySource(self):
        r"""识别来源，1:药品图片，2:用户输入
        :rtype: int
        """
        return self._IdentifySource

    @IdentifySource.setter
    def IdentifySource(self, IdentifySource):
        self._IdentifySource = IdentifySource


    def _deserialize(self, params):
        self._DrugId = params.get("DrugId")
        self._DrugName = params.get("DrugName")
        self._TradeName = params.get("TradeName")
        self._Specification = params.get("Specification")
        self._Manufacturer = params.get("Manufacturer")
        self._DrugRxType = params.get("DrugRxType")
        self._DocUrl = params.get("DocUrl")
        self._IdentifySource = params.get("IdentifySource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrugInstructionInfo(AbstractModel):
    r"""药品说明书信息

    """

    def __init__(self):
        r"""
        :param _DrugId: 药品id
        :type DrugId: str
        :param _DrugName: 药品名称
        :type DrugName: str
        :param _TradeName: 商品名称
        :type TradeName: str
        :param _Specification: 规格
        :type Specification: str
        :param _Manufacturer: 生产企业
        :type Manufacturer: str
        :param _DrugUsage: 用法用量
        :type DrugUsage: str
        :param _Indication: 适应症
        :type Indication: str
        :param _AdverseReaction: 不良反应
        :type AdverseReaction: str
        :param _DrugRxType: 是否处方药，0:非处方药，1:处方药
        :type DrugRxType: int
        :param _DocUrl: 药品说明书URL
        :type DocUrl: str
        """
        self._DrugId = None
        self._DrugName = None
        self._TradeName = None
        self._Specification = None
        self._Manufacturer = None
        self._DrugUsage = None
        self._Indication = None
        self._AdverseReaction = None
        self._DrugRxType = None
        self._DocUrl = None

    @property
    def DrugId(self):
        r"""药品id
        :rtype: str
        """
        return self._DrugId

    @DrugId.setter
    def DrugId(self, DrugId):
        self._DrugId = DrugId

    @property
    def DrugName(self):
        r"""药品名称
        :rtype: str
        """
        return self._DrugName

    @DrugName.setter
    def DrugName(self, DrugName):
        self._DrugName = DrugName

    @property
    def TradeName(self):
        r"""商品名称
        :rtype: str
        """
        return self._TradeName

    @TradeName.setter
    def TradeName(self, TradeName):
        self._TradeName = TradeName

    @property
    def Specification(self):
        r"""规格
        :rtype: str
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Manufacturer(self):
        r"""生产企业
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def DrugUsage(self):
        r"""用法用量
        :rtype: str
        """
        return self._DrugUsage

    @DrugUsage.setter
    def DrugUsage(self, DrugUsage):
        self._DrugUsage = DrugUsage

    @property
    def Indication(self):
        r"""适应症
        :rtype: str
        """
        return self._Indication

    @Indication.setter
    def Indication(self, Indication):
        self._Indication = Indication

    @property
    def AdverseReaction(self):
        r"""不良反应
        :rtype: str
        """
        return self._AdverseReaction

    @AdverseReaction.setter
    def AdverseReaction(self, AdverseReaction):
        self._AdverseReaction = AdverseReaction

    @property
    def DrugRxType(self):
        r"""是否处方药，0:非处方药，1:处方药
        :rtype: int
        """
        return self._DrugRxType

    @DrugRxType.setter
    def DrugRxType(self, DrugRxType):
        self._DrugRxType = DrugRxType

    @property
    def DocUrl(self):
        r"""药品说明书URL
        :rtype: str
        """
        return self._DocUrl

    @DocUrl.setter
    def DocUrl(self, DocUrl):
        self._DocUrl = DocUrl


    def _deserialize(self, params):
        self._DrugId = params.get("DrugId")
        self._DrugName = params.get("DrugName")
        self._TradeName = params.get("TradeName")
        self._Specification = params.get("Specification")
        self._Manufacturer = params.get("Manufacturer")
        self._DrugUsage = params.get("DrugUsage")
        self._Indication = params.get("Indication")
        self._AdverseReaction = params.get("AdverseReaction")
        self._DrugRxType = params.get("DrugRxType")
        self._DocUrl = params.get("DocUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLLMDiagnosisDrugChatRequest(AbstractModel):
    r"""GetLLMDiagnosisDrugChat请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PartnerId: <p>合作方ID</p>
        :type PartnerId: str
        :param _PartnerSecret: <p>合作方密钥</p>
        :type PartnerSecret: str
        :param _HospitalAppId: <p>医院应用ID</p>
        :type HospitalAppId: str
        :param _DialogueId: <p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :type DialogueId: str
        :param _Message: <p>本次问答用户输入的问题，（最大长度1000）</p>
        :type Message: str
        :param _ResultType: <p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :type ResultType: int
        :param _Prompt: <p>提示词</p>
        :type Prompt: str
        """
        self._PartnerId = None
        self._PartnerSecret = None
        self._HospitalAppId = None
        self._DialogueId = None
        self._Message = None
        self._ResultType = None
        self._Prompt = None

    @property
    def PartnerId(self):
        r"""<p>合作方ID</p>
        :rtype: str
        """
        return self._PartnerId

    @PartnerId.setter
    def PartnerId(self, PartnerId):
        self._PartnerId = PartnerId

    @property
    def PartnerSecret(self):
        r"""<p>合作方密钥</p>
        :rtype: str
        """
        return self._PartnerSecret

    @PartnerSecret.setter
    def PartnerSecret(self, PartnerSecret):
        self._PartnerSecret = PartnerSecret

    @property
    def HospitalAppId(self):
        r"""<p>医院应用ID</p>
        :rtype: str
        """
        return self._HospitalAppId

    @HospitalAppId.setter
    def HospitalAppId(self, HospitalAppId):
        self._HospitalAppId = HospitalAppId

    @property
    def DialogueId(self):
        r"""<p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :rtype: str
        """
        return self._DialogueId

    @DialogueId.setter
    def DialogueId(self, DialogueId):
        self._DialogueId = DialogueId

    @property
    def Message(self):
        r"""<p>本次问答用户输入的问题，（最大长度1000）</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ResultType(self):
        r"""<p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :rtype: int
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Prompt(self):
        r"""<p>提示词</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt


    def _deserialize(self, params):
        self._PartnerId = params.get("PartnerId")
        self._PartnerSecret = params.get("PartnerSecret")
        self._HospitalAppId = params.get("HospitalAppId")
        self._DialogueId = params.get("DialogueId")
        self._Message = params.get("Message")
        self._ResultType = params.get("ResultType")
        self._Prompt = params.get("Prompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLLMDiagnosisDrugChatResponse(AbstractModel):
    r"""GetLLMDiagnosisDrugChat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: <p>错误码，0成功，非0失败</p>
        :type Code: int
        :param _Message: <p>错误信息</p>
        :type Message: str
        :param _Data: <p>返回数据</p>
        :type Data: :class:`tencentcloud.ig.v20210518.models.LLMDiagnosisDrugData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""<p>错误码，0成功，非0失败</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""<p>返回数据</p>
        :rtype: :class:`tencentcloud.ig.v20210518.models.LLMDiagnosisDrugData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = LLMDiagnosisDrugData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetLLMDiagnosisDrugRequest(AbstractModel):
    r"""GetLLMDiagnosisDrug请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PartnerId: <p>合作方ID</p>
        :type PartnerId: str
        :param _PartnerSecret: <p>合作方密钥</p>
        :type PartnerSecret: str
        :param _HospitalAppId: <p>医院应用ID</p>
        :type HospitalAppId: str
        :param _DialogueId: <p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :type DialogueId: str
        :param _Message: <p>本次问答用户输入的问题，（最大长度1000，传了图片链接，此参数可为空）</p>
        :type Message: str
        :param _ImageUrl: <p>药品图片链接</p>
        :type ImageUrl: str
        :param _ResultType: <p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :type ResultType: int
        :param _Prompt: <p>提示词</p>
        :type Prompt: str
        """
        self._PartnerId = None
        self._PartnerSecret = None
        self._HospitalAppId = None
        self._DialogueId = None
        self._Message = None
        self._ImageUrl = None
        self._ResultType = None
        self._Prompt = None

    @property
    def PartnerId(self):
        r"""<p>合作方ID</p>
        :rtype: str
        """
        return self._PartnerId

    @PartnerId.setter
    def PartnerId(self, PartnerId):
        self._PartnerId = PartnerId

    @property
    def PartnerSecret(self):
        r"""<p>合作方密钥</p>
        :rtype: str
        """
        return self._PartnerSecret

    @PartnerSecret.setter
    def PartnerSecret(self, PartnerSecret):
        self._PartnerSecret = PartnerSecret

    @property
    def HospitalAppId(self):
        r"""<p>医院应用ID</p>
        :rtype: str
        """
        return self._HospitalAppId

    @HospitalAppId.setter
    def HospitalAppId(self, HospitalAppId):
        self._HospitalAppId = HospitalAppId

    @property
    def DialogueId(self):
        r"""<p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :rtype: str
        """
        return self._DialogueId

    @DialogueId.setter
    def DialogueId(self, DialogueId):
        self._DialogueId = DialogueId

    @property
    def Message(self):
        r"""<p>本次问答用户输入的问题，（最大长度1000，传了图片链接，此参数可为空）</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ImageUrl(self):
        r"""<p>药品图片链接</p>
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ResultType(self):
        r"""<p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :rtype: int
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Prompt(self):
        r"""<p>提示词</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt


    def _deserialize(self, params):
        self._PartnerId = params.get("PartnerId")
        self._PartnerSecret = params.get("PartnerSecret")
        self._HospitalAppId = params.get("HospitalAppId")
        self._DialogueId = params.get("DialogueId")
        self._Message = params.get("Message")
        self._ImageUrl = params.get("ImageUrl")
        self._ResultType = params.get("ResultType")
        self._Prompt = params.get("Prompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLLMDiagnosisDrugResponse(AbstractModel):
    r"""GetLLMDiagnosisDrug返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: <p>错误码，0成功，非0失败</p>
        :type Code: int
        :param _Message: <p>错误信息</p>
        :type Message: str
        :param _Data: <p>返回数据</p>
        :type Data: :class:`tencentcloud.ig.v20210518.models.LLMDiagnosisDrugData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""<p>错误码，0成功，非0失败</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""<p>返回数据</p>
        :rtype: :class:`tencentcloud.ig.v20210518.models.LLMDiagnosisDrugData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = LLMDiagnosisDrugData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetLLMDiagnosisHealthRequest(AbstractModel):
    r"""GetLLMDiagnosisHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PartnerId: <p>合作方ID</p>
        :type PartnerId: str
        :param _PartnerSecret: <p>合作方密钥</p>
        :type PartnerSecret: str
        :param _HospitalAppId: <p>医院应用ID</p>
        :type HospitalAppId: str
        :param _DialogueId: <p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :type DialogueId: str
        :param _Message: <p>本次问答用户输入的问题，（最大长度1000）</p>
        :type Message: str
        :param _ResultType: <p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :type ResultType: int
        :param _Sex: <p>性别，0:未知，1:男，2:女</p>
        :type Sex: int
        :param _Age: <p>年龄，0:未知，最大值：120</p>
        :type Age: int
        :param _RoundNumber: <p>追问轮数，-1:不追问；0:使用默认规则； 1-10:按指定轮数追问；（最大值10轮）； 默认：0</p>
        :type RoundNumber: int
        :param _OutputStructured: <p>是否追问结构化结果，0：否，1：是；</p>
        :type OutputStructured: int
        """
        self._PartnerId = None
        self._PartnerSecret = None
        self._HospitalAppId = None
        self._DialogueId = None
        self._Message = None
        self._ResultType = None
        self._Sex = None
        self._Age = None
        self._RoundNumber = None
        self._OutputStructured = None

    @property
    def PartnerId(self):
        r"""<p>合作方ID</p>
        :rtype: str
        """
        return self._PartnerId

    @PartnerId.setter
    def PartnerId(self, PartnerId):
        self._PartnerId = PartnerId

    @property
    def PartnerSecret(self):
        r"""<p>合作方密钥</p>
        :rtype: str
        """
        return self._PartnerSecret

    @PartnerSecret.setter
    def PartnerSecret(self, PartnerSecret):
        self._PartnerSecret = PartnerSecret

    @property
    def HospitalAppId(self):
        r"""<p>医院应用ID</p>
        :rtype: str
        """
        return self._HospitalAppId

    @HospitalAppId.setter
    def HospitalAppId(self, HospitalAppId):
        self._HospitalAppId = HospitalAppId

    @property
    def DialogueId(self):
        r"""<p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :rtype: str
        """
        return self._DialogueId

    @DialogueId.setter
    def DialogueId(self, DialogueId):
        self._DialogueId = DialogueId

    @property
    def Message(self):
        r"""<p>本次问答用户输入的问题，（最大长度1000）</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ResultType(self):
        r"""<p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :rtype: int
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Sex(self):
        r"""<p>性别，0:未知，1:男，2:女</p>
        :rtype: int
        """
        return self._Sex

    @Sex.setter
    def Sex(self, Sex):
        self._Sex = Sex

    @property
    def Age(self):
        r"""<p>年龄，0:未知，最大值：120</p>
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def RoundNumber(self):
        r"""<p>追问轮数，-1:不追问；0:使用默认规则； 1-10:按指定轮数追问；（最大值10轮）； 默认：0</p>
        :rtype: int
        """
        return self._RoundNumber

    @RoundNumber.setter
    def RoundNumber(self, RoundNumber):
        self._RoundNumber = RoundNumber

    @property
    def OutputStructured(self):
        r"""<p>是否追问结构化结果，0：否，1：是；</p>
        :rtype: int
        """
        return self._OutputStructured

    @OutputStructured.setter
    def OutputStructured(self, OutputStructured):
        self._OutputStructured = OutputStructured


    def _deserialize(self, params):
        self._PartnerId = params.get("PartnerId")
        self._PartnerSecret = params.get("PartnerSecret")
        self._HospitalAppId = params.get("HospitalAppId")
        self._DialogueId = params.get("DialogueId")
        self._Message = params.get("Message")
        self._ResultType = params.get("ResultType")
        self._Sex = params.get("Sex")
        self._Age = params.get("Age")
        self._RoundNumber = params.get("RoundNumber")
        self._OutputStructured = params.get("OutputStructured")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLLMDiagnosisHealthResponse(AbstractModel):
    r"""GetLLMDiagnosisHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: <p>错误码，0成功，非0失败</p>
        :type Code: int
        :param _Message: <p>错误信息</p>
        :type Message: str
        :param _Data: <p>返回数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ig.v20210518.models.LLMDiagnosisHealthData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""<p>错误码，0成功，非0失败</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""<p>返回数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ig.v20210518.models.LLMDiagnosisHealthData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = LLMDiagnosisHealthData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GetLLMReportInterpretationRequest(AbstractModel):
    r"""GetLLMReportInterpretation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PartnerId: <p>合作方ID</p>
        :type PartnerId: str
        :param _PartnerSecret: <p>合作方密钥</p>
        :type PartnerSecret: str
        :param _HospitalId: <p>接入医院id</p>
        :type HospitalId: str
        :param _DialogueId: <p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :type DialogueId: str
        :param _Message: <p>本次问答用户输入的问题</p>
        :type Message: str
        :param _ReportFileInfos: <p>报告文件信息</p>
        :type ReportFileInfos: list of ReportFileInfoReq
        :param _ResultType: <p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :type ResultType: int
        :param _Prompt: <p>报告解读提示词</p>
        :type Prompt: str
        :param _QaPrompt: <p>无报告问答提示词</p>
        :type QaPrompt: str
        """
        self._PartnerId = None
        self._PartnerSecret = None
        self._HospitalId = None
        self._DialogueId = None
        self._Message = None
        self._ReportFileInfos = None
        self._ResultType = None
        self._Prompt = None
        self._QaPrompt = None

    @property
    def PartnerId(self):
        r"""<p>合作方ID</p>
        :rtype: str
        """
        return self._PartnerId

    @PartnerId.setter
    def PartnerId(self, PartnerId):
        self._PartnerId = PartnerId

    @property
    def PartnerSecret(self):
        r"""<p>合作方密钥</p>
        :rtype: str
        """
        return self._PartnerSecret

    @PartnerSecret.setter
    def PartnerSecret(self, PartnerSecret):
        self._PartnerSecret = PartnerSecret

    @property
    def HospitalId(self):
        r"""<p>接入医院id</p>
        :rtype: str
        """
        return self._HospitalId

    @HospitalId.setter
    def HospitalId(self, HospitalId):
        self._HospitalId = HospitalId

    @property
    def DialogueId(self):
        r"""<p>对话ID，由接入方生成，相同对话ID会保持相同的上下文，接入方根据业务场景使用相同或新建对话ID（建议使用UUID值）</p><p>入参限制：长度限制10-50</p>
        :rtype: str
        """
        return self._DialogueId

    @DialogueId.setter
    def DialogueId(self, DialogueId):
        self._DialogueId = DialogueId

    @property
    def Message(self):
        r"""<p>本次问答用户输入的问题</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ReportFileInfos(self):
        r"""<p>报告文件信息</p>
        :rtype: list of ReportFileInfoReq
        """
        return self._ReportFileInfos

    @ReportFileInfos.setter
    def ReportFileInfos(self, ReportFileInfos):
        self._ReportFileInfos = ReportFileInfos

    @property
    def ResultType(self):
        r"""<p>返回类型：0:正常返回； 1:流式返回； 默认：0</p>
        :rtype: int
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def Prompt(self):
        r"""<p>报告解读提示词</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def QaPrompt(self):
        r"""<p>无报告问答提示词</p>
        :rtype: str
        """
        return self._QaPrompt

    @QaPrompt.setter
    def QaPrompt(self, QaPrompt):
        self._QaPrompt = QaPrompt


    def _deserialize(self, params):
        self._PartnerId = params.get("PartnerId")
        self._PartnerSecret = params.get("PartnerSecret")
        self._HospitalId = params.get("HospitalId")
        self._DialogueId = params.get("DialogueId")
        self._Message = params.get("Message")
        if params.get("ReportFileInfos") is not None:
            self._ReportFileInfos = []
            for item in params.get("ReportFileInfos"):
                obj = ReportFileInfoReq()
                obj._deserialize(item)
                self._ReportFileInfos.append(obj)
        self._ResultType = params.get("ResultType")
        self._Prompt = params.get("Prompt")
        self._QaPrompt = params.get("QaPrompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLLMReportInterpretationResponse(AbstractModel):
    r"""GetLLMReportInterpretation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: <p>错误码，0成功，非0失败</p>
        :type Code: int
        :param _Message: <p>错误信息</p>
        :type Message: str
        :param _Data: <p>返回数据</p>
        :type Data: :class:`tencentcloud.ig.v20210518.models.LLMReportInterpretationData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""<p>错误码，0成功，非0失败</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""<p>返回数据</p>
        :rtype: :class:`tencentcloud.ig.v20210518.models.LLMReportInterpretationData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = LLMReportInterpretationData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class GuessQuestion(AbstractModel):
    r"""猜你想问信息

    """

    def __init__(self):
        r"""
        :param _Title: 问题标题
        :type Title: str
        """
        self._Title = None

    @property
    def Title(self):
        r"""问题标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthFollowUpQuestion(AbstractModel):
    r"""症状自查追问问题

    """

    def __init__(self):
        r"""
        :param _PromptType: <p>追问类型</p>
        :type PromptType: str
        :param _Choices: <p>追问选项列表</p>
        :type Choices: list of str
        :param _QuestionType: <p>追问题型，单选或多选</p>
        :type QuestionType: str
        :param _SpecialType: <p>追问特殊类型，如部位题、时间题</p>
        :type SpecialType: str
        :param _Question: <p>追问问题内容</p>
        :type Question: str
        """
        self._PromptType = None
        self._Choices = None
        self._QuestionType = None
        self._SpecialType = None
        self._Question = None

    @property
    def PromptType(self):
        r"""<p>追问类型</p>
        :rtype: str
        """
        return self._PromptType

    @PromptType.setter
    def PromptType(self, PromptType):
        self._PromptType = PromptType

    @property
    def Choices(self):
        r"""<p>追问选项列表</p>
        :rtype: list of str
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def QuestionType(self):
        r"""<p>追问题型，单选或多选</p>
        :rtype: str
        """
        return self._QuestionType

    @QuestionType.setter
    def QuestionType(self, QuestionType):
        self._QuestionType = QuestionType

    @property
    def SpecialType(self):
        r"""<p>追问特殊类型，如部位题、时间题</p>
        :rtype: str
        """
        return self._SpecialType

    @SpecialType.setter
    def SpecialType(self, SpecialType):
        self._SpecialType = SpecialType

    @property
    def Question(self):
        r"""<p>追问问题内容</p>
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question


    def _deserialize(self, params):
        self._PromptType = params.get("PromptType")
        self._Choices = params.get("Choices")
        self._QuestionType = params.get("QuestionType")
        self._SpecialType = params.get("SpecialType")
        self._Question = params.get("Question")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightWordInfo(AbstractModel):
    r"""高亮词信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Type: 类型 1:疾病，2:检验/检查，3:药品，4:科室，5:自定义配置
        :type Type: int
        :param _JumpType: 跳转类型 h5:h5类型，mini_wx:微信小程序
        :type JumpType: str
        :param _JumpUrl: 跳转URL
        :type JumpUrl: str
        :param _JumpAppid: 跳转小程序Appid
        :type JumpAppid: str
        :param _JumpOriginId: 跳转小程序原始ID
        :type JumpOriginId: str
        """
        self._Name = None
        self._Type = None
        self._JumpType = None
        self._JumpUrl = None
        self._JumpAppid = None
        self._JumpOriginId = None

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""类型 1:疾病，2:检验/检查，3:药品，4:科室，5:自定义配置
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def JumpType(self):
        r"""跳转类型 h5:h5类型，mini_wx:微信小程序
        :rtype: str
        """
        return self._JumpType

    @JumpType.setter
    def JumpType(self, JumpType):
        self._JumpType = JumpType

    @property
    def JumpUrl(self):
        r"""跳转URL
        :rtype: str
        """
        return self._JumpUrl

    @JumpUrl.setter
    def JumpUrl(self, JumpUrl):
        self._JumpUrl = JumpUrl

    @property
    def JumpAppid(self):
        r"""跳转小程序Appid
        :rtype: str
        """
        return self._JumpAppid

    @JumpAppid.setter
    def JumpAppid(self, JumpAppid):
        self._JumpAppid = JumpAppid

    @property
    def JumpOriginId(self):
        r"""跳转小程序原始ID
        :rtype: str
        """
        return self._JumpOriginId

    @JumpOriginId.setter
    def JumpOriginId(self, JumpOriginId):
        self._JumpOriginId = JumpOriginId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._JumpType = params.get("JumpType")
        self._JumpUrl = params.get("JumpUrl")
        self._JumpAppid = params.get("JumpAppid")
        self._JumpOriginId = params.get("JumpOriginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LLMDiagnosisDrugData(AbstractModel):
    r"""大模型问药返回数据

    """

    def __init__(self):
        r"""
        :param _Content: <p>大模型返回问答内容</p>
        :type Content: str
        :param _Think: <p>大模型返回思考内容</p>
        :type Think: str
        :param _Sort: <p>序号，无业务含义，标识流式结果的序号</p>
        :type Sort: int
        :param _IsFinish: <p>流式输出结束标识，false:未结束，true:结束</p>
        :type IsFinish: bool
        :param _IsSensitive: <p>是否命中敏感词，false:否，true:是；</p>
        :type IsSensitive: bool
        :param _ReferResourceItems: <p>引用资料列表，流式输出方式，只在流式输出第一次返回；</p>
        :type ReferResourceItems: list of ReferResourceInfo
        :param _GuessQuestions: <p>猜你想问列表，流式输出方式，只在流式结束输出结果；</p>
        :type GuessQuestions: list of GuessQuestion
        :param _HighlightWords: <p>高亮词列表，流式输出方式在流式过程中输出结果。</p>
        :type HighlightWords: list of HighlightWordInfo
        :param _DrugList: <p>药品列表，流式输出方式，只在流式结束输出结果。</p>
        :type DrugList: list of StandardDrugCardInfo
        """
        self._Content = None
        self._Think = None
        self._Sort = None
        self._IsFinish = None
        self._IsSensitive = None
        self._ReferResourceItems = None
        self._GuessQuestions = None
        self._HighlightWords = None
        self._DrugList = None

    @property
    def Content(self):
        r"""<p>大模型返回问答内容</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Think(self):
        r"""<p>大模型返回思考内容</p>
        :rtype: str
        """
        return self._Think

    @Think.setter
    def Think(self, Think):
        self._Think = Think

    @property
    def Sort(self):
        r"""<p>序号，无业务含义，标识流式结果的序号</p>
        :rtype: int
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def IsFinish(self):
        r"""<p>流式输出结束标识，false:未结束，true:结束</p>
        :rtype: bool
        """
        return self._IsFinish

    @IsFinish.setter
    def IsFinish(self, IsFinish):
        self._IsFinish = IsFinish

    @property
    def IsSensitive(self):
        r"""<p>是否命中敏感词，false:否，true:是；</p>
        :rtype: bool
        """
        return self._IsSensitive

    @IsSensitive.setter
    def IsSensitive(self, IsSensitive):
        self._IsSensitive = IsSensitive

    @property
    def ReferResourceItems(self):
        r"""<p>引用资料列表，流式输出方式，只在流式输出第一次返回；</p>
        :rtype: list of ReferResourceInfo
        """
        return self._ReferResourceItems

    @ReferResourceItems.setter
    def ReferResourceItems(self, ReferResourceItems):
        self._ReferResourceItems = ReferResourceItems

    @property
    def GuessQuestions(self):
        r"""<p>猜你想问列表，流式输出方式，只在流式结束输出结果；</p>
        :rtype: list of GuessQuestion
        """
        return self._GuessQuestions

    @GuessQuestions.setter
    def GuessQuestions(self, GuessQuestions):
        self._GuessQuestions = GuessQuestions

    @property
    def HighlightWords(self):
        r"""<p>高亮词列表，流式输出方式在流式过程中输出结果。</p>
        :rtype: list of HighlightWordInfo
        """
        return self._HighlightWords

    @HighlightWords.setter
    def HighlightWords(self, HighlightWords):
        self._HighlightWords = HighlightWords

    @property
    def DrugList(self):
        r"""<p>药品列表，流式输出方式，只在流式结束输出结果。</p>
        :rtype: list of StandardDrugCardInfo
        """
        return self._DrugList

    @DrugList.setter
    def DrugList(self, DrugList):
        self._DrugList = DrugList


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Think = params.get("Think")
        self._Sort = params.get("Sort")
        self._IsFinish = params.get("IsFinish")
        self._IsSensitive = params.get("IsSensitive")
        if params.get("ReferResourceItems") is not None:
            self._ReferResourceItems = []
            for item in params.get("ReferResourceItems"):
                obj = ReferResourceInfo()
                obj._deserialize(item)
                self._ReferResourceItems.append(obj)
        if params.get("GuessQuestions") is not None:
            self._GuessQuestions = []
            for item in params.get("GuessQuestions"):
                obj = GuessQuestion()
                obj._deserialize(item)
                self._GuessQuestions.append(obj)
        if params.get("HighlightWords") is not None:
            self._HighlightWords = []
            for item in params.get("HighlightWords"):
                obj = HighlightWordInfo()
                obj._deserialize(item)
                self._HighlightWords.append(obj)
        if params.get("DrugList") is not None:
            self._DrugList = []
            for item in params.get("DrugList"):
                obj = StandardDrugCardInfo()
                obj._deserialize(item)
                self._DrugList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LLMDiagnosisHealthData(AbstractModel):
    r"""大模型症状自查返回数据

    """

    def __init__(self):
        r"""
        :param _Content: <p>大模型返回问答内容</p>
        :type Content: str
        :param _Think: <p>大模型返回思考内容</p>
        :type Think: str
        :param _Sort: <p>序号，无业务含义，标识流式结果的序号</p>
        :type Sort: int
        :param _IsFinish: <p>流式输出结束标识，false:未结束，true:结束</p>
        :type IsFinish: bool
        :param _IsSensitive: <p>是否命中敏感词，false:否，true:是；</p>
        :type IsSensitive: bool
        :param _Kind: <p>结果类型，0：正常结果，1：追问问题</p>
        :type Kind: int
        :param _RiskReminder: <p>风险提示</p>
        :type RiskReminder: str
        :param _ReferResourceItems: <p>引用资料列表，流式输出方式，只在流式输出第一次返回；</p>
        :type ReferResourceItems: list of ReferResourceInfo
        :param _GuessQuestions: <p>猜你想问列表，流式输出方式，只在流式结束输出结果；</p>
        :type GuessQuestions: list of GuessQuestion
        :param _HighlightWords: <p>高亮词列表，流式输出方式在流式过程中输出结果。</p>
        :type HighlightWords: list of HighlightWordInfo
        :param _FollowUpQuestions: <p>追问问题列表，流式输出方式，只在流式结束输出结果。只会在kind=1追问类型时有结果。</p>
        :type FollowUpQuestions: list of HealthFollowUpQuestion
        :param _DrugList: <p>药品列表，流式输出方式，只在流式结束输出结果。</p>
        :type DrugList: list of StandardDrugCardInfo
        """
        self._Content = None
        self._Think = None
        self._Sort = None
        self._IsFinish = None
        self._IsSensitive = None
        self._Kind = None
        self._RiskReminder = None
        self._ReferResourceItems = None
        self._GuessQuestions = None
        self._HighlightWords = None
        self._FollowUpQuestions = None
        self._DrugList = None

    @property
    def Content(self):
        r"""<p>大模型返回问答内容</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Think(self):
        r"""<p>大模型返回思考内容</p>
        :rtype: str
        """
        return self._Think

    @Think.setter
    def Think(self, Think):
        self._Think = Think

    @property
    def Sort(self):
        r"""<p>序号，无业务含义，标识流式结果的序号</p>
        :rtype: int
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def IsFinish(self):
        r"""<p>流式输出结束标识，false:未结束，true:结束</p>
        :rtype: bool
        """
        return self._IsFinish

    @IsFinish.setter
    def IsFinish(self, IsFinish):
        self._IsFinish = IsFinish

    @property
    def IsSensitive(self):
        r"""<p>是否命中敏感词，false:否，true:是；</p>
        :rtype: bool
        """
        return self._IsSensitive

    @IsSensitive.setter
    def IsSensitive(self, IsSensitive):
        self._IsSensitive = IsSensitive

    @property
    def Kind(self):
        r"""<p>结果类型，0：正常结果，1：追问问题</p>
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind

    @property
    def RiskReminder(self):
        r"""<p>风险提示</p>
        :rtype: str
        """
        return self._RiskReminder

    @RiskReminder.setter
    def RiskReminder(self, RiskReminder):
        self._RiskReminder = RiskReminder

    @property
    def ReferResourceItems(self):
        r"""<p>引用资料列表，流式输出方式，只在流式输出第一次返回；</p>
        :rtype: list of ReferResourceInfo
        """
        return self._ReferResourceItems

    @ReferResourceItems.setter
    def ReferResourceItems(self, ReferResourceItems):
        self._ReferResourceItems = ReferResourceItems

    @property
    def GuessQuestions(self):
        r"""<p>猜你想问列表，流式输出方式，只在流式结束输出结果；</p>
        :rtype: list of GuessQuestion
        """
        return self._GuessQuestions

    @GuessQuestions.setter
    def GuessQuestions(self, GuessQuestions):
        self._GuessQuestions = GuessQuestions

    @property
    def HighlightWords(self):
        r"""<p>高亮词列表，流式输出方式在流式过程中输出结果。</p>
        :rtype: list of HighlightWordInfo
        """
        return self._HighlightWords

    @HighlightWords.setter
    def HighlightWords(self, HighlightWords):
        self._HighlightWords = HighlightWords

    @property
    def FollowUpQuestions(self):
        r"""<p>追问问题列表，流式输出方式，只在流式结束输出结果。只会在kind=1追问类型时有结果。</p>
        :rtype: list of HealthFollowUpQuestion
        """
        return self._FollowUpQuestions

    @FollowUpQuestions.setter
    def FollowUpQuestions(self, FollowUpQuestions):
        self._FollowUpQuestions = FollowUpQuestions

    @property
    def DrugList(self):
        r"""<p>药品列表，流式输出方式，只在流式结束输出结果。</p>
        :rtype: list of StandardDrugCardInfo
        """
        return self._DrugList

    @DrugList.setter
    def DrugList(self, DrugList):
        self._DrugList = DrugList


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Think = params.get("Think")
        self._Sort = params.get("Sort")
        self._IsFinish = params.get("IsFinish")
        self._IsSensitive = params.get("IsSensitive")
        self._Kind = params.get("Kind")
        self._RiskReminder = params.get("RiskReminder")
        if params.get("ReferResourceItems") is not None:
            self._ReferResourceItems = []
            for item in params.get("ReferResourceItems"):
                obj = ReferResourceInfo()
                obj._deserialize(item)
                self._ReferResourceItems.append(obj)
        if params.get("GuessQuestions") is not None:
            self._GuessQuestions = []
            for item in params.get("GuessQuestions"):
                obj = GuessQuestion()
                obj._deserialize(item)
                self._GuessQuestions.append(obj)
        if params.get("HighlightWords") is not None:
            self._HighlightWords = []
            for item in params.get("HighlightWords"):
                obj = HighlightWordInfo()
                obj._deserialize(item)
                self._HighlightWords.append(obj)
        if params.get("FollowUpQuestions") is not None:
            self._FollowUpQuestions = []
            for item in params.get("FollowUpQuestions"):
                obj = HealthFollowUpQuestion()
                obj._deserialize(item)
                self._FollowUpQuestions.append(obj)
        if params.get("DrugList") is not None:
            self._DrugList = []
            for item in params.get("DrugList"):
                obj = StandardDrugCardInfo()
                obj._deserialize(item)
                self._DrugList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LLMReportInterpretationData(AbstractModel):
    r"""大模型症状自查返回数据

    """

    def __init__(self):
        r"""
        :param _Content: <p>大模型返回问答内容</p>
        :type Content: str
        :param _Think: <p>大模型返回思考内容</p>
        :type Think: str
        :param _Sort: <p>序号，无业务含义，标识流式结果的序号</p>
        :type Sort: int
        :param _IsFinish: <p>流式输出结束标识，false:未结束，true:结束</p>
        :type IsFinish: bool
        :param _IsSensitive: <p>是否命中敏感词，false:否，true:是；</p>
        :type IsSensitive: bool
        :param _IsSupportFile: <p>是否支持报告类型，false:否，true:是； 默认返回true，不支持的报告类型返回false</p>
        :type IsSupportFile: bool
        :param _ReportInfos: <p>返回的报告列表，和传入报告文件顺序一致</p>
        :type ReportInfos: list of ReportFileInfoRsp
        :param _ReferResourceItems: <p>引用资料列表，流式输出方式，只在流式输出第一次返回；</p>
        :type ReferResourceItems: list of ReferResourceInfo
        :param _GuessQuestions: <p>猜你想问列表，流式输出方式，只在流式结束输出结果；</p>
        :type GuessQuestions: list of GuessQuestion
        :param _HighlightWords: <p>高亮词列表，流式输出方式在流式过程中输出结果。</p>
        :type HighlightWords: list of HighlightWordInfo
        """
        self._Content = None
        self._Think = None
        self._Sort = None
        self._IsFinish = None
        self._IsSensitive = None
        self._IsSupportFile = None
        self._ReportInfos = None
        self._ReferResourceItems = None
        self._GuessQuestions = None
        self._HighlightWords = None

    @property
    def Content(self):
        r"""<p>大模型返回问答内容</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Think(self):
        r"""<p>大模型返回思考内容</p>
        :rtype: str
        """
        return self._Think

    @Think.setter
    def Think(self, Think):
        self._Think = Think

    @property
    def Sort(self):
        r"""<p>序号，无业务含义，标识流式结果的序号</p>
        :rtype: int
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def IsFinish(self):
        r"""<p>流式输出结束标识，false:未结束，true:结束</p>
        :rtype: bool
        """
        return self._IsFinish

    @IsFinish.setter
    def IsFinish(self, IsFinish):
        self._IsFinish = IsFinish

    @property
    def IsSensitive(self):
        r"""<p>是否命中敏感词，false:否，true:是；</p>
        :rtype: bool
        """
        return self._IsSensitive

    @IsSensitive.setter
    def IsSensitive(self, IsSensitive):
        self._IsSensitive = IsSensitive

    @property
    def IsSupportFile(self):
        r"""<p>是否支持报告类型，false:否，true:是； 默认返回true，不支持的报告类型返回false</p>
        :rtype: bool
        """
        return self._IsSupportFile

    @IsSupportFile.setter
    def IsSupportFile(self, IsSupportFile):
        self._IsSupportFile = IsSupportFile

    @property
    def ReportInfos(self):
        r"""<p>返回的报告列表，和传入报告文件顺序一致</p>
        :rtype: list of ReportFileInfoRsp
        """
        return self._ReportInfos

    @ReportInfos.setter
    def ReportInfos(self, ReportInfos):
        self._ReportInfos = ReportInfos

    @property
    def ReferResourceItems(self):
        r"""<p>引用资料列表，流式输出方式，只在流式输出第一次返回；</p>
        :rtype: list of ReferResourceInfo
        """
        return self._ReferResourceItems

    @ReferResourceItems.setter
    def ReferResourceItems(self, ReferResourceItems):
        self._ReferResourceItems = ReferResourceItems

    @property
    def GuessQuestions(self):
        r"""<p>猜你想问列表，流式输出方式，只在流式结束输出结果；</p>
        :rtype: list of GuessQuestion
        """
        return self._GuessQuestions

    @GuessQuestions.setter
    def GuessQuestions(self, GuessQuestions):
        self._GuessQuestions = GuessQuestions

    @property
    def HighlightWords(self):
        r"""<p>高亮词列表，流式输出方式在流式过程中输出结果。</p>
        :rtype: list of HighlightWordInfo
        """
        return self._HighlightWords

    @HighlightWords.setter
    def HighlightWords(self, HighlightWords):
        self._HighlightWords = HighlightWords


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Think = params.get("Think")
        self._Sort = params.get("Sort")
        self._IsFinish = params.get("IsFinish")
        self._IsSensitive = params.get("IsSensitive")
        self._IsSupportFile = params.get("IsSupportFile")
        if params.get("ReportInfos") is not None:
            self._ReportInfos = []
            for item in params.get("ReportInfos"):
                obj = ReportFileInfoRsp()
                obj._deserialize(item)
                self._ReportInfos.append(obj)
        if params.get("ReferResourceItems") is not None:
            self._ReferResourceItems = []
            for item in params.get("ReferResourceItems"):
                obj = ReferResourceInfo()
                obj._deserialize(item)
                self._ReferResourceItems.append(obj)
        if params.get("GuessQuestions") is not None:
            self._GuessQuestions = []
            for item in params.get("GuessQuestions"):
                obj = GuessQuestion()
                obj._deserialize(item)
                self._GuessQuestions.append(obj)
        if params.get("HighlightWords") is not None:
            self._HighlightWords = []
            for item in params.get("HighlightWords"):
                obj = HighlightWordInfo()
                obj._deserialize(item)
                self._HighlightWords.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDrugInstructionsRequest(AbstractModel):
    r"""QueryDrugInstructions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PartnerId: <p>合作方ID</p>
        :type PartnerId: str
        :param _PartnerSecret: <p>合作方密钥</p>
        :type PartnerSecret: str
        :param _HospitalAppId: <p>医院应用ID</p>
        :type HospitalAppId: str
        :param _Message: <p>本次问答用户输入的问题，（最大长度1000）</p>
        :type Message: str
        """
        self._PartnerId = None
        self._PartnerSecret = None
        self._HospitalAppId = None
        self._Message = None

    @property
    def PartnerId(self):
        r"""<p>合作方ID</p>
        :rtype: str
        """
        return self._PartnerId

    @PartnerId.setter
    def PartnerId(self, PartnerId):
        self._PartnerId = PartnerId

    @property
    def PartnerSecret(self):
        r"""<p>合作方密钥</p>
        :rtype: str
        """
        return self._PartnerSecret

    @PartnerSecret.setter
    def PartnerSecret(self, PartnerSecret):
        self._PartnerSecret = PartnerSecret

    @property
    def HospitalAppId(self):
        r"""<p>医院应用ID</p>
        :rtype: str
        """
        return self._HospitalAppId

    @HospitalAppId.setter
    def HospitalAppId(self, HospitalAppId):
        self._HospitalAppId = HospitalAppId

    @property
    def Message(self):
        r"""<p>本次问答用户输入的问题，（最大长度1000）</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._PartnerId = params.get("PartnerId")
        self._PartnerSecret = params.get("PartnerSecret")
        self._HospitalAppId = params.get("HospitalAppId")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDrugInstructionsResponse(AbstractModel):
    r"""QueryDrugInstructions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: <p>错误码，0成功，非0失败</p>
        :type Code: int
        :param _Message: <p>错误信息</p>
        :type Message: str
        :param _Data: <p>返回数据</p>
        :type Data: list of StandardDrugInstructionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Message = None
        self._Data = None
        self._RequestId = None

    @property
    def Code(self):
        r"""<p>错误码，0成功，非0失败</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Data(self):
        r"""<p>返回数据</p>
        :rtype: list of StandardDrugInstructionInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = StandardDrugInstructionInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ReferResourceInfo(AbstractModel):
    r"""引用资料信息

    """

    def __init__(self):
        r"""
        :param _Title: 资料标题
        :type Title: str
        :param _Type: 资料来源类型，1:问答库，2:文档，3:医典百科，4:临床指南，5:药品说明书
        :type Type: str
        :param _Url: 资料详情链接
        :type Url: str
        """
        self._Title = None
        self._Type = None
        self._Url = None

    @property
    def Title(self):
        r"""资料标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Type(self):
        r"""资料来源类型，1:问答库，2:文档，3:医典百科，4:临床指南，5:药品说明书
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        r"""资料详情链接
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFileInfoReq(AbstractModel):
    r"""报告文件信息参数

    """

    def __init__(self):
        r"""
        :param _ReportFileUrl: <p>报告文件链接</p>
        :type ReportFileUrl: str
        :param _ReportFileType: <p>报告文件类型，1:pdf，2:图片</p>
        :type ReportFileType: int
        :param _ReportId: <p>报告id</p>
        :type ReportId: str
        """
        self._ReportFileUrl = None
        self._ReportFileType = None
        self._ReportId = None

    @property
    def ReportFileUrl(self):
        r"""<p>报告文件链接</p>
        :rtype: str
        """
        return self._ReportFileUrl

    @ReportFileUrl.setter
    def ReportFileUrl(self, ReportFileUrl):
        self._ReportFileUrl = ReportFileUrl

    @property
    def ReportFileType(self):
        r"""<p>报告文件类型，1:pdf，2:图片</p>
        :rtype: int
        """
        return self._ReportFileType

    @ReportFileType.setter
    def ReportFileType(self, ReportFileType):
        self._ReportFileType = ReportFileType

    @property
    def ReportId(self):
        r"""<p>报告id</p>
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId


    def _deserialize(self, params):
        self._ReportFileUrl = params.get("ReportFileUrl")
        self._ReportFileType = params.get("ReportFileType")
        self._ReportId = params.get("ReportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportFileInfoRsp(AbstractModel):
    r"""报告文件信息返回

    """

    def __init__(self):
        r"""
        :param _ReportId: <p>报告id</p>
        :type ReportId: str
        :param _IsAnalysis: <p>是否解析成功</p>
        :type IsAnalysis: bool
        :param _ErrInfo: <p>解析错误信息</p>
        :type ErrInfo: str
        """
        self._ReportId = None
        self._IsAnalysis = None
        self._ErrInfo = None

    @property
    def ReportId(self):
        r"""<p>报告id</p>
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def IsAnalysis(self):
        r"""<p>是否解析成功</p>
        :rtype: bool
        """
        return self._IsAnalysis

    @IsAnalysis.setter
    def IsAnalysis(self, IsAnalysis):
        self._IsAnalysis = IsAnalysis

    @property
    def ErrInfo(self):
        r"""<p>解析错误信息</p>
        :rtype: str
        """
        return self._ErrInfo

    @ErrInfo.setter
    def ErrInfo(self, ErrInfo):
        self._ErrInfo = ErrInfo


    def _deserialize(self, params):
        self._ReportId = params.get("ReportId")
        self._IsAnalysis = params.get("IsAnalysis")
        self._ErrInfo = params.get("ErrInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardDrugCardInfo(AbstractModel):
    r"""标准药品卡片信息

    """

    def __init__(self):
        r"""
        :param _StandardDrugName: 标准药品名
        :type StandardDrugName: str
        :param _DrugInfos: 药品列表
        :type DrugInfos: list of DrugCardInfo
        """
        self._StandardDrugName = None
        self._DrugInfos = None

    @property
    def StandardDrugName(self):
        r"""标准药品名
        :rtype: str
        """
        return self._StandardDrugName

    @StandardDrugName.setter
    def StandardDrugName(self, StandardDrugName):
        self._StandardDrugName = StandardDrugName

    @property
    def DrugInfos(self):
        r"""药品列表
        :rtype: list of DrugCardInfo
        """
        return self._DrugInfos

    @DrugInfos.setter
    def DrugInfos(self, DrugInfos):
        self._DrugInfos = DrugInfos


    def _deserialize(self, params):
        self._StandardDrugName = params.get("StandardDrugName")
        if params.get("DrugInfos") is not None:
            self._DrugInfos = []
            for item in params.get("DrugInfos"):
                obj = DrugCardInfo()
                obj._deserialize(item)
                self._DrugInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StandardDrugInstructionInfo(AbstractModel):
    r"""药品说明书标准药品结果

    """

    def __init__(self):
        r"""
        :param _StandardDrugName: 标准药品名
        :type StandardDrugName: str
        :param _DrugInfos: 药品列表
        :type DrugInfos: list of DrugInstructionInfo
        """
        self._StandardDrugName = None
        self._DrugInfos = None

    @property
    def StandardDrugName(self):
        r"""标准药品名
        :rtype: str
        """
        return self._StandardDrugName

    @StandardDrugName.setter
    def StandardDrugName(self, StandardDrugName):
        self._StandardDrugName = StandardDrugName

    @property
    def DrugInfos(self):
        r"""药品列表
        :rtype: list of DrugInstructionInfo
        """
        return self._DrugInfos

    @DrugInfos.setter
    def DrugInfos(self, DrugInfos):
        self._DrugInfos = DrugInfos


    def _deserialize(self, params):
        self._StandardDrugName = params.get("StandardDrugName")
        if params.get("DrugInfos") is not None:
            self._DrugInfos = []
            for item in params.get("DrugInfos"):
                obj = DrugInstructionInfo()
                obj._deserialize(item)
                self._DrugInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        