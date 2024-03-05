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
from tencentcloud.clb.v20180317 import models


class ClbClient(AbstractClient):
    _apiVersion = '2018-03-17'
    _endpoint = 'clb.tencentcloudapi.com'
    _service = 'clb'


    def AssociateTargetGroups(self, request):
        """本接口(AssociateTargetGroups)用来将目标组绑定到负载均衡的监听器（四层协议）或转发规则（七层协议）上。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for AssociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AutoRewrite(self, request):
        """用户需要先创建出一个HTTPS:443监听器，并在其下创建转发规则。通过调用本接口，系统会自动创建出一个HTTP:80监听器（如果之前不存在），并在其下创建转发规则，与HTTPS:443监听器下的Domains（在入参中指定）对应。创建成功后可以通过HTTP:80地址自动跳转为HTTPS:443地址进行访问。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for AutoRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.AutoRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AutoRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AutoRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.AutoRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeregisterTargets(self, request):
        """批量解绑四七层后端服务。批量解绑的资源数量上限为500。只支持VPC网络负载均衡。

        :param request: Request instance for BatchDeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeregisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeregisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyTargetTag(self, request):
        """BatchModifyTargetTag 接口用于批量修改负载均衡监听器绑定的后端机器的标签。批量修改的资源数量上限为500。本接口为同步接口。<br/>负载均衡的4层和7层监听器支持此接口，传统型负载均衡不支持。

        :param request: Request instance for BatchModifyTargetTag.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetTagRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyTargetTag", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyTargetTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyTargetWeight(self, request):
        """BatchModifyTargetWeight 接口用于批量修改负载均衡监听器绑定的后端机器的转发权重。批量修改的资源数量上限为500。本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。<br/>负载均衡的4层和7层监听器支持此接口，传统型负载均衡不支持。

        :param request: Request instance for BatchModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRegisterTargets(self, request):
        """批量绑定虚拟主机或弹性网卡，支持跨域绑定，支持四层、七层（TCP、UDP、HTTP、HTTPS）协议绑定。批量绑定的资源数量上限为500。只支持VPC网络负载均衡。

        :param request: Request instance for BatchRegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRegisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRegisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneLoadBalancer(self, request):
        """克隆负载均衡实例，根据指定的负载均衡实例，复制出相同规则和绑定关系的负载均衡实例。克隆接口为异步操作，克隆的数据以调用CloneLoadBalancer时为准，如果调用CloneLoadBalancer后克隆CLB发生变化，变化规则不会克隆。

        注：查询实例创建状态可以根据返回值中的requestId访问[DescribeTaskStatus](https://cloud.tencent.com/document/product/214/30683)接口

        限制说明：
        实例属性维度限制
          仅支持克隆按量计费实例，不支持包年包月实例。
          不支持克隆未关联实例计费项的 CLB。
          不支持克隆传统型负载均衡实例和高防 CLB。
          不支持克隆基础网络类型的实例。
          不支持克隆 IPv6、IPv6 NAT64 版本以及混绑的实例。
          个性化配置、重定向配置、安全组默认放通开关的配置将不会被克隆，需重新配置。
          执行克隆操作前，请确保实例上没有使用已过期证书，否则会导致克隆失败。
        监听器维度限制
          不支持克隆监听器为 QUIC 类型和端口段的实例。
          不支持监听器为 TCP_SSL 的内网型负载均衡的实例。
          不支持克隆七层监听器没有转发规则的实例。
          当实例的监听器个数超过50个时，不支持克隆。
        后端服务维度限制
          不支持克隆绑定的后端服务类型为目标组和 SCF 云函数的实例。

        通过接口调用：
        BGP带宽包必须传带宽包id
        独占集群克隆必须传对应的参数，否则按共享型创建
        功能内测中，请提交 [内测申请](https://cloud.tencent.com/apply/p/1akuvsmyn0g)。

        :param request: Request instance for CloneLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.CloneLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CloneLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CloneLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClsLogSet(self, request):
        """创建CLB专有日志集，此日志集用于存储CLB的日志。

        :param request: Request instance for CreateClsLogSet.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateClsLogSetRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateClsLogSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClsLogSet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClsLogSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateListener(self, request):
        """在一个负载均衡实例下创建监听器。
        本接口为异步接口，接口返回成功后，需以返回的 RequestId 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancer(self, request):
        """本接口(CreateLoadBalancer)用来创建负载均衡实例（本接口只支持购买按量计费的负载均衡，包年包月的负载均衡请通过控制台购买）。为了使用负载均衡服务，您必须购买一个或多个负载均衡实例。成功调用该接口后，会返回负载均衡实例的唯一 ID。负载均衡实例的类型分为：公网、内网。详情可参考产品说明中的产品类型。
        注意：(1)指定可用区申请负载均衡、跨zone容灾(仅香港支持)【如果您需要体验该功能，请通过 [工单申请](https://console.cloud.tencent.com/workorder/category)】；(2)目前只有北京、上海、广州支持IPv6；(3)一个账号在每个地域的默认购买配额为：公网100个，内网100个。
        本接口为异步接口，接口成功返回后，可使用 DescribeLoadBalancers 接口查询负载均衡实例的状态（如创建中、正常），以确定是否创建成功。

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancerSnatIps(self, request):
        """针对SnatPro负载均衡，这个接口用于添加SnatIp，如果负载均衡没有开启SnatPro，添加SnatIp后会自动开启。
        本接口为异步接口，接口返回成功后，需以得到的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for CreateLoadBalancerSnatIps.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerSnatIpsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerSnatIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancerSnatIps", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerSnatIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """CreateRule 接口用于在一个已存在的负载均衡七层监听器下创建转发规则，七层监听器中，后端服务必须绑定到规则上而非监听器上。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTargetGroup(self, request):
        """创建目标组。该功能正在内测中，如需使用，请通过[工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1)。

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        """创建主题，默认开启全文索引和键值索引。如果不存在CLB专有日志集，则创建失败。

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListener(self, request):
        """本接口用来删除负载均衡实例下的监听器（四层和七层）。
        本接口为异步接口，接口返回成功后，需以得到的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListener", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancer(self, request):
        """DeleteLoadBalancer 接口用以删除指定的一个或多个负载均衡实例。成功删除后，会把负载均衡实例下的监听器、转发规则一起删除，并把后端服务解绑。
        本接口为异步接口，接口返回成功后，需以返回的 RequestId 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancerListeners(self, request):
        """该接口支持删除负载均衡的多个监听器。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeleteLoadBalancerListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancerListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancerSnatIps(self, request):
        """这个接口用于删除SnatPro的负载均衡的SnatIp。
        本接口为异步接口，接口返回成功后，需以得到的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeleteLoadBalancerSnatIps.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerSnatIpsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerSnatIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancerSnatIps", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerSnatIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRewrite(self, request):
        """DeleteRewrite 接口支持删除指定转发规则之间的重定向关系。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for DeleteRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """DeleteRule 接口用来删除负载均衡实例七层监听器下的转发规则。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTargetGroups(self, request):
        """删除目标组

        :param request: Request instance for DeleteTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterFunctionTargets(self, request):
        """DeregisterFunctionTargets 接口用来将一个云函数从负载均衡的转发规则上解绑，对于七层监听器，还需通过 LocationId 或 Domain+Url 指定转发规则。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 [DescribeTaskStatus](https://cloud.tencent.com/document/product/214/30683) 接口查询本次任务是否成功。
        <br/>限制说明：

        - 仅广州、深圳金融、上海、上海金融、北京、成都、中国香港、新加坡、孟买、东京、硅谷地域支持绑定 SCF。
        - 仅标准账户类型支持绑定 SCF，传统账户类型不支持。建议升级为标准账户类型，详情可参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。
        - 传统型负载均衡不支持绑定 SCF。
        - 基础网络类型不支持绑定 SCF。
        - CLB 默认支持绑定同地域下的所有 SCF，可支持跨 VPC 绑定 SCF，不支持跨地域绑定。
        - 目前仅 IPv4、IPv6 NAT64 版本的负载均衡支持绑定 SCF，IPv6 版本的暂不支持。
        - 仅七层（HTTP、HTTPS）监听器支持绑定 SCF，四层（TCP、UDP、TCP SSL）监听器和七层 QUIC 监听器不支持。
        - CLB 绑定 SCF 仅支持绑定“Event 函数”类型的云函数。

        :param request: Request instance for DeregisterFunctionTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterFunctionTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterFunctionTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterFunctionTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterFunctionTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterTargetGroupInstances(self, request):
        """从目标组中解绑服务器。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeregisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterTargets(self, request):
        """DeregisterTargets 接口用来将一台或多台后端服务从负载均衡的监听器或转发规则上解绑，对于四层监听器，只需指定监听器ID即可，对于七层监听器，还需通过LocationId或Domain+Url指定转发规则。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for DeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterTargetsFromClassicalLB(self, request):
        """DeregisterTargetsFromClassicalLB 接口用于解绑负载均衡后端服务。本接口为异步接口，接口返回成功后，需以返回的 RequestId 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DeregisterTargetsFromClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterTargetsFromClassicalLB", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterTargetsFromClassicalLBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockIPList(self, request):
        """查询一个负载均衡所封禁的IP列表（黑名单）。（接口灰度中，如需使用请提工单）

        :param request: Request instance for DescribeBlockIPList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockIPList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockIPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockIPTask(self, request):
        """根据 ModifyBlockIPList 接口返回的异步任务的ID，查询封禁IP（黑名单）异步任务的执行状态。（接口灰度中，如需使用请提工单）

        :param request: Request instance for DescribeBlockIPTask.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPTaskRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockIPTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockIPTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBByInstanceId(self, request):
        """DescribeClassicalLBByInstanceId用于通过后端实例ID获取传统型负载均衡ID列表。

        :param request: Request instance for DescribeClassicalLBByInstanceId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBByInstanceId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBByInstanceIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBHealthStatus(self, request):
        """DescribeClassicalLBHealthStatus用于获取传统型负载均衡后端的健康状态

        :param request: Request instance for DescribeClassicalLBHealthStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBHealthStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBHealthStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBListeners(self, request):
        """DescribeClassicalLBListeners 接口用于获取传统型负载均衡的监听器信息。

        :param request: Request instance for DescribeClassicalLBListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBTargets(self, request):
        """DescribeClassicalLBTargets用于获取传统型负载均衡绑定的后端服务。

        :param request: Request instance for DescribeClassicalLBTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClsLogSet(self, request):
        """获取用户的CLB专有日志集。

        :param request: Request instance for DescribeClsLogSet.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClsLogSetRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClsLogSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClsLogSet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClsLogSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterResources(self, request):
        """查询独占集群中的资源列表，支持按集群ID、VIP、负载均衡ID、是否闲置为过滤条件检索。

        :param request: Request instance for DescribeClusterResources.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClusterResourcesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClusterResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossTargets(self, request):
        """查询跨域2.0版本云联网后端子机和网卡信息。

        :param request: Request instance for DescribeCrossTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeCrossTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeCrossTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomizedConfigAssociateList(self, request):
        """拉取配置绑定的 server 或 location，如果 domain 存在，结果将根据 domain 过滤。或拉取配置绑定的 loadbalancer。

        :param request: Request instance for DescribeCustomizedConfigAssociateList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigAssociateListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigAssociateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomizedConfigAssociateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomizedConfigAssociateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomizedConfigList(self, request):
        """拉取个性化配置列表，返回用户 AppId 下指定类型的配置。

        :param request: Request instance for DescribeCustomizedConfigList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomizedConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomizedConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExclusiveClusters(self, request):
        """查询集群信息列表，支持以集群类型、集群唯一ID、集群名字、集群标签、集群内vip、集群内负载均衡唯一id、集群网络类型、可用区等条件进行检索

        :param request: Request instance for DescribeExclusiveClusters.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeExclusiveClustersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeExclusiveClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExclusiveClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExclusiveClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdleLoadBalancers(self, request):
        """闲置实例是指创建超过7天后付费实例，且没有创建规则或创建规则没有绑定子机的负载均衡实例。

        :param request: Request instance for DescribeIdleLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeIdleLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeIdleLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdleLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdleLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLBListeners(self, request):
        """查询后端云主机或弹性网卡绑定的负载均衡，支持弹性网卡和cvm查询。

        :param request: Request instance for DescribeLBListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLBListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLBListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLBListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLBListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListeners(self, request):
        """DescribeListeners 接口可根据负载均衡器 ID、监听器的协议或端口作为过滤条件获取监听器列表。如果不指定任何过滤条件，则返回该负载均衡实例下的所有监听器。

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerListByCertId(self, request):
        """根据证书ID查询其在一个地域中所关联到负载均衡实例列表

        :param request: Request instance for DescribeLoadBalancerListByCertId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerListByCertId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerListByCertIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerOverview(self, request):
        """查询运行中、隔离中、即将到期和负载均衡总数。

        :param request: Request instance for DescribeLoadBalancerOverview.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerOverviewRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerTraffic(self, request):
        """查询账号下的高流量负载均衡，返回前10个负载均衡。如果是子账号登录，只返回子账号有权限的负载均衡。

        :param request: Request instance for DescribeLoadBalancerTraffic.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerTrafficRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerTrafficResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerTraffic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerTrafficResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancers(self, request):
        """查询一个地域的负载均衡实例列表。

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancersDetail(self, request):
        """查询负载均衡的详细信息，包括监听器，规则及后端目标。

        :param request: Request instance for DescribeLoadBalancersDetail.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersDetailRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancersDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancersDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuota(self, request):
        """查询用户当前地域下的各项配额

        :param request: Request instance for DescribeQuota.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeQuotaRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResources(self, request):
        """查询用户在当前地域支持可用区列表和资源列表。

        :param request: Request instance for DescribeResources.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeResourcesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRewrite(self, request):
        """DescribeRewrite 接口可根据负载均衡实例ID，查询一个负载均衡实例下转发规则的重定向关系。如果不指定监听器ID或转发规则ID，则返回该负载均衡实例下的所有重定向关系。

        :param request: Request instance for DescribeRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupInstances(self, request):
        """获取目标组绑定的服务器信息

        :param request: Request instance for DescribeTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupList(self, request):
        """获取目标组列表

        :param request: Request instance for DescribeTargetGroupList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroups(self, request):
        """查询目标组信息

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetHealth(self, request):
        """DescribeTargetHealth 接口用来获取负载均衡后端服务的健康检查结果，不支持传统型负载均衡。

        :param request: Request instance for DescribeTargetHealth.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetHealth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetHealthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargets(self, request):
        """DescribeTargets 接口用来查询负载均衡实例的某些监听器绑定的后端服务列表。

        :param request: Request instance for DescribeTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """本接口用于查询异步任务的执行状态，对于非查询类的接口（创建/删除负载均衡实例、监听器、规则以及绑定或解绑后端服务等），在接口调用成功后，都需要使用本接口查询任务最终是否执行成功。

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateTargetGroups(self, request):
        """解除规则的目标组关联关系。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for DisassociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateLoadBalancer(self, request):
        """InquiryPriceCreateLoadBalancer接口查询创建负载均衡的价格。

        :param request: Request instance for InquiryPriceCreateLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.InquiryPriceCreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.InquiryPriceCreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceModifyLoadBalancer(self, request):
        """InquiryPriceModifyLoadBalancer接口修改负载均衡配置询价。

        :param request: Request instance for InquiryPriceModifyLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.InquiryPriceModifyLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.InquiryPriceModifyLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceModifyLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceModifyLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRefundLoadBalancer(self, request):
        """InquiryPriceRefundLoadBalancer接口查询负载均衡退费价格。

        :param request: Request instance for InquiryPriceRefundLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.InquiryPriceRefundLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.InquiryPriceRefundLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRefundLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRefundLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewLoadBalancer(self, request):
        """InquiryPriceRenewLoadBalancer接口查询对负载均衡续费的价格，只支持预付费负载均衡续费。

        :param request: Request instance for InquiryPriceRenewLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.InquiryPriceRenewLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.InquiryPriceRenewLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManualRewrite(self, request):
        """用户手动配置原访问地址和重定向地址，系统自动将原访问地址的请求重定向至对应路径的目的地址。同一域名下可以配置多条路径作为重定向策略，实现http/https之间请求的自动跳转。设置重定向时，需满足如下约束条件：若A已经重定向至B，则A不能再重定向至C（除非先删除老的重定向关系，再建立新的重定向关系），B不能重定向至任何其它地址。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for ManualRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.ManualRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ManualRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManualRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.ManualRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigrateClassicalLoadBalancers(self, request):
        """本接口将传统型负载均衡迁移成(原应用型)负载均衡
        本接口为异步接口，接口成功返回后，可使用 DescribeLoadBalancers 接口查询负载均衡实例的状态（如创建中、正常），以确定是否创建成功。

        :param request: Request instance for MigrateClassicalLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.MigrateClassicalLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.MigrateClassicalLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateClassicalLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateClassicalLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockIPList(self, request):
        """修改负载均衡的IP（client IP）封禁黑名单列表，一个转发规则最多支持封禁 2000000 个IP，及黑名单容量为 2000000。
        （接口灰度中，如需使用请提工单）

        :param request: Request instance for ModifyBlockIPList.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyBlockIPListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyBlockIPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockIPList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockIPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomain(self, request):
        """ModifyDomain接口用来修改负载均衡七层监听器下的域名。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for ModifyDomain.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainAttributes(self, request):
        """ModifyDomainAttributes接口用于修改负载均衡7层监听器转发规则的域名级别属性，如修改域名、修改DefaultServer、开启/关闭Http2、修改证书。
        本接口为异步接口，本接口返回成功后，需以返回的RequestId为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for ModifyDomainAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionTargets(self, request):
        """修改负载均衡转发规则上所绑定的云函数。

        :param request: Request instance for ModifyFunctionTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyFunctionTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyFunctionTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionTargets", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyListener(self, request):
        """ModifyListener接口用来修改负载均衡监听器的属性，包括监听器名称、健康检查参数、证书信息、转发策略等。本接口不支持传统型负载均衡。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyListener", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerAttributes(self, request):
        """修改负载均衡实例的属性。支持修改负载均衡实例的名称、设置负载均衡的跨域属性。
        本接口为异步接口，接口返回成功后，需以得到的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerMixIpTarget(self, request):
        """修改IPv6FullChain负载均衡7层监听器支持混绑IPv4/IPv6目标特性。

        :param request: Request instance for ModifyLoadBalancerMixIpTarget.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerMixIpTargetRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerMixIpTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerMixIpTarget", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerMixIpTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerSla(self, request):
        """本接口（ModifyLoadBalancerSla）用于将按量计费模式的共享型实例升级为性能容量型实例。<br/>
        限制条件：
        - 本接口只支持升级按量计费的CLB实例，包年包月的CLB实例升级请通过控制台进行升级。
        - 升级为性能容量型实例后，不支持再回退到共享型实例。
        - 传统型负载均衡实例不支持升级为性能容量型实例。

        :param request: Request instance for ModifyLoadBalancerSla.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerSlaRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerSlaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerSla", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerSlaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancersProject(self, request):
        """修改一个或多个负载均衡实例所属项目。

        :param request: Request instance for ModifyLoadBalancersProject.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancersProjectRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancersProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancersProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancersProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        """ModifyRule 接口用来修改负载均衡七层监听器下的转发规则的各项属性，包括转发路径、健康检查属性、转发策略等。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupAttribute(self, request):
        """修改目标组的名称或者默认端口属性

        :param request: Request instance for ModifyTargetGroupAttribute.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupInstancesPort(self, request):
        """批量修改目标组服务器端口。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for ModifyTargetGroupInstancesPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupInstancesPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupInstancesPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupInstancesWeight(self, request):
        """批量修改目标组的服务器权重。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for ModifyTargetGroupInstancesWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupInstancesWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupInstancesWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetPort(self, request):
        """ModifyTargetPort接口用于修改监听器绑定的后端服务的端口。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for ModifyTargetPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetWeight(self, request):
        """ModifyTargetWeight 接口用于修改负载均衡绑定的后端服务的转发权重。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for ModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterFunctionTargets(self, request):
        """RegisterFunctionTargets 接口用来将一个云函数绑定到负载均衡的7层转发规则，在此之前您需要先行创建相关的7层监听器（HTTP、HTTPS）和转发规则。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。<br/>
        限制说明：
        - 仅广州、深圳金融、上海、上海金融、北京、成都、中国香港、新加坡、孟买、东京、硅谷地域支持绑定 SCF。
        - 仅标准账户类型支持绑定 SCF，传统账户类型不支持。建议升级为标准账户类型，详情可参见 [账户类型升级说明](https://cloud.tencent.com/document/product/1199/49090)。
        - 传统型负载均衡不支持绑定 SCF。
        - 基础网络类型不支持绑定 SCF。
        - CLB 默认支持绑定同地域下的所有 SCF，可支持跨 VPC 绑定 SCF，不支持跨地域绑定。
        - 目前仅 IPv4、IPv6 NAT64 版本的负载均衡支持绑定 SCF，IPv6 版本的暂不支持。
        - 仅七层（HTTP、HTTPS）监听器支持绑定 SCF，四层（TCP、UDP、TCP SSL）监听器和七层 QUIC 监听器不支持。
        - CLB 绑定 SCF 仅支持绑定“Event 函数”类型的云函数。

        :param request: Request instance for RegisterFunctionTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterFunctionTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterFunctionTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterFunctionTargets", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterFunctionTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterTargetGroupInstances(self, request):
        """注册服务器到目标组。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for RegisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterTargets(self, request):
        """RegisterTargets 接口用来将一台或多台后端服务绑定到负载均衡的监听器（或7层转发规则），在此之前您需要先行创建相关的4层监听器或7层转发规则。对于四层监听器（TCP、UDP），只需指定监听器ID即可，对于七层监听器（HTTP、HTTPS），还需通过LocationId或者Domain+Url指定转发规则。
        本接口为异步接口，本接口返回成功后需以返回的RequestID为入参，调用DescribeTaskStatus接口查询本次任务是否成功。

        :param request: Request instance for RegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterTargetsWithClassicalLB(self, request):
        """RegisterTargetsWithClassicalLB 接口用于绑定后端服务到传统型负载均衡。本接口为异步接口，接口返回成功后，需以返回的 RequestId 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。

        :param request: Request instance for RegisterTargetsWithClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterTargetsWithClassicalLB", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterTargetsWithClassicalLBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceCertForLoadBalancers(self, request):
        """ReplaceCertForLoadBalancers 接口用以替换负载均衡实例所关联的证书，对于各个地域的负载均衡，如果指定的老的证书ID与其有关联关系，则会先解除关联，再建立新证书与该负载均衡的关联关系。
        此接口支持替换服务端证书或客户端证书。
        需要使用的新证书，可以通过传入证书ID来指定，如果不指定证书ID，则必须传入证书内容等相关信息，用以新建证书并绑定至负载均衡。
        注：本接口仅可从广州地域调用。

        :param request: Request instance for ReplaceCertForLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.ReplaceCertForLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ReplaceCertForLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceCertForLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceCertForLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCustomizedConfigForLoadBalancer(self, request):
        """负载均衡维度的个性化配置相关操作：创建、删除、修改、绑定、解绑

        :param request: Request instance for SetCustomizedConfigForLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetCustomizedConfigForLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetCustomizedConfigForLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCustomizedConfigForLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.SetCustomizedConfigForLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerClsLog(self, request):
        """增加、删除、更新负载均衡的日志服务(CLS)主题。

        :param request: Request instance for SetLoadBalancerClsLog.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerClsLog", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerClsLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerSecurityGroups(self, request):
        """SetLoadBalancerSecurityGroups 接口支持对一个公网负载均衡实例执行设置（绑定、解绑）安全组操作。查询一个负载均衡实例目前已绑定的安全组，可使用 DescribeLoadBalancers 接口。本接口是set语义，
        绑定操作时，入参需要传入负载均衡实例要绑定的所有安全组（已绑定的+新增绑定的）。
        解绑操作时，入参需要传入负载均衡实例执行解绑后所绑定的所有安全组；如果要解绑所有安全组，可不传此参数，或传入空数组。注意：内网 CLB 绑定 EIP 后，CLB 上的安全组对来自 EIP 的流量不生效，对来自内网 CLB 的流量生效。

        :param request: Request instance for SetLoadBalancerSecurityGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerStartStatus(self, request):
        """启停负载均衡实例或者监听器。
        本接口为异步接口，接口返回成功后，需以得到的 RequestID 为入参，调用 DescribeTaskStatus 接口查询本次任务是否成功。
        该功能正在内测中，如需使用，请通过[工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1)。

        :param request: Request instance for SetLoadBalancerStartStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerStartStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerStartStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerStartStatus", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerStartStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetSecurityGroupForLoadbalancers(self, request):
        """绑定或解绑一个安全组到多个公网负载均衡实例。注意：内网负载均衡不支持绑定安全组。

        :param request: Request instance for SetSecurityGroupForLoadbalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetSecurityGroupForLoadbalancers", params, headers=headers)
            response = json.loads(body)
            model = models.SetSecurityGroupForLoadbalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))