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
        :param _ArrivedTime: 到场时间
        :type ArrivedTime: str
        :param _LeaveTime: 出场时间
        :type LeaveTime: str
        :param _StaySecond: 停留时间，秒
        :type StaySecond: int
        :param _InCapPic: 到场抓拍图片
        :type InCapPic: str
        :param _OutCapPic: 出场抓拍图片
        :type OutCapPic: str
        :param _TraceId: 轨迹编码
        :type TraceId: str
        """
        self._ArrivedTime = None
        self._LeaveTime = None
        self._StaySecond = None
        self._InCapPic = None
        self._OutCapPic = None
        self._TraceId = None

    @property
    def ArrivedTime(self):
        """到场时间
        :rtype: str
        """
        return self._ArrivedTime

    @ArrivedTime.setter
    def ArrivedTime(self, ArrivedTime):
        self._ArrivedTime = ArrivedTime

    @property
    def LeaveTime(self):
        """出场时间
        :rtype: str
        """
        return self._LeaveTime

    @LeaveTime.setter
    def LeaveTime(self, LeaveTime):
        self._LeaveTime = LeaveTime

    @property
    def StaySecond(self):
        """停留时间，秒
        :rtype: int
        """
        return self._StaySecond

    @StaySecond.setter
    def StaySecond(self, StaySecond):
        self._StaySecond = StaySecond

    @property
    def InCapPic(self):
        """到场抓拍图片
        :rtype: str
        """
        return self._InCapPic

    @InCapPic.setter
    def InCapPic(self, InCapPic):
        self._InCapPic = InCapPic

    @property
    def OutCapPic(self):
        """出场抓拍图片
        :rtype: str
        """
        return self._OutCapPic

    @OutCapPic.setter
    def OutCapPic(self, OutCapPic):
        self._OutCapPic = OutCapPic

    @property
    def TraceId(self):
        """轨迹编码
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId


    def _deserialize(self, params):
        self._ArrivedTime = params.get("ArrivedTime")
        self._LeaveTime = params.get("LeaveTime")
        self._StaySecond = params.get("StaySecond")
        self._InCapPic = params.get("InCapPic")
        self._OutCapPic = params.get("OutCapPic")
        self._TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraPersonInfo(AbstractModel):
    """摄像头抓图人物属性

    """

    def __init__(self):
        r"""
        :param _TempId: 临时id，还未生成face id时返回
        :type TempId: str
        :param _FaceId: 人脸face id
        :type FaceId: int
        :param _IdType: 确定当次返回的哪个id有效，1-FaceId，2-TempId
        :type IdType: int
        :param _FacePic: 当次抓拍到的人脸图片base编码
        :type FacePic: str
        :param _Time: 当次抓拍时间戳
        :type Time: int
        :param _PersonInfo: 当前的person基本信息，图片以FacePic为准，结构体内未填
        :type PersonInfo: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        """
        self._TempId = None
        self._FaceId = None
        self._IdType = None
        self._FacePic = None
        self._Time = None
        self._PersonInfo = None

    @property
    def TempId(self):
        """临时id，还未生成face id时返回
        :rtype: str
        """
        return self._TempId

    @TempId.setter
    def TempId(self, TempId):
        self._TempId = TempId

    @property
    def FaceId(self):
        """人脸face id
        :rtype: int
        """
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def IdType(self):
        """确定当次返回的哪个id有效，1-FaceId，2-TempId
        :rtype: int
        """
        return self._IdType

    @IdType.setter
    def IdType(self, IdType):
        self._IdType = IdType

    @property
    def FacePic(self):
        """当次抓拍到的人脸图片base编码
        :rtype: str
        """
        return self._FacePic

    @FacePic.setter
    def FacePic(self, FacePic):
        self._FacePic = FacePic

    @property
    def Time(self):
        """当次抓拍时间戳
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def PersonInfo(self):
        """当前的person基本信息，图片以FacePic为准，结构体内未填
        :rtype: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        """
        return self._PersonInfo

    @PersonInfo.setter
    def PersonInfo(self, PersonInfo):
        self._PersonInfo = PersonInfo


    def _deserialize(self, params):
        self._TempId = params.get("TempId")
        self._FaceId = params.get("FaceId")
        self._IdType = params.get("IdType")
        self._FacePic = params.get("FacePic")
        self._Time = params.get("Time")
        if params.get("PersonInfo") is not None:
            self._PersonInfo = PersonInfo()
            self._PersonInfo._deserialize(params.get("PersonInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _Name: 账号名；需要是手机号
        :type Name: str
        :param _Password: 密码；需要是(`~!@#$%^&*()_+=-）中的至少两种且八位以上
        :type Password: str
        :param _ShopCode: 客户门店编码
        :type ShopCode: str
        :param _Remark: 备注说明; 30个字符以内
        :type Remark: str
        """
        self._CompanyId = None
        self._Name = None
        self._Password = None
        self._ShopCode = None
        self._Remark = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def Name(self):
        """账号名；需要是手机号
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        """密码；需要是(`~!@#$%^&*()_+=-）中的至少两种且八位以上
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ShopCode(self):
        """客户门店编码
        :rtype: str
        """
        return self._ShopCode

    @ShopCode.setter
    def ShopCode(self, ShopCode):
        self._ShopCode = ShopCode

    @property
    def Remark(self):
        """备注说明; 30个字符以内
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._ShopCode = params.get("ShopCode")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateFacePictureRequest(AbstractModel):
    """CreateFacePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _PersonType: 人物类型（0表示普通顾客，1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :type PersonType: int
        :param _Picture: 图片BASE编码
        :type Picture: str
        :param _PictureName: 图片名称
        :type PictureName: str
        :param _ShopId: 店铺ID，如果不填表示操作集团身份库
        :type ShopId: int
        :param _IsForceUpload: 是否强制更新：为ture时会为用户创建一个新的指定PersonType的身份;目前这个参数已废弃，可不传
        :type IsForceUpload: bool
        """
        self._CompanyId = None
        self._PersonType = None
        self._Picture = None
        self._PictureName = None
        self._ShopId = None
        self._IsForceUpload = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def PersonType(self):
        """人物类型（0表示普通顾客，1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :rtype: int
        """
        return self._PersonType

    @PersonType.setter
    def PersonType(self, PersonType):
        self._PersonType = PersonType

    @property
    def Picture(self):
        """图片BASE编码
        :rtype: str
        """
        return self._Picture

    @Picture.setter
    def Picture(self, Picture):
        self._Picture = Picture

    @property
    def PictureName(self):
        """图片名称
        :rtype: str
        """
        return self._PictureName

    @PictureName.setter
    def PictureName(self, PictureName):
        self._PictureName = PictureName

    @property
    def ShopId(self):
        """店铺ID，如果不填表示操作集团身份库
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def IsForceUpload(self):
        """是否强制更新：为ture时会为用户创建一个新的指定PersonType的身份;目前这个参数已废弃，可不传
        :rtype: bool
        """
        return self._IsForceUpload

    @IsForceUpload.setter
    def IsForceUpload(self, IsForceUpload):
        self._IsForceUpload = IsForceUpload


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._PersonType = params.get("PersonType")
        self._Picture = params.get("Picture")
        self._PictureName = params.get("PictureName")
        self._ShopId = params.get("ShopId")
        self._IsForceUpload = params.get("IsForceUpload")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFacePictureResponse(AbstractModel):
    """CreateFacePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PersonId: 人物ID
        :type PersonId: int
        :param _Status: 0.正常建档 1.重复身份 2.未检测到人脸 3.检测到多个人脸 4.人脸大小过小 5.人脸质量不达标 6.其他错误
        :type Status: int
        :param _PictureUrl: 图片url
        :type PictureUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PersonId = None
        self._Status = None
        self._PictureUrl = None
        self._RequestId = None

    @property
    def PersonId(self):
        """人物ID
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Status(self):
        """0.正常建档 1.重复身份 2.未检测到人脸 3.检测到多个人脸 4.人脸大小过小 5.人脸质量不达标 6.其他错误
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PictureUrl(self):
        """图片url
        :rtype: str
        """
        return self._PictureUrl

    @PictureUrl.setter
    def PictureUrl(self, PictureUrl):
        self._PictureUrl = PictureUrl

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Status = params.get("Status")
        self._PictureUrl = params.get("PictureUrl")
        self._RequestId = params.get("RequestId")


class DailyTracePoint(AbstractModel):
    """客户天轨迹

    """

    def __init__(self):
        r"""
        :param _TraceDate: 轨迹日期
        :type TraceDate: str
        :param _TracePointSet: 轨迹点序列
        :type TracePointSet: list of PersonTracePoint
        """
        self._TraceDate = None
        self._TracePointSet = None

    @property
    def TraceDate(self):
        """轨迹日期
        :rtype: str
        """
        return self._TraceDate

    @TraceDate.setter
    def TraceDate(self, TraceDate):
        self._TraceDate = TraceDate

    @property
    def TracePointSet(self):
        """轨迹点序列
        :rtype: list of PersonTracePoint
        """
        return self._TracePointSet

    @TracePointSet.setter
    def TracePointSet(self, TracePointSet):
        self._TracePointSet = TracePointSet


    def _deserialize(self, params):
        self._TraceDate = params.get("TraceDate")
        if params.get("TracePointSet") is not None:
            self._TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = PersonTracePoint()
                obj._deserialize(item)
                self._TracePointSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonFeatureRequest(AbstractModel):
    """DeletePersonFeature请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _PersonId: 顾客ID
        :type PersonId: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._PersonId = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def PersonId(self):
        """顾客ID
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonFeatureResponse(AbstractModel):
    """DeletePersonFeature返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCameraPersonRequest(AbstractModel):
    """DescribeCameraPerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param _ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :type ShopId: int
        :param _CameraId: 摄像头id
        :type CameraId: int
        :param _StartTime: 拉取开始时间戳，单位秒
        :type StartTime: int
        :param _EndTime: 拉取结束时间戳，单位秒，不超过StartTime+10秒，超过默认为StartTime+10
        :type EndTime: int
        :param _PosId: pos机id
        :type PosId: str
        :param _Num: 拉取图片数，默认为1，最大为3
        :type Num: int
        :param _IsNeedPic: 是否需要base64的图片，0-不需要，1-需要，默认0
        :type IsNeedPic: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._CameraId = None
        self._StartTime = None
        self._EndTime = None
        self._PosId = None
        self._Num = None
        self._IsNeedPic = None

    @property
    def CompanyId(self):
        """优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def CameraId(self):
        """摄像头id
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def StartTime(self):
        """拉取开始时间戳，单位秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """拉取结束时间戳，单位秒，不超过StartTime+10秒，超过默认为StartTime+10
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PosId(self):
        """pos机id
        :rtype: str
        """
        return self._PosId

    @PosId.setter
    def PosId(self, PosId):
        self._PosId = PosId

    @property
    def Num(self):
        """拉取图片数，默认为1，最大为3
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def IsNeedPic(self):
        """是否需要base64的图片，0-不需要，1-需要，默认0
        :rtype: int
        """
        return self._IsNeedPic

    @IsNeedPic.setter
    def IsNeedPic(self, IsNeedPic):
        self._IsNeedPic = IsNeedPic


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._CameraId = params.get("CameraId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PosId = params.get("PosId")
        self._Num = params.get("Num")
        self._IsNeedPic = params.get("IsNeedPic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCameraPersonResponse(AbstractModel):
    """DescribeCameraPerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团id
        :type CompanyId: str
        :param _ShopId: 店铺id
        :type ShopId: int
        :param _CameraId: 摄像机id
        :type CameraId: int
        :param _PosId: pos机id
        :type PosId: str
        :param _Infos: 抓取的顾客信息
        :type Infos: list of CameraPersonInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._CameraId = None
        self._PosId = None
        self._Infos = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团id
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺id
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def CameraId(self):
        """摄像机id
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def PosId(self):
        """pos机id
        :rtype: str
        """
        return self._PosId

    @PosId.setter
    def PosId(self, PosId):
        self._PosId = PosId

    @property
    def Infos(self):
        """抓取的顾客信息
        :rtype: list of CameraPersonInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._CameraId = params.get("CameraId")
        self._PosId = params.get("PosId")
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = CameraPersonInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPersonArrivedMallRequest(AbstractModel):
    """DescribeClusterPersonArrivedMall请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场编码
        :type MallId: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        """
        self._MallId = None
        self._PersonId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def MallId(self):
        """卖场编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def StartTime(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._PersonId = params.get("PersonId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPersonArrivedMallResponse(AbstractModel):
    """DescribeClusterPersonArrivedMall返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场系统编码
        :type MallId: str
        :param _MallCode: 卖场客户编码
        :type MallCode: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _ArrivedMallSet: 到场信息
        :type ArrivedMallSet: list of ArrivedMallInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MallId = None
        self._MallCode = None
        self._PersonId = None
        self._ArrivedMallSet = None
        self._RequestId = None

    @property
    def MallId(self):
        """卖场系统编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def MallCode(self):
        """卖场客户编码
        :rtype: str
        """
        return self._MallCode

    @MallCode.setter
    def MallCode(self, MallCode):
        self._MallCode = MallCode

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ArrivedMallSet(self):
        """到场信息
        :rtype: list of ArrivedMallInfo
        """
        return self._ArrivedMallSet

    @ArrivedMallSet.setter
    def ArrivedMallSet(self, ArrivedMallSet):
        self._ArrivedMallSet = ArrivedMallSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._MallCode = params.get("MallCode")
        self._PersonId = params.get("PersonId")
        if params.get("ArrivedMallSet") is not None:
            self._ArrivedMallSet = []
            for item in params.get("ArrivedMallSet"):
                obj = ArrivedMallInfo()
                obj._deserialize(item)
                self._ArrivedMallSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterPersonTraceRequest(AbstractModel):
    """DescribeClusterPersonTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场编码
        :type MallId: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        """
        self._MallId = None
        self._PersonId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def MallId(self):
        """卖场编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def StartTime(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._PersonId = params.get("PersonId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterPersonTraceResponse(AbstractModel):
    """DescribeClusterPersonTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场系统编码
        :type MallId: str
        :param _MallCode: 卖场用户编码
        :type MallCode: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _TracePointSet: 轨迹序列
        :type TracePointSet: list of DailyTracePoint
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MallId = None
        self._MallCode = None
        self._PersonId = None
        self._TracePointSet = None
        self._RequestId = None

    @property
    def MallId(self):
        """卖场系统编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def MallCode(self):
        """卖场用户编码
        :rtype: str
        """
        return self._MallCode

    @MallCode.setter
    def MallCode(self, MallCode):
        self._MallCode = MallCode

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def TracePointSet(self):
        """轨迹序列
        :rtype: list of DailyTracePoint
        """
        return self._TracePointSet

    @TracePointSet.setter
    def TracePointSet(self, TracePointSet):
        self._TracePointSet = TracePointSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._MallCode = params.get("MallCode")
        self._PersonId = params.get("PersonId")
        if params.get("TracePointSet") is not None:
            self._TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = DailyTracePoint()
                obj._deserialize(item)
                self._TracePointSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeFaceIdByTempIdRequest(AbstractModel):
    """DescribeFaceIdByTempId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param _ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :type ShopId: int
        :param _TempId: 临时id
        :type TempId: str
        :param _CameraId: 摄像头id
        :type CameraId: int
        :param _PosId: pos机id
        :type PosId: str
        :param _PictureExpires: 图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :type PictureExpires: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._TempId = None
        self._CameraId = None
        self._PosId = None
        self._PictureExpires = None

    @property
    def CompanyId(self):
        """优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def TempId(self):
        """临时id
        :rtype: str
        """
        return self._TempId

    @TempId.setter
    def TempId(self, TempId):
        self._TempId = TempId

    @property
    def CameraId(self):
        """摄像头id
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def PosId(self):
        """pos机id
        :rtype: str
        """
        return self._PosId

    @PosId.setter
    def PosId(self, PosId):
        self._PosId = PosId

    @property
    def PictureExpires(self):
        """图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :rtype: int
        """
        return self._PictureExpires

    @PictureExpires.setter
    def PictureExpires(self, PictureExpires):
        self._PictureExpires = PictureExpires


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._TempId = params.get("TempId")
        self._CameraId = params.get("CameraId")
        self._PosId = params.get("PosId")
        self._PictureExpires = params.get("PictureExpires")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFaceIdByTempIdResponse(AbstractModel):
    """DescribeFaceIdByTempId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团id
        :type CompanyId: str
        :param _ShopId: 店铺id
        :type ShopId: int
        :param _CameraId: 摄像机id
        :type CameraId: int
        :param _PosId: pos机id
        :type PosId: str
        :param _TempId: 请求的临时id
        :type TempId: str
        :param _FaceId: 临时id对应的face id
        :type FaceId: int
        :param _PersonInfo: 顾客属性信息
        :type PersonInfo: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._CameraId = None
        self._PosId = None
        self._TempId = None
        self._FaceId = None
        self._PersonInfo = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团id
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺id
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def CameraId(self):
        """摄像机id
        :rtype: int
        """
        return self._CameraId

    @CameraId.setter
    def CameraId(self, CameraId):
        self._CameraId = CameraId

    @property
    def PosId(self):
        """pos机id
        :rtype: str
        """
        return self._PosId

    @PosId.setter
    def PosId(self, PosId):
        self._PosId = PosId

    @property
    def TempId(self):
        """请求的临时id
        :rtype: str
        """
        return self._TempId

    @TempId.setter
    def TempId(self, TempId):
        self._TempId = TempId

    @property
    def FaceId(self):
        """临时id对应的face id
        :rtype: int
        """
        return self._FaceId

    @FaceId.setter
    def FaceId(self, FaceId):
        self._FaceId = FaceId

    @property
    def PersonInfo(self):
        """顾客属性信息
        :rtype: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        """
        return self._PersonInfo

    @PersonInfo.setter
    def PersonInfo(self, PersonInfo):
        self._PersonInfo = PersonInfo

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._CameraId = params.get("CameraId")
        self._PosId = params.get("PosId")
        self._TempId = params.get("TempId")
        self._FaceId = params.get("FaceId")
        if params.get("PersonInfo") is not None:
            self._PersonInfo = PersonInfo()
            self._PersonInfo._deserialize(params.get("PersonInfo"))
        self._RequestId = params.get("RequestId")


class DescribeHistoryNetworkInfoRequest(AbstractModel):
    """DescribeHistoryNetworkInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Time: 请求时间戳
        :type Time: int
        :param _CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param _ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，为0则拉取集团全部店铺当前
        :type ShopId: int
        :param _StartDay: 拉取开始日期，格式：2018-09-05
        :type StartDay: str
        :param _EndDay: 拉取结束日期，格式L:2018-09-05，超过StartDay 90天，按StartDay+90天算
        :type EndDay: str
        :param _Limit: 拉取条数，默认10
        :type Limit: int
        :param _Offset: 拉取偏移，返回offset之后的数据
        :type Offset: int
        """
        self._Time = None
        self._CompanyId = None
        self._ShopId = None
        self._StartDay = None
        self._EndDay = None
        self._Limit = None
        self._Offset = None

    @property
    def Time(self):
        """请求时间戳
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def CompanyId(self):
        """优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，为0则拉取集团全部店铺当前
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def StartDay(self):
        """拉取开始日期，格式：2018-09-05
        :rtype: str
        """
        return self._StartDay

    @StartDay.setter
    def StartDay(self, StartDay):
        self._StartDay = StartDay

    @property
    def EndDay(self):
        """拉取结束日期，格式L:2018-09-05，超过StartDay 90天，按StartDay+90天算
        :rtype: str
        """
        return self._EndDay

    @EndDay.setter
    def EndDay(self, EndDay):
        self._EndDay = EndDay

    @property
    def Limit(self):
        """拉取条数，默认10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """拉取偏移，返回offset之后的数据
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._StartDay = params.get("StartDay")
        self._EndDay = params.get("EndDay")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHistoryNetworkInfoResponse(AbstractModel):
    """DescribeHistoryNetworkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: 网络状态数据
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkHistoryInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        """网络状态数据
        :rtype: :class:`tencentcloud.youmall.v20180228.models.NetworkHistoryInfo`
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self._InstanceSet = NetworkHistoryInfo()
            self._InstanceSet._deserialize(params.get("InstanceSet"))
        self._RequestId = params.get("RequestId")


class DescribeNetworkInfoRequest(AbstractModel):
    """DescribeNetworkInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Time: 请求时间戳
        :type Time: int
        :param _CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param _ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，不填则拉取集团全部店铺当前
        :type ShopId: int
        """
        self._Time = None
        self._CompanyId = None
        self._ShopId = None

    @property
    def Time(self):
        """请求时间戳
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def CompanyId(self):
        """优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，不填则拉取集团全部店铺当前
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInfoResponse(AbstractModel):
    """DescribeNetworkInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: 网络状态详情
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkLastInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        """网络状态详情
        :rtype: :class:`tencentcloud.youmall.v20180228.models.NetworkLastInfo`
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self._InstanceSet = NetworkLastInfo()
            self._InstanceSet._deserialize(params.get("InstanceSet"))
        self._RequestId = params.get("RequestId")


class DescribePersonArrivedMallRequest(AbstractModel):
    """DescribePersonArrivedMall请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场编码
        :type MallId: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        """
        self._MallId = None
        self._PersonId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def MallId(self):
        """卖场编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def StartTime(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._PersonId = params.get("PersonId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonArrivedMallResponse(AbstractModel):
    """DescribePersonArrivedMall返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场系统编码
        :type MallId: str
        :param _MallCode: 卖场用户编码
        :type MallCode: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _ArrivedMallSet: 到场轨迹
        :type ArrivedMallSet: list of ArrivedMallInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MallId = None
        self._MallCode = None
        self._PersonId = None
        self._ArrivedMallSet = None
        self._RequestId = None

    @property
    def MallId(self):
        """卖场系统编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def MallCode(self):
        """卖场用户编码
        :rtype: str
        """
        return self._MallCode

    @MallCode.setter
    def MallCode(self, MallCode):
        self._MallCode = MallCode

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def ArrivedMallSet(self):
        """到场轨迹
        :rtype: list of ArrivedMallInfo
        """
        return self._ArrivedMallSet

    @ArrivedMallSet.setter
    def ArrivedMallSet(self, ArrivedMallSet):
        self._ArrivedMallSet = ArrivedMallSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._MallCode = params.get("MallCode")
        self._PersonId = params.get("PersonId")
        if params.get("ArrivedMallSet") is not None:
            self._ArrivedMallSet = []
            for item in params.get("ArrivedMallSet"):
                obj = ArrivedMallInfo()
                obj._deserialize(item)
                self._ArrivedMallSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePersonInfoByFacePictureRequest(AbstractModel):
    """DescribePersonInfoByFacePicture请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param _ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :type ShopId: int
        :param _Picture: 人脸图片BASE编码
        :type Picture: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._Picture = None

    @property
    def CompanyId(self):
        """优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Picture(self):
        """人脸图片BASE编码
        :rtype: str
        """
        return self._Picture

    @Picture.setter
    def Picture(self, Picture):
        self._Picture = Picture


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._Picture = params.get("Picture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonInfoByFacePictureResponse(AbstractModel):
    """DescribePersonInfoByFacePicture返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团id
        :type CompanyId: str
        :param _ShopId: 店铺id
        :type ShopId: int
        :param _PersonId: 顾客face id
        :type PersonId: int
        :param _PictureUrl: 顾客底图url
        :type PictureUrl: str
        :param _PersonType: 顾客类型（0表示普通顾客，1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :type PersonType: int
        :param _FirstVisitTime: 顾客首次进店时间
        :type FirstVisitTime: str
        :param _VisitTimes: 顾客历史到访次数
        :type VisitTimes: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._PersonId = None
        self._PictureUrl = None
        self._PersonType = None
        self._FirstVisitTime = None
        self._VisitTimes = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团id
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺id
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def PersonId(self):
        """顾客face id
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PictureUrl(self):
        """顾客底图url
        :rtype: str
        """
        return self._PictureUrl

    @PictureUrl.setter
    def PictureUrl(self, PictureUrl):
        self._PictureUrl = PictureUrl

    @property
    def PersonType(self):
        """顾客类型（0表示普通顾客，1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :rtype: int
        """
        return self._PersonType

    @PersonType.setter
    def PersonType(self, PersonType):
        self._PersonType = PersonType

    @property
    def FirstVisitTime(self):
        """顾客首次进店时间
        :rtype: str
        """
        return self._FirstVisitTime

    @FirstVisitTime.setter
    def FirstVisitTime(self, FirstVisitTime):
        self._FirstVisitTime = FirstVisitTime

    @property
    def VisitTimes(self):
        """顾客历史到访次数
        :rtype: int
        """
        return self._VisitTimes

    @VisitTimes.setter
    def VisitTimes(self, VisitTimes):
        self._VisitTimes = VisitTimes

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._PersonId = params.get("PersonId")
        self._PictureUrl = params.get("PictureUrl")
        self._PersonType = params.get("PersonType")
        self._FirstVisitTime = params.get("FirstVisitTime")
        self._VisitTimes = params.get("VisitTimes")
        self._RequestId = params.get("RequestId")


class DescribePersonInfoRequest(AbstractModel):
    """DescribePersonInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _StartPersonId: 起始ID，第一次拉取时StartPersonId传0，后续送入的值为上一页最后一条数据项的PersonId
        :type StartPersonId: int
        :param _Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param _Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        :param _PictureExpires: 图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :type PictureExpires: int
        :param _PersonType: 身份类型(0表示普通顾客，1 白名单，2 表示黑名单）
        :type PersonType: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._StartPersonId = None
        self._Offset = None
        self._Limit = None
        self._PictureExpires = None
        self._PersonType = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def StartPersonId(self):
        """起始ID，第一次拉取时StartPersonId传0，后续送入的值为上一页最后一条数据项的PersonId
        :rtype: int
        """
        return self._StartPersonId

    @StartPersonId.setter
    def StartPersonId(self, StartPersonId):
        self._StartPersonId = StartPersonId

    @property
    def Offset(self):
        """偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit:每页的数据项，最大100，超过100会被强制指定为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def PictureExpires(self):
        """图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :rtype: int
        """
        return self._PictureExpires

    @PictureExpires.setter
    def PictureExpires(self, PictureExpires):
        self._PictureExpires = PictureExpires

    @property
    def PersonType(self):
        """身份类型(0表示普通顾客，1 白名单，2 表示黑名单）
        :rtype: int
        """
        return self._PersonType

    @PersonType.setter
    def PersonType(self, PersonType):
        self._PersonType = PersonType


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._StartPersonId = params.get("StartPersonId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._PictureExpires = params.get("PictureExpires")
        self._PersonType = params.get("PersonType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonInfoResponse(AbstractModel):
    """DescribePersonInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _PersonInfoSet: 用户信息
        :type PersonInfoSet: list of PersonInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._TotalCount = None
        self._PersonInfoSet = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PersonInfoSet(self):
        """用户信息
        :rtype: list of PersonInfo
        """
        return self._PersonInfoSet

    @PersonInfoSet.setter
    def PersonInfoSet(self, PersonInfoSet):
        self._PersonInfoSet = PersonInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._TotalCount = params.get("TotalCount")
        if params.get("PersonInfoSet") is not None:
            self._PersonInfoSet = []
            for item in params.get("PersonInfoSet"):
                obj = PersonInfo()
                obj._deserialize(item)
                self._PersonInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePersonRequest(AbstractModel):
    """DescribePerson请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场编码
        :type MallId: str
        :param _Offset: 查询偏移
        :type Offset: int
        :param _Limit: 查询数量，默认20，最大查询数量100
        :type Limit: int
        """
        self._MallId = None
        self._Offset = None
        self._Limit = None

    @property
    def MallId(self):
        """卖场编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def Offset(self):
        """查询偏移
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询数量，默认20，最大查询数量100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonResponse(AbstractModel):
    """DescribePerson返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总计客户数量
        :type TotalCount: int
        :param _PersonSet: 客户信息
        :type PersonSet: list of PersonProfile
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PersonSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总计客户数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PersonSet(self):
        """客户信息
        :rtype: list of PersonProfile
        """
        return self._PersonSet

    @PersonSet.setter
    def PersonSet(self, PersonSet):
        self._PersonSet = PersonSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self._PersonSet = []
            for item in params.get("PersonSet"):
                obj = PersonProfile()
                obj._deserialize(item)
                self._PersonSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePersonTraceDetailRequest(AbstractModel):
    """DescribePersonTraceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场编码
        :type MallId: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _TraceId: 轨迹编码
        :type TraceId: str
        """
        self._MallId = None
        self._PersonId = None
        self._TraceId = None

    @property
    def MallId(self):
        """卖场编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def TraceId(self):
        """轨迹编码
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._PersonId = params.get("PersonId")
        self._TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonTraceDetailResponse(AbstractModel):
    """DescribePersonTraceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场编码
        :type MallId: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _TraceId: 轨迹编码
        :type TraceId: str
        :param _CoordinateSet: 轨迹点坐标序列
        :type CoordinateSet: list of PersonCoordinate
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MallId = None
        self._PersonId = None
        self._TraceId = None
        self._CoordinateSet = None
        self._RequestId = None

    @property
    def MallId(self):
        """卖场编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def TraceId(self):
        """轨迹编码
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def CoordinateSet(self):
        """轨迹点坐标序列
        :rtype: list of PersonCoordinate
        """
        return self._CoordinateSet

    @CoordinateSet.setter
    def CoordinateSet(self, CoordinateSet):
        self._CoordinateSet = CoordinateSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._PersonId = params.get("PersonId")
        self._TraceId = params.get("TraceId")
        if params.get("CoordinateSet") is not None:
            self._CoordinateSet = []
            for item in params.get("CoordinateSet"):
                obj = PersonCoordinate()
                obj._deserialize(item)
                self._CoordinateSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePersonTraceRequest(AbstractModel):
    """DescribePersonTrace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场编码
        :type MallId: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _StartTime: 查询开始时间
        :type StartTime: str
        :param _EndTime: 查询结束时间
        :type EndTime: str
        """
        self._MallId = None
        self._PersonId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def MallId(self):
        """卖场编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def StartTime(self):
        """查询开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._PersonId = params.get("PersonId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonTraceResponse(AbstractModel):
    """DescribePersonTrace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MallId: 卖场系统编码
        :type MallId: str
        :param _MallCode: 卖场用户编码
        :type MallCode: str
        :param _PersonId: 客户编码
        :type PersonId: str
        :param _TraceRouteSet: 轨迹列表
        :type TraceRouteSet: list of PersonTraceRoute
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MallId = None
        self._MallCode = None
        self._PersonId = None
        self._TraceRouteSet = None
        self._RequestId = None

    @property
    def MallId(self):
        """卖场系统编码
        :rtype: str
        """
        return self._MallId

    @MallId.setter
    def MallId(self, MallId):
        self._MallId = MallId

    @property
    def MallCode(self):
        """卖场用户编码
        :rtype: str
        """
        return self._MallCode

    @MallCode.setter
    def MallCode(self, MallCode):
        self._MallCode = MallCode

    @property
    def PersonId(self):
        """客户编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def TraceRouteSet(self):
        """轨迹列表
        :rtype: list of PersonTraceRoute
        """
        return self._TraceRouteSet

    @TraceRouteSet.setter
    def TraceRouteSet(self, TraceRouteSet):
        self._TraceRouteSet = TraceRouteSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MallId = params.get("MallId")
        self._MallCode = params.get("MallCode")
        self._PersonId = params.get("PersonId")
        if params.get("TraceRouteSet") is not None:
            self._TraceRouteSet = []
            for item in params.get("TraceRouteSet"):
                obj = PersonTraceRoute()
                obj._deserialize(item)
                self._TraceRouteSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePersonVisitInfoRequest(AbstractModel):
    """DescribePersonVisitInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param _Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd，已废弃，请使用StartDateTime
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd，已废弃，请使用EndDateTime
        :type EndDate: str
        :param _PictureExpires: 图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :type PictureExpires: int
        :param _StartDateTime: 开始时间，格式yyyy-MM-dd HH:mm:ss
        :type StartDateTime: str
        :param _EndDateTime: 结束时间，格式yyyy-MM-dd HH:mm:ss
        :type EndDateTime: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._Offset = None
        self._Limit = None
        self._StartDate = None
        self._EndDate = None
        self._PictureExpires = None
        self._StartDateTime = None
        self._EndDateTime = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Offset(self):
        """偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit:每页的数据项，最大100，超过100会被强制指定为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd，已废弃，请使用StartDateTime
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd，已废弃，请使用EndDateTime
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def PictureExpires(self):
        """图片url过期时间：在当前时间+PictureExpires秒后，图片url无法继续正常访问；单位s；默认值1*24*60*60（1天）
        :rtype: int
        """
        return self._PictureExpires

    @PictureExpires.setter
    def PictureExpires(self, PictureExpires):
        self._PictureExpires = PictureExpires

    @property
    def StartDateTime(self):
        """开始时间，格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._StartDateTime

    @StartDateTime.setter
    def StartDateTime(self, StartDateTime):
        self._StartDateTime = StartDateTime

    @property
    def EndDateTime(self):
        """结束时间，格式yyyy-MM-dd HH:mm:ss
        :rtype: str
        """
        return self._EndDateTime

    @EndDateTime.setter
    def EndDateTime(self, EndDateTime):
        self._EndDateTime = EndDateTime


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._PictureExpires = params.get("PictureExpires")
        self._StartDateTime = params.get("StartDateTime")
        self._EndDateTime = params.get("EndDateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonVisitInfoResponse(AbstractModel):
    """DescribePersonVisitInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _PersonVisitInfoSet: 用户到访明细
        :type PersonVisitInfoSet: list of PersonVisitInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._TotalCount = None
        self._PersonVisitInfoSet = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PersonVisitInfoSet(self):
        """用户到访明细
        :rtype: list of PersonVisitInfo
        """
        return self._PersonVisitInfoSet

    @PersonVisitInfoSet.setter
    def PersonVisitInfoSet(self, PersonVisitInfoSet):
        self._PersonVisitInfoSet = PersonVisitInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._TotalCount = params.get("TotalCount")
        if params.get("PersonVisitInfoSet") is not None:
            self._PersonVisitInfoSet = []
            for item in params.get("PersonVisitInfoSet"):
                obj = PersonVisitInfo()
                obj._deserialize(item)
                self._PersonVisitInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShopHourTrafficInfoRequest(AbstractModel):
    """DescribeShopHourTrafficInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _StartDate: 开始日期，格式：yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式：yyyy-MM-dd
        :type EndDate: str
        :param _Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param _Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._StartDate = None
        self._EndDate = None
        self._Offset = None
        self._Limit = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def StartDate(self):
        """开始日期，格式：yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式：yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Offset(self):
        """偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit:每页的数据项，最大100，超过100会被强制指定为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShopHourTrafficInfoResponse(AbstractModel):
    """DescribeShopHourTrafficInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _TotalCount: 查询结果总数
        :type TotalCount: int
        :param _ShopHourTrafficInfoSet: 分时客流信息
        :type ShopHourTrafficInfoSet: list of ShopHourTrafficInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._TotalCount = None
        self._ShopHourTrafficInfoSet = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def TotalCount(self):
        """查询结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ShopHourTrafficInfoSet(self):
        """分时客流信息
        :rtype: list of ShopHourTrafficInfo
        """
        return self._ShopHourTrafficInfoSet

    @ShopHourTrafficInfoSet.setter
    def ShopHourTrafficInfoSet(self, ShopHourTrafficInfoSet):
        self._ShopHourTrafficInfoSet = ShopHourTrafficInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._TotalCount = params.get("TotalCount")
        if params.get("ShopHourTrafficInfoSet") is not None:
            self._ShopHourTrafficInfoSet = []
            for item in params.get("ShopHourTrafficInfoSet"):
                obj = ShopHourTrafficInfo()
                obj._deserialize(item)
                self._ShopHourTrafficInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShopInfoRequest(AbstractModel):
    """DescribeShopInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param _Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit:每页的数据项，最大100，超过100会被强制指定为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShopInfoResponse(AbstractModel):
    """DescribeShopInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 门店总数
        :type TotalCount: int
        :param _ShopInfoSet: 门店列表信息
        :type ShopInfoSet: list of ShopInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ShopInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """门店总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ShopInfoSet(self):
        """门店列表信息
        :rtype: list of ShopInfo
        """
        return self._ShopInfoSet

    @ShopInfoSet.setter
    def ShopInfoSet(self, ShopInfoSet):
        self._ShopInfoSet = ShopInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ShopInfoSet") is not None:
            self._ShopInfoSet = []
            for item in params.get("ShopInfoSet"):
                obj = ShopInfo()
                obj._deserialize(item)
                self._ShopInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShopTrafficInfoRequest(AbstractModel):
    """DescribeShopTrafficInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 介绍日期，格式yyyy-MM-dd
        :type EndDate: str
        :param _Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param _Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._StartDate = None
        self._EndDate = None
        self._Offset = None
        self._Limit = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """介绍日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Offset(self):
        """偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit:每页的数据项，最大100，超过100会被强制指定为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShopTrafficInfoResponse(AbstractModel):
    """DescribeShopTrafficInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _TotalCount: 查询结果总数
        :type TotalCount: int
        :param _ShopDayTrafficInfoSet: 客流信息列表
        :type ShopDayTrafficInfoSet: list of ShopDayTrafficInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._TotalCount = None
        self._ShopDayTrafficInfoSet = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def TotalCount(self):
        """查询结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ShopDayTrafficInfoSet(self):
        """客流信息列表
        :rtype: list of ShopDayTrafficInfo
        """
        return self._ShopDayTrafficInfoSet

    @ShopDayTrafficInfoSet.setter
    def ShopDayTrafficInfoSet(self, ShopDayTrafficInfoSet):
        self._ShopDayTrafficInfoSet = ShopDayTrafficInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._TotalCount = params.get("TotalCount")
        if params.get("ShopDayTrafficInfoSet") is not None:
            self._ShopDayTrafficInfoSet = []
            for item in params.get("ShopDayTrafficInfoSet"):
                obj = ShopDayTrafficInfo()
                obj._deserialize(item)
                self._ShopDayTrafficInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrajectoryDataRequest(AbstractModel):
    """DescribeTrajectoryData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param _Limit: 限制返回数据的最大条数，最大 400（负数代为 400）
        :type Limit: int
        :param _Gender: 顾客性别顾虑，0是男，1是女，其它代表不分性别
        :type Gender: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._StartDate = None
        self._EndDate = None
        self._Limit = None
        self._Gender = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Limit(self):
        """限制返回数据的最大条数，最大 400（负数代为 400）
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Gender(self):
        """顾客性别顾虑，0是男，1是女，其它代表不分性别
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Limit = params.get("Limit")
        self._Gender = params.get("Gender")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrajectoryDataResponse(AbstractModel):
    """DescribeTrajectoryData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _TotalPerson: 总人数
        :type TotalPerson: int
        :param _TotalTrajectory: 总动迹数目
        :type TotalTrajectory: int
        :param _Person: 返回动迹中的总人数
        :type Person: int
        :param _Trajectory: 返回动迹的数目
        :type Trajectory: int
        :param _Data: 返回动迹的具体信息
        :type Data: list of TrajectorySunData
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._TotalPerson = None
        self._TotalTrajectory = None
        self._Person = None
        self._Trajectory = None
        self._Data = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def TotalPerson(self):
        """总人数
        :rtype: int
        """
        return self._TotalPerson

    @TotalPerson.setter
    def TotalPerson(self, TotalPerson):
        self._TotalPerson = TotalPerson

    @property
    def TotalTrajectory(self):
        """总动迹数目
        :rtype: int
        """
        return self._TotalTrajectory

    @TotalTrajectory.setter
    def TotalTrajectory(self, TotalTrajectory):
        self._TotalTrajectory = TotalTrajectory

    @property
    def Person(self):
        """返回动迹中的总人数
        :rtype: int
        """
        return self._Person

    @Person.setter
    def Person(self, Person):
        self._Person = Person

    @property
    def Trajectory(self):
        """返回动迹的数目
        :rtype: int
        """
        return self._Trajectory

    @Trajectory.setter
    def Trajectory(self, Trajectory):
        self._Trajectory = Trajectory

    @property
    def Data(self):
        """返回动迹的具体信息
        :rtype: list of TrajectorySunData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._TotalPerson = params.get("TotalPerson")
        self._TotalTrajectory = params.get("TotalTrajectory")
        self._Person = params.get("Person")
        self._Trajectory = params.get("Trajectory")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TrajectorySunData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneFlowAgeInfoByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowAgeInfoByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowAgeInfoByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowAgeInfoByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _ZoneName: 区域名称
        :type ZoneName: str
        :param _Data: 当前年龄段占比
        :type Data: list of float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._ZoneName = None
        self._Data = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """区域名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Data(self):
        """当前年龄段占比
        :rtype: list of float
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeZoneFlowAndStayTimeRequest(AbstractModel):
    """DescribeZoneFlowAndStayTime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowAndStayTimeResponse(AbstractModel):
    """DescribeZoneFlowAndStayTime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团id
        :type CompanyId: str
        :param _ShopId: 店铺id
        :type ShopId: int
        :param _Data: 各区域人流数目和停留时长
        :type Data: list of ZoneFlowAndAvrStayTime
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._Data = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团id
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺id
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Data(self):
        """各区域人流数目和停留时长
        :rtype: list of ZoneFlowAndAvrStayTime
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ZoneFlowAndAvrStayTime()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneFlowDailyByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowDailyByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowDailyByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowDailyByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团id
        :type CompanyId: str
        :param _ShopId: 店铺id
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _ZoneName: 区域名称
        :type ZoneName: str
        :param _Data: 每日人流量
        :type Data: list of ZoneDayFlow
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._ZoneName = None
        self._Data = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团id
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺id
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """区域名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Data(self):
        """每日人流量
        :rtype: list of ZoneDayFlow
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ZoneDayFlow()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneFlowGenderAvrStayTimeByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowGenderAvrStayTimeByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowGenderAvrStayTimeByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _ZoneName: 区域名称
        :type ZoneName: str
        :param _Data: 不同年龄段男女停留时间（返回格式为数组，从第 1 个到最后一个数据，年龄段分别为 0-17，18 - 23,  24 - 30, 31 - 40, 41 - 50, 51 - 60, 61 - 100）
        :type Data: list of ZoneAgeGroupAvrStayTime
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._ZoneName = None
        self._Data = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """区域名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Data(self):
        """不同年龄段男女停留时间（返回格式为数组，从第 1 个到最后一个数据，年龄段分别为 0-17，18 - 23,  24 - 30, 31 - 40, 41 - 50, 51 - 60, 61 - 100）
        :rtype: list of ZoneAgeGroupAvrStayTime
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ZoneAgeGroupAvrStayTime()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneFlowGenderInfoByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowGenderInfoByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowGenderInfoByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowGenderInfoByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _ZoneName: 区域名称
        :type ZoneName: str
        :param _MalePercent: 男性占比
        :type MalePercent: float
        :param _FemalePercent: 女性占比
        :type FemalePercent: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._ZoneName = None
        self._MalePercent = None
        self._FemalePercent = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """区域名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def MalePercent(self):
        """男性占比
        :rtype: float
        """
        return self._MalePercent

    @MalePercent.setter
    def MalePercent(self, MalePercent):
        self._MalePercent = MalePercent

    @property
    def FemalePercent(self):
        """女性占比
        :rtype: float
        """
        return self._FemalePercent

    @FemalePercent.setter
    def FemalePercent(self, FemalePercent):
        self._FemalePercent = FemalePercent

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._MalePercent = params.get("MalePercent")
        self._FemalePercent = params.get("FemalePercent")
        self._RequestId = params.get("RequestId")


class DescribeZoneFlowHourlyByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowHourlyByZoneId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._StartDate = None
        self._EndDate = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneFlowHourlyByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowHourlyByZoneId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _ZoneName: 区域名称
        :type ZoneName: str
        :param _Data: 各个分时人流量
        :type Data: list of ZoneHourFlow
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ZoneId = None
        self._ZoneName = None
        self._Data = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """区域名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Data(self):
        """各个分时人流量
        :rtype: list of ZoneHourFlow
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ZoneHourFlow()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeZoneTrafficInfoRequest(AbstractModel):
    """DescribeZoneTrafficInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 店铺ID
        :type ShopId: int
        :param _StartDate: 开始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param _EndDate: 结束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param _Offset: 偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :type Offset: int
        :param _Limit: Limit:每页的数据项，最大100，超过100会被强制指定为100
        :type Limit: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._StartDate = None
        self._EndDate = None
        self._Offset = None
        self._Limit = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def StartDate(self):
        """开始日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """结束日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Offset(self):
        """偏移量：分页控制参数，第一页传0，第n页Offset=(n-1)*Limit
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Limit:每页的数据项，最大100，超过100会被强制指定为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneTrafficInfoResponse(AbstractModel):
    """DescribeZoneTrafficInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _TotalCount: 查询结果总数
        :type TotalCount: int
        :param _ZoneTrafficInfoSet: 区域客流信息列表
        :type ZoneTrafficInfoSet: list of ZoneTrafficInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._TotalCount = None
        self._ZoneTrafficInfoSet = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def TotalCount(self):
        """查询结果总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ZoneTrafficInfoSet(self):
        """区域客流信息列表
        :rtype: list of ZoneTrafficInfo
        """
        return self._ZoneTrafficInfoSet

    @ZoneTrafficInfoSet.setter
    def ZoneTrafficInfoSet(self, ZoneTrafficInfoSet):
        self._ZoneTrafficInfoSet = ZoneTrafficInfoSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._TotalCount = params.get("TotalCount")
        if params.get("ZoneTrafficInfoSet") is not None:
            self._ZoneTrafficInfoSet = []
            for item in params.get("ZoneTrafficInfoSet"):
                obj = ZoneTrafficInfo()
                obj._deserialize(item)
                self._ZoneTrafficInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class GenderAgeTrafficDetail(AbstractModel):
    """性别年龄分组下的客流信息

    """

    def __init__(self):
        r"""
        :param _Gender: 性别: 0男1女
        :type Gender: int
        :param _AgeGap: 年龄区间，枚举值：0-17、18-23、24-30、31-40、41-50、51-60、>60
        :type AgeGap: str
        :param _TrafficCount: 客流量
        :type TrafficCount: int
        """
        self._Gender = None
        self._AgeGap = None
        self._TrafficCount = None

    @property
    def Gender(self):
        """性别: 0男1女
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def AgeGap(self):
        """年龄区间，枚举值：0-17、18-23、24-30、31-40、41-50、51-60、>60
        :rtype: str
        """
        return self._AgeGap

    @AgeGap.setter
    def AgeGap(self, AgeGap):
        self._AgeGap = AgeGap

    @property
    def TrafficCount(self):
        """客流量
        :rtype: int
        """
        return self._TrafficCount

    @TrafficCount.setter
    def TrafficCount(self, TrafficCount):
        self._TrafficCount = TrafficCount


    def _deserialize(self, params):
        self._Gender = params.get("Gender")
        self._AgeGap = params.get("AgeGap")
        self._TrafficCount = params.get("TrafficCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HourTrafficInfoDetail(AbstractModel):
    """分时客流量详细信息

    """

    def __init__(self):
        r"""
        :param _Hour: 小时 取值为：0，1，2，3，4，5，6，7，8，9，10，11，12，13，14，15，16，17，18，19，20，21，22，23
        :type Hour: int
        :param _HourTrafficTotalCount: 分时客流量
        :type HourTrafficTotalCount: int
        """
        self._Hour = None
        self._HourTrafficTotalCount = None

    @property
    def Hour(self):
        """小时 取值为：0，1，2，3，4，5，6，7，8，9，10，11，12，13，14，15，16，17，18，19，20，21，22，23
        :rtype: int
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def HourTrafficTotalCount(self):
        """分时客流量
        :rtype: int
        """
        return self._HourTrafficTotalCount

    @HourTrafficTotalCount.setter
    def HourTrafficTotalCount(self, HourTrafficTotalCount):
        self._HourTrafficTotalCount = HourTrafficTotalCount


    def _deserialize(self, params):
        self._Hour = params.get("Hour")
        self._HourTrafficTotalCount = params.get("HourTrafficTotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonFeatureInfoRequest(AbstractModel):
    """ModifyPersonFeatureInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _PersonId: 需要修改的顾客id
        :type PersonId: int
        :param _Picture: 图片BASE编码
        :type Picture: str
        :param _PictureName: 图片名称（尽量不要重复）
        :type PictureName: str
        :param _PersonType: 人物类型，仅能操作黑白名单顾客（1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :type PersonType: int
        :param _ShopId: 店铺ID，如果不填表示操作集团身份库
        :type ShopId: int
        """
        self._CompanyId = None
        self._PersonId = None
        self._Picture = None
        self._PictureName = None
        self._PersonType = None
        self._ShopId = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def PersonId(self):
        """需要修改的顾客id
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Picture(self):
        """图片BASE编码
        :rtype: str
        """
        return self._Picture

    @Picture.setter
    def Picture(self, Picture):
        self._Picture = Picture

    @property
    def PictureName(self):
        """图片名称（尽量不要重复）
        :rtype: str
        """
        return self._PictureName

    @PictureName.setter
    def PictureName(self, PictureName):
        self._PictureName = PictureName

    @property
    def PersonType(self):
        """人物类型，仅能操作黑白名单顾客（1 白名单，2 表示黑名单，101表示集团白名单，102表示集团黑名单）
        :rtype: int
        """
        return self._PersonType

    @PersonType.setter
    def PersonType(self, PersonType):
        self._PersonType = PersonType

    @property
    def ShopId(self):
        """店铺ID，如果不填表示操作集团身份库
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._PersonId = params.get("PersonId")
        self._Picture = params.get("Picture")
        self._PictureName = params.get("PictureName")
        self._PersonType = params.get("PersonType")
        self._ShopId = params.get("ShopId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonFeatureInfoResponse(AbstractModel):
    """ModifyPersonFeatureInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 店铺ID，如果不填表示操作集团身份库
        :type ShopId: int
        :param _PersonId: 请求的顾客id
        :type PersonId: int
        :param _PersonIdBind: 图片实际绑定person_id，可能与请求的person_id不同，以此id为准
        :type PersonIdBind: int
        :param _PersonType: 请求的顾客类型
        :type PersonType: int
        :param _SimilarPersonIds: 与请求的person_id类型相同、与请求图片特征相似的一个或多个person_id，需要额外确认这些id是否是同一个人
        :type SimilarPersonIds: list of int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._PersonId = None
        self._PersonIdBind = None
        self._PersonType = None
        self._SimilarPersonIds = None
        self._RequestId = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺ID，如果不填表示操作集团身份库
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def PersonId(self):
        """请求的顾客id
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonIdBind(self):
        """图片实际绑定person_id，可能与请求的person_id不同，以此id为准
        :rtype: int
        """
        return self._PersonIdBind

    @PersonIdBind.setter
    def PersonIdBind(self, PersonIdBind):
        self._PersonIdBind = PersonIdBind

    @property
    def PersonType(self):
        """请求的顾客类型
        :rtype: int
        """
        return self._PersonType

    @PersonType.setter
    def PersonType(self, PersonType):
        self._PersonType = PersonType

    @property
    def SimilarPersonIds(self):
        """与请求的person_id类型相同、与请求图片特征相似的一个或多个person_id，需要额外确认这些id是否是同一个人
        :rtype: list of int
        """
        return self._SimilarPersonIds

    @SimilarPersonIds.setter
    def SimilarPersonIds(self, SimilarPersonIds):
        self._SimilarPersonIds = SimilarPersonIds

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._PersonId = params.get("PersonId")
        self._PersonIdBind = params.get("PersonIdBind")
        self._PersonType = params.get("PersonType")
        self._SimilarPersonIds = params.get("SimilarPersonIds")
        self._RequestId = params.get("RequestId")


class ModifyPersonTagInfoRequest(AbstractModel):
    """ModifyPersonTagInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param _ShopId: 优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，为0则拉取集团全部店铺当前
        :type ShopId: int
        :param _Tags: 需要设置的顾客信息，批量设置最大为10个
        :type Tags: list of PersonTagInfo
        """
        self._CompanyId = None
        self._ShopId = None
        self._Tags = None

    @property
    def CompanyId(self):
        """优mall集团id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """优mall店铺id，通过"指定身份标识获取客户门店列表"接口获取，为0则拉取集团全部店铺当前
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Tags(self):
        """需要设置的顾客信息，批量设置最大为10个
        :rtype: list of PersonTagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = PersonTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonTagInfoResponse(AbstractModel):
    """ModifyPersonTagInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPersonTypeRequest(AbstractModel):
    """ModifyPersonType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _PersonId: 顾客ID
        :type PersonId: int
        :param _PersonType: 身份类型(0表示普通顾客，1 白名单，2 表示黑名单）
        :type PersonType: int
        :param _PersonSubType: 身份子类型:
PersonType=0时(普通顾客)，0普通顾客
PersonType=1时(白名单)，0店员，1商场人员，2其他类型人员，3区域经理，4注册会员，5VIP用户
PersonType=2时(黑名单)，0普通黑名单，1小偷)
        :type PersonSubType: int
        """
        self._CompanyId = None
        self._ShopId = None
        self._PersonId = None
        self._PersonType = None
        self._PersonSubType = None

    @property
    def CompanyId(self):
        """集团ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def PersonId(self):
        """顾客ID
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonType(self):
        """身份类型(0表示普通顾客，1 白名单，2 表示黑名单）
        :rtype: int
        """
        return self._PersonType

    @PersonType.setter
    def PersonType(self, PersonType):
        self._PersonType = PersonType

    @property
    def PersonSubType(self):
        """身份子类型:
PersonType=0时(普通顾客)，0普通顾客
PersonType=1时(白名单)，0店员，1商场人员，2其他类型人员，3区域经理，4注册会员，5VIP用户
PersonType=2时(黑名单)，0普通黑名单，1小偷)
        :rtype: int
        """
        return self._PersonSubType

    @PersonSubType.setter
    def PersonSubType(self, PersonSubType):
        self._PersonSubType = PersonSubType


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._PersonId = params.get("PersonId")
        self._PersonType = params.get("PersonType")
        self._PersonSubType = params.get("PersonSubType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonTypeResponse(AbstractModel):
    """ModifyPersonType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NetworkAndShopInfo(AbstractModel):
    """网络状态

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团id
        :type CompanyId: str
        :param _ShopId: 店铺id
        :type ShopId: int
        :param _Province: 店铺省份
        :type Province: str
        :param _City: 店铺城市
        :type City: str
        :param _ShopName: 店铺名
        :type ShopName: str
        :param _Upload: 上传带宽，单位Mb/s，-1：未知
        :type Upload: float
        :param _Download: 下载带宽，单位Mb/s，-1：未知
        :type Download: float
        :param _MinRtt: 最小延迟，单位ms，-1：未知
        :type MinRtt: float
        :param _AvgRtt: 平均延迟，单位ms，-1：未知
        :type AvgRtt: float
        :param _MaxRtt: 最大延迟，单位ms，-1：未知
        :type MaxRtt: float
        :param _MdevRtt: 平均偏差延迟，单位ms，-1：未知
        :type MdevRtt: float
        :param _Loss: 丢包率百分比，-1：未知
        :type Loss: float
        :param _UpdateTime: 更新时间戳
        :type UpdateTime: int
        :param _Mac: 上报网络状态设备
        :type Mac: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._Province = None
        self._City = None
        self._ShopName = None
        self._Upload = None
        self._Download = None
        self._MinRtt = None
        self._AvgRtt = None
        self._MaxRtt = None
        self._MdevRtt = None
        self._Loss = None
        self._UpdateTime = None
        self._Mac = None

    @property
    def CompanyId(self):
        """集团id
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺id
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Province(self):
        """店铺省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """店铺城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def ShopName(self):
        """店铺名
        :rtype: str
        """
        return self._ShopName

    @ShopName.setter
    def ShopName(self, ShopName):
        self._ShopName = ShopName

    @property
    def Upload(self):
        """上传带宽，单位Mb/s，-1：未知
        :rtype: float
        """
        return self._Upload

    @Upload.setter
    def Upload(self, Upload):
        self._Upload = Upload

    @property
    def Download(self):
        """下载带宽，单位Mb/s，-1：未知
        :rtype: float
        """
        return self._Download

    @Download.setter
    def Download(self, Download):
        self._Download = Download

    @property
    def MinRtt(self):
        """最小延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._MinRtt

    @MinRtt.setter
    def MinRtt(self, MinRtt):
        self._MinRtt = MinRtt

    @property
    def AvgRtt(self):
        """平均延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._AvgRtt

    @AvgRtt.setter
    def AvgRtt(self, AvgRtt):
        self._AvgRtt = AvgRtt

    @property
    def MaxRtt(self):
        """最大延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._MaxRtt

    @MaxRtt.setter
    def MaxRtt(self, MaxRtt):
        self._MaxRtt = MaxRtt

    @property
    def MdevRtt(self):
        """平均偏差延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._MdevRtt

    @MdevRtt.setter
    def MdevRtt(self, MdevRtt):
        self._MdevRtt = MdevRtt

    @property
    def Loss(self):
        """丢包率百分比，-1：未知
        :rtype: float
        """
        return self._Loss

    @Loss.setter
    def Loss(self, Loss):
        self._Loss = Loss

    @property
    def UpdateTime(self):
        """更新时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Mac(self):
        """上报网络状态设备
        :rtype: str
        """
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._ShopName = params.get("ShopName")
        self._Upload = params.get("Upload")
        self._Download = params.get("Download")
        self._MinRtt = params.get("MinRtt")
        self._AvgRtt = params.get("AvgRtt")
        self._MaxRtt = params.get("MaxRtt")
        self._MdevRtt = params.get("MdevRtt")
        self._Loss = params.get("Loss")
        self._UpdateTime = params.get("UpdateTime")
        self._Mac = params.get("Mac")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkHistoryInfo(AbstractModel):
    """查询网络状态历史数据输出

    """

    def __init__(self):
        r"""
        :param _Count: 总数
        :type Count: int
        :param _CompanyId: 集团id
        :type CompanyId: str
        :param _ShopId: 店铺id
        :type ShopId: int
        :param _Province: 店铺省份
        :type Province: str
        :param _City: 店铺城市
        :type City: str
        :param _ShopName: 店铺名称
        :type ShopName: str
        :param _Infos: 网络信息
        :type Infos: list of NetworkInfo
        """
        self._Count = None
        self._CompanyId = None
        self._ShopId = None
        self._Province = None
        self._City = None
        self._ShopName = None
        self._Infos = None

    @property
    def Count(self):
        """总数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CompanyId(self):
        """集团id
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """店铺id
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Province(self):
        """店铺省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """店铺城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def ShopName(self):
        """店铺名称
        :rtype: str
        """
        return self._ShopName

    @ShopName.setter
    def ShopName(self, ShopName):
        self._ShopName = ShopName

    @property
    def Infos(self):
        """网络信息
        :rtype: list of NetworkInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._ShopName = params.get("ShopName")
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = NetworkInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInfo(AbstractModel):
    """没有店铺信息的网络状态

    """

    def __init__(self):
        r"""
        :param _Upload: 上传带宽，单位Mb/s，-1：未知
        :type Upload: float
        :param _Download: 下载带宽，单位Mb/s，-1：未知
        :type Download: float
        :param _MinRtt: 最小延迟，单位ms，-1：未知
        :type MinRtt: float
        :param _AvgRtt: 平均延迟，单位ms，-1：未知
        :type AvgRtt: float
        :param _MaxRtt: 最大延迟，单位ms，-1：未知
        :type MaxRtt: float
        :param _MdevRtt: 平均偏差延迟，单位ms，-1：未知
        :type MdevRtt: float
        :param _Loss: 丢包率百分比，-1：未知
        :type Loss: float
        :param _UpdateTime: 更新时间戳
        :type UpdateTime: int
        :param _Mac: 上报网络状态设备
        :type Mac: str
        """
        self._Upload = None
        self._Download = None
        self._MinRtt = None
        self._AvgRtt = None
        self._MaxRtt = None
        self._MdevRtt = None
        self._Loss = None
        self._UpdateTime = None
        self._Mac = None

    @property
    def Upload(self):
        """上传带宽，单位Mb/s，-1：未知
        :rtype: float
        """
        return self._Upload

    @Upload.setter
    def Upload(self, Upload):
        self._Upload = Upload

    @property
    def Download(self):
        """下载带宽，单位Mb/s，-1：未知
        :rtype: float
        """
        return self._Download

    @Download.setter
    def Download(self, Download):
        self._Download = Download

    @property
    def MinRtt(self):
        """最小延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._MinRtt

    @MinRtt.setter
    def MinRtt(self, MinRtt):
        self._MinRtt = MinRtt

    @property
    def AvgRtt(self):
        """平均延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._AvgRtt

    @AvgRtt.setter
    def AvgRtt(self, AvgRtt):
        self._AvgRtt = AvgRtt

    @property
    def MaxRtt(self):
        """最大延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._MaxRtt

    @MaxRtt.setter
    def MaxRtt(self, MaxRtt):
        self._MaxRtt = MaxRtt

    @property
    def MdevRtt(self):
        """平均偏差延迟，单位ms，-1：未知
        :rtype: float
        """
        return self._MdevRtt

    @MdevRtt.setter
    def MdevRtt(self, MdevRtt):
        self._MdevRtt = MdevRtt

    @property
    def Loss(self):
        """丢包率百分比，-1：未知
        :rtype: float
        """
        return self._Loss

    @Loss.setter
    def Loss(self, Loss):
        self._Loss = Loss

    @property
    def UpdateTime(self):
        """更新时间戳
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Mac(self):
        """上报网络状态设备
        :rtype: str
        """
        return self._Mac

    @Mac.setter
    def Mac(self, Mac):
        self._Mac = Mac


    def _deserialize(self, params):
        self._Upload = params.get("Upload")
        self._Download = params.get("Download")
        self._MinRtt = params.get("MinRtt")
        self._AvgRtt = params.get("AvgRtt")
        self._MaxRtt = params.get("MaxRtt")
        self._MdevRtt = params.get("MdevRtt")
        self._Loss = params.get("Loss")
        self._UpdateTime = params.get("UpdateTime")
        self._Mac = params.get("Mac")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkLastInfo(AbstractModel):
    """获取当前门店最新网络状态数据返回结构

    """

    def __init__(self):
        r"""
        :param _Count: 总数
        :type Count: int
        :param _Infos: 网络状态
        :type Infos: list of NetworkAndShopInfo
        """
        self._Count = None
        self._Infos = None

    @property
    def Count(self):
        """总数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Infos(self):
        """网络状态
        :rtype: list of NetworkAndShopInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = NetworkAndShopInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonCoordinate(AbstractModel):
    """轨迹点坐标

    """

    def __init__(self):
        r"""
        :param _CADX: CAD图X坐标
        :type CADX: float
        :param _CADY: CAD图Y坐标
        :type CADY: float
        :param _CapTime: 抓拍时间点
        :type CapTime: str
        :param _CapPic: 抓拍图片
        :type CapPic: str
        :param _MallAreaType: 卖场区域类型
        :type MallAreaType: int
        :param _PosId: 坐标编号
        :type PosId: int
        :param _ShopId: 门店编号
        :type ShopId: int
        :param _Event: 事件
        :type Event: str
        """
        self._CADX = None
        self._CADY = None
        self._CapTime = None
        self._CapPic = None
        self._MallAreaType = None
        self._PosId = None
        self._ShopId = None
        self._Event = None

    @property
    def CADX(self):
        """CAD图X坐标
        :rtype: float
        """
        return self._CADX

    @CADX.setter
    def CADX(self, CADX):
        self._CADX = CADX

    @property
    def CADY(self):
        """CAD图Y坐标
        :rtype: float
        """
        return self._CADY

    @CADY.setter
    def CADY(self, CADY):
        self._CADY = CADY

    @property
    def CapTime(self):
        """抓拍时间点
        :rtype: str
        """
        return self._CapTime

    @CapTime.setter
    def CapTime(self, CapTime):
        self._CapTime = CapTime

    @property
    def CapPic(self):
        """抓拍图片
        :rtype: str
        """
        return self._CapPic

    @CapPic.setter
    def CapPic(self, CapPic):
        self._CapPic = CapPic

    @property
    def MallAreaType(self):
        """卖场区域类型
        :rtype: int
        """
        return self._MallAreaType

    @MallAreaType.setter
    def MallAreaType(self, MallAreaType):
        self._MallAreaType = MallAreaType

    @property
    def PosId(self):
        """坐标编号
        :rtype: int
        """
        return self._PosId

    @PosId.setter
    def PosId(self, PosId):
        self._PosId = PosId

    @property
    def ShopId(self):
        """门店编号
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def Event(self):
        """事件
        :rtype: str
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event


    def _deserialize(self, params):
        self._CADX = params.get("CADX")
        self._CADY = params.get("CADY")
        self._CapTime = params.get("CapTime")
        self._CapPic = params.get("CapPic")
        self._MallAreaType = params.get("MallAreaType")
        self._PosId = params.get("PosId")
        self._ShopId = params.get("ShopId")
        self._Event = params.get("Event")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _PersonId: 用户ID
        :type PersonId: int
        :param _PersonPicture: 人脸图片Base64内容，已弃用，返回默认空值
        :type PersonPicture: str
        :param _Gender: 性别：0男1女
        :type Gender: int
        :param _Age: 年龄
        :type Age: int
        :param _PersonType: 身份类型（0表示普通顾客，1 白名单，2 表示黑名单）
        :type PersonType: int
        :param _PersonPictureUrl: 人脸图片Url，在有效期内可以访问下载
        :type PersonPictureUrl: str
        :param _PersonSubType: 身份子类型:
PersonType=0时(普通顾客)，0普通顾客
PersonType=1时(白名单)，0店员，1商场人员，2其他类型人员，3区域经理，4注册用户，5VIP用户
PersonType=2时(黑名单)，0普通黑名单，1小偷)
        :type PersonSubType: int
        :param _VisitTimes: 到访次数，-1表示未知
        :type VisitTimes: int
        :param _VisitDays: 到访天数，-1表示未知
        :type VisitDays: int
        """
        self._PersonId = None
        self._PersonPicture = None
        self._Gender = None
        self._Age = None
        self._PersonType = None
        self._PersonPictureUrl = None
        self._PersonSubType = None
        self._VisitTimes = None
        self._VisitDays = None

    @property
    def PersonId(self):
        """用户ID
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def PersonPicture(self):
        """人脸图片Base64内容，已弃用，返回默认空值
        :rtype: str
        """
        return self._PersonPicture

    @PersonPicture.setter
    def PersonPicture(self, PersonPicture):
        self._PersonPicture = PersonPicture

    @property
    def Gender(self):
        """性别：0男1女
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        """年龄
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def PersonType(self):
        """身份类型（0表示普通顾客，1 白名单，2 表示黑名单）
        :rtype: int
        """
        return self._PersonType

    @PersonType.setter
    def PersonType(self, PersonType):
        self._PersonType = PersonType

    @property
    def PersonPictureUrl(self):
        """人脸图片Url，在有效期内可以访问下载
        :rtype: str
        """
        return self._PersonPictureUrl

    @PersonPictureUrl.setter
    def PersonPictureUrl(self, PersonPictureUrl):
        self._PersonPictureUrl = PersonPictureUrl

    @property
    def PersonSubType(self):
        """身份子类型:
PersonType=0时(普通顾客)，0普通顾客
PersonType=1时(白名单)，0店员，1商场人员，2其他类型人员，3区域经理，4注册用户，5VIP用户
PersonType=2时(黑名单)，0普通黑名单，1小偷)
        :rtype: int
        """
        return self._PersonSubType

    @PersonSubType.setter
    def PersonSubType(self, PersonSubType):
        self._PersonSubType = PersonSubType

    @property
    def VisitTimes(self):
        """到访次数，-1表示未知
        :rtype: int
        """
        return self._VisitTimes

    @VisitTimes.setter
    def VisitTimes(self, VisitTimes):
        self._VisitTimes = VisitTimes

    @property
    def VisitDays(self):
        """到访天数，-1表示未知
        :rtype: int
        """
        return self._VisitDays

    @VisitDays.setter
    def VisitDays(self, VisitDays):
        self._VisitDays = VisitDays


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._PersonPicture = params.get("PersonPicture")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._PersonType = params.get("PersonType")
        self._PersonPictureUrl = params.get("PersonPictureUrl")
        self._PersonSubType = params.get("PersonSubType")
        self._VisitTimes = params.get("VisitTimes")
        self._VisitDays = params.get("VisitDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonProfile(AbstractModel):
    """来访客人基本资料

    """

    def __init__(self):
        r"""
        :param _PersonId: 客人编码
        :type PersonId: str
        :param _Gender: 性别
        :type Gender: int
        :param _Age: 年龄
        :type Age: int
        :param _FirstArrivedTime: 首次到场时间
        :type FirstArrivedTime: str
        :param _ArrivedCount: 来访次数
        :type ArrivedCount: int
        :param _PicUrl: 客户图片
        :type PicUrl: str
        :param _Similarity: 置信度
        :type Similarity: float
        """
        self._PersonId = None
        self._Gender = None
        self._Age = None
        self._FirstArrivedTime = None
        self._ArrivedCount = None
        self._PicUrl = None
        self._Similarity = None

    @property
    def PersonId(self):
        """客人编码
        :rtype: str
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def Gender(self):
        """性别
        :rtype: int
        """
        return self._Gender

    @Gender.setter
    def Gender(self, Gender):
        self._Gender = Gender

    @property
    def Age(self):
        """年龄
        :rtype: int
        """
        return self._Age

    @Age.setter
    def Age(self, Age):
        self._Age = Age

    @property
    def FirstArrivedTime(self):
        """首次到场时间
        :rtype: str
        """
        return self._FirstArrivedTime

    @FirstArrivedTime.setter
    def FirstArrivedTime(self, FirstArrivedTime):
        self._FirstArrivedTime = FirstArrivedTime

    @property
    def ArrivedCount(self):
        """来访次数
        :rtype: int
        """
        return self._ArrivedCount

    @ArrivedCount.setter
    def ArrivedCount(self, ArrivedCount):
        self._ArrivedCount = ArrivedCount

    @property
    def PicUrl(self):
        """客户图片
        :rtype: str
        """
        return self._PicUrl

    @PicUrl.setter
    def PicUrl(self, PicUrl):
        self._PicUrl = PicUrl

    @property
    def Similarity(self):
        """置信度
        :rtype: float
        """
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._Gender = params.get("Gender")
        self._Age = params.get("Age")
        self._FirstArrivedTime = params.get("FirstArrivedTime")
        self._ArrivedCount = params.get("ArrivedCount")
        self._PicUrl = params.get("PicUrl")
        self._Similarity = params.get("Similarity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonTagInfo(AbstractModel):
    """修改顾客属性参数

    """

    def __init__(self):
        r"""
        :param _OldType: 顾客原类型
        :type OldType: int
        :param _NewType: 顾客新类型
        :type NewType: int
        :param _PersonId: 顾客face id
        :type PersonId: int
        """
        self._OldType = None
        self._NewType = None
        self._PersonId = None

    @property
    def OldType(self):
        """顾客原类型
        :rtype: int
        """
        return self._OldType

    @OldType.setter
    def OldType(self, OldType):
        self._OldType = OldType

    @property
    def NewType(self):
        """顾客新类型
        :rtype: int
        """
        return self._NewType

    @NewType.setter
    def NewType(self, NewType):
        self._NewType = NewType

    @property
    def PersonId(self):
        """顾客face id
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId


    def _deserialize(self, params):
        self._OldType = params.get("OldType")
        self._NewType = params.get("NewType")
        self._PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonTracePoint(AbstractModel):
    """客户轨迹点

    """

    def __init__(self):
        r"""
        :param _MallAreaId: 卖场区域编码
        :type MallAreaId: int
        :param _ShopId: 门店编码
        :type ShopId: int
        :param _MallAreaType: 卖场区域类型
        :type MallAreaType: int
        :param _TraceEventType: 轨迹事件
        :type TraceEventType: int
        :param _TraceEventTime: 轨迹事件发生时间点
        :type TraceEventTime: str
        :param _CapPic: 抓拍图片
        :type CapPic: str
        :param _ShoppingBagType: 购物袋类型
        :type ShoppingBagType: int
        :param _ShoppingBagCount: 购物袋数量
        :type ShoppingBagCount: int
        """
        self._MallAreaId = None
        self._ShopId = None
        self._MallAreaType = None
        self._TraceEventType = None
        self._TraceEventTime = None
        self._CapPic = None
        self._ShoppingBagType = None
        self._ShoppingBagCount = None

    @property
    def MallAreaId(self):
        """卖场区域编码
        :rtype: int
        """
        return self._MallAreaId

    @MallAreaId.setter
    def MallAreaId(self, MallAreaId):
        self._MallAreaId = MallAreaId

    @property
    def ShopId(self):
        """门店编码
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def MallAreaType(self):
        """卖场区域类型
        :rtype: int
        """
        return self._MallAreaType

    @MallAreaType.setter
    def MallAreaType(self, MallAreaType):
        self._MallAreaType = MallAreaType

    @property
    def TraceEventType(self):
        """轨迹事件
        :rtype: int
        """
        return self._TraceEventType

    @TraceEventType.setter
    def TraceEventType(self, TraceEventType):
        self._TraceEventType = TraceEventType

    @property
    def TraceEventTime(self):
        """轨迹事件发生时间点
        :rtype: str
        """
        return self._TraceEventTime

    @TraceEventTime.setter
    def TraceEventTime(self, TraceEventTime):
        self._TraceEventTime = TraceEventTime

    @property
    def CapPic(self):
        """抓拍图片
        :rtype: str
        """
        return self._CapPic

    @CapPic.setter
    def CapPic(self, CapPic):
        self._CapPic = CapPic

    @property
    def ShoppingBagType(self):
        """购物袋类型
        :rtype: int
        """
        return self._ShoppingBagType

    @ShoppingBagType.setter
    def ShoppingBagType(self, ShoppingBagType):
        self._ShoppingBagType = ShoppingBagType

    @property
    def ShoppingBagCount(self):
        """购物袋数量
        :rtype: int
        """
        return self._ShoppingBagCount

    @ShoppingBagCount.setter
    def ShoppingBagCount(self, ShoppingBagCount):
        self._ShoppingBagCount = ShoppingBagCount


    def _deserialize(self, params):
        self._MallAreaId = params.get("MallAreaId")
        self._ShopId = params.get("ShopId")
        self._MallAreaType = params.get("MallAreaType")
        self._TraceEventType = params.get("TraceEventType")
        self._TraceEventTime = params.get("TraceEventTime")
        self._CapPic = params.get("CapPic")
        self._ShoppingBagType = params.get("ShoppingBagType")
        self._ShoppingBagCount = params.get("ShoppingBagCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonTraceRoute(AbstractModel):
    """客户轨迹序列

    """

    def __init__(self):
        r"""
        :param _TraceId: 轨迹编码
        :type TraceId: str
        :param _TracePointSet: 轨迹点序列
        :type TracePointSet: list of PersonTracePoint
        """
        self._TraceId = None
        self._TracePointSet = None

    @property
    def TraceId(self):
        """轨迹编码
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def TracePointSet(self):
        """轨迹点序列
        :rtype: list of PersonTracePoint
        """
        return self._TracePointSet

    @TracePointSet.setter
    def TracePointSet(self, TracePointSet):
        self._TracePointSet = TracePointSet


    def _deserialize(self, params):
        self._TraceId = params.get("TraceId")
        if params.get("TracePointSet") is not None:
            self._TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = PersonTracePoint()
                obj._deserialize(item)
                self._TracePointSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PersonVisitInfo(AbstractModel):
    """用户到访明细

    """

    def __init__(self):
        r"""
        :param _PersonId: 用户ID
        :type PersonId: int
        :param _VisitId: 用户到访ID
        :type VisitId: int
        :param _InTime: 到访时间：Unix时间戳
        :type InTime: int
        :param _CapturedPicture: 抓拍到的头像Base64内容，已弃用，返回默认空值
        :type CapturedPicture: str
        :param _MaskType: 口罩类型：0不戴口罩，1戴口罩
        :type MaskType: int
        :param _GlassType: 眼镜类型：0不戴眼镜，1普通眼镜 , 2墨镜
        :type GlassType: int
        :param _HairType: 发型：0 短发,  1长发
        :type HairType: int
        :param _CapturedPictureUrl: 抓拍到的头像Url，在有效期内可以访问下载
        :type CapturedPictureUrl: str
        :param _SceneInfo: 抓拍头像的场景图信息
        :type SceneInfo: :class:`tencentcloud.youmall.v20180228.models.SceneInfo`
        """
        self._PersonId = None
        self._VisitId = None
        self._InTime = None
        self._CapturedPicture = None
        self._MaskType = None
        self._GlassType = None
        self._HairType = None
        self._CapturedPictureUrl = None
        self._SceneInfo = None

    @property
    def PersonId(self):
        """用户ID
        :rtype: int
        """
        return self._PersonId

    @PersonId.setter
    def PersonId(self, PersonId):
        self._PersonId = PersonId

    @property
    def VisitId(self):
        """用户到访ID
        :rtype: int
        """
        return self._VisitId

    @VisitId.setter
    def VisitId(self, VisitId):
        self._VisitId = VisitId

    @property
    def InTime(self):
        """到访时间：Unix时间戳
        :rtype: int
        """
        return self._InTime

    @InTime.setter
    def InTime(self, InTime):
        self._InTime = InTime

    @property
    def CapturedPicture(self):
        """抓拍到的头像Base64内容，已弃用，返回默认空值
        :rtype: str
        """
        return self._CapturedPicture

    @CapturedPicture.setter
    def CapturedPicture(self, CapturedPicture):
        self._CapturedPicture = CapturedPicture

    @property
    def MaskType(self):
        """口罩类型：0不戴口罩，1戴口罩
        :rtype: int
        """
        return self._MaskType

    @MaskType.setter
    def MaskType(self, MaskType):
        self._MaskType = MaskType

    @property
    def GlassType(self):
        """眼镜类型：0不戴眼镜，1普通眼镜 , 2墨镜
        :rtype: int
        """
        return self._GlassType

    @GlassType.setter
    def GlassType(self, GlassType):
        self._GlassType = GlassType

    @property
    def HairType(self):
        """发型：0 短发,  1长发
        :rtype: int
        """
        return self._HairType

    @HairType.setter
    def HairType(self, HairType):
        self._HairType = HairType

    @property
    def CapturedPictureUrl(self):
        """抓拍到的头像Url，在有效期内可以访问下载
        :rtype: str
        """
        return self._CapturedPictureUrl

    @CapturedPictureUrl.setter
    def CapturedPictureUrl(self, CapturedPictureUrl):
        self._CapturedPictureUrl = CapturedPictureUrl

    @property
    def SceneInfo(self):
        """抓拍头像的场景图信息
        :rtype: :class:`tencentcloud.youmall.v20180228.models.SceneInfo`
        """
        return self._SceneInfo

    @SceneInfo.setter
    def SceneInfo(self, SceneInfo):
        self._SceneInfo = SceneInfo


    def _deserialize(self, params):
        self._PersonId = params.get("PersonId")
        self._VisitId = params.get("VisitId")
        self._InTime = params.get("InTime")
        self._CapturedPicture = params.get("CapturedPicture")
        self._MaskType = params.get("MaskType")
        self._GlassType = params.get("GlassType")
        self._HairType = params.get("HairType")
        self._CapturedPictureUrl = params.get("CapturedPictureUrl")
        if params.get("SceneInfo") is not None:
            self._SceneInfo = SceneInfo()
            self._SceneInfo._deserialize(params.get("SceneInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCallbackRequest(AbstractModel):
    """RegisterCallback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 集团id，通过"指定身份标识获取客户门店列表"接口获取
        :type CompanyId: str
        :param _BackUrl: 通知回调地址，完整url，示例（http://youmall.tencentcloudapi.com/）
        :type BackUrl: str
        :param _Time: 请求时间戳
        :type Time: int
        :param _NeedFacePic: 是否需要顾客图片，1-需要图片，其它-不需要图片
        :type NeedFacePic: int
        """
        self._CompanyId = None
        self._BackUrl = None
        self._Time = None
        self._NeedFacePic = None

    @property
    def CompanyId(self):
        """集团id，通过"指定身份标识获取客户门店列表"接口获取
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def BackUrl(self):
        """通知回调地址，完整url，示例（http://youmall.tencentcloudapi.com/）
        :rtype: str
        """
        return self._BackUrl

    @BackUrl.setter
    def BackUrl(self, BackUrl):
        self._BackUrl = BackUrl

    @property
    def Time(self):
        """请求时间戳
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def NeedFacePic(self):
        """是否需要顾客图片，1-需要图片，其它-不需要图片
        :rtype: int
        """
        return self._NeedFacePic

    @NeedFacePic.setter
    def NeedFacePic(self, NeedFacePic):
        self._NeedFacePic = NeedFacePic


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._BackUrl = params.get("BackUrl")
        self._Time = params.get("Time")
        self._NeedFacePic = params.get("NeedFacePic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCallbackResponse(AbstractModel):
    """RegisterCallback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    """场景图信息

    """

    def __init__(self):
        r"""
        :param _ScenePictureURL: 场景图
        :type ScenePictureURL: str
        :param _HeadX: 抓拍头像左上角X坐标在场景图中的像素点位置
        :type HeadX: int
        :param _HeadY: 抓拍头像左上角Y坐标在场景图中的像素点位置
        :type HeadY: int
        :param _HeadWidth: 抓拍头像在场景图中占有的像素宽度
        :type HeadWidth: int
        :param _HeadHeight: 抓拍头像在场景图中占有的像素高度
        :type HeadHeight: int
        """
        self._ScenePictureURL = None
        self._HeadX = None
        self._HeadY = None
        self._HeadWidth = None
        self._HeadHeight = None

    @property
    def ScenePictureURL(self):
        """场景图
        :rtype: str
        """
        return self._ScenePictureURL

    @ScenePictureURL.setter
    def ScenePictureURL(self, ScenePictureURL):
        self._ScenePictureURL = ScenePictureURL

    @property
    def HeadX(self):
        """抓拍头像左上角X坐标在场景图中的像素点位置
        :rtype: int
        """
        return self._HeadX

    @HeadX.setter
    def HeadX(self, HeadX):
        self._HeadX = HeadX

    @property
    def HeadY(self):
        """抓拍头像左上角Y坐标在场景图中的像素点位置
        :rtype: int
        """
        return self._HeadY

    @HeadY.setter
    def HeadY(self, HeadY):
        self._HeadY = HeadY

    @property
    def HeadWidth(self):
        """抓拍头像在场景图中占有的像素宽度
        :rtype: int
        """
        return self._HeadWidth

    @HeadWidth.setter
    def HeadWidth(self, HeadWidth):
        self._HeadWidth = HeadWidth

    @property
    def HeadHeight(self):
        """抓拍头像在场景图中占有的像素高度
        :rtype: int
        """
        return self._HeadHeight

    @HeadHeight.setter
    def HeadHeight(self, HeadHeight):
        self._HeadHeight = HeadHeight


    def _deserialize(self, params):
        self._ScenePictureURL = params.get("ScenePictureURL")
        self._HeadX = params.get("HeadX")
        self._HeadY = params.get("HeadY")
        self._HeadWidth = params.get("HeadWidth")
        self._HeadHeight = params.get("HeadHeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShopDayTrafficInfo(AbstractModel):
    """门店客流量列表信息

    """

    def __init__(self):
        r"""
        :param _Date: 日期
        :type Date: str
        :param _DayTrafficTotalCount: 客流量
        :type DayTrafficTotalCount: int
        :param _GenderAgeTrafficDetailSet: 性别年龄分组下的客流信息
        :type GenderAgeTrafficDetailSet: list of GenderAgeTrafficDetail
        """
        self._Date = None
        self._DayTrafficTotalCount = None
        self._GenderAgeTrafficDetailSet = None

    @property
    def Date(self):
        """日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def DayTrafficTotalCount(self):
        """客流量
        :rtype: int
        """
        return self._DayTrafficTotalCount

    @DayTrafficTotalCount.setter
    def DayTrafficTotalCount(self, DayTrafficTotalCount):
        self._DayTrafficTotalCount = DayTrafficTotalCount

    @property
    def GenderAgeTrafficDetailSet(self):
        """性别年龄分组下的客流信息
        :rtype: list of GenderAgeTrafficDetail
        """
        return self._GenderAgeTrafficDetailSet

    @GenderAgeTrafficDetailSet.setter
    def GenderAgeTrafficDetailSet(self, GenderAgeTrafficDetailSet):
        self._GenderAgeTrafficDetailSet = GenderAgeTrafficDetailSet


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._DayTrafficTotalCount = params.get("DayTrafficTotalCount")
        if params.get("GenderAgeTrafficDetailSet") is not None:
            self._GenderAgeTrafficDetailSet = []
            for item in params.get("GenderAgeTrafficDetailSet"):
                obj = GenderAgeTrafficDetail()
                obj._deserialize(item)
                self._GenderAgeTrafficDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShopHourTrafficInfo(AbstractModel):
    """分时客流量信息

    """

    def __init__(self):
        r"""
        :param _Date: 日期，格式yyyy-MM-dd
        :type Date: str
        :param _HourTrafficInfoDetailSet: 分时客流详细信息
        :type HourTrafficInfoDetailSet: list of HourTrafficInfoDetail
        """
        self._Date = None
        self._HourTrafficInfoDetailSet = None

    @property
    def Date(self):
        """日期，格式yyyy-MM-dd
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def HourTrafficInfoDetailSet(self):
        """分时客流详细信息
        :rtype: list of HourTrafficInfoDetail
        """
        return self._HourTrafficInfoDetailSet

    @HourTrafficInfoDetailSet.setter
    def HourTrafficInfoDetailSet(self, HourTrafficInfoDetailSet):
        self._HourTrafficInfoDetailSet = HourTrafficInfoDetailSet


    def _deserialize(self, params):
        self._Date = params.get("Date")
        if params.get("HourTrafficInfoDetailSet") is not None:
            self._HourTrafficInfoDetailSet = []
            for item in params.get("HourTrafficInfoDetailSet"):
                obj = HourTrafficInfoDetail()
                obj._deserialize(item)
                self._HourTrafficInfoDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShopInfo(AbstractModel):
    """客户所属的门店信息

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: str
        :param _ShopId: 门店ID
        :type ShopId: int
        :param _ShopName: 门店名称
        :type ShopName: str
        :param _ShopCode: 客户门店编码
        :type ShopCode: str
        :param _Province: 省
        :type Province: str
        :param _City: 市
        :type City: str
        :param _CompanyName: 公司名称
        :type CompanyName: str
        """
        self._CompanyId = None
        self._ShopId = None
        self._ShopName = None
        self._ShopCode = None
        self._Province = None
        self._City = None
        self._CompanyName = None

    @property
    def CompanyId(self):
        """公司ID
        :rtype: str
        """
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ShopId(self):
        """门店ID
        :rtype: int
        """
        return self._ShopId

    @ShopId.setter
    def ShopId(self, ShopId):
        self._ShopId = ShopId

    @property
    def ShopName(self):
        """门店名称
        :rtype: str
        """
        return self._ShopName

    @ShopName.setter
    def ShopName(self, ShopName):
        self._ShopName = ShopName

    @property
    def ShopCode(self):
        """客户门店编码
        :rtype: str
        """
        return self._ShopCode

    @ShopCode.setter
    def ShopCode(self, ShopCode):
        self._ShopCode = ShopCode

    @property
    def Province(self):
        """省
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def CompanyName(self):
        """公司名称
        :rtype: str
        """
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._ShopId = params.get("ShopId")
        self._ShopName = params.get("ShopName")
        self._ShopCode = params.get("ShopCode")
        self._Province = params.get("Province")
        self._City = params.get("City")
        self._CompanyName = params.get("CompanyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrajectorySunData(AbstractModel):
    """轨迹动线信息子结构

    """

    def __init__(self):
        r"""
        :param _Zones: 区域动线，形如 x-x-x-x-x，其中 x 为区域 ID
        :type Zones: str
        :param _Count: 该动线出现次数
        :type Count: int
        :param _AvgStayTime: 该动线平均停留时间（秒）
        :type AvgStayTime: int
        """
        self._Zones = None
        self._Count = None
        self._AvgStayTime = None

    @property
    def Zones(self):
        """区域动线，形如 x-x-x-x-x，其中 x 为区域 ID
        :rtype: str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Count(self):
        """该动线出现次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AvgStayTime(self):
        """该动线平均停留时间（秒）
        :rtype: int
        """
        return self._AvgStayTime

    @AvgStayTime.setter
    def AvgStayTime(self, AvgStayTime):
        self._AvgStayTime = AvgStayTime


    def _deserialize(self, params):
        self._Zones = params.get("Zones")
        self._Count = params.get("Count")
        self._AvgStayTime = params.get("AvgStayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneAgeGroupAvrStayTime(AbstractModel):
    """区域性别平均停留时间子结构

    """

    def __init__(self):
        r"""
        :param _MaleAvrStayTime: 男性平均停留时间
        :type MaleAvrStayTime: float
        :param _FemaleAvrStayTime: 女性平均停留时间
        :type FemaleAvrStayTime: float
        """
        self._MaleAvrStayTime = None
        self._FemaleAvrStayTime = None

    @property
    def MaleAvrStayTime(self):
        """男性平均停留时间
        :rtype: float
        """
        return self._MaleAvrStayTime

    @MaleAvrStayTime.setter
    def MaleAvrStayTime(self, MaleAvrStayTime):
        self._MaleAvrStayTime = MaleAvrStayTime

    @property
    def FemaleAvrStayTime(self):
        """女性平均停留时间
        :rtype: float
        """
        return self._FemaleAvrStayTime

    @FemaleAvrStayTime.setter
    def FemaleAvrStayTime(self, FemaleAvrStayTime):
        self._FemaleAvrStayTime = FemaleAvrStayTime


    def _deserialize(self, params):
        self._MaleAvrStayTime = params.get("MaleAvrStayTime")
        self._FemaleAvrStayTime = params.get("FemaleAvrStayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneDayFlow(AbstractModel):
    """每日客流统计子结构

    """

    def __init__(self):
        r"""
        :param _Day: 日期，如 2018-08-6
        :type Day: str
        :param _FlowCount: 客流量
        :type FlowCount: int
        """
        self._Day = None
        self._FlowCount = None

    @property
    def Day(self):
        """日期，如 2018-08-6
        :rtype: str
        """
        return self._Day

    @Day.setter
    def Day(self, Day):
        self._Day = Day

    @property
    def FlowCount(self):
        """客流量
        :rtype: int
        """
        return self._FlowCount

    @FlowCount.setter
    def FlowCount(self, FlowCount):
        self._FlowCount = FlowCount


    def _deserialize(self, params):
        self._Day = params.get("Day")
        self._FlowCount = params.get("FlowCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneFlowAndAvrStayTime(AbstractModel):
    """客流停留统计子结构

    """

    def __init__(self):
        r"""
        :param _ZoneId: 区域id
        :type ZoneId: int
        :param _ZoneName: 区域名称
        :type ZoneName: str
        :param _FlowCount: 人流量
        :type FlowCount: int
        :param _AvrStayTime: 平均停留时长
        :type AvrStayTime: int
        """
        self._ZoneId = None
        self._ZoneName = None
        self._FlowCount = None
        self._AvrStayTime = None

    @property
    def ZoneId(self):
        """区域id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """区域名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def FlowCount(self):
        """人流量
        :rtype: int
        """
        return self._FlowCount

    @FlowCount.setter
    def FlowCount(self, FlowCount):
        self._FlowCount = FlowCount

    @property
    def AvrStayTime(self):
        """平均停留时长
        :rtype: int
        """
        return self._AvrStayTime

    @AvrStayTime.setter
    def AvrStayTime(self, AvrStayTime):
        self._AvrStayTime = AvrStayTime


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._FlowCount = params.get("FlowCount")
        self._AvrStayTime = params.get("AvrStayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneHourFlow(AbstractModel):
    """客流统计分时数据子结构

    """

    def __init__(self):
        r"""
        :param _Hour: 分时 0~23
        :type Hour: int
        :param _FlowCount: 客流量
        :type FlowCount: int
        """
        self._Hour = None
        self._FlowCount = None

    @property
    def Hour(self):
        """分时 0~23
        :rtype: int
        """
        return self._Hour

    @Hour.setter
    def Hour(self, Hour):
        self._Hour = Hour

    @property
    def FlowCount(self):
        """客流量
        :rtype: int
        """
        return self._FlowCount

    @FlowCount.setter
    def FlowCount(self, FlowCount):
        self._FlowCount = FlowCount


    def _deserialize(self, params):
        self._Hour = params.get("Hour")
        self._FlowCount = params.get("FlowCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneTrafficInfo(AbstractModel):
    """门店区域客流信息

    """

    def __init__(self):
        r"""
        :param _Date: 日期
        :type Date: str
        :param _ZoneTrafficInfoDetailSet: 门店区域客流详细信息
        :type ZoneTrafficInfoDetailSet: list of ZoneTrafficInfoDetail
        """
        self._Date = None
        self._ZoneTrafficInfoDetailSet = None

    @property
    def Date(self):
        """日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def ZoneTrafficInfoDetailSet(self):
        """门店区域客流详细信息
        :rtype: list of ZoneTrafficInfoDetail
        """
        return self._ZoneTrafficInfoDetailSet

    @ZoneTrafficInfoDetailSet.setter
    def ZoneTrafficInfoDetailSet(self, ZoneTrafficInfoDetailSet):
        self._ZoneTrafficInfoDetailSet = ZoneTrafficInfoDetailSet


    def _deserialize(self, params):
        self._Date = params.get("Date")
        if params.get("ZoneTrafficInfoDetailSet") is not None:
            self._ZoneTrafficInfoDetailSet = []
            for item in params.get("ZoneTrafficInfoDetailSet"):
                obj = ZoneTrafficInfoDetail()
                obj._deserialize(item)
                self._ZoneTrafficInfoDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneTrafficInfoDetail(AbstractModel):
    """门店区域客流详细信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 区域ID
        :type ZoneId: int
        :param _ZoneName: 区域名称
        :type ZoneName: str
        :param _TrafficTotalCount: 客流量
        :type TrafficTotalCount: int
        :param _AvgStayTime: 平均停留时间
        :type AvgStayTime: int
        """
        self._ZoneId = None
        self._ZoneName = None
        self._TrafficTotalCount = None
        self._AvgStayTime = None

    @property
    def ZoneId(self):
        """区域ID
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """区域名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def TrafficTotalCount(self):
        """客流量
        :rtype: int
        """
        return self._TrafficTotalCount

    @TrafficTotalCount.setter
    def TrafficTotalCount(self, TrafficTotalCount):
        self._TrafficTotalCount = TrafficTotalCount

    @property
    def AvgStayTime(self):
        """平均停留时间
        :rtype: int
        """
        return self._AvgStayTime

    @AvgStayTime.setter
    def AvgStayTime(self, AvgStayTime):
        self._AvgStayTime = AvgStayTime


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._TrafficTotalCount = params.get("TrafficTotalCount")
        self._AvgStayTime = params.get("AvgStayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        