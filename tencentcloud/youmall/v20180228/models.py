# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class DescribePersonInfoRequest(AbstractModel):
    """DescribePersonInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param StartPersonId: 起始ID，第一次拉取时StartPersonId传0，后续送入的值为上一页最后一条数据项的PersonId
        :type StartPersonId: int
        :param Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartPersonId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartPersonId = params.get("StartPersonId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePersonInfoResponse(AbstractModel):
    """DescribePersonInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 总数
        :type TotalCount: int
        :param PersonInfoSet: 用户信息
        :type PersonInfoSet: list of PersonInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.PersonInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonInfoSet") is not None:
            self.PersonInfoSet = []
            for item in params.get("PersonInfoSet"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonVisitInfoRequest(AbstractModel):
    """DescribePersonVisitInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePersonVisitInfoResponse(AbstractModel):
    """DescribePersonVisitInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 总数
        :type TotalCount: int
        :param PersonVisitInfoSet: 用户到访明细
        :type PersonVisitInfoSet: list of PersonVisitInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.PersonVisitInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonVisitInfoSet") is not None:
            self.PersonVisitInfoSet = []
            for item in params.get("PersonVisitInfoSet"):
                obj = PersonVisitInfo()
                obj._deserialize(item)
                self.PersonVisitInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShopHourTrafficInfoRequest(AbstractModel):
    """DescribeShopHourTrafficInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param StartDate: 开始日期，格式：yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式：yyyy-MM-dd
        :type EndDate: str
        :param Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeShopHourTrafficInfoResponse(AbstractModel):
    """DescribeShopHourTrafficInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 查询结果总数
        :type TotalCount: int
        :param ShopHourTrafficInfoSet: 分时客流信息
        :type ShopHourTrafficInfoSet: list of ShopHourTrafficInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.ShopHourTrafficInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("ShopHourTrafficInfoSet") is not None:
            self.ShopHourTrafficInfoSet = []
            for item in params.get("ShopHourTrafficInfoSet"):
                obj = ShopHourTrafficInfo()
                obj._deserialize(item)
                self.ShopHourTrafficInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShopInfoRequest(AbstractModel):
    """DescribeShopInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeShopInfoResponse(AbstractModel):
    """DescribeShopInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 门店总数
        :type TotalCount: int
        :param ShopInfoSet: 门店列表信息
        :type ShopInfoSet: list of ShopInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ShopInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ShopInfoSet") is not None:
            self.ShopInfoSet = []
            for item in params.get("ShopInfoSet"):
                obj = ShopInfo()
                obj._deserialize(item)
                self.ShopInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShopTrafficInfoRequest(AbstractModel):
    """DescribeShopTrafficInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 介绍日期，格式yyyy-MM-dd
        :type EndDate: str
        :param Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeShopTrafficInfoResponse(AbstractModel):
    """DescribeShopTrafficInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 查询结果总数
        :type TotalCount: int
        :param ShopDayTrafficInfoSet: 客流信息列表
        :type ShopDayTrafficInfoSet: list of ShopDayTrafficInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.ShopDayTrafficInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("ShopDayTrafficInfoSet") is not None:
            self.ShopDayTrafficInfoSet = []
            for item in params.get("ShopDayTrafficInfoSet"):
                obj = ShopDayTrafficInfo()
                obj._deserialize(item)
                self.ShopDayTrafficInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneTrafficInfoRequest(AbstractModel):
    """DescribeZoneTrafficInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeZoneTrafficInfoResponse(AbstractModel):
    """DescribeZoneTrafficInfo返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 查询结果总数
        :type TotalCount: int
        :param ZoneTrafficInfoSet: 区域客流信息列表
        :type ZoneTrafficInfoSet: list of ZoneTrafficInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.ZoneTrafficInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneTrafficInfoSet") is not None:
            self.ZoneTrafficInfoSet = []
            for item in params.get("ZoneTrafficInfoSet"):
                obj = ZoneTrafficInfo()
                obj._deserialize(item)
                self.ZoneTrafficInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class GenderAgeTrafficDetail(AbstractModel):
    """性别年龄分组下的客流信息

    """

    def __init__(self):
        """
        :param Gender: 性别: 0男1女
        :type Gender: int
        :param AgeGap: 年龄区间，枚举值：0-17、18-23、24-30、31-40、41-50、51-60、>60
        :type AgeGap: str
        :param TrafficCount: 客流量
        :type TrafficCount: int
        """
        self.Gender = None
        self.AgeGap = None
        self.TrafficCount = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        self.AgeGap = params.get("AgeGap")
        self.TrafficCount = params.get("TrafficCount")


class HourTrafficInfoDetail(AbstractModel):
    """分时客流量详细信息

    """

    def __init__(self):
        """
        :param Hour: 小时 取值为：0，1，2，3，4，5，6，7，8，9，10，11，12，13，14，15，16，17，18，19，20，21，22，23
        :type Hour: int
        :param HourTrafficTotalCount: 分时客流量
        :type HourTrafficTotalCount: int
        """
        self.Hour = None
        self.HourTrafficTotalCount = None


    def _deserialize(self, params):
        self.Hour = params.get("Hour")
        self.HourTrafficTotalCount = params.get("HourTrafficTotalCount")


class PersonInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        """
        :param PersonId: 用户ID
        :type PersonId: int
        :param PersonPicture: 人脸图片，这里返回的是图片内容的Base64编码
        :type PersonPicture: str
        :param Gender: 性别：0男1女
        :type Gender: int
        :param Age: 年龄
        :type Age: int
        :param PersonType: 身份类型：0-普通顾客，1~10黑名单，11~20白名单，11店员
        :type PersonType: int
        """
        self.PersonId = None
        self.PersonPicture = None
        self.Gender = None
        self.Age = None
        self.PersonType = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonPicture = params.get("PersonPicture")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.PersonType = params.get("PersonType")


class PersonVisitInfo(AbstractModel):
    """用户到访明细

    """

    def __init__(self):
        """
        :param PersonId: 用户ID
        :type PersonId: int
        :param VisitId: 用户到访ID
        :type VisitId: int
        :param InTime: 到访时间：Unix时间戳
        :type InTime: int
        :param CapturedPicture: 抓拍到的头像，这里返回的是图片内容的Base64编码
        :type CapturedPicture: str
        :param MaskType: 口罩类型：0不戴口罩，1戴口罩
        :type MaskType: int
        :param GlassType: 眼镜类型：0不戴眼镜，1普通眼镜 , 2墨镜
        :type GlassType: int
        :param HairType: 发型：0 短发,  1长发
        :type HairType: int
        """
        self.PersonId = None
        self.VisitId = None
        self.InTime = None
        self.CapturedPicture = None
        self.MaskType = None
        self.GlassType = None
        self.HairType = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.VisitId = params.get("VisitId")
        self.InTime = params.get("InTime")
        self.CapturedPicture = params.get("CapturedPicture")
        self.MaskType = params.get("MaskType")
        self.GlassType = params.get("GlassType")
        self.HairType = params.get("HairType")


class RegisterCallbackRequest(AbstractModel):
    """RegisterCallback请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param BackUrl: 通知回调地址，完整url，示例（http://youmall.tencentcloudapi.com/）
        :type BackUrl: str
        :param Time: 请求时间戳
        :type Time: int
        :param NeedFacePic: 是否需要顾客图片，1-需要图片，其它-不需要图片
        :type NeedFacePic: int
        """
        self.CompanyId = None
        self.BackUrl = None
        self.Time = None
        self.NeedFacePic = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.BackUrl = params.get("BackUrl")
        self.Time = params.get("Time")
        self.NeedFacePic = params.get("NeedFacePic")


class RegisterCallbackResponse(AbstractModel):
    """RegisterCallback返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ShopDayTrafficInfo(AbstractModel):
    """门店客流量列表信息

    """

    def __init__(self):
        """
        :param Date: 日期
        :type Date: str
        :param DayTrafficTotalCount: 客流量
        :type DayTrafficTotalCount: int
        :param GenderAgeTrafficDetailSet: 性别年龄分组下的客流信息
        :type GenderAgeTrafficDetailSet: list of GenderAgeTrafficDetail
        """
        self.Date = None
        self.DayTrafficTotalCount = None
        self.GenderAgeTrafficDetailSet = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.DayTrafficTotalCount = params.get("DayTrafficTotalCount")
        if params.get("GenderAgeTrafficDetailSet") is not None:
            self.GenderAgeTrafficDetailSet = []
            for item in params.get("GenderAgeTrafficDetailSet"):
                obj = GenderAgeTrafficDetail()
                obj._deserialize(item)
                self.GenderAgeTrafficDetailSet.append(obj)


class ShopHourTrafficInfo(AbstractModel):
    """分时客流量信息

    """

    def __init__(self):
        """
        :param Date: 日期，格式yyyy-MM-dd
        :type Date: str
        :param HourTrafficInfoDetailSet: 分时客流详细信息
        :type HourTrafficInfoDetailSet: list of HourTrafficInfoDetail
        """
        self.Date = None
        self.HourTrafficInfoDetailSet = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        if params.get("HourTrafficInfoDetailSet") is not None:
            self.HourTrafficInfoDetailSet = []
            for item in params.get("HourTrafficInfoDetailSet"):
                obj = HourTrafficInfoDetail()
                obj._deserialize(item)
                self.HourTrafficInfoDetailSet.append(obj)


class ShopInfo(AbstractModel):
    """客户所属的门店信息

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param ShopName: 门店名称
        :type ShopName: str
        :param ShopCode: 客户门店编码
        :type ShopCode: str
        :param Province: 省
        :type Province: str
        :param City: 市
        :type City: str
        :param CompanyName: 公司名称
        :type CompanyName: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ShopName = None
        self.ShopCode = None
        self.Province = None
        self.City = None
        self.CompanyName = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ShopName = params.get("ShopName")
        self.ShopCode = params.get("ShopCode")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.CompanyName = params.get("CompanyName")


class ZoneTrafficInfo(AbstractModel):
    """门店区域客流信息

    """

    def __init__(self):
        """
        :param Date: 日期
        :type Date: str
        :param ZoneTrafficInfoDetailSet: 门店区域客流详细信息
        :type ZoneTrafficInfoDetailSet: list of ZoneTrafficInfoDetail
        """
        self.Date = None
        self.ZoneTrafficInfoDetailSet = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        if params.get("ZoneTrafficInfoDetailSet") is not None:
            self.ZoneTrafficInfoDetailSet = []
            for item in params.get("ZoneTrafficInfoDetailSet"):
                obj = ZoneTrafficInfoDetail()
                obj._deserialize(item)
                self.ZoneTrafficInfoDetailSet.append(obj)


class ZoneTrafficInfoDetail(AbstractModel):
    """门店区域客流详细信息

    """

    def __init__(self):
        """
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param ZoneName: 区域名称
        :type ZoneName: str
        :param TrafficTotalCount: 客流量
        :type TrafficTotalCount: int
        :param AvgStayTime: 平均停留时间
        :type AvgStayTime: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.TrafficTotalCount = None
        self.AvgStayTime = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.TrafficTotalCount = params.get("TrafficTotalCount")
        self.AvgStayTime = params.get("AvgStayTime")