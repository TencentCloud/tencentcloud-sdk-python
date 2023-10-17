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


class AndroidAppInfo(AbstractModel):
    """渠道合作Android加固App信息

    """

    def __init__(self):
        r"""
        :param _AppMd5: app文件的md5算法值，需要正确传递，在线加固必输。
例如linux环境下执行算法命令md5sum ：
#md5sum test.apk 
d40cc11e4bddd643ecdf29cde729a12b
        :type AppMd5: str
        :param _AppSize: app的大小，非必输。
        :type AppSize: int
        :param _AppUrl: app下载链接，在线加固必输。
        :type AppUrl: str
        :param _AppName: app名称，非必输
        :type AppName: str
        :param _AppPkgName: app的包名，本次操作的包名。
当Android是按年收费、免费试用加固时，在线加固和输出工具要求该字段必输，且与AndroidPlan.AppPkgName值相等。
        :type AppPkgName: str
        :param _AppFileName: app的文件名，非必输。
        :type AppFileName: str
        :param _AppVersion: app版本号，非必输。
        :type AppVersion: str
        :param _AppType: Android app的文件类型，本次加固操作的应用类型 。
Android在线加固和输出工具加固必输，其值需等于“apk”或“aab”，且与AndroidAppInfo.AppType值相等。
        :type AppType: str
        """
        self._AppMd5 = None
        self._AppSize = None
        self._AppUrl = None
        self._AppName = None
        self._AppPkgName = None
        self._AppFileName = None
        self._AppVersion = None
        self._AppType = None

    @property
    def AppMd5(self):
        return self._AppMd5

    @AppMd5.setter
    def AppMd5(self, AppMd5):
        self._AppMd5 = AppMd5

    @property
    def AppSize(self):
        return self._AppSize

    @AppSize.setter
    def AppSize(self, AppSize):
        self._AppSize = AppSize

    @property
    def AppUrl(self):
        return self._AppUrl

    @AppUrl.setter
    def AppUrl(self, AppUrl):
        self._AppUrl = AppUrl

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def AppFileName(self):
        return self._AppFileName

    @AppFileName.setter
    def AppFileName(self, AppFileName):
        self._AppFileName = AppFileName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType


    def _deserialize(self, params):
        self._AppMd5 = params.get("AppMd5")
        self._AppSize = params.get("AppSize")
        self._AppUrl = params.get("AppUrl")
        self._AppName = params.get("AppName")
        self._AppPkgName = params.get("AppPkgName")
        self._AppFileName = params.get("AppFileName")
        self._AppVersion = params.get("AppVersion")
        self._AppType = params.get("AppType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidPlan(AbstractModel):
    """渠道合作Android加固策略信息

    """

    def __init__(self):
        r"""
        :param _PlanId: 非必输字段，PlanId 是指本次加固使用的配置策略Id，可通过载入上次配置接口获取。其值非0时，代表引用对应的策略。
        :type PlanId: int
        :param _AppPkgName: 本次操作的包名。
当收费模式是android按年收费和android免费试用的在线加固和输出工具加固时，要求该字段必输，且与AndroidAppInfo.AppPkgName值相等。
        :type AppPkgName: str
        :param _AppType: android app的文件类型，本次加固操作的应用类型 。 
android在线加固和输出工具加固必输，其值需等于“apk”或“aab”，且与AndroidAppInfo.AppType值相等。

        :type AppType: str
        :param _EncryptParam: android加固必输字段。
加固策略，json格式字符串。
字段说明（0-关闭，1-开启）：
        "enable"=1 #DEX整体加固;
        "antiprotect"=1 #反调试;
        "antirepack"=1 #防重打包、防篡改;
        "dexsig"=1       #签名校验;
        "antimonitor"=1 #防模拟器运行保护;
        "ptrace"=1 #防动态注入、动态调试;
        "so"."enable" = 1 #文件加密;
        "vmp"."enable" = 1 #VMP虚拟化保护;
        "respro"."assets"."enable" = 1 #assets资源文件加密
       "respro"."res"."enable" = 1 #res资源文件加密

so文件加密：
支持5种架构:
apk 格式: /lib/armeabi/libxxx.so,/lib/arm64-v8a/libxxx.so,/lib/armeabi-v7a/libxxx.so,/lib/x86/libxxx.so,/lib/x86_64/libxxx.so
aab格式: /base/lib/armeabi/libxxx.so,/base/lib/arm64-v8a/libxxx.so,/base/lib/armeabi-v7a/libxxx.so,/base/lib/x86/libxxx.so,/base/lib/x86_64/libxxx.so
请列举 SO 库在 apk 文件解压后的完整有效路径，如:/lib/armeabi/libxxx.so；
需要加固的 SO 库需确认为自研的 SO 库，不要加固第三方 SO 库，否则会增加 crash 风险

res资源文件加密注意事项：
请指定需要加密的文件全路径，如：res/layout/1.xml;
res资源文件加密不能加密APP图标
res目录文件，不能加密以下后缀规则的文件".wav", ".mp2", ".mp3", ".ogg", ".aac", ".mpg",".mpeg", ".mid", ".midi", ".smf", ".jet", ".rtttl", ".imy", ".xmf", ".mp4", ".m4a", ".m4v", ".3gp",".3gpp", ".3g2", ".3gpp2", ".amr", ".awb", ".wma", ".wmv"

assets资源文件加密注意事项:
请指定需要加密的文件全路径，如：assets/main.js；可以完整路径，也可以相对路径。
如果有通配符需要完整路径 ":all"或者"*"代表所有文件
assets资源文件加密不能加密APP图标
assets目录文件，不能加密以下后缀规则的文件".wav", ".mp2", ".mp3", ".ogg", ".aac", ".mpg",".mpeg", ".mid", ".midi", ".smf", ".jet", ".rtttl", ".imy", ".xmf", ".mp4", ".m4a", ".m4v", ".3gp",".3gpp", ".3g2", ".3gpp2", ".amr", ".awb", ".wma", ".wmv"


apk[dex+so+vmp+res+assets]加固参数示例：
‘{
    "dex": {
        "enable": 1,
        "antiprotect": 1,
        "antirepack": 1,
        "dexsig": 1,
        "antimonitor": 1,
        "ptrace": 1
    },
    "so": {
        "enable": 1,
        "ver": "1.3.3",
        "file": [
            "/lib/armeabi/libtest.so"
        ]
    },
    "vmp": {
        "enable": 1,
        "ndkpath": "/xxx/android-ndk-r10e",
        "profile": "/xxx/vmpprofile.txt",
        "mapping": "/xxx/mapping.txt"
    },
    "respro": {
        "assets": {
            "enable": 1,
            "file": [
                "assets/1.js",
                "assets/2.jpg"
            ]
        },
        "res": {
            "enable": 1,
            "file": [
                "res/layout/1.xml",
                "res/layout/2.xml"
            ]
        }
    }
}’

aab加固方案一 
[dex+res+assets]加固json字符串：
‘{
    "dex": {
        "enable": 1,
        "antiprotect": 1,
        "antimonitor": 1
    },
    "respro": {
        "assets": {
            "enable": 1,
            "file": [
                "assets/1.js",
                "assets/2.jpg"
            ]
        },
        "res": {
            "enable": 1,
            "file": [
                "res/layout/1.xml",
                "res/layout/2.xml"
            ]
        }
    }
}’

aab加固方案二
单独vmp加固：
‘{
    "vmp": {
        "enable": 1,
        "ndkpath": "/xxx/android-ndk-r10e",
        "profile": "/xxx/vmpprofile.txt",
        "mapping": "/xxx/mapping.txt",
        "antiprotect": 1,
        "antimonitor": 1
    }
}’
        :type EncryptParam: str
        """
        self._PlanId = None
        self._AppPkgName = None
        self._AppType = None
        self._EncryptParam = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def EncryptParam(self):
        return self._EncryptParam

    @EncryptParam.setter
    def EncryptParam(self, EncryptParam):
        self._EncryptParam = EncryptParam


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._AppPkgName = params.get("AppPkgName")
        self._AppType = params.get("AppType")
        self._EncryptParam = params.get("EncryptParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AndroidResult(AbstractModel):
    """Android加固结果

    """

    def __init__(self):
        r"""
        :param _ResultId: 结果Id,用于查询加固结果
        :type ResultId: str
        :param _OrderId: 与当前任务关联的订单id
        :type OrderId: str
        :param _ResourceId: 与当前任务关联的资源Id
        :type ResourceId: str
        :param _OpUin: 本次任务发起者
        :type OpUin: int
        :param _AppType: 应用类型：android-apk; android-aab;
        :type AppType: str
        :param _AppPkgName: 应用包名
        :type AppPkgName: str
        :param _BindAppPkgName: 后台资源绑定的包名
        :type BindAppPkgName: str
        :param _EncryptState: 加固结果
        :type EncryptState: int
        :param _EncryptStateDesc: 加固结果描述
        :type EncryptStateDesc: str
        :param _EncryptErrCode: 加固失败错误码
        :type EncryptErrCode: int
        :param _EncryptErrDesc: 加固失败原因
        :type EncryptErrDesc: str
        :param _EncryptErrRef: 加固失败解决方案
        :type EncryptErrRef: str
        :param _CreatTime: 任务创建时间
        :type CreatTime: str
        :param _StartTime: 任务开始处理时间
        :type StartTime: str
        :param _EndTime: 任务处理结束时间
        :type EndTime: str
        :param _CostTime: 加固耗时（秒单位）
        :type CostTime: int
        :param _AppUrl: 在线加固-android应用原包下载链接
        :type AppUrl: str
        :param _AppMd5: 在线加固-android应用文件MD5算法值
        :type AppMd5: str
        :param _AppName: 在线加固-android应用应用名称
        :type AppName: str
        :param _AppVersion: 在线加固-android应用版本；
        :type AppVersion: str
        :param _AppSize: 在线加固-android应用大小
        :type AppSize: int
        :param _OnlineToolVersion: 在线加固-android加固-腾讯云应用加固工具版本
        :type OnlineToolVersion: str
        :param _EncryptAppMd5: 在线加固-android加固，加固成功后文件md5算法值
        :type EncryptAppMd5: str
        :param _EncryptAppSize: 在线加固-android加固，加固成功后应用大小
        :type EncryptAppSize: int
        :param _EncryptPkgUrl: 在线加固-android加固，加固包下载链接。
        :type EncryptPkgUrl: str
        :param _OutputToolVersion: 输出工具-android加固-腾讯云输出工具版本
        :type OutputToolVersion: str
        :param _OutputToolSize: 输出工具-android加固-工具大小
        :type OutputToolSize: int
        :param _ToolOutputTime: 输出工具-android加固-工具输出时间
        :type ToolOutputTime: str
        :param _ToolExpireTime: 输出工具-android加固-工具到期时间
        :type ToolExpireTime: str
        :param _OutputToolUrl: 输出工具-android加固-输出工具下载链接
        :type OutputToolUrl: str
        :param _AndroidPlan: 本次android加固策略信息
        :type AndroidPlan: :class:`tencentcloud.ms.v20180408.models.AndroidPlan`
        """
        self._ResultId = None
        self._OrderId = None
        self._ResourceId = None
        self._OpUin = None
        self._AppType = None
        self._AppPkgName = None
        self._BindAppPkgName = None
        self._EncryptState = None
        self._EncryptStateDesc = None
        self._EncryptErrCode = None
        self._EncryptErrDesc = None
        self._EncryptErrRef = None
        self._CreatTime = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None
        self._AppUrl = None
        self._AppMd5 = None
        self._AppName = None
        self._AppVersion = None
        self._AppSize = None
        self._OnlineToolVersion = None
        self._EncryptAppMd5 = None
        self._EncryptAppSize = None
        self._EncryptPkgUrl = None
        self._OutputToolVersion = None
        self._OutputToolSize = None
        self._ToolOutputTime = None
        self._ToolExpireTime = None
        self._OutputToolUrl = None
        self._AndroidPlan = None

    @property
    def ResultId(self):
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def OpUin(self):
        return self._OpUin

    @OpUin.setter
    def OpUin(self, OpUin):
        self._OpUin = OpUin

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def BindAppPkgName(self):
        return self._BindAppPkgName

    @BindAppPkgName.setter
    def BindAppPkgName(self, BindAppPkgName):
        self._BindAppPkgName = BindAppPkgName

    @property
    def EncryptState(self):
        return self._EncryptState

    @EncryptState.setter
    def EncryptState(self, EncryptState):
        self._EncryptState = EncryptState

    @property
    def EncryptStateDesc(self):
        return self._EncryptStateDesc

    @EncryptStateDesc.setter
    def EncryptStateDesc(self, EncryptStateDesc):
        self._EncryptStateDesc = EncryptStateDesc

    @property
    def EncryptErrCode(self):
        return self._EncryptErrCode

    @EncryptErrCode.setter
    def EncryptErrCode(self, EncryptErrCode):
        self._EncryptErrCode = EncryptErrCode

    @property
    def EncryptErrDesc(self):
        return self._EncryptErrDesc

    @EncryptErrDesc.setter
    def EncryptErrDesc(self, EncryptErrDesc):
        self._EncryptErrDesc = EncryptErrDesc

    @property
    def EncryptErrRef(self):
        return self._EncryptErrRef

    @EncryptErrRef.setter
    def EncryptErrRef(self, EncryptErrRef):
        self._EncryptErrRef = EncryptErrRef

    @property
    def CreatTime(self):
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

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
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def AppUrl(self):
        return self._AppUrl

    @AppUrl.setter
    def AppUrl(self, AppUrl):
        self._AppUrl = AppUrl

    @property
    def AppMd5(self):
        return self._AppMd5

    @AppMd5.setter
    def AppMd5(self, AppMd5):
        self._AppMd5 = AppMd5

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def AppSize(self):
        return self._AppSize

    @AppSize.setter
    def AppSize(self, AppSize):
        self._AppSize = AppSize

    @property
    def OnlineToolVersion(self):
        return self._OnlineToolVersion

    @OnlineToolVersion.setter
    def OnlineToolVersion(self, OnlineToolVersion):
        self._OnlineToolVersion = OnlineToolVersion

    @property
    def EncryptAppMd5(self):
        return self._EncryptAppMd5

    @EncryptAppMd5.setter
    def EncryptAppMd5(self, EncryptAppMd5):
        self._EncryptAppMd5 = EncryptAppMd5

    @property
    def EncryptAppSize(self):
        return self._EncryptAppSize

    @EncryptAppSize.setter
    def EncryptAppSize(self, EncryptAppSize):
        self._EncryptAppSize = EncryptAppSize

    @property
    def EncryptPkgUrl(self):
        return self._EncryptPkgUrl

    @EncryptPkgUrl.setter
    def EncryptPkgUrl(self, EncryptPkgUrl):
        self._EncryptPkgUrl = EncryptPkgUrl

    @property
    def OutputToolVersion(self):
        return self._OutputToolVersion

    @OutputToolVersion.setter
    def OutputToolVersion(self, OutputToolVersion):
        self._OutputToolVersion = OutputToolVersion

    @property
    def OutputToolSize(self):
        return self._OutputToolSize

    @OutputToolSize.setter
    def OutputToolSize(self, OutputToolSize):
        self._OutputToolSize = OutputToolSize

    @property
    def ToolOutputTime(self):
        return self._ToolOutputTime

    @ToolOutputTime.setter
    def ToolOutputTime(self, ToolOutputTime):
        self._ToolOutputTime = ToolOutputTime

    @property
    def ToolExpireTime(self):
        return self._ToolExpireTime

    @ToolExpireTime.setter
    def ToolExpireTime(self, ToolExpireTime):
        self._ToolExpireTime = ToolExpireTime

    @property
    def OutputToolUrl(self):
        return self._OutputToolUrl

    @OutputToolUrl.setter
    def OutputToolUrl(self, OutputToolUrl):
        self._OutputToolUrl = OutputToolUrl

    @property
    def AndroidPlan(self):
        return self._AndroidPlan

    @AndroidPlan.setter
    def AndroidPlan(self, AndroidPlan):
        self._AndroidPlan = AndroidPlan


    def _deserialize(self, params):
        self._ResultId = params.get("ResultId")
        self._OrderId = params.get("OrderId")
        self._ResourceId = params.get("ResourceId")
        self._OpUin = params.get("OpUin")
        self._AppType = params.get("AppType")
        self._AppPkgName = params.get("AppPkgName")
        self._BindAppPkgName = params.get("BindAppPkgName")
        self._EncryptState = params.get("EncryptState")
        self._EncryptStateDesc = params.get("EncryptStateDesc")
        self._EncryptErrCode = params.get("EncryptErrCode")
        self._EncryptErrDesc = params.get("EncryptErrDesc")
        self._EncryptErrRef = params.get("EncryptErrRef")
        self._CreatTime = params.get("CreatTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        self._AppUrl = params.get("AppUrl")
        self._AppMd5 = params.get("AppMd5")
        self._AppName = params.get("AppName")
        self._AppVersion = params.get("AppVersion")
        self._AppSize = params.get("AppSize")
        self._OnlineToolVersion = params.get("OnlineToolVersion")
        self._EncryptAppMd5 = params.get("EncryptAppMd5")
        self._EncryptAppSize = params.get("EncryptAppSize")
        self._EncryptPkgUrl = params.get("EncryptPkgUrl")
        self._OutputToolVersion = params.get("OutputToolVersion")
        self._OutputToolSize = params.get("OutputToolSize")
        self._ToolOutputTime = params.get("ToolOutputTime")
        self._ToolExpireTime = params.get("ToolExpireTime")
        self._OutputToolUrl = params.get("OutputToolUrl")
        if params.get("AndroidPlan") is not None:
            self._AndroidPlan = AndroidPlan()
            self._AndroidPlan._deserialize(params.get("AndroidPlan"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppDetailInfo(AbstractModel):
    """app的详细基础信息

    """

    def __init__(self):
        r"""
        :param _AppName: app的名称
        :type AppName: str
        :param _AppPkgName: app的包名
        :type AppPkgName: str
        :param _AppVersion: app的版本号
        :type AppVersion: str
        :param _AppSize: app的大小
        :type AppSize: int
        :param _AppMd5: app的md5
        :type AppMd5: str
        :param _AppIconUrl: app的图标url
        :type AppIconUrl: str
        :param _FileName: app的文件名称
        :type FileName: str
        """
        self._AppName = None
        self._AppPkgName = None
        self._AppVersion = None
        self._AppSize = None
        self._AppMd5 = None
        self._AppIconUrl = None
        self._FileName = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def AppSize(self):
        return self._AppSize

    @AppSize.setter
    def AppSize(self, AppSize):
        self._AppSize = AppSize

    @property
    def AppMd5(self):
        return self._AppMd5

    @AppMd5.setter
    def AppMd5(self, AppMd5):
        self._AppMd5 = AppMd5

    @property
    def AppIconUrl(self):
        return self._AppIconUrl

    @AppIconUrl.setter
    def AppIconUrl(self, AppIconUrl):
        self._AppIconUrl = AppIconUrl

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._AppPkgName = params.get("AppPkgName")
        self._AppVersion = params.get("AppVersion")
        self._AppSize = params.get("AppSize")
        self._AppMd5 = params.get("AppMd5")
        self._AppIconUrl = params.get("AppIconUrl")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppInfo(AbstractModel):
    """提交的app基本信息

    """

    def __init__(self):
        r"""
        :param _AppUrl: app的url，必须保证不用权限校验就可以下载
        :type AppUrl: str
        :param _AppMd5: app的md5，需要正确传递
        :type AppMd5: str
        :param _AppSize: app的大小
        :type AppSize: int
        :param _FileName: app的文件名
        :type FileName: str
        :param _AppPkgName: app的包名，需要正确的传递此字段
        :type AppPkgName: str
        :param _AppVersion: app的版本号
        :type AppVersion: str
        :param _AppIconUrl: app的图标url
        :type AppIconUrl: str
        :param _AppName: app的名称
        :type AppName: str
        """
        self._AppUrl = None
        self._AppMd5 = None
        self._AppSize = None
        self._FileName = None
        self._AppPkgName = None
        self._AppVersion = None
        self._AppIconUrl = None
        self._AppName = None

    @property
    def AppUrl(self):
        return self._AppUrl

    @AppUrl.setter
    def AppUrl(self, AppUrl):
        self._AppUrl = AppUrl

    @property
    def AppMd5(self):
        return self._AppMd5

    @AppMd5.setter
    def AppMd5(self, AppMd5):
        self._AppMd5 = AppMd5

    @property
    def AppSize(self):
        return self._AppSize

    @AppSize.setter
    def AppSize(self, AppSize):
        self._AppSize = AppSize

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def AppIconUrl(self):
        return self._AppIconUrl

    @AppIconUrl.setter
    def AppIconUrl(self, AppIconUrl):
        self._AppIconUrl = AppIconUrl

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName


    def _deserialize(self, params):
        self._AppUrl = params.get("AppUrl")
        self._AppMd5 = params.get("AppMd5")
        self._AppSize = params.get("AppSize")
        self._FileName = params.get("FileName")
        self._AppPkgName = params.get("AppPkgName")
        self._AppVersion = params.get("AppVersion")
        self._AppIconUrl = params.get("AppIconUrl")
        self._AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSetInfo(AbstractModel):
    """加固后app的信息，包含基本信息和加固信息

    """

    def __init__(self):
        r"""
        :param _ItemId: 任务唯一标识
        :type ItemId: str
        :param _AppName: app的名称
        :type AppName: str
        :param _AppPkgName: app的包名
        :type AppPkgName: str
        :param _AppVersion: app的版本号
        :type AppVersion: str
        :param _AppMd5: app的md5
        :type AppMd5: str
        :param _AppSize: app的大小
        :type AppSize: int
        :param _ServiceEdition: 加固服务版本
        :type ServiceEdition: str
        :param _ShieldCode: 加固结果返回码
        :type ShieldCode: int
        :param _AppUrl: 加固后的APP下载地址
        :type AppUrl: str
        :param _TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type TaskStatus: int
        :param _ClientIp: 请求的客户端ip
        :type ClientIp: str
        :param _TaskTime: 提交加固时间
        :type TaskTime: int
        :param _AppIconUrl: app的图标url
        :type AppIconUrl: str
        :param _ShieldMd5: 加固后app的md5
        :type ShieldMd5: str
        :param _ShieldSize: 加固后app的大小
        :type ShieldSize: int
        """
        self._ItemId = None
        self._AppName = None
        self._AppPkgName = None
        self._AppVersion = None
        self._AppMd5 = None
        self._AppSize = None
        self._ServiceEdition = None
        self._ShieldCode = None
        self._AppUrl = None
        self._TaskStatus = None
        self._ClientIp = None
        self._TaskTime = None
        self._AppIconUrl = None
        self._ShieldMd5 = None
        self._ShieldSize = None

    @property
    def ItemId(self):
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def AppVersion(self):
        return self._AppVersion

    @AppVersion.setter
    def AppVersion(self, AppVersion):
        self._AppVersion = AppVersion

    @property
    def AppMd5(self):
        return self._AppMd5

    @AppMd5.setter
    def AppMd5(self, AppMd5):
        self._AppMd5 = AppMd5

    @property
    def AppSize(self):
        return self._AppSize

    @AppSize.setter
    def AppSize(self, AppSize):
        self._AppSize = AppSize

    @property
    def ServiceEdition(self):
        return self._ServiceEdition

    @ServiceEdition.setter
    def ServiceEdition(self, ServiceEdition):
        self._ServiceEdition = ServiceEdition

    @property
    def ShieldCode(self):
        return self._ShieldCode

    @ShieldCode.setter
    def ShieldCode(self, ShieldCode):
        self._ShieldCode = ShieldCode

    @property
    def AppUrl(self):
        return self._AppUrl

    @AppUrl.setter
    def AppUrl(self, AppUrl):
        self._AppUrl = AppUrl

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def TaskTime(self):
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def AppIconUrl(self):
        return self._AppIconUrl

    @AppIconUrl.setter
    def AppIconUrl(self, AppIconUrl):
        self._AppIconUrl = AppIconUrl

    @property
    def ShieldMd5(self):
        return self._ShieldMd5

    @ShieldMd5.setter
    def ShieldMd5(self, ShieldMd5):
        self._ShieldMd5 = ShieldMd5

    @property
    def ShieldSize(self):
        return self._ShieldSize

    @ShieldSize.setter
    def ShieldSize(self, ShieldSize):
        self._ShieldSize = ShieldSize


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        self._AppName = params.get("AppName")
        self._AppPkgName = params.get("AppPkgName")
        self._AppVersion = params.get("AppVersion")
        self._AppMd5 = params.get("AppMd5")
        self._AppSize = params.get("AppSize")
        self._ServiceEdition = params.get("ServiceEdition")
        self._ShieldCode = params.get("ShieldCode")
        self._AppUrl = params.get("AppUrl")
        self._TaskStatus = params.get("TaskStatus")
        self._ClientIp = params.get("ClientIp")
        self._TaskTime = params.get("TaskTime")
        self._AppIconUrl = params.get("AppIconUrl")
        self._ShieldMd5 = params.get("ShieldMd5")
        self._ShieldSize = params.get("ShieldSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppletInfo(AbstractModel):
    """小程序加固信息

    """

    def __init__(self):
        r"""
        :param _AppletJsUrl: 客户JS包
        :type AppletJsUrl: str
        :param _AppletLevel: 小程序加固等级配置
1 - 开启代码混淆、代码压缩、代码反调试保护。 2 - 开启字符串编码和代码变换，代码膨胀，随机插入冗余代码，开启代码控制流平坦化，保证业务逻辑正常前提下，扁平化代码逻辑分支，破坏代码简单的线性结构。 3 - 开启代码加密，对字符串、函数、变量、属性、类、数组等结构进行加密保护，更多得代码控制流平坦化，扁平化逻辑分支。
        :type AppletLevel: int
        :param _Name: 本次加固输出产物名称，如”test.zip“,非空必须是 ”.zip“结尾
        :type Name: str
        """
        self._AppletJsUrl = None
        self._AppletLevel = None
        self._Name = None

    @property
    def AppletJsUrl(self):
        return self._AppletJsUrl

    @AppletJsUrl.setter
    def AppletJsUrl(self, AppletJsUrl):
        self._AppletJsUrl = AppletJsUrl

    @property
    def AppletLevel(self):
        return self._AppletLevel

    @AppletLevel.setter
    def AppletLevel(self, AppletLevel):
        self._AppletLevel = AppletLevel

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._AppletJsUrl = params.get("AppletJsUrl")
        self._AppletLevel = params.get("AppletLevel")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppletPlan(AbstractModel):
    """小程序加固配置

    """

    def __init__(self):
        r"""
        :param _PlanId: 策略Id
        :type PlanId: int
        :param _AppletLevel: 1 - 开启代码混淆、代码压缩、代码反调试保护。
2 - 开启字符串编码和代码变换，代码膨胀，随机插入冗余代码，开启代码控制流平坦化，保证业务逻辑正常前提下，扁平化代码逻辑分支，破坏代码简单的线性结构。
3 - 开启代码加密，对字符串、函数、变量、属性、类、数组等结构进行加密保护，更多得代码控制流平坦化，扁平化逻辑分支。
        :type AppletLevel: int
        """
        self._PlanId = None
        self._AppletLevel = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def AppletLevel(self):
        return self._AppletLevel

    @AppletLevel.setter
    def AppletLevel(self, AppletLevel):
        self._AppletLevel = AppletLevel


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._AppletLevel = params.get("AppletLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppletResult(AbstractModel):
    """渠道合作加固小程序加固结果

    """

    def __init__(self):
        r"""
        :param _ResultId: 加固任务结果id
        :type ResultId: str
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _OrderId: 订单id
        :type OrderId: str
        :param _OpUin: 操作账号
        :type OpUin: int
        :param _EncryptState: 加固结果
        :type EncryptState: int
        :param _EncryptStateDesc: 加固结果描述
        :type EncryptStateDesc: str
        :param _EncryptErrCode: 失败错误码
        :type EncryptErrCode: int
        :param _EncryptErrDesc: 失败原因
        :type EncryptErrDesc: str
        :param _EncryptErrRef: 解决方案
        :type EncryptErrRef: str
        :param _CreatTime: 任务创建时间
        :type CreatTime: str
        :param _StartTime: 任务开始处理时间
        :type StartTime: str
        :param _EndTime: 任务处理结束时间
        :type EndTime: str
        :param _CostTime: 加固耗时（秒单位）
        :type CostTime: int
        :param _EncryptPkgUrl: 在线加固成功下载包
        :type EncryptPkgUrl: str
        :param _AppletInfo: 本次加固配置
        :type AppletInfo: :class:`tencentcloud.ms.v20180408.models.AppletInfo`
        """
        self._ResultId = None
        self._ResourceId = None
        self._OrderId = None
        self._OpUin = None
        self._EncryptState = None
        self._EncryptStateDesc = None
        self._EncryptErrCode = None
        self._EncryptErrDesc = None
        self._EncryptErrRef = None
        self._CreatTime = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None
        self._EncryptPkgUrl = None
        self._AppletInfo = None

    @property
    def ResultId(self):
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def OpUin(self):
        return self._OpUin

    @OpUin.setter
    def OpUin(self, OpUin):
        self._OpUin = OpUin

    @property
    def EncryptState(self):
        return self._EncryptState

    @EncryptState.setter
    def EncryptState(self, EncryptState):
        self._EncryptState = EncryptState

    @property
    def EncryptStateDesc(self):
        return self._EncryptStateDesc

    @EncryptStateDesc.setter
    def EncryptStateDesc(self, EncryptStateDesc):
        self._EncryptStateDesc = EncryptStateDesc

    @property
    def EncryptErrCode(self):
        return self._EncryptErrCode

    @EncryptErrCode.setter
    def EncryptErrCode(self, EncryptErrCode):
        self._EncryptErrCode = EncryptErrCode

    @property
    def EncryptErrDesc(self):
        return self._EncryptErrDesc

    @EncryptErrDesc.setter
    def EncryptErrDesc(self, EncryptErrDesc):
        self._EncryptErrDesc = EncryptErrDesc

    @property
    def EncryptErrRef(self):
        return self._EncryptErrRef

    @EncryptErrRef.setter
    def EncryptErrRef(self, EncryptErrRef):
        self._EncryptErrRef = EncryptErrRef

    @property
    def CreatTime(self):
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

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
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def EncryptPkgUrl(self):
        return self._EncryptPkgUrl

    @EncryptPkgUrl.setter
    def EncryptPkgUrl(self, EncryptPkgUrl):
        self._EncryptPkgUrl = EncryptPkgUrl

    @property
    def AppletInfo(self):
        return self._AppletInfo

    @AppletInfo.setter
    def AppletInfo(self, AppletInfo):
        self._AppletInfo = AppletInfo


    def _deserialize(self, params):
        self._ResultId = params.get("ResultId")
        self._ResourceId = params.get("ResourceId")
        self._OrderId = params.get("OrderId")
        self._OpUin = params.get("OpUin")
        self._EncryptState = params.get("EncryptState")
        self._EncryptStateDesc = params.get("EncryptStateDesc")
        self._EncryptErrCode = params.get("EncryptErrCode")
        self._EncryptErrDesc = params.get("EncryptErrDesc")
        self._EncryptErrRef = params.get("EncryptErrRef")
        self._CreatTime = params.get("CreatTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        self._EncryptPkgUrl = params.get("EncryptPkgUrl")
        if params.get("AppletInfo") is not None:
            self._AppletInfo = AppletInfo()
            self._AppletInfo._deserialize(params.get("AppletInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindInfo(AbstractModel):
    """用户绑定app的基本信息

    """

    def __init__(self):
        r"""
        :param _AppIconUrl: app的icon的url
        :type AppIconUrl: str
        :param _AppName: app的名称
        :type AppName: str
        :param _AppPkgName: app的包名
        :type AppPkgName: str
        """
        self._AppIconUrl = None
        self._AppName = None
        self._AppPkgName = None

    @property
    def AppIconUrl(self):
        return self._AppIconUrl

    @AppIconUrl.setter
    def AppIconUrl(self, AppIconUrl):
        self._AppIconUrl = AppIconUrl

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName


    def _deserialize(self, params):
        self._AppIconUrl = params.get("AppIconUrl")
        self._AppName = params.get("AppName")
        self._AppPkgName = params.get("AppPkgName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelEncryptTaskRequest(AbstractModel):
    """CancelEncryptTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultId: 加固任务结果Id 
        :type ResultId: str
        """
        self._ResultId = None

    @property
    def ResultId(self):
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId


    def _deserialize(self, params):
        self._ResultId = params.get("ResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelEncryptTaskResponse(AbstractModel):
    """CancelEncryptTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _State: 1: 取消任务成功 ； -1 ：取消任务失败，原因为任务进程已结束，不能取消。
        :type State: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._State = None
        self._RequestId = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._State = params.get("State")
        self._RequestId = params.get("RequestId")


class CreateBindInstanceRequest(AbstractModel):
    """CreateBindInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id，全局唯一
        :type ResourceId: str
        :param _AppIconUrl: app的icon的url
        :type AppIconUrl: str
        :param _AppName: app的名称
        :type AppName: str
        :param _AppPkgName: app的包名
        :type AppPkgName: str
        """
        self._ResourceId = None
        self._AppIconUrl = None
        self._AppName = None
        self._AppPkgName = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppIconUrl(self):
        return self._AppIconUrl

    @AppIconUrl.setter
    def AppIconUrl(self, AppIconUrl):
        self._AppIconUrl = AppIconUrl

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppIconUrl = params.get("AppIconUrl")
        self._AppName = params.get("AppName")
        self._AppPkgName = params.get("AppPkgName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBindInstanceResponse(AbstractModel):
    """CreateBindInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Progress = None
        self._RequestId = None

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Progress = params.get("Progress")
        self._RequestId = params.get("RequestId")


class CreateCosSecKeyInstanceRequest(AbstractModel):
    """CreateCosSecKeyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CosRegion: 地域信息，例如广州：ap-guangzhou，上海：ap-shanghai，默认为广州。
        :type CosRegion: str
        :param _Duration: 密钥有效时间，默认为1小时。
        :type Duration: int
        """
        self._CosRegion = None
        self._Duration = None

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._CosRegion = params.get("CosRegion")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosSecKeyInstanceResponse(AbstractModel):
    """CreateCosSecKeyInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CosAppid: COS密钥对应的AppId
        :type CosAppid: int
        :param _CosBucket: COS密钥对应的存储桶名
        :type CosBucket: str
        :param _CosRegion: 存储桶对应的地域
        :type CosRegion: str
        :param _ExpireTime: 密钥过期时间
        :type ExpireTime: int
        :param _CosId: 密钥ID信息
        :type CosId: str
        :param _CosKey: 密钥KEY信息
        :type CosKey: str
        :param _CosTocken: 密钥TOCKEN信息
        :type CosTocken: str
        :param _CosPrefix: 密钥可访问的文件前缀人。例如：CosPrefix=test/123/666，则该密钥只能操作test/123/666为前缀的文件，例如test/123/666/1.txt
        :type CosPrefix: str
        :param _CosToken: 密钥TOCKEN信息
        :type CosToken: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CosAppid = None
        self._CosBucket = None
        self._CosRegion = None
        self._ExpireTime = None
        self._CosId = None
        self._CosKey = None
        self._CosTocken = None
        self._CosPrefix = None
        self._CosToken = None
        self._RequestId = None

    @property
    def CosAppid(self):
        return self._CosAppid

    @CosAppid.setter
    def CosAppid(self, CosAppid):
        self._CosAppid = CosAppid

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CosId(self):
        return self._CosId

    @CosId.setter
    def CosId(self, CosId):
        self._CosId = CosId

    @property
    def CosKey(self):
        return self._CosKey

    @CosKey.setter
    def CosKey(self, CosKey):
        self._CosKey = CosKey

    @property
    def CosTocken(self):
        warnings.warn("parameter `CosTocken` is deprecated", DeprecationWarning) 

        return self._CosTocken

    @CosTocken.setter
    def CosTocken(self, CosTocken):
        warnings.warn("parameter `CosTocken` is deprecated", DeprecationWarning) 

        self._CosTocken = CosTocken

    @property
    def CosPrefix(self):
        return self._CosPrefix

    @CosPrefix.setter
    def CosPrefix(self, CosPrefix):
        self._CosPrefix = CosPrefix

    @property
    def CosToken(self):
        return self._CosToken

    @CosToken.setter
    def CosToken(self, CosToken):
        self._CosToken = CosToken

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CosAppid = params.get("CosAppid")
        self._CosBucket = params.get("CosBucket")
        self._CosRegion = params.get("CosRegion")
        self._ExpireTime = params.get("ExpireTime")
        self._CosId = params.get("CosId")
        self._CosKey = params.get("CosKey")
        self._CosTocken = params.get("CosTocken")
        self._CosPrefix = params.get("CosPrefix")
        self._CosToken = params.get("CosToken")
        self._RequestId = params.get("RequestId")


class CreateEncryptInstanceRequest(AbstractModel):
    """CreateEncryptInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlatformType: 平台类型  1.android加固   2.ios源码混淆  3.sdk加固  4.applet小程序加固
        :type PlatformType: int
        :param _OrderType: 订单采购类型 1-免费试用 2-按年收费 3-按次收费
        :type OrderType: int
        :param _EncryptOpType: 1-在线加固、  2-输出工具加固
        :type EncryptOpType: int
        :param _ResourceId: 本次加固使用的资源id
        :type ResourceId: str
        :param _AndroidAppInfo: 渠道合作android加固App信息 
        :type AndroidAppInfo: :class:`tencentcloud.ms.v20180408.models.AndroidAppInfo`
        :param _AndroidPlan: 渠道合作android加固策略信息
        :type AndroidPlan: :class:`tencentcloud.ms.v20180408.models.AndroidPlan`
        :param _AppletInfo: 小程序加固信息
        :type AppletInfo: :class:`tencentcloud.ms.v20180408.models.AppletInfo`
        :param _IOSInfo: iOS混淆信息
        :type IOSInfo: :class:`tencentcloud.ms.v20180408.models.IOSInfo`
        """
        self._PlatformType = None
        self._OrderType = None
        self._EncryptOpType = None
        self._ResourceId = None
        self._AndroidAppInfo = None
        self._AndroidPlan = None
        self._AppletInfo = None
        self._IOSInfo = None

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def EncryptOpType(self):
        return self._EncryptOpType

    @EncryptOpType.setter
    def EncryptOpType(self, EncryptOpType):
        self._EncryptOpType = EncryptOpType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AndroidAppInfo(self):
        return self._AndroidAppInfo

    @AndroidAppInfo.setter
    def AndroidAppInfo(self, AndroidAppInfo):
        self._AndroidAppInfo = AndroidAppInfo

    @property
    def AndroidPlan(self):
        return self._AndroidPlan

    @AndroidPlan.setter
    def AndroidPlan(self, AndroidPlan):
        self._AndroidPlan = AndroidPlan

    @property
    def AppletInfo(self):
        return self._AppletInfo

    @AppletInfo.setter
    def AppletInfo(self, AppletInfo):
        self._AppletInfo = AppletInfo

    @property
    def IOSInfo(self):
        return self._IOSInfo

    @IOSInfo.setter
    def IOSInfo(self, IOSInfo):
        self._IOSInfo = IOSInfo


    def _deserialize(self, params):
        self._PlatformType = params.get("PlatformType")
        self._OrderType = params.get("OrderType")
        self._EncryptOpType = params.get("EncryptOpType")
        self._ResourceId = params.get("ResourceId")
        if params.get("AndroidAppInfo") is not None:
            self._AndroidAppInfo = AndroidAppInfo()
            self._AndroidAppInfo._deserialize(params.get("AndroidAppInfo"))
        if params.get("AndroidPlan") is not None:
            self._AndroidPlan = AndroidPlan()
            self._AndroidPlan._deserialize(params.get("AndroidPlan"))
        if params.get("AppletInfo") is not None:
            self._AppletInfo = AppletInfo()
            self._AppletInfo._deserialize(params.get("AppletInfo"))
        if params.get("IOSInfo") is not None:
            self._IOSInfo = IOSInfo()
            self._IOSInfo._deserialize(params.get("IOSInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEncryptInstanceResponse(AbstractModel):
    """CreateEncryptInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultId: 加固任务Id
        :type ResultId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultId = None
        self._RequestId = None

    @property
    def ResultId(self):
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultId = params.get("ResultId")
        self._RequestId = params.get("RequestId")


class CreateOrderInstanceRequest(AbstractModel):
    """CreateOrderInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlatformType: 平台类型枚举值：1-android加固  ；2-ios源码混淆 ； 3-sdk加固 ； 4-applet小程序加固
        :type PlatformType: int
        :param _OrderType: 订单采购类型 1-免费试用 ；2-按年收费 ；3-按次收费
        :type OrderType: int
        :param _AppPkgNameList: 代表应用包名列表，值为单个包名（例如：“a.b.xxx”）或多个包名用逗号隔开(例如：“a.b.xxx,b.c.xxx”)。
当android按年收费加固或android免费试用加固时，该字段要求非空，即PlatformType=1 并且 OrderType=2时，AppPkgNameList必传值。

        :type AppPkgNameList: str
        """
        self._PlatformType = None
        self._OrderType = None
        self._AppPkgNameList = None

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def AppPkgNameList(self):
        return self._AppPkgNameList

    @AppPkgNameList.setter
    def AppPkgNameList(self, AppPkgNameList):
        self._AppPkgNameList = AppPkgNameList


    def _deserialize(self, params):
        self._PlatformType = params.get("PlatformType")
        self._OrderType = params.get("OrderType")
        self._AppPkgNameList = params.get("AppPkgNameList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrderInstanceResponse(AbstractModel):
    """CreateOrderInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单Id
        :type OrderId: str
        :param _ResourceId: 与订单关联的资源id
        :type ResourceId: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._ResourceId = None
        self._RequestId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._ResourceId = params.get("ResourceId")
        self._RequestId = params.get("RequestId")


class CreateResourceInstancesRequest(AbstractModel):
    """CreateResourceInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Pid: 资源类型id。13624：加固专业版。
        :type Pid: int
        :param _TimeUnit: 时间单位，取值为d，m，y，分别表示天，月，年。
        :type TimeUnit: str
        :param _TimeSpan: 时间数量。
        :type TimeSpan: int
        :param _ResourceNum: 资源数量。
        :type ResourceNum: int
        """
        self._Pid = None
        self._TimeUnit = None
        self._TimeSpan = None
        self._ResourceNum = None

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def TimeUnit(self):
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def ResourceNum(self):
        return self._ResourceNum

    @ResourceNum.setter
    def ResourceNum(self, ResourceNum):
        self._ResourceNum = ResourceNum


    def _deserialize(self, params):
        self._Pid = params.get("Pid")
        self._TimeUnit = params.get("TimeUnit")
        self._TimeSpan = params.get("TimeSpan")
        self._ResourceNum = params.get("ResourceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceInstancesResponse(AbstractModel):
    """CreateResourceInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceSet: 新创建的资源列表。
        :type ResourceSet: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceSet = None
        self._RequestId = None

    @property
    def ResourceSet(self):
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceSet = params.get("ResourceSet")
        self._RequestId = params.get("RequestId")


class CreateShieldInstanceRequest(AbstractModel):
    """CreateShieldInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppInfo: 待加固的应用信息
        :type AppInfo: :class:`tencentcloud.ms.v20180408.models.AppInfo`
        :param _ServiceInfo: 加固服务信息
        :type ServiceInfo: :class:`tencentcloud.ms.v20180408.models.ServiceInfo`
        """
        self._AppInfo = None
        self._ServiceInfo = None

    @property
    def AppInfo(self):
        return self._AppInfo

    @AppInfo.setter
    def AppInfo(self, AppInfo):
        self._AppInfo = AppInfo

    @property
    def ServiceInfo(self):
        return self._ServiceInfo

    @ServiceInfo.setter
    def ServiceInfo(self, ServiceInfo):
        self._ServiceInfo = ServiceInfo


    def _deserialize(self, params):
        if params.get("AppInfo") is not None:
            self._AppInfo = AppInfo()
            self._AppInfo._deserialize(params.get("AppInfo"))
        if params.get("ServiceInfo") is not None:
            self._ServiceInfo = ServiceInfo()
            self._ServiceInfo._deserialize(params.get("ServiceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShieldInstanceResponse(AbstractModel):
    """CreateShieldInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param _ItemId: 任务唯一标识
        :type ItemId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Progress = None
        self._ItemId = None
        self._RequestId = None

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ItemId(self):
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Progress = params.get("Progress")
        self._ItemId = params.get("ItemId")
        self._RequestId = params.get("RequestId")


class CreateShieldPlanInstanceRequest(AbstractModel):
    """CreateShieldPlanInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _PlanName: 策略名称
        :type PlanName: str
        :param _PlanInfo: 策略具体信息
        :type PlanInfo: :class:`tencentcloud.ms.v20180408.models.PlanInfo`
        """
        self._ResourceId = None
        self._PlanName = None
        self._PlanInfo = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def PlanInfo(self):
        return self._PlanInfo

    @PlanInfo.setter
    def PlanInfo(self, PlanInfo):
        self._PlanInfo = PlanInfo


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._PlanName = params.get("PlanName")
        if params.get("PlanInfo") is not None:
            self._PlanInfo = PlanInfo()
            self._PlanInfo._deserialize(params.get("PlanInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateShieldPlanInstanceResponse(AbstractModel):
    """CreateShieldPlanInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlanId: 策略id
        :type PlanId: int
        :param _Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlanId = None
        self._Progress = None
        self._RequestId = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._Progress = params.get("Progress")
        self._RequestId = params.get("RequestId")


class DeleteShieldInstancesRequest(AbstractModel):
    """DeleteShieldInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ItemIds: 任务唯一标识ItemId的列表
        :type ItemIds: list of str
        """
        self._ItemIds = None

    @property
    def ItemIds(self):
        return self._ItemIds

    @ItemIds.setter
    def ItemIds(self, ItemIds):
        self._ItemIds = ItemIds


    def _deserialize(self, params):
        self._ItemIds = params.get("ItemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShieldInstancesResponse(AbstractModel):
    """DeleteShieldInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Progress = None
        self._RequestId = None

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Progress = params.get("Progress")
        self._RequestId = params.get("RequestId")


class DescribeApkDetectionResultRequest(AbstractModel):
    """DescribeApkDetectionResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApkUrl: 软件包的下载链接
        :type ApkUrl: str
        :param _ApkMd5: 软件包的md5值，具有唯一性。腾讯APK云检测服务会根据md5值来判断该包是否为库中已收集的样本，已存在，则返回检测结果，反之，需要一定时间检测该样本。
        :type ApkMd5: str
        """
        self._ApkUrl = None
        self._ApkMd5 = None

    @property
    def ApkUrl(self):
        return self._ApkUrl

    @ApkUrl.setter
    def ApkUrl(self, ApkUrl):
        self._ApkUrl = ApkUrl

    @property
    def ApkMd5(self):
        return self._ApkMd5

    @ApkMd5.setter
    def ApkMd5(self, ApkMd5):
        self._ApkMd5 = ApkMd5


    def _deserialize(self, params):
        self._ApkUrl = params.get("ApkUrl")
        self._ApkMd5 = params.get("ApkMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApkDetectionResultResponse(AbstractModel):
    """DescribeApkDetectionResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 响应结果，ok表示正常，error表示错误
        :type Result: str
        :param _Reason: Result为error错误时的原因说明
        :type Reason: str
        :param _ResultList: APK检测结果数组
        :type ResultList: list of ResultListItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._Reason = None
        self._ResultList = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ResultList(self):
        return self._ResultList

    @ResultList.setter
    def ResultList(self, ResultList):
        self._ResultList = ResultList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._Reason = params.get("Reason")
        if params.get("ResultList") is not None:
            self._ResultList = []
            for item in params.get("ResultList"):
                obj = ResultListItem()
                obj._deserialize(item)
                self._ResultList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEncryptInstancesRequest(AbstractModel):
    """DescribeEncryptInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 多记录查询时使用，页码
        :type PageNumber: int
        :param _PageSize: 多记录每页展示数量
        :type PageSize: int
        :param _OrderField: 多记录查询时排序使用  仅支持CreateTime 任务创建时间排序
        :type OrderField: str
        :param _OrderDirection: 升序（asc）还是降序（desc），默认：desc。
        :type OrderDirection: str
        :param _PlatformType: (条件过滤字段) 平台类型  1.android加固   2.ios源码混淆  3.sdk加固  4.applet小程序加固
        :type PlatformType: int
        :param _OrderType: (条件过滤字段) 订单采购类型 1-免费试用 2-按年收费 3-按次收费
        :type OrderType: int
        :param _EncryptOpType: (条件过滤字段) 1-在线加固 或 2-输出工具加固
        :type EncryptOpType: int
        :param _ResultId: (条件过滤字段) 单记录查询时使用，结果ID该字段非空时，结构会根据结果ID进行单记录查询，符合查询条件时，只返回一条记录。
        :type ResultId: str
        :param _OrderId: (条件过滤字段) 查询与订单Id关联的任务
        :type OrderId: str
        :param _ResourceId: (条件过滤字段) 查询与资源Id关联的任务
        :type ResourceId: str
        :param _AppType: (条件过滤字段) 应用类型：android-apk; android-aab;
        :type AppType: str
        :param _AppPkgName: （条件过滤字段）应用的包名
        :type AppPkgName: str
        :param _EncryptState: 加固结果，
0：正在排队；
1：加固成功；
2：加固中；
3：加固失败；
5：重试；
多记录查询时，根据查询结果进行检索使用。
        :type EncryptState: list of int
        """
        self._PageNumber = None
        self._PageSize = None
        self._OrderField = None
        self._OrderDirection = None
        self._PlatformType = None
        self._OrderType = None
        self._EncryptOpType = None
        self._ResultId = None
        self._OrderId = None
        self._ResourceId = None
        self._AppType = None
        self._AppPkgName = None
        self._EncryptState = None

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
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def EncryptOpType(self):
        return self._EncryptOpType

    @EncryptOpType.setter
    def EncryptOpType(self, EncryptOpType):
        self._EncryptOpType = EncryptOpType

    @property
    def ResultId(self):
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def EncryptState(self):
        return self._EncryptState

    @EncryptState.setter
    def EncryptState(self, EncryptState):
        self._EncryptState = EncryptState


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        self._PlatformType = params.get("PlatformType")
        self._OrderType = params.get("OrderType")
        self._EncryptOpType = params.get("EncryptOpType")
        self._ResultId = params.get("ResultId")
        self._OrderId = params.get("OrderId")
        self._ResourceId = params.get("ResourceId")
        self._AppType = params.get("AppType")
        self._AppPkgName = params.get("AppPkgName")
        self._EncryptState = params.get("EncryptState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEncryptInstancesResponse(AbstractModel):
    """DescribeEncryptInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _EncryptResults: 渠道合作加固信息数组
        :type EncryptResults: list of EncryptResults
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._EncryptResults = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EncryptResults(self):
        return self._EncryptResults

    @EncryptResults.setter
    def EncryptResults(self, EncryptResults):
        self._EncryptResults = EncryptResults

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EncryptResults") is not None:
            self._EncryptResults = []
            for item in params.get("EncryptResults"):
                obj = EncryptResults()
                obj._deserialize(item)
                self._EncryptResults.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEncryptPlanRequest(AbstractModel):
    """DescribeEncryptPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PlatformType: 平台类型  1.android加固   2.ios源码混淆  3.sdk加固  4.applet小程序加固
        :type PlatformType: int
        :param _OrderType: 订单采购类型 1-免费试用 2-按年收费 3-按次收费
        :type OrderType: int
        :param _EncryptOpType: 1-在线加固；2-输出工具
        :type EncryptOpType: int
        :param _ResourceId: 本次加固使用的资源id
        :type ResourceId: str
        :param _AppPkgName: （条件过滤字段）加固查询时，根据包名查询
        :type AppPkgName: str
        :param _AppType: （条件过滤字段）加固查询时，根据应用格式查询，枚举值：“apk”、“aab”
        :type AppType: str
        """
        self._PlatformType = None
        self._OrderType = None
        self._EncryptOpType = None
        self._ResourceId = None
        self._AppPkgName = None
        self._AppType = None

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def EncryptOpType(self):
        return self._EncryptOpType

    @EncryptOpType.setter
    def EncryptOpType(self, EncryptOpType):
        self._EncryptOpType = EncryptOpType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def AppType(self):
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType


    def _deserialize(self, params):
        self._PlatformType = params.get("PlatformType")
        self._OrderType = params.get("OrderType")
        self._EncryptOpType = params.get("EncryptOpType")
        self._ResourceId = params.get("ResourceId")
        self._AppPkgName = params.get("AppPkgName")
        self._AppType = params.get("AppType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEncryptPlanResponse(AbstractModel):
    """DescribeEncryptPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PlatformType: 平台类型整型值  
        :type PlatformType: int
        :param _PlatformTypeDesc: 平台类型描述 1.android加固   2.ios源码混淆  3.sdk加固  4.applet小程序加固
        :type PlatformTypeDesc: str
        :param _EncryptOpType: 1- 在线加固 2-输出工具加固
        :type EncryptOpType: int
        :param _EncryptOpTypeDesc: 1- 在线加固 2-输出工具加固
        :type EncryptOpTypeDesc: str
        :param _OrderType: 订单收费类型枚举值
        :type OrderType: int
        :param _OrderTypeDesc: 订单收费类型描述
        :type OrderTypeDesc: str
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _AndroidPlan: 上次加固策略
注意：此字段可能返回 null，表示取不到有效值。
        :type AndroidPlan: :class:`tencentcloud.ms.v20180408.models.AndroidPlan`
        :param _AppletPlan: 上次小程序加固策略
注意：此字段可能返回 null，表示取不到有效值。
        :type AppletPlan: :class:`tencentcloud.ms.v20180408.models.AppletPlan`
        :param _IOSPlan: 上次ios源码混淆加固配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IOSPlan: :class:`tencentcloud.ms.v20180408.models.IOSPlan`
        :param _SDKPlan: 上次sdk加固配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SDKPlan: :class:`tencentcloud.ms.v20180408.models.SDKPlan`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PlatformType = None
        self._PlatformTypeDesc = None
        self._EncryptOpType = None
        self._EncryptOpTypeDesc = None
        self._OrderType = None
        self._OrderTypeDesc = None
        self._ResourceId = None
        self._AndroidPlan = None
        self._AppletPlan = None
        self._IOSPlan = None
        self._SDKPlan = None
        self._RequestId = None

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def PlatformTypeDesc(self):
        return self._PlatformTypeDesc

    @PlatformTypeDesc.setter
    def PlatformTypeDesc(self, PlatformTypeDesc):
        self._PlatformTypeDesc = PlatformTypeDesc

    @property
    def EncryptOpType(self):
        return self._EncryptOpType

    @EncryptOpType.setter
    def EncryptOpType(self, EncryptOpType):
        self._EncryptOpType = EncryptOpType

    @property
    def EncryptOpTypeDesc(self):
        return self._EncryptOpTypeDesc

    @EncryptOpTypeDesc.setter
    def EncryptOpTypeDesc(self, EncryptOpTypeDesc):
        self._EncryptOpTypeDesc = EncryptOpTypeDesc

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def OrderTypeDesc(self):
        return self._OrderTypeDesc

    @OrderTypeDesc.setter
    def OrderTypeDesc(self, OrderTypeDesc):
        self._OrderTypeDesc = OrderTypeDesc

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AndroidPlan(self):
        return self._AndroidPlan

    @AndroidPlan.setter
    def AndroidPlan(self, AndroidPlan):
        self._AndroidPlan = AndroidPlan

    @property
    def AppletPlan(self):
        return self._AppletPlan

    @AppletPlan.setter
    def AppletPlan(self, AppletPlan):
        self._AppletPlan = AppletPlan

    @property
    def IOSPlan(self):
        return self._IOSPlan

    @IOSPlan.setter
    def IOSPlan(self, IOSPlan):
        self._IOSPlan = IOSPlan

    @property
    def SDKPlan(self):
        return self._SDKPlan

    @SDKPlan.setter
    def SDKPlan(self, SDKPlan):
        self._SDKPlan = SDKPlan

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PlatformType = params.get("PlatformType")
        self._PlatformTypeDesc = params.get("PlatformTypeDesc")
        self._EncryptOpType = params.get("EncryptOpType")
        self._EncryptOpTypeDesc = params.get("EncryptOpTypeDesc")
        self._OrderType = params.get("OrderType")
        self._OrderTypeDesc = params.get("OrderTypeDesc")
        self._ResourceId = params.get("ResourceId")
        if params.get("AndroidPlan") is not None:
            self._AndroidPlan = AndroidPlan()
            self._AndroidPlan._deserialize(params.get("AndroidPlan"))
        if params.get("AppletPlan") is not None:
            self._AppletPlan = AppletPlan()
            self._AppletPlan._deserialize(params.get("AppletPlan"))
        if params.get("IOSPlan") is not None:
            self._IOSPlan = IOSPlan()
            self._IOSPlan._deserialize(params.get("IOSPlan"))
        if params.get("SDKPlan") is not None:
            self._SDKPlan = SDKPlan()
            self._SDKPlan._deserialize(params.get("SDKPlan"))
        self._RequestId = params.get("RequestId")


class DescribeOrderInstancesRequest(AbstractModel):
    """DescribeOrderInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: 页码
        :type PageNumber: int
        :param _PageSize: 每页展示数量
        :type PageSize: int
        :param _OrderField: 按某个字段排序，目前仅支持CreateTime排序。
        :type OrderField: str
        :param _OrderDirection: 升序（asc）还是降序（desc），默认：desc。
        :type OrderDirection: str
        :param _PlatformType: （条件过滤字段）平台类型  1.android加固   2.ios源码混淆  3.sdk加固  4.applet小程序加固
        :type PlatformType: int
        :param _OrderType: （条件过滤字段）订单采购类型 1-免费试用 2-按年收费 3-按次收费
        :type OrderType: int
        :param _ApprovalStatus: （条件过滤字段）订单审批状态：
        :type ApprovalStatus: int
        :param _ResourceStatus: （条件过滤字段）资源状态：
        :type ResourceStatus: int
        :param _OrderId: （条件过滤字段）订单ID
        :type OrderId: str
        :param _ResourceId: （条件过滤字段）资源ID
        :type ResourceId: str
        :param _AppPkgName: （条件过滤字段）包名，查询android加固订单时使用
        :type AppPkgName: str
        """
        self._PageNumber = None
        self._PageSize = None
        self._OrderField = None
        self._OrderDirection = None
        self._PlatformType = None
        self._OrderType = None
        self._ApprovalStatus = None
        self._ResourceStatus = None
        self._OrderId = None
        self._ResourceId = None
        self._AppPkgName = None

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
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def ApprovalStatus(self):
        return self._ApprovalStatus

    @ApprovalStatus.setter
    def ApprovalStatus(self, ApprovalStatus):
        self._ApprovalStatus = ApprovalStatus

    @property
    def ResourceStatus(self):
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        self._PlatformType = params.get("PlatformType")
        self._OrderType = params.get("OrderType")
        self._ApprovalStatus = params.get("ApprovalStatus")
        self._ResourceStatus = params.get("ResourceStatus")
        self._OrderId = params.get("OrderId")
        self._ResourceId = params.get("ResourceId")
        self._AppPkgName = params.get("AppPkgName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrderInstancesResponse(AbstractModel):
    """DescribeOrderInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _Orders: 订单信息
        :type Orders: list of Orders
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Orders = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Orders(self):
        return self._Orders

    @Orders.setter
    def Orders(self, Orders):
        self._Orders = Orders

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Orders") is not None:
            self._Orders = []
            for item in params.get("Orders"):
                obj = Orders()
                obj._deserialize(item)
                self._Orders.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceInstancesRequest(AbstractModel):
    """DescribeResourceInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 支持CreateTime、ExpireTime、AppName、AppPkgName、BindValue、IsBind过滤
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 数量限制，默认为20，最大值为100。
        :type Limit: int
        :param _Pids: 资源类别id数组，13624：加固专业版，12750：企业版。空数组表示返回全部资源。
        :type Pids: list of int non-negative
        :param _OrderField: 按某个字段排序，目前支持CreateTime、ExpireTime其中的一个排序。
        :type OrderField: str
        :param _OrderDirection: 升序（asc）还是降序（desc），默认：desc。
        :type OrderDirection: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Pids = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Pids(self):
        return self._Pids

    @Pids.setter
    def Pids(self, Pids):
        self._Pids = Pids

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Pids = params.get("Pids")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceInstancesResponse(AbstractModel):
    """DescribeResourceInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合要求的资源数量
        :type TotalCount: int
        :param _ResourceSet: 符合要求的资源数组
        :type ResourceSet: list of ResourceInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResourceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResourceSet(self):
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShieldInstancesRequest(AbstractModel):
    """DescribeShieldInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 支持通过app名称，app包名，加固的服务版本，提交的渠道进行筛选。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 数量限制，默认为20，最大值为100。
        :type Limit: int
        :param _ItemIds: 可以提供ItemId数组来查询一个或者多个结果。注意不可以同时指定ItemIds和Filters。
        :type ItemIds: list of str
        :param _OrderField: 按某个字段排序，目前仅支持TaskTime排序。
        :type OrderField: str
        :param _OrderDirection: 升序（asc）还是降序（desc），默认：desc。
        :type OrderDirection: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._ItemIds = None
        self._OrderField = None
        self._OrderDirection = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ItemIds(self):
        return self._ItemIds

    @ItemIds.setter
    def ItemIds(self, ItemIds):
        self._ItemIds = ItemIds

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDirection(self):
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ItemIds = params.get("ItemIds")
        self._OrderField = params.get("OrderField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShieldInstancesResponse(AbstractModel):
    """DescribeShieldInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合要求的app数量
        :type TotalCount: int
        :param _AppSet: 一个关于app详细信息的结构体，主要包括app的基本信息和加固信息。
        :type AppSet: list of AppSetInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AppSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AppSet(self):
        return self._AppSet

    @AppSet.setter
    def AppSet(self, AppSet):
        self._AppSet = AppSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AppSet") is not None:
            self._AppSet = []
            for item in params.get("AppSet"):
                obj = AppSetInfo()
                obj._deserialize(item)
                self._AppSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShieldPlanInstanceRequest(AbstractModel):
    """DescribeShieldPlanInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _Pid: 服务类别id
        :type Pid: int
        """
        self._ResourceId = None
        self._Pid = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShieldPlanInstanceResponse(AbstractModel):
    """DescribeShieldPlanInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindInfo: 绑定资源信息
        :type BindInfo: :class:`tencentcloud.ms.v20180408.models.BindInfo`
        :param _ShieldPlanInfo: 加固策略信息
        :type ShieldPlanInfo: :class:`tencentcloud.ms.v20180408.models.ShieldPlanInfo`
        :param _ResourceServiceInfo: 加固资源信息
        :type ResourceServiceInfo: :class:`tencentcloud.ms.v20180408.models.ResourceServiceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindInfo = None
        self._ShieldPlanInfo = None
        self._ResourceServiceInfo = None
        self._RequestId = None

    @property
    def BindInfo(self):
        return self._BindInfo

    @BindInfo.setter
    def BindInfo(self, BindInfo):
        self._BindInfo = BindInfo

    @property
    def ShieldPlanInfo(self):
        return self._ShieldPlanInfo

    @ShieldPlanInfo.setter
    def ShieldPlanInfo(self, ShieldPlanInfo):
        self._ShieldPlanInfo = ShieldPlanInfo

    @property
    def ResourceServiceInfo(self):
        return self._ResourceServiceInfo

    @ResourceServiceInfo.setter
    def ResourceServiceInfo(self, ResourceServiceInfo):
        self._ResourceServiceInfo = ResourceServiceInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BindInfo") is not None:
            self._BindInfo = BindInfo()
            self._BindInfo._deserialize(params.get("BindInfo"))
        if params.get("ShieldPlanInfo") is not None:
            self._ShieldPlanInfo = ShieldPlanInfo()
            self._ShieldPlanInfo._deserialize(params.get("ShieldPlanInfo"))
        if params.get("ResourceServiceInfo") is not None:
            self._ResourceServiceInfo = ResourceServiceInfo()
            self._ResourceServiceInfo._deserialize(params.get("ResourceServiceInfo"))
        self._RequestId = params.get("RequestId")


class DescribeShieldResultRequest(AbstractModel):
    """DescribeShieldResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ItemId: 任务唯一标识
        :type ItemId: str
        """
        self._ItemId = None

    @property
    def ItemId(self):
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId


    def _deserialize(self, params):
        self._ItemId = params.get("ItemId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShieldResultResponse(AbstractModel):
    """DescribeShieldResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 任务状态: 0-请返回,1-已完成,2-处理中,3-处理出错,4-处理超时
        :type TaskStatus: int
        :param _AppDetailInfo: app加固前的详细信息
        :type AppDetailInfo: :class:`tencentcloud.ms.v20180408.models.AppDetailInfo`
        :param _ShieldInfo: app加固后的详细信息
        :type ShieldInfo: :class:`tencentcloud.ms.v20180408.models.ShieldInfo`
        :param _StatusDesc: 状态描述
        :type StatusDesc: str
        :param _StatusRef: 状态指引
        :type StatusRef: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._AppDetailInfo = None
        self._ShieldInfo = None
        self._StatusDesc = None
        self._StatusRef = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def AppDetailInfo(self):
        return self._AppDetailInfo

    @AppDetailInfo.setter
    def AppDetailInfo(self, AppDetailInfo):
        self._AppDetailInfo = AppDetailInfo

    @property
    def ShieldInfo(self):
        return self._ShieldInfo

    @ShieldInfo.setter
    def ShieldInfo(self, ShieldInfo):
        self._ShieldInfo = ShieldInfo

    @property
    def StatusDesc(self):
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def StatusRef(self):
        return self._StatusRef

    @StatusRef.setter
    def StatusRef(self, StatusRef):
        self._StatusRef = StatusRef

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskStatus = params.get("TaskStatus")
        if params.get("AppDetailInfo") is not None:
            self._AppDetailInfo = AppDetailInfo()
            self._AppDetailInfo._deserialize(params.get("AppDetailInfo"))
        if params.get("ShieldInfo") is not None:
            self._ShieldInfo = ShieldInfo()
            self._ShieldInfo._deserialize(params.get("ShieldInfo"))
        self._StatusDesc = params.get("StatusDesc")
        self._StatusRef = params.get("StatusRef")
        self._RequestId = params.get("RequestId")


class DescribeUrlDetectionResultRequest(AbstractModel):
    """DescribeUrlDetectionResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 查询的网址
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
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
        


class DescribeUrlDetectionResultResponse(AbstractModel):
    """DescribeUrlDetectionResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: [查询结果]查询结果；枚举值：0 查询成功，否则查询失败
        :type ResultCode: int
        :param _RespVer: [固定信息]响应协议版本号
        :type RespVer: int
        :param _UrlType: [查询结果]url恶意状态
枚举值：
0-1：未知，访问暂无风险。
2 ：	风险网址，具体的恶意类型定义参考恶意大类EvilClass字段。
3-4：安全，访问无风险。

注意：查询结果EvilClass字段在Urltype=2时，才有意义。
        :type UrlType: int
        :param _EvilClass: [查询结果]url恶意类型大类:{
    "1": "社工欺诈（仿冒、账号钓鱼、中奖诈骗）",
    "2": "信息诈骗（虚假充值、虚假兼职、虚假金融投资、虚假信用卡代办、网络赌博诈骗）",
    "3": "虚假销售（男女保健美容减肥产品、电子产品、虚假广告、违法销售）",
    "4": "恶意文件（病毒文件，木马文件，恶意apk文件的下载链接以及站点，挂马网站）",
    "5": "博彩网站（博彩网站，在线赌博网站）",
    "6": "色情网站（涉嫌传播色情内容，提供色情服务的网站）"
  }
        :type EvilClass: int
        :param _EvilType: 该字段暂为空
        :type EvilType: int
        :param _Level: 该字段暂为空
        :type Level: int
        :param _DetectTime: [查询详情]url检出时间；时间戳
        :type DetectTime: int
        :param _Wording: 该字段暂为空
        :type Wording: str
        :param _WordingTitle: 该字段暂为空
        :type WordingTitle: str
        :param _UrlTypeDesc: [查询结果]url恶意状态说明；为UrlType字段值对应的说明
        :type UrlTypeDesc: str
        :param _EvilClassDesc: [查询结果]url恶意大类说明；为EvilClass字段值对应的说明
        :type EvilClassDesc: str
        :param _EvilTypeDesc: 该字段暂为空
        :type EvilTypeDesc: str
        :param _LevelDesc: 该字段暂为空
        :type LevelDesc: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._RespVer = None
        self._UrlType = None
        self._EvilClass = None
        self._EvilType = None
        self._Level = None
        self._DetectTime = None
        self._Wording = None
        self._WordingTitle = None
        self._UrlTypeDesc = None
        self._EvilClassDesc = None
        self._EvilTypeDesc = None
        self._LevelDesc = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def RespVer(self):
        return self._RespVer

    @RespVer.setter
    def RespVer(self, RespVer):
        self._RespVer = RespVer

    @property
    def UrlType(self):
        return self._UrlType

    @UrlType.setter
    def UrlType(self, UrlType):
        self._UrlType = UrlType

    @property
    def EvilClass(self):
        return self._EvilClass

    @EvilClass.setter
    def EvilClass(self, EvilClass):
        self._EvilClass = EvilClass

    @property
    def EvilType(self):
        return self._EvilType

    @EvilType.setter
    def EvilType(self, EvilType):
        self._EvilType = EvilType

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def DetectTime(self):
        return self._DetectTime

    @DetectTime.setter
    def DetectTime(self, DetectTime):
        self._DetectTime = DetectTime

    @property
    def Wording(self):
        return self._Wording

    @Wording.setter
    def Wording(self, Wording):
        self._Wording = Wording

    @property
    def WordingTitle(self):
        return self._WordingTitle

    @WordingTitle.setter
    def WordingTitle(self, WordingTitle):
        self._WordingTitle = WordingTitle

    @property
    def UrlTypeDesc(self):
        return self._UrlTypeDesc

    @UrlTypeDesc.setter
    def UrlTypeDesc(self, UrlTypeDesc):
        self._UrlTypeDesc = UrlTypeDesc

    @property
    def EvilClassDesc(self):
        return self._EvilClassDesc

    @EvilClassDesc.setter
    def EvilClassDesc(self, EvilClassDesc):
        self._EvilClassDesc = EvilClassDesc

    @property
    def EvilTypeDesc(self):
        return self._EvilTypeDesc

    @EvilTypeDesc.setter
    def EvilTypeDesc(self, EvilTypeDesc):
        self._EvilTypeDesc = EvilTypeDesc

    @property
    def LevelDesc(self):
        return self._LevelDesc

    @LevelDesc.setter
    def LevelDesc(self, LevelDesc):
        self._LevelDesc = LevelDesc

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._RespVer = params.get("RespVer")
        self._UrlType = params.get("UrlType")
        self._EvilClass = params.get("EvilClass")
        self._EvilType = params.get("EvilType")
        self._Level = params.get("Level")
        self._DetectTime = params.get("DetectTime")
        self._Wording = params.get("Wording")
        self._WordingTitle = params.get("WordingTitle")
        self._UrlTypeDesc = params.get("UrlTypeDesc")
        self._EvilClassDesc = params.get("EvilClassDesc")
        self._EvilTypeDesc = params.get("EvilTypeDesc")
        self._LevelDesc = params.get("LevelDesc")
        self._RequestId = params.get("RequestId")


class DescribeUserBaseInfoInstanceRequest(AbstractModel):
    """DescribeUserBaseInfoInstance请求参数结构体

    """


class DescribeUserBaseInfoInstanceResponse(AbstractModel):
    """DescribeUserBaseInfoInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserUin: 用户uin信息
        :type UserUin: int
        :param _UserAppid: 用户APPID信息
        :type UserAppid: int
        :param _TimeStamp: 系统时间戳
        :type TimeStamp: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserUin = None
        self._UserAppid = None
        self._TimeStamp = None
        self._RequestId = None

    @property
    def UserUin(self):
        return self._UserUin

    @UserUin.setter
    def UserUin(self, UserUin):
        self._UserUin = UserUin

    @property
    def UserAppid(self):
        return self._UserAppid

    @UserAppid.setter
    def UserAppid(self, UserAppid):
        self._UserAppid = UserAppid

    @property
    def TimeStamp(self):
        return self._TimeStamp

    @TimeStamp.setter
    def TimeStamp(self, TimeStamp):
        self._TimeStamp = TimeStamp

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserUin = params.get("UserUin")
        self._UserAppid = params.get("UserAppid")
        self._TimeStamp = params.get("TimeStamp")
        self._RequestId = params.get("RequestId")


class EncryptResults(AbstractModel):
    """渠道合作加固结果信息

    """

    def __init__(self):
        r"""
        :param _PlatformType: 平台类型枚举值  1-android加固   2-ios源码混淆  3-sdk加固  4-applet小程序加固
        :type PlatformType: int
        :param _PlatformDesc: 平台类型描述  1-android加固   2-ios源码混淆  3-sdk加固  4-applet小程序加固
        :type PlatformDesc: str
        :param _OrderType: 订单采购类型枚举值， 1-免费试用 2-按年收费 3-按次收费
        :type OrderType: int
        :param _OrderTypeDesc: 订单采购类型 描述：1-免费试用 2-按年收费 3-按次收费
        :type OrderTypeDesc: str
        :param _EncryptOpType: 枚举值：1-在线加固 或 2-输出工具加固
        :type EncryptOpType: int
        :param _EncryptOpTypeDesc: 描述：1-在线加固 或 2-输出工具加固
        :type EncryptOpTypeDesc: str
        :param _ResourceId: 与当前任务关联的资源Id
        :type ResourceId: str
        :param _OrderId: 与当前任务关联的订单Id
        :type OrderId: str
        :param _AndroidResult: 对应PlatformType平台类型值   1-android加固结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AndroidResult: :class:`tencentcloud.ms.v20180408.models.AndroidResult`
        :param _IOSResult: 对应PlatformType平台类型值   2-ios源码混淆加固结果
注意：此字段可能返回 null，表示取不到有效值。
        :type IOSResult: :class:`tencentcloud.ms.v20180408.models.IOSResult`
        :param _SDKResult: 对应PlatformType平台类型值   3-sdk加固结果
注意：此字段可能返回 null，表示取不到有效值。
        :type SDKResult: :class:`tencentcloud.ms.v20180408.models.SDKResult`
        :param _AppletResult: 对应PlatformType平台类型值   4-applet小程序加固结果
注意：此字段可能返回 null，表示取不到有效值。
        :type AppletResult: :class:`tencentcloud.ms.v20180408.models.AppletResult`
        """
        self._PlatformType = None
        self._PlatformDesc = None
        self._OrderType = None
        self._OrderTypeDesc = None
        self._EncryptOpType = None
        self._EncryptOpTypeDesc = None
        self._ResourceId = None
        self._OrderId = None
        self._AndroidResult = None
        self._IOSResult = None
        self._SDKResult = None
        self._AppletResult = None

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def PlatformDesc(self):
        return self._PlatformDesc

    @PlatformDesc.setter
    def PlatformDesc(self, PlatformDesc):
        self._PlatformDesc = PlatformDesc

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def OrderTypeDesc(self):
        return self._OrderTypeDesc

    @OrderTypeDesc.setter
    def OrderTypeDesc(self, OrderTypeDesc):
        self._OrderTypeDesc = OrderTypeDesc

    @property
    def EncryptOpType(self):
        return self._EncryptOpType

    @EncryptOpType.setter
    def EncryptOpType(self, EncryptOpType):
        self._EncryptOpType = EncryptOpType

    @property
    def EncryptOpTypeDesc(self):
        return self._EncryptOpTypeDesc

    @EncryptOpTypeDesc.setter
    def EncryptOpTypeDesc(self, EncryptOpTypeDesc):
        self._EncryptOpTypeDesc = EncryptOpTypeDesc

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def AndroidResult(self):
        return self._AndroidResult

    @AndroidResult.setter
    def AndroidResult(self, AndroidResult):
        self._AndroidResult = AndroidResult

    @property
    def IOSResult(self):
        return self._IOSResult

    @IOSResult.setter
    def IOSResult(self, IOSResult):
        self._IOSResult = IOSResult

    @property
    def SDKResult(self):
        return self._SDKResult

    @SDKResult.setter
    def SDKResult(self, SDKResult):
        self._SDKResult = SDKResult

    @property
    def AppletResult(self):
        return self._AppletResult

    @AppletResult.setter
    def AppletResult(self, AppletResult):
        self._AppletResult = AppletResult


    def _deserialize(self, params):
        self._PlatformType = params.get("PlatformType")
        self._PlatformDesc = params.get("PlatformDesc")
        self._OrderType = params.get("OrderType")
        self._OrderTypeDesc = params.get("OrderTypeDesc")
        self._EncryptOpType = params.get("EncryptOpType")
        self._EncryptOpTypeDesc = params.get("EncryptOpTypeDesc")
        self._ResourceId = params.get("ResourceId")
        self._OrderId = params.get("OrderId")
        if params.get("AndroidResult") is not None:
            self._AndroidResult = AndroidResult()
            self._AndroidResult._deserialize(params.get("AndroidResult"))
        if params.get("IOSResult") is not None:
            self._IOSResult = IOSResult()
            self._IOSResult._deserialize(params.get("IOSResult"))
        if params.get("SDKResult") is not None:
            self._SDKResult = SDKResult()
            self._SDKResult._deserialize(params.get("SDKResult"))
        if params.get("AppletResult") is not None:
            self._AppletResult = AppletResult()
            self._AppletResult._deserialize(params.get("AppletResult"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """筛选数据结构

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段
        :type Name: str
        :param _Value: 需要过滤字段的值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IOSInfo(AbstractModel):
    """iOS加固信息

    	InfoPListUrl  string `json:"InfoPListUrl"`  //info.plist的url，必须保证不用权限校验就可以下载
    	InfoPListSize int64  `json:"InfoPListSize"` //info.plist文件的大小
    	InfoPListMd5  string `json:"InfoPListMd5"`  //info.plist文件的md5
    	BuildType     string `json:"BuildType"`     //release: 需要INFO-PLIST文件，会生成工具部署安装包，并带有license文件，绑定机器；nobind不需要INFO-PLIST文件，不绑定机器

    """

    def __init__(self):
        r"""
        :param _InfoPListUrl: info.plist的url，必须保证不用权限校验就可以下载
        :type InfoPListUrl: str
        :param _InfoPListSize: info.plist文件的大小
        :type InfoPListSize: int
        :param _InfoPListMd5: info.plist文件的md5
        :type InfoPListMd5: str
        :param _BuildType: release: 需要INFO-PLIST文件，会生成工具部署安装包，并带有license文件，绑定机器；nobind不需要INFO-PLIST文件，不绑定机器
        :type BuildType: str
        """
        self._InfoPListUrl = None
        self._InfoPListSize = None
        self._InfoPListMd5 = None
        self._BuildType = None

    @property
    def InfoPListUrl(self):
        return self._InfoPListUrl

    @InfoPListUrl.setter
    def InfoPListUrl(self, InfoPListUrl):
        self._InfoPListUrl = InfoPListUrl

    @property
    def InfoPListSize(self):
        return self._InfoPListSize

    @InfoPListSize.setter
    def InfoPListSize(self, InfoPListSize):
        self._InfoPListSize = InfoPListSize

    @property
    def InfoPListMd5(self):
        return self._InfoPListMd5

    @InfoPListMd5.setter
    def InfoPListMd5(self, InfoPListMd5):
        self._InfoPListMd5 = InfoPListMd5

    @property
    def BuildType(self):
        return self._BuildType

    @BuildType.setter
    def BuildType(self, BuildType):
        self._BuildType = BuildType


    def _deserialize(self, params):
        self._InfoPListUrl = params.get("InfoPListUrl")
        self._InfoPListSize = params.get("InfoPListSize")
        self._InfoPListMd5 = params.get("InfoPListMd5")
        self._BuildType = params.get("BuildType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IOSPlan(AbstractModel):
    """渠道合作IOS源码混淆配置

    """

    def __init__(self):
        r"""
        :param _PlanId: 策略id
        :type PlanId: int
        """
        self._PlanId = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IOSResult(AbstractModel):
    """渠道合作ios源码混淆加固结果

    """

    def __init__(self):
        r"""
        :param _ResultId: 加固任务结果Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultId: str
        :param _OpUin: 用户uid
注意：此字段可能返回 null，表示取不到有效值。
        :type OpUin: int
        :param _EncryptType: 加固类型，这里为ios
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptType: str
        :param _ResourceId: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _EncryptState: 加固状态
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptState: int
        :param _EncryptErrno: 业务错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptErrno: int
        :param _EncryptErrDesc: 业务错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptErrDesc: str
        :param _CreatTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatTime: str
        :param _StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CostTime: 消耗时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CostTime: int
        :param _EncryptPkgUrl: 加固（混淆）包结果url
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptPkgUrl: str
        """
        self._ResultId = None
        self._OpUin = None
        self._EncryptType = None
        self._ResourceId = None
        self._EncryptState = None
        self._EncryptErrno = None
        self._EncryptErrDesc = None
        self._CreatTime = None
        self._StartTime = None
        self._EndTime = None
        self._CostTime = None
        self._EncryptPkgUrl = None

    @property
    def ResultId(self):
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId

    @property
    def OpUin(self):
        return self._OpUin

    @OpUin.setter
    def OpUin(self, OpUin):
        self._OpUin = OpUin

    @property
    def EncryptType(self):
        return self._EncryptType

    @EncryptType.setter
    def EncryptType(self, EncryptType):
        self._EncryptType = EncryptType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def EncryptState(self):
        return self._EncryptState

    @EncryptState.setter
    def EncryptState(self, EncryptState):
        self._EncryptState = EncryptState

    @property
    def EncryptErrno(self):
        return self._EncryptErrno

    @EncryptErrno.setter
    def EncryptErrno(self, EncryptErrno):
        self._EncryptErrno = EncryptErrno

    @property
    def EncryptErrDesc(self):
        return self._EncryptErrDesc

    @EncryptErrDesc.setter
    def EncryptErrDesc(self, EncryptErrDesc):
        self._EncryptErrDesc = EncryptErrDesc

    @property
    def CreatTime(self):
        return self._CreatTime

    @CreatTime.setter
    def CreatTime(self, CreatTime):
        self._CreatTime = CreatTime

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
    def CostTime(self):
        return self._CostTime

    @CostTime.setter
    def CostTime(self, CostTime):
        self._CostTime = CostTime

    @property
    def EncryptPkgUrl(self):
        return self._EncryptPkgUrl

    @EncryptPkgUrl.setter
    def EncryptPkgUrl(self, EncryptPkgUrl):
        self._EncryptPkgUrl = EncryptPkgUrl


    def _deserialize(self, params):
        self._ResultId = params.get("ResultId")
        self._OpUin = params.get("OpUin")
        self._EncryptType = params.get("EncryptType")
        self._ResourceId = params.get("ResourceId")
        self._EncryptState = params.get("EncryptState")
        self._EncryptErrno = params.get("EncryptErrno")
        self._EncryptErrDesc = params.get("EncryptErrDesc")
        self._CreatTime = params.get("CreatTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CostTime = params.get("CostTime")
        self._EncryptPkgUrl = params.get("EncryptPkgUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OptPluginListItem(AbstractModel):
    """APK检测服务：非广告插件结果列表(SDK、风险插件等)

    """

    def __init__(self):
        r"""
        :param _PluginType: 非广告类型
        :type PluginType: str
        :param _PluginName: 非广告插件名称
        :type PluginName: str
        :param _PluginDesc: 非广告插件描述
        :type PluginDesc: str
        """
        self._PluginType = None
        self._PluginName = None
        self._PluginDesc = None

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginDesc(self):
        return self._PluginDesc

    @PluginDesc.setter
    def PluginDesc(self, PluginDesc):
        self._PluginDesc = PluginDesc


    def _deserialize(self, params):
        self._PluginType = params.get("PluginType")
        self._PluginName = params.get("PluginName")
        self._PluginDesc = params.get("PluginDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Orders(AbstractModel):
    """渠道合作加固订单资源信息

    """

    def __init__(self):
        r"""
        :param _OrderId: 订单号
        :type OrderId: str
        :param _PlatformType: 平台类型整型值 
        :type PlatformType: int
        :param _PlatformTypeDesc: 平台类型描述：  1.android加固   2.ios源码混淆  3.sdk加固  4.applet小程序加固
        :type PlatformTypeDesc: str
        :param _OrderType: 订单采购类型整型值
        :type OrderType: int
        :param _OrderTypeDesc: 订单采购类型描述： 1-免费试用 2-按年收费 3-按次收费
        :type OrderTypeDesc: str
        :param _AppPkgName: android包年收费加固的包名
        :type AppPkgName: str
        :param _ResourceId: 资源号
        :type ResourceId: str
        :param _ResourceStatus: 资源状态整型值
        :type ResourceStatus: int
        :param _ResourceStatusDesc: 资源状态描述
0-未生效、1-生效中、2-已失效。
        :type ResourceStatusDesc: str
        :param _TestTimes: 订单类型为免费试用时的免费加固次数。
        :type TestTimes: int
        :param _ValidTime: 资源生效时间
        :type ValidTime: str
        :param _ExpireTime: 资源过期时间
        :type ExpireTime: str
        :param _CreateTime: 资源创建时间
        :type CreateTime: str
        :param _Approver: 订单审批人
        :type Approver: str
        :param _ApprovalStatus: 订单审批状态整型值
        :type ApprovalStatus: int
        :param _ApprovalStatusDesc: 订单审批状态整型值描述：0-未审批、1-审批通过、2-驳回。
        :type ApprovalStatusDesc: str
        :param _ApprovalTime: 订单审批时间
        :type ApprovalTime: str
        :param _TimesTaskTotalCount: 按次收费加固资源，其关联的总任务数
        :type TimesTaskTotalCount: int
        :param _TimesTaskSuccessCount: 按次收费加固资源，其关联的任务成功数
        :type TimesTaskSuccessCount: int
        :param _TimesTaskFailCount: 按次收费加固资源，其关联的任务失败数
        :type TimesTaskFailCount: int
        """
        self._OrderId = None
        self._PlatformType = None
        self._PlatformTypeDesc = None
        self._OrderType = None
        self._OrderTypeDesc = None
        self._AppPkgName = None
        self._ResourceId = None
        self._ResourceStatus = None
        self._ResourceStatusDesc = None
        self._TestTimes = None
        self._ValidTime = None
        self._ExpireTime = None
        self._CreateTime = None
        self._Approver = None
        self._ApprovalStatus = None
        self._ApprovalStatusDesc = None
        self._ApprovalTime = None
        self._TimesTaskTotalCount = None
        self._TimesTaskSuccessCount = None
        self._TimesTaskFailCount = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def PlatformType(self):
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def PlatformTypeDesc(self):
        return self._PlatformTypeDesc

    @PlatformTypeDesc.setter
    def PlatformTypeDesc(self, PlatformTypeDesc):
        self._PlatformTypeDesc = PlatformTypeDesc

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def OrderTypeDesc(self):
        return self._OrderTypeDesc

    @OrderTypeDesc.setter
    def OrderTypeDesc(self, OrderTypeDesc):
        self._OrderTypeDesc = OrderTypeDesc

    @property
    def AppPkgName(self):
        return self._AppPkgName

    @AppPkgName.setter
    def AppPkgName(self, AppPkgName):
        self._AppPkgName = AppPkgName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceStatus(self):
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceStatusDesc(self):
        return self._ResourceStatusDesc

    @ResourceStatusDesc.setter
    def ResourceStatusDesc(self, ResourceStatusDesc):
        self._ResourceStatusDesc = ResourceStatusDesc

    @property
    def TestTimes(self):
        return self._TestTimes

    @TestTimes.setter
    def TestTimes(self, TestTimes):
        self._TestTimes = TestTimes

    @property
    def ValidTime(self):
        return self._ValidTime

    @ValidTime.setter
    def ValidTime(self, ValidTime):
        self._ValidTime = ValidTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Approver(self):
        return self._Approver

    @Approver.setter
    def Approver(self, Approver):
        self._Approver = Approver

    @property
    def ApprovalStatus(self):
        return self._ApprovalStatus

    @ApprovalStatus.setter
    def ApprovalStatus(self, ApprovalStatus):
        self._ApprovalStatus = ApprovalStatus

    @property
    def ApprovalStatusDesc(self):
        return self._ApprovalStatusDesc

    @ApprovalStatusDesc.setter
    def ApprovalStatusDesc(self, ApprovalStatusDesc):
        self._ApprovalStatusDesc = ApprovalStatusDesc

    @property
    def ApprovalTime(self):
        return self._ApprovalTime

    @ApprovalTime.setter
    def ApprovalTime(self, ApprovalTime):
        self._ApprovalTime = ApprovalTime

    @property
    def TimesTaskTotalCount(self):
        return self._TimesTaskTotalCount

    @TimesTaskTotalCount.setter
    def TimesTaskTotalCount(self, TimesTaskTotalCount):
        self._TimesTaskTotalCount = TimesTaskTotalCount

    @property
    def TimesTaskSuccessCount(self):
        return self._TimesTaskSuccessCount

    @TimesTaskSuccessCount.setter
    def TimesTaskSuccessCount(self, TimesTaskSuccessCount):
        self._TimesTaskSuccessCount = TimesTaskSuccessCount

    @property
    def TimesTaskFailCount(self):
        return self._TimesTaskFailCount

    @TimesTaskFailCount.setter
    def TimesTaskFailCount(self, TimesTaskFailCount):
        self._TimesTaskFailCount = TimesTaskFailCount


    def _deserialize(self, params):
        self._OrderId = params.get("OrderId")
        self._PlatformType = params.get("PlatformType")
        self._PlatformTypeDesc = params.get("PlatformTypeDesc")
        self._OrderType = params.get("OrderType")
        self._OrderTypeDesc = params.get("OrderTypeDesc")
        self._AppPkgName = params.get("AppPkgName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceStatus = params.get("ResourceStatus")
        self._ResourceStatusDesc = params.get("ResourceStatusDesc")
        self._TestTimes = params.get("TestTimes")
        self._ValidTime = params.get("ValidTime")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._Approver = params.get("Approver")
        self._ApprovalStatus = params.get("ApprovalStatus")
        self._ApprovalStatusDesc = params.get("ApprovalStatusDesc")
        self._ApprovalTime = params.get("ApprovalTime")
        self._TimesTaskTotalCount = params.get("TimesTaskTotalCount")
        self._TimesTaskSuccessCount = params.get("TimesTaskSuccessCount")
        self._TimesTaskFailCount = params.get("TimesTaskFailCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanDetailInfo(AbstractModel):
    """加固策略具体信息

    """

    def __init__(self):
        r"""
        :param _IsDefault: 默认策略，1为默认，0为非默认
        :type IsDefault: int
        :param _PlanId: 策略id
        :type PlanId: int
        :param _PlanName: 策略名称
        :type PlanName: str
        :param _PlanInfo: 策略信息
        :type PlanInfo: :class:`tencentcloud.ms.v20180408.models.PlanInfo`
        """
        self._IsDefault = None
        self._PlanId = None
        self._PlanName = None
        self._PlanInfo = None

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def PlanInfo(self):
        return self._PlanInfo

    @PlanInfo.setter
    def PlanInfo(self, PlanInfo):
        self._PlanInfo = PlanInfo


    def _deserialize(self, params):
        self._IsDefault = params.get("IsDefault")
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        if params.get("PlanInfo") is not None:
            self._PlanInfo = PlanInfo()
            self._PlanInfo._deserialize(params.get("PlanInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanInfo(AbstractModel):
    """加固策略信息

    """

    def __init__(self):
        r"""
        :param _ApkSizeOpt: apk大小优化，0关闭，1开启
        :type ApkSizeOpt: int
        :param _Dex: Dex加固，0关闭，1开启
        :type Dex: int
        :param _So: So加固，0关闭，1开启
        :type So: int
        :param _Bugly: 数据收集，0关闭，1开启
        :type Bugly: int
        :param _AntiRepack: 防止重打包，0关闭，1开启
        :type AntiRepack: int
        :param _SeperateDex: Dex分离，0关闭，1开启
        :type SeperateDex: int
        :param _Db: 内存保护，0关闭，1开启
        :type Db: int
        :param _DexSig: Dex签名校验，0关闭，1开启
        :type DexSig: int
        :param _SoInfo: So文件信息
        :type SoInfo: :class:`tencentcloud.ms.v20180408.models.SoInfo`
        :param _AntiVMP: vmp，0关闭，1开启
        :type AntiVMP: int
        :param _SoType: 保护so的强度，
        :type SoType: list of str
        :param _AntiLogLeak: 防日志泄漏，0关闭，1开启
        :type AntiLogLeak: int
        :param _AntiQemuRoot: root检测，0关闭，1开启
        :type AntiQemuRoot: int
        :param _AntiAssets: 资源防篡改，0关闭，1开启
        :type AntiAssets: int
        :param _AntiScreenshot: 防止截屏，0关闭，1开启
        :type AntiScreenshot: int
        :param _AntiSSL: SSL证书防窃取，0关闭，1开启
        :type AntiSSL: int
        """
        self._ApkSizeOpt = None
        self._Dex = None
        self._So = None
        self._Bugly = None
        self._AntiRepack = None
        self._SeperateDex = None
        self._Db = None
        self._DexSig = None
        self._SoInfo = None
        self._AntiVMP = None
        self._SoType = None
        self._AntiLogLeak = None
        self._AntiQemuRoot = None
        self._AntiAssets = None
        self._AntiScreenshot = None
        self._AntiSSL = None

    @property
    def ApkSizeOpt(self):
        return self._ApkSizeOpt

    @ApkSizeOpt.setter
    def ApkSizeOpt(self, ApkSizeOpt):
        self._ApkSizeOpt = ApkSizeOpt

    @property
    def Dex(self):
        return self._Dex

    @Dex.setter
    def Dex(self, Dex):
        self._Dex = Dex

    @property
    def So(self):
        return self._So

    @So.setter
    def So(self, So):
        self._So = So

    @property
    def Bugly(self):
        return self._Bugly

    @Bugly.setter
    def Bugly(self, Bugly):
        self._Bugly = Bugly

    @property
    def AntiRepack(self):
        return self._AntiRepack

    @AntiRepack.setter
    def AntiRepack(self, AntiRepack):
        self._AntiRepack = AntiRepack

    @property
    def SeperateDex(self):
        return self._SeperateDex

    @SeperateDex.setter
    def SeperateDex(self, SeperateDex):
        self._SeperateDex = SeperateDex

    @property
    def Db(self):
        return self._Db

    @Db.setter
    def Db(self, Db):
        self._Db = Db

    @property
    def DexSig(self):
        return self._DexSig

    @DexSig.setter
    def DexSig(self, DexSig):
        self._DexSig = DexSig

    @property
    def SoInfo(self):
        return self._SoInfo

    @SoInfo.setter
    def SoInfo(self, SoInfo):
        self._SoInfo = SoInfo

    @property
    def AntiVMP(self):
        return self._AntiVMP

    @AntiVMP.setter
    def AntiVMP(self, AntiVMP):
        self._AntiVMP = AntiVMP

    @property
    def SoType(self):
        return self._SoType

    @SoType.setter
    def SoType(self, SoType):
        self._SoType = SoType

    @property
    def AntiLogLeak(self):
        return self._AntiLogLeak

    @AntiLogLeak.setter
    def AntiLogLeak(self, AntiLogLeak):
        self._AntiLogLeak = AntiLogLeak

    @property
    def AntiQemuRoot(self):
        return self._AntiQemuRoot

    @AntiQemuRoot.setter
    def AntiQemuRoot(self, AntiQemuRoot):
        self._AntiQemuRoot = AntiQemuRoot

    @property
    def AntiAssets(self):
        return self._AntiAssets

    @AntiAssets.setter
    def AntiAssets(self, AntiAssets):
        self._AntiAssets = AntiAssets

    @property
    def AntiScreenshot(self):
        return self._AntiScreenshot

    @AntiScreenshot.setter
    def AntiScreenshot(self, AntiScreenshot):
        self._AntiScreenshot = AntiScreenshot

    @property
    def AntiSSL(self):
        return self._AntiSSL

    @AntiSSL.setter
    def AntiSSL(self, AntiSSL):
        self._AntiSSL = AntiSSL


    def _deserialize(self, params):
        self._ApkSizeOpt = params.get("ApkSizeOpt")
        self._Dex = params.get("Dex")
        self._So = params.get("So")
        self._Bugly = params.get("Bugly")
        self._AntiRepack = params.get("AntiRepack")
        self._SeperateDex = params.get("SeperateDex")
        self._Db = params.get("Db")
        self._DexSig = params.get("DexSig")
        if params.get("SoInfo") is not None:
            self._SoInfo = SoInfo()
            self._SoInfo._deserialize(params.get("SoInfo"))
        self._AntiVMP = params.get("AntiVMP")
        self._SoType = params.get("SoType")
        self._AntiLogLeak = params.get("AntiLogLeak")
        self._AntiQemuRoot = params.get("AntiQemuRoot")
        self._AntiAssets = params.get("AntiAssets")
        self._AntiScreenshot = params.get("AntiScreenshot")
        self._AntiSSL = params.get("AntiSSL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginListItem(AbstractModel):
    """APK检测服务：广告插件结果结构体

    """

    def __init__(self):
        r"""
        :param _PluginType: 数字类型，分别为 1-通知栏广告，2-积分墙广告，3-banner广告，4- 悬浮窗图标广告，5-精品推荐列表广告, 6-插播广告
        :type PluginType: str
        :param _PluginName: 广告插件名称
        :type PluginName: str
        :param _PluginDesc: 广告插件描述
        :type PluginDesc: str
        """
        self._PluginType = None
        self._PluginName = None
        self._PluginDesc = None

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginDesc(self):
        return self._PluginDesc

    @PluginDesc.setter
    def PluginDesc(self, PluginDesc):
        self._PluginDesc = PluginDesc


    def _deserialize(self, params):
        self._PluginType = params.get("PluginType")
        self._PluginName = params.get("PluginName")
        self._PluginDesc = params.get("PluginDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestLocalTaskRequest(AbstractModel):
    """RequestLocalTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientId: Client Id
        :type ClientId: str
        """
        self._ClientId = None

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestLocalTaskResponse(AbstractModel):
    """RequestLocalTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Sid: 返回的任务id
        :type Sid: str
        :param _SrcFileMd5: 任务文件的mk5
        :type SrcFileMd5: str
        :param _SrcFileSize: 文件大小，可不传
        :type SrcFileSize: int
        :param _SrcFileUrl: 任务文件的下载地址，必须无鉴权可下载
        :type SrcFileUrl: str
        :param _SrcFileType: release: 需要INFO-PLIST文件，会生成工具部署安装包，并带有license文件，绑定机器；nobind不需要INFO-PLIST文件，不绑定机器
        :type SrcFileType: str
        :param _SrcFileVersion: enterprise
trial
        :type SrcFileVersion: str
        :param _EncryptParam: 补充字段
        :type EncryptParam: str
        :param _EncryptState: 任务状态
        :type EncryptState: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Sid = None
        self._SrcFileMd5 = None
        self._SrcFileSize = None
        self._SrcFileUrl = None
        self._SrcFileType = None
        self._SrcFileVersion = None
        self._EncryptParam = None
        self._EncryptState = None
        self._RequestId = None

    @property
    def Sid(self):
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def SrcFileMd5(self):
        return self._SrcFileMd5

    @SrcFileMd5.setter
    def SrcFileMd5(self, SrcFileMd5):
        self._SrcFileMd5 = SrcFileMd5

    @property
    def SrcFileSize(self):
        return self._SrcFileSize

    @SrcFileSize.setter
    def SrcFileSize(self, SrcFileSize):
        self._SrcFileSize = SrcFileSize

    @property
    def SrcFileUrl(self):
        return self._SrcFileUrl

    @SrcFileUrl.setter
    def SrcFileUrl(self, SrcFileUrl):
        self._SrcFileUrl = SrcFileUrl

    @property
    def SrcFileType(self):
        return self._SrcFileType

    @SrcFileType.setter
    def SrcFileType(self, SrcFileType):
        self._SrcFileType = SrcFileType

    @property
    def SrcFileVersion(self):
        return self._SrcFileVersion

    @SrcFileVersion.setter
    def SrcFileVersion(self, SrcFileVersion):
        self._SrcFileVersion = SrcFileVersion

    @property
    def EncryptParam(self):
        return self._EncryptParam

    @EncryptParam.setter
    def EncryptParam(self, EncryptParam):
        self._EncryptParam = EncryptParam

    @property
    def EncryptState(self):
        return self._EncryptState

    @EncryptState.setter
    def EncryptState(self, EncryptState):
        self._EncryptState = EncryptState

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._SrcFileMd5 = params.get("SrcFileMd5")
        self._SrcFileSize = params.get("SrcFileSize")
        self._SrcFileUrl = params.get("SrcFileUrl")
        self._SrcFileType = params.get("SrcFileType")
        self._SrcFileVersion = params.get("SrcFileVersion")
        self._EncryptParam = params.get("EncryptParam")
        self._EncryptState = params.get("EncryptState")
        self._RequestId = params.get("RequestId")


class ResourceInfo(AbstractModel):
    """拉取某个用户的所有资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 用户购买的资源id，全局唯一
        :type ResourceId: str
        :param _Pid: 资源的pid，MTP加固-12767，应用加固-12750 MTP反作弊-12766 源代码混淆-12736
        :type Pid: int
        :param _CreateTime: 购买时间戳
        :type CreateTime: int
        :param _ExpireTime: 到期时间戳
        :type ExpireTime: int
        :param _IsBind: 0-未绑定，1-已绑定
        :type IsBind: int
        :param _BindInfo: 用户绑定app的基本信息
        :type BindInfo: :class:`tencentcloud.ms.v20180408.models.BindInfo`
        :param _ResourceName: 资源名称，如应用加固，漏洞扫描
        :type ResourceName: str
        """
        self._ResourceId = None
        self._Pid = None
        self._CreateTime = None
        self._ExpireTime = None
        self._IsBind = None
        self._BindInfo = None
        self._ResourceName = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsBind(self):
        return self._IsBind

    @IsBind.setter
    def IsBind(self, IsBind):
        self._IsBind = IsBind

    @property
    def BindInfo(self):
        return self._BindInfo

    @BindInfo.setter
    def BindInfo(self, BindInfo):
        self._BindInfo = BindInfo

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Pid = params.get("Pid")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._IsBind = params.get("IsBind")
        if params.get("BindInfo") is not None:
            self._BindInfo = BindInfo()
            self._BindInfo._deserialize(params.get("BindInfo"))
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceServiceInfo(AbstractModel):
    """资源服务信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间戳
        :type CreateTime: int
        :param _ExpireTime: 到期时间戳
        :type ExpireTime: int
        :param _ResourceName: 资源名称，如应用加固，源码混淆
        :type ResourceName: str
        """
        self._CreateTime = None
        self._ExpireTime = None
        self._ResourceName = None

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResultListItem(AbstractModel):
    """APK检测服务参数返回具体信息

    """

    def __init__(self):
        r"""
        :param _Banner: banner广告软件标记，分别为-1-不确定，0-否，1-是
        :type Banner: str
        :param _BoutiqueRecommand: 精品推荐列表广告标记，分别为-1-不确定，0-否，1-是
        :type BoutiqueRecommand: str
        :param _FloatWindows: 悬浮窗图标广告标记,分别为-1-不确定，0-否，1-是
        :type FloatWindows: str
        :param _IntegralWall: 积分墙广告软件标记，分别为 -1 -不确定，0-否，1-是
        :type IntegralWall: str
        :param _Md5: 安装包的md5
        :type Md5: str
        :param _NotifyBar: 通知栏广告软件标记，分别为-1-不确定，0-否，1-是
        :type NotifyBar: str
        :param _Official: 1表示官方，0表示非官方
        :type Official: str
        :param _PluginList: 广告插件结果列表
        :type PluginList: list of PluginListItem
        :param _OptPluginList: 非广告插件结果列表(SDK、风险插件等)
        :type OptPluginList: list of OptPluginListItem
        :param _SafeType: 数字类型，分别为0-未知， 1-安全软件，2-风险软件，3-病毒软件
        :type SafeType: str
        :param _Sid: Session id，合作方可以用来区分回调数据，需要唯一。
        :type Sid: str
        :param _SoftName: 安装包名称
        :type SoftName: str
        :param _Spot: 插播广告软件标记，取值：-1 不确定，0否， 1 是
        :type Spot: str
        :param _VirusName: 病毒名称，utf8编码
        :type VirusName: str
        :param _VirusDesc: 病毒描述，utf8编码
        :type VirusDesc: str
        :param _RepackageStatus: 二次打包状态：0-表示默认；1-表示二次
        :type RepackageStatus: str
        :param _Errno: 应用错误码：0、1-表示正常；                  

2表示System Error(engine analysis error).

3表示App analysis error, please confirm it.

4表示App have not cert, please confirm it.

5表示App size is zero, please confirm it.

6表示App have not package name, please confirm it.

7表示App build time is empty, please confirm it.

8表示App have not valid cert, please confirm it.

99表示Other error.

1000表示App downloadlink download fail, please confirm it.

1001表示APP md5 different between real md5, please confirm it.

1002表示App md5 uncollect, please offer downloadlink.
        :type Errno: str
        :param _ErrMsg: 对应errno的错误信息描述
        :type ErrMsg: str
        """
        self._Banner = None
        self._BoutiqueRecommand = None
        self._FloatWindows = None
        self._IntegralWall = None
        self._Md5 = None
        self._NotifyBar = None
        self._Official = None
        self._PluginList = None
        self._OptPluginList = None
        self._SafeType = None
        self._Sid = None
        self._SoftName = None
        self._Spot = None
        self._VirusName = None
        self._VirusDesc = None
        self._RepackageStatus = None
        self._Errno = None
        self._ErrMsg = None

    @property
    def Banner(self):
        return self._Banner

    @Banner.setter
    def Banner(self, Banner):
        self._Banner = Banner

    @property
    def BoutiqueRecommand(self):
        return self._BoutiqueRecommand

    @BoutiqueRecommand.setter
    def BoutiqueRecommand(self, BoutiqueRecommand):
        self._BoutiqueRecommand = BoutiqueRecommand

    @property
    def FloatWindows(self):
        return self._FloatWindows

    @FloatWindows.setter
    def FloatWindows(self, FloatWindows):
        self._FloatWindows = FloatWindows

    @property
    def IntegralWall(self):
        return self._IntegralWall

    @IntegralWall.setter
    def IntegralWall(self, IntegralWall):
        self._IntegralWall = IntegralWall

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def NotifyBar(self):
        return self._NotifyBar

    @NotifyBar.setter
    def NotifyBar(self, NotifyBar):
        self._NotifyBar = NotifyBar

    @property
    def Official(self):
        return self._Official

    @Official.setter
    def Official(self, Official):
        self._Official = Official

    @property
    def PluginList(self):
        return self._PluginList

    @PluginList.setter
    def PluginList(self, PluginList):
        self._PluginList = PluginList

    @property
    def OptPluginList(self):
        return self._OptPluginList

    @OptPluginList.setter
    def OptPluginList(self, OptPluginList):
        self._OptPluginList = OptPluginList

    @property
    def SafeType(self):
        return self._SafeType

    @SafeType.setter
    def SafeType(self, SafeType):
        self._SafeType = SafeType

    @property
    def Sid(self):
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def SoftName(self):
        return self._SoftName

    @SoftName.setter
    def SoftName(self, SoftName):
        self._SoftName = SoftName

    @property
    def Spot(self):
        return self._Spot

    @Spot.setter
    def Spot(self, Spot):
        self._Spot = Spot

    @property
    def VirusName(self):
        return self._VirusName

    @VirusName.setter
    def VirusName(self, VirusName):
        self._VirusName = VirusName

    @property
    def VirusDesc(self):
        return self._VirusDesc

    @VirusDesc.setter
    def VirusDesc(self, VirusDesc):
        self._VirusDesc = VirusDesc

    @property
    def RepackageStatus(self):
        return self._RepackageStatus

    @RepackageStatus.setter
    def RepackageStatus(self, RepackageStatus):
        self._RepackageStatus = RepackageStatus

    @property
    def Errno(self):
        return self._Errno

    @Errno.setter
    def Errno(self, Errno):
        self._Errno = Errno

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._Banner = params.get("Banner")
        self._BoutiqueRecommand = params.get("BoutiqueRecommand")
        self._FloatWindows = params.get("FloatWindows")
        self._IntegralWall = params.get("IntegralWall")
        self._Md5 = params.get("Md5")
        self._NotifyBar = params.get("NotifyBar")
        self._Official = params.get("Official")
        if params.get("PluginList") is not None:
            self._PluginList = []
            for item in params.get("PluginList"):
                obj = PluginListItem()
                obj._deserialize(item)
                self._PluginList.append(obj)
        if params.get("OptPluginList") is not None:
            self._OptPluginList = []
            for item in params.get("OptPluginList"):
                obj = OptPluginListItem()
                obj._deserialize(item)
                self._OptPluginList.append(obj)
        self._SafeType = params.get("SafeType")
        self._Sid = params.get("Sid")
        self._SoftName = params.get("SoftName")
        self._Spot = params.get("Spot")
        self._VirusName = params.get("VirusName")
        self._VirusDesc = params.get("VirusDesc")
        self._RepackageStatus = params.get("RepackageStatus")
        self._Errno = params.get("Errno")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SDKPlan(AbstractModel):
    """渠道合作sdk加固策略配置

    """

    def __init__(self):
        r"""
        :param _PlanId: 策略id
        :type PlanId: int
        """
        self._PlanId = None

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SDKResult(AbstractModel):
    """渠道合作加固sdk加固结果

    """

    def __init__(self):
        r"""
        :param _ResultId: 加固任务结果Id
        :type ResultId: str
        """
        self._ResultId = None

    @property
    def ResultId(self):
        return self._ResultId

    @ResultId.setter
    def ResultId(self, ResultId):
        self._ResultId = ResultId


    def _deserialize(self, params):
        self._ResultId = params.get("ResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    """提交app加固的服务信息

    """

    def __init__(self):
        r"""
        :param _ServiceEdition: 服务版本，基础版basic，专业版professional，企业版enterprise。
        :type ServiceEdition: str
        :param _CallbackUrl: 任务处理完成后的反向通知回调地址，如果不需要通知请传递空字符串。通知为POST请求，post包体数据示例{"Response":{"ItemId":"4cdad8fb86f036b06bccb3f58971c306","ShieldCode":0,"ShieldMd5":"78701576793c4a5f04e1c9660de0aa0b","ShieldSize":11997354,"TaskStatus":1,"TaskTime":1539148141}}，调用方需要返回如下信息，{"Result":"ok","Reason":"xxxxx"}，如果Result字段值不等于ok会继续回调。
        :type CallbackUrl: str
        :param _SubmitSource: 提交来源 YYB-应用宝 RDM-rdm MC-控制台 MAC_TOOL-mac工具 WIN_TOOL-window工具。
        :type SubmitSource: str
        :param _PlanId: 加固策略编号，如果不传则使用系统默认加固策略。如果指定的plan不存在会返回错误。
        :type PlanId: int
        """
        self._ServiceEdition = None
        self._CallbackUrl = None
        self._SubmitSource = None
        self._PlanId = None

    @property
    def ServiceEdition(self):
        return self._ServiceEdition

    @ServiceEdition.setter
    def ServiceEdition(self, ServiceEdition):
        self._ServiceEdition = ServiceEdition

    @property
    def CallbackUrl(self):
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SubmitSource(self):
        return self._SubmitSource

    @SubmitSource.setter
    def SubmitSource(self, SubmitSource):
        self._SubmitSource = SubmitSource

    @property
    def PlanId(self):
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._ServiceEdition = params.get("ServiceEdition")
        self._CallbackUrl = params.get("CallbackUrl")
        self._SubmitSource = params.get("SubmitSource")
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShieldInfo(AbstractModel):
    """加固后app的信息

    """

    def __init__(self):
        r"""
        :param _ShieldCode: 加固结果的返回码
        :type ShieldCode: int
        :param _ShieldSize: 加固后app的大小
        :type ShieldSize: int
        :param _ShieldMd5: 加固后app的md5
        :type ShieldMd5: str
        :param _AppUrl: 加固后的APP下载地址，该地址有效期为20分钟，请及时下载
        :type AppUrl: str
        :param _TaskTime: 加固的提交时间
        :type TaskTime: int
        :param _ItemId: 任务唯一标识
        :type ItemId: str
        :param _ServiceEdition: 加固版本，basic基础版，professional专业版，enterprise企业版
        :type ServiceEdition: str
        """
        self._ShieldCode = None
        self._ShieldSize = None
        self._ShieldMd5 = None
        self._AppUrl = None
        self._TaskTime = None
        self._ItemId = None
        self._ServiceEdition = None

    @property
    def ShieldCode(self):
        return self._ShieldCode

    @ShieldCode.setter
    def ShieldCode(self, ShieldCode):
        self._ShieldCode = ShieldCode

    @property
    def ShieldSize(self):
        return self._ShieldSize

    @ShieldSize.setter
    def ShieldSize(self, ShieldSize):
        self._ShieldSize = ShieldSize

    @property
    def ShieldMd5(self):
        return self._ShieldMd5

    @ShieldMd5.setter
    def ShieldMd5(self, ShieldMd5):
        self._ShieldMd5 = ShieldMd5

    @property
    def AppUrl(self):
        return self._AppUrl

    @AppUrl.setter
    def AppUrl(self, AppUrl):
        self._AppUrl = AppUrl

    @property
    def TaskTime(self):
        return self._TaskTime

    @TaskTime.setter
    def TaskTime(self, TaskTime):
        self._TaskTime = TaskTime

    @property
    def ItemId(self):
        return self._ItemId

    @ItemId.setter
    def ItemId(self, ItemId):
        self._ItemId = ItemId

    @property
    def ServiceEdition(self):
        return self._ServiceEdition

    @ServiceEdition.setter
    def ServiceEdition(self, ServiceEdition):
        self._ServiceEdition = ServiceEdition


    def _deserialize(self, params):
        self._ShieldCode = params.get("ShieldCode")
        self._ShieldSize = params.get("ShieldSize")
        self._ShieldMd5 = params.get("ShieldMd5")
        self._AppUrl = params.get("AppUrl")
        self._TaskTime = params.get("TaskTime")
        self._ItemId = params.get("ItemId")
        self._ServiceEdition = params.get("ServiceEdition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShieldPlanInfo(AbstractModel):
    """加固策略信息

    """

    def __init__(self):
        r"""
        :param _TotalCount: 加固策略数量
        :type TotalCount: int
        :param _PlanSet: 加固策略具体信息数组
        :type PlanSet: list of PlanDetailInfo
        """
        self._TotalCount = None
        self._PlanSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PlanSet(self):
        return self._PlanSet

    @PlanSet.setter
    def PlanSet(self, PlanSet):
        self._PlanSet = PlanSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PlanSet") is not None:
            self._PlanSet = []
            for item in params.get("PlanSet"):
                obj = PlanDetailInfo()
                obj._deserialize(item)
                self._PlanSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SoInfo(AbstractModel):
    """so加固信息

    """

    def __init__(self):
        r"""
        :param _SoFileNames: so文件列表
        :type SoFileNames: list of str
        """
        self._SoFileNames = None

    @property
    def SoFileNames(self):
        return self._SoFileNames

    @SoFileNames.setter
    def SoFileNames(self, SoFileNames):
        self._SoFileNames = SoFileNames


    def _deserialize(self, params):
        self._SoFileNames = params.get("SoFileNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClientStateRequest(AbstractModel):
    """UpdateClientState请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClientId: Client Id
        :type ClientId: str
        :param _Ip: Ip addr
        :type Ip: str
        :param _Internal: 内部分组
        :type Internal: int
        :param _ServerVersion: Client  Version
        :type ServerVersion: str
        :param _Hostname: 主机
        :type Hostname: str
        :param _Os: 系统
        :type Os: str
        """
        self._ClientId = None
        self._Ip = None
        self._Internal = None
        self._ServerVersion = None
        self._Hostname = None
        self._Os = None

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Internal(self):
        return self._Internal

    @Internal.setter
    def Internal(self, Internal):
        self._Internal = Internal

    @property
    def ServerVersion(self):
        return self._ServerVersion

    @ServerVersion.setter
    def ServerVersion(self, ServerVersion):
        self._ServerVersion = ServerVersion

    @property
    def Hostname(self):
        return self._Hostname

    @Hostname.setter
    def Hostname(self, Hostname):
        self._Hostname = Hostname

    @property
    def Os(self):
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._Ip = params.get("Ip")
        self._Internal = params.get("Internal")
        self._ServerVersion = params.get("ServerVersion")
        self._Hostname = params.get("Hostname")
        self._Os = params.get("Os")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClientStateResponse(AbstractModel):
    """UpdateClientState返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: 返回值
        :type ResultCode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._RequestId = params.get("RequestId")


class UpdateLocalTaskResultRequest(AbstractModel):
    """UpdateLocalTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sid: 任务id
        :type Sid: str
        :param _ResultCode: 一级任务code。标记任务状态
        :type ResultCode: int
        :param _SubCode: 二级错误码
        :type SubCode: int
        :param _ErrMsg: 二级错误信息
        :type ErrMsg: str
        :param _Result: 结果
        :type Result: str
        """
        self._Sid = None
        self._ResultCode = None
        self._SubCode = None
        self._ErrMsg = None
        self._Result = None

    @property
    def Sid(self):
        return self._Sid

    @Sid.setter
    def Sid(self, Sid):
        self._Sid = Sid

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def SubCode(self):
        return self._SubCode

    @SubCode.setter
    def SubCode(self, SubCode):
        self._SubCode = SubCode

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._Sid = params.get("Sid")
        self._ResultCode = params.get("ResultCode")
        self._SubCode = params.get("SubCode")
        self._ErrMsg = params.get("ErrMsg")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateLocalTaskResultResponse(AbstractModel):
    """UpdateLocalTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultCode: 标记成功
        :type ResultCode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultCode = None
        self._RequestId = None

    @property
    def ResultCode(self):
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultCode = params.get("ResultCode")
        self._RequestId = params.get("RequestId")