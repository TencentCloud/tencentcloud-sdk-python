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
from tencentcloud.ssa.v20180608 import models


class SsaClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'ssa.tencentcloudapi.com'
    _service = 'ssa'


    def DescribeAssetDetail(self, request):
        """资产安全页资产详情

        :param request: Request instance for DescribeAssetDetail.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeAssetDetailRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeAssetDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetDetailResponse()
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


    def DescribeAssetList(self, request):
        """资产安全资产列表

        :param request: Request instance for DescribeAssetList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeAssetListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeAssetListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetListResponse()
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


    def DescribeAssetsMappingList(self, request):
        """资产测绘-测绘列表

        :param request: Request instance for DescribeAssetsMappingList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeAssetsMappingListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeAssetsMappingListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssetsMappingList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetsMappingListResponse()
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


    def DescribeCheckConfigAssetList(self, request):
        """云安全配置管理资产组列表

        :param request: Request instance for DescribeCheckConfigAssetList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeCheckConfigAssetListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeCheckConfigAssetListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCheckConfigAssetList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCheckConfigAssetListResponse()
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


    def DescribeCheckConfigDetail(self, request):
        """云安全配置检查项详情

        :param request: Request instance for DescribeCheckConfigDetail.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeCheckConfigDetailRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeCheckConfigDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCheckConfigDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCheckConfigDetailResponse()
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


    def DescribeComplianceAssetList(self, request):
        """合规管理-资产列表

        :param request: Request instance for DescribeComplianceAssetList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeComplianceAssetListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeComplianceAssetListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceAssetList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceAssetListResponse()
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


    def DescribeComplianceDetail(self, request):
        """合规管理检查项详情

        :param request: Request instance for DescribeComplianceDetail.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeComplianceDetailRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeComplianceDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceDetailResponse()
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


    def DescribeComplianceList(self, request):
        """合规管理总览页检查项列表

        :param request: Request instance for DescribeComplianceList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeComplianceListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeComplianceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComplianceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceListResponse()
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


    def DescribeConfigList(self, request):
        """云配置检查项总览页检查项列表

        :param request: Request instance for DescribeConfigList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeConfigListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeConfigListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigListResponse()
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


    def DescribeEventDetail(self, request):
        """获取安全事件详情

        :param request: Request instance for DescribeEventDetail.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeEventDetailRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeEventDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEventDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEventDetailResponse()
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


    def DescribeLeakDetectionList(self, request):
        """获取泄露列表

        :param request: Request instance for DescribeLeakDetectionList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeLeakDetectionListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeLeakDetectionListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLeakDetectionList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLeakDetectionListResponse()
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


    def DescribeSafetyEventList(self, request):
        """获取安全事件列表

        :param request: Request instance for DescribeSafetyEventList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeSafetyEventListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeSafetyEventListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSafetyEventList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSafetyEventListResponse()
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


    def DescribeSocCspmCompliance(self, request):
        """合规详情项

        :param request: Request instance for DescribeSocCspmCompliance.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCspmComplianceRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeSocCspmComplianceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSocCspmCompliance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSocCspmComplianceResponse()
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


    def DescribeVulDetail(self, request):
        """漏洞列表页，获取漏洞详情信息

        :param request: Request instance for DescribeVulDetail.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeVulDetailRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeVulDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVulDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDetailResponse()
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


    def DescribeVulList(self, request):
        """漏洞管理页，获取漏洞列表

        :param request: Request instance for DescribeVulList.
        :type request: :class:`tencentcloud.ssa.v20180608.models.DescribeVulListRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.DescribeVulListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVulList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulListResponse()
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


    def SaDivulgeDataQueryPub(self, request):
        """查询【通用字段】【泄露监测数据列表】

        :param request: Request instance for SaDivulgeDataQueryPub.
        :type request: :class:`tencentcloud.ssa.v20180608.models.SaDivulgeDataQueryPubRequest`
        :rtype: :class:`tencentcloud.ssa.v20180608.models.SaDivulgeDataQueryPubResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SaDivulgeDataQueryPub", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SaDivulgeDataQueryPubResponse()
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