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


class AppConfig(AbstractModel):
    """应用配置

    """

    def __init__(self):
        r"""
        :param _KnowledgeQa: 知识问答管理应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type KnowledgeQa: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaConfig`
        :param _Summary: 知识摘要应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Summary: :class:`tencentcloud.lke.v20231130.models.SummaryConfig`
        :param _Classify: 标签提取应用配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Classify: :class:`tencentcloud.lke.v20231130.models.ClassifyConfig`
        """
        self._KnowledgeQa = None
        self._Summary = None
        self._Classify = None

    @property
    def KnowledgeQa(self):
        return self._KnowledgeQa

    @KnowledgeQa.setter
    def KnowledgeQa(self, KnowledgeQa):
        self._KnowledgeQa = KnowledgeQa

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def Classify(self):
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify


    def _deserialize(self, params):
        if params.get("KnowledgeQa") is not None:
            self._KnowledgeQa = KnowledgeQaConfig()
            self._KnowledgeQa._deserialize(params.get("KnowledgeQa"))
        if params.get("Summary") is not None:
            self._Summary = SummaryConfig()
            self._Summary._deserialize(params.get("Summary"))
        if params.get("Classify") is not None:
            self._Classify = ClassifyConfig()
            self._Classify._deserialize(params.get("Classify"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppInfo(AbstractModel):
    """应用详情

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
注意：此字段可能返回 null，表示取不到有效值。
        :type AppType: str
        :param _AppTypeDesc: 应用类型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type AppTypeDesc: str
        :param _AppBizId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBizId: str
        :param _Name: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Avatar: 应用头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _Desc: 应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _AppStatus: 应用状态，1：未上线，2：运行中，3：停用
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatus: int
        :param _AppStatusDesc: 状态说明
注意：此字段可能返回 null，表示取不到有效值。
        :type AppStatusDesc: str
        :param _UpdateTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Operator: 最后修改人
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param _ModelAliasName: 模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelAliasName: str
        """
        self._AppType = None
        self._AppTypeDesc = None
        self._AppBizId = None
        self._Name = None
        self._Avatar = None
        self._Desc = None
        self._AppStatus = None
        self._AppStatusDesc = None
        self._UpdateTime = None
        self._Operator = None
        self._ModelName = None
        self._ModelAliasName = None

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppTypeDesc(self):
        return self._AppTypeDesc

    @AppTypeDesc.setter
    def AppTypeDesc(self, AppTypeDesc):
        self._AppTypeDesc = AppTypeDesc

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def AppStatusDesc(self):
        return self._AppStatusDesc

    @AppStatusDesc.setter
    def AppStatusDesc(self, AppStatusDesc):
        self._AppStatusDesc = AppStatusDesc

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelAliasName(self):
        return self._ModelAliasName

    @ModelAliasName.setter
    def ModelAliasName(self, ModelAliasName):
        self._ModelAliasName = ModelAliasName


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._AppTypeDesc = params.get("AppTypeDesc")
        self._AppBizId = params.get("AppBizId")
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._Desc = params.get("Desc")
        self._AppStatus = params.get("AppStatus")
        self._AppStatusDesc = params.get("AppStatusDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Operator = params.get("Operator")
        self._ModelName = params.get("ModelName")
        self._ModelAliasName = params.get("ModelAliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppModel(AbstractModel):
    """应用模型配置

    """

    def __init__(self):
        r"""
        :param _Name: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Desc: 模型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _ContextLimit: 上下文指代轮次
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextLimit: int
        :param _AliasName: 模型别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param _TokenBalance: token余量
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenBalance: float
        """
        self._Name = None
        self._Desc = None
        self._ContextLimit = None
        self._AliasName = None
        self._TokenBalance = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ContextLimit(self):
        return self._ContextLimit

    @ContextLimit.setter
    def ContextLimit(self, ContextLimit):
        self._ContextLimit = ContextLimit

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def TokenBalance(self):
        return self._TokenBalance

    @TokenBalance.setter
    def TokenBalance(self, TokenBalance):
        self._TokenBalance = TokenBalance


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._ContextLimit = params.get("ContextLimit")
        self._AliasName = params.get("AliasName")
        self._TokenBalance = params.get("TokenBalance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabel(AbstractModel):
    """属性标签详情信息

    """

    def __init__(self):
        r"""
        :param _Source: 属性标签来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param _AttrBizId: 属性ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrBizId: str
        :param _AttrKey: 属性标识
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrKey: str
        :param _AttrName: 属性名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrName: str
        :param _Labels: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        """
        self._Source = None
        self._AttrBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._Labels = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AttrBizId(self):
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

    @property
    def AttrKey(self):
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._AttrBizId = params.get("AttrBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabelDetail(AbstractModel):
    """属性标签详情

    """

    def __init__(self):
        r"""
        :param _AttrBizId: 属性ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrBizId: str
        :param _AttrKey: 属性标识
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrKey: str
        :param _AttrName: 属性名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrName: str
        :param _LabelNames: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelNames: list of str
        :param _IsUpdating: 属性标签是否在更新中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUpdating: bool
        """
        self._AttrBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._LabelNames = None
        self._IsUpdating = None

    @property
    def AttrBizId(self):
        return self._AttrBizId

    @AttrBizId.setter
    def AttrBizId(self, AttrBizId):
        self._AttrBizId = AttrBizId

    @property
    def AttrKey(self):
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def LabelNames(self):
        return self._LabelNames

    @LabelNames.setter
    def LabelNames(self, LabelNames):
        self._LabelNames = LabelNames

    @property
    def IsUpdating(self):
        return self._IsUpdating

    @IsUpdating.setter
    def IsUpdating(self, IsUpdating):
        self._IsUpdating = IsUpdating


    def _deserialize(self, params):
        self._AttrBizId = params.get("AttrBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        self._LabelNames = params.get("LabelNames")
        self._IsUpdating = params.get("IsUpdating")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttrLabelRefer(AbstractModel):
    """属性标签引用信息

    """

    def __init__(self):
        r"""
        :param _Source: 属性标签来源，1：属性标签
        :type Source: int
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: str
        :param _LabelBizIds: 标签ID
        :type LabelBizIds: list of str
        """
        self._Source = None
        self._AttributeBizId = None
        self._LabelBizIds = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def AttributeBizId(self):
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def LabelBizIds(self):
        return self._LabelBizIds

    @LabelBizIds.setter
    def LabelBizIds(self, LabelBizIds):
        self._LabelBizIds = LabelBizIds


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._AttributeBizId = params.get("AttributeBizId")
        self._LabelBizIds = params.get("LabelBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeFilters(AbstractModel):
    """导出知识标签过滤器

    """

    def __init__(self):
        r"""
        :param _Query: 检索，属性或标签名称
        :type Query: str
        """
        self._Query = None

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeLabel(AbstractModel):
    """属性标签

    """

    def __init__(self):
        r"""
        :param _LabelBizId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelBizId: str
        :param _LabelName: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        :param _SimilarLabels: 相似标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SimilarLabels: list of str
        """
        self._LabelBizId = None
        self._LabelName = None
        self._SimilarLabels = None

    @property
    def LabelBizId(self):
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def SimilarLabels(self):
        return self._SimilarLabels

    @SimilarLabels.setter
    def SimilarLabels(self, SimilarLabels):
        self._SimilarLabels = SimilarLabels


    def _deserialize(self, params):
        self._LabelBizId = params.get("LabelBizId")
        self._LabelName = params.get("LabelName")
        self._SimilarLabels = params.get("SimilarLabels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseConfig(AbstractModel):
    """应用基础配置

    """

    def __init__(self):
        r"""
        :param _Name: 应用名称
        :type Name: str
        :param _Avatar: 应用头像
        :type Avatar: str
        :param _Desc: 应用描述
        :type Desc: str
        """
        self._Name = None
        self._Avatar = None
        self._Desc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Avatar = params.get("Avatar")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelExistRequest(AbstractModel):
    """CheckAttributeLabelExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _LabelName: 属性名称
        :type LabelName: str
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _LastLabelBizId: 滚动加载，最后一个属性标签ID
        :type LastLabelBizId: str
        """
        self._BotBizId = None
        self._LabelName = None
        self._AttributeBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._LastLabelBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName

    @property
    def AttributeBizId(self):
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LastLabelBizId(self):
        return self._LastLabelBizId

    @LastLabelBizId.setter
    def LastLabelBizId(self, LastLabelBizId):
        self._LastLabelBizId = LastLabelBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LabelName = params.get("LabelName")
        self._AttributeBizId = params.get("AttributeBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LastLabelBizId = params.get("LastLabelBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelExistResponse(AbstractModel):
    """CheckAttributeLabelExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsExist: 是否存在
        :type IsExist: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsExist = None
        self._RequestId = None

    @property
    def IsExist(self):
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsExist = params.get("IsExist")
        self._RequestId = params.get("RequestId")


class CheckAttributeLabelReferRequest(AbstractModel):
    """CheckAttributeLabelRefer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _LabelBizId: 属性标签
        :type LabelBizId: str
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: list of str
        """
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._LabelBizId = None
        self._AttributeBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LabelBizId(self):
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def AttributeBizId(self):
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LabelBizId = params.get("LabelBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAttributeLabelReferResponse(AbstractModel):
    """CheckAttributeLabelRefer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsRefer: 是否引用
        :type IsRefer: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsRefer = None
        self._RequestId = None

    @property
    def IsRefer(self):
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsRefer = params.get("IsRefer")
        self._RequestId = params.get("RequestId")


class ClassifyConfig(AbstractModel):
    """标签提取配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Labels: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of ClassifyLabel
        :param _Greeting: 欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Greeting: str
        """
        self._Model = None
        self._Labels = None
        self._Greeting = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Greeting(self):
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = ClassifyLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Greeting = params.get("Greeting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyLabel(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param _Name: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: 标签描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Values: 标签取值范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        """
        self._Name = None
        self._Description = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Context(AbstractModel):
    """获取不满意回复上下文响

    """

    def __init__(self):
        r"""
        :param _RecordBizId: 消息记录ID信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordBizId: str
        :param _IsVisitor: 是否为用户
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVisitor: bool
        :param _NickName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type NickName: str
        :param _Avatar: 头像
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _Content: 消息内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _FileInfos: 文档信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfos: list of MsgFileInfo
        """
        self._RecordBizId = None
        self._IsVisitor = None
        self._NickName = None
        self._Avatar = None
        self._Content = None
        self._FileInfos = None

    @property
    def RecordBizId(self):
        return self._RecordBizId

    @RecordBizId.setter
    def RecordBizId(self, RecordBizId):
        self._RecordBizId = RecordBizId

    @property
    def IsVisitor(self):
        return self._IsVisitor

    @IsVisitor.setter
    def IsVisitor(self, IsVisitor):
        self._IsVisitor = IsVisitor

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def FileInfos(self):
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos


    def _deserialize(self, params):
        self._RecordBizId = params.get("RecordBizId")
        self._IsVisitor = params.get("IsVisitor")
        self._NickName = params.get("NickName")
        self._Avatar = params.get("Avatar")
        self._Content = params.get("Content")
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = MsgFileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConvertDocumentRequest(AbstractModel):
    """ConvertDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileUrl: 图片的 Url 地址。 支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。 支持的图片大小：所下载图片经 Base64 编码后不超过 8M。图片下载时间不超过 3 秒。 支持的图片像素：单边介于20-10000px之间。 图片存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议图片存储于腾讯云。 非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type FileUrl: str
        :param _FileBase64: 图片的 Base64 值。 支持的图片格式：PNG、JPG、JPEG、PDF，暂不支持 GIF 格式。 支持的图片大小：所下载图片经Base64编码后不超过 8M。图片下载时间不超过 3 秒。 支持的图片像素：单边介于20-10000px之间。 图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :type FileBase64: str
        :param _FileStartPageNumber: 当传入文件是PDF类型（FileType=PDF）时，用来指定pdf识别的起始页码，识别的页码包含当前值。
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 当传入文件是PDF类型（FileType=PDF）时，用来指定pdf识别的结束页码，识别的页码包含当前值。
建议一次请求的页面不超过3页。
        :type FileEndPageNumber: int
        """
        self._FileUrl = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileBase64(self):
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber


    def _deserialize(self, params):
        self._FileUrl = params.get("FileUrl")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConvertDocumentResponse(AbstractModel):
    """ConvertDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WordRecognizeInfo: 识别生成的word文件base64编码的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type WordRecognizeInfo: list of WordRecognizeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WordRecognizeInfo = None
        self._RequestId = None

    @property
    def WordRecognizeInfo(self):
        return self._WordRecognizeInfo

    @WordRecognizeInfo.setter
    def WordRecognizeInfo(self, WordRecognizeInfo):
        self._WordRecognizeInfo = WordRecognizeInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WordRecognizeInfo") is not None:
            self._WordRecognizeInfo = []
            for item in params.get("WordRecognizeInfo"):
                obj = WordRecognizeInfo()
                obj._deserialize(item)
                self._WordRecognizeInfo.append(obj)
        self._RequestId = params.get("RequestId")


class Coord(AbstractModel):
    """坐标

    """

    def __init__(self):
        r"""
        :param _X: 横坐标
        :type X: int
        :param _Y: 纵坐标
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppRequest(AbstractModel):
    """CreateApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _BaseConfig: 应用基础配置
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        """
        self._AppType = None
        self._BaseConfig = None

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def BaseConfig(self):
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    """CreateApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBizId = None
        self._RequestId = None

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._RequestId = params.get("RequestId")


class CreateAttributeLabelRequest(AbstractModel):
    """CreateAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _AttrKey: 属性标识
        :type AttrKey: str
        :param _AttrName: 属性名称
        :type AttrName: str
        :param _Labels: 属性标签
        :type Labels: list of AttributeLabel
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._Labels = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttrKey(self):
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAttributeLabelResponse(AbstractModel):
    """CreateAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCorpRequest(AbstractModel):
    """CreateCorp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FullName: 企业全称
        :type FullName: str
        :param _ContactName: 联系人名称
        :type ContactName: str
        :param _Email: 联系人邮箱
        :type Email: str
        :param _Telephone: 联系人手机号
        :type Telephone: str
        """
        self._FullName = None
        self._ContactName = None
        self._Email = None
        self._Telephone = None

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def ContactName(self):
        return self._ContactName

    @ContactName.setter
    def ContactName(self, ContactName):
        self._ContactName = ContactName

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Telephone(self):
        return self._Telephone

    @Telephone.setter
    def Telephone(self, Telephone):
        self._Telephone = Telephone


    def _deserialize(self, params):
        self._FullName = params.get("FullName")
        self._ContactName = params.get("ContactName")
        self._Email = params.get("Email")
        self._Telephone = params.get("Telephone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCorpResponse(AbstractModel):
    """CreateCorp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpBizId: 企业ID
        :type CorpBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CorpBizId = None
        self._RequestId = None

    @property
    def CorpBizId(self):
        return self._CorpBizId

    @CorpBizId.setter
    def CorpBizId(self, CorpBizId):
        self._CorpBizId = CorpBizId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CorpBizId = params.get("CorpBizId")
        self._RequestId = params.get("RequestId")


class CreateQACateRequest(AbstractModel):
    """CreateQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ParentBizId: 父级业务ID
        :type ParentBizId: str
        :param _Name: 分类名称

        :type Name: str
        """
        self._BotBizId = None
        self._ParentBizId = None
        self._Name = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ParentBizId(self):
        return self._ParentBizId

    @ParentBizId.setter
    def ParentBizId(self, ParentBizId):
        self._ParentBizId = ParentBizId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ParentBizId = params.get("ParentBizId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQACateResponse(AbstractModel):
    """CreateQACate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CanAdd: 是否可新增

        :type CanAdd: bool
        :param _CanEdit: 是否可编辑
        :type CanEdit: bool
        :param _CanDelete: 是否可删除

        :type CanDelete: bool
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._CateBizId = None
        self._RequestId = None

    @property
    def CanAdd(self):
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        self._CateBizId = params.get("CateBizId")
        self._RequestId = params.get("RequestId")


class CreateQARequest(AbstractModel):
    """CreateQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _CustomParam: 自定义参数
        :type CustomParam: str
        :param _AttrLabels: 属性标签引用
        :type AttrLabels: list of AttrLabelRefer
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _ExpireStart: 有效开始时间，unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        """
        self._BotBizId = None
        self._Question = None
        self._Answer = None
        self._AttrRange = None
        self._CustomParam = None
        self._AttrLabels = None
        self._DocBizId = None
        self._CateBizId = None
        self._ExpireStart = None
        self._ExpireEnd = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def CustomParam(self):
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def ExpireStart(self):
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._AttrRange = params.get("AttrRange")
        self._CustomParam = params.get("CustomParam")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._DocBizId = params.get("DocBizId")
        self._CateBizId = params.get("CateBizId")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQAResponse(AbstractModel):
    """CreateQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QaBizId = None
        self._RequestId = None

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._RequestId = params.get("RequestId")


class CreateReconstructDocumentFlowConfig(AbstractModel):
    """创建智能文档解析任务的配置信息

    """

    def __init__(self):
        r"""
        :param _TableResultType: Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为1
        :type TableResultType: str
        """
        self._TableResultType = None

    @property
    def TableResultType(self):
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        self._TableResultType = TableResultType


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowRequest(AbstractModel):
    """CreateReconstructDocumentFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileBase64: 文件的 Base64 值。 支持的文件格式：PNG、JPG、JPEG、PDF。 支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。 支持的图片像素：单边介于20-10000px之间。 文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :type FileBase64: str
        :param _FileUrl: 文件的 Url 地址。 支持的文件格式：PNG、JPG、JPEG、PDF。 支持的文件大小：所下载文件经 Base64 编码后不超过 100M。文件下载时间不超过 15 秒。 支持的图片像素：单边介于20-10000px之间。 文件存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type FileUrl: str
        :param _FileStartPageNumber: 当传入文件是PDF类型时，用来指定pdf识别的起始页码，识别的页码包含当前值。默认为1，表示从pdf文件的第1页开始识别。
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 当传入文件是PDF类型时，用来指定pdf识别的结束页码，识别的页码包含当前值。默认为100，表示识别到pdf文件的第100页。单次调用最多支持识别100页内容，即FileEndPageNumber-FileStartPageNumber需要不大于100。
        :type FileEndPageNumber: int
        :param _Config: 创建文档解析任务配置信息
        :type Config: :class:`tencentcloud.lke.v20231130.models.CreateReconstructDocumentFlowConfig`
        """
        self._FileBase64 = None
        self._FileUrl = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileBase64(self):
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileStartPageNumber(self):
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileBase64 = params.get("FileBase64")
        self._FileUrl = params.get("FileUrl")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateReconstructDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowResponse(AbstractModel):
    """CreateReconstructDocumentFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateRejectedQuestionRequest(AbstractModel):
    """CreateRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Question: 拒答问题


        :type Question: str
        :param _BusinessSource: 拒答问题来源的数据源唯一id，取值1，2


        :type BusinessSource: int
        :param _BusinessId: 拒答问题来源的数据源唯一id


        :type BusinessId: str
        """
        self._BotBizId = None
        self._Question = None
        self._BusinessSource = None
        self._BusinessId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def BusinessSource(self):
        return self._BusinessSource

    @BusinessSource.setter
    def BusinessSource(self, BusinessSource):
        self._BusinessSource = BusinessSource

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._BusinessSource = params.get("BusinessSource")
        self._BusinessId = params.get("BusinessId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRejectedQuestionResponse(AbstractModel):
    """CreateRejectedQuestion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateReleaseRequest(AbstractModel):
    """CreateRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _Desc: 发布描述
        :type Desc: str
        """
        self._BotBizId = None
        self._Desc = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseResponse(AbstractModel):
    """CreateRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReleaseBizId: 发布ID
        :type ReleaseBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReleaseBizId = None
        self._RequestId = None

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """临时密钥结构

    """

    def __init__(self):
        r"""
        :param _Token: token
注意：此字段可能返回 null，表示取不到有效值。
        :type Token: str
        :param _TmpSecretId: 临时证书密钥ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param _TmpSecretKey: 临时证书密钥Key
注意：此字段可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        """
        self._Token = None
        self._TmpSecretId = None
        self._TmpSecretKey = None

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppRequest(AbstractModel):
    """DeleteApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        """
        self._AppBizId = None
        self._AppType = None

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppResponse(AbstractModel):
    """DeleteApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteAttributeLabelRequest(AbstractModel):
    """DeleteAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _AttributeBizIds: 属性ID
        :type AttributeBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._AttributeBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizIds(self):
        return self._AttributeBizIds

    @AttributeBizIds.setter
    def AttributeBizIds(self, AttributeBizIds):
        self._AttributeBizIds = AttributeBizIds

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizIds = params.get("AttributeBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttributeLabelResponse(AbstractModel):
    """DeleteAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDocRequest(AbstractModel):
    """DeleteDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizIds: 文档业务ID列表
        :type DocBizIds: list of str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._DocBizIds = None
        self._BotBizId = None

    @property
    def DocBizIds(self):
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._DocBizIds = params.get("DocBizIds")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocResponse(AbstractModel):
    """DeleteDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteQACateRequest(AbstractModel):
    """DeleteQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQACateResponse(AbstractModel):
    """DeleteQACate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteQARequest(AbstractModel):
    """DeleteQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: 问答ID
        :type QaBizIds: list of str
        """
        self._BotBizId = None
        self._QaBizIds = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQAResponse(AbstractModel):
    """DeleteQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRejectedQuestionRequest(AbstractModel):
    """DeleteRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _RejectedBizIds: 拒答问题来源的数据源唯一id



        :type RejectedBizIds: list of str
        """
        self._BotBizId = None
        self._RejectedBizIds = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def RejectedBizIds(self):
        return self._RejectedBizIds

    @RejectedBizIds.setter
    def RejectedBizIds(self, RejectedBizIds):
        self._RejectedBizIds = RejectedBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._RejectedBizIds = params.get("RejectedBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRejectedQuestionResponse(AbstractModel):
    """DeleteRejectedQuestion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAppRequest(AbstractModel):
    """DescribeApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _IsRelease: 是否发布后的配置
        :type IsRelease: bool
        """
        self._AppBizId = None
        self._AppType = None
        self._IsRelease = None

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def IsRelease(self):
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        self._IsRelease = params.get("IsRelease")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppResponse(AbstractModel):
    """DescribeApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用 ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _AppTypeDesc: 应用类型说明
        :type AppTypeDesc: str
        :param _BaseConfig: 应用类型说明
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        :param _AppConfig: 应用配置
        :type AppConfig: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        :param _AvatarInAppeal: 头像是否在申诉中
        :type AvatarInAppeal: bool
        :param _RoleInAppeal: 角色描述是否在申诉中
        :type RoleInAppeal: bool
        :param _NameInAppeal: 名称是否在申诉中
        :type NameInAppeal: bool
        :param _GreetingInAppeal: 欢迎语是否在申诉中
        :type GreetingInAppeal: bool
        :param _BareAnswerInAppeal: 未知问题回复语是否在申诉中
        :type BareAnswerInAppeal: bool
        :param _AppKey: 应用appKey
        :type AppKey: str
        :param _AppStatus: 应用状态，1：未上线，2：运行中，3：停用
        :type AppStatus: int
        :param _AppStatusDesc: 状态说明
        :type AppStatusDesc: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBizId = None
        self._AppType = None
        self._AppTypeDesc = None
        self._BaseConfig = None
        self._AppConfig = None
        self._AvatarInAppeal = None
        self._RoleInAppeal = None
        self._NameInAppeal = None
        self._GreetingInAppeal = None
        self._BareAnswerInAppeal = None
        self._AppKey = None
        self._AppStatus = None
        self._AppStatusDesc = None
        self._RequestId = None

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppTypeDesc(self):
        return self._AppTypeDesc

    @AppTypeDesc.setter
    def AppTypeDesc(self, AppTypeDesc):
        self._AppTypeDesc = AppTypeDesc

    @property
    def BaseConfig(self):
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig

    @property
    def AppConfig(self):
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig

    @property
    def AvatarInAppeal(self):
        return self._AvatarInAppeal

    @AvatarInAppeal.setter
    def AvatarInAppeal(self, AvatarInAppeal):
        self._AvatarInAppeal = AvatarInAppeal

    @property
    def RoleInAppeal(self):
        return self._RoleInAppeal

    @RoleInAppeal.setter
    def RoleInAppeal(self, RoleInAppeal):
        self._RoleInAppeal = RoleInAppeal

    @property
    def NameInAppeal(self):
        return self._NameInAppeal

    @NameInAppeal.setter
    def NameInAppeal(self, NameInAppeal):
        self._NameInAppeal = NameInAppeal

    @property
    def GreetingInAppeal(self):
        return self._GreetingInAppeal

    @GreetingInAppeal.setter
    def GreetingInAppeal(self, GreetingInAppeal):
        self._GreetingInAppeal = GreetingInAppeal

    @property
    def BareAnswerInAppeal(self):
        return self._BareAnswerInAppeal

    @BareAnswerInAppeal.setter
    def BareAnswerInAppeal(self, BareAnswerInAppeal):
        self._BareAnswerInAppeal = BareAnswerInAppeal

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def AppStatus(self):
        return self._AppStatus

    @AppStatus.setter
    def AppStatus(self, AppStatus):
        self._AppStatus = AppStatus

    @property
    def AppStatusDesc(self):
        return self._AppStatusDesc

    @AppStatusDesc.setter
    def AppStatusDesc(self, AppStatusDesc):
        self._AppStatusDesc = AppStatusDesc

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        self._AppTypeDesc = params.get("AppTypeDesc")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        if params.get("AppConfig") is not None:
            self._AppConfig = AppConfig()
            self._AppConfig._deserialize(params.get("AppConfig"))
        self._AvatarInAppeal = params.get("AvatarInAppeal")
        self._RoleInAppeal = params.get("RoleInAppeal")
        self._NameInAppeal = params.get("NameInAppeal")
        self._GreetingInAppeal = params.get("GreetingInAppeal")
        self._BareAnswerInAppeal = params.get("BareAnswerInAppeal")
        self._AppKey = params.get("AppKey")
        self._AppStatus = params.get("AppStatus")
        self._AppStatusDesc = params.get("AppStatusDesc")
        self._RequestId = params.get("RequestId")


class DescribeAttributeLabelRequest(AbstractModel):
    """DescribeAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: str
        :param _Limit: 每次加载的数量 
        :type Limit: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Query: 查询标签或相似标签
        :type Query: str
        :param _LastLabelBizId: 滚动加载游标的标签ID
        :type LastLabelBizId: str
        """
        self._BotBizId = None
        self._AttributeBizId = None
        self._Limit = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None
        self._LastLabelBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizId(self):
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def LastLabelBizId(self):
        return self._LastLabelBizId

    @LastLabelBizId.setter
    def LastLabelBizId(self, LastLabelBizId):
        self._LastLabelBizId = LastLabelBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        self._Limit = params.get("Limit")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        self._LastLabelBizId = params.get("LastLabelBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttributeLabelResponse(AbstractModel):
    """DescribeAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: str
        :param _AttrKey: 属性标识
        :type AttrKey: str
        :param _AttrName: 属性名称
        :type AttrName: str
        :param _LabelNumber: 标签数量
        :type LabelNumber: str
        :param _Labels: 标签名称
        :type Labels: list of AttributeLabel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AttributeBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._LabelNumber = None
        self._Labels = None
        self._RequestId = None

    @property
    def AttributeBizId(self):
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def AttrKey(self):
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def LabelNumber(self):
        return self._LabelNumber

    @LabelNumber.setter
    def LabelNumber(self, LabelNumber):
        self._LabelNumber = LabelNumber

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AttributeBizId = params.get("AttributeBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        self._LabelNumber = params.get("LabelNumber")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCorpRequest(AbstractModel):
    """DescribeCorp请求参数结构体

    """


class DescribeCorpResponse(AbstractModel):
    """DescribeCorp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CorpBizId: 企业ID

        :type CorpBizId: str
        :param _RobotQuota: 机器人配额

        :type RobotQuota: int
        :param _FullName: 企业全称

        :type FullName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CorpBizId = None
        self._RobotQuota = None
        self._FullName = None
        self._RequestId = None

    @property
    def CorpBizId(self):
        return self._CorpBizId

    @CorpBizId.setter
    def CorpBizId(self, CorpBizId):
        self._CorpBizId = CorpBizId

    @property
    def RobotQuota(self):
        return self._RobotQuota

    @RobotQuota.setter
    def RobotQuota(self, RobotQuota):
        self._RobotQuota = RobotQuota

    @property
    def FullName(self):
        return self._FullName

    @FullName.setter
    def FullName(self, FullName):
        self._FullName = FullName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CorpBizId = params.get("CorpBizId")
        self._RobotQuota = params.get("RobotQuota")
        self._FullName = params.get("FullName")
        self._RequestId = params.get("RequestId")


class DescribeDocRequest(AbstractModel):
    """DescribeDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocResponse(AbstractModel):
    """DescribeDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _FileName: 文件名称
        :type FileName: str
        :param _FileType: 文件类型
        :type FileType: str
        :param _CosUrl: cos路径
        :type CosUrl: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 文档状态(5审核通过 7审核中 8审核不通过 9审核通过 10待发布 11发布中 12发布成功 13学习中 14学习失败)

        :type Status: int
        :param _StatusDesc: 文档状态描述
        :type StatusDesc: str
        :param _Reason: 生成失败原因
        :type Reason: str
        :param _IsRefer: 答案中是否引用
        :type IsRefer: bool
        :param _QaNum: 问答对数量
        :type QaNum: int
        :param _IsDeleted: 是否删除
        :type IsDeleted: bool
        :param _Source: 文档来源
        :type Source: int
        :param _SourceDesc: 文档来源描述
        :type SourceDesc: str
        :param _IsAllowRestart: 是否允许重新生成
        :type IsAllowRestart: bool
        :param _IsDeletedQa: qa是否已删除
        :type IsDeletedQa: bool
        :param _IsCreatingQa: 问答是否生成中
        :type IsCreatingQa: bool
        :param _IsAllowDelete: 是否允许删除
        :type IsAllowDelete: bool
        :param _IsAllowRefer: 是否允许操作引用开关
        :type IsAllowRefer: bool
        :param _IsCreatedQa: 是否生成过问答
        :type IsCreatedQa: bool
        :param _DocCharSize: 文档字符量
        :type DocCharSize: str
        :param _IsAllowEdit: 是否允许编辑
        :type IsAllowEdit: bool
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件范围
        :type AttrRange: int
        :param _AttrLabels: 属性标签
        :type AttrLabels: list of AttrLabel
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocBizId = None
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._IsRefer = None
        self._QaNum = None
        self._IsDeleted = None
        self._Source = None
        self._SourceDesc = None
        self._IsAllowRestart = None
        self._IsDeletedQa = None
        self._IsCreatingQa = None
        self._IsAllowDelete = None
        self._IsAllowRefer = None
        self._IsCreatedQa = None
        self._DocCharSize = None
        self._IsAllowEdit = None
        self._AttrRange = None
        self._AttrLabels = None
        self._RequestId = None

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def IsRefer(self):
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def QaNum(self):
        return self._QaNum

    @QaNum.setter
    def QaNum(self, QaNum):
        self._QaNum = QaNum

    @property
    def IsDeleted(self):
        return self._IsDeleted

    @IsDeleted.setter
    def IsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def IsAllowRestart(self):
        return self._IsAllowRestart

    @IsAllowRestart.setter
    def IsAllowRestart(self, IsAllowRestart):
        self._IsAllowRestart = IsAllowRestart

    @property
    def IsDeletedQa(self):
        return self._IsDeletedQa

    @IsDeletedQa.setter
    def IsDeletedQa(self, IsDeletedQa):
        self._IsDeletedQa = IsDeletedQa

    @property
    def IsCreatingQa(self):
        return self._IsCreatingQa

    @IsCreatingQa.setter
    def IsCreatingQa(self, IsCreatingQa):
        self._IsCreatingQa = IsCreatingQa

    @property
    def IsAllowDelete(self):
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowRefer(self):
        return self._IsAllowRefer

    @IsAllowRefer.setter
    def IsAllowRefer(self, IsAllowRefer):
        self._IsAllowRefer = IsAllowRefer

    @property
    def IsCreatedQa(self):
        return self._IsCreatedQa

    @IsCreatedQa.setter
    def IsCreatedQa(self, IsCreatedQa):
        self._IsCreatedQa = IsCreatedQa

    @property
    def DocCharSize(self):
        return self._DocCharSize

    @DocCharSize.setter
    def DocCharSize(self, DocCharSize):
        self._DocCharSize = DocCharSize

    @property
    def IsAllowEdit(self):
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._IsRefer = params.get("IsRefer")
        self._QaNum = params.get("QaNum")
        self._IsDeleted = params.get("IsDeleted")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._IsAllowRestart = params.get("IsAllowRestart")
        self._IsDeletedQa = params.get("IsDeletedQa")
        self._IsCreatingQa = params.get("IsCreatingQa")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowRefer = params.get("IsAllowRefer")
        self._IsCreatedQa = params.get("IsCreatedQa")
        self._DocCharSize = params.get("DocCharSize")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQARequest(AbstractModel):
    """DescribeQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QaBizId: QA业务ID

        :type QaBizId: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._QaBizId = None
        self._BotBizId = None

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQAResponse(AbstractModel):
    """DescribeQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QaBizId: QA业务ID

        :type QaBizId: str
        :param _Question: 问题

        :type Question: str
        :param _Answer: 答案

        :type Answer: str
        :param _CustomParam: 自定义参数
        :type CustomParam: str
        :param _Source: 来源

        :type Source: int
        :param _SourceDesc: 来源描述

        :type SourceDesc: str
        :param _UpdateTime: 更新时间

        :type UpdateTime: str
        :param _Status: 状态

        :type Status: int
        :param _StatusDesc: 状态描述

        :type StatusDesc: str
        :param _CateBizId: 分类ID

        :type CateBizId: str
        :param _IsAllowAccept: 是否允许校验

        :type IsAllowAccept: bool
        :param _IsAllowDelete: 是否允许删除

        :type IsAllowDelete: bool
        :param _IsAllowEdit: 是否允许编辑

        :type IsAllowEdit: bool
        :param _DocBizId: 文档id

        :type DocBizId: str
        :param _FileName: 文档名称

        :type FileName: str
        :param _FileType: 文档类型

        :type FileType: str
        :param _SegmentBizId: 分片ID

        :type SegmentBizId: str
        :param _PageContent: 分片内容
        :type PageContent: str
        :param _Highlights: 分片高亮内容
        :type Highlights: list of Highlight
        :param _OrgData: 分片内容

        :type OrgData: str
        :param _AttrRange: 属性标签适用范围

        :type AttrRange: int
        :param _AttrLabels: 属性标签
        :type AttrLabels: list of AttrLabel
        :param _ExpireStart: 有效开始时间，unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._CustomParam = None
        self._Source = None
        self._SourceDesc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._CateBizId = None
        self._IsAllowAccept = None
        self._IsAllowDelete = None
        self._IsAllowEdit = None
        self._DocBizId = None
        self._FileName = None
        self._FileType = None
        self._SegmentBizId = None
        self._PageContent = None
        self._Highlights = None
        self._OrgData = None
        self._AttrRange = None
        self._AttrLabels = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._RequestId = None

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CustomParam(self):
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def IsAllowAccept(self):
        return self._IsAllowAccept

    @IsAllowAccept.setter
    def IsAllowAccept(self, IsAllowAccept):
        self._IsAllowAccept = IsAllowAccept

    @property
    def IsAllowDelete(self):
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowEdit(self):
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def SegmentBizId(self):
        return self._SegmentBizId

    @SegmentBizId.setter
    def SegmentBizId(self, SegmentBizId):
        self._SegmentBizId = SegmentBizId

    @property
    def PageContent(self):
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def Highlights(self):
        return self._Highlights

    @Highlights.setter
    def Highlights(self, Highlights):
        self._Highlights = Highlights

    @property
    def OrgData(self):
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def ExpireStart(self):
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._CustomParam = params.get("CustomParam")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._CateBizId = params.get("CateBizId")
        self._IsAllowAccept = params.get("IsAllowAccept")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._SegmentBizId = params.get("SegmentBizId")
        self._PageContent = params.get("PageContent")
        if params.get("Highlights") is not None:
            self._Highlights = []
            for item in params.get("Highlights"):
                obj = Highlight()
                obj._deserialize(item)
                self._Highlights.append(obj)
        self._OrgData = params.get("OrgData")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._RequestId = params.get("RequestId")


class DescribeReferRequest(AbstractModel):
    """DescribeRefer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReferBizIds: 引用ID
        :type ReferBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReferBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReferBizIds(self):
        return self._ReferBizIds

    @ReferBizIds.setter
    def ReferBizIds(self, ReferBizIds):
        self._ReferBizIds = ReferBizIds

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReferBizIds = params.get("ReferBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReferResponse(AbstractModel):
    """DescribeRefer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 引用列表
        :type List: list of ReferDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReferDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReleaseInfoRequest(AbstractModel):
    """DescribeReleaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        """
        self._BotBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseInfoResponse(AbstractModel):
    """DescribeReleaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LastTime: 最后发布时间
        :type LastTime: str
        :param _Status: 发布状态
        :type Status: int
        :param _IsUpdated: 是否编辑过

        :type IsUpdated: bool
        :param _Msg: 失败原因

        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LastTime = None
        self._Status = None
        self._IsUpdated = None
        self._Msg = None
        self._RequestId = None

    @property
    def LastTime(self):
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsUpdated(self):
        return self._IsUpdated

    @IsUpdated.setter
    def IsUpdated(self, IsUpdated):
        self._IsUpdated = IsUpdated

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LastTime = params.get("LastTime")
        self._Status = params.get("Status")
        self._IsUpdated = params.get("IsUpdated")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeReleaseRequest(AbstractModel):
    """DescribeRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _ReleaseBizId: 发布详情
        :type ReleaseBizId: str
        """
        self._BotBizId = None
        self._ReleaseBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReleaseBizId = params.get("ReleaseBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseResponse(AbstractModel):
    """DescribeRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Description: 发布描述
        :type Description: str
        :param _Status: 发布状态(1待发布 2发布中 3发布成功 4发布失败 5发布中 6发布中 7发布失败 9发布暂停)
        :type Status: int
        :param _StatusDesc: 发布状态描述
        :type StatusDesc: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreateTime = None
        self._Description = None
        self._Status = None
        self._StatusDesc = None
        self._RequestId = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._RequestId = params.get("RequestId")


class DescribeRobotBizIDByAppKeyRequest(AbstractModel):
    """DescribeRobotBizIDByAppKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppKey: 应用appkey
        :type AppKey: str
        """
        self._AppKey = None

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey


    def _deserialize(self, params):
        self._AppKey = params.get("AppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRobotBizIDByAppKeyResponse(AbstractModel):
    """DescribeRobotBizIDByAppKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用业务ID
        :type BotBizId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BotBizId = None
        self._RequestId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._RequestId = params.get("RequestId")


class DescribeStorageCredentialRequest(AbstractModel):
    """DescribeStorageCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _FileType: 文件类型,正常的文件名类型后缀，例如 xlsx、pdf、 docx、png 等
        :type FileType: str
        :param _IsPublic: IsPublic为空用于上传文件时选择场景，当上传为图片文件是IsPublic为true，上传文档文件时场景IsPublic为false
        :type IsPublic: bool
        :param _TypeKey: 存储类型: offline:离线文件，realtime:实时文件；为空默认为offline
        :type TypeKey: str
        """
        self._BotBizId = None
        self._FileType = None
        self._IsPublic = None
        self._TypeKey = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def IsPublic(self):
        return self._IsPublic

    @IsPublic.setter
    def IsPublic(self, IsPublic):
        self._IsPublic = IsPublic

    @property
    def TypeKey(self):
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileType = params.get("FileType")
        self._IsPublic = params.get("IsPublic")
        self._TypeKey = params.get("TypeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStorageCredentialResponse(AbstractModel):
    """DescribeStorageCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 密钥信息
        :type Credentials: :class:`tencentcloud.lke.v20231130.models.Credentials`
        :param _ExpiredTime: 失效时间
        :type ExpiredTime: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Bucket: 对象存储桶
        :type Bucket: str
        :param _Region: 对象存储可用区
        :type Region: str
        :param _FilePath: 文件存储目录
        :type FilePath: str
        :param _Type: 存储类型
        :type Type: str
        :param _CorpUin: 主号
        :type CorpUin: str
        :param _ImagePath: 图片存储目录
        :type ImagePath: str
        :param _UploadPath: 上传存储路径，到具体文件
        :type UploadPath: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._ExpiredTime = None
        self._StartTime = None
        self._Bucket = None
        self._Region = None
        self._FilePath = None
        self._Type = None
        self._CorpUin = None
        self._ImagePath = None
        self._UploadPath = None
        self._RequestId = None

    @property
    def Credentials(self):
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CorpUin(self):
        return self._CorpUin

    @CorpUin.setter
    def CorpUin(self, CorpUin):
        self._CorpUin = CorpUin

    @property
    def ImagePath(self):
        return self._ImagePath

    @ImagePath.setter
    def ImagePath(self, ImagePath):
        self._ImagePath = ImagePath

    @property
    def UploadPath(self):
        return self._UploadPath

    @UploadPath.setter
    def UploadPath(self, UploadPath):
        self._UploadPath = UploadPath

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._ExpiredTime = params.get("ExpiredTime")
        self._StartTime = params.get("StartTime")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._FilePath = params.get("FilePath")
        self._Type = params.get("Type")
        self._CorpUin = params.get("CorpUin")
        self._ImagePath = params.get("ImagePath")
        self._UploadPath = params.get("UploadPath")
        self._RequestId = params.get("RequestId")


class DescribeUnsatisfiedReplyContextRequest(AbstractModel):
    """DescribeUnsatisfiedReplyContext请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReplyBizId: 回复ID
        :type ReplyBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReplyBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizId(self):
        return self._ReplyBizId

    @ReplyBizId.setter
    def ReplyBizId(self, ReplyBizId):
        self._ReplyBizId = ReplyBizId

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizId = params.get("ReplyBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnsatisfiedReplyContextResponse(AbstractModel):
    """DescribeUnsatisfiedReplyContext返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 不满意回复上下文
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Context
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Context()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DocumentElement(AbstractModel):
    """文档元素字段

    """

    def __init__(self):
        r"""
        :param _Index: 文档元素索引
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Type: 元素类型，包括paragraph、table、formula、figure、title、header、footer、figure_text

注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Text: 元素内容，当type为figure或formula(公式识别关闭)时该字段内容为图片的位置

注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Polygon: 元素坐标，左上角(x1, y1)，右上角(x2, y2)，右下角(x3, y3)，左下角(x4, y4)

注意：此字段可能返回 null，表示取不到有效值。
        :type Polygon: :class:`tencentcloud.lke.v20231130.models.Polygon`
        :param _Level: 元素层级
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _InsetImageName: 入参开启EnableInsetImage后返回，表示在InsetImagePackage中的内嵌图片名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InsetImageName: str
        :param _Elements: 嵌套的文档元素信息，一般包含的是文档内嵌入图片的文字识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Elements: list of DocumentElement
        """
        self._Index = None
        self._Type = None
        self._Text = None
        self._Polygon = None
        self._Level = None
        self._InsetImageName = None
        self._Elements = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Polygon(self):
        return self._Polygon

    @Polygon.setter
    def Polygon(self, Polygon):
        self._Polygon = Polygon

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def InsetImageName(self):
        return self._InsetImageName

    @InsetImageName.setter
    def InsetImageName(self, InsetImageName):
        self._InsetImageName = InsetImageName

    @property
    def Elements(self):
        return self._Elements

    @Elements.setter
    def Elements(self, Elements):
        self._Elements = Elements


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Type = params.get("Type")
        self._Text = params.get("Text")
        if params.get("Polygon") is not None:
            self._Polygon = Polygon()
            self._Polygon._deserialize(params.get("Polygon"))
        self._Level = params.get("Level")
        self._InsetImageName = params.get("InsetImageName")
        if params.get("Elements") is not None:
            self._Elements = []
            for item in params.get("Elements"):
                obj = DocumentElement()
                obj._deserialize(item)
                self._Elements.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocumentRecognizeInfo(AbstractModel):
    """单页文档识别的内容

    """

    def __init__(self):
        r"""
        :param _PageNumber: 输入PDF文件的页码，从1开始。输入图片的话值始终为1
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _Angle: 旋转角度

注意：此字段可能返回 null，表示取不到有效值。
        :type Angle: int
        :param _Height: AI算法识别处理后的图片高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param _Width: AI算法识别处理后的图片宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param _OriginHeight: 图片的原始高度，输入PDF文件则表示单页PDF转图片之后的图片高度
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginHeight: int
        :param _OriginWidth: 图片的原始宽度，输入PDF文件则表示单页PDF转图片之后的图片宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginWidth: int
        :param _Elements: 文档元素信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Elements: list of DocumentElement
        :param _RotatedAngle: 旋转角度

注意：此字段可能返回 null，表示取不到有效值。
        :type RotatedAngle: float
        """
        self._PageNumber = None
        self._Angle = None
        self._Height = None
        self._Width = None
        self._OriginHeight = None
        self._OriginWidth = None
        self._Elements = None
        self._RotatedAngle = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Angle(self):
        return self._Angle

    @Angle.setter
    def Angle(self, Angle):
        self._Angle = Angle

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def OriginHeight(self):
        return self._OriginHeight

    @OriginHeight.setter
    def OriginHeight(self, OriginHeight):
        self._OriginHeight = OriginHeight

    @property
    def OriginWidth(self):
        return self._OriginWidth

    @OriginWidth.setter
    def OriginWidth(self, OriginWidth):
        self._OriginWidth = OriginWidth

    @property
    def Elements(self):
        return self._Elements

    @Elements.setter
    def Elements(self, Elements):
        self._Elements = Elements

    @property
    def RotatedAngle(self):
        return self._RotatedAngle

    @RotatedAngle.setter
    def RotatedAngle(self, RotatedAngle):
        self._RotatedAngle = RotatedAngle


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._Angle = params.get("Angle")
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._OriginHeight = params.get("OriginHeight")
        self._OriginWidth = params.get("OriginWidth")
        if params.get("Elements") is not None:
            self._Elements = []
            for item in params.get("Elements"):
                obj = DocumentElement()
                obj._deserialize(item)
                self._Elements.append(obj)
        self._RotatedAngle = params.get("RotatedAngle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingObject(AbstractModel):
    """向量

    """

    def __init__(self):
        r"""
        :param _Embedding: 向量
        :type Embedding: list of float
        """
        self._Embedding = None

    @property
    def Embedding(self):
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding


    def _deserialize(self, params):
        self._Embedding = params.get("Embedding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttributeLabelRequest(AbstractModel):
    """ExportAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _AttributeBizIds: 属性ID
        :type AttributeBizIds: list of str
        :param _Filters: 根据筛选数据导出
        :type Filters: :class:`tencentcloud.lke.v20231130.models.AttributeFilters`
        """
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._AttributeBizIds = None
        self._Filters = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AttributeBizIds(self):
        return self._AttributeBizIds

    @AttributeBizIds.setter
    def AttributeBizIds(self, AttributeBizIds):
        self._AttributeBizIds = AttributeBizIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._AttributeBizIds = params.get("AttributeBizIds")
        if params.get("Filters") is not None:
            self._Filters = AttributeFilters()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttributeLabelResponse(AbstractModel):
    """ExportAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 导出任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ExportQAListRequest(AbstractModel):
    """ExportQAList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: QA业务ID
        :type QaBizIds: list of str
        :param _Filters: 查询参数
        :type Filters: :class:`tencentcloud.lke.v20231130.models.QAQuery`
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._Filters = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        if params.get("Filters") is not None:
            self._Filters = QAQuery()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportQAListResponse(AbstractModel):
    """ExportQAList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExportUnsatisfiedReplyRequest(AbstractModel):
    """ExportUnsatisfiedReply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReplyBizIds: 勾选导出ID列表
        :type ReplyBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Filters: 检索过滤器
        :type Filters: :class:`tencentcloud.lke.v20231130.models.Filters`
        """
        self._BotBizId = None
        self._ReplyBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Filters = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizIds(self):
        return self._ReplyBizIds

    @ReplyBizIds.setter
    def ReplyBizIds(self, ReplyBizIds):
        self._ReplyBizIds = ReplyBizIds

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizIds = params.get("ReplyBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        if params.get("Filters") is not None:
            self._Filters = Filters()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportUnsatisfiedReplyResponse(AbstractModel):
    """ExportUnsatisfiedReply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FileInfo(AbstractModel):
    """实时上传的文件信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 文件大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: str
        :param _FileUrl: 文件的URL地址，COS地址
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param _FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _DocId: 解析后返回的DocID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocId: str
        """
        self._FileName = None
        self._FileSize = None
        self._FileUrl = None
        self._FileType = None
        self._DocId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def DocId(self):
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        self._DocId = params.get("DocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """不满意回复检索过滤

    """

    def __init__(self):
        r"""
        :param _Query: 检索，用户问题或答案
        :type Query: str
        :param _Reasons: 错误类型检索

        :type Reasons: list of str
        """
        self._Query = None
        self._Reasons = None

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Reasons(self):
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateQARequest(AbstractModel):
    """GenerateQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizIds: 文档ID
        :type DocBizIds: list of str
        """
        self._BotBizId = None
        self._DocBizIds = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizIds(self):
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizIds = params.get("DocBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateQAResponse(AbstractModel):
    """GenerateQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class GetAnswerTypeDataCountRequest(AbstractModel):
    """GetAnswerTypeDataCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始日期
        :type StartTime: int
        :param _EndTime: 结束日期
        :type EndTime: int
        :param _AppBizId: 应用id
        :type AppBizId: list of str
        :param _Type: 消息来源(1、分享用户端  2、对话API  3、对话测试  4、应用评测)
        :type Type: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AppBizId = None
        self._Type = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizId = params.get("AppBizId")
        self._Type = params.get("Type")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAnswerTypeDataCountResponse(AbstractModel):
    """GetAnswerTypeDataCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总消息数
        :type Total: int
        :param _ModelReplyCount: 大模型直接回复总数
        :type ModelReplyCount: int
        :param _KnowledgeCount: 知识型回复总数
        :type KnowledgeCount: int
        :param _TaskFlowCount: 任务流回复总数
        :type TaskFlowCount: int
        :param _SearchEngineCount: 搜索引擎回复总数
        :type SearchEngineCount: int
        :param _ImageUnderstandingCount: 图片理解回复总数
        :type ImageUnderstandingCount: int
        :param _RejectCount: 拒答回复总数
        :type RejectCount: int
        :param _SensitiveCount: 敏感回复总数
        :type SensitiveCount: int
        :param _ConcurrentLimitCount: 并发超限回复总数
        :type ConcurrentLimitCount: int
        :param _UnknownIssuesCount: 未知问题回复总数
        :type UnknownIssuesCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ModelReplyCount = None
        self._KnowledgeCount = None
        self._TaskFlowCount = None
        self._SearchEngineCount = None
        self._ImageUnderstandingCount = None
        self._RejectCount = None
        self._SensitiveCount = None
        self._ConcurrentLimitCount = None
        self._UnknownIssuesCount = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ModelReplyCount(self):
        return self._ModelReplyCount

    @ModelReplyCount.setter
    def ModelReplyCount(self, ModelReplyCount):
        self._ModelReplyCount = ModelReplyCount

    @property
    def KnowledgeCount(self):
        return self._KnowledgeCount

    @KnowledgeCount.setter
    def KnowledgeCount(self, KnowledgeCount):
        self._KnowledgeCount = KnowledgeCount

    @property
    def TaskFlowCount(self):
        return self._TaskFlowCount

    @TaskFlowCount.setter
    def TaskFlowCount(self, TaskFlowCount):
        self._TaskFlowCount = TaskFlowCount

    @property
    def SearchEngineCount(self):
        return self._SearchEngineCount

    @SearchEngineCount.setter
    def SearchEngineCount(self, SearchEngineCount):
        self._SearchEngineCount = SearchEngineCount

    @property
    def ImageUnderstandingCount(self):
        return self._ImageUnderstandingCount

    @ImageUnderstandingCount.setter
    def ImageUnderstandingCount(self, ImageUnderstandingCount):
        self._ImageUnderstandingCount = ImageUnderstandingCount

    @property
    def RejectCount(self):
        return self._RejectCount

    @RejectCount.setter
    def RejectCount(self, RejectCount):
        self._RejectCount = RejectCount

    @property
    def SensitiveCount(self):
        return self._SensitiveCount

    @SensitiveCount.setter
    def SensitiveCount(self, SensitiveCount):
        self._SensitiveCount = SensitiveCount

    @property
    def ConcurrentLimitCount(self):
        return self._ConcurrentLimitCount

    @ConcurrentLimitCount.setter
    def ConcurrentLimitCount(self, ConcurrentLimitCount):
        self._ConcurrentLimitCount = ConcurrentLimitCount

    @property
    def UnknownIssuesCount(self):
        return self._UnknownIssuesCount

    @UnknownIssuesCount.setter
    def UnknownIssuesCount(self, UnknownIssuesCount):
        self._UnknownIssuesCount = UnknownIssuesCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._ModelReplyCount = params.get("ModelReplyCount")
        self._KnowledgeCount = params.get("KnowledgeCount")
        self._TaskFlowCount = params.get("TaskFlowCount")
        self._SearchEngineCount = params.get("SearchEngineCount")
        self._ImageUnderstandingCount = params.get("ImageUnderstandingCount")
        self._RejectCount = params.get("RejectCount")
        self._SensitiveCount = params.get("SensitiveCount")
        self._ConcurrentLimitCount = params.get("ConcurrentLimitCount")
        self._UnknownIssuesCount = params.get("UnknownIssuesCount")
        self._RequestId = params.get("RequestId")


class GetAppKnowledgeCountRequest(AbstractModel):
    """GetAppKnowledgeCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 类型：doc-文档；qa-问答对
        :type Type: str
        :param _AppBizId: 应用ID
        :type AppBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)	
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._Type = None
        self._AppBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AppBizId = params.get("AppBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAppKnowledgeCountResponse(AbstractModel):
    """GetAppKnowledgeCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetAppSecretRequest(AbstractModel):
    """GetAppSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用ID
        :type AppBizId: str
        """
        self._AppBizId = None

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAppSecretResponse(AbstractModel):
    """GetAppSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppKey: 应用密钥
        :type AppKey: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsRelease: 是否发布
        :type IsRelease: bool
        :param _HasPermission: 是否有查看权限
        :type HasPermission: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppKey = None
        self._CreateTime = None
        self._IsRelease = None
        self._HasPermission = None
        self._RequestId = None

    @property
    def AppKey(self):
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsRelease(self):
        return self._IsRelease

    @IsRelease.setter
    def IsRelease(self, IsRelease):
        self._IsRelease = IsRelease

    @property
    def HasPermission(self):
        return self._HasPermission

    @HasPermission.setter
    def HasPermission(self, HasPermission):
        self._HasPermission = HasPermission

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppKey = params.get("AppKey")
        self._CreateTime = params.get("CreateTime")
        self._IsRelease = params.get("IsRelease")
        self._HasPermission = params.get("HasPermission")
        self._RequestId = params.get("RequestId")


class GetDocPreviewRequest(AbstractModel):
    """GetDocPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档业务ID
        :type DocBizId: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _TypeKey: 存储类型: offline:离线文件，realtime:实时文件；为空默认为offline
        :type TypeKey: str
        """
        self._DocBizId = None
        self._BotBizId = None
        self._TypeKey = None

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def TypeKey(self):
        return self._TypeKey

    @TypeKey.setter
    def TypeKey(self, TypeKey):
        self._TypeKey = TypeKey


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._BotBizId = params.get("BotBizId")
        self._TypeKey = params.get("TypeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDocPreviewResponse(AbstractModel):
    """GetDocPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名

        :type FileName: str
        :param _FileType: 文件类型
        :type FileType: str
        :param _CosUrl: cos路径

        :type CosUrl: str
        :param _Url: cos临时地址

        :type Url: str
        :param _Bucket: cos桶

        :type Bucket: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._Url = None
        self._Bucket = None
        self._RequestId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._Url = params.get("Url")
        self._Bucket = params.get("Bucket")
        self._RequestId = params.get("RequestId")


class GetEmbeddingRequest(AbstractModel):
    """GetEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型名称
        :type Model: str
        :param _Inputs: 需要 embedding 的文本, 单条文本最大长度500个字符, 总条数最大7条
        :type Inputs: list of str
        :param _Online: 是否在线, 后台异步任务使用离线, 实时任务使用在线, 默认值: false
        :type Online: bool
        """
        self._Model = None
        self._Inputs = None
        self._Online = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Inputs(self):
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def Online(self):
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Inputs = params.get("Inputs")
        self._Online = params.get("Online")
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
        :param _Data: 特征
        :type Data: list of EmbeddingObject
        :param _Usage: 消耗量，返回TotalToken
        :type Usage: :class:`tencentcloud.lke.v20231130.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EmbeddingObject()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetLikeDataCountRequest(AbstractModel):
    """GetLikeDataCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始日期
        :type StartTime: int
        :param _EndTime: 结束日期
        :type EndTime: int
        :param _AppBizId: 应用id
        :type AppBizId: list of str
        :param _Type: 消息来源(1、分享用户端  2、对话API)
        :type Type: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._StartTime = None
        self._EndTime = None
        self._AppBizId = None
        self._Type = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AppBizId = params.get("AppBizId")
        self._Type = params.get("Type")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLikeDataCountResponse(AbstractModel):
    """GetLikeDataCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 可评价消息数
        :type Total: int
        :param _AppraisalTotal: 评价数
        :type AppraisalTotal: int
        :param _ParticipationRate: 参评率
        :type ParticipationRate: float
        :param _LikeTotal: 点赞数
        :type LikeTotal: int
        :param _LikeRate: 点赞率
        :type LikeRate: float
        :param _DislikeTotal: 点踩数
        :type DislikeTotal: int
        :param _DislikeRate: 点踩率
        :type DislikeRate: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AppraisalTotal = None
        self._ParticipationRate = None
        self._LikeTotal = None
        self._LikeRate = None
        self._DislikeTotal = None
        self._DislikeRate = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AppraisalTotal(self):
        return self._AppraisalTotal

    @AppraisalTotal.setter
    def AppraisalTotal(self, AppraisalTotal):
        self._AppraisalTotal = AppraisalTotal

    @property
    def ParticipationRate(self):
        return self._ParticipationRate

    @ParticipationRate.setter
    def ParticipationRate(self, ParticipationRate):
        self._ParticipationRate = ParticipationRate

    @property
    def LikeTotal(self):
        return self._LikeTotal

    @LikeTotal.setter
    def LikeTotal(self, LikeTotal):
        self._LikeTotal = LikeTotal

    @property
    def LikeRate(self):
        return self._LikeRate

    @LikeRate.setter
    def LikeRate(self, LikeRate):
        self._LikeRate = LikeRate

    @property
    def DislikeTotal(self):
        return self._DislikeTotal

    @DislikeTotal.setter
    def DislikeTotal(self, DislikeTotal):
        self._DislikeTotal = DislikeTotal

    @property
    def DislikeRate(self):
        return self._DislikeRate

    @DislikeRate.setter
    def DislikeRate(self, DislikeRate):
        self._DislikeRate = DislikeRate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._AppraisalTotal = params.get("AppraisalTotal")
        self._ParticipationRate = params.get("ParticipationRate")
        self._LikeTotal = params.get("LikeTotal")
        self._LikeRate = params.get("LikeRate")
        self._DislikeTotal = params.get("DislikeTotal")
        self._DislikeRate = params.get("DislikeRate")
        self._RequestId = params.get("RequestId")


class GetMsgRecordRequest(AbstractModel):
    """GetMsgRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: int
        :param _Count: 数量
        :type Count: int
        :param _SessionId: 会话sessionid
        :type SessionId: str
        :param _LastRecordId: 最后一条记录ID
        :type LastRecordId: str
        :param _BotAppKey: 应用AppKey
        :type BotAppKey: str
        :param _Scene: 场景, 体验: 1; 正式: 2
        :type Scene: int
        """
        self._Type = None
        self._Count = None
        self._SessionId = None
        self._LastRecordId = None
        self._BotAppKey = None
        self._Scene = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def LastRecordId(self):
        return self._LastRecordId

    @LastRecordId.setter
    def LastRecordId(self, LastRecordId):
        self._LastRecordId = LastRecordId

    @property
    def BotAppKey(self):
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def Scene(self):
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Count = params.get("Count")
        self._SessionId = params.get("SessionId")
        self._LastRecordId = params.get("LastRecordId")
        self._BotAppKey = params.get("BotAppKey")
        self._Scene = params.get("Scene")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMsgRecordResponse(AbstractModel):
    """GetMsgRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 会话记录
        :type Records: list of MsgRecord
        :param _SessionDisassociatedTimestamp: session 清除关联上下文时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionDisassociatedTimestamp: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._SessionDisassociatedTimestamp = None
        self._RequestId = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def SessionDisassociatedTimestamp(self):
        return self._SessionDisassociatedTimestamp

    @SessionDisassociatedTimestamp.setter
    def SessionDisassociatedTimestamp(self, SessionDisassociatedTimestamp):
        self._SessionDisassociatedTimestamp = SessionDisassociatedTimestamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = MsgRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._SessionDisassociatedTimestamp = params.get("SessionDisassociatedTimestamp")
        self._RequestId = params.get("RequestId")


class GetReconstructDocumentResultRequest(AbstractModel):
    """GetReconstructDocumentResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一id
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReconstructDocumentResultResponse(AbstractModel):
    """GetReconstructDocumentResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态: Success->执行完成；Processing->执行中；Failed->执行失败；WaitExecute->等待执行；
        :type Status: str
        :param _DocumentRecognizeResultUrl: 输入文件中嵌入的图片中文字内容的识别结果，存储在腾讯云cos的下载地址
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: 文档解析失败的页码
        :type FailedPages: list of ReconstructDocumentFailedPage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = ReconstructDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        self._RequestId = params.get("RequestId")


class GetTaskStatusRequest(AbstractModel):
    """GetTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._TaskId = None
        self._TaskType = None
        self._BotBizId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskStatusResponse(AbstractModel):
    """GetTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _TaskType: 任务类型
        :type TaskType: str
        :param _Status: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Message: 任务消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Params: 任务参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: :class:`tencentcloud.lke.v20231130.models.TaskParams`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._TaskType = None
        self._Status = None
        self._Message = None
        self._Params = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        if params.get("Params") is not None:
            self._Params = TaskParams()
            self._Params._deserialize(params.get("Params"))
        self._RequestId = params.get("RequestId")


class GetWsTokenReq_Label(AbstractModel):
    """获取ws token label

    """

    def __init__(self):
        r"""
        :param _Name: 标签名
        :type Name: str
        :param _Values: 标签值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWsTokenRequest(AbstractModel):
    """GetWsToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 接入类型
        :type Type: int
        :param _BotAppKey: 应用AppKey
        :type BotAppKey: str
        :param _VisitorBizId: 坐席ID
        :type VisitorBizId: str
        :param _VisitorLabels: 坐席标签
        :type VisitorLabels: list of GetWsTokenReq_Label
        """
        self._Type = None
        self._BotAppKey = None
        self._VisitorBizId = None
        self._VisitorLabels = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BotAppKey(self):
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def VisitorBizId(self):
        return self._VisitorBizId

    @VisitorBizId.setter
    def VisitorBizId(self, VisitorBizId):
        self._VisitorBizId = VisitorBizId

    @property
    def VisitorLabels(self):
        return self._VisitorLabels

    @VisitorLabels.setter
    def VisitorLabels(self, VisitorLabels):
        self._VisitorLabels = VisitorLabels


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._BotAppKey = params.get("BotAppKey")
        self._VisitorBizId = params.get("VisitorBizId")
        if params.get("VisitorLabels") is not None:
            self._VisitorLabels = []
            for item in params.get("VisitorLabels"):
                obj = GetWsTokenReq_Label()
                obj._deserialize(item)
                self._VisitorLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetWsTokenResponse(AbstractModel):
    """GetWsToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: token值
        :type Token: str
        :param _Balance: 余额; 余额大于 0 时表示有效.
注意：此字段可能返回 null，表示取不到有效值。
        :type Balance: float
        :param _InputLenLimit: 对话窗输入字符限制
        :type InputLenLimit: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._Balance = None
        self._InputLenLimit = None
        self._RequestId = None

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def InputLenLimit(self):
        return self._InputLenLimit

    @InputLenLimit.setter
    def InputLenLimit(self, InputLenLimit):
        self._InputLenLimit = InputLenLimit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._Balance = params.get("Balance")
        self._InputLenLimit = params.get("InputLenLimit")
        self._RequestId = params.get("RequestId")


class GroupQARequest(AbstractModel):
    """GroupQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: QA业务ID列表
        :type QaBizIds: list of str
        :param _CateBizId: 分组 ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupQAResponse(AbstractModel):
    """GroupQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Highlight(AbstractModel):
    """分片高亮内容

    """

    def __init__(self):
        r"""
        :param _StartPos: 高亮起始位置

注意：此字段可能返回 null，表示取不到有效值。
        :type StartPos: str
        :param _EndPos: 高亮结束位置

注意：此字段可能返回 null，表示取不到有效值。
        :type EndPos: str
        :param _Text: 高亮子文本

注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        """
        self._StartPos = None
        self._EndPos = None
        self._Text = None

    @property
    def StartPos(self):
        return self._StartPos

    @StartPos.setter
    def StartPos(self, StartPos):
        self._StartPos = StartPos

    @property
    def EndPos(self):
        return self._EndPos

    @EndPos.setter
    def EndPos(self, EndPos):
        self._EndPos = EndPos

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._StartPos = params.get("StartPos")
        self._EndPos = params.get("EndPos")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreUnsatisfiedReplyRequest(AbstractModel):
    """IgnoreUnsatisfiedReply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _ReplyBizIds: 不满意回复ID
        :type ReplyBizIds: list of str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._ReplyBizIds = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReplyBizIds(self):
        return self._ReplyBizIds

    @ReplyBizIds.setter
    def ReplyBizIds(self, ReplyBizIds):
        self._ReplyBizIds = ReplyBizIds

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReplyBizIds = params.get("ReplyBizIds")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreUnsatisfiedReplyResponse(AbstractModel):
    """IgnoreUnsatisfiedReply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class IsTransferIntentRequest(AbstractModel):
    """IsTransferIntent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 内容
        :type Content: str
        :param _BotAppKey: 应用appKey
        :type BotAppKey: str
        """
        self._Content = None
        self._BotAppKey = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def BotAppKey(self):
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._BotAppKey = params.get("BotAppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsTransferIntentResponse(AbstractModel):
    """IsTransferIntent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Hit: 是否意图转人工
        :type Hit: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Hit = None
        self._RequestId = None

    @property
    def Hit(self):
        return self._Hit

    @Hit.setter
    def Hit(self, Hit):
        self._Hit = Hit

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Hit = params.get("Hit")
        self._RequestId = params.get("RequestId")


class KnowledgeQaConfig(AbstractModel):
    """知识问答配置

    """

    def __init__(self):
        r"""
        :param _Greeting: 欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Greeting: str
        :param _RoleDescription: 角色描述，300字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleDescription: str
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Search: 知识搜索配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Search: list of KnowledgeQaSearch
        :param _Output: 知识管理输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.lke.v20231130.models.KnowledgeQaOutput`
        """
        self._Greeting = None
        self._RoleDescription = None
        self._Model = None
        self._Search = None
        self._Output = None

    @property
    def Greeting(self):
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting

    @property
    def RoleDescription(self):
        return self._RoleDescription

    @RoleDescription.setter
    def RoleDescription(self, RoleDescription):
        self._RoleDescription = RoleDescription

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Search(self):
        return self._Search

    @Search.setter
    def Search(self, Search):
        self._Search = Search

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._Greeting = params.get("Greeting")
        self._RoleDescription = params.get("RoleDescription")
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Search") is not None:
            self._Search = []
            for item in params.get("Search"):
                obj = KnowledgeQaSearch()
                obj._deserialize(item)
                self._Search.append(obj)
        if params.get("Output") is not None:
            self._Output = KnowledgeQaOutput()
            self._Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaOutput(AbstractModel):
    """应用管理输出配置

    """

    def __init__(self):
        r"""
        :param _Method: 输出方式 1：流式 2：非流式
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: int
        :param _UseGeneralKnowledge: 通用模型回复
注意：此字段可能返回 null，表示取不到有效值。
        :type UseGeneralKnowledge: bool
        :param _BareAnswer: 未知回复语，300字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type BareAnswer: str
        :param _ShowQuestionClarify: 是否展示问题澄清开关
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowQuestionClarify: bool
        :param _UseQuestionClarify: 是否打开问题澄清
注意：此字段可能返回 null，表示取不到有效值。
        :type UseQuestionClarify: bool
        :param _QuestionClarifyKeywords: 问题澄清关键词列表
注意：此字段可能返回 null，表示取不到有效值。
        :type QuestionClarifyKeywords: list of str
        """
        self._Method = None
        self._UseGeneralKnowledge = None
        self._BareAnswer = None
        self._ShowQuestionClarify = None
        self._UseQuestionClarify = None
        self._QuestionClarifyKeywords = None

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def UseGeneralKnowledge(self):
        return self._UseGeneralKnowledge

    @UseGeneralKnowledge.setter
    def UseGeneralKnowledge(self, UseGeneralKnowledge):
        self._UseGeneralKnowledge = UseGeneralKnowledge

    @property
    def BareAnswer(self):
        return self._BareAnswer

    @BareAnswer.setter
    def BareAnswer(self, BareAnswer):
        self._BareAnswer = BareAnswer

    @property
    def ShowQuestionClarify(self):
        return self._ShowQuestionClarify

    @ShowQuestionClarify.setter
    def ShowQuestionClarify(self, ShowQuestionClarify):
        self._ShowQuestionClarify = ShowQuestionClarify

    @property
    def UseQuestionClarify(self):
        return self._UseQuestionClarify

    @UseQuestionClarify.setter
    def UseQuestionClarify(self, UseQuestionClarify):
        self._UseQuestionClarify = UseQuestionClarify

    @property
    def QuestionClarifyKeywords(self):
        return self._QuestionClarifyKeywords

    @QuestionClarifyKeywords.setter
    def QuestionClarifyKeywords(self, QuestionClarifyKeywords):
        self._QuestionClarifyKeywords = QuestionClarifyKeywords


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._UseGeneralKnowledge = params.get("UseGeneralKnowledge")
        self._BareAnswer = params.get("BareAnswer")
        self._ShowQuestionClarify = params.get("ShowQuestionClarify")
        self._UseQuestionClarify = params.get("UseQuestionClarify")
        self._QuestionClarifyKeywords = params.get("QuestionClarifyKeywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeQaSearch(AbstractModel):
    """检索配置

    """

    def __init__(self):
        r"""
        :param _Type: 知识来源 doc：文档，qa：问答  taskflow：业务流程，search：搜索增强
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ReplyFlexibility: 问答-回复灵活度 1：已采纳答案直接回复 2：已采纳润色后回复
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyFlexibility: int
        :param _UseSearchEngine: 搜索增强-搜索引擎状态
注意：此字段可能返回 null，表示取不到有效值。
        :type UseSearchEngine: bool
        :param _ShowSearchEngine: 是否显示搜索引擎检索状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowSearchEngine: bool
        :param _IsEnabled: 知识来源，是否选择
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEnabled: bool
        :param _QaTopN: 问答最大召回数量, 默认2，限制5
注意：此字段可能返回 null，表示取不到有效值。
        :type QaTopN: int
        :param _DocTopN: 文档最大召回数量, 默认3，限制5
注意：此字段可能返回 null，表示取不到有效值。
        :type DocTopN: int
        :param _Confidence: 检索置信度，针对文档和问答有效，最小0.01，最大0.99
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        """
        self._Type = None
        self._ReplyFlexibility = None
        self._UseSearchEngine = None
        self._ShowSearchEngine = None
        self._IsEnabled = None
        self._QaTopN = None
        self._DocTopN = None
        self._Confidence = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ReplyFlexibility(self):
        return self._ReplyFlexibility

    @ReplyFlexibility.setter
    def ReplyFlexibility(self, ReplyFlexibility):
        self._ReplyFlexibility = ReplyFlexibility

    @property
    def UseSearchEngine(self):
        return self._UseSearchEngine

    @UseSearchEngine.setter
    def UseSearchEngine(self, UseSearchEngine):
        self._UseSearchEngine = UseSearchEngine

    @property
    def ShowSearchEngine(self):
        return self._ShowSearchEngine

    @ShowSearchEngine.setter
    def ShowSearchEngine(self, ShowSearchEngine):
        self._ShowSearchEngine = ShowSearchEngine

    @property
    def IsEnabled(self):
        return self._IsEnabled

    @IsEnabled.setter
    def IsEnabled(self, IsEnabled):
        self._IsEnabled = IsEnabled

    @property
    def QaTopN(self):
        return self._QaTopN

    @QaTopN.setter
    def QaTopN(self, QaTopN):
        self._QaTopN = QaTopN

    @property
    def DocTopN(self):
        return self._DocTopN

    @DocTopN.setter
    def DocTopN(self, DocTopN):
        self._DocTopN = DocTopN

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ReplyFlexibility = params.get("ReplyFlexibility")
        self._UseSearchEngine = params.get("UseSearchEngine")
        self._ShowSearchEngine = params.get("ShowSearchEngine")
        self._IsEnabled = params.get("IsEnabled")
        self._QaTopN = params.get("QaTopN")
        self._DocTopN = params.get("DocTopN")
        self._Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """标签ID

    """

    def __init__(self):
        r"""
        :param _LabelBizId: 标签ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelBizId: str
        :param _LabelName: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        """
        self._LabelBizId = None
        self._LabelName = None

    @property
    def LabelBizId(self):
        return self._LabelBizId

    @LabelBizId.setter
    def LabelBizId(self, LabelBizId):
        self._LabelBizId = LabelBizId

    @property
    def LabelName(self):
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName


    def _deserialize(self, params):
        self._LabelBizId = params.get("LabelBizId")
        self._LabelName = params.get("LabelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppCategoryRequest(AbstractModel):
    """ListAppCategory请求参数结构体

    """


class ListAppCategoryResponse(AbstractModel):
    """ListAppCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 应用类型列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of ListAppCategoryRspOption
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListAppCategoryRspOption()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAppCategoryRspOption(AbstractModel):
    """应用类型详情

    """

    def __init__(self):
        r"""
        :param _Text: 类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Value: 类型值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Logo: 类型log
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        """
        self._Text = None
        self._Value = None
        self._Logo = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        self._Logo = params.get("Logo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppRequest(AbstractModel):
    """ListApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _PageSize: 每页数目，整型
        :type PageSize: int
        :param _PageNumber: 页码，整型
        :type PageNumber: int
        :param _Keyword: 关键词：应用/修改人
        :type Keyword: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._AppType = None
        self._PageSize = None
        self._PageNumber = None
        self._Keyword = None
        self._LoginSubAccountUin = None

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._Keyword = params.get("Keyword")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAppResponse(AbstractModel):
    """ListApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数量
        :type Total: str
        :param _List: 标签列表
        :type List: list of AppInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AppInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListAttributeLabelRequest(AbstractModel):
    """ListAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Query: 查询内容
        :type Query: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttributeLabelResponse(AbstractModel):
    """ListAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: str
        :param _List: 列表
        :type List: list of AttrLabelDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttrLabelDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListDocItem(AbstractModel):
    """文档列表详情描述

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocBizId: str
        :param _FileName: 文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _CosUrl: cos路径
注意：此字段可能返回 null，表示取不到有效值。
        :type CosUrl: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Status: 文档状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusDesc: 文档状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param _IsRefer: 答案中是否引用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRefer: bool
        :param _QaNum: 问答对数量
注意：此字段可能返回 null，表示取不到有效值。
        :type QaNum: int
        :param _IsDeleted: 是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeleted: bool
        :param _Source: 文档来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param _SourceDesc: 文档来源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceDesc: str
        :param _IsAllowRestart: 是否允许重新生成
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowRestart: bool
        :param _IsDeletedQa: qa是否已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDeletedQa: bool
        :param _IsCreatingQa: 问答是否生成中
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCreatingQa: bool
        :param _IsAllowDelete: 是否允许删除
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowDelete: bool
        :param _IsAllowRefer: 是否允许操作引用开关
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowRefer: bool
        :param _IsCreatedQa: 问答是否生成过
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCreatedQa: bool
        :param _DocCharSize: 文档字符量
注意：此字段可能返回 null，表示取不到有效值。
        :type DocCharSize: str
        :param _AttrRange: 属性标签适用范围
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrRange: int
        :param _AttrLabels: 属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :type AttrLabels: list of AttrLabel
        :param _IsAllowEdit: 是否允许编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowEdit: bool
        :param _ReferUrlType: 外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReferUrlType: int
        :param _WebUrl: 网页(或自定义链接)地址
注意：此字段可能返回 null，表示取不到有效值。
        :type WebUrl: str
        :param _ExpireStart: 有效开始时间，unix时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireEnd: str
        """
        self._DocBizId = None
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._IsRefer = None
        self._QaNum = None
        self._IsDeleted = None
        self._Source = None
        self._SourceDesc = None
        self._IsAllowRestart = None
        self._IsDeletedQa = None
        self._IsCreatingQa = None
        self._IsAllowDelete = None
        self._IsAllowRefer = None
        self._IsCreatedQa = None
        self._DocCharSize = None
        self._AttrRange = None
        self._AttrLabels = None
        self._IsAllowEdit = None
        self._ReferUrlType = None
        self._WebUrl = None
        self._ExpireStart = None
        self._ExpireEnd = None

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def IsRefer(self):
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def QaNum(self):
        return self._QaNum

    @QaNum.setter
    def QaNum(self, QaNum):
        self._QaNum = QaNum

    @property
    def IsDeleted(self):
        return self._IsDeleted

    @IsDeleted.setter
    def IsDeleted(self, IsDeleted):
        self._IsDeleted = IsDeleted

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def IsAllowRestart(self):
        return self._IsAllowRestart

    @IsAllowRestart.setter
    def IsAllowRestart(self, IsAllowRestart):
        self._IsAllowRestart = IsAllowRestart

    @property
    def IsDeletedQa(self):
        return self._IsDeletedQa

    @IsDeletedQa.setter
    def IsDeletedQa(self, IsDeletedQa):
        self._IsDeletedQa = IsDeletedQa

    @property
    def IsCreatingQa(self):
        return self._IsCreatingQa

    @IsCreatingQa.setter
    def IsCreatingQa(self, IsCreatingQa):
        self._IsCreatingQa = IsCreatingQa

    @property
    def IsAllowDelete(self):
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowRefer(self):
        return self._IsAllowRefer

    @IsAllowRefer.setter
    def IsAllowRefer(self, IsAllowRefer):
        self._IsAllowRefer = IsAllowRefer

    @property
    def IsCreatedQa(self):
        return self._IsCreatedQa

    @IsCreatedQa.setter
    def IsCreatedQa(self, IsCreatedQa):
        self._IsCreatedQa = IsCreatedQa

    @property
    def DocCharSize(self):
        return self._DocCharSize

    @DocCharSize.setter
    def DocCharSize(self, DocCharSize):
        self._DocCharSize = DocCharSize

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def IsAllowEdit(self):
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def ReferUrlType(self):
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def WebUrl(self):
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def ExpireStart(self):
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._IsRefer = params.get("IsRefer")
        self._QaNum = params.get("QaNum")
        self._IsDeleted = params.get("IsDeleted")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._IsAllowRestart = params.get("IsAllowRestart")
        self._IsDeletedQa = params.get("IsDeletedQa")
        self._IsCreatingQa = params.get("IsCreatingQa")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowRefer = params.get("IsAllowRefer")
        self._IsCreatedQa = params.get("IsCreatedQa")
        self._DocCharSize = params.get("DocCharSize")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabel()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._ReferUrlType = params.get("ReferUrlType")
        self._WebUrl = params.get("WebUrl")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocRequest(AbstractModel):
    """ListDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _Query: 查询内容
        :type Query: str
        :param _Status: 文档状态： 7 审核中、8 审核失败、10 待发布、11 发布中、12 已发布、13 学习中、14 学习失败 20 已过期
        :type Status: list of int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._Status = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocResponse(AbstractModel):
    """ListDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ListDocItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListDocItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListModelRequest(AbstractModel):
    """ListModel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)	
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        """
        self._AppType = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._AppType = params.get("AppType")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListModelResponse(AbstractModel):
    """ListModel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 模型列表
        :type List: list of ModelInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ModelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQACateRequest(AbstractModel):
    """ListQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        """
        self._BotBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListQACateResponse(AbstractModel):
    """ListQACate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 列表
        :type List: list of QACate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = QACate()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQARequest(AbstractModel):
    """ListQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页大小
        :type PageSize: int
        :param _Query: 查询问题
        :type Query: str
        :param _AcceptStatus: 校验状态(1未校验2采纳3不采纳)
        :type AcceptStatus: list of int
        :param _ReleaseStatus: 发布状态(2待发布 3发布中 4已发布 7审核中 8审核失败 9人工申述中 11人工申述失败)
        :type ReleaseStatus: list of int
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _Source: 来源(1 文档生成 2 批量导入 3 手动添加)
        :type Source: int
        :param _QueryAnswer: 查询答案
        :type QueryAnswer: str
        :param _QaBizIds: QA业务ID列表
        :type QaBizIds: list of str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._AcceptStatus = None
        self._ReleaseStatus = None
        self._DocBizId = None
        self._Source = None
        self._QueryAnswer = None
        self._QaBizIds = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def AcceptStatus(self):
        return self._AcceptStatus

    @AcceptStatus.setter
    def AcceptStatus(self, AcceptStatus):
        self._AcceptStatus = AcceptStatus

    @property
    def ReleaseStatus(self):
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def QueryAnswer(self):
        return self._QueryAnswer

    @QueryAnswer.setter
    def QueryAnswer(self, QueryAnswer):
        self._QueryAnswer = QueryAnswer

    @property
    def QaBizIds(self):
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._AcceptStatus = params.get("AcceptStatus")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._DocBizId = params.get("DocBizId")
        self._Source = params.get("Source")
        self._QueryAnswer = params.get("QueryAnswer")
        self._QaBizIds = params.get("QaBizIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListQAResponse(AbstractModel):
    """ListQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 问答数量
        :type Total: str
        :param _WaitVerifyTotal: 待校验问答数量
        :type WaitVerifyTotal: str
        :param _NotAcceptedTotal: 未采纳问答数量
        :type NotAcceptedTotal: str
        :param _AcceptedTotal: 已采纳问答数量
        :type AcceptedTotal: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _List: 问答详情
        :type List: list of ListQaItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._WaitVerifyTotal = None
        self._NotAcceptedTotal = None
        self._AcceptedTotal = None
        self._PageNumber = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def WaitVerifyTotal(self):
        return self._WaitVerifyTotal

    @WaitVerifyTotal.setter
    def WaitVerifyTotal(self, WaitVerifyTotal):
        self._WaitVerifyTotal = WaitVerifyTotal

    @property
    def NotAcceptedTotal(self):
        return self._NotAcceptedTotal

    @NotAcceptedTotal.setter
    def NotAcceptedTotal(self, NotAcceptedTotal):
        self._NotAcceptedTotal = NotAcceptedTotal

    @property
    def AcceptedTotal(self):
        return self._AcceptedTotal

    @AcceptedTotal.setter
    def AcceptedTotal(self, AcceptedTotal):
        self._AcceptedTotal = AcceptedTotal

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._WaitVerifyTotal = params.get("WaitVerifyTotal")
        self._NotAcceptedTotal = params.get("NotAcceptedTotal")
        self._AcceptedTotal = params.get("AcceptedTotal")
        self._PageNumber = params.get("PageNumber")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListQaItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQaItem(AbstractModel):
    """问答详情数据

    """

    def __init__(self):
        r"""
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        :param _Source: 来源
        :type Source: int
        :param _SourceDesc: 来源描述
        :type SourceDesc: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 状态
        :type Status: int
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsAllowEdit: 是否允许编辑
        :type IsAllowEdit: bool
        :param _IsAllowDelete: 是否允许删除
        :type IsAllowDelete: bool
        :param _IsAllowAccept: 是否允许校验
        :type IsAllowAccept: bool
        :param _FileName: 文档名称
        :type FileName: str
        :param _FileType: 文档类型
        :type FileType: str
        :param _QaCharSize: 问答字符数
        :type QaCharSize: str
        """
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._Source = None
        self._SourceDesc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._DocBizId = None
        self._CreateTime = None
        self._IsAllowEdit = None
        self._IsAllowDelete = None
        self._IsAllowAccept = None
        self._FileName = None
        self._FileType = None
        self._QaCharSize = None

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsAllowEdit(self):
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def IsAllowDelete(self):
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete

    @property
    def IsAllowAccept(self):
        return self._IsAllowAccept

    @IsAllowAccept.setter
    def IsAllowAccept(self, IsAllowAccept):
        self._IsAllowAccept = IsAllowAccept

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def QaCharSize(self):
        return self._QaCharSize

    @QaCharSize.setter
    def QaCharSize(self, QaCharSize):
        self._QaCharSize = QaCharSize


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._DocBizId = params.get("DocBizId")
        self._CreateTime = params.get("CreateTime")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._IsAllowDelete = params.get("IsAllowDelete")
        self._IsAllowAccept = params.get("IsAllowAccept")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._QaCharSize = params.get("QaCharSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRejectedQuestionPreviewRequest(AbstractModel):
    """ListRejectedQuestionPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _Query: 查询内容
        :type Query: str
        :param _ReleaseBizId: 发布单ID
        :type ReleaseBizId: str
        :param _Actions: 状态(1新增2更新3删除)
        :type Actions: list of int non-negative
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._Actions = None
        self._StartTime = None
        self._EndTime = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Actions = params.get("Actions")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRejectedQuestionPreviewResponse(AbstractModel):
    """ListRejectedQuestionPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ReleaseRejectedQuestion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseRejectedQuestion()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListRejectedQuestionRequest(AbstractModel):
    """ListRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码

        :type PageNumber: int
        :param _PageSize: 每页数量

        :type PageSize: int
        :param _Query: 查询内容

        :type Query: str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRejectedQuestionResponse(AbstractModel):
    """ListRejectedQuestion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: str
        :param _List: 拒答问题列表
        :type List: list of RejectedQuestion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RejectedQuestion()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseConfigPreviewRequest(AbstractModel):
    """ListReleaseConfigPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _Query: 查询内容
        :type Query: str
        :param _ReleaseBizId: 发布单ID
        :type ReleaseBizId: str
        :param _Actions: 状态(1新增2更新3删除)
        :type Actions: list of int non-negative
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _ReleaseStatus: 发布状态
        :type ReleaseStatus: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._Actions = None
        self._StartTime = None
        self._EndTime = None
        self._ReleaseStatus = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ReleaseStatus(self):
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Actions = params.get("Actions")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReleaseStatus = params.get("ReleaseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseConfigPreviewResponse(AbstractModel):
    """ListReleaseConfigPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数量
        :type Total: str
        :param _List: 配置项列表
        :type List: list of ReleaseConfigs
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseConfigs()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseDocPreviewRequest(AbstractModel):
    """ListReleaseDocPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _Query: 查询内容
        :type Query: str
        :param _ReleaseBizId: 发布业务ID
        :type ReleaseBizId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Actions: 状态(1新增2修改3删除)
        :type Actions: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._StartTime = None
        self._EndTime = None
        self._Actions = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Actions = params.get("Actions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseDocPreviewResponse(AbstractModel):
    """ListReleaseDocPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ReleaseDoc
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseDoc()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseItem(AbstractModel):
    """发布列表详情

    """

    def __init__(self):
        r"""
        :param _ReleaseBizId: 版本ID
        :type ReleaseBizId: str
        :param _Operator: 发布人
        :type Operator: str
        :param _Desc: 发布描述
        :type Desc: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Status: 发布状态
        :type Status: int
        :param _StatusDesc: 发布状态描述
        :type StatusDesc: str
        :param _Reason: 失败原因
        :type Reason: str
        :param _SuccessCount: 发布成功数
        :type SuccessCount: int
        :param _FailCount: 发布失败数
        :type FailCount: int
        """
        self._ReleaseBizId = None
        self._Operator = None
        self._Desc = None
        self._UpdateTime = None
        self._Status = None
        self._StatusDesc = None
        self._Reason = None
        self._SuccessCount = None
        self._FailCount = None

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def SuccessCount(self):
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount


    def _deserialize(self, params):
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._Operator = params.get("Operator")
        self._Desc = params.get("Desc")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Reason = params.get("Reason")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseQAPreviewRequest(AbstractModel):
    """ListReleaseQAPreview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        :param _Query: 查询内容
        :type Query: str
        :param _ReleaseBizId: 发布单ID
        :type ReleaseBizId: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Actions: 状态(1新增2修改3删除)
        :type Actions: list of int non-negative
        :param _ReleaseStatus: 发布状态(4发布成功5发布失败)
        :type ReleaseStatus: list of int non-negative
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._ReleaseBizId = None
        self._StartTime = None
        self._EndTime = None
        self._Actions = None
        self._ReleaseStatus = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def ReleaseStatus(self):
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._ReleaseBizId = params.get("ReleaseBizId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Actions = params.get("Actions")
        self._ReleaseStatus = params.get("ReleaseStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseQAPreviewResponse(AbstractModel):
    """ListReleaseQAPreview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 文档数量
        :type Total: str
        :param _List: 文档列表
        :type List: list of ReleaseQA
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ReleaseQA()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListReleaseRequest(AbstractModel):
    """ListRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页数量
        :type PageSize: int
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReleaseResponse(AbstractModel):
    """ListRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 发布列表数量
        :type Total: str
        :param _List: 发布列表
        :type List: list of ListReleaseItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListReleaseItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListSelectDocRequest(AbstractModel):
    """ListSelectDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _FileName: 文档名称

        :type FileName: str
        :param _Status: 文档状态： 7 审核中、8 审核失败、10 待发布、11 发布中、12 已发布、13 学习中、14 学习失败 20 已过期
        :type Status: list of int
        """
        self._BotBizId = None
        self._FileName = None
        self._Status = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSelectDocResponse(AbstractModel):
    """ListSelectDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 下拉框内容
        :type List: list of Option
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Option()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListUnsatisfiedReplyRequest(AbstractModel):
    """ListUnsatisfiedReply请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 分页数量
        :type PageSize: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _Query: 用户请求(问题或答案)
        :type Query: str
        :param _Reasons: 错误类型检索
        :type Reasons: list of str
        """
        self._BotBizId = None
        self._PageNumber = None
        self._PageSize = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._Query = None
        self._Reasons = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Reasons(self):
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._Query = params.get("Query")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUnsatisfiedReplyResponse(AbstractModel):
    """ListUnsatisfiedReply返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: str
        :param _List: 不满意回复列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of UnsatisfiedReply
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._List = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UnsatisfiedReply()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class Message(AbstractModel):
    """一条message代表一条对话记录
    role表示角色  user或者assistant
    content表示对话内容

    """

    def __init__(self):
        r"""
        :param _Role: role表示角色  user标识用户提问，assistant标识返回的答案

注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _Content: 对话内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
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
        


class ModelInfo(AbstractModel):
    """模型信息

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelName: str
        :param _ModelDesc: 模型描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelDesc: str
        :param _AliasName: 模型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        """
        self._ModelName = None
        self._ModelDesc = None
        self._AliasName = None

    @property
    def ModelName(self):
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelDesc(self):
        return self._ModelDesc

    @ModelDesc.setter
    def ModelDesc(self, ModelDesc):
        self._ModelDesc = ModelDesc

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._ModelDesc = params.get("ModelDesc")
        self._AliasName = params.get("AliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppRequest(AbstractModel):
    """ModifyApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用 ID
        :type AppBizId: str
        :param _AppType: 应用类型；knowledge_qa-知识问答管理；summary-知识摘要；classifys-知识标签提取
        :type AppType: str
        :param _BaseConfig: 应用基础配置
        :type BaseConfig: :class:`tencentcloud.lke.v20231130.models.BaseConfig`
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)	
        :type LoginSubAccountUin: str
        :param _AppConfig: 应用配置
        :type AppConfig: :class:`tencentcloud.lke.v20231130.models.AppConfig`
        """
        self._AppBizId = None
        self._AppType = None
        self._BaseConfig = None
        self._LoginSubAccountUin = None
        self._AppConfig = None

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def BaseConfig(self):
        return self._BaseConfig

    @BaseConfig.setter
    def BaseConfig(self, BaseConfig):
        self._BaseConfig = BaseConfig

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AppConfig(self):
        return self._AppConfig

    @AppConfig.setter
    def AppConfig(self, AppConfig):
        self._AppConfig = AppConfig


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._AppType = params.get("AppType")
        if params.get("BaseConfig") is not None:
            self._BaseConfig = BaseConfig()
            self._BaseConfig._deserialize(params.get("BaseConfig"))
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        if params.get("AppConfig") is not None:
            self._AppConfig = AppConfig()
            self._AppConfig._deserialize(params.get("AppConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppResponse(AbstractModel):
    """ModifyApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppBizId: 应用App
注意：此字段可能返回 null，表示取不到有效值。
        :type AppBizId: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppBizId = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def AppBizId(self):
        return self._AppBizId

    @AppBizId.setter
    def AppBizId(self, AppBizId):
        self._AppBizId = AppBizId

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppBizId = params.get("AppBizId")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ModifyAttributeLabelRequest(AbstractModel):
    """ModifyAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _AttributeBizId: 属性ID
        :type AttributeBizId: str
        :param _AttrKey: 属性标识
        :type AttrKey: str
        :param _AttrName: 属性名称
        :type AttrName: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _DeleteLabelBizIds: 删除的属性标签
        :type DeleteLabelBizIds: list of str
        :param _Labels: 新增或编辑的属性标签
        :type Labels: list of AttributeLabel
        """
        self._BotBizId = None
        self._AttributeBizId = None
        self._AttrKey = None
        self._AttrName = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._DeleteLabelBizIds = None
        self._Labels = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def AttributeBizId(self):
        return self._AttributeBizId

    @AttributeBizId.setter
    def AttributeBizId(self, AttributeBizId):
        self._AttributeBizId = AttributeBizId

    @property
    def AttrKey(self):
        return self._AttrKey

    @AttrKey.setter
    def AttrKey(self, AttrKey):
        self._AttrKey = AttrKey

    @property
    def AttrName(self):
        return self._AttrName

    @AttrName.setter
    def AttrName(self, AttrName):
        self._AttrName = AttrName

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def DeleteLabelBizIds(self):
        return self._DeleteLabelBizIds

    @DeleteLabelBizIds.setter
    def DeleteLabelBizIds(self, DeleteLabelBizIds):
        self._DeleteLabelBizIds = DeleteLabelBizIds

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._AttributeBizId = params.get("AttributeBizId")
        self._AttrKey = params.get("AttrKey")
        self._AttrName = params.get("AttrName")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._DeleteLabelBizIds = params.get("DeleteLabelBizIds")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabel()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAttributeLabelResponse(AbstractModel):
    """ModifyAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyDocAttrRangeRequest(AbstractModel):
    """ModifyDocAttrRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizIds: 文档ID
        :type DocBizIds: list of str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _AttrLabels: 属性标签引用
        :type AttrLabels: list of AttrLabelRefer
        """
        self._BotBizId = None
        self._DocBizIds = None
        self._AttrRange = None
        self._AttrLabels = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizIds(self):
        return self._DocBizIds

    @DocBizIds.setter
    def DocBizIds(self, DocBizIds):
        self._DocBizIds = DocBizIds

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizIds = params.get("DocBizIds")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocAttrRangeResponse(AbstractModel):
    """ModifyDocAttrRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDocRequest(AbstractModel):
    """ModifyDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _IsRefer: 是否引用链接
        :type IsRefer: bool
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        :param _AttrLabels: 适用范围，关联的属性标签
        :type AttrLabels: list of AttrLabelRefer
        :param _WebUrl: 网页(或自定义链接)地址
        :type WebUrl: str
        :param _ReferUrlType: 外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
        :type ReferUrlType: int
        :param _ExpireStart: 有效开始时间，unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        """
        self._BotBizId = None
        self._DocBizId = None
        self._IsRefer = None
        self._AttrRange = None
        self._LoginUin = None
        self._LoginSubAccountUin = None
        self._AttrLabels = None
        self._WebUrl = None
        self._ReferUrlType = None
        self._ExpireStart = None
        self._ExpireEnd = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def IsRefer(self):
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def WebUrl(self):
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def ReferUrlType(self):
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def ExpireStart(self):
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        self._IsRefer = params.get("IsRefer")
        self._AttrRange = params.get("AttrRange")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._WebUrl = params.get("WebUrl")
        self._ReferUrlType = params.get("ReferUrlType")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDocResponse(AbstractModel):
    """ModifyDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyQAAttrRangeRequest(AbstractModel):
    """ModifyQAAttrRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizIds: 问答ID
        :type QaBizIds: list of str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _AttrLabels: 属性标签引用
        :type AttrLabels: list of AttrLabelRefer
        """
        self._BotBizId = None
        self._QaBizIds = None
        self._AttrRange = None
        self._AttrLabels = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizIds(self):
        return self._QaBizIds

    @QaBizIds.setter
    def QaBizIds(self, QaBizIds):
        self._QaBizIds = QaBizIds

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizIds = params.get("QaBizIds")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQAAttrRangeResponse(AbstractModel):
    """ModifyQAAttrRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyQACateRequest(AbstractModel):
    """ModifyQACate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Name: 分类名称

        :type Name: str
        :param _CateBizId: 分类业务ID
        :type CateBizId: str
        """
        self._BotBizId = None
        self._Name = None
        self._CateBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Name = params.get("Name")
        self._CateBizId = params.get("CateBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQACateResponse(AbstractModel):
    """ModifyQACate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyQARequest(AbstractModel):
    """ModifyQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        :param _CustomParam: 自定义参数
        :type CustomParam: str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件
        :type AttrRange: int
        :param _AttrLabels: 属性标签引用
        :type AttrLabels: list of AttrLabelRefer
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _ExpireStart: 有效开始时间，unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        """
        self._BotBizId = None
        self._QaBizId = None
        self._Question = None
        self._Answer = None
        self._CustomParam = None
        self._AttrRange = None
        self._AttrLabels = None
        self._DocBizId = None
        self._CateBizId = None
        self._ExpireStart = None
        self._ExpireEnd = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def CustomParam(self):
        return self._CustomParam

    @CustomParam.setter
    def CustomParam(self, CustomParam):
        self._CustomParam = CustomParam

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def ExpireStart(self):
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._QaBizId = params.get("QaBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._CustomParam = params.get("CustomParam")
        self._AttrRange = params.get("AttrRange")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._DocBizId = params.get("DocBizId")
        self._CateBizId = params.get("CateBizId")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQAResponse(AbstractModel):
    """ModifyQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRejectedQuestionRequest(AbstractModel):
    """ModifyRejectedQuestion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Question: 拒答问题


        :type Question: str
        :param _RejectedBizId: 拒答问题来源的数据源唯一id



        :type RejectedBizId: str
        """
        self._BotBizId = None
        self._Question = None
        self._RejectedBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def RejectedBizId(self):
        return self._RejectedBizId

    @RejectedBizId.setter
    def RejectedBizId(self, RejectedBizId):
        self._RejectedBizId = RejectedBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._Question = params.get("Question")
        self._RejectedBizId = params.get("RejectedBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRejectedQuestionResponse(AbstractModel):
    """ModifyRejectedQuestion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MsgFileInfo(AbstractModel):
    """文档信息

    """

    def __init__(self):
        r"""
        :param _FileName: 文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _FileSize: 文档大小
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: str
        :param _FileUrl: 文档URL
注意：此字段可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param _FileType: 文档类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        :param _DocId: 文档ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DocId: str
        """
        self._FileName = None
        self._FileSize = None
        self._FileUrl = None
        self._FileType = None
        self._DocId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def DocId(self):
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        self._DocId = params.get("DocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecord(AbstractModel):
    """消息详情

    """

    def __init__(self):
        r"""
        :param _Content: 内容
        :type Content: str
        :param _SessionId: 当前记录所对应的 Session ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _RecordId: 记录ID
        :type RecordId: str
        :param _RelatedRecordId: 关联记录ID
        :type RelatedRecordId: str
        :param _IsFromSelf: 是否来自自己
        :type IsFromSelf: bool
        :param _FromName: 发送者名称
        :type FromName: str
        :param _FromAvatar: 发送者头像
        :type FromAvatar: str
        :param _Timestamp: 时间戳
        :type Timestamp: str
        :param _HasRead: 是否已读
        :type HasRead: bool
        :param _Score: 评价
        :type Score: int
        :param _CanRating: 是否评分
        :type CanRating: bool
        :param _CanFeedback: 是否展示反馈按钮
注意：此字段可能返回 null，表示取不到有效值。
        :type CanFeedback: bool
        :param _Type: 记录类型
        :type Type: int
        :param _References: 引用来源
        :type References: list of MsgRecordReference
        :param _Reasons: 评价原因
        :type Reasons: list of str
        :param _IsLlmGenerated: 是否大模型
        :type IsLlmGenerated: bool
        :param _ImageUrls: 图片链接，可公有读
        :type ImageUrls: list of str
        :param _TokenStat: 当次 token 统计信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenStat: :class:`tencentcloud.lke.v20231130.models.TokenStat`
        :param _ReplyMethod: 回复方式
1:大模型直接回复;
2:保守回复, 未知问题回复;
3:拒答问题回复;
4:敏感回复;
5:问答对直接回复, 已采纳问答对优先回复;
6:欢迎语回复;
7:并发超限回复;
8:全局干预知识;
9:任务流程过程回复, 当历史记录中 task_flow.type = 0 时, 为大模型回复;
10:任务流程答案回复;
11:搜索引擎回复;
12:知识润色后回复;
13:图片理解回复;
14:实时文档回复;
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyMethod: int
        :param _OptionCards: 选项卡, 用于多轮对话
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionCards: list of str
        :param _TaskFlow: 任务信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFlow: :class:`tencentcloud.lke.v20231130.models.TaskFlowInfo`
        :param _FileInfos: 用户传入的文件信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FileInfos: list of FileInfo
        """
        self._Content = None
        self._SessionId = None
        self._RecordId = None
        self._RelatedRecordId = None
        self._IsFromSelf = None
        self._FromName = None
        self._FromAvatar = None
        self._Timestamp = None
        self._HasRead = None
        self._Score = None
        self._CanRating = None
        self._CanFeedback = None
        self._Type = None
        self._References = None
        self._Reasons = None
        self._IsLlmGenerated = None
        self._ImageUrls = None
        self._TokenStat = None
        self._ReplyMethod = None
        self._OptionCards = None
        self._TaskFlow = None
        self._FileInfos = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RelatedRecordId(self):
        return self._RelatedRecordId

    @RelatedRecordId.setter
    def RelatedRecordId(self, RelatedRecordId):
        self._RelatedRecordId = RelatedRecordId

    @property
    def IsFromSelf(self):
        return self._IsFromSelf

    @IsFromSelf.setter
    def IsFromSelf(self, IsFromSelf):
        self._IsFromSelf = IsFromSelf

    @property
    def FromName(self):
        return self._FromName

    @FromName.setter
    def FromName(self, FromName):
        self._FromName = FromName

    @property
    def FromAvatar(self):
        return self._FromAvatar

    @FromAvatar.setter
    def FromAvatar(self, FromAvatar):
        self._FromAvatar = FromAvatar

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def HasRead(self):
        return self._HasRead

    @HasRead.setter
    def HasRead(self, HasRead):
        self._HasRead = HasRead

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def CanRating(self):
        return self._CanRating

    @CanRating.setter
    def CanRating(self, CanRating):
        self._CanRating = CanRating

    @property
    def CanFeedback(self):
        return self._CanFeedback

    @CanFeedback.setter
    def CanFeedback(self, CanFeedback):
        self._CanFeedback = CanFeedback

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def References(self):
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def Reasons(self):
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons

    @property
    def IsLlmGenerated(self):
        return self._IsLlmGenerated

    @IsLlmGenerated.setter
    def IsLlmGenerated(self, IsLlmGenerated):
        self._IsLlmGenerated = IsLlmGenerated

    @property
    def ImageUrls(self):
        return self._ImageUrls

    @ImageUrls.setter
    def ImageUrls(self, ImageUrls):
        self._ImageUrls = ImageUrls

    @property
    def TokenStat(self):
        return self._TokenStat

    @TokenStat.setter
    def TokenStat(self, TokenStat):
        self._TokenStat = TokenStat

    @property
    def ReplyMethod(self):
        return self._ReplyMethod

    @ReplyMethod.setter
    def ReplyMethod(self, ReplyMethod):
        self._ReplyMethod = ReplyMethod

    @property
    def OptionCards(self):
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def TaskFlow(self):
        return self._TaskFlow

    @TaskFlow.setter
    def TaskFlow(self, TaskFlow):
        self._TaskFlow = TaskFlow

    @property
    def FileInfos(self):
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._SessionId = params.get("SessionId")
        self._RecordId = params.get("RecordId")
        self._RelatedRecordId = params.get("RelatedRecordId")
        self._IsFromSelf = params.get("IsFromSelf")
        self._FromName = params.get("FromName")
        self._FromAvatar = params.get("FromAvatar")
        self._Timestamp = params.get("Timestamp")
        self._HasRead = params.get("HasRead")
        self._Score = params.get("Score")
        self._CanRating = params.get("CanRating")
        self._CanFeedback = params.get("CanFeedback")
        self._Type = params.get("Type")
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = MsgRecordReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._Reasons = params.get("Reasons")
        self._IsLlmGenerated = params.get("IsLlmGenerated")
        self._ImageUrls = params.get("ImageUrls")
        if params.get("TokenStat") is not None:
            self._TokenStat = TokenStat()
            self._TokenStat._deserialize(params.get("TokenStat"))
        self._ReplyMethod = params.get("ReplyMethod")
        self._OptionCards = params.get("OptionCards")
        if params.get("TaskFlow") is not None:
            self._TaskFlow = TaskFlowInfo()
            self._TaskFlow._deserialize(params.get("TaskFlow"))
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecordReference(AbstractModel):
    """聊天详情Refer

    """

    def __init__(self):
        r"""
        :param _Id: id
        :type Id: str
        :param _Url: 链接
        :type Url: str
        :param _Type: 类型
        :type Type: int
        :param _Name: 名称
        :type Name: str
        :param _DocId: 来源文档ID
        :type DocId: str
        """
        self._Id = None
        self._Url = None
        self._Type = None
        self._Name = None
        self._DocId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DocId(self):
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._DocId = params.get("DocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Option(AbstractModel):
    """下拉框选项

    """

    def __init__(self):
        r"""
        :param _Text: 文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Value: 值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _CharSize: 文件字符数
注意：此字段可能返回 null，表示取不到有效值。
        :type CharSize: str
        :param _FileType: 文件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileType: str
        """
        self._Text = None
        self._Value = None
        self._CharSize = None
        self._FileType = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def CharSize(self):
        return self._CharSize

    @CharSize.setter
    def CharSize(self, CharSize):
        self._CharSize = CharSize

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Value = params.get("Value")
        self._CharSize = params.get("CharSize")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocRequest(AbstractModel):
    """ParseDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 文件名称(需要包括文件后缀, 最大长度1024字节)
        :type Name: str
        :param _Url: 文件下载链接 (支持的文件类型: docx, txt, markdown, pdf), 该地址需要外网可以直接无状态访问
        :type Url: str
        :param _TaskId: 任务ID, 用于幂等去重, 业务自行定义(最大长度64字节)
        :type TaskId: str
        :param _Policy: 切分策略
        :type Policy: str
        :param _Operate: 默认值: parse
        :type Operate: str
        """
        self._Name = None
        self._Url = None
        self._TaskId = None
        self._Policy = None
        self._Operate = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Operate(self):
        warnings.warn("parameter `Operate` is deprecated", DeprecationWarning) 

        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        warnings.warn("parameter `Operate` is deprecated", DeprecationWarning) 

        self._Operate = Operate


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        self._TaskId = params.get("TaskId")
        self._Policy = params.get("Policy")
        self._Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseDocResponse(AbstractModel):
    """ParseDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Polygon(AbstractModel):
    """文本的坐标，以四个顶点坐标表示
    注意：此字段可能返回 null，表示取不到有效值

    """

    def __init__(self):
        r"""
        :param _LeftTop: 左上顶点坐标
        :type LeftTop: :class:`tencentcloud.lke.v20231130.models.Coord`
        :param _RightTop: 右上顶点坐标
        :type RightTop: :class:`tencentcloud.lke.v20231130.models.Coord`
        :param _RightBottom: 右下顶点坐标
        :type RightBottom: :class:`tencentcloud.lke.v20231130.models.Coord`
        :param _LeftBottom: 左下顶点坐标
        :type LeftBottom: :class:`tencentcloud.lke.v20231130.models.Coord`
        """
        self._LeftTop = None
        self._RightTop = None
        self._RightBottom = None
        self._LeftBottom = None

    @property
    def LeftTop(self):
        return self._LeftTop

    @LeftTop.setter
    def LeftTop(self, LeftTop):
        self._LeftTop = LeftTop

    @property
    def RightTop(self):
        return self._RightTop

    @RightTop.setter
    def RightTop(self, RightTop):
        self._RightTop = RightTop

    @property
    def RightBottom(self):
        return self._RightBottom

    @RightBottom.setter
    def RightBottom(self, RightBottom):
        self._RightBottom = RightBottom

    @property
    def LeftBottom(self):
        return self._LeftBottom

    @LeftBottom.setter
    def LeftBottom(self, LeftBottom):
        self._LeftBottom = LeftBottom


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self._LeftTop = Coord()
            self._LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self._RightTop = Coord()
            self._RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self._RightBottom = Coord()
            self._RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self._LeftBottom = Coord()
            self._LeftBottom._deserialize(params.get("LeftBottom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Procedure(AbstractModel):
    """执行过程信息记录

    """

    def __init__(self):
        r"""
        :param _Name: 执行过程英语名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Title: 中文名, 用于展示
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Status: 状态常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Count: 消耗 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self._Name = None
        self._Title = None
        self._Status = None
        self._Count = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QACate(AbstractModel):
    """获取QA分类分组

    """

    def __init__(self):
        r"""
        :param _CateBizId: QA分类的业务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CateBizId: str
        :param _Name: 分类名称

注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Total: 分类下QA数量

注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _CanAdd: 是否可新增

注意：此字段可能返回 null，表示取不到有效值。
        :type CanAdd: bool
        :param _CanEdit: 是否可编辑

注意：此字段可能返回 null，表示取不到有效值。
        :type CanEdit: bool
        :param _CanDelete: 是否可删除

注意：此字段可能返回 null，表示取不到有效值。
        :type CanDelete: bool
        :param _Children: 子分类
注意：此字段可能返回 null，表示取不到有效值。
        :type Children: list of QACate
        """
        self._CateBizId = None
        self._Name = None
        self._Total = None
        self._CanAdd = None
        self._CanEdit = None
        self._CanDelete = None
        self._Children = None

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CanAdd(self):
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanEdit(self):
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit

    @property
    def CanDelete(self):
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def Children(self):
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children


    def _deserialize(self, params):
        self._CateBizId = params.get("CateBizId")
        self._Name = params.get("Name")
        self._Total = params.get("Total")
        self._CanAdd = params.get("CanAdd")
        self._CanEdit = params.get("CanEdit")
        self._CanDelete = params.get("CanDelete")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = QACate()
                obj._deserialize(item)
                self._Children.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QAList(AbstractModel):
    """问答列表

    """

    def __init__(self):
        r"""
        :param _QaBizId: 问答ID
        :type QaBizId: str
        :param _IsAccepted: 是否采纳
        :type IsAccepted: bool
        :param _CateBizId: 分类ID
        :type CateBizId: str
        :param _Question: 问题
        :type Question: str
        :param _Answer: 答案
        :type Answer: str
        """
        self._QaBizId = None
        self._IsAccepted = None
        self._CateBizId = None
        self._Question = None
        self._Answer = None

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def IsAccepted(self):
        return self._IsAccepted

    @IsAccepted.setter
    def IsAccepted(self, IsAccepted):
        self._IsAccepted = IsAccepted

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer


    def _deserialize(self, params):
        self._QaBizId = params.get("QaBizId")
        self._IsAccepted = params.get("IsAccepted")
        self._CateBizId = params.get("CateBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QAQuery(AbstractModel):
    """QA查询参数

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码


        :type PageNumber: int
        :param _PageSize: 每页数量

        :type PageSize: int
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _Query: 查询内容

        :type Query: str
        :param _CateBizId: 分类ID

        :type CateBizId: str
        :param _AcceptStatus: 校验状态

        :type AcceptStatus: list of int non-negative
        :param _ReleaseStatus: 发布状态

        :type ReleaseStatus: list of int non-negative
        :param _DocBizId: 文档ID

        :type DocBizId: str
        :param _QaBizId: QAID

        :type QaBizId: str
        :param _Source: 来源

        :type Source: int
        :param _QueryAnswer: 查询答案

        :type QueryAnswer: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._BotBizId = None
        self._Query = None
        self._CateBizId = None
        self._AcceptStatus = None
        self._ReleaseStatus = None
        self._DocBizId = None
        self._QaBizId = None
        self._Source = None
        self._QueryAnswer = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def CateBizId(self):
        return self._CateBizId

    @CateBizId.setter
    def CateBizId(self, CateBizId):
        self._CateBizId = CateBizId

    @property
    def AcceptStatus(self):
        return self._AcceptStatus

    @AcceptStatus.setter
    def AcceptStatus(self, AcceptStatus):
        self._AcceptStatus = AcceptStatus

    @property
    def ReleaseStatus(self):
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def QueryAnswer(self):
        return self._QueryAnswer

    @QueryAnswer.setter
    def QueryAnswer(self, QueryAnswer):
        self._QueryAnswer = QueryAnswer


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._BotBizId = params.get("BotBizId")
        self._Query = params.get("Query")
        self._CateBizId = params.get("CateBizId")
        self._AcceptStatus = params.get("AcceptStatus")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._DocBizId = params.get("DocBizId")
        self._QaBizId = params.get("QaBizId")
        self._Source = params.get("Source")
        self._QueryAnswer = params.get("QueryAnswer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryParseDocResultRequest(AbstractModel):
    """QueryParseDocResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryParseDocResultResponse(AbstractModel):
    """QueryParseDocResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 等待 / 执行中 / 成功 / 失败
        :type Status: str
        :param _Name: 解析后的文件内容
        :type Name: str
        :param _Url: 文件下载地址
        :type Url: str
        :param _Reason: 解析失败原因
        :type Reason: str
        :param _Usage: 消耗量，输出页数
        :type Usage: :class:`tencentcloud.lke.v20231130.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Name = None
        self._Url = None
        self._Reason = None
        self._Usage = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        self._Reason = params.get("Reason")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class QueryRewriteRequest(AbstractModel):
    """QueryRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Question: 需要改写的问题
        :type Question: str
        :param _Messages: 需要改写的多轮历史会话
        :type Messages: list of Message
        :param _Model: 模型名称
        :type Model: str
        """
        self._Question = None
        self._Messages = None
        self._Model = None

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        self._Question = params.get("Question")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Model = params.get("Model")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRewriteResponse(AbstractModel):
    """QueryRewrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 改写结果
        :type Content: str
        :param _Usage: 消耗量，返回输入token数，输出token数以及总token数
        :type Usage: :class:`tencentcloud.lke.v20231130.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._Usage = None
        self._RequestId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class RateMsgRecordRequest(AbstractModel):
    """RateMsgRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotAppKey: 应用appKey
        :type BotAppKey: str
        :param _RecordId: 消息ID
        :type RecordId: str
        :param _Score: 1点赞2点踩
        :type Score: int
        :param _Reasons: 原因
        :type Reasons: list of str
        """
        self._BotAppKey = None
        self._RecordId = None
        self._Score = None
        self._Reasons = None

    @property
    def BotAppKey(self):
        return self._BotAppKey

    @BotAppKey.setter
    def BotAppKey(self, BotAppKey):
        self._BotAppKey = BotAppKey

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Reasons(self):
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._BotAppKey = params.get("BotAppKey")
        self._RecordId = params.get("RecordId")
        self._Score = params.get("Score")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateMsgRecordResponse(AbstractModel):
    """RateMsgRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ReconstructDocumentConfig(AbstractModel):
    """ReconstructDocument配置选项

    """

    def __init__(self):
        r"""
        :param _EnableInsetImage: 生成的Markdown中是否嵌入图片
        :type EnableInsetImage: bool
        """
        self._EnableInsetImage = None

    @property
    def EnableInsetImage(self):
        return self._EnableInsetImage

    @EnableInsetImage.setter
    def EnableInsetImage(self, EnableInsetImage):
        self._EnableInsetImage = EnableInsetImage


    def _deserialize(self, params):
        self._EnableInsetImage = params.get("EnableInsetImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentFailedPage(AbstractModel):
    """文档解析失败记录

    """

    def __init__(self):
        r"""
        :param _PageNumber: 失败页码
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentRequest(AbstractModel):
    """ReconstructDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileBase64: 文件的 Base64 值。 支持的文件格式：PNG、JPG、JPEG、PDF。 支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。 支持的图片像素：单边介于20-10000px之间。 文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :type FileBase64: str
        :param _FileUrl: 文件的 Url 地址。 支持的文件格式：PNG、JPG、JPEG、PDF。 支持的文件大小：所下载文件经 Base64 编码后不超过 8M。文件下载时间不超过 3 秒。 支持的图片像素：单边介于20-10000px之间。 文件存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 Url 速度和稳定性可能受一定影响。
        :type FileUrl: str
        :param _FileStartPageNumber: 当传入文件是PDF类型时，用来指定pdf识别的起始页码，识别的页码包含当前值。默认为1，表示从pdf文件的第1页开始识别。
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 当传入文件是PDF类型时，用来指定pdf识别的结束页码，识别的页码包含当前值。默认为10，表示识别到pdf文件的第10页。单次调用最多支持识别10页内容，即FileEndPageNumber-FileStartPageNumber需要不大于10。
        :type FileEndPageNumber: int
        :param _Config: 配置选项，支持配置是否在生成的Markdown中是否嵌入图片
        :type Config: :class:`tencentcloud.lke.v20231130.models.ReconstructDocumentConfig`
        """
        self._FileBase64 = None
        self._FileUrl = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileBase64(self):
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileStartPageNumber(self):
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileBase64 = params.get("FileBase64")
        self._FileUrl = params.get("FileUrl")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = ReconstructDocumentConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentResponse(AbstractModel):
    """ReconstructDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MarkdownBase64: 识别生成的Markdown文件base64编码的字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type MarkdownBase64: str
        :param _InsetImagePackage: 输入文件中嵌入的图片放在一个文件夹中打包为.zip压缩文件，识别生成的Markdown文件通过路径关联插入本文件夹中的图片。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsetImagePackage: str
        :param _DocumentRecognizeInfo: 输入文件中嵌入的图片中文字内容的识别结果
注意：此字段可能返回 null，表示取不到有效值。
        :type DocumentRecognizeInfo: list of DocumentRecognizeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MarkdownBase64 = None
        self._InsetImagePackage = None
        self._DocumentRecognizeInfo = None
        self._RequestId = None

    @property
    def MarkdownBase64(self):
        return self._MarkdownBase64

    @MarkdownBase64.setter
    def MarkdownBase64(self, MarkdownBase64):
        self._MarkdownBase64 = MarkdownBase64

    @property
    def InsetImagePackage(self):
        return self._InsetImagePackage

    @InsetImagePackage.setter
    def InsetImagePackage(self, InsetImagePackage):
        self._InsetImagePackage = InsetImagePackage

    @property
    def DocumentRecognizeInfo(self):
        return self._DocumentRecognizeInfo

    @DocumentRecognizeInfo.setter
    def DocumentRecognizeInfo(self, DocumentRecognizeInfo):
        self._DocumentRecognizeInfo = DocumentRecognizeInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MarkdownBase64 = params.get("MarkdownBase64")
        self._InsetImagePackage = params.get("InsetImagePackage")
        if params.get("DocumentRecognizeInfo") is not None:
            self._DocumentRecognizeInfo = []
            for item in params.get("DocumentRecognizeInfo"):
                obj = DocumentRecognizeInfo()
                obj._deserialize(item)
                self._DocumentRecognizeInfo.append(obj)
        self._RequestId = params.get("RequestId")


class ReferDetail(AbstractModel):
    """引用来源详情

    """

    def __init__(self):
        r"""
        :param _ReferBizId: 引用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ReferBizId: str
        :param _DocType: 文档类型 (1 QA, 2 文档段)
注意：此字段可能返回 null，表示取不到有效值。
        :type DocType: int
        :param _DocName: 文档名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DocName: str
        :param _PageContent: 分片内容
注意：此字段可能返回 null，表示取不到有效值。
        :type PageContent: str
        :param _Question: 问题
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _Answer: 答案
注意：此字段可能返回 null，表示取不到有效值。
        :type Answer: str
        :param _Confidence: 置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param _Mark: 标记
注意：此字段可能返回 null，表示取不到有效值。
        :type Mark: int
        :param _Highlights: 分片高亮内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Highlights: list of Highlight
        :param _OrgData: 原始内容
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgData: str
        """
        self._ReferBizId = None
        self._DocType = None
        self._DocName = None
        self._PageContent = None
        self._Question = None
        self._Answer = None
        self._Confidence = None
        self._Mark = None
        self._Highlights = None
        self._OrgData = None

    @property
    def ReferBizId(self):
        return self._ReferBizId

    @ReferBizId.setter
    def ReferBizId(self, ReferBizId):
        self._ReferBizId = ReferBizId

    @property
    def DocType(self):
        return self._DocType

    @DocType.setter
    def DocType(self, DocType):
        self._DocType = DocType

    @property
    def DocName(self):
        return self._DocName

    @DocName.setter
    def DocName(self, DocName):
        self._DocName = DocName

    @property
    def PageContent(self):
        return self._PageContent

    @PageContent.setter
    def PageContent(self, PageContent):
        self._PageContent = PageContent

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def Mark(self):
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def Highlights(self):
        return self._Highlights

    @Highlights.setter
    def Highlights(self, Highlights):
        self._Highlights = Highlights

    @property
    def OrgData(self):
        return self._OrgData

    @OrgData.setter
    def OrgData(self, OrgData):
        self._OrgData = OrgData


    def _deserialize(self, params):
        self._ReferBizId = params.get("ReferBizId")
        self._DocType = params.get("DocType")
        self._DocName = params.get("DocName")
        self._PageContent = params.get("PageContent")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Confidence = params.get("Confidence")
        self._Mark = params.get("Mark")
        if params.get("Highlights") is not None:
            self._Highlights = []
            for item in params.get("Highlights"):
                obj = Highlight()
                obj._deserialize(item)
                self._Highlights.append(obj)
        self._OrgData = params.get("OrgData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectedQuestion(AbstractModel):
    """发布拒答

    """

    def __init__(self):
        r"""
        :param _RejectedBizId: 拒答问题ID


注意：此字段可能返回 null，表示取不到有效值。
        :type RejectedBizId: str
        :param _Question: 被拒答的问题

注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param _UpdateTime: 更新时间

注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _IsAllowEdit: 是否允许编辑

注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowEdit: bool
        :param _IsAllowDelete: 是否允许删除

注意：此字段可能返回 null，表示取不到有效值。
        :type IsAllowDelete: bool
        """
        self._RejectedBizId = None
        self._Question = None
        self._Status = None
        self._StatusDesc = None
        self._UpdateTime = None
        self._IsAllowEdit = None
        self._IsAllowDelete = None

    @property
    def RejectedBizId(self):
        return self._RejectedBizId

    @RejectedBizId.setter
    def RejectedBizId(self, RejectedBizId):
        self._RejectedBizId = RejectedBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsAllowEdit(self):
        return self._IsAllowEdit

    @IsAllowEdit.setter
    def IsAllowEdit(self, IsAllowEdit):
        self._IsAllowEdit = IsAllowEdit

    @property
    def IsAllowDelete(self):
        return self._IsAllowDelete

    @IsAllowDelete.setter
    def IsAllowDelete(self, IsAllowDelete):
        self._IsAllowDelete = IsAllowDelete


    def _deserialize(self, params):
        self._RejectedBizId = params.get("RejectedBizId")
        self._Question = params.get("Question")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._UpdateTime = params.get("UpdateTime")
        self._IsAllowEdit = params.get("IsAllowEdit")
        self._IsAllowDelete = params.get("IsAllowDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseConfigs(AbstractModel):
    """发布配置项

    """

    def __init__(self):
        r"""
        :param _ConfigItem: 配置项描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigItem: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Action: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: int
        :param _Value: 变更后的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _LastValue: 变更前的内容
注意：此字段可能返回 null，表示取不到有效值。
        :type LastValue: str
        :param _Content: 变更内容(优先级展示content内容,content为空取value内容)
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Message: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._ConfigItem = None
        self._UpdateTime = None
        self._Action = None
        self._Value = None
        self._LastValue = None
        self._Content = None
        self._Message = None

    @property
    def ConfigItem(self):
        return self._ConfigItem

    @ConfigItem.setter
    def ConfigItem(self, ConfigItem):
        self._ConfigItem = ConfigItem

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def LastValue(self):
        return self._LastValue

    @LastValue.setter
    def LastValue(self, LastValue):
        self._LastValue = LastValue

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._ConfigItem = params.get("ConfigItem")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        self._LastValue = params.get("LastValue")
        self._Content = params.get("Content")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseDoc(AbstractModel):
    """发布文档详情

    """

    def __init__(self):
        r"""
        :param _FileName: 文件名
        :type FileName: str
        :param _FileType: 文件类型
        :type FileType: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Action: 状态
        :type Action: int
        :param _ActionDesc: 状态描述
        :type ActionDesc: str
        :param _Message: 失败原因
        :type Message: str
        :param _DocBizId: 文档业务ID
        :type DocBizId: str
        """
        self._FileName = None
        self._FileType = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Message = None
        self._DocBizId = None

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Message = params.get("Message")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseQA(AbstractModel):
    """发布问答

    """

    def __init__(self):
        r"""
        :param _Question: 问题
        :type Question: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Action: 状态
        :type Action: int
        :param _ActionDesc: 状态描述
        :type ActionDesc: str
        :param _Source: 来源
        :type Source: int
        :param _SourceDesc: 来源描述
        :type SourceDesc: str
        :param _FileName: 文件名字
        :type FileName: str
        :param _FileType: 文档类型
        :type FileType: str
        :param _Message: 失败原因
        :type Message: str
        :param _ReleaseStatus: 发布状态
        :type ReleaseStatus: int
        :param _QaBizId: QAID
        :type QaBizId: str
        :param _DocBizId: 文档业务ID
        :type DocBizId: str
        """
        self._Question = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Source = None
        self._SourceDesc = None
        self._FileName = None
        self._FileType = None
        self._Message = None
        self._ReleaseStatus = None
        self._QaBizId = None
        self._DocBizId = None

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def SourceDesc(self):
        return self._SourceDesc

    @SourceDesc.setter
    def SourceDesc(self, SourceDesc):
        self._SourceDesc = SourceDesc

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ReleaseStatus(self):
        return self._ReleaseStatus

    @ReleaseStatus.setter
    def ReleaseStatus(self, ReleaseStatus):
        self._ReleaseStatus = ReleaseStatus

    @property
    def QaBizId(self):
        return self._QaBizId

    @QaBizId.setter
    def QaBizId(self, QaBizId):
        self._QaBizId = QaBizId

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Source = params.get("Source")
        self._SourceDesc = params.get("SourceDesc")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._Message = params.get("Message")
        self._ReleaseStatus = params.get("ReleaseStatus")
        self._QaBizId = params.get("QaBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseRejectedQuestion(AbstractModel):
    """发布拒答

    """

    def __init__(self):
        r"""
        :param _Question: 问题
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _Action: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: int
        :param _ActionDesc: 状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionDesc: str
        :param _Message: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._Question = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDesc = None
        self._Message = None

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDesc(self):
        return self._ActionDesc

    @ActionDesc.setter
    def ActionDesc(self, ActionDesc):
        self._ActionDesc = ActionDesc

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Question = params.get("Question")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDesc = params.get("ActionDesc")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSessionRequest(AbstractModel):
    """ResetSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _IsOnlyEmptyTheDialog: 是否仅清空会话关联
        :type IsOnlyEmptyTheDialog: bool
        """
        self._SessionId = None
        self._IsOnlyEmptyTheDialog = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def IsOnlyEmptyTheDialog(self):
        return self._IsOnlyEmptyTheDialog

    @IsOnlyEmptyTheDialog.setter
    def IsOnlyEmptyTheDialog(self, IsOnlyEmptyTheDialog):
        self._IsOnlyEmptyTheDialog = IsOnlyEmptyTheDialog


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._IsOnlyEmptyTheDialog = params.get("IsOnlyEmptyTheDialog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetSessionResponse(AbstractModel):
    """ResetSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RetryDocAuditRequest(AbstractModel):
    """RetryDocAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDocAuditResponse(AbstractModel):
    """RetryDocAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RetryDocParseRequest(AbstractModel):
    """RetryDocParse请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryDocParseResponse(AbstractModel):
    """RetryDocParse返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RetryReleaseRequest(AbstractModel):
    """RetryRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 机器人ID
        :type BotBizId: str
        :param _ReleaseBizId: 发布业务ID
        :type ReleaseBizId: str
        """
        self._BotBizId = None
        self._ReleaseBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def ReleaseBizId(self):
        return self._ReleaseBizId

    @ReleaseBizId.setter
    def ReleaseBizId(self, ReleaseBizId):
        self._ReleaseBizId = ReleaseBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._ReleaseBizId = params.get("ReleaseBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryReleaseResponse(AbstractModel):
    """RetryRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SaveDocRequest(AbstractModel):
    """SaveDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileType: 文件类型(md|txt|docx|pdf|xlsx)
        :type FileType: str
        :param _CosUrl: 平台cos路径，与DescribeStorageCredential接口查询UploadPath参数保持一致
        :type CosUrl: str
        :param _ETag: ETag 全称为 Entity Tag，是对象被创建时标识对象内容的信息标签，可用于检查对象的内容是否发生变化
        :type ETag: str
        :param _CosHash: cos_hash x-cos-hash-crc64ecma 头部中的 CRC64编码进行校验上传到云端的文件和本地文件的一致性
        :type CosHash: str
        :param _Size: 文件大小
        :type Size: str
        :param _AttrRange: 属性标签适用范围 1：全部，2：按条件范围
        :type AttrRange: int
        :param _Source: 来源(0 源文件导入 1 网页导入)
        :type Source: int
        :param _WebUrl: 网页(或自定义链接)地址
        :type WebUrl: str
        :param _AttrLabels: 属性标签引用
        :type AttrLabels: list of AttrLabelRefer
        :param _ReferUrlType: 外部引用链接类型 0：系统链接 1：自定义链接
值为1时，WebUrl 字段不能为空，否则不生效。
        :type ReferUrlType: int
        :param _ExpireStart: 有效开始时间，unix时间戳
        :type ExpireStart: str
        :param _ExpireEnd: 有效结束时间，unix时间戳，0代表永久有效
        :type ExpireEnd: str
        :param _IsRefer: 是否引用链接
        :type IsRefer: bool
        :param _Opt: 文档操作类型：1：批量导入；2:文档导入
        :type Opt: int
        """
        self._BotBizId = None
        self._FileName = None
        self._FileType = None
        self._CosUrl = None
        self._ETag = None
        self._CosHash = None
        self._Size = None
        self._AttrRange = None
        self._Source = None
        self._WebUrl = None
        self._AttrLabels = None
        self._ReferUrlType = None
        self._ExpireStart = None
        self._ExpireEnd = None
        self._IsRefer = None
        self._Opt = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def ETag(self):
        return self._ETag

    @ETag.setter
    def ETag(self, ETag):
        self._ETag = ETag

    @property
    def CosHash(self):
        return self._CosHash

    @CosHash.setter
    def CosHash(self, CosHash):
        self._CosHash = CosHash

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def AttrRange(self):
        return self._AttrRange

    @AttrRange.setter
    def AttrRange(self, AttrRange):
        self._AttrRange = AttrRange

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def WebUrl(self):
        return self._WebUrl

    @WebUrl.setter
    def WebUrl(self, WebUrl):
        self._WebUrl = WebUrl

    @property
    def AttrLabels(self):
        return self._AttrLabels

    @AttrLabels.setter
    def AttrLabels(self, AttrLabels):
        self._AttrLabels = AttrLabels

    @property
    def ReferUrlType(self):
        return self._ReferUrlType

    @ReferUrlType.setter
    def ReferUrlType(self, ReferUrlType):
        self._ReferUrlType = ReferUrlType

    @property
    def ExpireStart(self):
        return self._ExpireStart

    @ExpireStart.setter
    def ExpireStart(self, ExpireStart):
        self._ExpireStart = ExpireStart

    @property
    def ExpireEnd(self):
        return self._ExpireEnd

    @ExpireEnd.setter
    def ExpireEnd(self, ExpireEnd):
        self._ExpireEnd = ExpireEnd

    @property
    def IsRefer(self):
        return self._IsRefer

    @IsRefer.setter
    def IsRefer(self, IsRefer):
        self._IsRefer = IsRefer

    @property
    def Opt(self):
        return self._Opt

    @Opt.setter
    def Opt(self, Opt):
        self._Opt = Opt


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._CosUrl = params.get("CosUrl")
        self._ETag = params.get("ETag")
        self._CosHash = params.get("CosHash")
        self._Size = params.get("Size")
        self._AttrRange = params.get("AttrRange")
        self._Source = params.get("Source")
        self._WebUrl = params.get("WebUrl")
        if params.get("AttrLabels") is not None:
            self._AttrLabels = []
            for item in params.get("AttrLabels"):
                obj = AttrLabelRefer()
                obj._deserialize(item)
                self._AttrLabels.append(obj)
        self._ReferUrlType = params.get("ReferUrlType")
        self._ExpireStart = params.get("ExpireStart")
        self._ExpireEnd = params.get("ExpireEnd")
        self._IsRefer = params.get("IsRefer")
        self._Opt = params.get("Opt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaveDocResponse(AbstractModel):
    """SaveDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocBizId: 文档ID
        :type DocBizId: str
        :param _ErrorMsg: 导入错误信息
        :type ErrorMsg: str
        :param _ErrorLink: 错误链接
        :type ErrorLink: str
        :param _ErrorLinkText: 错误链接文本
        :type ErrorLinkText: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocBizId = None
        self._ErrorMsg = None
        self._ErrorLink = None
        self._ErrorLinkText = None
        self._RequestId = None

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorLink(self):
        return self._ErrorLink

    @ErrorLink.setter
    def ErrorLink(self, ErrorLink):
        self._ErrorLink = ErrorLink

    @property
    def ErrorLinkText(self):
        return self._ErrorLinkText

    @ErrorLinkText.setter
    def ErrorLinkText(self, ErrorLinkText):
        self._ErrorLinkText = ErrorLinkText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DocBizId = params.get("DocBizId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorLink = params.get("ErrorLink")
        self._ErrorLinkText = params.get("ErrorLinkText")
        self._RequestId = params.get("RequestId")


class StopDocParseRequest(AbstractModel):
    """StopDocParse请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _DocBizId: 文档ID
        :type DocBizId: str
        """
        self._BotBizId = None
        self._DocBizId = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def DocBizId(self):
        return self._DocBizId

    @DocBizId.setter
    def DocBizId(self, DocBizId):
        self._DocBizId = DocBizId


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._DocBizId = params.get("DocBizId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopDocParseResponse(AbstractModel):
    """StopDocParse返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SummaryConfig(AbstractModel):
    """知识摘要应用配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.lke.v20231130.models.AppModel`
        :param _Output: 知识摘要输出配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Output: :class:`tencentcloud.lke.v20231130.models.SummaryOutput`
        :param _Greeting: 欢迎语，200字符以内
注意：此字段可能返回 null，表示取不到有效值。
        :type Greeting: str
        """
        self._Model = None
        self._Output = None
        self._Greeting = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Greeting(self):
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = AppModel()
            self._Model._deserialize(params.get("Model"))
        if params.get("Output") is not None:
            self._Output = SummaryOutput()
            self._Output._deserialize(params.get("Output"))
        self._Greeting = params.get("Greeting")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SummaryOutput(AbstractModel):
    """知识摘要输出配置

    """

    def __init__(self):
        r"""
        :param _Method: 输出方式 1：流式 2：非流式
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: int
        :param _Requirement: 输出要求 1：文本总结 2：自定义要求
注意：此字段可能返回 null，表示取不到有效值。
        :type Requirement: int
        :param _RequireCommand: 自定义要求指令
注意：此字段可能返回 null，表示取不到有效值。
        :type RequireCommand: str
        """
        self._Method = None
        self._Requirement = None
        self._RequireCommand = None

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Requirement(self):
        return self._Requirement

    @Requirement.setter
    def Requirement(self, Requirement):
        self._Requirement = Requirement

    @property
    def RequireCommand(self):
        return self._RequireCommand

    @RequireCommand.setter
    def RequireCommand(self, RequireCommand):
        self._RequireCommand = RequireCommand


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._Requirement = params.get("Requirement")
        self._RequireCommand = params.get("RequireCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFlowInfo(AbstractModel):
    """任务流程信息

    """

    def __init__(self):
        r"""
        :param _TaskFlowId: 任务流程ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFlowId: str
        :param _TaskFlowName: 任务流程名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskFlowName: str
        :param _QueryRewrite: Query 重写结果
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryRewrite: str
        :param _HitIntent: 命中意图
注意：此字段可能返回 null，表示取不到有效值。
        :type HitIntent: str
        :param _Type: 任务流程回复类型
0: 任务流回复
1: 任务流静默
2: 任务流拉回话术
3: 任务流自定义回复
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        """
        self._TaskFlowId = None
        self._TaskFlowName = None
        self._QueryRewrite = None
        self._HitIntent = None
        self._Type = None

    @property
    def TaskFlowId(self):
        return self._TaskFlowId

    @TaskFlowId.setter
    def TaskFlowId(self, TaskFlowId):
        self._TaskFlowId = TaskFlowId

    @property
    def TaskFlowName(self):
        return self._TaskFlowName

    @TaskFlowName.setter
    def TaskFlowName(self, TaskFlowName):
        self._TaskFlowName = TaskFlowName

    @property
    def QueryRewrite(self):
        return self._QueryRewrite

    @QueryRewrite.setter
    def QueryRewrite(self, QueryRewrite):
        self._QueryRewrite = QueryRewrite

    @property
    def HitIntent(self):
        return self._HitIntent

    @HitIntent.setter
    def HitIntent(self, HitIntent):
        self._HitIntent = HitIntent

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TaskFlowId = params.get("TaskFlowId")
        self._TaskFlowName = params.get("TaskFlowName")
        self._QueryRewrite = params.get("QueryRewrite")
        self._HitIntent = params.get("HitIntent")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskParams(AbstractModel):
    """任务参数

    """

    def __init__(self):
        r"""
        :param _CosPath: 下载地址,需要通过cos桶临时密钥去下载
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPath: str
        """
        self._CosPath = None

    @property
    def CosPath(self):
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath


    def _deserialize(self, params):
        self._CosPath = params.get("CosPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenStat(AbstractModel):
    """当前执行的 token 统计信息

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param _RequestId: 请求 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        :param _RecordId: 对应哪条会话, 会话 ID, 用于回答的消息存储使用, 可提前生成, 保存消息时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _UsedCount: token 已使用数
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedCount: int
        :param _FreeCount: 免费 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type FreeCount: int
        :param _OrderCount: 订单总 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderCount: int
        :param _StatusSummary: 当前执行状态汇总, 常量: 使用中: processing, 成功: success, 失败: failed
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusSummary: str
        :param _StatusSummaryTitle: 当前执行状态汇总后中文展示
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusSummaryTitle: str
        :param _Elapsed: 当前请求执行时间, 单位 ms
注意：此字段可能返回 null，表示取不到有效值。
        :type Elapsed: int
        :param _TokenCount: 当前请求消耗 token 数
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenCount: int
        :param _Procedures: 执行过程信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Procedures: list of Procedure
        """
        self._SessionId = None
        self._RequestId = None
        self._RecordId = None
        self._UsedCount = None
        self._FreeCount = None
        self._OrderCount = None
        self._StatusSummary = None
        self._StatusSummaryTitle = None
        self._Elapsed = None
        self._TokenCount = None
        self._Procedures = None

    @property
    def SessionId(self):
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def UsedCount(self):
        return self._UsedCount

    @UsedCount.setter
    def UsedCount(self, UsedCount):
        self._UsedCount = UsedCount

    @property
    def FreeCount(self):
        return self._FreeCount

    @FreeCount.setter
    def FreeCount(self, FreeCount):
        self._FreeCount = FreeCount

    @property
    def OrderCount(self):
        return self._OrderCount

    @OrderCount.setter
    def OrderCount(self, OrderCount):
        self._OrderCount = OrderCount

    @property
    def StatusSummary(self):
        return self._StatusSummary

    @StatusSummary.setter
    def StatusSummary(self, StatusSummary):
        self._StatusSummary = StatusSummary

    @property
    def StatusSummaryTitle(self):
        return self._StatusSummaryTitle

    @StatusSummaryTitle.setter
    def StatusSummaryTitle(self, StatusSummaryTitle):
        self._StatusSummaryTitle = StatusSummaryTitle

    @property
    def Elapsed(self):
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def TokenCount(self):
        return self._TokenCount

    @TokenCount.setter
    def TokenCount(self, TokenCount):
        self._TokenCount = TokenCount

    @property
    def Procedures(self):
        return self._Procedures

    @Procedures.setter
    def Procedures(self, Procedures):
        self._Procedures = Procedures


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")
        self._RecordId = params.get("RecordId")
        self._UsedCount = params.get("UsedCount")
        self._FreeCount = params.get("FreeCount")
        self._OrderCount = params.get("OrderCount")
        self._StatusSummary = params.get("StatusSummary")
        self._StatusSummaryTitle = params.get("StatusSummaryTitle")
        self._Elapsed = params.get("Elapsed")
        self._TokenCount = params.get("TokenCount")
        if params.get("Procedures") is not None:
            self._Procedures = []
            for item in params.get("Procedures"):
                obj = Procedure()
                obj._deserialize(item)
                self._Procedures.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnsatisfiedReply(AbstractModel):
    """不满意回复

    """

    def __init__(self):
        r"""
        :param _ReplyBizId: 不满意回复ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplyBizId: str
        :param _RecordBizId: 消息记录ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordBizId: str
        :param _Question: 用户问题
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _Answer: 应用回复
注意：此字段可能返回 null，表示取不到有效值。
        :type Answer: str
        :param _Reasons: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Reasons: list of str
        """
        self._ReplyBizId = None
        self._RecordBizId = None
        self._Question = None
        self._Answer = None
        self._Reasons = None

    @property
    def ReplyBizId(self):
        return self._ReplyBizId

    @ReplyBizId.setter
    def ReplyBizId(self, ReplyBizId):
        self._ReplyBizId = ReplyBizId

    @property
    def RecordBizId(self):
        return self._RecordBizId

    @RecordBizId.setter
    def RecordBizId(self, RecordBizId):
        self._RecordBizId = RecordBizId

    @property
    def Question(self):
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def Reasons(self):
        return self._Reasons

    @Reasons.setter
    def Reasons(self, Reasons):
        self._Reasons = Reasons


    def _deserialize(self, params):
        self._ReplyBizId = params.get("ReplyBizId")
        self._RecordBizId = params.get("RecordBizId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        self._Reasons = params.get("Reasons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadAttributeLabelRequest(AbstractModel):
    """UploadAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _FileName: 文件名
        :type FileName: str
        :param _CosUrl: cos路径
        :type CosUrl: str
        :param _CosHash: x-cos-hash-crc64ecma 头部中的 CRC64编码进行校验上传到云端的文件和本地文件的一致性
        :type CosHash: str
        :param _Size: 文件大小
        :type Size: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._BotBizId = None
        self._FileName = None
        self._CosUrl = None
        self._CosHash = None
        self._Size = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CosUrl(self):
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def CosHash(self):
        return self._CosHash

    @CosHash.setter
    def CosHash(self, CosHash):
        self._CosHash = CosHash

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._BotBizId = params.get("BotBizId")
        self._FileName = params.get("FileName")
        self._CosUrl = params.get("CosUrl")
        self._CosHash = params.get("CosHash")
        self._Size = params.get("Size")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadAttributeLabelResponse(AbstractModel):
    """UploadAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: 导入错误
        :type ErrorMsg: str
        :param _ErrorLink: 错误链接
        :type ErrorLink: str
        :param _ErrorLinkText: 错误链接文本
        :type ErrorLinkText: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._ErrorLink = None
        self._ErrorLinkText = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ErrorLink(self):
        return self._ErrorLink

    @ErrorLink.setter
    def ErrorLink(self, ErrorLink):
        self._ErrorLink = ErrorLink

    @property
    def ErrorLinkText(self):
        return self._ErrorLinkText

    @ErrorLinkText.setter
    def ErrorLinkText(self, ErrorLinkText):
        self._ErrorLinkText = ErrorLinkText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorMsg = params.get("ErrorMsg")
        self._ErrorLink = params.get("ErrorLink")
        self._ErrorLinkText = params.get("ErrorLinkText")
        self._RequestId = params.get("RequestId")


class Usage(AbstractModel):
    """消耗量

    """

    def __init__(self):
        r"""
        :param _TotalPages: 文档页数
        :type TotalPages: int
        :param _InputTokens: 输入token数
        :type InputTokens: int
        :param _OutputTokens: 输出token数
        :type OutputTokens: int
        :param _TotalTokens: 总token数
        :type TotalTokens: int
        """
        self._TotalPages = None
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None

    @property
    def TotalPages(self):
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def InputTokens(self):
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._TotalPages = params.get("TotalPages")
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyQARequest(AbstractModel):
    """VerifyQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _List: 问答列表
        :type List: list of QAList
        :param _BotBizId: 应用ID
        :type BotBizId: str
        :param _LoginUin: 登录用户主账号(集成商模式必填)
        :type LoginUin: str
        :param _LoginSubAccountUin: 登录用户子账号(集成商模式必填)
        :type LoginSubAccountUin: str
        """
        self._List = None
        self._BotBizId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def BotBizId(self):
        return self._BotBizId

    @BotBizId.setter
    def BotBizId(self, BotBizId):
        self._BotBizId = BotBizId

    @property
    def LoginUin(self):
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = QAList()
                obj._deserialize(item)
                self._List.append(obj)
        self._BotBizId = params.get("BotBizId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyQAResponse(AbstractModel):
    """VerifyQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class WordRecognizeInfo(AbstractModel):
    """解析为 word 文档的结果

    """

    def __init__(self):
        r"""
        :param _PageNumber: 输入文件的页码数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        :param _WordBase64: word的base64
注意：此字段可能返回 null，表示取不到有效值。
        :type WordBase64: str
        """
        self._PageNumber = None
        self._WordBase64 = None

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def WordBase64(self):
        return self._WordBase64

    @WordBase64.setter
    def WordBase64(self, WordBase64):
        self._WordBase64 = WordBase64


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._WordBase64 = params.get("WordBase64")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        