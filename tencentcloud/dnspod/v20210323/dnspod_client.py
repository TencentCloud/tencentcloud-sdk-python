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
from tencentcloud.dnspod.v20210323 import models


class DnspodClient(AbstractClient):
    _apiVersion = '2021-03-23'
    _endpoint = 'dnspod.tencentcloudapi.com'
    _service = 'dnspod'


    def CreateDomain(self, request):
        """添加域名

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainResponse()
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


    def CreateDomainAlias(self, request):
        """创建域名别名

        :param request: Request instance for CreateDomainAlias.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainAliasRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainAlias", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainAliasResponse()
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
        """批量添加域名

        :param request: Request instance for CreateDomainBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainBatch", params, headers=headers)
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


    def CreateDomainGroup(self, request):
        """创建域名分组

        :param request: Request instance for CreateDomainGroup.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainGroupRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateDomainGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomainGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainGroupResponse()
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


    def CreateRecord(self, request):
        """添加记录

        :param request: Request instance for CreateRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRecordResponse()
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


    def CreateRecordBatch(self, request):
        """批量添加记录

        :param request: Request instance for CreateRecordBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.CreateRecordBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordBatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRecordBatchResponse()
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


    def DeleteDomain(self, request):
        """删除域名

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDomainResponse()
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


    def DeleteDomainAlias(self, request):
        """删除域名别名

        :param request: Request instance for DeleteDomainAlias.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainAliasRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteDomainAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomainAlias", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDomainAliasResponse()
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


    def DeleteRecord(self, request):
        """删除记录

        :param request: Request instance for DeleteRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRecordResponse()
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


    def DeleteShareDomain(self, request):
        """删除域名共享

        :param request: Request instance for DeleteShareDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DeleteShareDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DeleteShareDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShareDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteShareDomainResponse()
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


    def DescribeBatchTask(self, request):
        """获取任务详情

        :param request: Request instance for DescribeBatchTask.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeBatchTaskRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeBatchTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBatchTaskResponse()
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


    def DescribeDomain(self, request):
        """获取域名信息

        :param request: Request instance for DescribeDomain.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainResponse()
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


    def DescribeDomainAliasList(self, request):
        """获取域名别名列表

        :param request: Request instance for DescribeDomainAliasList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAliasListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainAliasListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainAliasList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainAliasListResponse()
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


    def DescribeDomainList(self, request):
        """获取域名列表

        :param request: Request instance for DescribeDomainList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainListResponse()
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


    def DescribeDomainLogList(self, request):
        """获取域名日志

        :param request: Request instance for DescribeDomainLogList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainLogListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainLogList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainLogListResponse()
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


    def DescribeDomainPurview(self, request):
        """获取域名权限

        :param request: Request instance for DescribeDomainPurview.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPurviewRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainPurviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainPurview", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainPurviewResponse()
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


    def DescribeDomainShareInfo(self, request):
        """获取域名共享信息

        :param request: Request instance for DescribeDomainShareInfo.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainShareInfoRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeDomainShareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainShareInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainShareInfoResponse()
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


    def DescribeRecord(self, request):
        """获取记录信息

        :param request: Request instance for DescribeRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordResponse()
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


    def DescribeRecordLineList(self, request):
        """获取等级允许的线路

        :param request: Request instance for DescribeRecordLineList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordLineListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordLineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordLineList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordLineListResponse()
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


    def DescribeRecordList(self, request):
        """获取某个域名下的解析记录

        :param request: Request instance for DescribeRecordList.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordListRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordListResponse()
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


    def DescribeRecordType(self, request):
        """获取等级允许的记录类型

        :param request: Request instance for DescribeRecordType.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordTypeRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeRecordTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordType", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordTypeResponse()
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


    def DescribeUserDetail(self, request):
        """获取帐户信息

        :param request: Request instance for DescribeUserDetail.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.DescribeUserDetailRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.DescribeUserDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserDetailResponse()
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


    def ModifyDomainLock(self, request):
        """锁定域名

        :param request: Request instance for ModifyDomainLock.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainLockRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainLockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainLock", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainLockResponse()
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


    def ModifyDomainOwner(self, request):
        """域名过户

        :param request: Request instance for ModifyDomainOwner.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainOwnerRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainOwner", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainOwnerResponse()
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


    def ModifyDomainRemark(self, request):
        """设置域名备注

        :param request: Request instance for ModifyDomainRemark.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainRemarkRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainRemark", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainRemarkResponse()
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


    def ModifyDomainStatus(self, request):
        """修改域名状态

        :param request: Request instance for ModifyDomainStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainStatusResponse()
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


    def ModifyDomainUnlock(self, request):
        """域名锁定解锁

        :param request: Request instance for ModifyDomainUnlock.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainUnlockRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDomainUnlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainUnlock", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainUnlockResponse()
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


    def ModifyDynamicDNS(self, request):
        """更新动态 DNS 记录

        :param request: Request instance for ModifyDynamicDNS.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyDynamicDNSRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyDynamicDNSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDynamicDNS", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDynamicDNSResponse()
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


    def ModifyRecord(self, request):
        """修改记录

        :param request: Request instance for ModifyRecord.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRecordResponse()
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


    def ModifyRecordBatch(self, request):
        """批量修改记录

        :param request: Request instance for ModifyRecordBatch.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordBatchRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordBatch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRecordBatchResponse()
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


    def ModifyRecordRemark(self, request):
        """设置记录备注

        :param request: Request instance for ModifyRecordRemark.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRemarkRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordRemark", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRecordRemarkResponse()
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


    def ModifyRecordStatus(self, request):
        """修改解析记录的状态

        :param request: Request instance for ModifyRecordStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifyRecordStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRecordStatusResponse()
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


    def ModifySubdomainStatus(self, request):
        """暂停子域名的解析记录

        :param request: Request instance for ModifySubdomainStatus.
        :type request: :class:`tencentcloud.dnspod.v20210323.models.ModifySubdomainStatusRequest`
        :rtype: :class:`tencentcloud.dnspod.v20210323.models.ModifySubdomainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubdomainStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubdomainStatusResponse()
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