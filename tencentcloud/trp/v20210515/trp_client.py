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
from tencentcloud.trp.v20210515 import models


class TrpClient(AbstractClient):
    _apiVersion = '2021-05-15'
    _endpoint = 'trp.tencentcloudapi.com'
    _service = 'trp'


    def CreateCodeBatch(self, request):
        """新增批次

        :param request: Request instance for CreateCodeBatch.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateCodeBatchRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateCodeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodeBatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCodeBatchResponse()
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


    def CreateCodePack(self, request):
        """生成码包

        :param request: Request instance for CreateCodePack.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateCodePackRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateCodePackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCodePack", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCodePackResponse()
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


    def CreateMerchant(self, request):
        """新建商户

        :param request: Request instance for CreateMerchant.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateMerchantRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMerchant", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMerchantResponse()
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


    def CreateProduct(self, request):
        """新建商品

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProduct", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProductResponse()
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


    def CreateTraceChain(self, request):
        """上链溯源信息

        :param request: Request instance for CreateTraceChain.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateTraceChainRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateTraceChainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceChain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTraceChainResponse()
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


    def CreateTraceCodes(self, request):
        """批量导入二维码，只支持平台发的码

        :param request: Request instance for CreateTraceCodes.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateTraceCodesRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateTraceCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceCodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTraceCodesResponse()
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


    def CreateTraceData(self, request):
        """新增溯源信息

        :param request: Request instance for CreateTraceData.
        :type request: :class:`tencentcloud.trp.v20210515.models.CreateTraceDataRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.CreateTraceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTraceData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTraceDataResponse()
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


    def DeleteCodeBatch(self, request):
        """删除批次

        :param request: Request instance for DeleteCodeBatch.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteCodeBatchRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteCodeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCodeBatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCodeBatchResponse()
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


    def DeleteMerchant(self, request):
        """删除商户

        :param request: Request instance for DeleteMerchant.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteMerchantRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMerchant", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMerchantResponse()
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


    def DeleteProduct(self, request):
        """删除商品，如果商品被使用，则不可删除

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProduct", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProductResponse()
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


    def DeleteTraceData(self, request):
        """删除溯源信息，如果已经上链则不可删除

        :param request: Request instance for DeleteTraceData.
        :type request: :class:`tencentcloud.trp.v20210515.models.DeleteTraceDataRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DeleteTraceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTraceData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTraceDataResponse()
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


    def DescribeCodeBatchById(self, request):
        """查询批次信息

        :param request: Request instance for DescribeCodeBatchById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeBatchById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCodeBatchByIdResponse()
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


    def DescribeCodeBatchs(self, request):
        """查询批次列表

        :param request: Request instance for DescribeCodeBatchs.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodeBatchsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodeBatchs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCodeBatchsResponse()
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


    def DescribeCodePacks(self, request):
        """查询码包列表

        :param request: Request instance for DescribeCodePacks.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodePacksRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodePacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodePacks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCodePacksResponse()
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


    def DescribeCodesByPack(self, request):
        """查询码包的二维码列表，上限 3 万

        :param request: Request instance for DescribeCodesByPack.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeCodesByPackRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeCodesByPackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCodesByPack", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCodesByPackResponse()
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


    def DescribeMerchantById(self, request):
        """查询商户信息

        :param request: Request instance for DescribeMerchantById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMerchantById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMerchantByIdResponse()
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


    def DescribeMerchants(self, request):
        """查询商户列表

        :param request: Request instance for DescribeMerchants.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeMerchantsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMerchants", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMerchantsResponse()
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


    def DescribeProductById(self, request):
        """查询商品信息

        :param request: Request instance for DescribeProductById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeProductByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeProductByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductByIdResponse()
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


    def DescribeProducts(self, request):
        """查询商品列表

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProducts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductsResponse()
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


    def DescribeTraceCodeById(self, request):
        """查询二维码信息

        :param request: Request instance for DescribeTraceCodeById.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodeByIdRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodeByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceCodeById", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTraceCodeByIdResponse()
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


    def DescribeTraceCodes(self, request):
        """查询二维码列表

        :param request: Request instance for DescribeTraceCodes.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodesRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTraceCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceCodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTraceCodesResponse()
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


    def DescribeTraceDataList(self, request):
        """查询溯源信息，通常溯源信息跟生产批次绑定，即一个批次的所有溯源信息都是一样的

        :param request: Request instance for DescribeTraceDataList.
        :type request: :class:`tencentcloud.trp.v20210515.models.DescribeTraceDataListRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.DescribeTraceDataListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTraceDataList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTraceDataListResponse()
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


    def ModifyCodeBatch(self, request):
        """修改批次

        :param request: Request instance for ModifyCodeBatch.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyCodeBatchRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyCodeBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCodeBatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCodeBatchResponse()
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


    def ModifyMerchant(self, request):
        """编辑商户

        :param request: Request instance for ModifyMerchant.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyMerchantRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyMerchantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMerchant", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMerchantResponse()
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


    def ModifyProduct(self, request):
        """编辑商品

        :param request: Request instance for ModifyProduct.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyProductRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProduct", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProductResponse()
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


    def ModifyTraceCode(self, request):
        """冻结或者激活二维码，所属的批次的冻结状态优先级大于单个二维码的状态，即如果批次是冻结的，那么该批次下二维码的状态都是冻结的

        :param request: Request instance for ModifyTraceCode.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyTraceCodeRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyTraceCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTraceCode", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTraceCodeResponse()
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


    def ModifyTraceData(self, request):
        """修改溯源信息

        :param request: Request instance for ModifyTraceData.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTraceData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTraceDataResponse()
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


    def ModifyTraceDataRanks(self, request):
        """修改溯源信息的排序

        :param request: Request instance for ModifyTraceDataRanks.
        :type request: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataRanksRequest`
        :rtype: :class:`tencentcloud.trp.v20210515.models.ModifyTraceDataRanksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTraceDataRanks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTraceDataRanksResponse()
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