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
from tencentcloud.iottid.v20190411 import models


class IottidClient(AbstractClient):
    _apiVersion = '2019-04-11'
    _endpoint = 'iottid.tencentcloudapi.com'
    _service = 'iottid'


    def AuthTestTid(self, request):
        """单向认证测试TID

        :param request: Request instance for AuthTestTid.
        :type request: :class:`tencentcloud.iottid.v20190411.models.AuthTestTidRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.AuthTestTidResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthTestTid", params, headers=headers)
            response = json.loads(body)
            model = models.AuthTestTidResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BurnTidNotify(self, request):
        """安全芯片TID烧录回执

        :param request: Request instance for BurnTidNotify.
        :type request: :class:`tencentcloud.iottid.v20190411.models.BurnTidNotifyRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.BurnTidNotifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BurnTidNotify", params, headers=headers)
            response = json.loads(body)
            model = models.BurnTidNotifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeliverTidNotify(self, request):
        """安全芯片为载体的TID空发回执，绑定TID与订单号。

        :param request: Request instance for DeliverTidNotify.
        :type request: :class:`tencentcloud.iottid.v20190411.models.DeliverTidNotifyRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.DeliverTidNotifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeliverTidNotify", params, headers=headers)
            response = json.loads(body)
            model = models.DeliverTidNotifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeliverTids(self, request):
        """设备服务商请求空发产品订单的TID信息

        :param request: Request instance for DeliverTids.
        :type request: :class:`tencentcloud.iottid.v20190411.models.DeliverTidsRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.DeliverTidsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeliverTids", params, headers=headers)
            response = json.loads(body)
            model = models.DeliverTidsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAvailableLibCount(self, request):
        """查询指定订单的可空发的白盒密钥数量

        :param request: Request instance for DescribeAvailableLibCount.
        :type request: :class:`tencentcloud.iottid.v20190411.models.DescribeAvailableLibCountRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.DescribeAvailableLibCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableLibCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableLibCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePermission(self, request):
        """查询企业用户TID平台控制台权限

        :param request: Request instance for DescribePermission.
        :type request: :class:`tencentcloud.iottid.v20190411.models.DescribePermissionRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.DescribePermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadTids(self, request):
        """下载芯片订单的TID

        :param request: Request instance for DownloadTids.
        :type request: :class:`tencentcloud.iottid.v20190411.models.DownloadTidsRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.DownloadTidsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadTids", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadTidsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadDeviceUniqueCode(self, request):
        """上传硬件唯一标识码，是软加固设备身份参数。本接口如遇到错误数据，则所有当次上传数据失效。

        :param request: Request instance for UploadDeviceUniqueCode.
        :type request: :class:`tencentcloud.iottid.v20190411.models.UploadDeviceUniqueCodeRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.UploadDeviceUniqueCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadDeviceUniqueCode", params, headers=headers)
            response = json.loads(body)
            model = models.UploadDeviceUniqueCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VerifyChipBurnInfo(self, request):
        """下载控制台验证芯片烧录信息，保证TID与中心信息一致

        :param request: Request instance for VerifyChipBurnInfo.
        :type request: :class:`tencentcloud.iottid.v20190411.models.VerifyChipBurnInfoRequest`
        :rtype: :class:`tencentcloud.iottid.v20190411.models.VerifyChipBurnInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyChipBurnInfo", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyChipBurnInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)