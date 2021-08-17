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


class ArrivedMallInfo(AbstractModel):
    """客户到场信息

    """

    def __init__(self):
        r"""
        :param ArrivedTime: 到场时间
        :type ArrivedTime: str
        :param LeaveTime: 出场时间
        :type LeaveTime: str
        :param StaySecond: 停留时间，秒
        :type StaySecond: int
        :param InCapPic: 到场抓拍图片
        :type InCapPic: str
        :param OutCapPic: 出场抓拍图片
        :type OutCapPic: str
        :param TraceId: 轨迹编码
        :type TraceId: str
        """
        self.ArrivedTime = None
        self.LeaveTime = None
        self.StaySecond = None
        self.InCapPic = None
        self.OutCapPic = None
        self.TraceId = None


    def _deserialize(self, params):
        self.ArrivedTime = params.get("ArrivedTime")
        self.LeaveTime = params.get("LeaveTime")
        self.StaySecond = params.get("StaySecond")
        self.InCapPic = params.get("InCapPic")
        self.OutCapPic = params.get("OutCapPic")
        self.TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraPersonInfo(AbstractModel):
    """摄像头抓图人物属性

    """

    def __init__(self):
        r"""
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
        :param PersonInfo: 当前的person基本信息，图片以FacePic为准，结构体内未填
        :type PersonInfo: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        """
        self.TempId = None
        self.FaceId = None
        self.IdType = None
        self.FacePic = None
        self.Time = None
        self.PersonInfo = None


    def _deserialize(self, params):
        self.TempId = params.get("TempId")
        self.FaceId = params.get("FaceId")
        self.IdType = params.get("IdType")
        self.FacePic = params.get("FacePic")
        self.Time = params.get("Time")
        if params.get("PersonInfo") is not None:
            self.PersonInfo = PersonInfo()
            self.PersonInfo._deserialize(params.get("PersonInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param Name: 账号名；需要是手机号
        :type Name: str
        :param Password: 密码；需要是(`~!@#$%^&*()_+=-）中的至少两种且八位以上
        :type Password: str
        :param ShopCode: 客户门店编码
        :type ShopCode: str
        :param Remark: 备注说明; 30个字符以内
        :type Remark: str
        """
        self.CompanyId = None
        self.Name = None
        self.Password = None
        self.ShopCode = None
        self.Remark = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.ShopCode = params.get("ShopCode")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFacePictureRequest(AbstractModel):
    """CreateFacePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param PersonType: 人物类型（0表示普通顾客，1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :type PersonType: int
        :param Picture: 图片BASE编码
        :type Picture: str
        :param PictureName: 图片名称
        :type PictureName: str
        :param ShopId: 店铺ID，如果不填表示操作集团身份库
        :type ShopId: int
        :param IsForceUpload: 是否强制更新：为ture时会为用户创建一个新的指定PersonType的身份;目前这个参数已废弃，可不传
        :type IsForceUpload: bool
        """
        self.CompanyId = None
        self.PersonType = None
        self.Picture = None
        self.PictureName = None
        self.ShopId = None
        self.IsForceUpload = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.PersonType = params.get("PersonType")
        self.Picture = params.get("Picture")
        self.PictureName = params.get("PictureName")
        self.ShopId = params.get("ShopId")
        self.IsForceUpload = params.get("IsForceUpload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFacePictureResponse(AbstractModel):
    """CreateFacePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param PersonId: 人物ID
        :type PersonId: int
        :param Status: 0.正常建档 1.重复身份 2.未检测到人脸 3.检测到多个人脸 4.人脸大小过小 5.人脸质量不达标 6.其他错误
        :type Status: int
        :param PictureUrl: 图片url
        :type PictureUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PersonId = None
        self.Status = None
        self.PictureUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Status = params.get("Status")
        self.PictureUrl = params.get("PictureUrl")
        self.RequestId = params.get("RequestId")


class DailyTracePoint(AbstractModel):
    """客户天轨迹

    """

    def __init__(self):
        r"""
        :param TraceDate: 轨迹日期
        :type TraceDate: str
        :param TracePointSet: 轨迹点序列
        :type TracePointSet: list of PersonTracePoint
        """
        self.TraceDate = None
        self.TracePointSet = None


    def _deserialize(self, params):
        self.TraceDate = params.get("TraceDate")
        if params.get("TracePointSet") is not None:
            self.TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = PersonTracePoint()
                obj._deserialize(item)
                self.TracePointSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonFeatureRequest(AbstractModel):
    """DeletePersonFeature请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param PersonId: 顾客ID
        :type PersonId: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonFeatureResponse(AbstractModel):
    """DeletePersonFeature返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCameraPersonRequest(AbstractModel):
    """DescribeCameraPerson请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCameraPersonResponse(AbstractModel):
    """DescribeCameraPerson返回参数结构体

    """

    def __init__(self):
        r"""
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeClusterPersonArrivedMallRequest(AbstractModel):
    """DescribeClusterPersonArrivedMall请求参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场编码
        :type MallId: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPersonArrivedMallResponse(AbstractModel):
    """DescribeClusterPersonArrivedMall返回参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场系统编码
        :type MallId: str
        :param MallCode: 卖场客户编码
        :type MallCode: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param ArrivedMallSet: 到场信息
        :type ArrivedMallSet: list of ArrivedMallInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.ArrivedMallSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("ArrivedMallSet") is not None:
            self.ArrivedMallSet = []
            for item in params.get("ArrivedMallSet"):
                obj = ArrivedMallInfo()
                obj._deserialize(item)
                self.ArrivedMallSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterPersonTraceRequest(AbstractModel):
    """DescribeClusterPersonTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场编码
        :type MallId: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPersonTraceResponse(AbstractModel):
    """DescribeClusterPersonTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场系统编码
        :type MallId: str
        :param MallCode: 卖场用户编码
        :type MallCode: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param TracePointSet: 轨迹序列
        :type TracePointSet: list of DailyTracePoint
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.TracePointSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("TracePointSet") is not None:
            self.TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = DailyTracePoint()
                obj._deserialize(item)
                self.TracePointSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFaceIdByTempIdRequest(AbstractModel):
    """DescribeFaceIdByTempId请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param PictureExpires: 图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :type PictureExpires: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.TempId = None
        self.CameraId = None
        self.PosId = None
        self.PictureExpires = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TempId = params.get("TempId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")
        self.PictureExpires = params.get("PictureExpires")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFaceIdByTempIdResponse(AbstractModel):
    """DescribeFaceIdByTempId返回参数结构体

    """

    def __init__(self):
        r"""
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
        :param PersonInfo: 顾客属性信息
        :type PersonInfo: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.CameraId = None
        self.PosId = None
        self.TempId = None
        self.FaceId = None
        self.PersonInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")
        self.TempId = params.get("TempId")
        self.FaceId = params.get("FaceId")
        if params.get("PersonInfo") is not None:
            self.PersonInfo = PersonInfo()
            self.PersonInfo._deserialize(params.get("PersonInfo"))
        self.RequestId = params.get("RequestId")


class DescribeHistoryNetworkInfoRequest(AbstractModel):
    """DescribeHistoryNetworkInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHistoryNetworkInfoResponse(AbstractModel):
    """DescribeHistoryNetworkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceSet: 网络状态数据
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkHistoryInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInfoResponse(AbstractModel):
    """DescribeNetworkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceSet: 网络状态详情
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkLastInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = NetworkLastInfo()
            self.InstanceSet._deserialize(params.get("InstanceSet"))
        self.RequestId = params.get("RequestId")


class DescribePersonArrivedMallRequest(AbstractModel):
    """DescribePersonArrivedMall请求参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场编码
        :type MallId: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonArrivedMallResponse(AbstractModel):
    """DescribePersonArrivedMall返回参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场系统编码
        :type MallId: str
        :param MallCode: 卖场用户编码
        :type MallCode: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param ArrivedMallSet: 到场轨迹
        :type ArrivedMallSet: list of ArrivedMallInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.ArrivedMallSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("ArrivedMallSet") is not None:
            self.ArrivedMallSet = []
            for item in params.get("ArrivedMallSet"):
                obj = ArrivedMallInfo()
                obj._deserialize(item)
                self.ArrivedMallSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonInfoByFacePictureRequest(AbstractModel):
    """DescribePersonInfoByFacePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :type ShopId: int
        :param Picture: 人脸图片BASE编码
        :type Picture: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Picture = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Picture = params.get("Picture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonInfoByFacePictureResponse(AbstractModel):
    """DescribePersonInfoByFacePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团id
        :type CompanyId: str
        :param ShopId: 店铺id
        :type ShopId: int
        :param PersonId: 顾客face id
        :type PersonId: int
        :param PictureUrl: 顾客底图url
        :type PictureUrl: str
        :param PersonType: 顾客类型（0表示普通顾客，1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :type PersonType: int
        :param FirstVisitTime: 顾客首次进店时间
        :type FirstVisitTime: str
        :param VisitTimes: 顾客历史到访次数
        :type VisitTimes: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None
        self.PictureUrl = None
        self.PersonType = None
        self.FirstVisitTime = None
        self.VisitTimes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")
        self.PictureUrl = params.get("PictureUrl")
        self.PersonType = params.get("PersonType")
        self.FirstVisitTime = params.get("FirstVisitTime")
        self.VisitTimes = params.get("VisitTimes")
        self.RequestId = params.get("RequestId")


class DescribePersonInfoRequest(AbstractModel):
    """DescribePersonInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param PersonType: 身份类型(0表示普通顾客，1 白名单，2 表示黑名单）
        :type PersonType: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartPersonId = None
        self.Offset = None
        self.Limit = None
        self.PictureExpires = None
        self.PersonType = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartPersonId = params.get("StartPersonId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PictureExpires = params.get("PictureExpires")
        self.PersonType = params.get("PersonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonInfoResponse(AbstractModel):
    """DescribePersonInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 总数
        :type TotalCount: int
        :param PersonInfoSet: 用户信息
        :type PersonInfoSet: list of PersonInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribePersonRequest(AbstractModel):
    """DescribePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场编码
        :type MallId: str
        :param Offset: 查询偏移
        :type Offset: int
        :param Limit: 查询数量，默认20，最大查询数量100
        :type Limit: int
        """
        self.MallId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonResponse(AbstractModel):
    """DescribePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总计客户数量
        :type TotalCount: int
        :param PersonSet: 客户信息
        :type PersonSet: list of PersonProfile
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = PersonProfile()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonTraceDetailRequest(AbstractModel):
    """DescribePersonTraceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场编码
        :type MallId: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param TraceId: 轨迹编码
        :type TraceId: str
        """
        self.MallId = None
        self.PersonId = None
        self.TraceId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonTraceDetailResponse(AbstractModel):
    """DescribePersonTraceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场编码
        :type MallId: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param TraceId: 轨迹编码
        :type TraceId: str
        :param CoordinateSet: 轨迹点坐标序列
        :type CoordinateSet: list of PersonCoordinate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.PersonId = None
        self.TraceId = None
        self.CoordinateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")
        if params.get("CoordinateSet") is not None:
            self.CoordinateSet = []
            for item in params.get("CoordinateSet"):
                obj = PersonCoordinate()
                obj._deserialize(item)
                self.CoordinateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonTraceRequest(AbstractModel):
    """DescribePersonTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场编码
        :type MallId: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonTraceResponse(AbstractModel):
    """DescribePersonTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param MallId: 卖场系统编码
        :type MallId: str
        :param MallCode: 卖场用户编码
        :type MallCode: str
        :param PersonId: 客户编码
        :type PersonId: str
        :param TraceRouteSet: 轨迹列表
        :type TraceRouteSet: list of PersonTraceRoute
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.TraceRouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("TraceRouteSet") is not None:
            self.TraceRouteSet = []
            for item in params.get("TraceRouteSet"):
                obj = PersonTraceRoute()
                obj._deserialize(item)
                self.TraceRouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonVisitInfoRequest(AbstractModel):
    """DescribePersonVisitInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        :param StartDate: 开始日期，格式yyyy-MM-dd，已废弃，请使用StartDateTime
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd，已废弃，请使用EndDateTime
        :type EndDate: str
        :param PictureExpires: 图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :type PictureExpires: int
        :param StartDateTime: 开始时间，格式yyyy-MM-dd HH:mm:ss
        :type StartDateTime: str
        :param EndDateTime: 结束时间，格式yyyy-MM-dd HH:mm:ss
        :type EndDateTime: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Offset = None
        self.Limit = None
        self.StartDate = None
        self.EndDate = None
        self.PictureExpires = None
        self.StartDateTime = None
        self.EndDateTime = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.PictureExpires = params.get("PictureExpires")
        self.StartDateTime = params.get("StartDateTime")
        self.EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonVisitInfoResponse(AbstractModel):
    """DescribePersonVisitInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 总数
        :type TotalCount: int
        :param PersonVisitInfoSet: 用户到访明细
        :type PersonVisitInfoSet: list of PersonVisitInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShopHourTrafficInfoResponse(AbstractModel):
    """DescribeShopHourTrafficInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 查询结果总数
        :type TotalCount: int
        :param ShopHourTrafficInfoSet: 分时客流信息
        :type ShopHourTrafficInfoSet: list of ShopHourTrafficInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShopInfoResponse(AbstractModel):
    """DescribeShopInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 门店总数
        :type TotalCount: int
        :param ShopInfoSet: 门店列表信息
        :type ShopInfoSet: list of ShopInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShopTrafficInfoResponse(AbstractModel):
    """DescribeShopTrafficInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 查询结果总数
        :type TotalCount: int
        :param ShopDayTrafficInfoSet: 客流信息列表
        :type ShopDayTrafficInfoSet: list of ShopDayTrafficInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeTrajectoryDataRequest(AbstractModel):
    """DescribeTrajectoryData请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param Limit: 限制返回数据的最大条数，最大 400（负数代为 400）
        :type Limit: int
        :param Gender: 顾客性别顾虑，0是男，1是女，其它代表不分性别
        :type Gender: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Gender = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Gender = params.get("Gender")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrajectoryDataResponse(AbstractModel):
    """DescribeTrajectoryData返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param TotalPerson: 总人数
        :type TotalPerson: int
        :param TotalTrajectory: 总动迹数目
        :type TotalTrajectory: int
        :param Person: 返回动迹中的总人数
        :type Person: int
        :param Trajectory: 返回动迹的数目
        :type Trajectory: int
        :param Data: 返回动迹的具体信息
        :type Data: list of TrajectorySunData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalPerson = None
        self.TotalTrajectory = None
        self.Person = None
        self.Trajectory = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalPerson = params.get("TotalPerson")
        self.TotalTrajectory = params.get("TotalTrajectory")
        self.Person = params.get("Person")
        self.Trajectory = params.get("Trajectory")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TrajectorySunData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowAgeInfoByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowAgeInfoByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowAgeInfoByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowAgeInfoByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param ZoneName: 区域名称
        :type ZoneName: str
        :param Data: 当前年龄段占比
        :type Data: list of float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowAndStayTimeRequest(AbstractModel):
    """DescribeZoneFlowAndStayTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowAndStayTimeResponse(AbstractModel):
    """DescribeZoneFlowAndStayTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团id
        :type CompanyId: str
        :param ShopId: 店铺id
        :type ShopId: int
        :param Data: 各区域人流数目和停留时长
        :type Data: list of ZoneFlowAndAvrStayTime
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneFlowAndAvrStayTime()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowDailyByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowDailyByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowDailyByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowDailyByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团id
        :type CompanyId: str
        :param ShopId: 店铺id
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param ZoneName: 区域名称
        :type ZoneName: str
        :param Data: 每日人流量
        :type Data: list of ZoneDayFlow
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneDayFlow()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowGenderAvrStayTimeByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowGenderAvrStayTimeByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowGenderAvrStayTimeByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param ZoneName: 区域名称
        :type ZoneName: str
        :param Data: 不同年龄段男女停留时间（返回格式为数组，从第 1 个到最后一个数据，年龄段分别为 0-17，18 - 23,  24 - 30, 31 - 40, 41 - 50, 51 - 60, 61 - 100）
        :type Data: list of ZoneAgeGroupAvrStayTime
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneAgeGroupAvrStayTime()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowGenderInfoByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowGenderInfoByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowGenderInfoByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowGenderInfoByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param ZoneName: 区域名称
        :type ZoneName: str
        :param MalePercent: 男性占比
        :type MalePercent: float
        :param FemalePercent: 女性占比
        :type FemalePercent: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.MalePercent = None
        self.FemalePercent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.MalePercent = params.get("MalePercent")
        self.FemalePercent = params.get("FemalePercent")
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowHourlyByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowHourlyByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowHourlyByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowHourlyByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID
        :type ShopId: int
        :param ZoneId: 区域ID
        :type ZoneId: int
        :param ZoneName: 区域名称
        :type ZoneName: str
        :param Data: 各个分时人流量
        :type Data: list of ZoneHourFlow
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneHourFlow()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneTrafficInfoRequest(AbstractModel):
    """DescribeZoneTrafficInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneTrafficInfoResponse(AbstractModel):
    """DescribeZoneTrafficInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param TotalCount: 查询结果总数
        :type TotalCount: int
        :param ZoneTrafficInfoSet: 区域客流信息列表
        :type ZoneTrafficInfoSet: list of ZoneTrafficInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HourTrafficInfoDetail(AbstractModel):
    """分时客流量详细信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonFeatureInfoRequest(AbstractModel):
    """ModifyPersonFeatureInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param PersonId: 需要修改的顾客id
        :type PersonId: int
        :param Picture: 图片BASE编码
        :type Picture: str
        :param PictureName: 图片名称（尽量不要重复）
        :type PictureName: str
        :param PersonType: 人物类型，仅能操作黑白名单顾客（1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :type PersonType: int
        :param ShopId: 店铺ID，如果不填表示操作集团身份库
        :type ShopId: int
        """
        self.CompanyId = None
        self.PersonId = None
        self.Picture = None
        self.PictureName = None
        self.PersonType = None
        self.ShopId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.PersonId = params.get("PersonId")
        self.Picture = params.get("Picture")
        self.PictureName = params.get("PictureName")
        self.PersonType = params.get("PersonType")
        self.ShopId = params.get("ShopId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonFeatureInfoResponse(AbstractModel):
    """ModifyPersonFeatureInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 店铺ID，如果不填表示操作集团身份库
        :type ShopId: int
        :param PersonId: 请求的顾客id
        :type PersonId: int
        :param PersonIdBind: 图片实际绑定person_id，可能与请求的person_id不同，以此id为准
        :type PersonIdBind: int
        :param PersonType: 请求的顾客类型
        :type PersonType: int
        :param SimilarPersonIds: 与请求的person_id类型相同、与请求图片特征相似的一个或多个person_id，需要额外确认这些id是否是同一个人
        :type SimilarPersonIds: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None
        self.PersonIdBind = None
        self.PersonType = None
        self.SimilarPersonIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")
        self.PersonIdBind = params.get("PersonIdBind")
        self.PersonType = params.get("PersonType")
        self.SimilarPersonIds = params.get("SimilarPersonIds")
        self.RequestId = params.get("RequestId")


class ModifyPersonTagInfoRequest(AbstractModel):
    """ModifyPersonTagInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonTagInfoResponse(AbstractModel):
    """ModifyPersonTagInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonTypeRequest(AbstractModel):
    """ModifyPersonType请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 集团ID
        :type CompanyId: str
        :param ShopId: 门店ID
        :type ShopId: int
        :param PersonId: 顾客ID
        :type PersonId: int
        :param PersonType: 身份类型(0表示普通顾客，1 白名单，2 表示黑名单）
        :type PersonType: int
        :param PersonSubType: 身份子类型:
PersonType=0时(普通顾客)，0普通顾客
PersonType=1时(白名单)，0店员，1商场人员，2其他类型人员，3区域经理，4注册会员，5VIP用户
PersonType=2时(黑名单)，0普通黑名单，1小偷)
        :type PersonSubType: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None
        self.PersonType = None
        self.PersonSubType = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")
        self.PersonType = params.get("PersonType")
        self.PersonSubType = params.get("PersonSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonTypeResponse(AbstractModel):
    """ModifyPersonType返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NetworkAndShopInfo(AbstractModel):
    """网络状态

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkHistoryInfo(AbstractModel):
    """查询网络状态历史数据输出

    """

    def __init__(self):
        r"""
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
        :type Infos: list of NetworkInfo
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
                obj = NetworkInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInfo(AbstractModel):
    """没有店铺信息的网络状态

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkLastInfo(AbstractModel):
    """获取当前门店最新网络状态数据返回结构

    """

    def __init__(self):
        r"""
        :param Count: 总数
        :type Count: int
        :param Infos: 网络状态
        :type Infos: list of NetworkAndShopInfo
        """
        self.Count = None
        self.Infos = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = NetworkAndShopInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonCoordinate(AbstractModel):
    """轨迹点坐标

    """

    def __init__(self):
        r"""
        :param CADX: CAD图X坐标
        :type CADX: float
        :param CADY: CAD图Y坐标
        :type CADY: float
        :param CapTime: 抓拍时间点
        :type CapTime: str
        :param CapPic: 抓拍图片
        :type CapPic: str
        :param MallAreaType: 卖场区域类型
        :type MallAreaType: int
        :param PosId: 坐标编号
        :type PosId: int
        :param ShopId: 门店编号
        :type ShopId: int
        :param Event: 事件
        :type Event: str
        """
        self.CADX = None
        self.CADY = None
        self.CapTime = None
        self.CapPic = None
        self.MallAreaType = None
        self.PosId = None
        self.ShopId = None
        self.Event = None


    def _deserialize(self, params):
        self.CADX = params.get("CADX")
        self.CADY = params.get("CADY")
        self.CapTime = params.get("CapTime")
        self.CapPic = params.get("CapPic")
        self.MallAreaType = params.get("MallAreaType")
        self.PosId = params.get("PosId")
        self.ShopId = params.get("ShopId")
        self.Event = params.get("Event")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param PersonId: 用户ID
        :type PersonId: int
        :param PersonPicture: 人脸图片Base64内容，已弃用，返回默认空值
        :type PersonPicture: str
        :param Gender: 性别：0男1女
        :type Gender: int
        :param Age: 年龄
        :type Age: int
        :param PersonType: 身份类型（0表示普通顾客，1 白名单，2 表示黑名单）
        :type PersonType: int
        :param PersonPictureUrl: 人脸图片Url，在有效期内可以访问下载
        :type PersonPictureUrl: str
        :param PersonSubType: 身份子类型:
PersonType=0时(普通顾客)，0普通顾客
PersonType=1时(白名单)，0店员，1商场人员，2其他类型人员，3区域经理，4注册用户，5VIP用户
PersonType=2时(黑名单)，0普通黑名单，1小偷)
        :type PersonSubType: int
        :param VisitTimes: 到访次数，-1表示未知
        :type VisitTimes: int
        :param VisitDays: 到访天数，-1表示未知
        :type VisitDays: int
        """
        self.PersonId = None
        self.PersonPicture = None
        self.Gender = None
        self.Age = None
        self.PersonType = None
        self.PersonPictureUrl = None
        self.PersonSubType = None
        self.VisitTimes = None
        self.VisitDays = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonPicture = params.get("PersonPicture")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.PersonType = params.get("PersonType")
        self.PersonPictureUrl = params.get("PersonPictureUrl")
        self.PersonSubType = params.get("PersonSubType")
        self.VisitTimes = params.get("VisitTimes")
        self.VisitDays = params.get("VisitDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonProfile(AbstractModel):
    """来访客人基本资料

    """

    def __init__(self):
        r"""
        :param PersonId: 客人编码
        :type PersonId: str
        :param Gender: 性别
        :type Gender: int
        :param Age: 年龄
        :type Age: int
        :param FirstArrivedTime: 首次到场时间
        :type FirstArrivedTime: str
        :param ArrivedCount: 来访次数
        :type ArrivedCount: int
        :param PicUrl: 客户图片
        :type PicUrl: str
        :param Similarity: 置信度
        :type Similarity: float
        """
        self.PersonId = None
        self.Gender = None
        self.Age = None
        self.FirstArrivedTime = None
        self.ArrivedCount = None
        self.PicUrl = None
        self.Similarity = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.FirstArrivedTime = params.get("FirstArrivedTime")
        self.ArrivedCount = params.get("ArrivedCount")
        self.PicUrl = params.get("PicUrl")
        self.Similarity = params.get("Similarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonTagInfo(AbstractModel):
    """修改顾客属性参数

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonTracePoint(AbstractModel):
    """客户轨迹点

    """

    def __init__(self):
        r"""
        :param MallAreaId: 卖场区域编码
        :type MallAreaId: int
        :param ShopId: 门店编码
        :type ShopId: int
        :param MallAreaType: 卖场区域类型
        :type MallAreaType: int
        :param TraceEventType: 轨迹事件
        :type TraceEventType: int
        :param TraceEventTime: 轨迹事件发生时间点
        :type TraceEventTime: str
        :param CapPic: 抓拍图片
        :type CapPic: str
        :param ShoppingBagType: 购物袋类型
        :type ShoppingBagType: int
        :param ShoppingBagCount: 购物袋数量
        :type ShoppingBagCount: int
        """
        self.MallAreaId = None
        self.ShopId = None
        self.MallAreaType = None
        self.TraceEventType = None
        self.TraceEventTime = None
        self.CapPic = None
        self.ShoppingBagType = None
        self.ShoppingBagCount = None


    def _deserialize(self, params):
        self.MallAreaId = params.get("MallAreaId")
        self.ShopId = params.get("ShopId")
        self.MallAreaType = params.get("MallAreaType")
        self.TraceEventType = params.get("TraceEventType")
        self.TraceEventTime = params.get("TraceEventTime")
        self.CapPic = params.get("CapPic")
        self.ShoppingBagType = params.get("ShoppingBagType")
        self.ShoppingBagCount = params.get("ShoppingBagCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonTraceRoute(AbstractModel):
    """客户轨迹序列

    """

    def __init__(self):
        r"""
        :param TraceId: 轨迹编码
        :type TraceId: str
        :param TracePointSet: 轨迹点序列
        :type TracePointSet: list of PersonTracePoint
        """
        self.TraceId = None
        self.TracePointSet = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        if params.get("TracePointSet") is not None:
            self.TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = PersonTracePoint()
                obj._deserialize(item)
                self.TracePointSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonVisitInfo(AbstractModel):
    """用户到访明细

    """

    def __init__(self):
        r"""
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
        :param SceneInfo: 抓拍头像的场景图信息
        :type SceneInfo: :class:`tencentcloud.youmall.v20180228.models.SceneInfo`
        """
        self.PersonId = None
        self.VisitId = None
        self.InTime = None
        self.CapturedPicture = None
        self.MaskType = None
        self.GlassType = None
        self.HairType = None
        self.CapturedPictureUrl = None
        self.SceneInfo = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.VisitId = params.get("VisitId")
        self.InTime = params.get("InTime")
        self.CapturedPicture = params.get("CapturedPicture")
        self.MaskType = params.get("MaskType")
        self.GlassType = params.get("GlassType")
        self.HairType = params.get("HairType")
        self.CapturedPictureUrl = params.get("CapturedPictureUrl")
        if params.get("SceneInfo") is not None:
            self.SceneInfo = SceneInfo()
            self.SceneInfo._deserialize(params.get("SceneInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCallbackRequest(AbstractModel):
    """RegisterCallback请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCallbackResponse(AbstractModel):
    """RegisterCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    """场景图信息

    """

    def __init__(self):
        r"""
        :param ScenePictureURL: 场景图
        :type ScenePictureURL: str
        :param HeadX: 抓拍头像左上角X坐标在场景图中的像素点位置
        :type HeadX: int
        :param HeadY: 抓拍头像左上角Y坐标在场景图中的像素点位置
        :type HeadY: int
        :param HeadWidth: 抓拍头像在场景图中占有的像素宽度
        :type HeadWidth: int
        :param HeadHeight: 抓拍头像在场景图中占有的像素高度
        :type HeadHeight: int
        """
        self.ScenePictureURL = None
        self.HeadX = None
        self.HeadY = None
        self.HeadWidth = None
        self.HeadHeight = None


    def _deserialize(self, params):
        self.ScenePictureURL = params.get("ScenePictureURL")
        self.HeadX = params.get("HeadX")
        self.HeadY = params.get("HeadY")
        self.HeadWidth = params.get("HeadWidth")
        self.HeadHeight = params.get("HeadHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShopDayTrafficInfo(AbstractModel):
    """门店客流量列表信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShopHourTrafficInfo(AbstractModel):
    """分时客流量信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShopInfo(AbstractModel):
    """客户所属的门店信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrajectorySunData(AbstractModel):
    """轨迹动线信息子结构

    """

    def __init__(self):
        r"""
        :param Zones: 区域动线，形如 x-x-x-x-x，其中 x 为区域 ID
        :type Zones: str
        :param Count: 该动线出现次数
        :type Count: int
        :param AvgStayTime: 该动线平均停留时间（秒）
        :type AvgStayTime: int
        """
        self.Zones = None
        self.Count = None
        self.AvgStayTime = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.Count = params.get("Count")
        self.AvgStayTime = params.get("AvgStayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneAgeGroupAvrStayTime(AbstractModel):
    """区域性别平均停留时间子结构

    """

    def __init__(self):
        r"""
        :param MaleAvrStayTime: 男性平均停留时间
        :type MaleAvrStayTime: float
        :param FemaleAvrStayTime: 女性平均停留时间
        :type FemaleAvrStayTime: float
        """
        self.MaleAvrStayTime = None
        self.FemaleAvrStayTime = None


    def _deserialize(self, params):
        self.MaleAvrStayTime = params.get("MaleAvrStayTime")
        self.FemaleAvrStayTime = params.get("FemaleAvrStayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDayFlow(AbstractModel):
    """每日客流统计子结构

    """

    def __init__(self):
        r"""
        :param Day: 日期，如 2018-08-6
        :type Day: str
        :param FlowCount: 客流量
        :type FlowCount: int
        """
        self.Day = None
        self.FlowCount = None


    def _deserialize(self, params):
        self.Day = params.get("Day")
        self.FlowCount = params.get("FlowCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFlowAndAvrStayTime(AbstractModel):
    """客流停留统计子结构

    """

    def __init__(self):
        r"""
        :param ZoneId: 区域id
        :type ZoneId: int
        :param ZoneName: 区域名称
        :type ZoneName: str
        :param FlowCount: 人流量
        :type FlowCount: int
        :param AvrStayTime: 平均停留时长
        :type AvrStayTime: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.FlowCount = None
        self.AvrStayTime = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.FlowCount = params.get("FlowCount")
        self.AvrStayTime = params.get("AvrStayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneHourFlow(AbstractModel):
    """客流统计分时数据子结构

    """

    def __init__(self):
        r"""
        :param Hour: 分时 0~23
        :type Hour: int
        :param FlowCount: 客流量
        :type FlowCount: int
        """
        self.Hour = None
        self.FlowCount = None


    def _deserialize(self, params):
        self.Hour = params.get("Hour")
        self.FlowCount = params.get("FlowCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneTrafficInfo(AbstractModel):
    """门店区域客流信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneTrafficInfoDetail(AbstractModel):
    """门店区域客流详细信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        