# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class CameraControl(AbstractModel):
    r"""控制摄像机运动的协议

    """

    def __init__(self):
        r"""
        :param _Type: 枚举值：“simple”, “down_back”, “forward_up”, “right_turn_forward”, “left_turn_forward”
simple：简单运镜，此类型下可在"config"中六选一进行运镜
down_back：镜头下压并后退 -> 下移拉远，此类型下config参数无需填写
forward_up：镜头前进并上仰 -> 推进上移，此类型下config参数无需填写
right_turn_forward：先右旋转后前进 -> 右旋推进，此类型下config参数无需填写
left_turn_forward：先左旋并前进 -> 左旋推进，此类型下config参数无需填写
        :type Type: str
        :param _Config: 包含六个字段，用于指定摄像机在不同方向上的运动或变化。
- 当运镜类型指定simple时必填，指定其他类型时不填
- 参数6选1，即只能有一个参数不为0，其余参数为0
        :type Config: :class:`tencentcloud.vclm.v20240523.models.CameraControlConfig`
        """
        self._Type = None
        self._Config = None

    @property
    def Type(self):
        r"""枚举值：“simple”, “down_back”, “forward_up”, “right_turn_forward”, “left_turn_forward”
simple：简单运镜，此类型下可在"config"中六选一进行运镜
down_back：镜头下压并后退 -> 下移拉远，此类型下config参数无需填写
forward_up：镜头前进并上仰 -> 推进上移，此类型下config参数无需填写
right_turn_forward：先右旋转后前进 -> 右旋推进，此类型下config参数无需填写
left_turn_forward：先左旋并前进 -> 左旋推进，此类型下config参数无需填写
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Config(self):
        r"""包含六个字段，用于指定摄像机在不同方向上的运动或变化。
- 当运镜类型指定simple时必填，指定其他类型时不填
- 参数6选1，即只能有一个参数不为0，其余参数为0
        :rtype: :class:`tencentcloud.vclm.v20240523.models.CameraControlConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Config") is not None:
            self._Config = CameraControlConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CameraControlConfig(AbstractModel):
    r"""指定摄像机在不同方向上的运动或变化

    """

    def __init__(self):
        r"""
        :param _Horizontal: 水平运镜，控制摄像机在水平方向上的移动量（沿x轴平移）

取值范围：[-10, 10]，负值表示向左平移，正值表示向右平移
        :type Horizontal: float
        :param _Vertical: 垂直运镜，控制摄像机在垂直方向上的移动量（沿y轴平移）

取值范围：[-10, 10]，负值表示向下平移，正值表示向上平移
        :type Vertical: float
        :param _Pan: 水平摇镜，控制摄像机在水平面上的旋转量（绕y轴旋转）

取值范围：[-10, 10]，负值表示绕y轴向左旋转，正值表示绕y轴向右旋转
        :type Pan: float
        :param _Tilt: 垂直摇镜，控制摄像机在垂直面上的旋转量（沿x轴旋转）

取值范围：[-10, 10]，负值表示绕x轴向下旋转，正值表示绕x轴向上旋转
        :type Tilt: float
        :param _Roll: 旋转运镜，控制摄像机的滚动量（绕z轴旋转）

取值范围：[-10, 10]，负值表示绕z轴逆时针旋转，正值表示绕z轴顺时针旋转
        :type Roll: float
        :param _Zoom: 变焦，控制摄像机的焦距变化，影响视野的远近

取值范围：[-10, 10]，负值表示焦距变长、视野范围变小，正值表示焦距变短、视野范围变大
        :type Zoom: float
        """
        self._Horizontal = None
        self._Vertical = None
        self._Pan = None
        self._Tilt = None
        self._Roll = None
        self._Zoom = None

    @property
    def Horizontal(self):
        r"""水平运镜，控制摄像机在水平方向上的移动量（沿x轴平移）

取值范围：[-10, 10]，负值表示向左平移，正值表示向右平移
        :rtype: float
        """
        return self._Horizontal

    @Horizontal.setter
    def Horizontal(self, Horizontal):
        self._Horizontal = Horizontal

    @property
    def Vertical(self):
        r"""垂直运镜，控制摄像机在垂直方向上的移动量（沿y轴平移）

取值范围：[-10, 10]，负值表示向下平移，正值表示向上平移
        :rtype: float
        """
        return self._Vertical

    @Vertical.setter
    def Vertical(self, Vertical):
        self._Vertical = Vertical

    @property
    def Pan(self):
        r"""水平摇镜，控制摄像机在水平面上的旋转量（绕y轴旋转）

取值范围：[-10, 10]，负值表示绕y轴向左旋转，正值表示绕y轴向右旋转
        :rtype: float
        """
        return self._Pan

    @Pan.setter
    def Pan(self, Pan):
        self._Pan = Pan

    @property
    def Tilt(self):
        r"""垂直摇镜，控制摄像机在垂直面上的旋转量（沿x轴旋转）

取值范围：[-10, 10]，负值表示绕x轴向下旋转，正值表示绕x轴向上旋转
        :rtype: float
        """
        return self._Tilt

    @Tilt.setter
    def Tilt(self, Tilt):
        self._Tilt = Tilt

    @property
    def Roll(self):
        r"""旋转运镜，控制摄像机的滚动量（绕z轴旋转）

取值范围：[-10, 10]，负值表示绕z轴逆时针旋转，正值表示绕z轴顺时针旋转
        :rtype: float
        """
        return self._Roll

    @Roll.setter
    def Roll(self, Roll):
        self._Roll = Roll

    @property
    def Zoom(self):
        r"""变焦，控制摄像机的焦距变化，影响视野的远近

取值范围：[-10, 10]，负值表示焦距变长、视野范围变小，正值表示焦距变短、视野范围变大
        :rtype: float
        """
        return self._Zoom

    @Zoom.setter
    def Zoom(self, Zoom):
        self._Zoom = Zoom


    def _deserialize(self, params):
        self._Horizontal = params.get("Horizontal")
        self._Vertical = params.get("Vertical")
        self._Pan = params.get("Pan")
        self._Tilt = params.get("Tilt")
        self._Roll = params.get("Roll")
        self._Zoom = params.get("Zoom")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAnimateImageJobRequest(AbstractModel):
    r"""CheckAnimateImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 动作模板ID。
        :type TemplateId: str
        :param _ImageUrl: 图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageUrl: str
        :param _ImageBase64: 图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageBase64: str
        :param _EnableBodyJoins: 是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :type EnableBodyJoins: bool
        :param _EnableFace: 是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :type EnableFace: bool
        """
        self._TemplateId = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._EnableBodyJoins = None
        self._EnableFace = None

    @property
    def TemplateId(self):
        r"""动作模板ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ImageUrl(self):
        r"""图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def EnableBodyJoins(self):
        r"""是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :rtype: bool
        """
        return self._EnableBodyJoins

    @EnableBodyJoins.setter
    def EnableBodyJoins(self, EnableBodyJoins):
        self._EnableBodyJoins = EnableBodyJoins

    @property
    def EnableFace(self):
        r"""是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :rtype: bool
        """
        return self._EnableFace

    @EnableFace.setter
    def EnableFace(self, EnableFace):
        self._EnableFace = EnableFace


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._EnableBodyJoins = params.get("EnableBodyJoins")
        self._EnableFace = params.get("EnableFace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAnimateImageJobResponse(AbstractModel):
    r"""CheckAnimateImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckPass: 输入图是否通过校验。
        :type CheckPass: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckPass = None
        self._RequestId = None

    @property
    def CheckPass(self):
        r"""输入图是否通过校验。
        :rtype: bool
        """
        return self._CheckPass

    @CheckPass.setter
    def CheckPass(self, CheckPass):
        self._CheckPass = CheckPass

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CheckPass = params.get("CheckPass")
        self._RequestId = params.get("RequestId")


class CreateAigcElementRequest(AbstractModel):
    r"""CreateAigcElement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 
        :type Name: str
        :param _Description: 
        :type Description: str
        :param _ReferenceType: 
        :type ReferenceType: str
        :param _ElementImageList: 
        :type ElementImageList: :class:`tencentcloud.vclm.v20240523.models.ElementImageList`
        :param _VideoList: 
        :type VideoList: list of str
        :param _Provider: 
        :type Provider: list of str
        :param _TagList: 
        :type TagList: list of TagList
        """
        self._Name = None
        self._Description = None
        self._ReferenceType = None
        self._ElementImageList = None
        self._VideoList = None
        self._Provider = None
        self._TagList = None

    @property
    def Name(self):
        r"""
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ReferenceType(self):
        r"""
        :rtype: str
        """
        return self._ReferenceType

    @ReferenceType.setter
    def ReferenceType(self, ReferenceType):
        self._ReferenceType = ReferenceType

    @property
    def ElementImageList(self):
        r"""
        :rtype: :class:`tencentcloud.vclm.v20240523.models.ElementImageList`
        """
        return self._ElementImageList

    @ElementImageList.setter
    def ElementImageList(self, ElementImageList):
        self._ElementImageList = ElementImageList

    @property
    def VideoList(self):
        r"""
        :rtype: list of str
        """
        return self._VideoList

    @VideoList.setter
    def VideoList(self, VideoList):
        self._VideoList = VideoList

    @property
    def Provider(self):
        r"""
        :rtype: list of str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def TagList(self):
        r"""
        :rtype: list of TagList
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ReferenceType = params.get("ReferenceType")
        if params.get("ElementImageList") is not None:
            self._ElementImageList = ElementImageList()
            self._ElementImageList._deserialize(params.get("ElementImageList"))
        self._VideoList = params.get("VideoList")
        self._Provider = params.get("Provider")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagList()
                obj._deserialize(item)
                self._TagList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAigcElementResponse(AbstractModel):
    r"""CreateAigcElement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _ElementId: 
        :type ElementId: str
        :param _Status: 
        :type Status: str
        :param _Provider: 
        :type Provider: list of str
        :param _CreatedAt: 
        :type CreatedAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._ElementId = None
        self._Status = None
        self._Provider = None
        self._CreatedAt = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def ElementId(self):
        r"""
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def Status(self):
        r"""
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Provider(self):
        r"""
        :rtype: list of str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def CreatedAt(self):
        r"""
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._ElementId = params.get("ElementId")
        self._Status = params.get("Status")
        self._Provider = params.get("Provider")
        self._CreatedAt = params.get("CreatedAt")
        self._RequestId = params.get("RequestId")


class DeleteAigcElementRequest(AbstractModel):
    r"""DeleteAigcElement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ElementId: 
        :type ElementId: str
        """
        self._ElementId = None

    @property
    def ElementId(self):
        r"""
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId


    def _deserialize(self, params):
        self._ElementId = params.get("ElementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAigcElementResponse(AbstractModel):
    r"""DeleteAigcElement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ElementId: 
        :type ElementId: str
        :param _Deleted: 
        :type Deleted: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ElementId = None
        self._Deleted = None
        self._RequestId = None

    @property
    def ElementId(self):
        r"""
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def Deleted(self):
        r"""
        :rtype: bool
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ElementId = params.get("ElementId")
        self._Deleted = params.get("Deleted")
        self._RequestId = params.get("RequestId")


class DescribeAigcElementRequest(AbstractModel):
    r"""DescribeAigcElement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ElementId: 
        :type ElementId: str
        """
        self._ElementId = None

    @property
    def ElementId(self):
        r"""
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId


    def _deserialize(self, params):
        self._ElementId = params.get("ElementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAigcElementResponse(AbstractModel):
    r"""DescribeAigcElement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>主体名称</p>
        :type Name: str
        :param _ElementId: <p>主体id</p>
        :type ElementId: str
        :param _Description: <p>主体描述</p>
        :type Description: str
        :param _ReferenceType: <p>主体参考方式</p><p>枚举值：</p><ul><li>video_refer： 视频角色主体</li><li>image_refer： 多图主体</li></ul>
        :type ReferenceType: str
        :param _Status: <p>任务状态</p><p>枚举值：</p><ul><li>pending： 执行中</li><li>failed： 任务失败</li><li>succeed： 任务成功</li></ul>
        :type Status: str
        :param _Provider: <p>厂商列表</p>
        :type Provider: list of str
        :param _ElementImageList: <p>主体参考图，可通过多张图片设定主体及其细节</p>
        :type ElementImageList: :class:`tencentcloud.vclm.v20240523.models.ElementImageList`
        :param _VideoList: <p>主体参考视频，可通过视频设定主体及其细节</p>
        :type VideoList: list of str
        :param _TagList: <p>为主体配置标签，一个主体可以配置多个标签</p>
        :type TagList: list of TagList
        :param _ProviderDetails: <p>厂商聚合字段</p>
        :type ProviderDetails: list of ProviderDetail
        :param _CreatedAt: <p>创建时间</p>
        :type CreatedAt: str
        :param _UpdatedAt: <p>更新时间</p>
        :type UpdatedAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._ElementId = None
        self._Description = None
        self._ReferenceType = None
        self._Status = None
        self._Provider = None
        self._ElementImageList = None
        self._VideoList = None
        self._TagList = None
        self._ProviderDetails = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._RequestId = None

    @property
    def Name(self):
        r"""<p>主体名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ElementId(self):
        r"""<p>主体id</p>
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId

    @property
    def Description(self):
        r"""<p>主体描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ReferenceType(self):
        r"""<p>主体参考方式</p><p>枚举值：</p><ul><li>video_refer： 视频角色主体</li><li>image_refer： 多图主体</li></ul>
        :rtype: str
        """
        return self._ReferenceType

    @ReferenceType.setter
    def ReferenceType(self, ReferenceType):
        self._ReferenceType = ReferenceType

    @property
    def Status(self):
        r"""<p>任务状态</p><p>枚举值：</p><ul><li>pending： 执行中</li><li>failed： 任务失败</li><li>succeed： 任务成功</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Provider(self):
        r"""<p>厂商列表</p>
        :rtype: list of str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def ElementImageList(self):
        r"""<p>主体参考图，可通过多张图片设定主体及其细节</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.ElementImageList`
        """
        return self._ElementImageList

    @ElementImageList.setter
    def ElementImageList(self, ElementImageList):
        self._ElementImageList = ElementImageList

    @property
    def VideoList(self):
        r"""<p>主体参考视频，可通过视频设定主体及其细节</p>
        :rtype: list of str
        """
        return self._VideoList

    @VideoList.setter
    def VideoList(self, VideoList):
        self._VideoList = VideoList

    @property
    def TagList(self):
        r"""<p>为主体配置标签，一个主体可以配置多个标签</p>
        :rtype: list of TagList
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def ProviderDetails(self):
        r"""<p>厂商聚合字段</p>
        :rtype: list of ProviderDetail
        """
        return self._ProviderDetails

    @ProviderDetails.setter
    def ProviderDetails(self, ProviderDetails):
        self._ProviderDetails = ProviderDetails

    @property
    def CreatedAt(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ElementId = params.get("ElementId")
        self._Description = params.get("Description")
        self._ReferenceType = params.get("ReferenceType")
        self._Status = params.get("Status")
        self._Provider = params.get("Provider")
        if params.get("ElementImageList") is not None:
            self._ElementImageList = ElementImageList()
            self._ElementImageList._deserialize(params.get("ElementImageList"))
        self._VideoList = params.get("VideoList")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = TagList()
                obj._deserialize(item)
                self._TagList.append(obj)
        if params.get("ProviderDetails") is not None:
            self._ProviderDetails = []
            for item in params.get("ProviderDetails"):
                obj = ProviderDetail()
                obj._deserialize(item)
                self._ProviderDetails.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._RequestId = params.get("RequestId")


class DescribeAigcVideoJobRequest(AbstractModel):
    r"""DescribeAigcVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。

示例值：1194931538865782784
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。

示例值：1194931538865782784
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAigcVideoJobResponse(AbstractModel):
    r"""DescribeAigcVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
示例值：RUN
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
示例值：FailedOperation.DriverFailed
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
示例值：驱动失败
        :type ErrorMessage: str
        :param _ResultUrl: 结果视频 URL。有效期 24 小时。

示例值：https://console.cloud.tencent.com/result.mp4
        :type ResultUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
示例值：RUN
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
示例值：FailedOperation.DriverFailed
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
示例值：驱动失败
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultUrl(self):
        r"""结果视频 URL。有效期 24 小时。

示例值：https://console.cloud.tencent.com/result.mp4
        :rtype: str
        """
        return self._ResultUrl

    @ResultUrl.setter
    def ResultUrl(self, ResultUrl):
        self._ResultUrl = ResultUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultUrl = params.get("ResultUrl")
        self._RequestId = params.get("RequestId")


class DescribeHumanActorJobRequest(AbstractModel):
    r"""DescribeHumanActorJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHumanActorJobResponse(AbstractModel):
    r"""DescribeHumanActorJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ResultVideoUrl = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class DescribeHunyuanToVideoJobRequest(AbstractModel):
    r"""DescribeHunyuanToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHunyuanToVideoJobResponse(AbstractModel):
    r"""DescribeHunyuanToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeImageAnimateJobRequest(AbstractModel):
    r"""DescribeImageAnimateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageAnimateJobResponse(AbstractModel):
    r"""DescribeImageAnimateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 错误码。
        :type ErrorCode: str
        :param _ErrorMessage: 错误信息。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _MaskVideoUrl: 掩码视频链接
        :type MaskVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._MaskVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""错误码。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""错误信息。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def MaskVideoUrl(self):
        r"""掩码视频链接
        :rtype: str
        """
        return self._MaskVideoUrl

    @MaskVideoUrl.setter
    def MaskVideoUrl(self, MaskVideoUrl):
        self._MaskVideoUrl = MaskVideoUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._MaskVideoUrl = params.get("MaskVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeImageToVideoGeneralJobRequest(AbstractModel):
    r"""DescribeImageToVideoGeneralJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageToVideoGeneralJobResponse(AbstractModel):
    r"""DescribeImageToVideoGeneralJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeImageToVideoJobRequest(AbstractModel):
    r"""DescribeImageToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageToVideoJobResponse(AbstractModel):
    r"""DescribeImageToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _VideoId: <p>视频id</p>
        :type VideoId: str
        :param _Duration: <p>视频总时长，单位s</p>
        :type Duration: str
        :param _FinalUnitDeduction: <p>任务最终扣减积分数值</p>
        :type FinalUnitDeduction: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._VideoId = None
        self._Duration = None
        self._FinalUnitDeduction = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def VideoId(self):
        r"""<p>视频id</p>
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def Duration(self):
        r"""<p>视频总时长，单位s</p>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FinalUnitDeduction(self):
        r"""<p>任务最终扣减积分数值</p>
        :rtype: str
        """
        return self._FinalUnitDeduction

    @FinalUnitDeduction.setter
    def FinalUnitDeduction(self, FinalUnitDeduction):
        self._FinalUnitDeduction = FinalUnitDeduction

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._VideoId = params.get("VideoId")
        self._Duration = params.get("Duration")
        self._FinalUnitDeduction = params.get("FinalUnitDeduction")
        self._RequestId = params.get("RequestId")


class DescribeImageToVideoViduJobRequest(AbstractModel):
    r"""DescribeImageToVideoViduJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageToVideoViduJobResponse(AbstractModel):
    r"""DescribeImageToVideoViduJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _Credits: <p>该任务消耗的积分数量。</p>
        :type Credits: float
        :param _Payload: <p>任务调用时传入的透传参数。</p>
        :type Payload: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._Credits = None
        self._Payload = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def Credits(self):
        r"""<p>该任务消耗的积分数量。</p>
        :rtype: float
        """
        return self._Credits

    @Credits.setter
    def Credits(self, Credits):
        self._Credits = Credits

    @property
    def Payload(self):
        r"""<p>任务调用时传入的透传参数。</p>
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._Credits = params.get("Credits")
        self._Payload = params.get("Payload")
        self._RequestId = params.get("RequestId")


class DescribeMotionControlKlingJobRequest(AbstractModel):
    r"""DescribeMotionControlKlingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMotionControlKlingJobResponse(AbstractModel):
    r"""DescribeMotionControlKlingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _Duration: <p>视频时长。</p>
        :type Duration: str
        :param _FinalUnitDeduction: <p>消耗积分数。</p>
        :type FinalUnitDeduction: str
        :param _VideoId: <p>视频id</p>
        :type VideoId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._Duration = None
        self._FinalUnitDeduction = None
        self._VideoId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def Duration(self):
        r"""<p>视频时长。</p>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FinalUnitDeduction(self):
        r"""<p>消耗积分数。</p>
        :rtype: str
        """
        return self._FinalUnitDeduction

    @FinalUnitDeduction.setter
    def FinalUnitDeduction(self, FinalUnitDeduction):
        self._FinalUnitDeduction = FinalUnitDeduction

    @property
    def VideoId(self):
        r"""<p>视频id</p>
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._Duration = params.get("Duration")
        self._FinalUnitDeduction = params.get("FinalUnitDeduction")
        self._VideoId = params.get("VideoId")
        self._RequestId = params.get("RequestId")


class DescribePortraitSingJobRequest(AbstractModel):
    r"""DescribePortraitSingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePortraitSingJobResponse(AbstractModel):
    r"""DescribePortraitSingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _StatusCode: 任务状态码
—RUN：处理中
—FAIL：处理失败
—STOP：处理终止
—DONE：处理完成
        :type StatusCode: str
        :param _StatusMsg: 任务状态信息
        :type StatusMsg: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为FAIL时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为FAIL时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 生成视频的URL地址。有效期24小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._StatusCode = None
        self._StatusMsg = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StatusCode(self):
        r"""任务状态码
—RUN：处理中
—FAIL：处理失败
—STOP：处理终止
—DONE：处理完成
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMsg(self):
        r"""任务状态信息
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为FAIL时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为FAIL时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""生成视频的URL地址。有效期24小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StatusCode = params.get("StatusCode")
        self._StatusMsg = params.get("StatusMsg")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeReferenceToVideoViduJobRequest(AbstractModel):
    r"""DescribeReferenceToVideoViduJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReferenceToVideoViduJobResponse(AbstractModel):
    r"""DescribeReferenceToVideoViduJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _Credits: <p>该任务消耗的积分数量。</p>
        :type Credits: float
        :param _Payload: <p>任务调用时传入的透传参数。</p>
        :type Payload: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._Credits = None
        self._Payload = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def Credits(self):
        r"""<p>该任务消耗的积分数量。</p>
        :rtype: float
        """
        return self._Credits

    @Credits.setter
    def Credits(self, Credits):
        self._Credits = Credits

    @property
    def Payload(self):
        r"""<p>任务调用时传入的透传参数。</p>
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._Credits = params.get("Credits")
        self._Payload = params.get("Payload")
        self._RequestId = params.get("RequestId")


class DescribeTemplateToVideoJobRequest(AbstractModel):
    r"""DescribeTemplateToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateToVideoJobResponse(AbstractModel):
    r"""DescribeTemplateToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeTextToVideoJobRequest(AbstractModel):
    r"""DescribeTextToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTextToVideoJobResponse(AbstractModel):
    r"""DescribeTextToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _VideoId: <p>视频id</p>
        :type VideoId: str
        :param _Duration: <p>视频总时长，单位s</p>
        :type Duration: str
        :param _FinalUnitDeduction: <p>任务最终扣减积分数值</p>
        :type FinalUnitDeduction: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._VideoId = None
        self._Duration = None
        self._FinalUnitDeduction = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def VideoId(self):
        r"""<p>视频id</p>
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def Duration(self):
        r"""<p>视频总时长，单位s</p>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FinalUnitDeduction(self):
        r"""<p>任务最终扣减积分数值</p>
        :rtype: str
        """
        return self._FinalUnitDeduction

    @FinalUnitDeduction.setter
    def FinalUnitDeduction(self, FinalUnitDeduction):
        self._FinalUnitDeduction = FinalUnitDeduction

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._VideoId = params.get("VideoId")
        self._Duration = params.get("Duration")
        self._FinalUnitDeduction = params.get("FinalUnitDeduction")
        self._RequestId = params.get("RequestId")


class DescribeTextToVideoViduJobRequest(AbstractModel):
    r"""DescribeTextToVideoViduJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTextToVideoViduJobResponse(AbstractModel):
    r"""DescribeTextToVideoViduJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _Credits: <p>该任务消耗的积分数量。</p>
        :type Credits: float
        :param _Payload: <p>任务调用时传入的透传参数。</p>
        :type Payload: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._Credits = None
        self._Payload = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def Credits(self):
        r"""<p>该任务消耗的积分数量。</p>
        :rtype: float
        """
        return self._Credits

    @Credits.setter
    def Credits(self, Credits):
        self._Credits = Credits

    @property
    def Payload(self):
        r"""<p>任务调用时传入的透传参数。</p>
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._Credits = params.get("Credits")
        self._Payload = params.get("Payload")
        self._RequestId = params.get("RequestId")


class DescribeVideoEditJobRequest(AbstractModel):
    r"""DescribeVideoEditJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoEditJobResponse(AbstractModel):
    r"""DescribeVideoEditJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ResultVideoUrl = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class DescribeVideoEditKlingJobRequest(AbstractModel):
    r"""DescribeVideoEditKlingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoEditKlingJobResponse(AbstractModel):
    r"""DescribeVideoEditKlingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _VideoId: <p>视频id</p>
        :type VideoId: str
        :param _Duration: <p>时长</p>
        :type Duration: str
        :param _FinalUnitDeduction: <p>消耗积分数</p>
        :type FinalUnitDeduction: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._VideoId = None
        self._Duration = None
        self._FinalUnitDeduction = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def VideoId(self):
        r"""<p>视频id</p>
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def Duration(self):
        r"""<p>时长</p>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FinalUnitDeduction(self):
        r"""<p>消耗积分数</p>
        :rtype: str
        """
        return self._FinalUnitDeduction

    @FinalUnitDeduction.setter
    def FinalUnitDeduction(self, FinalUnitDeduction):
        self._FinalUnitDeduction = FinalUnitDeduction

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._VideoId = params.get("VideoId")
        self._Duration = params.get("Duration")
        self._FinalUnitDeduction = params.get("FinalUnitDeduction")
        self._RequestId = params.get("RequestId")


class DescribeVideoExtendKlingJobRequest(AbstractModel):
    r"""DescribeVideoExtendKlingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoExtendKlingJobResponse(AbstractModel):
    r"""DescribeVideoExtendKlingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: <p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :type Status: str
        :param _ErrorCode: <p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorCode: str
        :param _ErrorMessage: <p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :type ErrorMessage: str
        :param _ResultVideoUrl: <p>结果视频 URL。有效期 24 小时。</p>
        :type ResultVideoUrl: str
        :param _Duration: <p>视频时长。</p>
        :type Duration: str
        :param _FinalUnitDeduction: <p>消耗积分数。</p>
        :type FinalUnitDeduction: str
        :param _VideoId: <p>视频id</p>
        :type VideoId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._Duration = None
        self._FinalUnitDeduction = None
        self._VideoId = None
        self._RequestId = None

    @property
    def Status(self):
        r"""<p>任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""<p>任务执行错误码。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>任务执行错误信息。当任务状态不为 FAIL 时，该值为&quot;&quot;。</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""<p>结果视频 URL。有效期 24 小时。</p>
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def Duration(self):
        r"""<p>视频时长。</p>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def FinalUnitDeduction(self):
        r"""<p>消耗积分数。</p>
        :rtype: str
        """
        return self._FinalUnitDeduction

    @FinalUnitDeduction.setter
    def FinalUnitDeduction(self, FinalUnitDeduction):
        self._FinalUnitDeduction = FinalUnitDeduction

    @property
    def VideoId(self):
        r"""<p>视频id</p>
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._Duration = params.get("Duration")
        self._FinalUnitDeduction = params.get("FinalUnitDeduction")
        self._VideoId = params.get("VideoId")
        self._RequestId = params.get("RequestId")


class DescribeVideoFaceFusionJobRequest(AbstractModel):
    r"""DescribeVideoFaceFusionJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoFaceFusionJobResponse(AbstractModel):
    r"""DescribeVideoFaceFusionJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _ResultVideoUrl: 结果视频 URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def ResultVideoUrl(self):
        r"""结果视频 URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeVideoStylizationJobRequest(AbstractModel):
    r"""DescribeVideoStylizationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoStylizationJobResponse(AbstractModel):
    r"""DescribeVideoStylizationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        :param _StatusCode: 任务状态码。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
        :type StatusCode: str
        :param _StatusMsg: 任务状态描述。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
        :type StatusMsg: str
        :param _ResultVideoUrl: 处理结果视频Url。URL有效期为24小时。
        :type ResultVideoUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._StatusCode = None
        self._StatusMsg = None
        self._ResultVideoUrl = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def StatusCode(self):
        r"""任务状态码。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMsg(self):
        r"""任务状态描述。取值说明：
JobInit:  "初始化中"；
JobModerationFailed: "审核失败"；
JobRunning: "处理中"；
JobFailed: "处理失败"；
JobSuccess: "处理完成"。
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def ResultVideoUrl(self):
        r"""处理结果视频Url。URL有效期为24小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._StatusCode = params.get("StatusCode")
        self._StatusMsg = params.get("StatusMsg")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._RequestId = params.get("RequestId")


class DescribeVideoVoiceJobRequest(AbstractModel):
    r"""DescribeVideoVoiceJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoVoiceJobResponse(AbstractModel):
    r"""DescribeVideoVoiceJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :type Status: str
        :param _ResultVideoUrl: 结果视频URL。有效期 24 小时。
        :type ResultVideoUrl: str
        :param _ErrorCode: 任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :type ErrorCode: str
        :param _ErrorMessage: 任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ResultVideoUrl = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。  WAIT：等待中，RUN：执行中，FAIL：任务失败，DONE：任务成功
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ResultVideoUrl(self):
        r"""结果视频URL。有效期 24 小时。
        :rtype: str
        """
        return self._ResultVideoUrl

    @ResultVideoUrl.setter
    def ResultVideoUrl(self, ResultVideoUrl):
        self._ResultVideoUrl = ResultVideoUrl

    @property
    def ErrorCode(self):
        r"""任务执行错误码。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""任务执行错误信息。当任务状态不为 FAIL 时，该值为""。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ResultVideoUrl = params.get("ResultVideoUrl")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class DynamicMask(AbstractModel):
    r"""动态笔刷

    """

    def __init__(self):
        r"""
        :param _Mask: <p>动态笔刷涂抹区域（用户通过运动笔刷涂抹的 mask 图片）</p><p>支持传入图片Base64编码或图片URL（确保可访问，格式要求同 Image 字段）<br>图片格式支持.jpg / .jpeg / .png<br>图片长宽比必须与输入图片相同（即Image字段），否则任务失败<br>StaticMask 和 DynamicMasks.Mask 这两张图片的分辨率必须一致，否则任务失败</p>
        :type Mask: str
        :param _Trajectories: <p>运动轨迹坐标序列</p><p>生成5s的视频，轨迹长度不超过77，即坐标个数取值范围：[2, 77]<br>轨迹坐标系，以图片左下角为坐标原点<br>注1：坐标点个数越多轨迹刻画越准确，如只有2个轨迹点则为这两点连接的直线<br>注2：轨迹方向以传入顺序为指向，以最先传入的坐标为轨迹起点，依次连接后续坐标形成运动轨迹</p>
        :type Trajectories: list of Trajectory
        """
        self._Mask = None
        self._Trajectories = None

    @property
    def Mask(self):
        r"""<p>动态笔刷涂抹区域（用户通过运动笔刷涂抹的 mask 图片）</p><p>支持传入图片Base64编码或图片URL（确保可访问，格式要求同 Image 字段）<br>图片格式支持.jpg / .jpeg / .png<br>图片长宽比必须与输入图片相同（即Image字段），否则任务失败<br>StaticMask 和 DynamicMasks.Mask 这两张图片的分辨率必须一致，否则任务失败</p>
        :rtype: str
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def Trajectories(self):
        r"""<p>运动轨迹坐标序列</p><p>生成5s的视频，轨迹长度不超过77，即坐标个数取值范围：[2, 77]<br>轨迹坐标系，以图片左下角为坐标原点<br>注1：坐标点个数越多轨迹刻画越准确，如只有2个轨迹点则为这两点连接的直线<br>注2：轨迹方向以传入顺序为指向，以最先传入的坐标为轨迹起点，依次连接后续坐标形成运动轨迹</p>
        :rtype: list of Trajectory
        """
        return self._Trajectories

    @Trajectories.setter
    def Trajectories(self, Trajectories):
        self._Trajectories = Trajectories


    def _deserialize(self, params):
        self._Mask = params.get("Mask")
        if params.get("Trajectories") is not None:
            self._Trajectories = []
            for item in params.get("Trajectories"):
                obj = Trajectory()
                obj._deserialize(item)
                self._Trajectories.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Element(AbstractModel):
    r"""Element

    """

    def __init__(self):
        r"""
        :param _ElementId: <p>ID配置</p>
        :type ElementId: str
        """
        self._ElementId = None

    @property
    def ElementId(self):
        r"""<p>ID配置</p>
        :rtype: str
        """
        return self._ElementId

    @ElementId.setter
    def ElementId(self, ElementId):
        self._ElementId = ElementId


    def _deserialize(self, params):
        self._ElementId = params.get("ElementId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ElementImageList(AbstractModel):
    r"""主体正面图 参考图列表

    """

    def __init__(self):
        r"""
        :param _ReferImages: <p>主体参考图</p>
        :type ReferImages: list of ReferImageItem
        :param _FrontalImage: <p>主体主图</p>
        :type FrontalImage: str
        """
        self._ReferImages = None
        self._FrontalImage = None

    @property
    def ReferImages(self):
        r"""<p>主体参考图</p>
        :rtype: list of ReferImageItem
        """
        return self._ReferImages

    @ReferImages.setter
    def ReferImages(self, ReferImages):
        self._ReferImages = ReferImages

    @property
    def FrontalImage(self):
        r"""<p>主体主图</p>
        :rtype: str
        """
        return self._FrontalImage

    @FrontalImage.setter
    def FrontalImage(self, FrontalImage):
        self._FrontalImage = FrontalImage


    def _deserialize(self, params):
        if params.get("ReferImages") is not None:
            self._ReferImages = []
            for item in params.get("ReferImages"):
                obj = ReferImageItem()
                obj._deserialize(item)
                self._ReferImages.append(obj)
        self._FrontalImage = params.get("FrontalImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraParam(AbstractModel):
    r"""扩展字段。

    """

    def __init__(self):
        r"""
        :param _UserDesignatedUrl: <p>预签名的上传url，支持把视频直接传到客户指定的地址。</p>
        :type UserDesignatedUrl: str
        :param _CallbackUrl: <p>回调地址<br>需要您在创建任务时主动设置 CallbackUrl，请求方法为 POST，当视频生成结束时，我们将向此地址发送生成结果。<br>数据格式如下：<br>{<br>    &quot;JobId&quot;: &quot;1397428070633955328&quot;,<br>    &quot;Status&quot;: &quot;DONE&quot;,<br>    &quot;ErrorCode&quot;: &quot;&quot;,<br>    &quot;ErrorMessage&quot;: &quot;&quot;,<br>    &quot;ResultVideoUrl&quot;: &quot;https://vcg.cos.tencentcos.cn/template_to_video/fa80b846-b933-4981-afad-8a39b46ef2ca.mp4&quot;<br>}</p>
        :type CallbackUrl: str
        :param _BGMText: <p>BGM音频文本。</p>
        :type BGMText: str
        """
        self._UserDesignatedUrl = None
        self._CallbackUrl = None
        self._BGMText = None

    @property
    def UserDesignatedUrl(self):
        r"""<p>预签名的上传url，支持把视频直接传到客户指定的地址。</p>
        :rtype: str
        """
        return self._UserDesignatedUrl

    @UserDesignatedUrl.setter
    def UserDesignatedUrl(self, UserDesignatedUrl):
        self._UserDesignatedUrl = UserDesignatedUrl

    @property
    def CallbackUrl(self):
        r"""<p>回调地址<br>需要您在创建任务时主动设置 CallbackUrl，请求方法为 POST，当视频生成结束时，我们将向此地址发送生成结果。<br>数据格式如下：<br>{<br>    &quot;JobId&quot;: &quot;1397428070633955328&quot;,<br>    &quot;Status&quot;: &quot;DONE&quot;,<br>    &quot;ErrorCode&quot;: &quot;&quot;,<br>    &quot;ErrorMessage&quot;: &quot;&quot;,<br>    &quot;ResultVideoUrl&quot;: &quot;https://vcg.cos.tencentcos.cn/template_to_video/fa80b846-b933-4981-afad-8a39b46ef2ca.mp4&quot;<br>}</p>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def BGMText(self):
        r"""<p>BGM音频文本。</p>
        :rtype: str
        """
        return self._BGMText

    @BGMText.setter
    def BGMText(self, BGMText):
        self._BGMText = BGMText


    def _deserialize(self, params):
        self._UserDesignatedUrl = params.get("UserDesignatedUrl")
        self._CallbackUrl = params.get("CallbackUrl")
        self._BGMText = params.get("BGMText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceMergeInfo(AbstractModel):
    r"""人脸图片和待被融合的素材模板图的人脸位置信息。

    """

    def __init__(self):
        r"""
        :param _MergeFaceImage: 融合图片
        :type MergeFaceImage: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _MergeFaceRect: 上传的图片人脸位置信息（人脸框）
Width、Height >= 30。
        :type MergeFaceRect: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        :param _TemplateFaceID: 素材人脸ID，不填默认取上传图片中最大人脸。
        :type TemplateFaceID: str
        """
        self._MergeFaceImage = None
        self._MergeFaceRect = None
        self._TemplateFaceID = None

    @property
    def MergeFaceImage(self):
        r"""融合图片
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._MergeFaceImage

    @MergeFaceImage.setter
    def MergeFaceImage(self, MergeFaceImage):
        self._MergeFaceImage = MergeFaceImage

    @property
    def MergeFaceRect(self):
        r"""上传的图片人脸位置信息（人脸框）
Width、Height >= 30。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        """
        return self._MergeFaceRect

    @MergeFaceRect.setter
    def MergeFaceRect(self, MergeFaceRect):
        self._MergeFaceRect = MergeFaceRect

    @property
    def TemplateFaceID(self):
        r"""素材人脸ID，不填默认取上传图片中最大人脸。
        :rtype: str
        """
        return self._TemplateFaceID

    @TemplateFaceID.setter
    def TemplateFaceID(self, TemplateFaceID):
        self._TemplateFaceID = TemplateFaceID


    def _deserialize(self, params):
        if params.get("MergeFaceImage") is not None:
            self._MergeFaceImage = Image()
            self._MergeFaceImage._deserialize(params.get("MergeFaceImage"))
        if params.get("MergeFaceRect") is not None:
            self._MergeFaceRect = FaceRect()
            self._MergeFaceRect._deserialize(params.get("MergeFaceRect"))
        self._TemplateFaceID = params.get("TemplateFaceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceRect(AbstractModel):
    r"""人脸框信息。

    """

    def __init__(self):
        r"""
        :param _X: <p>人脸框左上角横坐标。</p>
        :type X: int
        :param _Y: <p>人脸框左上角纵坐标。</p>
        :type Y: int
        :param _Width: <p>人脸框宽度。<br>单位：px</p>
        :type Width: int
        :param _Height: <p>人脸框高度。<br>单位：px</p>
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""<p>人脸框左上角横坐标。</p>
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""<p>人脸框左上角纵坐标。</p>
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""<p>人脸框宽度。<br>单位：px</p>
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""<p>人脸框高度。<br>单位：px</p>
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceTemplateInfo(AbstractModel):
    r"""模板信息

    """

    def __init__(self):
        r"""
        :param _TemplateFaceID: 角色ID。需要与MergeInfos中的TemplateFaceID依次对应。需要填数字，建议填"0"、"1"，依次累加。
        :type TemplateFaceID: str
        :param _TemplateFaceImage: 视频模板中要替换的人脸图片
        :type TemplateFaceImage: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _TemplateFaceRect: 视频模板中要替换的人脸图片的人脸框。不填默认取要替换的人脸图片中最大人脸。
        :type TemplateFaceRect: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        """
        self._TemplateFaceID = None
        self._TemplateFaceImage = None
        self._TemplateFaceRect = None

    @property
    def TemplateFaceID(self):
        r"""角色ID。需要与MergeInfos中的TemplateFaceID依次对应。需要填数字，建议填"0"、"1"，依次累加。
        :rtype: str
        """
        return self._TemplateFaceID

    @TemplateFaceID.setter
    def TemplateFaceID(self, TemplateFaceID):
        self._TemplateFaceID = TemplateFaceID

    @property
    def TemplateFaceImage(self):
        r"""视频模板中要替换的人脸图片
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._TemplateFaceImage

    @TemplateFaceImage.setter
    def TemplateFaceImage(self, TemplateFaceImage):
        self._TemplateFaceImage = TemplateFaceImage

    @property
    def TemplateFaceRect(self):
        r"""视频模板中要替换的人脸图片的人脸框。不填默认取要替换的人脸图片中最大人脸。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.FaceRect`
        """
        return self._TemplateFaceRect

    @TemplateFaceRect.setter
    def TemplateFaceRect(self, TemplateFaceRect):
        self._TemplateFaceRect = TemplateFaceRect


    def _deserialize(self, params):
        self._TemplateFaceID = params.get("TemplateFaceID")
        if params.get("TemplateFaceImage") is not None:
            self._TemplateFaceImage = Image()
            self._TemplateFaceImage._deserialize(params.get("TemplateFaceImage"))
        if params.get("TemplateFaceRect") is not None:
            self._TemplateFaceRect = FaceRect()
            self._TemplateFaceRect._deserialize(params.get("TemplateFaceRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    r"""图片

    """

    def __init__(self):
        r"""
        :param _Base64: 图片Base64
        :type Base64: str
        :param _Url: 图片Url
        :type Url: str
        """
        self._Base64 = None
        self._Url = None

    @property
    def Base64(self):
        r"""图片Base64
        :rtype: str
        """
        return self._Base64

    @Base64.setter
    def Base64(self, Base64):
        self._Base64 = Base64

    @property
    def Url(self):
        r"""图片Url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Base64 = params.get("Base64")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    r"""参考图列表

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片URL
        :type ImageUrl: str
        :param _Type: 首帧：first_frame
尾帧：end_frame
其他：空

        :type Type: str
        """
        self._ImageUrl = None
        self._Type = None

    @property
    def ImageUrl(self):
        r"""图片URL
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def Type(self):
        r"""首帧：first_frame
尾帧：end_frame
其他：空

        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoParam(AbstractModel):
    r"""logo参数

    """

    def __init__(self):
        r"""
        :param _LogoUrl: 水印 Url
        :type LogoUrl: str
        :param _LogoImage: 水印 Base64，Url 和 Base64 二选一传入，如果都提供以 Url 为准
        :type LogoImage: str
        :param _LogoRect: 水印图片位于生成结果图中的坐标及宽高，将按照坐标对标识图片进行位置和大小的拉伸匹配。
        :type LogoRect: :class:`tencentcloud.vclm.v20240523.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        r"""水印 Url
        :rtype: str
        """
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        r"""水印 Base64，Url 和 Base64 二选一传入，如果都提供以 Url 为准
        :rtype: str
        """
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        r"""水印图片位于生成结果图中的坐标及宽高，将按照坐标对标识图片进行位置和大小的拉伸匹配。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoRect`
        """
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect


    def _deserialize(self, params):
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        if params.get("LogoRect") is not None:
            self._LogoRect = LogoRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoRect(AbstractModel):
    r"""水印图输入框

    """

    def __init__(self):
        r"""
        :param _X: <p>水印图框X坐标值。当值大于0时，坐标轴原点位于原图左侧，方向指右；当值小于0时，坐标轴原点位于原图右侧，方向指左。</p>
        :type X: int
        :param _Y: <p>水印图框Y坐标值。当值大于0时，坐标轴原点位于原图上侧，方向指下；当值小于0时，坐标轴原点位于原图下侧，方向指上。</p>
        :type Y: int
        :param _Width: <p>水印图框宽度。<br>单位：px</p>
        :type Width: int
        :param _Height: <p>水印图框高度。<br>单位：px</p>
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        r"""<p>水印图框X坐标值。当值大于0时，坐标轴原点位于原图左侧，方向指右；当值小于0时，坐标轴原点位于原图右侧，方向指左。</p>
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""<p>水印图框Y坐标值。当值大于0时，坐标轴原点位于原图上侧，方向指下；当值小于0时，坐标轴原点位于原图下侧，方向指上。</p>
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        r"""<p>水印图框宽度。<br>单位：px</p>
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""<p>水印图框高度。<br>单位：px</p>
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiPrompt(AbstractModel):
    r"""各分镜信息，如提示词、时长等

    通过index、prompt、duration参数定义分镜序号及相应提示词和时长，其中：

    最多支持6个分镜，最小支持1个分镜

    每个分镜相关内容的最大长度不超过512

    每个分镜的时长不大于当前任务的总时长，不小于1

    所有分镜的时长之和等于当前任务的总时长

    用key:value承载，如下：

    "multi_prompt":[
    	{
      	"index":int,
        "prompt": "string",
        "duration": "5"
      },
      {
      	"index":int,
        "prompt": "string",
        "duration": "5"
      }
    ]
    当mult_shot参数为true且shot_type参数为customize时，当前参数不得为空

    """

    def __init__(self):
        r"""
        :param _Index: <p>分镜序号</p>
        :type Index: int
        :param _Prompt: <p>分镜提示词</p>
        :type Prompt: str
        :param _Duration: <p>时长</p>
        :type Duration: str
        """
        self._Index = None
        self._Prompt = None
        self._Duration = None

    @property
    def Index(self):
        r"""<p>分镜序号</p>
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Prompt(self):
        r"""<p>分镜提示词</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Duration(self):
        r"""<p>时长</p>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Prompt = params.get("Prompt")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProviderDetail(AbstractModel):
    r"""ProviderDetail

    """

    def __init__(self):
        r"""
        :param _Provider: <p>供应商详情</p>
        :type Provider: str
        :param _Status: <p>状态</p>
        :type Status: str
        :param _ErrorMessage: <p>错误信息</p>
        :type ErrorMessage: str
        """
        self._Provider = None
        self._Status = None
        self._ErrorMessage = None

    @property
    def Provider(self):
        r"""<p>供应商详情</p>
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Status(self):
        r"""<p>状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMessage(self):
        r"""<p>错误信息</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._Provider = params.get("Provider")
        self._Status = params.get("Status")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReferImageItem(AbstractModel):
    r"""生成视频时所引用的音色

    """

    def __init__(self):
        r"""
        :param _ImageUrl: <p>图片地址</p>
        :type ImageUrl: str
        """
        self._ImageUrl = None

    @property
    def ImageUrl(self):
        r"""<p>图片地址</p>
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReferVideoInfo(AbstractModel):
    r"""参考视频信息

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 视频地址
        :type VideoUrl: str
        :param _ReferType: 视频类型
feature为特征参考视频
base为待编辑视频
        :type ReferType: str
        :param _KeepOriginalSound: 否保留视频原声，yes为保留，no为不保留；
当前参数对特征参考视频（feature）也生效。
        :type KeepOriginalSound: str
        """
        self._VideoUrl = None
        self._ReferType = None
        self._KeepOriginalSound = None

    @property
    def VideoUrl(self):
        r"""视频地址
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def ReferType(self):
        r"""视频类型
feature为特征参考视频
base为待编辑视频
        :rtype: str
        """
        return self._ReferType

    @ReferType.setter
    def ReferType(self, ReferType):
        self._ReferType = ReferType

    @property
    def KeepOriginalSound(self):
        r"""否保留视频原声，yes为保留，no为不保留；
当前参数对特征参考视频（feature）也生效。
        :rtype: str
        """
        return self._KeepOriginalSound

    @KeepOriginalSound.setter
    def KeepOriginalSound(self, KeepOriginalSound):
        self._KeepOriginalSound = KeepOriginalSound


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._ReferType = params.get("ReferType")
        self._KeepOriginalSound = params.get("KeepOriginalSound")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReferenceSubject(AbstractModel):
    r"""参考主体，主要用作参考图生视频。由主体id、主体图（三视图）以及声音组成。

    """

    def __init__(self):
        r"""
        :param _Id: <p>主体id，后续生成时在提示词中可以通过@主体id的方式使用。</p>
        :type Id: str
        :param _Images: <p>该主体对应的图片url，每个主体最多支持3张图片<br>注1：支持传入图片URL（确保可访问）<br>注2：图片支持 png、jpeg、jpg、webp格式<br>注3：图片像素不能小于 128*128，且比例需要小于1:4或者4:1，且大小不超过50M。</p>
        :type Images: list of str
        :param _Name: <p>主体id，后续生成时可以通过@主体id的方式使用</p>
        :type Name: str
        :param _Videos: <p>主体视频，该主体对应的视频url，与videos必填一个<br>注1： 仅viduq2-pro模型支持使用视频主体<br>注2：每个主体中的图片和视频，共享3个槽位<br>注3：支持1个5秒视频<br>注4：支持传入视频 URL（确保可访问）<br>注5：视频支持 mp4、avi、mov格式<br>注6：视频像素不能小于 128*128，且比例需要小于1:4或者4:1<br>注7：请注意，base64 decode之后的字节长度需要小于20M，且编码必须包含适当的内容类型字符串</p>
        :type Videos: list of str
        :param _VoiceId: <p>音色ID用来决定视频中的声音音色，为空时系统会自动推荐，可选枚举值参考列表：[音色列表](URL https://shengshu.feishu.cn/sheets/EgFvs6DShhiEBStmjzccr5gonOg)</p>
        :type VoiceId: str
        """
        self._Id = None
        self._Images = None
        self._Name = None
        self._Videos = None
        self._VoiceId = None

    @property
    def Id(self):
        r"""<p>主体id，后续生成时在提示词中可以通过@主体id的方式使用。</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Images(self):
        r"""<p>该主体对应的图片url，每个主体最多支持3张图片<br>注1：支持传入图片URL（确保可访问）<br>注2：图片支持 png、jpeg、jpg、webp格式<br>注3：图片像素不能小于 128*128，且比例需要小于1:4或者4:1，且大小不超过50M。</p>
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Name(self):
        r"""<p>主体id，后续生成时可以通过@主体id的方式使用</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Videos(self):
        r"""<p>主体视频，该主体对应的视频url，与videos必填一个<br>注1： 仅viduq2-pro模型支持使用视频主体<br>注2：每个主体中的图片和视频，共享3个槽位<br>注3：支持1个5秒视频<br>注4：支持传入视频 URL（确保可访问）<br>注5：视频支持 mp4、avi、mov格式<br>注6：视频像素不能小于 128*128，且比例需要小于1:4或者4:1<br>注7：请注意，base64 decode之后的字节长度需要小于20M，且编码必须包含适当的内容类型字符串</p>
        :rtype: list of str
        """
        return self._Videos

    @Videos.setter
    def Videos(self, Videos):
        self._Videos = Videos

    @property
    def VoiceId(self):
        r"""<p>音色ID用来决定视频中的声音音色，为空时系统会自动推荐，可选枚举值参考列表：[音色列表](URL https://shengshu.feishu.cn/sheets/EgFvs6DShhiEBStmjzccr5gonOg)</p>
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Images = params.get("Images")
        self._Name = params.get("Name")
        self._Videos = params.get("Videos")
        self._VoiceId = params.get("VoiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAigcVideoJobRequest(AbstractModel):
    r"""SubmitAigcVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Vendor: <p>模型名称。</p><p>枚举值：</p><p>● Vidu；</p><p>● Kling：可灵；</p><p>● HY：混元；</p><p>● YT：优图；</p><p>示例值：Vidu</p>
        :type Vendor: str
        :param _Model: <p>模型版本。</p><p>枚举值：</p><p>● 当Vendor为Vidu时，可选值[q2, q2-pro, q2-turbo, q3-pro, q3-turbo]</p><p>● 当Vendor为Kling时，可选值[v1.6, v2.0, v2.1, v2.5, v2.6]</p><p>● 当Vendor为HY时，默认值：[v1.5]</p><p>● 当Vendor为YT时，默认值：[v2.0]</p>
        :type Model: str
        :param _ModelParam: <p>模型参数Json-Format字符串<br> <a href="https://cloud.tencent.com/document/product/1616/128996">模型参数列表</a></p>
        :type ModelParam: str
        :param _Prompt: <p>正向文本提示词。不能超过2000个字符</p><p>示例值：一只小猫在草地奔跑</p>
        :type Prompt: str
        :param _LogoAdd: <p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Vendor = None
        self._Model = None
        self._ModelParam = None
        self._Prompt = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Vendor(self):
        r"""<p>模型名称。</p><p>枚举值：</p><p>● Vidu；</p><p>● Kling：可灵；</p><p>● HY：混元；</p><p>● YT：优图；</p><p>示例值：Vidu</p>
        :rtype: str
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Model(self):
        r"""<p>模型版本。</p><p>枚举值：</p><p>● 当Vendor为Vidu时，可选值[q2, q2-pro, q2-turbo, q3-pro, q3-turbo]</p><p>● 当Vendor为Kling时，可选值[v1.6, v2.0, v2.1, v2.5, v2.6]</p><p>● 当Vendor为HY时，默认值：[v1.5]</p><p>● 当Vendor为YT时，默认值：[v2.0]</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def ModelParam(self):
        r"""<p>模型参数Json-Format字符串<br> <a href="https://cloud.tencent.com/document/product/1616/128996">模型参数列表</a></p>
        :rtype: str
        """
        return self._ModelParam

    @ModelParam.setter
    def ModelParam(self, ModelParam):
        self._ModelParam = ModelParam

    @property
    def Prompt(self):
        r"""<p>正向文本提示词。不能超过2000个字符</p><p>示例值：一只小猫在草地奔跑</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Model = params.get("Model")
        self._ModelParam = params.get("ModelParam")
        self._Prompt = params.get("Prompt")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAigcVideoJobResponse(AbstractModel):
    r"""SubmitAigcVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHumanActorJobRequest(AbstractModel):
    r"""SubmitHumanActorJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本提示词，不能超过5000字符。
提示词支持全局和局部控制：

- 全局控制：正常输入提示词即可
- 局部控制：可用双井号进行特定时间的提示词约束，例如： "画面中的人物正在对着镜头讲话，偶尔做些手势匹配说话的内容。镜头保持固定。#3#画面中的人物正在对着镜头讲话，同时做出单手做向左方引导的手势。镜头保持固定。"（意思是第三秒的时候让人物做出左方引导手势）
 -- 局部控制时间建议整数，最大可读小数点后两位。
        :type Prompt: str
        :param _AudioUrl: 传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav
- 音频大小：10M以内
        :type AudioUrl: str
        :param _ImageUrl: 传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:4到4:1范围内
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :type ImageUrl: str
        :param _ImageBase64: 传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageUrl为准。
        :type ImageBase64: str
        :param _Resolution: 生成视频分辨率
枚举值：720p，1080p
默认1080p
        :type Resolution: str
        :param _FrameRate: 生成视频帧数，单位fps。
枚举值：25，50
默认50帧
        :type FrameRate: int
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Prompt = None
        self._AudioUrl = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._Resolution = None
        self._FrameRate = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        r"""文本提示词，不能超过5000字符。
提示词支持全局和局部控制：

- 全局控制：正常输入提示词即可
- 局部控制：可用双井号进行特定时间的提示词约束，例如： "画面中的人物正在对着镜头讲话，偶尔做些手势匹配说话的内容。镜头保持固定。#3#画面中的人物正在对着镜头讲话，同时做出单手做向左方引导的手势。镜头保持固定。"（意思是第三秒的时候让人物做出左方引导手势）
 -- 局部控制时间建议整数，最大可读小数点后两位。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def AudioUrl(self):
        r"""传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav
- 音频大小：10M以内
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def ImageUrl(self):
        r"""传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:4到4:1范围内
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageUrl为准。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Resolution(self):
        r"""生成视频分辨率
枚举值：720p，1080p
默认1080p
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def FrameRate(self):
        r"""生成视频帧数，单位fps。
枚举值：25，50
默认50帧
        :rtype: int
        """
        return self._FrameRate

    @FrameRate.setter
    def FrameRate(self, FrameRate):
        self._FrameRate = FrameRate

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._AudioUrl = params.get("AudioUrl")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._Resolution = params.get("Resolution")
        self._FrameRate = params.get("FrameRate")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHumanActorJobResponse(AbstractModel):
    r"""SubmitHumanActorJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitHunyuanToVideoJobRequest(AbstractModel):
    r"""SubmitHunyuanToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。 示例值：一只猫在草原上奔跑，写实风格
        :type Prompt: str
        :param _Image: 输入图片
上传图url大小不超过 10M，base64不超过8M。
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :type Image: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _Resolution: 目前仅支持720p视频分辨率，默认720p。
        :type Resolution: str
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。
 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。
        :type LogoAdd: int
        :param _LogoParam: 默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Prompt = None
        self._Image = None
        self._Resolution = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        r"""视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。 示例值：一只猫在草原上奔跑，写实风格
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Image(self):
        r"""输入图片
上传图url大小不超过 10M，base64不超过8M。
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Resolution(self):
        r"""目前仅支持720p视频分辨率，默认720p。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。
 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        self._Resolution = params.get("Resolution")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanToVideoJobResponse(AbstractModel):
    r"""SubmitHunyuanToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitImageAnimateJobRequest(AbstractModel):
    r"""SubmitImageAnimateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageUrl: 图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageUrl: str
        :param _ImageBase64: 图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :type ImageBase64: str
        :param _TemplateId: 动作模板ID。取值说明：ke3 科目三；tuziwu 兔子舞；huajiangwu 划桨舞。

        :type TemplateId: str
        :param _EnableAudio: 结果视频是否保留模板音频。默认为true
        :type EnableAudio: bool
        :param _EnableBodyJoins: 是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :type EnableBodyJoins: bool
        :param _EnableSegment: 是否对结果视频背景进行分割，默认值为false。
true：分割结果视频，结果视频（ResultVideoUrl）将为去除背景的绿幕视频，并返回掩码视频（MaskVideoUrl）；
false：不分割结果视频，结果视频（ResultVideoUrl）为带背景的视频，掩码视频（MaskVideoUrl）为空字符串。
        :type EnableSegment: bool
        :param _LogoAdd: 为生成视频添加标识的开关，默认为0。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        :param _EnableFace: 是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :type EnableFace: bool
        """
        self._ImageUrl = None
        self._ImageBase64 = None
        self._TemplateId = None
        self._EnableAudio = None
        self._EnableBodyJoins = None
        self._EnableSegment = None
        self._LogoAdd = None
        self._LogoParam = None
        self._EnableFace = None

    @property
    def ImageUrl(self):
        r"""图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""图片base64数据。
图片格式：支持PNG、JPG、JPEG、BMP、WEBP格式；
图片分辨率：长边分辨率范围【192，4096】；
图片大小：不超过10M；
图片宽高比：【宽：高】数值在 1:2 到 1:1.2 范围内
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def TemplateId(self):
        r"""动作模板ID。取值说明：ke3 科目三；tuziwu 兔子舞；huajiangwu 划桨舞。

        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def EnableAudio(self):
        r"""结果视频是否保留模板音频。默认为true
        :rtype: bool
        """
        return self._EnableAudio

    @EnableAudio.setter
    def EnableAudio(self, EnableAudio):
        self._EnableAudio = EnableAudio

    @property
    def EnableBodyJoins(self):
        r"""是否对输入图采用加强检测方案。

默认不加强检测（false），仅对输入图做必要的基础检测。

开启加强检测（true）有助于提升效果稳定性，将根据选择的动作模板提取建议的人体关键点，并判断输入图中是否包含这些人体关键点。加强检测仅对人像输入图生效，对非人输入图不生效。
        :rtype: bool
        """
        return self._EnableBodyJoins

    @EnableBodyJoins.setter
    def EnableBodyJoins(self, EnableBodyJoins):
        self._EnableBodyJoins = EnableBodyJoins

    @property
    def EnableSegment(self):
        r"""是否对结果视频背景进行分割，默认值为false。
true：分割结果视频，结果视频（ResultVideoUrl）将为去除背景的绿幕视频，并返回掩码视频（MaskVideoUrl）；
false：不分割结果视频，结果视频（ResultVideoUrl）为带背景的视频，掩码视频（MaskVideoUrl）为空字符串。
        :rtype: bool
        """
        return self._EnableSegment

    @EnableSegment.setter
    def EnableSegment(self, EnableSegment):
        self._EnableSegment = EnableSegment

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为0。
1：添加标识。
0：不添加标识。
其他数值：默认按1处理。
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。
默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def EnableFace(self):
        r"""是否开启人脸检测。

默认开启人脸检测（true），拦截主体为人像但无人脸、人脸不完整或被遮挡的输入图。可选关闭人脸检测（false）。
        :rtype: bool
        """
        return self._EnableFace

    @EnableFace.setter
    def EnableFace(self, EnableFace):
        self._EnableFace = EnableFace


    def _deserialize(self, params):
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._TemplateId = params.get("TemplateId")
        self._EnableAudio = params.get("EnableAudio")
        self._EnableBodyJoins = params.get("EnableBodyJoins")
        self._EnableSegment = params.get("EnableSegment")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._EnableFace = params.get("EnableFace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageAnimateJobResponse(AbstractModel):
    r"""SubmitImageAnimateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 图片跳舞任务ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""图片跳舞任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitImageToVideoGeneralJobRequest(AbstractModel):
    r"""SubmitImageToVideoGeneralJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: 输入图片
Base64 和 Url 必须提供一个，如果都提供以ImageUrl为准。
上传图url大小不超过 8M
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :type Image: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _Prompt: 视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。
        :type Prompt: str
        :param _Resolution: 输出视频分辨率。可选择：480p、720p、1080p。
        :type Resolution: str
        :param _Fps: 生成视频的帧率，从16, 24, 30中选择。默认值：30
        :type Fps: int
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。  1：添加标识；  0：不添加标识；  其他数值：默认按1处理。
        :type LogoAdd: int
        :param _LogoParam: 默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Image = None
        self._Prompt = None
        self._Resolution = None
        self._Fps = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Image(self):
        r"""输入图片
Base64 和 Url 必须提供一个，如果都提供以ImageUrl为准。
上传图url大小不超过 8M
支持jpg，png，jpeg，webp，bmp，tiff 格式
单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Prompt(self):
        r"""视频内容的描述，中文正向提示词。最多支持200个 utf-8 字符（首尾空格不计入字符数）。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Resolution(self):
        r"""输出视频分辨率。可选择：480p、720p、1080p。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Fps(self):
        r"""生成视频的帧率，从16, 24, 30中选择。默认值：30
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。  1：添加标识；  0：不添加标识；  其他数值：默认按1处理。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        self._Prompt = params.get("Prompt")
        self._Resolution = params.get("Resolution")
        self._Fps = params.get("Fps")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageToVideoGeneralJobResponse(AbstractModel):
    r"""SubmitImageToVideoGeneralJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitImageToVideoJobRequest(AbstractModel):
    r"""SubmitImageToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: <p>模型名称。<br>v1.6：Kling-V1-6<br>v2.0：Kling-V2-Master<br>v2.1：Kling-V2-1<br>v2.5：Kling-V2-5-Turbo<br>v2.6：Kling-V2-6<br>V3.0：kling-v3</p>
        :type Model: str
        :param _Image: <p>参考图像。</p><ul><li>支持传入图片Base64编码或图片URL（确保可访问）</li><li>图片文件大小不能超过10MB，图片分辨率不小于300*300px，图片宽高比要在1:2.5 ~ 2.5:1之间</li><li>Image 参数与 ImageTail 参数至少二选一，二者不能同时为空</li><li>图片格式支持.jpg / .jpeg / .png</li></ul>
        :type Image: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _ImageTail: <p>参考尾帧图像。</p><ul><li>支持传入图片Base64编码或图片URL（确保可访问）</li><li>图片文件大小不能超过10MB，图片分辨率不小于300*300px，图片宽高比要在1:2.5 ~ 2.5:1之间</li><li>Image 参数与 ImageTail 参数至少二选一，二者不能同时为空</li><li>图片格式支持.jpg / .jpeg / .png</li><li>ImageTail参数、DynamicMasks/StaticMask参数、CameraControl参数三选一，不能同时使用</li></ul>
        :type ImageTail: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _Prompt: <p>正向文本提示词。不能超过2500个字符</p>
        :type Prompt: str
        :param _NegativePrompt: <p>负向文本提示词。不能超过2500个字符</p>
        :type NegativePrompt: str
        :param _Duration: <p>生成视频时长，单位s。默认值为5。<br>枚举值：3，4，5，6，7，8，9，10，11，12，13，14，15</p><p>不同模型支持时长不同</p><ul><li>模型v1.6、v2.0、v2.5、v2.6：支持5、10</li><li>模型v3.0：支持3～15s</li></ul>
        :type Duration: str
        :param _Mode: <p>生成视频的模式<br>枚举值：std，pro<br>其中std：标准模式（标准），基础模式，性价比高<br>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</p><p>不同模型版本、视频模式支持范围不同</p><ul><li>v1.6：首尾帧与仅首帧情况下只支持pro</li><li>v2.0、v3.0 ：无需配置</li><li>v2.1、v2.5、v2.6：首尾帧情况下只支持pro</li></ul>
        :type Mode: str
        :param _CfgScale: <p>生成视频的自由度；值越大，模型自由度越小，与用户输入的提示词相关性越强。<br>v2.0、v2.5、v2.6模型的不支持当前参数<br>取值范围：[0, 1]</p>
        :type CfgScale: float
        :param _Sound: <p>生成视频时是否同时生成声音<br>枚举值：on，off<br>不同模型版本、视频模式支持范围不同</p><ul><li>v2.6：有首尾帧的pro模式只能生成无声的视频</li></ul>
        :type Sound: str
        :param _LogoAdd: <p>为生成视频添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        :param _MultiShot: <p>是否生成多镜头视频</p><ul><li>当前参数为true时，Prompt参数无效，且不支持设定首尾帧生视频</li><li>当前参数为false时，ShotType参数及MultiPrompt参数无效</li></ul>
        :type MultiShot: bool
        :param _ShotType: <p>分镜方式</p><ul><li>枚举值：customize，intelligence</li><li>当MultiShot参数为true时，当前参数必填</li></ul>
        :type ShotType: str
        :param _MultiPrompt: <p>各分镜信息，如提示词、时长等<br>通过Index、Prompt、Duration参数定义分镜序号及相应提示词和时长，其中：</p><ul><li>最多支持6个分镜，最小支持1个分镜</li><li>每个分镜相关内容的最大长度不超过512</li><li>每个分镜的时长不大于当前任务的总时长，不小于1</li><li>所有分镜的时长之和等于当前任务的总时长</li></ul><p>用key:value承载，如下：<br>&quot;MultiPrompt&quot;:[<br>    {<br>      &quot;Index&quot;:int,<br>    &quot;Prompt&quot;: &quot;string&quot;,<br>    &quot;Duration&quot;: &quot;5&quot;<br>  },<br>  {<br>      &quot;Index&quot;:int,<br>    &quot;Prompt&quot;: &quot;string&quot;,<br>    &quot;Duration&quot;: &quot;5&quot;<br>  }<br>]</p><ul><li>当MultiShot参数为true且ShotType参数为customize时，当前参数不得为空</li></ul>
        :type MultiPrompt: list of MultiPrompt
        :param _ElementList: <p>参考主体列表</p><ul><li><p>基于主体库中主体的ID配置，用key:value承载，如下：</p><pre><code>  &quot;ElementList&quot;:[      {         &quot;ElementId&quot;:long    },    {         &quot;ElementId&quot;:long    }  ]</code></pre></li><li><p>最多支持3个参考主体</p></li><li><p>主体分为视频定制主体（简称：视频角色主体）和图片定制主体（简称：多图主体），适用范围不同，请注意区分</p></li><li><p>更多主体信息详见：可灵「主体库 3.0」使用指南</p></li></ul>
        :type ElementList: list of Element
        :param _StaticMask: <p>静态笔刷涂抹区域（用户通过运动笔刷涂抹的 mask 图片）<br>“运动笔刷”能力包含“动态笔刷 DynamicMasks”和“静态笔刷 StaticMask”两种<br>支持传入图片Base64编码或图片URL（确保可访问，格式要求同 Image 字段）<br>图片格式支持.jpg / .jpeg / .png<br>图片长宽比必须与输入图片相同（即Image字段），否则任务失败（failed）<br>StaticMask和 DynamicMasks.Mask这两张图片的分辨率必须一致，否则任务失败（failed）</p>
        :type StaticMask: str
        :param _DynamicMasks: <p>动态笔刷配置列表<br>可配置多组（最多6组），每组包含“涂抹区域 Mask”与“运动轨迹 Trajectories”序列</p>
        :type DynamicMasks: list of DynamicMask
        :param _CameraControl: <p>控制摄像机运动的协议（如未指定，模型将根据输入的文本/图片进行智能匹配）</p>
        :type CameraControl: :class:`tencentcloud.vclm.v20240523.models.CameraControl`
        :param _CallbackUrl: <p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :type CallbackUrl: str
        :param _VoiceList: <p>生成视频时所引用的音色的列表</p><p>一次视频生成任务至多引用2个音色<br>当VoiceList参数不为空且Prompt参数中引用音色ID时，视频生成任务按“有指定音色”计量计费<br>VoiceId参数值通过音色定制接口返回，也可使用系统预置音色，详见音色定制相关API；非对口型API的VoiceId<br>ElementList参数与VoiceList参数互斥，不能共存<br>v3模型不支持指定音色<br>用key:value承载，如下：<br>&quot;VoiceList&quot;:[<br>  {&quot;VoiceId&quot;:&quot;VoiceId_1&quot;},<br>  {&quot;VoiceId&quot;:&quot;VoiceId_2&quot;}<br>]</p>
        :type VoiceList: list of Voice
        """
        self._Model = None
        self._Image = None
        self._ImageTail = None
        self._Prompt = None
        self._NegativePrompt = None
        self._Duration = None
        self._Mode = None
        self._CfgScale = None
        self._Sound = None
        self._LogoAdd = None
        self._LogoParam = None
        self._MultiShot = None
        self._ShotType = None
        self._MultiPrompt = None
        self._ElementList = None
        self._StaticMask = None
        self._DynamicMasks = None
        self._CameraControl = None
        self._CallbackUrl = None
        self._VoiceList = None

    @property
    def Model(self):
        r"""<p>模型名称。<br>v1.6：Kling-V1-6<br>v2.0：Kling-V2-Master<br>v2.1：Kling-V2-1<br>v2.5：Kling-V2-5-Turbo<br>v2.6：Kling-V2-6<br>V3.0：kling-v3</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Image(self):
        r"""<p>参考图像。</p><ul><li>支持传入图片Base64编码或图片URL（确保可访问）</li><li>图片文件大小不能超过10MB，图片分辨率不小于300*300px，图片宽高比要在1:2.5 ~ 2.5:1之间</li><li>Image 参数与 ImageTail 参数至少二选一，二者不能同时为空</li><li>图片格式支持.jpg / .jpeg / .png</li></ul>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageTail(self):
        r"""<p>参考尾帧图像。</p><ul><li>支持传入图片Base64编码或图片URL（确保可访问）</li><li>图片文件大小不能超过10MB，图片分辨率不小于300*300px，图片宽高比要在1:2.5 ~ 2.5:1之间</li><li>Image 参数与 ImageTail 参数至少二选一，二者不能同时为空</li><li>图片格式支持.jpg / .jpeg / .png</li><li>ImageTail参数、DynamicMasks/StaticMask参数、CameraControl参数三选一，不能同时使用</li></ul>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._ImageTail

    @ImageTail.setter
    def ImageTail(self, ImageTail):
        self._ImageTail = ImageTail

    @property
    def Prompt(self):
        r"""<p>正向文本提示词。不能超过2500个字符</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        r"""<p>负向文本提示词。不能超过2500个字符</p>
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Duration(self):
        r"""<p>生成视频时长，单位s。默认值为5。<br>枚举值：3，4，5，6，7，8，9，10，11，12，13，14，15</p><p>不同模型支持时长不同</p><ul><li>模型v1.6、v2.0、v2.5、v2.6：支持5、10</li><li>模型v3.0：支持3～15s</li></ul>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Mode(self):
        r"""<p>生成视频的模式<br>枚举值：std，pro<br>其中std：标准模式（标准），基础模式，性价比高<br>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</p><p>不同模型版本、视频模式支持范围不同</p><ul><li>v1.6：首尾帧与仅首帧情况下只支持pro</li><li>v2.0、v3.0 ：无需配置</li><li>v2.1、v2.5、v2.6：首尾帧情况下只支持pro</li></ul>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CfgScale(self):
        r"""<p>生成视频的自由度；值越大，模型自由度越小，与用户输入的提示词相关性越强。<br>v2.0、v2.5、v2.6模型的不支持当前参数<br>取值范围：[0, 1]</p>
        :rtype: float
        """
        return self._CfgScale

    @CfgScale.setter
    def CfgScale(self, CfgScale):
        self._CfgScale = CfgScale

    @property
    def Sound(self):
        r"""<p>生成视频时是否同时生成声音<br>枚举值：on，off<br>不同模型版本、视频模式支持范围不同</p><ul><li>v2.6：有首尾帧的pro模式只能生成无声的视频</li></ul>
        :rtype: str
        """
        return self._Sound

    @Sound.setter
    def Sound(self, Sound):
        self._Sound = Sound

    @property
    def LogoAdd(self):
        r"""<p>为生成视频添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def MultiShot(self):
        r"""<p>是否生成多镜头视频</p><ul><li>当前参数为true时，Prompt参数无效，且不支持设定首尾帧生视频</li><li>当前参数为false时，ShotType参数及MultiPrompt参数无效</li></ul>
        :rtype: bool
        """
        return self._MultiShot

    @MultiShot.setter
    def MultiShot(self, MultiShot):
        self._MultiShot = MultiShot

    @property
    def ShotType(self):
        r"""<p>分镜方式</p><ul><li>枚举值：customize，intelligence</li><li>当MultiShot参数为true时，当前参数必填</li></ul>
        :rtype: str
        """
        return self._ShotType

    @ShotType.setter
    def ShotType(self, ShotType):
        self._ShotType = ShotType

    @property
    def MultiPrompt(self):
        r"""<p>各分镜信息，如提示词、时长等<br>通过Index、Prompt、Duration参数定义分镜序号及相应提示词和时长，其中：</p><ul><li>最多支持6个分镜，最小支持1个分镜</li><li>每个分镜相关内容的最大长度不超过512</li><li>每个分镜的时长不大于当前任务的总时长，不小于1</li><li>所有分镜的时长之和等于当前任务的总时长</li></ul><p>用key:value承载，如下：<br>&quot;MultiPrompt&quot;:[<br>    {<br>      &quot;Index&quot;:int,<br>    &quot;Prompt&quot;: &quot;string&quot;,<br>    &quot;Duration&quot;: &quot;5&quot;<br>  },<br>  {<br>      &quot;Index&quot;:int,<br>    &quot;Prompt&quot;: &quot;string&quot;,<br>    &quot;Duration&quot;: &quot;5&quot;<br>  }<br>]</p><ul><li>当MultiShot参数为true且ShotType参数为customize时，当前参数不得为空</li></ul>
        :rtype: list of MultiPrompt
        """
        return self._MultiPrompt

    @MultiPrompt.setter
    def MultiPrompt(self, MultiPrompt):
        self._MultiPrompt = MultiPrompt

    @property
    def ElementList(self):
        r"""<p>参考主体列表</p><ul><li><p>基于主体库中主体的ID配置，用key:value承载，如下：</p><pre><code>  &quot;ElementList&quot;:[      {         &quot;ElementId&quot;:long    },    {         &quot;ElementId&quot;:long    }  ]</code></pre></li><li><p>最多支持3个参考主体</p></li><li><p>主体分为视频定制主体（简称：视频角色主体）和图片定制主体（简称：多图主体），适用范围不同，请注意区分</p></li><li><p>更多主体信息详见：可灵「主体库 3.0」使用指南</p></li></ul>
        :rtype: list of Element
        """
        return self._ElementList

    @ElementList.setter
    def ElementList(self, ElementList):
        self._ElementList = ElementList

    @property
    def StaticMask(self):
        r"""<p>静态笔刷涂抹区域（用户通过运动笔刷涂抹的 mask 图片）<br>“运动笔刷”能力包含“动态笔刷 DynamicMasks”和“静态笔刷 StaticMask”两种<br>支持传入图片Base64编码或图片URL（确保可访问，格式要求同 Image 字段）<br>图片格式支持.jpg / .jpeg / .png<br>图片长宽比必须与输入图片相同（即Image字段），否则任务失败（failed）<br>StaticMask和 DynamicMasks.Mask这两张图片的分辨率必须一致，否则任务失败（failed）</p>
        :rtype: str
        """
        return self._StaticMask

    @StaticMask.setter
    def StaticMask(self, StaticMask):
        self._StaticMask = StaticMask

    @property
    def DynamicMasks(self):
        r"""<p>动态笔刷配置列表<br>可配置多组（最多6组），每组包含“涂抹区域 Mask”与“运动轨迹 Trajectories”序列</p>
        :rtype: list of DynamicMask
        """
        return self._DynamicMasks

    @DynamicMasks.setter
    def DynamicMasks(self, DynamicMasks):
        self._DynamicMasks = DynamicMasks

    @property
    def CameraControl(self):
        r"""<p>控制摄像机运动的协议（如未指定，模型将根据输入的文本/图片进行智能匹配）</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.CameraControl`
        """
        return self._CameraControl

    @CameraControl.setter
    def CameraControl(self, CameraControl):
        self._CameraControl = CameraControl

    @property
    def CallbackUrl(self):
        r"""<p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def VoiceList(self):
        r"""<p>生成视频时所引用的音色的列表</p><p>一次视频生成任务至多引用2个音色<br>当VoiceList参数不为空且Prompt参数中引用音色ID时，视频生成任务按“有指定音色”计量计费<br>VoiceId参数值通过音色定制接口返回，也可使用系统预置音色，详见音色定制相关API；非对口型API的VoiceId<br>ElementList参数与VoiceList参数互斥，不能共存<br>v3模型不支持指定音色<br>用key:value承载，如下：<br>&quot;VoiceList&quot;:[<br>  {&quot;VoiceId&quot;:&quot;VoiceId_1&quot;},<br>  {&quot;VoiceId&quot;:&quot;VoiceId_2&quot;}<br>]</p>
        :rtype: list of Voice
        """
        return self._VoiceList

    @VoiceList.setter
    def VoiceList(self, VoiceList):
        self._VoiceList = VoiceList


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        if params.get("ImageTail") is not None:
            self._ImageTail = Image()
            self._ImageTail._deserialize(params.get("ImageTail"))
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Duration = params.get("Duration")
        self._Mode = params.get("Mode")
        self._CfgScale = params.get("CfgScale")
        self._Sound = params.get("Sound")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._MultiShot = params.get("MultiShot")
        self._ShotType = params.get("ShotType")
        if params.get("MultiPrompt") is not None:
            self._MultiPrompt = []
            for item in params.get("MultiPrompt"):
                obj = MultiPrompt()
                obj._deserialize(item)
                self._MultiPrompt.append(obj)
        if params.get("ElementList") is not None:
            self._ElementList = []
            for item in params.get("ElementList"):
                obj = Element()
                obj._deserialize(item)
                self._ElementList.append(obj)
        self._StaticMask = params.get("StaticMask")
        if params.get("DynamicMasks") is not None:
            self._DynamicMasks = []
            for item in params.get("DynamicMasks"):
                obj = DynamicMask()
                obj._deserialize(item)
                self._DynamicMasks.append(obj)
        if params.get("CameraControl") is not None:
            self._CameraControl = CameraControl()
            self._CameraControl._deserialize(params.get("CameraControl"))
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("VoiceList") is not None:
            self._VoiceList = []
            for item in params.get("VoiceList"):
                obj = Voice()
                obj._deserialize(item)
                self._VoiceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageToVideoJobResponse(AbstractModel):
    r"""SubmitImageToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitImageToVideoViduJobRequest(AbstractModel):
    r"""SubmitImageToVideoViduJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Images: <p>上传单张图时【首帧生视频】：</p><p>模型将以此参数中传入的图片为首帧画面来生成视频。<br>注1：支持传入图片 Base64 编码或图片URL（确保可访问）；<br>注2：支持上传1 张图；<br>注3：图片支持 png、jpeg、jpg、webp格式；<br>注4：图片比例需要小于 1:4 或者 4:1 ；<br>注5：图片大小不超过50M。</p><p>上传两张图时【首尾帧生视频】：<br>上传的第一张图片视作首帧图，第二张图片视作尾帧图，模型将以此参数中传入的图片来生成视频<br>注1: 首尾帧两张输入图的分辨率需相近，首帧图的分辨率/尾帧图的分辨率要在0.8～1.25之间。且图片比例需要小于1:4或者4:1；<br>注2: 支持传入图片 Base64 编码或图片URL（确保可访问）；<br>注3: 图片支持 png、jpeg、jpg、webp格式；<br>注4: 图片大小不超过50M；</p>
        :type Images: list of str
        :param _Model: <p>模型名称，可选值，默认值viduq2-turbo</p><ul><li>viduq2-pro：新模型，效果好，细节丰富</li><li>viduq2-turbo：新模型，效果好，生成快</li><li>viduq3-turbo：对比viduq3-pro，生成速度更快</li><li>viduq3-pro：高效生成优质音视频内容，让视频内容更生动、更形象、更立体，效果更好</li></ul>
        :type Model: str
        :param _Prompt: <p>文本提示词<br>生成视频的文本描述。<br>注1：字符长度不能超过 2000 个字符<br>注2：若使用is_rec推荐提示词参数，模型将不考虑此参数所输入的提示词</p>
        :type Prompt: str
        :param _IsRec: <p>是否使用推荐提示词，默认关闭<br>-true：是，由系统自动推荐提示词，并使用提示词内容生成视频，推荐提示词数量=1<br>-false：否，根据输入的prompt生成视频<br>注意：启用推荐提示词后，每个任务多消耗1积分</p>
        :type IsRec: bool
        :param _Audio: <p>【首帧生视频】</p><p>是否使用音视频直出能力，默认关闭，枚举值为：</p><ul><li>false：不需要音视频直出，输出静音视频</li><li>true：需要音视频直出，输出带台词以及背景音的视频<br>注1：该参数为true时，voice_id参数才生效<br>注2：该参数为true时，仅q3模型支持错峰<br>注3：当model 为q3-pro或q3-turbo 时，该参数默认值为true</li></ul><p>【首尾帧生视频】</p><ul><li>false：不需要音视频直出，输出静音视频</li><li>true：需要音画同步，输出声音的视频（包括台词和音效）<br>注1：仅q3系列模型支持该参数</li></ul>
        :type Audio: bool
        :param _VoiceId: <p>音色id<br>用来决定视频中的声音音色，为空时系统会自动推荐，可选枚举值参考列表：新音色列表<br>暂不支持声音复刻功能</p>
        :type VoiceId: str
        :param _Duration: <p>视频时长参数：<br>【首帧生视频】：<br>viduq3-pro、viduq3-turboxa0默认为 5，可选：1 - 16<br>viduq2-pro、viduq2-turboxa0默认为 5，可选：1 - 10</p><p>【首尾帧生视频】：<br>viduq3-proxa0、viduq3-turbo默认为 5，可选：1 - 16<br>viduq2-pro、viduq2-turboxa0默认为 5，可选：1 - 8</p>
        :type Duration: int
        :param _Resolution: <p>分辨率参数<br>【首帧生视频】：</p><ul><li>viduq3-pro 、viduq3-turbo 1-16秒：默认 720p，可选：540p、720p、1080p</li><li>viduq2-pro、viduq2-turbo 1-10秒：默认 720p，可选：720p、1080p<br>示例值：720p</li></ul><p>【首尾帧生视频】：<br>-xa0viduq3-proxa0、viduq3-turbo1-16秒：默认 720p，可选：540p、720p、1080p<br>-xa0viduq2-proxa0、xa0viduq2-turbo1-8秒：默认 720p，可选：540p、720p、1080p</p>
        :type Resolution: str
        :param _MovementAmplitude: <p>运动幅度<br>默认 auto，可选值：auto、small、medium、large<br>注：q2、q3系列模型改参数不生效</p>
        :type MovementAmplitude: str
        :param _Bgm: <p>bgm</p>
        :type Bgm: bool
        :param _AudioType: <p>音频类型，audio为true时必填，默认为all<br>注：该参数目前仅支持q2、q1、2.0系列模型的音频拆分</p><p>枚举值：</p><ul><li>all： 音效+人声</li><li>speech_only： 仅人声</li><li>sound_effect_only： 仅音效</li></ul>
        :type AudioType: str
        :param _MetaData: <p>元数据标识，json格式字符串，透传字段，您可以 自定义格式 或使用 示例格式 ，示例如下：<br>{<br>&quot;Label&quot;: &quot;your_label&quot;,<br>&quot;ContentProducer&quot;: &quot;your_content_producer&quot;,<br>&quot;ContentPropagator&quot;: &quot;your_content_propagator&quot;,<br>&quot;ProduceID&quot;: &quot;your_product_id&quot;,<br>&quot;PropagateID&quot;: &quot;your_propagate_id&quot;,<br>&quot;ReservedCode1&quot;: &quot;your_reserved_code1&quot;,<br>&quot;ReservedCode2&quot;: &quot;your_reserved_code2&quot;<br>}<br>该参数为空时，默认使用vidu生成的元数据标识</p>
        :type MetaData: str
        :param _CallbackUrl: <p>Callback 协议<br>需要您在创建任务时主动设置 callback_url，请求方法为 POST，当视频生成完成时，将向此地址发送包含任务最新状态的回调请求。回调请求内容结构与查询任务API的返回体一致<br>回调返回的&quot;status&quot;包括以下状态：</p><ul><li>success 任务完成（如发送失败，回调三次）</li><li>failed 任务失败（如发送失败，回调三次）</li></ul>
        :type CallbackUrl: str
        :param _Payload: <p>透传参数<br>不做任何处理，仅数据传输<br>注：最多 1048576个字符</p>
        :type Payload: str
        :param _OffPeak: <p>错峰模式，默认为：false，可选值：</p><ul><li>true：错峰生成视频；</li><li>false：即时生成视频；<br>注1：错峰模式消耗的积分更低<br>注2：错峰模式下提交的任务，会在48小时内生成，未能完成的任务会被自动取消，并返还该任务的积分</li></ul>
        :type OffPeak: bool
        :param _LogoAdd: <p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Images = None
        self._Model = None
        self._Prompt = None
        self._IsRec = None
        self._Audio = None
        self._VoiceId = None
        self._Duration = None
        self._Resolution = None
        self._MovementAmplitude = None
        self._Bgm = None
        self._AudioType = None
        self._MetaData = None
        self._CallbackUrl = None
        self._Payload = None
        self._OffPeak = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Images(self):
        r"""<p>上传单张图时【首帧生视频】：</p><p>模型将以此参数中传入的图片为首帧画面来生成视频。<br>注1：支持传入图片 Base64 编码或图片URL（确保可访问）；<br>注2：支持上传1 张图；<br>注3：图片支持 png、jpeg、jpg、webp格式；<br>注4：图片比例需要小于 1:4 或者 4:1 ；<br>注5：图片大小不超过50M。</p><p>上传两张图时【首尾帧生视频】：<br>上传的第一张图片视作首帧图，第二张图片视作尾帧图，模型将以此参数中传入的图片来生成视频<br>注1: 首尾帧两张输入图的分辨率需相近，首帧图的分辨率/尾帧图的分辨率要在0.8～1.25之间。且图片比例需要小于1:4或者4:1；<br>注2: 支持传入图片 Base64 编码或图片URL（确保可访问）；<br>注3: 图片支持 png、jpeg、jpg、webp格式；<br>注4: 图片大小不超过50M；</p>
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Model(self):
        r"""<p>模型名称，可选值，默认值viduq2-turbo</p><ul><li>viduq2-pro：新模型，效果好，细节丰富</li><li>viduq2-turbo：新模型，效果好，生成快</li><li>viduq3-turbo：对比viduq3-pro，生成速度更快</li><li>viduq3-pro：高效生成优质音视频内容，让视频内容更生动、更形象、更立体，效果更好</li></ul>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Prompt(self):
        r"""<p>文本提示词<br>生成视频的文本描述。<br>注1：字符长度不能超过 2000 个字符<br>注2：若使用is_rec推荐提示词参数，模型将不考虑此参数所输入的提示词</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def IsRec(self):
        r"""<p>是否使用推荐提示词，默认关闭<br>-true：是，由系统自动推荐提示词，并使用提示词内容生成视频，推荐提示词数量=1<br>-false：否，根据输入的prompt生成视频<br>注意：启用推荐提示词后，每个任务多消耗1积分</p>
        :rtype: bool
        """
        return self._IsRec

    @IsRec.setter
    def IsRec(self, IsRec):
        self._IsRec = IsRec

    @property
    def Audio(self):
        r"""<p>【首帧生视频】</p><p>是否使用音视频直出能力，默认关闭，枚举值为：</p><ul><li>false：不需要音视频直出，输出静音视频</li><li>true：需要音视频直出，输出带台词以及背景音的视频<br>注1：该参数为true时，voice_id参数才生效<br>注2：该参数为true时，仅q3模型支持错峰<br>注3：当model 为q3-pro或q3-turbo 时，该参数默认值为true</li></ul><p>【首尾帧生视频】</p><ul><li>false：不需要音视频直出，输出静音视频</li><li>true：需要音画同步，输出声音的视频（包括台词和音效）<br>注1：仅q3系列模型支持该参数</li></ul>
        :rtype: bool
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def VoiceId(self):
        r"""<p>音色id<br>用来决定视频中的声音音色，为空时系统会自动推荐，可选枚举值参考列表：新音色列表<br>暂不支持声音复刻功能</p>
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId

    @property
    def Duration(self):
        r"""<p>视频时长参数：<br>【首帧生视频】：<br>viduq3-pro、viduq3-turboxa0默认为 5，可选：1 - 16<br>viduq2-pro、viduq2-turboxa0默认为 5，可选：1 - 10</p><p>【首尾帧生视频】：<br>viduq3-proxa0、viduq3-turbo默认为 5，可选：1 - 16<br>viduq2-pro、viduq2-turboxa0默认为 5，可选：1 - 8</p>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Resolution(self):
        r"""<p>分辨率参数<br>【首帧生视频】：</p><ul><li>viduq3-pro 、viduq3-turbo 1-16秒：默认 720p，可选：540p、720p、1080p</li><li>viduq2-pro、viduq2-turbo 1-10秒：默认 720p，可选：720p、1080p<br>示例值：720p</li></ul><p>【首尾帧生视频】：<br>-xa0viduq3-proxa0、viduq3-turbo1-16秒：默认 720p，可选：540p、720p、1080p<br>-xa0viduq2-proxa0、xa0viduq2-turbo1-8秒：默认 720p，可选：540p、720p、1080p</p>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MovementAmplitude(self):
        r"""<p>运动幅度<br>默认 auto，可选值：auto、small、medium、large<br>注：q2、q3系列模型改参数不生效</p>
        :rtype: str
        """
        return self._MovementAmplitude

    @MovementAmplitude.setter
    def MovementAmplitude(self, MovementAmplitude):
        self._MovementAmplitude = MovementAmplitude

    @property
    def Bgm(self):
        r"""<p>bgm</p>
        :rtype: bool
        """
        return self._Bgm

    @Bgm.setter
    def Bgm(self, Bgm):
        self._Bgm = Bgm

    @property
    def AudioType(self):
        r"""<p>音频类型，audio为true时必填，默认为all<br>注：该参数目前仅支持q2、q1、2.0系列模型的音频拆分</p><p>枚举值：</p><ul><li>all： 音效+人声</li><li>speech_only： 仅人声</li><li>sound_effect_only： 仅音效</li></ul>
        :rtype: str
        """
        return self._AudioType

    @AudioType.setter
    def AudioType(self, AudioType):
        self._AudioType = AudioType

    @property
    def MetaData(self):
        r"""<p>元数据标识，json格式字符串，透传字段，您可以 自定义格式 或使用 示例格式 ，示例如下：<br>{<br>&quot;Label&quot;: &quot;your_label&quot;,<br>&quot;ContentProducer&quot;: &quot;your_content_producer&quot;,<br>&quot;ContentPropagator&quot;: &quot;your_content_propagator&quot;,<br>&quot;ProduceID&quot;: &quot;your_product_id&quot;,<br>&quot;PropagateID&quot;: &quot;your_propagate_id&quot;,<br>&quot;ReservedCode1&quot;: &quot;your_reserved_code1&quot;,<br>&quot;ReservedCode2&quot;: &quot;your_reserved_code2&quot;<br>}<br>该参数为空时，默认使用vidu生成的元数据标识</p>
        :rtype: str
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def CallbackUrl(self):
        r"""<p>Callback 协议<br>需要您在创建任务时主动设置 callback_url，请求方法为 POST，当视频生成完成时，将向此地址发送包含任务最新状态的回调请求。回调请求内容结构与查询任务API的返回体一致<br>回调返回的&quot;status&quot;包括以下状态：</p><ul><li>success 任务完成（如发送失败，回调三次）</li><li>failed 任务失败（如发送失败，回调三次）</li></ul>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Payload(self):
        r"""<p>透传参数<br>不做任何处理，仅数据传输<br>注：最多 1048576个字符</p>
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def OffPeak(self):
        r"""<p>错峰模式，默认为：false，可选值：</p><ul><li>true：错峰生成视频；</li><li>false：即时生成视频；<br>注1：错峰模式消耗的积分更低<br>注2：错峰模式下提交的任务，会在48小时内生成，未能完成的任务会被自动取消，并返还该任务的积分</li></ul>
        :rtype: bool
        """
        return self._OffPeak

    @OffPeak.setter
    def OffPeak(self, OffPeak):
        self._OffPeak = OffPeak

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Images = params.get("Images")
        self._Model = params.get("Model")
        self._Prompt = params.get("Prompt")
        self._IsRec = params.get("IsRec")
        self._Audio = params.get("Audio")
        self._VoiceId = params.get("VoiceId")
        self._Duration = params.get("Duration")
        self._Resolution = params.get("Resolution")
        self._MovementAmplitude = params.get("MovementAmplitude")
        self._Bgm = params.get("Bgm")
        self._AudioType = params.get("AudioType")
        self._MetaData = params.get("MetaData")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Payload = params.get("Payload")
        self._OffPeak = params.get("OffPeak")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitImageToVideoViduJobResponse(AbstractModel):
    r"""SubmitImageToVideoViduJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitMotionControlKlingJobRequest(AbstractModel):
    r"""SubmitMotionControlKlingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: <p>模型名称  枚举值：kling-v2-6, kling-v3。</p>
        :type Model: str
        :param _Prompt: <p>文本提示词，可包含正向描述和负向描述</p><p>可将提示词模板化来满足不同的视频生成需求</p><p>不能超过2500个字</p>
        :type Prompt: str
        :param _Image: <p>参考图像，生成视频中的人物、背景等元素均以参考图为准  视频内容需满足以下要求：  人物比例尽量与参考动作比例一致，尽量避免全身动作驱动半身人物进行生成  人物需要露出清晰的上半身或全身的肢体及头部，避免遮挡  画面中人物避免存在极端朝向，比如倒立、平卧等。人物占画面比例不得太低  支持真实/风格化的角色（包括人物/类人动物/部分纯动物/部分类人肢体比例的角色）通过  包含支持传入图片Base64编码或图片URL（确保可访问）。</p>
        :type Image: str
        :param _Video: <p>参考视频的获取链接。生成视频中的人物动作与参考视频一致。  视频内容需满足以下要求：  人物需要漏出清晰的上半身或全身的全部肢体及头部，避免遮挡  建议上传1人动作视频，2人及以上会取画面占比最大的人物动作进行生成  推荐使用真人动作，部分风格化的人物/类人肢体比例可以通过  动作视频一镜到底，角色始终出现在画面中，避免切镜、运镜等。否则会被截取  动作避免过快，相对平稳的动作生成效果更佳  视频文件支持.mp4/.mov，文件大小不超过100MB，仅支持长宽的边长均位于340px~3850px之间，上述校验不通过会返回错误码等信息  视频时长下限不短于3秒，时长上限与人物朝向参考（character_orientation）有关：  当人物朝向与视频中人物一致时，视频时长最长可达30秒；  当人物朝向与图片中人物一致时，视频时长最长可达10秒；  如果您的动作难度比较高、速度比较快，有一定概率生成不足上传视频时长的结果，因为模型只能提取有效动作时长进行生成，最短提取出3s可用连续动作即可生成。请注意，因此消耗的积分将无法退还，建议适当调整动作难度与速度  系统会校验视频内容，如有问题会返回错误码等信息。</p>
        :type Video: str
        :param _Mode: <p>生成视频的模式</p><p>枚举值：std，pro<br>其中std：标准模式（标准），基础模式，性价比高<br>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</p>
        :type Mode: str
        :param _KeepOriginalSound: <p>可选择是否保留视频原声  枚举值：yes，no  其中yes：保留视频原声  其中no：不保留视频原声。</p>
        :type KeepOriginalSound: str
        :param _CharacterOrientation: <p>生成视频中人物的朝向，可选择与图片一致或与视频一致  枚举值：image，video，其中：  其中image：与图片中人物朝向一致；此时参考视频时长不得超过10秒；  其中video：与视频中人物朝向一致；此时参考视频时长不得超过30秒；  引用主体时，生成的视频暂时只能参考视频中的人物朝向。</p>
        :type CharacterOrientation: str
        :param _ElementList: <p>参考主体列表  基于主体库中主体的ID配置，用key:value承载，如下：  &quot;element_list&quot;:[     {        &quot;element_id&quot;:long   },   {        &quot;element_id&quot;:long   } ] 参考主体数量与有无参考视频、参考图片数量有关，其中：  当使用首帧生成视频时，最多支持3个主体；  当使用首尾帧生成视频时，kling-v3-omni模型最多支持3个主体，kling-video-o1模不支持主体；  有参考视频时，参考图片数量和参考主体数量之和不得超过4，且不支持使用视频角色主体；  无参考视频时，参考图片数量和参考主体数量之和不得超过7；</p>
        :type ElementList: list of Element
        :param _CallbackUrl: <p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :type CallbackUrl: str
        :param _LogoAdd: <p>为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Model = None
        self._Prompt = None
        self._Image = None
        self._Video = None
        self._Mode = None
        self._KeepOriginalSound = None
        self._CharacterOrientation = None
        self._ElementList = None
        self._CallbackUrl = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Model(self):
        r"""<p>模型名称  枚举值：kling-v2-6, kling-v3。</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Prompt(self):
        r"""<p>文本提示词，可包含正向描述和负向描述</p><p>可将提示词模板化来满足不同的视频生成需求</p><p>不能超过2500个字</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Image(self):
        r"""<p>参考图像，生成视频中的人物、背景等元素均以参考图为准  视频内容需满足以下要求：  人物比例尽量与参考动作比例一致，尽量避免全身动作驱动半身人物进行生成  人物需要露出清晰的上半身或全身的肢体及头部，避免遮挡  画面中人物避免存在极端朝向，比如倒立、平卧等。人物占画面比例不得太低  支持真实/风格化的角色（包括人物/类人动物/部分纯动物/部分类人肢体比例的角色）通过  包含支持传入图片Base64编码或图片URL（确保可访问）。</p>
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Video(self):
        r"""<p>参考视频的获取链接。生成视频中的人物动作与参考视频一致。  视频内容需满足以下要求：  人物需要漏出清晰的上半身或全身的全部肢体及头部，避免遮挡  建议上传1人动作视频，2人及以上会取画面占比最大的人物动作进行生成  推荐使用真人动作，部分风格化的人物/类人肢体比例可以通过  动作视频一镜到底，角色始终出现在画面中，避免切镜、运镜等。否则会被截取  动作避免过快，相对平稳的动作生成效果更佳  视频文件支持.mp4/.mov，文件大小不超过100MB，仅支持长宽的边长均位于340px~3850px之间，上述校验不通过会返回错误码等信息  视频时长下限不短于3秒，时长上限与人物朝向参考（character_orientation）有关：  当人物朝向与视频中人物一致时，视频时长最长可达30秒；  当人物朝向与图片中人物一致时，视频时长最长可达10秒；  如果您的动作难度比较高、速度比较快，有一定概率生成不足上传视频时长的结果，因为模型只能提取有效动作时长进行生成，最短提取出3s可用连续动作即可生成。请注意，因此消耗的积分将无法退还，建议适当调整动作难度与速度  系统会校验视频内容，如有问题会返回错误码等信息。</p>
        :rtype: str
        """
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Mode(self):
        r"""<p>生成视频的模式</p><p>枚举值：std，pro<br>其中std：标准模式（标准），基础模式，性价比高<br>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</p>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def KeepOriginalSound(self):
        r"""<p>可选择是否保留视频原声  枚举值：yes，no  其中yes：保留视频原声  其中no：不保留视频原声。</p>
        :rtype: str
        """
        return self._KeepOriginalSound

    @KeepOriginalSound.setter
    def KeepOriginalSound(self, KeepOriginalSound):
        self._KeepOriginalSound = KeepOriginalSound

    @property
    def CharacterOrientation(self):
        r"""<p>生成视频中人物的朝向，可选择与图片一致或与视频一致  枚举值：image，video，其中：  其中image：与图片中人物朝向一致；此时参考视频时长不得超过10秒；  其中video：与视频中人物朝向一致；此时参考视频时长不得超过30秒；  引用主体时，生成的视频暂时只能参考视频中的人物朝向。</p>
        :rtype: str
        """
        return self._CharacterOrientation

    @CharacterOrientation.setter
    def CharacterOrientation(self, CharacterOrientation):
        self._CharacterOrientation = CharacterOrientation

    @property
    def ElementList(self):
        r"""<p>参考主体列表  基于主体库中主体的ID配置，用key:value承载，如下：  &quot;element_list&quot;:[     {        &quot;element_id&quot;:long   },   {        &quot;element_id&quot;:long   } ] 参考主体数量与有无参考视频、参考图片数量有关，其中：  当使用首帧生成视频时，最多支持3个主体；  当使用首尾帧生成视频时，kling-v3-omni模型最多支持3个主体，kling-video-o1模不支持主体；  有参考视频时，参考图片数量和参考主体数量之和不得超过4，且不支持使用视频角色主体；  无参考视频时，参考图片数量和参考主体数量之和不得超过7；</p>
        :rtype: list of Element
        """
        return self._ElementList

    @ElementList.setter
    def ElementList(self, ElementList):
        self._ElementList = ElementList

    @property
    def CallbackUrl(self):
        r"""<p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def LogoAdd(self):
        r"""<p>为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Prompt = params.get("Prompt")
        self._Image = params.get("Image")
        self._Video = params.get("Video")
        self._Mode = params.get("Mode")
        self._KeepOriginalSound = params.get("KeepOriginalSound")
        self._CharacterOrientation = params.get("CharacterOrientation")
        if params.get("ElementList") is not None:
            self._ElementList = []
            for item in params.get("ElementList"):
                obj = Element()
                obj._deserialize(item)
                self._ElementList.append(obj)
        self._CallbackUrl = params.get("CallbackUrl")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitMotionControlKlingJobResponse(AbstractModel):
    r"""SubmitMotionControlKlingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitPortraitSingJobRequest(AbstractModel):
    r"""SubmitPortraitSingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AudioUrl: 传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav、m4a
        :type AudioUrl: str
        :param _ImageUrl: 传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:2到2:1范围内
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :type ImageUrl: str
        :param _ImageBase64: 传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageBase64为准。
        :type ImageBase64: str
        :param _Mode: 唱演模式，默认使用人像模式。
Person：人像模式，仅支持上传人像图片，人像生成效果更好，如果图中未检测到有效人脸将被拦截，生成时会将视频短边分辨率放缩至512。
Pet：宠物模式，支持宠物等非人像图片，固定生成512:512分辨率视频。
        :type Mode: str
        :param _Resolution: 生成视频尺寸。可选取值："512:512"。

人像模式下，如果不传该参数，默认生成视频的短边分辨率为512，长边分辨率不固定、由模型根据生成效果自动适配得到。如需固定生成分辨率可传入512:512。

宠物模式下，如果不传该参数，默认将脸部唱演视频回贴原图，生成视频分辨率与原图一致。如不需要脸部回贴，仅保留脸部唱演视频，可传入512:512。
        :type Resolution: str
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 
1：添加标识；
 0：不添加标识；
其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._AudioUrl = None
        self._ImageUrl = None
        self._ImageBase64 = None
        self._Mode = None
        self._Resolution = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def AudioUrl(self):
        r"""传入音频URL地址，音频要求：
- 音频时长：2秒 - 60秒
- 音频格式：mp3、wav、m4a
        :rtype: str
        """
        return self._AudioUrl

    @AudioUrl.setter
    def AudioUrl(self, AudioUrl):
        self._AudioUrl = AudioUrl

    @property
    def ImageUrl(self):
        r"""传入图片URL地址，图片要求：
- 图片格式：jpg、jpeg、png、bmp、webp
- 图片分辨率：192～4096
- 图片大小：不超过10M
- 图片宽高比：图片【宽：高】在1:2到2:1范围内
- 图片内容：避免上传无人脸、无宠物脸或脸部过小、不完整、不清晰、偏转角度过大、嘴部被遮挡的图片。
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageBase64(self):
        r"""传入图片Base64编码，编码后请求体大小不超过10M。
图片Base64编码与URL地址必传其一，如果都传以ImageBase64为准。
        :rtype: str
        """
        return self._ImageBase64

    @ImageBase64.setter
    def ImageBase64(self, ImageBase64):
        self._ImageBase64 = ImageBase64

    @property
    def Mode(self):
        r"""唱演模式，默认使用人像模式。
Person：人像模式，仅支持上传人像图片，人像生成效果更好，如果图中未检测到有效人脸将被拦截，生成时会将视频短边分辨率放缩至512。
Pet：宠物模式，支持宠物等非人像图片，固定生成512:512分辨率视频。
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Resolution(self):
        r"""生成视频尺寸。可选取值："512:512"。

人像模式下，如果不传该参数，默认生成视频的短边分辨率为512，长边分辨率不固定、由模型根据生成效果自动适配得到。如需固定生成分辨率可传入512:512。

宠物模式下，如果不传该参数，默认将脸部唱演视频回贴原图，生成视频分辨率与原图一致。如不需要脸部回贴，仅保留脸部唱演视频，可传入512:512。
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 
1：添加标识；
 0：不添加标识；
其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._AudioUrl = params.get("AudioUrl")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageBase64 = params.get("ImageBase64")
        self._Mode = params.get("Mode")
        self._Resolution = params.get("Resolution")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitPortraitSingJobResponse(AbstractModel):
    r"""SubmitPortraitSingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。任务有效期为48小时。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID。任务有效期为48小时。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitReferenceToVideoViduJobRequest(AbstractModel):
    r"""SubmitReferenceToVideoViduJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>文本提示词<br>生成视频的文本描述。<br>注1：字符长度不能超过 2000 个字符<br>注2：使用Subjects主体参数时，可以通过@主体id 来表示主体内容，例如：&quot;@1 和 @2 在一起吃火锅，并且旁白音说火锅大家都爱吃。&quot;</p>
        :type Prompt: str
        :param _Images: <p>图像参考<br>【非主体调用时传入】<br>支持上传1～7张图片，模型将以此参数中传入的图片中的主题为参考生成具备主体一致的视频。<br>支持传入图片 Base64 编码或图片URL（确保可访问）<br>图片支持 png、jpeg、jpg、webp格式<br>图片像素不能小于 128*128，且比例需要小于1:4或者4:1，且大小不超过50M。</p>
        :type Images: list of str
        :param _Subjects: <p>参考生图主体信息，支持1-7个主体，主体图片共1 ～ 7张<br>【主体调用时传入】</p>
        :type Subjects: list of ReferenceSubject
        :param _Videos: <p>视频参考支持上传1～2个视频，模型将以此参数中传入的视频作为参考，生成具备主体一致的视频。<br>注1： 仅viduq2-pro模型支持该参数<br>注2：使用视频参考功能时，最多支持上传 1个8秒 视频 或 2个5秒 视频<br>注3：视频支持 mp4、avi、mov格式<br>注4：视频像素不能小于 128*128，且比例需要小于1:4或者4:1，且大小不超过100M。</p>
        :type Videos: list of str
        :param _Model: <p>模型名称，可选值，当前仅可并且默认viduq2</p><ul><li>viduq2：最新模型</li></ul>
        :type Model: str
        :param _Audio: <p>是否使用音视频直出能力，默认false，可选值 true、false</p><ul><li>true：使用音视频直出能力。</li><li>false：不使用音视频直出能力。<br>仅上传主体时支持此功能</li></ul>
        :type Audio: bool
        :param _AudioType: <p>音频类型，audio为true时必填，默认为all</p><p>枚举值：</p><ul><li>all： 音效+人声</li><li>speech_only： 仅人声</li><li>sound_effect_only： 仅音效</li></ul>
        :type AudioType: str
        :param _Bgm: <p>是否为生成的视频添加背景音乐。<br>默认：false，可选值 true 、false<br>【仅支持非主体调用时生效】</p><ul><li>传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。</li><li>BGM不限制时长，系统根据视频时长自动适配</li><li>BGM参数在q2系列模型的duration为 9秒 或 10秒 时不生效</li></ul>
        :type Bgm: bool
        :param _Duration: <p>视频时长参数：<br>默认5秒，可选：1-10（整数）</p>
        :type Duration: int
        :param _AspectRatio: <p>比例<br>默认值：16:9<br>【非主体调用时】<br>可选值如下：16:9、9:16、4:3、3:4、1:1</p><p>【主体调用时】<br>可选值如下：16:9、9:16、1:1<br>注：q2模型 支持任意宽高比</p>
        :type AspectRatio: str
        :param _Resolution: <p>分辨率参数<br>默认 720p, 可选：540p、720p、1080p</p>
        :type Resolution: str
        :param _MovementAmplitude: <p>运动幅度默认 auto，可选值：auto、small、medium、large<br>注：使用q2系列模型时该参数不生效</p>
        :type MovementAmplitude: str
        :param _MetaData: <p>元数据标识，json格式字符串，透传字段，您可以 自定义格式 或使用 示例格式 ，示例如下：<br>{<br>&quot;Label&quot;: &quot;your_label&quot;,&quot;ContentProducer&quot;: &quot;yourcontentproducer&quot;,&quot;ContentPropagator&quot;: &quot;your_content_propagator&quot;,&quot;ProduceID&quot;: &quot;yourproductid&quot;, &quot;PropagateID&quot;: &quot;your_propagate_id&quot;,&quot;ReservedCode1&quot;: &quot;yourreservedcode1&quot;, &quot;ReservedCode2&quot;: &quot;your_reserved_code2&quot;<br>}<br>该参数为空时，默认使用vidu生成的元数据标识</p>
        :type MetaData: str
        :param _CallbackUrl: <p>Callback 协议<br>需要您在创建任务时主动设置 callback_url，请求方法为 POST，当视频生成完成时，将向此地址发送包含任务最新状态的回调请求。回调请求内容结构与查询任务API的返回体一致<br>回调返回的&quot;status&quot;包括以下状态：</p><ul><li>success 任务完成（如发送失败，回调三次）</li><li>failed 任务失败（如发送失败，回调三次）</li></ul>
        :type CallbackUrl: str
        :param _Payload: <p>透传参数不做任何处理，仅数据传输注：最多 1048576个字符</p>
        :type Payload: str
        :param _OffPeak: <p>错峰模式，默认为：false，可选值：</p><ul><li>true：错峰生成视频；</li><li>false：即时生成视频；<br>注1：错峰模式消耗的积分更低<br>注2：错峰模式下提交的任务，会在48小时内生成，未能完成的任务会被自动取消，并返还该任务的积分</li></ul>
        :type OffPeak: bool
        :param _LogoAdd: <p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Prompt = None
        self._Images = None
        self._Subjects = None
        self._Videos = None
        self._Model = None
        self._Audio = None
        self._AudioType = None
        self._Bgm = None
        self._Duration = None
        self._AspectRatio = None
        self._Resolution = None
        self._MovementAmplitude = None
        self._MetaData = None
        self._CallbackUrl = None
        self._Payload = None
        self._OffPeak = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        r"""<p>文本提示词<br>生成视频的文本描述。<br>注1：字符长度不能超过 2000 个字符<br>注2：使用Subjects主体参数时，可以通过@主体id 来表示主体内容，例如：&quot;@1 和 @2 在一起吃火锅，并且旁白音说火锅大家都爱吃。&quot;</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Images(self):
        r"""<p>图像参考<br>【非主体调用时传入】<br>支持上传1～7张图片，模型将以此参数中传入的图片中的主题为参考生成具备主体一致的视频。<br>支持传入图片 Base64 编码或图片URL（确保可访问）<br>图片支持 png、jpeg、jpg、webp格式<br>图片像素不能小于 128*128，且比例需要小于1:4或者4:1，且大小不超过50M。</p>
        :rtype: list of str
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Subjects(self):
        r"""<p>参考生图主体信息，支持1-7个主体，主体图片共1 ～ 7张<br>【主体调用时传入】</p>
        :rtype: list of ReferenceSubject
        """
        return self._Subjects

    @Subjects.setter
    def Subjects(self, Subjects):
        self._Subjects = Subjects

    @property
    def Videos(self):
        r"""<p>视频参考支持上传1～2个视频，模型将以此参数中传入的视频作为参考，生成具备主体一致的视频。<br>注1： 仅viduq2-pro模型支持该参数<br>注2：使用视频参考功能时，最多支持上传 1个8秒 视频 或 2个5秒 视频<br>注3：视频支持 mp4、avi、mov格式<br>注4：视频像素不能小于 128*128，且比例需要小于1:4或者4:1，且大小不超过100M。</p>
        :rtype: list of str
        """
        return self._Videos

    @Videos.setter
    def Videos(self, Videos):
        self._Videos = Videos

    @property
    def Model(self):
        r"""<p>模型名称，可选值，当前仅可并且默认viduq2</p><ul><li>viduq2：最新模型</li></ul>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Audio(self):
        r"""<p>是否使用音视频直出能力，默认false，可选值 true、false</p><ul><li>true：使用音视频直出能力。</li><li>false：不使用音视频直出能力。<br>仅上传主体时支持此功能</li></ul>
        :rtype: bool
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def AudioType(self):
        r"""<p>音频类型，audio为true时必填，默认为all</p><p>枚举值：</p><ul><li>all： 音效+人声</li><li>speech_only： 仅人声</li><li>sound_effect_only： 仅音效</li></ul>
        :rtype: str
        """
        return self._AudioType

    @AudioType.setter
    def AudioType(self, AudioType):
        self._AudioType = AudioType

    @property
    def Bgm(self):
        r"""<p>是否为生成的视频添加背景音乐。<br>默认：false，可选值 true 、false<br>【仅支持非主体调用时生效】</p><ul><li>传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。</li><li>BGM不限制时长，系统根据视频时长自动适配</li><li>BGM参数在q2系列模型的duration为 9秒 或 10秒 时不生效</li></ul>
        :rtype: bool
        """
        return self._Bgm

    @Bgm.setter
    def Bgm(self, Bgm):
        self._Bgm = Bgm

    @property
    def Duration(self):
        r"""<p>视频时长参数：<br>默认5秒，可选：1-10（整数）</p>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def AspectRatio(self):
        r"""<p>比例<br>默认值：16:9<br>【非主体调用时】<br>可选值如下：16:9、9:16、4:3、3:4、1:1</p><p>【主体调用时】<br>可选值如下：16:9、9:16、1:1<br>注：q2模型 支持任意宽高比</p>
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def Resolution(self):
        r"""<p>分辨率参数<br>默认 720p, 可选：540p、720p、1080p</p>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def MovementAmplitude(self):
        r"""<p>运动幅度默认 auto，可选值：auto、small、medium、large<br>注：使用q2系列模型时该参数不生效</p>
        :rtype: str
        """
        return self._MovementAmplitude

    @MovementAmplitude.setter
    def MovementAmplitude(self, MovementAmplitude):
        self._MovementAmplitude = MovementAmplitude

    @property
    def MetaData(self):
        r"""<p>元数据标识，json格式字符串，透传字段，您可以 自定义格式 或使用 示例格式 ，示例如下：<br>{<br>&quot;Label&quot;: &quot;your_label&quot;,&quot;ContentProducer&quot;: &quot;yourcontentproducer&quot;,&quot;ContentPropagator&quot;: &quot;your_content_propagator&quot;,&quot;ProduceID&quot;: &quot;yourproductid&quot;, &quot;PropagateID&quot;: &quot;your_propagate_id&quot;,&quot;ReservedCode1&quot;: &quot;yourreservedcode1&quot;, &quot;ReservedCode2&quot;: &quot;your_reserved_code2&quot;<br>}<br>该参数为空时，默认使用vidu生成的元数据标识</p>
        :rtype: str
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def CallbackUrl(self):
        r"""<p>Callback 协议<br>需要您在创建任务时主动设置 callback_url，请求方法为 POST，当视频生成完成时，将向此地址发送包含任务最新状态的回调请求。回调请求内容结构与查询任务API的返回体一致<br>回调返回的&quot;status&quot;包括以下状态：</p><ul><li>success 任务完成（如发送失败，回调三次）</li><li>failed 任务失败（如发送失败，回调三次）</li></ul>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Payload(self):
        r"""<p>透传参数不做任何处理，仅数据传输注：最多 1048576个字符</p>
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def OffPeak(self):
        r"""<p>错峰模式，默认为：false，可选值：</p><ul><li>true：错峰生成视频；</li><li>false：即时生成视频；<br>注1：错峰模式消耗的积分更低<br>注2：错峰模式下提交的任务，会在48小时内生成，未能完成的任务会被自动取消，并返还该任务的积分</li></ul>
        :rtype: bool
        """
        return self._OffPeak

    @OffPeak.setter
    def OffPeak(self, OffPeak):
        self._OffPeak = OffPeak

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Images = params.get("Images")
        if params.get("Subjects") is not None:
            self._Subjects = []
            for item in params.get("Subjects"):
                obj = ReferenceSubject()
                obj._deserialize(item)
                self._Subjects.append(obj)
        self._Videos = params.get("Videos")
        self._Model = params.get("Model")
        self._Audio = params.get("Audio")
        self._AudioType = params.get("AudioType")
        self._Bgm = params.get("Bgm")
        self._Duration = params.get("Duration")
        self._AspectRatio = params.get("AspectRatio")
        self._Resolution = params.get("Resolution")
        self._MovementAmplitude = params.get("MovementAmplitude")
        self._MetaData = params.get("MetaData")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Payload = params.get("Payload")
        self._OffPeak = params.get("OffPeak")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitReferenceToVideoViduJobResponse(AbstractModel):
    r"""SubmitReferenceToVideoViduJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitTemplateToVideoJobRequest(AbstractModel):
    r"""SubmitTemplateToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Template: <p>特效模板名称。请在 <a href="https://cloud.tencent.com/document/product/1616/119194">视频特效模板列表</a>  中选择想要生成的特效对应的 template 名称。</p>
        :type Template: str
        :param _Images: <p>参考图像，不同特效输入图片的数量详见： <a href="https://cloud.tencent.com/document/product/1616/119194">视频特效模板-图片要求说明</a></p><ul><li>支持传入图片Base64编码或图片URL（确保可访问）</li><li>图片格式：支持png、jpg、jpeg、webp、bmp、tiff</li><li>图片文件：大小不能超过10MB（base64后），图片分辨率不小于300×300px，不大于4096×4096，图片宽高比应在1:4 ~ 4:1之间</li></ul>
        :type Images: list of Image
        :param _LogoAdd: <p>为生成视频添加标识的开关，默认为1。传0 需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a> 申请开启显式标识自主完成后方可生效。<br>1：添加标识；<br>0：不添加标识；<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a> 申请开启显式标识自主完成。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        :param _Resolution: <p>视频输出分辨率，默认值：360p 。不同特效支持的清晰度及消耗积分数详见：<a href="https://cloud.tencent.com/document/product/1616/119194">视频特效模板-单次调用消耗积分数列</a></p>
        :type Resolution: str
        :param _BGM: <p>是否为生成的视频添加背景音乐。默认：false，  传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。</p>
        :type BGM: bool
        :param _ExtraParam: <p>扩展字段。</p>
        :type ExtraParam: :class:`tencentcloud.vclm.v20240523.models.ExtraParam`
        """
        self._Template = None
        self._Images = None
        self._LogoAdd = None
        self._LogoParam = None
        self._Resolution = None
        self._BGM = None
        self._ExtraParam = None

    @property
    def Template(self):
        r"""<p>特效模板名称。请在 <a href="https://cloud.tencent.com/document/product/1616/119194">视频特效模板列表</a>  中选择想要生成的特效对应的 template 名称。</p>
        :rtype: str
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Images(self):
        r"""<p>参考图像，不同特效输入图片的数量详见： <a href="https://cloud.tencent.com/document/product/1616/119194">视频特效模板-图片要求说明</a></p><ul><li>支持传入图片Base64编码或图片URL（确保可访问）</li><li>图片格式：支持png、jpg、jpeg、webp、bmp、tiff</li><li>图片文件：大小不能超过10MB（base64后），图片分辨率不小于300×300px，不大于4096×4096，图片宽高比应在1:4 ~ 4:1之间</li></ul>
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def LogoAdd(self):
        r"""<p>为生成视频添加标识的开关，默认为1。传0 需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a> 申请开启显式标识自主完成后方可生效。<br>1：添加标识；<br>0：不添加标识；<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a> 申请开启显式标识自主完成。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Resolution(self):
        r"""<p>视频输出分辨率，默认值：360p 。不同特效支持的清晰度及消耗积分数详见：<a href="https://cloud.tencent.com/document/product/1616/119194">视频特效模板-单次调用消耗积分数列</a></p>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def BGM(self):
        r"""<p>是否为生成的视频添加背景音乐。默认：false，  传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。</p>
        :rtype: bool
        """
        return self._BGM

    @BGM.setter
    def BGM(self, BGM):
        self._BGM = BGM

    @property
    def ExtraParam(self):
        r"""<p>扩展字段。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.ExtraParam`
        """
        return self._ExtraParam

    @ExtraParam.setter
    def ExtraParam(self, ExtraParam):
        self._ExtraParam = ExtraParam


    def _deserialize(self, params):
        self._Template = params.get("Template")
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._Resolution = params.get("Resolution")
        self._BGM = params.get("BGM")
        if params.get("ExtraParam") is not None:
            self._ExtraParam = ExtraParam()
            self._ExtraParam._deserialize(params.get("ExtraParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTemplateToVideoJobResponse(AbstractModel):
    r"""SubmitTemplateToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitTextToVideoJobRequest(AbstractModel):
    r"""SubmitTextToVideoJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>正向文本提示词。不能超过2500个字符</p>
        :type Prompt: str
        :param _Model: <p>模型名称。<br>v1.6：Kling-V1-6<br>v2.0：Kling-V2-Master<br>v2.5：Kling-V2-5-Turbo<br>v2.6：Kling-V2-6<br>v3.0：kling-v3</p>
        :type Model: str
        :param _NegativePrompt: <p>负向文本提示词。不能超过2500个字符</p>
        :type NegativePrompt: str
        :param _Duration: <p>生成视频时长，单位s。默认值为5。<br>枚举值：3，4，5，6，7，8，9，10，11，12，13，14，15</p><p>不同模型支持时长不同</p><ul><li>模型v1.6、v2.0、v2.5、v2.6：支持5、10</li><li>模型v3.0：支持3～15s</li></ul>
        :type Duration: str
        :param _Mode: <p>生成视频的模式；</p><p>枚举值：std，pro</p><ul><li>其中std：标准模式（标准），基础模式，性价比高</li><li>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</li></ul><p>不同模型版本、视频模式支持范围不同</p><ul><li>v1.6：std、pro。</li><li>v2.0、v3.0：模型无需配置。</li><li>v2.5：首尾帧情况下支持pro。</li><li>v2.6：仅支持pro，选择v2.6模型时，默认自动生成高品质pro视频。</li></ul>
        :type Mode: str
        :param _CfgScale: <p>生成视频的自由度；值越大，模型自由度越小，与用户输入的提示词相关性越强。<br>取值范围：[0, 1]<br>v2.0、v2.5、v2.6 模型不支持当前参数<br>默认值：0.5。</p>
        :type CfgScale: float
        :param _AspectRatio: <p>生成视频的画面纵横比（宽:高）<br>枚举值：16:9, 9:16, 1:1<br>默认值：16:9</p>
        :type AspectRatio: str
        :param _Sound: <p>生成视频时是否同时生成声音</p><ul><li>枚举值：on，off</li></ul><p>仅V2.6及后续版本模型支持当前参数，v2.6模型的std模式只能生成无声的视频</p>
        :type Sound: str
        :param _LogoAdd: <p>为生成视频添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        :param _MultiShot: <p>是否生成多镜头视频</p><ul><li>当前参数为true时，prompt参数无效</li><li>当前参数为false时，shot_type参数及multi_prompt参数无效</li></ul>
        :type MultiShot: bool
        :param _ShotType: <p>分镜方式</p><p>枚举值：customize，intelligence<br>当MultiShot参数为true时，当前参数必填</p>
        :type ShotType: str
        :param _MultiPrompt: <p>各分镜提示词，可包含正向描述和负向描述</p><p>通过index、prompt、duration参数定义分镜序号及相应提示词和时长，其中：</p><ul><li>最多支持6个分镜，最小支持1个分镜</li><li>每个分镜相关内容的最大长度不超过512</li><li>每个分镜的时长不大于当前任务的总时长，不小于1</li><li>所有分镜的时长之和等于当前任务的总时长</li><li>当MultiShot参数为true且ShotType参数为customize时，当前参数不得为空<br>用key:value承载，如下：<pre><code> &quot;MultiPrompt&quot;:[              {                &quot;Index&quot;:int,              &quot;Prompt&quot;: &quot;string&quot;,              &quot;Duration&quot;: &quot;5&quot;            }  ]</code></pre></li></ul>
        :type MultiPrompt: list of MultiPrompt
        :param _CameraControl: <p>控制摄像机运动的协议（如未指定，模型将根据输入的文本/图片进行智能匹配）</p>
        :type CameraControl: :class:`tencentcloud.vclm.v20240523.models.CameraControl`
        :param _CallbackUrl: <p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :type CallbackUrl: str
        """
        self._Prompt = None
        self._Model = None
        self._NegativePrompt = None
        self._Duration = None
        self._Mode = None
        self._CfgScale = None
        self._AspectRatio = None
        self._Sound = None
        self._LogoAdd = None
        self._LogoParam = None
        self._MultiShot = None
        self._ShotType = None
        self._MultiPrompt = None
        self._CameraControl = None
        self._CallbackUrl = None

    @property
    def Prompt(self):
        r"""<p>正向文本提示词。不能超过2500个字符</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Model(self):
        r"""<p>模型名称。<br>v1.6：Kling-V1-6<br>v2.0：Kling-V2-Master<br>v2.5：Kling-V2-5-Turbo<br>v2.6：Kling-V2-6<br>v3.0：kling-v3</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def NegativePrompt(self):
        r"""<p>负向文本提示词。不能超过2500个字符</p>
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Duration(self):
        r"""<p>生成视频时长，单位s。默认值为5。<br>枚举值：3，4，5，6，7，8，9，10，11，12，13，14，15</p><p>不同模型支持时长不同</p><ul><li>模型v1.6、v2.0、v2.5、v2.6：支持5、10</li><li>模型v3.0：支持3～15s</li></ul>
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Mode(self):
        r"""<p>生成视频的模式；</p><p>枚举值：std，pro</p><ul><li>其中std：标准模式（标准），基础模式，性价比高</li><li>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</li></ul><p>不同模型版本、视频模式支持范围不同</p><ul><li>v1.6：std、pro。</li><li>v2.0、v3.0：模型无需配置。</li><li>v2.5：首尾帧情况下支持pro。</li><li>v2.6：仅支持pro，选择v2.6模型时，默认自动生成高品质pro视频。</li></ul>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CfgScale(self):
        r"""<p>生成视频的自由度；值越大，模型自由度越小，与用户输入的提示词相关性越强。<br>取值范围：[0, 1]<br>v2.0、v2.5、v2.6 模型不支持当前参数<br>默认值：0.5。</p>
        :rtype: float
        """
        return self._CfgScale

    @CfgScale.setter
    def CfgScale(self, CfgScale):
        self._CfgScale = CfgScale

    @property
    def AspectRatio(self):
        r"""<p>生成视频的画面纵横比（宽:高）<br>枚举值：16:9, 9:16, 1:1<br>默认值：16:9</p>
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def Sound(self):
        r"""<p>生成视频时是否同时生成声音</p><ul><li>枚举值：on，off</li></ul><p>仅V2.6及后续版本模型支持当前参数，v2.6模型的std模式只能生成无声的视频</p>
        :rtype: str
        """
        return self._Sound

    @Sound.setter
    def Sound(self, Sound):
        self._Sound = Sound

    @property
    def LogoAdd(self):
        r"""<p>为生成视频添加标识的开关，默认为1。<br>1：添加标识。<br>0：不添加标识。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def MultiShot(self):
        r"""<p>是否生成多镜头视频</p><ul><li>当前参数为true时，prompt参数无效</li><li>当前参数为false时，shot_type参数及multi_prompt参数无效</li></ul>
        :rtype: bool
        """
        return self._MultiShot

    @MultiShot.setter
    def MultiShot(self, MultiShot):
        self._MultiShot = MultiShot

    @property
    def ShotType(self):
        r"""<p>分镜方式</p><p>枚举值：customize，intelligence<br>当MultiShot参数为true时，当前参数必填</p>
        :rtype: str
        """
        return self._ShotType

    @ShotType.setter
    def ShotType(self, ShotType):
        self._ShotType = ShotType

    @property
    def MultiPrompt(self):
        r"""<p>各分镜提示词，可包含正向描述和负向描述</p><p>通过index、prompt、duration参数定义分镜序号及相应提示词和时长，其中：</p><ul><li>最多支持6个分镜，最小支持1个分镜</li><li>每个分镜相关内容的最大长度不超过512</li><li>每个分镜的时长不大于当前任务的总时长，不小于1</li><li>所有分镜的时长之和等于当前任务的总时长</li><li>当MultiShot参数为true且ShotType参数为customize时，当前参数不得为空<br>用key:value承载，如下：<pre><code> &quot;MultiPrompt&quot;:[              {                &quot;Index&quot;:int,              &quot;Prompt&quot;: &quot;string&quot;,              &quot;Duration&quot;: &quot;5&quot;            }  ]</code></pre></li></ul>
        :rtype: list of MultiPrompt
        """
        return self._MultiPrompt

    @MultiPrompt.setter
    def MultiPrompt(self, MultiPrompt):
        self._MultiPrompt = MultiPrompt

    @property
    def CameraControl(self):
        r"""<p>控制摄像机运动的协议（如未指定，模型将根据输入的文本/图片进行智能匹配）</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.CameraControl`
        """
        return self._CameraControl

    @CameraControl.setter
    def CameraControl(self, CameraControl):
        self._CameraControl = CameraControl

    @property
    def CallbackUrl(self):
        r"""<p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Model = params.get("Model")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Duration = params.get("Duration")
        self._Mode = params.get("Mode")
        self._CfgScale = params.get("CfgScale")
        self._AspectRatio = params.get("AspectRatio")
        self._Sound = params.get("Sound")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._MultiShot = params.get("MultiShot")
        self._ShotType = params.get("ShotType")
        if params.get("MultiPrompt") is not None:
            self._MultiPrompt = []
            for item in params.get("MultiPrompt"):
                obj = MultiPrompt()
                obj._deserialize(item)
                self._MultiPrompt.append(obj)
        if params.get("CameraControl") is not None:
            self._CameraControl = CameraControl()
            self._CameraControl._deserialize(params.get("CameraControl"))
        self._CallbackUrl = params.get("CallbackUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTextToVideoJobResponse(AbstractModel):
    r"""SubmitTextToVideoJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitTextToVideoViduJobRequest(AbstractModel):
    r"""SubmitTextToVideoViduJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>文本提示词<br>生成视频的文本描述。<br>注：字符长度不能超过 2000 个字符</p>
        :type Prompt: str
        :param _Model: <p>模型名称，可选值，默认viduq2</p><ul><li>viduq2：最新模型</li><li>viduq3-turbo：对比viduq3-pro，生成速度更快</li><li>viduq3-pro：高效生成优质音视频内容，让视频内容更生动、更形象、更立体，效果更好</li></ul>
        :type Model: str
        :param _Duration: <p>视频时长参数，默认值依据模型而定：</p><ul><li>viduq3-pro、viduq3-turbo: 默认5秒，可选：1-16</li><li>viduq2 : 默认5秒，可选：1-10</li></ul>
        :type Duration: int
        :param _Bgm: <p>是否为生成的视频添加背景音乐。<br>默认：false，可选值 true 、false<br>传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。</p><ul><li>BGM不限制时长，系统根据视频时长自动适配</li><li>BGM参数在q2模型的duration为 9秒 或 10秒 时不生效；该参数在q3系列模型中不生效</li></ul>
        :type Bgm: bool
        :param _AspectRatio: <p>比例<br>默认 16:9，可选值如下：16:9、9:16、4:3、3:4、1:1</p>
        :type AspectRatio: str
        :param _Resolution: <p>分辨率参数，默认值依据模型和视频时长而定：</p><ul><li>viduq3-pro、viduq3-turbo(1-16秒)：默认 720p，可选：540p、720p、1080p</li><li>viduq2(1-10秒)：默认 720p，可选：540p、720p、1080p</li></ul>
        :type Resolution: str
        :param _Style: <p>风格<br>默认 general，可选值：general、anime<br>general：通用风格，可以通过提示词来控制风格<br>anime：动漫风格，仅在动漫风格表现突出，可以通过不同的动漫风格提示词来控制<br>注：使用q2、q3系列模型时该参数不生效</p>
        :type Style: str
        :param _MovementAmplitude: <p>运动幅度<br>默认 auto，可选值：auto、small、medium、large<br>注：使用q2、q3系列模型时该参数不生效</p>
        :type MovementAmplitude: str
        :param _Audio: <p>是否使用音视频直出能力，默认为true，枚举值为：</p><ul><li>false：不需要音视频直出，输出静音视频</li><li>true：需要音画同步，输出声音的视频（包括台词和音效）<br>注1：仅q3系列模型支持该参数</li></ul>
        :type Audio: bool
        :param _MetaData: <p>元数据标识，json格式字符串，透传字段，您可以 自定义格式 或使用 示例格式 ，示例如下：<br>{<br>&quot;Label&quot;: &quot;your_label&quot;,<br>&quot;ContentProducer&quot;: &quot;your_content_producer&quot;,<br>&quot;ContentPropagator&quot;: &quot;your_content_propagator&quot;,<br>&quot;ProduceID&quot;: &quot;your_product_id&quot;,<br>&quot;PropagateID&quot;: &quot;your_propagate_id&quot;,<br>&quot;ReservedCode1&quot;: &quot;your_reserved_code1&quot;,<br>&quot;ReservedCode2&quot;: &quot;your_reserved_code2&quot;<br>}<br>该参数为空时，默认使用vidu生成的元数据标识</p>
        :type MetaData: str
        :param _CallbackUrl: <p>Callback 协议<br>需要您在创建任务时主动设置 callback_url，请求方法为 POST，当视频生成任务完成时，将向此地址发送包含任务最新状态的回调请求。回调请求内容结构与查询任务API的返回体一致<br>回调返回的&quot;status&quot;包括以下状态：</p><ul><li>success 任务完成（如发送失败，回调三次）</li><li>failed 任务失败（如发送失败，回调三次）</li></ul>
        :type CallbackUrl: str
        :param _Payload: <p>透传参数 不做任何处理，仅数据传输 注：最多 1048576个字符</p>
        :type Payload: str
        :param _OffPeak: <p>错峰模式，默认为：false，可选值：</p><ul><li>true：错峰生成视频；</li><li>false：即时生成视频；<br>注1：错峰模式消耗的积分更低<br>注2：错峰模式下提交的任务，会在48小时内生成，未能完成的任务会被自动取消，并返还该任务的积分</li></ul>
        :type OffPeak: bool
        :param _LogoAdd: <p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._Prompt = None
        self._Model = None
        self._Duration = None
        self._Bgm = None
        self._AspectRatio = None
        self._Resolution = None
        self._Style = None
        self._MovementAmplitude = None
        self._Audio = None
        self._MetaData = None
        self._CallbackUrl = None
        self._Payload = None
        self._OffPeak = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        r"""<p>文本提示词<br>生成视频的文本描述。<br>注：字符长度不能超过 2000 个字符</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Model(self):
        r"""<p>模型名称，可选值，默认viduq2</p><ul><li>viduq2：最新模型</li><li>viduq3-turbo：对比viduq3-pro，生成速度更快</li><li>viduq3-pro：高效生成优质音视频内容，让视频内容更生动、更形象、更立体，效果更好</li></ul>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Duration(self):
        r"""<p>视频时长参数，默认值依据模型而定：</p><ul><li>viduq3-pro、viduq3-turbo: 默认5秒，可选：1-16</li><li>viduq2 : 默认5秒，可选：1-10</li></ul>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Bgm(self):
        r"""<p>是否为生成的视频添加背景音乐。<br>默认：false，可选值 true 、false<br>传 true 时系统将从预设 BGM 库中自动挑选合适的音乐并添加；不传或为 false 则不添加 BGM。</p><ul><li>BGM不限制时长，系统根据视频时长自动适配</li><li>BGM参数在q2模型的duration为 9秒 或 10秒 时不生效；该参数在q3系列模型中不生效</li></ul>
        :rtype: bool
        """
        return self._Bgm

    @Bgm.setter
    def Bgm(self, Bgm):
        self._Bgm = Bgm

    @property
    def AspectRatio(self):
        r"""<p>比例<br>默认 16:9，可选值如下：16:9、9:16、4:3、3:4、1:1</p>
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def Resolution(self):
        r"""<p>分辨率参数，默认值依据模型和视频时长而定：</p><ul><li>viduq3-pro、viduq3-turbo(1-16秒)：默认 720p，可选：540p、720p、1080p</li><li>viduq2(1-10秒)：默认 720p，可选：540p、720p、1080p</li></ul>
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Style(self):
        r"""<p>风格<br>默认 general，可选值：general、anime<br>general：通用风格，可以通过提示词来控制风格<br>anime：动漫风格，仅在动漫风格表现突出，可以通过不同的动漫风格提示词来控制<br>注：使用q2、q3系列模型时该参数不生效</p>
        :rtype: str
        """
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def MovementAmplitude(self):
        r"""<p>运动幅度<br>默认 auto，可选值：auto、small、medium、large<br>注：使用q2、q3系列模型时该参数不生效</p>
        :rtype: str
        """
        return self._MovementAmplitude

    @MovementAmplitude.setter
    def MovementAmplitude(self, MovementAmplitude):
        self._MovementAmplitude = MovementAmplitude

    @property
    def Audio(self):
        r"""<p>是否使用音视频直出能力，默认为true，枚举值为：</p><ul><li>false：不需要音视频直出，输出静音视频</li><li>true：需要音画同步，输出声音的视频（包括台词和音效）<br>注1：仅q3系列模型支持该参数</li></ul>
        :rtype: bool
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def MetaData(self):
        r"""<p>元数据标识，json格式字符串，透传字段，您可以 自定义格式 或使用 示例格式 ，示例如下：<br>{<br>&quot;Label&quot;: &quot;your_label&quot;,<br>&quot;ContentProducer&quot;: &quot;your_content_producer&quot;,<br>&quot;ContentPropagator&quot;: &quot;your_content_propagator&quot;,<br>&quot;ProduceID&quot;: &quot;your_product_id&quot;,<br>&quot;PropagateID&quot;: &quot;your_propagate_id&quot;,<br>&quot;ReservedCode1&quot;: &quot;your_reserved_code1&quot;,<br>&quot;ReservedCode2&quot;: &quot;your_reserved_code2&quot;<br>}<br>该参数为空时，默认使用vidu生成的元数据标识</p>
        :rtype: str
        """
        return self._MetaData

    @MetaData.setter
    def MetaData(self, MetaData):
        self._MetaData = MetaData

    @property
    def CallbackUrl(self):
        r"""<p>Callback 协议<br>需要您在创建任务时主动设置 callback_url，请求方法为 POST，当视频生成任务完成时，将向此地址发送包含任务最新状态的回调请求。回调请求内容结构与查询任务API的返回体一致<br>回调返回的&quot;status&quot;包括以下状态：</p><ul><li>success 任务完成（如发送失败，回调三次）</li><li>failed 任务失败（如发送失败，回调三次）</li></ul>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Payload(self):
        r"""<p>透传参数 不做任何处理，仅数据传输 注：最多 1048576个字符</p>
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def OffPeak(self):
        r"""<p>错峰模式，默认为：false，可选值：</p><ul><li>true：错峰生成视频；</li><li>false：即时生成视频；<br>注1：错峰模式消耗的积分更低<br>注2：错峰模式下提交的任务，会在48小时内生成，未能完成的任务会被自动取消，并返还该任务的积分</li></ul>
        :rtype: bool
        """
        return self._OffPeak

    @OffPeak.setter
    def OffPeak(self, OffPeak):
        self._OffPeak = OffPeak

    @property
    def LogoAdd(self):
        r"""<p>为生成结果图添加显式水印标识的开关，默认为1。<br>1：添加。<br>0：不添加。<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。<br>示例值：1</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Model = params.get("Model")
        self._Duration = params.get("Duration")
        self._Bgm = params.get("Bgm")
        self._AspectRatio = params.get("AspectRatio")
        self._Resolution = params.get("Resolution")
        self._Style = params.get("Style")
        self._MovementAmplitude = params.get("MovementAmplitude")
        self._Audio = params.get("Audio")
        self._MetaData = params.get("MetaData")
        self._CallbackUrl = params.get("CallbackUrl")
        self._Payload = params.get("Payload")
        self._OffPeak = params.get("OffPeak")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitTextToVideoViduJobResponse(AbstractModel):
    r"""SubmitTextToVideoViduJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoEditJobRequest(AbstractModel):
    r"""SubmitVideoEditJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: <p>参考视频URL。默认为待编辑视频。</p><ul><li>视频格式：支持MP4</li><li>视频时长：输入视频时长≤10秒</li><li>视频大小：不超过200M</li><li>视频文件：输入的视频帧率及分辨率不做限制（建议输入16：9或9：16的视频；分辨率建议在2160px内，帧率建议在60fps内）；输出视频是帧率会≥16fps，分辨率为720p</li></ul>
        :type VideoUrl: str
        :param _Prompt: <p>视频内容的描述，中文正向提示词。支持视频内容增加、删除、修改等能力</p><ul><li>最多支持200个 utf-8 字符（首尾空格不计入字符数）</li><li>不传prompt的时候，Images.N参考图列表必须要传图，且传的图片是经过图片编辑之后的结果图</li></ul>
        :type Prompt: str
        :param _Images: <p>参考图列表。用于对视频内容做风格迁移、内容替换、内容删减、内容增加做参考。</p><ul><li>支持传入图片Base64编码或图片URL</li><li>图片格式：支持jpg，png，jpeg，webp，bmp，tiff 格式</li><li>图片文件：大小不能超过10MB（base64后）。单边分辨率不超过5000px，不小于50px，图片长宽限制1:4 ~ 4:1。<br>示例值：[{ &quot;Url&quot;: &quot;https://console.cloud.tencent.com/cos/image.png&quot;}]</li></ul>
        :type Images: list of Image
        :param _Image: <p>图片base64或者图片url</p><ul><li>Base64 和 Url 必须提供一个，如果都提供以Url为准。</li><li>上传图url大小不超过 8M</li><li>支持jpg，png，jpeg，webp，bmp，tiff 格式</li><li>单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1</li></ul>
        :type Image: :class:`tencentcloud.vclm.v20240523.models.Image`
        :param _VideoEditParam: <p>扩展字段。</p>
        :type VideoEditParam: :class:`tencentcloud.vclm.v20240523.models.VideoEditParam`
        :param _LogoAdd: <p>为生成视频添加标识的开关，默认为1。传0 需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成后方可生效。<br>1：添加标识；<br>0：不添加标识；<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往   <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._VideoUrl = None
        self._Prompt = None
        self._Images = None
        self._Image = None
        self._VideoEditParam = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def VideoUrl(self):
        r"""<p>参考视频URL。默认为待编辑视频。</p><ul><li>视频格式：支持MP4</li><li>视频时长：输入视频时长≤10秒</li><li>视频大小：不超过200M</li><li>视频文件：输入的视频帧率及分辨率不做限制（建议输入16：9或9：16的视频；分辨率建议在2160px内，帧率建议在60fps内）；输出视频是帧率会≥16fps，分辨率为720p</li></ul>
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def Prompt(self):
        r"""<p>视频内容的描述，中文正向提示词。支持视频内容增加、删除、修改等能力</p><ul><li>最多支持200个 utf-8 字符（首尾空格不计入字符数）</li><li>不传prompt的时候，Images.N参考图列表必须要传图，且传的图片是经过图片编辑之后的结果图</li></ul>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Images(self):
        r"""<p>参考图列表。用于对视频内容做风格迁移、内容替换、内容删减、内容增加做参考。</p><ul><li>支持传入图片Base64编码或图片URL</li><li>图片格式：支持jpg，png，jpeg，webp，bmp，tiff 格式</li><li>图片文件：大小不能超过10MB（base64后）。单边分辨率不超过5000px，不小于50px，图片长宽限制1:4 ~ 4:1。<br>示例值：[{ &quot;Url&quot;: &quot;https://console.cloud.tencent.com/cos/image.png&quot;}]</li></ul>
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def Image(self):
        warnings.warn("parameter `Image` is deprecated", DeprecationWarning) 

        r"""<p>图片base64或者图片url</p><ul><li>Base64 和 Url 必须提供一个，如果都提供以Url为准。</li><li>上传图url大小不超过 8M</li><li>支持jpg，png，jpeg，webp，bmp，tiff 格式</li><li>单边分辨率不超过5000，不小于50，长宽限制1:4 ~ 4:1</li></ul>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        warnings.warn("parameter `Image` is deprecated", DeprecationWarning) 

        self._Image = Image

    @property
    def VideoEditParam(self):
        r"""<p>扩展字段。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.VideoEditParam`
        """
        return self._VideoEditParam

    @VideoEditParam.setter
    def VideoEditParam(self, VideoEditParam):
        self._VideoEditParam = VideoEditParam

    @property
    def LogoAdd(self):
        r"""<p>为生成视频添加标识的开关，默认为1。传0 需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成后方可生效。<br>1：添加标识；<br>0：不添加标识；<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往   <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._Prompt = params.get("Prompt")
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        if params.get("VideoEditParam") is not None:
            self._VideoEditParam = VideoEditParam()
            self._VideoEditParam._deserialize(params.get("VideoEditParam"))
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoEditJobResponse(AbstractModel):
    r"""SubmitVideoEditJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoEditKlingJobRequest(AbstractModel):
    r"""SubmitVideoEditKlingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: <p>文本提示词，可包含正向描述和负向描述</p><p>可将提示词模板化来满足不同的视频生成需求</p><p>不能超过2500个字</p>
        :type Prompt: str
        :param _Model: <p>模型名称，支持kling-video-o1，kling-v3-omni。默认kling-video-o1。</p>
        :type Model: str
        :param _ImageList: <p>参考图列表</p><p>包括主体、场景、风格等参考图片，也可作为首帧或尾帧生成视频；当作为首帧或尾帧生成视频时：</p><p>通过type参数来定义图片是否为首尾帧：first_frame为首帧，end_frame为尾帧</p><p>暂时不支持仅尾帧，即有尾帧图时必须有首帧图</p><p>首帧或首尾帧生视频时，不能使用视频编辑功能</p><p>用key:value承载，如下：</p><p>&quot;ImageInfo&quot;:[<br>    {<br>      &quot;ImageUrl&quot;:&quot;https://cos.ap-guangzhou.myqcloud.com/test.png&quot;,<br>    &quot;Type&quot;:&quot;first_frame&quot;<br>  },<br>  {<br>      &quot;ImageUrl&quot;:&quot;https://cos.ap-guangzhou.myqcloud.com/test.png&quot;,<br>    &quot;Type&quot;:&quot;end_frame&quot;<br>  }<br>]<br>支持传入图片URL（确保可访问）</p><p>图片格式支持.jpg / .jpeg / .png</p><p>图片文件大小不能超过10MB，图片宽高尺寸不小于300px，不大于8000px，图片宽高比要在1:2.5 ~ 2.5:1之间</p><p>有参考视频时，参考图片数量不得超过4；无参考视频时，参考图片数量不得超过7</p><p>数组中超过2张图片时，不支持设置尾帧</p>
        :type ImageList: list of ImageInfo
        :param _AspectRatio: <p>生成视频的画面纵横比（宽:高）</p><p>枚举值：16:9, 9:16, 1:1</p><p>未使用首帧参考或视频编辑功能时，当前参数必填</p>
        :type AspectRatio: str
        :param _Duration: <p>生成视频时长，单位s</p><p>枚举值：3，4，5，6，7，8，9，10，其中：使用文生视频、首帧图生视频时，仅支持5和10s<br>使用视频编辑功能（“refer_type”:“base”）时，输出结果与传入视频时长相同，此时当前参数无效；此时，按输入视频时长四舍五入取整计量计费</p>
        :type Duration: int
        :param _LogoAdd: <p>为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        :param _Mode: <p>生成视频的模式</p><p>枚举值：std，pro<br>其中std：标准模式（标准），基础模式，性价比高<br>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</p>
        :type Mode: str
        :param _VideoList: <p>参考视频，通过URL方式获取</p><p>可作为特征参考视频，也可作为待编辑视频，默认为待编辑视频；可选择性保留视频原声<br>通过ReferType参数区分参考视频类型：feature为特征参考视频，base为待编辑视频<br>参考视频为待编辑视频时，不能定义视频首尾帧<br>通过KeepOriginalSound参数选择是否保留视频原声，yes为保留，no为不保留；当前参数对特征参考视频（feature）也生效</p><ul><li>视频格式仅支持MP4/MOV</li><li>仅支持时长≥3秒且≤10秒的视频</li><li>视频宽高尺寸需介于720px（含）和2160px（含）之间</li><li>视频帧率基于24fps～60fps，生成视频时会输出为24fps</li><li>至多仅支持上传1段视频，视频大小不超过200MB</li></ul>
        :type VideoList: list of ReferVideoInfo
        :param _MultiShot: <p>是否生成多镜头视频  当前参数为true时，prompt参数无效，且不支持设定首尾帧生视频  当前参数为false时，shot_type参数及multi_prompt参数无效</p>
        :type MultiShot: bool
        :param _ShotType: <p>分镜方式  枚举值：customize  当multi_shot参数为true时，当前参数必填</p>
        :type ShotType: str
        :param _MultiPrompt: <p>各分镜信息，如提示词、时长等  通过index、prompt、duration参数定义分镜序号及相应提示词和时长，其中：  最多支持6个分镜，最小支持1个分镜  每个分镜相关内容的最大长度不超过512  每个分镜的时长不大于当前任务的总时长，不小于1  所有分镜的时长之和等于当前任务的总时长</p>
        :type MultiPrompt: list of MultiPrompt
        :param _ElementList: <p>参考主体列表  基于主体库中主体的ID配置，用key:value承载，如下：  &quot;element_list&quot;:[     {        &quot;element_id&quot;:long   },   {        &quot;element_id&quot;:long   } ] 参考主体数量与有无参考视频、参考图片数量有关，其中：  当使用首帧生成视频时，最多支持3个主体；  当使用首尾帧生成视频时，kling-v3-omni模型最多支持3个主体，kling-video-o1模不支持主体；  有参考视频时，参考图片数量和参考主体数量之和不得超过4，且不支持使用视频角色主体；  无参考视频时，参考图片数量和参考主体数量之和不得超过7；</p>
        :type ElementList: list of Element
        :param _CallbackUrl: <p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :type CallbackUrl: str
        :param _Sound: <p>是否开启声音</p>
        :type Sound: str
        """
        self._Prompt = None
        self._Model = None
        self._ImageList = None
        self._AspectRatio = None
        self._Duration = None
        self._LogoAdd = None
        self._LogoParam = None
        self._Mode = None
        self._VideoList = None
        self._MultiShot = None
        self._ShotType = None
        self._MultiPrompt = None
        self._ElementList = None
        self._CallbackUrl = None
        self._Sound = None

    @property
    def Prompt(self):
        r"""<p>文本提示词，可包含正向描述和负向描述</p><p>可将提示词模板化来满足不同的视频生成需求</p><p>不能超过2500个字</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Model(self):
        r"""<p>模型名称，支持kling-video-o1，kling-v3-omni。默认kling-video-o1。</p>
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def ImageList(self):
        r"""<p>参考图列表</p><p>包括主体、场景、风格等参考图片，也可作为首帧或尾帧生成视频；当作为首帧或尾帧生成视频时：</p><p>通过type参数来定义图片是否为首尾帧：first_frame为首帧，end_frame为尾帧</p><p>暂时不支持仅尾帧，即有尾帧图时必须有首帧图</p><p>首帧或首尾帧生视频时，不能使用视频编辑功能</p><p>用key:value承载，如下：</p><p>&quot;ImageInfo&quot;:[<br>    {<br>      &quot;ImageUrl&quot;:&quot;https://cos.ap-guangzhou.myqcloud.com/test.png&quot;,<br>    &quot;Type&quot;:&quot;first_frame&quot;<br>  },<br>  {<br>      &quot;ImageUrl&quot;:&quot;https://cos.ap-guangzhou.myqcloud.com/test.png&quot;,<br>    &quot;Type&quot;:&quot;end_frame&quot;<br>  }<br>]<br>支持传入图片URL（确保可访问）</p><p>图片格式支持.jpg / .jpeg / .png</p><p>图片文件大小不能超过10MB，图片宽高尺寸不小于300px，不大于8000px，图片宽高比要在1:2.5 ~ 2.5:1之间</p><p>有参考视频时，参考图片数量不得超过4；无参考视频时，参考图片数量不得超过7</p><p>数组中超过2张图片时，不支持设置尾帧</p>
        :rtype: list of ImageInfo
        """
        return self._ImageList

    @ImageList.setter
    def ImageList(self, ImageList):
        self._ImageList = ImageList

    @property
    def AspectRatio(self):
        r"""<p>生成视频的画面纵横比（宽:高）</p><p>枚举值：16:9, 9:16, 1:1</p><p>未使用首帧参考或视频编辑功能时，当前参数必填</p>
        :rtype: str
        """
        return self._AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, AspectRatio):
        self._AspectRatio = AspectRatio

    @property
    def Duration(self):
        r"""<p>生成视频时长，单位s</p><p>枚举值：3，4，5，6，7，8，9，10，其中：使用文生视频、首帧图生视频时，仅支持5和10s<br>使用视频编辑功能（“refer_type”:“base”）时，输出结果与传入视频时长相同，此时当前参数无效；此时，按输入视频时长四舍五入取整计量计费</p>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def LogoAdd(self):
        r"""<p>为生成视频添加标识的开关，默认为1，0 需前往 控制台 申请开启显示标识自主完成方可生效。 1：添加标识； 0：不添加标识； 其他数值：默认按1处理。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>默认在生成视频的右下角添加“ AI 生成”字样，如需替换为其他的标识图片，需前往 控制台 申请开启显示标识自主完成。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def Mode(self):
        r"""<p>生成视频的模式</p><p>枚举值：std，pro<br>其中std：标准模式（标准），基础模式，性价比高<br>其中pro：专家模式（高品质），高表现模式，生成视频质量更佳</p>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def VideoList(self):
        r"""<p>参考视频，通过URL方式获取</p><p>可作为特征参考视频，也可作为待编辑视频，默认为待编辑视频；可选择性保留视频原声<br>通过ReferType参数区分参考视频类型：feature为特征参考视频，base为待编辑视频<br>参考视频为待编辑视频时，不能定义视频首尾帧<br>通过KeepOriginalSound参数选择是否保留视频原声，yes为保留，no为不保留；当前参数对特征参考视频（feature）也生效</p><ul><li>视频格式仅支持MP4/MOV</li><li>仅支持时长≥3秒且≤10秒的视频</li><li>视频宽高尺寸需介于720px（含）和2160px（含）之间</li><li>视频帧率基于24fps～60fps，生成视频时会输出为24fps</li><li>至多仅支持上传1段视频，视频大小不超过200MB</li></ul>
        :rtype: list of ReferVideoInfo
        """
        return self._VideoList

    @VideoList.setter
    def VideoList(self, VideoList):
        self._VideoList = VideoList

    @property
    def MultiShot(self):
        r"""<p>是否生成多镜头视频  当前参数为true时，prompt参数无效，且不支持设定首尾帧生视频  当前参数为false时，shot_type参数及multi_prompt参数无效</p>
        :rtype: bool
        """
        return self._MultiShot

    @MultiShot.setter
    def MultiShot(self, MultiShot):
        self._MultiShot = MultiShot

    @property
    def ShotType(self):
        r"""<p>分镜方式  枚举值：customize  当multi_shot参数为true时，当前参数必填</p>
        :rtype: str
        """
        return self._ShotType

    @ShotType.setter
    def ShotType(self, ShotType):
        self._ShotType = ShotType

    @property
    def MultiPrompt(self):
        r"""<p>各分镜信息，如提示词、时长等  通过index、prompt、duration参数定义分镜序号及相应提示词和时长，其中：  最多支持6个分镜，最小支持1个分镜  每个分镜相关内容的最大长度不超过512  每个分镜的时长不大于当前任务的总时长，不小于1  所有分镜的时长之和等于当前任务的总时长</p>
        :rtype: list of MultiPrompt
        """
        return self._MultiPrompt

    @MultiPrompt.setter
    def MultiPrompt(self, MultiPrompt):
        self._MultiPrompt = MultiPrompt

    @property
    def ElementList(self):
        r"""<p>参考主体列表  基于主体库中主体的ID配置，用key:value承载，如下：  &quot;element_list&quot;:[     {        &quot;element_id&quot;:long   },   {        &quot;element_id&quot;:long   } ] 参考主体数量与有无参考视频、参考图片数量有关，其中：  当使用首帧生成视频时，最多支持3个主体；  当使用首尾帧生成视频时，kling-v3-omni模型最多支持3个主体，kling-video-o1模不支持主体；  有参考视频时，参考图片数量和参考主体数量之和不得超过4，且不支持使用视频角色主体；  无参考视频时，参考图片数量和参考主体数量之和不得超过7；</p>
        :rtype: list of Element
        """
        return self._ElementList

    @ElementList.setter
    def ElementList(self, ElementList):
        self._ElementList = ElementList

    @property
    def CallbackUrl(self):
        r"""<p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def Sound(self):
        r"""<p>是否开启声音</p>
        :rtype: str
        """
        return self._Sound

    @Sound.setter
    def Sound(self, Sound):
        self._Sound = Sound


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Model = params.get("Model")
        if params.get("ImageList") is not None:
            self._ImageList = []
            for item in params.get("ImageList"):
                obj = ImageInfo()
                obj._deserialize(item)
                self._ImageList.append(obj)
        self._AspectRatio = params.get("AspectRatio")
        self._Duration = params.get("Duration")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._Mode = params.get("Mode")
        if params.get("VideoList") is not None:
            self._VideoList = []
            for item in params.get("VideoList"):
                obj = ReferVideoInfo()
                obj._deserialize(item)
                self._VideoList.append(obj)
        self._MultiShot = params.get("MultiShot")
        self._ShotType = params.get("ShotType")
        if params.get("MultiPrompt") is not None:
            self._MultiPrompt = []
            for item in params.get("MultiPrompt"):
                obj = MultiPrompt()
                obj._deserialize(item)
                self._MultiPrompt.append(obj)
        if params.get("ElementList") is not None:
            self._ElementList = []
            for item in params.get("ElementList"):
                obj = Element()
                obj._deserialize(item)
                self._ElementList.append(obj)
        self._CallbackUrl = params.get("CallbackUrl")
        self._Sound = params.get("Sound")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoEditKlingJobResponse(AbstractModel):
    r"""SubmitVideoEditKlingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoExtendKlingJobRequest(AbstractModel):
    r"""SubmitVideoExtendKlingJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoId: <p>视频ID  支持通过文本、图片和视频延长生成的视频的ID（原视频不能超过3分钟）  请注意，基于目前的清理策略、视频生成30天之后会被清理，则无法进行延长</p>
        :type VideoId: str
        :param _Prompt: <p>正向文本提示词  不能超过2500个字符</p>
        :type Prompt: str
        :param _NegativePrompt: <p>负向文本提示词  不能超过2500个字符</p>
        :type NegativePrompt: str
        :param _CfgScale: <p>提示词参考强度  取值范围：[0,1]，数值越大参考强度越大</p>
        :type CfgScale: float
        :param _CallbackUrl: <p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :type CallbackUrl: str
        :param _LogoAdd: <p>为生成视频添加标识的开关，默认为1。传0 需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成后方可生效。<br>1：添加标识；<br>0：不添加标识；<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :type LogoAdd: int
        :param _LogoParam: <p>标识内容设置。<br>默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往   <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成。</p>
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._VideoId = None
        self._Prompt = None
        self._NegativePrompt = None
        self._CfgScale = None
        self._CallbackUrl = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def VideoId(self):
        r"""<p>视频ID  支持通过文本、图片和视频延长生成的视频的ID（原视频不能超过3分钟）  请注意，基于目前的清理策略、视频生成30天之后会被清理，则无法进行延长</p>
        :rtype: str
        """
        return self._VideoId

    @VideoId.setter
    def VideoId(self, VideoId):
        self._VideoId = VideoId

    @property
    def Prompt(self):
        r"""<p>正向文本提示词  不能超过2500个字符</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        r"""<p>负向文本提示词  不能超过2500个字符</p>
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def CfgScale(self):
        r"""<p>提示词参考强度  取值范围：[0,1]，数值越大参考强度越大</p>
        :rtype: float
        """
        return self._CfgScale

    @CfgScale.setter
    def CfgScale(self, CfgScale):
        self._CfgScale = CfgScale

    @property
    def CallbackUrl(self):
        r"""<p>本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知</p>
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def LogoAdd(self):
        r"""<p>为生成视频添加标识的开关，默认为1。传0 需前往  <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成后方可生效。<br>1：添加标识；<br>0：不添加标识；<br>其他数值：默认按1处理。<br>建议您使用显著标识来提示，该视频是 AI 生成的视频。</p>
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""<p>标识内容设置。<br>默认在生成视频的右下角添加“ AI 生成”或“视频由 AI 生成”字样，如需替换为其他的标识图片，需前往   <a href="https://console.cloud.tencent.com/vtc/setting">控制台</a>  申请开启显式标识自主完成。</p>
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._VideoId = params.get("VideoId")
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._CfgScale = params.get("CfgScale")
        self._CallbackUrl = params.get("CallbackUrl")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoExtendKlingJobResponse(AbstractModel):
    r"""SubmitVideoExtendKlingJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: <p>任务ID。</p>
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoFaceFusionJobRequest(AbstractModel):
    r"""SubmitVideoFaceFusionJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 视频素材下载地址。用户自定义模板视频下载地址，使用前需要先调用视频审核接口进行内容审核。视频限制：分辨率≤4k，fps≤25，视频大小≤1G，时长≤20 秒，支持格式mp4。

输入视频建议：
姿态：人脸相对镜头水平方向角度转动不超过 90°,垂直方向角度转动不超过 20°。遮挡：脸部遮挡面积不超过 50%，不要完全遮挡五官，不要有半透明遮挡（强光，玻璃，透明眼镜等）、以及细碎离散的脸部遮挡（如飘落的花瓣）。妆容及光照：避免浓妆、复杂妆容，避免复杂光照、闪烁，这些属性无法完全恢复，并对稳定性有影响。针对特殊表情和微表情，针对局部肌肉控制下的微表情，以及过于夸张的特殊表情等不保证表情效果完全恢复。
        :type VideoUrl: str
        :param _TemplateInfos: 视频素材模板的人脸位置信息。
目前最多支持融合视频素材中的 6 张人脸  
输入图片要求：  
1、用户图限制大小不超过 10MB  
2、图片最大分辨率不超过 4k，建议最小为 128，  人脸框最小为 68
3、支持格式 jpg，png  
4、如果用户图中未指定人脸且有多张人脸，  默认融合最大人脸  
输入图片建议：  包含上述视频中出现的人物的单人照，并且正面、清晰、无遮挡
        :type TemplateInfos: list of FaceTemplateInfo
        :param _MergeInfos: 用户人脸图片位置信息。
输入图片要求：
1、用户图限制大小不超过 10MB
2、图片最大分辨率不超过 4k，建议最小为 128，人脸框最小为 68
3、支持格式 jpg，png
4、如果未指定人脸且用户图中有多张人脸，
默认融合最大人脸
输入图建议：
正脸无遮挡
        :type MergeInfos: list of FaceMergeInfo
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 
1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 视频水印Logo参数标识内容设置。   
默认在融合结果图右下角添加“AI生成”类似字样，您可根据自身需要替换为其他的Logo图片。   
输入建议：输入水印图片宽高需小于视频宽高
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._VideoUrl = None
        self._TemplateInfos = None
        self._MergeInfos = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def VideoUrl(self):
        r"""视频素材下载地址。用户自定义模板视频下载地址，使用前需要先调用视频审核接口进行内容审核。视频限制：分辨率≤4k，fps≤25，视频大小≤1G，时长≤20 秒，支持格式mp4。

输入视频建议：
姿态：人脸相对镜头水平方向角度转动不超过 90°,垂直方向角度转动不超过 20°。遮挡：脸部遮挡面积不超过 50%，不要完全遮挡五官，不要有半透明遮挡（强光，玻璃，透明眼镜等）、以及细碎离散的脸部遮挡（如飘落的花瓣）。妆容及光照：避免浓妆、复杂妆容，避免复杂光照、闪烁，这些属性无法完全恢复，并对稳定性有影响。针对特殊表情和微表情，针对局部肌肉控制下的微表情，以及过于夸张的特殊表情等不保证表情效果完全恢复。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def TemplateInfos(self):
        r"""视频素材模板的人脸位置信息。
目前最多支持融合视频素材中的 6 张人脸  
输入图片要求：  
1、用户图限制大小不超过 10MB  
2、图片最大分辨率不超过 4k，建议最小为 128，  人脸框最小为 68
3、支持格式 jpg，png  
4、如果用户图中未指定人脸且有多张人脸，  默认融合最大人脸  
输入图片建议：  包含上述视频中出现的人物的单人照，并且正面、清晰、无遮挡
        :rtype: list of FaceTemplateInfo
        """
        return self._TemplateInfos

    @TemplateInfos.setter
    def TemplateInfos(self, TemplateInfos):
        self._TemplateInfos = TemplateInfos

    @property
    def MergeInfos(self):
        r"""用户人脸图片位置信息。
输入图片要求：
1、用户图限制大小不超过 10MB
2、图片最大分辨率不超过 4k，建议最小为 128，人脸框最小为 68
3、支持格式 jpg，png
4、如果未指定人脸且用户图中有多张人脸，
默认融合最大人脸
输入图建议：
正脸无遮挡
        :rtype: list of FaceMergeInfo
        """
        return self._MergeInfos

    @MergeInfos.setter
    def MergeInfos(self, MergeInfos):
        self._MergeInfos = MergeInfos

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 
1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 
建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""视频水印Logo参数标识内容设置。   
默认在融合结果图右下角添加“AI生成”类似字样，您可根据自身需要替换为其他的Logo图片。   
输入建议：输入水印图片宽高需小于视频宽高
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        if params.get("TemplateInfos") is not None:
            self._TemplateInfos = []
            for item in params.get("TemplateInfos"):
                obj = FaceTemplateInfo()
                obj._deserialize(item)
                self._TemplateInfos.append(obj)
        if params.get("MergeInfos") is not None:
            self._MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = FaceMergeInfo()
                obj._deserialize(item)
                self._MergeInfos.append(obj)
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoFaceFusionJobResponse(AbstractModel):
    r"""SubmitVideoFaceFusionJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 视频人脸融合任务的job id（job有效期24小时）
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""视频人脸融合任务的job id（job有效期24小时）
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoStylizationJobRequest(AbstractModel):
    r"""SubmitVideoStylizationJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StyleId: 风格ID。取值说明：
2d_anime：2D动漫；
3d_cartoon：3D卡通；
3d_china：3D国潮；
pixel_art：像素风。
        :type StyleId: str
        :param _VideoUrl: 输入视频URL。视频要求：
- 视频格式：mp4、mov；
- 视频时长：1～60秒；
- 视频分辨率：540P~2056P，即长宽像素数均在540px～2056px范围内；
- 视频大小：不超过200M；
- 视频FPS：15～60fps。
        :type VideoUrl: str
        :param _StyleStrength: 风格化强度。取值说明：
low：风格化强度弱；
medium：风格化强度中等；
high：风格化强度强。
默认值为medium。
        :type StyleStrength: str
        """
        self._StyleId = None
        self._VideoUrl = None
        self._StyleStrength = None

    @property
    def StyleId(self):
        r"""风格ID。取值说明：
2d_anime：2D动漫；
3d_cartoon：3D卡通；
3d_china：3D国潮；
pixel_art：像素风。
        :rtype: str
        """
        return self._StyleId

    @StyleId.setter
    def StyleId(self, StyleId):
        self._StyleId = StyleId

    @property
    def VideoUrl(self):
        r"""输入视频URL。视频要求：
- 视频格式：mp4、mov；
- 视频时长：1～60秒；
- 视频分辨率：540P~2056P，即长宽像素数均在540px～2056px范围内；
- 视频大小：不超过200M；
- 视频FPS：15～60fps。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def StyleStrength(self):
        r"""风格化强度。取值说明：
low：风格化强度弱；
medium：风格化强度中等；
high：风格化强度强。
默认值为medium。
        :rtype: str
        """
        return self._StyleStrength

    @StyleStrength.setter
    def StyleStrength(self, StyleStrength):
        self._StyleStrength = StyleStrength


    def _deserialize(self, params):
        self._StyleId = params.get("StyleId")
        self._VideoUrl = params.get("VideoUrl")
        self._StyleStrength = params.get("StyleStrength")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoStylizationJobResponse(AbstractModel):
    r"""SubmitVideoStylizationJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。任务有效期为48小时。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID。任务有效期为48小时。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class SubmitVideoVoiceJobRequest(AbstractModel):
    r"""SubmitVideoVoiceJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VideoUrl: 输入视频的Url  上传视频时长限制：1-15s 视频格式：MP4，MOV 视频大小：不超过1 GB URL地址中不能包含中文字符。
        :type VideoUrl: str
        :param _Prompt: 描述音效内容的正向提示词。输入上限50个字符。
        :type Prompt: str
        :param _NegativePrompt: 音效内容的原始负向提示词。输入上限50个字符。
        :type NegativePrompt: str
        :param _LogoAdd: 为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        self._VideoUrl = None
        self._Prompt = None
        self._NegativePrompt = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def VideoUrl(self):
        r"""输入视频的Url  上传视频时长限制：1-15s 视频格式：MP4，MOV 视频大小：不超过1 GB URL地址中不能包含中文字符。
        :rtype: str
        """
        return self._VideoUrl

    @VideoUrl.setter
    def VideoUrl(self, VideoUrl):
        self._VideoUrl = VideoUrl

    @property
    def Prompt(self):
        r"""描述音效内容的正向提示词。输入上限50个字符。
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        r"""音效内容的原始负向提示词。输入上限50个字符。
        :rtype: str
        """
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def LogoAdd(self):
        r"""为生成视频添加标识的开关，默认为1。 1：添加标识。 0：不添加标识。 其他数值：默认按1处理。 建议您使用显著标识来提示，该视频是 AI 生成的视频。
        :rtype: int
        """
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        r"""标识内容设置。 默认在生成视频的右下角添加“视频由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :rtype: :class:`tencentcloud.vclm.v20240523.models.LogoParam`
        """
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._VideoUrl = params.get("VideoUrl")
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitVideoVoiceJobResponse(AbstractModel):
    r"""SubmitVideoVoiceJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class TagList(AbstractModel):
    r"""生成视频时所引用的音色

    """

    def __init__(self):
        r"""
        :param _TagId: <p>tag标签</p>
        :type TagId: str
        """
        self._TagId = None

    @property
    def TagId(self):
        r"""<p>tag标签</p>
        :rtype: str
        """
        return self._TagId

    @TagId.setter
    def TagId(self, TagId):
        self._TagId = TagId


    def _deserialize(self, params):
        self._TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Trajectory(AbstractModel):
    r"""运动轨迹坐标序列

    """

    def __init__(self):
        r"""
        :param _X: 轨迹点横坐标（在像素二维坐标系下，以输入图片image左下为原点的像素坐标）
        :type X: int
        :param _Y: 轨迹点纵坐标（在像素二维坐标系下，以输入图片image左下为原点的像素坐标）
        :type Y: int
        """
        self._X = None
        self._Y = None

    @property
    def X(self):
        r"""轨迹点横坐标（在像素二维坐标系下，以输入图片image左下为原点的像素坐标）
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""轨迹点纵坐标（在像素二维坐标系下，以输入图片image左下为原点的像素坐标）
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEditParam(AbstractModel):
    r"""视频编辑参数

    """

    def __init__(self):
        r"""
        :param _Magic: 魔法词，针对特定场景生效。不同场景传不同的值。默认不传。
- 换人场景：1
        :type Magic: str
        """
        self._Magic = None

    @property
    def Magic(self):
        r"""魔法词，针对特定场景生效。不同场景传不同的值。默认不传。
- 换人场景：1
        :rtype: str
        """
        return self._Magic

    @Magic.setter
    def Magic(self, Magic):
        self._Magic = Magic


    def _deserialize(self, params):
        self._Magic = params.get("Magic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Voice(AbstractModel):
    r"""生成视频时所引用的音色

    """

    def __init__(self):
        r"""
        :param _VoiceId: <p>音色id</p>
        :type VoiceId: str
        """
        self._VoiceId = None

    @property
    def VoiceId(self):
        r"""<p>音色id</p>
        :rtype: str
        """
        return self._VoiceId

    @VoiceId.setter
    def VoiceId(self, VoiceId):
        self._VoiceId = VoiceId


    def _deserialize(self, params):
        self._VoiceId = params.get("VoiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        