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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.domain.v20180808 import models


class DomainClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'domain.tencentcloudapi.com'


    def BatchModifyDomainInfo(self, request):
        """本接口 ( BatchModifyDomainInfo ) 用于批量域名信息修改 。

        :param request: Request instance for BatchModifyDomainInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.BatchModifyDomainInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.BatchModifyDomainInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchModifyDomainInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchModifyDomainInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckBatchStatus(self, request):
        """本接口 ( CheckBatchStatus ) 用于查询批量操作日志状态 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for CheckBatchStatus.
        :type request: :class:`tencentcloud.domain.v20180808.models.CheckBatchStatusRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CheckBatchStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckBatchStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckBatchStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckDomain(self, request):
        """检查域名是否可以注册。

        :param request: Request instance for CheckDomain.
        :type request: :class:`tencentcloud.domain.v20180808.models.CheckDomainRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CheckDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDomainBatch(self, request):
        """本接口 ( CreateDomainBatch ) 用于批量注册域名 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for CreateDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateDomainBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDomainBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTemplate(self, request):
        """本接口 ( CreateTemplate ) 用于添加域名信息模板 。

        :param request: Request instance for CreateTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTemplate(self, request):
        """本接口 ( DeleteTemplate ) 用于删除域名信息模板。

        :param request: Request instance for DeleteTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.DeleteTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DeleteTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBatchOperationLogDetails(self, request):
        """本接口 ( DescribeBatchOperationLogDetails ) 用于获取批量操作日志详情。

        :param request: Request instance for DescribeBatchOperationLogDetails.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogDetailsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBatchOperationLogDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBatchOperationLogDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBatchOperationLogs(self, request):
        """本接口 ( DescribeBatchOperationLogs ) 用于获取批量操作日志 。

        :param request: Request instance for DescribeBatchOperationLogs.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogsRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeBatchOperationLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBatchOperationLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBatchOperationLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDomainBaseInfo(self, request):
        """本接口 (  DescribeDomainBaseInfo) 获取域名基础信息。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for DescribeDomainBaseInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainBaseInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainBaseInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainBaseInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainBaseInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDomainNameList(self, request):
        """本接口 (  DescribeDomainNameList ) 获取域名列表。

        :param request: Request instance for DescribeDomainNameList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainNameListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainNameListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainNameList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainNameListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDomainPriceList(self, request):
        """按照域名后缀获取对应的价格列表

        :param request: Request instance for DescribeDomainPriceList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainPriceListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainPriceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainPriceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainPriceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTemplate(self, request):
        """本接口 (DescribeTemplate) 用于获取模板信息。

        :param request: Request instance for DescribeTemplate.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTemplateList(self, request):
        """本接口 (DescribeTemplateList) 用于获取模板列表。

        :param request: Request instance for DescribeTemplateList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTemplateList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTemplateListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDomainDNSBatch(self, request):
        """本接口 ( ModifyDomainDNSBatch) 用于批量修改域名DNS信息 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for ModifyDomainDNSBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyDomainDNSBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyDomainDNSBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomainDNSBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainDNSBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDomainOwnerBatch(self, request):
        """本接口 ( ModifyDomainOwnerBatch) 用于域名批量账号间转移 。

        :param request: Request instance for ModifyDomainOwnerBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.ModifyDomainOwnerBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.ModifyDomainOwnerBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomainOwnerBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainOwnerBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewDomainBatch(self, request):
        """本接口 ( RenewDomainBatch ) 用于批量续费域名 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for RenewDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.RenewDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.RenewDomainBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDomainBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDomainBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetDomainAutoRenew(self, request):
        """本接口 ( SetDomainAutoRenew ) 用于设置域名自动续费。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for SetDomainAutoRenew.
        :type request: :class:`tencentcloud.domain.v20180808.models.SetDomainAutoRenewRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.SetDomainAutoRenewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetDomainAutoRenew", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetDomainAutoRenewResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransferInDomainBatch(self, request):
        """本接口 ( TransferInDomainBatch ) 用于批量转入域名 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for TransferInDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.TransferInDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.TransferInDomainBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransferInDomainBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransferInDomainBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransferProhibitionBatch(self, request):
        """本接口 ( TransferInDomainBatch ) 用于批量禁止域名转移 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for TransferProhibitionBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.TransferProhibitionBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.TransferProhibitionBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransferProhibitionBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransferProhibitionBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateProhibitionBatch(self, request):
        """本接口 ( UpdateProhibitionBatch ) 用于批量设置禁止域名更新 。

        :param request: Request instance for UpdateProhibitionBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.UpdateProhibitionBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.UpdateProhibitionBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateProhibitionBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateProhibitionBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadImage(self, request):
        """本接口 ( UploadImage ) 用于上传资质照片 。

        :param request: Request instance for UploadImage.
        :type request: :class:`tencentcloud.domain.v20180808.models.UploadImageRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.UploadImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadImageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)