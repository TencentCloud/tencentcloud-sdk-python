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


class CameraPersonInfo(AbstractModel):
    """摄像头抓图人物属性

    """

    def __init__(self):
        """
        :param TempId: 临时id，还未生成face id时返回
        :type TempId: str
        :param FaceId: 人脸face id
        :type FaceId: int
        :param IdType: 确定当次返回的哪个id有效，1-FaceId，2-TempId
        :type IdType: int
        :param FacePic: 当次抓拍到的人脸图片base编码
        :type FacePic: str
        :param Time: 当次抓拍时间戳
        :type Time: int
        """
        self.TempId = None
        self.FaceId = None
        self.IdType = None
        self.FacePic = None
        self.Time = None


    def _deserialize(self, params):
        self.TempId = params.get("TempId")
        self.FaceId = params.get("FaceId")
        self.IdType = params.get("IdType")
        self.FacePic = params.get("FacePic")
        self.Time = params.get("Time")


class DescribeCameraPersonRequest(AbstractModel):
    """DescribeCameraPerson请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :type ShopId: int
        :param CameraId: 摄像头id
        :type CameraId: int
        :param StartTime: 拉取开始时间戳，单位秒
        :type StartTime: int
        :param EndTime: 拉取结束时间戳，单位秒，不超过StartTime+10秒，超过默认为StartTime+10
        :type EndTime: int
        :param PosId: pos机id
        :type PosId: str
        :param Num: 拉取图片数，默认为1，最大为3
        :type Num: int
        :param IsNeedPic: 是否需要base64的图片，0-不需要，1-需要，默认0
        :type IsNeedPic: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.CameraId = None
        self.StartTime = None
        self.EndTime = None
        self.PosId = None
        self.Num = None
        self.IsNeedPic = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.CameraId = params.get("CameraId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PosId = params.get("PosId")
        self.Num = params.get("Num")
        self.IsNeedPic = params.get("IsNeedPic")


class DescribeCameraPersonResponse(AbstractModel):
    """DescribeCameraPerson返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 集团id
        :type CompanyId: str
        :param ShopId: 店铺id
        :type ShopId: int
        :param CameraId: 摄像机id
        :type CameraId: int
        :param PosId: pos机id
        :type PosId: str
        :param Infos: 抓取的顾客信息
        :type Infos: list of CameraPersonInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.CameraId = None
        self.PosId = None
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = CameraPersonInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFaceIdByTempIdRequest(AbstractModel):
    """DescribeFaceIdByTempId请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :type ShopId: int
        :param TempId: 临时id
        :type TempId: str
        :param CameraId: 摄像头id
        :type CameraId: int
        :param PosId: pos机id
        :type PosId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TempId = None
        self.CameraId = None
        self.PosId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TempId = params.get("TempId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")


class DescribeFaceIdByTempIdResponse(AbstractModel):
    """DescribeFaceIdByTempId返回参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 集团id
        :type CompanyId: str
        :param ShopId: 店铺id
        :type ShopId: int
        :param CameraId: 摄像机id
        :type CameraId: int
        :param PosId: pos机id
        :type PosId: str
        :param TempId: 请求的临时id
        :type TempId: str
        :param FaceId: 临时id对应的face id
        :type FaceId: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.CameraId = None
        self.PosId = None
        self.TempId = None
        self.FaceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")
        self.TempId = params.get("TempId")
        self.FaceId = params.get("FaceId")
        self.RequestId = params.get("RequestId")


class DescribeHistoryNetworkInfoRequest(AbstractModel):
    """DescribeHistoryNetworkInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Time: 请求时间戳
        :type Time: int
        :param CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，为0则拉取集团全部店铺当前
        :type ShopId: int
        :param StartDay: 拉取开始日期，格式：2018-09-05
        :type StartDay: str
        :param EndDay: 拉取结束日期，格式L:2018-09-05，超过StartDay 90天，按StartDay+90天算
        :type EndDay: str
        :param Limit: 拉取条数，默认10
        :type Limit: int
        :param Offset: 拉取偏移，返回offset之后的数据
        :type Offset: int
        """
        self.Time = None
        self.CompanyId = None
        self.ShopId = None
        self.StartDay = None
        self.EndDay = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDay = params.get("StartDay")
        self.EndDay = params.get("EndDay")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeHistoryNetworkInfoResponse(AbstractModel):
    """DescribeHistoryNetworkInfo返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceSet: 网络状态数据
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkHistoryInfo`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = NetworkHistoryInfo()
            self.InstanceSet._deserialize(params.get("InstanceSet"))
        self.RequestId = params.get("RequestId")


class DescribeNetworkInfoRequest(AbstractModel):
    """DescribeNetworkInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Time: 请求时间戳
        :type Time: int
        :param CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，不填则拉取集团全部店铺当前
        :type ShopId: int
        """
        self.Time = None
        self.CompanyId = None
        self.ShopId = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")


class DescribeNetworkInfoResponse(AbstractModel):
    """DescribeNetworkInfo返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceSet: 网络状态详情
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkLastInfo`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = NetworkLastInfo()
            self.InstanceSet._deserialize(params.get("InstanceSet"))
        self.RequestId = params.get("RequestId")


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
        :param PictureExpires: 图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :type PictureExpires: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartPersonId = None
        self.Offset = None
        self.Limit = None
        self.PictureExpires = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartPersonId = params.get("StartPersonId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PictureExpires = params.get("PictureExpires")


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
        :param PictureExpires: 图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :type PictureExpires: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None
        self.PictureExpires = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PictureExpires = params.get("PictureExpires")


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


class ModifyPersonTagInfoRequest(AbstractModel):
    """ModifyPersonTagInfo请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，为0则拉取集团全部店铺当前
        :type ShopId: int
        :param Tags: 需要设置的顾客信息，批量设置最大为10个
        :type Tags: list of PersonTagInfo
        """
        self.CompanyId = None
        self.ShopId = None
        self.Tags = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = PersonTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)


class ModifyPersonTagInfoResponse(AbstractModel):
    """ModifyPersonTagInfo返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NetworkHistoryInfo(AbstractModel):
    """查询网络状态历史数据输出

    """

    def __init__(self):
        """
        :param Count: 总数
        :type Count: int
        :param CompanyId: 集团id
        :type CompanyId: str
        :param ShopId: 店铺id
        :type ShopId: int
        :param Province: 店铺省份
        :type Province: str
        :param City: 店铺城市
        :type City: str
        :param ShopName: 店铺名称
        :type ShopName: str
        :param Infos: 网络信息
        :type Infos: list of NetworkInfoNoShop
        """
        self.Count = None
        self.CompanyId = None
        self.ShopId = None
        self.Province = None
        self.City = None
        self.ShopName = None
        self.Infos = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.ShopName = params.get("ShopName")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = NetworkInfoNoShop()
                obj._deserialize(item)
                self.Infos.append(obj)


class NetworkInfo(AbstractModel):
    """网络状态

    """

    def __init__(self):
        """
        :param CompanyId: 集团id
        :type CompanyId: str
        :param ShopId: 店铺id
        :type ShopId: int
        :param Province: 店铺省份
        :type Province: str
        :param City: 店铺城市
        :type City: str
        :param ShopName: 店铺名
        :type ShopName: str
        :param Upload: 上传带宽，单位Mb/s，-1：未知
        :type Upload: float
        :param Download: 下载带宽，单位Mb/s，-1：未知
        :type Download: float
        :param MinRtt: 最小延迟，单位ms，-1：未知
        :type MinRtt: float
        :param AvgRtt: 平均延迟，单位ms，-1：未知
        :type AvgRtt: float
        :param MaxRtt: 最大延迟，单位ms，-1：未知
        :type MaxRtt: float
        :param MdevRtt: 平均偏差延迟，单位ms，-1：未知
        :type MdevRtt: float
        :param Loss: 丢包率百分比，-1：未知
        :type Loss: float
        :param UpdateTime: 更新时间戳
        :type UpdateTime: int
        :param Mac: 上报网络状态设备
        :type Mac: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Province = None
        self.City = None
        self.ShopName = None
        self.Upload = None
        self.Download = None
        self.MinRtt = None
        self.AvgRtt = None
        self.MaxRtt = None
        self.MdevRtt = None
        self.Loss = None
        self.UpdateTime = None
        self.Mac = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.ShopName = params.get("ShopName")
        self.Upload = params.get("Upload")
        self.Download = params.get("Download")
        self.MinRtt = params.get("MinRtt")
        self.AvgRtt = params.get("AvgRtt")
        self.MaxRtt = params.get("MaxRtt")
        self.MdevRtt = params.get("MdevRtt")
        self.Loss = params.get("Loss")
        self.UpdateTime = params.get("UpdateTime")
        self.Mac = params.get("Mac")


class NetworkInfoNoShop(AbstractModel):
    """没有店铺信息的网络状态

    """

    def __init__(self):
        """
        :param Upload: 上传带宽，单位Mb/s，-1：未知
        :type Upload: float
        :param Download: 下载带宽，单位Mb/s，-1：未知
        :type Download: float
        :param MinRtt: 最小延迟，单位ms，-1：未知
        :type MinRtt: float
        :param AvgRtt: 平均延迟，单位ms，-1：未知
        :type AvgRtt: float
        :param MaxRtt: 最大延迟，单位ms，-1：未知
        :type MaxRtt: float
        :param MdevRtt: 平均偏差延迟，单位ms，-1：未知
        :type MdevRtt: float
        :param Loss: 丢包率百分比，-1：未知
        :type Loss: float
        :param UpdateTime: 更新时间戳
        :type UpdateTime: int
        :param Mac: 上报网络状态设备
        :type Mac: str
        """
        self.Upload = None
        self.Download = None
        self.MinRtt = None
        self.AvgRtt = None
        self.MaxRtt = None
        self.MdevRtt = None
        self.Loss = None
        self.UpdateTime = None
        self.Mac = None


    def _deserialize(self, params):
        self.Upload = params.get("Upload")
        self.Download = params.get("Download")
        self.MinRtt = params.get("MinRtt")
        self.AvgRtt = params.get("AvgRtt")
        self.MaxRtt = params.get("MaxRtt")
        self.MdevRtt = params.get("MdevRtt")
        self.Loss = params.get("Loss")
        self.UpdateTime = params.get("UpdateTime")
        self.Mac = params.get("Mac")


class NetworkLastInfo(AbstractModel):
    """获取当前门店最新网络状态数据返回结构

    """

    def __init__(self):
        """
        :param Count: 总数
        :type Count: int
        :param Infos: 网络状态
        :type Infos: list of NetworkInfo
        """
        self.Count = None
        self.Infos = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = NetworkInfo()
                obj._deserialize(item)
                self.Infos.append(obj)


class PersonInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        """
        :param PersonId: 用户ID
        :type PersonId: int
        :param PersonPicture: 人脸图片Base64内容，已弃用，返回默认空值
        :type PersonPicture: str
        :param Gender: 性别：0男1女
        :type Gender: int
        :param Age: 年龄
        :type Age: int
        :param PersonType: 身份类型：0-普通顾客，1~10黑名单，11~20白名单，11店员
        :type PersonType: int
        :param PersonPictureUrl: 人脸图片Url，在有效期内可以访问下载
        :type PersonPictureUrl: str
        """
        self.PersonId = None
        self.PersonPicture = None
        self.Gender = None
        self.Age = None
        self.PersonType = None
        self.PersonPictureUrl = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonPicture = params.get("PersonPicture")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.PersonType = params.get("PersonType")
        self.PersonPictureUrl = params.get("PersonPictureUrl")


class PersonTagInfo(AbstractModel):
    """修改顾客属性参数

    """

    def __init__(self):
        """
        :param OldType: 顾客原类型
        :type OldType: int
        :param NewType: 顾客新类型
        :type NewType: int
        :param PersonId: 顾客face id
        :type PersonId: int
        """
        self.OldType = None
        self.NewType = None
        self.PersonId = None


    def _deserialize(self, params):
        self.OldType = params.get("OldType")
        self.NewType = params.get("NewType")
        self.PersonId = params.get("PersonId")


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
        :param CapturedPicture: 抓拍到的头像Base64内容，已弃用，返回默认空值
        :type CapturedPicture: str
        :param MaskType: 口罩类型：0不戴口罩，1戴口罩
        :type MaskType: int
        :param GlassType: 眼镜类型：0不戴眼镜，1普通眼镜 , 2墨镜
        :type GlassType: int
        :param HairType: 发型：0 短发,  1长发
        :type HairType: int
        :param CapturedPictureUrl: 抓拍到的头像Url，在有效期内可以访问下载
        :type CapturedPictureUrl: str
        """
        self.PersonId = None
        self.VisitId = None
        self.InTime = None
        self.CapturedPicture = None
        self.MaskType = None
        self.GlassType = None
        self.HairType = None
        self.CapturedPictureUrl = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.VisitId = params.get("VisitId")
        self.InTime = params.get("InTime")
        self.CapturedPicture = params.get("CapturedPicture")
        self.MaskType = params.get("MaskType")
        self.GlassType = params.get("GlassType")
        self.HairType = params.get("HairType")
        self.CapturedPictureUrl = params.get("CapturedPictureUrl")


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