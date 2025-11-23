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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.vcube.v20220410 import models
from typing import Dict


class VcubeClient(AbstractClient):
    _apiVersion = '2022-04-10'
    _endpoint = 'vcube.tencentcloudapi.com'
    _service = 'vcube'

    async def CreateActivityLicense(
            self,
            request: models.CreateActivityLicenseRequest,
            opts: Dict = None,
    ) -> models.CreateActivityLicenseResponse:
        """
        创建活动license
        """
        
        kwargs = {}
        kwargs["action"] = "CreateActivityLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateActivityLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationAndBindLicense(
            self,
            request: models.CreateApplicationAndBindLicenseRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationAndBindLicenseResponse:
        """
        创建应用并绑定license或者XMagic
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationAndBindLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationAndBindLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationAndVideo(
            self,
            request: models.CreateApplicationAndVideoRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationAndVideoResponse:
        """
        创建应用和视频播放license 目前只有国际站可以用
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationAndVideo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationAndVideoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationAndWebPlayerLicense(
            self,
            request: models.CreateApplicationAndWebPlayerLicenseRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationAndWebPlayerLicenseResponse:
        """
        创建 web 播放器基础版
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationAndWebPlayerLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationAndWebPlayerLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLicense(
            self,
            request: models.CreateLicenseRequest,
            opts: Dict = None,
    ) -> models.CreateLicenseResponse:
        """
        绑定license
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTestXMagic(
            self,
            request: models.CreateTestXMagicRequest,
            opts: Dict = None,
    ) -> models.CreateTestXMagicResponse:
        """
        申请开通测试版腾讯特效
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTestXMagic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTestXMagicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrialApplicationAndLicense(
            self,
            request: models.CreateTrialApplicationAndLicenseRequest,
            opts: Dict = None,
    ) -> models.CreateTrialApplicationAndLicenseResponse:
        """
        创建测试应用并开通测试 license
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrialApplicationAndLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrialApplicationAndLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrialLicense(
            self,
            request: models.CreateTrialLicenseRequest,
            opts: Dict = None,
    ) -> models.CreateTrialLicenseResponse:
        """
        开通测试license
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrialLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrialLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateXMagic(
            self,
            request: models.CreateXMagicRequest,
            opts: Dict = None,
    ) -> models.CreateXMagicResponse:
        """
        x08开通正式版优图美视功能，针对已经有Application的情况
        """
        
        kwargs = {}
        kwargs["action"] = "CreateXMagic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateXMagicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationAndVideoLicense(
            self,
            request: models.DeleteApplicationAndVideoLicenseRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationAndVideoLicenseResponse:
        """
        删除视频播放器 License 和相关应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationAndVideoLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationAndVideoLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationAndWebPlayerLicense(
            self,
            request: models.DeleteApplicationAndWebPlayerLicenseRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationAndWebPlayerLicenseResponse:
        """
        删除web播放器license和应用
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationAndWebPlayerLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationAndWebPlayerLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFeatureList(
            self,
            request: models.DescribeFeatureListRequest,
            opts: Dict = None,
    ) -> models.DescribeFeatureListResponse:
        """
        查询功能列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFeatureList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFeatureListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLicenseList(
            self,
            request: models.DescribeLicenseListRequest,
            opts: Dict = None,
    ) -> models.DescribeLicenseListResponse:
        """
        总览页查询临期License列表，和统计数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLicenseList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLicenseListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNews(
            self,
            request: models.DescribeNewsRequest,
            opts: Dict = None,
    ) -> models.DescribeNewsResponse:
        """
        查询产品动态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSTS(
            self,
            request: models.DescribeSTSRequest,
            opts: Dict = None,
    ) -> models.DescribeSTSResponse:
        """
        获取临时秘钥，用于图片，特效包上传
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSTS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSTSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrialFeature(
            self,
            request: models.DescribeTrialFeatureRequest,
            opts: Dict = None,
    ) -> models.DescribeTrialFeatureResponse:
        """
        查询测试应用可以开通的功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrialFeature"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrialFeatureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserConfig(
            self,
            request: models.DescribeUserConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserConfigResponse:
        """
        查询用户个性配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVcubeApplicationAndLicense(
            self,
            request: models.DescribeVcubeApplicationAndLicenseRequest,
            opts: Dict = None,
    ) -> models.DescribeVcubeApplicationAndLicenseResponse:
        """
        查询用户license， 按照应用分类
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVcubeApplicationAndLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVcubeApplicationAndLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVcubeApplicationAndPlayList(
            self,
            request: models.DescribeVcubeApplicationAndPlayListRequest,
            opts: Dict = None,
    ) -> models.DescribeVcubeApplicationAndPlayListResponse:
        """
        查询用户点播直播等license， 按照应用分类,国际站专用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVcubeApplicationAndPlayList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVcubeApplicationAndPlayListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVcubeApplicationAndXMagicList(
            self,
            request: models.DescribeVcubeApplicationAndXMagicListRequest,
            opts: Dict = None,
    ) -> models.DescribeVcubeApplicationAndXMagicListResponse:
        """
        查询用户优图license， 按照应用分类
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVcubeApplicationAndXMagicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVcubeApplicationAndXMagicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVcubeResources(
            self,
            request: models.DescribeVcubeResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeVcubeResourcesResponse:
        """
        查询视立方 license 资源，所有的资源包
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVcubeResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVcubeResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVcubeResourcesList(
            self,
            request: models.DescribeVcubeResourcesListRequest,
            opts: Dict = None,
    ) -> models.DescribeVcubeResourcesListResponse:
        """
        查询视立方 license 资源，包括资源包赠送和直接购买的资源
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVcubeResourcesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVcubeResourcesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeXMagicResource(
            self,
            request: models.DescribeXMagicResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeXMagicResourceResponse:
        """
        用途美视资源包用于开通正式优图美视
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeXMagicResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeXMagicResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeXMagicResourceList(
            self,
            request: models.DescribeXMagicResourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeXMagicResourceListResponse:
        """
        用于优图美视资源列表展示
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeXMagicResourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeXMagicResourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplication(
            self,
            request: models.ModifyApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationResponse:
        """
        更改测试包名信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFormalApplication(
            self,
            request: models.ModifyFormalApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyFormalApplicationResponse:
        """
        修改正式应用的包名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFormalApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFormalApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLicense(
            self,
            request: models.ModifyLicenseRequest,
            opts: Dict = None,
    ) -> models.ModifyLicenseResponse:
        """
        正式license 升降配，点播精简版、基础版
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPresetApplication(
            self,
            request: models.ModifyPresetApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyPresetApplicationResponse:
        """
        修改内置应用包名
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPresetApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPresetApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTrialLicense(
            self,
            request: models.ModifyTrialLicenseRequest,
            opts: Dict = None,
    ) -> models.ModifyTrialLicenseResponse:
        """
        续期测试license
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTrialLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTrialLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyXMagic(
            self,
            request: models.ModifyXMagicRequest,
            opts: Dict = None,
    ) -> models.ModifyXMagicResponse:
        """
        使用一个腾讯特效资源，更新现在的腾讯特效license，license功能和到期时间会以新的资源为准，老资源会被替换下来
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyXMagic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyXMagicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewLicense(
            self,
            request: models.RenewLicenseRequest,
            opts: Dict = None,
    ) -> models.RenewLicenseResponse:
        """
        正式license 续期与变更有效期
        """
        
        kwargs = {}
        kwargs["action"] = "RenewLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewTestXMagic(
            self,
            request: models.RenewTestXMagicRequest,
            opts: Dict = None,
    ) -> models.RenewTestXMagicResponse:
        """
        续期测试版优图美视
        """
        
        kwargs = {}
        kwargs["action"] = "RenewTestXMagic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewTestXMagicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewVideo(
            self,
            request: models.RenewVideoRequest,
            opts: Dict = None,
    ) -> models.RenewVideoResponse:
        """
        续期国际站视频播放功能和中国站web基础版
        """
        
        kwargs = {}
        kwargs["action"] = "RenewVideo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewVideoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTestXMagic(
            self,
            request: models.UpdateTestXMagicRequest,
            opts: Dict = None,
    ) -> models.UpdateTestXMagicResponse:
        """
        将测试xmagic升级到正式版
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTestXMagic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTestXMagicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTrialLicense(
            self,
            request: models.UpdateTrialLicenseRequest,
            opts: Dict = None,
    ) -> models.UpdateTrialLicenseResponse:
        """
        测试 license 升级为正式 license
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTrialLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTrialLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateXMagic(
            self,
            request: models.UpdateXMagicRequest,
            opts: Dict = None,
    ) -> models.UpdateXMagicResponse:
        """
        更新优图美视的申请信息 Status 为2，3的时候可用
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateXMagic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateXMagicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)