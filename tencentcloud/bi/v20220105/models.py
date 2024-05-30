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


class ApplyEmbedIntervalRequest(AbstractModel):
    """ApplyEmbedInterval请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 分享项目id，必选
        :type ProjectId: int
        :param _PageId: 分享页面id，嵌出看板时此为空值0
        :type PageId: int
        :param _BIToken: 需要申请延期的Token
        :type BIToken: str
        :param _ExtraParam: 备用字段
        :type ExtraParam: str
        :param _Scope: panel,看板；page，页面
        :type Scope: str
        """
        self._ProjectId = None
        self._PageId = None
        self._BIToken = None
        self._ExtraParam = None
        self._Scope = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def BIToken(self):
        return self._BIToken

    @BIToken.setter
    def BIToken(self, BIToken):
        self._BIToken = BIToken

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        self._BIToken = params.get("BIToken")
        self._ExtraParam = params.get("ExtraParam")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyEmbedIntervalResponse(AbstractModel):
    """ApplyEmbedInterval返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 额外参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 结果数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedTokenInfo`
        :param _Msg: 结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = ApplyEmbedTokenInfo()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ApplyEmbedTokenInfo(AbstractModel):
    """申请Token延期

    """

    def __init__(self):
        r"""
        :param _Result: 申请结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        """
        self._Result = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BaseStateAction(AbstractModel):
    """列表查询返回的每条记录的操作属性

    """

    def __init__(self):
        r"""
        :param _ShowEdit: 编辑是否可见
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowEdit: bool
        :param _IsEdit: 编辑是否可点击
注意：此字段可能返回 null，表示取不到有效值。
        :type IsEdit: bool
        :param _EditText: 编辑按钮的文本
注意：此字段可能返回 null，表示取不到有效值。
        :type EditText: str
        :param _EditTips: 编辑不可用时的提示文本
注意：此字段可能返回 null，表示取不到有效值。
        :type EditTips: str
        :param _ShowDel: 删除是否可见
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowDel: bool
        :param _IsDel: 删除是否可点击
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDel: bool
        :param _DelText: 删除按钮的文本
注意：此字段可能返回 null，表示取不到有效值。
        :type DelText: str
        :param _DelTips: 删除不可用时的提示文本
注意：此字段可能返回 null，表示取不到有效值。
        :type DelTips: str
        :param _ShowCopy: 复制是否可见
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowCopy: bool
        :param _ShowView: 是否可见
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowView: bool
        :param _ShowRename: 是否可重命名
注意：此字段可能返回 null，表示取不到有效值。
        :type ShowRename: bool
        """
        self._ShowEdit = None
        self._IsEdit = None
        self._EditText = None
        self._EditTips = None
        self._ShowDel = None
        self._IsDel = None
        self._DelText = None
        self._DelTips = None
        self._ShowCopy = None
        self._ShowView = None
        self._ShowRename = None

    @property
    def ShowEdit(self):
        return self._ShowEdit

    @ShowEdit.setter
    def ShowEdit(self, ShowEdit):
        self._ShowEdit = ShowEdit

    @property
    def IsEdit(self):
        return self._IsEdit

    @IsEdit.setter
    def IsEdit(self, IsEdit):
        self._IsEdit = IsEdit

    @property
    def EditText(self):
        return self._EditText

    @EditText.setter
    def EditText(self, EditText):
        self._EditText = EditText

    @property
    def EditTips(self):
        return self._EditTips

    @EditTips.setter
    def EditTips(self, EditTips):
        self._EditTips = EditTips

    @property
    def ShowDel(self):
        return self._ShowDel

    @ShowDel.setter
    def ShowDel(self, ShowDel):
        self._ShowDel = ShowDel

    @property
    def IsDel(self):
        return self._IsDel

    @IsDel.setter
    def IsDel(self, IsDel):
        self._IsDel = IsDel

    @property
    def DelText(self):
        return self._DelText

    @DelText.setter
    def DelText(self, DelText):
        self._DelText = DelText

    @property
    def DelTips(self):
        return self._DelTips

    @DelTips.setter
    def DelTips(self, DelTips):
        self._DelTips = DelTips

    @property
    def ShowCopy(self):
        return self._ShowCopy

    @ShowCopy.setter
    def ShowCopy(self, ShowCopy):
        self._ShowCopy = ShowCopy

    @property
    def ShowView(self):
        return self._ShowView

    @ShowView.setter
    def ShowView(self, ShowView):
        self._ShowView = ShowView

    @property
    def ShowRename(self):
        return self._ShowRename

    @ShowRename.setter
    def ShowRename(self, ShowRename):
        self._ShowRename = ShowRename


    def _deserialize(self, params):
        self._ShowEdit = params.get("ShowEdit")
        self._IsEdit = params.get("IsEdit")
        self._EditText = params.get("EditText")
        self._EditTips = params.get("EditTips")
        self._ShowDel = params.get("ShowDel")
        self._IsDel = params.get("IsDel")
        self._DelText = params.get("DelText")
        self._DelTips = params.get("DelTips")
        self._ShowCopy = params.get("ShowCopy")
        self._ShowView = params.get("ShowView")
        self._ShowRename = params.get("ShowRename")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorpUserListData(AbstractModel):
    """企业用户列表

    """

    def __init__(self):
        r"""
        :param _List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of UserIdAndUserName
        :param _Total: 总数
        :type Total: int
        :param _TotalPages: 页数
        :type TotalPages: int
        """
        self._List = None
        self._Total = None
        self._TotalPages = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UserIdAndUserName()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatasourceCloudRequest(AbstractModel):
    """CreateDatasourceCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 后端提供字典：域类型，1、腾讯云，2、本地
        :type ServiceType: str
        :param _DbType: 驱动
        :type DbType: str
        :param _Charset: 数据库编码
        :type Charset: str
        :param _DbUser: 用户名
        :type DbUser: str
        :param _DbPwd: 密码
        :type DbPwd: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _SourceName: 数据库别名
        :type SourceName: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Vip: 公有云内网ip
        :type Vip: str
        :param _Vport: 公有云内网端口
        :type Vport: str
        :param _VpcId: vpc标识
        :type VpcId: str
        :param _UniqVpcId: 统一vpc标识
        :type UniqVpcId: str
        :param _RegionId: 区域标识（gz,bj)
        :type RegionId: str
        :param _ExtraParam: 扩展参数
        :type ExtraParam: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _ProdDbName: 数据源产品名
        :type ProdDbName: str
        :param _DataOrigin: 第三方数据源标识
        :type DataOrigin: str
        :param _DataOriginProjectId: 第三方项目id
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: 第三方数据源id
        :type DataOriginDatasourceId: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        """
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._ProjectId = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._UniqVpcId = None
        self._RegionId = None
        self._ExtraParam = None
        self._InstanceId = None
        self._ProdDbName = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ClusterId = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProdDbName(self):
        return self._ProdDbName

    @ProdDbName.setter
    def ProdDbName(self, ProdDbName):
        self._ProdDbName = ProdDbName

    @property
    def DataOrigin(self):
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._ProjectId = params.get("ProjectId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._RegionId = params.get("RegionId")
        self._ExtraParam = params.get("ExtraParam")
        self._InstanceId = params.get("InstanceId")
        self._ProdDbName = params.get("ProdDbName")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatasourceCloudResponse(AbstractModel):
    """CreateDatasourceCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: 成功无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = IdDTO()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateDatasourceRequest(AbstractModel):
    """CreateDatasource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DbHost: HOST
        :type DbHost: str
        :param _DbPort: 端口
        :type DbPort: int
        :param _ServiceType: 后端提供字典：域类型，1、腾讯云，2、本地
        :type ServiceType: str
        :param _DbType: 驱动
        :type DbType: str
        :param _Charset: 数据库编码
        :type Charset: str
        :param _DbUser: 用户名
        :type DbUser: str
        :param _DbPwd: 密码
        :type DbPwd: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _SourceName: 数据库别名
        :type SourceName: str
        :param _ProjectId: 项目id
        :type ProjectId: int
        :param _Catalog: catalog值
        :type Catalog: str
        :param _DataOrigin: 第三方数据源标识
        :type DataOrigin: str
        :param _DataOriginProjectId: 第三方项目id
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: 第三方数据源id
        :type DataOriginDatasourceId: str
        :param _ExtraParam: 扩展参数
        :type ExtraParam: str
        :param _UniqVpcId: 腾讯云私有网络统一标识
        :type UniqVpcId: str
        :param _Vip: 私有网络ip
        :type Vip: str
        :param _Vport: 私有网络端口
        :type Vport: str
        :param _VpcId: 腾讯云私有网络标识
        :type VpcId: str
        :param _OperationAuthLimit: 操作权限限制
        :type OperationAuthLimit: list of str
        """
        self._DbHost = None
        self._DbPort = None
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._ProjectId = None
        self._Catalog = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ExtraParam = None
        self._UniqVpcId = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._OperationAuthLimit = None

    @property
    def DbHost(self):
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPort(self):
        return self._DbPort

    @DbPort.setter
    def DbPort(self, DbPort):
        self._DbPort = DbPort

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def DataOrigin(self):
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def OperationAuthLimit(self):
        return self._OperationAuthLimit

    @OperationAuthLimit.setter
    def OperationAuthLimit(self, OperationAuthLimit):
        self._OperationAuthLimit = OperationAuthLimit


    def _deserialize(self, params):
        self._DbHost = params.get("DbHost")
        self._DbPort = params.get("DbPort")
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._ProjectId = params.get("ProjectId")
        self._Catalog = params.get("Catalog")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ExtraParam = params.get("ExtraParam")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._OperationAuthLimit = params.get("OperationAuthLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDatasourceResponse(AbstractModel):
    """CreateDatasource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: 数据源id
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.IdDTO`
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = IdDTO()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateEmbedTokenRequest(AbstractModel):
    """CreateEmbedToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 分享项目id
        :type ProjectId: int
        :param _PageId: 分享页面id，嵌出看板时此为空值0
        :type PageId: int
        :param _Scope: page表示嵌出页面，panel表嵌出整个看板
        :type Scope: str
        :param _ExpireTime: 过期时间。 单位：分钟 最大值：240。即，4小时 默认值：240
        :type ExpireTime: str
        :param _ExtraParam: 备用字段
        :type ExtraParam: str
        :param _UserCorpId: 使用者企业Id(仅用于多用户)
        :type UserCorpId: str
        :param _UserId: 使用者Id(仅用于多用户)
        :type UserId: str
        :param _TicketNum: 访问次数限制，限制范围1-99999，为空则不设置访问次数限制
        :type TicketNum: int
        :param _GlobalParam: 全局筛选参数 报表过滤条件的全局参数。 格式为JSON格式的字符串
**目前仅支持字符类型页面参数绑定到全局参数
**
[
    {
        "ParamKey": "name",  //页面参数名称
        "JoinType": "AND",     // 连接方式,目前仅支持AND
        "WhereList": [
            {
                "Operator": "-neq",   // 操作符，参考以下说明
                "Value": [                   //操作值，单值数组只传一个值
                    "zZWJMD",
                    "ZzVGHX",
                    "湖南省",
                    "河北省"
                ]
            }
        ]
    },
    {
        "ParamKey": "genderParam",
        "JoinType": "AND",
        "WhereList": [
            {
                "Operator": "-neq",
                "Value": [
                    "男"
                ]
            }
        ]
    }
]



Operator 目前支持
-neq  不等于!=操作符
-eq  等于=操作符
-is     in操作符

        :type GlobalParam: str
        """
        self._ProjectId = None
        self._PageId = None
        self._Scope = None
        self._ExpireTime = None
        self._ExtraParam = None
        self._UserCorpId = None
        self._UserId = None
        self._TicketNum = None
        self._GlobalParam = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def UserCorpId(self):
        return self._UserCorpId

    @UserCorpId.setter
    def UserCorpId(self, UserCorpId):
        self._UserCorpId = UserCorpId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TicketNum(self):
        return self._TicketNum

    @TicketNum.setter
    def TicketNum(self, TicketNum):
        self._TicketNum = TicketNum

    @property
    def GlobalParam(self):
        return self._GlobalParam

    @GlobalParam.setter
    def GlobalParam(self, GlobalParam):
        self._GlobalParam = GlobalParam


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageId = params.get("PageId")
        self._Scope = params.get("Scope")
        self._ExpireTime = params.get("ExpireTime")
        self._ExtraParam = params.get("ExtraParam")
        self._UserCorpId = params.get("UserCorpId")
        self._UserId = params.get("UserId")
        self._TicketNum = params.get("TicketNum")
        self._GlobalParam = params.get("GlobalParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmbedTokenResponse(AbstractModel):
    """CreateEmbedToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.EmbedTokenInfo`
        :param _Msg: 结果描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = EmbedTokenInfo()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 项目名称
        :type Name: str
        :param _ColorCode: logo底色
        :type ColorCode: str
        :param _Logo: 项目Logo
        :type Logo: str
        :param _Mark: 备注
        :type Mark: str
        :param _IsApply: 是否允许用户申请
        :type IsApply: bool
        :param _DefaultPanelType: 默认看板
        :type DefaultPanelType: int
        :param _ManagePlatform: 管理平台
        :type ManagePlatform: str
        """
        self._Name = None
        self._ColorCode = None
        self._Logo = None
        self._Mark = None
        self._IsApply = None
        self._DefaultPanelType = None
        self._ManagePlatform = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ColorCode(self):
        return self._ColorCode

    @ColorCode.setter
    def ColorCode(self, ColorCode):
        self._ColorCode = ColorCode

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Mark(self):
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def IsApply(self):
        return self._IsApply

    @IsApply.setter
    def IsApply(self, IsApply):
        self._IsApply = IsApply

    @property
    def DefaultPanelType(self):
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType

    @property
    def ManagePlatform(self):
        return self._ManagePlatform

    @ManagePlatform.setter
    def ManagePlatform(self, ManagePlatform):
        self._ManagePlatform = ManagePlatform


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ColorCode = params.get("ColorCode")
        self._Logo = params.get("Logo")
        self._Mark = params.get("Mark")
        self._IsApply = params.get("IsApply")
        self._DefaultPanelType = params.get("DefaultPanelType")
        self._ManagePlatform = params.get("ManagePlatform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 额外数据
        :type Extra: str
        :param _Data: 数据
        :type Data: :class:`tencentcloud.bi.v20220105.models.Data`
        :param _Msg: 返回信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = Data()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateUserRoleProjectRequest(AbstractModel):
    """CreateUserRoleProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _RoleIdList: 角色ID列表
        :type RoleIdList: list of int
        :param _UserList: 用户列表（废弃）
        :type UserList: list of UserIdAndUserName
        :param _UserInfoList: 用户列表（新）
        :type UserInfoList: list of UserInfo
        """
        self._ProjectId = None
        self._RoleIdList = None
        self._UserList = None
        self._UserInfoList = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RoleIdList(self):
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def UserInfoList(self):
        return self._UserInfoList

    @UserInfoList.setter
    def UserInfoList(self, UserInfoList):
        self._UserInfoList = UserInfoList


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RoleIdList = params.get("RoleIdList")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserIdAndUserName()
                obj._deserialize(item)
                self._UserList.append(obj)
        if params.get("UserInfoList") is not None:
            self._UserInfoList = []
            for item in params.get("UserInfoList"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserRoleProjectResponse(AbstractModel):
    """CreateUserRoleProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.DataId`
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = DataId()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateUserRoleRequest(AbstractModel):
    """CreateUserRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleIdList: 角色ID列表
        :type RoleIdList: list of int
        :param _UserList: 用户列表（废弃）
        :type UserList: list of UserIdAndUserName
        :param _UserInfoList: 用户列表（新）
        :type UserInfoList: list of UserInfo
        """
        self._RoleIdList = None
        self._UserList = None
        self._UserInfoList = None

    @property
    def RoleIdList(self):
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def UserInfoList(self):
        return self._UserInfoList

    @UserInfoList.setter
    def UserInfoList(self, UserInfoList):
        self._UserInfoList = UserInfoList


    def _deserialize(self, params):
        self._RoleIdList = params.get("RoleIdList")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserIdAndUserName()
                obj._deserialize(item)
                self._UserList.append(obj)
        if params.get("UserInfoList") is not None:
            self._UserInfoList = []
            for item in params.get("UserInfoList"):
                obj = UserInfo()
                obj._deserialize(item)
                self._UserInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserRoleResponse(AbstractModel):
    """CreateUserRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.DataId`
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = DataId()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class Data(AbstractModel):
    """数据

    """

    def __init__(self):
        r"""
        :param _Id: 项目Id
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataId(AbstractModel):
    """数据ID

    """

    def __init__(self):
        r"""
        :param _Id: 数据id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceInfo(AbstractModel):
    """数据源详情

    """

    def __init__(self):
        r"""
        :param _Id: 数据库ID
        :type Id: int
        :param _DbName: 数据库名称
        :type DbName: str
        :param _ServiceType: 域类型，1、腾讯云，2、本地
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _SourceName: 数据库别名
        :type SourceName: str
        :param _DbType: 数据库驱动
        :type DbType: str
        :param _DbHost: HOST
        :type DbHost: str
        :param _DbPort: 端口
        :type DbPort: int
        :param _DbUser: 用户名
        :type DbUser: str
        :param _Charset: 数据库编码
        :type Charset: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _UpdatedAt: 修改时间
        :type UpdatedAt: str
        :param _CreatedUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedUser: str
        :param _Catalog: catalog值
注意：此字段可能返回 null，表示取不到有效值。
        :type Catalog: str
        :param _ConnectType: 连接类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectType: str
        :param _ProjectId: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _Desc: 数据源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Status: 数据源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _SourcePlat: 来源平台
注意：此字段可能返回 null，表示取不到有效值。
        :type SourcePlat: str
        :param _ExtraParam: 扩展参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraParam: str
        :param _AddInfo: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AddInfo: str
        :param _ProjectName: 项目名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _EngineType: 引擎类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineType: str
        :param _Manager: 数据源负责人
注意：此字段可能返回 null，表示取不到有效值。
        :type Manager: str
        :param _OperatorWhitelist: 特定操作人员白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorWhitelist: str
        :param _VpcId: 数据源的vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _UniqVpcId: 数据源的uniqVpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _RegionId: 数据源的地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param _StateAction: 操作属性
注意：此字段可能返回 null，表示取不到有效值。
        :type StateAction: :class:`tencentcloud.bi.v20220105.models.BaseStateAction`
        :param _UpdatedUser: 更新人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedUser: str
        :param _PermissionList: 权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PermissionList: list of PermissionGroup
        :param _AuthList: 权限值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthList: list of str
        :param _DataOrigin: 第三方数据源标识
注意：此字段可能返回 null，表示取不到有效值。
        :type DataOrigin: str
        :param _DataOriginProjectId: 第三方项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: 第三方数据源id
注意：此字段可能返回 null，表示取不到有效值。
        :type DataOriginDatasourceId: str
        :param _ClusterId: 集群id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self._Id = None
        self._DbName = None
        self._ServiceType = None
        self._SourceName = None
        self._DbType = None
        self._DbHost = None
        self._DbPort = None
        self._DbUser = None
        self._Charset = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._CreatedUser = None
        self._Catalog = None
        self._ConnectType = None
        self._ProjectId = None
        self._Desc = None
        self._Status = None
        self._SourcePlat = None
        self._ExtraParam = None
        self._AddInfo = None
        self._ProjectName = None
        self._EngineType = None
        self._Manager = None
        self._OperatorWhitelist = None
        self._VpcId = None
        self._UniqVpcId = None
        self._RegionId = None
        self._StateAction = None
        self._UpdatedUser = None
        self._PermissionList = None
        self._AuthList = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ClusterId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def DbHost(self):
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPort(self):
        return self._DbPort

    @DbPort.setter
    def DbPort(self, DbPort):
        self._DbPort = DbPort

    @property
    def DbUser(self):
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def CreatedUser(self):
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def ConnectType(self):
        return self._ConnectType

    @ConnectType.setter
    def ConnectType(self, ConnectType):
        self._ConnectType = ConnectType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourcePlat(self):
        return self._SourcePlat

    @SourcePlat.setter
    def SourcePlat(self, SourcePlat):
        self._SourcePlat = SourcePlat

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def AddInfo(self):
        return self._AddInfo

    @AddInfo.setter
    def AddInfo(self, AddInfo):
        self._AddInfo = AddInfo

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def Manager(self):
        return self._Manager

    @Manager.setter
    def Manager(self, Manager):
        self._Manager = Manager

    @property
    def OperatorWhitelist(self):
        return self._OperatorWhitelist

    @OperatorWhitelist.setter
    def OperatorWhitelist(self, OperatorWhitelist):
        self._OperatorWhitelist = OperatorWhitelist

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def StateAction(self):
        return self._StateAction

    @StateAction.setter
    def StateAction(self, StateAction):
        self._StateAction = StateAction

    @property
    def UpdatedUser(self):
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def PermissionList(self):
        return self._PermissionList

    @PermissionList.setter
    def PermissionList(self, PermissionList):
        self._PermissionList = PermissionList

    @property
    def AuthList(self):
        return self._AuthList

    @AuthList.setter
    def AuthList(self, AuthList):
        self._AuthList = AuthList

    @property
    def DataOrigin(self):
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DbName = params.get("DbName")
        self._ServiceType = params.get("ServiceType")
        self._SourceName = params.get("SourceName")
        self._DbType = params.get("DbType")
        self._DbHost = params.get("DbHost")
        self._DbPort = params.get("DbPort")
        self._DbUser = params.get("DbUser")
        self._Charset = params.get("Charset")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._CreatedUser = params.get("CreatedUser")
        self._Catalog = params.get("Catalog")
        self._ConnectType = params.get("ConnectType")
        self._ProjectId = params.get("ProjectId")
        self._Desc = params.get("Desc")
        self._Status = params.get("Status")
        self._SourcePlat = params.get("SourcePlat")
        self._ExtraParam = params.get("ExtraParam")
        self._AddInfo = params.get("AddInfo")
        self._ProjectName = params.get("ProjectName")
        self._EngineType = params.get("EngineType")
        self._Manager = params.get("Manager")
        self._OperatorWhitelist = params.get("OperatorWhitelist")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._RegionId = params.get("RegionId")
        if params.get("StateAction") is not None:
            self._StateAction = BaseStateAction()
            self._StateAction._deserialize(params.get("StateAction"))
        self._UpdatedUser = params.get("UpdatedUser")
        if params.get("PermissionList") is not None:
            self._PermissionList = []
            for item in params.get("PermissionList"):
                obj = PermissionGroup()
                obj._deserialize(item)
                self._PermissionList.append(obj)
        self._AuthList = params.get("AuthList")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatasourceInfoData(AbstractModel):
    """数据源详情列表

    """

    def __init__(self):
        r"""
        :param _List: 数据源详情列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of DatasourceInfo
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _TotalPages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPages: int
        """
        self._List = None
        self._Total = None
        self._TotalPages = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DatasourceInfo()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDatasourceRequest(AbstractModel):
    """DeleteDatasource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 数据源id
        :type Id: int
        :param _ProjectId: 项目id
        :type ProjectId: int
        """
        self._Id = None
        self._ProjectId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDatasourceResponse(AbstractModel):
    """DeleteDatasource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Extra: 扩展
        :type Extra: str
        :param _Msg: 信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Data = params.get("Data")
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 项目ID
        :type Id: int
        :param _Seed: 随机数
        :type Seed: str
        :param _DefaultPanelType: 默认看板
        :type DefaultPanelType: int
        """
        self._Id = None
        self._Seed = None
        self._DefaultPanelType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Seed(self):
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def DefaultPanelType(self):
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Seed = params.get("Seed")
        self._DefaultPanelType = params.get("DefaultPanelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: ”“
        :type Extra: str
        :param _Data: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Msg: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteUserRoleProjectRequest(AbstractModel):
    """DeleteUserRoleProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._ProjectId = None
        self._UserId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserRoleProjectResponse(AbstractModel):
    """DeleteUserRoleProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteUserRoleRequest(AbstractModel):
    """DeleteUserRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserRoleResponse(AbstractModel):
    """DeleteUserRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDatasourceListRequest(AbstractModel):
    """DescribeDatasourceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 无
        :type ProjectId: int
        :param _AllPage: 返回所有页面，默认false
        :type AllPage: bool
        :param _DbName: 数据库名称检索
        :type DbName: str
        :param _PageNo: 无
        :type PageNo: int
        :param _PageSize: 无
        :type PageSize: int
        :param _Keyword: 搜索关键词
        :type Keyword: str
        :param _PermissionType: 过滤无权限列表的参数（0 全量，1 使用权限，2 编辑权限）
        :type PermissionType: int
        """
        self._ProjectId = None
        self._AllPage = None
        self._DbName = None
        self._PageNo = None
        self._PageSize = None
        self._Keyword = None
        self._PermissionType = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AllPage(self):
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PermissionType(self):
        return self._PermissionType

    @PermissionType.setter
    def PermissionType(self, PermissionType):
        self._PermissionType = PermissionType


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AllPage = params.get("AllPage")
        self._DbName = params.get("DbName")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._Keyword = params.get("Keyword")
        self._PermissionType = params.get("PermissionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatasourceListResponse(AbstractModel):
    """DescribeDatasourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: 列表详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.DatasourceInfoData`
        :param _Extra: 信息
        :type Extra: str
        :param _Msg: 信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = DatasourceInfoData()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeProjectInfoRequest(AbstractModel):
    """DescribeProjectInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 项目Id
        :type Id: int
        :param _DefaultPanelType: 默认看板
        :type DefaultPanelType: int
        """
        self._Id = None
        self._DefaultPanelType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DefaultPanelType(self):
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._DefaultPanelType = params.get("DefaultPanelType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectInfoResponse(AbstractModel):
    """DescribeProjectInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Data: 项目详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.Project`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        if params.get("Data") is not None:
            self._Data = Project()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeProjectListRequest(AbstractModel):
    """DescribeProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 页容，初版默认20，将来可能根据屏幕宽度动态变化
        :type PageSize: int
        :param _PageNo: 页标
        :type PageNo: int
        :param _Keyword: 检索模糊字段
        :type Keyword: str
        :param _AllPage: 是否全部展示，如果是ture，则忽略分页
        :type AllPage: bool
        :param _ModuleCollection: 角色信息
        :type ModuleCollection: str
        """
        self._PageSize = None
        self._PageNo = None
        self._Keyword = None
        self._AllPage = None
        self._ModuleCollection = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def AllPage(self):
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def ModuleCollection(self):
        return self._ModuleCollection

    @ModuleCollection.setter
    def ModuleCollection(self, ModuleCollection):
        self._ModuleCollection = ModuleCollection


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNo = params.get("PageNo")
        self._Keyword = params.get("Keyword")
        self._AllPage = params.get("AllPage")
        self._ModuleCollection = params.get("ModuleCollection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectListResponse(AbstractModel):
    """DescribeProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 接口信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.ProjectListData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        if params.get("Data") is not None:
            self._Data = ProjectListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeUserProjectListRequest(AbstractModel):
    """DescribeUserProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _AllPage: 无
        :type AllPage: bool
        :param _PageNo: 无
        :type PageNo: int
        :param _PageSize: 无
        :type PageSize: int
        """
        self._ProjectId = None
        self._AllPage = None
        self._PageNo = None
        self._PageSize = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AllPage(self):
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._AllPage = params.get("AllPage")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserProjectListResponse(AbstractModel):
    """DescribeUserProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.CorpUserListData`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        if params.get("Data") is not None:
            self._Data = CorpUserListData()
            self._Data._deserialize(params.get("Data"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeUserRoleListRequest(AbstractModel):
    """DescribeUserRoleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页数
        :type PageSize: int
        :param _AllPage: 全部页码
        :type AllPage: bool
        :param _UserType: 0 企业用户 1 访客 不填表示所有用户
        :type UserType: str
        :param _Keyword: 模糊搜索的关键字
        :type Keyword: str
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _IsOnlyBindAppUser: 是否只获取绑定企微应用的
        :type IsOnlyBindAppUser: bool
        """
        self._PageNo = None
        self._PageSize = None
        self._AllPage = None
        self._UserType = None
        self._Keyword = None
        self._ProjectId = None
        self._IsOnlyBindAppUser = None

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def AllPage(self):
        return self._AllPage

    @AllPage.setter
    def AllPage(self, AllPage):
        self._AllPage = AllPage

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IsOnlyBindAppUser(self):
        return self._IsOnlyBindAppUser

    @IsOnlyBindAppUser.setter
    def IsOnlyBindAppUser(self, IsOnlyBindAppUser):
        self._IsOnlyBindAppUser = IsOnlyBindAppUser


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._AllPage = params.get("AllPage")
        self._UserType = params.get("UserType")
        self._Keyword = params.get("Keyword")
        self._ProjectId = params.get("ProjectId")
        self._IsOnlyBindAppUser = params.get("IsOnlyBindAppUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserRoleListResponse(AbstractModel):
    """DescribeUserRoleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.UserRoleListData`
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = UserRoleListData()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeUserRoleProjectListRequest(AbstractModel):
    """DescribeUserRoleProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页数
        :type PageSize: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _IsOnlyBindAppUser: 是否只获取绑定企微应用的
        :type IsOnlyBindAppUser: bool
        """
        self._PageNo = None
        self._PageSize = None
        self._ProjectId = None
        self._IsOnlyBindAppUser = None

    @property
    def PageNo(self):
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IsOnlyBindAppUser(self):
        return self._IsOnlyBindAppUser

    @IsOnlyBindAppUser.setter
    def IsOnlyBindAppUser(self, IsOnlyBindAppUser):
        self._IsOnlyBindAppUser = IsOnlyBindAppUser


    def _deserialize(self, params):
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._ProjectId = params.get("ProjectId")
        self._IsOnlyBindAppUser = params.get("IsOnlyBindAppUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserRoleProjectListResponse(AbstractModel):
    """DescribeUserRoleProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.bi.v20220105.models.UserRoleListData`
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        if params.get("Data") is not None:
            self._Data = UserRoleListData()
            self._Data._deserialize(params.get("Data"))
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class EmbedTokenInfo(AbstractModel):
    """报表嵌出数据结构-强鉴权

    """

    def __init__(self):
        r"""
        :param _Id: 信息标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _BIToken: 令牌
注意：此字段可能返回 null，表示取不到有效值。
        :type BIToken: str
        :param _ProjectId: 项目Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _CreatedUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedUser: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedUser: 更新人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedUser: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _PageId: 页面Id
注意：此字段可能返回 null，表示取不到有效值。
        :type PageId: str
        :param _ExtraParam: 备用
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraParam: str
        :param _Scope: 嵌出类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Scope: str
        :param _ExpireTime: 过期时间，分钟为单位，最大240
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param _UserCorpId: 使用者企业Id(仅用于多用户)
注意：此字段可能返回 null，表示取不到有效值。
        :type UserCorpId: str
        :param _UserId: 使用者Id(仅用于多用户)
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param _TicketNum: 访问次数限制，限制范围1-99999，为空则不设置访问次数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TicketNum: int
        :param _GlobalParam: 全局参数
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalParam: str
        """
        self._Id = None
        self._BIToken = None
        self._ProjectId = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._PageId = None
        self._ExtraParam = None
        self._Scope = None
        self._ExpireTime = None
        self._UserCorpId = None
        self._UserId = None
        self._TicketNum = None
        self._GlobalParam = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BIToken(self):
        return self._BIToken

    @BIToken.setter
    def BIToken(self, BIToken):
        self._BIToken = BIToken

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreatedUser(self):
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedUser(self):
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PageId(self):
        return self._PageId

    @PageId.setter
    def PageId(self, PageId):
        self._PageId = PageId

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def Scope(self):
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UserCorpId(self):
        return self._UserCorpId

    @UserCorpId.setter
    def UserCorpId(self, UserCorpId):
        self._UserCorpId = UserCorpId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def TicketNum(self):
        return self._TicketNum

    @TicketNum.setter
    def TicketNum(self, TicketNum):
        self._TicketNum = TicketNum

    @property
    def GlobalParam(self):
        return self._GlobalParam

    @GlobalParam.setter
    def GlobalParam(self, GlobalParam):
        self._GlobalParam = GlobalParam


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._BIToken = params.get("BIToken")
        self._ProjectId = params.get("ProjectId")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._PageId = params.get("PageId")
        self._ExtraParam = params.get("ExtraParam")
        self._Scope = params.get("Scope")
        self._ExpireTime = params.get("ExpireTime")
        self._UserCorpId = params.get("UserCorpId")
        self._UserId = params.get("UserId")
        self._TicketNum = params.get("TicketNum")
        self._GlobalParam = params.get("GlobalParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorInfo(AbstractModel):
    """自定义错误信息对象

    """

    def __init__(self):
        r"""
        :param _ErrorTip: 错误说明字段
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorTip: str
        :param _ErrorMessage: 原始异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _ErrorLevel: 错误等级字段
ERROR
WARN
INFO
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorLevel: str
        :param _DocLink: 指引文档链接
注意：此字段可能返回 null，表示取不到有效值。
        :type DocLink: str
        :param _FAQ: 快速指引说明
注意：此字段可能返回 null，表示取不到有效值。
        :type FAQ: str
        :param _ReservedField: 预留字段1
注意：此字段可能返回 null，表示取不到有效值。
        :type ReservedField: str
        """
        self._ErrorTip = None
        self._ErrorMessage = None
        self._ErrorLevel = None
        self._DocLink = None
        self._FAQ = None
        self._ReservedField = None

    @property
    def ErrorTip(self):
        return self._ErrorTip

    @ErrorTip.setter
    def ErrorTip(self, ErrorTip):
        self._ErrorTip = ErrorTip

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ErrorLevel(self):
        return self._ErrorLevel

    @ErrorLevel.setter
    def ErrorLevel(self, ErrorLevel):
        self._ErrorLevel = ErrorLevel

    @property
    def DocLink(self):
        return self._DocLink

    @DocLink.setter
    def DocLink(self, DocLink):
        self._DocLink = DocLink

    @property
    def FAQ(self):
        return self._FAQ

    @FAQ.setter
    def FAQ(self, FAQ):
        self._FAQ = FAQ

    @property
    def ReservedField(self):
        return self._ReservedField

    @ReservedField.setter
    def ReservedField(self, ReservedField):
        self._ReservedField = ReservedField


    def _deserialize(self, params):
        self._ErrorTip = params.get("ErrorTip")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ErrorLevel = params.get("ErrorLevel")
        self._DocLink = params.get("DocLink")
        self._FAQ = params.get("FAQ")
        self._ReservedField = params.get("ReservedField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdDTO(AbstractModel):
    """仅包含id的对象

    """

    def __init__(self):
        r"""
        :param _Id: 请求id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _AccessKey: key
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param _ProjectId: id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _TranId: 事务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param _TranStatus: 事务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TranStatus: int
        """
        self._Id = None
        self._AccessKey = None
        self._ProjectId = None
        self._TranId = None
        self._TranStatus = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def TranStatus(self):
        return self._TranStatus

    @TranStatus.setter
    def TranStatus(self, TranStatus):
        self._TranStatus = TranStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._AccessKey = params.get("AccessKey")
        self._ProjectId = params.get("ProjectId")
        self._TranId = params.get("TranId")
        self._TranStatus = params.get("TranStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatasourceCloudRequest(AbstractModel):
    """ModifyDatasourceCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 后端提供字典：域类型，1、腾讯云，2、本地
        :type ServiceType: str
        :param _DbType: 驱动
        :type DbType: str
        :param _Charset: 数据库编码
        :type Charset: str
        :param _DbUser: 用户名
        :type DbUser: str
        :param _DbPwd: 密码
        :type DbPwd: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _SourceName: 数据库别名
        :type SourceName: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Id: 住键
        :type Id: int
        :param _Vip: 公有云内网ip
        :type Vip: str
        :param _Vport: 公有云内网端口
        :type Vport: str
        :param _VpcId: vpc标识
        :type VpcId: str
        :param _UniqVpcId: 统一vpc标识
        :type UniqVpcId: str
        :param _RegionId: 区域标识（gz,bj)
        :type RegionId: str
        :param _ExtraParam: 扩展参数
        :type ExtraParam: str
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ProdDbName: 数据源产品名
        :type ProdDbName: str
        :param _DataOrigin: 第三方数据源标识
        :type DataOrigin: str
        :param _DataOriginProjectId: 第三方项目id
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: 第三方数据源id
        :type DataOriginDatasourceId: str
        :param _ClusterId: 集群id
        :type ClusterId: str
        """
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._ProjectId = None
        self._Id = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None
        self._UniqVpcId = None
        self._RegionId = None
        self._ExtraParam = None
        self._InstanceId = None
        self._ProdDbName = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ClusterId = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProdDbName(self):
        return self._ProdDbName

    @ProdDbName.setter
    def ProdDbName(self, ProdDbName):
        self._ProdDbName = ProdDbName

    @property
    def DataOrigin(self):
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._ProjectId = params.get("ProjectId")
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._RegionId = params.get("RegionId")
        self._ExtraParam = params.get("ExtraParam")
        self._InstanceId = params.get("InstanceId")
        self._ProdDbName = params.get("ProdDbName")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatasourceCloudResponse(AbstractModel):
    """ModifyDatasourceCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: 成功无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Data = params.get("Data")
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyDatasourceRequest(AbstractModel):
    """ModifyDatasource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DbHost: HOST
        :type DbHost: str
        :param _DbPort: 端口
        :type DbPort: int
        :param _ServiceType: 后端提供字典：域类型，1、腾讯云，2、本地
        :type ServiceType: str
        :param _DbType: 驱动
        :type DbType: str
        :param _Charset: 数据库编码
        :type Charset: str
        :param _DbUser: 用户名
        :type DbUser: str
        :param _DbPwd: 密码
        :type DbPwd: str
        :param _DbName: 数据库名称
        :type DbName: str
        :param _SourceName: 数据库别名
        :type SourceName: str
        :param _Id: 数据源id
        :type Id: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Catalog: catalog值
        :type Catalog: str
        :param _DataOrigin: 第三方数据源标识
        :type DataOrigin: str
        :param _DataOriginProjectId: 第三方项目id
        :type DataOriginProjectId: str
        :param _DataOriginDatasourceId: 第三方数据源id
        :type DataOriginDatasourceId: str
        :param _ExtraParam: 扩展参数
        :type ExtraParam: str
        :param _UniqVpcId: 腾讯云私有网络统一标识
        :type UniqVpcId: str
        :param _Vip: 私有网络ip
        :type Vip: str
        :param _Vport: 私有网络端口
        :type Vport: str
        :param _VpcId: 腾讯云私有网络标识
        :type VpcId: str
        """
        self._DbHost = None
        self._DbPort = None
        self._ServiceType = None
        self._DbType = None
        self._Charset = None
        self._DbUser = None
        self._DbPwd = None
        self._DbName = None
        self._SourceName = None
        self._Id = None
        self._ProjectId = None
        self._Catalog = None
        self._DataOrigin = None
        self._DataOriginProjectId = None
        self._DataOriginDatasourceId = None
        self._ExtraParam = None
        self._UniqVpcId = None
        self._Vip = None
        self._Vport = None
        self._VpcId = None

    @property
    def DbHost(self):
        return self._DbHost

    @DbHost.setter
    def DbHost(self, DbHost):
        self._DbHost = DbHost

    @property
    def DbPort(self):
        return self._DbPort

    @DbPort.setter
    def DbPort(self, DbPort):
        self._DbPort = DbPort

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def DbType(self):
        return self._DbType

    @DbType.setter
    def DbType(self, DbType):
        self._DbType = DbType

    @property
    def Charset(self):
        return self._Charset

    @Charset.setter
    def Charset(self, Charset):
        self._Charset = Charset

    @property
    def DbUser(self):
        return self._DbUser

    @DbUser.setter
    def DbUser(self, DbUser):
        self._DbUser = DbUser

    @property
    def DbPwd(self):
        return self._DbPwd

    @DbPwd.setter
    def DbPwd(self, DbPwd):
        self._DbPwd = DbPwd

    @property
    def DbName(self):
        return self._DbName

    @DbName.setter
    def DbName(self, DbName):
        self._DbName = DbName

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Catalog(self):
        return self._Catalog

    @Catalog.setter
    def Catalog(self, Catalog):
        self._Catalog = Catalog

    @property
    def DataOrigin(self):
        return self._DataOrigin

    @DataOrigin.setter
    def DataOrigin(self, DataOrigin):
        self._DataOrigin = DataOrigin

    @property
    def DataOriginProjectId(self):
        return self._DataOriginProjectId

    @DataOriginProjectId.setter
    def DataOriginProjectId(self, DataOriginProjectId):
        self._DataOriginProjectId = DataOriginProjectId

    @property
    def DataOriginDatasourceId(self):
        return self._DataOriginDatasourceId

    @DataOriginDatasourceId.setter
    def DataOriginDatasourceId(self, DataOriginDatasourceId):
        self._DataOriginDatasourceId = DataOriginDatasourceId

    @property
    def ExtraParam(self):
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def Vport(self):
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._DbHost = params.get("DbHost")
        self._DbPort = params.get("DbPort")
        self._ServiceType = params.get("ServiceType")
        self._DbType = params.get("DbType")
        self._Charset = params.get("Charset")
        self._DbUser = params.get("DbUser")
        self._DbPwd = params.get("DbPwd")
        self._DbName = params.get("DbName")
        self._SourceName = params.get("SourceName")
        self._Id = params.get("Id")
        self._ProjectId = params.get("ProjectId")
        self._Catalog = params.get("Catalog")
        self._DataOrigin = params.get("DataOrigin")
        self._DataOriginProjectId = params.get("DataOriginProjectId")
        self._DataOriginDatasourceId = params.get("DataOriginDatasourceId")
        self._ExtraParam = params.get("ExtraParam")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Vip = params.get("Vip")
        self._Vport = params.get("Vport")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDatasourceResponse(AbstractModel):
    """ModifyDatasource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 提示
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Data = None
        self._Extra = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Data = params.get("Data")
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 项目Id
        :type Id: int
        :param _Name: 名字
        :type Name: str
        :param _ColorCode: 颜色值
        :type ColorCode: str
        :param _Logo: 图标
        :type Logo: str
        :param _Mark: 备注
        :type Mark: str
        :param _IsApply: 可申请
        :type IsApply: bool
        :param _Seed: 种子
        :type Seed: str
        :param _DefaultPanelType: 默认看板
        :type DefaultPanelType: int
        :param _PanelScope: 2
        :type PanelScope: str
        :param _ManagePlatform: 项目管理平台
        :type ManagePlatform: str
        """
        self._Id = None
        self._Name = None
        self._ColorCode = None
        self._Logo = None
        self._Mark = None
        self._IsApply = None
        self._Seed = None
        self._DefaultPanelType = None
        self._PanelScope = None
        self._ManagePlatform = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ColorCode(self):
        return self._ColorCode

    @ColorCode.setter
    def ColorCode(self, ColorCode):
        self._ColorCode = ColorCode

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Mark(self):
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def IsApply(self):
        return self._IsApply

    @IsApply.setter
    def IsApply(self, IsApply):
        self._IsApply = IsApply

    @property
    def Seed(self):
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def DefaultPanelType(self):
        return self._DefaultPanelType

    @DefaultPanelType.setter
    def DefaultPanelType(self, DefaultPanelType):
        self._DefaultPanelType = DefaultPanelType

    @property
    def PanelScope(self):
        return self._PanelScope

    @PanelScope.setter
    def PanelScope(self, PanelScope):
        self._PanelScope = PanelScope

    @property
    def ManagePlatform(self):
        return self._ManagePlatform

    @ManagePlatform.setter
    def ManagePlatform(self, ManagePlatform):
        self._ManagePlatform = ManagePlatform


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ColorCode = params.get("ColorCode")
        self._Logo = params.get("Logo")
        self._Mark = params.get("Mark")
        self._IsApply = params.get("IsApply")
        self._Seed = params.get("Seed")
        self._DefaultPanelType = params.get("DefaultPanelType")
        self._PanelScope = params.get("PanelScope")
        self._ManagePlatform = params.get("ManagePlatform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Data: 返回数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _Msg: 结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Data = None
        self._Msg = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Data = params.get("Data")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyUserRoleProjectRequest(AbstractModel):
    """ModifyUserRoleProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _UserId: 用户ID
        :type UserId: str
        :param _RoleIdList: 角色ID 列表
        :type RoleIdList: list of int
        :param _Email: 邮箱
        :type Email: str
        :param _UserName: 用户名
        :type UserName: str
        :param _AppUserId: 企业微信应用用户id
        :type AppUserId: str
        """
        self._ProjectId = None
        self._UserId = None
        self._RoleIdList = None
        self._Email = None
        self._UserName = None
        self._AppUserId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoleIdList(self):
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def AppUserId(self):
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._UserId = params.get("UserId")
        self._RoleIdList = params.get("RoleIdList")
        self._Email = params.get("Email")
        self._UserName = params.get("UserName")
        self._AppUserId = params.get("AppUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserRoleProjectResponse(AbstractModel):
    """ModifyUserRoleProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class ModifyUserRoleRequest(AbstractModel):
    """ModifyUserRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _RoleIdList: 角色ID 列表
        :type RoleIdList: list of int
        :param _Email: 邮箱
        :type Email: str
        :param _UserName: 用户名
        :type UserName: str
        :param _PhoneNumber: 手机号
        :type PhoneNumber: str
        :param _AreaCode: 手机区号
        :type AreaCode: str
        :param _AppUserId: 企业微信应用用户id
        :type AppUserId: str
        """
        self._UserId = None
        self._RoleIdList = None
        self._Email = None
        self._UserName = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._AppUserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoleIdList(self):
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def AppUserId(self):
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RoleIdList = params.get("RoleIdList")
        self._Email = params.get("Email")
        self._UserName = params.get("UserName")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._AppUserId = params.get("AppUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserRoleResponse(AbstractModel):
    """ModifyUserRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorInfo: 自定义错误信息对象
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.bi.v20220105.models.ErrorInfo`
        :param _Extra: 扩展
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Msg: 消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Data: 数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorInfo = None
        self._Extra = None
        self._Msg = None
        self._Data = None
        self._RequestId = None

    @property
    def ErrorInfo(self):
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Extra = params.get("Extra")
        self._Msg = params.get("Msg")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class PermissionComponent(AbstractModel):
    """商业版本权限单元

    """

    def __init__(self):
        r"""
        :param _ModuleId: 权限值
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleId: str
        :param _IncludeType: 可见/可用
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeType: str
        :param _UpgradeVersionType: 目标升级版本
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeVersionType: str
        :param _Tips: 补充信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tips: str
        :param _TipsKey: 补充信息的key值
注意：此字段可能返回 null，表示取不到有效值。
        :type TipsKey: str
        """
        self._ModuleId = None
        self._IncludeType = None
        self._UpgradeVersionType = None
        self._Tips = None
        self._TipsKey = None

    @property
    def ModuleId(self):
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def IncludeType(self):
        return self._IncludeType

    @IncludeType.setter
    def IncludeType(self, IncludeType):
        self._IncludeType = IncludeType

    @property
    def UpgradeVersionType(self):
        return self._UpgradeVersionType

    @UpgradeVersionType.setter
    def UpgradeVersionType(self, UpgradeVersionType):
        self._UpgradeVersionType = UpgradeVersionType

    @property
    def Tips(self):
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def TipsKey(self):
        return self._TipsKey

    @TipsKey.setter
    def TipsKey(self, TipsKey):
        self._TipsKey = TipsKey


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._IncludeType = params.get("IncludeType")
        self._UpgradeVersionType = params.get("UpgradeVersionType")
        self._Tips = params.get("Tips")
        self._TipsKey = params.get("TipsKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PermissionGroup(AbstractModel):
    """商业化版本权限分组

    """

    def __init__(self):
        r"""
        :param _ModuleGroup: 分组名
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleGroup: str
        :param _Components: 权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Components: list of PermissionComponent
        """
        self._ModuleGroup = None
        self._Components = None

    @property
    def ModuleGroup(self):
        return self._ModuleGroup

    @ModuleGroup.setter
    def ModuleGroup(self, ModuleGroup):
        self._ModuleGroup = ModuleGroup

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components


    def _deserialize(self, params):
        self._ModuleGroup = params.get("ModuleGroup")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = PermissionComponent()
                obj._deserialize(item)
                self._Components.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Project(AbstractModel):
    """项目信息描述

    """

    def __init__(self):
        r"""
        :param _Id: 项目ID
        :type Id: int
        :param _Logo: 项目Logo
注意：此字段可能返回 null，表示取不到有效值。
        :type Logo: str
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _ColorCode: logo底色
注意：此字段可能返回 null，表示取不到有效值。
        :type ColorCode: str
        :param _CreatedUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedUser: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _MemberCount: 成员个数
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberCount: int
        :param _PageCount: 页面个数
注意：此字段可能返回 null，表示取不到有效值。
        :type PageCount: int
        :param _LastModifyName: 最后修改报表、简报名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModifyName: str
        :param _Source: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Apply: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Apply: bool
        :param _UpdatedUser: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedUser: str
        :param _UpdatedAt: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _CorpId: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: str
        :param _Mark: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Mark: str
        :param _Seed: ""
注意：此字段可能返回 null，表示取不到有效值。
        :type Seed: str
        :param _AuthList: 项目内权限列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthList: list of str
        :param _PanelScope: 默认看板
注意：此字段可能返回 null，表示取不到有效值。
        :type PanelScope: str
        :param _IsExternalManage: 是否被托管
注意：此字段可能返回 null，表示取不到有效值。
        :type IsExternalManage: bool
        :param _ManagePlatform: 托管平台名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagePlatform: str
        :param _ConfigList: 定制化参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigList: list of ProjectConfigList
        """
        self._Id = None
        self._Logo = None
        self._Name = None
        self._ColorCode = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._MemberCount = None
        self._PageCount = None
        self._LastModifyName = None
        self._Source = None
        self._Apply = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._CorpId = None
        self._Mark = None
        self._Seed = None
        self._AuthList = None
        self._PanelScope = None
        self._IsExternalManage = None
        self._ManagePlatform = None
        self._ConfigList = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Logo(self):
        return self._Logo

    @Logo.setter
    def Logo(self, Logo):
        self._Logo = Logo

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ColorCode(self):
        return self._ColorCode

    @ColorCode.setter
    def ColorCode(self, ColorCode):
        self._ColorCode = ColorCode

    @property
    def CreatedUser(self):
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def MemberCount(self):
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def PageCount(self):
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def LastModifyName(self):
        return self._LastModifyName

    @LastModifyName.setter
    def LastModifyName(self, LastModifyName):
        self._LastModifyName = LastModifyName

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Apply(self):
        return self._Apply

    @Apply.setter
    def Apply(self, Apply):
        self._Apply = Apply

    @property
    def UpdatedUser(self):
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Mark(self):
        return self._Mark

    @Mark.setter
    def Mark(self, Mark):
        self._Mark = Mark

    @property
    def Seed(self):
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def AuthList(self):
        return self._AuthList

    @AuthList.setter
    def AuthList(self, AuthList):
        self._AuthList = AuthList

    @property
    def PanelScope(self):
        return self._PanelScope

    @PanelScope.setter
    def PanelScope(self, PanelScope):
        self._PanelScope = PanelScope

    @property
    def IsExternalManage(self):
        return self._IsExternalManage

    @IsExternalManage.setter
    def IsExternalManage(self, IsExternalManage):
        self._IsExternalManage = IsExternalManage

    @property
    def ManagePlatform(self):
        return self._ManagePlatform

    @ManagePlatform.setter
    def ManagePlatform(self, ManagePlatform):
        self._ManagePlatform = ManagePlatform

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Logo = params.get("Logo")
        self._Name = params.get("Name")
        self._ColorCode = params.get("ColorCode")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._MemberCount = params.get("MemberCount")
        self._PageCount = params.get("PageCount")
        self._LastModifyName = params.get("LastModifyName")
        self._Source = params.get("Source")
        self._Apply = params.get("Apply")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._CorpId = params.get("CorpId")
        self._Mark = params.get("Mark")
        self._Seed = params.get("Seed")
        self._AuthList = params.get("AuthList")
        self._PanelScope = params.get("PanelScope")
        self._IsExternalManage = params.get("IsExternalManage")
        self._ManagePlatform = params.get("ManagePlatform")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ProjectConfigList()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectConfigList(AbstractModel):
    """定制化查询

    """

    def __init__(self):
        r"""
        :param _ModuleGroup: 模块组
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleGroup: str
        :param _Components: 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Components: list of ProjectConfigResult
        """
        self._ModuleGroup = None
        self._Components = None

    @property
    def ModuleGroup(self):
        return self._ModuleGroup

    @ModuleGroup.setter
    def ModuleGroup(self, ModuleGroup):
        self._ModuleGroup = ModuleGroup

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components


    def _deserialize(self, params):
        self._ModuleGroup = params.get("ModuleGroup")
        if params.get("Components") is not None:
            self._Components = []
            for item in params.get("Components"):
                obj = ProjectConfigResult()
                obj._deserialize(item)
                self._Components.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectConfigResult(AbstractModel):
    """定制化查询

    """

    def __init__(self):
        r"""
        :param _ModuleId: 配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleId: str
        :param _IncludeType: 配置方式
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeType: str
        :param _Params: 额外参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: str
        """
        self._ModuleId = None
        self._IncludeType = None
        self._Params = None

    @property
    def ModuleId(self):
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def IncludeType(self):
        return self._IncludeType

    @IncludeType.setter
    def IncludeType(self, IncludeType):
        self._IncludeType = IncludeType

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._IncludeType = params.get("IncludeType")
        self._Params = params.get("Params")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectListData(AbstractModel):
    """项目列表数据

    """

    def __init__(self):
        r"""
        :param _List: 数组
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of Project
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _TotalPages: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPages: int
        """
        self._List = None
        self._Total = None
        self._TotalPages = None

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = Project()
                obj._deserialize(item)
                self._List.append(obj)
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserIdAndUserName(AbstractModel):
    """用户ID和用户名

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _CorpId: 企业ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpId: str
        :param _Email: 电子邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _LastLogin: 最后一次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLogin: str
        :param _Status: 停启用状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _FirstModify: 首次登陆是否修改密码
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstModify: int
        :param _PhoneNumber: 手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _AreaCode: 手机区号
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCode: str
        :param _CreatedUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedUser: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedUser: 更改人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedUser: str
        :param _UpdatedAt: 更改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _GlobalUserName: 全局角色
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalUserName: str
        :param _Mobile: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        :param _AppId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _AppUserId: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserId: str
        :param _AppUserAliasName: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserAliasName: str
        :param _AppUserName: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserName: str
        :param _InValidateAppRange: 1
注意：此字段可能返回 null，表示取不到有效值。
        :type InValidateAppRange: bool
        """
        self._UserId = None
        self._UserName = None
        self._CorpId = None
        self._Email = None
        self._LastLogin = None
        self._Status = None
        self._FirstModify = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._GlobalUserName = None
        self._Mobile = None
        self._AppId = None
        self._AppUserId = None
        self._AppUserAliasName = None
        self._AppUserName = None
        self._InValidateAppRange = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def LastLogin(self):
        return self._LastLogin

    @LastLogin.setter
    def LastLogin(self, LastLogin):
        self._LastLogin = LastLogin

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FirstModify(self):
        return self._FirstModify

    @FirstModify.setter
    def FirstModify(self, FirstModify):
        self._FirstModify = FirstModify

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def CreatedUser(self):
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedUser(self):
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def GlobalUserName(self):
        return self._GlobalUserName

    @GlobalUserName.setter
    def GlobalUserName(self, GlobalUserName):
        self._GlobalUserName = GlobalUserName

    @property
    def Mobile(self):
        return self._Mobile

    @Mobile.setter
    def Mobile(self, Mobile):
        self._Mobile = Mobile

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppUserId(self):
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId

    @property
    def AppUserAliasName(self):
        return self._AppUserAliasName

    @AppUserAliasName.setter
    def AppUserAliasName(self, AppUserAliasName):
        self._AppUserAliasName = AppUserAliasName

    @property
    def AppUserName(self):
        return self._AppUserName

    @AppUserName.setter
    def AppUserName(self, AppUserName):
        self._AppUserName = AppUserName

    @property
    def InValidateAppRange(self):
        return self._InValidateAppRange

    @InValidateAppRange.setter
    def InValidateAppRange(self, InValidateAppRange):
        self._InValidateAppRange = InValidateAppRange


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._CorpId = params.get("CorpId")
        self._Email = params.get("Email")
        self._LastLogin = params.get("LastLogin")
        self._Status = params.get("Status")
        self._FirstModify = params.get("FirstModify")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._GlobalUserName = params.get("GlobalUserName")
        self._Mobile = params.get("Mobile")
        self._AppId = params.get("AppId")
        self._AppUserId = params.get("AppUserId")
        self._AppUserAliasName = params.get("AppUserAliasName")
        self._AppUserName = params.get("AppUserName")
        self._InValidateAppRange = params.get("InValidateAppRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfo(AbstractModel):
    """用户ID和用户名

    """

    def __init__(self):
        r"""
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _PhoneNumber: 手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _AreaCode: 手机号区号
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCode: str
        :param _AppUserId: 企微账号id
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserId: str
        :param _AppUserName: 企微账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserName: str
        """
        self._UserId = None
        self._UserName = None
        self._Email = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._AppUserId = None
        self._AppUserName = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def AppUserId(self):
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId

    @property
    def AppUserName(self):
        return self._AppUserName

    @AppUserName.setter
    def AppUserName(self, AppUserName):
        self._AppUserName = AppUserName


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._Email = params.get("Email")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._AppUserId = params.get("AppUserId")
        self._AppUserName = params.get("AppUserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserRoleListData(AbstractModel):
    """用户角色信息

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _TotalPages: 总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPages: int
        :param _List: 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of UserRoleListDataUserRoleInfo
        """
        self._Total = None
        self._TotalPages = None
        self._List = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def TotalPages(self):
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._TotalPages = params.get("TotalPages")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UserRoleListDataUserRoleInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserRoleListDataRoleInfo(AbstractModel):
    """用户角色列表角色信息

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名字
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param _RoleId: 角色ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: int
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _ProjectName: 项目名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _ScopeType: 是否为全局角色（0 不是 1 是）
注意：此字段可能返回 null，表示取不到有效值。
        :type ScopeType: int
        :param _ModuleCollection: 角色key
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleCollection: str
        """
        self._RoleName = None
        self._RoleId = None
        self._ProjectId = None
        self._ProjectName = None
        self._ScopeType = None
        self._ModuleCollection = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def RoleId(self):
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ScopeType(self):
        return self._ScopeType

    @ScopeType.setter
    def ScopeType(self, ScopeType):
        self._ScopeType = ScopeType

    @property
    def ModuleCollection(self):
        return self._ModuleCollection

    @ModuleCollection.setter
    def ModuleCollection(self, ModuleCollection):
        self._ModuleCollection = ModuleCollection


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._RoleId = params.get("RoleId")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ScopeType = params.get("ScopeType")
        self._ModuleCollection = params.get("ModuleCollection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserRoleListDataUserRoleInfo(AbstractModel):
    """用户角色信息

    """

    def __init__(self):
        r"""
        :param _Id: 业务ID
        :type Id: int
        :param _RoleList: 角色列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleList: list of UserRoleListDataRoleInfo
        :param _RoleIdList: 角色ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleIdList: list of int non-negative
        :param _UserId: 用户ID
        :type UserId: str
        :param _UserName: 用户名
        :type UserName: str
        :param _CorpId: 企业ID
        :type CorpId: str
        :param _Email: 邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param _CreatedUser: 创建人
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedUser: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedUser: 更新人
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedUser: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _LastLogin: 最后一次登录时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastLogin: str
        :param _Status: 账号状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _PhoneNumber: 手机号码
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _AreaCode: 手机号区号
注意：此字段可能返回 null，表示取不到有效值。
        :type AreaCode: str
        :param _RootAccount: 是否为主账号
注意：此字段可能返回 null，表示取不到有效值。
        :type RootAccount: bool
        :param _CorpAdmin: 是否为企业管理员
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpAdmin: bool
        :param _AppUserId: 企微用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserId: str
        :param _AppUserAliasName: 昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserAliasName: str
        :param _AppUserName: 应用用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUserName: str
        :param _InValidateAppRange: 是否在可见范围内
注意：此字段可能返回 null，表示取不到有效值。
        :type InValidateAppRange: bool
        :param _AppOpenUserId: 用户openid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppOpenUserId: str
        """
        self._Id = None
        self._RoleList = None
        self._RoleIdList = None
        self._UserId = None
        self._UserName = None
        self._CorpId = None
        self._Email = None
        self._CreatedUser = None
        self._CreatedAt = None
        self._UpdatedUser = None
        self._UpdatedAt = None
        self._LastLogin = None
        self._Status = None
        self._PhoneNumber = None
        self._AreaCode = None
        self._RootAccount = None
        self._CorpAdmin = None
        self._AppUserId = None
        self._AppUserAliasName = None
        self._AppUserName = None
        self._InValidateAppRange = None
        self._AppOpenUserId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RoleList(self):
        return self._RoleList

    @RoleList.setter
    def RoleList(self, RoleList):
        self._RoleList = RoleList

    @property
    def RoleIdList(self):
        return self._RoleIdList

    @RoleIdList.setter
    def RoleIdList(self, RoleIdList):
        self._RoleIdList = RoleIdList

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def CorpId(self):
        return self._CorpId

    @CorpId.setter
    def CorpId(self, CorpId):
        self._CorpId = CorpId

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CreatedUser(self):
        return self._CreatedUser

    @CreatedUser.setter
    def CreatedUser(self, CreatedUser):
        self._CreatedUser = CreatedUser

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedUser(self):
        return self._UpdatedUser

    @UpdatedUser.setter
    def UpdatedUser(self, UpdatedUser):
        self._UpdatedUser = UpdatedUser

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def LastLogin(self):
        return self._LastLogin

    @LastLogin.setter
    def LastLogin(self, LastLogin):
        self._LastLogin = LastLogin

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AreaCode(self):
        return self._AreaCode

    @AreaCode.setter
    def AreaCode(self, AreaCode):
        self._AreaCode = AreaCode

    @property
    def RootAccount(self):
        return self._RootAccount

    @RootAccount.setter
    def RootAccount(self, RootAccount):
        self._RootAccount = RootAccount

    @property
    def CorpAdmin(self):
        return self._CorpAdmin

    @CorpAdmin.setter
    def CorpAdmin(self, CorpAdmin):
        self._CorpAdmin = CorpAdmin

    @property
    def AppUserId(self):
        return self._AppUserId

    @AppUserId.setter
    def AppUserId(self, AppUserId):
        self._AppUserId = AppUserId

    @property
    def AppUserAliasName(self):
        return self._AppUserAliasName

    @AppUserAliasName.setter
    def AppUserAliasName(self, AppUserAliasName):
        self._AppUserAliasName = AppUserAliasName

    @property
    def AppUserName(self):
        return self._AppUserName

    @AppUserName.setter
    def AppUserName(self, AppUserName):
        self._AppUserName = AppUserName

    @property
    def InValidateAppRange(self):
        return self._InValidateAppRange

    @InValidateAppRange.setter
    def InValidateAppRange(self, InValidateAppRange):
        self._InValidateAppRange = InValidateAppRange

    @property
    def AppOpenUserId(self):
        return self._AppOpenUserId

    @AppOpenUserId.setter
    def AppOpenUserId(self, AppOpenUserId):
        self._AppOpenUserId = AppOpenUserId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("RoleList") is not None:
            self._RoleList = []
            for item in params.get("RoleList"):
                obj = UserRoleListDataRoleInfo()
                obj._deserialize(item)
                self._RoleList.append(obj)
        self._RoleIdList = params.get("RoleIdList")
        self._UserId = params.get("UserId")
        self._UserName = params.get("UserName")
        self._CorpId = params.get("CorpId")
        self._Email = params.get("Email")
        self._CreatedUser = params.get("CreatedUser")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedUser = params.get("UpdatedUser")
        self._UpdatedAt = params.get("UpdatedAt")
        self._LastLogin = params.get("LastLogin")
        self._Status = params.get("Status")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AreaCode = params.get("AreaCode")
        self._RootAccount = params.get("RootAccount")
        self._CorpAdmin = params.get("CorpAdmin")
        self._AppUserId = params.get("AppUserId")
        self._AppUserAliasName = params.get("AppUserAliasName")
        self._AppUserName = params.get("AppUserName")
        self._InValidateAppRange = params.get("InValidateAppRange")
        self._AppOpenUserId = params.get("AppOpenUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        