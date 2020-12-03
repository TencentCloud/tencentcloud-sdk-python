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
from tencentcloud.tic.v20201117 import models


class TicClient(AbstractClient):
    _apiVersion = '2020-11-17'
    _endpoint = 'tic.tencentcloudapi.com'
    _service = 'tic'


    def ApplyStack(self, request):
        """本接口（ApplyStack）用于触发资源栈下某个版本的Apply事件。

        - 当版本处于PLAN_IN_PROGRESS或APPLY_IN_PROGRESS状态时，将无法再执行本操作
        - 当版本处于APPLY_COMPLETED状态时，本操作无法执行

        :param request: Request instance for ApplyStack.
        :type request: :class:`tencentcloud.tic.v20201117.models.ApplyStackRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.ApplyStackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyStack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyStackResponse()
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


    def CreateStack(self, request):
        """本接口（CreateStack）用于通过传递一个COS的terraform zip模版URL来创建一个资源栈。创建资源栈后仍需要用户调用对应的plan, apply, destory执行对应的事件。

        :param request: Request instance for CreateStack.
        :type request: :class:`tencentcloud.tic.v20201117.models.CreateStackRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.CreateStackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStackResponse()
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


    def CreateStackVersion(self, request):
        """本接口（CreateStackVersion）用于给资源栈新增一个HCL模版版本，仅限COS链接，且为zip格式。

        :param request: Request instance for CreateStackVersion.
        :type request: :class:`tencentcloud.tic.v20201117.models.CreateStackVersionRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.CreateStackVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStackVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStackVersionResponse()
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


    def DeleteStack(self, request):
        """本接口（DeleteStack）用于删除一个资源栈（配置、版本、事件信息）。但不会销毁资源管理的云资源。如果需要销毁资源栈管理的云资源，请调用 DestoryStack 接口销毁云资源。

        :param request: Request instance for DeleteStack.
        :type request: :class:`tencentcloud.tic.v20201117.models.DeleteStackRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.DeleteStackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStackResponse()
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


    def DeleteStackVersion(self, request):
        """本接口（DeleteStackVersion）用于删除一个版本，处于PLAN_IN_PROGRESS和APPLY_IN_PROGRESS状态中的版本无法删除。

        :param request: Request instance for DeleteStackVersion.
        :type request: :class:`tencentcloud.tic.v20201117.models.DeleteStackVersionRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.DeleteStackVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStackVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStackVersionResponse()
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


    def DescribeStackEvent(self, request):
        """本接口（DescribeStackEvent）用于获取单个事件详情，尤其是可以得到事件的详细控制台输出文本。

        :param request: Request instance for DescribeStackEvent.
        :type request: :class:`tencentcloud.tic.v20201117.models.DescribeStackEventRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.DescribeStackEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStackEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStackEventResponse()
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


    def DescribeStackEvents(self, request):
        """本接口（DescribeStackEvents）用于查看一个或多个事件详细信息。

        - 可以根据事件ID过滤感兴趣的事件
        - 也可以根据版本ID，资源栈ID，事件类型，事件状态过滤事件，过滤信息详细请见过滤器Filter
        - 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的事件

        :param request: Request instance for DescribeStackEvents.
        :type request: :class:`tencentcloud.tic.v20201117.models.DescribeStackEventsRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.DescribeStackEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStackEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStackEventsResponse()
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


    def DescribeStackVersions(self, request):
        """本接口（DescribeStackVersions）用于查询一个或多个版本的详细信息。

        - 可以根据版本ID查询感兴趣的版本
        - 可以根据版本名字和状态来过滤版本，详见过滤器Filter
        - 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的版本

        :param request: Request instance for DescribeStackVersions.
        :type request: :class:`tencentcloud.tic.v20201117.models.DescribeStackVersionsRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.DescribeStackVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStackVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStackVersionsResponse()
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


    def DescribeStacks(self, request):
        """本接口（DescribeStacks）用于查询一个或多个资源栈的详细信息。

        - 可以根据资源栈ID来查询感兴趣的资源栈信息
        - 若参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的资源栈

        :param request: Request instance for DescribeStacks.
        :type request: :class:`tencentcloud.tic.v20201117.models.DescribeStacksRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.DescribeStacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStacksResponse()
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


    def DestroyStack(self, request):
        """本接口（DestroyStack）用于删除资源栈下的某个版本所创建的资源。

        :param request: Request instance for DestroyStack.
        :type request: :class:`tencentcloud.tic.v20201117.models.DestroyStackRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.DestroyStackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyStack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyStackResponse()
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


    def PlanStack(self, request):
        """本接口（PlanStack）用于触发资源栈下某个版本的PLAN事件。

        - 当版本处于PLAN_IN_PROGRESS或APPLY_IN_PROGRESS状态时，将无法再执行本操作
        - 当版本处于APPLY_COMPLETED状态时，本操作无法执行

        :param request: Request instance for PlanStack.
        :type request: :class:`tencentcloud.tic.v20201117.models.PlanStackRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.PlanStackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PlanStack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PlanStackResponse()
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


    def UpdateStack(self, request):
        """本接口（UpdateStack）用于更新资源栈的名称和描述。

        :param request: Request instance for UpdateStack.
        :type request: :class:`tencentcloud.tic.v20201117.models.UpdateStackRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.UpdateStackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateStack", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateStackResponse()
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


    def UpdateStackVersion(self, request):
        """本接口（UpdateStackVersion）用于更新一个版本的模版内容，名称或描述，模版仅限COS URL，且为zip格式。

        :param request: Request instance for UpdateStackVersion.
        :type request: :class:`tencentcloud.tic.v20201117.models.UpdateStackVersionRequest`
        :rtype: :class:`tencentcloud.tic.v20201117.models.UpdateStackVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateStackVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateStackVersionResponse()
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