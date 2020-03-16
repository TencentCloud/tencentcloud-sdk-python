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

from tencentcloud.common.abstract_model import AbstractModel


class CheckDomainRequest(AbstractModel):
    """CheckDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 所查询域名名称
        :type DomainName: str
        :param Period: 年限
        :type Period: str
        """
        self.DomainName = None
        self.Period = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Period = params.get("Period")


class CheckDomainResponse(AbstractModel):
    """CheckDomain返回参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 所查询域名名称
        :type DomainName: str
        :param Available: 是否能够注册
        :type Available: bool
        :param Reason: 不能注册原因
        :type Reason: str
        :param Premium: 是否是溢价词
        :type Premium: bool
        :param Price: 域名价格
        :type Price: int
        :param BlackWord: 是否是敏感词
        :type BlackWord: bool
        :param Describe: 溢价词描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param FeeRenew: 溢价词的续费价格
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeRenew: int
        :param RealPrice: 域名真实价格
注意：此字段可能返回 null，表示取不到有效值。
        :type RealPrice: int
        :param FeeTransfer: 溢价词的转入价格
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeTransfer: int
        :param FeeRestore: 溢价词的赎回价格
        :type FeeRestore: int
        :param Period: 检测年限
        :type Period: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainName = None
        self.Available = None
        self.Reason = None
        self.Premium = None
        self.Price = None
        self.BlackWord = None
        self.Describe = None
        self.FeeRenew = None
        self.RealPrice = None
        self.FeeTransfer = None
        self.FeeRestore = None
        self.Period = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Available = params.get("Available")
        self.Reason = params.get("Reason")
        self.Premium = params.get("Premium")
        self.Price = params.get("Price")
        self.BlackWord = params.get("BlackWord")
        self.Describe = params.get("Describe")
        self.FeeRenew = params.get("FeeRenew")
        self.RealPrice = params.get("RealPrice")
        self.FeeTransfer = params.get("FeeTransfer")
        self.FeeRestore = params.get("FeeRestore")
        self.Period = params.get("Period")
        self.RequestId = params.get("RequestId")


class DescribeDomainPriceListRequest(AbstractModel):
    """DescribeDomainPriceList请求参数结构体

    """

    def __init__(self):
        """
        :param TldList: 查询价格的后缀列表。默认则为全部后缀
        :type TldList: list of str
        :param Year: 查询购买的年份，默认会列出所有年份的价格
        :type Year: list of int
        :param Operation: 域名的购买类型：new  新购，renew 续费，redem 赎回，tran 转入
        :type Operation: list of str
        """
        self.TldList = None
        self.Year = None
        self.Operation = None


    def _deserialize(self, params):
        self.TldList = params.get("TldList")
        self.Year = params.get("Year")
        self.Operation = params.get("Operation")


class DescribeDomainPriceListResponse(AbstractModel):
    """DescribeDomainPriceList返回参数结构体

    """

    def __init__(self):
        """
        :param PriceList: 域名价格列表
        :type PriceList: list of PriceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PriceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PriceList") is not None:
            self.PriceList = []
            for item in params.get("PriceList"):
                obj = PriceInfo()
                obj._deserialize(item)
                self.PriceList.append(obj)
        self.RequestId = params.get("RequestId")


class PriceInfo(AbstractModel):
    """域名价格信息

    """

    def __init__(self):
        """
        :param Tld: 域名后缀，例如.com
        :type Tld: str
        :param Year: 购买年限，范围[1-10]
        :type Year: int
        :param Price: 域名原价
        :type Price: int
        :param RealPrice: 域名现价
        :type RealPrice: int
        :param Operation: 商品的购买类型，新购，续费，赎回，转入，续费并转入
        :type Operation: str
        """
        self.Tld = None
        self.Year = None
        self.Price = None
        self.RealPrice = None
        self.Operation = None


    def _deserialize(self, params):
        self.Tld = params.get("Tld")
        self.Year = params.get("Year")
        self.Price = params.get("Price")
        self.RealPrice = params.get("RealPrice")
        self.Operation = params.get("Operation")