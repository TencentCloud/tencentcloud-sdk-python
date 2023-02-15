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


class CreateBPFakeAPPListRequest(AbstractModel):
    """CreateBPFakeAPPList请求参数结构体

    """

    def __init__(self):
        r"""
        :param FakeAPPs: 仿冒应用下载链接。请严格按照模版进行填写：https://bma-privacy-detection-1251316161.cosgz.myqcloud.com/20221206/f8c7521fbd84f4c4e7c2a25ac233857e/批量仿冒应用举报模板.xlsx
        :type FakeAPPs: str
        """
        self.FakeAPPs = None


    def _deserialize(self, params):
        self.FakeAPPs = params.get("FakeAPPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeAPPListResponse(AbstractModel):
    """CreateBPFakeAPPList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPFakeAPPRequest(AbstractModel):
    """CreateBPFakeAPP请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 企业id
        :type CompanyId: int
        :param FakeAPPName: 仿冒应用名称
        :type FakeAPPName: str
        :param APPChan: 仿冒来源
        :type APPChan: str
        :param FakeAPPPackageName: 仿冒应用包名
        :type FakeAPPPackageName: str
        :param FakeAPPCert: 仿冒应用证书
        :type FakeAPPCert: str
        :param FakeAPPSize: 仿冒应用大小
        :type FakeAPPSize: str
        :param FakeAPPSnapshots: 仿冒截图
        :type FakeAPPSnapshots: list of str
        :param Note: 备注
        :type Note: str
        """
        self.CompanyId = None
        self.FakeAPPName = None
        self.APPChan = None
        self.FakeAPPPackageName = None
        self.FakeAPPCert = None
        self.FakeAPPSize = None
        self.FakeAPPSnapshots = None
        self.Note = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.FakeAPPName = params.get("FakeAPPName")
        self.APPChan = params.get("APPChan")
        self.FakeAPPPackageName = params.get("FakeAPPPackageName")
        self.FakeAPPCert = params.get("FakeAPPCert")
        self.FakeAPPSize = params.get("FakeAPPSize")
        self.FakeAPPSnapshots = params.get("FakeAPPSnapshots")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeAPPResponse(AbstractModel):
    """CreateBPFakeAPP返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPFakeURLRequest(AbstractModel):
    """CreateBPFakeURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 企业id
        :type CompanyId: int
        :param FakeURL: 仿冒网址
        :type FakeURL: str
        :param FakeURLSnapshots: 仿冒网址截图
        :type FakeURLSnapshots: list of str
        :param Note: 备注
        :type Note: str
        """
        self.CompanyId = None
        self.FakeURL = None
        self.FakeURLSnapshots = None
        self.Note = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.FakeURL = params.get("FakeURL")
        self.FakeURLSnapshots = params.get("FakeURLSnapshots")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLResponse(AbstractModel):
    """CreateBPFakeURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBPFakeURLsRequest(AbstractModel):
    """CreateBPFakeURLs请求参数结构体

    """

    def __init__(self):
        r"""
        :param FakeURLs: 仿冒网址下载链接：请严格按照模版要求填写，https://bma-privacy-detection-1251316161.cosgz.myqcloud.com/20221124/ff3273b24104d03fa3a8d0629a7f71a9/批量仿冒网址举报模板.xlsx
        :type FakeURLs: str
        """
        self.FakeURLs = None


    def _deserialize(self, params):
        self.FakeURLs = params.get("FakeURLs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBPFakeURLsResponse(AbstractModel):
    """CreateBPFakeURLs返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")