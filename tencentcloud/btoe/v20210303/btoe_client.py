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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.btoe.v20210303 import models


class BtoeClient(AbstractClient):
    _apiVersion = '2021-03-03'
    _endpoint = 'btoe.tencentcloudapi.com'
    _service = 'btoe'


    def CreateAudioDeposit(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的音频原文件或下载URL，BTOE对音频原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。音频类型支持格式：mp3、wav、wma、midi、flac；原文件上传大小不超过5 MB，下载URL文件大小不超过25 MB。

        :param request: Request instance for CreateAudioDeposit.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateAudioDepositRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateAudioDepositResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAudioDeposit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAudioDepositResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataDeposit(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的业务数据明文，业务数据明文存证写入后不可修改，BTOE对业务数据明文存证生成含有电子签章的区块链存证电子凭证。

        :param request: Request instance for CreateDataDeposit.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateDataDepositRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateDataDepositResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataDeposit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataDepositResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDocDeposit(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的文档原文件或下载URL，BTOE对文档原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。文档类型支持格式：doc、docx、xls、xlsx、ppt、pptx、 pdf、html、txt、md、csv；原文件上传大小不超过5 MB，下载URL文件大小不超过10 MB。

        :param request: Request instance for CreateDocDeposit.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateDocDepositRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateDocDepositResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDocDeposit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDocDepositResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHashDeposit(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。

        :param request: Request instance for CreateHashDeposit.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateHashDepositRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateHashDepositResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHashDeposit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHashDepositResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHashDepositNoCert(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链，本接口不生成区块链存证电子凭证。

        :param request: Request instance for CreateHashDepositNoCert.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateHashDepositNoCertRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateHashDepositNoCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHashDepositNoCert", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHashDepositNoCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHashDepositNoSeal(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链，并生成无电子签章的区块链存证电子凭证。

        :param request: Request instance for CreateHashDepositNoSeal.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateHashDepositNoSealRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateHashDepositNoSealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHashDepositNoSeal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHashDepositNoSealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImageDeposit(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的图片原文件或下载URL，BTOE对图片原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。图片类型支持格式：png、jpg、jpeg、bmp、gif、svg；原文件上传大小不超过5 MB，下载URL文件大小不超过10 MB。

        :param request: Request instance for CreateImageDeposit.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateImageDepositRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateImageDepositResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageDeposit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageDepositResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoDeposit(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的视频的原文件或下载URL，BTOE对视频原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。视频文件支持格式：mp4、avi、mkv、mov、flv,wmv,rmvb,3gp；文件大小限制：直接上传原文件不大于5MB，下载URL文件大小不大于200 MB。

        :param request: Request instance for CreateVideoDeposit.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateVideoDepositRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateVideoDepositResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoDeposit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoDepositResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebpageDeposit(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE提交待存证网页的URL，BTOE对URL进行网页快照，并将快照图片存储，将网页快照Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。URL格式必须以http、https开头。

        :param request: Request instance for CreateWebpageDeposit.
        :type request: :class:`tencentcloud.btoe.v20210303.models.CreateWebpageDepositRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.CreateWebpageDepositResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebpageDeposit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebpageDepositResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDepositCert(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过存证编码向BTOE查询存证电子凭证信息。

        :param request: Request instance for GetDepositCert.
        :type request: :class:`tencentcloud.btoe.v20210303.models.GetDepositCertRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.GetDepositCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDepositCert", params, headers=headers)
            response = json.loads(body)
            model = models.GetDepositCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDepositFile(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过存证编码向BTOE获取存证文件的下载URL。
        -注：Hash类存证、业务数据明文存证不产生存证文件。

        :param request: Request instance for GetDepositFile.
        :type request: :class:`tencentcloud.btoe.v20210303.models.GetDepositFileRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.GetDepositFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDepositFile", params, headers=headers)
            response = json.loads(body)
            model = models.GetDepositFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDepositInfo(self, request):
        r"""功能迭代，已上线更高版本的接口2021-05-14

        用户通过存证编码向BTOE查询存证基本信息。

        :param request: Request instance for GetDepositInfo.
        :type request: :class:`tencentcloud.btoe.v20210303.models.GetDepositInfoRequest`
        :rtype: :class:`tencentcloud.btoe.v20210303.models.GetDepositInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDepositInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetDepositInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))