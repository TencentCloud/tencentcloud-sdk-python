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


class DescribeDomainInfoRequest(AbstractModel):
    """DescribeDomainInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 要查询的域名
        :type Key: str
        :param _Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self._Key = None
        self._Option = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainInfoResponse(AbstractModel):
    """DescribeDomainInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param _Result: 判定结果，如：black、white、grey
        :type Result: str
        :param _Confidence: 置信度，取值0-100
        :type Confidence: int
        :param _ThreatTypes: 威胁类型。
botnet = 僵尸网络
trojan = 木马
ransomware = 勒索软件
worm = 蠕虫
dga = 域名生成算法
c2 = c&c
compromised = 失陷主机
dynamicIP = 动态IP
proxy = 代理
idc = idc 机房
whitelist = 白名单
tor = 暗网
miner = 挖矿
maleware site = 恶意站点
malware IP = 恶意IP
等等
        :type ThreatTypes: list of str
        :param _Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of TagType
        :param _Intelligences: 对应的历史上的威胁情报事件
        :type Intelligences: list of IntelligenceType
        :param _Context: 情报相关的上下文
        :type Context: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._Result = None
        self._Confidence = None
        self._ThreatTypes = None
        self._Tags = None
        self._Intelligences = None
        self._Context = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def ThreatTypes(self):
        return self._ThreatTypes

    @ThreatTypes.setter
    def ThreatTypes(self, ThreatTypes):
        self._ThreatTypes = ThreatTypes

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Intelligences(self):
        return self._Intelligences

    @Intelligences.setter
    def Intelligences(self, Intelligences):
        self._Intelligences = Intelligences

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._Result = params.get("Result")
        self._Confidence = params.get("Confidence")
        self._ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Intelligences") is not None:
            self._Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self._Intelligences.append(obj)
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeFileInfoRequest(AbstractModel):
    """DescribeFileInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 要查询文件的MD5
        :type Key: str
        :param _Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self._Key = None
        self._Option = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileInfoResponse(AbstractModel):
    """DescribeFileInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param _Result: 判定结果，如：black、white、grey
        :type Result: str
        :param _Confidence: 置信度，取值0-100
        :type Confidence: int
        :param _FileInfo: 文件类型，文件hash
（md5,sha1,sha256）,文件大小等等文件
基础信息
        :type FileInfo: list of FileInfoType
        :param _Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of TagType
        :param _Intelligences: 对应的历史上的威胁情报事件
        :type Intelligences: list of IntelligenceType
        :param _Context: 情报相关的上下文
        :type Context: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._Result = None
        self._Confidence = None
        self._FileInfo = None
        self._Tags = None
        self._Intelligences = None
        self._Context = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def FileInfo(self):
        return self._FileInfo

    @FileInfo.setter
    def FileInfo(self, FileInfo):
        self._FileInfo = FileInfo

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Intelligences(self):
        return self._Intelligences

    @Intelligences.setter
    def Intelligences(self, Intelligences):
        self._Intelligences = Intelligences

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._Result = params.get("Result")
        self._Confidence = params.get("Confidence")
        if params.get("FileInfo") is not None:
            self._FileInfo = []
            for item in params.get("FileInfo"):
                obj = FileInfoType()
                obj._deserialize(item)
                self._FileInfo.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Intelligences") is not None:
            self._Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self._Intelligences.append(obj)
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeIpInfoRequest(AbstractModel):
    """DescribeIpInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 要查询的IP
        :type Key: str
        :param _Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self._Key = None
        self._Option = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpInfoResponse(AbstractModel):
    """DescribeIpInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param _Result: 判定结果，如：black、white、grey
        :type Result: str
        :param _Confidence: 置信度，取值0-100
        :type Confidence: int
        :param _ThreatTypes: 威胁类型。
botnet = 僵尸网络
trojan = 木马
ransomware = 勒索软件
worm = 蠕虫
dga = 域名生成算法
c2 = c&c
compromised = 失陷主机
dynamicIP = 动态IP
proxy = 代理
idc = idc 机房
whitelist = 白名单
tor = 暗网
miner = 挖矿
maleware site = 恶意站点
malware IP = 恶意IP
等等
        :type ThreatTypes: list of str
        :param _Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of TagType
        :param _Intelligences: 对应的历史上的威胁情报事件
        :type Intelligences: list of IntelligenceType
        :param _Context: 情报相关的上下文
        :type Context: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._Result = None
        self._Confidence = None
        self._ThreatTypes = None
        self._Tags = None
        self._Intelligences = None
        self._Context = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def ThreatTypes(self):
        return self._ThreatTypes

    @ThreatTypes.setter
    def ThreatTypes(self, ThreatTypes):
        self._ThreatTypes = ThreatTypes

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Intelligences(self):
        return self._Intelligences

    @Intelligences.setter
    def Intelligences(self, Intelligences):
        self._Intelligences = Intelligences

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._Result = params.get("Result")
        self._Confidence = params.get("Confidence")
        self._ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Intelligences") is not None:
            self._Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self._Intelligences.append(obj)
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class DescribeThreatInfoRequest(AbstractModel):
    """DescribeThreatInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Key: 查询对象，域名或IP
        :type Key: str
        :param _Type: 查询类型，当前取值为domain或ip
        :type Type: str
        :param _Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self._Key = None
        self._Type = None
        self._Option = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Option(self):
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        self._Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeThreatInfoResponse(AbstractModel):
    """DescribeThreatInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param _Result: 判定结果，如：black、white、grey
        :type Result: str
        :param _Confidence: 置信度，取值0-100
        :type Confidence: int
        :param _ThreatTypes: 威胁类型。
botnet = 僵尸网络
trojan = 木马
ransomware = 勒索软件
worm = 蠕虫
dga = 域名生成算法
c2 = c&c
compromised = 失陷主机
dynamicIP = 动态IP
proxy = 代理
idc = idc 机房
whitelist = 白名单
tor = 暗网
miner = 挖矿
maleware site = 恶意站点
malware IP = 恶意IP
等等
        :type ThreatTypes: list of str
        :param _Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of str
        :param _Status: 当前状态
active = 活跃
sinkholed = sinkholed
inactive = 不活跃
unknown = 未知
expired = 过期
        :type Status: str
        :param _Context: 情报相关的上下文，参数option=1 的时候提供
每个数据默认为3 条
        :type Context: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReturnCode = None
        self._Result = None
        self._Confidence = None
        self._ThreatTypes = None
        self._Tags = None
        self._Status = None
        self._Context = None
        self._RequestId = None

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def ThreatTypes(self):
        return self._ThreatTypes

    @ThreatTypes.setter
    def ThreatTypes(self, ThreatTypes):
        self._ThreatTypes = ThreatTypes

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReturnCode = params.get("ReturnCode")
        self._Result = params.get("Result")
        self._Confidence = params.get("Confidence")
        self._ThreatTypes = params.get("ThreatTypes")
        self._Tags = params.get("Tags")
        self._Status = params.get("Status")
        self._Context = params.get("Context")
        self._RequestId = params.get("RequestId")


class FileInfoType(AbstractModel):
    """文件信息类型

    """

    def __init__(self):
        r"""
        :param _DetectId: 判定渠道
        :type DetectId: str
        :param _DetectPriority: 检测优先级
        :type DetectPriority: str
        :param _EnginePriority: 引擎优先级
        :type EnginePriority: str
        :param _FileExist: 样本是否存在
        :type FileExist: str
        :param _FileForceUpload: 文件上传
        :type FileForceUpload: str
        :param _FileSize: 文件大小
        :type FileSize: str
        :param _FileupTime: 文件上传时间
        :type FileupTime: str
        :param _FullVirusName: 病毒文件全名
        :type FullVirusName: str
        :param _IdcPosition: IDC位置
        :type IdcPosition: str
        :param _Md5Type: 文件md5值
        :type Md5Type: str
        :param _PeExist: PE结构是否存在
        :type PeExist: str
        :param _PeForceUpload: PE结构上传
        :type PeForceUpload: str
        :param _SafeLevel: 安全性等级
        :type SafeLevel: str
        :param _ScanModiTime: 扫描时间
        :type ScanModiTime: str
        :param _SubdetectId: 子判定渠道
        :type SubdetectId: str
        :param _UserDefName: 病毒名
        :type UserDefName: str
        :param _VirusType: 病毒类型
        :type VirusType: str
        :param _WhiteScore: 白名单分数
        :type WhiteScore: str
        """
        self._DetectId = None
        self._DetectPriority = None
        self._EnginePriority = None
        self._FileExist = None
        self._FileForceUpload = None
        self._FileSize = None
        self._FileupTime = None
        self._FullVirusName = None
        self._IdcPosition = None
        self._Md5Type = None
        self._PeExist = None
        self._PeForceUpload = None
        self._SafeLevel = None
        self._ScanModiTime = None
        self._SubdetectId = None
        self._UserDefName = None
        self._VirusType = None
        self._WhiteScore = None

    @property
    def DetectId(self):
        return self._DetectId

    @DetectId.setter
    def DetectId(self, DetectId):
        self._DetectId = DetectId

    @property
    def DetectPriority(self):
        return self._DetectPriority

    @DetectPriority.setter
    def DetectPriority(self, DetectPriority):
        self._DetectPriority = DetectPriority

    @property
    def EnginePriority(self):
        return self._EnginePriority

    @EnginePriority.setter
    def EnginePriority(self, EnginePriority):
        self._EnginePriority = EnginePriority

    @property
    def FileExist(self):
        return self._FileExist

    @FileExist.setter
    def FileExist(self, FileExist):
        self._FileExist = FileExist

    @property
    def FileForceUpload(self):
        return self._FileForceUpload

    @FileForceUpload.setter
    def FileForceUpload(self, FileForceUpload):
        self._FileForceUpload = FileForceUpload

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileupTime(self):
        return self._FileupTime

    @FileupTime.setter
    def FileupTime(self, FileupTime):
        self._FileupTime = FileupTime

    @property
    def FullVirusName(self):
        return self._FullVirusName

    @FullVirusName.setter
    def FullVirusName(self, FullVirusName):
        self._FullVirusName = FullVirusName

    @property
    def IdcPosition(self):
        return self._IdcPosition

    @IdcPosition.setter
    def IdcPosition(self, IdcPosition):
        self._IdcPosition = IdcPosition

    @property
    def Md5Type(self):
        return self._Md5Type

    @Md5Type.setter
    def Md5Type(self, Md5Type):
        self._Md5Type = Md5Type

    @property
    def PeExist(self):
        return self._PeExist

    @PeExist.setter
    def PeExist(self, PeExist):
        self._PeExist = PeExist

    @property
    def PeForceUpload(self):
        return self._PeForceUpload

    @PeForceUpload.setter
    def PeForceUpload(self, PeForceUpload):
        self._PeForceUpload = PeForceUpload

    @property
    def SafeLevel(self):
        return self._SafeLevel

    @SafeLevel.setter
    def SafeLevel(self, SafeLevel):
        self._SafeLevel = SafeLevel

    @property
    def ScanModiTime(self):
        return self._ScanModiTime

    @ScanModiTime.setter
    def ScanModiTime(self, ScanModiTime):
        self._ScanModiTime = ScanModiTime

    @property
    def SubdetectId(self):
        return self._SubdetectId

    @SubdetectId.setter
    def SubdetectId(self, SubdetectId):
        self._SubdetectId = SubdetectId

    @property
    def UserDefName(self):
        return self._UserDefName

    @UserDefName.setter
    def UserDefName(self, UserDefName):
        self._UserDefName = UserDefName

    @property
    def VirusType(self):
        return self._VirusType

    @VirusType.setter
    def VirusType(self, VirusType):
        self._VirusType = VirusType

    @property
    def WhiteScore(self):
        return self._WhiteScore

    @WhiteScore.setter
    def WhiteScore(self, WhiteScore):
        self._WhiteScore = WhiteScore


    def _deserialize(self, params):
        self._DetectId = params.get("DetectId")
        self._DetectPriority = params.get("DetectPriority")
        self._EnginePriority = params.get("EnginePriority")
        self._FileExist = params.get("FileExist")
        self._FileForceUpload = params.get("FileForceUpload")
        self._FileSize = params.get("FileSize")
        self._FileupTime = params.get("FileupTime")
        self._FullVirusName = params.get("FullVirusName")
        self._IdcPosition = params.get("IdcPosition")
        self._Md5Type = params.get("Md5Type")
        self._PeExist = params.get("PeExist")
        self._PeForceUpload = params.get("PeForceUpload")
        self._SafeLevel = params.get("SafeLevel")
        self._ScanModiTime = params.get("ScanModiTime")
        self._SubdetectId = params.get("SubdetectId")
        self._UserDefName = params.get("UserDefName")
        self._VirusType = params.get("VirusType")
        self._WhiteScore = params.get("WhiteScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceType(AbstractModel):
    """{ "source": "inergj_ai_predict", "stamp": "msraminer", "time": 1531994023 }

    """

    def __init__(self):
        r"""
        :param _Source: 来源
        :type Source: str
        :param _Stamp: 标记
        :type Stamp: str
        :param _Time: 时间
        :type Time: int
        """
        self._Source = None
        self._Stamp = None
        self._Time = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Stamp(self):
        return self._Stamp

    @Stamp.setter
    def Stamp(self, Stamp):
        self._Stamp = Stamp

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Stamp = params.get("Stamp")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagType(AbstractModel):
    """标签及对应的解释

    """

    def __init__(self):
        r"""
        :param _Tag: 标签
        :type Tag: str
        :param _Desc: 标签对应的中文解释
        :type Desc: str
        """
        self._Tag = None
        self._Desc = None

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Tag = params.get("Tag")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        