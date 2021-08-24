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


class GetLocalEngineRequest(AbstractModel):
    """GetLocalEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param Key: 购买服务后获得的授权信息，用于保证请求有效性
        :type Key: str
        """
        self.Key = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLocalEngineResponse(AbstractModel):
    """GetLocalEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 接口调用状态，成功返回200，失败返回400
        :type Status: int
        :param Info: 接口调用描述信息，成功返回"scan success"，失败返回"scan error"
        :type Info: str
        :param Data: 本地引擎下载地址
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class GetScanResultRequest(AbstractModel):
    """GetScanResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param Key: 购买服务后获得的授权信息，用于保证请求有效性
        :type Key: str
        :param Md5: 需要获取扫描接口的md5（只允许单个md5）
        :type Md5: str
        """
        self.Key = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetScanResultResponse(AbstractModel):
    """GetScanResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 接口调用状态，成功返回200，失败返回400
        :type Status: int
        :param Info: 接口调用描述信息，成功返回"scan success"，失败返回"scan error"
        :type Info: str
        :param Data: 实际结果信息，包括md5、scan_status、virus_name三个字段；virus_name报毒名："torjan.**":黑样本的报毒名、".":样本不报毒、"" :样本无检出信息，需上传扫描；
scan_status样本状态：-1无检出信息需上传扫描、0样本扫描中、1样本扫描结束且不报毒、2样本扫描结束且报黑、3样本下载失败；
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ScanFileHashRequest(AbstractModel):
    """ScanFileHash请求参数结构体

    """

    def __init__(self):
        r"""
        :param Key: 购买服务后获得的授权信息，用于保证请求有效性
        :type Key: str
        :param Md5s: 需要查询的md5值（支持单个和多个，多个md5间用逗号分格）
        :type Md5s: str
        :param WithCategory: 保留字段默认填0
        :type WithCategory: str
        :param SensitiveLevel: 松严规则控制字段默认填10（5-松、10-标准、15-严）
        :type SensitiveLevel: str
        """
        self.Key = None
        self.Md5s = None
        self.WithCategory = None
        self.SensitiveLevel = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Md5s = params.get("Md5s")
        self.WithCategory = params.get("WithCategory")
        self.SensitiveLevel = params.get("SensitiveLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanFileHashResponse(AbstractModel):
    """ScanFileHash返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 接口调用状态，成功返回200，失败返回400
        :type Status: int
        :param Info: 接口调用描述信息，成功返回"scan success"，失败返回"scan error"
        :type Info: str
        :param Data: 云查实际结果信息，包括md5、return_state、virus_state、virus_name字符逗号间隔；        
return_state查询状态：-1/0代表失败、1/2代表成功；
virus_state文状件态：0文件不存在、1白、2黑、3未知、4感染性、5低可信白；
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class ScanFileRequest(AbstractModel):
    """ScanFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param Key: 购买服务后获得的授权信息，用于保证请求有效性
        :type Key: str
        :param Sample: 文件下载url地址
        :type Sample: str
        :param Md5: 文件的md5值
        :type Md5: str
        """
        self.Key = None
        self.Sample = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sample = params.get("Sample")
        self.Md5 = params.get("Md5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanFileResponse(AbstractModel):
    """ScanFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 接口调用状态，成功返回200，失败返回400
        :type Status: int
        :param Info: 接口调用描述信息，成功返回"success"，失败返回"invalid request"
        :type Info: str
        :param Data: 异步扫描任务提交成功返回success
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")