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
from tencentcloud.tkgdq.v20190411 import models


class TkgdqClient(AbstractClient):
    _apiVersion = '2019-04-11'
    _endpoint = 'tkgdq.tencentcloudapi.com'
    _service = 'tkgdq'


    def DescribeEntity(self, request):
        """输入实体名称，返回实体相关的信息如实体别名、实体英文名、实体详细信息、相关实体等

        :param request: Request instance for DescribeEntity.
        :type request: :class:`tencentcloud.tkgdq.v20190411.models.DescribeEntityRequest`
        :rtype: :class:`tencentcloud.tkgdq.v20190411.models.DescribeEntityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEntity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEntityResponse()
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


    def DescribeRelation(self, request):
        """输入两个实体，返回两个实体间的关系，例如马化腾与腾讯公司不仅是相关实体，二者还存在隶属关系（马化腾属于腾讯公司）。

        :param request: Request instance for DescribeRelation.
        :type request: :class:`tencentcloud.tkgdq.v20190411.models.DescribeRelationRequest`
        :rtype: :class:`tencentcloud.tkgdq.v20190411.models.DescribeRelationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRelation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRelationResponse()
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


    def DescribeTriple(self, request):
        """三元组查询，主要分为两类，SP查询和PO查询。SP查询表示已知主语和谓语查询宾语，PO查询表示已知宾语和谓语查询主语。每一个SP或PO查询都是一个可独立执行的查询，TQL支持SP查询的嵌套查询，即主语可以是一个嵌套的子查询。其他复杂的三元组查询方法，请参考官网API文档示例。

        :param request: Request instance for DescribeTriple.
        :type request: :class:`tencentcloud.tkgdq.v20190411.models.DescribeTripleRequest`
        :rtype: :class:`tencentcloud.tkgdq.v20190411.models.DescribeTripleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTriple", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTripleResponse()
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