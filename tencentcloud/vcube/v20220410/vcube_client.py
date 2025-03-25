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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.vcube.v20220410 import models


class VcubeClient(AbstractClient):
    _apiVersion = '2022-04-10'
    _endpoint = 'vcube.tencentcloudapi.com'
    _service = 'vcube'


    def CreateActivityLicense(self, request):
        """创建活动license

        :param request: Request instance for CreateActivityLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateActivityLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateActivityLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateActivityLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CreateActivityLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationAndBindLicense(self, request):
        """创建应用并绑定license或者XMagic

        :param request: Request instance for CreateApplicationAndBindLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateApplicationAndBindLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateApplicationAndBindLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationAndBindLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationAndBindLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationAndVideo(self, request):
        """创建应用和视频播放license 目前只有国际站可以用

        :param request: Request instance for CreateApplicationAndVideo.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateApplicationAndVideoRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateApplicationAndVideoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationAndVideo", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationAndVideoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplicationAndWebPlayerLicense(self, request):
        """创建 web 播放器基础版

        :param request: Request instance for CreateApplicationAndWebPlayerLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateApplicationAndWebPlayerLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateApplicationAndWebPlayerLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationAndWebPlayerLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationAndWebPlayerLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLicense(self, request):
        """绑定license

        :param request: Request instance for CreateLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTestXMagic(self, request):
        """申请开通测试版腾讯特效

        :param request: Request instance for CreateTestXMagic.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateTestXMagicRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateTestXMagicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTestXMagic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTestXMagicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrialApplicationAndLicense(self, request):
        """创建测试应用并开通测试 license

        :param request: Request instance for CreateTrialApplicationAndLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateTrialApplicationAndLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateTrialApplicationAndLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrialApplicationAndLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrialApplicationAndLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrialLicense(self, request):
        """开通测试license

        :param request: Request instance for CreateTrialLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateTrialLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateTrialLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrialLicense", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrialLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateXMagic(self, request):
        """x08开通正式版优图美视功能，针对已经有Application的情况

        :param request: Request instance for CreateXMagic.
        :type request: :class:`tencentcloud.vcube.v20220410.models.CreateXMagicRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.CreateXMagicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateXMagic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateXMagicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFeatureList(self, request):
        """查询功能列表

        :param request: Request instance for DescribeFeatureList.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeFeatureListRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeFeatureListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFeatureList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFeatureListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseList(self, request):
        """总览页查询临期License列表，和统计数据

        :param request: Request instance for DescribeLicenseList.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeLicenseListRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeLicenseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNews(self, request):
        """查询产品动态

        :param request: Request instance for DescribeNews.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeNewsRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeNewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSTS(self, request):
        """获取临时秘钥，用于图片，特效包上传

        :param request: Request instance for DescribeSTS.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeSTSRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeSTSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSTS", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSTSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrialFeature(self, request):
        """查询测试应用可以开通的功能

        :param request: Request instance for DescribeTrialFeature.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeTrialFeatureRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeTrialFeatureResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrialFeature", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrialFeatureResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserConfig(self, request):
        """查询用户个性配置

        :param request: Request instance for DescribeUserConfig.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeUserConfigRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeUserConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVcubeApplicationAndLicense(self, request):
        """查询用户license， 按照应用分类

        :param request: Request instance for DescribeVcubeApplicationAndLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeApplicationAndLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeApplicationAndLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVcubeApplicationAndLicense", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVcubeApplicationAndLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVcubeApplicationAndPlayList(self, request):
        """查询用户点播直播等license， 按照应用分类,国际站专用

        :param request: Request instance for DescribeVcubeApplicationAndPlayList.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeApplicationAndPlayListRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeApplicationAndPlayListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVcubeApplicationAndPlayList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVcubeApplicationAndPlayListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVcubeApplicationAndXMagicList(self, request):
        """查询用户优图license， 按照应用分类

        :param request: Request instance for DescribeVcubeApplicationAndXMagicList.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeApplicationAndXMagicListRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeApplicationAndXMagicListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVcubeApplicationAndXMagicList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVcubeApplicationAndXMagicListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVcubeResources(self, request):
        """查询视立方 license 资源，所有的资源包

        :param request: Request instance for DescribeVcubeResources.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeResourcesRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVcubeResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVcubeResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVcubeResourcesList(self, request):
        """查询视立方 license 资源，包括资源包赠送和直接购买的资源

        :param request: Request instance for DescribeVcubeResourcesList.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeResourcesListRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeVcubeResourcesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVcubeResourcesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVcubeResourcesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeXMagicResource(self, request):
        """用途美视资源包用于开通正式优图美视

        :param request: Request instance for DescribeXMagicResource.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeXMagicResourceRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeXMagicResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeXMagicResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeXMagicResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeXMagicResourceList(self, request):
        """用于优图美视资源列表展示

        :param request: Request instance for DescribeXMagicResourceList.
        :type request: :class:`tencentcloud.vcube.v20220410.models.DescribeXMagicResourceListRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.DescribeXMagicResourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeXMagicResourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeXMagicResourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplication(self, request):
        """更改测试包名信息

        :param request: Request instance for ModifyApplication.
        :type request: :class:`tencentcloud.vcube.v20220410.models.ModifyApplicationRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.ModifyApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFormalApplication(self, request):
        """修改正式应用的包名称

        :param request: Request instance for ModifyFormalApplication.
        :type request: :class:`tencentcloud.vcube.v20220410.models.ModifyFormalApplicationRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.ModifyFormalApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFormalApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFormalApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicense(self, request):
        """正式license 升降配，点播精简版、基础版

        :param request: Request instance for ModifyLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.ModifyLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.ModifyLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicense", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPresetApplication(self, request):
        """修改内置应用包名

        :param request: Request instance for ModifyPresetApplication.
        :type request: :class:`tencentcloud.vcube.v20220410.models.ModifyPresetApplicationRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.ModifyPresetApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPresetApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPresetApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTrialLicense(self, request):
        """续期测试license

        :param request: Request instance for ModifyTrialLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.ModifyTrialLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.ModifyTrialLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTrialLicense", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTrialLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyXMagic(self, request):
        """使用一个腾讯特效资源，更新现在的腾讯特效license，license功能和到期时间会以新的资源为准，老资源会被替换下来

        :param request: Request instance for ModifyXMagic.
        :type request: :class:`tencentcloud.vcube.v20220410.models.ModifyXMagicRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.ModifyXMagicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyXMagic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyXMagicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewLicense(self, request):
        """正式license 续期与变更有效期

        :param request: Request instance for RenewLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.RenewLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.RenewLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewLicense", params, headers=headers)
            response = json.loads(body)
            model = models.RenewLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewTestXMagic(self, request):
        """续期测试版优图美视

        :param request: Request instance for RenewTestXMagic.
        :type request: :class:`tencentcloud.vcube.v20220410.models.RenewTestXMagicRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.RenewTestXMagicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewTestXMagic", params, headers=headers)
            response = json.loads(body)
            model = models.RenewTestXMagicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewVideo(self, request):
        """续期国际站视频播放功能和中国站web基础版

        :param request: Request instance for RenewVideo.
        :type request: :class:`tencentcloud.vcube.v20220410.models.RenewVideoRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.RenewVideoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewVideo", params, headers=headers)
            response = json.loads(body)
            model = models.RenewVideoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTestXMagic(self, request):
        """将测试xmagic升级到正式版

        :param request: Request instance for UpdateTestXMagic.
        :type request: :class:`tencentcloud.vcube.v20220410.models.UpdateTestXMagicRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.UpdateTestXMagicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTestXMagic", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTestXMagicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTrialLicense(self, request):
        """测试 license 升级为正式 license

        :param request: Request instance for UpdateTrialLicense.
        :type request: :class:`tencentcloud.vcube.v20220410.models.UpdateTrialLicenseRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.UpdateTrialLicenseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTrialLicense", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTrialLicenseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateXMagic(self, request):
        """更新优图美视的申请信息 Status 为2，3的时候可用

        :param request: Request instance for UpdateXMagic.
        :type request: :class:`tencentcloud.vcube.v20220410.models.UpdateXMagicRequest`
        :rtype: :class:`tencentcloud.vcube.v20220410.models.UpdateXMagicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateXMagic", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateXMagicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))