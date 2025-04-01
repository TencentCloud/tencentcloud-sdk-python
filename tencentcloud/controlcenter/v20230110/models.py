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


class AccountFactoryItem(AbstractModel):
    """账号工厂基线项

    """

    def __init__(self):
        r"""
        :param _Identifier: 账号工厂基线项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :type Identifier: str
        :param _Name: 基线项名称，功能项名字唯一，仅支持英文字母、数宇、汉字、符号@、＆_[]-的组合，1-25个中文或英文字符。
        :type Name: str
        :param _NameEn: 基线项英文名称，基线项名字唯一，仅支持英文字母、数字、空格、符号@、＆_[]-的组合，1-64个英文字符。
        :type NameEn: str
        :param _Weight: 基线项权重，数值小权重越高，取值范围大于等于0。
        :type Weight: int
        :param _Required: 基线项是否必填，1必填，0非必填
        :type Required: int
        :param _DependsOn: 基线项依赖项，N的取值范围与该基线项依赖的其它基线项个数有关。
        :type DependsOn: list of DependsOnItem
        :param _Description: 基线描述，长度为2~256个英文或中文字符，默认值为空。
        :type Description: str
        :param _DescriptionEn: 基线项英文描述，长度为2~1024个英文字符，默认值为空。
        :type DescriptionEn: str
        :param _Classify: 基线分类，长度为2~32个英文或中文字符，不能为空。
        :type Classify: str
        :param _ClassifyEn: 基线英文分类，长度为2~64个英文字符，不能为空。
        :type ClassifyEn: str
        """
        self._Identifier = None
        self._Name = None
        self._NameEn = None
        self._Weight = None
        self._Required = None
        self._DependsOn = None
        self._Description = None
        self._DescriptionEn = None
        self._Classify = None
        self._ClassifyEn = None

    @property
    def Identifier(self):
        """账号工厂基线项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Name(self):
        """基线项名称，功能项名字唯一，仅支持英文字母、数宇、汉字、符号@、＆_[]-的组合，1-25个中文或英文字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NameEn(self):
        """基线项英文名称，基线项名字唯一，仅支持英文字母、数字、空格、符号@、＆_[]-的组合，1-64个英文字符。
        :rtype: str
        """
        return self._NameEn

    @NameEn.setter
    def NameEn(self, NameEn):
        self._NameEn = NameEn

    @property
    def Weight(self):
        """基线项权重，数值小权重越高，取值范围大于等于0。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Required(self):
        """基线项是否必填，1必填，0非必填
        :rtype: int
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def DependsOn(self):
        """基线项依赖项，N的取值范围与该基线项依赖的其它基线项个数有关。
        :rtype: list of DependsOnItem
        """
        return self._DependsOn

    @DependsOn.setter
    def DependsOn(self, DependsOn):
        self._DependsOn = DependsOn

    @property
    def Description(self):
        """基线描述，长度为2~256个英文或中文字符，默认值为空。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DescriptionEn(self):
        """基线项英文描述，长度为2~1024个英文字符，默认值为空。
        :rtype: str
        """
        return self._DescriptionEn

    @DescriptionEn.setter
    def DescriptionEn(self, DescriptionEn):
        self._DescriptionEn = DescriptionEn

    @property
    def Classify(self):
        """基线分类，长度为2~32个英文或中文字符，不能为空。
        :rtype: str
        """
        return self._Classify

    @Classify.setter
    def Classify(self, Classify):
        self._Classify = Classify

    @property
    def ClassifyEn(self):
        """基线英文分类，长度为2~64个英文字符，不能为空。
        :rtype: str
        """
        return self._ClassifyEn

    @ClassifyEn.setter
    def ClassifyEn(self, ClassifyEn):
        self._ClassifyEn = ClassifyEn


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Name = params.get("Name")
        self._NameEn = params.get("NameEn")
        self._Weight = params.get("Weight")
        self._Required = params.get("Required")
        if params.get("DependsOn") is not None:
            self._DependsOn = []
            for item in params.get("DependsOn"):
                obj = DependsOnItem()
                obj._deserialize(item)
                self._DependsOn.append(obj)
        self._Description = params.get("Description")
        self._DescriptionEn = params.get("DescriptionEn")
        self._Classify = params.get("Classify")
        self._ClassifyEn = params.get("ClassifyEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineConfigItem(AbstractModel):
    """账号工厂基线配置项

    """

    def __init__(self):
        r"""
        :param _Identifier: 账号工厂基线项唯一标识,只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :type Identifier: str
        :param _Configuration: 账号工厂基线项配置，不同基线项配置参数不同。
        :type Configuration: str
        """
        self._Identifier = None
        self._Configuration = None

    @property
    def Identifier(self):
        """账号工厂基线项唯一标识,只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Configuration(self):
        """账号工厂基线项配置，不同基线项配置参数不同。
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Configuration = params.get("Configuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineInfoItem(AbstractModel):
    """账号工厂基线信息

    """

    def __init__(self):
        r"""
        :param _Identifier: 账号工厂基线项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :type Identifier: str
        :param _Configuration: 账号工厂基线项配置，不同的基线项配置参数不同。
        :type Configuration: str
        :param _ApplyCount: 基线应用的账号数量。
        :type ApplyCount: int
        """
        self._Identifier = None
        self._Configuration = None
        self._ApplyCount = None

    @property
    def Identifier(self):
        """账号工厂基线项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Configuration(self):
        """账号工厂基线项配置，不同的基线项配置参数不同。
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def ApplyCount(self):
        """基线应用的账号数量。
        :rtype: int
        """
        return self._ApplyCount

    @ApplyCount.setter
    def ApplyCount(self, ApplyCount):
        self._ApplyCount = ApplyCount


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Configuration = params.get("Configuration")
        self._ApplyCount = params.get("ApplyCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaselineStepTaskInfo(AbstractModel):
    """基线项部署任务信息列表

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一Id，只能包含英文字母、数字，是16个字符的随机字符串。
        :type TaskId: str
        :param _Identifier: 基线功能项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :type Identifier: str
        :param _MemberUin: 被应用基线项的成员账号uin
        :type MemberUin: int
        :param _Status: 基线项应用的状态,Running表示基线项应用中,Success表示基线项应用成功,Failed表示基线项应用失败,Pending表示基线项待应用,Skipped表示基线项被跳过
        :type Status: str
        :param _ErrCode: 错误码
        :type ErrCode: str
        :param _ErrMessage: 错误信息
        :type ErrMessage: str
        :param _Output: 基线项部署输出
        :type Output: str
        :param _CreateTime: 创建时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :type CreateTime: str
        :param _UpdateTime: 更新时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :type UpdateTime: str
        """
        self._TaskId = None
        self._Identifier = None
        self._MemberUin = None
        self._Status = None
        self._ErrCode = None
        self._ErrMessage = None
        self._Output = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TaskId(self):
        """任务唯一Id，只能包含英文字母、数字，是16个字符的随机字符串。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Identifier(self):
        """基线功能项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def MemberUin(self):
        """被应用基线项的成员账号uin
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Status(self):
        """基线项应用的状态,Running表示基线项应用中,Success表示基线项应用成功,Failed表示基线项应用失败,Pending表示基线项待应用,Skipped表示基线项被跳过
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrCode(self):
        """错误码
        :rtype: str
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def ErrMessage(self):
        """错误信息
        :rtype: str
        """
        return self._ErrMessage

    @ErrMessage.setter
    def ErrMessage(self, ErrMessage):
        self._ErrMessage = ErrMessage

    @property
    def Output(self):
        """基线项部署输出
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def CreateTime(self):
        """创建时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Identifier = params.get("Identifier")
        self._MemberUin = params.get("MemberUin")
        self._Status = params.get("Status")
        self._ErrCode = params.get("ErrCode")
        self._ErrMessage = params.get("ErrMessage")
        self._Output = params.get("Output")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchApplyAccountBaselinesRequest(AbstractModel):
    """BatchApplyAccountBaselines请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUinList: 成员账号uin，也是被应用基线的账号uin。
        :type MemberUinList: list of int
        :param _BaselineConfigItems: 基线项配置信息列表。
        :type BaselineConfigItems: list of BaselineConfigItem
        """
        self._MemberUinList = None
        self._BaselineConfigItems = None

    @property
    def MemberUinList(self):
        """成员账号uin，也是被应用基线的账号uin。
        :rtype: list of int
        """
        return self._MemberUinList

    @MemberUinList.setter
    def MemberUinList(self, MemberUinList):
        self._MemberUinList = MemberUinList

    @property
    def BaselineConfigItems(self):
        """基线项配置信息列表。
        :rtype: list of BaselineConfigItem
        """
        return self._BaselineConfigItems

    @BaselineConfigItems.setter
    def BaselineConfigItems(self, BaselineConfigItems):
        self._BaselineConfigItems = BaselineConfigItems


    def _deserialize(self, params):
        self._MemberUinList = params.get("MemberUinList")
        if params.get("BaselineConfigItems") is not None:
            self._BaselineConfigItems = []
            for item in params.get("BaselineConfigItems"):
                obj = BaselineConfigItem()
                obj._deserialize(item)
                self._BaselineConfigItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchApplyAccountBaselinesResponse(AbstractModel):
    """BatchApplyAccountBaselines返回参数结构体

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


class DependsOnItem(AbstractModel):
    """依赖项

    """

    def __init__(self):
        r"""
        :param _Type: 依赖项类型，只有LandingZoneSetUp或AccountFactorySetUp。LandingZoneSetUp表示landingZone的依赖项；AccountFactorySetUp表示账号工厂的依赖项
        :type Type: str
        :param _Identifier: 功能项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :type Identifier: str
        """
        self._Type = None
        self._Identifier = None

    @property
    def Type(self):
        """依赖项类型，只有LandingZoneSetUp或AccountFactorySetUp。LandingZoneSetUp表示landingZone的依赖项；AccountFactorySetUp表示账号工厂的依赖项
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Identifier(self):
        """功能项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Identifier = params.get("Identifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAccountFactoryBaselineRequest(AbstractModel):
    """GetAccountFactoryBaseline请求参数结构体

    """


class GetAccountFactoryBaselineResponse(AbstractModel):
    """GetAccountFactoryBaseline返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 资源所属主账号uin。
        :type OwnerUin: int
        :param _Name: 基线项名称，基线项名字唯一，仅支持英文字母、数宇、汉字、符号@、＆_[]-的组合，1-25个中文或英文字符。
        :type Name: str
        :param _BaselineConfigItems: 基线项配置列表。
        :type BaselineConfigItems: list of BaselineInfoItem
        :param _CreateTime: 创建时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :type CreateTime: str
        :param _UpdateTime: 更新时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OwnerUin = None
        self._Name = None
        self._BaselineConfigItems = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        """资源所属主账号uin。
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Name(self):
        """基线项名称，基线项名字唯一，仅支持英文字母、数宇、汉字、符号@、＆_[]-的组合，1-25个中文或英文字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BaselineConfigItems(self):
        """基线项配置列表。
        :rtype: list of BaselineInfoItem
        """
        return self._BaselineConfigItems

    @BaselineConfigItems.setter
    def BaselineConfigItems(self, BaselineConfigItems):
        self._BaselineConfigItems = BaselineConfigItems

    @property
    def CreateTime(self):
        """创建时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间，按照ISO8601标准表示，格式为yyyy-MM-dd hh:mm:ss。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
        self._OwnerUin = params.get("OwnerUin")
        self._Name = params.get("Name")
        if params.get("BaselineConfigItems") is not None:
            self._BaselineConfigItems = []
            for item in params.get("BaselineConfigItems"):
                obj = BaselineInfoItem()
                obj._deserialize(item)
                self._BaselineConfigItems.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ListAccountFactoryBaselineItemsRequest(AbstractModel):
    """ListAccountFactoryBaselineItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回记录最大数目,取值范围0~200。
        :type Limit: int
        :param _Offset: 偏移量，取值范围大于等于0。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """返回记录最大数目,取值范围0~200。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，取值范围大于等于0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAccountFactoryBaselineItemsResponse(AbstractModel):
    """ListAccountFactoryBaselineItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaselineItems: 账号工厂基线列表。
        :type BaselineItems: list of AccountFactoryItem
        :param _Total: 总数。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaselineItems = None
        self._Total = None
        self._RequestId = None

    @property
    def BaselineItems(self):
        """账号工厂基线列表。
        :rtype: list of AccountFactoryItem
        """
        return self._BaselineItems

    @BaselineItems.setter
    def BaselineItems(self, BaselineItems):
        self._BaselineItems = BaselineItems

    @property
    def Total(self):
        """总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("BaselineItems") is not None:
            self._BaselineItems = []
            for item in params.get("BaselineItems"):
                obj = AccountFactoryItem()
                obj._deserialize(item)
                self._BaselineItems.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class ListDeployStepTasksRequest(AbstractModel):
    """ListDeployStepTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Identifier: 功能项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :type Identifier: str
        :param _Limit: 返回记录最大数目,取值范围0~200。
        :type Limit: int
        :param _Offset: 偏移量，取值范围大于等于0。
        :type Offset: int
        """
        self._Identifier = None
        self._Limit = None
        self._Offset = None

    @property
    def Identifier(self):
        """功能项唯一标识，只能包含英文字母、数字和@、,._[]-:()（）【】+=，。，长度2-128个字符。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Limit(self):
        """返回记录最大数目,取值范围0~200。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，取值范围大于等于0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDeployStepTasksResponse(AbstractModel):
    """ListDeployStepTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaselineDeployStepTaskList: 账号工厂基线功能项应用信息列表。
        :type BaselineDeployStepTaskList: list of BaselineStepTaskInfo
        :param _Total: 总数。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaselineDeployStepTaskList = None
        self._Total = None
        self._RequestId = None

    @property
    def BaselineDeployStepTaskList(self):
        """账号工厂基线功能项应用信息列表。
        :rtype: list of BaselineStepTaskInfo
        """
        return self._BaselineDeployStepTaskList

    @BaselineDeployStepTaskList.setter
    def BaselineDeployStepTaskList(self, BaselineDeployStepTaskList):
        self._BaselineDeployStepTaskList = BaselineDeployStepTaskList

    @property
    def Total(self):
        """总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("BaselineDeployStepTaskList") is not None:
            self._BaselineDeployStepTaskList = []
            for item in params.get("BaselineDeployStepTaskList"):
                obj = BaselineStepTaskInfo()
                obj._deserialize(item)
                self._BaselineDeployStepTaskList.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class UpdateAccountFactoryBaselineRequest(AbstractModel):
    """UpdateAccountFactoryBaseline请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 基线名称，基线名字唯一，仅支持英文字母、数宇、汉字、符号@、＆_[]-的组合，1-25个中文或英文字符。
        :type Name: str
        :param _BaselineConfigItems: 基线配置，覆盖更新。可以通过controlcenter:GetAccountFactoryBaseline查询现有基线配置。可以通过controlcenter:ListAccountFactoryBaselineItems查询支持的基线列表。
        :type BaselineConfigItems: list of BaselineConfigItem
        """
        self._Name = None
        self._BaselineConfigItems = None

    @property
    def Name(self):
        """基线名称，基线名字唯一，仅支持英文字母、数宇、汉字、符号@、＆_[]-的组合，1-25个中文或英文字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BaselineConfigItems(self):
        """基线配置，覆盖更新。可以通过controlcenter:GetAccountFactoryBaseline查询现有基线配置。可以通过controlcenter:ListAccountFactoryBaselineItems查询支持的基线列表。
        :rtype: list of BaselineConfigItem
        """
        return self._BaselineConfigItems

    @BaselineConfigItems.setter
    def BaselineConfigItems(self, BaselineConfigItems):
        self._BaselineConfigItems = BaselineConfigItems


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("BaselineConfigItems") is not None:
            self._BaselineConfigItems = []
            for item in params.get("BaselineConfigItems"):
                obj = BaselineConfigItem()
                obj._deserialize(item)
                self._BaselineConfigItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAccountFactoryBaselineResponse(AbstractModel):
    """UpdateAccountFactoryBaseline返回参数结构体

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