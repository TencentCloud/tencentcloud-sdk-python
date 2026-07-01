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


class CompareCondition(AbstractModel):
    r"""BugLY比较结构体

    """

    def __init__(self):
        r"""
        :param _AppVersion: App版本
        :type AppVersion: str
        :param _Filters: 筛选条件
        :type Filters: :class:`tencentcloud.rum.v20210622.models.Filters`
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._AppVersion = None
        self._Filters = None
        self._StartTime = None
        self._EndTime = None

    @property
    def AppVersion(self):
        r"""App版本
        :rtype: str
        """
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def Filters(self):
        r"""筛选条件
        :rtype: :class:`tencentcloud.rum.v20210622.models.Filters`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._AppVersion = params.get("AppVersion")
        if params.get("Filters") is not None:
            self._Filters = Filters()
            self._Filters._deserialize(params.get("Filters"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseFileRequest(AbstractModel):
    r"""CreateReleaseFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: 项目 id
        :type ProjectID: int
        :param _Files: 文件信息列表
        :type Files: list of ReleaseFile
        """
        self._ProjectID = None
        self._Files = None

    @property
    def ProjectID(self):
        r"""项目 id
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def Files(self):
        r"""文件信息列表
        :rtype: list of ReleaseFile
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self._Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseFileResponse(AbstractModel):
    r"""CreateReleaseFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 调用结果
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""调用结果
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateStarProjectRequest(AbstractModel):
    r"""CreateStarProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例ID：taw-123
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStarProjectResponse(AbstractModel):
    r"""CreateStarProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 接口返回信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""接口返回信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateWhitelistRequest(AbstractModel):
    r"""CreateWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID：taw-123
        :type InstanceID: str
        :param _Remark: 备注（暂未作字节数限制）
        :type Remark: str
        :param _WhitelistUin: uin：业务方标识
        :type WhitelistUin: str
        :param _Aid: 业务方标识
        :type Aid: str
        """
        self._InstanceID = None
        self._Remark = None
        self._WhitelistUin = None
        self._Aid = None

    @property
    def InstanceID(self):
        r"""实例ID：taw-123
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Remark(self):
        r"""备注（暂未作字节数限制）
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def WhitelistUin(self):
        r"""uin：业务方标识
        :rtype: str
        """
        return self._WhitelistUin

    @WhitelistUin.setter
    def WhitelistUin(self, WhitelistUin):
        self._WhitelistUin = WhitelistUin

    @property
    def Aid(self):
        r"""业务方标识
        :rtype: str
        """
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Remark = params.get("Remark")
        self._WhitelistUin = params.get("WhitelistUin")
        self._Aid = params.get("Aid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhitelistResponse(AbstractModel):
    r"""CreateWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 消息
        :type Msg: str
        :param _ID: 白名单ID
        :type ID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._ID = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""消息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def ID(self):
        r"""白名单ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

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
        self._Msg = params.get("Msg")
        self._ID = params.get("ID")
        self._RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    r"""DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要删除的实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""需要删除的实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    r"""DeleteInstance返回参数结构体

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


class DeleteProjectRequest(AbstractModel):
    r"""DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 需要删除的项目 ID
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        r"""需要删除的项目 ID
        :rtype: int
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
        


class DeleteProjectResponse(AbstractModel):
    r"""DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 操作信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""操作信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteReleaseFileRequest(AbstractModel):
    r"""DeleteReleaseFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 文件 id
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        r"""文件 id
        :rtype: int
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
        


class DeleteReleaseFileResponse(AbstractModel):
    r"""DeleteReleaseFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 接口请求返回字符串
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""接口请求返回字符串
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteStarProjectRequest(AbstractModel):
    r"""DeleteStarProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID：****-1792
        :type InstanceID: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例ID：****-1792
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStarProjectResponse(AbstractModel):
    r"""DeleteStarProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 返回消息,请求成功才会返回，出现异常默认为null
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""返回消息,请求成功才会返回，出现异常默认为null
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteWhitelistRequest(AbstractModel):
    r"""DeleteWhitelist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _ID: 名单ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        r"""名单ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhitelistResponse(AbstractModel):
    r"""DeleteWhitelist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 消息success
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""消息success
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeAppDimensionMetricsRequest(AbstractModel):
    r"""DescribeAppDimensionMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 fields
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        :param _BusinessContext: 业务上下文参数
        :type BusinessContext: str
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._BusinessContext = None

    @property
    def ProjectID(self):
        r"""app 项目ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        r"""查询的表名
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        r"""查询指标 fields
        :rtype: str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        r"""查询的过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        r"""查询简单过滤条件
        :rtype: str
        """
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        r"""group by 条件
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        r"""order by 条件
        :rtype: list of str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""limit 参数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""offset 参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def BusinessContext(self):
        r"""业务上下文参数
        :rtype: str
        """
        return self._BusinessContext

    @BusinessContext.setter
    def BusinessContext(self, BusinessContext):
        self._BusinessContext = BusinessContext


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._BusinessContext = params.get("BusinessContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppDimensionMetricsResponse(AbstractModel):
    r"""DescribeAppDimensionMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询数据返回
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeAppMetricsDataRequest(AbstractModel):
    r"""DescribeAppMetricsData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 field
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        :param _GroupByModifier: group by 参数
        :type GroupByModifier: str
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._GroupByModifier = None

    @property
    def ProjectID(self):
        r"""app 项目ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        r"""查询的表名
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        r"""查询指标 field
        :rtype: str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        r"""查询的过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        r"""查询简单过滤条件
        :rtype: str
        """
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        r"""group by 条件
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        r"""order by 条件
        :rtype: list of str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""limit 参数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""offset 参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def GroupByModifier(self):
        r"""group by 参数
        :rtype: str
        """
        return self._GroupByModifier

    @GroupByModifier.setter
    def GroupByModifier(self, GroupByModifier):
        self._GroupByModifier = GroupByModifier


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._GroupByModifier = params.get("GroupByModifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppMetricsDataResponse(AbstractModel):
    r"""DescribeAppMetricsData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询数据返回
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeAppSingleCaseDetailListRequest(AbstractModel):
    r"""DescribeAppSingleCaseDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 field
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def ProjectID(self):
        r"""app 项目ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        r"""查询的表名
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        r"""查询指标 field
        :rtype: str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        r"""查询的过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        r"""查询简单过滤条件
        :rtype: str
        """
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        r"""group by 条件
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        r"""order by 条件
        :rtype: list of str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""limit 参数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""offset 参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppSingleCaseDetailListResponse(AbstractModel):
    r"""DescribeAppSingleCaseDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询数据返回
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeAppSingleCaseListRequest(AbstractModel):
    r"""DescribeAppSingleCaseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: app 项目 ID
        :type ProjectID: int
        :param _From: 查询的表名
        :type From: str
        :param _Fields: 查询指标 field
        :type Fields: str
        :param _Filter: 查询的过滤条件
        :type Filter: str
        :param _FilterSimple: 查询简单过滤条件
        :type FilterSimple: str
        :param _GroupBy: group by 条件
        :type GroupBy: list of str
        :param _OrderBy: order by 条件
        :type OrderBy: list of str
        :param _Limit: limit 参数
        :type Limit: int
        :param _Offset: offset 参数
        :type Offset: int
        """
        self._ProjectID = None
        self._From = None
        self._Fields = None
        self._Filter = None
        self._FilterSimple = None
        self._GroupBy = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None

    @property
    def ProjectID(self):
        r"""app 项目 ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def From(self):
        r"""查询的表名
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Fields(self):
        r"""查询指标 field
        :rtype: str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields

    @property
    def Filter(self):
        r"""查询的过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterSimple(self):
        r"""查询简单过滤条件
        :rtype: str
        """
        return self._FilterSimple

    @FilterSimple.setter
    def FilterSimple(self, FilterSimple):
        self._FilterSimple = FilterSimple

    @property
    def GroupBy(self):
        r"""group by 条件
        :rtype: list of str
        """
        return self._GroupBy

    @GroupBy.setter
    def GroupBy(self, GroupBy):
        self._GroupBy = GroupBy

    @property
    def OrderBy(self):
        r"""order by 条件
        :rtype: list of str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        r"""limit 参数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""offset 参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._From = params.get("From")
        self._Fields = params.get("Fields")
        self._Filter = params.get("Filter")
        self._FilterSimple = params.get("FilterSimple")
        self._GroupBy = params.get("GroupBy")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppSingleCaseListResponse(AbstractModel):
    r"""DescribeAppSingleCaseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 查询数据返回
        :type Data: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""查询数据返回
        :rtype: str
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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeApplicationExitReportDetailRequest(AbstractModel):
    r"""DescribeApplicationExitReportDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _ClientIdentify: <p>问题Id</p>
        :type ClientIdentify: str
        :param _StartEventTime: <p>开始时间</p>
        :type StartEventTime: int
        :param _EndEventTime: <p>结束时间</p>
        :type EndEventTime: int
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ParamToken = None
        self._ClientIdentify = None
        self._StartEventTime = None
        self._EndEventTime = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def ClientIdentify(self):
        r"""<p>问题Id</p>
        :rtype: str
        """
        return self._ClientIdentify

    @ClientIdentify.setter
    def ClientIdentify(self, ClientIdentify):
        self._ClientIdentify = ClientIdentify

    @property
    def StartEventTime(self):
        r"""<p>开始时间</p>
        :rtype: int
        """
        return self._StartEventTime

    @StartEventTime.setter
    def StartEventTime(self, StartEventTime):
        self._StartEventTime = StartEventTime

    @property
    def EndEventTime(self):
        r"""<p>结束时间</p>
        :rtype: int
        """
        return self._EndEventTime

    @EndEventTime.setter
    def EndEventTime(self, EndEventTime):
        self._EndEventTime = EndEventTime

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParamToken = params.get("ParamToken")
        self._ClientIdentify = params.get("ClientIdentify")
        self._StartEventTime = params.get("StartEventTime")
        self._EndEventTime = params.get("EndEventTime")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationExitReportDetailResponse(AbstractModel):
    r"""DescribeApplicationExitReportDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeApplicationExitReportListRequest(AbstractModel):
    r"""DescribeApplicationExitReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页展示最大数量</p>
        :type PageSize: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序类型</p>
        :type SortType: str
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ParamToken = None
        self._FormListString = None
        self._PageNumber = None
        self._PageSize = None
        self._SortField = None
        self._SortType = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页展示最大数量</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序类型</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParamToken = params.get("ParamToken")
        self._FormListString = params.get("FormListString")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationExitReportListResponse(AbstractModel):
    r"""DescribeApplicationExitReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeDataBridgeUrlV2Request(AbstractModel):
    r"""DescribeDataBridgeUrlV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目ID
        :type ID: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Type: pagepv：性能视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param _Level: 日志等级
        :type Level: str
        :param _Isp: 运营商
        :type Isp: str
        :param _Area: 地区
        :type Area: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Platform: 平台
        :type Platform: str
        :param _Device: 机型
        :type Device: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _IsAbroad: 是否海外
        :type IsAbroad: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Os: 操作系统
        :type Os: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Brand: 品牌
        :type Brand: str
        :param _From: 来源页面
        :type From: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Env: 环境变量
        :type Env: str
        :param _Name: url名称
        :type Name: str
        :param _Status: http状态码
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        :param _NetStatus: 网络状态
        :type NetStatus: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Level = None
        self._Isp = None
        self._Area = None
        self._NetType = None
        self._Platform = None
        self._Device = None
        self._VersionNum = None
        self._ExtFirst = None
        self._ExtSecond = None
        self._ExtThird = None
        self._IsAbroad = None
        self._Browser = None
        self._Os = None
        self._Engine = None
        self._Brand = None
        self._From = None
        self._CostType = None
        self._Env = None
        self._Name = None
        self._Status = None
        self._Ret = None
        self._NetStatus = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""pagepv：性能视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def IsAbroad(self):
        r"""是否海外
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CostType(self):
        r"""耗时计算方式
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        r"""环境变量
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Name(self):
        r"""url名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""http状态码
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        r"""retcode
        :rtype: str
        """
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def NetStatus(self):
        r"""网络状态
        :rtype: str
        """
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        self._Isp = params.get("Isp")
        self._Area = params.get("Area")
        self._NetType = params.get("NetType")
        self._Platform = params.get("Platform")
        self._Device = params.get("Device")
        self._VersionNum = params.get("VersionNum")
        self._ExtFirst = params.get("ExtFirst")
        self._ExtSecond = params.get("ExtSecond")
        self._ExtThird = params.get("ExtThird")
        self._IsAbroad = params.get("IsAbroad")
        self._Browser = params.get("Browser")
        self._Os = params.get("Os")
        self._Engine = params.get("Engine")
        self._Brand = params.get("Brand")
        self._From = params.get("From")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        self._NetStatus = params.get("NetStatus")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataBridgeUrlV2Response(AbstractModel):
    r"""DescribeDataBridgeUrlV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataCustomUrlRequest(AbstractModel):
    r"""DescribeDataCustomUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: top：资源top视图，allcount：性能视图，day：14天数据，condition：条件列表，pagepv：性能视图，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（使用 percentile2 计算分位数）；"avg" 表示均值（使用 avg 计算）。
        :type CostType: str
        :param _Url: 自定义测速的key的值
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""top：资源top视图，allcount：性能视图，day：14天数据，condition：条件列表，pagepv：性能视图，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（使用 percentile2 计算分位数）；"avg" 表示均值（使用 avg 计算）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""自定义测速的key的值
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataCustomUrlResponse(AbstractModel):
    r"""DescribeDataCustomUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataCustomUrlV2Request(AbstractModel):
    r"""DescribeDataCustomUrlV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: top：资源top视图，allcount：性能视图，day：14天数据，condition：条件列表，pagepv：性能视图，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 自定义测速的key的值
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""top：资源top视图，allcount：性能视图，day：14天数据，condition：条件列表，pagepv：性能视图，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时计算方式
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""自定义测速的key的值
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataCustomUrlV2Response(AbstractModel):
    r"""DescribeDataCustomUrlV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataEventUrlRequest(AbstractModel):
    r"""DescribeDataEventUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，ckuv：获取uv趋势，ckpv：获取pv趋势，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: netType | 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。也可通过 Type=condition（show tag values）查询当前数据集中的实际可选值。

        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Name: 筛选条件
        :type Name: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Name = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，day：14天数据，condition：条件列表，ckuv：获取uv趋势，ckpv：获取pv趋势，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""netType | 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。也可通过 Type=condition（show tag values）查询当前数据集中的实际可选值。

        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Name(self):
        r"""筛选条件
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Name = params.get("Name")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEventUrlResponse(AbstractModel):
    r"""DescribeDataEventUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataEventUrlV2Request(AbstractModel):
    r"""DescribeDataEventUrlV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，ckuv：获取uv趋势，ckpv：获取pv趋势，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Name: 筛选条件
        :type Name: str
        :param _Env: 环境
        :type Env: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Name = None
        self._Env = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，day：14天数据，condition：条件列表，ckuv：获取uv趋势，ckpv：获取pv趋势，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Name(self):
        r"""筛选条件
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Name = params.get("Name")
        self._Env = params.get("Env")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEventUrlV2Response(AbstractModel):
    r"""DescribeDataEventUrlV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataFetchProjectRequest(AbstractModel):
    r"""DescribeDataFetchProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，示例值：1625454840
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间，示例值：1625454840
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _Status: HTTP 状态码（tag 值）：用于过滤字段 status；取值一般为 200/301/404/500 等，也可配合 4xx/5xx 统计逻辑使用
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._Status = None
        self._Ret = None

    @property
    def StartTime(self):
        r"""开始时间，示例值：1625454840
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间，示例值：1625454840
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        r"""HTTP 状态码（tag 值）：用于过滤字段 status；取值一般为 200/301/404/500 等，也可配合 4xx/5xx 统计逻辑使用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        r"""retcode
        :rtype: str
        """
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchProjectResponse(AbstractModel):
    r"""DescribeDataFetchProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataFetchUrlInfoRequest(AbstractModel):
    r"""DescribeDataFetchUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: Type	是	String	无枚举值。此接口不使用 Type 做分支判断，SQL 固定 group by "url"，Type 字段传任何值不影响查询。

        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""Type	是	String	无枚举值。此接口不使用 Type 做分支判断，SQL 固定 group by "url"，Type 字段传任何值不影响查询。

        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlInfoResponse(AbstractModel):
    r"""DescribeDataFetchUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataFetchUrlRequest(AbstractModel):
    r"""DescribeDataFetchUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，pagepv：pv视图，day：14天数据，count40x：40X视图，count50x：50X视图，count5xand4x：40∑50视图，top：资源top视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _Status: HTTP 状态码（tag 值）：用于过滤字段 status；支持 4xx（status =~ /4[0-9]{2}/）和 5xx（status =~ /5[0-9]{2}/）等错误码统计。
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        :param _NetStatus: 网络状态(tag 值):用于过滤/聚合字段 netStatus；枚举值：0(正常)、1(弱网)、2(断网)、3(其他)。
        :type NetStatus: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._Status = None
        self._Ret = None
        self._NetStatus = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，pagepv：pv视图，day：14天数据，count40x：40X视图，count50x：50X视图，count5xand4x：40∑50视图，top：资源top视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        r"""HTTP 状态码（tag 值）：用于过滤字段 status；支持 4xx（status =~ /4[0-9]{2}/）和 5xx（status =~ /5[0-9]{2}/）等错误码统计。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        r"""retcode
        :rtype: str
        """
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def NetStatus(self):
        r"""网络状态(tag 值):用于过滤/聚合字段 netStatus；枚举值：0(正常)、1(弱网)、2(断网)、3(其他)。
        :rtype: str
        """
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        self._NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlResponse(AbstractModel):
    r"""DescribeDataFetchUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataFetchUrlV2Request(AbstractModel):
    r"""DescribeDataFetchUrlV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，pagepv：pv视图，day：14天数据，count40x：40X视图，count50x：50X视图，count5xand4x：40∑50视图，top：资源top视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _Status: httpcode响应码
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        :param _NetStatus: 网络状态
        :type NetStatus: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._Status = None
        self._Ret = None
        self._NetStatus = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，pagepv：pv视图，day：14天数据，count40x：40X视图，count50x：50X视图，count5xand4x：40∑50视图，top：资源top视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时计算方式
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        r"""httpcode响应码
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        r"""retcode
        :rtype: str
        """
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def NetStatus(self):
        r"""网络状态
        :rtype: str
        """
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        self._NetStatus = params.get("NetStatus")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlV2Response(AbstractModel):
    r"""DescribeDataFetchUrlV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataLogUrlInfoRequest(AbstractModel):
    r"""DescribeDataLogUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目ID
        :type ID: int
        :param _StartTime: 时间戳
        :type StartTime: int
        :param _EndTime: 时间戳
        :type EndTime: int
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        r"""时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""时间戳
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlInfoResponse(AbstractModel):
    r"""DescribeDataLogUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回字符串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataLogUrlStatisticsRequest(AbstractModel):
    r"""DescribeDataLogUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: analysis：异常分析，compare：异常列表对比，allcount：性能视图，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Env: 环境区分
        :type Env: str
        :param _ErrorMsg: js异常信息
        :type ErrorMsg: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None
        self._ErrorMsg = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""analysis：异常分析，compare：异常列表对比，allcount：性能视图，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        r"""环境区分
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ErrorMsg(self):
        r"""js异常信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        self._ErrorMsg = params.get("ErrorMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlStatisticsResponse(AbstractModel):
    r"""DescribeDataLogUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataLogUrlStatisticsV2Request(AbstractModel):
    r"""DescribeDataLogUrlStatisticsV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: analysis：异常分析，compare：异常列表对比，allcount：性能视图，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Env: 环境区分
        :type Env: str
        :param _ErrorMsg: js异常信息
        :type ErrorMsg: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None
        self._ErrorMsg = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""analysis：异常分析，compare：异常列表对比，allcount：性能视图，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        r"""环境区分
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ErrorMsg(self):
        r"""js异常信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        self._ErrorMsg = params.get("ErrorMsg")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlStatisticsV2Response(AbstractModel):
    r"""DescribeDataLogUrlStatisticsV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPerformancePageRequest(AbstractModel):
    r"""DescribeDataPerformancePage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目ID
        :type ID: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Type: pagepv：pv视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param _Level: 日志等级
        :type Level: str
        :param _Isp: 运营商
        :type Isp: str
        :param _Area: 地区
        :type Area: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Platform: 平台
        :type Platform: str
        :param _Device: 机型
        :type Device: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Os: 操作系统
        :type Os: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Brand: 品牌
        :type Brand: str
        :param _From: 来源页面
        :type From: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Env: 环境变量
        :type Env: str
        :param _NetStatus: 网络状态(tag 值):用于过滤/聚合字段 netStatus；枚举值：0(正常)、1(弱网)、2(断网)、3(其他)。 
        :type NetStatus: str
        :param _WebVitals: 是否返回webvitals数据
        :type WebVitals: bool
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Level = None
        self._Isp = None
        self._Area = None
        self._NetType = None
        self._Platform = None
        self._Device = None
        self._VersionNum = None
        self._ExtFirst = None
        self._ExtSecond = None
        self._ExtThird = None
        self._IsAbroad = None
        self._Browser = None
        self._Os = None
        self._Engine = None
        self._Brand = None
        self._From = None
        self._CostType = None
        self._Env = None
        self._NetStatus = None
        self._WebVitals = None

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""pagepv：pv视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        r"""环境变量
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def NetStatus(self):
        r"""网络状态(tag 值):用于过滤/聚合字段 netStatus；枚举值：0(正常)、1(弱网)、2(断网)、3(其他)。 
        :rtype: str
        """
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus

    @property
    def WebVitals(self):
        r"""是否返回webvitals数据
        :rtype: bool
        """
        return self._WebVitals

    @WebVitals.setter
    def WebVitals(self, WebVitals):
        self._WebVitals = WebVitals


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        self._Isp = params.get("Isp")
        self._Area = params.get("Area")
        self._NetType = params.get("NetType")
        self._Platform = params.get("Platform")
        self._Device = params.get("Device")
        self._VersionNum = params.get("VersionNum")
        self._ExtFirst = params.get("ExtFirst")
        self._ExtSecond = params.get("ExtSecond")
        self._ExtThird = params.get("ExtThird")
        self._IsAbroad = params.get("IsAbroad")
        self._Browser = params.get("Browser")
        self._Os = params.get("Os")
        self._Engine = params.get("Engine")
        self._Brand = params.get("Brand")
        self._From = params.get("From")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._NetStatus = params.get("NetStatus")
        self._WebVitals = params.get("WebVitals")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformancePageResponse(AbstractModel):
    r"""DescribeDataPerformancePage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPerformancePageV2Request(AbstractModel):
    r"""DescribeDataPerformancePageV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目ID
        :type ID: int
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _Type: pagepv：pv视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param _Level: 日志等级
        :type Level: str
        :param _Isp: 运营商
        :type Isp: str
        :param _Area: 地区
        :type Area: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Platform: 平台
        :type Platform: str
        :param _Device: 机型
        :type Device: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Os: 操作系统
        :type Os: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Brand: 品牌
        :type Brand: str
        :param _From: 来源页面
        :type From: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Env: 环境变量
        :type Env: str
        :param _NetStatus: 网络状态
        :type NetStatus: str
        :param _WebVitals: 是否返回webvitals数据
        :type WebVitals: bool
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Level = None
        self._Isp = None
        self._Area = None
        self._NetType = None
        self._Platform = None
        self._Device = None
        self._VersionNum = None
        self._ExtFirst = None
        self._ExtSecond = None
        self._ExtThird = None
        self._IsAbroad = None
        self._Browser = None
        self._Os = None
        self._Engine = None
        self._Brand = None
        self._From = None
        self._CostType = None
        self._Env = None
        self._NetStatus = None
        self._WebVitals = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""pagepv：pv视图，allcount：性能视图，falls：页面加载瀑布图，samp：首屏时间，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CostType(self):
        r"""耗时计算方式
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        r"""环境变量
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def NetStatus(self):
        r"""网络状态
        :rtype: str
        """
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus

    @property
    def WebVitals(self):
        r"""是否返回webvitals数据
        :rtype: bool
        """
        return self._WebVitals

    @WebVitals.setter
    def WebVitals(self, WebVitals):
        self._WebVitals = WebVitals

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        self._Isp = params.get("Isp")
        self._Area = params.get("Area")
        self._NetType = params.get("NetType")
        self._Platform = params.get("Platform")
        self._Device = params.get("Device")
        self._VersionNum = params.get("VersionNum")
        self._ExtFirst = params.get("ExtFirst")
        self._ExtSecond = params.get("ExtSecond")
        self._ExtThird = params.get("ExtThird")
        self._IsAbroad = params.get("IsAbroad")
        self._Browser = params.get("Browser")
        self._Os = params.get("Os")
        self._Engine = params.get("Engine")
        self._Brand = params.get("Brand")
        self._From = params.get("From")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._NetStatus = params.get("NetStatus")
        self._WebVitals = params.get("WebVitals")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformancePageV2Response(AbstractModel):
    r"""DescribeDataPerformancePageV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPvUrlInfoRequest(AbstractModel):
    r"""DescribeDataPvUrlInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: 查询类型（string）：当前后端实现固定按 from 聚合统计，未使用该字段（保留字段，传值不会影响结果）。
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""查询类型（string）：当前后端实现固定按 from 聚合统计，未使用该字段（保留字段，传值不会影响结果）。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlInfoResponse(AbstractModel):
    r"""DescribeDataPvUrlInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPvUrlStatisticsRequest(AbstractModel):
    r"""DescribeDataPvUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，vp：性能，ckuv：uv，ckpv：pv，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _Env: 环境
        :type Env: str
        :param _GroupByType: group by 参数值枚举1:1m  2:5m  3:30m  4:1h 
 5:1d
        :type GroupByType: int
        :param _IsNewData: 1: 查询智研
0: 走旧逻辑，已下线，勿使用
        :type IsNewData: int
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None
        self._GroupByType = None
        self._IsNewData = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，day：14天数据，vp：性能，ckuv：uv，ckpv：pv，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def GroupByType(self):
        r"""group by 参数值枚举1:1m  2:5m  3:30m  4:1h 
 5:1d
        :rtype: int
        """
        return self._GroupByType

    @GroupByType.setter
    def GroupByType(self, GroupByType):
        self._GroupByType = GroupByType

    @property
    def IsNewData(self):
        r"""1: 查询智研
0: 走旧逻辑，已下线，勿使用
        :rtype: int
        """
        return self._IsNewData

    @IsNewData.setter
    def IsNewData(self, IsNewData):
        self._IsNewData = IsNewData


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        self._GroupByType = params.get("GroupByType")
        self._IsNewData = params.get("IsNewData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlStatisticsResponse(AbstractModel):
    r"""DescribeDataPvUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataPvUrlStatisticsV2Request(AbstractModel):
    r"""DescribeDataPvUrlStatisticsV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: <p>开始时间</p>
        :type StartTime: int
        :param _Type: <p>allcount：性能视图，day：14天数据，vp：性能，ckuv：uv，ckpv：pv，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等</p>
        :type Type: str
        :param _EndTime: <p>结束时间</p>
        :type EndTime: int
        :param _ID: <p>项目ID</p>
        :type ID: int
        :param _ExtSecond: <p>自定义2</p>
        :type ExtSecond: str
        :param _Engine: <p>浏览器引擎</p>
        :type Engine: str
        :param _Isp: <p>运营商</p>
        :type Isp: str
        :param _From: <p>来源页面， 可多选，用 “,” 隔开的 String</p>
        :type From: str
        :param _Level: <p>日志等级</p>
        :type Level: str
        :param _Brand: <p>品牌</p>
        :type Brand: str
        :param _Area: <p>地区</p>
        :type Area: str
        :param _VersionNum: <p>版本</p>
        :type VersionNum: str
        :param _Platform: <p>平台</p>
        :type Platform: str
        :param _ExtThird: <p>自定义3</p>
        :type ExtThird: str
        :param _ExtFirst: <p>自定义1</p>
        :type ExtFirst: str
        :param _NetType: <p>网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知</p>
        :type NetType: str
        :param _Device: <p>机型</p>
        :type Device: str
        :param _IsAbroad: <p>显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。</p>
        :type IsAbroad: str
        :param _Os: <p>操作系统</p>
        :type Os: str
        :param _Browser: <p>浏览器</p>
        :type Browser: str
        :param _Env: <p>环境</p>
        :type Env: str
        :param _GroupByType: <p>group by 参数值枚举1:1m  2:5m  3:30m  4:1h<br> 5:1d</p>
        :type GroupByType: int
        :param _IsNewData: <p>1: 查询智研<br>0: 走旧逻辑，已下线，勿使用</p>
        :type IsNewData: int
        :param _ExtFourth: <p>自定义4</p>
        :type ExtFourth: str
        :param _ExtFifth: <p>自定义5</p>
        :type ExtFifth: str
        :param _ExtSixth: <p>自定义6</p>
        :type ExtSixth: str
        :param _ExtSeventh: <p>自定义7</p>
        :type ExtSeventh: str
        :param _ExtEighth: <p>自定义8</p>
        :type ExtEighth: str
        :param _ExtNinth: <p>自定义9</p>
        :type ExtNinth: str
        :param _ExtTenth: <p>自定义10</p>
        :type ExtTenth: str
        :param _Granularity: <p>时间段</p>
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None
        self._GroupByType = None
        self._IsNewData = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""<p>开始时间</p>
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""<p>allcount：性能视图，day：14天数据，vp：性能，ckuv：uv，ckpv：pv，condition：条件列表，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""<p>结束时间</p>
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""<p>项目ID</p>
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""<p>自定义2</p>
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""<p>浏览器引擎</p>
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""<p>运营商</p>
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""<p>来源页面， 可多选，用 “,” 隔开的 String</p>
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""<p>日志等级</p>
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""<p>品牌</p>
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""<p>地区</p>
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""<p>版本</p>
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""<p>平台</p>
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""<p>自定义3</p>
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""<p>自定义1</p>
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""<p>网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知</p>
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""<p>机型</p>
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""<p>显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。</p>
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""<p>操作系统</p>
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""<p>浏览器</p>
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        r"""<p>环境</p>
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def GroupByType(self):
        r"""<p>group by 参数值枚举1:1m  2:5m  3:30m  4:1h<br> 5:1d</p>
        :rtype: int
        """
        return self._GroupByType

    @GroupByType.setter
    def GroupByType(self, GroupByType):
        self._GroupByType = GroupByType

    @property
    def IsNewData(self):
        r"""<p>1: 查询智研<br>0: 走旧逻辑，已下线，勿使用</p>
        :rtype: int
        """
        return self._IsNewData

    @IsNewData.setter
    def IsNewData(self, IsNewData):
        self._IsNewData = IsNewData

    @property
    def ExtFourth(self):
        r"""<p>自定义4</p>
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""<p>自定义5</p>
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""<p>自定义6</p>
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""<p>自定义7</p>
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""<p>自定义8</p>
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""<p>自定义9</p>
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""<p>自定义10</p>
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""<p>时间段</p>
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        self._GroupByType = params.get("GroupByType")
        self._IsNewData = params.get("IsNewData")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlStatisticsV2Response(AbstractModel):
    r"""DescribeDataPvUrlStatisticsV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: <p>返回值</p>
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataReportCountRequest(AbstractModel):
    r"""DescribeDataReportCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ReportType: 上报类型（custom，event，log，miniProgramData，performance，pv，speed，webvitals）
        :type ReportType: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ReportType = None
        self._InstanceID = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ReportType(self):
        r"""上报类型（custom，event，log，miniProgramData，performance，pv，speed，webvitals）
        :rtype: str
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ReportType = params.get("ReportType")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataReportCountResponse(AbstractModel):
    r"""DescribeDataReportCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataReportCountV2Request(AbstractModel):
    r"""DescribeDataReportCountV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ReportType: 上报类型（custom，event，log，miniProgramData，performance，pv，speed，webvitals）
        :type ReportType: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ReportType = None
        self._InstanceID = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ReportType(self):
        r"""上报类型（custom，event，log，miniProgramData，performance，pv，speed，webvitals）
        :rtype: str
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ReportType = params.get("ReportType")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataReportCountV2Response(AbstractModel):
    r"""DescribeDataReportCountV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataRequest(AbstractModel):
    r"""DescribeData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 查询字符串
        :type Query: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._Query = None
        self._ID = None

    @property
    def Query(self):
        r"""查询字符串
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    r"""DescribeData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回字符串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataSetUrlStatisticsRequest(AbstractModel):
    r"""DescribeDataSetUrlStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，data：小程序，component：小程序相关，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时/数据量口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Env: 环境
        :type Env: str
        :param _PackageType: 小程序包类型（tag 值）：用于过滤字段 type（请求参数名为 PackageType）；取值由上报数据决定，可通过 Type=condition（show tag values）获取可选值集合。
        :type PackageType: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None
        self._PackageType = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，data：小程序，component：小程序相关，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时/数据量口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def PackageType(self):
        r"""小程序包类型（tag 值）：用于过滤字段 type（请求参数名为 PackageType）；取值由上报数据决定，可通过 Type=condition（show tag values）获取可选值集合。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSetUrlStatisticsResponse(AbstractModel):
    r"""DescribeDataSetUrlStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataSetUrlStatisticsV2Request(AbstractModel):
    r"""DescribeDataSetUrlStatisticsV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，data：小程序，component：小程序相关，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算
        :type CostType: str
        :param _Env: 环境
        :type Env: str
        :param _PackageType: 获取package
        :type PackageType: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None
        self._PackageType = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，data：小程序，component：小程序相关，day：14天数据，nettype：网络/平台视图，performance：页面性能TOP视图，version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：ISP视图/地区视图/浏览器视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时计算
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def PackageType(self):
        r"""获取package
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._PackageType = params.get("PackageType")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSetUrlStatisticsV2Response(AbstractModel):
    r"""DescribeDataSetUrlStatisticsV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticProjectRequest(AbstractModel):
    r"""DescribeDataStaticProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Url: 来源
        :type Url: list of str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: list of str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticProjectResponse(AbstractModel):
    r"""DescribeDataStaticProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticProjectV2Request(AbstractModel):
    r"""DescribeDataStaticProjectV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算
        :type CostType: str
        :param _Url: 来源
        :type Url: list of str
        :param _Env: 环境
        :type Env: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""allcount：性能视图，day：14天数据，condition：条件列表，area：请求速度分布，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图/ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级（1表示白名单日志，2表示一般日志，4表示错误日志，8表示Promise 错误，16表示Ajax 请求异常，32表示JS 加载异常，64表示图片加载异常，128表示css 加载异常，256表示console.error，512表示音视频资源异常，1024表示retcode 异常，2048表示aegis report，4096表示PV日志，8192表示自定义事件，16384表示小程序 页面不存在，32768表示websocket错误，65536表示js bridge错误）
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型（1,2,3,4,5,100），1表示WIFI, 2表示2G, 3表示3G, 4表示4G, 5表示5G, 6表示6G, 100表示未知。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时计算
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: list of str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticProjectV2Response(AbstractModel):
    r"""DescribeDataStaticProjectV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticResourceRequest(AbstractModel):
    r"""DescribeDataStaticResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: top：资源top视图，count40x：40X视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""top：资源top视图，count40x：40X视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticResourceResponse(AbstractModel):
    r"""DescribeDataStaticResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticResourceV2Request(AbstractModel):
    r"""DescribeDataStaticResourceV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: top：资源top视图，count40x：40X视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""top：资源top视图，count40x：40X视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时计算方式
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticResourceV2Response(AbstractModel):
    r"""DescribeDataStaticResourceV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticUrlRequest(AbstractModel):
    r"""DescribeDataStaticUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: pagepv：性能视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""pagepv：性能视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticUrlResponse(AbstractModel):
    r"""DescribeDataStaticUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataStaticUrlV2Request(AbstractModel):
    r"""DescribeDataStaticUrlV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _Type: pagepv：性能视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等
        :type Type: str
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算方式
        :type CostType: str
        :param _Url: 来源
        :type Url: str
        :param _Env: 环境
        :type Env: str
        :param _ExtFourth: 自定义4
        :type ExtFourth: str
        :param _ExtFifth: 自定义5
        :type ExtFifth: str
        :param _ExtSixth: 自定义6
        :type ExtSixth: str
        :param _ExtSeventh: 自定义7
        :type ExtSeventh: str
        :param _ExtEighth: 自定义8
        :type ExtEighth: str
        :param _ExtNinth: 自定义9
        :type ExtNinth: str
        :param _ExtTenth: 自定义10
        :type ExtTenth: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._ExtFourth = None
        self._ExtFifth = None
        self._ExtSixth = None
        self._ExtSeventh = None
        self._ExtEighth = None
        self._ExtNinth = None
        self._ExtTenth = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        r"""pagepv：性能视图，nettype/version/platform/isp/region/device/browser/ext1/ext2/ext3/ret/status/from/url/env/：网络平台视图/Version视图/设备视图/ISP视图/地区视图/浏览器视图//ext1视图等
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时计算方式
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        r"""来源
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def ExtFourth(self):
        r"""自定义4
        :rtype: str
        """
        return self._ExtFourth

    @ExtFourth.setter
    def ExtFourth(self, ExtFourth):
        self._ExtFourth = ExtFourth

    @property
    def ExtFifth(self):
        r"""自定义5
        :rtype: str
        """
        return self._ExtFifth

    @ExtFifth.setter
    def ExtFifth(self, ExtFifth):
        self._ExtFifth = ExtFifth

    @property
    def ExtSixth(self):
        r"""自定义6
        :rtype: str
        """
        return self._ExtSixth

    @ExtSixth.setter
    def ExtSixth(self, ExtSixth):
        self._ExtSixth = ExtSixth

    @property
    def ExtSeventh(self):
        r"""自定义7
        :rtype: str
        """
        return self._ExtSeventh

    @ExtSeventh.setter
    def ExtSeventh(self, ExtSeventh):
        self._ExtSeventh = ExtSeventh

    @property
    def ExtEighth(self):
        r"""自定义8
        :rtype: str
        """
        return self._ExtEighth

    @ExtEighth.setter
    def ExtEighth(self, ExtEighth):
        self._ExtEighth = ExtEighth

    @property
    def ExtNinth(self):
        r"""自定义9
        :rtype: str
        """
        return self._ExtNinth

    @ExtNinth.setter
    def ExtNinth(self, ExtNinth):
        self._ExtNinth = ExtNinth

    @property
    def ExtTenth(self):
        r"""自定义10
        :rtype: str
        """
        return self._ExtTenth

    @ExtTenth.setter
    def ExtTenth(self, ExtTenth):
        self._ExtTenth = ExtTenth

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._ExtFourth = params.get("ExtFourth")
        self._ExtFifth = params.get("ExtFifth")
        self._ExtSixth = params.get("ExtSixth")
        self._ExtSeventh = params.get("ExtSeventh")
        self._ExtEighth = params.get("ExtEighth")
        self._ExtNinth = params.get("ExtNinth")
        self._ExtTenth = params.get("ExtTenth")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticUrlV2Response(AbstractModel):
    r"""DescribeDataStaticUrlV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataWebVitalsPageRequest(AbstractModel):
    r"""DescribeDataWebVitalsPage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 查询维度：from=按页面来源(from)聚合输出；其他值/空值=输出整体汇总。
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Type: 按页面来源分组（group by from），返回每个页面的 LCP/FID/CLS/FCP
        :type Type: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。 
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: Web Vitals 口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。 
        :type CostType: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Type = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""查询维度：from=按页面来源(from)聚合输出；其他值/空值=输出整体汇总。
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Type(self):
        r"""按页面来源分组（group by from），返回每个页面的 LCP/FID/CLS/FCP
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型(tag 值):用于过滤/聚合字段 netType；枚举值：1(WiFi)、2(2G)、3(3G)、4(4G)、5(5G)、6(6G)、100(未知网络)。 
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""Web Vitals 口径："50"/"75"/"90"/"95"/"99"/"99.5" 分别表示 TP50/TP75/TP90/TP95/TP99/TP99.5（percentile2）；"avg" 表示均值（avg）。 
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Type = params.get("Type")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataWebVitalsPageResponse(AbstractModel):
    r"""DescribeDataWebVitalsPage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeDataWebVitalsPageV2Request(AbstractModel):
    r"""DescribeDataWebVitalsPageV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ID: 项目ID
        :type ID: int
        :param _ExtSecond: 自定义2
        :type ExtSecond: str
        :param _Engine: 浏览器引擎
        :type Engine: str
        :param _Isp: 运营商
        :type Isp: str
        :param _From: 来源页面
        :type From: str
        :param _Level: 日志等级
        :type Level: str
        :param _Type: 类型暂无
        :type Type: str
        :param _Brand: 品牌
        :type Brand: str
        :param _Area: 地区
        :type Area: str
        :param _VersionNum: 版本
        :type VersionNum: str
        :param _Platform: 平台
        :type Platform: str
        :param _ExtThird: 自定义3
        :type ExtThird: str
        :param _ExtFirst: 自定义1
        :type ExtFirst: str
        :param _NetType: 网络类型
        :type NetType: str
        :param _Device: 机型
        :type Device: str
        :param _IsAbroad: 显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :type IsAbroad: str
        :param _Os: 操作系统
        :type Os: str
        :param _Browser: 浏览器
        :type Browser: str
        :param _CostType: 耗时计算
        :type CostType: str
        :param _Env: 环境
        :type Env: str
        :param _Granularity: 时间段
        :type Granularity: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Type = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None
        self._Granularity = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        r"""自定义2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        r"""浏览器引擎
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        r"""运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        r"""来源页面
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        r"""日志等级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Type(self):
        r"""类型暂无
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Brand(self):
        r"""品牌
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        r"""地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        r"""版本
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        r"""平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        r"""自定义3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        r"""自定义1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        r"""网络类型
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        r"""机型
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        r"""显示是否海外,1表示海外，0表示非海外；默认值为空，查询所有。
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        r"""操作系统
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        r"""浏览器
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        r"""耗时计算
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Granularity(self):
        r"""时间段
        :rtype: str
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Type = params.get("Type")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataWebVitalsPageV2Response(AbstractModel):
    r"""DescribeDataWebVitalsPageV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回值
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回值
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeErrorRequest(AbstractModel):
    r"""DescribeError请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Date: 日期
        :type Date: str
        :param _ID: 项目ID
        :type ID: int
        """
        self._Date = None
        self._ID = None

    @property
    def Date(self):
        r"""日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorResponse(AbstractModel):
    r"""DescribeError返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 内容
        :type Content: str
        :param _ID: 项目ID
        :type ID: int
        :param _CreateTime: 时间
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._ID = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Content(self):
        r"""内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreateTime(self):
        r"""时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
        self._Content = params.get("Content")
        self._ID = params.get("ID")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class DescribeExceptionDetailRequest(AbstractModel):
    r"""DescribeExceptionDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ClientIdentify: <p>消息唯一标识</p>
        :type ClientIdentify: str
        :param _ClusterStackType: <p>集群堆栈类型</p>
        :type ClusterStackType: int
        :param _Feature: <p>特征</p>
        :type Feature: str
        :param _IssueType: <p>问题类型</p>
        :type IssueType: int
        :param _StartEventTime: <p>事件开始时间</p>
        :type StartEventTime: int
        :param _EndEventTime: <p>事件结束时间</p>
        :type EndEventTime: int
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ClientIdentify = None
        self._ClusterStackType = None
        self._Feature = None
        self._IssueType = None
        self._StartEventTime = None
        self._EndEventTime = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ClientIdentify(self):
        r"""<p>消息唯一标识</p>
        :rtype: str
        """
        return self._ClientIdentify

    @ClientIdentify.setter
    def ClientIdentify(self, ClientIdentify):
        self._ClientIdentify = ClientIdentify

    @property
    def ClusterStackType(self):
        r"""<p>集群堆栈类型</p>
        :rtype: int
        """
        return self._ClusterStackType

    @ClusterStackType.setter
    def ClusterStackType(self, ClusterStackType):
        self._ClusterStackType = ClusterStackType

    @property
    def Feature(self):
        r"""<p>特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

    @property
    def IssueType(self):
        r"""<p>问题类型</p>
        :rtype: int
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def StartEventTime(self):
        r"""<p>事件开始时间</p>
        :rtype: int
        """
        return self._StartEventTime

    @StartEventTime.setter
    def StartEventTime(self, StartEventTime):
        self._StartEventTime = StartEventTime

    @property
    def EndEventTime(self):
        r"""<p>事件结束时间</p>
        :rtype: int
        """
        return self._EndEventTime

    @EndEventTime.setter
    def EndEventTime(self, EndEventTime):
        self._EndEventTime = EndEventTime

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ClientIdentify = params.get("ClientIdentify")
        self._ClusterStackType = params.get("ClusterStackType")
        self._Feature = params.get("Feature")
        self._IssueType = params.get("IssueType")
        self._StartEventTime = params.get("StartEventTime")
        self._EndEventTime = params.get("EndEventTime")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExceptionDetailResponse(AbstractModel):
    r"""DescribeExceptionDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeExceptionReportListRequest(AbstractModel):
    r"""DescribeExceptionReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 form_list 的值</p>
        :type ParamToken: str
        :param _IssueType: <p>问题类型</p>
        :type IssueType: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序方式</p>
        :type SortType: str
        :param _Feature: <p>特征</p>
        :type Feature: str
        :param _PageSize: <p>每页数目</p>
        :type PageSize: int
        :param _PageNumber: <p>页码</p>
        :type PageNumber: int
        :param _ExtraData: <p>拓展字段</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._FormListString = None
        self._ParamToken = None
        self._IssueType = None
        self._SortField = None
        self._SortType = None
        self._Feature = None
        self._PageSize = None
        self._PageNumber = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 form_list 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def IssueType(self):
        r"""<p>问题类型</p>
        :rtype: int
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序方式</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Feature(self):
        r"""<p>特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

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
    def PageNumber(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def ExtraData(self):
        r"""<p>拓展字段</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FormListString = params.get("FormListString")
        self._ParamToken = params.get("ParamToken")
        self._IssueType = params.get("IssueType")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._Feature = params.get("Feature")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExceptionReportListResponse(AbstractModel):
    r"""DescribeExceptionReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeFOOMMallocProblemDetailRequest(AbstractModel):
    r"""DescribeFOOMMallocProblemDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ClientIdentify: <p>消息唯一标识</p>
        :type ClientIdentify: str
        :param _Feature: <p>特征</p>
        :type Feature: str
        :param _StartEventTime: <p>事件开始时间</p>
        :type StartEventTime: int
        :param _EndEventTime: <p>事件结束时间</p>
        :type EndEventTime: int
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ClientIdentify = None
        self._Feature = None
        self._StartEventTime = None
        self._EndEventTime = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ClientIdentify(self):
        r"""<p>消息唯一标识</p>
        :rtype: str
        """
        return self._ClientIdentify

    @ClientIdentify.setter
    def ClientIdentify(self, ClientIdentify):
        self._ClientIdentify = ClientIdentify

    @property
    def Feature(self):
        r"""<p>特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

    @property
    def StartEventTime(self):
        r"""<p>事件开始时间</p>
        :rtype: int
        """
        return self._StartEventTime

    @StartEventTime.setter
    def StartEventTime(self, StartEventTime):
        self._StartEventTime = StartEventTime

    @property
    def EndEventTime(self):
        r"""<p>事件结束时间</p>
        :rtype: int
        """
        return self._EndEventTime

    @EndEventTime.setter
    def EndEventTime(self, EndEventTime):
        self._EndEventTime = EndEventTime

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ClientIdentify = params.get("ClientIdentify")
        self._Feature = params.get("Feature")
        self._StartEventTime = params.get("StartEventTime")
        self._EndEventTime = params.get("EndEventTime")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFOOMMallocProblemDetailResponse(AbstractModel):
    r"""DescribeFOOMMallocProblemDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeFOOMMallocProblemListRequest(AbstractModel):
    r"""DescribeFOOMMallocProblemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页展示最大数量</p>
        :type PageSize: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序类型</p>
        :type SortType: str
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ParamToken = None
        self._FormListString = None
        self._PageNumber = None
        self._PageSize = None
        self._SortField = None
        self._SortType = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页展示最大数量</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序类型</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParamToken = params.get("ParamToken")
        self._FormListString = params.get("FormListString")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFOOMMallocProblemListResponse(AbstractModel):
    r"""DescribeFOOMMallocProblemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Message: <p>消息</p>
        :type Message: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Message = None
        self._Code = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Data = params.get("Data")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class DescribeFOOMMallocReportListRequest(AbstractModel):
    r"""DescribeFOOMMallocReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _Feature: <p>特征</p>
        :type Feature: str
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页展示最大数量</p>
        :type PageSize: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序类型</p>
        :type SortType: str
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._FormListString = None
        self._ParamToken = None
        self._Feature = None
        self._PageNumber = None
        self._PageSize = None
        self._SortField = None
        self._SortType = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def Feature(self):
        r"""<p>特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页展示最大数量</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序类型</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FormListString = params.get("FormListString")
        self._ParamToken = params.get("ParamToken")
        self._Feature = params.get("Feature")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFOOMMallocReportListResponse(AbstractModel):
    r"""DescribeFOOMMallocReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Message: <p>消息</p>
        :type Message: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Message = None
        self._Code = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Data = params.get("Data")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class DescribeFOOMProblemDetailRequest(AbstractModel):
    r"""DescribeFOOMProblemDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ClientIdentify: <p>消息唯一标识</p>
        :type ClientIdentify: str
        :param _Feature: <p>特征</p>
        :type Feature: str
        :param _StartEventTime: <p>事件开始时间</p>
        :type StartEventTime: int
        :param _EndEventTime: <p>事件结束时间</p>
        :type EndEventTime: int
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ClientIdentify = None
        self._Feature = None
        self._StartEventTime = None
        self._EndEventTime = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ClientIdentify(self):
        r"""<p>消息唯一标识</p>
        :rtype: str
        """
        return self._ClientIdentify

    @ClientIdentify.setter
    def ClientIdentify(self, ClientIdentify):
        self._ClientIdentify = ClientIdentify

    @property
    def Feature(self):
        r"""<p>特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

    @property
    def StartEventTime(self):
        r"""<p>事件开始时间</p>
        :rtype: int
        """
        return self._StartEventTime

    @StartEventTime.setter
    def StartEventTime(self, StartEventTime):
        self._StartEventTime = StartEventTime

    @property
    def EndEventTime(self):
        r"""<p>事件结束时间</p>
        :rtype: int
        """
        return self._EndEventTime

    @EndEventTime.setter
    def EndEventTime(self, EndEventTime):
        self._EndEventTime = EndEventTime

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ClientIdentify = params.get("ClientIdentify")
        self._Feature = params.get("Feature")
        self._StartEventTime = params.get("StartEventTime")
        self._EndEventTime = params.get("EndEventTime")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFOOMProblemDetailResponse(AbstractModel):
    r"""DescribeFOOMProblemDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeFOOMProblemListRequest(AbstractModel):
    r"""DescribeFOOMProblemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页展示最大数量</p>
        :type PageSize: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序类型</p>
        :type SortType: str
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ParamToken = None
        self._FormListString = None
        self._PageNumber = None
        self._PageSize = None
        self._SortField = None
        self._SortType = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页展示最大数量</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序类型</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParamToken = params.get("ParamToken")
        self._FormListString = params.get("FormListString")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFOOMProblemListResponse(AbstractModel):
    r"""DescribeFOOMProblemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Message: <p>消息</p>
        :type Message: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Message = None
        self._Code = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Data = params.get("Data")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class DescribeFOOMReportListRequest(AbstractModel):
    r"""DescribeFOOMReportList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _Feature: <p>特征</p>
        :type Feature: str
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页展示最大数量</p>
        :type PageSize: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序类型</p>
        :type SortType: str
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._FormListString = None
        self._ParamToken = None
        self._Feature = None
        self._PageNumber = None
        self._PageSize = None
        self._SortField = None
        self._SortType = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def Feature(self):
        r"""<p>特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页展示最大数量</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序类型</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FormListString = params.get("FormListString")
        self._ParamToken = params.get("ParamToken")
        self._Feature = params.get("Feature")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFOOMReportListResponse(AbstractModel):
    r"""DescribeFOOMReportList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Message: <p>消息</p>
        :type Message: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Message = None
        self._Code = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Data = params.get("Data")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class DescribeIssuesDistributionRequest(AbstractModel):
    r"""DescribeIssuesDistribution请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _DimType: <p>分布维度是自定义维度时，填‘user_custom’</p>
        :type DimType: str
        :param _Dimension: <p>维度，e.g. os_version, app_version, model等</p>
        :type Dimension: str
        :param _Intervals: <p>数字类型字段的区间范围</p>
        :type Intervals: list of int
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 form_list 的值</p>
        :type ParamToken: str
        :param _IssueId: <p>问题Id</p>
        :type IssueId: str
        :param _IssueType: <p>问题类型</p>
        :type IssueType: int
        :param _ParamLimit: <p>限制返回的个数，默认返回所有值</p>
        :type ParamLimit: int
        :param _MapKey: <p>键</p>
        :type MapKey: str
        :param _MapName: <p>名称</p>
        :type MapName: str
        :param _MetricType: <p>指标类型</p>
        :type MetricType: int
        :param _PageSize: <p>每页数目</p>
        :type PageSize: int
        :param _PageNumber: <p>页码</p>
        :type PageNumber: int
        :param _UserCustomKey: <p>用户自定义维度key</p>
        :type UserCustomKey: str
        :param _ExtraData: <p>拓展字段</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._FormListString = None
        self._DimType = None
        self._Dimension = None
        self._Intervals = None
        self._ParamToken = None
        self._IssueId = None
        self._IssueType = None
        self._ParamLimit = None
        self._MapKey = None
        self._MapName = None
        self._MetricType = None
        self._PageSize = None
        self._PageNumber = None
        self._UserCustomKey = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def DimType(self):
        r"""<p>分布维度是自定义维度时，填‘user_custom’</p>
        :rtype: str
        """
        return self._DimType

    @DimType.setter
    def DimType(self, DimType):
        self._DimType = DimType

    @property
    def Dimension(self):
        r"""<p>维度，e.g. os_version, app_version, model等</p>
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def Intervals(self):
        r"""<p>数字类型字段的区间范围</p>
        :rtype: list of int
        """
        return self._Intervals

    @Intervals.setter
    def Intervals(self, Intervals):
        self._Intervals = Intervals

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 form_list 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def IssueId(self):
        r"""<p>问题Id</p>
        :rtype: str
        """
        return self._IssueId

    @IssueId.setter
    def IssueId(self, IssueId):
        self._IssueId = IssueId

    @property
    def IssueType(self):
        r"""<p>问题类型</p>
        :rtype: int
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def ParamLimit(self):
        r"""<p>限制返回的个数，默认返回所有值</p>
        :rtype: int
        """
        return self._ParamLimit

    @ParamLimit.setter
    def ParamLimit(self, ParamLimit):
        self._ParamLimit = ParamLimit

    @property
    def MapKey(self):
        r"""<p>键</p>
        :rtype: str
        """
        return self._MapKey

    @MapKey.setter
    def MapKey(self, MapKey):
        self._MapKey = MapKey

    @property
    def MapName(self):
        r"""<p>名称</p>
        :rtype: str
        """
        return self._MapName

    @MapName.setter
    def MapName(self, MapName):
        self._MapName = MapName

    @property
    def MetricType(self):
        r"""<p>指标类型</p>
        :rtype: int
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

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
    def PageNumber(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def UserCustomKey(self):
        r"""<p>用户自定义维度key</p>
        :rtype: str
        """
        return self._UserCustomKey

    @UserCustomKey.setter
    def UserCustomKey(self, UserCustomKey):
        self._UserCustomKey = UserCustomKey

    @property
    def ExtraData(self):
        r"""<p>拓展字段</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FormListString = params.get("FormListString")
        self._DimType = params.get("DimType")
        self._Dimension = params.get("Dimension")
        self._Intervals = params.get("Intervals")
        self._ParamToken = params.get("ParamToken")
        self._IssueId = params.get("IssueId")
        self._IssueType = params.get("IssueType")
        self._ParamLimit = params.get("ParamLimit")
        self._MapKey = params.get("MapKey")
        self._MapName = params.get("MapName")
        self._MetricType = params.get("MetricType")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._UserCustomKey = params.get("UserCustomKey")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIssuesDistributionResponse(AbstractModel):
    r"""DescribeIssuesDistribution返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeIssuesListRequest(AbstractModel):
    r"""DescribeIssuesList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _FormList: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormList: str
        :param _FormListA: <p>接口调试专用，对比模式下条件A，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListA: str
        :param _FormListB: <p>接口调试专用，对比模式下条件B，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListB: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 form_list 的值</p>
        :type ParamToken: str
        :param _IssueType: <p>问题类型</p>
        :type IssueType: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序方式</p>
        :type SortType: str
        :param _PageSize: <p>每页数目</p>
        :type PageSize: int
        :param _PageNumber: <p>页码</p>
        :type PageNumber: int
        :param _SortABRatio: <p>问题对比列表模式下，用于标识是按照sort_field字段的A值排序还是B值还是ratio值</p>
        :type SortABRatio: str
        :param _Compare: <p>模式：false:问题列表模式，true:对比列表模式</p>
        :type Compare: bool
        :param _CompareStatus: <p>对比状态 0:所有 1:新增 2：遗留 3:已解决</p>
        :type CompareStatus: int
        :param _ExtraData: <p>拓展字段</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._FormList = None
        self._FormListA = None
        self._FormListB = None
        self._ParamToken = None
        self._IssueType = None
        self._SortField = None
        self._SortType = None
        self._PageSize = None
        self._PageNumber = None
        self._SortABRatio = None
        self._Compare = None
        self._CompareStatus = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FormList(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormList

    @FormList.setter
    def FormList(self, FormList):
        self._FormList = FormList

    @property
    def FormListA(self):
        r"""<p>接口调试专用，对比模式下条件A，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListA

    @FormListA.setter
    def FormListA(self, FormListA):
        self._FormListA = FormListA

    @property
    def FormListB(self):
        r"""<p>接口调试专用，对比模式下条件B，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListB

    @FormListB.setter
    def FormListB(self, FormListB):
        self._FormListB = FormListB

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 form_list 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def IssueType(self):
        r"""<p>问题类型</p>
        :rtype: int
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序方式</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

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
    def PageNumber(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def SortABRatio(self):
        r"""<p>问题对比列表模式下，用于标识是按照sort_field字段的A值排序还是B值还是ratio值</p>
        :rtype: str
        """
        return self._SortABRatio

    @SortABRatio.setter
    def SortABRatio(self, SortABRatio):
        self._SortABRatio = SortABRatio

    @property
    def Compare(self):
        r"""<p>模式：false:问题列表模式，true:对比列表模式</p>
        :rtype: bool
        """
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def CompareStatus(self):
        r"""<p>对比状态 0:所有 1:新增 2：遗留 3:已解决</p>
        :rtype: int
        """
        return self._CompareStatus

    @CompareStatus.setter
    def CompareStatus(self, CompareStatus):
        self._CompareStatus = CompareStatus

    @property
    def ExtraData(self):
        r"""<p>拓展字段</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FormList = params.get("FormList")
        self._FormListA = params.get("FormListA")
        self._FormListB = params.get("FormListB")
        self._ParamToken = params.get("ParamToken")
        self._IssueType = params.get("IssueType")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._SortABRatio = params.get("SortABRatio")
        self._Compare = params.get("Compare")
        self._CompareStatus = params.get("CompareStatus")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIssuesListResponse(AbstractModel):
    r"""DescribeIssuesList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeIssuesStatisticsTrendRequest(AbstractModel):
    r"""DescribeIssuesStatisticsTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 产品Id
        :type ProductId: str
        :param _ParamToken: 提供给前端使用，当填写本字段时，会覆盖 form_list 的值
        :type ParamToken: str
        :param _FormList: 接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息
        :type FormList: str
        :param _IssueId: 问题Id
        :type IssueId: str
        :param _IssueType: 问题类型
        :type IssueType: int
        :param _TimeWindow: 时间窗口
        :type TimeWindow: int
        :param _TotalSize: 累计值
        :type TotalSize: bool
        :param _Stat: 无
        :type Stat: int
        :param _MetricType: 指标类型
        :type MetricType: int
        :param _ExtraData: 拓展字段
        :type ExtraData: str
        :param _RequestHeader: 请求头
        :type RequestHeader: str
        :param _TrendStat: 无
        :type TrendStat: int
        """
        self._ProductId = None
        self._ParamToken = None
        self._FormList = None
        self._IssueId = None
        self._IssueType = None
        self._TimeWindow = None
        self._TotalSize = None
        self._Stat = None
        self._MetricType = None
        self._ExtraData = None
        self._RequestHeader = None
        self._TrendStat = None

    @property
    def ProductId(self):
        r"""产品Id
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParamToken(self):
        r"""提供给前端使用，当填写本字段时，会覆盖 form_list 的值
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def FormList(self):
        r"""接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息
        :rtype: str
        """
        return self._FormList

    @FormList.setter
    def FormList(self, FormList):
        self._FormList = FormList

    @property
    def IssueId(self):
        r"""问题Id
        :rtype: str
        """
        return self._IssueId

    @IssueId.setter
    def IssueId(self, IssueId):
        self._IssueId = IssueId

    @property
    def IssueType(self):
        r"""问题类型
        :rtype: int
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def TimeWindow(self):
        r"""时间窗口
        :rtype: int
        """
        return self._TimeWindow

    @TimeWindow.setter
    def TimeWindow(self, TimeWindow):
        self._TimeWindow = TimeWindow

    @property
    def TotalSize(self):
        r"""累计值
        :rtype: bool
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def Stat(self):
        r"""无
        :rtype: int
        """
        return self._Stat

    @Stat.setter
    def Stat(self, Stat):
        self._Stat = Stat

    @property
    def MetricType(self):
        r"""指标类型
        :rtype: int
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def ExtraData(self):
        r"""拓展字段
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""请求头
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def TrendStat(self):
        r"""无
        :rtype: int
        """
        return self._TrendStat

    @TrendStat.setter
    def TrendStat(self, TrendStat):
        self._TrendStat = TrendStat


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParamToken = params.get("ParamToken")
        self._FormList = params.get("FormList")
        self._IssueId = params.get("IssueId")
        self._IssueType = params.get("IssueType")
        self._TimeWindow = params.get("TimeWindow")
        self._TotalSize = params.get("TotalSize")
        self._Stat = params.get("Stat")
        self._MetricType = params.get("MetricType")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        self._TrendStat = params.get("TrendStat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIssuesStatisticsTrendResponse(AbstractModel):
    r"""DescribeIssuesStatisticsTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回值
        :type Data: str
        :param _Code: 状态码
        :type Code: int
        :param _Message: 消息
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""返回值
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""状态码
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""消息
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeLagANRProblemAccountDetailRequest(AbstractModel):
    r"""DescribeLagANRProblemAccountDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ClientIdentify: <p>消息唯一标识</p>
        :type ClientIdentify: str
        :param _Feature: <p>特征</p>
        :type Feature: str
        :param _StartEventTime: <p>事件开始时间</p>
        :type StartEventTime: int
        :param _EndEventTime: <p>事件结束时间</p>
        :type EndEventTime: int
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ClientIdentify = None
        self._Feature = None
        self._StartEventTime = None
        self._EndEventTime = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ClientIdentify(self):
        r"""<p>消息唯一标识</p>
        :rtype: str
        """
        return self._ClientIdentify

    @ClientIdentify.setter
    def ClientIdentify(self, ClientIdentify):
        self._ClientIdentify = ClientIdentify

    @property
    def Feature(self):
        r"""<p>特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

    @property
    def StartEventTime(self):
        r"""<p>事件开始时间</p>
        :rtype: int
        """
        return self._StartEventTime

    @StartEventTime.setter
    def StartEventTime(self, StartEventTime):
        self._StartEventTime = StartEventTime

    @property
    def EndEventTime(self):
        r"""<p>事件结束时间</p>
        :rtype: int
        """
        return self._EndEventTime

    @EndEventTime.setter
    def EndEventTime(self, EndEventTime):
        self._EndEventTime = EndEventTime

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ClientIdentify = params.get("ClientIdentify")
        self._Feature = params.get("Feature")
        self._StartEventTime = params.get("StartEventTime")
        self._EndEventTime = params.get("EndEventTime")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLagANRProblemAccountDetailResponse(AbstractModel):
    r"""DescribeLagANRProblemAccountDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeLagANRProblemFeatureAccountsRequest(AbstractModel):
    r"""DescribeLagANRProblemFeatureAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _Feature: <p>问题特征</p>
        :type Feature: str
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序类型</p>
        :type SortType: str
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页展示最大数量</p>
        :type PageSize: int
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._FormListString = None
        self._ParamToken = None
        self._Feature = None
        self._SortField = None
        self._SortType = None
        self._PageNumber = None
        self._PageSize = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def Feature(self):
        r"""<p>问题特征</p>
        :rtype: str
        """
        return self._Feature

    @Feature.setter
    def Feature(self, Feature):
        self._Feature = Feature

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序类型</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页展示最大数量</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._FormListString = params.get("FormListString")
        self._ParamToken = params.get("ParamToken")
        self._Feature = params.get("Feature")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLagANRProblemFeatureAccountsResponse(AbstractModel):
    r"""DescribeLagANRProblemFeatureAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Message: <p>消息</p>
        :type Message: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Message = None
        self._Code = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Data = params.get("Data")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class DescribeLagANRProblemListRequest(AbstractModel):
    r"""DescribeLagANRProblemList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _ParamToken: <p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :type ParamToken: str
        :param _FormListString: <p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :type FormListString: str
        :param _PageNumber: <p>当前页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页展示最大数量</p>
        :type PageSize: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序类型</p>
        :type SortType: str
        :param _ExtraData: <p>拓展数据</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._ParamToken = None
        self._FormListString = None
        self._PageNumber = None
        self._PageSize = None
        self._SortField = None
        self._SortType = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ParamToken(self):
        r"""<p>提供给前端使用，当填写本字段时，会覆盖 formlist 的值</p>
        :rtype: str
        """
        return self._ParamToken

    @ParamToken.setter
    def ParamToken(self, ParamToken):
        self._ParamToken = ParamToken

    @property
    def FormListString(self):
        r"""<p>接口调试专用，当 token 为空时，以这里的 value 作为筛选表单信息</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def PageNumber(self):
        r"""<p>当前页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页展示最大数量</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序类型</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def ExtraData(self):
        r"""<p>拓展数据</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._ParamToken = params.get("ParamToken")
        self._FormListString = params.get("FormListString")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLagANRProblemListResponse(AbstractModel):
    r"""DescribeLagANRProblemList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Message: <p>消息</p>
        :type Message: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Message = None
        self._Code = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

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
        self._Data = params.get("Data")
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        self._RequestId = params.get("RequestId")


class DescribeProjectLimitsRequest(AbstractModel):
    r"""DescribeProjectLimits请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: 项目ID
        :type ProjectID: int
        """
        self._ProjectID = None

    @property
    def ProjectID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectLimitsResponse(AbstractModel):
    r"""DescribeProjectLimits返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectLimitSet: 上报率数组列表
        :type ProjectLimitSet: list of ProjectLimit
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectLimitSet = None
        self._RequestId = None

    @property
    def ProjectLimitSet(self):
        r"""上报率数组列表
        :rtype: list of ProjectLimit
        """
        return self._ProjectLimitSet

    @ProjectLimitSet.setter
    def ProjectLimitSet(self, ProjectLimitSet):
        self._ProjectLimitSet = ProjectLimitSet

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
        if params.get("ProjectLimitSet") is not None:
            self._ProjectLimitSet = []
            for item in params.get("ProjectLimitSet"):
                obj = ProjectLimit()
                obj._deserialize(item)
                self._ProjectLimitSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    r"""DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页每页数目，整型
        :type Limit: int
        :param _Offset: 分页页码，整型
        :type Offset: int
        :param _Filters: 过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :type Filters: list of Filter
        :param _IsDemo: 该参数已废弃，demo模式请在Filters内注明
        :type IsDemo: int
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._IsDemo = None

    @property
    def Limit(self):
        r"""分页每页数目，整型
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页页码，整型
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def IsDemo(self):
        warnings.warn("parameter `IsDemo` is deprecated", DeprecationWarning) 

        r"""该参数已废弃，demo模式请在Filters内注明
        :rtype: int
        """
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        warnings.warn("parameter `IsDemo` is deprecated", DeprecationWarning) 

        self._IsDemo = IsDemo


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    r"""DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 列表总数
        :type TotalCount: int
        :param _ProjectSet: 项目列表
        :type ProjectSet: list of RumProject
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProjectSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""列表总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProjectSet(self):
        r"""项目列表
        :rtype: list of RumProject
        """
        return self._ProjectSet

    @ProjectSet.setter
    def ProjectSet(self, ProjectSet):
        self._ProjectSet = ProjectSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("ProjectSet") is not None:
            self._ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = RumProject()
                obj._deserialize(item)
                self._ProjectSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePvListRequest(AbstractModel):
    r"""DescribePvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: ID
        :type ProjectId: int
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Dimension: 对PV指标的查询维度。获取day：d，   获取min则不填。
        :type Dimension: str
        """
        self._ProjectId = None
        self._EndTime = None
        self._StartTime = None
        self._Dimension = None

    @property
    def ProjectId(self):
        r"""ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Dimension(self):
        r"""对PV指标的查询维度。获取day：d，   获取min则不填。
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePvListResponse(AbstractModel):
    r"""DescribePvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectPvSet: pv列表
        :type ProjectPvSet: list of RumPvInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectPvSet = None
        self._RequestId = None

    @property
    def ProjectPvSet(self):
        r"""pv列表
        :rtype: list of RumPvInfo
        """
        return self._ProjectPvSet

    @ProjectPvSet.setter
    def ProjectPvSet(self, ProjectPvSet):
        self._ProjectPvSet = ProjectPvSet

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
        if params.get("ProjectPvSet") is not None:
            self._ProjectPvSet = []
            for item in params.get("ProjectPvSet"):
                obj = RumPvInfo()
                obj._deserialize(item)
                self._ProjectPvSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReleaseFileSignRequest(AbstractModel):
    r"""DescribeReleaseFileSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Timeout: 超时时间，不填默认是 5 分钟
        :type Timeout: int
        :param _FileType: bucket类型，不填默认1:web，2:app
        :type FileType: int
        :param _Site: 获取临时签名的bucket是境内还是境外（1表示境外，其它表示境内）
        :type Site: int
        :param _ID: ProjectID
        :type ID: int
        """
        self._Timeout = None
        self._FileType = None
        self._Site = None
        self._ID = None

    @property
    def Timeout(self):
        r"""超时时间，不填默认是 5 分钟
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def FileType(self):
        r"""bucket类型，不填默认1:web，2:app
        :rtype: int
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def Site(self):
        r"""获取临时签名的bucket是境内还是境外（1表示境外，其它表示境内）
        :rtype: int
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def ID(self):
        r"""ProjectID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Timeout = params.get("Timeout")
        self._FileType = params.get("FileType")
        self._Site = params.get("Site")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFileSignResponse(AbstractModel):
    r"""DescribeReleaseFileSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretKey: 临时密钥key
        :type SecretKey: str
        :param _SecretID: 临时密钥 id
        :type SecretID: str
        :param _SessionToken: 临时密钥临时 token
        :type SessionToken: str
        :param _StartTime: 开始时间戳
        :type StartTime: int
        :param _ExpiredTime: 过期时间戳
        :type ExpiredTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretKey = None
        self._SecretID = None
        self._SessionToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def SecretKey(self):
        r"""临时密钥key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SecretID(self):
        r"""临时密钥 id
        :rtype: str
        """
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def SessionToken(self):
        r"""临时密钥临时 token
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def StartTime(self):
        r"""开始时间戳
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        r"""过期时间戳
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

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
        self._SecretKey = params.get("SecretKey")
        self._SecretID = params.get("SecretID")
        self._SessionToken = params.get("SessionToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class DescribeReleaseFilesRequest(AbstractModel):
    r"""DescribeReleaseFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: <p>项目 id</p>
        :type ProjectID: int
        :param _FileVersion: <p>文件版本</p>
        :type FileVersion: str
        :param _FileName: <p>查询过滤条件（根据sourcemap的文件名模糊匹配）</p>
        :type FileName: str
        :param _IgnoreDefaultTimeRange: <p>false/不传=保留「最近 3 个月」约束（旧行为）；true=绕过时间窗口</p>
        :type IgnoreDefaultTimeRange: bool
        """
        self._ProjectID = None
        self._FileVersion = None
        self._FileName = None
        self._IgnoreDefaultTimeRange = None

    @property
    def ProjectID(self):
        r"""<p>项目 id</p>
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def FileVersion(self):
        r"""<p>文件版本</p>
        :rtype: str
        """
        return self._FileVersion

    @FileVersion.setter
    def FileVersion(self, FileVersion):
        self._FileVersion = FileVersion

    @property
    def FileName(self):
        r"""<p>查询过滤条件（根据sourcemap的文件名模糊匹配）</p>
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def IgnoreDefaultTimeRange(self):
        r"""<p>false/不传=保留「最近 3 个月」约束（旧行为）；true=绕过时间窗口</p>
        :rtype: bool
        """
        return self._IgnoreDefaultTimeRange

    @IgnoreDefaultTimeRange.setter
    def IgnoreDefaultTimeRange(self, IgnoreDefaultTimeRange):
        self._IgnoreDefaultTimeRange = IgnoreDefaultTimeRange


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._FileVersion = params.get("FileVersion")
        self._FileName = params.get("FileName")
        self._IgnoreDefaultTimeRange = params.get("IgnoreDefaultTimeRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFilesResponse(AbstractModel):
    r"""DescribeReleaseFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Files: <p>文件信息列表</p>
        :type Files: list of ReleaseFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Files = None
        self._RequestId = None

    @property
    def Files(self):
        r"""<p>文件信息列表</p>
        :rtype: list of ReleaseFile
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

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
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self._Files.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRumGroupLogRequest(AbstractModel):
    r"""DescribeRumGroupLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 排序方式  desc  asc（必填）
        :type OrderBy: str
        :param _StartTime: 开始时间（必填）
        :type StartTime: str
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Page: 页数，第几页
        :type Page: int
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        :param _GroupField: 聚合字段
        :type GroupField: str
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Page = None
        self._Query = None
        self._EndTime = None
        self._ID = None
        self._GroupField = None

    @property
    def OrderBy(self):
        r"""排序方式  desc  asc（必填）
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        r"""开始时间（必填）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        r"""单次查询返回的原始日志条数，最大值为100（必填）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        r"""页数，第几页
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Query(self):
        r"""查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        r"""结束时间（必填）
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def GroupField(self):
        r"""聚合字段
        :rtype: str
        """
        return self._GroupField

    @GroupField.setter
    def GroupField(self, GroupField):
        self._GroupField = GroupField


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._GroupField = params.get("GroupField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumGroupLogResponse(AbstractModel):
    r"""DescribeRumGroupLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回字符串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumGroupLogV2Request(AbstractModel):
    r"""DescribeRumGroupLogV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 排序方式 desc asc（必填）
        :type OrderBy: str
        :param _StartTime: 开始时间（必填）
        :type StartTime: int
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Filter: 过滤条件
        :type Filter: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: int
        :param _ID: 项目ID（必填）
        :type ID: int
        :param _Label: 聚合字段
        :type Label: str
        :param _Last: 页数，第几页
        :type Last: int
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Filter = None
        self._EndTime = None
        self._ID = None
        self._Label = None
        self._Last = None

    @property
    def OrderBy(self):
        r"""排序方式 desc asc（必填）
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        r"""开始时间（必填）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        r"""单次查询返回的原始日志条数，最大值为100（必填）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        r"""过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def EndTime(self):
        r"""结束时间（必填）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Label(self):
        r"""聚合字段
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Last(self):
        r"""页数，第几页
        :rtype: int
        """
        return self._Last

    @Last.setter
    def Last(self, Last):
        self._Last = Last


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Filter = params.get("Filter")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._Label = params.get("Label")
        self._Last = params.get("Last")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumGroupLogV2Response(AbstractModel):
    r"""DescribeRumGroupLogV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: Query result in JSON string format
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Query result in JSON string format
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogDetailsV2Request(AbstractModel):
    r"""DescribeRumLogDetailsV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 排序方式 desc asc
        :type OrderBy: str
        :param _StartTime: 开始时间（必填）格式为时间戳 毫秒
        :type StartTime: int
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Filter: 查询的相关参数
        :type Filter: str
        :param _EndTime: 结束时间（必填）格式为时间戳 毫秒
        :type EndTime: int
        :param _ID: 项目ID（必填）
        :type ID: int
        :param _LastTime: 上次查询的最后一个日志的时间戳
        :type LastTime: int
        :param _LastRowId: 上次查询的最后一个日志的rowId
        :type LastRowId: int
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Filter = None
        self._EndTime = None
        self._ID = None
        self._LastTime = None
        self._LastRowId = None

    @property
    def OrderBy(self):
        r"""排序方式 desc asc
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        r"""开始时间（必填）格式为时间戳 毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        r"""单次查询返回的原始日志条数，最大值为100（必填）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        r"""查询的相关参数
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def EndTime(self):
        r"""结束时间（必填）格式为时间戳 毫秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def LastTime(self):
        r"""上次查询的最后一个日志的时间戳
        :rtype: int
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def LastRowId(self):
        r"""上次查询的最后一个日志的rowId
        :rtype: int
        """
        return self._LastRowId

    @LastRowId.setter
    def LastRowId(self, LastRowId):
        self._LastRowId = LastRowId


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Filter = params.get("Filter")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._LastTime = params.get("LastTime")
        self._LastRowId = params.get("LastRowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogDetailsV2Response(AbstractModel):
    r"""DescribeRumLogDetailsV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 日志明细
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""日志明细
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogExportRequest(AbstractModel):
    r"""DescribeRumLogExport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 导出标识name
        :type Name: str
        :param _StartTime: 开始时间（必填）
        :type StartTime: str
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        :param _Fields: field条件
        :type Fields: list of str
        """
        self._Name = None
        self._StartTime = None
        self._Query = None
        self._EndTime = None
        self._ID = None
        self._Fields = None

    @property
    def Name(self):
        r"""导出标识name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        r"""开始时间（必填）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Query(self):
        r"""查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        r"""结束时间（必填）
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Fields(self):
        r"""field条件
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._Fields = params.get("Fields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportResponse(AbstractModel):
    r"""DescribeRumLogExport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回字符串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogExportV2Request(AbstractModel):
    r"""DescribeRumLogExportV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: Export name
        :type Name: str
        :param _StartTime: Start time
        :type StartTime: int
        :param _Filter: Query statement
        :type Filter: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _Fields: c字段
        :type Fields: list of str
        """
        self._Name = None
        self._StartTime = None
        self._Filter = None
        self._EndTime = None
        self._ID = None
        self._Fields = None

    @property
    def Name(self):
        r"""Export name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        r"""Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Filter(self):
        r"""Query statement
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def EndTime(self):
        r"""End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Fields(self):
        r"""c字段
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._Filter = params.get("Filter")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._Fields = params.get("Fields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportV2Response(AbstractModel):
    r"""DescribeRumLogExportV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: Query result in JSON string format
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Query result in JSON string format
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogExportsRequest(AbstractModel):
    r"""DescribeRumLogExports请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 页面大小
        :type PageSize: int
        :param _PageNum: 页数，第几页
        :type PageNum: int
        :param _ID: 项目ID（必填）
        :type ID: int
        """
        self._PageSize = None
        self._PageNum = None
        self._ID = None

    @property
    def PageSize(self):
        r"""页面大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""页数，第几页
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportsResponse(AbstractModel):
    r"""DescribeRumLogExports返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回字符串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogExportsV2Request(AbstractModel):
    r"""DescribeRumLogExportsV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: Page size
        :type PageSize: int
        :param _PageNum: Page number
        :type PageNum: int
        :param _ID: Project ID
        :type ID: int
        """
        self._PageSize = None
        self._PageNum = None
        self._ID = None

    @property
    def PageSize(self):
        r"""Page size
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        r"""Page number
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def ID(self):
        r"""Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportsV2Response(AbstractModel):
    r"""DescribeRumLogExportsV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: Query result in JSON string format
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Query result in JSON string format
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogListRequest(AbstractModel):
    r"""DescribeRumLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 排序方式  desc  asc（必填）
        :type OrderBy: str
        :param _StartTime: 开始时间（必填）格式为时间戳 毫秒
        :type StartTime: str
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Page: 页数，第几页
        :type Page: int
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）格式为时间戳 毫秒
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Page = None
        self._Query = None
        self._EndTime = None
        self._ID = None

    @property
    def OrderBy(self):
        r"""排序方式  desc  asc（必填）
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        r"""开始时间（必填）格式为时间戳 毫秒
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        r"""单次查询返回的原始日志条数，最大值为100（必填）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        r"""页数，第几页
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Query(self):
        r"""查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        r"""结束时间（必填）格式为时间戳 毫秒
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogListResponse(AbstractModel):
    r"""DescribeRumLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回字符串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumLogTotalV2Request(AbstractModel):
    r"""DescribeRumLogTotalV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 排序方式 desc asc
        :type OrderBy: str
        :param _StartTime: 开始时间（必填）格式为时间戳 毫秒
        :type StartTime: int
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Filter: 查询的相关参数
        :type Filter: str
        :param _EndTime: 结束时间（必填）格式为时间戳 毫秒
        :type EndTime: int
        :param _ID: 项目ID（必填）
        :type ID: int
        :param _LastTime: 上次查询的最后一个日志的时间戳
        :type LastTime: int
        :param _LastRowId: 上次查询的最后一个日志的rowId
        :type LastRowId: int
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Filter = None
        self._EndTime = None
        self._ID = None
        self._LastTime = None
        self._LastRowId = None

    @property
    def OrderBy(self):
        r"""排序方式 desc asc
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        r"""开始时间（必填）格式为时间戳 毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        r"""单次查询返回的原始日志条数，最大值为100（必填）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        r"""查询的相关参数
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def EndTime(self):
        r"""结束时间（必填）格式为时间戳 毫秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def LastTime(self):
        r"""上次查询的最后一个日志的时间戳
        :rtype: int
        """
        return self._LastTime

    @LastTime.setter
    def LastTime(self, LastTime):
        self._LastTime = LastTime

    @property
    def LastRowId(self):
        r"""上次查询的最后一个日志的rowId
        :rtype: int
        """
        return self._LastRowId

    @LastRowId.setter
    def LastRowId(self, LastRowId):
        self._LastRowId = LastRowId


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Filter = params.get("Filter")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._LastTime = params.get("LastTime")
        self._LastRowId = params.get("LastRowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogTotalV2Response(AbstractModel):
    r"""DescribeRumLogTotalV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 日志总量
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""日志总量
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumStatsLogListRequest(AbstractModel):
    r"""DescribeRumStatsLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间（必填）
        :type StartTime: str
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Query: 查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :type Query: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: str
        :param _ID: 项目ID（必填）
        :type ID: int
        """
        self._StartTime = None
        self._Limit = None
        self._Query = None
        self._EndTime = None
        self._ID = None

    @property
    def StartTime(self):
        r"""开始时间（必填）
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        r"""单次查询返回的原始日志条数，最大值为100（必填）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Query(self):
        r"""查询语句，参考控制台请求参数，语句长度最大为4096（必填）
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        r"""结束时间（必填）
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumStatsLogListResponse(AbstractModel):
    r"""DescribeRumStatsLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回字符串
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""返回字符串
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeRumStatsLogListV2Request(AbstractModel):
    r"""DescribeRumStatsLogListV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间（必填）
        :type StartTime: int
        :param _Limit: 单次查询返回的原始日志条数，最大值为100（必填）
        :type Limit: int
        :param _Filter: 过滤条件
        :type Filter: str
        :param _EndTime: 结束时间（必填）
        :type EndTime: int
        :param _ID: 项目ID（必填）
        :type ID: int
        """
        self._StartTime = None
        self._Limit = None
        self._Filter = None
        self._EndTime = None
        self._ID = None

    @property
    def StartTime(self):
        r"""开始时间（必填）
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        r"""单次查询返回的原始日志条数，最大值为100（必填）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        r"""过滤条件
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def EndTime(self):
        r"""结束时间（必填）
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        r"""项目ID（必填）
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Filter = params.get("Filter")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumStatsLogListV2Response(AbstractModel):
    r"""DescribeRumStatsLogListV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: Query result in JSON string format
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""Query result in JSON string format
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeScoresRequest(AbstractModel):
    r"""DescribeScores请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _ID: 项目ID
        :type ID: int
        :param _IsDemo: 该参数已废弃
        :type IsDemo: int
        :param _IDList: 项目 ID 列表
        :type IDList: list of int
        """
        self._EndTime = None
        self._StartTime = None
        self._ID = None
        self._IsDemo = None
        self._IDList = None

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def IsDemo(self):
        warnings.warn("parameter `IsDemo` is deprecated", DeprecationWarning) 

        r"""该参数已废弃
        :rtype: int
        """
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        warnings.warn("parameter `IsDemo` is deprecated", DeprecationWarning) 

        self._IsDemo = IsDemo

    @property
    def IDList(self):
        r"""项目 ID 列表
        :rtype: list of int
        """
        return self._IDList

    @IDList.setter
    def IDList(self, IDList):
        self._IDList = IDList


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._ID = params.get("ID")
        self._IsDemo = params.get("IsDemo")
        self._IDList = params.get("IDList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoresResponse(AbstractModel):
    r"""DescribeScores返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScoreSet: 数组
        :type ScoreSet: list of ScoreInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreSet = None
        self._RequestId = None

    @property
    def ScoreSet(self):
        r"""数组
        :rtype: list of ScoreInfo
        """
        return self._ScoreSet

    @ScoreSet.setter
    def ScoreSet(self, ScoreSet):
        self._ScoreSet = ScoreSet

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
        if params.get("ScoreSet") is not None:
            self._ScoreSet = []
            for item in params.get("ScoreSet"):
                obj = ScoreInfo()
                obj._deserialize(item)
                self._ScoreSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScoresV2Request(AbstractModel):
    r"""DescribeScoresV2请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _IDList: 项目 ID 列表
        :type IDList: list of int
        :param _Type: 查询粒度，hour 或 day
        :type Type: str
        :param _Env: 环境
        :type Env: str
        """
        self._StartTime = None
        self._EndTime = None
        self._IDList = None
        self._Type = None
        self._Env = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IDList(self):
        r"""项目 ID 列表
        :rtype: list of int
        """
        return self._IDList

    @IDList.setter
    def IDList(self, IDList):
        self._IDList = IDList

    @property
    def Type(self):
        r"""查询粒度，hour 或 day
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Env(self):
        r"""环境
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IDList = params.get("IDList")
        self._Type = params.get("Type")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoresV2Response(AbstractModel):
    r"""DescribeScoresV2返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScoreSet: 项目得分数组
        :type ScoreSet: list of ScoreInfoV2
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreSet = None
        self._RequestId = None

    @property
    def ScoreSet(self):
        r"""项目得分数组
        :rtype: list of ScoreInfoV2
        """
        return self._ScoreSet

    @ScoreSet.setter
    def ScoreSet(self, ScoreSet):
        self._ScoreSet = ScoreSet

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
        if params.get("ScoreSet") is not None:
            self._ScoreSet = []
            for item in params.get("ScoreSet"):
                obj = ScoreInfoV2()
                obj._deserialize(item)
                self._ScoreSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTawAreasRequest(AbstractModel):
    r"""DescribeTawAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AreaIds: 片区Id
        :type AreaIds: list of int
        :param _AreaKeys: 片区Key
        :type AreaKeys: list of str
        :param _Limit: 分页Limit，默认根据AreaKeys和AreaStatuses参数查询所有。
        :type Limit: int
        :param _AreaStatuses: 片区状态(1=有效，2=无效)
        :type AreaStatuses: list of int
        :param _Offset: 分页Offset，默认根据AreaKeys和AreaStatuses参数查询所有。
        :type Offset: int
        """
        self._AreaIds = None
        self._AreaKeys = None
        self._Limit = None
        self._AreaStatuses = None
        self._Offset = None

    @property
    def AreaIds(self):
        r"""片区Id
        :rtype: list of int
        """
        return self._AreaIds

    @AreaIds.setter
    def AreaIds(self, AreaIds):
        self._AreaIds = AreaIds

    @property
    def AreaKeys(self):
        r"""片区Key
        :rtype: list of str
        """
        return self._AreaKeys

    @AreaKeys.setter
    def AreaKeys(self, AreaKeys):
        self._AreaKeys = AreaKeys

    @property
    def Limit(self):
        r"""分页Limit，默认根据AreaKeys和AreaStatuses参数查询所有。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AreaStatuses(self):
        r"""片区状态(1=有效，2=无效)
        :rtype: list of int
        """
        return self._AreaStatuses

    @AreaStatuses.setter
    def AreaStatuses(self, AreaStatuses):
        self._AreaStatuses = AreaStatuses

    @property
    def Offset(self):
        r"""分页Offset，默认根据AreaKeys和AreaStatuses参数查询所有。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._AreaIds = params.get("AreaIds")
        self._AreaKeys = params.get("AreaKeys")
        self._Limit = params.get("Limit")
        self._AreaStatuses = params.get("AreaStatuses")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawAreasResponse(AbstractModel):
    r"""DescribeTawAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 片区总数
        :type TotalCount: int
        :param _AreaSet: 片区列表
        :type AreaSet: list of RumAreaInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AreaSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""片区总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AreaSet(self):
        r"""片区列表
        :rtype: list of RumAreaInfo
        """
        return self._AreaSet

    @AreaSet.setter
    def AreaSet(self, AreaSet):
        self._AreaSet = AreaSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("AreaSet") is not None:
            self._AreaSet = []
            for item in params.get("AreaSet"):
                obj = RumAreaInfo()
                obj._deserialize(item)
                self._AreaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTawInstancesRequest(AbstractModel):
    r"""DescribeTawInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChargeStatuses: 计费状态
        :type ChargeStatuses: list of int
        :param _ChargeTypes: 计费类型
        :type ChargeTypes: list of int
        :param _Limit: 分页Limit
        :type Limit: int
        :param _Offset: 分页Offset
        :type Offset: int
        :param _AreaIds: 片区Id
        :type AreaIds: list of int
        :param _InstanceStatuses: 实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=销毁中，8=已销毁), 该参数已废弃，请在Filters内注明
        :type InstanceStatuses: list of int
        :param _InstanceIds: 实例Id, 该参数已废弃，请在Filters内注明
        :type InstanceIds: list of str
        :param _Filters: 过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :type Filters: list of Filter
        :param _IsDemo: 该参数已废弃，demo模式请在Filters内注明
        :type IsDemo: int
        """
        self._ChargeStatuses = None
        self._ChargeTypes = None
        self._Limit = None
        self._Offset = None
        self._AreaIds = None
        self._InstanceStatuses = None
        self._InstanceIds = None
        self._Filters = None
        self._IsDemo = None

    @property
    def ChargeStatuses(self):
        r"""计费状态
        :rtype: list of int
        """
        return self._ChargeStatuses

    @ChargeStatuses.setter
    def ChargeStatuses(self, ChargeStatuses):
        self._ChargeStatuses = ChargeStatuses

    @property
    def ChargeTypes(self):
        r"""计费类型
        :rtype: list of int
        """
        return self._ChargeTypes

    @ChargeTypes.setter
    def ChargeTypes(self, ChargeTypes):
        self._ChargeTypes = ChargeTypes

    @property
    def Limit(self):
        r"""分页Limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AreaIds(self):
        r"""片区Id
        :rtype: list of int
        """
        return self._AreaIds

    @AreaIds.setter
    def AreaIds(self, AreaIds):
        self._AreaIds = AreaIds

    @property
    def InstanceStatuses(self):
        warnings.warn("parameter `InstanceStatuses` is deprecated", DeprecationWarning) 

        r"""实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=销毁中，8=已销毁), 该参数已废弃，请在Filters内注明
        :rtype: list of int
        """
        return self._InstanceStatuses

    @InstanceStatuses.setter
    def InstanceStatuses(self, InstanceStatuses):
        warnings.warn("parameter `InstanceStatuses` is deprecated", DeprecationWarning) 

        self._InstanceStatuses = InstanceStatuses

    @property
    def InstanceIds(self):
        warnings.warn("parameter `InstanceIds` is deprecated", DeprecationWarning) 

        r"""实例Id, 该参数已废弃，请在Filters内注明
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        warnings.warn("parameter `InstanceIds` is deprecated", DeprecationWarning) 

        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        r"""过滤参数；demo模式传{"Name": "IsDemo", "Values":["1"]}
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def IsDemo(self):
        warnings.warn("parameter `IsDemo` is deprecated", DeprecationWarning) 

        r"""该参数已废弃，demo模式请在Filters内注明
        :rtype: int
        """
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        warnings.warn("parameter `IsDemo` is deprecated", DeprecationWarning) 

        self._IsDemo = IsDemo


    def _deserialize(self, params):
        self._ChargeStatuses = params.get("ChargeStatuses")
        self._ChargeTypes = params.get("ChargeTypes")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AreaIds = params.get("AreaIds")
        self._InstanceStatuses = params.get("InstanceStatuses")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawInstancesResponse(AbstractModel):
    r"""DescribeTawInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: 实例列表
        :type InstanceSet: list of RumInstanceInfo
        :param _TotalCount: 实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        r"""实例列表
        :rtype: list of RumInstanceInfo
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        r"""实例总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = RumInstanceInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTokenRequest(AbstractModel):
    r"""DescribeToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FormListString: <p>筛选条件</p>
        :type FormListString: str
        :param _FormListAString: <p>仅对比模式下填写，筛选条件A</p>
        :type FormListAString: str
        :param _FormListBString: <p>仅对比模式下填写，筛选条件B</p>
        :type FormListBString: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        :param _ExtraData: <p>拓展字段</p>
        :type ExtraData: str
        """
        self._FormListString = None
        self._FormListAString = None
        self._FormListBString = None
        self._RequestHeader = None
        self._ExtraData = None

    @property
    def FormListString(self):
        r"""<p>筛选条件</p>
        :rtype: str
        """
        return self._FormListString

    @FormListString.setter
    def FormListString(self, FormListString):
        self._FormListString = FormListString

    @property
    def FormListAString(self):
        r"""<p>仅对比模式下填写，筛选条件A</p>
        :rtype: str
        """
        return self._FormListAString

    @FormListAString.setter
    def FormListAString(self, FormListAString):
        self._FormListAString = FormListAString

    @property
    def FormListBString(self):
        r"""<p>仅对比模式下填写，筛选条件B</p>
        :rtype: str
        """
        return self._FormListBString

    @FormListBString.setter
    def FormListBString(self, FormListBString):
        self._FormListBString = FormListBString

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ExtraData(self):
        r"""<p>拓展字段</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData


    def _deserialize(self, params):
        self._FormListString = params.get("FormListString")
        self._FormListAString = params.get("FormListAString")
        self._FormListBString = params.get("FormListBString")
        self._RequestHeader = params.get("RequestHeader")
        self._ExtraData = params.get("ExtraData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenResponse(AbstractModel):
    r"""DescribeToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeTopIssuesRequest(AbstractModel):
    r"""DescribeTopIssues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: <p>产品Id</p>
        :type ProductId: str
        :param _Compare: <p>需要对比的查询条件，没有则不填</p>
        :type Compare: :class:`tencentcloud.rum.v20210622.models.CompareCondition`
        :param _Condition: <p>查询条件</p>
        :type Condition: :class:`tencentcloud.rum.v20210622.models.CompareCondition`
        :param _IssueType: <p>问题类型</p>
        :type IssueType: int
        :param _SortField: <p>排序字段</p>
        :type SortField: str
        :param _SortType: <p>排序方式</p>
        :type SortType: str
        :param _TopNum: <p>topN</p>
        :type TopNum: int
        :param _ExtraData: <p>拓展字段</p>
        :type ExtraData: str
        :param _RequestHeader: <p>请求头</p>
        :type RequestHeader: str
        """
        self._ProductId = None
        self._Compare = None
        self._Condition = None
        self._IssueType = None
        self._SortField = None
        self._SortType = None
        self._TopNum = None
        self._ExtraData = None
        self._RequestHeader = None

    @property
    def ProductId(self):
        r"""<p>产品Id</p>
        :rtype: str
        """
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def Compare(self):
        r"""<p>需要对比的查询条件，没有则不填</p>
        :rtype: :class:`tencentcloud.rum.v20210622.models.CompareCondition`
        """
        return self._Compare

    @Compare.setter
    def Compare(self, Compare):
        self._Compare = Compare

    @property
    def Condition(self):
        r"""<p>查询条件</p>
        :rtype: :class:`tencentcloud.rum.v20210622.models.CompareCondition`
        """
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def IssueType(self):
        r"""<p>问题类型</p>
        :rtype: int
        """
        return self._IssueType

    @IssueType.setter
    def IssueType(self, IssueType):
        self._IssueType = IssueType

    @property
    def SortField(self):
        r"""<p>排序字段</p>
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""<p>排序方式</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def TopNum(self):
        r"""<p>topN</p>
        :rtype: int
        """
        return self._TopNum

    @TopNum.setter
    def TopNum(self, TopNum):
        self._TopNum = TopNum

    @property
    def ExtraData(self):
        r"""<p>拓展字段</p>
        :rtype: str
        """
        return self._ExtraData

    @ExtraData.setter
    def ExtraData(self, ExtraData):
        self._ExtraData = ExtraData

    @property
    def RequestHeader(self):
        r"""<p>请求头</p>
        :rtype: str
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        if params.get("Compare") is not None:
            self._Compare = CompareCondition()
            self._Compare._deserialize(params.get("Compare"))
        if params.get("Condition") is not None:
            self._Condition = CompareCondition()
            self._Condition._deserialize(params.get("Condition"))
        self._IssueType = params.get("IssueType")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._TopNum = params.get("TopNum")
        self._ExtraData = params.get("ExtraData")
        self._RequestHeader = params.get("RequestHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopIssuesResponse(AbstractModel):
    r"""DescribeTopIssues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: <p>返回值</p>
        :type Data: str
        :param _Code: <p>状态码</p>
        :type Code: int
        :param _Message: <p>消息</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>返回值</p>
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Code(self):
        r"""<p>状态码</p>
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Data = params.get("Data")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeUvListRequest(AbstractModel):
    r"""DescribeUvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: ID
        :type ProjectId: int
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _Dimension: 获取day：d，   min:m
        :type Dimension: str
        """
        self._ProjectId = None
        self._EndTime = None
        self._StartTime = None
        self._Dimension = None

    @property
    def ProjectId(self):
        r"""ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Dimension(self):
        r"""获取day：d，   min:m
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUvListResponse(AbstractModel):
    r"""DescribeUvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectUvSet: uv列表
        :type ProjectUvSet: list of RumUvInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectUvSet = None
        self._RequestId = None

    @property
    def ProjectUvSet(self):
        r"""uv列表
        :rtype: list of RumUvInfo
        """
        return self._ProjectUvSet

    @ProjectUvSet.setter
    def ProjectUvSet(self, ProjectUvSet):
        self._ProjectUvSet = ProjectUvSet

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
        if params.get("ProjectUvSet") is not None:
            self._ProjectUvSet = []
            for item in params.get("ProjectUvSet"):
                obj = RumUvInfo()
                obj._deserialize(item)
                self._ProjectUvSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhitelistsRequest(AbstractModel):
    r"""DescribeWhitelists请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceID: 实例instance-ID
        :type InstanceID: str
        """
        self._InstanceID = None

    @property
    def InstanceID(self):
        r"""实例instance-ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhitelistsResponse(AbstractModel):
    r"""DescribeWhitelists返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WhitelistSet: 白名单列表
        :type WhitelistSet: list of Whitelist
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WhitelistSet = None
        self._RequestId = None

    @property
    def WhitelistSet(self):
        r"""白名单列表
        :rtype: list of Whitelist
        """
        return self._WhitelistSet

    @WhitelistSet.setter
    def WhitelistSet(self, WhitelistSet):
        self._WhitelistSet = WhitelistSet

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
        if params.get("WhitelistSet") is not None:
            self._WhitelistSet = []
            for item in params.get("WhitelistSet"):
                obj = Whitelist()
                obj._deserialize(item)
                self._WhitelistSet.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    · 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    · 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        :param _Name: 过滤键的名称。
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        r"""一个或者多个过滤值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        r"""过滤键的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    r"""BugLY筛选结构体

    """

    def __init__(self):
        r"""
        :param _IsReversed: 是否反转
        :type IsReversed: bool
        :param _Key: 键
        :type Key: str
        :param _Name: 名称
        :type Name: str
        :param _Operator: 运算符
        :type Operator: str
        :param _Type: 类型
        :type Type: int
        :param _Values: 值
        :type Values: list of str
        """
        self._IsReversed = None
        self._Key = None
        self._Name = None
        self._Operator = None
        self._Type = None
        self._Values = None

    @property
    def IsReversed(self):
        r"""是否反转
        :rtype: bool
        """
        return self._IsReversed

    @IsReversed.setter
    def IsReversed(self, IsReversed):
        self._IsReversed = IsReversed

    @property
    def Key(self):
        r"""键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

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
    def Operator(self):
        r"""运算符
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Type(self):
        r"""类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
        r"""值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._IsReversed = params.get("IsReversed")
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        self._Operator = params.get("Operator")
        self._Type = params.get("Type")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Kafka(AbstractModel):
    r"""旁路kafka配置

    """

    def __init__(self):
        r"""
        :param _EnableKafka: 1：开启
0：关闭
        :type EnableKafka: int
        :param _KafkaHost: host地址
        :type KafkaHost: str
        :param _KafkaTopic: topic
        :type KafkaTopic: str
        :param _KafkaVersion: 版本
        :type KafkaVersion: str
        :param _SaslUserName: username
        :type SaslUserName: str
        :param _SaslPassword: password
        :type SaslPassword: str
        :param _SaslMechanism: ssl
        :type SaslMechanism: str
        :param _SinkId: 默认算子id为0新增算子
一旦算子新增成功会返回正确的算子id值
        :type SinkId: int
        """
        self._EnableKafka = None
        self._KafkaHost = None
        self._KafkaTopic = None
        self._KafkaVersion = None
        self._SaslUserName = None
        self._SaslPassword = None
        self._SaslMechanism = None
        self._SinkId = None

    @property
    def EnableKafka(self):
        r"""1：开启
0：关闭
        :rtype: int
        """
        return self._EnableKafka

    @EnableKafka.setter
    def EnableKafka(self, EnableKafka):
        self._EnableKafka = EnableKafka

    @property
    def KafkaHost(self):
        r"""host地址
        :rtype: str
        """
        return self._KafkaHost

    @KafkaHost.setter
    def KafkaHost(self, KafkaHost):
        self._KafkaHost = KafkaHost

    @property
    def KafkaTopic(self):
        r"""topic
        :rtype: str
        """
        return self._KafkaTopic

    @KafkaTopic.setter
    def KafkaTopic(self, KafkaTopic):
        self._KafkaTopic = KafkaTopic

    @property
    def KafkaVersion(self):
        r"""版本
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SaslUserName(self):
        r"""username
        :rtype: str
        """
        return self._SaslUserName

    @SaslUserName.setter
    def SaslUserName(self, SaslUserName):
        self._SaslUserName = SaslUserName

    @property
    def SaslPassword(self):
        r"""password
        :rtype: str
        """
        return self._SaslPassword

    @SaslPassword.setter
    def SaslPassword(self, SaslPassword):
        self._SaslPassword = SaslPassword

    @property
    def SaslMechanism(self):
        r"""ssl
        :rtype: str
        """
        return self._SaslMechanism

    @SaslMechanism.setter
    def SaslMechanism(self, SaslMechanism):
        self._SaslMechanism = SaslMechanism

    @property
    def SinkId(self):
        r"""默认算子id为0新增算子
一旦算子新增成功会返回正确的算子id值
        :rtype: int
        """
        return self._SinkId

    @SinkId.setter
    def SinkId(self, SinkId):
        self._SinkId = SinkId


    def _deserialize(self, params):
        self._EnableKafka = params.get("EnableKafka")
        self._KafkaHost = params.get("KafkaHost")
        self._KafkaTopic = params.get("KafkaTopic")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SaslUserName = params.get("SaslUserName")
        self._SaslPassword = params.get("SaslPassword")
        self._SaslMechanism = params.get("SaslMechanism")
        self._SinkId = params.get("SinkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRequest(AbstractModel):
    r"""ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 要修改的实例id
        :type InstanceId: str
        :param _InstanceName: 新的实例名称(长度最大不超过255)
        :type InstanceName: str
        :param _InstanceDesc: 新的实例描述(长度最大不超过1024)
        :type InstanceDesc: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceDesc = None

    @property
    def InstanceId(self):
        r"""要修改的实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""新的实例名称(长度最大不超过255)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceDesc(self):
        r"""新的实例描述(长度最大不超过1024)
        :rtype: str
        """
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceDesc = params.get("InstanceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    r"""ModifyInstance返回参数结构体

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


class ModifyProjectLimitRequest(AbstractModel):
    r"""ModifyProjectLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectID: 项目ID
        :type ProjectID: int
        :param _ProjectInterface: 取值为[log speed performance webvitals pv event custom miniProgramData]其中之一
        :type ProjectInterface: str
        :param _ReportRate: 上报比例   10代表10%
        :type ReportRate: int
        :param _ReportType: 上报类型 1：比例  2：上报量
        :type ReportType: int
        :param _ID: 主键ID
        :type ID: int
        """
        self._ProjectID = None
        self._ProjectInterface = None
        self._ReportRate = None
        self._ReportType = None
        self._ID = None

    @property
    def ProjectID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ProjectInterface(self):
        r"""取值为[log speed performance webvitals pv event custom miniProgramData]其中之一
        :rtype: str
        """
        return self._ProjectInterface

    @ProjectInterface.setter
    def ProjectInterface(self, ProjectInterface):
        self._ProjectInterface = ProjectInterface

    @property
    def ReportRate(self):
        r"""上报比例   10代表10%
        :rtype: int
        """
        return self._ReportRate

    @ReportRate.setter
    def ReportRate(self, ReportRate):
        self._ReportRate = ReportRate

    @property
    def ReportType(self):
        r"""上报类型 1：比例  2：上报量
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def ID(self):
        r"""主键ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._ProjectInterface = params.get("ProjectInterface")
        self._ReportRate = params.get("ReportRate")
        self._ReportType = params.get("ReportType")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectLimitResponse(AbstractModel):
    r"""ModifyProjectLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 返回信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""返回信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    r"""ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ID: 项目 id
        :type ID: int
        :param _Name: 应用名称(可选，不为空且最长为 200字符)
        :type Name: str
        :param _URL: 项目网页地址(可选，最长为 256)
        :type URL: str
        :param _Repo: 项目仓库地址(可选，最长为 256)
        :type Repo: str
        :param _InstanceID: 项目需要转移到的实例 id(可选)
        :type InstanceID: str
        :param _Rate: 项目采样率(可选)
        :type Rate: str
        :param _EnableURLGroup: 是否开启聚类(可选)
        :type EnableURLGroup: int
        :param _Type: 项目类型(可接受值为 "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param _Desc: 应用描述(可选，最长为 1000字符)
        :type Desc: str
        :param _EnableKafka: 启动kafka配置
        :type EnableKafka: int
        :param _KafkaHost: kafka_host
        :type KafkaHost: str
        :param _KafkaTopic: topic
        :type KafkaTopic: str
        :param _KafkaVersion: kafka_version
        :type KafkaVersion: str
        :param _SaslUserName: kafka_username
        :type SaslUserName: str
        :param _SaslPassword: kafka_pwd
        :type SaslPassword: str
        :param _SaslMechanism: SaslMechanism
        :type SaslMechanism: str
        :param _SinkId: sink_id，日知汇算子id
        :type SinkId: int
        """
        self._ID = None
        self._Name = None
        self._URL = None
        self._Repo = None
        self._InstanceID = None
        self._Rate = None
        self._EnableURLGroup = None
        self._Type = None
        self._Desc = None
        self._EnableKafka = None
        self._KafkaHost = None
        self._KafkaTopic = None
        self._KafkaVersion = None
        self._SaslUserName = None
        self._SaslPassword = None
        self._SaslMechanism = None
        self._SinkId = None

    @property
    def ID(self):
        r"""项目 id
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        r"""应用名称(可选，不为空且最长为 200字符)
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def URL(self):
        r"""项目网页地址(可选，最长为 256)
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Repo(self):
        r"""项目仓库地址(可选，最长为 256)
        :rtype: str
        """
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def InstanceID(self):
        r"""项目需要转移到的实例 id(可选)
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Rate(self):
        r"""项目采样率(可选)
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def EnableURLGroup(self):
        r"""是否开启聚类(可选)
        :rtype: int
        """
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def Type(self):
        r"""项目类型(可接受值为 "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Desc(self):
        r"""应用描述(可选，最长为 1000字符)
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def EnableKafka(self):
        r"""启动kafka配置
        :rtype: int
        """
        return self._EnableKafka

    @EnableKafka.setter
    def EnableKafka(self, EnableKafka):
        self._EnableKafka = EnableKafka

    @property
    def KafkaHost(self):
        r"""kafka_host
        :rtype: str
        """
        return self._KafkaHost

    @KafkaHost.setter
    def KafkaHost(self, KafkaHost):
        self._KafkaHost = KafkaHost

    @property
    def KafkaTopic(self):
        r"""topic
        :rtype: str
        """
        return self._KafkaTopic

    @KafkaTopic.setter
    def KafkaTopic(self, KafkaTopic):
        self._KafkaTopic = KafkaTopic

    @property
    def KafkaVersion(self):
        r"""kafka_version
        :rtype: str
        """
        return self._KafkaVersion

    @KafkaVersion.setter
    def KafkaVersion(self, KafkaVersion):
        self._KafkaVersion = KafkaVersion

    @property
    def SaslUserName(self):
        r"""kafka_username
        :rtype: str
        """
        return self._SaslUserName

    @SaslUserName.setter
    def SaslUserName(self, SaslUserName):
        self._SaslUserName = SaslUserName

    @property
    def SaslPassword(self):
        r"""kafka_pwd
        :rtype: str
        """
        return self._SaslPassword

    @SaslPassword.setter
    def SaslPassword(self, SaslPassword):
        self._SaslPassword = SaslPassword

    @property
    def SaslMechanism(self):
        r"""SaslMechanism
        :rtype: str
        """
        return self._SaslMechanism

    @SaslMechanism.setter
    def SaslMechanism(self, SaslMechanism):
        self._SaslMechanism = SaslMechanism

    @property
    def SinkId(self):
        r"""sink_id，日知汇算子id
        :rtype: int
        """
        return self._SinkId

    @SinkId.setter
    def SinkId(self, SinkId):
        self._SinkId = SinkId


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._URL = params.get("URL")
        self._Repo = params.get("Repo")
        self._InstanceID = params.get("InstanceID")
        self._Rate = params.get("Rate")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._Type = params.get("Type")
        self._Desc = params.get("Desc")
        self._EnableKafka = params.get("EnableKafka")
        self._KafkaHost = params.get("KafkaHost")
        self._KafkaTopic = params.get("KafkaTopic")
        self._KafkaVersion = params.get("KafkaVersion")
        self._SaslUserName = params.get("SaslUserName")
        self._SaslPassword = params.get("SaslPassword")
        self._SaslMechanism = params.get("SaslMechanism")
        self._SinkId = params.get("SinkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    r"""ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Msg: 操作信息
        :type Msg: str
        :param _ID: 项目id
        :type ID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Msg = None
        self._ID = None
        self._RequestId = None

    @property
    def Msg(self):
        r"""操作信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def ID(self):
        r"""项目id
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

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
        self._Msg = params.get("Msg")
        self._ID = params.get("ID")
        self._RequestId = params.get("RequestId")


class ProjectLimit(AbstractModel):
    r"""项目接口限制类型

    """

    def __init__(self):
        r"""
        :param _ProjectInterface: 接口
        :type ProjectInterface: str
        :param _ReportRate: 上报率
        :type ReportRate: int
        :param _ReportType: 上报类型 1：上报率  2：上报量限制
        :type ReportType: int
        :param _ID: 主键ID
        :type ID: int
        :param _ProjectID: 项目ID
        :type ProjectID: int
        """
        self._ProjectInterface = None
        self._ReportRate = None
        self._ReportType = None
        self._ID = None
        self._ProjectID = None

    @property
    def ProjectInterface(self):
        r"""接口
        :rtype: str
        """
        return self._ProjectInterface

    @ProjectInterface.setter
    def ProjectInterface(self, ProjectInterface):
        self._ProjectInterface = ProjectInterface

    @property
    def ReportRate(self):
        r"""上报率
        :rtype: int
        """
        return self._ReportRate

    @ReportRate.setter
    def ReportRate(self, ReportRate):
        self._ReportRate = ReportRate

    @property
    def ReportType(self):
        r"""上报类型 1：上报率  2：上报量限制
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def ID(self):
        r"""主键ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ProjectID(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID


    def _deserialize(self, params):
        self._ProjectInterface = params.get("ProjectInterface")
        self._ReportRate = params.get("ReportRate")
        self._ReportType = params.get("ReportType")
        self._ID = params.get("ID")
        self._ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseFile(AbstractModel):
    r"""发布文件列表(SOURCEMAP)

    """

    def __init__(self):
        r"""
        :param _Version: <p>文件版本</p>
        :type Version: str
        :param _FileKey: <p>文件唯一 key</p>
        :type FileKey: str
        :param _FileName: <p>文件名</p>
        :type FileName: str
        :param _FileHash: <p>文件哈希值</p>
        :type FileHash: str
        :param _ID: <p>文件 id</p>
        :type ID: int
        :param _CreatedAt: <p>创建时间</p>
        :type CreatedAt: str
        """
        self._Version = None
        self._FileKey = None
        self._FileName = None
        self._FileHash = None
        self._ID = None
        self._CreatedAt = None

    @property
    def Version(self):
        r"""<p>文件版本</p>
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def FileKey(self):
        r"""<p>文件唯一 key</p>
        :rtype: str
        """
        return self._FileKey

    @FileKey.setter
    def FileKey(self, FileKey):
        self._FileKey = FileKey

    @property
    def FileName(self):
        r"""<p>文件名</p>
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileHash(self):
        r"""<p>文件哈希值</p>
        :rtype: str
        """
        return self._FileHash

    @FileHash.setter
    def FileHash(self, FileHash):
        self._FileHash = FileHash

    @property
    def ID(self):
        r"""<p>文件 id</p>
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreatedAt(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._FileKey = params.get("FileKey")
        self._FileName = params.get("FileName")
        self._FileHash = params.get("FileHash")
        self._ID = params.get("ID")
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceRequest(AbstractModel):
    r"""ResumeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要恢复的实例id
        :type InstanceId: str
        :param _IsModifyAll: 修改是否包括白名单
        :type IsModifyAll: bool
        """
        self._InstanceId = None
        self._IsModifyAll = None

    @property
    def InstanceId(self):
        r"""需要恢复的实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IsModifyAll(self):
        r"""修改是否包括白名单
        :rtype: bool
        """
        return self._IsModifyAll

    @IsModifyAll.setter
    def IsModifyAll(self, IsModifyAll):
        self._IsModifyAll = IsModifyAll


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IsModifyAll = params.get("IsModifyAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceResponse(AbstractModel):
    r"""ResumeInstance返回参数结构体

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


class ResumeProjectRequest(AbstractModel):
    r"""ResumeProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 id
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        r"""项目 id
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProjectResponse(AbstractModel):
    r"""ResumeProject返回参数结构体

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


class RumAreaInfo(AbstractModel):
    r"""Rum片区信息

    """

    def __init__(self):
        r"""
        :param _AreaId: 片区Id
        :type AreaId: int
        :param _AreaStatus: 片区状态(1=有效，2=无效)
        :type AreaStatus: int
        :param _AreaName: 片区名称
        :type AreaName: str
        :param _AreaKey: 片区Key
        :type AreaKey: str
        :param _AreaRegionID: 地域码表 id
        :type AreaRegionID: str
        :param _AreaRegionCode: 地域码表 code 如 ap-xxx（xxx 为地域词）
        :type AreaRegionCode: str
        :param _AreaAbbr: 地域缩写
        :type AreaAbbr: str
        """
        self._AreaId = None
        self._AreaStatus = None
        self._AreaName = None
        self._AreaKey = None
        self._AreaRegionID = None
        self._AreaRegionCode = None
        self._AreaAbbr = None

    @property
    def AreaId(self):
        r"""片区Id
        :rtype: int
        """
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def AreaStatus(self):
        r"""片区状态(1=有效，2=无效)
        :rtype: int
        """
        return self._AreaStatus

    @AreaStatus.setter
    def AreaStatus(self, AreaStatus):
        self._AreaStatus = AreaStatus

    @property
    def AreaName(self):
        r"""片区名称
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def AreaKey(self):
        r"""片区Key
        :rtype: str
        """
        return self._AreaKey

    @AreaKey.setter
    def AreaKey(self, AreaKey):
        self._AreaKey = AreaKey

    @property
    def AreaRegionID(self):
        r"""地域码表 id
        :rtype: str
        """
        return self._AreaRegionID

    @AreaRegionID.setter
    def AreaRegionID(self, AreaRegionID):
        self._AreaRegionID = AreaRegionID

    @property
    def AreaRegionCode(self):
        r"""地域码表 code 如 ap-xxx（xxx 为地域词）
        :rtype: str
        """
        return self._AreaRegionCode

    @AreaRegionCode.setter
    def AreaRegionCode(self, AreaRegionCode):
        self._AreaRegionCode = AreaRegionCode

    @property
    def AreaAbbr(self):
        r"""地域缩写
        :rtype: str
        """
        return self._AreaAbbr

    @AreaAbbr.setter
    def AreaAbbr(self, AreaAbbr):
        self._AreaAbbr = AreaAbbr


    def _deserialize(self, params):
        self._AreaId = params.get("AreaId")
        self._AreaStatus = params.get("AreaStatus")
        self._AreaName = params.get("AreaName")
        self._AreaKey = params.get("AreaKey")
        self._AreaRegionID = params.get("AreaRegionID")
        self._AreaRegionCode = params.get("AreaRegionCode")
        self._AreaAbbr = params.get("AreaAbbr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumInstanceInfo(AbstractModel):
    r"""Rum实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceStatus: 实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=已删除)
        :type InstanceStatus: int
        :param _AreaId: 片区Id
        :type AreaId: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _ClusterId: 集群Id
        :type ClusterId: int
        :param _InstanceDesc: 实例描述
        :type InstanceDesc: str
        :param _ChargeStatus: 计费状态(1=使用中，2=已过期，3=已销毁，4=分配中，5=分配失败)
        :type ChargeStatus: int
        :param _ChargeType: 计费类型(1=免费版，2=预付费，3=后付费)
        :type ChargeType: int
        :param _UpdatedAt: 更新时间
        :type UpdatedAt: str
        :param _DataRetentionDays: 数据保留时间(天)
        :type DataRetentionDays: int
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _InstanceType: 实例类型 1:原web相关类型 2:app端类型
        :type InstanceType: int
        """
        self._InstanceStatus = None
        self._AreaId = None
        self._Tags = None
        self._InstanceId = None
        self._ClusterId = None
        self._InstanceDesc = None
        self._ChargeStatus = None
        self._ChargeType = None
        self._UpdatedAt = None
        self._DataRetentionDays = None
        self._InstanceName = None
        self._CreatedAt = None
        self._InstanceType = None

    @property
    def InstanceStatus(self):
        r"""实例状态(1=创建中，2=运行中，3=异常，4=重启中，5=停止中，6=已停止，7=已删除)
        :rtype: int
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def AreaId(self):
        r"""片区Id
        :rtype: int
        """
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def Tags(self):
        r"""标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        r"""实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClusterId(self):
        r"""集群Id
        :rtype: int
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceDesc(self):
        r"""实例描述
        :rtype: str
        """
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc

    @property
    def ChargeStatus(self):
        r"""计费状态(1=使用中，2=已过期，3=已销毁，4=分配中，5=分配失败)
        :rtype: int
        """
        return self._ChargeStatus

    @ChargeStatus.setter
    def ChargeStatus(self, ChargeStatus):
        self._ChargeStatus = ChargeStatus

    @property
    def ChargeType(self):
        r"""计费类型(1=免费版，2=预付费，3=后付费)
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def UpdatedAt(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def DataRetentionDays(self):
        r"""数据保留时间(天)
        :rtype: int
        """
        return self._DataRetentionDays

    @DataRetentionDays.setter
    def DataRetentionDays(self, DataRetentionDays):
        self._DataRetentionDays = DataRetentionDays

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def InstanceType(self):
        r"""实例类型 1:原web相关类型 2:app端类型
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._InstanceStatus = params.get("InstanceStatus")
        self._AreaId = params.get("AreaId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._ClusterId = params.get("ClusterId")
        self._InstanceDesc = params.get("InstanceDesc")
        self._ChargeStatus = params.get("ChargeStatus")
        self._ChargeType = params.get("ChargeType")
        self._UpdatedAt = params.get("UpdatedAt")
        self._DataRetentionDays = params.get("DataRetentionDays")
        self._InstanceName = params.get("InstanceName")
        self._CreatedAt = params.get("CreatedAt")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumProject(AbstractModel):
    r"""Rum 项目信息

    """

    def __init__(self):
        r"""
        :param _Name: 项目名
        :type Name: str
        :param _Creator: 创建者 id
        :type Creator: str
        :param _InstanceID: 实例 id
        :type InstanceID: str
        :param _Type: 项目类型
        :type Type: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Repo: 项目仓库地址
        :type Repo: str
        :param _URL: 项目网址地址
        :type URL: str
        :param _Rate: 项目采样频率
        :type Rate: str
        :param _Key: 项目唯一key（长度 12 位）
        :type Key: str
        :param _EnableURLGroup: 是否开启url聚类
        :type EnableURLGroup: int
        :param _InstanceName: 实例名
        :type InstanceName: str
        :param _ID: 项目 ID
        :type ID: int
        :param _InstanceKey: 实例 key
        :type InstanceKey: str
        :param _Desc: 项目描述
        :type Desc: str
        :param _IsStar: 是否星标  1:是 0:否
        :type IsStar: int
        :param _ProjectStatus: 项目状态(1 创建中，2 运行中，3 异常，4 重启中，5 停止中，6 已停止， 7 销毁中，8 已销毁)
        :type ProjectStatus: int
        :param _AccessPoint: 日志接入点，用户忽略。
        :type AccessPoint: str
        :param _Kafka: kafka旁路配置信息
        :type Kafka: :class:`tencentcloud.rum.v20210622.models.Kafka`
        """
        self._Name = None
        self._Creator = None
        self._InstanceID = None
        self._Type = None
        self._CreateTime = None
        self._Repo = None
        self._URL = None
        self._Rate = None
        self._Key = None
        self._EnableURLGroup = None
        self._InstanceName = None
        self._ID = None
        self._InstanceKey = None
        self._Desc = None
        self._IsStar = None
        self._ProjectStatus = None
        self._AccessPoint = None
        self._Kafka = None

    @property
    def Name(self):
        r"""项目名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Creator(self):
        r"""创建者 id
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def InstanceID(self):
        r"""实例 id
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Type(self):
        r"""项目类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Repo(self):
        r"""项目仓库地址
        :rtype: str
        """
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def URL(self):
        r"""项目网址地址
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Rate(self):
        r"""项目采样频率
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Key(self):
        r"""项目唯一key（长度 12 位）
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def EnableURLGroup(self):
        r"""是否开启url聚类
        :rtype: int
        """
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def InstanceName(self):
        r"""实例名
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ID(self):
        r"""项目 ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceKey(self):
        r"""实例 key
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def Desc(self):
        r"""项目描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IsStar(self):
        r"""是否星标  1:是 0:否
        :rtype: int
        """
        return self._IsStar

    @IsStar.setter
    def IsStar(self, IsStar):
        self._IsStar = IsStar

    @property
    def ProjectStatus(self):
        r"""项目状态(1 创建中，2 运行中，3 异常，4 重启中，5 停止中，6 已停止， 7 销毁中，8 已销毁)
        :rtype: int
        """
        return self._ProjectStatus

    @ProjectStatus.setter
    def ProjectStatus(self, ProjectStatus):
        self._ProjectStatus = ProjectStatus

    @property
    def AccessPoint(self):
        r"""日志接入点，用户忽略。
        :rtype: str
        """
        return self._AccessPoint

    @AccessPoint.setter
    def AccessPoint(self, AccessPoint):
        self._AccessPoint = AccessPoint

    @property
    def Kafka(self):
        r"""kafka旁路配置信息
        :rtype: :class:`tencentcloud.rum.v20210622.models.Kafka`
        """
        return self._Kafka

    @Kafka.setter
    def Kafka(self, Kafka):
        self._Kafka = Kafka


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Creator = params.get("Creator")
        self._InstanceID = params.get("InstanceID")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._Repo = params.get("Repo")
        self._URL = params.get("URL")
        self._Rate = params.get("Rate")
        self._Key = params.get("Key")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._InstanceName = params.get("InstanceName")
        self._ID = params.get("ID")
        self._InstanceKey = params.get("InstanceKey")
        self._Desc = params.get("Desc")
        self._IsStar = params.get("IsStar")
        self._ProjectStatus = params.get("ProjectStatus")
        self._AccessPoint = params.get("AccessPoint")
        if params.get("Kafka") is not None:
            self._Kafka = Kafka()
            self._Kafka._deserialize(params.get("Kafka"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumPvInfo(AbstractModel):
    r"""rum 日志对象

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Pv: pv访问量
        :type Pv: str
        :param _CreateTime: 时间
        :type CreateTime: str
        """
        self._ProjectId = None
        self._Pv = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Pv(self):
        r"""pv访问量
        :rtype: str
        """
        return self._Pv

    @Pv.setter
    def Pv(self, Pv):
        self._Pv = Pv

    @property
    def CreateTime(self):
        r"""时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Pv = params.get("Pv")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumUvInfo(AbstractModel):
    r"""RumUv 访问量

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Uv: uv访问量
        :type Uv: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ProjectId = None
        self._Uv = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Uv(self):
        r"""uv访问量
        :rtype: str
        """
        return self._Uv

    @Uv.setter
    def Uv(self, Uv):
        self._Uv = Uv

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Uv = params.get("Uv")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreInfo(AbstractModel):
    r"""project Score分数实体

    """

    def __init__(self):
        r"""
        :param _StaticDuration: duration
        :type StaticDuration: str
        :param _PagePv: pv
        :type PagePv: str
        :param _ApiFail: 失败
        :type ApiFail: str
        :param _ApiNum: 请求
        :type ApiNum: str
        :param _StaticFail: fail
        :type StaticFail: str
        :param _ProjectID: 项目id
        :type ProjectID: int
        :param _PageUv: uv
        :type PageUv: str
        :param _ApiDuration: 请求次数
        :type ApiDuration: str
        :param _Score: 项目总分
        :type Score: str
        :param _PageError: error
        :type PageError: str
        :param _StaticNum: num
        :type StaticNum: str
        :param _RecordNum: num
        :type RecordNum: int
        :param _PageDuration: Duration
        :type PageDuration: str
        :param _CreateTime: 时间
        :type CreateTime: str
        :param _PagePerformanceScore: 页面性能评分
        :type PagePerformanceScore: str
        :param _JsErrorScore: js错误评分
        :type JsErrorScore: str
        :param _ApiPerformanceScore: API性能评分
        :type ApiPerformanceScore: str
        :param _ApiAvaliableScore: API可用性评分
        :type ApiAvaliableScore: str
        :param _StaticPerformanceScore: 静态资源性能评分
        :type StaticPerformanceScore: str
        :param _StaticAvaliableScore: 静态资源可用性评分
        :type StaticAvaliableScore: str
        """
        self._StaticDuration = None
        self._PagePv = None
        self._ApiFail = None
        self._ApiNum = None
        self._StaticFail = None
        self._ProjectID = None
        self._PageUv = None
        self._ApiDuration = None
        self._Score = None
        self._PageError = None
        self._StaticNum = None
        self._RecordNum = None
        self._PageDuration = None
        self._CreateTime = None
        self._PagePerformanceScore = None
        self._JsErrorScore = None
        self._ApiPerformanceScore = None
        self._ApiAvaliableScore = None
        self._StaticPerformanceScore = None
        self._StaticAvaliableScore = None

    @property
    def StaticDuration(self):
        r"""duration
        :rtype: str
        """
        return self._StaticDuration

    @StaticDuration.setter
    def StaticDuration(self, StaticDuration):
        self._StaticDuration = StaticDuration

    @property
    def PagePv(self):
        r"""pv
        :rtype: str
        """
        return self._PagePv

    @PagePv.setter
    def PagePv(self, PagePv):
        self._PagePv = PagePv

    @property
    def ApiFail(self):
        r"""失败
        :rtype: str
        """
        return self._ApiFail

    @ApiFail.setter
    def ApiFail(self, ApiFail):
        self._ApiFail = ApiFail

    @property
    def ApiNum(self):
        r"""请求
        :rtype: str
        """
        return self._ApiNum

    @ApiNum.setter
    def ApiNum(self, ApiNum):
        self._ApiNum = ApiNum

    @property
    def StaticFail(self):
        r"""fail
        :rtype: str
        """
        return self._StaticFail

    @StaticFail.setter
    def StaticFail(self, StaticFail):
        self._StaticFail = StaticFail

    @property
    def ProjectID(self):
        r"""项目id
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def PageUv(self):
        r"""uv
        :rtype: str
        """
        return self._PageUv

    @PageUv.setter
    def PageUv(self, PageUv):
        self._PageUv = PageUv

    @property
    def ApiDuration(self):
        r"""请求次数
        :rtype: str
        """
        return self._ApiDuration

    @ApiDuration.setter
    def ApiDuration(self, ApiDuration):
        self._ApiDuration = ApiDuration

    @property
    def Score(self):
        r"""项目总分
        :rtype: str
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def PageError(self):
        r"""error
        :rtype: str
        """
        return self._PageError

    @PageError.setter
    def PageError(self, PageError):
        self._PageError = PageError

    @property
    def StaticNum(self):
        r"""num
        :rtype: str
        """
        return self._StaticNum

    @StaticNum.setter
    def StaticNum(self, StaticNum):
        self._StaticNum = StaticNum

    @property
    def RecordNum(self):
        r"""num
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def PageDuration(self):
        r"""Duration
        :rtype: str
        """
        return self._PageDuration

    @PageDuration.setter
    def PageDuration(self, PageDuration):
        self._PageDuration = PageDuration

    @property
    def CreateTime(self):
        r"""时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PagePerformanceScore(self):
        r"""页面性能评分
        :rtype: str
        """
        return self._PagePerformanceScore

    @PagePerformanceScore.setter
    def PagePerformanceScore(self, PagePerformanceScore):
        self._PagePerformanceScore = PagePerformanceScore

    @property
    def JsErrorScore(self):
        r"""js错误评分
        :rtype: str
        """
        return self._JsErrorScore

    @JsErrorScore.setter
    def JsErrorScore(self, JsErrorScore):
        self._JsErrorScore = JsErrorScore

    @property
    def ApiPerformanceScore(self):
        r"""API性能评分
        :rtype: str
        """
        return self._ApiPerformanceScore

    @ApiPerformanceScore.setter
    def ApiPerformanceScore(self, ApiPerformanceScore):
        self._ApiPerformanceScore = ApiPerformanceScore

    @property
    def ApiAvaliableScore(self):
        r"""API可用性评分
        :rtype: str
        """
        return self._ApiAvaliableScore

    @ApiAvaliableScore.setter
    def ApiAvaliableScore(self, ApiAvaliableScore):
        self._ApiAvaliableScore = ApiAvaliableScore

    @property
    def StaticPerformanceScore(self):
        r"""静态资源性能评分
        :rtype: str
        """
        return self._StaticPerformanceScore

    @StaticPerformanceScore.setter
    def StaticPerformanceScore(self, StaticPerformanceScore):
        self._StaticPerformanceScore = StaticPerformanceScore

    @property
    def StaticAvaliableScore(self):
        r"""静态资源可用性评分
        :rtype: str
        """
        return self._StaticAvaliableScore

    @StaticAvaliableScore.setter
    def StaticAvaliableScore(self, StaticAvaliableScore):
        self._StaticAvaliableScore = StaticAvaliableScore


    def _deserialize(self, params):
        self._StaticDuration = params.get("StaticDuration")
        self._PagePv = params.get("PagePv")
        self._ApiFail = params.get("ApiFail")
        self._ApiNum = params.get("ApiNum")
        self._StaticFail = params.get("StaticFail")
        self._ProjectID = params.get("ProjectID")
        self._PageUv = params.get("PageUv")
        self._ApiDuration = params.get("ApiDuration")
        self._Score = params.get("Score")
        self._PageError = params.get("PageError")
        self._StaticNum = params.get("StaticNum")
        self._RecordNum = params.get("RecordNum")
        self._PageDuration = params.get("PageDuration")
        self._CreateTime = params.get("CreateTime")
        self._PagePerformanceScore = params.get("PagePerformanceScore")
        self._JsErrorScore = params.get("JsErrorScore")
        self._ApiPerformanceScore = params.get("ApiPerformanceScore")
        self._ApiAvaliableScore = params.get("ApiAvaliableScore")
        self._StaticPerformanceScore = params.get("StaticPerformanceScore")
        self._StaticAvaliableScore = params.get("StaticAvaliableScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreInfoV2(AbstractModel):
    r"""project Score分数实体

    """

    def __init__(self):
        r"""
        :param _ProjectID: <p>项目id</p>
        :type ProjectID: int
        :param _Score: <p>项目总分</p>
        :type Score: float
        :param _ApiPerformanceScore: <p>API性能评分</p>
        :type ApiPerformanceScore: float
        :param _ApiAvailableScore: <p>API可用性评分</p>
        :type ApiAvailableScore: float
        :param _ApiNum: <p>API调用总数</p>
        :type ApiNum: int
        :param _ApiFail: <p>API失败次数</p>
        :type ApiFail: int
        :param _ApiDuration: <p>API平均持续时间</p>
        :type ApiDuration: float
        :param _PagePerformanceScore: <p>页面性能评分</p>
        :type PagePerformanceScore: float
        :param _PagePv: <p>页面浏览量</p>
        :type PagePv: int
        :param _PageUv: <p>独立访客数</p>
        :type PageUv: int
        :param _PageError: <p>页面错误数</p>
        :type PageError: int
        :param _PageDuration: <p>首屏时间</p>
        :type PageDuration: float
        :param _PageLCP: <p>平均 LCP</p>
        :type PageLCP: float
        :param _PageFID: <p>平均 FID</p>
        :type PageFID: float
        :param _PageCLS: <p>平均 CLS</p>
        :type PageCLS: float
        :param _PageFCP: <p>平均 FCP</p>
        :type PageFCP: float
        :param _PageINP: <p>平均 INP</p>
        :type PageINP: float
        :param _JsErrorScore: <p>JavaScript错误评分</p>
        :type JsErrorScore: float
        :param _StaticAvailableScore: <p>静态资源可用性评分</p>
        :type StaticAvailableScore: float
        :param _StaticPerformanceScore: <p>静态资源性能评分</p>
        :type StaticPerformanceScore: float
        :param _StaticNum: <p>静态资源请求总数</p>
        :type StaticNum: int
        :param _StaticFail: <p>静态资源加载失败数</p>
        :type StaticFail: int
        :param _StaticDuration: <p>静态资源加载时间</p>
        :type StaticDuration: float
        :param _Exclusion: <p>忽略的配置项</p>
        :type Exclusion: str
        """
        self._ProjectID = None
        self._Score = None
        self._ApiPerformanceScore = None
        self._ApiAvailableScore = None
        self._ApiNum = None
        self._ApiFail = None
        self._ApiDuration = None
        self._PagePerformanceScore = None
        self._PagePv = None
        self._PageUv = None
        self._PageError = None
        self._PageDuration = None
        self._PageLCP = None
        self._PageFID = None
        self._PageCLS = None
        self._PageFCP = None
        self._PageINP = None
        self._JsErrorScore = None
        self._StaticAvailableScore = None
        self._StaticPerformanceScore = None
        self._StaticNum = None
        self._StaticFail = None
        self._StaticDuration = None
        self._Exclusion = None

    @property
    def ProjectID(self):
        r"""<p>项目id</p>
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def Score(self):
        r"""<p>项目总分</p>
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def ApiPerformanceScore(self):
        r"""<p>API性能评分</p>
        :rtype: float
        """
        return self._ApiPerformanceScore

    @ApiPerformanceScore.setter
    def ApiPerformanceScore(self, ApiPerformanceScore):
        self._ApiPerformanceScore = ApiPerformanceScore

    @property
    def ApiAvailableScore(self):
        r"""<p>API可用性评分</p>
        :rtype: float
        """
        return self._ApiAvailableScore

    @ApiAvailableScore.setter
    def ApiAvailableScore(self, ApiAvailableScore):
        self._ApiAvailableScore = ApiAvailableScore

    @property
    def ApiNum(self):
        r"""<p>API调用总数</p>
        :rtype: int
        """
        return self._ApiNum

    @ApiNum.setter
    def ApiNum(self, ApiNum):
        self._ApiNum = ApiNum

    @property
    def ApiFail(self):
        r"""<p>API失败次数</p>
        :rtype: int
        """
        return self._ApiFail

    @ApiFail.setter
    def ApiFail(self, ApiFail):
        self._ApiFail = ApiFail

    @property
    def ApiDuration(self):
        r"""<p>API平均持续时间</p>
        :rtype: float
        """
        return self._ApiDuration

    @ApiDuration.setter
    def ApiDuration(self, ApiDuration):
        self._ApiDuration = ApiDuration

    @property
    def PagePerformanceScore(self):
        r"""<p>页面性能评分</p>
        :rtype: float
        """
        return self._PagePerformanceScore

    @PagePerformanceScore.setter
    def PagePerformanceScore(self, PagePerformanceScore):
        self._PagePerformanceScore = PagePerformanceScore

    @property
    def PagePv(self):
        r"""<p>页面浏览量</p>
        :rtype: int
        """
        return self._PagePv

    @PagePv.setter
    def PagePv(self, PagePv):
        self._PagePv = PagePv

    @property
    def PageUv(self):
        r"""<p>独立访客数</p>
        :rtype: int
        """
        return self._PageUv

    @PageUv.setter
    def PageUv(self, PageUv):
        self._PageUv = PageUv

    @property
    def PageError(self):
        r"""<p>页面错误数</p>
        :rtype: int
        """
        return self._PageError

    @PageError.setter
    def PageError(self, PageError):
        self._PageError = PageError

    @property
    def PageDuration(self):
        r"""<p>首屏时间</p>
        :rtype: float
        """
        return self._PageDuration

    @PageDuration.setter
    def PageDuration(self, PageDuration):
        self._PageDuration = PageDuration

    @property
    def PageLCP(self):
        r"""<p>平均 LCP</p>
        :rtype: float
        """
        return self._PageLCP

    @PageLCP.setter
    def PageLCP(self, PageLCP):
        self._PageLCP = PageLCP

    @property
    def PageFID(self):
        r"""<p>平均 FID</p>
        :rtype: float
        """
        return self._PageFID

    @PageFID.setter
    def PageFID(self, PageFID):
        self._PageFID = PageFID

    @property
    def PageCLS(self):
        r"""<p>平均 CLS</p>
        :rtype: float
        """
        return self._PageCLS

    @PageCLS.setter
    def PageCLS(self, PageCLS):
        self._PageCLS = PageCLS

    @property
    def PageFCP(self):
        r"""<p>平均 FCP</p>
        :rtype: float
        """
        return self._PageFCP

    @PageFCP.setter
    def PageFCP(self, PageFCP):
        self._PageFCP = PageFCP

    @property
    def PageINP(self):
        r"""<p>平均 INP</p>
        :rtype: float
        """
        return self._PageINP

    @PageINP.setter
    def PageINP(self, PageINP):
        self._PageINP = PageINP

    @property
    def JsErrorScore(self):
        r"""<p>JavaScript错误评分</p>
        :rtype: float
        """
        return self._JsErrorScore

    @JsErrorScore.setter
    def JsErrorScore(self, JsErrorScore):
        self._JsErrorScore = JsErrorScore

    @property
    def StaticAvailableScore(self):
        r"""<p>静态资源可用性评分</p>
        :rtype: float
        """
        return self._StaticAvailableScore

    @StaticAvailableScore.setter
    def StaticAvailableScore(self, StaticAvailableScore):
        self._StaticAvailableScore = StaticAvailableScore

    @property
    def StaticPerformanceScore(self):
        r"""<p>静态资源性能评分</p>
        :rtype: float
        """
        return self._StaticPerformanceScore

    @StaticPerformanceScore.setter
    def StaticPerformanceScore(self, StaticPerformanceScore):
        self._StaticPerformanceScore = StaticPerformanceScore

    @property
    def StaticNum(self):
        r"""<p>静态资源请求总数</p>
        :rtype: int
        """
        return self._StaticNum

    @StaticNum.setter
    def StaticNum(self, StaticNum):
        self._StaticNum = StaticNum

    @property
    def StaticFail(self):
        r"""<p>静态资源加载失败数</p>
        :rtype: int
        """
        return self._StaticFail

    @StaticFail.setter
    def StaticFail(self, StaticFail):
        self._StaticFail = StaticFail

    @property
    def StaticDuration(self):
        r"""<p>静态资源加载时间</p>
        :rtype: float
        """
        return self._StaticDuration

    @StaticDuration.setter
    def StaticDuration(self, StaticDuration):
        self._StaticDuration = StaticDuration

    @property
    def Exclusion(self):
        r"""<p>忽略的配置项</p>
        :rtype: str
        """
        return self._Exclusion

    @Exclusion.setter
    def Exclusion(self, Exclusion):
        self._Exclusion = Exclusion


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._Score = params.get("Score")
        self._ApiPerformanceScore = params.get("ApiPerformanceScore")
        self._ApiAvailableScore = params.get("ApiAvailableScore")
        self._ApiNum = params.get("ApiNum")
        self._ApiFail = params.get("ApiFail")
        self._ApiDuration = params.get("ApiDuration")
        self._PagePerformanceScore = params.get("PagePerformanceScore")
        self._PagePv = params.get("PagePv")
        self._PageUv = params.get("PageUv")
        self._PageError = params.get("PageError")
        self._PageDuration = params.get("PageDuration")
        self._PageLCP = params.get("PageLCP")
        self._PageFID = params.get("PageFID")
        self._PageCLS = params.get("PageCLS")
        self._PageFCP = params.get("PageFCP")
        self._PageINP = params.get("PageINP")
        self._JsErrorScore = params.get("JsErrorScore")
        self._StaticAvailableScore = params.get("StaticAvailableScore")
        self._StaticPerformanceScore = params.get("StaticPerformanceScore")
        self._StaticNum = params.get("StaticNum")
        self._StaticFail = params.get("StaticFail")
        self._StaticDuration = params.get("StaticDuration")
        self._Exclusion = params.get("Exclusion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceRequest(AbstractModel):
    r"""StopInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要停止的实例id
        :type InstanceId: str
        :param _IsModifyAll: 修改是否包括白名单
        :type IsModifyAll: bool
        """
        self._InstanceId = None
        self._IsModifyAll = None

    @property
    def InstanceId(self):
        r"""需要停止的实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IsModifyAll(self):
        r"""修改是否包括白名单
        :rtype: bool
        """
        return self._IsModifyAll

    @IsModifyAll.setter
    def IsModifyAll(self, IsModifyAll):
        self._IsModifyAll = IsModifyAll


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IsModifyAll = params.get("IsModifyAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceResponse(AbstractModel):
    r"""StopInstance返回参数结构体

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


class StopProjectRequest(AbstractModel):
    r"""StopProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目 id
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        r"""项目 id
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopProjectResponse(AbstractModel):
    r"""StopProject返回参数结构体

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


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签key
        :type Key: str
        :param _Value: 标签value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签value
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Whitelist(AbstractModel):
    r"""白名单

    """

    def __init__(self):
        r"""
        :param _Remark: 备注
        :type Remark: str
        :param _InstanceID: 实例ID
        :type InstanceID: str
        :param _Ttl: 截止时间
        :type Ttl: str
        :param _ID: 白名单自增ID
        :type ID: str
        :param _WhitelistUin: 业务唯一标识
        :type WhitelistUin: str
        :param _CreateUser: 创建者ID
        :type CreateUser: str
        :param _Aid: aid标识
        :type Aid: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._Remark = None
        self._InstanceID = None
        self._Ttl = None
        self._ID = None
        self._WhitelistUin = None
        self._CreateUser = None
        self._Aid = None
        self._CreateTime = None

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceID(self):
        r"""实例ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Ttl(self):
        r"""截止时间
        :rtype: str
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def ID(self):
        r"""白名单自增ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def WhitelistUin(self):
        r"""业务唯一标识
        :rtype: str
        """
        return self._WhitelistUin

    @WhitelistUin.setter
    def WhitelistUin(self, WhitelistUin):
        self._WhitelistUin = WhitelistUin

    @property
    def CreateUser(self):
        r"""创建者ID
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def Aid(self):
        r"""aid标识
        :rtype: str
        """
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Remark = params.get("Remark")
        self._InstanceID = params.get("InstanceID")
        self._Ttl = params.get("Ttl")
        self._ID = params.get("ID")
        self._WhitelistUin = params.get("WhitelistUin")
        self._CreateUser = params.get("CreateUser")
        self._Aid = params.get("Aid")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        