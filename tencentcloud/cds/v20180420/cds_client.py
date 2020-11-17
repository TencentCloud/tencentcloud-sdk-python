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
from tencentcloud.cds.v20180420 import models


class CdsClient(AbstractClient):
    _apiVersion = '2018-04-20'
    _endpoint = 'cds.tencentcloudapi.com'
    _service = 'cds'


    def DescribeDasbImageIds(self, request):
        """获取镜像列表

        :param request: Request instance for DescribeDasbImageIds.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeDasbImageIdsRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeDasbImageIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDasbImageIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDasbImageIdsResponse()
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


    def DescribeDbauditInstanceType(self, request):
        """本接口 (DescribeDbauditInstanceType) 用于查询可售卖的产品规格列表。

        :param request: Request instance for DescribeDbauditInstanceType.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstanceTypeRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstanceTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDbauditInstanceType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDbauditInstanceTypeResponse()
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


    def DescribeDbauditInstances(self, request):
        """本接口 (DescribeDbauditInstances) 用于查询数据安全审计实例列表

        :param request: Request instance for DescribeDbauditInstances.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstancesRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDbauditInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDbauditInstancesResponse()
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


    def DescribeDbauditUsedRegions(self, request):
        """本接口 (DescribeDbauditUsedRegions) 用于查询可售卖地域列表。

        :param request: Request instance for DescribeDbauditUsedRegions.
        :type request: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditUsedRegionsRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.DescribeDbauditUsedRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDbauditUsedRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDbauditUsedRegionsResponse()
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


    def InquiryPriceDbauditInstance(self, request):
        """用于查询数据安全审计产品实例价格

        :param request: Request instance for InquiryPriceDbauditInstance.
        :type request: :class:`tencentcloud.cds.v20180420.models.InquiryPriceDbauditInstanceRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.InquiryPriceDbauditInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceDbauditInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceDbauditInstanceResponse()
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


    def ModifyDbauditInstancesRenewFlag(self, request):
        """本接口 (ModifyDbauditInstancesRenewFlag) 用于修改数据安全审计产品实例续费标识

        :param request: Request instance for ModifyDbauditInstancesRenewFlag.
        :type request: :class:`tencentcloud.cds.v20180420.models.ModifyDbauditInstancesRenewFlagRequest`
        :rtype: :class:`tencentcloud.cds.v20180420.models.ModifyDbauditInstancesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDbauditInstancesRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDbauditInstancesRenewFlagResponse()
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