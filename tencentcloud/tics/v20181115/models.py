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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class DescribeDomainInfoRequest(AbstractModel):
    """DescribeDomainInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 要查询的域名
        :type Key: str
        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainInfoResponse(AbstractModel):
    """DescribeDomainInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param Result: 判定结果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param ThreatTypes: 威胁类型。
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
        :param Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of TagType
        :param Intelligences: 对应的历史上的威胁情报事件
        :type Intelligences: list of IntelligenceType
        :param Context: 情报相关的上下文
        :type Context: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFileInfoRequest(AbstractModel):
    """DescribeFileInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 要查询文件的MD5
        :type Key: str
        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeFileInfoResponse(AbstractModel):
    """DescribeFileInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param Result: 判定结果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param FileInfo: 文件类型，文件hash
（md5,sha1,sha256）,文件大小等等文件
基础信息
        :type FileInfo: list of FileInfoType
        :param Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of TagType
        :param Intelligences: 对应的历史上的威胁情报事件
        :type Intelligences: list of IntelligenceType
        :param Context: 情报相关的上下文
        :type Context: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.FileInfo = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        if params.get("FileInfo") is not None:
            self.FileInfo = []
            for item in params.get("FileInfo"):
                obj = FileInfoType()
                obj._deserialize(item)
                self.FileInfo.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpInfoRequest(AbstractModel):
    """DescribeIpInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 要查询的IP
        :type Key: str
        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpInfoResponse(AbstractModel):
    """DescribeIpInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param Result: 判定结果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param ThreatTypes: 威胁类型。
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
        :param Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of TagType
        :param Intelligences: 对应的历史上的威胁情报事件
        :type Intelligences: list of IntelligenceType
        :param Context: 情报相关的上下文
        :type Context: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeThreatInfoRequest(AbstractModel):
    """DescribeThreatInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 查询对象，域名或IP
        :type Key: str
        :param Type: 查询类型，当前取值为domain或ip
        :type Type: str
        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Type = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeThreatInfoResponse(AbstractModel):
    """DescribeThreatInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据
        :type ReturnCode: int
        :param Result: 判定结果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param ThreatTypes: 威胁类型。
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
        :param Tags: 恶意标签，对应的团伙，家族等信息。
        :type Tags: list of str
        :param Status: 当前状态
active = 活跃
sinkholed = sinkholed
inactive = 不活跃
unknown = 未知
expired = 过期
        :type Status: str
        :param Context: 情报相关的上下文，参数option=1 的时候提供
每个数据默认为3 条
        :type Context: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Status = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        self.Tags = params.get("Tags")
        self.Status = params.get("Status")
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FileInfoType(AbstractModel):
    """文件信息类型

    """

    def __init__(self):
        """
        :param DetectId: 判定渠道
        :type DetectId: str
        :param DetectPriority: 检测优先级
        :type DetectPriority: str
        :param EnginePriority: 引擎优先级
        :type EnginePriority: str
        :param FileExist: 样本是否存在
        :type FileExist: str
        :param FileForceUpload: 文件上传
        :type FileForceUpload: str
        :param FileSize: 文件大小
        :type FileSize: str
        :param FileupTime: 文件上传时间
        :type FileupTime: str
        :param FullVirusName: 病毒文件全名
        :type FullVirusName: str
        :param IdcPosition: IDC位置
        :type IdcPosition: str
        :param Md5Type: 文件md5值
        :type Md5Type: str
        :param PeExist: PE结构是否存在
        :type PeExist: str
        :param PeForceUpload: PE结构上传
        :type PeForceUpload: str
        :param SafeLevel: 安全性等级
        :type SafeLevel: str
        :param ScanModiTime: 扫描时间
        :type ScanModiTime: str
        :param SubdetectId: 子判定渠道
        :type SubdetectId: str
        :param UserDefName: 病毒名
        :type UserDefName: str
        :param VirusType: 病毒类型
        :type VirusType: str
        :param WhiteScore: 白名单分数
        :type WhiteScore: str
        """
        self.DetectId = None
        self.DetectPriority = None
        self.EnginePriority = None
        self.FileExist = None
        self.FileForceUpload = None
        self.FileSize = None
        self.FileupTime = None
        self.FullVirusName = None
        self.IdcPosition = None
        self.Md5Type = None
        self.PeExist = None
        self.PeForceUpload = None
        self.SafeLevel = None
        self.ScanModiTime = None
        self.SubdetectId = None
        self.UserDefName = None
        self.VirusType = None
        self.WhiteScore = None


    def _deserialize(self, params):
        self.DetectId = params.get("DetectId")
        self.DetectPriority = params.get("DetectPriority")
        self.EnginePriority = params.get("EnginePriority")
        self.FileExist = params.get("FileExist")
        self.FileForceUpload = params.get("FileForceUpload")
        self.FileSize = params.get("FileSize")
        self.FileupTime = params.get("FileupTime")
        self.FullVirusName = params.get("FullVirusName")
        self.IdcPosition = params.get("IdcPosition")
        self.Md5Type = params.get("Md5Type")
        self.PeExist = params.get("PeExist")
        self.PeForceUpload = params.get("PeForceUpload")
        self.SafeLevel = params.get("SafeLevel")
        self.ScanModiTime = params.get("ScanModiTime")
        self.SubdetectId = params.get("SubdetectId")
        self.UserDefName = params.get("UserDefName")
        self.VirusType = params.get("VirusType")
        self.WhiteScore = params.get("WhiteScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IntelligenceType(AbstractModel):
    """{ "source": "inergj_ai_predict", "stamp": "msraminer", "time": 1531994023 }

    """

    def __init__(self):
        """
        :param Source: 来源
        :type Source: str
        :param Stamp: 标记
        :type Stamp: str
        :param Time: 时间
        :type Time: int
        """
        self.Source = None
        self.Stamp = None
        self.Time = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Stamp = params.get("Stamp")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagType(AbstractModel):
    """标签及对应的解释

    """

    def __init__(self):
        """
        :param Tag: 标签
        :type Tag: str
        :param Desc: 标签对应的中文解释
        :type Desc: str
        """
        self.Tag = None
        self.Desc = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        