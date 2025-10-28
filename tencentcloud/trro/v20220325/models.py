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


class BatchDeleteDevicesRequest(AbstractModel):
    r"""BatchDeleteDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标删除设备所属项目ID
        :type ProjectId: str
        :param _DeviceIds: 目标删除设备的设备ID数组
        :type DeviceIds: list of str
        """
        self._ProjectId = None
        self._DeviceIds = None

    @property
    def ProjectId(self):
        r"""目标删除设备所属项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceIds(self):
        r"""目标删除设备的设备ID数组
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteDevicesResponse(AbstractModel):
    r"""BatchDeleteDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedDeviceIds: 删除失败的设备ID列表
        :type FailedDeviceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedDeviceIds = None
        self._RequestId = None

    @property
    def FailedDeviceIds(self):
        r"""删除失败的设备ID列表
        :rtype: list of str
        """
        return self._FailedDeviceIds

    @FailedDeviceIds.setter
    def FailedDeviceIds(self, FailedDeviceIds):
        self._FailedDeviceIds = FailedDeviceIds

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
        self._FailedDeviceIds = params.get("FailedDeviceIds")
        self._RequestId = params.get("RequestId")


class BatchDeletePolicyRequest(AbstractModel):
    r"""BatchDeletePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 删除权限配置的项目ID
        :type ProjectId: str
        :param _RemoteDeviceIds: 删除权限配置的远端设备ID列表
        :type RemoteDeviceIds: list of str
        :param _PolicyMode: 删除权限配置的权限模式, black为黑名单，white为白名单
        :type PolicyMode: str
        """
        self._ProjectId = None
        self._RemoteDeviceIds = None
        self._PolicyMode = None

    @property
    def ProjectId(self):
        r"""删除权限配置的项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RemoteDeviceIds(self):
        r"""删除权限配置的远端设备ID列表
        :rtype: list of str
        """
        return self._RemoteDeviceIds

    @RemoteDeviceIds.setter
    def RemoteDeviceIds(self, RemoteDeviceIds):
        self._RemoteDeviceIds = RemoteDeviceIds

    @property
    def PolicyMode(self):
        r"""删除权限配置的权限模式, black为黑名单，white为白名单
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RemoteDeviceIds = params.get("RemoteDeviceIds")
        self._PolicyMode = params.get("PolicyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeletePolicyResponse(AbstractModel):
    r"""BatchDeletePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedRemoteDeviceIds: 删除权限配置失败的远端设备ID列表
        :type FailedRemoteDeviceIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedRemoteDeviceIds = None
        self._RequestId = None

    @property
    def FailedRemoteDeviceIds(self):
        r"""删除权限配置失败的远端设备ID列表
        :rtype: list of str
        """
        return self._FailedRemoteDeviceIds

    @FailedRemoteDeviceIds.setter
    def FailedRemoteDeviceIds(self, FailedRemoteDeviceIds):
        self._FailedRemoteDeviceIds = FailedRemoteDeviceIds

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
        self._FailedRemoteDeviceIds = params.get("FailedRemoteDeviceIds")
        self._RequestId = params.get("RequestId")


class BoundLicensesRequest(AbstractModel):
    r"""BoundLicenses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: license数量
        :type Count: int
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._Count = None
        self._DeviceId = None
        self._ProjectId = None

    @property
    def Count(self):
        r"""license数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DeviceId(self):
        r"""设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._DeviceId = params.get("DeviceId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundLicensesResponse(AbstractModel):
    r"""BoundLicenses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CloudStorage(AbstractModel):
    r"""云端录制文件上传到云存储的参数（对象存储cos）

    """

    def __init__(self):
        r"""
        :param _Vendor: 腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS
【注意】目前第三方云存储仅支持AWS，更多第三方云存储陆续支持中
示例值：0
        :type Vendor: int
        :param _Region: 腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-shanghai(cos, 具体参考云存储厂商支持的地域)
        :type Region: str
        :param _Bucket: 云存储桶名称。
        :type Bucket: str
        :param _AccessKey: 云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
        :type AccessKey: str
        :param _SecretKey: 云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
        :type SecretKey: str
        :param _FileNamePrefix: 云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，录制文件xxx.m3u8在 ["prefix1", "prefix2"]作用下，会变成prefix1/prefix2/TaskId/xxx.m3u8。
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        r"""腾讯云对象存储COS以及第三方云存储账号信息
0：腾讯云对象存储 COS
1：AWS
【注意】目前第三方云存储仅支持AWS，更多第三方云存储陆续支持中
示例值：0
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        r"""腾讯云对象存储的[地域信息]（https://cloud.tencent.com/document/product/436/6224#.E5.9C.B0.E5.9F.9F）。
示例值：cn-shanghai-1

AWS S3[地域信息]（https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions）
示例值：ap-shanghai(cos, 具体参考云存储厂商支持的地域)
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        r"""云存储桶名称。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        r"""云存储的access_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretId值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        r"""云存储的secret_key账号信息。
若存储至腾讯云对象存储COS，请前往https://console.cloud.tencent.com/cam/capi 查看或创建，对应链接中密钥字段的SecretKey值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        r"""云存储bucket 的指定位置，由字符串数组组成。合法的字符串范围az,AZ,0~9,'_'和'-'，举个例子，录制文件xxx.m3u8在 ["prefix1", "prefix2"]作用下，会变成prefix1/prefix2/TaskId/xxx.m3u8。
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingRequest(AbstractModel):
    r"""CreateCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _VideoStreamId: 视频流号
        :type VideoStreamId: int
        :param _CloudStorage: 腾讯云对象存储COS以及第三方云存储的账号信息
        :type CloudStorage: :class:`tencentcloud.trro.v20220325.models.CloudStorage`
        :param _MaxMediaFileDuration: 如果是aac或者mp4文件格式，超过长度限制后，系统会自动拆分视频文件。单位：分钟。默认为1440min（24h），取值范围为1-1440。【单文件限制最大为2G，满足文件大小 >2G 或录制时长度 > 24h任意一个条件，文件都会自动切分】 Hls 格式录制此参数不生效。
        :type MaxMediaFileDuration: int
        :param _OutputFormat: 输出文件的格式（存储至COS等第三方存储时有效）。0：输出文件为hls格式。1：输出文件格式为hls+mp4。2：输出文件格式为hls+aac 。3：(默认)输出文件格式为mp4。4：输出文件格式为aac。
        :type OutputFormat: int
        :param _MaxIdleTime: 房间内持续没有主播的状态超过MaxIdleTime的时长，自动停止录制，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。 示例值：30
        :type MaxIdleTime: int
        """
        self._ProjectId = None
        self._DeviceId = None
        self._VideoStreamId = None
        self._CloudStorage = None
        self._MaxMediaFileDuration = None
        self._OutputFormat = None
        self._MaxIdleTime = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def VideoStreamId(self):
        r"""视频流号
        :rtype: int
        """
        return self._VideoStreamId

    @VideoStreamId.setter
    def VideoStreamId(self, VideoStreamId):
        self._VideoStreamId = VideoStreamId

    @property
    def CloudStorage(self):
        r"""腾讯云对象存储COS以及第三方云存储的账号信息
        :rtype: :class:`tencentcloud.trro.v20220325.models.CloudStorage`
        """
        return self._CloudStorage

    @CloudStorage.setter
    def CloudStorage(self, CloudStorage):
        self._CloudStorage = CloudStorage

    @property
    def MaxMediaFileDuration(self):
        r"""如果是aac或者mp4文件格式，超过长度限制后，系统会自动拆分视频文件。单位：分钟。默认为1440min（24h），取值范围为1-1440。【单文件限制最大为2G，满足文件大小 >2G 或录制时长度 > 24h任意一个条件，文件都会自动切分】 Hls 格式录制此参数不生效。
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration

    @property
    def OutputFormat(self):
        r"""输出文件的格式（存储至COS等第三方存储时有效）。0：输出文件为hls格式。1：输出文件格式为hls+mp4。2：输出文件格式为hls+aac 。3：(默认)输出文件格式为mp4。4：输出文件格式为aac。
        :rtype: int
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def MaxIdleTime(self):
        r"""房间内持续没有主播的状态超过MaxIdleTime的时长，自动停止录制，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。 示例值：30
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._VideoStreamId = params.get("VideoStreamId")
        if params.get("CloudStorage") is not None:
            self._CloudStorage = CloudStorage()
            self._CloudStorage._deserialize(params.get("CloudStorage"))
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        self._OutputFormat = params.get("OutputFormat")
        self._MaxIdleTime = params.get("MaxIdleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingResponse(AbstractModel):
    r"""CreateCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。任务 ID需要业务保存下来，作为下次针对这个录制任务操作的参数。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""云录制服务分配的任务 ID。任务 ID 是对一次录制生命周期过程的唯一标识，结束录制时会失去意义。任务 ID需要业务保存下来，作为下次针对这个录制任务操作的参数。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    r"""CreateDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 创建设备所归属的项目ID
        :type ProjectId: str
        :param _DeviceId: 创建设备ID，项目内需要唯一，由小写英文字母、数字和下划线构成，长度不超过18
        :type DeviceId: str
        :param _DeviceName: 创建设备名称，长度小于24, 可包含中文、数字、英文字母和下划线
        :type DeviceName: str
        :param _DeviceType: 设备类型，field为现场设备（受控设备），remote为远端设备（操控设备），不填默认为field
        :type DeviceType: str
        :param _DeviceToken: 设备认证口令，由大小写英文字母和数字构成，须为16位
        :type DeviceToken: str
        """
        self._ProjectId = None
        self._DeviceId = None
        self._DeviceName = None
        self._DeviceType = None
        self._DeviceToken = None

    @property
    def ProjectId(self):
        r"""创建设备所归属的项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""创建设备ID，项目内需要唯一，由小写英文字母、数字和下划线构成，长度不超过18
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""创建设备名称，长度小于24, 可包含中文、数字、英文字母和下划线
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceType(self):
        r"""设备类型，field为现场设备（受控设备），remote为远端设备（操控设备），不填默认为field
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def DeviceToken(self):
        r"""设备认证口令，由大小写英文字母和数字构成，须为16位
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceType = params.get("DeviceType")
        self._DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDeviceResponse(AbstractModel):
    r"""CreateDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    r"""CreateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称，长度不超过24个字符
        :type ProjectName: str
        :param _ProjectDescription: 项目描述，长度不超过120个字符，不填默认为空
        :type ProjectDescription: str
        :param _PolicyMode: 权限模式，black为黑名单，white为白名单，不填默认为black
        :type PolicyMode: str
        """
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None

    @property
    def ProjectName(self):
        r"""项目名称，长度不超过24个字符
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        r"""项目描述，长度不超过120个字符，不填默认为空
        :rtype: str
        """
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        r"""权限模式，black为黑名单，white为白名单，不填默认为black
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    r"""CreateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID，长度为16位
        :type ProjectId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._RequestId = None

    @property
    def ProjectId(self):
        r"""项目ID，长度为16位
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

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
        self._ProjectId = params.get("ProjectId")
        self._RequestId = params.get("RequestId")


class DeleteCloudRecordingRequest(AbstractModel):
    r"""DeleteCloudRecording请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 录制任务的唯一Id，在启动录制成功后会返回。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""录制任务的唯一Id，在启动录制成功后会返回。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRecordingResponse(AbstractModel):
    r"""DeleteCloudRecording返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    r"""DeleteProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    r"""DeleteProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeDeviceInfoRequest(AbstractModel):
    r"""DescribeDeviceInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标设备所属项目ID
        :type ProjectId: str
        :param _DeviceId: 目标设备ID
        :type DeviceId: str
        """
        self._ProjectId = None
        self._DeviceId = None

    @property
    def ProjectId(self):
        r"""目标设备所属项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""目标设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceInfoResponse(AbstractModel):
    r"""DescribeDeviceInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceType: 设备类型，field为现场设备（被控方），remote为远端设备（操控方）
        :type DeviceType: str
        :param _DeviceStatus: 设备状态，offline为离线，ready为在线准备，connected为会话中
        :type DeviceStatus: str
        :param _LastReportTime: 设备状态最后更新时间
        :type LastReportTime: str
        :param _ModifyTime: 设备信息最后修改时间
        :type ModifyTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceName = None
        self._DeviceType = None
        self._DeviceStatus = None
        self._LastReportTime = None
        self._ModifyTime = None
        self._RequestId = None

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceType(self):
        r"""设备类型，field为现场设备（被控方），remote为远端设备（操控方）
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def DeviceStatus(self):
        r"""设备状态，offline为离线，ready为在线准备，connected为会话中
        :rtype: str
        """
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus

    @property
    def LastReportTime(self):
        r"""设备状态最后更新时间
        :rtype: str
        """
        return self._LastReportTime

    @LastReportTime.setter
    def LastReportTime(self, LastReportTime):
        self._LastReportTime = LastReportTime

    @property
    def ModifyTime(self):
        r"""设备信息最后修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
        self._DeviceName = params.get("DeviceName")
        self._DeviceType = params.get("DeviceType")
        self._DeviceStatus = params.get("DeviceStatus")
        self._LastReportTime = params.get("LastReportTime")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestId = params.get("RequestId")


class DescribeDeviceListRequest(AbstractModel):
    r"""DescribeDeviceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 设备所属项目ID
        :type ProjectId: str
        :param _DeviceType: 设备类型筛选，不填默认为全部设备类型
        :type DeviceType: str
        :param _SearchWords: 对设备ID或Name按关键字进行模糊匹配，不填则不进行模糊匹配
        :type SearchWords: str
        :param _PageSize: 每页返回的最大设备数，不填默认为10
        :type PageSize: int
        :param _PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        :param _DeviceStatus: 设备状态筛选，不填默认为不过滤。取值：["ready","connected","online"]，online代表ready或connected
        :type DeviceStatus: str
        """
        self._ProjectId = None
        self._DeviceType = None
        self._SearchWords = None
        self._PageSize = None
        self._PageNumber = None
        self._DeviceStatus = None

    @property
    def ProjectId(self):
        r"""设备所属项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceType(self):
        r"""设备类型筛选，不填默认为全部设备类型
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def SearchWords(self):
        r"""对设备ID或Name按关键字进行模糊匹配，不填则不进行模糊匹配
        :rtype: str
        """
        return self._SearchWords

    @SearchWords.setter
    def SearchWords(self, SearchWords):
        self._SearchWords = SearchWords

    @property
    def PageSize(self):
        r"""每页返回的最大设备数，不填默认为10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前页码，不填默认为1（首页）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def DeviceStatus(self):
        r"""设备状态筛选，不填默认为不过滤。取值：["ready","connected","online"]，online代表ready或connected
        :rtype: str
        """
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceType = params.get("DeviceType")
        self._SearchWords = params.get("SearchWords")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._DeviceStatus = params.get("DeviceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceListResponse(AbstractModel):
    r"""DescribeDeviceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 设备信息列表
        :type Devices: list of DeviceInfo
        :param _Total: 设备总数
        :type Total: int
        :param _Num: 本次返回的设备数
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._Total = None
        self._Num = None
        self._RequestId = None

    @property
    def Devices(self):
        r"""设备信息列表
        :rtype: list of DeviceInfo
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def Total(self):
        r"""设备总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Num(self):
        r"""本次返回的设备数
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

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
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._Total = params.get("Total")
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribeDeviceSessionDetailsRequest(AbstractModel):
    r"""DescribeDeviceSessionDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        """
        self._SessionId = None

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceSessionDetailsResponse(AbstractModel):
    r"""DescribeDeviceSessionDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Details: 按设备区分的会话详细数据
        :type Details: list of SessionDeviceDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Details = None
        self._RequestId = None

    @property
    def Details(self):
        r"""按设备区分的会话详细数据
        :rtype: list of SessionDeviceDetail
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

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
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = SessionDeviceDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceSessionListRequest(AbstractModel):
    r"""DescribeDeviceSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PageNumber: 页码，从1开始
        :type PageNumber: int
        :param _PageSize: 每页个数
        :type PageSize: int
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""页码，从1开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页个数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceSessionListResponse(AbstractModel):
    r"""DescribeDeviceSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总个数
        :type Total: int
        :param _DeviceSessionList: 会话列表
        :type DeviceSessionList: list of SessionInfo
        :param _Num: 本页数量
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DeviceSessionList = None
        self._Num = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DeviceSessionList(self):
        r"""会话列表
        :rtype: list of SessionInfo
        """
        return self._DeviceSessionList

    @DeviceSessionList.setter
    def DeviceSessionList(self, DeviceSessionList):
        self._DeviceSessionList = DeviceSessionList

    @property
    def Num(self):
        r"""本页数量
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

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
        self._Total = params.get("Total")
        if params.get("DeviceSessionList") is not None:
            self._DeviceSessionList = []
            for item in params.get("DeviceSessionList"):
                obj = SessionInfo()
                obj._deserialize(item)
                self._DeviceSessionList.append(obj)
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribePolicyRequest(AbstractModel):
    r"""DescribePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 查看权限的项目ID
        :type ProjectId: str
        :param _PolicyMode: 查看的权限模式，black为黑名单，white为白名单，不填默认为当前项目生效的权限模式
        :type PolicyMode: str
        :param _SearchMode: 模糊匹配模式，remoteMatch为远端设备ID匹配，fieldMatch为现场ID匹配，不填默认为remoteMatch
        :type SearchMode: str
        :param _SearchWords: 模糊匹配关键字，不填默认不进行模糊匹配
        :type SearchWords: str
        :param _PageSize: 每页返回的最大数量，不填默认为10
        :type PageSize: int
        :param _PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self._ProjectId = None
        self._PolicyMode = None
        self._SearchMode = None
        self._SearchWords = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def ProjectId(self):
        r"""查看权限的项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PolicyMode(self):
        r"""查看的权限模式，black为黑名单，white为白名单，不填默认为当前项目生效的权限模式
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def SearchMode(self):
        r"""模糊匹配模式，remoteMatch为远端设备ID匹配，fieldMatch为现场ID匹配，不填默认为remoteMatch
        :rtype: str
        """
        return self._SearchMode

    @SearchMode.setter
    def SearchMode(self, SearchMode):
        self._SearchMode = SearchMode

    @property
    def SearchWords(self):
        r"""模糊匹配关键字，不填默认不进行模糊匹配
        :rtype: str
        """
        return self._SearchWords

    @SearchWords.setter
    def SearchWords(self, SearchWords):
        self._SearchWords = SearchWords

    @property
    def PageSize(self):
        r"""每页返回的最大数量，不填默认为10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前页码，不填默认为1（首页）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PolicyMode = params.get("PolicyMode")
        self._SearchMode = params.get("SearchMode")
        self._SearchWords = params.get("SearchWords")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyResponse(AbstractModel):
    r"""DescribePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyMode: 权限模式
        :type PolicyMode: str
        :param _PolicyEnabled: 返回的权限模式是否为当前生效的权限模式
        :type PolicyEnabled: bool
        :param _PolicyInfo: 权限信息列表
        :type PolicyInfo: list of PolicyInfo
        :param _Num: 本次返回的权限信息数量
        :type Num: int
        :param _Total: 权限信息总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyMode = None
        self._PolicyEnabled = None
        self._PolicyInfo = None
        self._Num = None
        self._Total = None
        self._RequestId = None

    @property
    def PolicyMode(self):
        r"""权限模式
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def PolicyEnabled(self):
        r"""返回的权限模式是否为当前生效的权限模式
        :rtype: bool
        """
        return self._PolicyEnabled

    @PolicyEnabled.setter
    def PolicyEnabled(self, PolicyEnabled):
        self._PolicyEnabled = PolicyEnabled

    @property
    def PolicyInfo(self):
        r"""权限信息列表
        :rtype: list of PolicyInfo
        """
        return self._PolicyInfo

    @PolicyInfo.setter
    def PolicyInfo(self, PolicyInfo):
        self._PolicyInfo = PolicyInfo

    @property
    def Num(self):
        r"""本次返回的权限信息数量
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Total(self):
        r"""权限信息总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._PolicyMode = params.get("PolicyMode")
        self._PolicyEnabled = params.get("PolicyEnabled")
        if params.get("PolicyInfo") is not None:
            self._PolicyInfo = []
            for item in params.get("PolicyInfo"):
                obj = PolicyInfo()
                obj._deserialize(item)
                self._PolicyInfo.append(obj)
        self._Num = params.get("Num")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeProjectInfoRequest(AbstractModel):
    r"""DescribeProjectInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标项目ID，必填参数
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        r"""目标项目ID，必填参数
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectInfoResponse(AbstractModel):
    r"""DescribeProjectInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDescription: 项目描述
        :type ProjectDescription: str
        :param _PolicyMode: 项目权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param _ModifyTime: 项目信息修改时间
        :type ModifyTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None
        self._ModifyTime = None
        self._RequestId = None

    @property
    def ProjectName(self):
        r"""项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        r"""项目描述
        :rtype: str
        """
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        r"""项目权限模式，black为黑名单，white为白名单
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def ModifyTime(self):
        r"""项目信息修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

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
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestId = params.get("RequestId")


class DescribeProjectListRequest(AbstractModel):
    r"""DescribeProjectList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页返回的最大项目数量，不填默认为10
        :type PageSize: int
        :param _PageNumber: 当前页码，不填默认为1（首页）
        :type PageNumber: int
        """
        self._PageSize = None
        self._PageNumber = None

    @property
    def PageSize(self):
        r"""每页返回的最大项目数量，不填默认为10
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""当前页码，不填默认为1（首页）
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectListResponse(AbstractModel):
    r"""DescribeProjectList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Projects: 项目信息数组
        :type Projects: list of ProjectInfo
        :param _Total: 项目总数
        :type Total: int
        :param _Num: 本次返回的项目数
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Projects = None
        self._Total = None
        self._Num = None
        self._RequestId = None

    @property
    def Projects(self):
        r"""项目信息数组
        :rtype: list of ProjectInfo
        """
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def Total(self):
        r"""项目总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Num(self):
        r"""本次返回的项目数
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

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
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._Total = params.get("Total")
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribeRecentSessionListRequest(AbstractModel):
    r"""DescribeRecentSessionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _PageNumber: 页码，从1开始
        :type PageNumber: int
        :param _PageSize: 每页个数
        :type PageSize: int
        :param _DeviceId: 设备ID，支持过滤远端设备或现场设备
        :type DeviceId: str
        :param _StartTime: 时间范围的起始时间。时间范围最大为最近两小时，若不传或超出范围，则起始时间按两小时前计算
        :type StartTime: int
        :param _EndTime: 时间范围的结束时间。时间范围最大为最近两小时，若不传或超出范围，则结束时间按当前时间计算
        :type EndTime: int
        """
        self._ProjectId = None
        self._PageNumber = None
        self._PageSize = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PageNumber(self):
        r"""页码，从1开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页个数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def DeviceId(self):
        r"""设备ID，支持过滤远端设备或现场设备
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        r"""时间范围的起始时间。时间范围最大为最近两小时，若不传或超出范围，则起始时间按两小时前计算
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""时间范围的结束时间。时间范围最大为最近两小时，若不传或超出范围，则结束时间按当前时间计算
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecentSessionListResponse(AbstractModel):
    r"""DescribeRecentSessionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总个数
        :type Total: int
        :param _RecentSessionList: 会话列表
        :type RecentSessionList: list of RecentSessionInfo
        :param _Num: 本页数量
        :type Num: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RecentSessionList = None
        self._Num = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RecentSessionList(self):
        r"""会话列表
        :rtype: list of RecentSessionInfo
        """
        return self._RecentSessionList

    @RecentSessionList.setter
    def RecentSessionList(self, RecentSessionList):
        self._RecentSessionList = RecentSessionList

    @property
    def Num(self):
        r"""本页数量
        :rtype: int
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

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
        self._Total = params.get("Total")
        if params.get("RecentSessionList") is not None:
            self._RecentSessionList = []
            for item in params.get("RecentSessionList"):
                obj = RecentSessionInfo()
                obj._deserialize(item)
                self._RecentSessionList.append(obj)
        self._Num = params.get("Num")
        self._RequestId = params.get("RequestId")


class DescribeSessionStatisticsByIntervalRequest(AbstractModel):
    r"""DescribeSessionStatisticsByInterval请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _StatisticInterval: 统计时间间隔：hour|day|month
        :type StatisticInterval: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param _EndTime: 结束时间，单位：秒
        :type EndTime: int
        """
        self._ProjectId = None
        self._StatisticInterval = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def StatisticInterval(self):
        r"""统计时间间隔：hour|day|month
        :rtype: str
        """
        return self._StatisticInterval

    @StatisticInterval.setter
    def StatisticInterval(self, StatisticInterval):
        self._StatisticInterval = StatisticInterval

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        r"""起始时间，单位：秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._StatisticInterval = params.get("StatisticInterval")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionStatisticsByIntervalResponse(AbstractModel):
    r"""DescribeSessionStatisticsByInterval返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionStatistics: 各时间段的会话统计数据
        :type SessionStatistics: list of SessionIntervalStatistic
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionStatistics = None
        self._RequestId = None

    @property
    def SessionStatistics(self):
        r"""各时间段的会话统计数据
        :rtype: list of SessionIntervalStatistic
        """
        return self._SessionStatistics

    @SessionStatistics.setter
    def SessionStatistics(self, SessionStatistics):
        self._SessionStatistics = SessionStatistics

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
        if params.get("SessionStatistics") is not None:
            self._SessionStatistics = []
            for item in params.get("SessionStatistics"):
                obj = SessionIntervalStatistic()
                obj._deserialize(item)
                self._SessionStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSessionStatisticsRequest(AbstractModel):
    r"""DescribeSessionStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _StartTime: 起始时间，单位：秒
        :type StartTime: int
        :param _EndTime: 结束时间，单位：秒
        :type EndTime: int
        """
        self._ProjectId = None
        self._DeviceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def StartTime(self):
        r"""起始时间，单位：秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionStatisticsResponse(AbstractModel):
    r"""DescribeSessionStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionNum: 会话数量
        :type SessionNum: int
        :param _TotalDuration: 通话时长，单位：分钟
        :type TotalDuration: int
        :param _ActiveFieldDeviceNum: 活跃现场设备数
        :type ActiveFieldDeviceNum: int
        :param _ActiveRemoteDeviceNum: 活跃远端设备数
        :type ActiveRemoteDeviceNum: int
        :param _NotBadSessionRatio: 优良会话占比，单位：%
        :type NotBadSessionRatio: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionNum = None
        self._TotalDuration = None
        self._ActiveFieldDeviceNum = None
        self._ActiveRemoteDeviceNum = None
        self._NotBadSessionRatio = None
        self._RequestId = None

    @property
    def SessionNum(self):
        r"""会话数量
        :rtype: int
        """
        return self._SessionNum

    @SessionNum.setter
    def SessionNum(self, SessionNum):
        self._SessionNum = SessionNum

    @property
    def TotalDuration(self):
        r"""通话时长，单位：分钟
        :rtype: int
        """
        return self._TotalDuration

    @TotalDuration.setter
    def TotalDuration(self, TotalDuration):
        self._TotalDuration = TotalDuration

    @property
    def ActiveFieldDeviceNum(self):
        r"""活跃现场设备数
        :rtype: int
        """
        return self._ActiveFieldDeviceNum

    @ActiveFieldDeviceNum.setter
    def ActiveFieldDeviceNum(self, ActiveFieldDeviceNum):
        self._ActiveFieldDeviceNum = ActiveFieldDeviceNum

    @property
    def ActiveRemoteDeviceNum(self):
        r"""活跃远端设备数
        :rtype: int
        """
        return self._ActiveRemoteDeviceNum

    @ActiveRemoteDeviceNum.setter
    def ActiveRemoteDeviceNum(self, ActiveRemoteDeviceNum):
        self._ActiveRemoteDeviceNum = ActiveRemoteDeviceNum

    @property
    def NotBadSessionRatio(self):
        r"""优良会话占比，单位：%
        :rtype: int
        """
        return self._NotBadSessionRatio

    @NotBadSessionRatio.setter
    def NotBadSessionRatio(self, NotBadSessionRatio):
        self._NotBadSessionRatio = NotBadSessionRatio

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
        self._SessionNum = params.get("SessionNum")
        self._TotalDuration = params.get("TotalDuration")
        self._ActiveFieldDeviceNum = params.get("ActiveFieldDeviceNum")
        self._ActiveRemoteDeviceNum = params.get("ActiveRemoteDeviceNum")
        self._NotBadSessionRatio = params.get("NotBadSessionRatio")
        self._RequestId = params.get("RequestId")


class Device(AbstractModel):
    r"""查询用户设备的授权绑定情况

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _LicenseCount: 已经绑定license数量
        :type LicenseCount: int
        :param _RemainDay: 剩余天数：天
        :type RemainDay: int
        :param _ExpireTime: 过期时间：s
        :type ExpireTime: str
        :param _Duration: 服务时长：s
        :type Duration: str
        :param _LicenseIds: 已经绑定licenseId列表
        :type LicenseIds: list of str
        :param _MonthlyRemainTime: 每月license的限定时长
        :type MonthlyRemainTime: int
        :param _LimitedTime: 月封顶时长（分钟)
        :type LimitedTime: int
        """
        self._DeviceId = None
        self._DeviceName = None
        self._LicenseCount = None
        self._RemainDay = None
        self._ExpireTime = None
        self._Duration = None
        self._LicenseIds = None
        self._MonthlyRemainTime = None
        self._LimitedTime = None

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def LicenseCount(self):
        r"""已经绑定license数量
        :rtype: int
        """
        return self._LicenseCount

    @LicenseCount.setter
    def LicenseCount(self, LicenseCount):
        self._LicenseCount = LicenseCount

    @property
    def RemainDay(self):
        r"""剩余天数：天
        :rtype: int
        """
        return self._RemainDay

    @RemainDay.setter
    def RemainDay(self, RemainDay):
        self._RemainDay = RemainDay

    @property
    def ExpireTime(self):
        r"""过期时间：s
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Duration(self):
        r"""服务时长：s
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def LicenseIds(self):
        r"""已经绑定licenseId列表
        :rtype: list of str
        """
        return self._LicenseIds

    @LicenseIds.setter
    def LicenseIds(self, LicenseIds):
        self._LicenseIds = LicenseIds

    @property
    def MonthlyRemainTime(self):
        r"""每月license的限定时长
        :rtype: int
        """
        return self._MonthlyRemainTime

    @MonthlyRemainTime.setter
    def MonthlyRemainTime(self, MonthlyRemainTime):
        self._MonthlyRemainTime = MonthlyRemainTime

    @property
    def LimitedTime(self):
        r"""月封顶时长（分钟)
        :rtype: int
        """
        return self._LimitedTime

    @LimitedTime.setter
    def LimitedTime(self, LimitedTime):
        self._LimitedTime = LimitedTime


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._LicenseCount = params.get("LicenseCount")
        self._RemainDay = params.get("RemainDay")
        self._ExpireTime = params.get("ExpireTime")
        self._Duration = params.get("Duration")
        self._LicenseIds = params.get("LicenseIds")
        self._MonthlyRemainTime = params.get("MonthlyRemainTime")
        self._LimitedTime = params.get("LimitedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeviceInfo(AbstractModel):
    r"""设备信息

    """

    def __init__(self):
        r"""
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _DeviceName: 设备名称
        :type DeviceName: str
        :param _DeviceStatus: 设备状态，offline为离线，ready为在线准备，connected为会话中
        :type DeviceStatus: str
        :param _DeviceType: 设备类型，field为现场设备（受控方），remote为远端设备（操控方）
        :type DeviceType: str
        :param _ModifyTime: 设备信息最近修改时间
        :type ModifyTime: str
        :param _LastReportTime: 设备状态最近更新时间
        :type LastReportTime: str
        :param _ProjectId: 设备所属项目Id
        :type ProjectId: str
        """
        self._DeviceId = None
        self._DeviceName = None
        self._DeviceStatus = None
        self._DeviceType = None
        self._ModifyTime = None
        self._LastReportTime = None
        self._ProjectId = None

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""设备名称
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceStatus(self):
        r"""设备状态，offline为离线，ready为在线准备，connected为会话中
        :rtype: str
        """
        return self._DeviceStatus

    @DeviceStatus.setter
    def DeviceStatus(self, DeviceStatus):
        self._DeviceStatus = DeviceStatus

    @property
    def DeviceType(self):
        r"""设备类型，field为现场设备（受控方），remote为远端设备（操控方）
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def ModifyTime(self):
        r"""设备信息最近修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def LastReportTime(self):
        r"""设备状态最近更新时间
        :rtype: str
        """
        return self._LastReportTime

    @LastReportTime.setter
    def LastReportTime(self, LastReportTime):
        self._LastReportTime = LastReportTime

    @property
    def ProjectId(self):
        r"""设备所属项目Id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceStatus = params.get("DeviceStatus")
        self._DeviceType = params.get("DeviceType")
        self._ModifyTime = params.get("ModifyTime")
        self._LastReportTime = params.get("LastReportTime")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DurationDetails(AbstractModel):
    r"""会话时长明细

    """

    def __init__(self):
        r"""
        :param _SessionTime: 会话时间
        :type SessionTime: str
        :param _Voice: 语音:min
        :type Voice: int
        :param _SD: 标清:min
        :type SD: int
        :param _HD: 高清:min
        :type HD: int
        :param _FHD: 超高清:min
        :type FHD: int
        :param _TwoK: 2k:min
        :type TwoK: int
        :param _FourK: 4k:min
        :type FourK: int
        :param _Online: 在线时长:min
        :type Online: int
        :param _MultiSD: 多网标清:min
        :type MultiSD: int
        :param _MultiHD: 多网高清:min
        :type MultiHD: int
        :param _MultiFHD: 多网超高清:min
        :type MultiFHD: int
        :param _MultiTwoK: 多网2k:min
        :type MultiTwoK: int
        :param _MultiFourK: 多网4k:min
        :type MultiFourK: int
        :param _MultiOnline: 多网在线时长:min
        :type MultiOnline: int
        :param _DeductDuration: 抵扣时长:min
        :type DeductDuration: int
        """
        self._SessionTime = None
        self._Voice = None
        self._SD = None
        self._HD = None
        self._FHD = None
        self._TwoK = None
        self._FourK = None
        self._Online = None
        self._MultiSD = None
        self._MultiHD = None
        self._MultiFHD = None
        self._MultiTwoK = None
        self._MultiFourK = None
        self._MultiOnline = None
        self._DeductDuration = None

    @property
    def SessionTime(self):
        r"""会话时间
        :rtype: str
        """
        return self._SessionTime

    @SessionTime.setter
    def SessionTime(self, SessionTime):
        self._SessionTime = SessionTime

    @property
    def Voice(self):
        r"""语音:min
        :rtype: int
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def SD(self):
        r"""标清:min
        :rtype: int
        """
        return self._SD

    @SD.setter
    def SD(self, SD):
        self._SD = SD

    @property
    def HD(self):
        r"""高清:min
        :rtype: int
        """
        return self._HD

    @HD.setter
    def HD(self, HD):
        self._HD = HD

    @property
    def FHD(self):
        r"""超高清:min
        :rtype: int
        """
        return self._FHD

    @FHD.setter
    def FHD(self, FHD):
        self._FHD = FHD

    @property
    def TwoK(self):
        r"""2k:min
        :rtype: int
        """
        return self._TwoK

    @TwoK.setter
    def TwoK(self, TwoK):
        self._TwoK = TwoK

    @property
    def FourK(self):
        r"""4k:min
        :rtype: int
        """
        return self._FourK

    @FourK.setter
    def FourK(self, FourK):
        self._FourK = FourK

    @property
    def Online(self):
        r"""在线时长:min
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def MultiSD(self):
        r"""多网标清:min
        :rtype: int
        """
        return self._MultiSD

    @MultiSD.setter
    def MultiSD(self, MultiSD):
        self._MultiSD = MultiSD

    @property
    def MultiHD(self):
        r"""多网高清:min
        :rtype: int
        """
        return self._MultiHD

    @MultiHD.setter
    def MultiHD(self, MultiHD):
        self._MultiHD = MultiHD

    @property
    def MultiFHD(self):
        r"""多网超高清:min
        :rtype: int
        """
        return self._MultiFHD

    @MultiFHD.setter
    def MultiFHD(self, MultiFHD):
        self._MultiFHD = MultiFHD

    @property
    def MultiTwoK(self):
        r"""多网2k:min
        :rtype: int
        """
        return self._MultiTwoK

    @MultiTwoK.setter
    def MultiTwoK(self, MultiTwoK):
        self._MultiTwoK = MultiTwoK

    @property
    def MultiFourK(self):
        r"""多网4k:min
        :rtype: int
        """
        return self._MultiFourK

    @MultiFourK.setter
    def MultiFourK(self, MultiFourK):
        self._MultiFourK = MultiFourK

    @property
    def MultiOnline(self):
        r"""多网在线时长:min
        :rtype: int
        """
        return self._MultiOnline

    @MultiOnline.setter
    def MultiOnline(self, MultiOnline):
        self._MultiOnline = MultiOnline

    @property
    def DeductDuration(self):
        r"""抵扣时长:min
        :rtype: int
        """
        return self._DeductDuration

    @DeductDuration.setter
    def DeductDuration(self, DeductDuration):
        self._DeductDuration = DeductDuration


    def _deserialize(self, params):
        self._SessionTime = params.get("SessionTime")
        self._Voice = params.get("Voice")
        self._SD = params.get("SD")
        self._HD = params.get("HD")
        self._FHD = params.get("FHD")
        self._TwoK = params.get("TwoK")
        self._FourK = params.get("FourK")
        self._Online = params.get("Online")
        self._MultiSD = params.get("MultiSD")
        self._MultiHD = params.get("MultiHD")
        self._MultiFHD = params.get("MultiFHD")
        self._MultiTwoK = params.get("MultiTwoK")
        self._MultiFourK = params.get("MultiFourK")
        self._MultiOnline = params.get("MultiOnline")
        self._DeductDuration = params.get("DeductDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLicenseRequest(AbstractModel):
    r"""GetDeviceLicense请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标设备所属项目ID
        :type ProjectId: str
        :param _DeviceId: 目标设备ID
        :type DeviceId: str
        """
        self._ProjectId = None
        self._DeviceId = None

    @property
    def ProjectId(self):
        r"""目标设备所属项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""目标设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDeviceLicenseResponse(AbstractModel):
    r"""GetDeviceLicense返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AvailableCount: 指定设备已经绑定的可用license数量
        :type AvailableCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AvailableCount = None
        self._RequestId = None

    @property
    def AvailableCount(self):
        r"""指定设备已经绑定的可用license数量
        :rtype: int
        """
        return self._AvailableCount

    @AvailableCount.setter
    def AvailableCount(self, AvailableCount):
        self._AvailableCount = AvailableCount

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
        self._AvailableCount = params.get("AvailableCount")
        self._RequestId = params.get("RequestId")


class GetDevicesRequest(AbstractModel):
    r"""GetDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 页码
        :type PageNum: int
        :param _PageSize: 页面数量
        :type PageSize: int
        :param _ProjectId: 项目 ID
        :type ProjectId: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        """
        self._PageNum = None
        self._PageSize = None
        self._ProjectId = None
        self._DeviceId = None

    @property
    def PageNum(self):
        r"""页码
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""页面数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProjectId(self):
        r"""项目 ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDevicesResponse(AbstractModel):
    r"""GetDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Devices: 设备授权列表
        :type Devices: list of Device
        :param _TotalCount: 列表数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Devices = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Devices(self):
        r"""设备授权列表
        :rtype: list of Device
        """
        return self._Devices

    @Devices.setter
    def Devices(self, Devices):
        self._Devices = Devices

    @property
    def TotalCount(self):
        r"""列表数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Devices") is not None:
            self._Devices = []
            for item in params.get("Devices"):
                obj = Device()
                obj._deserialize(item)
                self._Devices.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetDurationDetailsRequest(AbstractModel):
    r"""GetDurationDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _PageNum: 页码
        :type PageNum: int
        :param _PageSize: 页面数量
        :type PageSize: int
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _DeviceId: 设备ID，不传查全部设备
        :type DeviceId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._PageNum = None
        self._PageSize = None
        self._ProjectId = None
        self._DeviceId = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNum(self):
        r"""页码
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""页面数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""设备ID，不传查全部设备
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDurationDetailsResponse(AbstractModel):
    r"""GetDurationDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 列表总数
        :type TotalCount: int
        :param _DurationDetails: 时长明细列表
        :type DurationDetails: list of DurationDetails
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DurationDetails = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""列表总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DurationDetails(self):
        r"""时长明细列表
        :rtype: list of DurationDetails
        """
        return self._DurationDetails

    @DurationDetails.setter
    def DurationDetails(self, DurationDetails):
        self._DurationDetails = DurationDetails

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
        self._TotalCount = params.get("TotalCount")
        if params.get("DurationDetails") is not None:
            self._DurationDetails = []
            for item in params.get("DurationDetails"):
                obj = DurationDetails()
                obj._deserialize(item)
                self._DurationDetails.append(obj)
        self._RequestId = params.get("RequestId")


class GetLicenseStatRequest(AbstractModel):
    r"""GetLicenseStat请求参数结构体

    """


class GetLicenseStatResponse(AbstractModel):
    r"""GetLicenseStat返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Valid: 有效授权
        :type Valid: int
        :param _Bound: 已绑定授权
        :type Bound: int
        :param _UnBound: 未绑定授权
        :type UnBound: int
        :param _Expire: 过期授权
        :type Expire: int
        :param _MonthlyExpire: 当月用量超时授权个数
        :type MonthlyExpire: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Valid = None
        self._Bound = None
        self._UnBound = None
        self._Expire = None
        self._MonthlyExpire = None
        self._RequestId = None

    @property
    def Valid(self):
        r"""有效授权
        :rtype: int
        """
        return self._Valid

    @Valid.setter
    def Valid(self, Valid):
        self._Valid = Valid

    @property
    def Bound(self):
        r"""已绑定授权
        :rtype: int
        """
        return self._Bound

    @Bound.setter
    def Bound(self, Bound):
        self._Bound = Bound

    @property
    def UnBound(self):
        r"""未绑定授权
        :rtype: int
        """
        return self._UnBound

    @UnBound.setter
    def UnBound(self, UnBound):
        self._UnBound = UnBound

    @property
    def Expire(self):
        r"""过期授权
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def MonthlyExpire(self):
        r"""当月用量超时授权个数
        :rtype: int
        """
        return self._MonthlyExpire

    @MonthlyExpire.setter
    def MonthlyExpire(self, MonthlyExpire):
        self._MonthlyExpire = MonthlyExpire

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
        self._Valid = params.get("Valid")
        self._Bound = params.get("Bound")
        self._UnBound = params.get("UnBound")
        self._Expire = params.get("Expire")
        self._MonthlyExpire = params.get("MonthlyExpire")
        self._RequestId = params.get("RequestId")


class GetLicensesRequest(AbstractModel):
    r"""GetLicenses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNum: 页码
        :type PageNum: int
        :param _PageSize: 页面数量
        :type PageSize: int
        :param _ProjectId: projectId
        :type ProjectId: str
        :param _DeviceId: DeviceId
        :type DeviceId: str
        :param _Status: license状态：0:未绑定；1:已绑定；2:已停服；3:已退费
        :type Status: int
        """
        self._PageNum = None
        self._PageSize = None
        self._ProjectId = None
        self._DeviceId = None
        self._Status = None

    @property
    def PageNum(self):
        r"""页码
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""页面数量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ProjectId(self):
        r"""projectId
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""DeviceId
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Status(self):
        r"""license状态：0:未绑定；1:已绑定；2:已停服；3:已退费
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLicensesResponse(AbstractModel):
    r"""GetLicenses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Licenses: license列表
        :type Licenses: list of License
        :param _TotalCount: license列表项数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Licenses = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Licenses(self):
        r"""license列表
        :rtype: list of License
        """
        return self._Licenses

    @Licenses.setter
    def Licenses(self, Licenses):
        self._Licenses = Licenses

    @property
    def TotalCount(self):
        r"""license列表项数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Licenses") is not None:
            self._Licenses = []
            for item in params.get("Licenses"):
                obj = License()
                obj._deserialize(item)
                self._Licenses.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GetTotalDurationRequest(AbstractModel):
    r"""GetTotalDuration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _DeviceId: 设备id，不传查全部
        :type DeviceId: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ProjectId = None
        self._DeviceId = None

    @property
    def StartTime(self):
        r"""开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""设备id，不传查全部
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTotalDurationResponse(AbstractModel):
    r"""GetTotalDuration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Voice: 语音:min
        :type Voice: int
        :param _SD: 标清:min
        :type SD: int
        :param _HD: 高清:min
        :type HD: int
        :param _FHD: 超高清:min
        :type FHD: int
        :param _TwoK: 2k:min
        :type TwoK: int
        :param _FourK: 4k:min
        :type FourK: int
        :param _Online: 在线时长:min 
        :type Online: int
        :param _MultiSD: 多网标清:min
        :type MultiSD: int
        :param _MultiHD: 多网高清:min
        :type MultiHD: int
        :param _MultiFHD: 多网超高清:min
        :type MultiFHD: int
        :param _MultiTwoK: 多网2k:min
        :type MultiTwoK: int
        :param _MultiFourK: 多网4k:min
        :type MultiFourK: int
        :param _MultiOnline: 多网在线时长:min 
        :type MultiOnline: int
        :param _DeductDuration: 总抵扣时长:min 
        :type DeductDuration: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Voice = None
        self._SD = None
        self._HD = None
        self._FHD = None
        self._TwoK = None
        self._FourK = None
        self._Online = None
        self._MultiSD = None
        self._MultiHD = None
        self._MultiFHD = None
        self._MultiTwoK = None
        self._MultiFourK = None
        self._MultiOnline = None
        self._DeductDuration = None
        self._RequestId = None

    @property
    def Voice(self):
        r"""语音:min
        :rtype: int
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice

    @property
    def SD(self):
        r"""标清:min
        :rtype: int
        """
        return self._SD

    @SD.setter
    def SD(self, SD):
        self._SD = SD

    @property
    def HD(self):
        r"""高清:min
        :rtype: int
        """
        return self._HD

    @HD.setter
    def HD(self, HD):
        self._HD = HD

    @property
    def FHD(self):
        r"""超高清:min
        :rtype: int
        """
        return self._FHD

    @FHD.setter
    def FHD(self, FHD):
        self._FHD = FHD

    @property
    def TwoK(self):
        r"""2k:min
        :rtype: int
        """
        return self._TwoK

    @TwoK.setter
    def TwoK(self, TwoK):
        self._TwoK = TwoK

    @property
    def FourK(self):
        r"""4k:min
        :rtype: int
        """
        return self._FourK

    @FourK.setter
    def FourK(self, FourK):
        self._FourK = FourK

    @property
    def Online(self):
        r"""在线时长:min 
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online

    @property
    def MultiSD(self):
        r"""多网标清:min
        :rtype: int
        """
        return self._MultiSD

    @MultiSD.setter
    def MultiSD(self, MultiSD):
        self._MultiSD = MultiSD

    @property
    def MultiHD(self):
        r"""多网高清:min
        :rtype: int
        """
        return self._MultiHD

    @MultiHD.setter
    def MultiHD(self, MultiHD):
        self._MultiHD = MultiHD

    @property
    def MultiFHD(self):
        r"""多网超高清:min
        :rtype: int
        """
        return self._MultiFHD

    @MultiFHD.setter
    def MultiFHD(self, MultiFHD):
        self._MultiFHD = MultiFHD

    @property
    def MultiTwoK(self):
        r"""多网2k:min
        :rtype: int
        """
        return self._MultiTwoK

    @MultiTwoK.setter
    def MultiTwoK(self, MultiTwoK):
        self._MultiTwoK = MultiTwoK

    @property
    def MultiFourK(self):
        r"""多网4k:min
        :rtype: int
        """
        return self._MultiFourK

    @MultiFourK.setter
    def MultiFourK(self, MultiFourK):
        self._MultiFourK = MultiFourK

    @property
    def MultiOnline(self):
        r"""多网在线时长:min 
        :rtype: int
        """
        return self._MultiOnline

    @MultiOnline.setter
    def MultiOnline(self, MultiOnline):
        self._MultiOnline = MultiOnline

    @property
    def DeductDuration(self):
        r"""总抵扣时长:min 
        :rtype: int
        """
        return self._DeductDuration

    @DeductDuration.setter
    def DeductDuration(self, DeductDuration):
        self._DeductDuration = DeductDuration

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
        self._Voice = params.get("Voice")
        self._SD = params.get("SD")
        self._HD = params.get("HD")
        self._FHD = params.get("FHD")
        self._TwoK = params.get("TwoK")
        self._FourK = params.get("FourK")
        self._Online = params.get("Online")
        self._MultiSD = params.get("MultiSD")
        self._MultiHD = params.get("MultiHD")
        self._MultiFHD = params.get("MultiFHD")
        self._MultiTwoK = params.get("MultiTwoK")
        self._MultiFourK = params.get("MultiFourK")
        self._MultiOnline = params.get("MultiOnline")
        self._DeductDuration = params.get("DeductDuration")
        self._RequestId = params.get("RequestId")


class License(AbstractModel):
    r"""按授权查看的license列表

    """

    def __init__(self):
        r"""
        :param _Count: 该类型的license个数
        :type Count: int
        :param _Status: license状态：0:未绑定；1:已绑定；2:已停服；3:已退费
        :type Status: int
        :param _ExpireTime: 到期时间戳：s
        :type ExpireTime: str
        :param _Duration: 服务时长：s
        :type Duration: str
        :param _RemainDay: 剩余天数：天
        :type RemainDay: int
        :param _LicenseIds: 该类型的licenseId列表
        :type LicenseIds: list of str
        """
        self._Count = None
        self._Status = None
        self._ExpireTime = None
        self._Duration = None
        self._RemainDay = None
        self._LicenseIds = None

    @property
    def Count(self):
        r"""该类型的license个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Status(self):
        r"""license状态：0:未绑定；1:已绑定；2:已停服；3:已退费
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        r"""到期时间戳：s
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Duration(self):
        r"""服务时长：s
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RemainDay(self):
        r"""剩余天数：天
        :rtype: int
        """
        return self._RemainDay

    @RemainDay.setter
    def RemainDay(self, RemainDay):
        self._RemainDay = RemainDay

    @property
    def LicenseIds(self):
        r"""该类型的licenseId列表
        :rtype: list of str
        """
        return self._LicenseIds

    @LicenseIds.setter
    def LicenseIds(self, LicenseIds):
        self._LicenseIds = LicenseIds


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._Duration = params.get("Duration")
        self._RemainDay = params.get("RemainDay")
        self._LicenseIds = params.get("LicenseIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCallbackUrlRequest(AbstractModel):
    r"""ModifyCallbackUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _CallbackUrl: 回调URL
        :type CallbackUrl: str
        :param _SignKey: 回调签名密钥，用于校验回调信息的完整性
        :type SignKey: str
        """
        self._ProjectId = None
        self._CallbackUrl = None
        self._SignKey = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CallbackUrl(self):
        r"""回调URL
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def SignKey(self):
        r"""回调签名密钥，用于校验回调信息的完整性
        :rtype: str
        """
        return self._SignKey

    @SignKey.setter
    def SignKey(self, SignKey):
        self._SignKey = SignKey


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._CallbackUrl = params.get("CallbackUrl")
        self._SignKey = params.get("SignKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCallbackUrlResponse(AbstractModel):
    r"""ModifyCallbackUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Code: 响应码，0：成功，其他：失败
        :type Code: int
        :param _Msg: 响应消息，ok:成功，其他：失败
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Code = None
        self._Msg = None
        self._RequestId = None

    @property
    def Code(self):
        r"""响应码，0：成功，其他：失败
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        r"""响应消息，ok:成功，其他：失败
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyDeviceRequest(AbstractModel):
    r"""ModifyDevice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 要修改设备归属项目的项目ID
        :type ProjectId: str
        :param _DeviceId: 要修改设备的设备ID
        :type DeviceId: str
        :param _DeviceName: 修改后的设备名称，不填则不修改
        :type DeviceName: str
        :param _DeviceToken: 修改后的设备认证口令，不填则不修改
        :type DeviceToken: str
        """
        self._ProjectId = None
        self._DeviceId = None
        self._DeviceName = None
        self._DeviceToken = None

    @property
    def ProjectId(self):
        r"""要修改设备归属项目的项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""要修改设备的设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""修改后的设备名称，不填则不修改
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceToken(self):
        r"""修改后的设备认证口令，不填则不修改
        :rtype: str
        """
        return self._DeviceToken

    @DeviceToken.setter
    def DeviceToken(self, DeviceToken):
        self._DeviceToken = DeviceToken


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._DeviceToken = params.get("DeviceToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDeviceResponse(AbstractModel):
    r"""ModifyDevice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyPolicyRequest(AbstractModel):
    r"""ModifyPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 修改权限配置的项目ID
        :type ProjectId: str
        :param _RemoteDeviceId: 修改权限配置的远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceIds: 权限修改涉及的现场设备ID数组
        :type FieldDeviceIds: list of str
        :param _PolicyMode: 修改的目标权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param _ModifyMode: 修改模式，add为新增（添加现场设备I关联），remove为删除（解除现场设备关联），set为设置（更新现场设备关联）
        :type ModifyMode: str
        """
        self._ProjectId = None
        self._RemoteDeviceId = None
        self._FieldDeviceIds = None
        self._PolicyMode = None
        self._ModifyMode = None

    @property
    def ProjectId(self):
        r"""修改权限配置的项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RemoteDeviceId(self):
        r"""修改权限配置的远端设备ID
        :rtype: str
        """
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceIds(self):
        r"""权限修改涉及的现场设备ID数组
        :rtype: list of str
        """
        return self._FieldDeviceIds

    @FieldDeviceIds.setter
    def FieldDeviceIds(self, FieldDeviceIds):
        self._FieldDeviceIds = FieldDeviceIds

    @property
    def PolicyMode(self):
        r"""修改的目标权限模式，black为黑名单，white为白名单
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def ModifyMode(self):
        r"""修改模式，add为新增（添加现场设备I关联），remove为删除（解除现场设备关联），set为设置（更新现场设备关联）
        :rtype: str
        """
        return self._ModifyMode

    @ModifyMode.setter
    def ModifyMode(self, ModifyMode):
        self._ModifyMode = ModifyMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceIds = params.get("FieldDeviceIds")
        self._PolicyMode = params.get("PolicyMode")
        self._ModifyMode = params.get("ModifyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPolicyResponse(AbstractModel):
    r"""ModifyPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedInsertIds: 添加关联失败的现场设备ID列表
        :type FailedInsertIds: list of str
        :param _FailedDeleteIds: 解除关联失败的现场设备ID列表
        :type FailedDeleteIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedInsertIds = None
        self._FailedDeleteIds = None
        self._RequestId = None

    @property
    def FailedInsertIds(self):
        r"""添加关联失败的现场设备ID列表
        :rtype: list of str
        """
        return self._FailedInsertIds

    @FailedInsertIds.setter
    def FailedInsertIds(self, FailedInsertIds):
        self._FailedInsertIds = FailedInsertIds

    @property
    def FailedDeleteIds(self):
        r"""解除关联失败的现场设备ID列表
        :rtype: list of str
        """
        return self._FailedDeleteIds

    @FailedDeleteIds.setter
    def FailedDeleteIds(self, FailedDeleteIds):
        self._FailedDeleteIds = FailedDeleteIds

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
        self._FailedInsertIds = params.get("FailedInsertIds")
        self._FailedDeleteIds = params.get("FailedDeleteIds")
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    r"""ModifyProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 目标修改项目的项目ID
        :type ProjectId: str
        :param _ProjectName: 修改后的项目名称，不填则不修改
        :type ProjectName: str
        :param _ProjectDescription: 修改后的项目描述，不填则不修改
        :type ProjectDescription: str
        :param _PolicyMode: 修改后的权限模式，black为黑名单，white为白名单,不填则不修改
        :type PolicyMode: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None

    @property
    def ProjectId(self):
        r"""目标修改项目的项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""修改后的项目名称，不填则不修改
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        r"""修改后的项目描述，不填则不修改
        :rtype: str
        """
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        r"""修改后的权限模式，black为黑名单，white为白名单,不填则不修改
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    r"""ModifyProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyProjectSecModeRequest(AbstractModel):
    r"""ModifyProjectSecMode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _Mode: 安全模式  
0：关闭项目共享密钥 
1：开启项目共享密钥
        :type Mode: int
        :param _Key: 项目密钥 32位 小写英文+数字；  项目密钥模式必填
        :type Key: str
        :param _AutoRegister: 自动注册方式
0：关闭自动注册
1：仅允许现场设备自动注册
2：仅允许远端设备自动注册
3：允许现场和远端设备均自动注册
        :type AutoRegister: int
        :param _FieldListEnable: 是否允许远端获取现场设备列表（getGwList）
0：不允许
1：允许
        :type FieldListEnable: int
        """
        self._ProjectId = None
        self._Mode = None
        self._Key = None
        self._AutoRegister = None
        self._FieldListEnable = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Mode(self):
        r"""安全模式  
0：关闭项目共享密钥 
1：开启项目共享密钥
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Key(self):
        r"""项目密钥 32位 小写英文+数字；  项目密钥模式必填
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def AutoRegister(self):
        r"""自动注册方式
0：关闭自动注册
1：仅允许现场设备自动注册
2：仅允许远端设备自动注册
3：允许现场和远端设备均自动注册
        :rtype: int
        """
        return self._AutoRegister

    @AutoRegister.setter
    def AutoRegister(self, AutoRegister):
        self._AutoRegister = AutoRegister

    @property
    def FieldListEnable(self):
        r"""是否允许远端获取现场设备列表（getGwList）
0：不允许
1：允许
        :rtype: int
        """
        return self._FieldListEnable

    @FieldListEnable.setter
    def FieldListEnable(self, FieldListEnable):
        self._FieldListEnable = FieldListEnable


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Mode = params.get("Mode")
        self._Key = params.get("Key")
        self._AutoRegister = params.get("AutoRegister")
        self._FieldListEnable = params.get("FieldListEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectSecModeResponse(AbstractModel):
    r"""ModifyProjectSecMode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class MultiNet(AbstractModel):
    r"""多网的网卡状态信息

    """

    def __init__(self):
        r"""
        :param _NetId: 网卡序号
        :type NetId: int
        :param _NetIp: 网卡IP
        :type NetIp: str
        :param _Rtt: 时延，单位ms
        :type Rtt: list of int
        :param _Lost: 丢包率，单位%
        :type Lost: list of int
        :param _SendBps: 发送bps，单位kbps
        :type SendBps: list of int
        :param _RecvBps: 接收bps，单位kbps
        :type RecvBps: list of int
        """
        self._NetId = None
        self._NetIp = None
        self._Rtt = None
        self._Lost = None
        self._SendBps = None
        self._RecvBps = None

    @property
    def NetId(self):
        r"""网卡序号
        :rtype: int
        """
        return self._NetId

    @NetId.setter
    def NetId(self, NetId):
        self._NetId = NetId

    @property
    def NetIp(self):
        r"""网卡IP
        :rtype: str
        """
        return self._NetIp

    @NetIp.setter
    def NetIp(self, NetIp):
        self._NetIp = NetIp

    @property
    def Rtt(self):
        r"""时延，单位ms
        :rtype: list of int
        """
        return self._Rtt

    @Rtt.setter
    def Rtt(self, Rtt):
        self._Rtt = Rtt

    @property
    def Lost(self):
        r"""丢包率，单位%
        :rtype: list of int
        """
        return self._Lost

    @Lost.setter
    def Lost(self, Lost):
        self._Lost = Lost

    @property
    def SendBps(self):
        r"""发送bps，单位kbps
        :rtype: list of int
        """
        return self._SendBps

    @SendBps.setter
    def SendBps(self, SendBps):
        self._SendBps = SendBps

    @property
    def RecvBps(self):
        r"""接收bps，单位kbps
        :rtype: list of int
        """
        return self._RecvBps

    @RecvBps.setter
    def RecvBps(self, RecvBps):
        self._RecvBps = RecvBps


    def _deserialize(self, params):
        self._NetId = params.get("NetId")
        self._NetIp = params.get("NetIp")
        self._Rtt = params.get("Rtt")
        self._Lost = params.get("Lost")
        self._SendBps = params.get("SendBps")
        self._RecvBps = params.get("RecvBps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyInfo(AbstractModel):
    r"""权限信息

    """

    def __init__(self):
        r"""
        :param _RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceIds: 关联的现场设备ID
        :type FieldDeviceIds: list of str
        :param _ModifyTime: 最近添加时间
        :type ModifyTime: str
        """
        self._RemoteDeviceId = None
        self._FieldDeviceIds = None
        self._ModifyTime = None

    @property
    def RemoteDeviceId(self):
        r"""远端设备ID
        :rtype: str
        """
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceIds(self):
        r"""关联的现场设备ID
        :rtype: list of str
        """
        return self._FieldDeviceIds

    @FieldDeviceIds.setter
    def FieldDeviceIds(self, FieldDeviceIds):
        self._FieldDeviceIds = FieldDeviceIds

    @property
    def ModifyTime(self):
        r"""最近添加时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceIds = params.get("FieldDeviceIds")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    r"""项目信息

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _ProjectDescription: 项目描述
        :type ProjectDescription: str
        :param _PolicyMode: 项目权限模式，black为黑名单，white为白名单
        :type PolicyMode: str
        :param _ModifyTime: 项目信息修改时间
        :type ModifyTime: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._ProjectDescription = None
        self._PolicyMode = None
        self._ModifyTime = None

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""项目名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectDescription(self):
        r"""项目描述
        :rtype: str
        """
        return self._ProjectDescription

    @ProjectDescription.setter
    def ProjectDescription(self, ProjectDescription):
        self._ProjectDescription = ProjectDescription

    @property
    def PolicyMode(self):
        r"""项目权限模式，black为黑名单，white为白名单
        :rtype: str
        """
        return self._PolicyMode

    @PolicyMode.setter
    def PolicyMode(self, PolicyMode):
        self._PolicyMode = PolicyMode

    @property
    def ModifyTime(self):
        r"""项目信息修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ProjectDescription = params.get("ProjectDescription")
        self._PolicyMode = params.get("PolicyMode")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishParams(AbstractModel):
    r"""转推参数，一个任务最多支持10个推流URL。

    """

    def __init__(self):
        r"""
        :param _PublishUrl: 腾讯云直播推流地址url
        :type PublishUrl: str
        :param _IsTencentUrl: 是否是腾讯云CDN，0为转推非腾讯云CDN，1为转推腾讯CDN，不携带该参数默认为1。
        :type IsTencentUrl: int
        """
        self._PublishUrl = None
        self._IsTencentUrl = None

    @property
    def PublishUrl(self):
        r"""腾讯云直播推流地址url
        :rtype: str
        """
        return self._PublishUrl

    @PublishUrl.setter
    def PublishUrl(self, PublishUrl):
        self._PublishUrl = PublishUrl

    @property
    def IsTencentUrl(self):
        r"""是否是腾讯云CDN，0为转推非腾讯云CDN，1为转推腾讯CDN，不携带该参数默认为1。
        :rtype: int
        """
        return self._IsTencentUrl

    @IsTencentUrl.setter
    def IsTencentUrl(self, IsTencentUrl):
        self._IsTencentUrl = IsTencentUrl


    def _deserialize(self, params):
        self._PublishUrl = params.get("PublishUrl")
        self._IsTencentUrl = params.get("IsTencentUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecentSessionInfo(AbstractModel):
    r"""最新会话信息

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceId: 现场设备ID
        :type FieldDeviceId: str
        :param _Resolution: 分辨率
        :type Resolution: str
        :param _StartTime: 会话开始时间
        :type StartTime: int
        :param _LatestUpdateTime: 最后更新时间
        :type LatestUpdateTime: int
        """
        self._SessionId = None
        self._RemoteDeviceId = None
        self._FieldDeviceId = None
        self._Resolution = None
        self._StartTime = None
        self._LatestUpdateTime = None

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RemoteDeviceId(self):
        r"""远端设备ID
        :rtype: str
        """
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceId(self):
        r"""现场设备ID
        :rtype: str
        """
        return self._FieldDeviceId

    @FieldDeviceId.setter
    def FieldDeviceId(self, FieldDeviceId):
        self._FieldDeviceId = FieldDeviceId

    @property
    def Resolution(self):
        r"""分辨率
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def StartTime(self):
        r"""会话开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def LatestUpdateTime(self):
        r"""最后更新时间
        :rtype: int
        """
        return self._LatestUpdateTime

    @LatestUpdateTime.setter
    def LatestUpdateTime(self, LatestUpdateTime):
        self._LatestUpdateTime = LatestUpdateTime


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceId = params.get("FieldDeviceId")
        self._Resolution = params.get("Resolution")
        self._StartTime = params.get("StartTime")
        self._LatestUpdateTime = params.get("LatestUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionDeviceDetail(AbstractModel):
    r"""会话数据详单（按设备区分）

    """

    def __init__(self):
        r"""
        :param _DeviceType: 设备类型：field或remote
        :type DeviceType: str
        :param _StartTime: 起始点位时间，单位：秒
        :type StartTime: int
        :param _EndTime: 结束点位时间，单位：秒
        :type EndTime: int
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _Rate: 码率，单位：kbps
        :type Rate: list of int
        :param _Fps: 帧率
        :type Fps: list of int
        :param _Lost: 丢包率，单位：%
        :type Lost: list of float
        :param _NetworkLatency: 网络时延，单位：ms
        :type NetworkLatency: list of int
        :param _VideoLatency: 视频时延，单位：ms
        :type VideoLatency: list of int
        :param _CpuUsed: CPU使用率，单位：%
        :type CpuUsed: list of float
        :param _MemUsed: 内存使用率，单位：%
        :type MemUsed: list of float
        :param _TimeOffset: 时间偏移量，单位：秒
        :type TimeOffset: list of int non-negative
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _DeviceId: 设备ID
        :type DeviceId: str
        :param _Ver: sdk版本
        :type Ver: str
        :param _SdkMode: 模式(p2p/server)
        :type SdkMode: str
        :param _DecodeCost: 解码耗时，单位：ms
        :type DecodeCost: list of int
        :param _RenderConst: 【已废弃，使用RenderCost】
注意：此字段可能返回 null，表示取不到有效值。
        :type RenderConst: list of int
        :param _K100: 卡顿k100
        :type K100: list of float
        :param _K150: 卡顿k150
        :type K150: list of float
        :param _NACK: nack请求数
        :type NACK: list of int
        :param _BitRateEstimate: 服务端调控码率,单位：kbps
        :type BitRateEstimate: list of int
        :param _Width: 宽度
        :type Width: int
        :param _Height: 高度
        :type Height: int
        :param _EncodeCost: 编码耗时，单位：ms
        :type EncodeCost: list of int
        :param _CaptureCost: 采集耗时，单位：ms
        :type CaptureCost: list of int
        :param _RenderCost: 渲染耗时，单位：ms
        :type RenderCost: list of int
        :param _ConfigWidth: 配置宽度
        :type ConfigWidth: int
        :param _ConfigHeight: 配置高度
        :type ConfigHeight: int
        :param _FrameDelta: 平均帧间隔
        :type FrameDelta: list of int
        :param _MaxFrameDelta: 最大帧间隔
        :type MaxFrameDelta: list of int
        :param _TotalBitrateEstimate: 总码率评估,单位：kbps
        :type TotalBitrateEstimate: list of int
        :param _Lag100Duration: 帧间隔大于100ms的卡顿时长
        :type Lag100Duration: list of int
        :param _Lag150Duration: 帧间隔大于150ms的卡顿时长
        :type Lag150Duration: list of int
        :param _MultiMode: 是否开启多网：0 单网，1 多网
        :type MultiMode: int
        :param _MultiNet: 多网卡信息
        :type MultiNet: list of MultiNet
        """
        self._DeviceType = None
        self._StartTime = None
        self._EndTime = None
        self._SessionId = None
        self._Rate = None
        self._Fps = None
        self._Lost = None
        self._NetworkLatency = None
        self._VideoLatency = None
        self._CpuUsed = None
        self._MemUsed = None
        self._TimeOffset = None
        self._ProjectId = None
        self._DeviceId = None
        self._Ver = None
        self._SdkMode = None
        self._DecodeCost = None
        self._RenderConst = None
        self._K100 = None
        self._K150 = None
        self._NACK = None
        self._BitRateEstimate = None
        self._Width = None
        self._Height = None
        self._EncodeCost = None
        self._CaptureCost = None
        self._RenderCost = None
        self._ConfigWidth = None
        self._ConfigHeight = None
        self._FrameDelta = None
        self._MaxFrameDelta = None
        self._TotalBitrateEstimate = None
        self._Lag100Duration = None
        self._Lag150Duration = None
        self._MultiMode = None
        self._MultiNet = None

    @property
    def DeviceType(self):
        r"""设备类型：field或remote
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def StartTime(self):
        r"""起始点位时间，单位：秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束点位时间，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Rate(self):
        r"""码率，单位：kbps
        :rtype: list of int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Fps(self):
        r"""帧率
        :rtype: list of int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Lost(self):
        r"""丢包率，单位：%
        :rtype: list of float
        """
        return self._Lost

    @Lost.setter
    def Lost(self, Lost):
        self._Lost = Lost

    @property
    def NetworkLatency(self):
        r"""网络时延，单位：ms
        :rtype: list of int
        """
        return self._NetworkLatency

    @NetworkLatency.setter
    def NetworkLatency(self, NetworkLatency):
        self._NetworkLatency = NetworkLatency

    @property
    def VideoLatency(self):
        r"""视频时延，单位：ms
        :rtype: list of int
        """
        return self._VideoLatency

    @VideoLatency.setter
    def VideoLatency(self, VideoLatency):
        self._VideoLatency = VideoLatency

    @property
    def CpuUsed(self):
        r"""CPU使用率，单位：%
        :rtype: list of float
        """
        return self._CpuUsed

    @CpuUsed.setter
    def CpuUsed(self, CpuUsed):
        self._CpuUsed = CpuUsed

    @property
    def MemUsed(self):
        r"""内存使用率，单位：%
        :rtype: list of float
        """
        return self._MemUsed

    @MemUsed.setter
    def MemUsed(self, MemUsed):
        self._MemUsed = MemUsed

    @property
    def TimeOffset(self):
        r"""时间偏移量，单位：秒
        :rtype: list of int non-negative
        """
        return self._TimeOffset

    @TimeOffset.setter
    def TimeOffset(self, TimeOffset):
        self._TimeOffset = TimeOffset

    @property
    def ProjectId(self):
        r"""项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""设备ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Ver(self):
        r"""sdk版本
        :rtype: str
        """
        return self._Ver

    @Ver.setter
    def Ver(self, Ver):
        self._Ver = Ver

    @property
    def SdkMode(self):
        r"""模式(p2p/server)
        :rtype: str
        """
        return self._SdkMode

    @SdkMode.setter
    def SdkMode(self, SdkMode):
        self._SdkMode = SdkMode

    @property
    def DecodeCost(self):
        r"""解码耗时，单位：ms
        :rtype: list of int
        """
        return self._DecodeCost

    @DecodeCost.setter
    def DecodeCost(self, DecodeCost):
        self._DecodeCost = DecodeCost

    @property
    def RenderConst(self):
        warnings.warn("parameter `RenderConst` is deprecated", DeprecationWarning) 

        r"""【已废弃，使用RenderCost】
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._RenderConst

    @RenderConst.setter
    def RenderConst(self, RenderConst):
        warnings.warn("parameter `RenderConst` is deprecated", DeprecationWarning) 

        self._RenderConst = RenderConst

    @property
    def K100(self):
        r"""卡顿k100
        :rtype: list of float
        """
        return self._K100

    @K100.setter
    def K100(self, K100):
        self._K100 = K100

    @property
    def K150(self):
        r"""卡顿k150
        :rtype: list of float
        """
        return self._K150

    @K150.setter
    def K150(self, K150):
        self._K150 = K150

    @property
    def NACK(self):
        r"""nack请求数
        :rtype: list of int
        """
        return self._NACK

    @NACK.setter
    def NACK(self, NACK):
        self._NACK = NACK

    @property
    def BitRateEstimate(self):
        r"""服务端调控码率,单位：kbps
        :rtype: list of int
        """
        return self._BitRateEstimate

    @BitRateEstimate.setter
    def BitRateEstimate(self, BitRateEstimate):
        self._BitRateEstimate = BitRateEstimate

    @property
    def Width(self):
        r"""宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def EncodeCost(self):
        r"""编码耗时，单位：ms
        :rtype: list of int
        """
        return self._EncodeCost

    @EncodeCost.setter
    def EncodeCost(self, EncodeCost):
        self._EncodeCost = EncodeCost

    @property
    def CaptureCost(self):
        r"""采集耗时，单位：ms
        :rtype: list of int
        """
        return self._CaptureCost

    @CaptureCost.setter
    def CaptureCost(self, CaptureCost):
        self._CaptureCost = CaptureCost

    @property
    def RenderCost(self):
        r"""渲染耗时，单位：ms
        :rtype: list of int
        """
        return self._RenderCost

    @RenderCost.setter
    def RenderCost(self, RenderCost):
        self._RenderCost = RenderCost

    @property
    def ConfigWidth(self):
        r"""配置宽度
        :rtype: int
        """
        return self._ConfigWidth

    @ConfigWidth.setter
    def ConfigWidth(self, ConfigWidth):
        self._ConfigWidth = ConfigWidth

    @property
    def ConfigHeight(self):
        r"""配置高度
        :rtype: int
        """
        return self._ConfigHeight

    @ConfigHeight.setter
    def ConfigHeight(self, ConfigHeight):
        self._ConfigHeight = ConfigHeight

    @property
    def FrameDelta(self):
        r"""平均帧间隔
        :rtype: list of int
        """
        return self._FrameDelta

    @FrameDelta.setter
    def FrameDelta(self, FrameDelta):
        self._FrameDelta = FrameDelta

    @property
    def MaxFrameDelta(self):
        r"""最大帧间隔
        :rtype: list of int
        """
        return self._MaxFrameDelta

    @MaxFrameDelta.setter
    def MaxFrameDelta(self, MaxFrameDelta):
        self._MaxFrameDelta = MaxFrameDelta

    @property
    def TotalBitrateEstimate(self):
        r"""总码率评估,单位：kbps
        :rtype: list of int
        """
        return self._TotalBitrateEstimate

    @TotalBitrateEstimate.setter
    def TotalBitrateEstimate(self, TotalBitrateEstimate):
        self._TotalBitrateEstimate = TotalBitrateEstimate

    @property
    def Lag100Duration(self):
        r"""帧间隔大于100ms的卡顿时长
        :rtype: list of int
        """
        return self._Lag100Duration

    @Lag100Duration.setter
    def Lag100Duration(self, Lag100Duration):
        self._Lag100Duration = Lag100Duration

    @property
    def Lag150Duration(self):
        r"""帧间隔大于150ms的卡顿时长
        :rtype: list of int
        """
        return self._Lag150Duration

    @Lag150Duration.setter
    def Lag150Duration(self, Lag150Duration):
        self._Lag150Duration = Lag150Duration

    @property
    def MultiMode(self):
        r"""是否开启多网：0 单网，1 多网
        :rtype: int
        """
        return self._MultiMode

    @MultiMode.setter
    def MultiMode(self, MultiMode):
        self._MultiMode = MultiMode

    @property
    def MultiNet(self):
        r"""多网卡信息
        :rtype: list of MultiNet
        """
        return self._MultiNet

    @MultiNet.setter
    def MultiNet(self, MultiNet):
        self._MultiNet = MultiNet


    def _deserialize(self, params):
        self._DeviceType = params.get("DeviceType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SessionId = params.get("SessionId")
        self._Rate = params.get("Rate")
        self._Fps = params.get("Fps")
        self._Lost = params.get("Lost")
        self._NetworkLatency = params.get("NetworkLatency")
        self._VideoLatency = params.get("VideoLatency")
        self._CpuUsed = params.get("CpuUsed")
        self._MemUsed = params.get("MemUsed")
        self._TimeOffset = params.get("TimeOffset")
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._Ver = params.get("Ver")
        self._SdkMode = params.get("SdkMode")
        self._DecodeCost = params.get("DecodeCost")
        self._RenderConst = params.get("RenderConst")
        self._K100 = params.get("K100")
        self._K150 = params.get("K150")
        self._NACK = params.get("NACK")
        self._BitRateEstimate = params.get("BitRateEstimate")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._EncodeCost = params.get("EncodeCost")
        self._CaptureCost = params.get("CaptureCost")
        self._RenderCost = params.get("RenderCost")
        self._ConfigWidth = params.get("ConfigWidth")
        self._ConfigHeight = params.get("ConfigHeight")
        self._FrameDelta = params.get("FrameDelta")
        self._MaxFrameDelta = params.get("MaxFrameDelta")
        self._TotalBitrateEstimate = params.get("TotalBitrateEstimate")
        self._Lag100Duration = params.get("Lag100Duration")
        self._Lag150Duration = params.get("Lag150Duration")
        self._MultiMode = params.get("MultiMode")
        if params.get("MultiNet") is not None:
            self._MultiNet = []
            for item in params.get("MultiNet"):
                obj = MultiNet()
                obj._deserialize(item)
                self._MultiNet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionInfo(AbstractModel):
    r"""会话信息

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _RemoteDeviceId: 远端设备ID
        :type RemoteDeviceId: str
        :param _FieldDeviceId: 现场设备ID
        :type FieldDeviceId: str
        :param _Resolution: 分辨率
        :type Resolution: str
        :param _StartTime: 会话开始时间
        :type StartTime: int
        :param _EndTime: 会话结束时间
        :type EndTime: int
        :param _Quality: 通话质量：good|normal|bad，对应优良差
        :type Quality: str
        """
        self._SessionId = None
        self._RemoteDeviceId = None
        self._FieldDeviceId = None
        self._Resolution = None
        self._StartTime = None
        self._EndTime = None
        self._Quality = None

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RemoteDeviceId(self):
        r"""远端设备ID
        :rtype: str
        """
        return self._RemoteDeviceId

    @RemoteDeviceId.setter
    def RemoteDeviceId(self, RemoteDeviceId):
        self._RemoteDeviceId = RemoteDeviceId

    @property
    def FieldDeviceId(self):
        r"""现场设备ID
        :rtype: str
        """
        return self._FieldDeviceId

    @FieldDeviceId.setter
    def FieldDeviceId(self, FieldDeviceId):
        self._FieldDeviceId = FieldDeviceId

    @property
    def Resolution(self):
        r"""分辨率
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def StartTime(self):
        r"""会话开始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""会话结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Quality(self):
        r"""通话质量：good|normal|bad，对应优良差
        :rtype: str
        """
        return self._Quality

    @Quality.setter
    def Quality(self, Quality):
        self._Quality = Quality


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._RemoteDeviceId = params.get("RemoteDeviceId")
        self._FieldDeviceId = params.get("FieldDeviceId")
        self._Resolution = params.get("Resolution")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Quality = params.get("Quality")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionIntervalStatistic(AbstractModel):
    r"""单位时间间隔的会话统计数据

    """

    def __init__(self):
        r"""
        :param _ActiveFieldDeviceNum: 活跃现场设备数
        :type ActiveFieldDeviceNum: int
        :param _ActiveRemoteDeviceNum: 活跃远端设备数
        :type ActiveRemoteDeviceNum: int
        :param _SessionNum: 会话数量
        :type SessionNum: int
        :param _TotalDuration: 会话时长，单位：分钟
        :type TotalDuration: int
        :param _StartTime: 时间戳，单位：秒
        :type StartTime: int
        :param _EndTime: 时间戳，单位：秒
        :type EndTime: int
        :param _NotBadSessionRatio: 优良会话占比，单位：%
        :type NotBadSessionRatio: int
        """
        self._ActiveFieldDeviceNum = None
        self._ActiveRemoteDeviceNum = None
        self._SessionNum = None
        self._TotalDuration = None
        self._StartTime = None
        self._EndTime = None
        self._NotBadSessionRatio = None

    @property
    def ActiveFieldDeviceNum(self):
        r"""活跃现场设备数
        :rtype: int
        """
        return self._ActiveFieldDeviceNum

    @ActiveFieldDeviceNum.setter
    def ActiveFieldDeviceNum(self, ActiveFieldDeviceNum):
        self._ActiveFieldDeviceNum = ActiveFieldDeviceNum

    @property
    def ActiveRemoteDeviceNum(self):
        r"""活跃远端设备数
        :rtype: int
        """
        return self._ActiveRemoteDeviceNum

    @ActiveRemoteDeviceNum.setter
    def ActiveRemoteDeviceNum(self, ActiveRemoteDeviceNum):
        self._ActiveRemoteDeviceNum = ActiveRemoteDeviceNum

    @property
    def SessionNum(self):
        r"""会话数量
        :rtype: int
        """
        return self._SessionNum

    @SessionNum.setter
    def SessionNum(self, SessionNum):
        self._SessionNum = SessionNum

    @property
    def TotalDuration(self):
        r"""会话时长，单位：分钟
        :rtype: int
        """
        return self._TotalDuration

    @TotalDuration.setter
    def TotalDuration(self, TotalDuration):
        self._TotalDuration = TotalDuration

    @property
    def StartTime(self):
        r"""时间戳，单位：秒
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""时间戳，单位：秒
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def NotBadSessionRatio(self):
        r"""优良会话占比，单位：%
        :rtype: int
        """
        return self._NotBadSessionRatio

    @NotBadSessionRatio.setter
    def NotBadSessionRatio(self, NotBadSessionRatio):
        self._NotBadSessionRatio = NotBadSessionRatio


    def _deserialize(self, params):
        self._ActiveFieldDeviceNum = params.get("ActiveFieldDeviceNum")
        self._ActiveRemoteDeviceNum = params.get("ActiveRemoteDeviceNum")
        self._SessionNum = params.get("SessionNum")
        self._TotalDuration = params.get("TotalDuration")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._NotBadSessionRatio = params.get("NotBadSessionRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishLiveStreamRequest(AbstractModel):
    r"""StartPublishLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WithTranscoding: 是否转码，0表示无需转码，1表示需要转码。是否收取转码费是由WithTranscoding参数决定的，WithTranscoding为0，表示旁路转推，不会收取转码费用，WithTranscoding为1，表示混流转推，会收取转码费用。 示例值：1
        :type WithTranscoding: int
        :param _MaxIdleTime: 所有参与混流转推的主播持续离开TRTC房间或切换成观众超过MaxIdleTime的时长，自动停止转推，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
        :type MaxIdleTime: int
        :param _VideoParams: 转推视频参数
        :type VideoParams: :class:`tencentcloud.trro.v20220325.models.VideoParams`
        :param _PublishParams: 转推的URL参数，一个任务最多支持10个推流URL
        :type PublishParams: list of PublishParams
        """
        self._WithTranscoding = None
        self._MaxIdleTime = None
        self._VideoParams = None
        self._PublishParams = None

    @property
    def WithTranscoding(self):
        r"""是否转码，0表示无需转码，1表示需要转码。是否收取转码费是由WithTranscoding参数决定的，WithTranscoding为0，表示旁路转推，不会收取转码费用，WithTranscoding为1，表示混流转推，会收取转码费用。 示例值：1
        :rtype: int
        """
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def MaxIdleTime(self):
        r"""所有参与混流转推的主播持续离开TRTC房间或切换成观众超过MaxIdleTime的时长，自动停止转推，单位：秒。默认值为 30 秒，该值需大于等于 5秒，且小于等于 86400秒(24小时)。
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def VideoParams(self):
        r"""转推视频参数
        :rtype: :class:`tencentcloud.trro.v20220325.models.VideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def PublishParams(self):
        r"""转推的URL参数，一个任务最多支持10个推流URL
        :rtype: list of PublishParams
        """
        return self._PublishParams

    @PublishParams.setter
    def PublishParams(self, PublishParams):
        self._PublishParams = PublishParams


    def _deserialize(self, params):
        self._WithTranscoding = params.get("WithTranscoding")
        self._MaxIdleTime = params.get("MaxIdleTime")
        if params.get("VideoParams") is not None:
            self._VideoParams = VideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("PublishParams") is not None:
            self._PublishParams = []
            for item in params.get("PublishParams"):
                obj = PublishParams()
                obj._deserialize(item)
                self._PublishParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishLiveStreamResponse(AbstractModel):
    r"""StartPublishLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 用于唯一标识转推任务，由腾讯云服务端生成，后续停止请求需要携带TaskiD参数。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""用于唯一标识转推任务，由腾讯云服务端生成，后续停止请求需要携带TaskiD参数。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopPublishLiveStreamRequest(AbstractModel):
    r"""StopPublishLiveStream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 唯一标识转推任务。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""唯一标识转推任务。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishLiveStreamResponse(AbstractModel):
    r"""StopPublishLiveStream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class VideoList(AbstractModel):
    r"""原视频流参数列表

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目id
        :type ProjectId: str
        :param _DeviceId: 设备id
        :type DeviceId: str
        :param _VideoStreamId: 流id
        :type VideoStreamId: int
        :param _Width: 子画面在输出时的宽度，单位为像素值，不填默认为0。
        :type Width: int
        :param _Height: 子画面在输出时的高度，单位为像素值，不填默认为0。
        :type Height: int
        """
        self._ProjectId = None
        self._DeviceId = None
        self._VideoStreamId = None
        self._Width = None
        self._Height = None

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DeviceId(self):
        r"""设备id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def VideoStreamId(self):
        r"""流id
        :rtype: int
        """
        return self._VideoStreamId

    @VideoStreamId.setter
    def VideoStreamId(self, VideoStreamId):
        self._VideoStreamId = VideoStreamId

    @property
    def Width(self):
        r"""子画面在输出时的宽度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""子画面在输出时的高度，单位为像素值，不填默认为0。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DeviceId = params.get("DeviceId")
        self._VideoStreamId = params.get("VideoStreamId")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoParams(AbstractModel):
    r"""转推视频参数

    """

    def __init__(self):
        r"""
        :param _Width: 输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :type Width: int
        :param _Height: 输出流高，音视频输出时必填。取值范围[0,1080]，单位为像素值。
        :type Height: int
        :param _Fps: 输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :type Fps: int
        :param _BitRate: 输出流码率，音视频输出时必填。取值范围[1,10000]，单位为kbps。
        :type BitRate: int
        :param _Gop: 输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :type Gop: int
        :param _VideoList: 转推视频流列表
        :type VideoList: list of VideoList
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None
        self._VideoList = None

    @property
    def Width(self):
        r"""输出流宽，音视频输出时必填。取值范围[0,1920]，单位为像素值。
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        r"""输出流高，音视频输出时必填。取值范围[0,1080]，单位为像素值。
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        r"""输出流帧率，音视频输出时必填。取值范围[1,60]，表示混流的输出帧率可选范围为1到60fps。
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        r"""输出流码率，音视频输出时必填。取值范围[1,10000]，单位为kbps。
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        r"""输出流gop，音视频输出时必填。取值范围[1,5]，单位为秒。
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop

    @property
    def VideoList(self):
        r"""转推视频流列表
        :rtype: list of VideoList
        """
        return self._VideoList

    @VideoList.setter
    def VideoList(self, VideoList):
        self._VideoList = VideoList


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        if params.get("VideoList") is not None:
            self._VideoList = []
            for item in params.get("VideoList"):
                obj = VideoList()
                obj._deserialize(item)
                self._VideoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        