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


class CreateNoticeContentTmplRequest(AbstractModel):
    r"""CreateNoticeContentTmpl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplName: 模板名称
        :type TmplName: str
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _TmplContents: 模板内容
        :type TmplContents: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        :param _TmplLanguage: 模板语言 en/zh
        :type TmplLanguage: str
        """
        self._TmplName = None
        self._MonitorType = None
        self._TmplContents = None
        self._TmplLanguage = None

    @property
    def TmplName(self):
        r"""模板名称
        :rtype: str
        """
        return self._TmplName

    @TmplName.setter
    def TmplName(self, TmplName):
        self._TmplName = TmplName

    @property
    def MonitorType(self):
        r"""监控类型
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def TmplContents(self):
        r"""模板内容
        :rtype: :class:`tencentcloud.monitor.v20230616.models.NoticeContentTmplItem`
        """
        return self._TmplContents

    @TmplContents.setter
    def TmplContents(self, TmplContents):
        self._TmplContents = TmplContents

    @property
    def TmplLanguage(self):
        r"""模板语言 en/zh
        :rtype: str
        """
        return self._TmplLanguage

    @TmplLanguage.setter
    def TmplLanguage(self, TmplLanguage):
        self._TmplLanguage = TmplLanguage


    def _deserialize(self, params):
        self._TmplName = params.get("TmplName")
        self._MonitorType = params.get("MonitorType")
        if params.get("TmplContents") is not None:
            self._TmplContents = NoticeContentTmplItem()
            self._TmplContents._deserialize(params.get("TmplContents"))
        self._TmplLanguage = params.get("TmplLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNoticeContentTmplResponse(AbstractModel):
    r"""CreateNoticeContentTmpl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TmplID: 自定义内容模板ID
        :type TmplID: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TmplID = None
        self._RequestId = None

    @property
    def TmplID(self):
        r"""自定义内容模板ID
        :rtype: str
        """
        return self._TmplID

    @TmplID.setter
    def TmplID(self, TmplID):
        self._TmplID = TmplID

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
        self._TmplID = params.get("TmplID")
        self._RequestId = params.get("RequestId")


class DescribeAlarmNotifyHistoriesRequest(AbstractModel):
    r"""DescribeAlarmNotifyHistories请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorType: 监控类型
        :type MonitorType: str
        :param _QueryBaseTime: 起始时间点，unix秒级时间戳
        :type QueryBaseTime: int
        :param _QueryBeforeSeconds: 从 QueryBaseTime 开始，需要查询往前多久的时间，单位秒
        :type QueryBeforeSeconds: int
        :param _PageParams: 分页参数
        :type PageParams: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        :param _Namespace: 当监控类型为 MT_QCE 时候需要填写，归属的命名空间
        :type Namespace: str
        :param _ModelName: 当监控类型为 MT_QCE 时候需要填写， 告警策略类型
        :type ModelName: str
        :param _PolicyId: 查询某个策略的通知历史
        :type PolicyId: str
        """
        self._MonitorType = None
        self._QueryBaseTime = None
        self._QueryBeforeSeconds = None
        self._PageParams = None
        self._Namespace = None
        self._ModelName = None
        self._PolicyId = None

    @property
    def MonitorType(self):
        r"""监控类型
        :rtype: str
        """
        return self._MonitorType

    @MonitorType.setter
    def MonitorType(self, MonitorType):
        self._MonitorType = MonitorType

    @property
    def QueryBaseTime(self):
        r"""起始时间点，unix秒级时间戳
        :rtype: int
        """
        return self._QueryBaseTime

    @QueryBaseTime.setter
    def QueryBaseTime(self, QueryBaseTime):
        self._QueryBaseTime = QueryBaseTime

    @property
    def QueryBeforeSeconds(self):
        r"""从 QueryBaseTime 开始，需要查询往前多久的时间，单位秒
        :rtype: int
        """
        return self._QueryBeforeSeconds

    @QueryBeforeSeconds.setter
    def QueryBeforeSeconds(self, QueryBeforeSeconds):
        self._QueryBeforeSeconds = QueryBeforeSeconds

    @property
    def PageParams(self):
        r"""分页参数
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PageByNoParams`
        """
        return self._PageParams

    @PageParams.setter
    def PageParams(self, PageParams):
        self._PageParams = PageParams

    @property
    def Namespace(self):
        r"""当监控类型为 MT_QCE 时候需要填写，归属的命名空间
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ModelName(self):
        r"""当监控类型为 MT_QCE 时候需要填写， 告警策略类型
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def PolicyId(self):
        r"""查询某个策略的通知历史
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._MonitorType = params.get("MonitorType")
        self._QueryBaseTime = params.get("QueryBaseTime")
        self._QueryBeforeSeconds = params.get("QueryBeforeSeconds")
        if params.get("PageParams") is not None:
            self._PageParams = PageByNoParams()
            self._PageParams._deserialize(params.get("PageParams"))
        self._Namespace = params.get("Namespace")
        self._ModelName = params.get("ModelName")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAlarmNotifyHistoriesResponse(AbstractModel):
    r"""DescribeAlarmNotifyHistories返回参数结构体

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


class DingDingRobotNoticeTmpl(AbstractModel):
    r"""钉钉机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        :param _TitleTmpl: 标题模板
        :type TitleTmpl: str
        """
        self._ContentTmpl = None
        self._TitleTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl

    @property
    def TitleTmpl(self):
        r"""标题模板
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DingDingRobotNoticeTmplMatcher(AbstractModel):
    r"""钉钉机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.DingDingRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.DingDingRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = DingDingRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeiShuRobotNoticeTmpl(AbstractModel):
    r"""飞书机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        :param _TitleTmpl: 标题模板
        :type TitleTmpl: str
        """
        self._ContentTmpl = None
        self._TitleTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl

    @property
    def TitleTmpl(self):
        r"""标题模板
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FeiShuRobotNoticeTmplMatcher(AbstractModel):
    r"""飞书机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.FeiShuRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.FeiShuRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = FeiShuRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NoticeContentTmplItem(AbstractModel):
    r"""内容通知模板元素

    """

    def __init__(self):
        r"""
        :param _QCloudYehe: 官网通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :type QCloudYehe: list of QCloudYeheNoticeTmplMatcher
        :param _WeWorkRobot: 企业微信机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WeWorkRobot: list of WeWorkRobotNoticeTmplMatcher
        :param _DingDingRobot: 钉钉机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DingDingRobot: list of DingDingRobotNoticeTmplMatcher
        :param _FeiShuRobot: 飞书机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FeiShuRobot: list of FeiShuRobotNoticeTmplMatcher
        :param _Webhook: 自定义Webhook通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Webhook: list of WebhookNoticeTmplMatcher
        :param _TeamsRobot: Teams机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TeamsRobot: list of TeamsRobotNoticeTmplMatcher
        :param _PagerDutyRobot: PagerDutyRobot机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PagerDutyRobot: list of PagerDutyRobotNoticeTmplMatcher
        """
        self._QCloudYehe = None
        self._WeWorkRobot = None
        self._DingDingRobot = None
        self._FeiShuRobot = None
        self._Webhook = None
        self._TeamsRobot = None
        self._PagerDutyRobot = None

    @property
    def QCloudYehe(self):
        r"""官网通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of QCloudYeheNoticeTmplMatcher
        """
        return self._QCloudYehe

    @QCloudYehe.setter
    def QCloudYehe(self, QCloudYehe):
        self._QCloudYehe = QCloudYehe

    @property
    def WeWorkRobot(self):
        r"""企业微信机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WeWorkRobotNoticeTmplMatcher
        """
        return self._WeWorkRobot

    @WeWorkRobot.setter
    def WeWorkRobot(self, WeWorkRobot):
        self._WeWorkRobot = WeWorkRobot

    @property
    def DingDingRobot(self):
        r"""钉钉机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DingDingRobotNoticeTmplMatcher
        """
        return self._DingDingRobot

    @DingDingRobot.setter
    def DingDingRobot(self, DingDingRobot):
        self._DingDingRobot = DingDingRobot

    @property
    def FeiShuRobot(self):
        r"""飞书机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of FeiShuRobotNoticeTmplMatcher
        """
        return self._FeiShuRobot

    @FeiShuRobot.setter
    def FeiShuRobot(self, FeiShuRobot):
        self._FeiShuRobot = FeiShuRobot

    @property
    def Webhook(self):
        r"""自定义Webhook通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WebhookNoticeTmplMatcher
        """
        return self._Webhook

    @Webhook.setter
    def Webhook(self, Webhook):
        self._Webhook = Webhook

    @property
    def TeamsRobot(self):
        r"""Teams机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TeamsRobotNoticeTmplMatcher
        """
        return self._TeamsRobot

    @TeamsRobot.setter
    def TeamsRobot(self, TeamsRobot):
        self._TeamsRobot = TeamsRobot

    @property
    def PagerDutyRobot(self):
        r"""PagerDutyRobot机器人通知渠道配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PagerDutyRobotNoticeTmplMatcher
        """
        return self._PagerDutyRobot

    @PagerDutyRobot.setter
    def PagerDutyRobot(self, PagerDutyRobot):
        self._PagerDutyRobot = PagerDutyRobot


    def _deserialize(self, params):
        if params.get("QCloudYehe") is not None:
            self._QCloudYehe = []
            for item in params.get("QCloudYehe"):
                obj = QCloudYeheNoticeTmplMatcher()
                obj._deserialize(item)
                self._QCloudYehe.append(obj)
        if params.get("WeWorkRobot") is not None:
            self._WeWorkRobot = []
            for item in params.get("WeWorkRobot"):
                obj = WeWorkRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._WeWorkRobot.append(obj)
        if params.get("DingDingRobot") is not None:
            self._DingDingRobot = []
            for item in params.get("DingDingRobot"):
                obj = DingDingRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._DingDingRobot.append(obj)
        if params.get("FeiShuRobot") is not None:
            self._FeiShuRobot = []
            for item in params.get("FeiShuRobot"):
                obj = FeiShuRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._FeiShuRobot.append(obj)
        if params.get("Webhook") is not None:
            self._Webhook = []
            for item in params.get("Webhook"):
                obj = WebhookNoticeTmplMatcher()
                obj._deserialize(item)
                self._Webhook.append(obj)
        if params.get("TeamsRobot") is not None:
            self._TeamsRobot = []
            for item in params.get("TeamsRobot"):
                obj = TeamsRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._TeamsRobot.append(obj)
        if params.get("PagerDutyRobot") is not None:
            self._PagerDutyRobot = []
            for item in params.get("PagerDutyRobot"):
                obj = PagerDutyRobotNoticeTmplMatcher()
                obj._deserialize(item)
                self._PagerDutyRobot.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageByNoParams(AbstractModel):
    r"""分页请求参数

    """

    def __init__(self):
        r"""
        :param _PerPage: 每个分页的数量是多少
注意：此字段可能返回 null，表示取不到有效值。
        :type PerPage: int
        :param _PageNo: 第几个分页，从1开始
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNo: str
        """
        self._PerPage = None
        self._PageNo = None

    @property
    def PerPage(self):
        r"""每个分页的数量是多少
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PerPage

    @PerPage.setter
    def PerPage(self, PerPage):
        self._PerPage = PerPage

    @property
    def PageNo(self):
        r"""第几个分页，从1开始
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo


    def _deserialize(self, params):
        self._PerPage = params.get("PerPage")
        self._PageNo = params.get("PageNo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PagerDutyRobotNoticeTmpl(AbstractModel):
    r"""告警通知自定义PagerDutyRobot内容模板

    """

    def __init__(self):
        r"""
        :param _Body: 请求体模板 仅支持json
        :type Body: str
        :param _Headers: 请求头 暂时未支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of PagerDutyRobotNoticeTmplHeader
        :param _TitleTmpl: 标题模板
        :type TitleTmpl: str
        """
        self._Body = None
        self._Headers = None
        self._TitleTmpl = None

    @property
    def Body(self):
        r"""请求体模板 仅支持json
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Headers(self):
        r"""请求头 暂时未支持
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PagerDutyRobotNoticeTmplHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def TitleTmpl(self):
        r"""标题模板
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._Body = params.get("Body")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = PagerDutyRobotNoticeTmplHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PagerDutyRobotNoticeTmplHeader(AbstractModel):
    r"""告警通知自定义PagerDutyRobot模板中的请求体头部描述

    """

    def __init__(self):
        r"""
        :param _Key: http请求中header的key
        :type Key: str
        :param _Values: http请求中header的value
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        r"""http请求中header的key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""http请求中header的value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PagerDutyRobotNoticeTmplMatcher(AbstractModel):
    r"""告警通知自定义PagerDutyRobot的通知内容模板匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 自定义PagerDutyRobot内容模板
        :type Template: :class:`tencentcloud.monitor.v20230616.models.PagerDutyRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""自定义PagerDutyRobot内容模板
        :rtype: :class:`tencentcloud.monitor.v20230616.models.PagerDutyRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = PagerDutyRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheNoticeTmpl(AbstractModel):
    r"""官网通知内容模板

    """

    def __init__(self):
        r"""
        :param _Email: 邮件通知渠道
        :type Email: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _QYWX: 企业微信通知渠道
        :type QYWX: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _SMS: 短信通知渠道
        :type SMS: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _Voice: 语音通知渠道
        :type Voice: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _WeChat: 微信通知渠道
        :type WeChat: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheWeChatNoticeTmplItem`
        :param _Site: 站内信通知渠道
        :type Site: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        :param _Andon: 安灯通知渠道
        :type Andon: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        self._Email = None
        self._QYWX = None
        self._SMS = None
        self._Voice = None
        self._WeChat = None
        self._Site = None
        self._Andon = None

    @property
    def Email(self):
        r"""邮件通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def QYWX(self):
        r"""企业微信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._QYWX

    @QYWX.setter
    def QYWX(self, QYWX):
        self._QYWX = QYWX

    @property
    def SMS(self):
        r"""短信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._SMS

    @SMS.setter
    def SMS(self, SMS):
        self._SMS = SMS

    @property
    def Voice(self):
        r"""语音通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def WeChat(self):
        r"""微信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheWeChatNoticeTmplItem`
        """
        return self._WeChat

    @WeChat.setter
    def WeChat(self, WeChat):
        self._WeChat = WeChat

    @property
    def Site(self):
        r"""站内信通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def Andon(self):
        r"""安灯通知渠道
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmplItem`
        """
        return self._Andon

    @Andon.setter
    def Andon(self, Andon):
        self._Andon = Andon


    def _deserialize(self, params):
        if params.get("Email") is not None:
            self._Email = QCloudYeheNoticeTmplItem()
            self._Email._deserialize(params.get("Email"))
        if params.get("QYWX") is not None:
            self._QYWX = QCloudYeheNoticeTmplItem()
            self._QYWX._deserialize(params.get("QYWX"))
        if params.get("SMS") is not None:
            self._SMS = QCloudYeheNoticeTmplItem()
            self._SMS._deserialize(params.get("SMS"))
        if params.get("Voice") is not None:
            self._Voice = QCloudYeheNoticeTmplItem()
            self._Voice._deserialize(params.get("Voice"))
        if params.get("WeChat") is not None:
            self._WeChat = QCloudYeheWeChatNoticeTmplItem()
            self._WeChat._deserialize(params.get("WeChat"))
        if params.get("Site") is not None:
            self._Site = QCloudYeheNoticeTmplItem()
            self._Site._deserialize(params.get("Site"))
        if params.get("Andon") is not None:
            self._Andon = QCloudYeheNoticeTmplItem()
            self._Andon._deserialize(params.get("Andon"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheNoticeTmplItem(AbstractModel):
    r"""官网通知内容模板元素

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        :param _TitleTmpl: 标题
        :type TitleTmpl: str
        """
        self._ContentTmpl = None
        self._TitleTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl

    @property
    def TitleTmpl(self):
        r"""标题
        :rtype: str
        """
        return self._TitleTmpl

    @TitleTmpl.setter
    def TitleTmpl(self, TitleTmpl):
        self._TitleTmpl = TitleTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        self._TitleTmpl = params.get("TitleTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheNoticeTmplMatcher(AbstractModel):
    r"""官网内容通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.QCloudYeheNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = QCloudYeheNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QCloudYeheWeChatNoticeTmplItem(AbstractModel):
    r"""官网通知内容模板元素

    """

    def __init__(self):
        r"""
        :param _AlarmContentTmpl: 告警内容模板
        :type AlarmContentTmpl: str
        :param _AlarmObjectTmpl: 告警对象模板
        :type AlarmObjectTmpl: str
        :param _AlarmRegionTmpl: 告警地域模板
        :type AlarmRegionTmpl: str
        :param _AlarmTimeTmpl: 告警时间模板
        :type AlarmTimeTmpl: str
        """
        self._AlarmContentTmpl = None
        self._AlarmObjectTmpl = None
        self._AlarmRegionTmpl = None
        self._AlarmTimeTmpl = None

    @property
    def AlarmContentTmpl(self):
        r"""告警内容模板
        :rtype: str
        """
        return self._AlarmContentTmpl

    @AlarmContentTmpl.setter
    def AlarmContentTmpl(self, AlarmContentTmpl):
        self._AlarmContentTmpl = AlarmContentTmpl

    @property
    def AlarmObjectTmpl(self):
        r"""告警对象模板
        :rtype: str
        """
        return self._AlarmObjectTmpl

    @AlarmObjectTmpl.setter
    def AlarmObjectTmpl(self, AlarmObjectTmpl):
        self._AlarmObjectTmpl = AlarmObjectTmpl

    @property
    def AlarmRegionTmpl(self):
        r"""告警地域模板
        :rtype: str
        """
        return self._AlarmRegionTmpl

    @AlarmRegionTmpl.setter
    def AlarmRegionTmpl(self, AlarmRegionTmpl):
        self._AlarmRegionTmpl = AlarmRegionTmpl

    @property
    def AlarmTimeTmpl(self):
        r"""告警时间模板
        :rtype: str
        """
        return self._AlarmTimeTmpl

    @AlarmTimeTmpl.setter
    def AlarmTimeTmpl(self, AlarmTimeTmpl):
        self._AlarmTimeTmpl = AlarmTimeTmpl


    def _deserialize(self, params):
        self._AlarmContentTmpl = params.get("AlarmContentTmpl")
        self._AlarmObjectTmpl = params.get("AlarmObjectTmpl")
        self._AlarmRegionTmpl = params.get("AlarmRegionTmpl")
        self._AlarmTimeTmpl = params.get("AlarmTimeTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamsRobotNoticeTmpl(AbstractModel):
    r"""企业微信机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        """
        self._ContentTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TeamsRobotNoticeTmplMatcher(AbstractModel):
    r"""企业微信机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.TeamsRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.TeamsRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = TeamsRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeWorkRobotNoticeTmpl(AbstractModel):
    r"""企业微信机器人内容模板配置

    """

    def __init__(self):
        r"""
        :param _ContentTmpl: 内容模板
        :type ContentTmpl: str
        """
        self._ContentTmpl = None

    @property
    def ContentTmpl(self):
        r"""内容模板
        :rtype: str
        """
        return self._ContentTmpl

    @ContentTmpl.setter
    def ContentTmpl(self, ContentTmpl):
        self._ContentTmpl = ContentTmpl


    def _deserialize(self, params):
        self._ContentTmpl = params.get("ContentTmpl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeWorkRobotNoticeTmplMatcher(AbstractModel):
    r"""企业微信机器人通知模板的匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 模板配置
        :type Template: :class:`tencentcloud.monitor.v20230616.models.WeWorkRobotNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid;
Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""模板配置
        :rtype: :class:`tencentcloud.monitor.v20230616.models.WeWorkRobotNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = WeWorkRobotNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookNoticeTmpl(AbstractModel):
    r"""告警通知自定义Webhook内容模板

    """

    def __init__(self):
        r"""
        :param _Body: 请求体
        :type Body: str
        :param _BodyContentType: 请求体的类型，非必填、默认为JSON
注意：此字段可能返回 null，表示取不到有效值。
        :type BodyContentType: str
        :param _Headers: 请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of WebhookNoticeTmplHeader
        """
        self._Body = None
        self._BodyContentType = None
        self._Headers = None

    @property
    def Body(self):
        r"""请求体
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def BodyContentType(self):
        r"""请求体的类型，非必填、默认为JSON
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BodyContentType

    @BodyContentType.setter
    def BodyContentType(self, BodyContentType):
        self._BodyContentType = BodyContentType

    @property
    def Headers(self):
        r"""请求头
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WebhookNoticeTmplHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._BodyContentType = params.get("BodyContentType")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = WebhookNoticeTmplHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookNoticeTmplHeader(AbstractModel):
    r"""告警通知自定义Webhook模板中的请求体头部描述

    """

    def __init__(self):
        r"""
        :param _Key: http请求中header的key
        :type Key: str
        :param _Values: http请求中header的value
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        r"""http请求中header的key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""http请求中header的value
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebhookNoticeTmplMatcher(AbstractModel):
    r"""告警通知自定义Webhook的通知内容模板匹配器

    """

    def __init__(self):
        r"""
        :param _MatchingStatus: 匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :type MatchingStatus: list of str
        :param _Template: 自定义Webhook内容模板
        :type Template: :class:`tencentcloud.monitor.v20230616.models.WebhookNoticeTmpl`
        """
        self._MatchingStatus = None
        self._Template = None

    @property
    def MatchingStatus(self):
        r"""匹配状态 Invalid; Trigger 告警触发; Recovery 告警恢复
        :rtype: list of str
        """
        return self._MatchingStatus

    @MatchingStatus.setter
    def MatchingStatus(self, MatchingStatus):
        self._MatchingStatus = MatchingStatus

    @property
    def Template(self):
        r"""自定义Webhook内容模板
        :rtype: :class:`tencentcloud.monitor.v20230616.models.WebhookNoticeTmpl`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template


    def _deserialize(self, params):
        self._MatchingStatus = params.get("MatchingStatus")
        if params.get("Template") is not None:
            self._Template = WebhookNoticeTmpl()
            self._Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        