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


class Album(AbstractModel):
    r"""Album

    """

    def __init__(self):
        r"""
        :param _AlbumName: 专辑名
        :type AlbumName: str
        :param _ImagePathMap: 专辑图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePathMap: list of ImagePath
        """
        self._AlbumName = None
        self._ImagePathMap = None

    @property
    def AlbumName(self):
        r"""专辑名
        :rtype: str
        """
        return self._AlbumName

    @AlbumName.setter
    def AlbumName(self, AlbumName):
        self._AlbumName = AlbumName

    @property
    def ImagePathMap(self):
        r"""专辑图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImagePath
        """
        return self._ImagePathMap

    @ImagePathMap.setter
    def ImagePathMap(self, ImagePathMap):
        self._ImagePathMap = ImagePathMap


    def _deserialize(self, params):
        self._AlbumName = params.get("AlbumName")
        if params.get("ImagePathMap") is not None:
            self._ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self._ImagePathMap.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationLicenseInput(AbstractModel):
    r"""用户license基础信息

    """

    def __init__(self):
        r"""
        :param _AppName: 应用名称，注：后面三个字段AndroidPackageName、IOSBundleId、PcIdentifier，三者选填一个
        :type AppName: str
        :param _AndroidPackageName: app的安卓包名
        :type AndroidPackageName: str
        :param _IOSBundleId: app的IOS的BundleId名
        :type IOSBundleId: str
        :param _PcIdentifier: PC标识名
        :type PcIdentifier: str
        """
        self._AppName = None
        self._AndroidPackageName = None
        self._IOSBundleId = None
        self._PcIdentifier = None

    @property
    def AppName(self):
        r"""应用名称，注：后面三个字段AndroidPackageName、IOSBundleId、PcIdentifier，三者选填一个
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AndroidPackageName(self):
        r"""app的安卓包名
        :rtype: str
        """
        return self._AndroidPackageName

    @AndroidPackageName.setter
    def AndroidPackageName(self, AndroidPackageName):
        self._AndroidPackageName = AndroidPackageName

    @property
    def IOSBundleId(self):
        r"""app的IOS的BundleId名
        :rtype: str
        """
        return self._IOSBundleId

    @IOSBundleId.setter
    def IOSBundleId(self, IOSBundleId):
        self._IOSBundleId = IOSBundleId

    @property
    def PcIdentifier(self):
        r"""PC标识名
        :rtype: str
        """
        return self._PcIdentifier

    @PcIdentifier.setter
    def PcIdentifier(self, PcIdentifier):
        self._PcIdentifier = PcIdentifier


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._AndroidPackageName = params.get("AndroidPackageName")
        self._IOSBundleId = params.get("IOSBundleId")
        self._PcIdentifier = params.get("PcIdentifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Artist(AbstractModel):
    r"""Artist

    """

    def __init__(self):
        r"""
        :param _ArtistName: 歌手名
        :type ArtistName: str
        """
        self._ArtistName = None

    @property
    def ArtistName(self):
        r"""歌手名
        :rtype: str
        """
        return self._ArtistName

    @ArtistName.setter
    def ArtistName(self, ArtistName):
        self._ArtistName = ArtistName


    def _deserialize(self, params):
        self._ArtistName = params.get("ArtistName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthInfo(AbstractModel):
    r"""AuthInfo集合

    """

    def __init__(self):
        r"""
        :param _SubjectName: 主体名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectName: str
        :param _ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _AppScene: 应用场景
        :type AppScene: int
        :param _AppRegion: 应用地域
        :type AppRegion: int
        :param _AuthPeriod: 授权时间
        :type AuthPeriod: int
        :param _Commercialization: 是否可商业化
        :type Commercialization: int
        :param _Platform: 是否可跨平台
        :type Platform: int
        :param _Id: 加密后Id
        :type Id: str
        """
        self._SubjectName = None
        self._ProjectName = None
        self._AppScene = None
        self._AppRegion = None
        self._AuthPeriod = None
        self._Commercialization = None
        self._Platform = None
        self._Id = None

    @property
    def SubjectName(self):
        r"""主体名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubjectName

    @SubjectName.setter
    def SubjectName(self, SubjectName):
        self._SubjectName = SubjectName

    @property
    def ProjectName(self):
        r"""项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def AppScene(self):
        r"""应用场景
        :rtype: int
        """
        return self._AppScene

    @AppScene.setter
    def AppScene(self, AppScene):
        self._AppScene = AppScene

    @property
    def AppRegion(self):
        r"""应用地域
        :rtype: int
        """
        return self._AppRegion

    @AppRegion.setter
    def AppRegion(self, AppRegion):
        self._AppRegion = AppRegion

    @property
    def AuthPeriod(self):
        r"""授权时间
        :rtype: int
        """
        return self._AuthPeriod

    @AuthPeriod.setter
    def AuthPeriod(self, AuthPeriod):
        self._AuthPeriod = AuthPeriod

    @property
    def Commercialization(self):
        r"""是否可商业化
        :rtype: int
        """
        return self._Commercialization

    @Commercialization.setter
    def Commercialization(self, Commercialization):
        self._Commercialization = Commercialization

    @property
    def Platform(self):
        r"""是否可跨平台
        :rtype: int
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Id(self):
        r"""加密后Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._SubjectName = params.get("SubjectName")
        self._ProjectName = params.get("ProjectName")
        self._AppScene = params.get("AppScene")
        self._AppRegion = params.get("AppRegion")
        self._AuthPeriod = params.get("AuthPeriod")
        self._Commercialization = params.get("Commercialization")
        self._Platform = params.get("Platform")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeKTVMusicDetailsRequest(AbstractModel):
    r"""BatchDescribeKTVMusicDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicIds: 歌曲Id列表，注：列表最大长度为50
        :type MusicIds: list of str
        """
        self._MusicIds = None

    @property
    def MusicIds(self):
        r"""歌曲Id列表，注：列表最大长度为50
        :rtype: list of str
        """
        return self._MusicIds

    @MusicIds.setter
    def MusicIds(self, MusicIds):
        self._MusicIds = MusicIds


    def _deserialize(self, params):
        self._MusicIds = params.get("MusicIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDescribeKTVMusicDetailsResponse(AbstractModel):
    r"""BatchDescribeKTVMusicDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicDetailInfoSet: 歌曲详情列表信息
        :type KTVMusicDetailInfoSet: list of KTVMusicDetailInfo
        :param _NotExistMusicIdSet: 不存在的歌曲 ID 列表。
        :type NotExistMusicIdSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicDetailInfoSet = None
        self._NotExistMusicIdSet = None
        self._RequestId = None

    @property
    def KTVMusicDetailInfoSet(self):
        r"""歌曲详情列表信息
        :rtype: list of KTVMusicDetailInfo
        """
        return self._KTVMusicDetailInfoSet

    @KTVMusicDetailInfoSet.setter
    def KTVMusicDetailInfoSet(self, KTVMusicDetailInfoSet):
        self._KTVMusicDetailInfoSet = KTVMusicDetailInfoSet

    @property
    def NotExistMusicIdSet(self):
        r"""不存在的歌曲 ID 列表。
        :rtype: list of str
        """
        return self._NotExistMusicIdSet

    @NotExistMusicIdSet.setter
    def NotExistMusicIdSet(self, NotExistMusicIdSet):
        self._NotExistMusicIdSet = NotExistMusicIdSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicDetailInfoSet") is not None:
            self._KTVMusicDetailInfoSet = []
            for item in params.get("KTVMusicDetailInfoSet"):
                obj = KTVMusicDetailInfo()
                obj._deserialize(item)
                self._KTVMusicDetailInfoSet.append(obj)
        self._NotExistMusicIdSet = params.get("NotExistMusicIdSet")
        self._RequestId = params.get("RequestId")


class ChorusClip(AbstractModel):
    r"""副歌片段信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 副歌时间，单位：毫秒
        :type StartTime: int
        :param _EndTime: 副歌结束时间，单位：毫秒
        :type EndTime: int
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        r"""副歌时间，单位：毫秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""副歌结束时间，单位：毫秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKTVRobotRequest(AbstractModel):
    r"""CreateKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        :param _JoinRoomInput: 进房参数。
        :type JoinRoomInput: :class:`tencentcloud.ame.v20190916.models.JoinRoomInput`
        :param _ApplicationLicenseInput: license基础信息
        :type ApplicationLicenseInput: :class:`tencentcloud.ame.v20190916.models.ApplicationLicenseInput`
        :param _SyncRobotCommands: 创建机器人时初始化参数。
        :type SyncRobotCommands: list of SyncRobotCommand
        """
        self._RTCSystem = None
        self._JoinRoomInput = None
        self._ApplicationLicenseInput = None
        self._SyncRobotCommands = None

    @property
    def RTCSystem(self):
        r"""RTC厂商类型，取值有：
<li>TRTC</li>
        :rtype: str
        """
        return self._RTCSystem

    @RTCSystem.setter
    def RTCSystem(self, RTCSystem):
        self._RTCSystem = RTCSystem

    @property
    def JoinRoomInput(self):
        r"""进房参数。
        :rtype: :class:`tencentcloud.ame.v20190916.models.JoinRoomInput`
        """
        return self._JoinRoomInput

    @JoinRoomInput.setter
    def JoinRoomInput(self, JoinRoomInput):
        self._JoinRoomInput = JoinRoomInput

    @property
    def ApplicationLicenseInput(self):
        r"""license基础信息
        :rtype: :class:`tencentcloud.ame.v20190916.models.ApplicationLicenseInput`
        """
        return self._ApplicationLicenseInput

    @ApplicationLicenseInput.setter
    def ApplicationLicenseInput(self, ApplicationLicenseInput):
        self._ApplicationLicenseInput = ApplicationLicenseInput

    @property
    def SyncRobotCommands(self):
        r"""创建机器人时初始化参数。
        :rtype: list of SyncRobotCommand
        """
        return self._SyncRobotCommands

    @SyncRobotCommands.setter
    def SyncRobotCommands(self, SyncRobotCommands):
        self._SyncRobotCommands = SyncRobotCommands


    def _deserialize(self, params):
        self._RTCSystem = params.get("RTCSystem")
        if params.get("JoinRoomInput") is not None:
            self._JoinRoomInput = JoinRoomInput()
            self._JoinRoomInput._deserialize(params.get("JoinRoomInput"))
        if params.get("ApplicationLicenseInput") is not None:
            self._ApplicationLicenseInput = ApplicationLicenseInput()
            self._ApplicationLicenseInput._deserialize(params.get("ApplicationLicenseInput"))
        if params.get("SyncRobotCommands") is not None:
            self._SyncRobotCommands = []
            for item in params.get("SyncRobotCommands"):
                obj = SyncRobotCommand()
                obj._deserialize(item)
                self._SyncRobotCommands.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKTVRobotResponse(AbstractModel):
    r"""CreateKTVRobot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RobotId: 机器人Id。
        :type RobotId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RobotId = None
        self._RequestId = None

    @property
    def RobotId(self):
        r"""机器人Id。
        :rtype: str
        """
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RobotId = params.get("RobotId")
        self._RequestId = params.get("RequestId")


class DataInfo(AbstractModel):
    r"""数据信息

    """

    def __init__(self):
        r"""
        :param _Name: Song Name
        :type Name: str
        :param _Version: 歌曲版本
        :type Version: str
        :param _Duration: 歌曲总时长（非试听时长）
        :type Duration: str
        :param _AuditionBegin: 试听开始时间
        :type AuditionBegin: int
        :param _AuditionEnd: 试听结束时间
        :type AuditionEnd: int
        :param _TagNames: 标签名称
        :type TagNames: list of str
        """
        self._Name = None
        self._Version = None
        self._Duration = None
        self._AuditionBegin = None
        self._AuditionEnd = None
        self._TagNames = None

    @property
    def Name(self):
        r"""Song Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        r"""歌曲版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Duration(self):
        r"""歌曲总时长（非试听时长）
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def AuditionBegin(self):
        r"""试听开始时间
        :rtype: int
        """
        return self._AuditionBegin

    @AuditionBegin.setter
    def AuditionBegin(self, AuditionBegin):
        self._AuditionBegin = AuditionBegin

    @property
    def AuditionEnd(self):
        r"""试听结束时间
        :rtype: int
        """
        return self._AuditionEnd

    @AuditionEnd.setter
    def AuditionEnd(self, AuditionEnd):
        self._AuditionEnd = AuditionEnd

    @property
    def TagNames(self):
        r"""标签名称
        :rtype: list of str
        """
        return self._TagNames

    @TagNames.setter
    def TagNames(self, TagNames):
        self._TagNames = TagNames


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._Duration = params.get("Duration")
        self._AuditionBegin = params.get("AuditionBegin")
        self._AuditionEnd = params.get("AuditionEnd")
        self._TagNames = params.get("TagNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthInfoRequest(AbstractModel):
    r"""DescribeAuthInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量：Offset=Offset+Limit
        :type Offset: int
        :param _Limit: 数据条数
        :type Limit: int
        :param _Key: 搜索关键字
        :type Key: str
        """
        self._Offset = None
        self._Limit = None
        self._Key = None

    @property
    def Offset(self):
        r"""偏移量：Offset=Offset+Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""数据条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Key(self):
        r"""搜索关键字
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthInfoResponse(AbstractModel):
    r"""DescribeAuthInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthInfo: 授权项目列表
        :type AuthInfo: list of AuthInfo
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuthInfo = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AuthInfo(self):
        r"""授权项目列表
        :rtype: list of AuthInfo
        """
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuthInfo") is not None:
            self._AuthInfo = []
            for item in params.get("AuthInfo"):
                obj = AuthInfo()
                obj._deserialize(item)
                self._AuthInfo.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCloudMusicPurchasedRequest(AbstractModel):
    r"""DescribeCloudMusicPurchased请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AuthInfoId: 授权项目Id
        :type AuthInfoId: str
        """
        self._AuthInfoId = None

    @property
    def AuthInfoId(self):
        r"""授权项目Id
        :rtype: str
        """
        return self._AuthInfoId

    @AuthInfoId.setter
    def AuthInfoId(self, AuthInfoId):
        self._AuthInfoId = AuthInfoId


    def _deserialize(self, params):
        self._AuthInfoId = params.get("AuthInfoId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudMusicPurchasedResponse(AbstractModel):
    r"""DescribeCloudMusicPurchased返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicOpenDetail: 云音乐列表
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicOpenDetail: list of MusicOpenDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MusicOpenDetail = None
        self._RequestId = None

    @property
    def MusicOpenDetail(self):
        r"""云音乐列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MusicOpenDetail
        """
        return self._MusicOpenDetail

    @MusicOpenDetail.setter
    def MusicOpenDetail(self, MusicOpenDetail):
        self._MusicOpenDetail = MusicOpenDetail

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MusicOpenDetail") is not None:
            self._MusicOpenDetail = []
            for item in params.get("MusicOpenDetail"):
                obj = MusicOpenDetail()
                obj._deserialize(item)
                self._MusicOpenDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudMusicRequest(AbstractModel):
    r"""DescribeCloudMusic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicId: 歌曲Id
        :type MusicId: str
        :param _MusicType: 歌曲类型，可选值有：
<li>MP3-128K-FTW：含有水印的试听资源；</li>
<li>MP3-320K-FTD-P：320kbps歌曲热门片段；</li>
<li>MP3-320K-FTD：320kbps已核验歌曲完整资源。</li>
默认为：MP3-128K-FTW
        :type MusicType: str
        """
        self._MusicId = None
        self._MusicType = None

    @property
    def MusicId(self):
        r"""歌曲Id
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def MusicType(self):
        r"""歌曲类型，可选值有：
<li>MP3-128K-FTW：含有水印的试听资源；</li>
<li>MP3-320K-FTD-P：320kbps歌曲热门片段；</li>
<li>MP3-320K-FTD：320kbps已核验歌曲完整资源。</li>
默认为：MP3-128K-FTW
        :rtype: str
        """
        return self._MusicType

    @MusicType.setter
    def MusicType(self, MusicType):
        self._MusicType = MusicType


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._MusicType = params.get("MusicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudMusicResponse(AbstractModel):
    r"""DescribeCloudMusic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicId: 歌曲Id
        :type MusicId: str
        :param _MusicName: 歌曲名称
        :type MusicName: str
        :param _Duration: 歌曲时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _MusicUrl: 歌曲链接
        :type MusicUrl: str
        :param _MusicImageUrl: 歌曲图片
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicImageUrl: str
        :param _Singers: 歌手列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Singers: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MusicId = None
        self._MusicName = None
        self._Duration = None
        self._MusicUrl = None
        self._MusicImageUrl = None
        self._Singers = None
        self._RequestId = None

    @property
    def MusicId(self):
        r"""歌曲Id
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def MusicName(self):
        r"""歌曲名称
        :rtype: str
        """
        return self._MusicName

    @MusicName.setter
    def MusicName(self, MusicName):
        self._MusicName = MusicName

    @property
    def Duration(self):
        r"""歌曲时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def MusicUrl(self):
        r"""歌曲链接
        :rtype: str
        """
        return self._MusicUrl

    @MusicUrl.setter
    def MusicUrl(self, MusicUrl):
        self._MusicUrl = MusicUrl

    @property
    def MusicImageUrl(self):
        r"""歌曲图片
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MusicImageUrl

    @MusicImageUrl.setter
    def MusicImageUrl(self, MusicImageUrl):
        self._MusicImageUrl = MusicImageUrl

    @property
    def Singers(self):
        r"""歌手列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Singers

    @Singers.setter
    def Singers(self, Singers):
        self._Singers = Singers

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._MusicName = params.get("MusicName")
        self._Duration = params.get("Duration")
        self._MusicUrl = params.get("MusicUrl")
        self._MusicImageUrl = params.get("MusicImageUrl")
        self._Singers = params.get("Singers")
        self._RequestId = params.get("RequestId")


class DescribeItemByIdRequest(AbstractModel):
    r"""DescribeItemById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ItemIDs: 歌曲ID，目前暂不支持批量查询
        :type ItemIDs: str
        """
        self._ItemIDs = None

    @property
    def ItemIDs(self):
        r"""歌曲ID，目前暂不支持批量查询
        :rtype: str
        """
        return self._ItemIDs

    @ItemIDs.setter
    def ItemIDs(self, ItemIDs):
        self._ItemIDs = ItemIDs


    def _deserialize(self, params):
        self._ItemIDs = params.get("ItemIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeItemByIdResponse(AbstractModel):
    r"""DescribeItemById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 歌曲信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        r"""歌曲信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeItemsRequest(AbstractModel):
    r"""DescribeItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: offset (Default = 0)，(当前页-1) * Limit
        :type Offset: int
        :param _Limit: 条数，必须大于0，最大值为30
        :type Limit: int
        :param _CategoryId: （电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。
        :type CategoryId: str
        :param _CategoryCode: （电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。
        :type CategoryCode: str
        """
        self._Offset = None
        self._Limit = None
        self._CategoryId = None
        self._CategoryCode = None

    @property
    def Offset(self):
        r"""offset (Default = 0)，(当前页-1) * Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""条数，必须大于0，最大值为30
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CategoryId(self):
        r"""（电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def CategoryCode(self):
        r"""（电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。
        :rtype: str
        """
        return self._CategoryCode

    @CategoryCode.setter
    def CategoryCode(self, CategoryCode):
        self._CategoryCode = CategoryCode


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CategoryId = params.get("CategoryId")
        self._CategoryCode = params.get("CategoryCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeItemsResponse(AbstractModel):
    r"""DescribeItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Size: 当前页歌曲数量
        :type Size: int
        :param _Total: 总数据条数
        :type Total: int
        :param _HaveMore: 剩余数量（total-offset-size），通过这个值判断是否
还有下一页
        :type HaveMore: int
        :param _Items: Items 歌曲列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Offset = None
        self._Size = None
        self._Total = None
        self._HaveMore = None
        self._Items = None
        self._RequestId = None

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Size(self):
        r"""当前页歌曲数量
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Total(self):
        r"""总数据条数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def HaveMore(self):
        r"""剩余数量（total-offset-size），通过这个值判断是否
还有下一页
        :rtype: int
        """
        return self._HaveMore

    @HaveMore.setter
    def HaveMore(self, HaveMore):
        self._HaveMore = HaveMore

    @property
    def Items(self):
        r"""Items 歌曲列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Size = params.get("Size")
        self._Total = params.get("Total")
        self._HaveMore = params.get("HaveMore")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVMusicDetailRequest(AbstractModel):
    r"""DescribeKTVMusicDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicId: 曲目 Id
        :type MusicId: str
        """
        self._MusicId = None

    @property
    def MusicId(self):
        r"""曲目 Id
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMusicDetailResponse(AbstractModel):
    r"""DescribeKTVMusicDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicBaseInfo: 歌曲基础信息
        :type KTVMusicBaseInfo: :class:`tencentcloud.ame.v20190916.models.KTVMusicBaseInfo`
        :param _PlayToken: 播放凭证
        :type PlayToken: str
        :param _LyricsUrl: 歌词下载地址
        :type LyricsUrl: str
        :param _DefinitionInfoSet: 歌曲规格信息列表
        :type DefinitionInfoSet: list of KTVMusicDefinitionInfo
        :param _MidiJsonUrl: 音高数据文件下载地址
        :type MidiJsonUrl: str
        :param _ChorusClipSet: 副歌片段数据列表
        :type ChorusClipSet: list of ChorusClip
        :param _PreludeInterval: 前奏间隔，单位：毫秒；注：若参数返回为0则无人声部分
        :type PreludeInterval: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicBaseInfo = None
        self._PlayToken = None
        self._LyricsUrl = None
        self._DefinitionInfoSet = None
        self._MidiJsonUrl = None
        self._ChorusClipSet = None
        self._PreludeInterval = None
        self._RequestId = None

    @property
    def KTVMusicBaseInfo(self):
        r"""歌曲基础信息
        :rtype: :class:`tencentcloud.ame.v20190916.models.KTVMusicBaseInfo`
        """
        return self._KTVMusicBaseInfo

    @KTVMusicBaseInfo.setter
    def KTVMusicBaseInfo(self, KTVMusicBaseInfo):
        self._KTVMusicBaseInfo = KTVMusicBaseInfo

    @property
    def PlayToken(self):
        r"""播放凭证
        :rtype: str
        """
        return self._PlayToken

    @PlayToken.setter
    def PlayToken(self, PlayToken):
        self._PlayToken = PlayToken

    @property
    def LyricsUrl(self):
        r"""歌词下载地址
        :rtype: str
        """
        return self._LyricsUrl

    @LyricsUrl.setter
    def LyricsUrl(self, LyricsUrl):
        self._LyricsUrl = LyricsUrl

    @property
    def DefinitionInfoSet(self):
        r"""歌曲规格信息列表
        :rtype: list of KTVMusicDefinitionInfo
        """
        return self._DefinitionInfoSet

    @DefinitionInfoSet.setter
    def DefinitionInfoSet(self, DefinitionInfoSet):
        self._DefinitionInfoSet = DefinitionInfoSet

    @property
    def MidiJsonUrl(self):
        r"""音高数据文件下载地址
        :rtype: str
        """
        return self._MidiJsonUrl

    @MidiJsonUrl.setter
    def MidiJsonUrl(self, MidiJsonUrl):
        self._MidiJsonUrl = MidiJsonUrl

    @property
    def ChorusClipSet(self):
        r"""副歌片段数据列表
        :rtype: list of ChorusClip
        """
        return self._ChorusClipSet

    @ChorusClipSet.setter
    def ChorusClipSet(self, ChorusClipSet):
        self._ChorusClipSet = ChorusClipSet

    @property
    def PreludeInterval(self):
        r"""前奏间隔，单位：毫秒；注：若参数返回为0则无人声部分
        :rtype: int
        """
        return self._PreludeInterval

    @PreludeInterval.setter
    def PreludeInterval(self, PreludeInterval):
        self._PreludeInterval = PreludeInterval

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self._KTVMusicBaseInfo = KTVMusicBaseInfo()
            self._KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        self._PlayToken = params.get("PlayToken")
        self._LyricsUrl = params.get("LyricsUrl")
        if params.get("DefinitionInfoSet") is not None:
            self._DefinitionInfoSet = []
            for item in params.get("DefinitionInfoSet"):
                obj = KTVMusicDefinitionInfo()
                obj._deserialize(item)
                self._DefinitionInfoSet.append(obj)
        self._MidiJsonUrl = params.get("MidiJsonUrl")
        if params.get("ChorusClipSet") is not None:
            self._ChorusClipSet = []
            for item in params.get("ChorusClipSet"):
                obj = ChorusClip()
                obj._deserialize(item)
                self._ChorusClipSet.append(obj)
        self._PreludeInterval = params.get("PreludeInterval")
        self._RequestId = params.get("RequestId")


class DescribeKTVMusicTagsRequest(AbstractModel):
    r"""DescribeKTVMusicTags请求参数结构体

    """


class DescribeKTVMusicTagsResponse(AbstractModel):
    r"""DescribeKTVMusicTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TagGroupSet: 标签分组列表
        :type TagGroupSet: list of KTVMusicTagGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TagGroupSet = None
        self._RequestId = None

    @property
    def TagGroupSet(self):
        r"""标签分组列表
        :rtype: list of KTVMusicTagGroup
        """
        return self._TagGroupSet

    @TagGroupSet.setter
    def TagGroupSet(self, TagGroupSet):
        self._TagGroupSet = TagGroupSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TagGroupSet") is not None:
            self._TagGroupSet = []
            for item in params.get("TagGroupSet"):
                obj = KTVMusicTagGroup()
                obj._deserialize(item)
                self._TagGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVPlaylistDetailRequest(AbstractModel):
    r"""DescribeKTVPlaylistDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlaylistId: 歌单Id
        :type PlaylistId: str
        :param _Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Limit: int
        """
        self._PlaylistId = None
        self._Offset = None
        self._Limit = None

    @property
    def PlaylistId(self):
        r"""歌单Id
        :rtype: str
        """
        return self._PlaylistId

    @PlaylistId.setter
    def PlaylistId(self, PlaylistId):
        self._PlaylistId = PlaylistId

    @property
    def Offset(self):
        r"""分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._PlaylistId = params.get("PlaylistId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVPlaylistDetailResponse(AbstractModel):
    r"""DescribeKTVPlaylistDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicInfoSet: 歌曲基础信息列表
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param _PlaylistBaseInfo: 歌单基础信息
        :type PlaylistBaseInfo: :class:`tencentcloud.ame.v20190916.models.KTVPlaylistBaseInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicInfoSet = None
        self._PlaylistBaseInfo = None
        self._RequestId = None

    @property
    def KTVMusicInfoSet(self):
        r"""歌曲基础信息列表
        :rtype: list of KTVMusicBaseInfo
        """
        return self._KTVMusicInfoSet

    @KTVMusicInfoSet.setter
    def KTVMusicInfoSet(self, KTVMusicInfoSet):
        self._KTVMusicInfoSet = KTVMusicInfoSet

    @property
    def PlaylistBaseInfo(self):
        r"""歌单基础信息
        :rtype: :class:`tencentcloud.ame.v20190916.models.KTVPlaylistBaseInfo`
        """
        return self._PlaylistBaseInfo

    @PlaylistBaseInfo.setter
    def PlaylistBaseInfo(self, PlaylistBaseInfo):
        self._PlaylistBaseInfo = PlaylistBaseInfo

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicInfoSet") is not None:
            self._KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self._KTVMusicInfoSet.append(obj)
        if params.get("PlaylistBaseInfo") is not None:
            self._PlaylistBaseInfo = KTVPlaylistBaseInfo()
            self._PlaylistBaseInfo._deserialize(params.get("PlaylistBaseInfo"))
        self._RequestId = params.get("RequestId")


class DescribeKTVPlaylistsRequest(AbstractModel):
    r"""DescribeKTVPlaylists请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 歌单类型，取值有：
·OfficialRec：官方推荐
·Normal：自定义
当该字段未填时，默认为取OfficialRec
        :type Type: str
        :param _Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000
        :type Limit: int
        """
        self._Type = None
        self._Offset = None
        self._Limit = None

    @property
    def Type(self):
        r"""歌单类型，取值有：
·OfficialRec：官方推荐
·Normal：自定义
当该字段未填时，默认为取OfficialRec
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        r"""分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVPlaylistsResponse(AbstractModel):
    r"""DescribeKTVPlaylists返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlaylistBaseInfoSet: 推荐歌单列表
        :type PlaylistBaseInfoSet: list of KTVPlaylistBaseInfo
        :param _TotalCount: 推荐歌单列表总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlaylistBaseInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PlaylistBaseInfoSet(self):
        r"""推荐歌单列表
        :rtype: list of KTVPlaylistBaseInfo
        """
        return self._PlaylistBaseInfoSet

    @PlaylistBaseInfoSet.setter
    def PlaylistBaseInfoSet(self, PlaylistBaseInfoSet):
        self._PlaylistBaseInfoSet = PlaylistBaseInfoSet

    @property
    def TotalCount(self):
        r"""推荐歌单列表总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PlaylistBaseInfoSet") is not None:
            self._PlaylistBaseInfoSet = []
            for item in params.get("PlaylistBaseInfoSet"):
                obj = KTVPlaylistBaseInfo()
                obj._deserialize(item)
                self._PlaylistBaseInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeKTVRobotsRequest(AbstractModel):
    r"""DescribeKTVRobots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RobotIds: 机器人Id列表。
        :type RobotIds: list of str
        :param _Statuses: 机器人状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :type Statuses: list of str
        :param _CreateTime: 匹配创建时间在此时间段内的机器人。
<li>包含所指定的头尾时间点。</li>
        :type CreateTime: :class:`tencentcloud.ame.v20190916.models.TimeRange`
        :param _Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        :param _Limit: 分页返回的起始偏移量，默认值：10。
        :type Limit: int
        """
        self._RobotIds = None
        self._Statuses = None
        self._CreateTime = None
        self._Offset = None
        self._Limit = None

    @property
    def RobotIds(self):
        r"""机器人Id列表。
        :rtype: list of str
        """
        return self._RobotIds

    @RobotIds.setter
    def RobotIds(self, RobotIds):
        self._RobotIds = RobotIds

    @property
    def Statuses(self):
        r"""机器人状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :rtype: list of str
        """
        return self._Statuses

    @Statuses.setter
    def Statuses(self, Statuses):
        self._Statuses = Statuses

    @property
    def CreateTime(self):
        r"""匹配创建时间在此时间段内的机器人。
<li>包含所指定的头尾时间点。</li>
        :rtype: :class:`tencentcloud.ame.v20190916.models.TimeRange`
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Offset(self):
        r"""分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页返回的起始偏移量，默认值：10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RobotIds = params.get("RobotIds")
        self._Statuses = params.get("Statuses")
        if params.get("CreateTime") is not None:
            self._CreateTime = TimeRange()
            self._CreateTime._deserialize(params.get("CreateTime"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVRobotsResponse(AbstractModel):
    r"""DescribeKTVRobots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 机器人总数。
        :type TotalCount: int
        :param _KTVRobotInfoSet: 机器人信息集合。
        :type KTVRobotInfoSet: list of KTVRobotInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KTVRobotInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""机器人总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KTVRobotInfoSet(self):
        r"""机器人信息集合。
        :rtype: list of KTVRobotInfo
        """
        return self._KTVRobotInfoSet

    @KTVRobotInfoSet.setter
    def KTVRobotInfoSet(self, KTVRobotInfoSet):
        self._KTVRobotInfoSet = KTVRobotInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KTVRobotInfoSet") is not None:
            self._KTVRobotInfoSet = []
            for item in params.get("KTVRobotInfoSet"):
                obj = KTVRobotInfo()
                obj._deserialize(item)
                self._KTVRobotInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVSingerCategoriesRequest(AbstractModel):
    r"""DescribeKTVSingerCategories请求参数结构体

    """


class DescribeKTVSingerCategoriesResponse(AbstractModel):
    r"""DescribeKTVSingerCategories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GenderSet: 歌手性别分类列表
        :type GenderSet: list of KTVSingerCategoryInfo
        :param _AreaSet: 歌手区域分类列表
        :type AreaSet: list of KTVSingerCategoryInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GenderSet = None
        self._AreaSet = None
        self._RequestId = None

    @property
    def GenderSet(self):
        r"""歌手性别分类列表
        :rtype: list of KTVSingerCategoryInfo
        """
        return self._GenderSet

    @GenderSet.setter
    def GenderSet(self, GenderSet):
        self._GenderSet = GenderSet

    @property
    def AreaSet(self):
        r"""歌手区域分类列表
        :rtype: list of KTVSingerCategoryInfo
        """
        return self._AreaSet

    @AreaSet.setter
    def AreaSet(self, AreaSet):
        self._AreaSet = AreaSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GenderSet") is not None:
            self._GenderSet = []
            for item in params.get("GenderSet"):
                obj = KTVSingerCategoryInfo()
                obj._deserialize(item)
                self._GenderSet.append(obj)
        if params.get("AreaSet") is not None:
            self._AreaSet = []
            for item in params.get("AreaSet"):
                obj = KTVSingerCategoryInfo()
                obj._deserialize(item)
                self._AreaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVSingerMusicsRequest(AbstractModel):
    r"""DescribeKTVSingerMusics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SingerId: 歌手id
        :type SingerId: str
        :param _Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Limit: int
        """
        self._SingerId = None
        self._Offset = None
        self._Limit = None

    @property
    def SingerId(self):
        r"""歌手id
        :rtype: str
        """
        return self._SingerId

    @SingerId.setter
    def SingerId(self, SingerId):
        self._SingerId = SingerId

    @property
    def Offset(self):
        r"""分页偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SingerId = params.get("SingerId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVSingerMusicsResponse(AbstractModel):
    r"""DescribeKTVSingerMusics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总曲目数
        :type TotalCount: int
        :param _KTVMusicInfoSet: KTV 曲目列表
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KTVMusicInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总曲目数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KTVMusicInfoSet(self):
        r"""KTV 曲目列表
        :rtype: list of KTVMusicBaseInfo
        """
        return self._KTVMusicInfoSet

    @KTVMusicInfoSet.setter
    def KTVMusicInfoSet(self, KTVMusicInfoSet):
        self._KTVMusicInfoSet = KTVMusicInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KTVMusicInfoSet") is not None:
            self._KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self._KTVMusicInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVSingersRequest(AbstractModel):
    r"""DescribeKTVSingers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SingerIds: 歌手id集合，精确匹配歌手id
<li> 数组长度限制10</li>
        :type SingerIds: list of str
        :param _Genders: 歌手性别集合，不传为全部，精确匹配歌手性别类型，
<li>数组长度限制1</li>
<li>取值范围：直播互动曲库歌手分类信息接口，返回性别分类信息列表中，分类英文名</li>
        :type Genders: list of str
        :param _Areas: 歌手区域集合，不传为全部，精确匹配歌手区域
<li>数组长度限制10</li>
<li>取值范围：直播互动曲库歌手分类信息接口，返回的区域分类信息列表中，分类英文名</li>
        :type Areas: list of str
        :param _Sort: 排序方式。默认按照播放数倒序
<li> Sort.Field 可选 PlayCount。</li>
        :type Sort: :class:`tencentcloud.ame.v20190916.models.SortBy`
        :param _Offset: 分页偏移量，默认值：0。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Limit: int
        """
        self._SingerIds = None
        self._Genders = None
        self._Areas = None
        self._Sort = None
        self._Offset = None
        self._Limit = None

    @property
    def SingerIds(self):
        r"""歌手id集合，精确匹配歌手id
<li> 数组长度限制10</li>
        :rtype: list of str
        """
        return self._SingerIds

    @SingerIds.setter
    def SingerIds(self, SingerIds):
        self._SingerIds = SingerIds

    @property
    def Genders(self):
        r"""歌手性别集合，不传为全部，精确匹配歌手性别类型，
<li>数组长度限制1</li>
<li>取值范围：直播互动曲库歌手分类信息接口，返回性别分类信息列表中，分类英文名</li>
        :rtype: list of str
        """
        return self._Genders

    @Genders.setter
    def Genders(self, Genders):
        self._Genders = Genders

    @property
    def Areas(self):
        r"""歌手区域集合，不传为全部，精确匹配歌手区域
<li>数组长度限制10</li>
<li>取值范围：直播互动曲库歌手分类信息接口，返回的区域分类信息列表中，分类英文名</li>
        :rtype: list of str
        """
        return self._Areas

    @Areas.setter
    def Areas(self, Areas):
        self._Areas = Areas

    @property
    def Sort(self):
        r"""排序方式。默认按照播放数倒序
<li> Sort.Field 可选 PlayCount。</li>
        :rtype: :class:`tencentcloud.ame.v20190916.models.SortBy`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Offset(self):
        r"""分页偏移量，默认值：0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SingerIds = params.get("SingerIds")
        self._Genders = params.get("Genders")
        self._Areas = params.get("Areas")
        if params.get("Sort") is not None:
            self._Sort = SortBy()
            self._Sort._deserialize(params.get("Sort"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVSingersResponse(AbstractModel):
    r"""DescribeKTVSingers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总歌手数
        :type TotalCount: int
        :param _KTVSingerInfoSet: KTV歌手列表
        :type KTVSingerInfoSet: list of KTVSingerInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KTVSingerInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总歌手数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KTVSingerInfoSet(self):
        r"""KTV歌手列表
        :rtype: list of KTVSingerInfo
        """
        return self._KTVSingerInfoSet

    @KTVSingerInfoSet.setter
    def KTVSingerInfoSet(self, KTVSingerInfoSet):
        self._KTVSingerInfoSet = KTVSingerInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KTVSingerInfoSet") is not None:
            self._KTVSingerInfoSet = []
            for item in params.get("KTVSingerInfoSet"):
                obj = KTVSingerInfo()
                obj._deserialize(item)
                self._KTVSingerInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVSuggestionsRequest(AbstractModel):
    r"""DescribeKTVSuggestions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyWord: 联想关键词
        :type KeyWord: str
        """
        self._KeyWord = None

    @property
    def KeyWord(self):
        r"""联想关键词
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord


    def _deserialize(self, params):
        self._KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVSuggestionsResponse(AbstractModel):
    r"""DescribeKTVSuggestions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVSuggestionInfoSet: 联想词信息列表。返回总数最大为10。
        :type KTVSuggestionInfoSet: list of KTVSuggestionInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVSuggestionInfoSet = None
        self._RequestId = None

    @property
    def KTVSuggestionInfoSet(self):
        r"""联想词信息列表。返回总数最大为10。
        :rtype: list of KTVSuggestionInfo
        """
        return self._KTVSuggestionInfoSet

    @KTVSuggestionInfoSet.setter
    def KTVSuggestionInfoSet(self, KTVSuggestionInfoSet):
        self._KTVSuggestionInfoSet = KTVSuggestionInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVSuggestionInfoSet") is not None:
            self._KTVSuggestionInfoSet = []
            for item in params.get("KTVSuggestionInfoSet"):
                obj = KTVSuggestionInfo()
                obj._deserialize(item)
                self._KTVSuggestionInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeKTVTopListRequest(AbstractModel):
    r"""DescribeKTVTopList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 榜单类型。默认Hot
<li> Hot, 热歌榜。</li>
        :type Type: str
        :param _Period: 榜单周期 默认为Week
<li> Week, 周榜。</li>
<li> Month, 月榜。</li>
        :type Period: str
        """
        self._Type = None
        self._Period = None

    @property
    def Type(self):
        r"""榜单类型。默认Hot
<li> Hot, 热歌榜。</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Period(self):
        r"""榜单周期 默认为Week
<li> Week, 周榜。</li>
<li> Month, 月榜。</li>
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVTopListResponse(AbstractModel):
    r"""DescribeKTVTopList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KTVMusicTopInfoSet: 歌曲基础信息列表
        :type KTVMusicTopInfoSet: list of KTVMusicTopInfo
        :param _TotalCount: 返回总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KTVMusicTopInfoSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def KTVMusicTopInfoSet(self):
        r"""歌曲基础信息列表
        :rtype: list of KTVMusicTopInfo
        """
        return self._KTVMusicTopInfoSet

    @KTVMusicTopInfoSet.setter
    def KTVMusicTopInfoSet(self, KTVMusicTopInfoSet):
        self._KTVMusicTopInfoSet = KTVMusicTopInfoSet

    @property
    def TotalCount(self):
        r"""返回总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KTVMusicTopInfoSet") is not None:
            self._KTVMusicTopInfoSet = []
            for item in params.get("KTVMusicTopInfoSet"):
                obj = KTVMusicTopInfo()
                obj._deserialize(item)
                self._KTVMusicTopInfoSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLyricRequest(AbstractModel):
    r"""DescribeLyric请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ItemId: 歌曲ID
        :type ItemId: str
        :param _SubItemType: 格式，可选项，可不填写，默认值为：LRC-LRC。
<li>LRC-LRC：歌词；</li>
<li>JSON-ST：波形图。</li>
        :type SubItemType: str
        """
        self._ItemId = None
        self._SubItemType = None

    @property
    def ItemId(self):
        r"""歌曲ID
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def SubItemType(self):
        r"""格式，可选项，可不填写，默认值为：LRC-LRC。
<li>LRC-LRC：歌词；</li>
<li>JSON-ST：波形图。</li>
        :rtype: str
        """
        return self._SubItemType

    @SubItemType.setter
    def SubItemType(self, SubItemType):
        self._SubItemType = SubItemType


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._SubItemType = params.get("SubItemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLyricResponse(AbstractModel):
    r"""DescribeLyric返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Lyric: 歌词或者波形图详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Lyric: :class:`tencentcloud.ame.v20190916.models.Lyric`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Lyric = None
        self._RequestId = None

    @property
    def Lyric(self):
        r"""歌词或者波形图详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ame.v20190916.models.Lyric`
        """
        return self._Lyric

    @Lyric.setter
    def Lyric(self, Lyric):
        self._Lyric = Lyric

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Lyric") is not None:
            self._Lyric = Lyric()
            self._Lyric._deserialize(params.get("Lyric"))
        self._RequestId = params.get("RequestId")


class DescribeMusicRequest(AbstractModel):
    r"""DescribeMusic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ItemId: 歌曲ID
        :type ItemId: str
        :param _IdentityId: 在应用前端播放音乐C端用户的唯一标识。无需是账户信息，用户唯一标识即可。
        :type IdentityId: str
        :param _SubItemType: MP3-320K-FTD-P  为获取320kbps歌曲热门片段。
MP3-320K-FTD 为获取320kbps已核验歌曲完整资源。
        :type SubItemType: str
        :param _Ssl: CDN URL Protocol:HTTP or HTTPS/SSL
Values:Y , N(default)
        :type Ssl: str
        """
        self._ItemId = None
        self._IdentityId = None
        self._SubItemType = None
        self._Ssl = None

    @property
    def ItemId(self):
        r"""歌曲ID
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def IdentityId(self):
        r"""在应用前端播放音乐C端用户的唯一标识。无需是账户信息，用户唯一标识即可。
        :rtype: str
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def SubItemType(self):
        r"""MP3-320K-FTD-P  为获取320kbps歌曲热门片段。
MP3-320K-FTD 为获取320kbps已核验歌曲完整资源。
        :rtype: str
        """
        return self._SubItemType

    @SubItemType.setter
    def SubItemType(self, SubItemType):
        self._SubItemType = SubItemType

    @property
    def Ssl(self):
        r"""CDN URL Protocol:HTTP or HTTPS/SSL
Values:Y , N(default)
        :rtype: str
        """
        return self._Ssl

    @Ssl.setter
    def Ssl(self, Ssl):
        self._Ssl = Ssl


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._IdentityId = params.get("IdentityId")
        self._SubItemType = params.get("SubItemType")
        self._Ssl = params.get("Ssl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMusicResponse(AbstractModel):
    r"""DescribeMusic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Music: 音乐相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Music: :class:`tencentcloud.ame.v20190916.models.Music`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Music = None
        self._RequestId = None

    @property
    def Music(self):
        r"""音乐相关信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ame.v20190916.models.Music`
        """
        return self._Music

    @Music.setter
    def Music(self, Music):
        self._Music = Music

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Music") is not None:
            self._Music = Music()
            self._Music._deserialize(params.get("Music"))
        self._RequestId = params.get("RequestId")


class DescribeMusicSaleStatusRequest(AbstractModel):
    r"""DescribeMusicSaleStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicIds: 歌曲Id集合，可传单个，也可传多个，上线查询单次50个
        :type MusicIds: list of str
        :param _PurchaseType: 查询哪个渠道的数据，1为曲库包，2为单曲
        :type PurchaseType: int
        """
        self._MusicIds = None
        self._PurchaseType = None

    @property
    def MusicIds(self):
        r"""歌曲Id集合，可传单个，也可传多个，上线查询单次50个
        :rtype: list of str
        """
        return self._MusicIds

    @MusicIds.setter
    def MusicIds(self, MusicIds):
        self._MusicIds = MusicIds

    @property
    def PurchaseType(self):
        r"""查询哪个渠道的数据，1为曲库包，2为单曲
        :rtype: int
        """
        return self._PurchaseType

    @PurchaseType.setter
    def PurchaseType(self, PurchaseType):
        self._PurchaseType = PurchaseType


    def _deserialize(self, params):
        self._MusicIds = params.get("MusicIds")
        self._PurchaseType = params.get("PurchaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMusicSaleStatusResponse(AbstractModel):
    r"""DescribeMusicSaleStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicStatusSet: musicId对应歌曲状态
        :type MusicStatusSet: list of MusicStatus
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MusicStatusSet = None
        self._RequestId = None

    @property
    def MusicStatusSet(self):
        r"""musicId对应歌曲状态
        :rtype: list of MusicStatus
        """
        return self._MusicStatusSet

    @MusicStatusSet.setter
    def MusicStatusSet(self, MusicStatusSet):
        self._MusicStatusSet = MusicStatusSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MusicStatusSet") is not None:
            self._MusicStatusSet = []
            for item in params.get("MusicStatusSet"):
                obj = MusicStatus()
                obj._deserialize(item)
                self._MusicStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePackageItemsRequest(AbstractModel):
    r"""DescribePackageItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单id，从获取已购曲库包列表中获取
        :type OrderId: str
        :param _Offset: 默认0，Offset=Offset+Length
        :type Offset: int
        :param _Length: 默认20
        :type Length: int
        """
        self._OrderId = None
        self._Offset = None
        self._Length = None

    @property
    def OrderId(self):
        r"""订单id，从获取已购曲库包列表中获取
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Offset(self):
        r"""默认0，Offset=Offset+Length
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Length(self):
        r"""默认20
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Offset = params.get("Offset")
        self._Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackageItemsResponse(AbstractModel):
    r"""DescribePackageItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageItems: 已核销歌曲信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageItems: list of PackageItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackageItems = None
        self._RequestId = None

    @property
    def PackageItems(self):
        r"""已核销歌曲信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PackageItem
        """
        return self._PackageItems

    @PackageItems.setter
    def PackageItems(self, PackageItems):
        self._PackageItems = PackageItems

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PackageItems") is not None:
            self._PackageItems = []
            for item in params.get("PackageItems"):
                obj = PackageItem()
                obj._deserialize(item)
                self._PackageItems.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePackagesRequest(AbstractModel):
    r"""DescribePackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 默认0，Offset=Offset+Length
        :type Offset: int
        :param _Length: 默认20
        :type Length: int
        """
        self._Offset = None
        self._Length = None

    @property
    def Offset(self):
        r"""默认0，Offset=Offset+Length
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Length(self):
        r"""默认20
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackagesResponse(AbstractModel):
    r"""DescribePackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Packages: 已购曲库包列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Packages: list of Package
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Packages = None
        self._RequestId = None

    @property
    def Packages(self):
        r"""已购曲库包列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Package
        """
        return self._Packages

    @Packages.setter
    def Packages(self, Packages):
        self._Packages = Packages

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Packages") is not None:
            self._Packages = []
            for item in params.get("Packages"):
                obj = Package()
                obj._deserialize(item)
                self._Packages.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePkgOfflineMusicRequest(AbstractModel):
    r"""DescribePkgOfflineMusic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PackageOrderId: 订单id
        :type PackageOrderId: str
        :param _Limit: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条(注：单次上限为100)。
        :type Limit: int
        :param _Offset: 分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Offset: int
        """
        self._PackageOrderId = None
        self._Limit = None
        self._Offset = None

    @property
    def PackageOrderId(self):
        r"""订单id
        :rtype: str
        """
        return self._PackageOrderId

    @PackageOrderId.setter
    def PackageOrderId(self, PackageOrderId):
        self._PackageOrderId = PackageOrderId

    @property
    def Limit(self):
        r"""分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条(注：单次上限为100)。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页返回的记录条数，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._PackageOrderId = params.get("PackageOrderId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePkgOfflineMusicResponse(AbstractModel):
    r"""DescribePkgOfflineMusic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OfflineMusicSet: 曲库包中不可用歌曲信息
        :type OfflineMusicSet: list of OfflineMusicDetail
        :param _TotalCount: 返回总量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OfflineMusicSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def OfflineMusicSet(self):
        r"""曲库包中不可用歌曲信息
        :rtype: list of OfflineMusicDetail
        """
        return self._OfflineMusicSet

    @OfflineMusicSet.setter
    def OfflineMusicSet(self, OfflineMusicSet):
        self._OfflineMusicSet = OfflineMusicSet

    @property
    def TotalCount(self):
        r"""返回总量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("OfflineMusicSet") is not None:
            self._OfflineMusicSet = []
            for item in params.get("OfflineMusicSet"):
                obj = OfflineMusicDetail()
                obj._deserialize(item)
                self._OfflineMusicSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeStationsRequest(AbstractModel):
    r"""DescribeStations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 条数，必须大于0
        :type Limit: int
        :param _Offset: offset (Default = 0)，Offset=Offset+Limit
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        r"""条数，必须大于0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""offset (Default = 0)，Offset=Offset+Limit
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
        


class DescribeStationsResponse(AbstractModel):
    r"""DescribeStations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数量
        :type Total: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Size: 当前页station数量
        :type Size: int
        :param _HaveMore: 剩余数量（total-offset-size），通过这个值判断是否还有下一页
        :type HaveMore: int
        :param _Stations: Stations 素材库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Stations: list of Station
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Offset = None
        self._Size = None
        self._HaveMore = None
        self._Stations = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数量
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Offset(self):
        r"""分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Size(self):
        r"""当前页station数量
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def HaveMore(self):
        r"""剩余数量（total-offset-size），通过这个值判断是否还有下一页
        :rtype: int
        """
        return self._HaveMore

    @HaveMore.setter
    def HaveMore(self, HaveMore):
        self._HaveMore = HaveMore

    @property
    def Stations(self):
        r"""Stations 素材库列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Station
        """
        return self._Stations

    @Stations.setter
    def Stations(self, Stations):
        self._Stations = Stations

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Offset = params.get("Offset")
        self._Size = params.get("Size")
        self._HaveMore = params.get("HaveMore")
        if params.get("Stations") is not None:
            self._Stations = []
            for item in params.get("Stations"):
                obj = Station()
                obj._deserialize(item)
                self._Stations.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyKTVRobotRequest(AbstractModel):
    r"""DestroyKTVRobot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RobotId: 机器人Id。
        :type RobotId: str
        """
        self._RobotId = None

    @property
    def RobotId(self):
        r"""机器人Id。
        :rtype: str
        """
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId


    def _deserialize(self, params):
        self._RobotId = params.get("RobotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyKTVRobotResponse(AbstractModel):
    r"""DestroyKTVRobot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ImagePath(AbstractModel):
    r"""图片路径

    """

    def __init__(self):
        r"""
        :param _Key: station图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: station图片地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""station图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""station图片地址
注意：此字段可能返回 null，表示取不到有效值。
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
        


class Item(AbstractModel):
    r"""歌曲信息

    """

    def __init__(self):
        r"""
        :param _ItemID: Song ID
        :type ItemID: str
        :param _DataInfo: Song info
注意：此字段可能返回 null，表示取不到有效值。
        :type DataInfo: :class:`tencentcloud.ame.v20190916.models.DataInfo`
        :param _Album: 专辑信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Album: :class:`tencentcloud.ame.v20190916.models.Album`
        :param _Artists: 多个歌手集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Artists: list of Artist
        :param _Status: 歌曲状态，1:添加进购物车；2:核销进曲库包
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._ItemID = None
        self._DataInfo = None
        self._Album = None
        self._Artists = None
        self._Status = None

    @property
    def ItemID(self):
        r"""Song ID
        :rtype: str
        """
        return self._ItemID

    @ItemID.setter
    def ItemID(self, ItemID):
        self._ItemID = ItemID

    @property
    def DataInfo(self):
        r"""Song info
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ame.v20190916.models.DataInfo`
        """
        return self._DataInfo

    @DataInfo.setter
    def DataInfo(self, DataInfo):
        self._DataInfo = DataInfo

    @property
    def Album(self):
        r"""专辑信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ame.v20190916.models.Album`
        """
        return self._Album

    @Album.setter
    def Album(self, Album):
        self._Album = Album

    @property
    def Artists(self):
        r"""多个歌手集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Artist
        """
        return self._Artists

    @Artists.setter
    def Artists(self, Artists):
        self._Artists = Artists

    @property
    def Status(self):
        r"""歌曲状态，1:添加进购物车；2:核销进曲库包
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ItemID = params.get("ItemID")
        if params.get("DataInfo") is not None:
            self._DataInfo = DataInfo()
            self._DataInfo._deserialize(params.get("DataInfo"))
        if params.get("Album") is not None:
            self._Album = Album()
            self._Album._deserialize(params.get("Album"))
        if params.get("Artists") is not None:
            self._Artists = []
            for item in params.get("Artists"):
                obj = Artist()
                obj._deserialize(item)
                self._Artists.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JoinRoomInput(AbstractModel):
    r"""直播进房输入参数

    """

    def __init__(self):
        r"""
        :param _TRTCJoinRoomInput: TRTC进房参数
        :type TRTCJoinRoomInput: :class:`tencentcloud.ame.v20190916.models.TRTCJoinRoomInput`
        """
        self._TRTCJoinRoomInput = None

    @property
    def TRTCJoinRoomInput(self):
        r"""TRTC进房参数
        :rtype: :class:`tencentcloud.ame.v20190916.models.TRTCJoinRoomInput`
        """
        return self._TRTCJoinRoomInput

    @TRTCJoinRoomInput.setter
    def TRTCJoinRoomInput(self, TRTCJoinRoomInput):
        self._TRTCJoinRoomInput = TRTCJoinRoomInput


    def _deserialize(self, params):
        if params.get("TRTCJoinRoomInput") is not None:
            self._TRTCJoinRoomInput = TRTCJoinRoomInput()
            self._TRTCJoinRoomInput._deserialize(params.get("TRTCJoinRoomInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicBaseInfo(AbstractModel):
    r"""KTV 曲目基础信息

    """

    def __init__(self):
        r"""
        :param _MusicId: 歌曲 Id
        :type MusicId: str
        :param _Name: 歌曲名称
        :type Name: str
        :param _SingerInfoSet: 演唱者基础信息列表
        :type SingerInfoSet: list of KTVSingerBaseInfo
        :param _SingerSet: 已弃用，请使用SingerInfoSet
        :type SingerSet: list of str
        :param _LyricistSet: 作词者列表
        :type LyricistSet: list of str
        :param _ComposerSet: 作曲者列表
        :type ComposerSet: list of str
        :param _TagSet: 标签列表
        :type TagSet: list of str
        :param _Duration: 歌曲时长
        :type Duration: int
        """
        self._MusicId = None
        self._Name = None
        self._SingerInfoSet = None
        self._SingerSet = None
        self._LyricistSet = None
        self._ComposerSet = None
        self._TagSet = None
        self._Duration = None

    @property
    def MusicId(self):
        r"""歌曲 Id
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def Name(self):
        r"""歌曲名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SingerInfoSet(self):
        r"""演唱者基础信息列表
        :rtype: list of KTVSingerBaseInfo
        """
        return self._SingerInfoSet

    @SingerInfoSet.setter
    def SingerInfoSet(self, SingerInfoSet):
        self._SingerInfoSet = SingerInfoSet

    @property
    def SingerSet(self):
        r"""已弃用，请使用SingerInfoSet
        :rtype: list of str
        """
        return self._SingerSet

    @SingerSet.setter
    def SingerSet(self, SingerSet):
        self._SingerSet = SingerSet

    @property
    def LyricistSet(self):
        r"""作词者列表
        :rtype: list of str
        """
        return self._LyricistSet

    @LyricistSet.setter
    def LyricistSet(self, LyricistSet):
        self._LyricistSet = LyricistSet

    @property
    def ComposerSet(self):
        r"""作曲者列表
        :rtype: list of str
        """
        return self._ComposerSet

    @ComposerSet.setter
    def ComposerSet(self, ComposerSet):
        self._ComposerSet = ComposerSet

    @property
    def TagSet(self):
        r"""标签列表
        :rtype: list of str
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Duration(self):
        r"""歌曲时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._Name = params.get("Name")
        if params.get("SingerInfoSet") is not None:
            self._SingerInfoSet = []
            for item in params.get("SingerInfoSet"):
                obj = KTVSingerBaseInfo()
                obj._deserialize(item)
                self._SingerInfoSet.append(obj)
        self._SingerSet = params.get("SingerSet")
        self._LyricistSet = params.get("LyricistSet")
        self._ComposerSet = params.get("ComposerSet")
        self._TagSet = params.get("TagSet")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicDefinitionInfo(AbstractModel):
    r"""直播互动歌曲规格信息。

    """

    def __init__(self):
        r"""
        :param _Definition: 规格，取值有：
<li>audio/mi：低规格；</li>
<li>audio/lo：中规格；</li>
<li>audio/hi：高规格。</li>
        :type Definition: str
        :param _Bitrate: 码率，单位为 bps。
        :type Bitrate: int
        :param _Size: 文件大小，单位为字节。
        :type Size: int
        """
        self._Definition = None
        self._Bitrate = None
        self._Size = None

    @property
    def Definition(self):
        r"""规格，取值有：
<li>audio/mi：低规格；</li>
<li>audio/lo：中规格；</li>
<li>audio/hi：高规格。</li>
        :rtype: str
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def Bitrate(self):
        r"""码率，单位为 bps。
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Size(self):
        r"""文件大小，单位为字节。
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size


    def _deserialize(self, params):
        self._Definition = params.get("Definition")
        self._Bitrate = params.get("Bitrate")
        self._Size = params.get("Size")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicDetailInfo(AbstractModel):
    r"""即使广播曲库歌曲信息详情列表

    """

    def __init__(self):
        r"""
        :param _KTVMusicBaseInfo: 即使广播曲库歌曲基础信息
        :type KTVMusicBaseInfo: :class:`tencentcloud.ame.v20190916.models.KTVMusicBaseInfo`
        :param _PlayToken: 播放凭证
        :type PlayToken: str
        :param _LyricsUrl: 歌词下载地址
        :type LyricsUrl: str
        :param _DefinitionInfoSet: 歌曲规格信息列表
        :type DefinitionInfoSet: list of KTVMusicDefinitionInfo
        :param _MidiJsonUrl: 音高数据文件下载地址
        :type MidiJsonUrl: str
        :param _ChorusClipSet: 副歌片段数据列表
        :type ChorusClipSet: list of ChorusClip
        :param _PreludeInterval: 前奏间隔，单位：毫秒；注：若参数返回为0则无人声部分
        :type PreludeInterval: int
        """
        self._KTVMusicBaseInfo = None
        self._PlayToken = None
        self._LyricsUrl = None
        self._DefinitionInfoSet = None
        self._MidiJsonUrl = None
        self._ChorusClipSet = None
        self._PreludeInterval = None

    @property
    def KTVMusicBaseInfo(self):
        r"""即使广播曲库歌曲基础信息
        :rtype: :class:`tencentcloud.ame.v20190916.models.KTVMusicBaseInfo`
        """
        return self._KTVMusicBaseInfo

    @KTVMusicBaseInfo.setter
    def KTVMusicBaseInfo(self, KTVMusicBaseInfo):
        self._KTVMusicBaseInfo = KTVMusicBaseInfo

    @property
    def PlayToken(self):
        r"""播放凭证
        :rtype: str
        """
        return self._PlayToken

    @PlayToken.setter
    def PlayToken(self, PlayToken):
        self._PlayToken = PlayToken

    @property
    def LyricsUrl(self):
        r"""歌词下载地址
        :rtype: str
        """
        return self._LyricsUrl

    @LyricsUrl.setter
    def LyricsUrl(self, LyricsUrl):
        self._LyricsUrl = LyricsUrl

    @property
    def DefinitionInfoSet(self):
        r"""歌曲规格信息列表
        :rtype: list of KTVMusicDefinitionInfo
        """
        return self._DefinitionInfoSet

    @DefinitionInfoSet.setter
    def DefinitionInfoSet(self, DefinitionInfoSet):
        self._DefinitionInfoSet = DefinitionInfoSet

    @property
    def MidiJsonUrl(self):
        r"""音高数据文件下载地址
        :rtype: str
        """
        return self._MidiJsonUrl

    @MidiJsonUrl.setter
    def MidiJsonUrl(self, MidiJsonUrl):
        self._MidiJsonUrl = MidiJsonUrl

    @property
    def ChorusClipSet(self):
        r"""副歌片段数据列表
        :rtype: list of ChorusClip
        """
        return self._ChorusClipSet

    @ChorusClipSet.setter
    def ChorusClipSet(self, ChorusClipSet):
        self._ChorusClipSet = ChorusClipSet

    @property
    def PreludeInterval(self):
        r"""前奏间隔，单位：毫秒；注：若参数返回为0则无人声部分
        :rtype: int
        """
        return self._PreludeInterval

    @PreludeInterval.setter
    def PreludeInterval(self, PreludeInterval):
        self._PreludeInterval = PreludeInterval


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self._KTVMusicBaseInfo = KTVMusicBaseInfo()
            self._KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        self._PlayToken = params.get("PlayToken")
        self._LyricsUrl = params.get("LyricsUrl")
        if params.get("DefinitionInfoSet") is not None:
            self._DefinitionInfoSet = []
            for item in params.get("DefinitionInfoSet"):
                obj = KTVMusicDefinitionInfo()
                obj._deserialize(item)
                self._DefinitionInfoSet.append(obj)
        self._MidiJsonUrl = params.get("MidiJsonUrl")
        if params.get("ChorusClipSet") is not None:
            self._ChorusClipSet = []
            for item in params.get("ChorusClipSet"):
                obj = ChorusClip()
                obj._deserialize(item)
                self._ChorusClipSet.append(obj)
        self._PreludeInterval = params.get("PreludeInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicTagGroup(AbstractModel):
    r"""即使广播曲库歌曲标签分组信息

    """

    def __init__(self):
        r"""
        :param _EnglishGroupName: 标签分组英文名
        :type EnglishGroupName: str
        :param _ChineseGroupName: 标签分组中文名
        :type ChineseGroupName: str
        :param _TagSet: 标签分类下标签列表
        :type TagSet: list of KTVMusicTagInfo
        """
        self._EnglishGroupName = None
        self._ChineseGroupName = None
        self._TagSet = None

    @property
    def EnglishGroupName(self):
        r"""标签分组英文名
        :rtype: str
        """
        return self._EnglishGroupName

    @EnglishGroupName.setter
    def EnglishGroupName(self, EnglishGroupName):
        self._EnglishGroupName = EnglishGroupName

    @property
    def ChineseGroupName(self):
        r"""标签分组中文名
        :rtype: str
        """
        return self._ChineseGroupName

    @ChineseGroupName.setter
    def ChineseGroupName(self, ChineseGroupName):
        self._ChineseGroupName = ChineseGroupName

    @property
    def TagSet(self):
        r"""标签分类下标签列表
        :rtype: list of KTVMusicTagInfo
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._EnglishGroupName = params.get("EnglishGroupName")
        self._ChineseGroupName = params.get("ChineseGroupName")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = KTVMusicTagInfo()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicTagInfo(AbstractModel):
    r"""即使广播曲库歌曲标签信息

    """

    def __init__(self):
        r"""
        :param _TagId: 标签Id
        :type TagId: str
        :param _TagName: 标签
        :type TagName: str
        """
        self._TagId = None
        self._TagName = None

    @property
    def TagId(self):
        r"""标签Id
        :rtype: str
        """
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId

    @property
    def TagName(self):
        r"""标签
        :rtype: str
        """
        return self._TagName

    @TagName.setter
    def TagName(self, TagName):
        self._TagName = TagName


    def _deserialize(self, params):
        self._TagId = params.get("TagId")
        self._TagName = params.get("TagName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicTopInfo(AbstractModel):
    r"""排行榜结构

    """

    def __init__(self):
        r"""
        :param _MusicId: 歌曲Id
        :type MusicId: str
        :param _Name: 歌曲名称
        :type Name: str
        :param _SingerInfoSet: 歌手名称列表
        :type SingerInfoSet: list of KTVSingerBaseInfo
        :param _LyricistSet: 歌词名称列表
        :type LyricistSet: list of str
        :param _ComposerSet: 作曲列表
        :type ComposerSet: list of str
        :param _TagSet: 标签列表
        :type TagSet: list of str
        :param _Duration: 播放时长
        :type Duration: int
        """
        self._MusicId = None
        self._Name = None
        self._SingerInfoSet = None
        self._LyricistSet = None
        self._ComposerSet = None
        self._TagSet = None
        self._Duration = None

    @property
    def MusicId(self):
        r"""歌曲Id
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def Name(self):
        r"""歌曲名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SingerInfoSet(self):
        r"""歌手名称列表
        :rtype: list of KTVSingerBaseInfo
        """
        return self._SingerInfoSet

    @SingerInfoSet.setter
    def SingerInfoSet(self, SingerInfoSet):
        self._SingerInfoSet = SingerInfoSet

    @property
    def LyricistSet(self):
        r"""歌词名称列表
        :rtype: list of str
        """
        return self._LyricistSet

    @LyricistSet.setter
    def LyricistSet(self, LyricistSet):
        self._LyricistSet = LyricistSet

    @property
    def ComposerSet(self):
        r"""作曲列表
        :rtype: list of str
        """
        return self._ComposerSet

    @ComposerSet.setter
    def ComposerSet(self, ComposerSet):
        self._ComposerSet = ComposerSet

    @property
    def TagSet(self):
        r"""标签列表
        :rtype: list of str
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Duration(self):
        r"""播放时长
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._Name = params.get("Name")
        if params.get("SingerInfoSet") is not None:
            self._SingerInfoSet = []
            for item in params.get("SingerInfoSet"):
                obj = KTVSingerBaseInfo()
                obj._deserialize(item)
                self._SingerInfoSet.append(obj)
        self._LyricistSet = params.get("LyricistSet")
        self._ComposerSet = params.get("ComposerSet")
        self._TagSet = params.get("TagSet")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVPlaylistBaseInfo(AbstractModel):
    r"""推荐歌单基础信息

    """

    def __init__(self):
        r"""
        :param _PlaylistId: 歌单Id
        :type PlaylistId: str
        :param _Title: 歌单标题
        :type Title: str
        :param _Description: 歌单介绍
        :type Description: str
        :param _MusicNum: 歌曲数量
        :type MusicNum: int
        """
        self._PlaylistId = None
        self._Title = None
        self._Description = None
        self._MusicNum = None

    @property
    def PlaylistId(self):
        r"""歌单Id
        :rtype: str
        """
        return self._PlaylistId

    @PlaylistId.setter
    def PlaylistId(self, PlaylistId):
        self._PlaylistId = PlaylistId

    @property
    def Title(self):
        r"""歌单标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Description(self):
        r"""歌单介绍
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MusicNum(self):
        r"""歌曲数量
        :rtype: int
        """
        return self._MusicNum

    @MusicNum.setter
    def MusicNum(self, MusicNum):
        self._MusicNum = MusicNum


    def _deserialize(self, params):
        self._PlaylistId = params.get("PlaylistId")
        self._Title = params.get("Title")
        self._Description = params.get("Description")
        self._MusicNum = params.get("MusicNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVRobotInfo(AbstractModel):
    r"""机器人信息

    """

    def __init__(self):
        r"""
        :param _RobotId: 机器人Id。
        :type RobotId: str
        :param _Status: 状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :type Status: str
        :param _Playlists: 播放列表。
        :type Playlists: list of str
        :param _CurIndex: 当前歌单索引位置。
        :type CurIndex: int
        :param _Position: 播放进度，单位：毫秒。
        :type Position: int
        :param _SetAudioParamInput: 音频参数。
        :type SetAudioParamInput: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        :param _JoinRoomInput: 进房信息。
        :type JoinRoomInput: :class:`tencentcloud.ame.v20190916.models.JoinRoomInput`
        :param _RTCSystem: RTC厂商类型，取值有：
<li>TRTC</li>
        :type RTCSystem: str
        :param _SetPlayModeInput: 播放模式，PlayMode取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :type SetPlayModeInput: :class:`tencentcloud.ame.v20190916.models.SetPlayModeCommandInput`
        :param _SetVolumeInput: <del>音量，范围 0~100，默认为 50。</del>（已废弃，请采用 SetRealVolumeInput ）
        :type SetVolumeInput: :class:`tencentcloud.ame.v20190916.models.SetVolumeCommandInput`
        :param _SetRealVolumeInput: 真实音量，范围 0~100，默认为 50。
        :type SetRealVolumeInput: :class:`tencentcloud.ame.v20190916.models.SetRealVolumeCommandInput`
        """
        self._RobotId = None
        self._Status = None
        self._Playlists = None
        self._CurIndex = None
        self._Position = None
        self._SetAudioParamInput = None
        self._JoinRoomInput = None
        self._RTCSystem = None
        self._SetPlayModeInput = None
        self._SetVolumeInput = None
        self._SetRealVolumeInput = None

    @property
    def RobotId(self):
        r"""机器人Id。
        :rtype: str
        """
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId

    @property
    def Status(self):
        r"""状态，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>Destroy：销毁</li>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Playlists(self):
        r"""播放列表。
        :rtype: list of str
        """
        return self._Playlists

    @Playlists.setter
    def Playlists(self, Playlists):
        self._Playlists = Playlists

    @property
    def CurIndex(self):
        r"""当前歌单索引位置。
        :rtype: int
        """
        return self._CurIndex

    @CurIndex.setter
    def CurIndex(self, CurIndex):
        self._CurIndex = CurIndex

    @property
    def Position(self):
        r"""播放进度，单位：毫秒。
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def SetAudioParamInput(self):
        r"""音频参数。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        """
        return self._SetAudioParamInput

    @SetAudioParamInput.setter
    def SetAudioParamInput(self, SetAudioParamInput):
        self._SetAudioParamInput = SetAudioParamInput

    @property
    def JoinRoomInput(self):
        r"""进房信息。
        :rtype: :class:`tencentcloud.ame.v20190916.models.JoinRoomInput`
        """
        return self._JoinRoomInput

    @JoinRoomInput.setter
    def JoinRoomInput(self, JoinRoomInput):
        self._JoinRoomInput = JoinRoomInput

    @property
    def RTCSystem(self):
        r"""RTC厂商类型，取值有：
<li>TRTC</li>
        :rtype: str
        """
        return self._RTCSystem

    @RTCSystem.setter
    def RTCSystem(self, RTCSystem):
        self._RTCSystem = RTCSystem

    @property
    def SetPlayModeInput(self):
        r"""播放模式，PlayMode取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetPlayModeCommandInput`
        """
        return self._SetPlayModeInput

    @SetPlayModeInput.setter
    def SetPlayModeInput(self, SetPlayModeInput):
        self._SetPlayModeInput = SetPlayModeInput

    @property
    def SetVolumeInput(self):
        r"""<del>音量，范围 0~100，默认为 50。</del>（已废弃，请采用 SetRealVolumeInput ）
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetVolumeCommandInput`
        """
        return self._SetVolumeInput

    @SetVolumeInput.setter
    def SetVolumeInput(self, SetVolumeInput):
        self._SetVolumeInput = SetVolumeInput

    @property
    def SetRealVolumeInput(self):
        r"""真实音量，范围 0~100，默认为 50。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetRealVolumeCommandInput`
        """
        return self._SetRealVolumeInput

    @SetRealVolumeInput.setter
    def SetRealVolumeInput(self, SetRealVolumeInput):
        self._SetRealVolumeInput = SetRealVolumeInput


    def _deserialize(self, params):
        self._RobotId = params.get("RobotId")
        self._Status = params.get("Status")
        self._Playlists = params.get("Playlists")
        self._CurIndex = params.get("CurIndex")
        self._Position = params.get("Position")
        if params.get("SetAudioParamInput") is not None:
            self._SetAudioParamInput = SetAudioParamCommandInput()
            self._SetAudioParamInput._deserialize(params.get("SetAudioParamInput"))
        if params.get("JoinRoomInput") is not None:
            self._JoinRoomInput = JoinRoomInput()
            self._JoinRoomInput._deserialize(params.get("JoinRoomInput"))
        self._RTCSystem = params.get("RTCSystem")
        if params.get("SetPlayModeInput") is not None:
            self._SetPlayModeInput = SetPlayModeCommandInput()
            self._SetPlayModeInput._deserialize(params.get("SetPlayModeInput"))
        if params.get("SetVolumeInput") is not None:
            self._SetVolumeInput = SetVolumeCommandInput()
            self._SetVolumeInput._deserialize(params.get("SetVolumeInput"))
        if params.get("SetRealVolumeInput") is not None:
            self._SetRealVolumeInput = SetRealVolumeCommandInput()
            self._SetRealVolumeInput._deserialize(params.get("SetRealVolumeInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVSingerBaseInfo(AbstractModel):
    r"""KTV 歌手基础信息

    """

    def __init__(self):
        r"""
        :param _SingerId: 歌手id
        :type SingerId: str
        :param _Name: 歌手名
        :type Name: str
        """
        self._SingerId = None
        self._Name = None

    @property
    def SingerId(self):
        r"""歌手id
        :rtype: str
        """
        return self._SingerId

    @SingerId.setter
    def SingerId(self, SingerId):
        self._SingerId = SingerId

    @property
    def Name(self):
        r"""歌手名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._SingerId = params.get("SingerId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVSingerCategoryInfo(AbstractModel):
    r"""KTV歌手分类信息

    """

    def __init__(self):
        r"""
        :param _ChineseName: 分类中文名
        :type ChineseName: str
        :param _EnglishName: 分类英文名
        :type EnglishName: str
        """
        self._ChineseName = None
        self._EnglishName = None

    @property
    def ChineseName(self):
        r"""分类中文名
        :rtype: str
        """
        return self._ChineseName

    @ChineseName.setter
    def ChineseName(self, ChineseName):
        self._ChineseName = ChineseName

    @property
    def EnglishName(self):
        r"""分类英文名
        :rtype: str
        """
        return self._EnglishName

    @EnglishName.setter
    def EnglishName(self, EnglishName):
        self._EnglishName = EnglishName


    def _deserialize(self, params):
        self._ChineseName = params.get("ChineseName")
        self._EnglishName = params.get("EnglishName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVSingerInfo(AbstractModel):
    r"""直播互动歌曲的歌手信息。

    """

    def __init__(self):
        r"""
        :param _SingerId: 歌手id
        :type SingerId: str
        :param _Name: 歌手名
        :type Name: str
        :param _Gender: 歌手性别: 男，女，组合
        :type Gender: str
        :param _Area: 地区: 大陆，港台，欧美，日本
        :type Area: str
        :param _MusicCount: 歌曲数
        :type MusicCount: int
        :param _PlayCount: 歌曲总播放次数
        :type PlayCount: int
        """
        self._SingerId = None
        self._Name = None
        self._Gender = None
        self._Area = None
        self._MusicCount = None
        self._PlayCount = None

    @property
    def SingerId(self):
        r"""歌手id
        :rtype: str
        """
        return self._SingerId

    @SingerId.setter
    def SingerId(self, SingerId):
        self._SingerId = SingerId

    @property
    def Name(self):
        r"""歌手名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Gender(self):
        r"""歌手性别: 男，女，组合
        :rtype: str
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Area(self):
        r"""地区: 大陆，港台，欧美，日本
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def MusicCount(self):
        r"""歌曲数
        :rtype: int
        """
        return self._MusicCount

    @MusicCount.setter
    def MusicCount(self, MusicCount):
        self._MusicCount = MusicCount

    @property
    def PlayCount(self):
        r"""歌曲总播放次数
        :rtype: int
        """
        return self._PlayCount

    @PlayCount.setter
    def PlayCount(self, PlayCount):
        self._PlayCount = PlayCount


    def _deserialize(self, params):
        self._SingerId = params.get("SingerId")
        self._Name = params.get("Name")
        self._Gender = params.get("Gender")
        self._Area = params.get("Area")
        self._MusicCount = params.get("MusicCount")
        self._PlayCount = params.get("PlayCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVSuggestionInfo(AbstractModel):
    r"""即使广播曲库联想词信息

    """

    def __init__(self):
        r"""
        :param _Suggestion: 联想词
        :type Suggestion: str
        """
        self._Suggestion = None

    @property
    def Suggestion(self):
        r"""联想词
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion


    def _deserialize(self, params):
        self._Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Lyric(AbstractModel):
    r"""歌词信息

    """

    def __init__(self):
        r"""
        :param _Url: 歌词cdn地址
        :type Url: str
        :param _FileNameExt: 歌词后缀名
        :type FileNameExt: str
        :param _SubItemType: 歌词类型
        :type SubItemType: str
        """
        self._Url = None
        self._FileNameExt = None
        self._SubItemType = None

    @property
    def Url(self):
        r"""歌词cdn地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FileNameExt(self):
        r"""歌词后缀名
        :rtype: str
        """
        return self._FileNameExt

    @FileNameExt.setter
    def FileNameExt(self, FileNameExt):
        self._FileNameExt = FileNameExt

    @property
    def SubItemType(self):
        r"""歌词类型
        :rtype: str
        """
        return self._SubItemType

    @SubItemType.setter
    def SubItemType(self, SubItemType):
        self._SubItemType = SubItemType


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._FileNameExt = params.get("FileNameExt")
        self._SubItemType = params.get("SubItemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMusicOnShelvesRequest(AbstractModel):
    r"""ModifyMusicOnShelves请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicDetailInfos: 歌曲变更信息
        :type MusicDetailInfos: :class:`tencentcloud.ame.v20190916.models.MusicDetailInfo`
        :param _AmeKey: ame对接资源方密钥
        :type AmeKey: str
        """
        self._MusicDetailInfos = None
        self._AmeKey = None

    @property
    def MusicDetailInfos(self):
        r"""歌曲变更信息
        :rtype: :class:`tencentcloud.ame.v20190916.models.MusicDetailInfo`
        """
        return self._MusicDetailInfos

    @MusicDetailInfos.setter
    def MusicDetailInfos(self, MusicDetailInfos):
        self._MusicDetailInfos = MusicDetailInfos

    @property
    def AmeKey(self):
        r"""ame对接资源方密钥
        :rtype: str
        """
        return self._AmeKey

    @AmeKey.setter
    def AmeKey(self, AmeKey):
        self._AmeKey = AmeKey


    def _deserialize(self, params):
        if params.get("MusicDetailInfos") is not None:
            self._MusicDetailInfos = MusicDetailInfo()
            self._MusicDetailInfos._deserialize(params.get("MusicDetailInfos"))
        self._AmeKey = params.get("AmeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMusicOnShelvesResponse(AbstractModel):
    r"""ModifyMusicOnShelves返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Music(AbstractModel):
    r"""音乐详情

    """

    def __init__(self):
        r"""
        :param _Url: 音乐播放链接相对路径，必须通过在正版曲库直通车控制台上登记的域名进行拼接。
        :type Url: str
        :param _FileSize: 音频文件大小
        :type FileSize: int
        :param _FileExtension: 音频文件类型
        :type FileExtension: str
        :param _AuditionBegin: Song fragment start.试听片段开始时间，试听时长为auditionEnd-auditionBegin
Unit :ms
        :type AuditionBegin: int
        :param _AuditionEnd: Song fragment end.试听片段结束时间, 试听时长为auditionEnd-auditionBegin
Unit :ms
        :type AuditionEnd: int
        :param _FullUrl: 音乐播放链接全路径，前提是在正版曲库直通车控制台添加过域名，否则返回空字符。
如果添加过多个域名只返回第一个添加域名的播放全路径。
        :type FullUrl: str
        """
        self._Url = None
        self._FileSize = None
        self._FileExtension = None
        self._AuditionBegin = None
        self._AuditionEnd = None
        self._FullUrl = None

    @property
    def Url(self):
        r"""音乐播放链接相对路径，必须通过在正版曲库直通车控制台上登记的域名进行拼接。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def FileSize(self):
        r"""音频文件大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileExtension(self):
        r"""音频文件类型
        :rtype: str
        """
        return self._FileExtension

    @FileExtension.setter
    def FileExtension(self, FileExtension):
        self._FileExtension = FileExtension

    @property
    def AuditionBegin(self):
        r"""Song fragment start.试听片段开始时间，试听时长为auditionEnd-auditionBegin
Unit :ms
        :rtype: int
        """
        return self._AuditionBegin

    @AuditionBegin.setter
    def AuditionBegin(self, AuditionBegin):
        self._AuditionBegin = AuditionBegin

    @property
    def AuditionEnd(self):
        r"""Song fragment end.试听片段结束时间, 试听时长为auditionEnd-auditionBegin
Unit :ms
        :rtype: int
        """
        return self._AuditionEnd

    @AuditionEnd.setter
    def AuditionEnd(self, AuditionEnd):
        self._AuditionEnd = AuditionEnd

    @property
    def FullUrl(self):
        r"""音乐播放链接全路径，前提是在正版曲库直通车控制台添加过域名，否则返回空字符。
如果添加过多个域名只返回第一个添加域名的播放全路径。
        :rtype: str
        """
        return self._FullUrl

    @FullUrl.setter
    def FullUrl(self, FullUrl):
        self._FullUrl = FullUrl


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._FileSize = params.get("FileSize")
        self._FileExtension = params.get("FileExtension")
        self._AuditionBegin = params.get("AuditionBegin")
        self._AuditionEnd = params.get("AuditionEnd")
        self._FullUrl = params.get("FullUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicDetailInfo(AbstractModel):
    r"""歌曲变更细节

    """

    def __init__(self):
        r"""
        :param _MusicId: 资源方音乐Id
        :type MusicId: str
        :param _AmeId: 资源方识别信息
        :type AmeId: str
        :param _Tags: 分类标签
        :type Tags: list of str
        :param _HitWords: 关键词
        :type HitWords: list of str
        :param _Bpm: 节奏信息
        :type Bpm: int
        :param _Score: 商业化权益
        :type Score: float
        :param _Scene: 应用歌曲信息,1.图文/短视频,2.网络直播,3.网络电台FM,4.免费游戏,5.商业游戏,6.网店网站设计,7.广告营销,8.网络长视频
        :type Scene: list of str
        :param _Region: 应用地域,1. 中国大陆,2. 中国含港澳台,3. 全球
        :type Region: list of str
        :param _AuthPeriod: 授权时间,1. 1年, 5. 随片永久
        :type AuthPeriod: str
        :param _Commercialization: 商业化授权，1. 支持商业化 ,2. 不支持商业化
        :type Commercialization: str
        :param _Platform: 跨平台传播，1. 支持跨平台传播 ,2. 不支持跨平台传播
        :type Platform: str
        :param _Channel: 传播渠道
        :type Channel: str
        """
        self._MusicId = None
        self._AmeId = None
        self._Tags = None
        self._HitWords = None
        self._Bpm = None
        self._Score = None
        self._Scene = None
        self._Region = None
        self._AuthPeriod = None
        self._Commercialization = None
        self._Platform = None
        self._Channel = None

    @property
    def MusicId(self):
        r"""资源方音乐Id
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def AmeId(self):
        r"""资源方识别信息
        :rtype: str
        """
        return self._AmeId

    @AmeId.setter
    def AmeId(self, AmeId):
        self._AmeId = AmeId

    @property
    def Tags(self):
        r"""分类标签
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HitWords(self):
        r"""关键词
        :rtype: list of str
        """
        return self._HitWords

    @HitWords.setter
    def HitWords(self, HitWords):
        self._HitWords = HitWords

    @property
    def Bpm(self):
        r"""节奏信息
        :rtype: int
        """
        return self._Bpm

    @Bpm.setter
    def Bpm(self, Bpm):
        self._Bpm = Bpm

    @property
    def Score(self):
        r"""商业化权益
        :rtype: float
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Scene(self):
        r"""应用歌曲信息,1.图文/短视频,2.网络直播,3.网络电台FM,4.免费游戏,5.商业游戏,6.网店网站设计,7.广告营销,8.网络长视频
        :rtype: list of str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def Region(self):
        r"""应用地域,1. 中国大陆,2. 中国含港澳台,3. 全球
        :rtype: list of str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AuthPeriod(self):
        r"""授权时间,1. 1年, 5. 随片永久
        :rtype: str
        """
        return self._AuthPeriod

    @AuthPeriod.setter
    def AuthPeriod(self, AuthPeriod):
        self._AuthPeriod = AuthPeriod

    @property
    def Commercialization(self):
        r"""商业化授权，1. 支持商业化 ,2. 不支持商业化
        :rtype: str
        """
        return self._Commercialization

    @Commercialization.setter
    def Commercialization(self, Commercialization):
        self._Commercialization = Commercialization

    @property
    def Platform(self):
        r"""跨平台传播，1. 支持跨平台传播 ,2. 不支持跨平台传播
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Channel(self):
        r"""传播渠道
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._AmeId = params.get("AmeId")
        self._Tags = params.get("Tags")
        self._HitWords = params.get("HitWords")
        self._Bpm = params.get("Bpm")
        self._Score = params.get("Score")
        self._Scene = params.get("Scene")
        self._Region = params.get("Region")
        self._AuthPeriod = params.get("AuthPeriod")
        self._Commercialization = params.get("Commercialization")
        self._Platform = params.get("Platform")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicOpenDetail(AbstractModel):
    r"""对外开放信息

    """

    def __init__(self):
        r"""
        :param _MusicId: 音乐Id
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicId: str
        :param _AlbumName: 专辑名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumName: str
        :param _AlbumImageUrl: 专辑图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :type AlbumImageUrl: str
        :param _MusicName: 音乐名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicName: str
        :param _MusicImageUrl: 音乐图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :type MusicImageUrl: str
        :param _Singers: 歌手
注意：此字段可能返回 null，表示取不到有效值。
        :type Singers: list of str
        :param _Duration: 播放时长
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _LyricUrl: 歌词url
注意：此字段可能返回 null，表示取不到有效值。
        :type LyricUrl: str
        :param _WaveformUrl: 波形图url
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveformUrl: str
        """
        self._MusicId = None
        self._AlbumName = None
        self._AlbumImageUrl = None
        self._MusicName = None
        self._MusicImageUrl = None
        self._Singers = None
        self._Duration = None
        self._Tags = None
        self._LyricUrl = None
        self._WaveformUrl = None

    @property
    def MusicId(self):
        r"""音乐Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def AlbumName(self):
        r"""专辑名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlbumName

    @AlbumName.setter
    def AlbumName(self, AlbumName):
        self._AlbumName = AlbumName

    @property
    def AlbumImageUrl(self):
        r"""专辑图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlbumImageUrl

    @AlbumImageUrl.setter
    def AlbumImageUrl(self, AlbumImageUrl):
        self._AlbumImageUrl = AlbumImageUrl

    @property
    def MusicName(self):
        r"""音乐名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MusicName

    @MusicName.setter
    def MusicName(self, MusicName):
        self._MusicName = MusicName

    @property
    def MusicImageUrl(self):
        r"""音乐图片路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MusicImageUrl

    @MusicImageUrl.setter
    def MusicImageUrl(self, MusicImageUrl):
        self._MusicImageUrl = MusicImageUrl

    @property
    def Singers(self):
        r"""歌手
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Singers

    @Singers.setter
    def Singers(self, Singers):
        self._Singers = Singers

    @property
    def Duration(self):
        r"""播放时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Tags(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LyricUrl(self):
        r"""歌词url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LyricUrl

    @LyricUrl.setter
    def LyricUrl(self, LyricUrl):
        self._LyricUrl = LyricUrl

    @property
    def WaveformUrl(self):
        r"""波形图url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WaveformUrl

    @WaveformUrl.setter
    def WaveformUrl(self, WaveformUrl):
        self._WaveformUrl = WaveformUrl


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._AlbumName = params.get("AlbumName")
        self._AlbumImageUrl = params.get("AlbumImageUrl")
        self._MusicName = params.get("MusicName")
        self._MusicImageUrl = params.get("MusicImageUrl")
        self._Singers = params.get("Singers")
        self._Duration = params.get("Duration")
        self._Tags = params.get("Tags")
        self._LyricUrl = params.get("LyricUrl")
        self._WaveformUrl = params.get("WaveformUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicStatus(AbstractModel):
    r"""返回单曲页面歌曲是否在售状态

    """

    def __init__(self):
        r"""
        :param _MusicId: 歌曲Id
        :type MusicId: str
        :param _SaleStatus: 在售状态,0为在售，1为临时下架，2为永久下架
        :type SaleStatus: int
        """
        self._MusicId = None
        self._SaleStatus = None

    @property
    def MusicId(self):
        r"""歌曲Id
        :rtype: str
        """
        return self._MusicId

    @MusicId.setter
    def MusicId(self, MusicId):
        self._MusicId = MusicId

    @property
    def SaleStatus(self):
        r"""在售状态,0为在售，1为临时下架，2为永久下架
        :rtype: int
        """
        return self._SaleStatus

    @SaleStatus.setter
    def SaleStatus(self, SaleStatus):
        self._SaleStatus = SaleStatus


    def _deserialize(self, params):
        self._MusicId = params.get("MusicId")
        self._SaleStatus = params.get("SaleStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineMusicDetail(AbstractModel):
    r"""曲库包已下架歌曲详细信息

    """

    def __init__(self):
        r"""
        :param _ItemId: 歌曲Id
        :type ItemId: str
        :param _MusicName: 歌曲名称
        :type MusicName: str
        :param _OffRemark: 不可用原因
        :type OffRemark: str
        :param _OffTime: 不可用时间
        :type OffTime: str
        """
        self._ItemId = None
        self._MusicName = None
        self._OffRemark = None
        self._OffTime = None

    @property
    def ItemId(self):
        r"""歌曲Id
        :rtype: str
        """
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def MusicName(self):
        r"""歌曲名称
        :rtype: str
        """
        return self._MusicName

    @MusicName.setter
    def MusicName(self, MusicName):
        self._MusicName = MusicName

    @property
    def OffRemark(self):
        r"""不可用原因
        :rtype: str
        """
        return self._OffRemark

    @OffRemark.setter
    def OffRemark(self, OffRemark):
        self._OffRemark = OffRemark

    @property
    def OffTime(self):
        r"""不可用时间
        :rtype: str
        """
        return self._OffTime

    @OffTime.setter
    def OffTime(self, OffTime):
        self._OffTime = OffTime


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._MusicName = params.get("MusicName")
        self._OffRemark = params.get("OffRemark")
        self._OffTime = params.get("OffTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Package(AbstractModel):
    r"""曲库包信息

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单id
        :type OrderId: str
        :param _Name: 曲库包名称
        :type Name: str
        :param _AuthorizedArea: 授权地区-global: 全球  CN: 中国
        :type AuthorizedArea: str
        :param _AuthorizedLimit: 授权次数
        :type AuthorizedLimit: int
        :param _TermOfValidity: 套餐有效期，单位:天
        :type TermOfValidity: int
        :param _Commercial: 0:不可商业化；1:可商业化
        :type Commercial: int
        :param _PackagePrice: 套餐价格，单位：元
        :type PackagePrice: float
        :param _EffectTime: 生效开始时间,格式yyyy-MM-dd HH:mm:ss
        :type EffectTime: str
        :param _ExpireTime: 生效结束时间,格式yyyy-MM-dd HH:mm:ss
        :type ExpireTime: str
        :param _UsedCount: 剩余授权次数
        :type UsedCount: int
        :param _UseRanges: 曲库包用途信息
        :type UseRanges: list of UseRange
        """
        self._OrderId = None
        self._Name = None
        self._AuthorizedArea = None
        self._AuthorizedLimit = None
        self._TermOfValidity = None
        self._Commercial = None
        self._PackagePrice = None
        self._EffectTime = None
        self._ExpireTime = None
        self._UsedCount = None
        self._UseRanges = None

    @property
    def OrderId(self):
        r"""订单id
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def Name(self):
        r"""曲库包名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AuthorizedArea(self):
        r"""授权地区-global: 全球  CN: 中国
        :rtype: str
        """
        return self._AuthorizedArea

    @AuthorizedArea.setter
    def AuthorizedArea(self, AuthorizedArea):
        self._AuthorizedArea = AuthorizedArea

    @property
    def AuthorizedLimit(self):
        r"""授权次数
        :rtype: int
        """
        return self._AuthorizedLimit

    @AuthorizedLimit.setter
    def AuthorizedLimit(self, AuthorizedLimit):
        self._AuthorizedLimit = AuthorizedLimit

    @property
    def TermOfValidity(self):
        r"""套餐有效期，单位:天
        :rtype: int
        """
        return self._TermOfValidity

    @TermOfValidity.setter
    def TermOfValidity(self, TermOfValidity):
        self._TermOfValidity = TermOfValidity

    @property
    def Commercial(self):
        r"""0:不可商业化；1:可商业化
        :rtype: int
        """
        return self._Commercial

    @Commercial.setter
    def Commercial(self, Commercial):
        self._Commercial = Commercial

    @property
    def PackagePrice(self):
        r"""套餐价格，单位：元
        :rtype: float
        """
        return self._PackagePrice

    @PackagePrice.setter
    def PackagePrice(self, PackagePrice):
        self._PackagePrice = PackagePrice

    @property
    def EffectTime(self):
        r"""生效开始时间,格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._EffectTime

    @EffectTime.setter
    def EffectTime(self, EffectTime):
        self._EffectTime = EffectTime

    @property
    def ExpireTime(self):
        r"""生效结束时间,格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UsedCount(self):
        r"""剩余授权次数
        :rtype: int
        """
        return self._UsedCount

    @UsedCount.setter
    def UsedCount(self, UsedCount):
        self._UsedCount = UsedCount

    @property
    def UseRanges(self):
        r"""曲库包用途信息
        :rtype: list of UseRange
        """
        return self._UseRanges

    @UseRanges.setter
    def UseRanges(self, UseRanges):
        self._UseRanges = UseRanges


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._Name = params.get("Name")
        self._AuthorizedArea = params.get("AuthorizedArea")
        self._AuthorizedLimit = params.get("AuthorizedLimit")
        self._TermOfValidity = params.get("TermOfValidity")
        self._Commercial = params.get("Commercial")
        self._PackagePrice = params.get("PackagePrice")
        self._EffectTime = params.get("EffectTime")
        self._ExpireTime = params.get("ExpireTime")
        self._UsedCount = params.get("UsedCount")
        if params.get("UseRanges") is not None:
            self._UseRanges = []
            for item in params.get("UseRanges"):
                obj = UseRange()
                obj._deserialize(item)
                self._UseRanges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageItem(AbstractModel):
    r"""曲库包歌曲信息

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单id
        :type OrderId: str
        :param _TrackName: 歌曲名
        :type TrackName: str
        :param _ItemID: 歌曲ID
        :type ItemID: str
        :param _Img: 专辑图片
        :type Img: str
        :param _ArtistName: 歌手名
        :type ArtistName: str
        :param _Duration: 歌曲时长
        :type Duration: str
        :param _AuthorizedArea: 授权区域，global: 全球 CN: 中国
        :type AuthorizedArea: str
        :param _Tags: 标签数组
        :type Tags: list of str
        """
        self._OrderId = None
        self._TrackName = None
        self._ItemID = None
        self._Img = None
        self._ArtistName = None
        self._Duration = None
        self._AuthorizedArea = None
        self._Tags = None

    @property
    def OrderId(self):
        r"""订单id
        :rtype: str
        """
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def TrackName(self):
        r"""歌曲名
        :rtype: str
        """
        return self._TrackName

    @TrackName.setter
    def TrackName(self, TrackName):
        self._TrackName = TrackName

    @property
    def ItemID(self):
        r"""歌曲ID
        :rtype: str
        """
        return self._ItemID

    @ItemID.setter
    def ItemID(self, ItemID):
        self._ItemID = ItemID

    @property
    def Img(self):
        r"""专辑图片
        :rtype: str
        """
        return self._Img

    @Img.setter
    def Img(self, Img):
        self._Img = Img

    @property
    def ArtistName(self):
        r"""歌手名
        :rtype: str
        """
        return self._ArtistName

    @ArtistName.setter
    def ArtistName(self, ArtistName):
        self._ArtistName = ArtistName

    @property
    def Duration(self):
        r"""歌曲时长
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def AuthorizedArea(self):
        r"""授权区域，global: 全球 CN: 中国
        :rtype: str
        """
        return self._AuthorizedArea

    @AuthorizedArea.setter
    def AuthorizedArea(self, AuthorizedArea):
        self._AuthorizedArea = AuthorizedArea

    @property
    def Tags(self):
        r"""标签数组
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._TrackName = params.get("TrackName")
        self._ItemID = params.get("ItemID")
        self._Img = params.get("Img")
        self._ArtistName = params.get("ArtistName")
        self._Duration = params.get("Duration")
        self._AuthorizedArea = params.get("AuthorizedArea")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayCommandInput(AbstractModel):
    r"""播放指令输入参数

    """

    def __init__(self):
        r"""
        :param _Index: 歌曲位置索引。
        :type Index: int
        """
        self._Index = None

    @property
    def Index(self):
        r"""歌曲位置索引。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMusicOnTheShelvesRequest(AbstractModel):
    r"""PutMusicOnTheShelves请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MusicIds: 资源方歌曲Id
        :type MusicIds: list of str
        """
        self._MusicIds = None

    @property
    def MusicIds(self):
        r"""资源方歌曲Id
        :rtype: list of str
        """
        return self._MusicIds

    @MusicIds.setter
    def MusicIds(self, MusicIds):
        self._MusicIds = MusicIds


    def _deserialize(self, params):
        self._MusicIds = params.get("MusicIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMusicOnTheShelvesResponse(AbstractModel):
    r"""PutMusicOnTheShelves返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessNum: 操作成功数量
        :type SuccessNum: int
        :param _FailedNum: 操作失败数量
        :type FailedNum: int
        :param _FailedMusicIds: 失败歌曲Id
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMusicIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessNum = None
        self._FailedNum = None
        self._FailedMusicIds = None
        self._RequestId = None

    @property
    def SuccessNum(self):
        r"""操作成功数量
        :rtype: int
        """
        return self._SuccessNum

    @SuccessNum.setter
    def SuccessNum(self, SuccessNum):
        self._SuccessNum = SuccessNum

    @property
    def FailedNum(self):
        r"""操作失败数量
        :rtype: int
        """
        return self._FailedNum

    @FailedNum.setter
    def FailedNum(self, FailedNum):
        self._FailedNum = FailedNum

    @property
    def FailedMusicIds(self):
        r"""失败歌曲Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FailedMusicIds

    @FailedMusicIds.setter
    def FailedMusicIds(self, FailedMusicIds):
        self._FailedMusicIds = FailedMusicIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessNum = params.get("SuccessNum")
        self._FailedNum = params.get("FailedNum")
        self._FailedMusicIds = params.get("FailedMusicIds")
        self._RequestId = params.get("RequestId")


class ReportDataRequest(AbstractModel):
    r"""ReportData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportData: 上报数据
注:reportData为客户端压缩后的上报数据进行16进制转换的字符串数据
压缩说明：
a) 上报的json格式字符串通过流的转换（ByteArrayInputStream, java.util.zip.GZIPOutputStream），获取到压缩后的字节数组。
b) 将压缩后的字节数组转成16进制字符串。

reportData由两部分数据组成：
1）report_type（上报类型）
2）data（歌曲上报数据）
不同的report_type对应的data数据结构不一样。

详细说明请参考文档reportdata.docx：
https://github.com/tencentyun/ame-documents
        :type ReportData: str
        """
        self._ReportData = None

    @property
    def ReportData(self):
        r"""上报数据
注:reportData为客户端压缩后的上报数据进行16进制转换的字符串数据
压缩说明：
a) 上报的json格式字符串通过流的转换（ByteArrayInputStream, java.util.zip.GZIPOutputStream），获取到压缩后的字节数组。
b) 将压缩后的字节数组转成16进制字符串。

reportData由两部分数据组成：
1）report_type（上报类型）
2）data（歌曲上报数据）
不同的report_type对应的data数据结构不一样。

详细说明请参考文档reportdata.docx：
https://github.com/tencentyun/ame-documents
        :rtype: str
        """
        return self._ReportData

    @ReportData.setter
    def ReportData(self, ReportData):
        self._ReportData = ReportData


    def _deserialize(self, params):
        self._ReportData = params.get("ReportData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportDataResponse(AbstractModel):
    r"""ReportData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SearchKTVMusicsRequest(AbstractModel):
    r"""SearchKTVMusics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyWord: 搜索关键词
        :type KeyWord: str
        :param _Offset: 分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000。
        :type Offset: int
        :param _Limit: 分页返回的起始偏移量，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :type Limit: int
        :param _Sort: 排序方式。默认按照匹配度排序
<li> Sort.Field 可选 CreateTime</li>
<li> Sort.Order 可选 Desc </li>
<li> 当 KeyWord 不为空时，Sort.Field 字段无效， 搜索结果将以匹配度排序。</li>
        :type Sort: :class:`tencentcloud.ame.v20190916.models.SortBy`
        :param _TagIds: 标签 ID 集合，匹配集合指定所有 ID 。
<li>数组长度限制：10。</li>
        :type TagIds: list of str
        """
        self._KeyWord = None
        self._Offset = None
        self._Limit = None
        self._Sort = None
        self._TagIds = None

    @property
    def KeyWord(self):
        r"""搜索关键词
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord

    @property
    def Offset(self):
        r"""分页返回的起始偏移量，默认值：0。将返回第 Offset 到第 Offset+Limit-1 条。
取值范围：Offset + Limit 不超过5000。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页返回的起始偏移量，默认值：50。将返回第 Offset 到第 Offset+Limit-1 条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Sort(self):
        r"""排序方式。默认按照匹配度排序
<li> Sort.Field 可选 CreateTime</li>
<li> Sort.Order 可选 Desc </li>
<li> 当 KeyWord 不为空时，Sort.Field 字段无效， 搜索结果将以匹配度排序。</li>
        :rtype: :class:`tencentcloud.ame.v20190916.models.SortBy`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def TagIds(self):
        r"""标签 ID 集合，匹配集合指定所有 ID 。
<li>数组长度限制：10。</li>
        :rtype: list of str
        """
        return self._TagIds

    @TagIds.setter
    def TagIds(self, TagIds):
        self._TagIds = TagIds


    def _deserialize(self, params):
        self._KeyWord = params.get("KeyWord")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self._Sort = SortBy()
            self._Sort._deserialize(params.get("Sort"))
        self._TagIds = params.get("TagIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKTVMusicsResponse(AbstractModel):
    r"""SearchKTVMusics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _KTVMusicInfoSet: KTV 曲目列表
        :type KTVMusicInfoSet: list of KTVMusicBaseInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KTVMusicInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KTVMusicInfoSet(self):
        r"""KTV 曲目列表
        :rtype: list of KTVMusicBaseInfo
        """
        return self._KTVMusicInfoSet

    @KTVMusicInfoSet.setter
    def KTVMusicInfoSet(self, KTVMusicInfoSet):
        self._KTVMusicInfoSet = KTVMusicInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KTVMusicInfoSet") is not None:
            self._KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self._KTVMusicInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class SeekCommandInput(AbstractModel):
    r"""调整播放进度指令参数

    """

    def __init__(self):
        r"""
        :param _Position: 播放位置，单位：毫秒。
        :type Position: int
        """
        self._Position = None

    @property
    def Position(self):
        r"""播放位置，单位：毫秒。
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position


    def _deserialize(self, params):
        self._Position = params.get("Position")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageCommandInput(AbstractModel):
    r"""发送自定义信息指令参数

    """

    def __init__(self):
        r"""
        :param _Message: 自定义消息，json格式字符串。
        :type Message: str
        :param _Repeat: 消息重复次数，默认为 1。
        :type Repeat: int
        """
        self._Message = None
        self._Repeat = None

    @property
    def Message(self):
        r"""自定义消息，json格式字符串。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Repeat(self):
        r"""消息重复次数，默认为 1。
        :rtype: int
        """
        return self._Repeat

    @Repeat.setter
    def Repeat(self, Repeat):
        self._Repeat = Repeat


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Repeat = params.get("Repeat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAudioParamCommandInput(AbstractModel):
    r"""音频参数信息

    """

    def __init__(self):
        r"""
        :param _Definition: 规格，取值有：
<li>audio/mi：低规格</li>
<li>audio/lo：中规格</li>
<li>audio/hi：高规格</li>
        :type Definition: str
        :param _Type: 音频类型，取值有：
<li>Original：原唱</li>
<li>Accompaniment：伴奏</li>
        :type Type: str
        """
        self._Definition = None
        self._Type = None

    @property
    def Definition(self):
        r"""规格，取值有：
<li>audio/mi：低规格</li>
<li>audio/lo：中规格</li>
<li>audio/hi：高规格</li>
        :rtype: str
        """
        return self._Definition

    @Definition.setter
    def Definition(self, Definition):
        self._Definition = Definition

    @property
    def Type(self):
        r"""音频类型，取值有：
<li>Original：原唱</li>
<li>Accompaniment：伴奏</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Definition = params.get("Definition")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDestroyModeCommandInput(AbstractModel):
    r"""设置销毁模式

    """

    def __init__(self):
        r"""
        :param _DestroyMode: 销毁模式，取值有：
<li>Auto：房间没人时自动销毁</li>
<li>Expire：房间没人时过期自动销毁</li>
<li>Never：不自动销毁，需手动销毁</li>默认为：Auto。
        :type DestroyMode: str
        :param _DestroyExpireTime: 过期销毁时间，单位：秒，当DestroyMode取Expire时必填。
        :type DestroyExpireTime: int
        """
        self._DestroyMode = None
        self._DestroyExpireTime = None

    @property
    def DestroyMode(self):
        r"""销毁模式，取值有：
<li>Auto：房间没人时自动销毁</li>
<li>Expire：房间没人时过期自动销毁</li>
<li>Never：不自动销毁，需手动销毁</li>默认为：Auto。
        :rtype: str
        """
        return self._DestroyMode

    @DestroyMode.setter
    def DestroyMode(self, DestroyMode):
        self._DestroyMode = DestroyMode

    @property
    def DestroyExpireTime(self):
        r"""过期销毁时间，单位：秒，当DestroyMode取Expire时必填。
        :rtype: int
        """
        return self._DestroyExpireTime

    @DestroyExpireTime.setter
    def DestroyExpireTime(self, DestroyExpireTime):
        self._DestroyExpireTime = DestroyExpireTime


    def _deserialize(self, params):
        self._DestroyMode = params.get("DestroyMode")
        self._DestroyExpireTime = params.get("DestroyExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPlayModeCommandInput(AbstractModel):
    r"""设置播放模式

    """

    def __init__(self):
        r"""
        :param _PlayMode: 播放模式，取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :type PlayMode: str
        """
        self._PlayMode = None

    @property
    def PlayMode(self):
        r"""播放模式，取值有：
<li>RepeatPlaylist：列表循环</li>
<li>Order：顺序播放</li>
<li>RepeatSingle：单曲循环</li>
<li>Shuffle：随机播放</li>
        :rtype: str
        """
        return self._PlayMode

    @PlayMode.setter
    def PlayMode(self, PlayMode):
        self._PlayMode = PlayMode


    def _deserialize(self, params):
        self._PlayMode = params.get("PlayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetPlaylistCommandInput(AbstractModel):
    r"""设置播放列表指令参数

    """

    def __init__(self):
        r"""
        :param _Type: 变更类型，取值有：
<li>Add：添加</li>
<li>Delete：删除</li>
<li>ClearList：清空歌曲列表</li>
<li>Move：移动歌曲</li>
        :type Type: str
        :param _Index: 歌单索引位置，
当 Type 取 Add 时，-1表示添加在列表最后位置，大于-1表示要添加的位置；
当 Type 取 Delete 时，表示待删除歌曲的位置；
当 Type 取 Move 时，表示待调整歌曲的位置。
        :type Index: int
        :param _ChangedIndex: 当 Type 取 Move 时，必填，表示移动歌曲的目标位置。
        :type ChangedIndex: int
        :param _MusicIds: 歌曲 ID 列表，当 Type 取 Add 时，与MusicURLs必填其中一项。
        :type MusicIds: list of str
        :param _MusicURLs: 歌曲 URL 列表，当 Type 取 Add 时，与MusicIds必填其中一项。
注：URL必须以.mp3结尾且必须是mp3编码文件。
        :type MusicURLs: list of str
        """
        self._Type = None
        self._Index = None
        self._ChangedIndex = None
        self._MusicIds = None
        self._MusicURLs = None

    @property
    def Type(self):
        r"""变更类型，取值有：
<li>Add：添加</li>
<li>Delete：删除</li>
<li>ClearList：清空歌曲列表</li>
<li>Move：移动歌曲</li>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Index(self):
        r"""歌单索引位置，
当 Type 取 Add 时，-1表示添加在列表最后位置，大于-1表示要添加的位置；
当 Type 取 Delete 时，表示待删除歌曲的位置；
当 Type 取 Move 时，表示待调整歌曲的位置。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def ChangedIndex(self):
        r"""当 Type 取 Move 时，必填，表示移动歌曲的目标位置。
        :rtype: int
        """
        return self._ChangedIndex

    @ChangedIndex.setter
    def ChangedIndex(self, ChangedIndex):
        self._ChangedIndex = ChangedIndex

    @property
    def MusicIds(self):
        r"""歌曲 ID 列表，当 Type 取 Add 时，与MusicURLs必填其中一项。
        :rtype: list of str
        """
        return self._MusicIds

    @MusicIds.setter
    def MusicIds(self, MusicIds):
        self._MusicIds = MusicIds

    @property
    def MusicURLs(self):
        r"""歌曲 URL 列表，当 Type 取 Add 时，与MusicIds必填其中一项。
注：URL必须以.mp3结尾且必须是mp3编码文件。
        :rtype: list of str
        """
        return self._MusicURLs

    @MusicURLs.setter
    def MusicURLs(self, MusicURLs):
        self._MusicURLs = MusicURLs


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Index = params.get("Index")
        self._ChangedIndex = params.get("ChangedIndex")
        self._MusicIds = params.get("MusicIds")
        self._MusicURLs = params.get("MusicURLs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRealVolumeCommandInput(AbstractModel):
    r"""设置真实音量。

    """

    def __init__(self):
        r"""
        :param _RealVolume: 真实音量大小，取值范围为 0~100，默认值为 50。
        :type RealVolume: int
        """
        self._RealVolume = None

    @property
    def RealVolume(self):
        r"""真实音量大小，取值范围为 0~100，默认值为 50。
        :rtype: int
        """
        return self._RealVolume

    @RealVolume.setter
    def RealVolume(self, RealVolume):
        self._RealVolume = RealVolume


    def _deserialize(self, params):
        self._RealVolume = params.get("RealVolume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetVolumeCommandInput(AbstractModel):
    r"""设置音量。

    """

    def __init__(self):
        r"""
        :param _Volume: 音量大小，取值范围为 0~100，默认值为 50。
        :type Volume: int
        """
        self._Volume = None

    @property
    def Volume(self):
        r"""音量大小，取值范围为 0~100，默认值为 50。
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    r"""排序依据

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段
        :type Field: str
        :param _Order: 排序方式，可选值：Asc（升序）、Desc（降序）
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        r"""排序字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        r"""排序方式，可选值：Asc（升序）、Desc（降序）
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Station(AbstractModel):
    r"""分类内容

    """

    def __init__(self):
        r"""
        :param _CategoryID: StationID
        :type CategoryID: str
        :param _CategoryCode: Station MCCode
注意：此字段可能返回 null，表示取不到有效值。
        :type CategoryCode: str
        :param _Name: Category Name
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Rank: Station的排序值，供参考（返回结果已按其升序）
注意：此字段可能返回 null，表示取不到有效值。
        :type Rank: int
        :param _ImagePathMap: station图片集合
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePathMap: list of ImagePath
        """
        self._CategoryID = None
        self._CategoryCode = None
        self._Name = None
        self._Rank = None
        self._ImagePathMap = None

    @property
    def CategoryID(self):
        r"""StationID
        :rtype: str
        """
        return self._CategoryID

    @CategoryID.setter
    def CategoryID(self, CategoryID):
        self._CategoryID = CategoryID

    @property
    def CategoryCode(self):
        r"""Station MCCode
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CategoryCode

    @CategoryCode.setter
    def CategoryCode(self, CategoryCode):
        self._CategoryCode = CategoryCode

    @property
    def Name(self):
        r"""Category Name
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rank(self):
        r"""Station的排序值，供参考（返回结果已按其升序）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank

    @property
    def ImagePathMap(self):
        r"""station图片集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImagePath
        """
        return self._ImagePathMap

    @ImagePathMap.setter
    def ImagePathMap(self, ImagePathMap):
        self._ImagePathMap = ImagePathMap


    def _deserialize(self, params):
        self._CategoryID = params.get("CategoryID")
        self._CategoryCode = params.get("CategoryCode")
        self._Name = params.get("Name")
        self._Rank = params.get("Rank")
        if params.get("ImagePathMap") is not None:
            self._ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self._ImagePathMap.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncKTVRobotCommandRequest(AbstractModel):
    r"""SyncKTVRobotCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RobotId: 机器人Id。
        :type RobotId: str
        :param _Command: 指令，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>SwitchPrevious：上一首</li>
<li>SwitchNext：下一首</li>
<li>SetPlayMode：设置播放模式</li>
<li>Seek：调整播放进度</li>
<li>SetPlaylist：歌单变更</li>
<li>SetAudioParam：音频参数变更</li>
<li>SendMessage：发送自定义消息</li>
<li>SetDestroyMode：设置销毁模式</li>
<li><del>SetVolume：设置音量</del>（已废弃，请采用 SetRealVolume）</li>
<li>SetRealVolume：设置真实音量</li>
        :type Command: str
        :param _PlayCommandInput: 播放参数。
        :type PlayCommandInput: :class:`tencentcloud.ame.v20190916.models.PlayCommandInput`
        :param _SetPlaylistCommandInput: 播放列表变更信息，当Command取SetPlaylist时，必填。
        :type SetPlaylistCommandInput: :class:`tencentcloud.ame.v20190916.models.SetPlaylistCommandInput`
        :param _SeekCommandInput: 播放进度，当Command取Seek时，必填。
        :type SeekCommandInput: :class:`tencentcloud.ame.v20190916.models.SeekCommandInput`
        :param _SetAudioParamCommandInput: 音频参数，当Command取SetAudioParam时，必填。
        :type SetAudioParamCommandInput: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        :param _SendMessageCommandInput: 自定义消息，当Command取SendMessage时，必填。
        :type SendMessageCommandInput: :class:`tencentcloud.ame.v20190916.models.SendMessageCommandInput`
        :param _SetPlayModeCommandInput: 播放模式，当Command取SetPlayMode时，必填。
        :type SetPlayModeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetPlayModeCommandInput`
        :param _SetDestroyModeCommandInput: 销毁模式，当Command取SetDestroyMode时，必填。
        :type SetDestroyModeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetDestroyModeCommandInput`
        :param _SetVolumeCommandInput: <del>音量，当Command取SetVolume时，必填。</del>
（已废弃，请采用 SetRealVolumeCommandInput ）
        :type SetVolumeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetVolumeCommandInput`
        :param _SetRealVolumeCommandInput: 真实音量，当Command取SetRealVolume时，必填。
        :type SetRealVolumeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetRealVolumeCommandInput`
        """
        self._RobotId = None
        self._Command = None
        self._PlayCommandInput = None
        self._SetPlaylistCommandInput = None
        self._SeekCommandInput = None
        self._SetAudioParamCommandInput = None
        self._SendMessageCommandInput = None
        self._SetPlayModeCommandInput = None
        self._SetDestroyModeCommandInput = None
        self._SetVolumeCommandInput = None
        self._SetRealVolumeCommandInput = None

    @property
    def RobotId(self):
        r"""机器人Id。
        :rtype: str
        """
        return self._RobotId

    @RobotId.setter
    def RobotId(self, RobotId):
        self._RobotId = RobotId

    @property
    def Command(self):
        r"""指令，取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>SwitchPrevious：上一首</li>
<li>SwitchNext：下一首</li>
<li>SetPlayMode：设置播放模式</li>
<li>Seek：调整播放进度</li>
<li>SetPlaylist：歌单变更</li>
<li>SetAudioParam：音频参数变更</li>
<li>SendMessage：发送自定义消息</li>
<li>SetDestroyMode：设置销毁模式</li>
<li><del>SetVolume：设置音量</del>（已废弃，请采用 SetRealVolume）</li>
<li>SetRealVolume：设置真实音量</li>
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def PlayCommandInput(self):
        r"""播放参数。
        :rtype: :class:`tencentcloud.ame.v20190916.models.PlayCommandInput`
        """
        return self._PlayCommandInput

    @PlayCommandInput.setter
    def PlayCommandInput(self, PlayCommandInput):
        self._PlayCommandInput = PlayCommandInput

    @property
    def SetPlaylistCommandInput(self):
        r"""播放列表变更信息，当Command取SetPlaylist时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetPlaylistCommandInput`
        """
        return self._SetPlaylistCommandInput

    @SetPlaylistCommandInput.setter
    def SetPlaylistCommandInput(self, SetPlaylistCommandInput):
        self._SetPlaylistCommandInput = SetPlaylistCommandInput

    @property
    def SeekCommandInput(self):
        r"""播放进度，当Command取Seek时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SeekCommandInput`
        """
        return self._SeekCommandInput

    @SeekCommandInput.setter
    def SeekCommandInput(self, SeekCommandInput):
        self._SeekCommandInput = SeekCommandInput

    @property
    def SetAudioParamCommandInput(self):
        r"""音频参数，当Command取SetAudioParam时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        """
        return self._SetAudioParamCommandInput

    @SetAudioParamCommandInput.setter
    def SetAudioParamCommandInput(self, SetAudioParamCommandInput):
        self._SetAudioParamCommandInput = SetAudioParamCommandInput

    @property
    def SendMessageCommandInput(self):
        r"""自定义消息，当Command取SendMessage时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SendMessageCommandInput`
        """
        return self._SendMessageCommandInput

    @SendMessageCommandInput.setter
    def SendMessageCommandInput(self, SendMessageCommandInput):
        self._SendMessageCommandInput = SendMessageCommandInput

    @property
    def SetPlayModeCommandInput(self):
        r"""播放模式，当Command取SetPlayMode时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetPlayModeCommandInput`
        """
        return self._SetPlayModeCommandInput

    @SetPlayModeCommandInput.setter
    def SetPlayModeCommandInput(self, SetPlayModeCommandInput):
        self._SetPlayModeCommandInput = SetPlayModeCommandInput

    @property
    def SetDestroyModeCommandInput(self):
        r"""销毁模式，当Command取SetDestroyMode时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetDestroyModeCommandInput`
        """
        return self._SetDestroyModeCommandInput

    @SetDestroyModeCommandInput.setter
    def SetDestroyModeCommandInput(self, SetDestroyModeCommandInput):
        self._SetDestroyModeCommandInput = SetDestroyModeCommandInput

    @property
    def SetVolumeCommandInput(self):
        r"""<del>音量，当Command取SetVolume时，必填。</del>
（已废弃，请采用 SetRealVolumeCommandInput ）
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetVolumeCommandInput`
        """
        return self._SetVolumeCommandInput

    @SetVolumeCommandInput.setter
    def SetVolumeCommandInput(self, SetVolumeCommandInput):
        self._SetVolumeCommandInput = SetVolumeCommandInput

    @property
    def SetRealVolumeCommandInput(self):
        r"""真实音量，当Command取SetRealVolume时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetRealVolumeCommandInput`
        """
        return self._SetRealVolumeCommandInput

    @SetRealVolumeCommandInput.setter
    def SetRealVolumeCommandInput(self, SetRealVolumeCommandInput):
        self._SetRealVolumeCommandInput = SetRealVolumeCommandInput


    def _deserialize(self, params):
        self._RobotId = params.get("RobotId")
        self._Command = params.get("Command")
        if params.get("PlayCommandInput") is not None:
            self._PlayCommandInput = PlayCommandInput()
            self._PlayCommandInput._deserialize(params.get("PlayCommandInput"))
        if params.get("SetPlaylistCommandInput") is not None:
            self._SetPlaylistCommandInput = SetPlaylistCommandInput()
            self._SetPlaylistCommandInput._deserialize(params.get("SetPlaylistCommandInput"))
        if params.get("SeekCommandInput") is not None:
            self._SeekCommandInput = SeekCommandInput()
            self._SeekCommandInput._deserialize(params.get("SeekCommandInput"))
        if params.get("SetAudioParamCommandInput") is not None:
            self._SetAudioParamCommandInput = SetAudioParamCommandInput()
            self._SetAudioParamCommandInput._deserialize(params.get("SetAudioParamCommandInput"))
        if params.get("SendMessageCommandInput") is not None:
            self._SendMessageCommandInput = SendMessageCommandInput()
            self._SendMessageCommandInput._deserialize(params.get("SendMessageCommandInput"))
        if params.get("SetPlayModeCommandInput") is not None:
            self._SetPlayModeCommandInput = SetPlayModeCommandInput()
            self._SetPlayModeCommandInput._deserialize(params.get("SetPlayModeCommandInput"))
        if params.get("SetDestroyModeCommandInput") is not None:
            self._SetDestroyModeCommandInput = SetDestroyModeCommandInput()
            self._SetDestroyModeCommandInput._deserialize(params.get("SetDestroyModeCommandInput"))
        if params.get("SetVolumeCommandInput") is not None:
            self._SetVolumeCommandInput = SetVolumeCommandInput()
            self._SetVolumeCommandInput._deserialize(params.get("SetVolumeCommandInput"))
        if params.get("SetRealVolumeCommandInput") is not None:
            self._SetRealVolumeCommandInput = SetRealVolumeCommandInput()
            self._SetRealVolumeCommandInput._deserialize(params.get("SetRealVolumeCommandInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncKTVRobotCommandResponse(AbstractModel):
    r"""SyncKTVRobotCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SyncRobotCommand(AbstractModel):
    r"""KTV 机器人初始化参数，在创建后自动完成相关初始化工作。

    """

    def __init__(self):
        r"""
        :param _Command: 可同时传入多个指令，顺序执行。取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>SwitchPrevious：上一首</li>
<li>SwitchNext：下一首</li>
<li>SetPlayMode：设置播放模式</li>
<li>Seek：调整播放进度</li>
<li>SetPlaylist：歌单变更</li>
<li>SetAudioParam：音频参数变更</li>
<li>SendMessage：发送自定义消息</li>
<li>SetDestroyMode：设置销毁模式</li>
<li><del>SetVolume：设置音量</del>（已废弃，请采用 SetRealVolume）</li>
<li>SetRealVolume：设置真实音量</li>
        :type Command: str
        :param _PlayCommandInput: 播放参数。
        :type PlayCommandInput: :class:`tencentcloud.ame.v20190916.models.PlayCommandInput`
        :param _SetPlaylistCommandInput: 播放列表变更信息，当Command取SetPlaylist时，必填。
        :type SetPlaylistCommandInput: :class:`tencentcloud.ame.v20190916.models.SetPlaylistCommandInput`
        :param _SeekCommandInput: 播放进度，当Command取Seek时，必填。
        :type SeekCommandInput: :class:`tencentcloud.ame.v20190916.models.SeekCommandInput`
        :param _SetAudioParamCommandInput: 音频参数，当Command取SetAudioParam时，必填。
        :type SetAudioParamCommandInput: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        :param _SendMessageCommandInput: 自定义消息，当Command取SendMessage时，必填。
        :type SendMessageCommandInput: :class:`tencentcloud.ame.v20190916.models.SendMessageCommandInput`
        :param _SetPlayModeCommandInput: 播放模式，当Command取SetPlayMode时，必填。
        :type SetPlayModeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetPlayModeCommandInput`
        :param _SetDestroyModeCommandInput: 销毁模式，当Command取SetDestroyMode时，必填。
        :type SetDestroyModeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetDestroyModeCommandInput`
        :param _SetVolumeCommandInput: <del>音量，当Command取SetVolume时，必填。</del>
（已废弃，请采用 SetRealVolumeCommandInput）
        :type SetVolumeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetVolumeCommandInput`
        :param _SetRealVolumeCommandInput: 真实音量，当Command取SetRealVolume时，必填。
        :type SetRealVolumeCommandInput: :class:`tencentcloud.ame.v20190916.models.SetRealVolumeCommandInput`
        """
        self._Command = None
        self._PlayCommandInput = None
        self._SetPlaylistCommandInput = None
        self._SeekCommandInput = None
        self._SetAudioParamCommandInput = None
        self._SendMessageCommandInput = None
        self._SetPlayModeCommandInput = None
        self._SetDestroyModeCommandInput = None
        self._SetVolumeCommandInput = None
        self._SetRealVolumeCommandInput = None

    @property
    def Command(self):
        r"""可同时传入多个指令，顺序执行。取值有：
<li>Play：播放</li>
<li>Pause：暂停</li>
<li>SwitchPrevious：上一首</li>
<li>SwitchNext：下一首</li>
<li>SetPlayMode：设置播放模式</li>
<li>Seek：调整播放进度</li>
<li>SetPlaylist：歌单变更</li>
<li>SetAudioParam：音频参数变更</li>
<li>SendMessage：发送自定义消息</li>
<li>SetDestroyMode：设置销毁模式</li>
<li><del>SetVolume：设置音量</del>（已废弃，请采用 SetRealVolume）</li>
<li>SetRealVolume：设置真实音量</li>
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def PlayCommandInput(self):
        r"""播放参数。
        :rtype: :class:`tencentcloud.ame.v20190916.models.PlayCommandInput`
        """
        return self._PlayCommandInput

    @PlayCommandInput.setter
    def PlayCommandInput(self, PlayCommandInput):
        self._PlayCommandInput = PlayCommandInput

    @property
    def SetPlaylistCommandInput(self):
        r"""播放列表变更信息，当Command取SetPlaylist时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetPlaylistCommandInput`
        """
        return self._SetPlaylistCommandInput

    @SetPlaylistCommandInput.setter
    def SetPlaylistCommandInput(self, SetPlaylistCommandInput):
        self._SetPlaylistCommandInput = SetPlaylistCommandInput

    @property
    def SeekCommandInput(self):
        r"""播放进度，当Command取Seek时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SeekCommandInput`
        """
        return self._SeekCommandInput

    @SeekCommandInput.setter
    def SeekCommandInput(self, SeekCommandInput):
        self._SeekCommandInput = SeekCommandInput

    @property
    def SetAudioParamCommandInput(self):
        r"""音频参数，当Command取SetAudioParam时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetAudioParamCommandInput`
        """
        return self._SetAudioParamCommandInput

    @SetAudioParamCommandInput.setter
    def SetAudioParamCommandInput(self, SetAudioParamCommandInput):
        self._SetAudioParamCommandInput = SetAudioParamCommandInput

    @property
    def SendMessageCommandInput(self):
        r"""自定义消息，当Command取SendMessage时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SendMessageCommandInput`
        """
        return self._SendMessageCommandInput

    @SendMessageCommandInput.setter
    def SendMessageCommandInput(self, SendMessageCommandInput):
        self._SendMessageCommandInput = SendMessageCommandInput

    @property
    def SetPlayModeCommandInput(self):
        r"""播放模式，当Command取SetPlayMode时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetPlayModeCommandInput`
        """
        return self._SetPlayModeCommandInput

    @SetPlayModeCommandInput.setter
    def SetPlayModeCommandInput(self, SetPlayModeCommandInput):
        self._SetPlayModeCommandInput = SetPlayModeCommandInput

    @property
    def SetDestroyModeCommandInput(self):
        r"""销毁模式，当Command取SetDestroyMode时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetDestroyModeCommandInput`
        """
        return self._SetDestroyModeCommandInput

    @SetDestroyModeCommandInput.setter
    def SetDestroyModeCommandInput(self, SetDestroyModeCommandInput):
        self._SetDestroyModeCommandInput = SetDestroyModeCommandInput

    @property
    def SetVolumeCommandInput(self):
        r"""<del>音量，当Command取SetVolume时，必填。</del>
（已废弃，请采用 SetRealVolumeCommandInput）
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetVolumeCommandInput`
        """
        return self._SetVolumeCommandInput

    @SetVolumeCommandInput.setter
    def SetVolumeCommandInput(self, SetVolumeCommandInput):
        self._SetVolumeCommandInput = SetVolumeCommandInput

    @property
    def SetRealVolumeCommandInput(self):
        r"""真实音量，当Command取SetRealVolume时，必填。
        :rtype: :class:`tencentcloud.ame.v20190916.models.SetRealVolumeCommandInput`
        """
        return self._SetRealVolumeCommandInput

    @SetRealVolumeCommandInput.setter
    def SetRealVolumeCommandInput(self, SetRealVolumeCommandInput):
        self._SetRealVolumeCommandInput = SetRealVolumeCommandInput


    def _deserialize(self, params):
        self._Command = params.get("Command")
        if params.get("PlayCommandInput") is not None:
            self._PlayCommandInput = PlayCommandInput()
            self._PlayCommandInput._deserialize(params.get("PlayCommandInput"))
        if params.get("SetPlaylistCommandInput") is not None:
            self._SetPlaylistCommandInput = SetPlaylistCommandInput()
            self._SetPlaylistCommandInput._deserialize(params.get("SetPlaylistCommandInput"))
        if params.get("SeekCommandInput") is not None:
            self._SeekCommandInput = SeekCommandInput()
            self._SeekCommandInput._deserialize(params.get("SeekCommandInput"))
        if params.get("SetAudioParamCommandInput") is not None:
            self._SetAudioParamCommandInput = SetAudioParamCommandInput()
            self._SetAudioParamCommandInput._deserialize(params.get("SetAudioParamCommandInput"))
        if params.get("SendMessageCommandInput") is not None:
            self._SendMessageCommandInput = SendMessageCommandInput()
            self._SendMessageCommandInput._deserialize(params.get("SendMessageCommandInput"))
        if params.get("SetPlayModeCommandInput") is not None:
            self._SetPlayModeCommandInput = SetPlayModeCommandInput()
            self._SetPlayModeCommandInput._deserialize(params.get("SetPlayModeCommandInput"))
        if params.get("SetDestroyModeCommandInput") is not None:
            self._SetDestroyModeCommandInput = SetDestroyModeCommandInput()
            self._SetDestroyModeCommandInput._deserialize(params.get("SetDestroyModeCommandInput"))
        if params.get("SetVolumeCommandInput") is not None:
            self._SetVolumeCommandInput = SetVolumeCommandInput()
            self._SetVolumeCommandInput._deserialize(params.get("SetVolumeCommandInput"))
        if params.get("SetRealVolumeCommandInput") is not None:
            self._SetRealVolumeCommandInput = SetRealVolumeCommandInput()
            self._SetRealVolumeCommandInput._deserialize(params.get("SetRealVolumeCommandInput"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TRTCJoinRoomInput(AbstractModel):
    r"""TRTC推流进房信息

    """

    def __init__(self):
        r"""
        :param _Sign: 签名。
        :type Sign: str
        :param _RoomId: 房间号。
        :type RoomId: str
        :param _SdkAppId: 推流应用ID。
        :type SdkAppId: str
        :param _UserId: 用户唯一标识。
        :type UserId: str
        :param _PrivateMapKey: 进房钥匙，若需要权限控制请携带该参数。
 [privateMapKey 权限设置](/document/product/647/32240) 
        :type PrivateMapKey: str
        :param _Role: 用户角色，目前支持两种角色：
<li>anchor：主播</li>
<li>audience：观众</li>
        :type Role: str
        :param _RoomIdType: TRTC房间号的类型：
<li>Integer：数字类型</li>
<li> String：字符串类型</li>
默认为：Integer 。
        :type RoomIdType: str
        """
        self._Sign = None
        self._RoomId = None
        self._SdkAppId = None
        self._UserId = None
        self._PrivateMapKey = None
        self._Role = None
        self._RoomIdType = None

    @property
    def Sign(self):
        r"""签名。
        :rtype: str
        """
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def RoomId(self):
        r"""房间号。
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        r"""推流应用ID。
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserId(self):
        r"""用户唯一标识。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PrivateMapKey(self):
        r"""进房钥匙，若需要权限控制请携带该参数。
 [privateMapKey 权限设置](/document/product/647/32240) 
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey

    @property
    def Role(self):
        r"""用户角色，目前支持两种角色：
<li>anchor：主播</li>
<li>audience：观众</li>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RoomIdType(self):
        r"""TRTC房间号的类型：
<li>Integer：数字类型</li>
<li> String：字符串类型</li>
默认为：Integer 。
        :rtype: str
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType


    def _deserialize(self, params):
        self._Sign = params.get("Sign")
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        self._UserId = params.get("UserId")
        self._PrivateMapKey = params.get("PrivateMapKey")
        self._Role = params.get("Role")
        self._RoomIdType = params.get("RoomIdType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelves(AbstractModel):
    r"""下架歌曲复合结构

    """

    def __init__(self):
        r"""
        :param _MusicIds: 资源方对应音乐Id
        :type MusicIds: str
        :param _SaleStatus: 当曲目临时下架时：已订购客户无影响，无需消息通知。当曲目封杀下架后，推送消息至已订购老客户，枚举值，判断是否上/下架
在售状态，0在售，1临时下架，2永久下架
        :type SaleStatus: str
        """
        self._MusicIds = None
        self._SaleStatus = None

    @property
    def MusicIds(self):
        r"""资源方对应音乐Id
        :rtype: str
        """
        return self._MusicIds

    @MusicIds.setter
    def MusicIds(self, MusicIds):
        self._MusicIds = MusicIds

    @property
    def SaleStatus(self):
        r"""当曲目临时下架时：已订购客户无影响，无需消息通知。当曲目封杀下架后，推送消息至已订购老客户，枚举值，判断是否上/下架
在售状态，0在售，1临时下架，2永久下架
        :rtype: str
        """
        return self._SaleStatus

    @SaleStatus.setter
    def SaleStatus(self, SaleStatus):
        self._SaleStatus = SaleStatus


    def _deserialize(self, params):
        self._MusicIds = params.get("MusicIds")
        self._SaleStatus = params.get("SaleStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelvesRequest(AbstractModel):
    r"""TakeMusicOffShelves请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TakeMusicOffShelves: 资源方下架必传结构
        :type TakeMusicOffShelves: list of TakeMusicOffShelves
        """
        self._TakeMusicOffShelves = None

    @property
    def TakeMusicOffShelves(self):
        r"""资源方下架必传结构
        :rtype: list of TakeMusicOffShelves
        """
        return self._TakeMusicOffShelves

    @TakeMusicOffShelves.setter
    def TakeMusicOffShelves(self, TakeMusicOffShelves):
        self._TakeMusicOffShelves = TakeMusicOffShelves


    def _deserialize(self, params):
        if params.get("TakeMusicOffShelves") is not None:
            self._TakeMusicOffShelves = []
            for item in params.get("TakeMusicOffShelves"):
                obj = TakeMusicOffShelves()
                obj._deserialize(item)
                self._TakeMusicOffShelves.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelvesResponse(AbstractModel):
    r"""TakeMusicOffShelves返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessNum: 返回成功数量
        :type SuccessNum: int
        :param _FailedNum: 返回失败数量
        :type FailedNum: int
        :param _FailedMusicIds: 返回失败歌曲musicId
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMusicIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessNum = None
        self._FailedNum = None
        self._FailedMusicIds = None
        self._RequestId = None

    @property
    def SuccessNum(self):
        r"""返回成功数量
        :rtype: int
        """
        return self._SuccessNum

    @SuccessNum.setter
    def SuccessNum(self, SuccessNum):
        self._SuccessNum = SuccessNum

    @property
    def FailedNum(self):
        r"""返回失败数量
        :rtype: int
        """
        return self._FailedNum

    @FailedNum.setter
    def FailedNum(self, FailedNum):
        self._FailedNum = FailedNum

    @property
    def FailedMusicIds(self):
        r"""返回失败歌曲musicId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FailedMusicIds

    @FailedMusicIds.setter
    def FailedMusicIds(self, FailedMusicIds):
        self._FailedMusicIds = FailedMusicIds

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessNum = params.get("SuccessNum")
        self._FailedNum = params.get("FailedNum")
        self._FailedMusicIds = params.get("FailedMusicIds")
        self._RequestId = params.get("RequestId")


class TimeRange(AbstractModel):
    r"""时间范围

    """

    def __init__(self):
        r"""
        :param _Before: <li>大于等于此时间（起始时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :type Before: str
        :param _After: <li>小于此时间（结束时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :type After: str
        """
        self._Before = None
        self._After = None

    @property
    def Before(self):
        r"""<li>大于等于此时间（起始时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :rtype: str
        """
        return self._Before

    @Before.setter
    def Before(self, Before):
        self._Before = Before

    @property
    def After(self):
        r"""<li>小于此时间（结束时间）。</li>
<li>格式按照 ISO 8601标准表示，详见 <a href="https://cloud.tencent.com/document/product/266/11732#I" target="_blank">ISO 日期格式说明</a>。</li>
        :rtype: str
        """
        return self._After

    @After.setter
    def After(self, After):
        self._After = After


    def _deserialize(self, params):
        self._Before = params.get("Before")
        self._After = params.get("After")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UseRange(AbstractModel):
    r"""曲库包用途信息

    """

    def __init__(self):
        r"""
        :param _UseRangeId: 用途id
        :type UseRangeId: int
        :param _Name: 用途范围名称
        :type Name: str
        """
        self._UseRangeId = None
        self._Name = None

    @property
    def UseRangeId(self):
        r"""用途id
        :rtype: int
        """
        return self._UseRangeId

    @UseRangeId.setter
    def UseRangeId(self, UseRangeId):
        self._UseRangeId = UseRangeId

    @property
    def Name(self):
        r"""用途范围名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._UseRangeId = params.get("UseRangeId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        